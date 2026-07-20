# Pre-registration — one cross-community cell (interpretation contract)

**Frozen: 2026-07-17, BEFORE any retrieval number was seen.** This file is written after the
corpus + guards are built (Step 1) but before `run_cell.py measure` (Step 3) is ever run. The
contract below is fixed; the numbers are not yet known. Per [[feedback_recipes_die_on_transfer]]
and the build spec §2.

## What is being measured

For a chosen A↔B synonym pair (same MeSH concept, two lexically-dissimilar community names),
a query is generated from ONE side's docs only (blind to the other side) and we measure how
well each query form reaches the OTHER side's documents in the frozen corpus
`C = docs_A ∪ docs_B ∪ distractors`. Both directions (A→B, B→A) are run.

Query forms per direction (built from the source side, term forbidden where noted):
`raw_term` (floor) · `jargon` (control) · `neutral` (candidate) · `raw_term_far` (ceiling) ·
`naive_question` (floor). Generated arms: k=3 samples × {sonnet, opus} = 6 draws per arm per
direction.

**Primary metric:** `rank_first_target` (rank of the first far-community doc; lower = better)
and `recall_at_10` of the far community's docs. **Primary condition:** `clean` (cross-term
docs removed from corpus and target — see below); `inclusive` reported alongside, never
instead.

**The dual condition (folded in per the co-mention design note).** Every doc is tagged
`contains_other_term`. We report cross-community reach in two conditions:
- **inclusive** — full corpus, target = all far-side docs.
- **clean** — docs containing the *other* side's term removed from corpus AND target.
The dangerous leak is term A appearing in a `docs_B` target: it lets the `raw_term_A` floor
reach B by surface match and fakes lift. The primary read is on `clean`; a large
inclusive-vs-clean gap is itself reported as evidence of lexical bridging, not smoothed over.

## The four pre-committed verdicts (read on the `clean` condition, both directions)

1. **NEUTRALITY SUPPORTED** — iff `neutral` reaches the far docs at a better
   `rank_first_target` than **both** `raw_term` and `jargon`, in **both** directions, with the
   bootstrap CI on `neutral − jargon` and `neutral − raw_term` excluding 0. This is the entry's
   thesis measured cross-community for the first time.

2. **NEUTRALITY IS NOT THE LEVER (semantics suffices)** — iff `jargon ≈ neutral` at reaching
   the far docs (CI on `neutral − jargon` includes 0) while **both** beat `raw_term`. Honest
   negative: the *definition* (specificity) helps, but the *vocabulary constraint* adds no
   cross-community reach. This is a fully acceptable, publishable outcome.

3. **PAIR WAS RECONCILED / TOOL REDUNDANT** — iff even `raw_term` reaches the far docs well
   (e.g. `rank_first_target` ≤ 3 or `recall_at_10` ≥ 0.5 for the raw term). Means Guard 2/4b
   failed: the communities already share vocabulary or citations. **Discard the cell; do not
   report it as a tool result.** (Also pre-flagged if Guard 2 shows any direct A↔B citation or
   reference-Jaccard > 0.15, or the Guard 4b co-mention doc-rate > 0.34 on either side.)

4. **NULL / UNDERPOWERED** — iff nothing separates and the far docs are unreachable by ANY
   query including the `raw_term_far` ceiling (ceiling `rank_first_target` > 10 or
   `recall_at_10` < 0.3). Means corpus construction failed (far docs aren't retrievable at
   all); fix the corpus, not the interpretation.

## Scope commitment (frozen)

- **n = 1 pair is a DEMONSTRATION, not a benchmark.** It can show the mechanism exists (or
  fails) on one genuine cross-community pair; it CANNOT estimate an effect size. Report only as
  "the mechanism does / does not appear on one genuine cross-community pair." The claim-grade
  version is many pairs (the funded eval).
- Bootstrap: seeded (`BOOT_SEED=0`), 5000 resamples, 5th/95th percentile. With 6 draws per arm
  the CIs will be wide; that width is honest and is reported, not hidden.
- The generated queries are frozen in `queries.json` before scoring; scoring is deterministic
  and offline. Query-level leak flags (`leaks_own_term`, `leaks_far_term`) are reported per
  draw; any `neutral` draw that leaks the far term is a generation failure and is called out.
- No metric, threshold, or condition in this file may be changed after seeing a number. If the
  result is ambiguous between verdicts, it is reported as ambiguous, not forced.

## Chosen pair (filled at freeze, still before retrieval)

- **term_a = "Photoreflexometry"  ·  term_b = "Photoplethysmography"** (same MeSH descriptor
  D019260 [**factual typo — corrected post-freeze to D017156 / NLM 68017156**; identifier only,
  no threshold or verdict changed]; lexical overlap 0.0). Selected from Step 0: 66 lexically-dissimilar candidates → 4
  nominal memorization-screen survivors → **only 1 genuine opaque coinage** on reading the
  screen responses (the other 3 were false survivals: the model fully explained the concept
  and the whole-token leak check simply missed it). Photoreflexometry is the strong case: the
  blind model **misroutes** it to "pupillary light reflex measurement / Soviet ophthalmology"
  when the concept is actually optical blood-volume measurement (the pulse-oximeter signal) —
  the ideal opaque-coinage-over-non-obvious-prior-art regime ([[feedback_clean_testset_for_recall_tools]]).
- **Selection-by-reading is itself a finding, pre-committed here:** the automated screen
  verdict (4/66 SURVIVE) OVER-counts; the honest survivor count after reading responses is
  1/66. The write-up must report both numbers.
- **Known limit, acknowledged before retrieval:** term A ("Photoreflexometry") has ~7 PubMed
  tiab papers total (vs ~100 for term B), so `docs_A` will be SMALL and possibly partly
  non-English/abstract-less. This is a thin, asymmetric demonstration cell. If `docs_A` yields
  < 4 usable docs, the cell is reported as UNDERPOWERED on the A-side rather than stretched.
- Guard 2 (citation reconciliation) verdict: **INSUFFICIENT DATA** — docs_A = 4 (all older
  French phlebology papers), 0 of which have OpenAlex reference lists; docs_B = 4 with refs.
  Citation-disjointness is therefore UNESTABLISHED (as anticipated). No cross-citation was
  found, but with 0 A-side reference data that is not evidence of disjointness. The cell rests
  on the memorization-misroute + co-mention signals, not on Guard 2.
- Guard 4b (co-mention census) verdict: **LOW (0.25 on A-side)** — 1 of 4 docs_A contains
  "Photoplethysmography" (4 mentions); 0 of 10 docs_B contain "Photoreflexometry". Below the
  0.34 discard threshold, but NON-trivial: the primary read is the `clean` condition, and the
  inclusive-vs-clean gap on that one bridging A-doc is reported explicitly.
- **Corpus recorded facts (frozen):** docs_A=4, docs_B=10, distractors=8 (22 docs). docs_A is
  thin and single-subfield; per the underpowered rule this is at the n=4 floor and is reported
  as a thin, asymmetric demonstration, not an effect size.
- If either guard says RECONCILED, verdict 3 fires and the cell is discarded pre-retrieval. If
  Guard 2 says INSUFFICIENT DATA (too few docs with OpenAlex references — likely here given the
  thin, older Photoreflexometry literature), citation-disjointness is reported as
  **unestablished**, and the cell rests on the memorization-misroute + co-mention signals only.
