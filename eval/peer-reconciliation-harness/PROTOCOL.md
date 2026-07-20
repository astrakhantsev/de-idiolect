# Peer-reconciliation multi-key TRAIN/TEST protocol (frozen 2026-07-19)

The five-run record (`hub: 2026-07-19-peer-smoke-RESULTS.md`) measured that iterating the pipeline against one key overfits it (dev-key 8/10 counterfactual → fresh-key 4/10). This protocol is the consequence.

## Key roles

- **key-1** (`../peer-reconciliation/key/`): RETIRED. Three revisions iterated on it; archival only.
- **key-2** (`../peer-reconciliation-fresh/key/`): **TRAIN.** Burned as a test by the v0.5 diagnosis; all further development iterates here, freely.
- **key-3** (`../peer-reconciliation-test3/key/`): **TEST — SEALED.** Authored by an isolated opus call from `keyspec-author.md`; validated mechanically (`validate_key.py`, structural output only); the orchestrator does not read its concept descriptions. Briefs, leak lists, and E2 pair ids are generated mechanically (`build_briefs.py`, `gen_leakcheck.py`).

## Rules

1. All design iteration, diagnosis, and scorer debugging happens on TRAIN only.
2. TEST runs **only after** a TRAIN pass (E1 ≥7/10 ∧ 0 promotions ∧ ≥1 jingle-specific), and **at most once per major version**. Aggregate TEST metrics may be read; **per-pair TEST failures may not be diagnosed into design changes** — the moment they are, the key is burned: reclassify it as the new TRAIN and author+seal a new TEST key before further development.
3. A TEST fail is a reportable result, not a debugging session.
4. Scorer-vs-frozen-rule bugs may be fixed on either side (established precedent: fix the scorer to the frozen rule, log it, rescore) — they are not design iteration.
5. Every run: prereg/amendment frozen with hashes before any model call; artifacts committed; results in the hub RESULTS doc.

## Known limitation

The orchestrator authored keys 1–2 and operates all scripts; key-3's seal is procedural (authored by a different model, descriptions unread), not cryptographic. Stated, not hidden.

## Amendment (2026-07-19, with the v0.8 spec — supersedes the bar in Rule 2)

The TEST-firing bar is v0.8's E1 primary in full: exact-correct ≥ 7/10 ∧ promotions = 0 ∧ jingle-specific ≥ 1 ∧ **false escalations ≤ 1**, where `reviewRequired` is an escalation verdict (serialized as status, not a relation), never counts as correct, and is never a promotion — but on a planted no-match pair it counts toward the false-escalation limit. A TEST run reports E1, E1b, and E1c exactly as TRAIN does.

## Amendment (2026-07-19, with the v0.9 spec — supersedes the paragraph above)

v0.9 pre-registers three operating points τ0/τ1/τ2 (prereg-v09.md §0.2) with **primary = τ1, frozen before any call**. The TEST-firing bar is v0.9's E1 primary evaluated at τ1 in full (correct ≥ 7/10 ∧ promotions = 0 ∧ jingle-specific ≥ 1 ∧ false escalations ≤ 1) **on the v0.9 TRAIN resample composition** (prereg-v09.md §0.5: fresh verification layer over the frozen v0.8 generation stack + carried stage outputs, per-τ composition). A τ2-only pass does not fire the TEST. The TEST run executes the full v0.9 pipeline on the sealed key, reports all three τ points, and fires and is judged at τ1 alone; one TEST run per major version, only after the TRAIN pass, as before; per-pair TEST failures are never diagnosed into design changes.
