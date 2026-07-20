---
title: "Second-cell search — cross-cosine pre-filter (MeSH + cross-vocabulary) + memorization screen: no valid second cell in any curated-vocabulary pool, and why that is structural"
date: 2026-07-18
kind: addendum to 2026-07-17-cross-community-cell-RESULTS.md (follow-on: is there a valid SECOND cell?)
one_line: "Introduced a cheap Guard-0 pre-filter (bge cross-cosine between the two names — LOW = embedder does not already bridge = the regime the tool needs) and scanned MeSH (66 pairs) + a cross-vocabulary proxy via OLS4 (1488 pairs). MeSH: 12% low-cosine, ALL memorized → sweet spot empty. Cross-vocabulary: 35% low-cosine (3x MeSH) incl. obscure eponyms — but a memorization screen on 18 low-cosine pairs auto-flagged 14 sweet-spots that collapsed to 0 on READING (the model correctly bridges every eponym). Structural conclusion: named, curated synonyms are memorized BY CONSTRUCTION, so no curated-vocabulary pool yields a valid cell; the clean regimes are post-cutoff concepts (spec Guard 5) or private/local coinages (where the recall-backtest's C2 already worked)."
---

# Second-cell search — addendum

## Question

After the first cell (Photoreflexometry↔Photoplethysmography) returned a confounded null, is there a **valid second cell** available — a pair that is both **embedder-hard** (a low bge cross-cosine, so raw-term retrieval fails and the tool has room) and **opaque** (a frontier model does not already bridge the two names, so the tool is non-redundant)? And does the cross-vocabulary / UMLS route beat MeSH for finding one?

## Method (cheap, before building any corpus)

- **Guard-0 pre-filter:** bge-large cross-cosine between the two bare names. Reference points on this model: unrelated terms ≈ 0.51; the first cell's embedder-bridged pair = 0.750; racemic epinephrine↔racepinephrine = 0.859. "Low" (embedder-hard) ≈ < 0.65.
- **Scans:** MeSH candidate pairs (`scan_cross_cosine.py` → `cross_cosine_mesh.json`); cross-vocabulary proxy via EBI OLS4 (`scan_cross_cosine_ols.py` → `cross_cosine_ols_proxy.json`, junk URIs/codes filtered); true UMLS cross-SAB scanner built and ready for a UTS key (`scan_cross_cosine_umls.py`).
- **Memorization screen** on the low-cosine set (`screen_lowcosine.py` → `lowcosine_screen.json`): probe both names, stem-based bridge check.

## Results (numbers stored in the JSON files)

- **MeSH (66 pairs): sweet spot empty.** Only 8/66 (12%) are low-cosine, and all 8 are memorized eponym/descriptive pairs (Sprue↔Celiac 0.51, Grönblad-Strandberg↔Pseudoxanthoma 0.60, Kawasaki↔Mucocutaneous-Lymph-Node 0.65). The 3 memorization-survivors are all high-cosine (0.75–0.81). Low-cosine and opaque **anti-correlate** — entry-terms are one community's alternate names, so a name is either a famous eponym (low-cosine, memorized) or a morphological variant (opaque-ish, embedder-bridged).
- **Cross-vocabulary (OLS4 proxy, 1488 pairs): the low-cosine regime is populated — 3× MeSH.** 524/1488 (35%) are low-cosine, and unlike MeSH they include genuinely obscure eponyms (Fothergill↔trigeminal neuralgia 0.45, Verneuil↔hidradenitis 0.47, ceramide-trihexosidase-deficiency↔Fabry 0.48, bronze-diabetes↔hemochromatosis 0.48). So cross-source naming reaches the embedder-hard regime the tool needs.
- **But the memorization screen kills all of them.** On 18 low-cosine pairs (1 per concept), the automated check flagged **14/18 as sweet-spot** — a **false-positive artifact**. The stem-based bridge check calls a direction a "non-bridge" when the response does not echo the *other pair-term's exact root*; but for jangle pairs a model that fully knows the concept explains it with a **different** synonym (Verneuil → "hidradenitis," not the pair's "ectopic acne"), a root variant ("CRPS" vs the pair's "CRPS I"), or the pair is not a true synonym (EMT-the-process vs MET-the-gene). **On reading all 18 responses, the model correctly bridges EVERY pair** to its modern concept (Fothergill→trigeminal neuralgia, bronze diabetes→hemochromatosis, ceramide trihexosidase→Fabry, algoneurodystrophy→CRPS, Følling→PKU, Guam→ALS complex, Cerebroside Lipidoses→Gaucher, …). **Genuine sweet-spots after reading = 0.** (Same false-survivor failure mode as the Step-0 screen and the eggs/racepinephrine cases — automated opacity checks over-count; reading is mandatory. Measured ~3× this session.)

## Structural conclusion

**Named, curated medical synonyms are memorized *by construction*.** A pair only appears in MeSH/UMLS/OLS because someone named, documented, and cross-referenced it — the same property that puts it densely in the training corpus (the feasibility doc's "documented rediscoveries are memorized," now confirmed on cross-vocabulary eponyms too). So the tool's genuine value regime — **opaque × embedder-hard × real prior art** — is nearly disjoint from *any* curated-vocabulary pool: whatever is curated is findable, hence memorized.

The clean regimes that remain:
1. **Post-training-cutoff concepts** (the spec's Guard 5 temporal holdout) — non-memorization is *guaranteed*, not argued, and there is always a fresh frontier.
2. **Private / local coinages** — exactly where the recall-backtest's **C2 already worked** (a project's own opaque coinage "operating requirement" → value of information / Raiffa & Schlaifer, which the model did NOT bridge). This is the tool's demonstrable regime.
3. The obscure long-tail construct pairs behind **Larsen & Bong's INN test bed** (gated; email Larsen) — obscure enough to plausibly clear opacity, but not reachable pre-arrangement.

**Net for a second cell:** none is cheaply available from curated vocabularies (MeSH or UMLS/OLS), and a UTS key would not change this (true UMLS pairs are curated too, hence memorized). A valid public cell should be built from **post-cutoff** concepts; the tool's already-demonstrated value is on **private** coinages. The cross-cosine pre-filter (Guard 0) is a keeper regardless — it is the cheapest way to reject embedder-bridged pairs before spending on a corpus.

## Artifacts

`/mnt/f/src/minelit/flf-epistack/eval/cross-community/` — `scan_cross_cosine.py` + `cross_cosine_mesh.json`; `scan_cross_cosine_ols.py` + `cross_cosine_ols_proxy.json`; `scan_cross_cosine_umls.py` (ready for `UMLS_API_KEY`); `screen_lowcosine.py` + `lowcosine_screen.json` (with `CORRECTED_CONCLUSION`: 0 genuine sweet-spots after reading). Method memories: [[feedback_clean_testset_for_recall_tools]], [[feedback_reading_is_the_bottleneck]], [[feedback_unreviewed_artifact_assume_wrong]].
