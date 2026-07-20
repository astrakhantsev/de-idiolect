#!/usr/bin/env bash
# Executes staged model calls for the peer smoke test via the e2e isolation runner.
# Phases: gen | defs | verify | polarity | decompose  (calls.tsv format: kind model prompt out manifest)
set -uo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
RUN="$BASE/../e2e-cell/run_isolated.sh"
phase="${1:?gen|defs|verify|polarity|decompose}"

run_tsv() {
  local tsv="$1" fails=0
  [ -s "$tsv" ] || { echo "no calls in $tsv"; return 0; }
  while IFS=$'\t' read -r kind model prompt out manifest; do
    [ -n "$kind" ] || continue
    if [ -s "$out" ]; then echo "SKIP (exists): $out"; continue; fi
    echo ">> $kind $model $(basename "$prompt")"
    if ! "$RUN" "$kind" "$model" "$prompt" "$out" "$manifest"; then
      echo "CALL FAILED: $prompt"; fails=$((fails+1))
    fi
  done < "$tsv"
  echo "phase done, failures: $fails"; return 0
}

case "$phase" in
  gen)
    "$RUN" claude sonnet "$BASE/prompts/gen-community-a.md" "$BASE/runs/gen-a.out" "$BASE/runs/manifests/gen-a.json" || echo "gen-a FAILED"
    "$RUN" codex gpt-5.6-terra "$BASE/prompts/gen-community-b.md" "$BASE/runs/gen-b.out" "$BASE/runs/manifests/gen-b.json" || echo "gen-b FAILED"
    ;;
  checklist) run_tsv "$BASE/runs/checklists/calls.tsv" ;;
  defs)      run_tsv "$BASE/runs/definitions/calls.tsv" ;;
  verify)    run_tsv "$BASE/runs/verify/calls.tsv" ;;
  polarity)  run_tsv "$BASE/runs/polarity/calls.tsv" ;;
  decompose) run_tsv "$BASE/runs/decompose/calls.tsv" ;;
  *) echo "unknown phase"; exit 2 ;;
esac
