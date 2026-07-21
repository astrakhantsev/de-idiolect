#!/usr/bin/env bash
# run_cell.sh — component 3: cross-side definition-mediated matching (ENTRY §4.1 stage 2-3,
# §5.5 output shape) on the collider corpus. New code, kept in demo-collider/ (term-check.sh
# and term-scan.sh are unchanged); same receipts standard — every draw is isolated and writes
# a manifest with prompt/output hashes.
#
# TWO STAGES, both live, both isolated (fresh cwd + credentials-only HOME + pinned
# CLAUDE_CONFIG_DIR + all tools disallowed — so the caller's global CLAUDE.md/memory, which
# carry this project's "vocabulary seam / dependence" framing, cannot leak the answer):
#   define  — per concept, sonnet: a community-neutral constrained definition from that
#             concept's frozen usage excerpt ONLY (no names of people/methods/fields/objects).
#   verify  — per CELL, sonnet+opus: given the two concepts' raw USAGE excerpts (blind, unlabeled,
#             not told they share a case or which is "theory"/"bounds"), decide whether they share
#             a core premise; emit the three artifacts (typed SKOS relation, shared core, per-side
#             residues). Usage-based, NOT definition-vs-definition (§5.5: two defs through one
#             wordlist resemble by construction — a false-positive risk).
#
# Cells (excerpts/ carry the provenance header, stripped before it reaches any draw):
#   cell1  A1 accretion-growth mechanism (theory)  x  B1 white-dwarf survival bound (bounds)
#          -> ANSWER KEY: dependent. G&M derive B1 from A1; §4.1 even forward-references it.
#   cell2  A2 Hawking-evaporation/decay (theory)   x  B2 cosmic-ray survival (bounds)
#          -> ANSWER KEY: NOT a shared premise. Complementary safety arguments (decay OR stopped);
#             discrimination control against over-merging "both about safety" into "shared core".
set -euo pipefail
cd "$(dirname "$0")"                    # demo-collider/cross-side
EX=excerpts
RUNS=runs
mkdir -p "$RUNS/manifests" "$RUNS/prompts"
RUNS="$(cd "$RUNS" && pwd)"   # absolute: draws cd into a temp cwd, so prompt/out paths must not be relative
ts="$(date -u +%Y%m%dT%H%M%SZ)"

sha() { { command -v sha256sum >/dev/null 2>&1 && sha256sum "$1" || shasum -a 256 "$1"; } | cut -d' ' -f1; }
iso_now() { date -u +%Y-%m-%dT%H:%M:%SZ; }
if command -v timeout >/dev/null 2>&1; then TO="timeout 300"; elif command -v gtimeout >/dev/null 2>&1; then TO="gtimeout 300"; else TO=""; fi
# --disallowedTools is a DENYLIST, so it cannot be exhaustive against future tools.
# Blindness here does NOT rest on it being exhaustive: it rests on the no-access
# ENVIRONMENT (fresh HOME with only credentials, an empty temp cwd, no MCP configured),
# in which the draw has nothing external to read regardless of which tools nominally
# exist. The denylist still covers every tool that could reach the vault or the web
# (Bash/Read/Edit/Write/Glob/Grep/Task/Agent/WebFetch/WebSearch/NotebookEdit), plus the
# interactive/scheduling tools an adversarial review flagged, for defence in depth.
DISALLOW="Bash,Read,Edit,Write,Glob,Grep,Task,Agent,WebFetch,WebSearch,NotebookEdit,TodoWrite,Skill,AskUserQuestion,SendUserMessage,EnterPlanMode,ExitPlanMode,CronCreate,CronDelete,CronList,TaskCreate,TaskUpdate,TaskList,Monitor,TeamCreate,TeamDelete"
DRAWS_FAILED=0

# strip the bracketed provenance header line(s) — they name paper/section/side.
body() { grep -v '^\[' "$1"; }

