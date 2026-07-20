#!/bin/bash
# P0 (bare-coinage) arm: the ecologically-valid baseline. 2 cases x 2 models = 4 draws.
set -u
cd /tmp/claude-1000/-mnt-f-hub/b80c8555-b842-46b0-aa6d-c6660df65048/scratchpad/recall-backtest
ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"
run() {
  local brief="$1" model="$2"; local tag="${brief%.md}-${model}"
  claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$brief" > "out-$tag.md" 2> "out-$tag.err"
  echo "done out-$tag exit=$? bytes=$(wc -c < out-$tag.md 2>/dev/null)"
}
sha256sum c2-P0.md c4-P0.md
for b in c2-P0.md c4-P0.md; do run "$b" opus & done; wait
for b in c2-P0.md c4-P0.md; do run "$b" sonnet & done; wait
echo "P0_ALL_DONE"
wc -c out-*P0*.md 2>/dev/null
