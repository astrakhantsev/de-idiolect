#!/usr/bin/env bash
# v0.4 driver: archive v0.3 artifacts, freeze, then run all model phases through verify.
# Aggregation onward is done interactively (raw-verdict inspection before accepting scores).
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"

echo "== archive v0.3 =="
mkdir -p runs/v03-archive
for x in verify decompose definitions polarity e2 agg.json results.json excerpts.json retrieval.json; do
  [ -e "runs/$x" ] && mv "runs/$x" runs/v03-archive/
done
mkdir -p runs/verify runs/decompose runs/definitions runs/polarity runs/e2 runs/checklists

echo "== freeze v0.4 =="
{ echo "AMENDMENT v0.4 $(date -Iseconds)"; sha256sum prereg.md smoke.py core_specificity.py run_v04.sh prompts/checklist-extract.md prompts/gen-definition-v04.md; } >> freeze-manifest.txt

echo "== excerpts (v0.4 windows) =="
python3 smoke.py excerpts

echo "== checklists =="
python3 smoke.py prompts-checklist
bash run_calls.sh checklist
for f in runs/checklists/out-*.txt; do
  ./leakcheck_peer.sh def "$f" || { echo "LEAK in checklist $f — STOPPING"; exit 1; }
done

echo "== definitions (checklist-guided) =="
python3 smoke.py prompts-def
bash run_calls.sh defs
for f in runs/definitions/out-*.txt; do
  ./leakcheck_peer.sh def "$f" || { echo "LEAK in definition $f — STOPPING"; exit 1; }
done

echo "== polarity =="
python3 smoke.py prompts-polarity
bash run_calls.sh polarity

echo "== retrieval =="
"$VENVPY" retrieve_xc.py > runs/retrieval-summary.txt 2>&1 || { echo "retrieval FAILED"; exit 1; }
tail -25 runs/retrieval-summary.txt

echo "== verification =="
python3 smoke.py prompts-verify
bash run_calls.sh verify

echo "V04-MODEL-PHASES-DONE"
