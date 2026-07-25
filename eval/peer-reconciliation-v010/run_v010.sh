#!/usr/bin/env bash
# run_v010.sh — the ONE sealed key-3 v0.10 run driver. DO NOT run during the build (LLM calls +
# reads the sealed key at scoring). Sequence: projector -> freeze/build-H -> structure:read
# custody -> probe -> setup -> confirmatory draws -> attest-1 -> generation -> output-manifest
# -> (attest-2 + scoring, with the ONE bounded relaunch).
#
# RESUME MODEL (round-8 findings 2/3): every post-H phase writes a TYPED, H-bound receipt whose
# required outputs are re-hashed before the phase is skipped (a stale/damaged receipt HALTS; a
# missing receipt re-runs the phase). A pure INFRASTRUCTURE fault is RESUMABLE (§10-F2): the
# driver simply exits nonzero and a re-run resumes via the receipts — it is NOT a terminal and
# NEVER forfeits. There is NO EXIT-trap auto-forfeit. Only two events actually consume key-3, and
# each is logged EXPLICITLY at its decision point + mirrored into the durable custody ledger:
#   * attestation-2 integrity mismatch -> state:terminated-during-gen-or-attest2-mismatch +
#     custody forfeited-unspent (the post-generation state no longer matches the attested H);
#   * a scorer fault AFTER the atomic claim -> spend:fault-after-authorized-read (SPENT; the
#     scorer already recorded custody=spent at the claim).
# Eligible-outcome states are documentation ONLY and never block a later SAME-H resume:
#   projector/probe/attest-1 pre-gen failure -> resumable (no terminal logged); setup exhaustion
#   -> state:setup-exhaustion (config still eligible, §4.1a); a confirmatory draw failing the gate
#   -> state:confirmatory-phase-fail (this configuration/H RETIRED, but the key stays eligible for
#   a differently-H'd revision — the custody ledger is untouched).
#
# The SPEND LOG is per-H namespaced (spend.py); every spend-log/custody call carries --H "$H".
#
# PRECONDITIONS (operator, at freeze): corpora/a|b/01..11.md (+manifests), leakcheck_peer.sh,
# key/{concepts,answer_key}.json (SEALED), freeze-manifest.txt, recorded-cli.json, PREREG.md,
# REQUIRED-INVENTORY.txt. pairs.json is produced by the isolated projector below (phase 0.5).
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"
RECORDED="${RECORDED_MANIFEST:-$BASE/freeze-manifest.txt}"
RECORDED_CLI="${RECORDED_CLI:-$BASE/recorded-cli.json}"
SPENDLOG="$BASE/runs/spend-log.jsonl"
KEYCUSTODY="$BASE/key-custody.jsonl"   # durable cross-run key-3 custody ledger (gitignored)
mkdir -p runs

# Per-H terminal/state documentation marker (called only AFTER H is built). Round-9 finding 2:
# a FAILURE to persist a state/custody transition is a HARD HALT — never suppressed.
log_state() { python3 attest.py spend-log --event "$1" --H "$H" --out "$SPENDLOG" \
  || { echo "FATAL: could not persist state marker '$1' — halting (do NOT proceed unclassified)"; exit 99; }; }
# Durable cross-run forfeit (attest-2 mismatch): the key can never be scored under any H after this.
forfeit_custody() { python3 attest.py custody-log --state forfeited-unspent --H "$H" --event-ref "$1" --out "$KEYCUSTODY" \
  || { echo "FATAL: could not persist custody forfeit ('$1') — halting"; exit 99; }; }

calls() {  # run a staged tsv via the isolation wrapper; halt on run-scoped fault (rc>=2)
  local rc=0; bash "$BASE/run_calls.sh" "$1" || rc=$?
  if [ "$rc" -ge 2 ]; then echo "HALT: run-scoped fault in $1 (rc=$rc)"; exit "$rc"; fi
  [ "$rc" -eq 0 ] || echo "NOTE: failures in $1 routed per the frozen failure taxonomy"
}

