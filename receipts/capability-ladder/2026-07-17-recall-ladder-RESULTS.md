---
title: "Recall-lift model ladder — RESULTS (capability + cross-system probe for the 'gets worse as AI improves' claim)"
date: 2026-07-17
kind: experiment result (exploratory probe; Codex doc-review MAJOR REVISION folded — see §0)
parent: 2026-07-17-recall-backtest-RESULTS.md (C2/C4 cases, prereg, frozen targets)
raw: recall-ladder-raw/ (ladder draws, briefs, runners, logs) + recall-ladder-raw/backtest-clean-c2/ (imported Sonnet 5 / Opus 4.8 C2 rows) + recall-ladder-raw/codex-logs/ (Codex per-run tool traces)
status: "DESCRIPTIVE, exploratory. On the clean case (C2), a single opaque coinage stayed unrecoverable — all 8 tested P0 configs scored L0 (6 Claude versions + both GPT-5.6 configs), landing in wrong fields (security/audit); the neutral-definition arm scored L1/L1/L3/L3 on the 4 configs where it was run (only Opus 4.8 + Fable reached the owner). This is CONSISTENT WITH the recall half of the entry's claim but does NOT test its socialization setup, its 'worsening', or its presentation half; recall was flat, not worsening. GPT is a cross-SYSTEM probe (harness confounds), not a clean model-family comparison. C4 excluded (P0 stimulus underdetermined). Supporting receipt for a NON-load-bearing claim; not a tier-changer."
---

# Recall-lift model ladder — results (exploratory probe)

## 0. Status and review

This began as a capability/cross-vendor extension of the backtest ([[2026-07-17-recall-backtest-RESULTS]]). A Codex doc-review returned **MAJOR REVISION (7 findings)**, all folded here: the raw L-scores held, but the first draft's *synthesis* overclaimed — "capability-invariant / family-invariant", "mechanism", "plateau", "cross-family-validated", "answer-key unstable", and an over-stated primary-verification. What survives is a **narrow descriptive result**, below. Full review at `recall-ladder-raw/doc-review` (log).

## 1. The question, and what the probe actually manipulates

The entry's §1 makes an argued, explicitly **non-load-bearing** claim: *a more capable model **socialized into a community's idiolect** — briefed on its documents, fluent in its terms — produces a more fluent, better-cited, more confident report that the prior work isn't there. The presentation improves; the recall does not.*

This probe does **not** reproduce that setup. It feeds each model **one bare coined phrase** (the P0 arm) or **one domain-stripped definition** (the R arm) — no document corpus, no socialization — and asks the reverse-dictionary question (*what is this called, who owns it, oldest treatments*). So it can speak to a **narrower** question: does a single opaque coinage stay unrecoverable as model capability rises, and does the neutral definition recover the owner? It does not test socialization, does not measure the presentation half (except one anecdote, §3), and — since recall is *flat*, not degrading — does not show anything "getting worse."

Harness: Claude draws run headless `claude -p` with file tools denied (`Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch`), `WebSearch` + `safefetch` only, each in its own empty temp cwd (verified `rundir_empty`). **The GPT-5.6 draws are not the same harness** (finding 3): `codex exec` under a `read-only` sandbox (which blocks *writes* but not filesystem/shell *reads*), a different web-search interface, and a tool-instruction line adapted for Codex. Empty cwd + `--ignore-user-config` kept them blind in practice, but the tool-level isolation is not matched — so GPT is a **cross-system probe**, not a clean family comparison. Briefs are the frozen, hash-verified backtest briefs; every load-bearing hit checked against the primary.

## 2. Result — the clean case (C2: "cold-start operating requirement for the audit unit" → value of information)

Rubric (prereg): **L0** miss / wrong field · **L1** right field, no canonical term · **L2** canonical field term · **L3** a listed target source, correctly attributed.

