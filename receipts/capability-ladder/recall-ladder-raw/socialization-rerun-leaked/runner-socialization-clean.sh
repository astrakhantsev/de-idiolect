#!/bin/bash
# CLEAN re-run of the immersion arm: run dirs OUTSIDE <vault> so Claude Code does NOT
# auto-load the project's CLAUDE.md/AGENTS.md/MEMORY (the leak that confounded the first Part B —
# 4th instance of feedback_blind_pass_tool_level). Brief read by absolute path from the vault
# (reading the brief does NOT trigger project-context discovery; cwd does). File tools denied.
set -u
BRIEF=<vault>/10_projects/minelit/idiolect/recall-ladder-raw/briefs/c2-S-immersed.md
BASE=/tmp/claude-1000/-mnt-f-hub/93d71aaf-aae4-4850-b7aa-51b8ddea4778/scratchpad/socialization-clean
OUT=$BASE/out
RUNROOT=$BASE/runs
mkdir -p "$OUT" "$RUNROOT"
ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"
run() {
  local model="$1" draw="$2"; local tag="c2-S-${model}-${draw}"
  local rundir="$RUNROOT/$tag"; mkdir -p "$rundir"
  ( cd "$rundir" && claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$BRIEF" ) > "$OUT/out-$tag.md" 2> "$OUT/out-$tag.err"
  echo "done $tag exit=$? bytes=$(wc -c < "$OUT/out-$tag.md") rundir_empty=[$(ls -A "$rundir" 2>/dev/null | tr '\n' ' '):-EMPTY]"
}
echo "=== brief hash (must be d798686f...) ==="; sha256sum "$BRIEF"
echo "=== run cwd is OUTSIDE the vault: $RUNROOT ==="
for m in haiku sonnet opus fable; do run "$m" a & done; wait
for m in haiku sonnet opus fable; do run "$m" b & done; wait
echo "CLEAN_SOCIALIZATION_DONE"
echo "=== LEAK CHECK: grep new outputs for project-context markers (must be NONE) ==="
grep -liE "feedback_|novelty protocol|refuter|trap you flagged|your (own )?(project|notes|calibration|citation)|minelit|transfer bar|foreclosur|search-field-vocabulary|died on its" "$OUT"/out-*.md || echo "NONE — no project-context leak markers in any clean draw"
echo "=== sizes ==="; for f in "$OUT"/out-*.md; do printf "%-24s %6s\n" "$(basename "$f")" "$(wc -c < "$f")"; done