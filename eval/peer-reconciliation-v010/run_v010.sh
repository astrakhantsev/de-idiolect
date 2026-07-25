#!/usr/bin/env bash
# run_v010.sh — the ONE sealed key-3 v0.10 run driver. DO NOT run during the build (LLM calls +
# reads the sealed key at scoring). Sequence: projector -> freeze/build-H -> probe -> setup ->
# confirmatory draws -> attest-1 -> generation -> output-manifest -> (attest-2 + scoring, with
# the ONE bounded relaunch). RESUME-SAFE: each post-H phase writes an H-bound receipt and is
# SKIPPED on restart; completed confirmatory keys/draws are never regenerated.
#
# Terminal routing (§4.3/§4.4): projector/probe/attest-1 failures -> state:abort-before-gen
# (unspent, unforfeited pre-generation abort); setup exhaustion -> state:setup-exhaustion;
# a confirmatory draw failing the gate -> state:confirmatory-phase-fail (config retired);
# ANY fault after key-3 generation begins -> state:terminated-during-gen-or-attest2-mismatch
# (forfeited-unspent); a scoring fault AFTER the claim -> spend:fault-after-authorized-read (spent).
#
# PRECONDITIONS (operator, at freeze): corpora/a|b/01..11.md (+manifests), leakcheck_peer.sh,
# key/{concepts,answer_key}.json (SEALED), freeze-manifest.txt, recorded-cli.json, PREREG.md,
# REQUIRED-INVENTORY.txt. pairs.json is produced by the isolated projector below.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"
RECORDED="${RECORDED_MANIFEST:-$BASE/freeze-manifest.txt}"
RECORDED_CLI="${RECORDED_CLI:-$BASE/recorded-cli.json}"
SPENDLOG="$BASE/runs/spend-log.jsonl"
TERMINAL_SENTINEL="$BASE/runs/.terminal-logged"
mkdir -p runs

log_state() {  # append a terminal/documentation marker + set the intra-process dedup sentinel
  python3 attest.py spend-log --event "$1" --out "$SPENDLOG" 2>/dev/null || true
  : > "$TERMINAL_SENTINEL"
}
GEN_STARTED=0
on_exit() {  # ANY nonzero exit AFTER key-3 generation begins (without a more specific terminal
             # already logged) routes to forfeited-unspent (§4.3).
  local rc=$?
  [ "$rc" -eq 0 ] && return
  if [ "$GEN_STARTED" = 1 ] && [ ! -f "$TERMINAL_SENTINEL" ]; then
    python3 attest.py spend-log --event state:terminated-during-gen-or-attest2-mismatch --out "$SPENDLOG" 2>/dev/null || true
    echo "generation-phase fault -> forfeited-unspent (§4.3)"
  fi
}
trap on_exit EXIT

calls() {  # run a staged tsv via the isolation wrapper; halt on run-scoped fault (rc>=2)
  local rc=0; bash "$BASE/run_calls.sh" "$1" || rc=$?
  if [ "$rc" -ge 2 ]; then echo "HALT: run-scoped fault in $1 (rc=$rc)"; exit "$rc"; fi
  [ "$rc" -eq 0 ] || echo "NOTE: failures in $1 routed per the frozen failure taxonomy"
}
phase_done() { echo "{\"phase\":\"$1\",\"H\":\"$H\"}" > "runs/phase-$1.done"; }
phase_complete() { [ -f "runs/phase-$1.done" ] && grep -q "\"H\":\"$H\"" "runs/phase-$1.done"; }

gen_loop() {  # H1/H2 budget-2 loop: stage -> run -> gate -> re-stage regens ... to quiescence
  local promptcmd="$1" gatecmd="$2" calltsv="$3" regentsv="$4"
  python3 smoke_v010.py "$promptcmd"; calls "runs/$calltsv"; python3 smoke_v010.py "$gatecmd"
  for _ in 1 2; do
    [ -s "runs/$regentsv" ] || break
    calls "runs/$regentsv"; python3 smoke_v010.py "$gatecmd"
  done
}

echo "== phase 0: offline tests + gate fidelity + conformance (NO model calls) =="
python3 scripts/verify_gate_fidelity.py
python3 conformance_runner.py
python3 tests/test_v010.py