| model | tier / family | **P0 bare coinage (idiolect)** | **R neutral definition** |
|---|---|---|---|
| Haiku 4.5 | small · Claude | **L0** — "cannot identify"; intrusion-detection / recsys cold-start / NERC | **L1** — named forecasting/Bayesian field, no canonical term, "cannot identify" |
| Sonnet 5 | mid · Claude (newer gen) | **L0** — intrusion detection / simulation warm-up | **L1** — extremizing (Baron 2014 / Satopää 2014); missed value of information |
| Opus 4.5 | large · Claude | **L0** — Trusted Computing Base / Root of Trust (Thompson 1984) | *(not run)* |
| Opus 4.7 | large · Claude | **L0** — "cannot confidently identify"; internal-audit / recsys / power-systems | *(not run)* |
| Opus 4.8 | large · Claude | **L0** — Root of Trust / Münchhausen (from backtest clean rerun §8) | **L3** — value of information + Raiffa & Schlaifer 1961 / Howard 1966 |
| Fable 5 | frontier · Claude | **L0** — financial-audit "experienced-auditor test" (confident ~0.90; PCAOB AS 1215 primary-verified, GAO 1994 secondarily corroborated — and wrong field) | **L3** — value of information / EVSI + Raiffa & Schlaifer 1961 + Howard 1966 (named VoI as the governing concept) |
| GPT-5.6 (Codex `terra`) | cross-system | **L0** — Common Criteria FAU_GEN.1 / DoD Orange Book 1985 | *(not run — P0-only probe)* |
| GPT-5.6 (Codex `sol`) | cross-system | **L0** — cold-start stateful monitor (Handley/Paxson 2001) / Initial Operational Capability | *(not run — P0-only probe)* |

**Descriptive result.** On C2, **every tested P0 (bare-coinage) configuration scored L0** — 8 in all (six Claude versions across three sizes and two generations; both GPT-5.6 configs) — each landing in a security/audit *wrong* field, none reaching decision theory. On the **R (neutral-definition) arm, run on 4 configs, scores were L1 / L1 / L3 / L3** — only the two frontier Claude models (Opus 4.8, Fable) reached the registered owner; Haiku and Sonnet reached only the surrounding field.

**What this supports, and what it does not.** It is **consistent with** the recall half of the entry's claim: a single opaque coinage was not recovered by any tested model, and only the neutral definition (on the more capable models) reached the owner. It does **not** establish "capability-invariance", a "plateau", a causal "mechanism", or that behavior "gets worse" (recall was flat at floor, not worsening) — the design is one C2 prompt, mostly one draw per config, a coarse floor score, and the R arm on only four configs. These are **bounded observations pending replicated, full-arm testing**, not a scaling law.

**The GPT floor as a bounded cross-system datum.** Two GPT-5.6 configs, searching the live web, also scored L0 on C2-P0 — landing in *different* wrong fields from each other (`terra` → Common Criteria; `sol` → cold-start monitor / IOC), i.e. no single wrong-attractor. This is **suggestive** that the miss is not Claude-specific and partially speaks to the entry's confessed "Claude-family only" limitation — but as a **cross-system** observation (§1 harness confounds), not a matched-isolation family comparison. Do not call it "cross-family-validated."

## 3. Caveats — all load-bearing

1. **C4 is excluded because its P0 stimulus is underdetermined** (not because the answer key is "unstable" — a first-draft misdiagnosis, corrected per review). The bare slogan "read the enumerations, not the votes" does not uniquely encode the intended construct, so models split across *different* established readings — judgment aggregation / doctrinal paradox (Kornhauser & Sager 1986; most Claude draws, `terra`), deliberation-vs-aggregation (Manin 1987; cross-family), and decision fusion / evaluator effect (Steiner 1972, Chair & Varshney 1986, Nielsen & Molich 1990; `sol`). That divergence reflects an ambiguous *prompt*, not a defective target concept; challenging the backtest's answer key would require a faithful operational definition (the R arm), not the bare coinage. C4-P0 therefore cannot score a clean "miss", and C2 carries the result.

