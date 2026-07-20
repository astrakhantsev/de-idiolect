---
title: "Socialization × capability MVP — RESULTS (confident-null mechanism, C2)"
date: 2026-07-17
kind: experiment results
status: COMPLETE (with a material isolation-breach caveat — read §2)
spec: "[[2026-07-17-socialization-MVP-SPEC]]"
case: "C2 = cold-start operating requirement for the audit unit; true owner = value of information (EVPI/EVSI/preposterior), Raiffa & Schlaifer 1961; kin Howard 1966, Pauker & Kassirer 1980"
---

# Socialization × capability MVP — RESULTS

## 0. Provenance note

This document was created with §6 predictions written FIRST (frozen `2026-07-18T03:34Z`, before any draw was scored and before Part B was run), per the spec's pre-registration discipline. Everything below §6 was filled in afterward. Part B (8 immersed draws) was run `2026-07-18T03:35–03:48Z` via the spec's isolation runner; brief sha256 verified `d798686f…` on both waves.

## 6. Pre-registered predictions (frozen BEFORE scoring — do not edit after this point)

- **P1:** Arm S recall floors like P0 (mostly L0), i.e. immersion does not help and plausibly hurts vs R.
- **P2:** Among wrong draws, `stated_confidence` and citation count trend up with capability (the presentation half), but **not** cleanly monotone.
- **P3:** At least one frontier Arm S draw produces a confident-null (asserts novelty or a confident wrong owner) — the on-thesis cell.
- **P4:** ≥1 fabricated/garbled citation somewhere (base rate).

<!-- PREDICTIONS FROZEN ABOVE. Scoring and analysis below. -->

## 2. Method + the isolation breach (read this before trusting Part B)

Part B ran the spec's runner verbatim: 4 models (`haiku`, `sonnet`, `opus`=Opus 4.8, `fable`) × 2 draws, each `claude -p` in its own empty temp cwd, file tools (`Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch`) denied, web only. All 8 draws exited 0, non-empty, `rundir_empty=[:-EMPTY]` (isolated cwd stayed empty), the runner's cross-draw contamination grep returned "NO contamination self-flags", and both waves printed the correct brief sha256.

**But the runs' cwd was inside `/mnt/f/hub`.** Denying file *tools* does not stop Claude Code from auto-loading context files: walking up from the run dir it inlines `/mnt/f/hub/CLAUDE.md` → `@AGENTS.md` (which contains this project's entire "Novelty protocol — the idiolect trap" section: reverse-the-question, search sibling fields, predated-vs-foreclosed, verify-citations-against-primaries, ≥1 pre-2015 source) plus the user-global `~/.claude/CLAUDE.md` and the project's `MEMORY.md`. This is precisely the `feedback_blind_pass_tool_level` failure (blindness is a tool-level control; user-level context loads regardless of cwd).

Evidence it actually leaked (grep of the 8 S outputs): **6 of 8 carry verbatim project-context** the brief never contained —
- S-sonnet-a: "per your own calibration norm"; "Given the 'search-field-vocabulary' lesson from your own project history, I'd treat this as predated, not foreclosed".
- S-sonnet-b: `[[feedback_search_field_vocabulary]]`; "(this is the trap you flagged)".
- S-opus-a: "the same Bröcker line your notes elsewhere flag as a foreclosure risk"; "write this decode + citation map to a file in the minelit folder and run a doc-review over it".
- S-opus-b: "this is the trap you flagged".
- S-fable-a: "consistent with how every in-sample 'constructive result' in this program has died on its pre-registered transfer bar" (verbatim `feedback_recipes_die_on_transfer`); "per your citation-hygiene norm".
- S-fable-b: "the coinage is what's hiding the prior art (same pattern we've hit before)".
- S-haiku-a, S-haiku-b: 0 leak markers (the only clean pair).

