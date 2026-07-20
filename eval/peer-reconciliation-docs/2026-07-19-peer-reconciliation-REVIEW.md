---
title: "Peer reconciliation SPEC + completion ADDENDUM — joint Codex review (FULL TEXT)"
date: 2026-07-19
reviewer: "gpt-5.6-sol, xhigh, via codex-doc-review (joint review of both design docs)"
status: "MAJOR REVISION — 17 findings, NOT BUILD-READY. None folded yet; the post-deadline design revision works from THIS document. Summaries live in both design docs' status lines; this file is the authoritative full text, archived verbatim from the session task output."
relates_to: "2026-07-18-peer-reconciliation-SPEC.md · 2026-07-18-peer-reconciliation-completion-ADDENDUM.md · 2026-07-19-measurement-gaps.md (P6)"
---

# Verdict

**MAJOR REVISION — not build-ready.** The verifier cannot validly derive the five relation classes, the crosswalk schema does not yet guarantee immutable coexisting forks, and the evaluation plan contains circular/gameable endpoints. Several claims also exceed what the cited experiments established.

# Findings

## 1. The entailment direction reverses between documents

- **Where:** SPEC §2.4; ADDENDUM §3.1–§3.3.
- **Problem:** The SPEC asks whether “A’s definition entails B’s usage.” The addendum instead defines coverage as “B’s excerpts instantiate A’s definition,” which is the opposite logical direction: usage ⇒ definition. The addendum also never specifies whether one quote, every excerpt, or some proportion must instantiate the definition.
- **Impact:** An implementor can reverse broad/narrow labels or approve a relation from one cherry-picked overlapping quote.
- **Fix:** Define the tested proposition formally and per excerpt, e.g. `usage_excerpt ⇒ candidate_definition`, with `entailed | contradicted | unknown`, explicit aggregation rules, counterexample requirements, and an abstention outcome.

## 2. The composition table does not identify the claimed relations

- **Where:** ADDENDUM §3.3.
- **Problem:** Mutual observed coverage supports at most “observationally equivalent on these excerpts,” not `skos:exactMatch`. Mutual retrieval plus two coverage failures does not establish partial overlap; topically adjacent or co-occurring concepts can retrieve each other without sharing an extension. The table has no outcomes for mixed excerpts, insufficient evidence, polarity/fidelity failure, or `no/no/no` without surface similarity.
- **Impact:** Binary, noisy judgments are mechanically promoted into strong ontology claims, producing false exact, broad/narrow, and related mappings.
- **Fix:** Make table outputs provisional candidates, add `insufficientEvidence`, require explicit shared-core evidence for overlap, require counterexample/residue evidence for breadth, and reserve final SKOS typing for independent adjudication.

## 3. “ExactMatch candidate” and the emitted final relation are inconsistent

- **Where:** ADDENDUM §2 schema versus §3.3.
- **Problem:** The composition table emits an `exactMatch candidate`, but the schema has only a final `relation` field. No promotion step, reviewer decision, confidence, or candidate/final state exists.
- **Impact:** Implementations will either publish provisional machine judgments as final commons entries or invent incompatible approval workflows.
- **Fix:** Add explicit `proposed_relation`, `adjudicated_relation`, status, adjudicator provenance, and abstention/rejection fields.

## 4. Decoy calibration is circular and trivially gameable

- **Where:** ADDENDUM §3.4.
- **Problem:** Rejecting only a verifier that “never reaches no-match” lets an always-no-match verifier pass. Famous decoys or equivalent pairs let the model answer from memorized pair identities rather than quoted usage. The proposed decoys are themselves unverified “candidates to screen.”
- **Impact:** A verifier can pass calibration without using the intended evidence or having useful class discrimination.
- **Fix:** Freeze an anonymized, independently labeled, class-balanced calibration set with matched hard positives and negatives; measure the full confusion matrix and class bias; then evaluate on a separate held-out set. Do not expose recognizable terms when calibration is supposed to test evidence-following.

## 5. The community-identity endpoint rewards semantic erasure

- **Where:** ADDENDUM §6.
- **Problem:** At-chance identity is valid only when semantic content is held constant. For broad/narrow and partial-overlap pairs, faithful side-specific definitions should retain real conceptual residues, making community identity legitimately predictable. Conversely, vacuous generic definitions can achieve chance.
- **Impact:** The endpoint can label faithful definitions as non-neutral and reward definitions that discard the distinctions the system is meant to preserve.
- **Fix:** Run identity testing only on controlled exact-match/content-matched cases, or condition the classifier on semantic content. Jointly gate neutrality on fidelity and retrieval utility rather than treating chance identity alone as success.

## 6. The one-entry schema does not implement the SPEC’s three-artifact contract

