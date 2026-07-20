Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A procedure for building test items, used to create a harder difficulty level out of an existing easier one.

DEFINITION L1 (adds mechanism): A procedure for building test items that produces a harder difficulty level from an existing easier one. Instead of a person writing each new item by hand, an automated text-generating model is given the existing easy items and asked to produce more difficult variants of them. The new, tougher items are added to the test suite to extend how far its difficulty reaches.

DEFINITION L2 (adds measurement and conditions): A procedure for constructing benchmark or test-suite items that produces a harder or more challenging difficulty tier out of an existing easier tier. A text-generating model is prompted with the current easy items and asked to write tougher variants, so no person authors the new items from scratch; this yields a set of new advanced items (for example, sixty added to a coding benchmark) that push past the original items' difficulty. Difficulty is judged by how often the items are passed and by comparing the performance gap between the generated set and hand-written items (such as a small measured wording gap). The resulting items must be clearly marked as model-produced rather than passed off as human-written, and their difficulty tends to rise unevenly and lumpily, echoing the generating model's own training patterns instead of a deliberately designed progression.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons.
2. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons. Generated tasks were filtered only for execution validity and duplicate surface form.
3. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces.
4. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks.
5. This pattern held after normalizing for the number of available tools and the length of task instructions. A second ⟦TERM⟧ round used newly sampled generators and fresh validators.
6. The final audit used 1,200 paired operational tasks generated under a ⟦TERM⟧. The ⟦TERM⟧ supplied executable validators while withholding task-generation traces from every evaluated system.