# TYPED phase receipts (finding 3). phase_check: 0 = complete (skip), 2 = no receipt (run the
# phase); a stale/damaged receipt (required output missing/drift, H drift) HALTS the run.
phase_check() {  # phase_check <name> [k=v ...]
  local name="$1"; shift
  local a=(); local kv; for kv in "$@"; do a+=(--assert "$kv"); done
  local rc=0
  python3 attest.py phase-verify --phase "$name" --H "$H" --receipt "runs/phase-$name.done" "${a[@]+"${a[@]}"}" || rc=$?
  [ "$rc" -eq 1 ] && { echo "HALT: phase '$name' receipt stale/damaged — refusing to skip"; exit 1; }
  return "$rc"
}
phase_receipt() {  # phase_receipt <name> <require-csv> [k=v ...]
  local name="$1" require="$2"; shift 2
  local a=(); local kv; for kv in "$@"; do a+=(--assert "$kv"); done
  python3 attest.py phase-receipt --phase "$name" --H "$H" --require "$require" "${a[@]+"${a[@]}"}" --out "runs/phase-$name.done"
}

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
# RESUME: skip re-projection if pairs.json already exists (deterministic given the key). The
# projector emits a receipt bound to the pairs.json hash (round-9 finding 7); the driver verifies
# it at phase 1.5 before registering the per-H structure:read on the projector's behalf.
if [ -s pairs.json ] && [ -s runs/pairs-receipt.json ]; then
  echo "  pairs.json + receipt already present — resume skip (re-projection)"
else
  PAIRS_HASH_LINE="$(python3 make_pairs_manifest.py key pairs.json --recorded-hashes "$RECORDED" --emit-receipt runs/pairs-receipt.json)" \
    || { echo "PROJECTOR failed (hash-gate) — nothing read/spent; resumable (fix inputs + re-run)"; exit 1; }
  echo "  $PAIRS_HASH_LINE"
fi

echo "== phase 1: FREEZE + H (IMMUTABLE on restart; never rebuilt) =="
# Round-9 finding 1: the frozen H is IMMUTABLE. If runs/H.json exists we LOAD + self-verify it
# (verify-files re-hashes the tree vs H); a tree mismatch is an ATTESTATION FAILURE (HALT), NEVER a
# silent rebuild. Only a first, clean run builds H.
if [ -f runs/H.json ]; then
  python3 attest.py verify-files --H runs/H.json \
    || { echo "FATAL: runs/H.json exists but the tree no longer matches it (attestation failure) — do NOT rebuild; HALT"; exit 1; }
  echo "  existing runs/H.json self-verified against the current tree — immutable, not rebuilt"
else
  python3 attest.py build-H --recorded-manifest "$RECORDED" --out runs/H.json --runtime
fi
H="$(python3 -c 'import json;print(json.load(open("runs/H.json"))["H"])')"
# Round-9 finding 1: cross-H generation-start guard. If a DURABLE generation-started marker exists
# for a DIFFERENT H, an observed key-3 instance was already generating — never proceed, never
# overwrite; demand classification. (In-place new-H runs are unsupported — use a fresh checkout.)
if [ -f runs/generation-started.json ]; then
  PRIOR_GEN_H="$(python3 -c 'import json;print(json.load(open("runs/generation-started.json")).get("H",""))')"
  if [ "$PRIOR_GEN_H" != "$H" ]; then
    echo "FATAL: generation-started recorded for a DIFFERENT H ($PRIOR_GEN_H) than the loaded H ($H)."
    echo "  An observed key-3 generation instance exists. CLASSIFY it (forfeit) in its own workspace;"
    echo "  in-place new-H runs are UNSUPPORTED — start a revised-prereg instance in a FRESH checkout."
    exit 1
  fi
fi

echo "== phase 1.5: structure:read custody entry (per-H, one-shot; on behalf of a VERIFIED projector receipt) =="
if python3 -c "import sys;sys.path.insert(0,'.');import spend;sys.exit(0 if spend.projector_completed('$SPENDLOG','$H') else 1)"; then
  echo "  structure:read already logged for this H — skip"
else
  # round-9 finding 7: re-verify the projector receipt vs the CURRENT pairs.json before registering
  # (a tamper between projection and registration is refused).
  python3 make_pairs_manifest.py --verify-receipt runs/pairs-receipt.json --pairs pairs.json \
    || { echo "structure:read REFUSED — projector receipt does not match pairs.json (tamper) — HALT"; exit 1; }
  python3 attest.py spend-log --event structure:read --H "$H" --out "$SPENDLOG" \
    || { echo "structure:read REFUSED (already present / accidental-access) — HALT"; exit 1; }
fi

