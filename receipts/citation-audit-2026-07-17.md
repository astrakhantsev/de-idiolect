---
title: "Citation audit — FLF recall-extender entry"
date: 2026-07-17
one_line: "Verified the entry's load-bearing verbatim quotes/claims against primary text after a fabricated quote was found in §1. Result: ONE fabrication (Larsen & Bong recall figure, now fixed); all 16 other checks across §1/§2/§3/§5 verified. Method: 4 blind subagents, bare-safefetch + Wayback for blocked primaries."
---

# Citation audit — FLF recall-extender entry (2026-07-17)

Triggered when, while reading the Larsen & Bong 2016 primary for the construct-identity dataset question, the orchestrator noticed a §1 quotation that did not match the paper. Because one fabricated "read in full" quote implies the batch is suspect, all load-bearing verbatim quotes/claims were audited against primaries by four blind subagents (bare `safefetch`, Wayback for blocked primaries, per-item verdicts, exact source text required).

## The one real defect — FIXED

**§1, Larsen & Bong 2016.** The entry quoted, verbatim, that PhD students "found relevant articles containing a specific construct 'on average only 9% of the time, and relevant articles containing a pair of common constructs on average only 3% of the time.'" **That sentence is not in the paper.** What the paper actually says (verified, pp. 544–545): participants using full-text search (EBSCO) "retrieved 9% of the relevant constructs" on average; per-task recall ran as low as 3%; and the meta-analytic follow-up found "83% of participants would arrive at the conclusion that the relationship had not been tested at all." The 9% is real but was re-framed and wrapped in quotation marks the authors never wrote. **Fixed in §1** with the verified language, plus two genuinely-new assets from the same primary (the explicit Swanson extension, and the Table B1 warning that construct meaning is not predictable from names).

## Verified clean (primaries opened)

- **§1 empirical backbone — 4/4 MATCH.** Blair & Maron 1985 (the 75% recall stipulation / ~20% measured recall / ~80% precision quotes, all verbatim); Furnas et al. 1987 (the .07–.18 range, confirmed off the results-table page image after OCR garbled the decimals); Kelley 1927 (coins "jangle," pp. 63–64); Thorndike 1904 (credits Aikins for "jingle," p. 14).
- **§2 graveyard essays — 6/6 MATCH.** Hoekstra 2010 ("a continuous relation of trust"; knowledge-reengineering bottleneck; extends Feigenbaum's acquisition bottleneck); Doctorow "Metacrap" ("People are lazy" / "People lie"); Shirky 2003 ("you can't force an agreement to exist where none actually does").
- **§3 sociology + Relink — 3/3.** Star & Griesemer 1989 (coined "boundary objects"; cooperation-without-consensus faithful — PARAPHRASE-OK); Bowker & Star 1999 ("there is no such thing as a natural or universal classification system," verbatim, p. 131); Relink (arXiv:2601.07192 resolves; title/authors/Jan-2026 date and the reason-and-construct-over-build-then-reason characterization all confirmed).
- **§5 method claims — 8/8 identifiers resolve, descriptions accurate.** SciCo-Radar (2409.15113), GenOM (2508.10703), EDC (2404.03868, Zhang & Soh), KGGen (arXiv:2502.09956, NeurIPS 2025 — "aliases that Wikidata uses" quote and its EDC citation both confirmed), Guo (2311.09481), NeoN (2505.15426), Microsoft patents US8589791B2 / US10552522B2.

## Minor precision line-edits applied (§5)

- "SciCo-Radar" is our shorthand, not the paper's title (real title: Forer & Hope) — clarified in-line.
- NeoN is *neologism* (new-word) detection in Polish, not novel-*sense* detection — corrected (it supports the "new lexical item → generated definition" pattern, but is not strictly novel-sense; AXOLOTL'24 carries the novel-sense claim).
- The two Microsoft patents are one continuation family (the '522 continues the '791), not two independent efforts — corrected.

## Net

One fabrication (now fixed); every other load-bearing citation verified against primary text. The entry's citation integrity is sound. The fabrication pattern matches the project's standing lesson ([[feedback_reading_is_the_bottleneck]]): an unverified "read in full" quote had been inherited and hardened; opening the primary caught it.
