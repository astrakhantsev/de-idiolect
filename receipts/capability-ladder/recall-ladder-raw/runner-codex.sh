#!/bin/bash
# Cross-family GENERALITY probe (not a ladder rung): GPT-5.6-terra runs the P0 (bare-coinage,
# idiolect) arm on both live cases, to test whether the idiolect miss generalizes beyond the
# Claude family. Concept+question are byte-identical to the Claude P0 briefs; only the tool-
# plumbing line differs (Codex uses its own web_search, not safefetch/WebSearch) — a documented
# harness adaptation, noted as a confound. Blind + isolated: fresh empty cwd per draw,
# --ignore-user-config + --ignore-rules (no project config/AGENTS.md), read-only sandbox.
set -u
BASE=/tmp/claude-1000/-mnt-f-hub/93d71aaf-aae4-4850-b7aa-51b8ddea4778/scratchpad/haiku-ladder
BD=$BASE/briefs-codex
OUT=$BASE/out-codex
mkdir -p "$OUT"

run() {
  local brief="$1"; local tag="${brief%.md}"
  local rundir; rundir=$(mktemp -d)
  ( cd "$rundir" && timeout 420 codex exec -m gpt-5.6-terra \
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
echo "CODEX_DONE"
for f in "$OUT"/out-*.txt; do printf "%-28s %6s\n" "$(basename "$f")" "$(wc -c < "$f" 2>/dev/null)"; done
