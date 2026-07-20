---
title: "Cross-community cell — results (Photoreflexometry ↔ Photoplethysmography): the frozen Verdict-3 RULE triggered (NOT a supported reconciliation finding); three adversarial reviews show the cell supports no retrieval claim"
date: 2026-07-17
kind: results (built + run + THRICE Codex-reviewed; post-deadline / demonstration-grade single cell, n=1)
status: CLOSED, not pursued to a confirmatory rerun. The frozen **Verdict-3 RULE triggered** (raw-term score crossed a pre-registered — but, it turned out, chance-level — threshold). Its "pair reconciled / tool redundant" LABEL is **NOT a supported interpretation** of this cell (threshold at chance, Guard 2 unestablished, no direct-ask control). Everything beyond the rule-trigger is post-hoc/exploratory/confounded and makes NO retrieval claim. Durable value = one scoped Step-0 observation + a partial retrieval/rescoring harness + three adversarial reviews demonstrating the discipline.
depends_on: "2026-07-17-cross-community-cell-build-spec.md (6 guards / 5 verdicts), prereg.md (frozen before v1 retrieval), corpus.json/queries.json/results.json (v2), review-1/review-2 Codex logs (both MAJOR REVISION, folded)"
one_line: "Built a partial cross-community harness; screened 66 candidates to one genuinely opaque pair; ran the cell. The FROZEN pre-registration's Verdict-3 RULE triggered (both raw terms cross rank ≤3 and recall@10 ≥0.5) — but that threshold sits at chance, so it is a rule-trigger, NOT a supported reconciliation finding. THREE Codex MAJOR REVISIONs then showed every claim layered on top (chance-adjustment, direction-flip, neutral>jargon, a naive 'floor') is post-hoc and confounded — a leaked naive baseline, model-confounded arms, application-mismatched corpora, an unestablished citation guard, two unbuilt guards, a wrong descriptor id. No retrieval claim survives. What survives: one scoped Step-0 observation (in this Sonnet sweep, 4 automatic survivor flags → 1 after reading), a partial harness, and three reviews as evidence of the discipline the entry argues for."
---

# Cross-community cell — results (final, honest)

## Headline (finding first)

I built the cross-community pipeline and ran one A↔B cell. **The frozen pre-registration's Verdict-3 RULE triggered — but that is a threshold crossing, not evidence the communities are reconciled or the tool is redundant.** The "reconciled/redundant" label the rule carries is unsupported here: the threshold sits at chance, the citation guard is unestablished, and the direct-ask control was never built. Everything I then tried to layer on top (a reconciliation story, a generator–embedder dissociation, a direction flip, neutral>jargon) did not survive review. **Three** Codex passes (all MAJOR REVISION, each verified against the artifacts before folding) showed the cell is too confounded to support any retrieval claim. That correction — applied to my own work three times — is the honest deliverable, alongside a partial harness and one scoped Step-0 observation.

- **Step 0 gave one genuinely opaque pair** from 66 lexically-dissimilar candidates: **Photoreflexometry ↔ Photoplethysmography** (same MeSH descriptor **D017156**, NLM UID 68017156). Scoped precisely: **in this single Sonnet-only 66-record sweep, the automated screen flagged 4 survivors; manual reading reduced them to 1** (the 3 false survivals were Acetaminophen Sulphotransferase and two variants of the *same* Racepinephrine concept — so the 4 were not even 4 independent cases). The transferable hypothesis — *the whole-token leak check systematically over-counts, so survivor selection needs response-reading* — is consistent with this run but is **not** a measured error-rate (one model, one prompt, informal adjudication).
- **The frozen pre-registration's Verdict-3 RULE triggered** (a threshold crossing, reported as such — not endorsed as a reconciliation finding). The contract said: *if even `raw_term` reaches the far docs well (rank ≤ 3 or recall@10 ≥ 0.5), treat the pair as reconciled / tool redundant and discard it.* Both directions cross it (A→B raw_term rank 3 / recall 0.60; B→A rank 2 / recall 1.00). **But the threshold sits at chance** (random recall@10 ≈ 0.476), Guard 2 is unestablished, and there is no direct-ask control — so the rule's "reconciled/redundant" label is **not** a supported interpretation. The honest reading is: the pre-registered rule fired against a threshold that was itself mis-calibrated.
- **No further retrieval claim is made.** Prior drafts of this doc claimed "semantic reconciliation," a "generator–embedder dissociation," a "direction flip," and "neutral beats jargon." Adversarial review dismantled each. They are retained below only as a **post-hoc, exploratory, confounded** section, explicitly not a result.

