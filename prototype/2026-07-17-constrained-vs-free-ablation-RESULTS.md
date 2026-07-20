---
title: "Neutral-vocabulary vs free-text definition pilot — results (FLF recall-extender, Option 1b)"
date: 2026-07-17
kind: eval results (in-sample jargon-avoidance pilot, n=3; NOT a controlled-word-list test)
targets: "novelty-position.md strip 2 / entry §5-(i) — the one open STANDALONE component (controlled defining vocabulary). Does NOT touch the second open candidate, the fused assembly (§5-(ii))."
harness: "/mnt/f/src/minelit/flf-epistack/eval/recall-extender/ablation_constrained_vs_free.py (+ ablation_analysis.py)"
gen_model: "sonnet (primary) + opus (replication); bge-large-en-v1.5 retrieval"
review: "Codex doc-review (gpt-5.6-sol) 2026-07-17: MAJOR REVISION, 10 findings — all folded into this revision (relabelled scope, softened equivalence, added circularity + alias-leak caveats, corrected the open-claim count, downgraded 'pre-registered'/'model-agnostic', restricted the bottom line)."
one_line: "On the eggs fixture, a neutral-vocabulary constrained definition reaches the owning sub-literature at rank 1 with ZERO near-headword restatement and lexical overlap that even leans toward the distractors — i.e. by semantic match alone. A free-text definition also reaches rank 1 with a larger separation margin, but that margin co-occurs with substantial soft term-restatement (apoB free-text uses 'apolipoprotein'/'particle number') and owner-concentrated lexical overlap, so it is NOT a clean quality win. Net: no rank-1 difference on this saturated n=3 fixture; the constrained arm hits rank 1 without any lexical shortcut. This does NOT test strip 2's actual controlled-word-list design, and it updates the open claim only weakly."
---

# Neutral-vocabulary vs free-text definition pilot — results

> **Register (read first).** This is an **in-sample jargon-avoidance pilot**, n=3 concepts, one case, one corpus, one embedding model. It went through a Codex doc-review that returned **MAJOR REVISION**; this revision folds in all ten findings. It is **not** a test of strip 2's actual design (a fixed LDOCE-style defining-word list — see §6.1), **not** a clean one-variable ablation (§6.4), and its retrieval setup is **circular by construction** (§6.2). Treat it as a bounded demonstration, not a superiority result. [[feedback_unreviewed_artifact_assume_wrong]] fired here as predicted: every computed number held; the first-draft *interpretation* overclaimed and was corrected.

## 0. What this measured and why

The recall-extender novelty position (`novelty-position.md`; entry §5) cedes almost everything to prior art and holds **two** claims as `open (candidate)`: (i) strip 2, **a *controlled defining vocabulary* for machine-generated cross-community definitions**, and (ii) the **fused assembly** as one thing. This pilot touches **only (i), and only its standalone-component form** — the assembly (ii) is untouched. Every academic system and shipped product found in the searches uses **free text** for its generated definitions, so strip 2 is the one standalone component worth putting a number on. This is **Option 1b** from `2026-07-17-form-answers-and-eval-design-SESSION-SYNTHESIS.md` §7, on the retrieval harness that already existed. It was designed to try to *falsify* the claim, not confirm it.

## 1. Design (two conditions; primarily but not only a vocabulary difference)

