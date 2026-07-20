#!/usr/bin/env bash
# leakcheck_e2e.sh — the ONE frozen leak checker for the e2e cell (spec rev 2 §5-G2).
# Runs BOTH classes in one pass. Case-insensitive, word-boundary where meaningful.
# Exit 1 on any hit; prints every hit with its class. Pattern lists are frozen at
# spec approval; additions require a logged spec revision BEFORE generation.
set -euo pipefail
f="${1:?usage: leakcheck_e2e.sh <file>}"

answer_patterns=(
  'value of information' '\bVoI\b' '\bEVPI\b' '\bEVSI\b'
  'expected value of sample information' 'preposterior' 'Raiffa' 'Schlaifer'
  '\bHoward\b' 'target product profile' '\bTPP\b' 'threshold analysis'
  'decision-theoretic' 'Bayesian decision analysis' 'expected utility'
  'perfect information' 'information value' 'worth of (data|information)'
  'decision analysis'
)
coinage_patterns=(
  'operating requirement' 'cold-start' 'cold start' 'audit unit'
  'm\*' 'm-star' '\bmstar\b' 'dependence detector' 'effective count' 'n_eff'
)

hits=0
for p in "${answer_patterns[@]}"; do
  if grep -inE --color=never "$p" "$f" >/dev/null 2>&1; then
    echo "LEAK [answer]  pattern: $p"
    grep -inE --color=never "$p" "$f" | head -3
    hits=$((hits+1))
  fi
done
for p in "${coinage_patterns[@]}"; do
  if grep -inE --color=never "$p" "$f" >/dev/null 2>&1; then
    echo "LEAK [coinage] pattern: $p"
    grep -inE --color=never "$p" "$f" | head -3
    hits=$((hits+1))
  fi
done

if [[ $hits -gt 0 ]]; then
  echo "RESULT: FAIL ($hits pattern(s) hit)"
  exit 1
fi
echo "RESULT: CLEAN"
