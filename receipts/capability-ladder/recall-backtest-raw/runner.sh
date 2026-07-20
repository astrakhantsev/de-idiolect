#!/bin/bash
# Recall-lift backtest: 3 cases x 2 arms x 2 models = 12 blind, search-enabled draws.
# Reads/glob/grep denied; WebSearch + safefetch only. Self-contained.
set -u
cd /tmp/claude-1000/-mnt-f-hub/b80c8555-b842-46b0-aa6d-c6660df65048/scratchpad/recall-backtest

ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local brief="$1" model="$2"
  local tag="${brief%.md}-${model}"
  claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$brief" > "out-$tag.md" 2> "out-$tag.err"
  echo "done out-$tag exit=$?  bytes=$(wc -c < out-$tag.md 2>/dev/null)"
}

echo "=== brief hashes ==="
sha256sum c2-P.md c2-R.md c4-P.md c4-R.md covid-P.md covid-R.md

echo "=== WAVE 1: opus ==="
for b in c2-P.md c2-R.md c4-P.md c4-R.md covid-P.md covid-R.md; do run "$b" opus & done
wait

echo "=== WAVE 2: sonnet ==="
for b in c2-P.md c2-R.md c4-P.md c4-R.md covid-P.md covid-R.md; do run "$b" sonnet & done
wait

echo "ALL_DONE"
echo "=== output sizes ==="
wc -c out-*.md 2>/dev/null
echo "=== nonempty stderr (transient errors?) ==="
for f in out-*.err; do [ -s "$f" ] && echo "--- $f ---" && head -3 "$f"; done
