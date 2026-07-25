#!/usr/bin/env bash
# run_v010.sh — the ONE sealed key-3 v0.10 run driver. DO NOT run during the build (it makes
# LLM calls + reads the sealed key at the final scoring step). Encodes the exact prereg
# sequence: projector -> freeze -> probe -> setup -> confirmatory draws -> attest(1) ->
# generation -> attest(2) -> scoring. The generation phases loop the H1/H2 budget-2 regen
# cycle (up to 3 generations/artifact) until no regen/re-ask calls remain pending.
#
# PRECONDITIONS placed by the operator at run time (answer-blind except the sealed key):
#   corpora/a/*.md corpora/b/*.md (+manifests)  — frozen key-3 corpora (v0.9 recorded)
#   leakcheck_peer.sh                            — frozen key-3 leak checker (v0.9 recorded)
#   key/concepts.json key/answer_key.json        — SEALED; concepts.json parsed ONLY inside the
#       isolated projector (phase 0.5, custody-logged); answer_key.json read ONLY by the scorer
#       (phase 9, THE SPEND)
#   freeze-manifest.txt (recorded v0.9 manifests: corpora, BGE tree, SEALED recorded hashes)
#   recorded-cli.json = {"claude":"<ver>","codex":"<ver>"}  — recorded frozen CLI versions
# pairs.json is NOT placed by the operator — it is produced by the isolated projector below.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"          # for retrieval (BGE); tool-path/baseline calls use CLIs
RECORDED="${RECORDED_MANIFEST:-$BASE/freeze-manifest.txt}"
RECORDED_CLI="${RECORDED_CLI:-$BASE/recorded-cli.json}"
mkdir -p runs

calls() {  # run a staged tsv via the isolation wrapper; halt on run-scoped fault (rc>=2)
  local rc=0; bash "$BASE/run_calls.sh" "$1" || rc=$?
  if [ "$rc" -ge 2 ]; then echo "HALT: run-scoped fault in $1 (rc=$rc)"; exit "$rc"; fi
  [ "$rc" -eq 0 ] || echo "NOTE: failures in $1 routed per the frozen failure taxonomy"
}

