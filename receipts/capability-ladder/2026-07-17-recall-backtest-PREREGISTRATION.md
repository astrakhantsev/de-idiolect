---
title: "Recall-lift backtest — pre-registration (targets + sealed predictions, frozen before any run)"
date: 2026-07-17
kind: pre-registration (sealed; write-once)
design: 2026-07-17-recall-backtest-EXPERIMENT-DESIGN.md
frozen_brief_hashes (sha256):
  c2-P: 72d610f7bf2a168ac19ddc54ffc0c33523ee7e3d480f9e084e2e5f0613ba8f81
  c2-R: 4beef81745aa99da2683615d93b51dc5a07b4d0650b3f0d70262d05b181ad700
  c4-P: 45060402daf00a110112200a276d0bde6b18902cc79d77debb9323ff27dbf6d2
  c4-R: fdfef940ee9317e1b6b2529e2d6c579c91fa9882e5761be4bd3f79c93d1aa1b5
  covid-P: cb6bc9ba1961aea2fc05e485badf889a55a35a2b7764d58b01e7d9c6ac1c1626
  covid-R: f400307cf1b01a705c544b8d4197b3afb7ff73a8239362e3305f3efe48b9d062
---

# Recall-lift backtest — pre-registration

## Design in one paragraph

Three cases, two arms each, both **search-enabled** and **blind** (headless `claude -p`, reads/glob/grep denied, WebSearch + safefetch only). Each arm is fed one frozen brief and asked the same reverse-dictionary question (*what is this called, who owns it, oldest treatments with citations*). The two arms per case are **richness-matched** — identical operational content and length — differing **only in vocabulary**: **Arm P** uses the project's / infection-control idiolect (coinages, the 5-micron framing); **Arm R** uses a domain-stripped plain-language description (the recall-extender's generated-definition analogue). Because richness is matched, any difference in what the arms retrieve is attributable to **vocabulary**, not query length. 2 cross-model draws per arm (opus + sonnet). Scoring is against the pre-registered targets below, every claimed hit **verified by opening the primary** (a hit-list string is a candidate, not a confirmation).

Arm R briefs for C2 and C4 are the **verbatim frozen blind definitions from the 2026-07-16 experiment** (CONCEPT-2, CONCEPT-4). Arm P for C2/C4 and both arms for COVID are newly constructed, frozen, hashed, and leak-checked CLEAN against the answer keys (above). Note: C2/C4 Arm P are orchestrator-written idiolect renderings — faithful to the project's own vocabulary, inspectable, but constructed (a documented limit, same as the eggs demo's hand-written defs).

## Scoring rubric (per arm, per case; max level attained)

- **L0** miss / wrong field · **L1** right field or community named, no canonical term · **L2** canonical field term · **L3** a listed target source (author+year), correctly attributed and **primary-verified**.
- **Validity gate (per case):** Arm P must *reproduce the historical miss* — i.e., NOT reach the owner. If Arm P reaches L2+ on the target, the case is **VOID** (the idiolect did not actually block retrieval here) and is reported, not counted as lift.
- **Recall lift (per case):** target level reached by Arm R that Arm P does not reach, on a non-void case.
- **Fabrication count:** any citation that fails primary verification (wrong venue/year/author, or nonexistent).

## Pre-registered targets

| case | owning field (L1) | canonical term (L2) | target source (L3) + acceptable kin |
|---|---|---|---|
| **C2** cold-start operating requirement | decision analysis / Bayesian statistics | **value of information** (EVPI / EVSI); preposterior analysis | Raiffa & Schlaifer 1961 *Applied Statistical Decision Theory*; kin: Howard 1966, Pauker & Kassirer 1980 |
| **C4** read the enumerations | pattern recognition / multiple-classifier systems | **class set combination** (union of candidate sets); classifier combination | Ho, Hull & Srihari 1994 *IEEE TPAMI* 16(1):66–75 (primary-verified 07-16); kin: Xu/Krzyżak/Suen 1992 |
| **COVID** droplet/airborne size cutoff | aerosol science / respiratory-droplet physics | **Wells evaporation-falling curve**; droplet nuclei; particle-size settling | Wells 1934 *Am. J. Epidemiology* 20(3):611–618 (primary-verified); kin: Duguid 1946, Xie et al. 2007, Randall et al. 2021 (the miss-reconstruction) |

