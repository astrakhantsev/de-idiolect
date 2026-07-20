#!/bin/bash
# Launch the 5 blind weights-only draws in parallel. Self-contained, no positional args.
set -u
cd /tmp/claude-1000/-mnt-f-hub/9097f7a9-c6cf-46ce-ac93-3f86eec48a29/scratchpad/defnaming

DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,Bash,WebSearch,WebFetch,NotebookEdit"

run() {
  local name="$1" model="$2" brief="$3"
  if [ -n "$model" ]; then
    claude -p --model "$model" --allowedTools "" --disallowedTools "$DISALLOW" < "$brief" > "out-$name.md" 2> "out-$name.err"
  else
    claude -p --allowedTools "" --disallowedTools "$DISALLOW" < "$brief" > "out-$name.md" 2> "out-$name.err"
  fi
  echo "done $name exit=$?"
}

run D-opus opus brief-defs-frozen.md &
run D-sonnet sonnet brief-defs-frozen.md &
run D-default "" brief-defs-frozen.md &
run K-opus opus brief-control.md &
run K-sonnet sonnet brief-control.md &
wait
echo ALL_DONE
wc -c out-*.md 2>/dev/null
