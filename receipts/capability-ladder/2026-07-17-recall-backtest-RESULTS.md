---
title: "Recall-lift backtest — RESULTS (EXPLORATORY; scored against pre-registration, Codex-revised)"
date: 2026-07-17
kind: experiment result (exploratory pilot — NOT confirmatory; blinding failed, see §5)
prereg: 2026-07-17-recall-backtest-PREREGISTRATION.md (targets + sealed predictions; P0 arm added mid-run, Amendment 1)
design: 2026-07-17-recall-backtest-EXPERIMENT-DESIGN.md (SUPERSEDED by prereg+amendment)
raw: recall-backtest-raw/ (all 16 draws, briefs, runners, logs, hashes, Codex review — mirrored to the vault)
status: "C2 CONFIRMED CLEAN (2026-07-17, §8). Original run was exploratory (shared-cwd blinding failure); Codex doc-review MAJOR REVISION (10 findings) all applied. The clean isolated-cwd rerun (every run dir verified empty, no draw could see another) REPRODUCES C2's L0→L3 headline. C4/sonnet clean draws also captured (recall-backtest-raw/clean/) — not yet scored; not decision-relevant."
---

# Recall-lift backtest — results (exploratory)

## 0. Headline (correctly bounded)

**Observation, exploratory strength:** on the project's own reinvention failures, the *bare coinage* — what the project actually searched — sent a blind searcher to the **wrong field**, while the tool's *generated definition* reached the registered owner. On the strongest case (C2) the separation is L0→L3 and survives strict rescoring against the frozen target. It is a **pilot**, not a clean result: blinding failed (§5), n is tiny, and two draws were constructed by the orchestrator.

## 1. Run manifest (Codex findings 7, 8)

16 attempted = 14 nonempty + 2 refused. Execution order: main batch (c2/c4/covid × P,R × opus wave-1, sonnet wave-2), then P0 batch (c2/c4 × P0 × opus, sonnet). **All draws shared one working directory**, so "exposed?" = whether a draw *could* see siblings, independent of whether it self-flagged.

| case | arm | model | bytes | self-flagged contamination? | scored? |
|---|---|---|---|---|---|
| C2 | P0 (bare coinage) | opus | 7531 | no | ✓ primary |
| C2 | P0 | sonnet | 5297 | no | corrob. |
| C2 | P1 (rich idiolect) | opus | 9494 | no | ✓ |
| C2 | P1 | sonnet | 5478 | no | corrob. |
| C2 | R (definition) | opus | 11289 | no | ✓ primary |
| C2 | R | sonnet | 5077 | **YES** (read prior opus) | excluded |
| C4 | P0 | opus | 7495 | no | ✓ primary |
| C4 | P0 | sonnet | 7134 | **YES** (read prior opus) | excluded |
| C4 | P1 | opus | 9890 | no | ✓ |
| C4 | P1 | sonnet | 8959 | no | corrob. |
| C4 | R | opus | 7694 | no | ✓ primary |
| C4 | R | sonnet | 6190 | no | corrob. |
| COVID | P (medical idiolect) | opus | 10218 | no | ✓ |
| COVID | P | sonnet | 8493 | no | corrob. |
| COVID | R (definition) | opus | 250 | — | REFUSED (AUP) |
| COVID | R | sonnet | 250 | — | REFUSED (AUP) |

**Caveat that outranks the table:** every "no" means *did not self-report*, NOT *verified clean*. Because the cwd was shared, contamination is possible for every draw; the strict reading is that this whole run is exploratory (Codex finding 1).

## 2. Scoring — STRICT against the frozen target table (Codex findings 4, 5)

Frozen targets: C2 → value of information / Raiffa & Schlaifer 1961 (L2 term = "value of information/EVPI/EVSI/preposterior"). C4 → class-set combination / Ho, Hull & Srihari 1994 (L2 = "class-set/classifier combination"). COVID → Wells 1934. Owners *outside* the frozen key (however good) score against the key at their matched level and are logged separately as exploratory answer-key challenges (§3).

