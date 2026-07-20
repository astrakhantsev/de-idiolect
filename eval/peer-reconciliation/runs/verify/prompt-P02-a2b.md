DEFINITION of a concept:

⟦TERM⟧ is a percentage score computed over a single multi-step agent run (such as a research-assistant or transactional/audit task). As the agent works, it writes intermediate notes or claims ("vendor B invoice is duplicate", "balance confirmed against PO 4471"); ⟦TERM⟧ is the proportion of those notes that are still true at the end of the run — that survive without being contradicted or disproven by the agent's own later steps. It is tracked across the run's steps, including during fault injection and recovery, which can add new unverified notes that lower it. The score falls as runs lengthen (fine early, dropping sharply past about step 15 in ~30-step runs). It should be checked before trusting final-answer accuracy — requiring, say, above 75% — since correct answers can ride on broken notes. In a fixed suite (same model, no fault injection) it is comparable month-to-month, and an unexpected drop signals either a real regression or a scorer bug.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. ⟦TERM⟧ was computed over all scratchpad claims retained in the execution trace. The median ⟦TERM⟧ was 0.74, with lower values concentrated in runs that copied provisional dates into the final table.
2. ⟦TERM⟧ was computed over all scratchpad claims retained in the execution trace. The median ⟦TERM⟧ was 0.74, with lower values concentrated in runs that copied provisional dates into the final table. To test containment, each trajectory received one malformed citation record after the fourth repository query.
3. ⟦TERM⟧ was calculated from planning notes, extraction notes, and draft justifications. The ⟦TERM⟧ averaged 0.69 in successful retrieval-first runs and 0.38 in inference-first runs.
4. ⟦TERM⟧ was calculated from planning notes, extraction notes, and draft justifications. The ⟦TERM⟧ averaged 0.69 in successful retrieval-first runs and 0.38 in inference-first runs. We introduced fixed delays to selected repository interfaces while holding returned content constant.
5. Agents verified a budget spreadsheet with cross-sheet formulas and supporting invoices. ⟦TERM⟧ was estimated over all stated subtotal checks and provenance notes. The ⟦TERM⟧ was 0.77 for runs that maintained a single reconciliation table, compared with 0.46 for runs that restated totals in prose.
6. ⟦TERM⟧ was estimated over all stated subtotal checks and provenance notes. The ⟦TERM⟧ was 0.77 for runs that maintained a single reconciliation table, compared with 0.46 for runs that restated totals in prose.