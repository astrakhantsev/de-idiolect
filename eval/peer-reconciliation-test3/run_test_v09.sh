#!/usr/bin/env bash
# run_test_v09.sh — the ONE sealed key-3 TEST run under the frozen v0.9 spec
# (prereg-v09.md; PROTOCOL.md v0.9 amendment: fires once, judged at tau1, all τ reported,
# per-pair failures never diagnosed into design changes).
#
# Workspace notes: the KEY is sealed (hash-checked against SEALED-manifest.txt before
# anything runs); gen-community-*.md are sealed model inputs whose contents the
# orchestrator never reads; leakcheck_peer.sh is the sealed key-3-generated checker.
# The instrument (smoke.py, v09.py, prompts, runner, retrieval) is the frozen v0.9
# package copied verbatim from the TRAIN workspace, except: retrieve_xc.py carries a
# --no-determinism flag (TEST has no frozen retrieval baseline — this first execution
# IS the record) and split_corpus.py restores the mechanical corpus splitter.
# There are NO carried stage outputs (empty carried-manifest): every call is fresh.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"

calls() {
  local rc=0
  bash run_calls.sh "$1" || rc=$?
  if [ "$rc" -ge 2 ]; then echo "HALT: run-scoped fault in $1 (rc=$rc)"; exit "$rc"; fi
  [ "$rc" -eq 0 ] || echo "NOTE: failures in $1 routed per the frozen failure taxonomy"
}

echo "== phase 0: seal check + offline tests =="
sha256sum -c <(grep -E "key/concepts.json|key/answer_key.json" SEALED-manifest.txt) \
  || { echo "SEAL VIOLATION: key files changed"; exit 3; }
python3 test_v08.py
python3 test_v09.py

mkdir -p runs/v09 runs/manifests
[ -f runs/v09/carried-manifest.json ] || echo "[]" > runs/v09/carried-manifest.json

echo "== phase 1: instrument freeze (before any model call) =="
if [ ! -f runs/v09/.frozen ]; then
  {
    echo ""
    echo "== key-3 TEST FREEZE $(date -Iseconds) (v0.9 instrument; key sealed separately in SEALED-manifest.txt) =="
    sha256sum \
      prereg-v08.md prereg-v09.md smoke.py v09.py test_v08.py test_v09.py \
      retrieve_xc.py run_calls.sh run_test_v09.sh split_corpus.py \
      leakcheck_peer.sh \
      ../peer-reconciliation-harness/gen_leakcheck.py \
      ../e2e-cell/run_isolated.sh \
      ../peer-reconciliation-harness/PROTOCOL.md \
      prompts/checklist-extract.md prompts/gen-definition-v07.md \
      prompts/ladder-conformance.md prompts/polarity-check.md \
      prompts/verify-matrix.md prompts/verify-pair.md \
      prompts/decompose.md prompts/containment-v2.md \
      prompts/gen-community-a.md prompts/gen-community-b.md \
      key/concepts.json key/answer_key.json \
      runs/v09/carried-manifest.json
    "$VENVPY" retrieve_xc.py --snapshot-hash
  } >> freeze-manifest.txt
  touch runs/v09/.frozen
fi

echo "== phase 2: resolved model identifiers =="
if [ ! -f runs/v09/.models-recorded ]; then
  {
    echo "-- key-3 TEST resolved models $(date -Iseconds) --"
    th="$(mktemp -d)"; mkdir -p "$th/.claude"
    cp "$HOME/.claude/.credentials.json" "$th/.claude/.credentials.json"
    for m in sonnet opus; do
      rid="$( (cd "$(mktemp -d)" && HOME="$th" claude -p 'Reply with exactly: OK' --model "$m" --output-format json 2>/dev/null) \
        | python3 -c 'import json,sys
d=json.load(sys.stdin); u=d.get("modelUsage") or {}
print(",".join(sorted(u)) if u else d.get("model","unrecorded"))' || echo unrecorded)"
      echo "resolved_model[$m]: $rid"
    done
    rm -rf "$th"
    echo "codex_model: gpt-5.6-terra (pinned id)"
    echo "claude_cli_version: $(claude --version 2>/dev/null)"
    echo "codex_cli_version: $(codex --version 2>/dev/null)"
  } >> freeze-manifest.txt
  touch runs/v09/.models-recorded
fi

