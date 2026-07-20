#!/bin/bash
# Haiku rung for the recall-ladder: the 2 load-bearing arms (P0 bare coinage, R neutral
# definition) on the 2 live cases (C2, C4). Same isolation harness as the clean rerun:
# each draw in its OWN empty temp cwd; brief read by absolute path; output written OUTSIDE
# the run cwd; file tools denied; WebSearch + safefetch only. 4 draws, draw tag = d.
set -u
BASE=/tmp/claude-1000/-mnt-f-hub/93d71aaf-aae4-4850-b7aa-51b8ddea4778/scratchpad/haiku-ladder
BRIEFDIR=$BASE/briefs
OUT=$BASE/out
RUNROOT=$BASE/runs
mkdir -p "$OUT" "$RUNROOT"
ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local brief="$1" model="$2" draw="$3"
  local tag="${brief%.md}-${model}-${draw}"
  local rundir="$RUNROOT/$tag"
  mkdir -p "$rundir"
  ( cd "$rundir" && claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$BRIEFDIR/$brief" ) > "$OUT/out-$tag.md" 2> "$OUT/out-$tag.err"
  local ec=$?
  local leftover=$(ls -A "$rundir" 2>/dev/null | tr '\n' ' ')
  echo "done $tag exit=$ec bytes=$(wc -c < "$OUT/out-$tag.md") rundir_empty=[${leftover:-EMPTY}]"
}

echo "=== brief hashes (must match prereg) ==="
sha256sum "$BRIEFDIR"/c2-P0.md "$BRIEFDIR"/c2-R.md "$BRIEFDIR"/c4-P0.md "$BRIEFDIR"/c4-R.md

echo "=== WAVE d: haiku (4 load-bearing draws, parallel) ==="
for b in c2-P0.md c2-R.md c4-P0.md c4-R.md; do run "$b" haiku d & done
wait
echo "HAIKU_ALL_DONE"
echo "=== output sizes ==="; for f in "$OUT"/out-*-haiku-d.md; do printf "%-28s %7s\n" "$(basename "$f")" "$(wc -c < "$f")"; done
echo "=== contamination self-flag scan (should be empty) ==="
grep -liE "prior (model|run)|sibling|leaked prior|I saw this via|another draw" "$OUT"/out-*-haiku-d.md 2>/dev/null || echo "NONE"
echo "=== nonempty stderr ==="; for f in "$OUT"/out-*-haiku-d.err; do [ -s "$f" ] && echo "--- $(basename "$f") ---" && head -3 "$f"; done