- **Where:** SPEC §2.5; ADDENDUM §2.
- **Problem:** The SPEC requires a typed link, shared core, and residues as three artifacts; the addendum places them as unversioned fields inside one “merge artifact.” Relation-specific cardinality is undefined: no-match should have no shared core, exact match should normally have empty residues, and broad/narrow should have asymmetric residues.
- **Impact:** The container cannot independently cite, version, dispute, or supersede the three claimed artifacts, and it requires semantically invalid content for some verdicts.
- **Fix:** Either declare these explicitly as three immutable linked subrecords or revise the SPEC to call them components of one record. Define per-relation required/null fields; a no-match entry should emit rejection evidence, not a manufactured shared core.

## 7. The content-addressed ID breaks versioning and fork coexistence

- **Where:** ADDENDUM §2 `id`, `supersedes`, and provenance.
- **Problem:** The ID hashes only term strings, relation, and shared-core text. It omits communities, corpus/source hashes, residues, evidence, provenance, disputes, and lineage. Changed evidence or residues can therefore reuse the same ID; identical text regenerated from different sources/models collapses distinct provenance; an unchanged regeneration can supersede itself. Eight hex characters provide only 32 bits of collision space.
- **Impact:** Entries can collide or overwrite semantically distinct versions, directly defeating regenerable-cache provenance and coexisting forks.
- **Fix:** Separate a stable pair/sense key from an immutable version ID. Hash a canonical serialization of the complete immutable record with at least 128 bits, including corpus, evidence, provenance, and lineage.

## 8. Disputes and forks are asserted but not representable

- **Where:** ADDENDUM §2 design notes.
- **Problem:** `disputes: []` has no schema for link type, target, claimant, evidence, timestamp, or scope. `supersedes` permits only one predecessor and cannot represent multi-parent reconciliation or concurrent branches. No append-only storage/index rule is specified.
- **Impact:** “Forks coexist,” “typed disagreement,” and “no write-lock” are aspirational claims, not properties delivered by the schema.
- **Fix:** Specify immutable typed-link objects, actor/provenance fields, branch/root identity, multiple `derived_from` links, and append-only indexing semantics; test two simultaneous incompatible mappings before claiming the property.

## 9. SKOS broad/narrow direction is ambiguous

- **Where:** ADDENDUM §2 schema and §3.3.
- **Problem:** The schema stores both `skos:broadMatch | skos:narrowMatch` and `relation_direction`, but never defines which concept is the SKOS subject. “A broader” can be encoded as either `A narrowMatch B` or `B broadMatch A`.
- **Impact:** Two conforming implementations can emit opposite triples.
- **Fix:** Emit an explicit directed triple—`subject`, `predicate`, `object`—or store only `broader_side` and derive the SKOS triples deterministically.

## 10. Shared-core and residue production is absent from the build plan

- **Where:** SPEC §2.5; ADDENDUM §§3, 6, and 7 steps 6–7.
- **Problem:** The verifier produces coverage judgments, while step 7 merely “emits” a crosswalk. No step, prompt, algorithm, fidelity gate, or evidence rule generates the shared core or residues. Their evaluation reuses the same corpus from which they would be derived.
- **Impact:** The system’s distinctive output cannot actually be built from the specified steps. Same-corpus residue retrieval is circular and can succeed through copied topical or lexical cues.
- **Fix:** Add a separate decomposition stage with frozen prompts/schema, wordlist and fidelity checks, failure/abstention rules, and quote-level provenance. Evaluate residues on held-out side-specific documents plus a far-side exclusion test.

## 11. The frozen human key is neither frozen nor independent

- **Where:** SPEC §3 endpoints; ADDENDUM §6 and §7 step 8.
- **Problem:** The SPEC calls for a held-out frozen key, while the addendum places user adjudication after verifier execution and limits the user to verifier-selected quotes. It gives no sample size, adjudicator qualifications, agreement procedure, or rule for resolving uncertainty.
- **Impact:** The verifier controls the evidence used to judge itself, making typing accuracy circular and vulnerable to selective quotation.
- **Fix:** Freeze representative excerpts and relation labels before verifier output, using independent blind adjudication and tie-breaking. Keep calibration, development, and held-out evaluation pairs disjoint.

## 12. Screening tests discovery redundancy, not whether reconciliation artifacts add value

- **Where:** SPEC §3; ADDENDUM §§5 and 7.
- **Problem:** Guard 0, co-citation, and memorization screens reject pairs when terms or communities are already bridged. That is appropriate for measuring discovery lift, but not for testing relation typing, residue decomposition, disputes, or the commons artifact. The screens also provide only negative evidence; none establishes that two otherwise disconnected candidates really concern the same phenomenon.
- **Impact:** The gate can discard the best gold-labeled typing cases while admitting unsupported candidate pairs. The claimed “true A↔B pairs” have no acquisition or confirmation procedure.
- **Fix:** Separate a discovery-lift stratum from a relation-typing/artifact stratum. Obtain candidate pairs from independent expert nomination or controlled construction, freeze positive labels separately, and retain bridged pairs where typing remains nontrivial.