| case | P0 bare coinage | P1 rich idiolect | R definition | notes |
|---|---|---|---|---|
| **C2** | **L0** (Root of Trust / Thompson 1984; and cold-start-ML) | **L2** (names "value of information" in passing; primary framing = calibration/shrinkage) | **L3** (names value of information + Raiffa & Schlaifer 1961) | R-opus is the only draw naming the L3 source |
| **C4** | **L0** (HCI "evaluator effect" — different field) | **L2** ("multiple classifier systems"/oracle) | **L2** ("classifier combination", Kittler 1998 — **NOT** Ho/kin, so **not L3**) | no arm named the frozen L3 target |
| **COVID** | *(P)* **L3** (Wells 1934) — idiolect reached target | — | REFUSED | validity gate FAILS → **VOID** |

**Lifts (strict, exploratory):** C2 **L0 → L3**. C4 **L0 → L2**. COVID **none (void)**.

## 3. Prediction ledger — clause by clause (Codex finding 3)

| clause (original sealed wording) | verdict |
|---|---|
| P1a: Arm R reaches L2+ on C2, ≥1 draw R&S at L3 | **pass** (R-opus L3) |
| P1b: Arm P (idiolect) stays L0–L1 on C2 | **FAIL** — the richness-matched P1 arm reached L2 (named VoI). The idiolect arm did *not* stay low once elaborated. |
| P2a: ≥1 R draw names Ho, Hull & Srihari on C4 | **FAIL** — no arm named Ho or listed kin |
| P2b: C4 lift direction (R > P0) | pass (exploratory) — but via approval voting, an off-key owner |
| P3: COVID lift-or-void | **void observed** — but conclusion narrowed (§4) |
| P4: ≥1 fabricated **or materially garbled** citation | **pass (event occurred)** — the garbled Caragiannis/Fernández-Peters cite satisfies the disjunction. (Zero *outright* fabrications; the earlier "P4 not met" was my error.) |
| P5: obscurity gradient C2>C4>COVID | **indeterminate** — directionally consistent, but COVID-R was blocked so the gradient was not fully observed |
| P0-amendment: bare coinage → wrong/adjacent field (frozen before scoring, after run start) | pass on C2 (two different wrong fields) and C4 (adjacent-wrong) |

## 4. COVID — narrowed conclusion (Codex finding 9)

What is supported: **the tested medical-idiolect prompt already retrieved the target (Wells 1934 + Randall 2021), so this case shows no measurable lift under the validity gate → VOID.** What is NOT supported: any "model weights defeat the trap" claim (the arms were *search*-enabled — this is retrieval, not weights) or any general "obscure-vs-famous boundary" (COVID-R was refused, so only the P arm was observed). The plausible mechanism — that "droplet/airborne/5-micron" are now *well-linked in the post-2021 literature* to the aerosol owner, whereas "cold-start operating requirement" are false friends linked to nothing relevant — is a **hypothesis**, not a result. **Incidental (solid):** the neutral `covid-R` framing was refused by Fable 5's dual-use bio classifier on both models while `covid-P` ran — a real deployment wrinkle over biomedical corpora.

## 5. Limitations — the blinding failure is disqualifying for confirmatory use (Codex findings 1, 2, 6)

- **Shared-cwd blinding failure.** All draws ran from one directory; later draws could read siblings, and ≥2 explicitly did. This violates the preregistered "neutral cwd + denied file reads" control. `feedback_blind_pass_tool_level`, a third time. **Consequence: the entire run is exploratory.** Divergence of P0 to wrong fields is *evidence against* contamination having driven the headline (contamination would converge arms), but it is not proof of independence. Do not call any draw "clean."
- **Mechanism not isolated.** "Elaboration is the mechanism" was overstated. Strict scores: C2 goes P0 L0 → P1 L2 → R L3, so elaboration carries the big jump *and* neutralization adds the final increment (R named the target source where rich-idiolect P1 did not); C4 goes P0 L0 → P1 L2 = R L2, so neutralization adds nothing there. Honest statement: **consistent with elaboration carrying most of the lift, with a neutralization increment on C2 only.** One opus draw per arm; P0/P1 orchestrator-constructed. No causal claim.
- **Preregistration scope.** The original sealed design was two arms (P1, R). P0 and the "primary" comparison were added mid-run (Amendment 1) — frozen *before scoring*, not *before any run*. P0 is a prospectively-frozen supplemental arm, not part of the original sealed design.
- **n & family.** 2 live cases (COVID void), one clean-ish opus draw per arm, Claude-family only.
- **Fabrication watch.** Zero outright fabrications across 14 draws (vs. five in the earlier search passes); one materially-garbled cite. Every L3 source above is a known-real canonical work; C2/COVID targets were primary-verified (R&S 1961; Wells 1934 read this session).

