#!/bin/bash
set -u
BRIEF=/mnt/f/hub/10_projects/minelit/idiolect/recall-ladder-raw/briefs/c2-S-immersed.md
OUT=/mnt/f/hub/10_projects/minelit/idiolect/recall-ladder-raw/socialization
RUNROOT=$OUT/runs
mkdir -p "$OUT" "$RUNROOT"
ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"
run() {
  local model="$1" draw="$2"; local tag="c2-S-${model}-${draw}"
  local rundir="$RUNROOT/$tag"; mkdir -p "$rundir"
  ( cd "$rundir" && claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$BRIEF" ) > "$OUT/out-$tag.md" 2> "$OUT/out-$tag.err"
  echo "done $tag exit=$? bytes=$(wc -c < "$OUT/out-$tag.md") rundir_empty=[$(ls -A "$rundir"|tr '\n' ' '):-EMPTY]"
}
WAVE="${1:?usage: run-socialization-wave.sh <a|b>}"
sha256sum "$BRIEF"   # must match d798686f...
for m in haiku sonnet opus fable; do run "$m" "$WAVE" & done; wait
echo "WAVE_${WAVE}_DONE"
