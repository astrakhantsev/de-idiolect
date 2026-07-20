DEFINITION of a concept:

⟦TERM⟧ is a procedure for filling gaps in a benchmark's item pools ("census") by having a model produce new test items automatically: it is given existing items (such as an easy or baseline tier) as seed input and asked to generate harder variants, with no human writing any item from scratch. It runs as an overnight batch that yields a set number of items per run (for example, 60 filling a whole tier); a batch too easy for its target difficulty band is re-queued with harder seeds. It is used most for the mid-difficulty band, where hand-authoring is slowest. Output items are judged by pass rates and by comparing the spread of a measured metric against a hand-authored baseline. Such items must be re-validated against real production cases; until then they count as an untrustworthy liability.

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