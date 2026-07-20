DEFINITION of a concept:

A number, usually reported as a percentage, that scores how well the intermediate claims or notes an agent records during a task hold up by the end of the run. Inputs are the trail of statements the agent generates while working; the output is a single value where higher means more of those statements remained verified, reconciled, and internally consistent rather than being left unchecked or later contradicted by the agent itself. It is tracked per run and compared across agents, model versions, and time. Low values flag agents whose working notes include fabricated, unreconciled, or self-disproved claims, even when the final answer is correct. It applies whenever an agent produces a multi-step reasoning record, and is watched for degradation.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. ⟦TERM⟧ was computed over all scratchpad claims retained in the execution trace.
2. The median ⟦TERM⟧ was 0.74, with lower values concentrated in runs that copied provisional dates into the final table.
3. ⟦TERM⟧ was calculated from planning notes, extraction notes, and draft justifications.
4. The ⟦TERM⟧ averaged 0.69 in successful retrieval-first runs and 0.38 in inference-first runs.
5. ⟦TERM⟧ was estimated over all stated subtotal checks and provenance notes.
6. The ⟦TERM⟧ was 0.77 for runs that maintained a single reconciliation table, compared with 0.46 for runs that restated totals in prose.