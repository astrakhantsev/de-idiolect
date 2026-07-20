#!/bin/bash
# Second cross-family draw: GPT-5.6-sol (the doc-review-tuned variant; terra was code-tuned).
# Correlated with terra (same base model) — a sanity second GPT config, not an independent family.
# P0 (bare-coinage) arm on both live cases. Same isolation/harness as the terra probe.
set -u
BASE=/tmp/claude-1000/-mnt-f-hub/93d71aaf-aae4-4850-b7aa-51b8ddea4778/scratchpad/haiku-ladder
BD=$BASE/briefs-codex
OUT=$BASE/out-codex
mkdir -p "$OUT"

run() {
  local brief="$1"; local tag="${brief%.md}-sol"
  local rundir; rundir=$(mktemp -d)
  ( cd "$rundir" && timeout 420 codex exec -m gpt-5.6-sol \
      -c model_reasoning_effort="medium" \
      -c tools.web_search=true \
      --ignore-user-config --ignore-rules --skip-git-repo-check \
      -C "$rundir" -s read-only --ephemeral \
      -o "$OUT/out-$tag.txt" < "$BD/$brief" ) > "$OUT/log-$tag.txt" 2>&1
  echo "done $tag exit=$? bytes=$(wc -c < "$OUT/out-$tag.txt" 2>/dev/null) rundir_empty=[$(ls -A "$rundir" 2>/dev/null | tr '\n' ' ')]"
  rmdir "$rundir" 2>/dev/null
}

echo "=== codex brief hashes ==="; sha256sum "$BD"/c2-P0-codex.md "$BD"/c4-P0-codex.md
run c2-P0-codex.md
run c4-P0-codex.md
echo "SOL_DONE"
for f in "$OUT"/out-*-sol.txt; do printf "%-30s %6s\n" "$(basename "$f")" "$(wc -c < "$f" 2>/dev/null)"; done
