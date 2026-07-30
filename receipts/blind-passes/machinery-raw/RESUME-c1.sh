#!/usr/bin/env bash
set -euo pipefail
cd /tmp/claude-1000/-mnt-f-hub/4611a506-d944-4aff-9b44-66148b1dd8af/scratchpad
# TRULY blind: Read/Glob/Grep blocked so the run CANNOT open <vault>/_dashboard.md
# even though user-level ~/.claude/CLAUDE.md instructs it to at session start.
claude -p --model opus \
  --allowedTools "WebSearch,Bash(safefetch:*)" \
  --disallowedTools "Read,Glob,Grep,Task,Agent,Edit,Write" \
  < machinery-brief-inline.md > c1-opus.out.md 2> c1-opus.err
echo "c1 done"
