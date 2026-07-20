---
title: "Codex reviews of the v0.7 spec + implementation — doc review BLOCKING (10 findings): v0.7 reclassified as PILOT; findings = v0.8 spec requirements"
date: 2026-07-19
kind: review record (codex-doc-review of prereg.md + codex-review of the uncommitted diff; raw outputs persisted from session /tmp)
disposition: "v0.7 finishes unchanged and is scored as a PILOT (cannot fire the sealed TEST). Monotone scorer fix retained under the frozen scorer-toward-spec clause. All other findings deferred into a v0.8 re-freeze."
---

# v0.7 review record and disposition

## Code review (3 findings)

1. **[P1] Non-monotone profiles fell through to decompose** instead of insufficientEvidence per the frozen rule → **FIXED blind** (scorer-toward-frozen-spec clause; prereg's own text names non-monotone → insufficientEvidence).
2. **[P1] VariErr non-redistributable payload** untracked in repo → gitignored.
3. **[P2] recall-extender stage 3b self-matches** (top result selected from full corpus incl. owner community) → the entry's disclosed limit 3; post-deadline code fix or re-label as owner-retrieval diagnostic.

## Doc review: BLOCKING REVISION (verbatim findings, compressed)

1. **The amend-mid-run plan violates the freeze rule itself** — model calls had already occurred; blind folding does not satisfy "no threshold or rule may change after the first model call." Fix: v0.7 = pilot/finished-unchanged; all fixes go to a freshly frozen v0.7.1/v0.8 rerun from clean artifacts. **← ACCEPTED; governs the disposition.**
2. Composition table not exhaustive — (2,0)/(2,−1) without counterexamples match no rule; scorer has an undocumented insufficientEvidence branch. Fix: total 4×4 table over L ∈ {−1,0,1,2} + terminal flags.
3. Non-monotone routing divergence (= the code-review P1; spec text confirmed).
4. Evidence-absence and execution failures (input-insufficient, unparseable, refused, missing decompose) can become substantive classifications via L=−1 fallthrough. Fix: terminal insufficientEvidence/configFail for every infrastructure failure; distinguish semantic ABSTAIN from failure.
5. **closeMatch is three things at once** (escalation, E1b positive, "typed abstention") and collides with SKOS closeMatch (a mapping assertion); E1 is NOT substantively unchanged — TRAIN could pass with 6 correct + 3 false escalations; records schema has nowhere to put a non-relation escalation. Fix: rename (reviewRequired), serialize as status: abstained, decide explicitly whether false escalations fail the TEST bar, amend PROTOCOL.
6. Symmetry check level mismatch — a c≥2-at-L2 trigger is "confirmed" by an L1 re-judge, which is disagreement, not confirmation. Fix: re-judge the exact triggering level; L2-only failure = detail evidence, not breadth evidence.
7. Containment prompt positively biased ("known to be related"), no no_relation outcome, no machine-validated quotes — yet it can directly create hard relations. Fix: neutral wording + no_relation + verbatim-evidence requirement.
8. Ladder conformance unchecked — nothing verifies L1 ⊇ L0, L2 ⊇ L1, or checklist coverage; profiles may measure malformed ladders, the exact defect v0.7 diagnoses. Fix: conformance failures = configFail before verification.
9. E2 semantics undefined for v0.7 (inherited endpoint vs "not run" vs "E1 gates"); v0.6's gating logic was never preregistered. Fix: one explicit rule.
10. Effective-recipe delta claim incomplete (omits retained v0.6 stages; disciplined decompose originated v0.5); deleted repair docs still listed in corpus manifest; effective corpus not hashed in the freeze. Fix: full effective-spec delta table + manifest repair + corpus hashes in the freeze.

## Disposition

- **v0.7 = PILOT.** Finishes unchanged; scored under frozen v0.7 rules + the retained monotone fix; result reported with the pilot label; **cannot fire the sealed TEST key** (finding 1 + finding 5's bar-softening point).
- **v0.8** = fresh freeze addressing findings 2 and 4–10 (total composition table; terminal failure taxonomy; closeMatch → reviewRequired with records serialization + explicit TEST-bar rule; level-exact symmetry confirmation; neutral quote-gated containment with no_relation; ladder conformance gate; explicit E2 rule; effective-spec table + repaired, hashed corpus manifests), then a clean rerun. Post-deadline work unless directed otherwise.
- Meta-lesson, logged for the protocol: same-day amendment cycles outran the review cadence; the working rule going forward is the house norm — **no freeze without an independent review of the freezing document.**
