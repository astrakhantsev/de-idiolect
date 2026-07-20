#!/usr/bin/env bash
# run_p2_gen.sh — P2 step 2: checklist-guided definition generation (spec P2, frozen).
# Guided prompt assembly (spec "Prompt assembly", exact): prompt-D.md's instruction +
# constraints (its trailing "NOTES:" label is the one re-emitted after the checklist
# block, not duplicated), one blank line, the commitments header line, the extracted
# checklist verbatim, one blank line, "NOTES:", the C2 excerpts verbatim.
# Generation: sonnet + opus, isolated; leak hit -> full regeneration (fresh sample),
# max 3 attempts; 3 leaking attempts -> config FAILS LOUDLY (e2e §2.4 rule).
set -euo pipefail
cd "$(dirname "$0")"
ABS="$(pwd)"
E2E="$(cd ../../e2e-cell && pwd)"
mkdir -p runs/inputs runs/manifests

# assemble guided prompt (checklist must exist and have passed leakcheck)
[[ -s runs/checklist-extracted.txt ]] || { echo "no extracted checklist"; exit 2; }
{
  sed '/^NOTES:$/,$d' "$E2E/prompt-D.md"
  echo "The definition must additionally preserve each of these structural commitments:"
  cat runs/checklist-extracted.txt
  echo
  echo "NOTES:"
  cat "$E2E/runs/c2-excerpts.md"
} > runs/inputs/guided-prompt.md
sha256sum runs/inputs/guided-prompt.md

for m in sonnet opus; do
  ok=0
  for attempt in 1 2 3; do
    out="$ABS/runs/guided-$m-attempt$attempt.txt"
    bash "$E2E/run_isolated.sh" claude "$m" "$ABS/runs/inputs/guided-prompt.md" "$out" "$ABS/runs/manifests/guided-$m-attempt$attempt.manifest"
    if bash "$E2E/leakcheck_e2e.sh" "$out" > "$out.leakcheck" 2>&1; then
      cp "$out" "$ABS/runs/guided-$m-ACCEPTED.txt"
      echo "$m: attempt $attempt CLEAN -> accepted"
      ok=1
      break
    else
      echo "$m: attempt $attempt LEAKED (see $out.leakcheck)"
    fi
  done
  [[ $ok == 1 ]] || echo "$m: CONFIG FAILED LOUDLY (3 leaking attempts)"
done
echo "P2 generation stage complete"
