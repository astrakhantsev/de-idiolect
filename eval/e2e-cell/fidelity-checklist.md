# Fidelity checklist — frozen BEFORE generation (spec rev 3 §2.3; rev-2 findings 2 + 4b folded)

The generated definition, judged ONLY against the frozen excerpts, must have EVERY item below explicitly satisfied. **Omission fails** — an item not affirmatively PRESERVED is a failure, not a pass (rev-2 finding 2).

- (i) concerns a decision about whether an instrument/signal/tool is worth building or acquiring — must be PRESERVED
- (ii) is conditioned on a stated quality or accuracy level of that instrument — must be PRESERVED
- (iii) is prospective — the decision is made BEFORE the instrument is built — must be PRESERVED
- (iv) has threshold structure — act if quality clears a bar — must be PRESERVED
- (v) contains no benchmark, dataset, or metric specifics absent from the excerpts — must be PASS
- (vi) **external-name ban (rev-2 finding 4b):** the judge lists EVERY named field, discipline, method, author, or acronym appearing in the definition; any such name not present in the excerpts = FAIL. (This closes the named-solution-family hole the leak list alone cannot: an unlisted name like a specific technique or literature label would make retrieval trivial without tripping the frozen greps.)

**Failure rule (frozen):** any of (i)–(iv) not PRESERVED, or (v) violated, or (vi) non-empty → that generator config FAILS. No regeneration on fidelity grounds — fidelity failure is a result.

**Judge configuration (frozen):** claude opus via `run_isolated.sh` (credentials-only home, tools denied). Response schema: a JSON object `{"i": {"verdict": "...", "quote": "..."}, ..., "vi": {"names_found": [...], "names_not_in_excerpts": [...]}}`. Malformed output → exactly one re-ask with "Return only the JSON object."; still malformed → conservative FAIL for that config (rev-2 finding 2).

**Judge prompt (verbatim):** "You are given source notes and a candidate definition. Judge ONLY against the notes; do not use outside knowledge of what the concept 'should' be. For items i–iv answer PRESERVED or NOT-PRESERVED (treat omission as NOT-PRESERVED) with a one-sentence quote-based justification from the notes. For item v answer PASS or UNSUPPORTED-ADDITION with justification. For item vi, list every named field, discipline, method, author, or acronym in the definition, and separately list which of those do NOT appear in the notes. Return only a JSON object with keys i,ii,iii,iv,v,vi."