## Why nothing beyond the rule-trigger is claimable (three reviews)

Per [[feedback_unreviewed_artifact_assume_wrong]], each draft was reviewed before being relied on; per [[feedback_verify_dont_defer]], each finding was checked against the frozen artifacts before folding. All three reviews returned **MAJOR REVISION** (the third on framing precision, after the factual defects were fixed). The load-bearing, verified findings:

1. **The v2 "naive question" is a leaked query, not a floor.** It generated as *"What is photoplethysmography?"* in **both** directions (`queries.json`) — it names term B verbatim. So the earlier claim "a naive lay question helps as much as the neutral definition" is invalid; that arm is removed from all interpretation.
2. **The pre-registered threshold was mis-calibrated, but the fix is a post-hoc sensitivity analysis — not a new verdict.** With 10 of 21 clean docs as targets, random recall@10 ≈ 0.476 and random first-rank ≈ 2, so the `recall@10 ≥ 0.5` trigger sits at chance. That is a real lesson (**pre-register chance-adjusted thresholds**), but the frozen contract still says Verdict 3; I report Verdict 3 as pre-registered and the chance view as an explicitly post-hoc note. Changing the net verdict to "inconclusive" (as a prior draft did) would be exactly the post-hoc threshold change pre-registration forbids.
3. **The v2 run is itself post-outcome, not pre-registered.** After seeing v1, I changed context construction, leak handling, and regenerated non-deterministic queries. v2 is an exploratory correction of v1, not a clean pre-registered replication. A confirmatory result needs a fresh frozen protocol *before* generation.
4. **"At/above chance" were categorical labels with no test.** Only random-ranking *expectations* were computed — no null distribution, interval, or decision rule. Such classifications are withdrawn; observations are described only as above/below the random expectation.
5. **The A→B neutral-vs-jargon contrast is model-confounded.** All three Sonnet neutral draws leaked the obscure own-term and were dropped, leaving **3 Opus** neutral draws versus **6 mixed** jargon draws — the contrast mixes arm and model. The claim is suspended.
6. **Length was not matched** (a build-spec requirement): B→A jargon averages 1220 chars vs 1048 for neutral (A→B: 976 vs 967 kept). Reported here, listed in the deviation ledger.
7. **Guard/verdict accounting was stale** (see ledger): the spec has **six guards and five verdicts**; I built four guards and omitted the direct-ask control and its verdict.
8. **The "obscure vs common term" causal story is unsupported.** The A side (venous-refill phlebology, 4 docs) and B side (cardiac/wearable, 10 docs) differ in application, size, recency, and granularity; any direction difference is confounded with all of those, not attributable to term obscurity.
9. **The MeSH id was wrong** (D019260 → corrected to **D017156** across corpus.json + this doc; the frozen prereg's copy is annotated, not silently changed).
10. **Artifacts made auditable:** the two review logs and both run logs are now preserved in the code dir (`review-1-codex-v1doc.log`, `review-2-codex-v2doc.log`, `run-v1-…log`, `run-v2-…log`), not session scratchpad.

## What was built, and the honest deviation ledger (built vs the 6-guard / 5-verdict spec)

Pipeline at `/mnt/f/src/minelit/flf-epistack/eval/cross-community/`: `mesh_client.py`, `select_pairs.py`, `build_corpus.py`, `run_cell.py`, `prereg.md`, frozen `corpus.json`/`queries.json`/`results.json`.

| Spec element | Built? | Note |
|---|---|---|
| Guard 1 — human-asserted synonymy | ✅ | Confirmed against primary text (a paper titled *"Photoplethysmography (PPG) or photoreflexometry (PRM)"*). |
| Guard 2 — non-reconciliation (citation) | ⚠️ partial | Reconciliation *check* built (reference overlap + coverage), but returned **INSUFFICIENT DATA** (0 of 4 A-docs have OpenAlex refs). The spec's **backward-citation corpus expansion was NOT built** — I only inspected references, did not add cited works as corpus docs. |
| Guard 3 — memorization screen | ⚠️ | Built, but **Sonnet-only** (spec asks Sonnet + Opus). |
| Guard 4a — lexical dissimilarity | ✅ | 66 candidates from 48 seeds. |
| Guard 4b — co-mention census | ✅ | B-in-A 0.25, A-in-B 0.0; reported, not dropped. |
| Guard 5 — temporal holdout (post-cutoff pairs) | ❌ | Not built. |
| Guard 6 — direct-model-query baseline | ❌ | **Not built** — so verdict 5 ("tool adds nothing over direct-ask") could not be evaluated. This is the most consequential omission: it is the control for whether the model already holds the bridge. |
| Verdict 1 (neutrality supported) | ❌ unevaluable | Needs generated-arm contrasts; the only run is post-outcome and the A→B neutral arm is model-confounded (3 Opus vs 6 mixed). |
| Verdict 2 (not the lever) | ❌ unevaluable | Same reason. |
| Verdict 3 (reconciled/redundant) | ⚠️ rule triggered | Mechanically read from raw-term scores; but threshold at chance ⇒ trigger ≠ supported reconciliation. |
| Verdict 4 (null/underpowered) | ✅ did not trigger | Ceiling (far term) reaches its own side, so far docs are retrievable. |
| Verdict 5 (tool adds nothing over direct-ask) | ❌ not implemented | Needs Guard 6 (direct-ask), which was not built. |
| Secondary metric — retrieval-grounded term recovery | ❌ | Not built. |
| Scale | n=1 | Demonstration only, never an effect size. |

## Step 0 — the one scoped observation

48 seeds → **66 lexically-dissimilar candidate pairs** → memorization screen. **Automated: 4/66 survive. Reading the responses: 1 genuine opaque coinage** (Acetaminophen Sulphotransferase = enzyme false-match, 0 docs; Racemic Epinephrine ×2 = model gave the correct pharmacology). The 62 VOIDs are textbook synonyms the model bridges (Kawasaki↔Mucocutaneous Lymph Node Syndrome, Pompe↔Glycogen Storage Disease II, niacin↔nicotinic acid…). The survivor, Photoreflexometry, *misroutes* the model (guesses "pupillary light reflex / Soviet ophthalmology"). Takeaway ([[feedback_clean_testset_for_recall_tools]]), scoped to what this one Sonnet sweep shows: **the whole-token leak check flagged 4 survivors that manual reading cut to 1** (and the 4 were not independent — two are the same Racepinephrine concept). It is consistent with the hypothesis that the automated check over-counts and that selection needs response-reading, but it is **one model / one prompt / informal adjudication — not a measured error-rate.** This is independent of the retrieval confounds and is the cell's most durable observation.

## Post-hoc, exploratory, confounded (NOT a result — retained for audit only)

The v2 numbers (clean condition; A→B neutral = 3 Opus draws after Sonnet leak-drops; naive arm excluded as leaked; CIs are descriptive resampling-stability only):

| dir | arm | rank1st | recall@10 | random expectation |
|---|---|--:|--:|---|
| A→B | raw_term | 3 | 0.60 | rank 2.0 / recall 0.476 |
| A→B | jargon | 4 | 0.70 | |
| A→B | neutral (3 Opus) | 2.33 | 0.73 | |
| B→A | raw_term | 2 | 1.00 | rank 5.5 / recall 0.476 |
| B→A | jargon | 4.17 | 0.67 | |
| B→A | neutral | 3.83 | 0.72 | |

The apparent A→B "neutral beats raw_term/jargon" and B→A "raw_term beats neutral" pattern is **not interpretable**: the naive baseline is leaked, the A→B neutral arm is model-confounded, the arms are length-mismatched, the corpora differ in application/size/recency, Guard 2 is unestablished, and there is no direct-ask control. It supports no claim about neutrality, reconciliation, or any model dissociation. (v1's superseded numbers and its leaks are in `run-v1-…log`.)

## What a valid cell needs (DEFERRED — funded/post-deadline recommendations, not started, no owner assigned)

1. A **fresh frozen pre-registration with chance-adjusted decision rules**, written before generation.
2. A **non-leaking, direction-specific naive baseline** and the **direct-model-query control** (Guard 6) — the missing gate for "does the tool beat just asking the model."
3. **Same-application, symmetric, comparable-depth corpora** on both sides; **balanced models and lengths**; **established citation-disjointness** (needs sides with OpenAlex reference coverage — not old non-digital literature).
4. A pair the **embedder** does not already bridge. Sources: UMLS cross-source-vocabulary CUIs (free UTS key), or the Larsen & Bong jangle gold standard. *(Checked 2026-07-17: the L&B PDF's Table B1 gives cluster labels + counts only, not the individual construct names; searching a cluster label returns its own papers, not its jangle siblings — verified by reading Table B1 and an OpenAlex probe. L&B needs the dead-endpoint INN test-bed data.)*
5. **Many pairs**, for an effect size.

## Follow-on: is there a valid SECOND cell?

Searched (2026-07-18) via a cheap Guard-0 cross-cosine pre-filter + memorization screen. **Answer: not from any curated vocabulary.** MeSH sweet spot is empty (low-cosine pairs all memorized); the cross-vocabulary route (OLS4 proxy for UMLS) populates the low-cosine regime 3× better and surfaces obscure eponyms, but a screen on 18 of them auto-flagged 14 "sweet-spots" that **collapsed to 0 on reading** — the model correctly bridges every one. Structural reason: curated synonyms are memorized *by construction*, so a UTS key would not help. Clean regimes are post-cutoff concepts (Guard 5) or private coinages (where the recall-backtest's C2 already worked). Full write-up + numbers: **`2026-07-18-second-cell-search-ADDENDUM.md`**.

## Artifacts

`/mnt/f/src/minelit/flf-epistack/eval/cross-community/` — code + frozen `corpus.json`/`queries.json`/`results.json` (**v2 only**)/`candidate_pairs.json`; `review-1-codex-v1doc.log`, `review-2-codex-v2doc.log`, `review-3-codex-v3doc.log` (all MAJOR REVISION); `run-v1-…log`, `run-v2-…log`. **Audit-trail limits (stated honestly):** `../../.venv/bin/python run_cell.py` **rescores the frozen v2 artifacts only** — it does not reproduce selection, corpus build, or generation (non-deterministic); the **v1 query JSON was overwritten** by v2 (v1 scores + lengths survive in `run-v1-…log`, but not the v1 query texts); and `prereg.md` was **annotated post-freeze** for the descriptor-id typo (no threshold/verdict changed). A confirmatory rerun must version + hash the prereg and all v1/v2 artifacts before generation. Method memories: [[feedback_unreviewed_artifact_assume_wrong]], [[feedback_clean_testset_for_recall_tools]], [[feedback_recipes_die_on_transfer]], [[feedback_verify_dont_defer]], [[feedback_reading_is_the_bottleneck]], [[feedback_exploratory_phase_discipline]].
