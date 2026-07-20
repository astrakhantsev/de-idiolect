---
title: "End-to-end cell on C2 — RESULTS: pre-registered primary FAILED at the fidelity gate (quadrant D✗F✓)"
date: 2026-07-19
status: "COMPLETE — a clean pre-registered negative. Both definition configs failed the frozen fidelity gate on the same item (prospectivity) before retrieval; the equal-information frontier baseline routed to the owners. Everything below the verdict is exploratory description, per spec §4."
spec: "2026-07-18-e2e-cell-SPEC.md rev 3 (FROZEN; sha256 in eval/e2e-cell/runs/spec.sha256)"
artifacts: "/mnt/f/src/minelit/flf-epistack/eval/e2e-cell/ — corpus (records/FROZEN.json), prompts, checker, manifests, runs; all referenced by hash"
---

# E2e cell on C2 — results

## Verdict (pre-registered rules, applied without relitigating)

1. **Primary endpoint: FAILED at the generation stage.** Both definition configs (sonnet, opus) passed the leak check on the first attempt but **failed the frozen fidelity gate on the same item — (iii) prospectivity**: each definition collapsed "would an instrument this accurate be *worth building*" (the excerpts' explicitly simulated, decide-before-building framing) into "is this *produced* estimate worth using." Per the frozen rule (any of i–iv not PRESERVED → config fails; no regeneration on fidelity grounds; a failed config = primary failure), the primary failed twice over, before any retrieval ran.
2. **Mechanism replication, and the cell's main scientific content:** this is the *same definitional-drift failure* the 07-16 naming experiment documented (§7.3-iii, polarity inversion there; prospectivity collapse here) — now observed 2-for-2 on fresh generations, on a different drift axis, caught *pre-retrieval* by the gate the reviews mandated. Definitional drift is looking systematic, not incidental: **fidelity, not leakage, is the generation stage's binding constraint**, and a production pipeline needs round-trip fidelity as a *generation-time component*, not only an evaluation gate.
3. **Baseline quadrant: D✗F✓** (pre-interpreted in spec §4 as "null for the pipeline's mechanical form; the entry reports it"). The equal-information frontier baseline (GPT-5.6, reasoning effort high, isolated, same excerpts + same 18 shuffled records) returned `d02, d01, d10, d05, d04` — **both true value-of-information docs in its top 2**. On this cell, direct frontier inference with corpus access does what the mechanical pipeline was supposed to do — the §8 "marginal over asking the frontier model directly" baseline, measured for the first time, and it wins here.
4. **Detection endpoint: MISS** (frozen top-25 criterion; retrospective demo label). Diagnosis: the frozen background corpus was itself **contaminated with post-discovery material** — `30_reference/novelty-protocol.md`, written from this project's failures, contains the coinage, so the background-df=0 rule excluded "operating requirement" from candidacy entirely. The idiolect had propagated into the project's own reference corpus. Labeled-exploratory variant (contaminated file excluded): rank 224 of ~133k candidates — top ~0.2%, far from a usable top-25 cut. Raw TF-IDF keyness under-delivers as a surfacing stage; consistent with the entry's "candidate-term surfacing built; novel-sense detection unbuilt."

## Exploratory retrieval description (no claims — the definitions are fidelity-failed, so their routing is routing of a *drifted* construct)

N_docs = 18, M = 3 owners; chance: P(first-owner rank 1) = 0.167, E[hits@5] = 0.83. bge-large-en-v1.5, frozen pipeline (`retrieve.py` sha256 in runs/).

| arm | first-owner rank | hits@5 | top-4 (set) | reading |
|---|--:|--:|---|---|
| K1 bare coinage | 1 | 2 | d02(own) ·5082, d12(dist) ·5036, d18(dist), d04(mis) | **near-tie artifact**: a flat, low-similarity ranking (Δ=0.005 to a distractor) where an owner happens to edge first — not strong bridging |
| K2 in-project phrase | 5 | 1 | d04(mis), d05(mis), d06(mis), d12(dist) | **the misroute, replicated in embedding space**: "audit unit" pulls audit-sampling docs, "cold-start" pulls the recommender doc — the realistic project query steers wrong, exactly as the naming experiment's control did |
| N naive question | 2 | 2 | d04(mis), d01(own), d10(dist), d05(mis) | competitive with D-sonnet |
| D-sonnet (fidelity-FAILED) | 2 | 2 | d04(mis), d01(own), d02(own), d05(mis) | owner mass close behind a misroute top |
| D-opus (fidelity-FAILED) | 1 | 2 | **d02(own) ·6362, d01(own) ·6341**, d04(mis), d10(dist) | the cleanest owner structure of any arm — but unclaimable: it routes a drifted construct |
| F frontier baseline | 1 (its own censored metric) | 2 | d02, d01 top-2 | F✓ per its frozen definition |

Honest reading of the exploratory layer: had the fidelity gate not existed, this cell would have *looked* like a success for D-opus (owners at ranks 1–2 with margin) — which is precisely the trap: retrieval success for a definition that no longer says what the project's concept says. The gate did its job. Also of note: the D-vs-N mechanism comparison (pre-registered as binding had the primary passed) would have read "no definition-specific advantage established" — N reached rank 2, tying D-sonnet.

## Deviations and amendments, all logged

- **Amendment A1** (pre-freeze, pre-generation): d02's frozen sources unreachable (S2 405/429, Scholar captcha); same query re-pointed to PubMed, take-first, no skips. N=18/M=3 unchanged.
- Runner path fix (absolute paths) before any run; codex baseline effort pinned to `high` after the preflight exposed a `none` default (a weak-baseline hazard).
- Exploratory detection variant (`detect_exploratory.py`) is a separate, labeled script; the frozen `detect.py` and its MISS stand.
- Corpus agent dead-waited mid-assembly and was recovered by message with foreground-only instructions (process note; no effect on record content — all abstracts are real retrieved text, exclusions logged).
- Spec deviation, logged at freeze: no third full pre-run review round (exploratory-phase scope constraint); this post-hoc results review is the standard compensating control.

## What this adds to the FLF entry, if folded (user's call — spec §6: folding is outside the cell and contingent on the submission decision)

Three sentences, in the entry's own register: *the pre-registered end-to-end attempt failed at its own fidelity gate — both generated definitions drifted off the concept's prospective structure before retrieval could be scored, replicating the definitional-drift failure the earlier experiment found and identifying fidelity as the generation stage's binding constraint; the equal-information frontier baseline routed to the owner literature directly, giving the entry's "marginal over direct ask" caveat measured content on one cell; and the realistic in-project query misrouted in embedding space exactly as the coinage misrouted blind models, extending the misroute finding from naming to retrieval.* A failed pre-registered cell reported this way is on-message for an entry about confident nulls; it is not evidence the pipeline works.