2. **The presentation half is not measured; one vivid anecdote, with corrected provenance.** "More confident / fluent / better-cited as capability rises" was not scored (no rubric, no counts) and is contradicted elsewhere (Haiku was ~95% confident on a wrong C4 field; Opus 4.7 honestly hedged on C2). The vivid case: **Fable produced the most authoritative wrong answer on C2-P0 — ~0.90 confident, mapping the coinage to the financial-audit "experienced-auditor test."** Provenance, corrected per review: it fetched and quoted **PCAOB AS 1215 directly (primary-verified)** but **could not open the 1994 GAO Yellow Book primary and relied on a CPA Journal secondary account (secondarily corroborated, not primary-verified)**. Treat it as an anecdote, not a measured curve.

3. **Silent model remap caught.** `claude-opus-4-1` transparently remaps to Opus 4.8 (stderr warned); those two draws are 4.8 duplicates, discarded (kept in `recall-ladder-raw/opus-lineage/`, marked). Only Opus 4.5 and 4.7 are genuine older rungs. Any future ladder must set `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP=1` and verify model identity rather than trust that the CLI accepted the id.

## 4. What this is worth (strategic)

A modest, honestly-bounded receipt for a **non-load-bearing** claim. It converts the §1 parenthetical's support from "n = 3 historical anecdotes" to "a small probe: one opaque coinage stayed unrecoverable across 8 model configs (incl. two GPT configs), while the neutral definition reached the owner on the more capable Claude models." It does **not** validate the claim as stated (socialization, worsening, presentation all untested/unmeasured), and it does **not** move the tier gate (cross-person compounding, still untested/unbuilt). Realistic effect on P(≥$5k | submit): a point or two, via making one sub-component measured rather than argued. Cost was low (free scoring of captured draws + cheap CLI invocations). **Given the review, the honest question for the entry is whether to cite even the bounded version, or hold it out of the load-bearing claim entirely** — see §5.

## 5. Entry wording — DRAFT, deliberately dialed back; DECISION PENDING

The strong first-draft wording ("measured across six model versions... capability helps only once you are out of the idiolect") is **withdrawn** — per review finding 2, inserting it into §1 would present a narrower vocabulary-gap result as validation of the socialization/worsening claim, i.e. exactly the overclaim the entry is about. Two honest options for the user:

- **(A) Bounded footnote-grade note:** *"A small probe (appendix): one opaque coinage stayed unrecoverable — wrong field on all eight tested models, three sizes, two Claude generations, and two GPT-5.6 configs — while the domain-stripped definition reached the registered owner on the more capable Claude models. This is consistent with the recall half; it does not test the socialization setup, the presentation half, or any worsening, and the cross-vendor runs are a cross-system probe."*
- **(B) Hold it out of §1 entirely**, keep it only as a receipt in this RESULTS doc / appendix, and leave §1's claim graded exactly as it is ("argued mechanism, n = 3; suggestive, not a rate").

Recommendation: **(B) or a trimmed (A)**. The entry's credibility rests on not overclaiming; a bounded probe of one sub-component, two days out, is not worth the risk of a reviewer reading it as a scaling claim. The §5 "Claude-family only" limitation could get a one-line, hedged mention of the cross-system GPT floor regardless.

## 6. Doc map / audit trail

- Ladder draws + runners + briefs: `recall-ladder-raw/` (haiku/, opus-lineage/, fable/, codex/, briefs/).
- Imported C2 rows (Sonnet 5, Opus 4.8) from the backtest clean rerun: `recall-ladder-raw/backtest-clean-c2/`.
- Codex per-run tool-use traces: `recall-ladder-raw/codex-logs/`.
- Parent backtest (cases, prereg, frozen targets, C2 clean confirmation): [[2026-07-17-recall-backtest-RESULTS]], [[2026-07-17-recall-backtest-SESSION-SYNTHESIS]].
- Entry this feeds: `entry/FLF-entry-recall-extender.md` §1 (the claim) and §5 (the Claude-family limitation).
- Method lessons: [[feedback_unreviewed_artifact_assume_wrong]] (the synthesis layer overclaimed, numbers held — again), [[feedback_blind_pass_tool_level]] (isolation; Codex read-only ≠ read-denied), [[feedback_fanout_agreement_not_independence]] (cross-system > more same-family draws), [[feedback_verify_citations_primary_text]] (Fable's GAO cite was secondary, not primary).