echo "== phase 0.5: PROJECTOR — isolated blind pairs.json from the sealed key (custody) =="
# RESUME: skip if it already completed (pairs.json + its one-shot structure:read logged).
if [ -s pairs.json ] && python3 -c "import sys;sys.path.insert(0,'.');import spend;sys.exit(0 if spend.projector_completed('$SPENDLOG') else 1)"; then
  echo "  projector already completed — resume skip"
else
  PAIRS_HASH_LINE="$(python3 make_pairs_manifest.py key pairs.json --recorded-hashes "$RECORDED" --spend-log "$SPENDLOG")" \
    || { log_state state:abort-before-gen; echo "PROJECTOR failed (hash-gate) -> abort-before-gen (§4.3)"; exit 1; }
  echo "$(date -Iseconds) projector $PAIRS_HASH_LINE" >> runs/custody-log.txt
  echo "  $PAIRS_HASH_LINE (custody-logged)"
fi

echo "== phase 1: FREEZE + build-H --runtime (exact inventories; binds PREREG.md + recorded-cli.json) =="
python3 attest.py build-H --recorded-manifest "$RECORDED" --out runs/H.json --runtime
H="$(python3 -c 'import json;print(json.load(open("runs/H.json"))["H"])')"

echo "== phase 2: explicit-ID model probe (2 calls; membership) =="
if phase_complete probe; then echo "  probe already complete (H-bound) — skip"; else
  bash probe_explicit_id.sh || { log_state state:abort-before-gen; echo "PROBE failed -> abort-before-gen (§4.3)"; exit 1; }
  phase_done probe
fi

echo "== phase 3: confirmatory setup (per-key idempotent; completed keys are skipped, never regenerated) =="
python3 setup_confirmatory.py --H-value "$H" \
  || { log_state state:setup-exhaustion; echo "SETUP EXHAUSTION -> phase fails, config NOT retired (§4.1a)"; exit 2; }

echo "== phase 4: confirmatory draws — tool-path per conf key under H; gate <=1/40 =="
for ck in conf-key-1 conf-key-2; do
  if phase_complete "draw-$ck"; then echo "  draw $ck already complete (H-bound) — skip (no new draw)"; continue; fi
  bash run_confirmatory.sh runs/confirmatory/$ck "$H" \
    || { log_state state:confirmatory-phase-fail; echo "CONFIRMATORY $ck FAILED -> configuration RETIRED (§4.1)"; exit 3; }
  phase_done "draw-$ck"
done

echo "== phase 5: ATTESTATION POINT 1 (pre-generation) =="
if phase_complete attest1; then echo "  attest-1 already complete (H-bound) — skip"; else
  python3 attest.py attest --H runs/H.json --point 1 --recorded-cli "$RECORDED_CLI" --probe-log runs/probe-log.json \
    || { log_state state:abort-before-gen; echo "ATTEST-1 FAILED -> abort-before-gen, unspent+unforfeited (§4.3)"; exit 1; }
  python3 attest.py receipt --H runs/H.json --kind pre-generation --out runs/receipts.jsonl
  phase_done attest1
fi

echo "== phase 6: key-3 tool-arm generation (sealed-answer-material-blind) =="
GEN_STARTED=1   # from here, any uncaught nonzero exit routes to forfeited-unspent (EXIT trap)
if phase_complete generation; then echo "  generation already complete (H-bound) — skip"; else
  python3 smoke_v010.py excerpts
  gen_loop prompts-checklist gate-checklists checklists/calls.tsv checklists/regen-calls.tsv
  gen_loop prompts-def gate-ladders definitions/calls.tsv definitions/regen-calls.tsv
  # finding 6: DRAIN ladder mech/leak regens to quiescence BEFORE staging each conformance batch;
  # after gate_conformance stages semantic ladder regens, the loop top drains them before the next.
  while true; do
    while [ -s runs/definitions/regen-calls.tsv ]; do calls runs/definitions/regen-calls.tsv; python3 smoke_v010.py gate-ladders; done
    python3 smoke_v010.py prompts-conformance
    [ -s runs/conformance/calls.tsv ] || break
    calls runs/conformance/calls.tsv
    python3 smoke_v010.py gate-conformance
    while [ -s runs/conformance/rerun-calls.tsv ]; do calls runs/conformance/rerun-calls.tsv; python3 smoke_v010.py gate-conformance; done
  done
  python3 smoke_v010.py assert-resolved
  python3 smoke_v010.py prompts-polarity; calls runs/polarity/calls.tsv; python3 smoke_v010.py gate-polarity
  while [ -s runs/polarity/rerun-calls.tsv ]; do calls runs/polarity/rerun-calls.tsv; python3 smoke_v010.py gate-polarity; done
  python3 smoke_v010.py alive
  "$VENVPY" retrieve_xc_v010.py --v010 --no-determinism > runs/v010/retrieval-summary.txt 2>&1 \
    || { echo "RETRIEVAL FAILED"; tail -5 runs/v010/retrieval-summary.txt; exit 1; }
  python3 v010.py stage-verify; calls runs/v010/verify/calls.tsv
  python3 v010.py aggregate
  python3 v010.py stage-adaptive-1; calls runs/v010/symcheck/calls.tsv; calls runs/v010/decompose/calls.tsv
  python3 v010.py stage-adaptive-2; calls runs/v010/containment/calls.tsv
  python3 v010.py compose            # ANSWER-BLIND composed per-pair verdicts -> runs/v010/verdicts.json
  phase_done generation
