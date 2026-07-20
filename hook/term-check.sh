#!/usr/bin/env bash
# term-check.sh — the coin-time hook, v1 (ENTRY.md §4.2, trigger T1).
#
# Given a term and the files that use it, assemble the paragraphs that contain
# the term (nothing else), and ask an ISOLATED model call the reverse-dictionary
# question: what is this concept called, which fields own it, and what are the
# oldest treatments you would expect? Candidates are appended to term-flags.md,
# every one labeled UNVERIFIED.
#
# The two rules that make this a measurement instrument rather than a gadget:
#   1. Information boundary: the check call receives the frozen usage excerpts
#      ONLY — no project conclusions, no candidate owners, no session context.
#      A check call that knows your candidates is a verification call, not a
#      naming call (it will anchor on them).
#   2. Isolation: each draw runs with a fresh cwd and a fresh HOME containing
#      only the CLI credential file — no settings, no CLAUDE.md, no memory.
#      Your own global config carries your project's vocabulary and would leak
#      it into the draw. All tools are disallowed: the draw answers from
#      weights, so a hit means "the field's name for this is model-recoverable
#      from the usage alone."
#
# usage:
#   term-check.sh [options] <term> <file> [file...]
#     -m MODELS      comma-separated model list        (default: sonnet,opus)
#     -o OUTFILE     flags file to append to           (default: ./term-flags.md)
#     --trigger T    provenance label for the log      (default: manual)
#     --dry-run      assemble excerpts + prompt, print, run nothing
#     --max-words N  excerpt budget in words           (default: 2500)
#
# state:  .term-check/  (log.jsonl, seen-terms.txt, manifests/, prompts/)
# env:    TERM_CHECK_STATE  overrides the state dir location
set -euo pipefail

models="sonnet,opus"; outfile="./term-flags.md"; trigger="manual"
dry_run=0; max_words=2500
while [[ $# -gt 0 ]]; do
  case "$1" in
    -m) models="$2"; shift 2;;
    -o) outfile="$2"; shift 2;;
    --trigger) trigger="$2"; shift 2;;
    --dry-run) dry_run=1; shift;;
    --max-words) max_words="$2"; shift 2;;
    -h|--help) sed -n '2,31p' "$0"; exit 0;;
    --) shift; break;;
    -*) echo "unknown option: $1" >&2; exit 2;;
    *) break;;
  esac