echo "== phase 3: corpus generation (sealed prompts; 2 calls) =="
# paths MUST be absolute: run_isolated reads the prompt from inside a fresh temp cwd
# (harness fix 2026-07-19, logged: first launch aborted pre-call on relative paths)
RUNISO="$BASE/../e2e-cell/run_isolated.sh"
if [ ! -s corpora/a/manifest.json ]; then
  "$RUNISO" claude sonnet "$BASE/prompts/gen-community-a.md" "$BASE/runs/gen-a.out" "$BASE/runs/manifests/gen-a.json"
  python3 split_corpus.py a runs/gen-a.out
fi
if [ ! -s corpora/b/manifest.json ]; then
  "$RUNISO" codex gpt-5.6-terra "$BASE/prompts/gen-community-b.md" "$BASE/runs/gen-b.out" "$BASE/runs/manifests/gen-b.json"
  python3 split_corpus.py b runs/gen-b.out
fi
{ echo "-- key-3 TEST corpus hashes (outputs of the frozen gen prompts) --";
  sha256sum corpora/a/manifest.json corpora/b/manifest.json corpora/a/[0-9][0-9].md corpora/b/[0-9][0-9].md; } >> freeze-manifest.txt

echo "== phase 4: corpus leak checks =="
for f in corpora/a/[0-9][0-9].md; do ./leakcheck_peer.sh cross-a "$f" && ./leakcheck_peer.sh meta "$f" || { echo "LEAK in $f — halting"; exit 3; }; done
for f in corpora/b/[0-9][0-9].md; do ./leakcheck_peer.sh cross-b "$f" && ./leakcheck_peer.sh meta "$f" || { echo "LEAK in $f — halting"; exit 3; }; done

echo "== phase 5: excerpts (pool = all 11 docs) + floor =="
python3 smoke.py excerpts

echo "== phase 6: checklists =="
python3 smoke.py prompts-checklist
calls runs/checklists/calls.tsv
python3 smoke.py gate-checklists
if [ -s runs/checklists/regen-calls.tsv ]; then
  calls runs/checklists/regen-calls.tsv
  python3 smoke.py gate-checklists
fi

echo "== phase 7: ladders + conformance =="
python3 smoke.py prompts-def
calls runs/definitions/calls.tsv
python3 smoke.py gate-ladders
if [ -s runs/definitions/regen-calls.tsv ]; then
  calls runs/definitions/regen-calls.tsv
  python3 smoke.py gate-ladders
fi
python3 smoke.py prompts-conformance
calls runs/conformance/calls.tsv
python3 smoke.py gate-conformance
if [ -s runs/conformance/rerun-calls.tsv ]; then
  calls runs/conformance/rerun-calls.tsv
  python3 smoke.py gate-conformance
fi
if [ -s runs/definitions/regen-calls.tsv ]; then
  calls runs/definitions/regen-calls.tsv
  python3 smoke.py gate-ladders
  python3 smoke.py prompts-conformance
  calls runs/conformance/calls.tsv
  python3 smoke.py gate-conformance
  if [ -s runs/conformance/rerun-calls.tsv ]; then
    calls runs/conformance/rerun-calls.tsv
    python3 smoke.py gate-conformance
  fi
fi
python3 smoke.py assert-resolved

echo "== phase 8: polarity =="
python3 smoke.py prompts-polarity
calls runs/polarity/calls.tsv
python3 smoke.py gate-polarity
if [ -s runs/polarity/rerun-calls.tsv ]; then
  calls runs/polarity/rerun-calls.tsv
  python3 smoke.py gate-polarity
fi

echo "== phase 9: retrieval (both queries; first execution is the record) =="
python3 smoke.py alive
"$VENVPY" retrieve_xc.py --v09 --no-determinism > runs/v09/retrieval-summary.txt 2>&1 \
  || { echo "RETRIEVAL FAILED (run-scoped fault)"; tail -5 runs/v09/retrieval-summary.txt; exit 1; }

echo "== phase 10: verification + union-routed adaptive stages =="
python3 v09.py stage-verify
calls runs/v09/verify/calls.tsv
python3 v09.py aggregate
python3 v09.py stage-adaptive-1
calls runs/v09/symcheck/calls.tsv
calls runs/v09/decompose/calls.tsv
python3 v09.py stage-adaptive-2
calls runs/v09/containment/calls.tsv

echo "== phase 11: per-τ composition (bar = tau1; aggregate metrics only) =="
python3 v09.py compose

echo "KEY3-TEST-DONE"
