---
title: "Detection-on-vault — experiment spec (stage 1 of the recall extender, measured on the vault's own idiolect)"
date: 2026-07-18
kind: experiment spec (pre-registration draft — NOT yet frozen; gold set needs user sign-off per §4.3)
status: draft — awaiting Codex + Fable review, then user sign-off, then freeze
relates_to: "2026-07-17-architecture-diagram.md (the grey node) · entry/FLF-entry-recall-extender.md §3.1, §4a limit 1 · 2026-07-17-recall-backtest-SESSION-SYNTHESIS.md"
---

# Detection-on-vault — experiment spec

## 1. The question

**Does automatic term recognition, run over this vault, surface the project's own coined and locally-loaded terms without being told what they are — and does it beat simply asking an LLM to do the same?**

Stage 1 (detection) is the only component of the architecture that is currently graded "runs, but not wired into the measured path." In the eggs prototype the keyness step executes, but the three evaluated concepts and their owning communities are hand-supplied, so no run has ever been end-to-end. This experiment is the cheapest available route to changing that, because the vault is a real multi-year corpus with genuine local vocabulary and a ground-truth list that already exists for other reasons.

**Why the vault specifically.** The memorization screen established that famous documented rediscoveries are systematically memorized (5/5 VOID from weights alone) while the project's own obscure coinage survives. Internal data is therefore not a convenience fallback for this system — it is the only clean source currently reachable.

## 2. What this does and does not claim

**In scope:** whether detection can *select* the terms a later stage would define, on one corpus, against a frozen gold set, with a baseline that could eliminate the component.

**Explicitly out of scope**, and not to be inflated into by any reviewer: cross-community matching, cross-person compounding, the commons, definition quality, retrieval lift, and any end-to-end claim. A successful run here makes an end-to-end run *possible*; it does not constitute one. This is an exploratory, cheap, wide measurement and the freeze lives at the boundary defined in §8 — reviewers should not propose confirmatory machinery for it.

## 3. Corpus

**Detection corpus (D):** markdown under `10_projects/` and `20_areas/`, excluding the exclusions below. This is the "community writing" the architecture says stage 1 watches.

**Reference corpus (R):** two references, run separately, because they answer different questions.
- **R1 — rest-of-vault.** Everything in D not belonging to the target project. Answers: is this term local *to this project* relative to its author's other work?
- **R2 — general English.** A standard reference wordlist/frequency table. Answers: is this term local relative to English at large?

**Mandatory exclusions — the circularity guard.** The following are removed from D entirely, because they discuss the coinages *as coinages* and would let detection "find" a term inside the very document that defines it:
- `10_projects/minelit/idiolect/**` (this folder — every doc here is meta-textual about the terms)
- `glossary.md`, `novelty-position.md`
- the agent memory directory and `MEMORY.md`
- `15_sessions/**`, `00_inbox/_*.md` (session mirrors and reply files are transcript artifacts, not authored prose)
- `99_private/**` — never read, never listed, never counted

Failing to exclude these would produce a strong, meaningless positive result. This guard is the single most important line in the spec.

## 4. Ground truth

### 4.1 Construction rule

A term enters the gold set only if **both** hold:
1. It appears in a **pre-existing artifact written before this spec** — `glossary.md`, the recall-backtest case labels, or a memory `feedback_*` / `reference_*` stem. These were authored for other purposes, so the gold set is not curated for this experiment.
2. It occurs **≥ 3 times as running text** in the detection corpus D after exclusions.

Criterion 2 is a **raw-frequency** filter, deliberately not a keyness filter, so constructing the gold set cannot leak the metric under test.

### 4.2 Two subsets, scored separately

The architecture claims detection covers two different phenomena, and they should not be averaged together:

- **G-coin — coinages.** Novel multi-word terms with no standard-English reading. Candidates: *recall extender · idiolect trap · definition-mediated naming · cold-start operating requirement · demand-gap screen · vacancy-demand signal · named-framework halo · tracker graveyard · revenue-search scissors · asymmetric pros-cons audit*.
- **G-sense — ordinary words carrying a local sense.** This is the harder and more distinctive claim, and the one keyness is least likely to reach. Candidates: *arm · cell · draw · kill · gate · strip · ladder · seam · vacancy · scissors · halo*, each of which carries a project-specific meaning here that its ordinary English sense does not predict.

### 4.3 Sign-off required before freeze

G-sense cannot be frozen by the spec author alone — deciding that "kill" or "gate" carries a genuinely local sense is a judgement about the author's own usage. **The user must confirm, amend, or reject each G-sense candidate before the gold set is frozen.** G-coin is mechanical enough to freeze on the §4.1 rule alone. On freeze, both subsets are written to a separate file and hashed; the hash goes in the results doc.

## 5. Arms

Four arms, run over the same corpus, scored against the same frozen gold set. **B3 is the reason this experiment is worth running.**