For each of the three eggs concepts, both arms define the **same term** from the **same owner-community context**, **same generator model**, and are **forbidden the exact term itself**. They differ mainly in the defining vocabulary:
- **CONSTRAINED** — "use only plain, common English; no field name, no proper names, no jargon" (a *proxy* for the controlled-defining-vocabulary condition — see the §6.1 caveat: no explicit word list is supplied or enforced).
- **FREE-TEXT** — "natural expert prose, any standard field terminology" (the predecessors' condition).

They are **not a clean one-variable ablation**: the prompts also differ in persona/purpose ("cross-community search key" vs "specialist glossary") and the free definitions come out ~1.3× longer (§6.4). Metric: embed each definition with `bge-large-en-v1.5`, rank all 15 corpus docs by cosine, report the owning sub-field's `best_rank` (1 = top, lower better), `mean_rank` (over its 3 docs), and `margin` (best owner cosine − best non-owner cosine; >0 = owner above all distractors; has headroom when `best_rank` saturates). **k = 3** samples per (concept, arm), generated live via `claude -p` and **frozen** so the embedding step is deterministic. Anchors already measured: `naive_question` (floor), `raw_term` (ceiling) — these reproduce the entry §4a table exactly (5/4/8 and 1/1/1), an internal-consistency check on the harness.

## 2. Results — rank of owner's best document (sonnet primary; k=3, mean [min,max])

| concept (owner) | naive_q (floor) | raw_term (ceiling) | constrained | free-text |
|---|--:|--:|--:|--:|
| hyper-responder (lipidology) | 5 | 1 | **1 [1,1]** | **1 [1,1]** |
| apoB particle number (cardiology-biomarker) | 4 | 1 | **1 [1,1]** | **1 [1,1]** |
| isocaloric substitution (nutrition-epi) | 8 | 1 | **1 [1,1]** | **1 [1,1]** |

`best_rank` is **saturated at 1 for both arms, every concept, every sample.** The unsaturated metrics (mean over 3 concepts):

| metric | constrained | free-text | Δ (free − constrained) |
|---|--:|--:|--:|
| `mean_rank` | 2.074 | 2.000 | −0.074 |
| `margin` | 0.078 | 0.127 | **+0.049** (free's separation ~1.6× larger) |

**Opus replication** (same prompts, k=3): `best_rank` identical (both arms rank 1 everywhere); `mean_rank` constrained 2.333 / free 2.037; `margin` constrained 0.070 / free 0.131 (Δ +0.061). Same sign, same shape as sonnet.

## 3. Reading the numbers honestly (Codex #3)

`best_rank` saturating at 1 means **failure to see a difference here is not evidence of equivalence** — the metric has no headroom on this easy fixture, and n=3. The correct statement is narrow: **no rank-1 difference was observed on this fixture.** On the two metrics that *do* have headroom (`mean_rank`, `margin`), free-text is consistently, modestly ahead. So the raw numbers, taken alone, mildly favor free-text — **but §4 shows that edge is confounded with term-restatement**, so it is not a clean quality advantage.

## 4. Why free-text's margin edge is not a clean win — the alias-leak + overlap contrast (Codex #5, #6)

The saved, specified analysis (`ablation_analysis.py`; lowercase, `[a-z]{4,}` content-word types, set-based) reports, per arm, lexical overlap with the **owner** corpus, overlap with the **distractor** docs, and hits on **near-headword components/aliases** (the forms a full-string leak check misses). Mean over 3 concepts:

| arm | owner overlap | distractor overlap | alias/component hits |
|---|--:|--:|--:|
| constrained (sonnet) | 6.9 | 8.1 | **0.00** |
| free-text (sonnet) | 12.8 | 9.1 | **1.78** |
| constrained (opus) | 7.0 | 7.7 | 0.11 |
| free-text (opus) | 13.9 | 11.6 | 1.56 |

Two things fall out, and they reframe §3:

1. **Free-text substantially restates the headword.** The apoB free-text definitions use **"apolipoprotein," "apob," "particle number," "lipoprotein particles"** (≈3 alias hits/sample); isocaloric free-text uses "substitution," "energy-partition"; hyper-responder free-text uses "responsive." These near-headword forms lexically match the owner docs directly, so free-text's owner-retrieval and its larger margin are **partly soft term-restatement** — exactly what the weak `full-headword in text` check (0/18) missed. My first-draft "not term-restatement" claim was wrong for the free arm.
2. **The constrained arm reaches rank 1 with no lexical shortcut.** Its alias/component hits are ~0, and its lexical overlap actually **leans toward the distractors** (owner 6.9 vs distractor 8.1). It still reaches the owner at rank 1 — so it is matching **semantically**, not lexically.

So the margin gap cannot be read as "free-text is the better definition." It co-occurs with term-restatement the constrained arm does not use. This is **correlational, not a proven mediation** (no matched-content mediation ablation was run); stated as a contrast (owner-vs-distractor overlap, plus the alias screen), not a bare number.

## 5. What this does and does not update

**It does not test strip 2's actual design.** Strip 2 is a *fixed, small, domain-generic defining-word list* (LDOCE-style, enforced). The constrained arm only prompts "plain English"; no word list is supplied, enforced, or compliance-checked (§6.1). So **this pilot cannot update the controlled-defining-vocabulary claim on its own terms** — it tests jargon-avoidance prompting as a proxy.

**What it does show, bounded to this fixture:** a neutral-vocabulary definition reaches the owning specialist literature at **rank 1**, matching the raw term and far above the naive question (rank 4–8), **without any near-headword restatement and without an owner-leaning lexical overlap** — i.e. by semantic match. Free-text also reaches rank 1, with a larger separation margin that is **confounded with soft term-restatement**. So on a *leak-fair* reading the pilot does **not** show constrained losing to free-text; both reach the owner, and only the constrained arm does so without a lexical shortcut.

**What remains untested (Codex #7):** the controlled vocabulary's *actual* justification — (a) **cross-community neutrality** (a jargon-free key retrieves a *second* community holding the same concept under a different name; free-text, by restating source jargon, would not) and (b) **no-curation economics** (a static defining word list needs no maintenance) — is **not measured here.** This corpus has no true A↔B cross-community pairs and no community-identity probe or economic test. Those are the funded/post-deadline eval (UMLS "Entry Terms" / Larsen & Bong A↔B pairs; `2026-07-17-external-test-feasibility.md`). They are **design rationales, not findings**, and must be labelled so in any entry text.

## 6. Threats to validity (folded from the Codex review)

1. **Controlled vocabulary not actually tested (Codex #1).** Constrained arm = "plain English" prompt, not an enforced LDOCE-style word list with compliance checking. Proxy only.
2. **Generation↔retrieval circularity (Codex #2).** Each definition is generated *from* the owner docs, then used to retrieve *those same* docs. Rank-1 and owner-word overlap are partly baked in; this says nothing about unseen literature. The *between-arm contrast* is still fair (both arms share the circularity), but absolute rank-1 is not a generalization claim.
3. **Ceiling saturation (Codex #3).** `best_rank`=1 for both; no equivalence can be inferred from a saturated n=3 metric.
4. **Not one-variable (Codex #4).** Prompts differ in persona/purpose and length (~1.3×), not only vocabulary; neither the margin gap nor the rank tie is cleanly attributable to the vocabulary constraint.
5. **Mechanism is correlational (Codex #5).** §4's overlap contrast supports "free-text's margin co-occurs with restatement," not strict causation; no matched-content mediation ablation.
6. **Alias-leak (Codex #6).** Free-text restates near-headword components; the full-string leak check (0/18) understated this. Now screened in §4.
7. **Replication, not model-agnosticism (Codex #9).** Sonnet + Opus are the same family on identical data/prompts; call it a two-model replication. "Pre-registered" is not independently auditable from this mutable doc — the opus expectation was written before the opus run but is **not sealed**; treat §2's opus row as replication, not prospective preregistration.
8. **Open-claim count (Codex #8).** Two `open (candidate)` items exist (strip 2 + assembly); this pilot touches only strip 2's standalone component.

## 7. Bottom line (restricted to what was observed)

*On the eggs fixture, a neutral-vocabulary definition reaches the owning sub-literature at rank 1 — matching the raw term, far above the lay question, and doing so without restating the headword or leaning on owner jargon (it matches semantically). A free-text definition also reaches rank 1 with a larger separation margin, but that margin co-occurs with soft term-restatement, so it is not a clean quality advantage. No rank-1 difference was observed between the two on this saturated n=3 fixture.* This neither confirms nor refutes strip 2's controlled-word-list design (untested), and the controlled vocabulary's real payoff — cross-community neutrality and zero curation cost — remains an untested hypothesis, not a finding.

## 8. If this goes into the entry (a decision, not done)

Per Codex #10 the entry currently says no live-generation evaluation is built. If folded in, it must go in at **exactly the register of §7** — as a bounded owner-retrieval pilot with the §6 threats stated, correcting the entry/novelty-position/artifact-map together, and it should *strengthen* the entry's existing honesty move (§5 already calls strip 2 "not the pitch") rather than become a superiority claim. Recommended framing for the paid-work "how we'd measure it": the clean version = enforced defining-word list + compliance check + disjoint generation/retrieval corpora + true A↔B pairs + a community-identity probe.

## 9. Files

- Harness: `ablation_constrained_vs_free.py`; analysis: `ablation_analysis.py` (both in `/mnt/f/src/minelit/flf-epistack/eval/recall-extender/`)
- Frozen definitions: `ablation_definitions.json` (sonnet), `ablation_definitions_opus.json` (opus)
- Results JSON: `ablation-results.json`, `ablation-results-opus.json`
- Reproduce (deterministic): `HF_HUB_OFFLINE=1 ../../.venv/bin/python ablation_constrained_vs_free.py`
- Codex review verbatim: `/tmp/.../scratchpad/codex-docreview.log` (MAJOR REVISION, 10 findings, all folded)
