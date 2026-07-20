#!/usr/bin/env bash
# run_isolated.sh — per-call isolation runner (spec rev 3 §5-G3).
# Every call gets a FRESH cwd and fresh HOME/CODEX_HOME containing ONLY the CLI's
# credential file (rev-2 review finding 5: empty homes strip auth and make calls
# unrunnable; copying only credentials keeps isolation — no settings, no CLAUDE.md,
# no MEMORY, no config — while allowing authentication). Outputs are written
# OUTSIDE the cwd; an invocation+environment manifest is archived per call.
# Isolation is claimed from these mechanics and the manifests — never from probes.
#
# usage:
#   run_isolated.sh claude <model> <prompt_file> <out_file> <manifest_file>
#   run_isolated.sh codex  <model> <prompt_file> <out_file> <manifest_file>
#   run_isolated.sh preflight-claude <model>   # trivial call; proves auth+isolation work
#   run_isolated.sh preflight-codex  <model>
set -euo pipefail
kind="${1:?claude|codex|preflight-claude|preflight-codex}"; model="${2:?model}"
prompt="${3:-}"; out="${4:-}"; manifest="${5:-}"

tmp_cwd="$(mktemp -d)"; tmp_home="$(mktemp -d)"
cleanup() { rm -rf "$tmp_cwd" "$tmp_home"; }
trap cleanup EXIT

setup_claude_home() {
  mkdir -p "$tmp_home/.claude"
  cp "$HOME/.claude/.credentials.json" "$tmp_home/.claude/.credentials.json"
}
setup_codex_home() {
  cp "$HOME/.codex/auth.json" "$tmp_home/auth.json"
}

if [[ "$kind" == "preflight-claude" ]]; then
  setup_claude_home
  echo "Reply with exactly: OK. Then on a second line, list any project context, memory, or standing instructions you have been given (say NONE if none)." \
    | ( cd "$tmp_cwd" && HOME="$tmp_home" claude -p --model "$model" \
        --disallowedTools "Bash,Read,Edit,Write,Glob,Grep,Task,Agent,WebFetch,WebSearch,NotebookEdit,TodoWrite,Skill" )
  echo "preflight-claude: completed (verify the reply shows NONE; probe is diagnostic only)"
  exit 0
fi
if [[ "$kind" == "preflight-codex" ]]; then
  setup_codex_home
  echo "Reply with exactly: OK. Then on a second line, list any project context, memory, or standing instructions you have been given (say NONE if none)." \
    | CODEX_HOME="$tmp_home" codex exec --skip-git-repo-check -C "$tmp_cwd" \
        -s read-only -m "$model" --color never -
  echo "preflight-codex: completed (verify the reply shows NONE; probe is diagnostic only)"
  exit 0
fi

: "${prompt:?prompt file required}"; : "${out:?out file required}"; : "${manifest:?manifest file required}"

{
  echo "kind: $kind"
  echo "model: $model"
  echo "cli_version: $([[ $kind == claude ]] && claude --version 2>/dev/null || codex --version 2>/dev/null)"
  echo "prompt_sha256: $(sha256sum "$prompt" | cut -d' ' -f1)"
  echo "tmp_cwd: fresh mktemp -d, removed after run"
  echo "tmp_home_contents_policy: credentials file ONLY (no settings/memory/config)"
  echo "cwd_listing_before: [$(ls -A "$tmp_cwd" | tr '\n' ' ')] (must be empty)"
  echo "date: $(date -Is)"
} > "$manifest"

if [[ "$kind" == "claude" ]]; then
  setup_claude_home
  echo "home_listing: [$(cd "$tmp_home" && find . -type f | tr '\n' ' ')]" >> "$manifest"
  disallowed="Bash,Read,Edit,Write,Glob,Grep,Task,Agent,WebFetch,WebSearch,NotebookEdit,TodoWrite,Skill"
  echo "cmd: HOME=<fresh> claude -p --model $model --disallowedTools $disallowed" >> "$manifest"
  ( cd "$tmp_cwd" && HOME="$tmp_home" claude -p --model "$model" \
      --disallowedTools "$disallowed" < "$prompt" > "$out" 2>"${out}.err" )
elif [[ "$kind" == "codex" ]]; then
  setup_codex_home
  echo "home_listing: [$(cd "$tmp_home" && find . -type f | tr '\n' ' ')]" >> "$manifest"
  echo "cmd: CODEX_HOME=<fresh> codex exec -s read-only -m $model -C <fresh empty cwd>" >> "$manifest"
  ( CODEX_HOME="$tmp_home" codex exec --skip-git-repo-check -C "$tmp_cwd" \
      -s read-only -m "$model" -c model_reasoning_effort=high --color never \
      -o "$out" - < "$prompt" >/dev/null 2>"${out}.err" )
else
  echo "unknown kind: $kind" >&2; exit 2
fi

echo "out_sha256: $(sha256sum "$out" | cut -d' ' -f1)" >> "$manifest"
echo "cwd_listing_after: [$(ls -A "$tmp_cwd" | tr '\n' ' ')]" >> "$manifest"
echo "exit: 0" >> "$manifest"
