#!/usr/bin/env bash
# term-scan.sh — scan mode for the coin-time hook (ENTRY.md §4.1 stage 1 + §4.2,
# batch form). v1, post-submission addition (2026-07-20).
#
# term-check.sh checks ONE term you already know is a coinage. On a project with
# no glossary, neither trigger (T1 manual, T2 glossary-watch) has anything to
# fire on. term-scan closes that gap: point it at a project's prose and it
# surfaces the ~15 most project-local coined terms, then — on the ones you keep —
# runs the existing per-term check and assembles a seed glossary. Detect → seed →
# (glossary-watch can now watch the seed). It is the entry's detection stage
# (§4.1 stage 1) turned inward and batched.
#
# TWO PHASES, and the gate between them is mandatory:
#   Phase 1 (detect)  ONE model call over the project's prose returns candidate
#                     coinages. Writes scan-candidates.md and STOPS for curation.
#                     Never spends a naming draw. (--top N auto-keeps the top N.)
#   Phase 2 (check)   --check reads the curated file and runs term-check.sh on the
#                     terms you marked [x] — and only those, and only if the term
#                     actually appears in the source files. Assembles GLOSSARY-SEED.md.
#
# WHY THE GATE: surfacing is heuristic. A weak candidate that silently burned a
# naming draw would waste calls and credibility; a judge who got junk in the seed
# glossary would walk away worse than with no scan mode. So phase 1 costs one
# detection call and stops; nothing names anything until you say which terms.
#
# ISOLATION, AND WHAT IT DOES AND DOES NOT BUY HERE. The detection call MAY see
# project files wholesale — the C2 information boundary (excerpts only, no
# candidate owners) binds the per-term NAMING call in term-check.sh, not
# detection. But detection still runs through the same isolation mechanics (fresh
# cwd + fresh HOME with credentials only, CLAUDE_CONFIG_DIR pinned to it, all
# tools disallowed) so your own global config (CLAUDE.md, memory) cannot steer
# which terms it surfaces. This is isolation-FROM-config, not blindness-to-project.
#
# REUSE (composition over modification): phase 2 calls term-check.sh as a
# subprocess, so every naming draw inherits ALL of its reviewed isolation
# unchanged. term-check.sh is a runnable script, not a sourceable library (it
# would execute on `source`), so the ~15 lines of isolation mechanics for the
# single detection call are duplicated here rather than sourced. term-check.sh is
# not modified.
#
# usage:
#   term-scan.sh [options] [path...]                 # phase 1 (detect), then STOP
#   term-scan.sh --top N [options] [path...]         # phase 1 + auto-keep top N + phase 2
#   term-scan.sh --check [options] [path...]         # phase 2 on the curated candidates
#     paths                 files/dirs to scan                 (default: .)
#     --include GLOBS       comma-sep filename globs to include (default: *.md,*.txt,*.rst)
#     --exclude GLOBS       comma-sep path/name globs to exclude (added to defaults)
#     --max-words N         detection input word cap            (default: 18000)
#     --max-terms N         cap on terms checked in phase 2     (default: 10)
#     --top N               keep the top N candidates and run phase 2 in one shot
#     --check               run phase 2 only (read curated candidates)
#     --detect-model M      model for the detection call        (default: sonnet)
#     -m MODELS             phase-2 models (passed to term-check.sh) (default: sonnet)
#     -o OUTFILE            seed glossary to write               (default: ./GLOSSARY-SEED.md)
#     --candidates FILE     phase-1 candidate list / phase-2 input (default: ./scan-candidates.md)
#     --flags FILE          verbose per-draw flags file          (default: ./term-flags.md)
#     --dry-run             assemble detection input + prompt, print, run nothing
#
# default excludes always applied: dotdirs, GLOSSARY*/glossary*, 99_private/, and
# the scan's own output files.
#
# state:  .term-check/ (shared with term-check.sh; scan receipts under scan/)
# env:    TERM_CHECK_STATE  overrides the state dir; TERM_CHECK_BIN  path to term-check.sh
set -euo pipefail

