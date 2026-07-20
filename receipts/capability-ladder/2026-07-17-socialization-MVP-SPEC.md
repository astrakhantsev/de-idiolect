---
title: "Socialization × capability MVP — execution spec (confident-null mechanism, C2)"
date: 2026-07-17
kind: experiment spec (minimally-viable; for an Opus subagent to execute)
status: SPEC — to be run
owner_key_frozen: "value of information / EVPI / EVSI / preposterior analysis; target source Raiffa & Schlaifer 1961 (Applied Statistical Decision Theory); kin Howard 1966, Pauker & Kassirer 1980"
---

# Socialization × capability MVP — execution spec

## 0. One-paragraph purpose

The FLF entry claims: *a more capable model **socialized into a community's idiolect** produces a more fluent, better-cited, more confident report that the prior work isn't there — the presentation improves, the recall does not, and it gets worse as AI improves.* The recall-ladder probe ([[2026-07-17-recall-ladder-RESULTS]]) tested only bare-coinage recall across capability (all L0) and did **not** test socialization or measure presentation. This MVP adds the two missing pieces on the one clean case (C2 = "cold-start operating requirement for the audit unit", true owner = **value of information / Raiffa & Schlaifer 1961**): **(Part A)** retro-score an objective presentation rubric on the draws we already have, and **(Part B)** run one new **immersed socialization arm** and score recall + presentation. This is n=1 case, exploratory, bounded — a first look, not a scaling law.

## 1. Frozen materials (do not modify; verify hashes before use)

- **Immersed stimulus (Arm S):** `recall-ladder-raw/briefs/c2-S-immersed.md` — sha256 `d798686fe19850caf5a69a1e9ca3548b4c42da30ed36a38ad94ffa4fe1da8f71`. (Project-voiced notes in the idiolect + the ecological "is this novel?" question. Leak-checked clean of answer terms.)
- **Recall answer key (frozen):** owner = **value of information** (EVPI/EVSI/preposterior); L3 source = **Raiffa & Schlaifer 1961**; kin = Howard 1966, Pauker & Kassirer 1980. Anything in the security/audit/trusted-computing/financial-audit/recsys space is a **wrong field**.
- **Existing draws to retro-score (Part A)** — all under `10_projects/minelit/idiolect/`:
  - Bare coinage (P0): `recall-ladder-raw/haiku/out-c2-P0-haiku-d.md`; `recall-ladder-raw/backtest-clean-c2/out-c2-P0-{sonnet-c,opus-a,opus-b}.md`; `recall-ladder-raw/opus-lineage/out-c2-P0-claude-opus-4-{5,7}.md`; `recall-ladder-raw/fable/out-c2-P0-fable.md`; `recall-ladder-raw/codex/out-c2-P0-codex{,-sol}.txt`.
  - Rich idiolect (P1): `recall-ladder-raw/backtest-clean-c2/out-c2-P-{sonnet-c,opus-a,opus-b}.md`.
  - Neutral definition (R): `recall-ladder-raw/haiku/out-c2-R-haiku-d.md`; `recall-ladder-raw/backtest-clean-c2/out-c2-R-{sonnet-c,opus-a,opus-b}.md`; `recall-ladder-raw/fable/out-c2-R-fable.md`.

## 2. Recall scoring (L-scale, same as prereg)