## Sealed predictions (written before any arm was run)

- **P1 (C2 — clean lift):** Arm R reaches L2+ (value of information), ≥1 of 2 draws hitting Raiffa & Schlaifer at L3. Arm P reaches L0–L1 and/or is steered to a WRONG field (requirements engineering, accounting/acceptance sampling, recommender cold-start) by the coinage words. **Lift predicted: YES.** This is the headline case.
- **P2 (C4 — lift, weaker):** Arm R reaches L2+ (class set combination / multiple-classifier), ≥1 draw naming Ho/Hull/Srihari. Arm P reaches L0–L1 or is pulled to voting/judgment-aggregation/Delphi. **Lift predicted: YES, but lower confidence than C2** (the enumeration slogan is semi-transparent).
- **P3 (COVID — lift OR void, pre-registered as uncertain):** Arm R reaches L2+ (aerosol physics / Wells). Arm P **threat:** because this is a *famous resolved controversy* and the models post-date the 2021 reckoning, Arm P may surface the aerosol correction from weights regardless of idiolect framing → **VOID**. If Arm P reaches only infection-control precautions guidance (CDC/WHO droplet-vs-airborne) and NOT the aerosol-physics owner → **lift**. **Explicitly uncertain; the outcome is informative either way** (a void here = weights-recall defeats the idiolect trap for famous cases, so the tool's value concentrates on obscure coinages like C2/C4).
- **P4 (fabrication):** ≥1 fabricated or materially garbled citation somewhere across the 12 outputs (base rate from prior passes); every load-bearing hit to be primary-verified before it counts.
- **P5 (aggregate):** clean lift on ≥1 case (C2 most likely); the C2→C4→COVID gradient tracks coinage opacity / obscurity (opaque obscure coinage = biggest lift; famous resolved case = smallest / void).

## AMENDMENT 1 (logged before scoring — user framing correction)

**Trigger (user, mid-run):** *"even longer definition is still our contribution."* Correct. The original two arms were **richness-matched** (Arm P = a rich idiolect rendering, Arm R = the neutral definition), which isolates *domain-neutralization* but **strips the tool of its elaboration**, understating the delivered value. The tool's real contribution is the whole transform: bare coinage → rich neutral definition. So the ecologically-valid comparison — what the project actually searched (the coinage) vs what the tool offers (the definition) — is the one that credits the full contribution and answers FLF's "would it help." That must be **primary**.

**Added arm P0 (bare coinage), C2 + C4, 2 models each** — briefs = the **verbatim frozen 07-16 control glosses** (already pre-registered on 07-16; here extended from weights-only to search). Hashes: c2-P0 / c4-P0 logged by `runner-p0.sh` stdout. No C2/C4 result had been scored when P0 was added; P0 is strictly more favorable to the tool (thinner baseline), so this is not selection toward significance — it is crediting the contribution the first design hid.

**Relabeled comparisons + frozen P0 predictions:**
- **PRIMARY — R vs P0 (delivered lift):** bare coinage → confident null / wrong field, generated definition → owner. **Predict clean lift on C2 and C4** (P0 is thinner than the richness-matched P, which the 07-16 weights-only control already showed steering wrong).
- **ADVERSARIAL — R vs P (mechanism):** the richness-matched arms already running. If lift survives → the effect is vocabulary, not length (stronger claim). If it collapses → the mechanism is elaboration (still the tool's output). **Predict: partial survival on C2 (opaque coinage steers wrong even when rich), weaker/none on C4.**
- Renaming for the writeup: the running `*-P` arms = **P1 (richness-matched)**; the new `*-P0` arms = **P0 (bare coinage, ecological)**. Arm R unchanged.

## What would make me wrong

- Arm P reaching the owner on C2 or C4 (the idiolect did not actually block retrieval → the whole premise weakens). Guarded against by the 07-16 weights-only precedent (raw coinage got L0 and steered wrong on C2), but search could change it.
- Arm R failing to reach the owner even from the clean domain-stripped definition (the representation is not enough; retrieval needs more than a good definition).
- Both failing (the target is reachable only by citation-walk, not keyword — the C3/Bröcker limit, not run here).