includes="*.md,*.txt,*.rst"; user_excludes=""
max_words=18000; max_terms=10; top=""; check_mode=0
detect_model="sonnet"; check_models="sonnet"
outfile="./GLOSSARY-SEED.md"; candidates="./scan-candidates.md"; flagsfile="./term-flags.md"
dry_run=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --include) includes="$2"; shift 2;;
    --exclude) user_excludes="$2"; shift 2;;
    --max-words) max_words="$2"; shift 2;;
    --max-terms) max_terms="$2"; shift 2;;
    --top) top="$2"; shift 2;;
    --check) check_mode=1; shift;;
    --detect-model) detect_model="$2"; shift 2;;
    -m) check_models="$2"; shift 2;;
    -o) outfile="$2"; shift 2;;
    --candidates) candidates="$2"; shift 2;;
    --flags) flagsfile="$2"; shift 2;;
    --dry-run) dry_run=1; shift;;
    -h|--help) sed -n '2,63p' "$0"; exit 0;;
    --) shift; break;;
    -*) echo "unknown option: $1" >&2; exit 2;;
    *) break;;
  esac
done
paths=("$@"); [[ ${#paths[@]} -ge 1 ]] || paths=(".")

state="${TERM_CHECK_STATE:-.term-check}"
mkdir -p "$state/scan"
state="$(cd "$state" && pwd)"
scandir="$state/scan"
ts="$(date -u +%Y%m%dT%H%M%SZ)"

# Single-flight per state dir: two concurrent runs sharing an output/state would
# truncate the seed and race on receipt paths. Portable non-blocking mkdir lock
# (no flock dependency); released on any exit. term-check.sh children are
# unaffected — this guards only the scan orchestrator's shared writes.
if mkdir "$state/scan.lock" 2>/dev/null; then
  trap 'rmdir "$state/scan.lock" 2>/dev/null || true' EXIT
else
  echo "term-scan: another run holds $state/scan.lock — exiting (concurrent runs to one state dir corrupt shared output). Remove it if stale." >&2
  exit 1
fi

# Portable helpers (mirrors term-check.sh: stock macOS has shasum + BSD date and
# no coreutils timeout). Duplicated deliberately — see header REUSE note.
sha() { { command -v sha256sum >/dev/null 2>&1 && sha256sum "$1" || shasum -a 256 "$1"; } | cut -d' ' -f1; }
iso_now() { date -u +%Y-%m-%dT%H:%M:%SZ; }
if command -v timeout >/dev/null 2>&1; then timeout_bin="timeout"
elif command -v gtimeout >/dev/null 2>&1; then timeout_bin="gtimeout"
else timeout_bin=""; fi
runto() { if [[ -n "$timeout_bin" ]]; then "$timeout_bin" 300 "$@"; else "$@"; fi; }
disallowed="Bash,Read,Edit,Write,Glob,Grep,Task,Agent,WebFetch,WebSearch,NotebookEdit,TodoWrite,Skill"

# --- File discovery (shared by both phases). Include by basename glob; exclude by
# name-or-path glob (user + defaults) and any dotdir component. Globs are held as
# QUOTED array elements (populated via `read -ra`, never a bare word list) so the
# patterns stay literal instead of pathname-expanding against the cwd. Portable:
# no mapfile/associative arrays (bash 3.2 / stock macOS).
inc_globs=(); IFS=',' read -r -a inc_globs <<< "$includes"
exc_globs=('GLOSSARY*' 'glossary*' '99_private' 'GLOSSARY-SEED.md' 'scan-candidates.md' 'term-flags.md')
exc_globs+=("$(basename "$outfile")" "$(basename "$candidates")" "$(basename "$flagsfile")")
if [[ -n "$user_excludes" ]]; then
  _uex=(); IFS=',' read -r -a _uex <<< "$user_excludes"; exc_globs+=("${_uex[@]}")
fi
exc_display="${exc_globs[*]}"
list_raw() {
  local p
  for p in "$@"; do
    if [[ -f "$p" ]]; then printf '%s\n' "$p"
    elif [[ -d "$p" ]]; then find "$p" -type f 2>/dev/null
    else echo "term-scan: path not found, skipping: $p" >&2; fi
  done
}
discover_files() {  # populates global array `files`
  files=()
  local f base inc ex g
  while IFS= read -r f; do
    [[ -n "$f" ]] || continue
    base="$(basename "$f")"
    inc=0
    for g in "${inc_globs[@]}"; do case "$base" in $g) inc=1; break;; esac; done
    (( inc )) || continue
    case "/$f/" in */.*/*) continue;; esac      # any dotdir in the path
    ex=0
    for g in "${exc_globs[@]}"; do
      [[ -n "$g" ]] || continue
      case "$base" in $g) ex=1; break;; esac
      case "$f"    in $g|*/$g|$g/*|*/$g/*) ex=1; break;; esac
    done
    (( ex )) && continue
    files+=("$f")
  done < <(list_raw "${paths[@]}" | LC_ALL=C sort -u)
}

# ============================================================================
# PHASE 2 — check the curated terms and assemble the seed glossary.
# Split out first so --top can call it after phase 1 in the same run.
# ============================================================================

# Parse ONE per-term flags file (output of term-check.sh, first draw) into a
# compact restatement + candidate string for the seed line. term-check's prompt
# enforces a 1..4 numbered structure and the models render each section under a
# markdown heading (## N. Title). Section boundaries are therefore anchored on
# HEADING lines only — never on prose (the restatement legitimately contains
# phrases like "closest existing equivalents") and never on the candidate list's
# own 1./2./3. numbering (which would otherwise read as section headers). The
# candidate section may come back as a numbered/bulleted list OR a markdown table
# (| Candidate | Field |); both are handled. On any parse miss the seed line
# degrades to a pointer at the verbose flags file, so nothing is silently lost.
parse_restatement() {  # arg: per-term flags file (section 1 -> one-line restatement)
  awk '
    function looks_title(x,  t,nw,a){ t=x; gsub(/[[:space:]]+/," ",t); gsub(/^ | $/,"",t); nw=split(t,a," "); return (index(t,".")==0 && nw<=8) }
    /^### Draw:/ { d++; if (d>1) exit; next }        # first draw only
    d!=1 { next }
    /^#{1,6}[[:space:]]/ {                            # section boundaries only on markdown headings
      h=tolower($0)
      if (h ~ /closest|terms of art|called in established|existing terms/ || $0 ~ /^#{1,6}[[:space:]]*\**[[:space:]]*2[.)]/) { s=0; stop=1; next }
      if (!stop && (h ~ /restate|denote|what the term/ || $0 ~ /^#{1,6}[[:space:]]*\**[[:space:]]*1[.)]/)) {
        s=1; line=$0
        sub(/^#{1,6}[[:space:]]*/,"",line); sub(/^\**[[:space:]]*[0-9]+[.)][[:space:]]*/,"",line)
        gsub(/\*\*/,"",line); gsub(/^[[:space:]]+|[[:space:]]+$/,"",line)
        if (line!="" && !looks_title(line)) lines[++n]=line
      }
      next
    }
    stop { next }
    s && NF { l=$0; gsub(/\*\*/,"",l); gsub(/^[[:space:]]+|[[:space:]]+$/,"",l); if(l!="") lines[++n]=l }
    END {
      out=""
      for(i=1;i<=n;i++) out=(out=="")?lines[i]:out" "lines[i]
      gsub(/[[:space:]]+/," ",out)
      if (length(out)>320) out=substr(out,1,317) "..."
      print out
    }' "$1"
}
parse_candidates() {  # arg: per-term flags file — section 2 items -> "Name (Field); ..."
  awk '
    /^### Draw:/ { d++; if (d>1) exit; next }
    d!=1 { next }
    /^#{1,6}[[:space:]]/ {
      h=tolower($0)
      if (s && (h ~ /oldest|classic|treatment|coverage|fit|assessment|how well|does not fit/ || $0 ~ /^#{1,6}[[:space:]]*\**[[:space:]]*[34][.)]/)) { s=0; stop=1; next }
      if (!s && !stop && (h ~ /closest|terms of art|called in established|existing terms/ || $0 ~ /^#{1,6}[[:space:]]*\**[[:space:]]*2[.)]/)) { s=1; next }
      next
    }
    stop { next }
    s {
      line=$0; item=""
      if (line ~ /^[[:space:]]*\|[-:|[:space:]]*$/) next                                        # table separator row (incl. aligned :---: / ---:)
      if (line ~ /^[[:space:]]*\|/) {                                                           # table row: | name | field | ...
        m=split(line, c, /[[:space:]]*\|[[:space:]]*/); name=c[2]; field=c[3]
        gsub(/\*\*/,"",name); gsub(/`/,"",name); gsub(/^[[:space:]]+|[[:space:]]+$/,"",name)
        gsub(/\*\*/,"",field); gsub(/`/,"",field); gsub(/^[[:space:]]+|[[:space:]]+$/,"",field)
        lf=tolower(field); ln=tolower(name)
        if (lf ~ /^(field|discipline|area|domain|owner|owning field|owning literature)s?$/ || \
            ln ~ /^(candidate( term)?|term( of art)?|concept|name)s?$/) next                     # header row (field-cell/name-cell label)
        sub(/[[:space:]]*\([^()]*\)[[:space:]]*$/,"",name); sub(/[.]+$/,"",field)               # drop trailing gloss paren / period
        if (name!="" && name!="---") item=(field!=""&&field!="---")? name" ("field")" : name
      } else if (line ~ /^[[:space:]]*([-*]|[0-9]+[.)])[[:space:]]/) {                           # list item
        sub(/^[[:space:]]*([-*]|[0-9]+[.)])[[:space:]]*/,"",line)
        gsub(/\*\*/,"",line); gsub(/`/,"",line)
        if (match(line,/[[:space:]]+[—–-][[:space:]]+/)) {                                       # "Name — Field" -> "Name (Field)"
          name=substr(line,1,RSTART-1); field=substr(line,RSTART+RLENGTH)
          gsub(/^[[:space:]]+|[[:space:]]+$/,"",name); gsub(/^[[:space:]]+|[[:space:]]+$/,"",field); sub(/[.]+$/,"",field)
          item=(name!="")?((field!="")? name" ("field")" : name):""
        } else { gsub(/^[[:space:]]+|[[:space:]]+$/,"",line); item=line }
      }
      if (item!="") { out=(out=="")?item:out"; " item }
    }
    END { if (length(out)>400) out=substr(out,1,397) "..."; print out }' "$1"
}

run_phase2() {  # uses global array `kept_terms`; needs discovered `files`
  local termbin term tmpflag real_files nf status seeded rest cands f srcs
  termbin="${TERM_CHECK_BIN:-$(dirname "$0")/term-check.sh}"
  if [[ ! -f "$termbin" ]]; then
    echo "term-scan: term-check.sh not found at $termbin (set TERM_CHECK_BIN)" >&2; exit 2
  fi
  if [[ ${#kept_terms[@]} -eq 0 ]]; then
    echo "term-scan: no terms marked [x] in $candidates — nothing to check." >&2
    echo "  Edit $candidates, change '[ ]' to '[x]' on the terms you want checked, then rerun --check." >&2
    exit 1
  fi
  # --dry-run must reach here too: "run nothing" has to mean no naming draws in
  # phase 2 either. Print the plan (kept terms + their real source files) and stop.
  if (( dry_run )); then
    echo "term-scan: DRY RUN (phase 2) — ${#kept_terms[@]} kept term(s); no naming draws, no files written:" >&2
    for term in "${kept_terms[@]}"; do
      real_files=(); for f in "${files[@]}"; do grep -qiF -- "$term" "$f" 2>/dev/null && real_files+=("$f"); done
      if (( ${#real_files[@]} == 0 )); then echo "  - \"$term\": absent in sources — would SKIP" >&2
      else echo "  - \"$term\": would check ${#real_files[@]} file(s): ${real_files[*]}" >&2; fi
    done
    return 0
  fi
  # Header for the seed glossary (write once).
  {
    echo "# Seed glossary (UNVERIFIED) — generated by term-scan $ts"
    echo
    echo "One entry per curated term. Each restatement and candidate list is a **model proposal from the per-term isolated check, not a verified mapping** — the same UNVERIFIED doctrine as \`term-flags.md\`. Open one primary per candidate you intend to rely on before it enters a real glossary or a claim. Entry format matches \`glossary-watch.py\`'s regex, so this file can itself be watched (scan → seed → watch)."
    echo
  } > "$outfile"

  local checked=0
  for term in "${kept_terms[@]}"; do
    if (( checked >= max_terms )); then
      echo "term-scan: --max-terms=$max_terms reached; NOT checking remaining kept term: $term" >&2
      printf '{"ts":"%s","event":"scan-check","term":"%s","status":"skipped-max-terms"}\n' "$ts" "$term" >> "$state/log.jsonl"
      continue
    fi
    # Re-derive REAL source files by content match — enforces the no-invented-terms
    # rule: a term the detector hallucinated (not literally in the prose) is dropped.
    real_files=()
    for f in "${files[@]}"; do
      if grep -qiF -- "$term" "$f" 2>/dev/null; then real_files+=("$f"); fi
    done
    nf=${#real_files[@]}
    if (( nf == 0 )); then
      echo "term-scan: \"$term\" appears in none of the scanned files — skipping (not checking a term the prose does not contain)." >&2
      printf '{"ts":"%s","event":"scan-check","term":"%s","status":"absent-in-sources","files":0}\n' "$ts" "$term" >> "$state/log.jsonl"
      continue
    fi
    echo "term-scan: checking \"$term\" ($nf source file(s), models: $check_models)..." >&2
    tmpflag="$(mktemp)"
    status=ok
    bash "$termbin" -m "$check_models" -o "$tmpflag" --trigger scan -- "$term" "${real_files[@]}" >&2 || status="error:$?"
    cat "$tmpflag" >> "$flagsfile"
    rest="$(parse_restatement "$tmpflag")"; cands="$(parse_candidates "$tmpflag")"
    rm -f "$tmpflag"
    [[ -n "$rest"  ]] || rest="(could not segment the draw's restatement — see $flagsfile)"
    [[ -n "$cands" ]] || cands="(could not segment the draw's candidate list — see $flagsfile)"
    seeded=false
    srcs="$(printf '%s, ' "${real_files[@]}")"; srcs="${srcs%, }"
    if [[ "$status" == ok ]]; then
      printf -- '- **%s** — %s *Candidates (UNVERIFIED):* %s *Sources:* %s\n' \
        "$term" "$rest" "$cands" "$srcs" >> "$outfile"
      seeded=true
    else
      printf -- '- **%s** — CHECK FAILED (%s); see %s\n' "$term" "$status" "$flagsfile" >> "$outfile"
    fi
    checked=$((checked+1))
    printf '{"ts":"%s","event":"scan-check","term":"%s","status":"%s","files":%s,"models":"%s","seeded":%s}\n' \
      "$ts" "$term" "$status" "$nf" "$check_models" "$seeded" >> "$state/log.jsonl"
  done
  echo "term-scan: seed glossary written to $outfile ($checked term(s) checked). Verbose draws in $flagsfile. Every candidate is UNVERIFIED." >&2
}

# Read [x]-marked terms from a curated candidates file into global `kept_terms`.
read_kept_terms() {
  kept_terms=()
  [[ -f "$candidates" ]] || { echo "term-scan: candidates file not found: $candidates (run phase 1 first)" >&2; exit 2; }
  local line t
  # Anchor the checkbox to the LINE PREFIX (after optional indent): a detector
  # gloss/file field can contain the literal "- [x]", and matching it anywhere
  # would let an unchecked candidate slip through the curation gate. Regex held
  # in a variable (inline [[ =~ ]] mishandles the escaped brackets).
  local checked_re='^[[:space:]]*[-*][[:space:]]+\[[xX]\][[:space:]]'
  while IFS= read -r line; do
    [[ "$line" =~ $checked_re ]] || continue
    # extract the bold term:  - [x] **term** — ...
    t="$(printf '%s\n' "$line" | sed -n 's/^[^*]*\*\*\(.*\)\*\*.*$/\1/p')"
    [[ -n "$t" ]] && kept_terms+=("$t")
  done < "$candidates"
}

# ============================================================================
# --check : phase 2 only
# ============================================================================
if (( check_mode )); then
  discover_files
  read_kept_terms
  run_phase2
  exit 0
fi

# ============================================================================
# PHASE 1 — detect. Assemble (capped, evenly-sampled) input, one isolated draw,
# write candidates + manifest, STOP (or continue to phase 2 under --top).
# ============================================================================
discover_files
if [[ ${#files[@]} -eq 0 ]]; then
  echo "term-scan: no files matched (includes: $includes) under: ${paths[*]}" >&2; exit 1
fi

# Per-file word counts + total (for the manifest and the sampling ratio).
filelist="$scandir/$ts-detect-filelist.txt"
total_words=0
: > "$filelist"
for f in "${files[@]}"; do
  w="$(wc -w < "$f" 2>/dev/null | tr -d ' ')"; w="${w:-0}"
  total_words=$((total_words + w))
  printf '%8d  %s\n' "$w" "$f" >> "$filelist"
done

# Sampling ratio: 1 if within cap, else cap/total. Deterministic even paragraph
# downsampling (Bresenham-style) so coverage is spread across the whole input,
# not truncated to a prefix.
if (( total_words <= max_words )); then ratio="1"; sampling="full (${total_words} words <= cap ${max_words})"
else ratio="$(awk -v c="$max_words" -v t="$total_words" 'BEGIN{printf "%.6f", c/t}')"
     sampling="even paragraph downsample, ratio ${ratio} (input ${total_words} words > cap ${max_words})"; fi

# detect_input is transient: it is assembled here only to be embedded into the
# persisted prompt below, so it lives in a temp and is removed once the prompt is
# built (persisting both would be a ~verbatim duplicate receipt).
detect_input="$(mktemp)"
sstats="$(mktemp)"
awk -v ratio="$ratio" -v maxw="$max_words" -v statsf="$sstats" '
  BEGIN { RS=""; ORS=""; acc=0; kept=0; keptw=0; keptpar=0; paras=0 }
  {
    paras++
    acc += ratio
    if (int(acc) > kept) {                          # selected by even-downsample stride
      kept = int(acc)
      if (keptw == 0 || keptw + NF <= maxw) {       # hard word ceiling (always keep >=1 paragraph)
        print "[source: " FILENAME "]\n" $0 "\n\n"
        keptw += NF; keptpar++
      }
    }
  }
  END { printf "%d %d %d\n", paras, keptpar, keptw > statsf }' "${files[@]}" > "$detect_input"
read -r para_total para_kept words_kept < "$sstats"; rm -f "$sstats"

# The detection prompt: onomasiological direction ("what does THIS project name
# in a local way"), strict presence rule (no invented terms), machine-parseable
# one-line-per-term output.
detect_prompt="$scandir/$ts-detect-prompt.txt"
cat > "$detect_prompt" <<EOF
You are given prose excerpts from a SINGLE project's working documents. Each excerpt is tagged with its source file as [source: <path>].

Task: identify the terms this project uses in a PROJECT-LOCAL way — coinages, or ordinary words given a special local sense — that an outside expert in the relevant field would NOT recognize as this field's established vocabulary. These are the project's idiolect: names it made up (or repurposed) for things established fields usually call something else. Established terms of art are NOT what we want, however technical.

Return the up-to-15 MOST project-local such terms, most-local first. For each term, ALL of:
- it MUST appear verbatim in the excerpts. Do not invent, generalize, translate, or normalize a term that is not literally present in the text.
- a one-line gloss of what it denotes AS USED HERE, in plain language (do not merely repeat the term).
- the source files it appears in, taken from the [source: ...] tags.

Exclude: established terms of art; ordinary English used ordinarily; proper names of people, products, or venues; citations; and section/heading scaffolding.

Output NOTHING but the list — no preamble, no numbering, no trailing commentary, no code fence. One term per line, exactly three fields separated by " | " (space, pipe, space):

<term> | <one-line gloss> | <file1>, <file2>

If fewer than 15 qualify, return fewer. If none qualify, output a single line containing only: NONE

EXCERPTS ($para_kept of $para_total paragraphs, $words_kept words):

$(cat "$detect_input")
EOF
rm -f "$detect_input"                # content is now embedded in the persisted prompt
prompt_sha="$(sha "$detect_prompt")"

# Manifest for phase 1 (files, counts, sampling, prompt hash, model, isolation).
manifest="$scandir/$ts-detect-manifest.txt"
{
  echo "phase: 1 (detect)"
  echo "date: $(iso_now)"
  echo "paths: ${paths[*]}"
  echo "includes: $includes"
  echo "excludes (default+user): $exc_display"
  echo "files_matched: ${#files[@]} (per-file words in $(basename "$filelist"))"
  echo "words_total: $total_words   words_in_prompt: $words_kept   cap: $max_words"
  echo "paragraphs: kept $para_kept of $para_total"
  echo "sampling: $sampling"
  echo "detect_model: $detect_model"
  echo "prompt_sha256: $prompt_sha"
  echo "isolation: fresh cwd + fresh HOME (credentials only) + CLAUDE_CONFIG_DIR pinned + all tools disallowed"
  if [[ -n "$timeout_bin" ]]; then echo "timeout: 300s via $timeout_bin"; else echo "timeout: NONE (no timeout binary found)"; fi
} > "$manifest"

if (( dry_run )); then
  echo "--- DRY RUN: detection prompt ($words_kept words, $para_kept/$para_total paragraphs, sha256=$prompt_sha)"
  echo "--- files (${#files[@]}):"; cat "$filelist"
  echo "--- sampling: $sampling"
  echo "--- prompt follows ---"
  cat "$detect_prompt"
  exit 0
fi

# --- The isolated detection draw. Isolation-from-config (see header): the model
# sees the project prose we pipe in, but NOT the caller's global config.
detect_out="$scandir/$ts-detect.out"
echo "term-scan: detecting coinages over ${#files[@]} file(s), $words_kept words (model: $detect_model, isolated)..." >&2
tmp_cwd="$(mktemp -d)"; tmp_home="$(mktemp -d)"
mkdir -p "$tmp_home/.claude"
if [[ -f "$HOME/.claude/.credentials.json" ]]; then
  cp "$HOME/.claude/.credentials.json" "$tmp_home/.claude/.credentials.json"
  cred_policy="credentials file only"
else
  cred_policy="no credentials.json found (macOS Keychain auth assumed)"
fi
{
  echo "cwd_listing_before: [$(ls -A "$tmp_cwd" | tr '\n' ' ')] (must be empty)"
  echo "tmp_home_policy: $cred_policy (no settings/CLAUDE.md/memory)"
} >> "$manifest"
t0=$(date +%s); detect_status=ok
( cd "$tmp_cwd" && HOME="$tmp_home" CLAUDE_CONFIG_DIR="$tmp_home/.claude" \
    runto claude -p --model "$detect_model" \
    --disallowedTools "$disallowed" < "$detect_prompt" > "$detect_out" 2>"$detect_out.err" ) || detect_status="error:$?"
t1=$(date +%s)
echo "out_sha256: $(sha "$detect_out")" >> "$manifest"
echo "status: $detect_status  latency_s: $((t1-t0))" >> "$manifest"
rm -rf "$tmp_cwd" "$tmp_home"

if [[ "$detect_status" != ok ]]; then
  echo "term-scan: detection draw FAILED ($detect_status); see $detect_out.err" >&2
  printf '{"ts":"%s","event":"scan-detect","status":"%s","detect_model":"%s","files":%s,"words":%s,"prompt_sha256":"%s"}\n' \
    "$ts" "$detect_status" "$detect_model" "${#files[@]}" "$words_kept" "$prompt_sha" >> "$state/log.jsonl"
  exit 1
fi

# --- Parse the detection output into candidates. Robust to stray fences / list
# markers: keep lines with two " | " separators; term=field1, files=last field.
cand_tmp="$(mktemp)"
awk '
  { line=$0
    sub(/^[[:space:]]*([-*]|[0-9]+[.)])[[:space:]]*/,"",line)   # strip list marker
    if (line ~ /^```/) next
    if (index(line," | ")==0) next
    print line
  }' "$detect_out" > "$cand_tmp"
n_cand=$(grep -c . "$cand_tmp" || true)
if grep -qiE '^[[:space:]]*NONE[[:space:]]*$' "$detect_out" && (( n_cand == 0 )); then
  echo "term-scan: detection returned NONE — no project-local coinages surfaced." >&2
fi

# --- Write scan-candidates.md (checklist). --top N pre-marks the first N as [x].
top_n="${top:-0}"
{
  echo "# Scan candidates — $ts"
  echo
  echo "<!-- PHASE 1 of 2 (detect). Heuristic surfacings from one isolated model call over this project's prose — NOT checked mappings. -->"
  echo "<!-- CURATE: mark the terms you want checked by changing \"[ ]\" to \"[x]\". Leave or delete the rest. -->"
  echo "<!-- PHASE 2:  term-scan.sh --check [same -o / --candidates / --flags / path options]  -->"
  echo "<!-- Phase 2 checks ONLY [x]-marked terms (max --max-terms=$max_terms), and only if the term literally appears in the source files. Unchecked terms cost nothing. Detection is heuristic; the per-term check is the product. -->"
  echo "<!-- detect_model=$detect_model  files=${#files[@]}  words=$words_kept  prompt_sha256=$prompt_sha  manifest=$(basename "$manifest") -->"
  echo
  i=0
  while IFS= read -r line; do
    [[ -n "$line" ]] || continue
    # strip ONE layer of paired markdown emphasis only — a literal trailing '*' is
    # part of the coinage (e.g. m*) and must survive, or phase 2 checks a different term.
    term="$(printf '%s\n' "$line" | awk -F' \\| ' '{t=$1; gsub(/^[[:space:]]+|[[:space:]]+$/,"",t); if (sub(/^\*\*/,"",t)) sub(/\*\*$/,"",t); else if (sub(/^\*/,"",t)) sub(/\*$/,"",t); gsub(/`/,"",t); print t}')"
    gloss="$(printf '%s\n' "$line" | awk -F' \\| ' '{gsub(/^[[:space:]]+|[[:space:]]+$/,"",$2); print $2}')"
    fld="$(printf '%s\n' "$line" | awk -F' \\| ' '{f=$NF; gsub(/^[[:space:]]+|[[:space:]]+$/,"",f); print f}')"
    [[ -n "$term" ]] || continue
    i=$((i+1))
    mark="[ ]"; if (( i <= top_n )); then mark="[x]"; fi
    printf -- '- %s **%s** — %s *(files: %s)*\n' "$mark" "$term" "$gloss" "$fld"
  done < "$cand_tmp"
} > "$candidates"
rm -f "$cand_tmp"

printf '{"ts":"%s","event":"scan-detect","status":"ok","detect_model":"%s","files":%s,"words":%s,"words_total":%s,"candidates":%s,"sampling":"%s","prompt_sha256":"%s"}\n' \
  "$ts" "$detect_model" "${#files[@]}" "$words_kept" "$total_words" "$n_cand" "$sampling" "$prompt_sha" >> "$state/log.jsonl"

echo "term-scan: $n_cand candidate(s) written to $candidates (manifest: $manifest)." >&2

# --- The mandatory gate. Without --top, STOP here: no naming draw has run.
if [[ -z "$top" ]]; then
  echo "term-scan: PHASE 1 complete. Curate $candidates (mark [x] the terms to check), then run:" >&2
  echo "    bash $0 --check -o $outfile --candidates $candidates --flags $flagsfile ${paths[*]}" >&2
  exit 0
fi

# --top N: keep the pre-marked terms and run phase 2 now.
read_kept_terms
echo "term-scan: --top $top -> checking ${#kept_terms[@]} auto-kept term(s)." >&2
run_phase2
