#!/usr/bin/env bash
# leakcheck_peer.sh — frozen leak checker for the peer-reconciliation smoke test (prereg §Leak checks).
# usage: leakcheck_peer.sh cross-a <file>   # file belongs to corpus A: no B-only terms allowed
#        leakcheck_peer.sh cross-b <file>   # file belongs to corpus B: no A-only terms allowed
#        leakcheck_peer.sh meta    <file>   # no key-file meta-vocabulary
#        leakcheck_peer.sh def     <file>   # definitions: no coined term of EITHER side + meta
# Exit 1 on any hit; prints hits. Jingle strings ("drift audit", "ghost pass") are whitelisted cross-corpus.
set -euo pipefail
mode="${1:?mode}"; f="${2:?file}"

a_only=('shuffle fragility' 'claim survival tally' 'probe-shadow' 'missing-key test' 'pothole runs' 'notebook yank' 'spend silhouette' 'menu pinning')
b_only=('permutation sensitivity collapse' 'intermediate assertion persistence ratio' 'instrumentation latency steering' 'specification occlusion' 'seeded-defect audit' 'memory paraphrase perturbation' 'line-anchored rubric' 'self-contradiction incidence')
jingle=('drift audit' 'ghost pass')
meta=('exactMatch' 'broadMatch' 'narrowMatch' 'relatedMatch' 'noMatch' '\bbroader\b' '\bnarrower\b' 'shared core' '\bresidue' '\bplanted\b' 'answer key' 'community A' 'community B' '\bjingle\b')

fail=0
check() { local pat="$1" label="$2"; if grep -qiE "$pat" "$f"; then echo "LEAK[$label]: $pat"; fail=1; fi }

case "$mode" in
  cross-a) for t in "${b_only[@]}"; do check "$t" "b-term-in-a"; done ;;
  cross-b) for t in "${a_only[@]}"; do check "$t" "a-term-in-b"; done ;;
  meta)    for t in "${meta[@]}"; do check "$t" "meta"; done ;;
  def)     for t in "${a_only[@]}" "${b_only[@]}" "${jingle[@]}"; do check "$t" "term-in-def"; done
           for t in "${meta[@]}"; do check "$t" "meta"; done ;;
  *) echo "unknown mode $mode"; exit 2 ;;
esac
exit $fail
