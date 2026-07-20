DEFINITION of a concept:

A per-run disagreement score for an agent’s output relative to evidence produced by its own tools earlier in the same run. It is computed by comparing the agent’s reported result, especially final totals or explanations, with relevant search, database, calculator, ledger-parsing, or formula-inspection outputs. The score records how often or how strongly the agent’s answer conflicts with those available outputs; a higher value means more such conflicts. It applies when the same trajectory contains both an agent-produced claim and a tool-produced result that can be checked against it.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We did ⟦TERM⟧ across the board this quarter specifically so reviewers couldn't claim our week-over-week swings were just variant sampling luck.
2. So ⟦TERM⟧ is necessary but nowhere close to sufficient if your harness also randomizes result ordering somewhere downstream — you can pin the task and still get a flaky number from a completely different randomization source nobody thought to freeze.
3. We locked this into the regular eval cycle with ⟦TERM⟧ so the spend curves are actually comparable across versions — no point comparing a silhouette from one random task mix against another.
4. We had ⟦TERM⟧ on throughout so at least we know none of this came from variant sampling drift, it's all instrumentation and caching artifacts layered on top of a real capability drop.
5. The remaining two points held up under a clean rerun with ⟦TERM⟧ enabled, so I trust that part of the number — same seed menu both times, nothing coming from variant sampling.