run_draw() { # model  prompt_file  label
  local model="$1" prompt="$2" label="$3"
  local out="$RUNS/prompts/$ts-$label-$model.out"
  local manifest="$RUNS/manifests/$ts-$label-$model.txt"
  local tmp_cwd tmp_home cred rc=0
  # Pin the temp base to the system tmp: mktemp otherwise honours $TMPDIR, which could
  # point into a project tree whose ancestor CLAUDE.md the CLI would auto-discover from
  # the draw's cwd (fresh HOME removes the *global* CLAUDE.md but not a cwd-ancestor one).
  # /tmp has no CLAUDE.md ancestor on a standard system (same assumption term-check.sh makes).
  tmp_cwd="$(TMPDIR=/tmp mktemp -d)"; tmp_home="$(TMPDIR=/tmp mktemp -d)"; mkdir -p "$tmp_home/.claude"
  if [[ -f "$HOME/.claude/.credentials.json" ]]; then
    cp "$HOME/.claude/.credentials.json" "$tmp_home/.claude/.credentials.json"; cred="credentials file only"
  else cred="no credentials.json (macOS Keychain assumed)"; fi
  {
    echo "label: $label"; echo "model: $model"; echo "prompt_sha256: $(sha "$prompt")"
    echo "tmp_home_policy: $cred (no settings/CLAUDE.md/memory)"
    echo "cwd_listing_before: [$(ls -A "$tmp_cwd" | tr '\n' ' ')] (must be empty)"
    echo "cmd: HOME=<fresh> CLAUDE_CONFIG_DIR=<fresh>/.claude claude -p --model $model --disallowedTools <all>"
    echo "date: $(iso_now)"
  } > "$manifest"
  echo "run_cell: drawing $label / $model (isolated)..." >&2
  ( cd "$tmp_cwd" && HOME="$tmp_home" CLAUDE_CONFIG_DIR="$tmp_home/.claude" \
      $TO claude -p --model "$model" --disallowedTools "$DISALLOW" < "$prompt" > "$out" 2>"$out.err" ) \
    || rc=$?
  echo "out_sha256: $(sha "$out")" >> "$manifest"
  if [[ "$rc" -eq 0 && -s "$out" ]]; then
    echo "status: ok" >> "$manifest"
  else
    # A failed/empty draw must NOT masquerade as a real receipt (redirection already
    # created $out): record the failure and count it so the script exits nonzero.
    echo "status: FAILED (rc=$rc, empty=$([[ -s "$out" ]] && echo no || echo yes))" >> "$manifest"
    echo "run_cell: draw $label/$model FAILED (rc=$rc; see $out.err) — receipt is not valid" >&2
    DRAWS_FAILED=$((DRAWS_FAILED+1))
  fi
  rm -rf "$tmp_cwd" "$tmp_home"
}

# ---------------- DEFINE stage ----------------
define_prompt() { # excerpt_file  -> prompt on stdout
  cat <<EOF
Below is an excerpt from a technical document that repeatedly uses one central concept. From the excerpt ALONE, write a short, self-contained, operational definition of that concept: what kind of thing it is, its inputs and outputs, what it asserts, and when it applies.

Hard constraints:
- Use only ordinary, domain-neutral words and simple notation.
- Do NOT use any proper nouns: no names of people, methods, theories, fields, instruments, or specific physical objects. Describe roles generically (e.g. "a compact heavy object", "a surrounding medium"), not by name.
- Two to four sentences. Do not restate these instructions.

EXCERPT:

$(body "$1")
EOF
}

for c in A1-accretion-mechanism B1-wd-survival-bound A2-hawking-decay B2-cosmic-ray-survival; do
  p="$RUNS/prompts/$ts-define-$c.prompt"
  define_prompt "$EX/$c.txt" > "$p"
  run_draw sonnet "$p" "define-$c"
done

# ---------------- VERIFY stage ----------------
verify_prompt() { # excerpt1  excerpt2  -> prompt on stdout
  cat <<EOF
Below are two passages, PASSAGE 1 and PASSAGE 2, each taken from an unspecified technical document. Each describes a concept or argument. They may or may not be related.

Your task is to judge whether the two concepts share a COMMON CORE PREMISE: a single underlying assumption, quantity, or mechanism that BOTH depend on, such that if that premise were wrong, both would be affected. Do not treat mere topical similarity ("both are about safety", "both mention the same kind of object") as a shared core premise.

Answer with exactly these four labelled parts:
1. CORE OF EACH: one sentence restating the core of PASSAGE 1, and one for PASSAGE 2, in neutral terms.
2. SHARED CORE: Is there a single premise/mechanism both depend on? If yes, name it precisely and explain how each passage relies on it. If no, say "NONE" and explain why they are independent (e.g. complementary or alternative arguments).
3. RELATION: classify using one of these labels verbatim — exactMatch, broadMatch, narrowMatch, relatedMatch, or NO-MATCH. If broadMatch/narrowMatch, state which passage is the narrower one. (relatedMatch = associated but neither contains the other and they share no load-bearing premise; NO-MATCH = essentially unrelated.)
4. PER-SIDE RESIDUE: what is specific to PASSAGE 1 that PASSAGE 2 does not share, and vice versa.

"NONE / NO-MATCH / relatedMatch" are fully acceptable answers — many pairs genuinely do not share a core. Judge only from the two passages.

PASSAGE 1:

$(body "$1")

PASSAGE 2:

$(body "$2")
EOF
}

verify_cell() { # label  excerpt1  excerpt2
  local p="$RUNS/prompts/$ts-verify-$1.prompt"
  verify_prompt "$EX/$2.txt" "$EX/$3.txt" > "$p"
  run_draw sonnet "$p" "verify-$1"
  run_draw opus   "$p" "verify-$1"
}

verify_cell cell1 A1-accretion-mechanism B1-wd-survival-bound
verify_cell cell2 A2-hawking-decay        B2-cosmic-ray-survival

if [[ "$DRAWS_FAILED" -gt 0 ]]; then
  echo "=== run_cell: $DRAWS_FAILED draw(s) FAILED — the run is INCOMPLETE, do not treat its receipts as valid ===" >&2
  exit 1
fi
echo "=== run_cell done (all draws ok). outputs in $RUNS/prompts/, manifests in $RUNS/manifests/ ===" >&2
