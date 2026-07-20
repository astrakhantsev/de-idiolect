#!/usr/bin/env bash
# v0.5 fresh-key driver: freeze, generate corpora, run all model phases through verify.
# Scoring stages run interactively afterwards (raw-verdict inspection before accepting scores).
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
RUN="$BASE/../e2e-cell/run_isolated.sh"
VENVPY="$BASE/../../.venv/bin/python"

echo "== freeze v0.5 =="
{ echo "FRESH-KEY v0.5 FREEZE $(date -Iseconds)"; sha256sum prereg.md key/*.json prompts/*.md leakcheck_peer.sh smoke.py retrieve_xc.py e2_residues.py core_specificity.py run_calls.sh run_v05.sh; } > freeze-manifest.txt

echo "== corpus generation =="
"$RUN" claude sonnet "$BASE/prompts/gen-community-a.md" "$BASE/runs/gen-a.out" "$BASE/runs/manifests/gen-a.json"
"$RUN" codex gpt-5.6-terra "$BASE/prompts/gen-community-b.md" "$BASE/runs/gen-b.out" "$BASE/runs/manifests/gen-b.json"
python3 smoke.py split a runs/gen-a.out
python3 smoke.py split b runs/gen-b.out
for f in corpora/a/*.md; do
  ./leakcheck_peer.sh cross-a "$f" || { echo "LEAK cross-a $f — STOPPING"; exit 1; }
  ./leakcheck_peer.sh meta "$f" || { echo "LEAK meta $f — STOPPING"; exit 1; }
done
for f in corpora/b/*.md; do
  ./leakcheck_peer.sh cross-b "$f" || { echo "LEAK cross-b $f — STOPPING"; exit 1; }
  ./leakcheck_peer.sh meta "$f" || { echo "LEAK meta $f — STOPPING"; exit 1; }
done

echo "== excerpts =="
python3 smoke.py excerpts

echo "== checklists =="
python3 smoke.py prompts-checklist
bash run_calls.sh checklist
for f in runs/checklists/out-*.txt; do
  ./leakcheck_peer.sh def "$f" || { echo "LEAK checklist $f — STOPPING"; exit 1; }
done

echo "== definitions (checklist-guided) =="
python3 smoke.py prompts-def
bash run_calls.sh defs
for f in runs/definitions/out-*.txt; do
  ./leakcheck_peer.sh def "$f" || { echo "LEAK definition $f — STOPPING"; exit 1; }
done

echo "== polarity =="
python3 smoke.py prompts-polarity
bash run_calls.sh polarity

echo "== retrieval =="
"$VENVPY" retrieve_xc.py > runs/retrieval-summary.txt 2>&1 || { echo "retrieval FAILED"; exit 1; }
grep -o '"mutual": [a-z]*' runs/retrieval.json | sort | uniq -c

echo "== verification =="
python3 smoke.py prompts-verify
bash run_calls.sh verify

echo "V05-MODEL-PHASES-DONE"
