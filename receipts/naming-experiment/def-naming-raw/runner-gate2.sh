#!/bin/bash
# Gate 2: 4 blind draws (2 briefs x opus/sonnet), search-enabled, reads blocked. Self-contained.
set -u
cd /tmp/claude-1000/-mnt-f-hub/9097f7a9-c6cf-46ce-ac93-3f86eec48a29/scratchpad/defnaming

ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local name="$1" model="$2" brief="$3"
  claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$brief" > "out-$name.md" 2> "out-$name.err"
  echo "done $name exit=$?"
}

sha256sum gate2-brief-A.md gate2-brief-B.md

run G2A-opus opus gate2-brief-A.md &
run G2A-sonnet sonnet gate2-brief-A.md &
run G2B-opus opus gate2-brief-B.md &
run G2B-sonnet sonnet gate2-brief-B.md &
wait
echo ALL_DONE
wc -c out-G2*.md 2>/dev/null
