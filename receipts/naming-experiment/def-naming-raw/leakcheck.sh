#!/bin/bash
# Leakage check: scan a file for answer-key terms (case-insensitive) and, with -c flag, project coinages.
# Usage baked in per file below to avoid saferun positional-arg issue: edit TARGET.
set -u
TARGET="${1:?usage: leakcheck.sh <file> [coinage]}"
MODE="${2:-answers}"

ANSWERS='clemen|winkler|kish|design effect|effective sample|effective number|equivalent number|n_eff|value of information|EVPI|EVSI|preposterior|raiffa|schlaifer|target product profile|pauker|kassirer|br[oö]cker|proper scor|scoring rule|calibration.refinement|reliability.resolution|murphy|degroot|de groot|fienberg|blackwell|\browe\b|\bwright\b|delphi|sufficiency|best 1974|gustafson|howard 1966'
COINAGES='m\*|m-star|mstar|operating requirement|cold.start|audit unit|\bgate\b|\bgates\b|credence|enumerat|signal, not|the cut'

if [ "$MODE" = "coinage" ]; then
  PAT="$COINAGES"
else
  PAT="$ANSWERS"
fi

echo "=== leakcheck ($MODE) on $TARGET ==="
grep -inE "$PAT" "$TARGET" || echo "CLEAN: no hits"