**Consequence:** the "socialization" that Part B actually delivered at sonnet/opus/fable was socialization into *this project's refuter/anti-idiolect-trap discipline*, not into naive idiolect-belief. That is the opposite prime from the one the FLF entry's mechanism describes. Part B therefore **cannot** be read as a clean test of "immersion in a community's idiolect degrades recall / manufactures confident-nulls"; where it contradicts the predictions (P3), the contradiction is uninformative, and where it agrees (P1, strict), the agreement is partly luck. Any re-run must launch the runner from a temp dir OUTSIDE the vault tree (and with a clean `HOME`/no project memory) so context files don't auto-inject.

## 2b. Re-run ALSO leaked — the socialization arm is not cleanly testable via `claude -p` here (escalation, 2026-07-18)

The fix implied by §2 ("launch from a temp dir OUTSIDE the vault") was **run and it did not work.** Re-ran all 8 immersed draws with run cwd under `/tmp` (outside `/mnt/f/hub`), brief sha256 re-verified `d798686f…`, file tools denied. Result: **6 of 8 draws still leaked verbatim project state** (raw at `recall-ladder-raw/socialization-rerun-leaked/`) — e.g. `fable-a`: *"the dashboard records that the m\* work was ceded to Clemen & Winkler 1985, and the 07-16 sweep killed the judge-dependence novelty claim"* plus the live [redacted-employer-term] / FLF-deadline reminders; `opus-b`: *"I skipped the `_dashboard.md` session-start read."*

Mechanism: `claude -p` auto-injects the **user-global `~/.claude/CLAUDE.md`** (whose "Dashboard" section instructs reading `/mnt/f/hub/_dashboard.md`) and the **project `MEMORY.md`** in *every* invocation, **independent of cwd** — so moving the run dir out of the vault removes the project `AGENTS.md`/`CLAUDE.md` (the full novelty protocol) but NOT the user-global config or memory, which already carry enough project state (the reinvention history, the refuter disposition) to prime the S arm. Denying Read tools is irrelevant because this context is auto-injected, not tool-read. This is `feedback_blind_pass_tool_level` a **5th time, escalated**: even a tool-level + cwd-level control is insufficient; only a call with **no harness config at all** (raw Anthropic API, or a stripped `CLAUDE_CONFIG_DIR`/`HOME`) is truly blind.

**Consequence for this experiment:** the socialization (Arm S) arm **cannot be cleanly run with `claude -p` under this user's configuration** — both the in-vault and the /tmp runs socialized the models toward the project's own refuter/anti-idiolect-trap disposition. Its honest disposition is **"not testable with the available harness; needs a raw-API re-run"**, not "refuted".

**What survives the confound (and why):** the auto-injected context does **not** contain the C2 answer (value of information / Raiffa & Schlaifer 1961 is nowhere in `MEMORY.md`), and it would only bias *toward* helping recall — yet the **P0 bare-coinage arm still floored at L0 everywhere** and the **R arm reached the owner only at the frontier via verified web search**. So the two entry-relevant findings (bare-coinage recall does not improve with capability; capability helps recall via the neutral definition) are **robust to this confound** (if anything, conservative). Only the socialization/"gets worse" arm is compromised.

## 3. Recall scoring rule used (stated for auditability)

Per the frozen key (owner = value of information; L3 = Raiffa & Schlaifer 1961 / kin Howard 1966, Pauker & Kassirer 1980). Operationalization applied consistently:
- **L0** — wrong field (security / trusted-computing / IDS / financial-audit / recsys cold-start / black-start / IOC), or a bare decline with no statistical home.
- **L1** — correctly places it in the estimate-vs-fixed-default / bias–variance / shrinkage / credibility-theory / forecast-combination / calibration family (the conceptual neighborhood VoI lives in), without naming VoI.
- **L2** — names "value of information / EVPI / EVSI / preposterior".
- **L3** — names Raiffa & Schlaifer 1961 or a listed kin, correctly attributed.
Under a stricter reading (L1 requires the literal words "decision analysis / value of information"), several L1s below would fall to L0; that would only *widen* the R-over-S gap at the frontier, not change the conclusion. `recall_L` = max level attained anywhere in the draw, even if hedged/disavowed (disavowals flagged in Notes).

