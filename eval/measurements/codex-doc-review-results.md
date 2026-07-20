# Verdict: MAJOR REVISION REQUIRED

## Finding 1

- **Where:** [RESULTS.md:37](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:37), [RESULTS.md:41](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:41), [RESULTS.md:43](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:43), guided definitions and the frozen fidelity checklist.
- **Problem:** P2’s “2/2 PASS including prospectivity” contradicts the actual definitions. The checklist requires deciding whether a tool is worth building/acquiring before it exists. The guided definitions instead discuss checking or using a candidate estimate; “fixed in advance” describes the threshold, not the build decision—exactly the distinction line 41 acknowledges. P1 also never plants defects for items (i) or (ii), and S-a passes item (i) despite replacing build/acquire with retrospective use.
- **Impact:** P2 does not establish that checklist guidance fixed the e2e drift. P1 supports only that four author-written faithful examples pass and selected defects are caught, not that the gate “behaves exactly as designed.”
- **Fix:** Re-adjudicate both guided definitions against the literal build-before-existence criterion, add targeted seeded violations for items (i) and (ii), and revise P1/P2 verdicts, the gaps document, and entry-track flags accordingly.

## Finding 2

- **Where:** P3 candidate and evidence rules in [SPEC.md:59](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-SPEC.md:59) and [SPEC.md:63](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-SPEC.md:63); raw P3 verdicts.
- **Problem:** Nonqualifying candidates and non-primary evidence are counted. Examples include `w-205`, where an acronym with no authors or venue is mapped to a differently titled paper and graded `biblio=minor`; `w-275`, which is a theory rather than a specific published work; and `w-027`, which has no title, year, or venue. Verified verdicts such as `w-135`, `w-222`, `w-275`, and `w-189` rely on Wikipedia or an explanatory textbook page rather than the cited primary.
- **Impact:** The 66/100 survival rate and the claims of zero major mismatches/fabrications do not follow from the frozen inclusion and verification rules.
- **Fix:** Audit all 100 sampled occurrences for eligibility, downgrade secondary-only receipts under the frozen rule, apply the specified `minor` categories literally, and rescore. Add a receipt for the claimed seeded five-work recheck; none currently records its deterministic selection and primary evidence.

## Finding 3

- **Where:** [RESULTS.md:81](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:81).
- **Problem:** The statement that exceeding the fetch cap “cannot have inflated survival” is backwards. Extra fetch attempts increase the chance of obtaining the required receipt. Seven of the twelve works with more than three fetches were ultimately graded `exists=yes`.
- **Impact:** The reported survival can be upward-biased relative to the preregistered stop rule.
- **Fix:** Reconstruct a cap-compliant score from attempt logs. If attempt order is unavailable, conservatively downgrade affected successes or report a sensitivity range.

## Finding 4

- **Where:** [RESULTS.md:4](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:4), [RESULTS.md:70](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:70), [RESULTS.md:76](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:76), and [sample_occurrences.py:2](/mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/sample_occurrences.py:2).
- **Problem:** M2 changed P3 from verifying the complete frozen universe to sampling 100 occurrences after freeze. The results nevertheless call the sampled endpoints “pre-registered.” They also present 60/92 as a pre-registered work-validity rate, although the sampling script and freeze manifest explicitly classify induced-work statistics as exploratory and popularity-biased.
- **Impact:** The status claim that preregistered and exploratory results stayed separate is false, and 60/92 cannot estimate validity across the 410 unique works.
- **Fix:** Label 66/100 as a post-freeze amended primary endpoint and 60/92 as exploratory validity among occurrence-induced works. Use a separate random work sample if a population-level work rate is wanted.

## Finding 5

- **Where:** [RESULTS.md:17](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:17), [RESULTS.md:83](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:83), [RESULTS.md:87](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:87), and entry flag 4.
- **Problem:** “Overturns the fabrication anecdote,” “bibliographically sound,” and “attribution drift, not fabrication” exceed the measurement. Twenty-four occurrences remain existence-unverifiable; ten claims being absent from an abstract does not establish that they are misattributed; and the earlier anecdotes came from a different model/task population.
- **Impact:** The proposed shift in the entry’s motivation from fabrication to attribution/access is not supported.
- **Fix:** Report “no confirmed fabrication among the cases successfully checked” and “ten abstract-level non-confirmations.” Defer comparative conclusions until the same population and full-text verification are used.

## Finding 6

- **Where:** [RESULTS.md:83](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:83), `crossref_recheck.py`, and `crossref_recheck.json`.
- **Problem:** The claimed “18 exact bibliographic DOI matches, 2 spurious” is not reproducible from the artifact. The script records 20 fuzzy matches and does not require `author_ok`. At least three are plainly non-exact: `w-228` resolves to “Tunable glue,” `w-388` to “Communication complexity of common voting rules,” and `w-242` to a different, undated title rather than the cited 1897 work.
- **Impact:** The approximately 95% existence/bibliography estimate is unsupported.
- **Fix:** Persist a manual adjudication field for every Crossref result, require compatible title, authors, and year, and recompute the clean-match and survival counts.

## Finding 7

- **Where:** [RESULTS.md:68](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:68), [SPEC.md:74](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-SPEC.md:74), and [fuse_p4.py:118](/mnt/f/src/minelit/flf-epistack/eval/measurements/p4-union-keys/fuse_p4.py:118).
- **Problem:** The P4 scorer implements a stricter rule than the spec: it requires each U3 fusion to improve strictly, whereas the spec requires both to weakly dominate and at least one strict improvement across either fusion. The prose also falsely says K1 is the only arm besides D-opus with two owners in the top five; the table shows N, D-sonnet, and every listed fusion also have two.
- **Impact:** The current null remains unchanged because U3s fails weak dominance, but the executable rule is not the frozen rule and the interpretation exaggerates K1’s distinctiveness.
- **Fix:** Correct the predicate to `weak(U3s) && weak(U3o) && (strict(U3s) || strict(U3o))`, rerun, and describe K1 as tied on hits@5 but unique in retrieving `d03`.

## Finding 8

- **Where:** [RESULTS.md:2](/mnt/f/hub/10_projects/minelit/idiolect/2026-07-19-measurement-P1-P4-RESULTS.md:2).
- **Problem:** The title still says “provenance yield pending” while the status and body say P3 is complete.
- **Impact:** Readers and indexes receive contradictory completion state.
- **Fix:** Replace the stale title clause with the corrected P3 outcome after rescoring.

## Next steps

1. Re-adjudicate P2 and narrow the P1 conclusion.
2. Audit and rescore P3 under the frozen eligibility, primary-source, grading, and fetch-cap rules.
3. Correct Crossref adjudication, P4’s predicate/prose, and stale metadata.
4. Update the gaps document and entry-track flags only after the corrected scores are final.