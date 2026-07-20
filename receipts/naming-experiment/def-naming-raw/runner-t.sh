#!/bin/bash
# Targeted passes T1-T3 (verification, not blind). Self-contained.
set -u
cd /tmp/claude-1000/-mnt-f-hub/9097f7a9-c6cf-46ce-ac93-3f86eec48a29/scratchpad/defnaming

ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"

run() {
  local name="$1" model="$2" brief="$3"
  claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$brief" > "out-$name.md" 2> "out-$name.err"
  echo "done $name exit=$?"
}

sha256sum t1-brief-terminology.md t2-brief-patents-enterprise.md t3-brief-recent-academic.md

run T1-terminology opus t1-brief-terminology.md &
run T2-patents sonnet t2-brief-patents-enterprise.md &
run T3-recent sonnet t3-brief-recent-academic.md &
wait
echo ALL_DONE
wc -c out-T*.md 2>/dev/null
