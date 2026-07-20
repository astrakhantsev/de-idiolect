#!/bin/bash
# Assembly blind Pass-A: 3 cross-model draws, search-enabled, reads blocked. Self-contained.
set -u
cd /tmp/claude-1000/-mnt-f-hub/9097f7a9-c6cf-46ce-ac93-3f86eec48a29/scratchpad/defnaming

ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local name="$1" model="$2"
  if [ -n "$model" ]; then
    claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < passa-assembly-brief.md > "out-$name.md" 2> "out-$name.err"
  else
    claude -p --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < passa-assembly-brief.md > "out-$name.md" 2> "out-$name.err"
  fi
  echo "done $name exit=$?"
}

sha256sum passa-assembly-brief.md

run PA-opus opus &
run PA-sonnet sonnet &
run PA-default "" &
wait
echo ALL_DONE
wc -c out-PA*.md 2>/dev/null
