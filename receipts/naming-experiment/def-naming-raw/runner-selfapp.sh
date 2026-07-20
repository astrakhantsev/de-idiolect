#!/bin/bash
# Self-application blind naming pass: 3 cross-model draws, search-enabled, reads blocked. Self-contained.
set -u
cd /tmp/claude-1000/-mnt-f-hub/482c0e5e-95e2-408b-a2f6-3b7c77964f41/scratchpad/selfapp

ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local name="$1" model="$2"
  if [ -n "$model" ]; then
    claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < selfapp-brief.md > "out-$name.md" 2> "out-$name.err"
  else
    claude -p --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < selfapp-brief.md > "out-$name.md" 2> "out-$name.err"
  fi
  echo "done $name exit=$?"
}

sha256sum selfapp-brief.md

run SA-opus opus &
run SA-sonnet sonnet &
run SA-default "" &
wait
echo ALL_DONE
wc -c out-SA*.md 2>/dev/null
