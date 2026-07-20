#!/usr/bin/env bash
# v0.6 driver (workspace-agnostic: TRAIN = peer-reconciliation-fresh, TEST = peer-reconciliation-test3).
# Runs all model phases through verification; scoring stages are run interactively afterwards.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
RUN="$BASE/../e2e-cell/run_isolated.sh"
VENVPY="$BASE/../../.venv/bin/python"

echo "== archive prior runs =="
if [ -e runs/agg.json ] || [ -e runs/verify/calls.tsv ]; then
  mkdir -p runs/prior-archive
  for x in verify decompose definitions polarity e2 checklists symcheck containment agg.json results.json excerpts.json retrieval.json core_specificity.json; do
    [ -e "runs/$x" ] && mv "runs/$x" runs/prior-archive/ 2>/dev/null || true
  done
fi
mkdir -p runs/verify runs/decompose runs/definitions runs/polarity runs/e2 runs/checklists runs/symcheck runs/containment runs/manifests

echo "== freeze =="
{ echo "v0.6 FREEZE $(date -Iseconds)"; sha256sum prereg.md key/*.json prompts/*.md leakcheck_peer.sh smoke.py retrieve_xc.py e2_residues.py core_specificity.py run_calls.sh run_v06.sh; } >> freeze-manifest.txt

if [ ! -s corpora/a/01.md ]; then
  echo "== corpus generation (fresh workspace) =="
  "$RUN" claude sonnet "$BASE/prompts/gen-community-a.md" "$BASE/runs/gen-a.out" "$BASE/runs/manifests/gen-a.json"
  "$RUN" codex gpt-5.6-terra "$BASE/prompts/gen-community-b.md" "$BASE/runs/gen-b.out" "$BASE/runs/manifests/gen-b.json"
  python3 smoke.py split a runs/gen-a.out
  python3 smoke.py split b runs/gen-b.out
  for f in corpora/a/*.md; do ./leakcheck_peer.sh cross-a "$f" && ./leakcheck_peer.sh meta "$f" || { echo "LEAK $f — STOPPING"; exit 1; }; done
  for f in corpora/b/*.md; do ./leakcheck_peer.sh cross-b "$f" && ./leakcheck_peer.sh meta "$f" || { echo "LEAK $f — STOPPING"; exit 1; }; done
fi

echo "== excerpts (initial) =="
python3 smoke.py excerpts

echo "== coverage floor =="
python3 smoke.py coverage-repair
if [ -s runs/repair-calls.tsv ]; then
  bash run_calls.sh repair
  [ -s runs/gen-a-repair.out ] && python3 smoke.py split a runs/gen-a-repair.out
  [ -s runs/gen-b-repair.out ] && python3 smoke.py split b runs/gen-b-repair.out
  for f in corpora/a/1[2-4].md; do [ -e "$f" ] && { ./leakcheck_peer.sh cross-a "$f" && ./leakcheck_peer.sh meta "$f" || { echo "LEAK $f — STOPPING"; exit 1; }; }; done
  for f in corpora/b/1[2-4].md; do [ -e "$f" ] && { ./leakcheck_peer.sh cross-b "$f" && ./leakcheck_peer.sh meta "$f" || { echo "LEAK $f — STOPPING"; exit 1; }; }; done
  echo "== excerpts (post-repair) =="
  python3 smoke.py excerpts
fi

echo "== checklists =="
python3 smoke.py prompts-checklist
bash run_calls.sh checklist
for f in runs/checklists/out-*.txt; do ./leakcheck_peer.sh def "$f" || { echo "LEAK checklist $f — STOPPING"; exit 1; }; done

echo "== definitions =="
python3 smoke.py prompts-def
bash run_calls.sh defs
for f in runs/definitions/out-*.txt; do ./leakcheck_peer.sh def "$f" || { echo "LEAK definition $f — STOPPING"; exit 1; }; done

echo "== polarity =="
python3 smoke.py prompts-polarity
bash run_calls.sh polarity

echo "== retrieval =="
"$VENVPY" retrieve_xc.py > runs/retrieval-summary.txt 2>&1 || { echo "retrieval FAILED"; exit 1; }
grep -o '"mutual": [a-z]*' runs/retrieval.json | sort | uniq -c

echo "== verification =="
python3 smoke.py prompts-verify
bash run_calls.sh verify

echo "V06-MODEL-PHASES-DONE"
