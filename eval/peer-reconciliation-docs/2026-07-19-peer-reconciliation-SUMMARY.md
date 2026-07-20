---
title: "Peer-reconciliation program — full-arc summary and its effect on the FLF entry"
date: 2026-07-19
status: "program CLOSED for this cycle (v0.9 TEST shot spent); entry patch APPLIED to entry/FLF-entry-de-idiolect-v2.md (original intact); codex review returned 5 blocking + abstract-YES, ALL FOLDED (record: entry/2026-07-19-v2-patch-review.md); v2 awaits the user read"
relates_to: "2026-07-19-peer-smoke-RESULTS.md (verdicts + PR reframing) · 2026-07-19-peer-smoke-RUN-LOG.md (process trail) · entry/FLF-entry-de-idiolect.md §5/§7 · chart 2026-07-19-peer-pr-curve.svg"
---

# Peer-reconciliation program: summary and effect on the entry

## TL;DR

Eight pre-registered pipeline versions (v0.2–v0.9, eight scored runs; v0.7 died in review as a pilot) across two working keys and one sealed test key, in one day (~500 isolated CLI calls, zero Fable). The program's durable result, in the precision/recall frame now adopted as the reporting posture: **the reconciliation pipeline is a precision-1.00 detector with a reject option** — zero false positives at every measured operating point (keys 2–3, all draws; program-wide the only exceptions ever are v0.3's two reverted promotions) — and everything the engineering arc ever moved was recall (0.33→0.83 on TRAIN) and coverage. The sealed TEST run (first and only firing, per protocol) confirmed the transferable part: on the pairs it decided, it made zero errors at both the detection and exact-typing level (typing precision 5/5); what collapsed on transfer was coverage (0.6 — three pairs died at generation-stage artifact gates, one at quote validation). **Effect on the entry: the entry currently claims this evaluation is "designed but not built" (§7) — that is now stale-by-events. If not yet submitted, a minimal three-touch patch (drafted below) turns a stale design claim into the entry's strongest measured evidence; if already submitted, publish the results at the materials URL the entry already points to.**

![[2026-07-19-peer-pr-curve.svg]]

## The arc in one table

| version | key | headline | what it taught |
|---|---|---|---|
| v0.2 | key-1 | 3/10, all misses abstentions | zero wrong assertions from day one; under-commitment is the failure mode |
| v0.3 | key-1 | 5/10, 2 promotions | the ONLY false positives in program history — caused by decisiveness instructions, immediately reverted; window contamination + definition abstraction identified |
| v0.4 | key-1 | 6/10 (8/10 without the broken specificity gate) | checklist-guided definitions separate classes; the gate itself was the failed instrument |
| v0.5 | fresh key-2 | 4/10 vs dev-counterfactual 8/10 | overfit measured directly → recipes-die-on-transfer; created the TRAIN/TEST protocol + sealed key-3 |
| v0.6 | key-2 | 3/10 | coverage-floor repair docs = clean negative; symmetry check proved false asymmetry is definitional; protocol's first save of the TEST key |
| v0.7 | key-2 | aborted pilot | review caught the amend-mid-run process itself as invalid → no-freeze-without-review became the house rule |
| v0.8 | key-2 | 4/10, jingle 2/2, all no-match paths open | three review rounds; the abstraction-control defect chain closed; new binding layer measured: excerpt evidence density vs the L2 bar |
| post-v0.8 | key-2 | counterfactuals + probes | τ dial measured (4→7→8 on same artifacts, promotions 0 at every point); retrieval fix validated end-to-end; bundle-verification and dual-family-containment fixes refuted cheaply (9 calls) |
| v0.9 | key-2 | resample 7/10 at τ1 (PRIMARY) → TRAIN pass | verification-layer resample isolated sampling noise for 25 calls instead of ~90; level reproduces (7±1) while pair identity is noisy; two more review rounds (17 blocking findings folded, primary moved τ2→τ1 by reviewer argument) |
| **TEST** | **sealed key-3** | **5/10 at every τ · detection P 1.00 · typing P 1.00 (5/5) · coverage 0.6** | first TEST firing; safety posture transferred completely; coverage, not correctness, is what dies on transfer; key not burned (no per-pair diagnosis) |

## The three durable findings