echo "== phase 2: explicit-ID model probe (2 calls; membership) =="
if phase_check probe; then echo "  probe already complete (typed receipt) — skip"; else
  bash probe_explicit_id.sh || { echo "PROBE failed — pre-gen, nothing spent; resumable (re-run)"; exit 1; }
  phase_receipt probe runs/probe-log.json
fi

echo "== phase 3: confirmatory setup (per-key idempotent; completed keys are skipped, never regenerated) =="
python3 setup_confirmatory.py --H-value "$H" \
  || { log_state state:setup-exhaustion; echo "SETUP EXHAUSTION -> phase fails, config NOT retired, key still eligible (§4.1a)"; exit 2; }

echo "== phase 4: confirmatory draws — tool-path per conf key under H; gate <=1/40 =="
for ck in conf-key-1 conf-key-2; do
  if phase_check "draw-$ck" gate_pass=true; then echo "  draw $ck already complete (typed receipt) — skip"; continue; fi
  bash run_confirmatory.sh runs/confirmatory/$ck "$H" \
    || { log_state state:confirmatory-phase-fail; echo "CONFIRMATORY $ck FAILED -> configuration/H RETIRED (§4.1); key eligible for a new H"; exit 3; }
  # the TYPED confirmatory receipt IS runs/confirmatory/$ck/runs/confirmatory-result.json (gate_pass,
  # H, corpora hashes). Bind it as the phase receipt (require the result file; re-hashed on resume).
  phase_receipt "draw-$ck" "runs/confirmatory/$ck/runs/confirmatory-result.json" gate_pass=true
done

echo "== phase 5: ATTESTATION POINT 1 (POST-confirmatory; verifies BOTH confirmatory typed receipts) =="
# Round-9 finding 3: an attestation-1 failure here is POST-confirmatory (the draws already ran at
# phase 4), so it is NEVER silently resumable. It HALTS and demands classification: a benign
# (non-configuration) mismatch requires a RE-FREEZE + two NEW draws (once) in a fresh instance;
# a configuration mismatch RETIRES the configuration. Observed draw receipts are NOT reusable
# across a re-freeze (a new freeze = new H = new receipts). Pre-confirmatory aborts
# (projector/probe) are the resumable ones and were handled at their own phases.
if phase_check attest1; then echo "  attest-1 already complete (typed receipt) — skip"; else
  python3 attest.py attest --H runs/H.json --point 1 --recorded-cli "$RECORDED_CLI" --probe-log runs/probe-log.json \
      --confirmatory runs/confirmatory/conf-key-1 runs/confirmatory/conf-key-2 \
    || { echo "ATTESTATION-1 MISMATCH (post-confirmatory) — HALT, do NOT resume. CLASSIFY:";
         echo "  benign (non-configuration) mismatch -> re-freeze + two NEW draws required (once), fresh instance;";
         echo "  configuration mismatch -> configuration RETIRED. Observed draws are NOT reusable across a re-freeze.";
         exit 4; }
  python3 attest.py receipt --H runs/H.json --kind pre-generation --out runs/receipts.jsonl
  phase_receipt attest1 runs/attestation-point-1.json
fi

echo "== phase 6: key-3 tool-arm generation (sealed-answer-material-blind) =="
if phase_check generation; then echo "  generation already complete (typed receipt) — skip"; else
  # Round-9 finding 1: persist a DURABLE generation-started marker BEFORE the first key-3 call
  # (spend log + a single-file receipt for the cross-H startup guard). Idempotent for this H.
  if [ ! -f runs/generation-started.json ]; then
    log_state state:generation-started
    printf '{"H": "%s"}\n' "$H" > runs/generation-started.json
    python3 attest.py receipt --H runs/H.json --kind generation-started --out runs/receipts.jsonl
  fi
  python3 smoke_v010.py excerpts
  gen_loop prompts-checklist gate-checklists checklists/calls.tsv checklists/regen-calls.tsv
  gen_loop prompts-def gate-ladders definitions/calls.tsv definitions/regen-calls.tsv
  # DRAIN ladder mech/leak regens to quiescence BEFORE staging each conformance batch; after
  # gate_conformance stages semantic ladder regens, the loop top drains them before the next.
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
    || { echo "RETRIEVAL FAILED (infra) — resumable (re-run resumes via receipts)"; tail -5 runs/v010/retrieval-summary.txt; exit 1; }
  python3 v010.py stage-verify; calls runs/v010/verify/calls.tsv
  python3 v010.py aggregate
  python3 v010.py stage-adaptive-1; calls runs/v010/symcheck/calls.tsv; calls runs/v010/decompose/calls.tsv
  python3 v010.py stage-adaptive-2; calls runs/v010/containment/calls.tsv
  python3 v010.py compose            # ANSWER-BLIND composed per-pair verdicts -> runs/v010/verdicts.json
  phase_receipt generation runs/v010/verdicts.json