done
term="${1:?usage: term-check.sh [options] <term> <file> [file...]}"; shift
[[ $# -ge 1 ]] || { echo "at least one source file required" >&2; exit 2; }
for f in "$@"; do [[ -r "$f" ]] || { echo "cannot read: $f" >&2; exit 2; }; done
src_files="$*"

state="${TERM_CHECK_STATE:-.term-check}"
mkdir -p "$state/manifests" "$state/prompts"
state="$(cd "$state" && pwd)"   # absolute: draw subshells cd away from here
ts="$(date -u +%Y%m%dT%H%M%SZ)"

# Portable helpers (stock macOS has shasum + BSD date, and no coreutils timeout).
sha() { { command -v sha256sum >/dev/null 2>&1 && sha256sum "$1" || shasum -a 256 "$1"; } | cut -d' ' -f1; }
iso_now() { date -u +%Y-%m-%dT%H:%M:%SZ; }
if command -v timeout >/dev/null 2>&1; then timeout_bin="timeout"
elif command -v gtimeout >/dev/null 2>&1; then timeout_bin="gtimeout"
else timeout_bin=""; fi
runto() { if [[ -n "$timeout_bin" ]]; then "$timeout_bin" 300 "$@"; else "$@"; fi; }
slug="$(echo "$term" | tr '[:upper:] ' '[:lower:]-' | tr -cd 'a-z0-9-')"

# --- 1. Excerpt assembly: paragraphs (blank-line separated) that contain the
# term, case-insensitive fixed-string match, from the given files only, capped
# at the word budget. This is the whole information boundary: nothing but these
# paragraphs reaches the check call.
excerpts="$state/prompts/$ts-$slug-excerpts.txt"
stats="$(mktemp)"
awk -v term="$term" -v maxw="$max_words" -v statsf="$stats" '
  BEGIN { RS=""; lt = tolower(term) }
  {
    if (index(tolower($0), lt) == 0) next
    if (total + NF > maxw) { truncated = 1; exit }
    print "[source: " FILENAME "]"
    print $0
    print ""
    total += NF; count++
  }
  END { printf "%d %d %d\n", count, total, truncated + 0 > statsf }' "$@" > "$excerpts"
read -r para_count total_words truncated < "$stats"; rm -f "$stats"
if (( para_count == 0 )); then
  echo "term-check: no paragraph in the given files contains \"$term\" — nothing to check." >&2
  exit 1
fi

# --- 2. The reverse-dictionary prompt (Pass-A form: ask what the concept IS
# CALLED and who owns it — never "find prior art on X", which invites a null).
prompt="$state/prompts/$ts-$slug-prompt.txt"
cat > "$prompt" <<EOF
You are given excerpts from a working document that repeatedly use the term "$term". The term may be a local coinage — a name this project made up for something that established fields already treat under a different name. From the usage in the excerpts alone:

1. Restate in one or two sentences, in plain domain-neutral language, what the term appears to denote. Do not reuse the term itself in the restatement.
2. What is this concept called in established fields? List the closest existing terms of art (up to 5), each with the field that owns it.
3. For each candidate, name the oldest treatments or classic references you would expect to exist (author, venue, or decade is enough; exact citations are not required, and do not fabricate any).
4. Say how well the concept, as used in the excerpts, is already covered by the best candidate — and what about this usage, if anything, does not fit any of them.

Answer from general knowledge. Be specific about fields and their canonical vocabulary; do not pad the list. If the excerpts underdetermine the concept, say what is missing instead of guessing.

EXCERPTS ($para_count paragraphs):

$(cat "$excerpts")
EOF
prompt_sha="$(sha "$prompt")"

if (( dry_run )); then
  echo "--- DRY RUN: prompt ($total_words excerpt words, $para_count paragraphs, truncated=$truncated, sha256=$prompt_sha)"
  cat "$prompt"
  exit 0
fi

# --- 3. Isolated draws. Fresh cwd + fresh HOME containing only the credential
# file (macOS: if ~/.claude/.credentials.json does not exist, Keychain auth is
# assumed and the fresh HOME ships empty). Tools disallowed; 300s timeout.
disallowed="Bash,Read,Edit,Write,Glob,Grep,Task,Agent,WebFetch,WebSearch,NotebookEdit,TodoWrite,Skill"
draw_status=""; draw_latency=0
run_isolated_draw() { # args: model out_file manifest_file
  local model="$1" out="$2" manifest="$3" t0 t1 status cred_policy
  local tmp_cwd tmp_home
  tmp_cwd="$(mktemp -d)"; tmp_home="$(mktemp -d)"
  mkdir -p "$tmp_home/.claude"
  if [[ -f "$HOME/.claude/.credentials.json" ]]; then
    cp "$HOME/.claude/.credentials.json" "$tmp_home/.claude/.credentials.json"
    cred_policy="credentials file only"
  else
    cred_policy="no credentials.json found (macOS Keychain auth assumed)"
  fi
  {
    echo "term: $term"
    echo "model: $model"
    echo "trigger: $trigger"
    echo "prompt_sha256: $prompt_sha"
    echo "source_files: $src_files"
    echo "tmp_cwd: fresh mktemp -d, removed after run"
    echo "tmp_home_policy: $cred_policy (no settings/CLAUDE.md/memory)"
    echo "cwd_listing_before: [$(ls -A "$tmp_cwd" | tr '\n' ' ')] (must be empty)"
    echo "cmd: HOME=<fresh> CLAUDE_CONFIG_DIR=<fresh>/.claude claude -p --model $model --disallowedTools <all>"
    if [[ -n "$timeout_bin" ]]; then echo "timeout: 300s via $timeout_bin"; else echo "timeout: NONE (no timeout binary found)"; fi
    echo "date: $(iso_now)"
  } > "$manifest"
  t0=$(date +%s); status=ok
  # CLAUDE_CONFIG_DIR is pinned to the fresh home explicitly: if the caller has
  # it exported, the CLI would otherwise read the caller's REAL config from it,
  # silently bypassing the fresh-HOME isolation (adversarial-review finding).
  ( cd "$tmp_cwd" && HOME="$tmp_home" CLAUDE_CONFIG_DIR="$tmp_home/.claude" \
      runto claude -p --model "$model" \
      --disallowedTools "$disallowed" < "$prompt" > "$out" 2>"$out.err" ) || status="error:$?"
  t1=$(date +%s)
  echo "out_sha256: $(sha "$out")" >> "$manifest"
  echo "status: $status  latency_s: $((t1-t0))" >> "$manifest"
  rm -rf "$tmp_cwd" "$tmp_home"
  draw_status="$status"; draw_latency=$((t1-t0))
}

# --- 4. Flag output + instrumentation (one JSONL row per draw: without the
# log this is a gadget; with it, flags/day and flag precision are measurable).
flag_tmp="$(mktemp)"
{
  echo "## \`$term\` — flagged $ts (trigger: $trigger)"
  echo
  echo "- Source files: $src_files"
  echo "- Excerpts: $para_count paragraphs, $total_words words$( ((truncated)) && echo ' (TRUNCATED at budget)'; true ); prompt sha256 \`$prompt_sha\`"
  echo "- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on."
  echo
} >> "$flag_tmp"

overall_status="ok"
for model in ${models//,/ }; do
  out="$state/prompts/$ts-$slug-$model.out"
  manifest="$state/manifests/$ts-$slug-$model.txt"
  echo "term-check: drawing $model (isolated, weights-only)..." >&2
  run_isolated_draw "$model" "$out" "$manifest"
  [[ "$draw_status" == ok ]] || overall_status="$draw_status"
  {
    echo "### Draw: $model (status: $draw_status, ${draw_latency}s; manifest: $manifest)"
    echo
    if [[ "$draw_status" == ok ]]; then cat "$out"; else echo "_draw failed; see $out.err_"; fi
    echo
  } >> "$flag_tmp"
  printf '{"ts":"%s","term":"%s","trigger":"%s","model":"%s","event":"draw","status":"%s","latency_s":%s,"prompt_sha256":"%s","files":"%s"}\n' \
    "$ts" "$term" "$trigger" "$model" "$draw_status" "$draw_latency" "$prompt_sha" "$src_files" >> "$state/log.jsonl"
done

cat "$flag_tmp" >> "$outfile"; rm -f "$flag_tmp"
grep -qxF "$(echo "$term" | tr '[:upper:]' '[:lower:]')" "$state/seen-terms.txt" 2>/dev/null \
  || echo "$term" | tr '[:upper:]' '[:lower:]' >> "$state/seen-terms.txt"

echo "term-check: flag appended to $outfile (status: $overall_status). Candidates are UNVERIFIED until you open a primary." >&2
[[ "$overall_status" == ok ]]
