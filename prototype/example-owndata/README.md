# example-owndata — a worked run of recall_extender.py on non-eggs material

**Post-submission addition (2026-07-23), labeled and dated.** The competition entry was submitted 2026-07-19 AoE; this directory adds nothing to the entry's evidentiary record and changes no at-submission grade. It exists to show that `recall_extender.py` (the §5.1 prototype) runs on material other than the shipped eggs corpus, using the `--corpus`/`--concepts` flags added the same day (see `../README.md`'s "Post-submission addition (2026-07-23)" section for the flags and schema).

## What this is, and is not

- **Is:** a real, deterministic, offline run of the same pipeline as the eggs demo, over a different 13-document corpus, showing the `--corpus`/`--concepts` interface works end to end and produces a sane result.
- **Is not:** a new measurement, a bigger or better replication of the eggs routing-gain result, or evidence for anything beyond "the interface runs on this data." The corpus is small (13 short documents, 2 communities), hand-built by the same person who wrote the concept definitions, and the owning-community label for each concept was read directly off the source paper's own section structure (see `corpus.json`'s per-document `source` fields) rather than checked against an outside judge. Treat every number below the same way the eggs demo's own README treats its numbers: a worked example, not a validated result.
- Stage 1 (detect) is not wired into the three concepts below. Stage 2 (define) used **hand-authored** definitions (see `concepts.json`'s `_note`), not a live LLM call — no `--backend claude` run was attempted for this corpus. Stage 3 (retrieval) is the real, offline, deterministic part. Stage 3b (SKOS typing) fell back to the fixtures backend's generic default (`relatedMatch`, `source: fixture-default`) because `relation_fixtures.json` (shared with the eggs run, not parametrized by `--concepts`) has no entries for these three terms — that default is not a real typing judgment; a `--backend claude` run would produce one.

## The corpus and concepts

Two communities from the LHC/collider micro-black-hole safety case (see `../../demo-collider/README.md` for the full case background): **`collider-theory`** (the Hawking-evaporation and accretion-mechanism arguments) and **`collider-bounds`** (the cosmic-ray-survival and white-dwarf/neutron-star bound arguments). 13 short documents total (6 theory, 7 bounds), each a **verbatim substring** of a paragraph-level usage excerpt already committed in this repo — `demo-collider/cross-side/excerpts/*.txt` and `demo-collider/term-check/.term-check/prompts/*-excerpts.txt` — split at sentence boundaries, with inline math rendered to plain ASCII and `[...]` left in place wherever a sentence was skipped, matching those excerpt files' own stated convention. The full third-party paper texts are **not** committed anywhere in this repo (copyright boundary, `demo-collider/README.md`) and were not consulted directly for this addition — only the already-excerpted, already-committed passages were used. See each document's `source` field in `corpus.json` for exact provenance.

Three concepts, each a real term from the source papers with a **hand-authored**, community-neutral `constrained_definition` (written directly from the primary excerpts, following the same no-term/no-proper-name/no-field-name constraints as `llm_backend.py`'s `DEFINE_PROMPT` — see `concepts.json`'s `_note`):

| concept | owning community |
|---|---|
| accretion slow-down | collider-theory |
| macroscopic absorption | collider-bounds |
| crust penetration time | collider-bounds |

The naive question used for all three ("could a black hole made at a particle collider end up swallowing the Earth") is the lay framing of the collider safety case, analogous to the eggs demo's single recurring naive question.

## The command, exactly as run

```bash
python recall_extender.py --backend fixtures \
  --corpus example-owndata/corpus.json \
  --concepts example-owndata/concepts.json \
  --out example-owndata/results.json
```

Run from `prototype/`, with `bge-large-en-v1.5` cached locally (`HF_HUB_OFFLINE=1` was set; see `../README.md`'s Setup section for the uncached case). `results.json` in this directory is the genuine, unedited output of that exact command.

## What it found — and an honest read of the numbers

| concept | naive_q | raw_term | defn | gain |
|---|--:|--:|--:|--:|
| accretion slow-down | 2 | 1 | 1 | +1 |
| macroscopic absorption | 1 | 1 | 1 | +0 |
| crust penetration time | 1 | 1 | 1 | +0 |

Unlike the eggs demo (routing gains +4/+3/+7, naive-question owner rank 4-8 out of 15), the naive question here already lands the owner community at rank 1-2 out of 13. That is not a stronger routing effect — it is a **weaker one, and an artifact of this corpus's structure**: with only two communities and no lay/distractor buffer (the eggs corpus had a lay-public-health community plus a distractor community sitting between the naive question and each specialist owner), a lay question about the same general subject (black holes at colliders) is already close, in embedding space, to both `collider-theory` and `collider-bounds` documents. This is exactly the kind of corpus-dependence the eggs README's "Honest scope" section already flags (n=3 concepts, one case, no tuning) — it is not a new finding, just the same limitation showing up predictably on different data. The one genuinely informative thing this run adds: the interface's `--corpus`/`--concepts` plumbing produces a well-formed, sane result on unseen documents and terms, including the graceful stage-3b fallback when no relation fixture exists for a new term.

## Files

- `corpus.json` — 13 documents, provenance in `_note` and per-document `source` fields.
- `concepts.json` — 3 concepts, hand-authored definitions, provenance in `_note`.
- `results.json` — the run above, unedited.
