# demo-collider — the vocabulary-seam operations on a second provided case

> **Post-submission demonstration (2026-07-20), labeled and dated.** The competition entry was submitted 2026-07-19 AoE; the as-submitted state is tagged [`flf-submission`](../../../tree/flf-submission), and ENTRY.md and the submitted Google Doc are unchanged. This directory adds nothing to the entry's evidentiary record and **changes no at-submission grade**.

This is a **demonstration of the entry's operations on parts of a second FLF-provided case — the LHC/collider safety case** — alongside the eggs case (prototype, §5.1) and the project's own record (§2). It is **demonstration-grade**: a handful of author-selected concepts, answer-aware wherever a result is scored, run on one corpus. It does **not** upgrade the §5 measurements, does **not** run the live-community evaluation §7 still owes, and makes **no new claim of retrieval superiority** (§5.3's negative stands). Its one purpose is to show the operations moving on a second case — the generalizability dimension both judge-simulations scored as the entry's weakest. For where a limited reading budget is best spent across the whole package, see [`../READING-GUIDE.md`](../READING-GUIDE.md).

## Why the collider case

The LHC micro-black-hole safety case is essentially **closed and uncontested**, so — per FLF's framing of it — the job is not to settle a controversy but to **probe the dependency structure and weakest points** of the reassurance. It is the sharper case for one reason: the safety arguments *look* maximally independent. They come from different sub-fields with different formalisms and vocabularies — theoretical Hawking-radiation/decay arguments, and empirical astrophysical bounds (cosmic-ray survival, white-dwarf and neutron-star survival). A reader counts several independent reassurances. **Vocabulary is the surface along which their real dependence structure hides.** And because the case is closed, the dependence structure has an **answer key**: this is a *validation* target (does the method recover a dependence physicists already established?), not a discovery target — which is the more checkable of the two.

*(COVID is deliberately excluded from this package by a standing instruction and does not appear anywhere here.)*

## The corpus and the three sides

Four documents — the two core CERN safety papers and two critiques — fetched, identity-verified against the arXiv abstract page, and split into three **argument-type sides** (not one paper per side; theory and bounds arguments coexist *within* the same papers). Full citations, provenance, hashes, and the two identity corrections caught at fetch are in [`corpus/manifest.md`](corpus/manifest.md); the section→side map is in [`corpus/sides.md`](corpus/sides.md). Full paper texts are **not committed** (copyright boundary, below); [`corpus/fetch.sh`](corpus/fetch.sh) reproduces the local working corpus.

- **Side A — theory:** black-hole production, Hawking evaporation/decay, the accretion *mechanism* (Giddings & Mangano §§2.1, 4, 5).
- **Side B — bounds:** cosmic-ray survival, white-dwarf and neutron-star bounds (LSAG §2; Giddings & Mangano §§2.2, 7, 8).
- **Side C — critique:** the physics objection (Plaga) and the methodology critique (Ord, Hillerbrand & Sandberg).

## The three components

Each has a hard scope cap, and each replicates the receipts + scoring pattern of `hook/example/` and `hook/example-scan/`.

### 1 · Scan (detect → curate) — [`scan/`](scan/)

One isolated detection call per side surfaced side-local vocabulary; ≤4 genuinely side-local terms per side were curated (`[x]` in the candidate files). **Precision by hand = 28/32** (four weak candidates, enumerated in `scan-notes.md`). The honest finding: unlike a project with invented jargon, this case's "idiolect" is mostly **established terms of art from different sub-communities** — so the sides have visibly distinct vocabularies, but most terms are *reconciled within their own fields* (memorized), which predicts (entry §5.2/§7) that the per-term check recovers owners cheaply. Full curation and honest assessment: [`scan/scan-notes.md`](scan/scan-notes.md).

### 2 · term-check (reverse-dictionary), scored — [`term-check/`](term-check/)

Four contamination-clean curated terms (excerpts contain none of the expected owner vocabulary — [`term-check/contamination-check.md`](term-check/contamination-check.md)), each checked by the isolated sonnet+opus `term-check.sh` from its own side's excerpts. Selection was answer-aware; the scored result is only whether the check **reproduced the predeclared owner**. **All 8 draws (4 terms × 2 tiers) reproduced the predeclared owner or its canonical family**, cheaply and from weights — which, on this reconciled seam, *confirms* the entry's §5.2/§7 prediction (established vocabulary is memorized, so the hook is largely redundant) rather than showing a new capability. Two results are worth noting descriptively, not as discovery: **`macroscopic absorption`, a *bounds*-side term, reproduced *Bondi accretion* — the *theory*-side mechanism** (a term whose owner sits on the other side of the seam, consistent with the dependence component 3 tests properly); and `multiple bounds argument` (the critique's own name for "several safety arguments, each sufficient") reproduced *defense-in-depth / convergent evidence* — the same independence-of-evidence vocabulary the entry's diagnosis uses. Scored table and Hit criterion: [`term-check/scoring.md`](term-check/scoring.md).

### 3 · Cross-side matching: definition generation + usage-based verification (the §5.5 shape) — [`cross-side/`](cross-side/)

The dependence-structure component. For each of two concept pairs: per-concept community-neutral definitions are generated live (isolated) — the §4.1 stage-2 artifact, showing the vocabulary stripped — and then **pairwise verification runs on the two concepts' raw *usage* excerpts** (isolated sonnet+opus, blind: not told the passages share a case), emitting the entry's three artifacts: **typed SKOS relation · shared core · per-side residues**. Verification is usage-based per §5.5 (two definitions through one wordlist resemble by construction), so the generated definitions are *not* the matching key in this cell; retrieval-by-definition is §5.1's separate measurement and is not re-run here. The pairs are hand-selected, so this exercises the verify/type stage on a given pair, not discovery of the pair. The two cells were chosen to have known-*opposite* answers:

- **Cell 1 — accretion-growth mechanism (theory) × white-dwarf survival bound (bounds).** Answer key (the only independently-keyed part): **dependent** — Giddings & Mangano *derive* the bound from the accretion model; §4.1 even forward-references that "we will also perform similar calculations for accretion of white dwarfs and of neutron stars" (this sentence was withheld from the verify excerpt to keep the judgment blind). **Result: both draws found the dependence** — the shared accretion rate law dM/dt ∝ r_c²·F. As model outputs beyond the answer key (illustrative, not independently keyed), both typed it `broadMatch` — directed, `P2 skos:broadMatch P1`, i.e. P1 (the general mechanism) is the broader concept, per the entry's subject-is-narrower convention (§4.1) — and opus additionally separated out a part that is *independent*: the empirical "a comparable body survived, so we survive" inference layered on top of the shared core.
- **Cell 2 — Hawking-evaporation/decay (theory) × cosmic-ray survival (bounds).** Answer key: **not a shared premise** — these are complementary alternative arguments (black holes decay, *or* if stable they are stopped); this cell is the designed control against over-merging "both about safety" into "shared core." **Result: both draws returned NONE** ("a topical resemblance, not a shared load-bearing premise"); the relation label splits `NO-MATCH` (sonnet) / `relatedMatch` (opus) — agreeing on substance, differing on the fine label. On this control pair the operation did not manufacture a shared premise.

Full three-artifact record, both draws, and the honest scoring: [`cross-side/RESULTS.md`](cross-side/RESULTS.md).

## What this is, and is not

- **Is:** a worked demonstration, with receipts, that the entry's detect / check / define-then-verify operations run on parts of a second provided case, and that on this case they behave as the entry's own framework predicts — cheap owner-recovery on a reconciled seam, and, on an answer-keyed pair, a recovered *dependence* between two reassurances that a reader counts as independent.
- **Is not:** a recall estimate, a retrieval-superiority claim, the live-community §7 evaluation, or any change to the §5 record or an at-submission grade. Same-family (sonnet+opus) draws are a *correlated* read: convergence is weak evidence, divergence informative. Where a result is scored, the corpus is answer-aware and the case is closed, so the scoring is validation against a known answer, not discovery.

## Copyright boundary

The four papers' full texts are third-party copyrighted works and are **not committed**. Committed instead: the corpus **manifest** (URLs, versions, sha256, fetch dates), a **fetch script** that reproduces the local working corpus, and the **paragraph-level excerpts the tools actually consumed** (term-check's frozen excerpt files; the cross-side cell's frozen usage excerpts). The bulk-prose scan detection prompts and the full texts are gitignored. This is analysis-grade quotation, not redistribution.