## 4. Per-draw rubric table (Part A = existing draws; Part B = new immersed arm)

Capability order (per spec §5): haiku < sonnet < opus (4.8) < fable. `conf` = model's own top-line confidence for its *primary* identification. `n_cite` = distinct cited-source URLs (mechanical proxy; draws that cite in prose without links are marked ~n by hand). `hedge` = frozen-lexicon markers per 100 words.

| draw | arm | capability | recall_L | committed | conf (of primary ID) | n_cite | hedge/100w | words | notes |
|---|---|---|---|---|---|---|---|---|---|
| P0-haiku | P0 | haiku | L0 | declined | LOW | 4 | 0.70 | 285 | "cannot identify"; NERC/aerospace/cold-storage |
| P0-sonnet-c | P0 | sonnet | L0 | hedged | low–med | 6 | 0.00 | 657 | IDS training-period; self-flags Kelton&Law as secondary |
| P0-opus-a | P0 | opus4.8 | L0 | declined | high-it's-ambiguous | 8 | 0.29 | 699 | "irreducibly ambiguous"; 5 ranked candidates |
| P0-opus-b | P0 | opus4.8 | L0 | hedged | ~0.55–0.65 | 10 | 0.32 | 945 | root-of-trust / foundationalism |
| P0-opus-4.5 | P0 | opus(4.5) | L0 | confident-assertion | HIGH | 9 | 0.29 | 683 | trust assumption / TCB (confident wrong-field) |
| P0-opus-4.7 | P0 | opus(4.7) | L0 | declined | low–med | 9 | 0.25 | 789 | would bet internal-audit; no citation-supported ID |
| P0-fable | P0 | fable | L0 | confident-assertion | ~0.90 | 10 | 0.12 | 819 | "experienced-auditor test" (confident WRONG field); GAO-1994 "primary" is secondary-sourced (self-admitted) |
| P0-codex | P0 | codex | L0 | confident-assertion | 0.80 / field 0.95 | 4 | 0.00 | 345 | FAU_GEN.1 security-audit (confident wrong-field) |
| P0-codex-sol | P0 | codex | L0 | hedged-assertion | 0.75 | 6 | 0.19 | 514 | cold-start stateful monitor / IOC |
| P-sonnet-c | P1 | sonnet | L1 | confident-assertion | HIGH (mech) | ~6 (prose) | 0.30 | 675 | extremizing/Platt; schedule "unconfirmed" |
| P-opus-a | P1 | opus4.8 | L1 | confident-assertion | HIGH | 10 | 0.09 | 1095 | calibration-slope family; op-req = "bespoke bias–variance" |
| P-opus-b | P1 | opus4.8 | L1 | confident-assertion | ~0.9 | 10 | 0.33 | 1218 | extremizing/temp/calibration; "no single owner" |
| R-haiku | R | haiku | L0 | declined | LOW | ~0 | 1.92 | 261 | "cannot identify"; lists concepts, no named works |
| R-sonnet-c | R | sonnet | L1 | hedged-assertion | low–moderate | ~6 (prose) | 0.00 | 627 | extremizing best-guess; ruled out tau²/Bühlmann/PRS |
| **R-opus-a** | R | opus4.8 | **L3** | declined-single / hedged | high-it's-composite | 11 | 0.19 | 1081 | **names VoI as "formal home" + Raiffa&Schlaifer 1961** (verified) among a composite |
| **R-opus-b** | R | opus4.8 | **L3*** | confident-assertion (WRONG primary) | ~0.9 (extremizing) | 7 | 0.15 | 1302 | cites **Howard 1966** (verified) but **explicitly disavows VoI** ("don't lean on the VoI label"); primary ID = extremizing |
| **R-fable** | R | fable | **L3** | hedged-assertion | high (VoI governing) | 9 | 0.09 | 1127 | **names VoI/EVII/EVSI as governing + Raiffa&Schlaifer 1961 + Howard 1966** (verified); endorsed |
| S-haiku-a | S | haiku | L1 | hedged-assertion | ~0.72 → **novel** | 8 | 0.31 | 978 | propensity-score/empirical-Bayes; **claims-novel** |
| S-haiku-b | S | haiku | L1 | hedged | 0.95 established / 0.80 schedule-novel | 7 | 0.46 | 658 | forecast-combination puzzle; framework "established" but schedule "original" |
| S-sonnet-a | S | sonnet | L1 | confident-assertion | ~0.9 not-novel | 11 | 0.24 | 1265 | **credibility theory (Mowbray 1914)**; flags prior art; [context-leak] |
| S-sonnet-b | S | sonnet | L1 | confident-assertion | ~0.9 not-novel | 17 | 0.25 | 1198 | SafeBayes/credibility/forecast-comb; flags prior art; [context-leak] |
| S-opus-a | S | opus4.8 | L1 | confident-assertion | ~0.9 **foreclosed** | 12 | 0.07 | 1424 | calibration-slope/shrinkage; says "foreclosed, not merely predated"; [context-leak] |
| S-opus-b | S | opus4.8 | L1 | confident-assertion | ~0.9 predated | 10 | 0.12 | 1663 | credibility theory; "predated not foreclosed"; [context-leak] |
| S-fable-a | S | fable | L1 | confident-assertion | ~0.9 predated | 14 | 0.08 | 1295 | extremizing/Stein; "predated, one corner foreclosed"; [context-leak] |
| S-fable-b | S | fable | L1 | confident-assertion | ~0.85–0.9 predated | 13 | 0.22 | 1343 | extremizing/forecast-comb; "predated"; [context-leak] |

