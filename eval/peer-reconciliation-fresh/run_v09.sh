#!/usr/bin/env bash
# run_v09.sh — v0.9 TRAIN resample driver (prereg-v09.md is the authority).
# The v0.8 tree under runs/ is the frozen INPUT record and is never written to;
# all v0.9 outputs live under runs/v09/. Resumable via run_calls.sh completion checks.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"

# round-2 F4: absorb ONLY ordinary model-call failures (exit 1, routed per §4);
# a run-scoped harness fault (exit >= 2) halts the driver for repair.
calls() {
  local rc=0
  bash run_calls.sh "$1" || rc=$?
  if [ "$rc" -ge 2 ]; then echo "HALT: run-scoped fault in $1 (rc=$rc) — fix and re-execute"; exit "$rc"; fi
  [ "$rc" -eq 0 ] || echo "NOTE: failures in $1 routed per §4 (no retry at verification/adaptive stages)"
}

echo "== phase 0: offline tests (v0.8 suite + v0.9 suite; no model calls) =="
python3 test_v08.py
python3 test_v09.py

mkdir -p runs/v09

echo "== phase 1: carried stage outputs (§0.5) + provenance manifest =="
# round-2 F2: copy only on the first run (pre-freeze); a resume VERIFIES, never rewrites
if [ ! -f runs/v09/carried-manifest.json ]; then
  python3 v09.py carry-stages
else
  python3 v09.py verify-carried
fi

echo "== phase 2: freeze (full v0.9 inventory + carried manifest, before any model call) =="
if [ ! -f runs/v09/.frozen ]; then
  {
    echo ""
    echo "== v0.9 FREEZE $(date -Iseconds) (prereg-v09.md §2.7 inventory) =="
    sha256sum \
      prereg-v08.md prereg-v09.md smoke.py v09.py test_v08.py test_v09.py \
      retrieve_xc.py run_calls.sh run_v09.sh review_pairs.py cf_rescore_v08.py \
      leakcheck_peer.sh \
      ../peer-reconciliation-harness/gen_leakcheck.py \
      ../e2e-cell/run_isolated.sh \
      ../peer-reconciliation-harness/PROTOCOL.md \
      prompts/checklist-extract.md prompts/gen-definition-v07.md \
      prompts/ladder-conformance.md prompts/polarity-check.md \
      prompts/verify-matrix.md prompts/verify-pair.md \
      prompts/decompose.md prompts/containment-v2.md \
      key/concepts.json key/answer_key.json \
      corpora/a/manifest.json corpora/b/manifest.json \
      corpora/a/[0-9][0-9].md corpora/b/[0-9][0-9].md \
      runs/v09/carried-manifest.json
    "$VENVPY" retrieve_xc.py --snapshot-hash
  } >> freeze-manifest.txt
  touch runs/v09/.frozen
  echo "frozen (appended to freeze-manifest.txt)"
else
  echo "already frozen (runs/v09/.frozen)"
fi

echo "== phase 3: resolved model identifiers at run start (§7 of v0.8, carried) =="
if [ ! -f runs/v09/.models-recorded ]; then
  {
    echo "-- v0.9 resolved models at run start $(date -Iseconds) --"
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
    echo "codex_model: gpt-5.6-terra (pinned id; alias resolution not observable — v0.8 §7/§9-F9)"
    echo "claude_cli_version: $(claude --version 2>/dev/null)"
    echo "codex_cli_version: $(codex --version 2>/dev/null)"
  } >> freeze-manifest.txt
  touch runs/v09/.models-recorded
fi

echo "== phase 4: retrieval — both queries, one execution, determinism check (§2.2/§2.4) =="
"$VENVPY" retrieve_xc.py --v09 > runs/v09/retrieval-summary.txt 2>&1 \
  || { echo "RETRIEVAL FAILED (run-scoped fault)"; tail -5 runs/v09/retrieval-summary.txt; exit 1; }
grep -E "determinism" runs/v09/retrieval-summary.txt || { echo "determinism check line missing"; exit 1; }

echo "== phase 5: fresh verification layer (20 calls) =="
python3 v09.py stage-verify
calls runs/v09/verify/calls.tsv

echo "== phase 6: aggregate + union-route adaptive stages (§2.3) =="
python3 v09.py aggregate
python3 v09.py stage-adaptive-1
calls runs/v09/symcheck/calls.tsv
calls runs/v09/decompose/calls.tsv
python3 v09.py stage-adaptive-2
calls runs/v09/containment/calls.tsv

echo "== phase 7: per-τ composition (primary = tau1) =="
python3 v09.py compose

echo "V09-RESAMPLE-DONE"
