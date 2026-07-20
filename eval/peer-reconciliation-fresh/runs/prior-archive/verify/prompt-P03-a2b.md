DEFINITION of a concept:

⟦TERM⟧ is a procedure for producing new evaluation items when building or expanding a test suite—for example, adding a harder "adversarial" difficulty tier. Instead of a person writing test cases by hand, a model is given an existing, easier tier of the benchmark and prompted to generate tougher variants of those items; no human authors any item from scratch. The resulting items are added to the suite's live pool and are scored the same way as everything else, by pass rate, with no separate validation step before they go into use. Items made this way are not checked afterward against real production incidents, and once added they can remain in the active pool indefinitely unless someone deliberately retires or audits them. The term names this generation method and the items it yields.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons.
2. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons. Generated tasks were filtered only for execution validity and duplicate surface form.
3. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces.
4. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks.
5. This pattern held after normalizing for the number of available tools and the length of task instructions. A second ⟦TERM⟧ round used newly sampled generators and fresh validators.