# Committed example — `term-scan` run on this repo's own prose (2026-07-20)

Self-application of **scan mode** (`hook/term-scan.sh`): point the scanner at this project's prose, let it surface candidate coinages, curate, and check the kept ones into a seed glossary. Everything the two phases produced is committed here: the detection prompt and manifest with hashes (`.term-check/scan/`), the surfaced candidate list with the curation marks (`scan-candidates.md`), the per-term isolation manifests and raw draws (`.term-check/manifests/`, `.term-check/prompts/`), the instrumentation log (`.term-check/log.jsonl`), the assembled seed (`GLOSSARY-SEED.md`), the verbose per-draw flags (`term-flags.md`), and the term-selection contamination check (`contamination-check.txt`).

**This is a worked example with receipts, not a recall estimate.** The entry's §5 measurements (and their negatives) remain the evidentiary record; nothing here upgrades them. Scan's model-assisted detector is a *different* detector from the prototype's (which missed its one retrospective coinage endpoint, §5.3) and this run does not claim to fix that record.

## Protocol

From the repo root:

```
# phase 1 — detect (one isolated model call), writes scan-candidates.md, STOPS:
export TERM_CHECK_STATE=hook/example-scan/.term-check
bash hook/term-scan.sh --detect-model sonnet --max-words 18000 \
  -o hook/example-scan/GLOSSARY-SEED.md --candidates hook/example-scan/scan-candidates.md \
  --flags hook/example-scan/term-flags.md ENTRY.md receipts/*.md
# ... curate: mark [x] the terms to check (here: transparency gradient, the commons, misroute document) ...
# phase 2 — check the [x]-marked terms, assemble the seed:
bash hook/term-scan.sh --check -m sonnet \
  -o hook/example-scan/GLOSSARY-SEED.md --candidates hook/example-scan/scan-candidates.md \
  --flags hook/example-scan/term-flags.md ENTRY.md receipts/*.md
```

**Input and its deliberate exclusions.** Detection input was `ENTRY.md` + `receipts/*.md` — 7 files, 37,015 words, evenly downsampled to 15,885 (231 of 479 paragraphs) under the enforced 18k-word cap (manifest: `.term-check/scan/*-detect-manifest.txt`). `GLOSSARY.md`, `PSEUDOCODE.md`, and `hook/` were **excluded from the input**: each enumerates the coinages *as* coinages, which is answer-key contamination for a detection test. `GLOSSARY.md` is instead used *after the fact* as the answer key for scoring below.

## Phase 1 — what detection surfaced, scored by hand against `GLOSSARY.md` §A

15 candidates returned (`scan-candidates.md`). Scoring them against the 16 coinage headwords in [`GLOSSARY.md`](../../GLOSSARY.md) §A, as a free-recall test:

