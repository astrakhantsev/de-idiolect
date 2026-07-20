#!/usr/bin/env bash
# run_p1.sh — P1 fidelity-judge calibration (measurement spec P1, frozen).
# Judges all 9 authored definitions with the FROZEN e2e fidelity config:
# opus via run_isolated.sh, judge framing byte-identical to the e2e cell
# (header sliced from runs/fidelity-input-sonnet.md up to CANDIDATE DEFINITION:),
# one isolated call per definition, run order = ascending sha256(definition file).
set -euo pipefail
cd "$(dirname "$0")"
ABS="$(pwd)"
E2E="$(cd ../../e2e-cell && pwd)"
mkdir -p runs/inputs runs/manifests

header_end=$(grep -n '^CANDIDATE DEFINITION:$' "$E2E/runs/fidelity-input-sonnet.md" | cut -d: -f1)
head -n "$header_end" "$E2E/runs/fidelity-input-sonnet.md" > runs/inputs/_header.md

order_file=runs/run-order.txt
: > "$order_file"
for f in definitions/*.md; do
  id=$(basename "$f" .md)
  h=$(sha256sum "$f" | cut -d' ' -f1)
  echo "$h $id" >> "$order_file"
done
sort -o "$order_file" "$order_file"

while read -r h id; do
  in="$ABS/runs/inputs/fidelity-input-$id.md"
  cat runs/inputs/_header.md "definitions/$id.md" > "$in"
  echo "=== judging $id (def sha256 $h) ==="
  bash "$E2E/run_isolated.sh" claude opus "$in" "$ABS/runs/fidelity-$id.json" "$ABS/runs/manifests/fidelity-$id.manifest"
done < "$order_file"
echo "P1 judging complete: $(ls runs/fidelity-*.json | wc -l) verdict files"
