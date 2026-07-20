#!/bin/bash
# Fable 5 rung — the ceiling sanity check. Full rung: P0 (idiolect) + R (definition) on both
# live cases. Same isolation harness. NOTE: orchestrator is also Fable 5, but draws are blind
# (empty cwd, no project context) and scored against primary sources, so no self-grading bias.
set -u
BASE=/tmp/claude-1000/-mnt-f-hub/93d71aaf-aae4-4850-b7aa-51b8ddea4778/scratchpad/haiku-ladder
BRIEFDIR=$BASE/briefs
OUT=$BASE/out-fable
RUNROOT=$BASE/runs-fable
mkdir -p "$OUT" "$RUNROOT"
ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local brief="$1" model="$2"
  local tag="${brief%.md}-${model}"
  local rundir="$RUNROOT/$tag"
  mkdir -p "$rundir"
  ( cd "$rundir" && claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$BRIEFDIR/$brief" ) > "$OUT/out-$tag.md" 2> "$OUT/out-$tag.err"
  local ec=$?
  local leftover=$(ls -A "$rundir" 2>/dev/null | tr '\n' ' ')
  echo "done $tag exit=$ec bytes=$(wc -c < "$OUT/out-$tag.md") rundir_empty=[${leftover:-EMPTY}]"
}

echo "=== brief hashes (must match prereg) ==="
sha256sum "$BRIEFDIR"/c2-P0.md "$BRIEFDIR"/c2-R.md "$BRIEFDIR"/c4-P0.md "$BRIEFDIR"/c4-R.md
echo "=== Fable rung (4 draws, parallel) ==="
for b in c2-P0.md c2-R.md c4-P0.md c4-R.md; do run "$b" fable & done
wait
echo "FABLE_DONE"
echo "=== output sizes ==="; for f in "$OUT"/out-*.md; do printf "%-30s %7s\n" "$(basename "$f")" "$(wc -c < "$f")"; done
echo "=== nonempty stderr ==="; for f in "$OUT"/out-*.err; do [ -s "$f" ] && echo "--- $(basename "$f") ---" && head -3 "$f"; done
echo "SCRIPT_EXIT_OK"