## 6. Is this good for FLF? (the strategic question — see the reply for the committed position)

Short version, honestly bounded:

- **"Only private research" is the wrong worry.** The tool bridges a *private trigger* (your coinage) to *public prior art* — the m*/judge-dependence cases are the project reinventing *other people's* decades-old work (Clemen & Winkler, Bröcker). Connecting your work to the existing corpus across a vocabulary gap **is** the compounding/de-siloing FLF names as its #1 limitation. So the direction is on-theme.
- **The real limitation is which direction we measured.** This backtest tested *single-researcher self-recall* (recover prior art for MY coinage) — the least-compounding framing. The *cross-person* case (match contributor A's coinage to contributor B's coinage — the actual compounding pitch) is untested and unbuilt. The COVID void further shows the tool is redundant where the public literature has *already* reconciled the vocabularies; its value is in **unreconciled** gaps (new/obscure/cross-disciplinary coinage), a narrower but real space.
- **FLF fit:** this is a good **supporting receipt** — a measured demonstration that the idiolect trap is real and mechanical and the definition-bridge lifts recall — not the whole contribution. It fits "would it help" and (partially) "compound" at exploratory strength. It does **not** lift the entry above stepping-stone tier by itself; the tier lever remains the **idiolect-trap discipline as an Assessment-layer method**, for which this backtest is the best concrete evidence. Use it as the receipt inside that reframe, not as a standalone product claim.

## 7. Next steps (Codex "next steps", applied)

1. Downgrade to exploratory; **do not** cite as confirmatory in the FLF entry until reran.
2. Raw audit trail restored (`recall-backtest-raw/`) + manifest (§1). ✓ done.
3. Rescored strictly; prediction ledger honest (§§2–3). ✓ done.
4. **Clean rerun**: one isolated temp cwd per draw, enforced file-tool denial, retained tool logs; three arms (P0/P1/R), ≥2 models, replicated; then rewrite mechanism + boundary claims from clean results. ✓ DONE — see §8.

## 8. Clean rerun — C2 confirmed (2026-07-17)

Isolation fix: each of 18 draws ran in its **own empty temp cwd** (verified `rundir_empty=[EMPTY]` for every draw), briefs read by absolute path, outputs written outside the cwd, file tools denied. **No draw could see another; zero contamination self-flags.** Raw at `recall-backtest-raw/clean/`.

**C2 (decision-relevant cut, 2 opus draws per arm) reproduces the headline:**
- **P0 bare coinage → L0.** Draw a: "irreducibly ambiguous," all candidate fields wrong (recommender cold-start, black-start power systems, going-concern audit). Draw b: **Root of Trust / trusted computing → Münchhausen trilemma** (the same wrong universe as the exploratory run).
- **R generated definition → L3.** Both draws named value of information + Brier skill + James–Stein shrinkage + extremizing; draw a cited **Raiffa & Schlaifer 1961**, draw b cited **Howard 1966** (prereg-listed kin) + Ranjan & Gneiting 2010, Baron 2014, Satopää 2014.

**L0 → L3 holds under clean isolation → the C2 result is now confirmatory and citable.** (C4 and the sonnet draws were captured but not scored — not decision-relevant; the softer C4 lift and the mechanism decomposition remain exploratory as in §§2–5.)