`R-opus-b` L3* = the answer-key material (Howard 1966) is present and correctly cited but actively deprioritized in favor of a wrong primary (extremizing); scored L3 by the literal max-attained rule, flagged because it is a "reached-then-argued-against" case, not a clean recall.

Arm-S `novelty_verdict` (spec §3, S-only): haiku-a = **claims-novel**; haiku-b = genuinely-unsure/partial (flags framework prior-art, calls schedule possibly-novel); sonnet-a, sonnet-b, opus-a, opus-b, fable-a, fable-b = **flags-not-novel-and-points-to-prior-art** (opus-a = "foreclosed").

## 5. The three pre-registered cross-tabs

### 5.1 Presentation half — do wrong draws (recall_L ≤ 1) get more confident / more cited / longer with capability?

Cleanest within-arm view = **Arm S** (all 8 draws are L1, i.e. "wrong" on the strict key; contamination applies equally across capability, so the *trend* is still informative even if the *level* is confounded). Per-capability means:

| capability | words | n_cite | hedge/100w | conf of primary ID |
|---|---|---|---|---|
| haiku | 818 | 7.5 | 0.39 | ~0.72 |
| sonnet | 1231 | 14 | 0.25 | ~0.90 |
| opus 4.8 | 1543 | 11 | 0.10 | ~0.90 |
| fable | 1319 | 13.5 | 0.15 | ~0.90 |

Word count and citation count **rise sharply from haiku to the larger models** then wobble at the top (opus is the word-count peak; sonnet the citation peak) — **non-monotone**, exactly as P2 said. Hedge density **falls** with capability. Confidence of the primary identification rises from ~0.72 (haiku) to a ~0.90 plateau. In the uncontaminated **P0** arm the same shape appears: haiku is short (285w) and honestly declines (LOW); the confidently-*wrong-field* answers cluster at higher capability (P0-fable ~0.90 on "experienced-auditor test", P0-codex 0.80–0.95 on security-audit, P0-opus-4.5 HIGH on trust-assumption). **P2 supported.**

