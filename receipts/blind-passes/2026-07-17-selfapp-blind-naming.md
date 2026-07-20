---
title: "Self-application blind naming pass — the tool's own coinage, defined and blindly named"
date: 2026-07-17
kind: research data
status: "COMPLETE (2 of 3 draws). opus + sonnet draws succeeded and are contamination-clean; the default draw hit a TRANSIENT 'Usage credits' error (NOT an account quota wall — the interactive session and later claude -p calls, incl. --model opus/sonnet, all work). All 5 sealed predictions hit; the blind pass corroborated the map AND surfaced closer prior art the earlier passes missed (EDC, GESIS, Guo)."
method: "The tool demonstrated on itself, per criteria-first §2.4: the project's own coinage (working name withheld here and in the brief) was flagged by the glossary (detection), given a hand-written constrained definition (plain common words + simple notation, no proper names, no field terms — an approximation of the tool's fixed-word-list constraint, since no generator is built), and the definition alone was handed to blind searchers to name the thing and type its relations to what exists (matching). Frozen brief `def-naming-raw/selfapp-brief.md`, sha256 66da20b8034e16d0a336778f5d3ebb944950e2164e135d4e79f58cc5a9223d7b. Grep-verified CLEAN (0 hits) against the Pass-A ban list PLUS recall|precision|retriev|corpus|coinage|annotat. Three cross-model draws (opus/sonnet/default), WebSearch + bare safefetch, reads blocked (--disallowedTools Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch), query-ledger mandate, contamination grep after."
siblings: 2026-07-17-assembly-blind-passA.md (the novelty-position instrument; different question — that pass validated the assembly's absence claim, this pass completes the glossary row for the coinage and demonstrates the tool's own loop on its own name)
---

# Self-application blind naming pass

## Sealed predictions (orchestrator, before any run returned)

- **P1.** ≥2/3 draws place the whole in ontology/schema-matching or terminology/thesaurus territory (the assembly Pass-A precedent).
- **P2.** ≥2/3 draws independently reproduce the SKOS mapping-relation identification for the four labels (same thing / more general / more specific / related), despite the brief containing none of those field words.
- **P3.** 0/3 draws label any existing system **same thing** (exactMatch). This is the assembly row's kill-check re-run through the tool's own loop; if a draw does, and the claim survives orchestrator verification, the novelty position's `open (candidate)` on the assembly is wrong and the entry must say so.
- **P4.** ≥1 draw surfaces an owner or field no prior pass reached (prior base rate: every pass so far).
- **P5.** The union of proposed practitioner names (Q3) reaches ≥2 of the Gate-2 B-opus Q4 elements — pay-as-you-go / onomasiological / concept search / gloss- or definition-based matching — none of which appear in the brief.

## Results — 2 of 3 draws succeeded (opus + sonnet); default draw hit a transient error

**Correction to my own earlier note:** an initial check made *while the draws were still running* saw the default draw's error and two 0-byte files and wrongly concluded the whole run was quota-blocked. In fact the opus and sonnet draws completed a few minutes later (~16 KB each) and are valid. The default draw alone returned `Usage credits are required for this model` — a **transient** condition, **not** an account quota wall: the interactive session and subsequent `claude -p` calls (including `--model opus` / `--model sonnet`) all work fine. Archived: `def-naming-raw/out-SA-{opus,sonnet,default}.md`, `selfapp-brief.md`, `runner-selfapp.sh`.

**Blindness verified at tool level** (per `feedback_blind_pass_tool_level`): draws ran with `Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch` denied; contamination grep of both outputs against vault/project terms (`dashboard|_input|minelit|judge-dependence|recall.extend|idiolect|astrakhantsev|[2-employer-terms-redacted]`) = **0 hits**. Genuinely blind.

**Sealed-prediction scorecard (2 valid draws): 5 / 5 hit.**
- **P1 ✓** — both placed the whole in ontology-matching / terminology / IR-vocabulary territory (opus: "definition-mediated cross-vocabulary retrieval"; sonnet: "pay-as-you-go ontology alignment").
- **P2 ✓** — both reproduced the SKOS mapping relations verbatim (exactMatch/broadMatch/narrowMatch/relatedMatch) from the W3C spec, unprompted.
- **P3 ✓ (the kill-check) — held:** both explicitly found NO single "same thing" system (opus: "I found none… best read as an original composition"; sonnet: "No single item earns 'same thing'").
- **P4 ✓✓** — new owners no prior pass reached: **EDC** (opus — closest structural twin, since opened in primary) · **GESIS cross-concordances / KoMoHe** (sonnet) · **Guo et al. 2024 "Personalized Jargon Identification"** arXiv:2311.09481 (sonnet — the detection step) · SOLVENT / analogy-mining (both; Chan = FLF contributor) · Lesk 1986 (sonnet). *(The user separately surfaced **KGGen** NeurIPS 2025 and **Relink** arXiv:2601.07192 — same landscape.)*
- **P5 ✓** — practitioner-name proposals hit the Gate-2 elements (pay-as-you-go, ontology alignment, concept matching, definition-mediated / on-the-fly crosswalking).

**The payoff (the method working on itself):** the blind self-application both corroborated the earlier map AND surfaced closer prior art the targeted + assembly passes had missed — EDC most importantly. This is the "stunt that is also the method": the tool's own loop, run blind on its own description, found neighbours a socialized search did not. Folded into `novelty-position.md` and the entry §5.

**Verification status:** EDC opened in primary (abstract); KGGen opened in primary (method); GESIS + Guo remain run-level (the draws' reads), to be opened before any public reliance. A third draw can be added anytime: `bash def-naming-raw/runner-selfapp.sh`.