# H1/H2 budget-2 loop: stage prompts -> run -> gate -> re-stage regens -> run -> gate ...
gen_loop() {
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
# make_pairs_manifest.py runs as its OWN OS process: the ONLY place the sealed key is parsed
# for the pairing; it emits NOTHING but the blind pairs.json + `pairs_sha256: <h>`. It HASH-
# GATES concepts.json against the recorded value in freeze-manifest.txt BEFORE parsing (abort
# with nothing read on mismatch), and registers a single typed `structure:read` (NON-SPEND) in
# the ONE authoritative spend log the scorer + attest read. (H does not exist yet — it binds
# this blind pairs.json at phase 1 — so the integrity check is against the committed
# freeze-manifest.txt, the same recorded values H then binds; --H is added at run time only if
# an H already exists.) Hash also logged to the custody log.
PAIRS_HASH_LINE="$(python3 make_pairs_manifest.py key pairs.json --recorded-hashes "$RECORDED" --spend-log runs/spend-log.jsonl)"
echo "$(date -Iseconds) projector $PAIRS_HASH_LINE" >> runs/custody-log.txt
echo "  $PAIRS_HASH_LINE (custody-logged; structure:read registered in runs/spend-log.jsonl)"

echo "== phase 1: FREEZE + build-H (manifest-of-manifests; binds the blind pairs.json) =="
python3 attest.py build-H --recorded-manifest "$RECORDED" --out runs/H.json
H="$(python3 -c 'import json;print(json.load(open("runs/H.json"))["H"])')"

echo "== phase 2: explicit-ID model probe (2 calls; membership) =="
bash probe_explicit_id.sh    # writes runs/probe-log.json; aborts on membership failure

echo "== phase 3: confirmatory setup — 2 fresh TRAIN keys via the frozen v0.9 path (§4.1a) =="
python3 setup_confirmatory.py --H-value "$H"    # uses the in-workspace harness/split_corpus.py (in H)

echo "== phase 4: confirmatory draws — run the tool-path on each conf key under H; gate <=1/40 =="
# a draw failing the <=1/40 gate RETIRES the effective configuration (§4.1). Proceed only if both pass.
bash run_confirmatory.sh runs/confirmatory/conf-key-1 "$H"
bash run_confirmatory.sh runs/confirmatory/conf-key-2 "$H"

echo "== phase 5: ATTESTATION POINT 1 (pre-generation) =="
python3 attest.py attest --H runs/H.json --point 1 --recorded-cli "$RECORDED_CLI" --probe-log runs/probe-log.json
python3 attest.py receipt --H runs/H.json --kind pre-generation --out runs/receipts.jsonl

echo "== phase 6: key-3 tool-arm generation (sealed-answer-material-blind) =="
python3 smoke_v010.py excerpts
gen_loop prompts-checklist gate-checklists checklists/calls.tsv checklists/regen-calls.tsv
gen_loop prompts-def gate-ladders definitions/calls.tsv definitions/regen-calls.tsv
# semantic conformance: one ordered batch per side per generation index; loop with ladder regens
for _ in 0 1 2; do
  python3 smoke_v010.py prompts-conformance
  if [ -s runs/conformance/calls.tsv ]; then calls runs/conformance/calls.tsv; fi
  python3 smoke_v010.py gate-conformance
  if [ -s runs/conformance/rerun-calls.tsv ]; then calls runs/conformance/rerun-calls.tsv; python3 smoke_v010.py gate-conformance; fi
  if [ -s runs/definitions/regen-calls.tsv ]; then calls runs/definitions/regen-calls.tsv; python3 smoke_v010.py gate-ladders; fi
done
python3 smoke_v010.py assert-resolved
python3 smoke_v010.py prompts-polarity; calls runs/polarity/calls.tsv; python3 smoke_v010.py gate-polarity
if [ -s runs/polarity/rerun-calls.tsv ]; then calls runs/polarity/rerun-calls.tsv; python3 smoke_v010.py gate-polarity; fi
python3 smoke_v010.py alive
"$VENVPY" retrieve_xc_v010.py --v010 --no-determinism > runs/v010/retrieval-summary.txt 2>&1 \
  || { echo "RETRIEVAL FAILED (run-scoped fault)"; tail -5 runs/v010/retrieval-summary.txt; exit 1; }
python3 v010.py stage-verify; calls runs/v010/verify/calls.tsv
python3 v010.py aggregate
python3 v010.py stage-adaptive-1; calls runs/v010/symcheck/calls.tsv; calls runs/v010/decompose/calls.tsv
python3 v010.py stage-adaptive-2; calls runs/v010/containment/calls.tsv
python3 v010.py compose            # ANSWER-BLIND composed per-pair verdicts -> runs/v010/verdicts.json

echo "== phase 7: baselines (answer-blind generation + gate) =="
"$VENVPY" baseline_a.py retrieve
python3 baseline_a.py prompts; calls runs/baseline_a/calls.tsv; python3 baseline_a.py gate
if [ -s runs/baseline_a/reask-calls.tsv ]; then calls runs/baseline_a/reask-calls.tsv; python3 baseline_a.py gate; fi
python3 baseline_b.py prompts; calls runs/baseline_b/calls.tsv; python3 baseline_b.py gate
if [ -s runs/baseline_b/reask-calls.tsv ]; then calls runs/baseline_b/reask-calls.tsv; python3 baseline_b.py gate; fi

echo "== phase 8: ATTESTATION POINT 2 (post-generation, before scoring) =="
python3 attest.py attest --H runs/H.json --point 2 --recorded-cli "$RECORDED_CLI" --probe-log runs/probe-log.json
python3 attest.py receipt --H runs/H.json --kind post-generation --out runs/receipts.jsonl

echo "== phase 9: scoring — atomic-claim spend, with the ONE permitted pre-read relaunch =="
# The scorer appends `spend:authorized-read-claimed` UNDER THE LOCK immediately before the
# first key byte and `spend:authorized-read-complete` after; the driver appends NO post-hoc
# authorized-read. Relaunch rule: the driver records a bounded `state:scoring-attempt` (max 2)
# before each launch; a scorer failure BEFORE any claim (no claim entry) with attempts<2 gets
# ONE relaunch; a failure AFTER the claim means the key is SPENT — no relaunch, run invalid.
SPENDLOG="runs/spend-log.jsonl"
run_scorer_once() {
  python3 attest.py spend-log --event state:scoring-attempt --out "$SPENDLOG"   # bounded (max 2)
  python3 scorer_v010.py --key-dir key --recorded-hashes "$RECORDED" --pairs pairs.json \
    --H runs/H.json --spend-log "$SPENDLOG" \
    --tool-verdicts runs/v010/verdicts.json --baseline-a runs/baseline_a/records.json \
    --baseline-b runs/baseline_b/records.json --out runs/scores.json
}
if ! run_scorer_once; then
  if grep -q '"event": "spend:authorized-read-claimed"' "$SPENDLOG"; then
    echo "FAULT AFTER CLAIM — the sealed key is SPENT and the run is INVALID; NO relaunch (§4.4)"; exit 1
  fi
  echo "pre-read failure before any claim — taking the ONE permitted relaunch"
  run_scorer_once || { echo "relaunch also failed pre-read — forfeited-unspent (§4.4)"; exit 1; }
fi

echo "KEY3-V010-DONE"