## 13. The screening strata do not consistently target the no-canonical regime

- **Where:** SPEC §3 versus ADDENDUM §5.
- **Problem:** The addendum replaces the SPEC’s forum–academic and lab–external strata without stating precedence. Private×public cases like C2 are anchoring cases against established public owners, not peer/no-canonical cases. The cross-language stratum lacks a common-language and translation-control protocol. The synthetic “same referent” design supplies only exact-match cases, not broad/narrow, partial, or no-match ground truth.
- **Impact:** Results from materially different regimes could be pooled under one verifier claim, while several relation classes remain unevaluable.
- **Fix:** Publish one normative stratum table with eligibility, confounds, allowable claims, language handling, and required class coverage. Keep anchoring, peer, cross-language, and synthetic results separate.

## 14. Prior results are overstated or mischaracterized

- **Where:** SPEC §§2.2–2.4 and §3; ADDENDUM §§1, 3.5, and 5.
- **Problem:** The addendum calls its polarity-only check “the same rule as the e2e fidelity gate,” although the e2e gate covered multiple dimensions and actually caught prospectivity loss. It says the cross-community pipeline supplies reusable guards even though its results ledger says Guard 2 was insufficient, Guard 3 was Sonnet-only, and Guards 5–6 were unbuilt. “MeSH 66→1→0; OLS 1488→0” conflates separate MeSH passes and implies all 1,488 OLS pairs were screened; only 18 of 524 low-cosine OLS pairs were manually examined.
- **Impact:** The addendum understates new work and makes the evidence base look broader and cleaner than it is.
- **Fix:** Replace these claims with the exact ledgers: distinguish polarity from full fidelity, list only guards actually reusable, and report the OLS sampling denominator explicitly.

## 15. A zero-survivor screening result cannot support the proposed structural conclusion

- **Where:** ADDENDUM §5.
- **Problem:** The document says zero surviving named alignment pairs would show that public post-LLM alignment vocabulary reconciles in corpora and weights “within months.” The cited attrition evidence concerns curated medical synonyms, and the proposed alignment candidate list is small and convenience-selected. Screening failures can also arise from embedder similarity, automated-probe error, or pair-selection failure.
- **Impact:** A local negative screen would be generalized into a field-wide temporal claim the experiment cannot establish.
- **Fix:** Scope a zero result to the frozen candidate frame, models, corpora, and screens. Treat broader reconciliation-speed claims as separate sampling studies.

## 16. “Earliest attested” still performs implicit credit adjudication

- **Where:** SPEC §2.6; ADDENDUM §2.
- **Problem:** The schema labels a single date/source as `earliest_attested` without a search ledger or coverage bound. Omitting a computed priority field does not prevent readers from treating the earlier displayed date as a priority result.
- **Impact:** The commons can make unsupported precedence claims while claiming structurally to avoid credit adjudication.
- **Fix:** Rename it `earliest_found_in_search`, store search scope/date/coverage and competing attestations, and explicitly prohibit priority inference.

## 17. The budget and sample plan are mutually incompatible

- **Where:** ADDENDUM §§6–7.
- **Problem:** Per-class typing accuracy across five verdicts, held-out evaluation, decoy precision, independent adjudication, and fork/version testing require multiple labeled pairs. The gate requires only one survivor and never fixes class counts. Even the table’s one-pair ranges sum to roughly 8–14 agent-hours before missing work; prior cross-community documentation estimated pair selection alone at half a day to a day.
- **Impact:** The quoted 8–12 hours cannot deliver the stated endpoints, and implementors cannot tell whether they are building a demo, calibration set, or evaluable study.
- **Fix:** Freeze minimum cases per class and separate prototype, calibration, and held-out phases. Re-estimate candidate acquisition, manual screening, gold-key construction, decomposition, wordlist enforcement, verifier development, and schema/fork testing independently.

# Next steps

1. Consolidate both documents into one normative revision with a single guard/hazard table and explicit precedence.
2. Repair the entailment rule, add abstention, and replace the deterministic relation table with provisional evidence-based typing.
3. Redesign immutable IDs, relation-specific artifact cardinalities, disputes, and lineage before implementing the emitter.
4. Separate discovery screening from relation-typing evaluation and freeze an independent balanced gold set.
5. Add the missing shared-core/residue generation and held-out evaluation stages.
6. Recalculate scope and estimates only after sample counts and acceptance criteria are fixed.