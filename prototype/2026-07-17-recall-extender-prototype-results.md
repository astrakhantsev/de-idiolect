---
title: "Recall-extender prototype — runnable pipeline + the definition-mediated routing measurement"
date: 2026-07-17
kind: prototype result (hub mirror; code is source-of-truth in the workspace)
workspace: /mnt/f/src/minelit/flf-epistack/eval/recall-extender/ (recall_extender.py · llm_backend.py · corpus.json · concepts.json · relation_fixtures.json · results.json · README.md)
status: "BUILT + RUN 2026-07-17. Stage-3 retrieval is a real/deterministic/offline measurement; the committed offline run uses author-frozen definitions, and a --backend claude run generated them LIVE with routing unchanged (results-live.json). NOT end-to-end: detection is not wired into the evaluated concepts, which are hand-supplied; retrieval is to the concept's own owner community. Replaces the hand-run WebSearch eggs demo's query-crafting confound with an embedding measurement."
---

# Recall-extender prototype — results

A runnable prototype of the recall-extender workflow (Ingestion + Structure layers), demonstrated on the FLF eggs case. Detect a community-local term → generate a community-neutral constrained definition → use the *definition* (not the term) as the retrieval key across communities → label the relation with SKOS. Positioned as FLF's "prototype tool" shape, honestly NOT a system.

## What is real vs fixture

- **Stage 1 (detect)** — TF-IDF keyness across community sub-corpora. Real, deterministic, offline. Surfaces the local terms correctly (lipidology → "variation, response"; cardiology-biomarker → "particles, particle, lipoprotein, number"; nutrition-epi → "substitution, causal, energy").
- **Stage 3 (match)** — **`bge-large-en-v1.5` embeddings + cosine. Real, deterministic, offline — the load-bearing measurement.**
- **Stages 2 (define) and 3b (type)** — LLM steps behind a real `llm_backend.py` interface. The committed offline run uses author-frozen outputs; a `--backend claude` run generated them **live** (`results-live.json`, all defs `definition_source: live`) and the routing held at rank 1. (An earlier "Usage credits are required" error on one spawned draw was **transient**, not a quota wall — subsequent `claude -p` calls incl. `--model opus/sonnet` all work.)
- **Detection is NOT wired into the measured path**, and retrieval is to the concept's **own owner community** (not concept-to-concept cross-community alignment) — the three evaluated concepts + owners are hand-supplied. So this isolates and measures ONE link (definition-as-retrieval-key), not the whole pipeline running by itself.

## The measurement (worked run)

Rank of the owning sub-field's **best document** among all 15 corpus docs, under three query forms (lower = better):

| concept (owner) | naive question | raw term | **constrained definition** | gain |
|---|--:|--:|--:|--:|
| hyper-responder (lipidology) | 5 | 1 | **1** | +4 |
| apolipoprotein B particle number (cardiology biomarkers) | 4 | 1 | **1** | +3 |
| isocaloric substitution model (nutrition-epi methods) | 8 | 1 | **1** | +7 |

The naive question ("are eggs bad for you for heart health") retrieves the lay overview pages (A1/A3/A2) top in every case; the owner sits at rank 4–8. The constrained definition — community-neutral, containing none of the sub-field's own term — puts the owner at rank 1, matching the raw term (which the lay asker does not have). **The gap between what the asker has (the naive question) and what the tool supplies (the definition) is the routing effect, measured deterministically rather than by hand-run search.**

SKOS typing (stage 3b, fixtures): hyper-responder → B2 exactMatch · apolipoprotein B particle number → C1 exactMatch · isocaloric substitution → D2 exactMatch.

## Honest scope

- Stage 2 was **not generated live**; definitions are author-written (knowing the answer) and frozen. This measures *"given a good constrained definition, does it route better than the naive question?"* (yes, decisively) — **not** whether the automatic generator produces good-enough definitions (that question has only the one-cell exploratory result in `2026-07-16-definition-mediated-naming-EXPERIMENT.md`).
- n = 3 concepts, 15 docs, one case, one embedding model, no tuning, no held-out eval, only raw-term/naive-question baselines.
- Definition bleed into related sub-fields is visible and uncorrected (hyper-responder's definition ranks a cardiology-biomarker doc 3rd).
- Retrieval ≠ verification; the SKOS labels are frozen author judgments in this run.

## Why it matters for the entry

This upgrades the entry from "spec + hand-run demos" toward FLF's "prototype tool" shape, and it **resolves the Codex review's eggs-demo findings** (the hand-run WebSearch queries were analyst-crafted and mixed in domain vocabulary; this replaces them with a deterministic embedding measurement where the naive-question baseline is embedded identically, isolating the definition's contribution from query-crafting). It does not resolve the generator-quality question, which stays exploratory.
