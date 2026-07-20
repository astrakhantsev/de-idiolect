# Verdict

**REVISE BEFORE FREEZE.** The spec has material reproducibility gaps and several endpoints that overstate what the proposed measurements can establish.

# Findings

## 1. The pre-registration does not freeze the experimental materials

- **Where:** P1 “Materials,” P2 procedure, P3 candidate universe, shared machinery.
- **Problem:** The exact nine P1 definitions and five seeded edits are absent. There is also no hashed manifest of raw input files, rankings, prompts, or directory contents. P2 does not specify the exact prompt rendering or delimiter placement.
- **Impact:** Materials can change after the spec is frozen, and another implementor cannot reproduce the calls or verify that each seeded example changed only one checklist item.
- **Fix:** Before execution, add a hashed manifest containing every input path, exact P1 texts and paired diffs, raw-file snapshots, prompt templates, model settings, and the canonical spec hash. Archive each dynamically generated P2 prompt verbatim before its call.

## 2. P1 cannot support the stated “gate calibrated” interpretation

- **Where:** P1 interpretation table.
- **Problem:** Four definitions written and labeled faithful by the checklist’s author are a narrow non-degeneracy test, not an estimate that calibrates the gate’s false-positive rate. Therefore `FP 0/4 AND detection ≥4/5` does not justify “the e2e null stands STRONGER; no caveat.”
- **Impact:** A favorable result would be presented as stronger validation than the design supports, especially because the faithful labels are not independently adjudicated.
- **Fix:** Describe P1 as an author-constructed sanity check. A 0/4 result may show that the judge can pass selected faithful examples, but should not remove the judge-validity caveat. Require independent adjudication or a broader representative sample before claiming calibration.

## 3. The “one planted violation” assumption is not operationally protected

- **Where:** P1 seeded-defect arm.
- **Problem:** Adding an author or unsupported benchmark can violate both items v and vi, while changing prospectivity or threshold language may disturb other structural commitments. No exact paired texts or pre-judging item-level adjudication are specified. There is also no contingency if a seeded defect unexpectedly trips the leak checker.
- **Impact:** Detection and item-attribution rates may not measure the intended isolated defects.
- **Fix:** Freeze minimal paired diffs and record expected verdicts for all items i–vi, not just the planted item. If a seeded stimulus leaks or introduces multiple violations, declare it invalid or revise it before the overall freeze—not during execution.

## 4. P2 cannot attribute a 1/2 result to checklist guidance

- **Where:** P2 question and pre-registered endpoint.
- **Problem:** One guided sample from each of two models is compared with a historical 0/2 baseline. There are no contemporaneous unguided controls or repeated samples, yet 1/2 is defined as “measured support” that the checklist lifts the pass rate.
- **Impact:** Ordinary sampling variation, session differences, or model differences could be mistaken for an intervention effect.
- **Fix:** Run paired guided and unguided calls for each model with pre-specified repetitions. Otherwise report only the observed guided count on this cell and avoid “lift,” “pass rate,” or causal support language.

## 5. P3’s claimed candidate universe contradicts its extraction procedure

- **Where:** P3 “Candidate universe” and “Extraction.”
- **Problem:** The universe is defined as every qualifying citation, but extraction recall is explicitly not audited exhaustively and only two files per directory are spot-checked. Directory membership is also not frozen.
- **Impact:** Missed citations silently leave the denominator, potentially biasing the survival rate.
- **Fix:** Freeze a complete file-and-hash manifest, perform deterministic exhaustive extraction, or estimate extraction recall with a pre-specified random audit large enough to bound the error. Freeze and hash the completed ledger before verification begins.

## 6. P3 mixes citation occurrences, unique works, and claim assertions

- **Where:** P3 candidate definition, deduplication rule, and endpoints.
- **Problem:** The question concerns model-proposed citations, but the endpoint counts unique deduplicated works. Repeated proposals and multiple claims about one work are collapsed. The dedup key is also undefined for allowed candidates lacking a title, and year variants of the same work may remain separate. Global deduplication does not explain how “survival by source experiment” will retain every provenance occurrence.
- **Impact:** The denominator does not answer the stated question, and experiment-level comparisons may be impossible or misleading.
- **Fix:** Store occurrence-level citation-claim records linked to canonical-work records, retaining every source file and assertion. Report occurrence-level survival as the primary endpoint and unique-work validity separately. Canonicalize using DOI or another explicit bibliographic identity rule.

## 7. P3’s VERIFIED grade does not establish that an owner citation survived verification

- **Where:** P3 verification protocol.
- **Problem:** “Plausibly present at abstract/title level” is subjective and often cannot establish canonical ownership, oldest treatment, or direct prior art. Bibliographic deviations can still receive VERIFIED, Crossref is not itself a primary source, and “reasonable attempt” is undefined. PARTIAL error categories may overlap, while the random VERIFIED audit has no seed or selection rule.
- **Impact:** The survival rate may be inflated and cannot be reproduced consistently.
- **Fix:** Score separately: work existence, bibliographic match, support for the attributed technical claim, and support for ownership/oldest status. Require a primary-source URL plus exact supporting passage or page location. Define the search stop rule, tolerance rules, multilabel taxonomy, and random-audit seed before verification.

## 8. P4’s support rule is outcome-ambiguous

- **Where:** P4 question and comparison rule.
- **Problem:** “Beat any single key” conflicts with comparison against the best constituent, which effectively means matching or beating all constituents. “Strict improvement on at least one of the two” does not clearly identify whether “two” means metrics or U3 fusions.
- **Impact:** The same results could be classified differently after inspection.
- **Fix:** State the criterion symbolically—for example: both U3 variants must weakly dominate their selected best constituent on both metrics, and at least one `(fusion, metric)` comparison must be strictly better. Replace “beat any single key” with wording matching that rule.

## 9. Artifact paths and source-of-truth locations are unresolved

- **Where:** Shared machinery and “Budget & deliverables.”
- **Problem:** Relative paths such as `eval/...` and `runs/...` have no declared base directory. The spec currently lives in the hub, while the deliverables say it will be copied into the external workspace; the canonical copy and synchronization direction are not stated.
- **Impact:** Implementors may write into different trees, modify the wrong copy, or hash a noncanonical version.
- **Fix:** Declare `/mnt/f/src/minelit/flf-epistack/` as the execution root, make paths absolute or explicitly root-relative, designate one canonical spec/results location, and define the hub copy as a synchronized mirror.

# Next steps

1. Add the exact stimuli, prompt-rendering rules, canonical paths, and hashed input manifest.
2. Narrow the P1 and P2 interpretations to what their sample designs establish, or add independent adjudication and paired repetitions.
3. Redesign the P3 ledger around occurrence-level citation claims and define reproducible verification grades.
4. Resolve the P4 decision rule and dual-copy source of truth.
5. Run the next review only after those changes, then freeze and log the canonical SHA-256.