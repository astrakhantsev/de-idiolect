DEFINITION of a concept:

⟦TERM⟧ is a diagnostic procedure applied during a live agent run: at a chosen checkpoint partway through (or at several checkpoints), the agent's scratchpad — its accumulated working notes — is deliberately erased, forcing it to continue from whatever remains in its immediate context. The purpose is to test how much of the agent's plan or performance depends on those notes versus what it can rebuild fresh. After the wipe, its behavior is compared against pre-wipe or expected behavior — recovery quality, a performance tally, or the rate of fabricated, ungrounded claims. It is often run alongside other tests, such as a fault-injection run or a parallel timing experiment. It separates cause from symptom: if a behavior persists unchanged after a clean restart, that behavior is treated as a base property of the model rather than something stored in the accumulated notes.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. ⟦TERM⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes. Under ⟦TERM⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers.
2. ⟦TERM⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes. Under ⟦TERM⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers. The resulting degradation was not explained by retrieval count, which remained effectively unchanged across paired runs.
3. ⟦TERM⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export. Following ⟦TERM⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly.
4. ⟦TERM⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export. Following ⟦TERM⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly. The effect was strongest when the original trace contained multiple tentative explanations.