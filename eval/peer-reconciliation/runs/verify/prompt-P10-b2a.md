DEFINITION of a concept:

A numeric rate computed in agent task runs where a calculator, ledger-parser, formula-inspection, search, or database tool produced an earlier result. It compares the agent’s final stated output or totals with that tool-derived value and counts cases in which they disagree. The score is the proportion of runs or cases showing that disagreement. It applies only after the relevant external tool result exists in the same trajectory. The rate can differ across conditions and rises when evidence contains near-duplicate or equivalent identifiers or records. Measuring it requires shuffling or randomizing equivalent records across repeated harness runs to control order and identity effects.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We did ⟦TERM⟧ across the board this quarter specifically so reviewers couldn't claim our week-over-week swings were just variant sampling luck. Every eval now draws from the exact same frozen seed list, task for task, run for run.
2. So ⟦TERM⟧ is necessary but nowhere close to sufficient if your harness also randomizes result ordering somewhere downstream — you can pin the task and still get a flaky number from a completely different randomization source nobody thought to freeze.
3. Compare that to the previous version which was flat the whole way through, and you can basically eyeball which one is going to blow the budget on a long task before you even check the score. We locked this into the regular eval cycle with ⟦TERM⟧ so the spend curves are actually comparable across versions — no point comparing a silhouette from one random task mix against another. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks.
4. We had ⟦TERM⟧ on throughout so at least we know none of this came from variant sampling drift, it's all instrumentation and caching artifacts layered on top of a real capability drop. Writing up a harness fix ticket for the caching bug before we run this suite again.
5. The remaining two points held up under a clean rerun with ⟦TERM⟧ enabled, so I trust that part of the number — same seed menu both times, nothing coming from variant sampling.