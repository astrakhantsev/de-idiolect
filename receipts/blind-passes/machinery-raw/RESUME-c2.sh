#!/usr/bin/env bash
set -euo pipefail
cd /tmp/claude-1000/-mnt-f-hub/4611a506-d944-4aff-9b44-66148b1dd8af/scratchpad
claude -p --model sonnet \
  --allowedTools "WebSearch,Bash(safefetch:*)" \
  --disallowedTools "Read,Glob,Grep,Task,Agent,Edit,Write" \
  < machinery-brief-inline.md > c2-sonnet.out.md 2> c2-sonnet.err
echo "c2 done"
