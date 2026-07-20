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

1. The drift audit identified a first plan-action mismatch in 17 trajectories, most often after an agent broadened its search without updating the stated inclusion rule. ⟦TERM⟧ was computed over all scratchpad claims retained in the execution trace. The median ⟦TERM⟧ was 0.74, with lower values concentrated in runs that copied provisional dates into the final table.
2. ⟦TERM⟧ was computed over all scratchpad claims retained in the execution trace. The median ⟦TERM⟧ was 0.74, with lower values concentrated in runs that copied provisional dates into the final table. To test containment, each trajectory received one malformed citation record after the fourth repository query.
3. The line-anchored rubric reduced apparent completion accuracy by 11 percentage points because several previously accepted outputs lacked any traceable basis for their inferred fields. ⟦TERM⟧ was calculated from planning notes, extraction notes, and draft justifications. The ⟦TERM⟧ averaged 0.69 in successful retrieval-first runs and 0.38 in inference-first runs.
4. ⟦TERM⟧ was calculated from planning notes, extraction notes, and draft justifications. The ⟦TERM⟧ averaged 0.69 in successful retrieval-first runs and 0.38 in inference-first runs. We introduced fixed delays to selected repository interfaces while holding returned content constant.
5. Agents verified a budget spreadsheet with cross-sheet formulas and supporting invoices. ⟦TERM⟧ was estimated over all stated subtotal checks and provenance notes. The ⟦TERM⟧ was 0.77 for runs that maintained a single reconciliation table, compared with 0.46 for runs that restated totals in prose.
6. ⟦TERM⟧ was estimated over all stated subtotal checks and provenance notes. The ⟦TERM⟧ was 0.77 for runs that maintained a single reconciliation table, compared with 0.46 for runs that restated totals in prose. A seeded-defect audit placed one invoice with a duplicated line item into the input bundle midway through verification.