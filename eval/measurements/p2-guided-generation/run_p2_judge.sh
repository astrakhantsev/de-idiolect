#!/usr/bin/env bash
# run_p2_judge.sh — P2: frozen fidelity gate on the accepted guided definitions.
set -euo pipefail
cd "$(dirname "$0")"
ABS="$(pwd)"
E2E="$(cd ../../e2e-cell && pwd)"
header_end=$(grep -n '^CANDIDATE DEFINITION:$' "$E2E/runs/fidelity-input-sonnet.md" | cut -d: -f1)
head -n "$header_end" "$E2E/runs/fidelity-input-sonnet.md" > runs/inputs/_header.md
for m in sonnet opus; do
  [[ -s "runs/guided-$m-ACCEPTED.txt" ]] || { echo "$m: no accepted definition, skipping (config FAILED earlier)"; continue; }
  in="$ABS/runs/inputs/fidelity-input-guided-$m.md"
  cat runs/inputs/_header.md "runs/guided-$m-ACCEPTED.txt" > "$in"
  echo "=== judging guided-$m ==="
  bash "$E2E/run_isolated.sh" claude opus "$in" "$ABS/runs/fidelity-guided-$m.json" "$ABS/runs/manifests/fidelity-guided-$m.manifest"
done
echo "P2 judging complete"
