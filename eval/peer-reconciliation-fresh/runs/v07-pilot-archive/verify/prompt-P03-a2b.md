Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A procedure for producing new items to add to an evaluation suite by having an existing model create them, in order to expand the suite with harder tests.

DEFINITION L1 (adds mechanism): A procedure for producing new items to add to an evaluation suite so it can be extended with harder tests. An existing model is handed the suite's easier or earlier items and prompted to write new, tougher variants of them, and no person authors any of the new items by hand. The result is a fresh batch of test items that gets folded into the suite.

DEFINITION L2 (adds measurement and conditions): A procedure for extending an evaluation suite with new, harder test items without a person writing any of them. An existing model is given the suite's easier or earlier items and prompted to generate tougher variants; the resulting items (for example, a harder tier of a coding benchmark, or entries in a running census of items) are added directly to the suite. Their quality is judged only informally, by whether the pass rates they produce look reasonable, rather than by checking them against real production incidents or outcomes. Because the items are never validated against real-world results after creation, they can stay live in the suite over many months without anyone re-checking them, so they may drift, go stale, or end up carrying no useful signal while still counting as part of the suite.

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