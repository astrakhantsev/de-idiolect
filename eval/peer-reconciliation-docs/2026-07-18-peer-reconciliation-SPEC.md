---
title: "Peer reconciliation — de-idiolection between two live idiolects with no canonical owner (design spec + cell sketch)"
date: 2026-07-18
status: "DESIGN DRAFT — NOT BUILD-READY. Joint Codex review with the completion addendum (2026-07-19): MAJOR REVISION, 17 findings — including an entailment-direction reversal between the two docs (this SPEC's §2.4 definition⇒usage vs the addendum's usage⇒definition), non-immutable crosswalk IDs, gameable decoy calibration, and a discovery-vs-typing screening conflation. Revision required before any build (full review text: `2026-07-19-peer-reconciliation-REVIEW.md`; the addendum's status line carries the summary list). Still the FLF continuation-work design, in the entry §8's candidate clean regime."
relates_to: "entry/FLF-entry-recall-extender.md §3–§4, §8 · 2026-07-17-cross-community-cell-build-spec.md (guards reused) · 2026-07-16-definition-mediated-naming-EXPERIMENT.md (§7.3-iii round-trip lesson) · 30_reference/novelty-protocol.md (Pass-A blindness, applied at the definition layer) · 2026-07-18-e2e-cell-SPEC.md (the anchoring-regime sibling)"
---

# Peer reconciliation — the no-canonical regime

## 1. Two regimes, and why this one is different

Everything tested so far is **anchoring**: a private coinage maps to an *established* owner (decades old), so verification has a ground truth — the owner's primary texts — and translation has a privileged direction (toward the established vocabulary). The untested regime is **peer correspondence**: two live idiolects (e.g., two alignment groups whose directions only exist post-LLM, a few years old) name overlapping concepts, and **no canonical vocabulary exists for either to defer to**. Differences that change the design:

- **No ground truth.** Verification cannot check against "the field's text" — there isn't one. It must be *bilateral*.
- **No privileged direction.** Neither term is "the right one." Any output that crowns a winner is a canonical merge — the thing the architecture forbids — and in live fields it also adjudicates *credit*, which the tool must refuse to do.
- **Partial overlap is the modal case.** Recent parallel coinages rarely denote identical concepts; they overlap with residues. `skos:exactMatch` will be rare; the interesting output is the decomposition.
- **The jingle risk goes live.** Two groups using *similar* surface framings for genuinely different things is as likely as different names for the same thing. The verifier needs a first-class "no match, despite similarity" verdict.

## 2. The operation (pipeline extension; field terms: this is definition-mediated ontology alignment, lazy, with no merged resource — alignment/matching is ceded to the ontology-matching literature; the deltas are the independence control, the residue decomposition, and the refusal to canonicalize)

1. **Detect** in each community independently (candidate-term surfacing over each corpus, as in the anchoring pipeline).
2. **Generate independently — the critical control.** Community A's constrained definition is generated from A's texts only, by a runner blind to B's corpus and vocabulary; likewise B. One generator seeing both corpora would converge the definitions artificially and *manufacture* the match it is supposed to test — this is the novelty protocol's Pass-A blindness applied at the definition layer, and it is non-negotiable. (Shared-model correlation remains even with separated contexts — note it as a residual confound; cross-family generation for the two sides is the cheap mitigation.)
3. **Cross-retrieve bidirectionally.** A's definition as a query over B's corpus, and B's over A's. One direction succeeding and the other failing is itself informative (asymmetric coverage → broad/narrow candidates).
4. **Verify bilaterally, round-trip, twice.** (a) Does A's definition entail B's *usage* (checked against B's frozen excerpts, not B's definition)? (b) Does B's definition entail A's usage? The 07-16 polarity-inversion failure (a generated definition silently flipping a claim's direction) is the named hazard; the round-trip check runs per side. Verdicts: exact / A-broader / B-broader / partial-overlap / **no-match-despite-similarity** (the jingle verdict) — each with quoted usage evidence.
5. **Emit three artifacts, never one term:**
   - the **typed link** (SKOS relation + the verdict evidence),
   - the **shared-core definition** — a constrained definition both communities' excerpts satisfy (the manufactured boundary object; it *supplements* both terms, replaces neither),
   - the **residues** — what A's concept covers that the shared core doesn't, and B's likewise, each written in the constrained vocabulary.
6. **Provenance without adjudication.** Both terms' earliest attested uses, with dates and sources, recorded as data. No priority claim is computed or implied. Disputes (either community rejecting the mapping) are first-class typed links in the commons layer, not resolutions.

## 3. Test-cell sketch (the fundable evaluation)

**Domain:** post-LLM alignment vocabulary — recent enough that canonicals are absent, rich in genuinely-parallel coinage, and squarely in the entry §8 candidate clean regime (post-cutoff / genuinely-parallel).

**Pair selection (guards reused from the cross-community pipeline, which was built for exactly this screening):**
- **Co-citation / co-mention screen:** famous pairs are reconciled-in-corpus (e.g., goal misgeneralization ↔ objective robustness cross-cite in their founding papers) — screened OUT. Expect heavy attrition; that is the screen working.
- **Memorization probe (Guard 3 pattern):** ask clean-harness models about term A alone; if B or B's community surfaces, the pair is bridged in weights — OUT (or retained only for the *rescue* framing, not the discovery framing).
- **Guard 0 cross-cosine:** if the embedder already bridges the two term strings, the tool is redundant on that pair — OUT.
- **Promising strata after screening:** forum-idiolect vs academic-idiolect for the same recent concept (Alignment Forum / LessWrong coinages vs arXiv phrasings, often weakly cross-cited); lab-internal blog vocabulary vs external academic naming; post-cutoff concepts (Guard 5 pattern) as the renewable clean source.
- Candidate pairs to *screen, not assert*: activation steering ↔ representation engineering; scheming ↔ deceptive alignment; eval-gaming ↔ sandbagging (likely relatedMatch-with-residues, a good decomposition test rather than an exactMatch test). Every candidate goes through the screens before use; listing here is not evidence of validity.

**Endpoints (to be frozen at build time, chance-adjusted per the cross-community lessons):** bidirectional retrieval ranks vs chance and vs raw-term queries; verifier verdict agreement with a human-adjudicated key on a small held-out set; residue quality scored blind by each community's own texts (does the residue retrieve A-only content?). Equal-information frontier baseline throughout (hand both corpora to a frontier model, ask it to align the vocabularies directly) — the marginal-value question is the same as the anchoring regime's and must be answered against the same rising baseline.

**Known hazards to design against (from this project's own record):** artificial convergence via shared generator (mitigate: cross-family generation per side); polarity inversion (round-trip check per side); jingle false-positives (the no-match verdict must be reachable and rewarded in the verifier's instructions); curated-pair memorization (screens above); threshold-at-chance endpoints (pre-register with explicit chance baselines).

## 4. What this is not

Not a canonical merge, not a terminology standard, not a credit adjudicator, and not built. It is the design for the second regime of the same operation the FLF entry proposes for the first — written down while the constraints are fresh, to be reviewed and (if the continuation materializes) built as the funded evaluation.