fi

echo "== phase 7: baselines (answer-blind generation + gate) =="
if phase_check baselines; then echo "  baselines already complete (typed receipt) — skip"; else
  "$VENVPY" baseline_a.py retrieve
  python3 baseline_a.py prompts; calls runs/baseline_a/calls.tsv; python3 baseline_a.py gate
  while [ -s runs/baseline_a/reask-calls.tsv ]; do calls runs/baseline_a/reask-calls.tsv; python3 baseline_a.py gate; done
  python3 baseline_b.py prompts; calls runs/baseline_b/calls.tsv; python3 baseline_b.py gate
  while [ -s runs/baseline_b/reask-calls.tsv ]; do calls runs/baseline_b/reask-calls.tsv; python3 baseline_b.py gate; done
  phase_receipt baselines "runs/baseline_a/records.json,runs/baseline_b/records.json"
fi

echo "== phase 8a: build the EXACT step-7 OUTPUT MANIFEST (finding 4; set-equality vs staged calls) =="
python3 attest.py build-output-manifest --H runs/H.json --out runs/output-manifest.json

echo "== phase 9: scoring — fresh attest-2 + atomic-claim spend, with the ONE bounded relaunch =="
# Each attempt runs attestation-point-2 FRESH (finding 1), then appends a bounded
# state:scoring-attempt (max 2, per-H) with an EXPLICIT `|| exit` (a refused marker NEVER reaches
# the scorer), then the scorer (which claims under the lock immediately before the first key byte,
# checks key-file existence + verifies its inputs against the output-manifest PRE-CLAIM, and
# records custody=spent at the claim).
run_attempt() {
  python3 attest.py attest --H runs/H.json --point 2 --recorded-cli "$RECORDED_CLI" \
      --probe-log runs/probe-log.json --output-manifest runs/output-manifest.json \
    || { log_state state:terminated-during-gen-or-attest2-mismatch; forfeit_custody attest2-mismatch; \
         echo "ATTEST-2 mismatch -> forfeited-unspent (§4.3)"; exit 1; }
  python3 attest.py receipt --H runs/H.json --kind attest2 --out runs/receipts.jsonl
  python3 attest.py spend-log --event state:scoring-attempt --H "$H" --out "$SPENDLOG" \
    || { echo "scoring-attempt REFUSED (cap reached or terminal state) — NOT launching the scorer"; exit 1; }
  python3 scorer_v010.py score --key-dir key --recorded-hashes "$RECORDED" --pairs pairs.json \
    --H runs/H.json --spend-log "$SPENDLOG" --custody-ledger "$KEYCUSTODY" \
    --output-manifest runs/output-manifest.json \
    --tool-verdicts runs/v010/verdicts.json --baseline-a runs/baseline_a/records.json \
    --baseline-b runs/baseline_b/records.json --out runs/scores.json
}
classify_failure() {  # $1 = first|final — classify a failed attempt via the LOCKED log
  if grep -q '"event": "spend:authorized-read-claimed"' "$SPENDLOG"; then
    log_state spend:fault-after-authorized-read
    echo "FAULT AFTER CLAIM — the sealed key is SPENT (custody already recorded) and the run is INVALID; NO relaunch (§4.4)"; exit 1
  fi
  [ "$1" = "final" ] || return 0
  log_state state:terminated-during-gen-or-attest2-mismatch; forfeit_custody pre-read-final
  echo "pre-read failure after the one relaunch — forfeited-unspent (§4.4)"; exit 1
}
if run_attempt; then echo "KEY3-V010-DONE"; exit 0; fi
classify_failure first
echo "pre-read failure before any claim — the ONE permitted relaunch (re-attesting point 2 first)"
if run_attempt; then echo "KEY3-V010-DONE"; exit 0; fi
classify_failure final
