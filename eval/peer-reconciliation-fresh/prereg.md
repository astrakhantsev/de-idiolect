# Peer-reconciliation v0.5 — FRESH-KEY TRANSFER TEST, pre-registration

Frozen before any v0.5 generation or pipeline call; sha256 into `freeze-manifest.txt`. This run answers ONE question: **does the recipe iterated on the first key transfer to a key it has never seen?** (The project's measured prior is 7/7 in-sample recipes failing their fresh-item bar — this is that bar.)

## The frozen recipe (v0.4 minus the failed gate, plus disciplined decompose)

Identical to `../peer-reconciliation/prereg.md` + amendments v0.3/v0.4 with exactly two deltas:
1. **Core-specificity gate REMOVED from all pass conditions** (its v0.4 measurement was invalid: register-dominated bundle cosines, both valid cores false-negatived, target threat already handled by retrieval separation). `core_specificity.py` still runs as a **diagnostic only**.
2. **Decompose prompts carry a commitment discipline** (the v0.4 "single anomaly" recurrence): quantifiers and restrictive details are allowed in the core only if BOTH sides' excerpts support them; no catch-all generalization phrases; one-sided details belong in that side's residue.

Everything else frozen as-is: corpora register + families (A forum sonnet, B preprint codex terra), v0.4 excerpt windows (neighbor-drop + ⟦X⟧ masking), checklist-guided definitions (D_A opus, D_B codex terra), polarity gate, retrieval mutual-hit rule, v0.3 decidable-count aggregation, composition rule order (corrected rule 3), endpoints and bars (E1 ≥7/10 ∧ 0 promotions ∧ ≥1 jingle-specific; E2 per pair: decompose+quotes ∧ core-check ≥1 instantiates ∧ 0 contradicts per scoreable side ∧ ≥1 residue far-side exclusion; E3 n/a — already demonstrated, not re-run), leak checks (term lists updated to the fresh key's terms — a key change, not a rule change), records machinery.

## Fresh key

`key/concepts.json` + `key/answer_key.json`: 18 new fictitious agent-evaluation concepts, zero overlap with the first key, same class structure (2 exact · broad(a) · broad(b) · 2 relatedMatch with planted cores/residues · 2 jingle "echo test"/"salt run" · 2 noMatch). Authored by the orchestrator before any generation; never readable by pipeline calls.

## Pre-registered predictions (written before any call)

1. **Broad/narrow (P03, P04) are expected misses** — the known-open class (mechanism-specific definitions undermine the covers direction; thin-bundle abstains). The dual-register fix is deliberately NOT included so any fresh-key failure is attributable to transfer, not to an untested mechanism. Achievable ceiling if both miss: 8/10.
2. E1 PASS (≥7/10) is the transfer claim. A fresh-key score materially below the first key's counterfactual 8/10 = the recipe overfit its development key; report as such.
3. Jingle protection is predicted to hold via retrieval separation + fails/fails + similarity flag (decompose reachable only on mutual hits).

## Deviations handling

Scorer bugs fixed to frozen rules with logs (established precedent); deterministic classifier refusals marked unscoreable with ≥1-scoreable-side requirement; no threshold or rule may change after the first model call.

## AMENDMENT v0.6 (logged 2026-07-19, BEFORE any v0.6 call; this workspace is now the TRAIN key per ../peer-reconciliation-harness/PROTOCOL.md)

Three changes answering the v0.5 fresh-key defect classes; everything else frozen:

1. **Coverage floor (corpus input):** after initial extraction, any term with <4 DEV excerpts triggers a 3-document repair generation (same family, same register, mandatory thin-term usage); repair docs are numbered 12–14 and are DEV by construction; HELD-OUT stays docs 09–11. Full re-extraction, re-checklists, re-definitions, re-verification follow (a fresh run, not a patch).
2. **Symmetry check before broadnarrow (the P02 false-asymmetry fix):** a covers/fails(c≥2) asymmetry may assert broadnarrow ONLY if the failing direction is re-judged by the OTHER model family (b2a→opus, a2b→codex terra) and that second judge independently produces fails with c≥2 under the frozen aggregation; otherwise insufficientEvidence("asymmetry-unconfirmed").
3. **Directed containment question after decompose success (the P04 containment fix):** rule 5's decompose-success path no longer asserts relatedMatch directly; a codex-terra call answers t1_within_t2 / t2_within_t1 / partial_overlap / unclear from both masked excerpt sets; containment → broadnarrow with the derived side, partial_overlap → relatedMatch, unclear → insufficientEvidence. Jingle protection unchanged (decompose ABSTAIN → similarity flag path).

Endpoints and bars unchanged. TRAIN discipline: iteration permitted here; the sealed TEST key (key-3) is run only on a TRAIN pass (E1 ≥7/10 ∧ 0 promotions ∧ ≥1 jingle-specific), at most once, per PROTOCOL.md.

## AMENDMENT v0.7 (logged 2026-07-19, BEFORE any v0.7 call) — definition ladder + reject-option scoring

**Reversions (evidence-based):** repair docs 12–14 DELETED (v0.6 measured them as a clean negative: quantity up, decidability down); coverage floor dropped. Corpus reverts to the v0.5 state, so v0.7 differs from v0.5 by exactly: the ladder, the profile composition, closeMatch, and the scoring additions. Kept from v0.6: symmetry check (now on the level-1 judgment), containment question, disciplined decompose.

**1. Definition ladder.** Per term, ONE generation call produces three cumulative levels from the commitments checklist: **L0** = one sentence, the kind of thing and its immediate purpose (genus; NEVER sufficient for any match assertion — profile-shape evidence only); **L1** = L0 + the specific mechanism/process; **L2** = L1 + what is measured/how scored + applicability conditions (≈ the v0.4–v0.6 definition). JSON out {"L0","L1","L2"}; leak checks on the whole file; polarity gate and retrieval use L2 (minimal change from prior runs); symmetry check uses L1.

**2. Matrix verification.** One call per pair-direction judges every excerpt against ALL THREE levels (same instantiates/contradicts/insufficient verdicts). Quotes required for decided verdicts at L1/L2 and machine-checked as before; L0 is quote-exempt (it never carries match evidence). Per-level aggregation under the unchanged v0.3 rule. Per direction, the **coverage level L** = highest level whose aggregate is `covers` (−1 if none); non-monotone profiles (covers above a fails) are logged and treated as mixed → insufficientEvidence.

**3. Profile composition (frozen table; La = a2b coverage level, Lb = b2a).**
1. Polarity configFail → configFail. All levels <2 decidable in both directions → insufficientEvidence.
2. La=2 ∧ Lb=2 → exactMatch.
3. (La=2 ∧ Lb=1) ∨ (La=1 ∧ Lb=2) → **closeMatch** (divergence only at the detail level — the measured over-specification signature; an escalation verdict, not a match assertion).
4. La=2 ∧ Lb≤0 with c≥2 at L1 or L2 in b2a ∧ symmetry check (other family re-judges b2a against D_B L1) confirms fails with c≥2 → broadnarrow(a); mirror → broadnarrow(b); symmetry unconfirmed → closeMatch.
5. Otherwise (max(La,Lb) ≤ 1): mutual retrieval hit ∧ decompose success → containment question: t1_within_t2 → broadnarrow(b), t2_within_t1 → broadnarrow(a), partial_overlap → relatedMatch, unclear → closeMatch; no decompose path: identical/similar term strings → noMatchDespiteSimilarity, else noMatch.

**4. Scoring.** **E1 primary UNCHANGED and remains the TEST-firing bar** (≥7/10 exact-correct ∧ 0 promotions ∧ ≥1 jingle-specific; closeMatch counts as a typed abstention — neither correct nor a promotion; closeMatch on a no-match-class pair is tallied separately as a *false escalation*, not a promotion). Pre-registered secondaries: **E1b detection** (positive = any of exactMatch/broadnarrow/relatedMatch/closeMatch; negative = noMatch*; scored against planted match-class membership) and **E1c graded** (correct 1.0 · insufficientEvidence 0.4 · closeMatch on a match-class pair 0.7 · closeMatch on a no-match pair 0.2 · wrong hard assertion 0; reported, not gating). Rationale: reject-option / error–reject framing (Chow); deployment is triage, not oracle.

E2 not run for v0.7 (same deviation logic as v0.6: E1 gates). Models, families, isolation, leak rules, endpoints otherwise unchanged.