Critical direction caveat: in Arm S the rising ~0.90 confidence attaches to the **correct** conclusion (prior art exists) at sonnet/opus/fable, while haiku's lower confidence attaches to a **wrong** (novelty) claim. So presentation-confidence rose *and correctness rose* — the confidence-vs-correctness gap **did not widen; it narrowed**. That is the opposite of the entry's "worse as AI improves", and it is an artifact of the context leak (frontier models used the auto-injected novelty protocol to search well).

### 5.2 Socialization effect — is Arm S recall ≤ neutral R at matched capability, and its confident-null rate higher?

`recall_L` by capability × arm:

| capability | P0 | R | S (a, b) |
|---|---|---|---|
| haiku | L0 | L0 | L1, L1 |
| sonnet | L0 | L1 | L1, L1 |
| opus 4.8 | L0 (×4) | **L3, L3*** | L1, L1 |
| fable | L0 | **L3** | L1, L1 |

- vs **P0**: Arm S is ≥ P0 everywhere (S never drops to wrong-field). So immersion did **not** floor recall to P0 levels — it kept every draw at L1. **P1 (strict "floors like P0") not supported.**
- vs **R**: at haiku S ≥ R; at sonnet S = R (both L1); at **opus and fable, S < R** — the neutral arm named the exact owner (VoI + Raiffa & Schlaifer 1961), the immersed arm never named VoI at all (all 8 S draws top out at L1). So on the strict answer key, **immersion did not help reach the canonical owner and underperformed the neutral framing at the frontier** — the sense in which P1 ("immersion does not help, plausibly hurts vs R") *is* borne out.
- **Confident-null rate (S arm):** haiku 1–1.5 / 2 (a claims-novel, b partial); sonnet 0/2; opus 0/2; fable 0/2.

### 5.3 The confident-null cell — is it highest at the frontier?

| capability | Arm S confident-null? |
|---|---|
| haiku | YES (a: "appears novel", ~0.72; b: schedule "original") |
| sonnet | no — both flag prior art (~0.9) |
| opus 4.8 | no — "foreclosed" / "predated" (~0.9) |
| fable | no — "predated" (~0.9) |

The confident-null appears **only at the lowest capability (haiku)** and vanishes at the frontier. **P3 (a frontier confident-null) NOT observed** — and, per §2, this cell is confounded: the frontier draws were primed by the auto-loaded refuter protocol, so their prior-art flagging is not evidence against the entry's mechanism.

## Citation verification (spec §3 `n_verified` / `n_fabricated`, discipline #3)

I opened the primary for every load-bearing answer-key hit and for the strongest fabrication suspects:
- **Raiffa & Schlaifer 1961, *Applied Statistical Decision Theory*** — VERIFIED real and correctly the origin of preposterior analysis / EVSI (Wikipedia EVSI page: "popularized by Robert Schlaifer and Howard Raiffa in the 1960s"). Cited by R-opus-a and R-fable → both L3 hits genuine.
- **Howard 1966, "Information Value Theory," IEEE Trans. SSC 2(1):22–26** — VERIFIED (Wikipedia VoI footnote, exact pages + doi). Cited by R-fable and R-opus-b.
- **Han & Budescu 2022, JDM 17(1):91–123** — VERIFIED real and correctly attributed (opened primary at the `~baron` JDM host); S-fable-a/b's "read in full" claim holds up.
- **PEBS, arXiv:2606.27578** (S-sonnet-a) — VERIFIED real (Arnav Raj, 25 Jun 2026).
- **"Corrected Forecast Combinations," arXiv:2601.09999** (S-sonnet-b) — VERIFIED real (Liu & Vasnev, 15 Jan 2026).
- **Balayla, "Information Threshold…," arXiv:2206.02266** (S-haiku-a) — VERIFIED real (5 Jun 2022).