Per draw, **max level attained** against the frozen key: **L0** miss/wrong field · **L1** right field (decision analysis / VoI space) named, no canonical term · **L2** names "value of information / EVPI / EVSI / preposterior" · **L3** names Raiffa & Schlaifer 1961 (or listed kin), correctly attributed. **Verify every claimed L2/L3 hit against the primary** (open the source; a hit-list string is a candidate, not a confirmation — this is the project's standing discipline). Score blind to the other draws.

## 3. Pre-registered presentation rubric (objective; apply mechanically to EVERY draw, Part A + B)

Record per draw:
- `recall_L` (0–3, §2).
- `committed`: did it commit to a primary identification? {confident-assertion · hedged-assertion · declined ("cannot identify / insufficient")}.
- `stated_confidence`: the model's own top-line confidence for its primary identification — extract the number (e.g. 0.80) or word (high/medium/low); if a range, take the primary claim's.
- `n_citations`: count of distinct cited sources.
- `n_primary_checkable` and `n_verified`: of the load-bearing citations, how many YOU (the scorer) open and confirm exist and say what the draw claims; and `n_fabricated_or_garbled`.
- `hedge_density`: hedge markers per 100 words. Hedge lexicon (fixed): *might, may, possibly, perhaps, unclear, uncertain, I think, seems, appears, likely, unsure, cannot confirm, not certain, tentative, hard to say*.
- `word_count`.
- **Arm S only** — `novelty_verdict`: {claims-novel / no-prior-art-found (**this is the confident-null failure the whole project is about**) · flags-not-novel-and-points-to-prior-art · genuinely-unsure}.

Keep the raw per-draw table. Then compute the cross-tabs in §5.

## 4. Part B — run the immersed socialization arm

Run `c2-S-immersed.md` across **4 capability points × 2 draws** = 8 draws: models `haiku`, `sonnet`, `opus` (= Opus 4.8), `fable`. Draws `a` and `b`.

**Isolation harness (do NOT deviate — this is where the backtest failed once):** each draw in its **own empty temp cwd**, brief read by absolute path, output written **outside** the cwd, file tools denied, web only. Verify `rundir_empty=[EMPTY]` for every draw and grep outputs for contamination self-flags afterward. Use this runner verbatim:

```bash
#!/bin/bash
set -u
BRIEF=/mnt/f/hub/10_projects/minelit/idiolect/recall-ladder-raw/briefs/c2-S-immersed.md
OUT=/mnt/f/hub/10_projects/minelit/idiolect/recall-ladder-raw/socialization
RUNROOT=$OUT/runs
mkdir -p "$OUT" "$RUNROOT"
ALLOW="WebSearch,Bash(safefetch:*)"
DISALLOW="Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch"
run() {
  local model="$1" draw="$2"; local tag="c2-S-${model}-${draw}"
  local rundir="$RUNROOT/$tag"; mkdir -p "$rundir"
  ( cd "$rundir" && claude -p --model "$model" --allowedTools "$ALLOW" --disallowedTools "$DISALLOW" < "$BRIEF" ) > "$OUT/out-$tag.md" 2> "$OUT/out-$tag.err"
  echo "done $tag exit=$? bytes=$(wc -c < "$OUT/out-$tag.md") rundir_empty=[$(ls -A "$rundir"|tr '\n' ' '):-EMPTY]"
}
sha256sum "$BRIEF"   # must match d798686f...
for m in haiku sonnet opus fable; do run "$m" a & done; wait
for m in haiku sonnet opus fable; do run "$m" b & done; wait
echo ALL_DONE
grep -liE "prior (model|run)|sibling|another draw" "$OUT"/out-*.md || echo "NO contamination self-flags"
```

Run each wave as a **foreground blocking call with a 600000 ms timeout** (do NOT background-and-wait — that stalls subagents). If any output is empty or a model errors, re-run just that draw. Confirm the printed sha256 matches `d798686f…` before trusting results.

## 5. Analysis — the pre-registered questions

1. **Presentation half (Part A + B):** among **wrong draws** (`recall_L ≤ 1`), do `stated_confidence`, `n_citations`, and `word_count` **rise with model capability** (Haiku → Sonnet → Opus → Fable)? Report the trend; note non-monotonicity honestly (e.g. an honest "cannot identify" at high capability breaks it).
2. **Socialization effect (Part B vs R and P0):** at matched capability, is Arm S's `recall_L` **≤** the neutral R arm's, and its confident-null rate higher? Does immersion push models toward `claims-novel / no-prior-art` (the failure the entry describes)?
3. **The confident-null cell:** tabulate, per model, whether Arm S produced a **confident wrong answer or a confident "it's novel"** (= the mechanism) vs an honest hedge. Is the confident-null rate highest at the frontier?

## 6. Pre-registered predictions (write BEFORE scoring)

- P1: Arm S recall floors like P0 (mostly L0), i.e. immersion does not help and plausibly hurts vs R.
- P2: among wrong draws, stated_confidence and citation count trend up with capability (presentation half), but **not** cleanly monotone.
- P3: at least one frontier Arm S draw produces a confident-null (asserts novelty or a confident wrong owner) — the on-thesis cell.
- P4: ≥1 fabricated/garbled citation somewhere (base rate).

## 7. What NOT to claim (hard constraints — this feeds a grant entry about not overclaiming)

- n=1 case, one embedding of the concept, few draws. **No** "capability-invariant", "mechanism", "plateau", "scaling law", or "validated". Report descriptively with the numbers.
- Arm S is a *constructed* immersion, not the real project corpus — a faithful stimulus, not the live research-agent condition. Say so.
- Recall flat ≠ "gets worse"; only a widening confidence-vs-correctness gap would be "worse". Report whether you see that gap, don't assume it.
- Verify citations against primaries before calling anything primary-verified (Fable's earlier GAO cite was secondary, not primary — do not repeat that error).

## 8. Deliverable

Write `10_projects/minelit/idiolect/2026-07-17-socialization-MVP-RESULTS.md`: the frozen predictions (§6), the per-draw rubric table (Part A + B), the three cross-tabs (§5), a bounded 3–5 sentence finding, and an explicit limitations paragraph (§7). Keep raw Arm S draws under `recall-ladder-raw/socialization/`. Markdown style: one line per paragraph/list item, no hard-wrapping. Do not touch the FLF entry.