| arm | method | what it tests |
|---|---|---|
| **B0** | raw phrase frequency (most frequent n-grams in D) | the trivial floor — does anything beyond counting help at all? |
| **B1** | TF-IDF keyness, D vs R2 (general English) | the classic ATR formulation |
| **B2** | TF-IDF keyness, D vs R1 (rest-of-vault) | the community-local formulation the architecture actually specifies |
| **B3** | **LLM prompted directly:** "list the terms in this document that look like this group's own local vocabulary" | **the ablation — can a prompt replace the whole component?** |

**B3 is the load-bearing arm.** This session established that the raw term ties the constrained definition at rank 1, and that constrained vocabulary ties free-text prompting — twice now, a simpler baseline has matched a proposed component. Detection must be tested the same way before it is drawn as a required stage. If a plain prompt matches or beats the keyness arms, the honest conclusion is that stage 1 is a prompt, not a pipeline component, and the architecture diagram should say so.

**B3 contamination control.** B3 receives **only the document text** — never `glossary.md`, never memory, never this spec. Because user-global `CLAUDE.md` and `MEMORY.md` load into every `claude -p` invocation regardless of working directory (measured 5×, most recently 6/8 draws leaking from a temp cwd *outside* the vault), **B3 must run through the raw API with no harness config**, not through `claude -p` or a subagent. B0–B2 are deterministic and contamination-immune, so this control applies to B3 only.

## 6. Metrics

- **Recall @ k** against G-coin and G-sense separately, for k ∈ {10, 25, 50} per document/project.
- **Precision @ k** — judged by the user against the frozen gold set plus an "acceptable local term not in gold" category, since the gold set is certainly incomplete.
- **The gap statistic:** recall on G-sense minus recall on G-coin, per arm. This is the number that says whether the novel-sense half of the claim is real or whether detection only ever finds neologisms.

## 7. Sealed predictions

Recorded before any run, per the pre-registration discipline. Three numbers only.

1. **Keyness finds coinages and misses local senses.** B1/B2 recall on G-coin will substantially exceed their recall on G-sense, because TF-IDF keyness is a frequent-here-rare-elsewhere statistic and ordinary words carrying local meaning are *not* rare elsewhere. Confidence: **highly likely**.
2. **B3 matches or beats B1/B2 on G-sense.** An LLM reading prose can notice "this ordinary word is being used oddly here" in a way a frequency contrast structurally cannot. Confidence: **likely**.
3. **B2 beats B1 on G-coin.** Rest-of-vault is the better reference than general English, because the author's own non-project writing controls for personal style. Confidence: **likely**.

If 1 and 2 both hold, the architecture's stage 1 as drawn (ATR/keyness) is the wrong mechanism for half of what it claims to cover.

## 8. Decision rule

Written before the run so the result cannot be re-interpreted afterwards.

- **If B3 ≥ best keyness arm on both subsets** → detection is not a distinct component. Redraw stage 1 as a prompt, and record that a third proposed component was replaced by a simpler baseline.
- **If keyness wins on G-coin but loses badly on G-sense** → stage 1 is real but its scope claim is overstated. The entry and diagram must narrow "flag a word used in a group-local way" to coinage detection, and novel-sense detection becomes named future work.
- **If keyness wins on both** → stage 1 is validated on one corpus; the grey node becomes green *for this corpus only*, and an end-to-end run becomes possible.
- **In all three cases** the result is reportable. There is no outcome of this experiment that wastes the effort, which is the property that makes it worth running.

**Freeze boundary:** the gold set and these predictions freeze before the first arm runs. Nothing else in this spec is frozen — corpus tweaks and additional arms are allowed and should be logged, not suppressed.

## 9. Threats to validity

- **The author knows the vault.** I wrote or co-wrote much of D and chose the candidates in §4.2, so G-sense is exposed to selection. Mitigated by user sign-off (§4.3) and by the §4.1 rule that terms must come from artifacts predating this spec — not eliminated.
- **One corpus, one author, one idiolect.** Nothing here generalizes to cross-community or cross-person detection. It cannot, by construction.
- **The gold set is incomplete.** It is a lower bound on what detection *should* find, so recall is measurable but precision is not fully — hence the "acceptable but not in gold" category in §6.
- **"Coinage" is fuzzy.** The §4.1 rule makes membership operational rather than intuitive, but boundary cases will exist and should be logged rather than silently resolved.
- **Meta-textual inflation** is handled by §3's exclusions, and any failure of that guard invalidates the run rather than weakening it.

## 10. Deliverables and effort

A results doc with the scored table, the frozen gold-set hash, per-arm outputs, and the §8 decision applied; runnable scripts saved as named files under the prototype repo (not heredocs); raw per-arm outputs kept with the receipts.

Estimated at Claude-Code pace: **a few hours**, dominated by the corpus assembly and the user's precision judging, not by the modelling. B0–B2 are cheap and deterministic. B3 is a handful of raw-API calls.

**This does not fit before the FLF deadline (2026-07-19 AoE) and is not proposed as an entry component.** It is the named next experiment. The entry is submittable without it.

## 11. What this cannot answer

Whether the definition step helps, whether matching works across communities, whether verification is precise, whether the commons compounds, and whether any of this works for a second person. Those need different data, and two of them need data that one person's vault cannot contain at any effort level.