| Bucket | Candidates | Count |
|---|---|---|
| **§A headword hits** | idiolect trap, de-idiolection, transparency gradient, the commons | 4 |
| **§A partial** | misroute document (→ §A's *misroute*) | 1 |
| **§A "Program A/B" retracted coinages** (named inside §A's Program-A/B row) | the audit unit (m\*), operating requirement, "the signal, not the cut…" | 3 |
| **Genuine coinages, off the §A key** (from the case-study receipts) | coin-time tax, novelty ledger, self-application blind pass, quantity-role substitution, decision-sensitivity | 5 |
| **Weak** | minelit (a project *codename* — a proper name that should have been excluded), read the enumerations (vague) | 2 |

- **Precision by hand ≈ 13/15**: thirteen candidates are genuine project-local coinages/terms (from the entry or the case study); two are weak (`minelit` is a proper codename, a real precision miss; `read the enumerations` has a vague gloss). This is high — but note one input file, `receipts/idiolect-trap-case-study.md`, is itself a *graded term ledger* of the case-study's coinages, so that batch was partly handed to detection. The §A answer key is a *different* set (the entry's own coinages) and is **not** enumerated anywhere in the input, so the §A recall figure below is uncontaminated even though the precision figure is flattered.
- **§A recall is modest — ~4–5 of 16 headwords.** The eleven §A terms detection *missed*: vocabulary seam, confident null, opaque coinage, owner/owning literature, era-gated excerpts, fidelity gate, key/representation split, peer reconciliation, key (§5.5), Program A/Program B, coin-time. Two reasons, both instructive: (1) the ~57% paragraph downsample dropped much of ENTRY.md, where several of those terms are defined; (2) the receipts are dense with the case study's opaque, retracted coinages (m\* / "the audit unit", operating requirement, "the signal, not the cut", quantity-role substitution…), which are *legitimately* the most "project-local-looking" strings in the input, so a "most-local-first, top-15" detector surfaces them ahead of the entry's more transparent terms (vocabulary seam, owner).

**The honest reading:** the raw list mixes answer-key coinages, real-but-off-target coinages, and two weak ones (including a proper codename that slipped the "exclude proper names" instruction). That mix is exactly why phase 1 stops for curation and phase 2 spends draws only on `[x]`-marked terms — the surfacing is a convenience, not a measurement.

## Phase 2 — the checks on the three curated terms

Curated 3 of 15 (`[x]` in `scan-candidates.md`), sonnet-only. Term selection was answer-aware and the criterion is committed (`contamination-check.txt`): the chosen terms' frozen excerpts contain **none** of their `GLOSSARY.md` owner vocabulary (a hit would prove nothing). Three considered terms were **excluded** for the opposite reason — their excerpts state their owner or evaluation vocabulary verbatim (`operating requirement`, `quantity-role substitution`, `self-application blind pass`), shown in the receipt.

| Term | `GLOSSARY.md`'s expected owner | sonnet draw's top candidate(s) |
|---|---|---|
| `misroute document` | *misroute*: vocabulary-mismatch retrieval failure (IR); early IR's **"false drop"** | **Hit**: "**False drop** (information retrieval)" as the first candidate, then hard negative / false match / distractor. |
| `the commons` | pay-as-you-go data integration / **dataspaces** (Franklin, Halevy & Maier 2005); **emergent semantics** (Aberer 2004) | **Right neighborhood, not the exact citation**: "knowledge commons", "ontology/schema-alignment repository", "terminology crosswalk / term bank", "wiki-style versioned knowledge base with forking (CSCW / distributed systems)". Recovers the *shape* (shared, versioned, non-authoritative, forkable) without naming dataspaces/emergent-semantics — exactly the case where opening a primary (or the entry's define→match step) is what would confirm the owner. |
| `transparency gradient` | semantic transparency / compositionality (lexicology) | **Hit (cheap)**: "Semantic transparency", "term transparency / motivation", "motivated vs. arbitrary sign", "the vocabulary problem". A *transparent* coinage — its surface word "transparency" overlaps the owner — so recovery is easy by construction; that is the transparency-gradient finding (§2) applied to itself. |

`misroute document` recovered the answer-key owner exactly; `transparency gradient` recovered it cheaply (as expected for a transparent coinage); `the commons` recovered the right *family* but not the exact owner citation — the honest middle case. Every candidate in `GLOSSARY-SEED.md` is labeled **UNVERIFIED** — the seed is model-proposed names, not checked mappings, and the next step for any candidate you rely on is to open one primary.

## How to read this

- A 3-term, author-selected, answer-aware demonstration of the detect→curate→check→seed loop and its receipts — **not** a recall estimate. The `GLOSSARY-SEED.md` entries match `glossary-watch.py`'s entry regex, so the seed can itself be watched (scan → seed → watch closes the loop the hook needs on a project that started with no glossary).
- Detection was run once (`sonnet`, isolated-from-config). A different draw would surface a different top-15; the point of the two-phase gate is that this variance costs a curator's glance, never a wasted naming draw or a junk glossary entry.
- The committed detection receipt (`.term-check/scan/*-detect-prompt.txt`, with its `sha256` in the manifest) is the exact, frozen input the detector saw; the assembled pre-prompt input is not separately committed because it is byte-embedded in that prompt.
