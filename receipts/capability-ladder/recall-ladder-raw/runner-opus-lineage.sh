#!/bin/bash
# Within-Opus-lineage capability axis for the claim's RECALL half: the P0 (bare-coinage,
# idiolect) arm on the 2 live cases, across older Opus versions. Tests whether the idiolect
# miss stays floored as capability rises within ONE model family (removes the size/generation
# confound of the Haiku/Sonnet/Opus ladder). Same isolation harness: own empty cwd per draw,
# brief by absolute path, output outside cwd, file tools denied, WebSearch + safefetch only.
set -u
BASE=/tmp/claude-1000/-mnt-f-hub/93d71aaf-aae4-4850-b7aa-51b8ddea4778/scratchpad/haiku-ladder
BRIEFDIR=$BASE/briefs
OUT=$BASE/out-opus-lineage
RUNROOT=$BASE/runs-opus-lineage
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
sha256sum "$BRIEFDIR"/c2-P0.md "$BRIEFDIR"/c4-P0.md

echo "=== Opus lineage P0 draws (6, parallel) ==="
for m in claude-opus-4-1 claude-opus-4-5 claude-opus-4-7; do
  for b in c2-P0.md c4-P0.md; do run "$b" "$m" & done
done
wait
echo "OPUS_LINEAGE_DONE"
echo "=== output sizes ==="; for f in "$OUT"/out-*.md; do printf "%-34s %7s\n" "$(basename "$f")" "$(wc -c < "$f")"; done
echo "=== nonempty stderr ==="; for f in "$OUT"/out-*.err; do [ -s "$f" ] && echo "--- $(basename "$f") ---" && head -3 "$f"; done
echo "SCRIPT_EXIT_OK"