fi

echo "== phase 7: baselines (answer-blind generation + gate) =="
if phase_complete baselines; then echo "  baselines already complete (H-bound) — skip"; else
  "$VENVPY" baseline_a.py retrieve
  python3 baseline_a.py prompts; calls runs/baseline_a/calls.tsv; python3 baseline_a.py gate
  while [ -s runs/baseline_a/reask-calls.tsv ]; do calls runs/baseline_a/reask-calls.tsv; python3 baseline_a.py gate; done
  python3 baseline_b.py prompts; calls runs/baseline_b/calls.tsv; python3 baseline_b.py gate
  while [ -s runs/baseline_b/reask-calls.tsv ]; do calls runs/baseline_b/reask-calls.tsv; python3 baseline_b.py gate; done
  phase_done baselines
fi

echo "== phase 8a: build the step-7 OUTPUT MANIFEST (finding 3; binds every scorer input) =="
python3 attest.py build-output-manifest --H runs/H.json --out runs/output-manifest.json

echo "== phase 9: scoring — fresh attest-2 + atomic-claim spend, with the ONE bounded relaunch =="
# Each attempt runs attestation-point-2 FRESH (finding 1), then appends a bounded
# state:scoring-attempt (max 2) with an EXPLICIT `|| exit` (a refused marker NEVER reaches the
# scorer — no set -e suppression), then the scorer (which claims under the lock immediately
# before the first key byte + verifies its inputs against the output-manifest pre-claim).
run_attempt() {
  python3 attest.py attest --H runs/H.json --point 2 --recorded-cli "$RECORDED_CLI" \
      --probe-log runs/probe-log.json --output-manifest runs/output-manifest.json \
    || { log_state state:terminated-during-gen-or-attest2-mismatch; echo "ATTEST-2 mismatch -> forfeited-unspent (§4.3)"; exit 1; }
  python3 attest.py receipt --H runs/H.json --kind attest2 --out runs/receipts.jsonl
  python3 attest.py spend-log --event state:scoring-attempt --out "$SPENDLOG" \
    || { echo "scoring-attempt REFUSED (cap reached or terminal state) — NOT launching the scorer"; exit 1; }
  python3 scorer_v010.py --key-dir key --recorded-hashes "$RECORDED" --pairs pairs.json \
    --H runs/H.json --spend-log "$SPENDLOG" --output-manifest runs/output-manifest.json \
    --tool-verdicts runs/v010/verdicts.json --baseline-a runs/baseline_a/records.json \
    --baseline-b runs/baseline_b/records.json --out runs/scores.json
}
classify_failure() {  # $1 = first|final — classify a failed attempt via the LOCKED log
  if grep -q '"event": "spend:authorized-read-claimed"' "$SPENDLOG"; then
    log_state spend:fault-after-authorized-read
    echo "FAULT AFTER CLAIM — the sealed key is SPENT and the run is INVALID; NO relaunch (§4.4)"; exit 1
  fi
  [ "$1" = "final" ] || return 0
  log_state state:terminated-during-gen-or-attest2-mismatch
  echo "pre-read failure after the one relaunch — forfeited-unspent (§4.4)"; exit 1
}
if run_attempt; then echo "KEY3-V010-DONE"; exit 0; fi
classify_failure first
echo "pre-read failure before any claim — the ONE permitted relaunch (re-attesting point 2 first)"
if run_attempt; then echo "KEY3-V010-DONE"; exit 0; fi
classify_failure final