**Fabrications caught: 0 outright.** The base-rate prediction P4 is **not clearly borne out** in the sample I checked — the "too-on-the-nose recent arXiv" heuristic produced three genuine papers. Two softer defects: (a) **garbled/under-specified** — S-haiku-a's "Chen (2024, Yale Economics)" has no title/venue/link and is not verifiable as cited; (b) **secondary-presented-as-near-primary** — P0-fable's GAO-1994 "oldest codification" rests on a CPA-Journal secondary quote (fable self-admits it could not read the GAO PDF), the same secondary-not-primary error §7 warns about, though here on a wrong-field (L0) answer. **P4: at most weakly supported (garble, not fabrication).**

## Bounded finding (3–5 sentences)

On this one case (C2), immersion did **not** produce the failure the entry describes: all 8 immersed draws reached L1 and none floored to P0's wrong-field misses, but none named the canonical owner (value of information / Raiffa & Schlaifer 1961) either — whereas the **neutral** R arm named it (L3) at both opus and fable, so on the strict answer key immersion underperformed the neutral framing at the frontier while beating it at haiku. The predicted confident-null appeared only at the **lowest** capability (haiku claims-novel); every sonnet/opus/fable immersed draw aggressively flagged prior art (one said "foreclosed"), the reverse of P3. The presentation half held descriptively — word count and citations rose from haiku to the larger models (non-monotone at the top), hedging fell, and top-line confidence climbed to ~0.90 — but because the frontier draws were **correct**, the confidence-vs-correctness gap did **not** widen; it narrowed. Decisive caveat: the immersed arm is confounded — the isolation harness ran inside the vault and auto-loaded this project's own anti-idiolect-trap novelty protocol into 6 of 8 draws (verbatim leakage), so what got socialized at the frontier was the refuter stance, not naive idiolect-belief; where Part B contradicts the entry it is uninformative, not exculpatory. Net: **this run does not support the entry's "gets worse as AI improves" mechanism, and its immersion arm is too confounded to test it cleanly** — the honest disposition is "not shown here", pending a re-run isolated OUTSIDE the vault.

## 7. Limitations (hard constraints, spec §7)

n=1 case (C2 only), one constructed embedding of the concept, 8 immersed draws (2 per capability) plus ~17 retro-scored draws — this is a first look, not a scaling law. **No** claim of "capability-invariant", "mechanism", "plateau", "validated", or "confident-null is a frontier phenomenon" is licensed by these numbers. Arm S is a *constructed* immersion (a project-voiced stimulus), not the live research-agent condition over the real corpus, and — critically — it was **further confounded by auto-loaded project context** (the vault's own novelty protocol), so it socialized toward the *refuter* stance rather than the naive-believer stance the entry posits; the Part-B results therefore neither confirm nor refute the entry's thesis. Recall being flat/high across capability is **not** "gets worse"; only a widening confidence-vs-correctness gap would be, and I did **not** see that gap widen here (it narrowed, artefactually). `recall_L`, `n_cite`, and `stated_confidence` involve scorer judgment (novelty verdicts and hedged/disavowed cases are annotated, not hidden); the `n_cite` proxy undercounts prose-only citers (R-haiku, R-sonnet-c, P-sonnet-c). Citations were verified only for the load-bearing answer-key hits and the top fabrication suspects (6 opened, all real); the rest of the ~200 cited works across 25 draws are unverified. The single least-confounded signal — the P0 bare-coinage arm showing more-confident *wrong-field* identifications at fable/codex than haiku's honest decline — is directionally consistent with the presentation half but is weak and case-bound. Actionable fix for any re-run: launch the runner from a temp dir OUTSIDE `/mnt/f/hub` with a clean environment so CLAUDE.md/AGENTS.md/MEMORY do not auto-inject; only then is the immersion arm a clean test.
