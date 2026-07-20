# recall-extender — prototype (FLF EpiStack entry)

A small, runnable prototype of the "recall extender" workflow on the FLF eggs case. It isolates and **measures one link** of the proposed chain — using a community-neutral *definition* (not the term) as a retrieval key — and demonstrates the other stages around it (detection; SKOS relation typing) without wiring them into one automatic pipeline.

This is a **prototype, not a system** (FLF's named "prototype tool" shape), and it is **not** end-to-end. Three deliberate limits, each visible in the code (see *Honest scope*): detection is not wired into the evaluated concepts; the concepts + owners are hand-supplied; and the measured retrieval is to the concept's *own* owner community, not concept-to-concept matching between two specialist communities.

## What runs, and how honest each stage is

| stage | what it does | implementation | grade |
|---|---|---|---|
| 1 · detect | surface community-local terms (not wired into the measured concepts) | TF-IDF keyness across community sub-corpora (`sklearn`) | real, deterministic, offline |
| 2 · define | community-neutral constrained definition of a term | LLM via `llm_backend.py` | **live interface, verified working (`--backend claude`); the committed offline run uses author-frozen defs** |
| 3 · match | retrieve documents by the definition (to the concept's own owner community) | **`bge-large-en-v1.5` embeddings, cosine** | **real, deterministic, offline — the load-bearing measurement** |
| 3b · type | label concept↔match with a SKOS relation | LLM via `llm_backend.py` | live interface (verified); committed run uses author-frozen labels |

The **matching measurement (stage 3) is the point, and it is real**: it needs no LLM and no network. Only the two *generative* stages (2, 3b) use the LLM interface. The committed offline run uses frozen author-produced outputs (`concepts.json`, `relation_fixtures.json`) behind the real `define()`/`type_relation()` interface; a `--backend claude` run generates them live (verified 2026-07-17 — `results-live.json`, all defs `definition_source: live`, routing held at rank 1). An earlier "Usage credits are required" error on one spawned draw turned out to be **transient**, not a quota wall.

## Setup

Python 3.12. Install dependencies (any venv works):

```bash
pip install 'sentence-transformers>=5' 'torch>=2' 'numpy>=2' 'scikit-learn>=1.5'
```

The matching step uses `BAAI/bge-large-en-v1.5` (~1.3 GB); **the first run downloads it from Hugging Face** (needs network). To run fully offline once it is cached, `export HF_HUB_OFFLINE=1`. The `--backend claude` path needs the `claude` CLI on PATH (or add an API-keyed backend in `llm_backend.py`).

## Run it

```bash
python recall_extender.py --backend fixtures   # deterministic, reproducible (default)
python recall_extender.py --backend claude     # generates definitions + relations live
```

The run prints a `BACKEND EFFECTIVE` line and warns if `--backend claude` silently fell back to fixtures, so a live run cannot be mistaken for fixtures or vice versa.

## The measurement (worked run, 2026-07-17)

For each specialist concept, we rank all 15 corpus documents by cosine similarity to three query forms and report the rank of the **owning sub-field's best document** (lower = better):

| concept (owning sub-field) | naive question | raw term | **constrained definition** | routing gain |
|---|--:|--:|--:|--:|
| hyper-responder (lipidology) | 5 | 1 | **1** | +4 |
| apolipoprotein B particle number (cardiology biomarkers) | 4 | 1 | **1** | +3 |
| isocaloric substitution model (nutrition-epi methods) | 8 | 1 | **1** | +7 |

The **naive question** ("are eggs bad for you for heart health") retrieves the lay/public-health overview pages (A1/A3/A2) top in every case, burying the specialist owner at rank 4–8. The **constrained definition** — a community-neutral description containing none of the sub-field's own term — puts the owner at rank 1, matching the **raw term** (which the lay asker does not have). That gap between the naive question (what the asker has) and the definition (what the tool supplies) is the routing effect, and here it is a deterministic embedding measurement, not hand-run search.

## Honest scope (what this does NOT show)

- **Detection is not wired into the measured path, and retrieval is to the owner community.** Keyness (stage 1) surfaces each community's local terms but does not *select* the evaluated concepts — those and their owning communities are hand-supplied in `concepts.json`. The measured retrieval routes a definition to its *own* owner community's documents, with the naive question as the baseline; it is not concept-to-concept alignment between two specialist communities. So this is **not** an end-to-end or cross-community run.
- **Stage 2 (define) runs both ways.** The `fixtures` run uses author-written definitions (frozen); a `claude` run had the model generate them live and the routing held — all three live-generated, community-neutral definitions still pulled the owner to rank 1 (`results-live.json`). So the generator does produce routing definitions for these three; reliability at scale is untested. This measures *"given a good neutral definition, does it out-retrieve the naive question?"* — yes — not the generator's owner-recovery quality (the separate experiment `10_projects/minelit/idiolect/2026-07-16-definition-mediated-naming-EXPERIMENT.md`, one clean cell of four).
- **n = 3 concepts, 15 documents, one case, one embedding model.** No baselines beyond raw-term/naive-question, no tuning, no held-out evaluation.
- The definition bleeds into related sub-fields (the hyper-responder definition ranks a cardiology-biomarker doc 3rd) — expected, uncorrected.
- **Retrieval ≠ verification;** the SKOS labels differ fixtures-vs-live (fixtures: all exactMatch; live: narrowMatch/relatedMatch), showing the typing is genuinely model-dependent.

## Files

- `corpus.json` — 15 docs across 4 real eggs sub-fields + distractors (paraphrased real titles/snippets). Source URLs are listed in [`../receipts/naming-experiment/def-naming-raw/eggs-routing-raw.md`](../receipts/naming-experiment/def-naming-raw/eggs-routing-raw.md).
- `concepts.json` — 3 specialist concepts + their frozen constrained definitions (stage-2 fixtures).
- `relation_fixtures.json` — stage-3b SKOS judgments (fixtures).
- `recall_extender.py` — the pipeline.
- `llm_backend.py` — the pluggable LLM interface (`claude`/`fixtures`).
- `results.json` — the worked-run output.
