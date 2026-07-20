#!/usr/bin/env bash
# run_v08.sh — v0.8 TRAIN driver (prereg-v08.md is the authority). Resumable: staged
# calls skip existing outputs; freeze/probes run once behind sentinels. Failure policy:
# run_calls.sh exits nonzero on any call failure; the smoke.py gates route every failure
# per §1/§4/§9-F4 (the state machine is the only retry policy); the driver aborts only
# on run-scoped faults (retrieval, conformance run-halt, unresolved artifacts).
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"
VENVPY="$BASE/../../.venv/bin/python"

calls() { bash run_calls.sh "$1" || echo "NOTE: failures in $1 routed by gates (§9-F4)"; }

echo "== phase 0: offline tests (no model calls) =="
python3 test_v08.py

echo "== phase 1: archive v0.7 pilot -> runs/v07-pilot-archive =="
if [ ! -d runs/v07-pilot-archive ]; then
  mkdir -p runs/v07-pilot-archive runs/prior-archive
  for x in gen-a.out gen-a.out.err gen-b.out gen-b.out.err gen-a-repair.out.err; do
    [ -e "runs/$x" ] && mv "runs/$x" runs/prior-archive/ || true
  done
  for x in runs/*; do
    case "$(basename "$x")" in
      v07-pilot-archive|v06-archive|prior-archive) ;;
      *) mv "$x" runs/v07-pilot-archive/ ;;
    esac
  done
fi

echo "== phase 2: corpus manifests -> exactly docs 01-11 (§8) =="
python3 smoke.py manifests

echo "== phase 3: freeze (§8: all hashes before any model call) =="
if [ ! -f runs/.v08-frozen ]; then
  {
    echo ""
    echo "== v0.8 FREEZE $(date -Iseconds) (prereg-v08.md §8 inventory) =="
    sha256sum \
      prereg-v08.md smoke.py test_v08.py retrieve_xc.py run_calls.sh run_v08.sh \
      leakcheck_peer.sh \
      ../peer-reconciliation-harness/gen_leakcheck.py \
      ../e2e-cell/run_isolated.sh \
      ../peer-reconciliation-harness/PROTOCOL.md \
      prompts/checklist-extract.md prompts/gen-definition-v07.md \
      prompts/ladder-conformance.md prompts/polarity-check.md \
      prompts/verify-matrix.md prompts/verify-pair.md \
      prompts/decompose.md prompts/containment-v2.md \
      key/concepts.json key/answer_key.json \
      corpora/a/manifest.json corpora/b/manifest.json \
      corpora/a/[0-9][0-9].md corpora/b/[0-9][0-9].md
    "$VENVPY" retrieve_xc.py --snapshot-hash
  } >> freeze-manifest.txt
  touch runs/.v08-frozen
  echo "frozen (appended to freeze-manifest.txt)"
else
  echo "already frozen (runs/.v08-frozen)"
fi

echo "== phase 4: resolved model identifiers at run start (§7) =="
if [ ! -f runs/.v08-models-recorded ]; then
  {
    echo "-- v0.8 resolved models at run start $(date -Iseconds) --"
    th="$(mktemp -d)"; mkdir -p "$th/.claude"
    cp "$HOME/.claude/.credentials.json" "$th/.claude/.credentials.json"
    for m in sonnet opus; do
      rid="$( (cd "$(mktemp -d)" && HOME="$th" claude -p 'Reply with exactly: OK' --model "$m" --output-format json 2>/dev/null) \
        | python3 -c 'import json,sys
d=json.load(sys.stdin); u=d.get("modelUsage") or {}
print(",".join(sorted(u)) if u else d.get("model","unrecorded"))' || echo unrecorded)"
      echo "resolved_model[$m]: $rid"
    done
    rm -rf "$th"
    echo "codex_model: gpt-5.6-terra (pinned id; provider-side alias resolution not observable at this channel — §7/§9-F9)"
    echo "claude_cli_version: $(claude --version 2>/dev/null)"
    echo "codex_cli_version: $(codex --version 2>/dev/null)"
  } >> freeze-manifest.txt
  touch runs/.v08-models-recorded
fi

echo "== phase 5: excerpts (pool = all 11 docs, no reserved split — §9-F3/B1; floor check) =="
python3 smoke.py excerpts

echo "== phase 6: checklists (§2.2; gates §1/§9-F5) =="
python3 smoke.py prompts-checklist
calls runs/checklists/calls.tsv
python3 smoke.py gate-checklists
if [ -s runs/checklists/regen-calls.tsv ]; then
  calls runs/checklists/regen-calls.tsv
  python3 smoke.py gate-checklists
fi

echo "== phase 7: ladders (§2.3) + conformance (§2.4) =="
python3 smoke.py prompts-def
calls runs/definitions/calls.tsv
python3 smoke.py gate-ladders
if [ -s runs/definitions/regen-calls.tsv ]; then
  calls runs/definitions/regen-calls.tsv
  python3 smoke.py gate-ladders
fi
python3 smoke.py prompts-conformance
calls runs/conformance/calls.tsv
python3 smoke.py gate-conformance
if [ -s runs/conformance/rerun-calls.tsv ]; then
  calls runs/conformance/rerun-calls.tsv
  python3 smoke.py gate-conformance
fi
if [ -s runs/definitions/regen-calls.tsv ]; then
  calls runs/definitions/regen-calls.tsv
  python3 smoke.py gate-ladders
  python3 smoke.py prompts-conformance
  calls runs/conformance/calls.tsv
  python3 smoke.py gate-conformance
  if [ -s runs/conformance/rerun-calls.tsv ]; then
    calls runs/conformance/rerun-calls.tsv
    python3 smoke.py gate-conformance
  fi
fi
python3 smoke.py assert-resolved

echo "== phase 8: polarity (§2.5; §9-F4 one re-run then side-scoped configFail) =="
python3 smoke.py prompts-polarity
calls runs/polarity/calls.tsv
python3 smoke.py gate-polarity
if [ -s runs/polarity/rerun-calls.tsv ]; then
  calls runs/polarity/rerun-calls.tsv
  python3 smoke.py gate-polarity
fi

echo "== phase 9: retrieval (§2.6; run-scoped fault on failure) =="
python3 smoke.py alive
"$VENVPY" retrieve_xc.py > runs/retrieval-summary.txt 2>&1 \
  || { echo "RETRIEVAL FAILED (run-scoped fault §4 — fix and re-execute)"; tail -5 runs/retrieval-summary.txt; exit 1; }
grep -o '"mutual": [a-z]*' runs/retrieval.json | sort | uniq -c || true  # zero matches is legal (all-terminal run; round-3 F5)

echo "== phase 10: matrix verification (§2.7; failures -> §4, no retry) =="
python3 smoke.py prompts-verify
calls runs/verify/calls.tsv

echo "== phase 11: aggregate + symcheck + decompose + containment =="
python3 smoke.py aggregate
python3 smoke.py prompts-symcheck
calls runs/symcheck/calls.tsv
python3 smoke.py prompts-decompose
calls runs/decompose/calls.tsv
python3 smoke.py prompts-containment
calls runs/containment/calls.tsv

echo "== phase 12: compose (§4 terminals -> §5 table -> §6 endpoints) =="
python3 smoke.py compose

echo "V08-RUN-DONE"
