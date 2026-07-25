#!/usr/bin/env bash
# run_calls.sh — v0.8: executes one staged calls tsv via the e2e isolation runner.
# Sequential, NO automatic retry (§7; the §1 gate state machine is the only retry policy).
# On call failure the (possibly partial) output file is DELETED (§9-F4 no-stale-output
# rule) and the script continues; exits nonzero at the end if any call failed, so the
# driver/gates must route every failure — unresolved failures never pass silently.
# tsv format per row: kind \t model \t prompt \t out \t manifest
# Exit codes (v0.9 round-2 F4): 0 = clean; 1 = ordinary model-call failure(s), routed by
# the gates per §1/§9-F4/§4; 2 = run-scoped harness fault (missing runner, or EVERY staged
# call failing — the systemic signature) which must HALT the run for repair, never become
# a pair verdict.
set -uo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
RUN="$BASE/../e2e-cell/run_isolated.sh"
tsv="${1:?path to calls tsv}"
[ -x "$RUN" ] || { echo "RUN-SCOPED FAULT: isolation runner missing/unexecutable at $RUN"; exit 2; }

# A call is COMPLETED iff its manifest records a clean exit AND the output hash matches
# (round-3 F2: [ -s out ] alone could accept a truncated output after an interrupt).
completed() { # $1=out $2=manifest
  [ -s "$1" ] && [ -f "$2" ] || return 1
  grep -q '^exit: 0$' "$2" || return 1
  local want got
  want="$(grep -E '^out_sha256: [0-9a-f]{64}$' "$2" | head -1 | cut -d' ' -f2)"
  [ -n "$want" ] || return 1
  got="$(sha256sum "$1" | cut -d' ' -f1)"
  [ "$want" = "$got" ]
}

fails=0
attempted=0
[ -s "$tsv" ] || { echo "no calls in $tsv"; exit 0; }
while IFS=$'\t' read -r kind model prompt out manifest; do
  [ -n "$kind" ] || continue
  if completed "$out" "$manifest"; then echo "SKIP (completed): $out"; continue; fi
  # v0.10 hardening: a manifest recording a clean exit whose output hash NO LONGER matches is
  # a completed-call CORRUPTION/TAMPERING fault — NOT an interruption. Never delete-and-retry
  # (that would change the model draw and could silently alter a sealed-run result); HALT.
  if [ -f "$manifest" ] && grep -q '^exit: 0$' "$manifest" && [ -e "$out" ]; then
    echo "RUN-HALT: completed-call output hash mismatch (corruption/tampering) for $out"; exit 2
  fi
  # manifest without output = the call ran and FAILED (we deleted the output);
  # re-running it here would be an unauthorized retry — the gates route it (§1/§9-F4).
  if [ -f "$manifest" ] && [ ! -e "$out" ]; then
    echo "SKIP (attempted+failed, routed by gates): $out"; continue
  fi
  # any other leftover = interrupted mid-call -> re-execute as a logged §4 run-scoped fault
  if [ -f "$manifest" ] || [ -e "$out" ]; then
    echo "RE-EXEC (interrupted call — §4 run-scoped, logged): $out"
    rm -f "$out" "$manifest"
  fi
  echo ">> $kind $model $(basename "$prompt")"
  attempted=$((attempted+1))
  if ! "$RUN" "$kind" "$model" "$prompt" "$out" "$manifest"; then
    echo "CALL FAILED: $prompt (output deleted)"
    rm -f "$out"
    fails=$((fails+1))
  fi
done < "$tsv"
echo "tsv done ($tsv), failures: $fails/$attempted"
if [ "$attempted" -gt 1 ] && [ "$fails" -eq "$attempted" ]; then
  echo "RUN-SCOPED FAULT: every attempted call failed — systemic, halting for repair (§4)"
  exit 2
fi
[ "$fails" -eq 0 ] || exit 1
