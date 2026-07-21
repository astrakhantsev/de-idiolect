# Component 1 — per-side scan (detect → curate), scored by hand

**This is a worked demonstration with receipts, not a recall estimate.** The entry's §5 measurements (and their negatives) remain the evidentiary record; nothing here upgrades them or changes an at-submission grade. Scan's model-assisted detector is the entry's weakest measured component (the prototype's own keyness detector missed its one retrospective endpoint, §5.3); this run does not claim to fix that record — the curation gate exists precisely because surfacing is heuristic.

## Protocol

Three isolated detection calls (sonnet, isolation-from-config: fresh cwd + credentials-only HOME + pinned `CLAUDE_CONFIG_DIR` + all tools disallowed), one per side, over the prose-only side files (`../corpus/_work/side{A,B,C}-prose.md` — the papers' own section headings and the assembled provenance tags stripped, so heading text cannot pre-name a concept). Each side is well under the 18k-word cap, so input is full (no downsampling). Receipts committed here: the three candidate lists with curation marks (`side{A,B,C}-candidates.md`) and the prose-free detection manifests (`manifests/`, each recording the input path, word counts, sampling, prompt `sha256`, and isolation policy). The bulk-prose detection *prompts* are gitignored (`.term-check-scan/`) — they embed the papers' text.

## What detection surfaced, by side

| Side | Input words | Candidates | Character of the list |
|---|--:|--:|---|
| A — theory | 2,998 | 7 | accretion-mechanism vocabulary: *capture radius*, *accretion slow-down*, *perfect accretion*, *subatomic growth*, *Coulomb slow-down*, *electromagnetic capture radius*, *capture regime* |
| B — bounds | 3,953 | 12 | compact-star stopping/bound vocabulary: *crust penetration time*, *gravitational drift velocity*, *neutron-fluid region*, *macroscopic absorption*, *Schwinger discharge*, *binding/neutralization event*, *slowing distance*, *sub-escape velocities*, … |
| C — critique | 5,999 | 13 | two registers: mBH physics (*quasistable*, *mBH*, *scenario 3*, *subatomic accretion mechanism*) and risk methodology (*grey area*, *multiple bounds argument*, *theory failure*, *model failure*) |

**Precision by hand = 28/32** (four weak candidates, enumerated). The four rejected: a rhetorical device counted as a term (*LHC experimental programme* — the "Nature ran ~10³¹ LHC programmes" framing) and a generic descriptor (*geometric size*), both side B; one detector gloss that reads as a coinage but names a standard effect (*trans-horizon effect* for Hawking radiation, side B); and a bare abbreviation (*mBH*, side C). The other 28 are genuine side-local terms of art. (Side A: 7/7 genuine; side B: 9/12; side C: 12/13.) That mix — mostly genuine, a few weak — is exactly why phase 1 stops for curation.

## The honest reading — this case has few *coinages*; it has cross-field *terms of art*

Unlike a project with invented jargon (the eggs/entry cases), the LHC-safety literature's "idiolect" is mostly **established vocabulary from different sub-communities** — general-relativity/Hawking theory, stellar astrophysics, nuclear astrophysics, and decision theory. The detector surfaced these as "project-local" because each is local to *its own sub-field*, not because the project coined it. Three consequences, all of which the entry already predicts:

1. **The three sides do have visibly distinct vocabularies** — which is the premise of the whole seam argument: a reader crossing from the theory argument to the bounds argument to the critique is crossing three lexicons.
2. **Because most terms are established (reconciled within their fields, hence memorized), the per-term check should recover owners cheaply** — a *reconciled seam* where the hook is largely redundant (entry §5.2: curated/established vocabulary is memorized by construction; §7: the tool's value concentrates on unreconciled seams). Component 2 tests this directly and, honestly, mostly confirms it.
3. **The value here is not in the hook but in the cross-side dependence** between the sides — that a bounds-side reassurance and a theory-side mechanism rest on the *same* Bondi-accretion premise, packaged as two separately-counted reassurances. (In this corpus the two sides even share the word "accretion" — a *reconciled* seam, not two disjoint lexicons; the demonstration is that separate packaging invites double-counting despite shared terms. See the cross-side RESULTS.) That is component 3, not this scan.

## Curation

Marked `[x]` the ≤4 most genuinely side-local terms per side (12 total; see the candidate files). Component 2 (`../term-check/`) then runs the isolated reverse-dictionary check on the subset whose usage excerpts are **contamination-clean** (contain none of the expected owner's vocabulary — a hit would prove nothing). Two curated side-C terms, *quasistable* and *grey area*, were **excluded from scoring** because their excerpts name the owner outright (*quasistable*'s paragraphs say "metastable"; *grey area*'s say the argument may be "flawed"/"unsound") — recorded in `../term-check/contamination-check.md`. A third strong side-C candidate, *multiple bounds argument*, is clean and is the most on-theme term in the whole corpus (it is the critique's own name for "several safety arguments that cover for each other" — the independence question the demonstration is about), so it is scored.
