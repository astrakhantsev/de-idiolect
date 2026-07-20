#!/usr/bin/env bash
# v0.7 TRAIN driver: revert repair docs (v0.6 negative), archive prior runs, then
# checklists -> ladder definitions -> polarity -> retrieval -> matrix verification.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"

echo "== revert v0.6 repair docs =="
rm -f corpora/a/12.md corpora/a/13.md corpora/a/14.md corpora/b/12.md corpora/b/13.md corpora/b/14.md

echo "== archive v0.6 runs =="
mkdir -p runs/v06-archive
for x in verify decompose definitions polarity e2 checklists symcheck containment agg.json results.json excerpts.json retrieval.json repair-calls.tsv repair-a.md gen-a-repair.out; do
  [ -e "runs/$x" ] && mv "runs/$x" runs/v06-archive/ 2>/dev/null || true
done
mkdir -p runs/verify runs/decompose runs/definitions runs/polarity runs/checklists runs/symcheck runs/containment runs/manifests

echo "== freeze v0.7 =="
{ echo "v0.7 FREEZE $(date -Iseconds)"; sha256sum prereg.md smoke.py retrieve_xc.py prompts/gen-definition-v07.md prompts/verify-matrix.md prompts/containment.md run_v07.sh; } >> freeze-manifest.txt

echo "== excerpts (reverted corpus) =="
python3 smoke.py excerpts

echo "== checklists =="
python3 smoke.py prompts-checklist
bash run_calls.sh checklist
for f in runs/checklists/out-*.txt; do ./leakcheck_peer.sh def "$f" || { echo "LEAK checklist $f — STOPPING"; exit 1; }; done

echo "== ladder definitions =="
python3 smoke.py prompts-def
bash run_calls.sh defs
for f in runs/definitions/out-*.json; do ./leakcheck_peer.sh def "$f" || { echo "LEAK definition $f — STOPPING"; exit 1; }; done

echo "== polarity =="
python3 smoke.py prompts-polarity
bash run_calls.sh polarity

echo "== retrieval (L2 keys) =="
"$VENVPY" retrieve_xc.py > runs/retrieval-summary.txt 2>&1 || { echo "retrieval FAILED"; exit 1; }
grep -o '"mutual": [a-z]*' runs/retrieval.json | sort | uniq -c

echo "== matrix verification =="
python3 smoke.py prompts-verify
bash run_calls.sh verify

echo "V07-MODEL-PHASES-DONE"