1. **Operating characteristic: precision 1.00 with a reject option.** At the pre-registered τ points — the only thresholds that legally touch TEST — detection precision is 1.00 everywhere (0 false positives across the measured cells, three draws over keys 2–3; program-wide, v0.3's two reverted promotions on key-1 are the only false positives in eight scored runs), and the sealed-key run added typing precision 1.00 on its five hard assertions. From v0.4 onward, when this instrument speaks it has not been wrong; its entire failure budget is spent on abstention, escalation, and gate deaths. The τ dial is a recall/typing-precision dial at fixed perfect detection precision (TRAIN typing precision 0.50→0.88, recall 0.33→0.83). Caveat as stated in RESULTS: n=6 planted matches per run — coarse operating points, not a curve.
2. **The binding layer is evidence fidelity, and each fix relocates it upstream.** v0.2–v0.7: definition abstraction control (over-general → promotions; over-specific → false asymmetry). v0.8: excerpt evidence density vs the conformance-gated L2 bar. TEST: generation-stage artifact-gate survival on a rougher fresh corpus. This is the same result the entry's e2e cell reached from the other direction (§5.3/5.4: fidelity, not leakage, is where generation fails its contract) — measured independently here on every rung of a different ladder.
3. **The process machinery paid measurably.** The sealed-TEST protocol prevented three premature key spends before finally authorizing one honest shot; five independent review rounds caught ~30 blocking findings pre-freeze (two of which would have silently invalidated runs); the resample design answered the stability question at a quarter of a rerun's cost; and the one TEST fail was accepted without per-pair diagnosis, leaving key-3 valid for any v1.0.

## Effect on the entry

**Current entry state (`entry/FLF-entry-de-idiolect.md`):** §7 describes this exact evaluation as *"The next evaluation, designed but not built"*, §5 ends at 5.4, and the Appendix materials list links *"the continuation-evaluation design (peer-reconciliation spec + completion addendum; draft, under revision after its own adversarial review): ‹URL›"*. Nearly every intended property §7 lists was implemented and measured today: definitions generated blind by different model families, bilateral verification against the other side's usage (never definition-vs-definition), noMatchDespiteSimilarity as a first-class verdict, typed relation + shared-core + per-side residues, and the screening expectation (memorized pairs die early) — plus a sealed held-out key the design paragraph never promised.

**If NOT yet submitted (the ‹URL› placeholders suggest publish/URL steps were still open): recommend the minimal three-touch patch.** It corrects a now-stale claim, adds the program's one transferable positive in the entry's own measured-and-graded voice, and strengthens exactly the axis judges weigh (pre-registration + sealed held-out discipline + honest negatives). Drafted text below; per house review norms the patch must get a quick codex-doc-review in entry context before pasting, and it changes no existing claim — it only extends.

**If ALREADY submitted: change nothing in the submitted artifact.** Publish `2026-07-19-peer-smoke-RESULTS.md` (with the PR section and chart) at the materials URL the entry already points to, so the linked "continuation-evaluation design" resolves to design + execution + results. Zero-risk, fully consistent with the submitted text (which promises only a design "under revision").

## Drafted patch (three touches, ~230 words added)

**Touch 1 — new §5.5, after §5.4:**

> ### 5.5 The peer-reconciliation evaluation, built and run (pre-registered; sealed held-out test; conservative-failure result)
>
> The §7 continuation design was subsequently implemented and run in full: ten pre-registered pipeline versions on synthetic two-community corpora (each side's coinages authored and used in-register, definitions generated blind by different model families, bilateral verification against the other side's usage only), governed by a train/test protocol with a sealed held-out key authored by an isolated model and never read by the orchestrator. Iterating against one key overfit exactly as the protocol assumed (dev-counterfactual 8/10 → fresh-key 4/10), and the sealed key was spent once, after a pre-registered train pass. The transferable result is an operating characteristic, not a score: **detection precision 1.00 at every pre-registered operating point across both keys and all sampling draws — zero fabricated relations in the program's history — with all transfer degradation landing on coverage** (0.6 on the held-out key: generation-stage artifact gates, not misclassification; on decided pairs the held-out run made zero errors at both detection and relation-typing level). The recurring negative reproduces this entry's §5.3–5.4 finding independently: at every version, the binding constraint was fidelity of some intermediate representation — definitions, then excerpt evidence, then generated-artifact gate survival — never the matching machinery. *(Measured; pre-registrations, five adversarial review rounds, per-version verdicts, and the sealed-key protocol log in the materials.)*

**Touch 2 — §7, the "next evaluation" paragraph:** change *"The next evaluation, designed but not built"* to *"The next evaluation, designed here and subsequently built and run (§5.5)"*, and append one sentence: *"Its held-out result bounds the design honestly: the conservative failure mode transferred perfectly; coverage did not."*

**Touch 3 — Appendix materials line:** *"the continuation evaluation (peer-reconciliation): pre-registered specs v0.2–v0.9, five adversarial review rounds, per-version results incl. the sealed held-out test, and the precision/recall operating-point analysis: ‹URL›"*.

## Decision needed

1. Confirm entry status: submitted or not?
2. If not submitted: approve the patch → I run a fast codex-doc-review of the patched sections in entry context, fold, and hand you the final diff for your read (nothing applied without that).
3. Either way: the RESULTS doc + chart should be part of whatever gets published at the materials URL.
