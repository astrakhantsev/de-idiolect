Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A checking procedure that tests whether an item's score depends on how the request is worded rather than on the actual task it poses.

DEFINITION L1 (adds mechanism): A checking procedure that tests whether an item's score depends on how the request is worded rather than on the actual task. The same underlying task is rewritten into two phrasing variants (for example casual versus formal, or terser and more casual versus the original) while keeping the ask identical, and both the original and its reworded twin are run through the same evaluation. The outcomes on that identical underlying task are then compared.

DEFINITION L2 (adds measurement and conditions): A checking procedure that tests whether an item's score is driven by wording rather than by the actual task it poses. Each item is rewritten into two phrasing variants (for example casual versus formal, bullet list versus prose, or terser and more casual versus the original) while the ask is kept identical, and both the original and its reworded twin are run through the same evaluation. It measures the average point gap in score between the original phrasing and the reworded phrasing, comparing each original item against its own matched twin rather than against unrelated items. It applies to existing test suites or item tiers, including ones already in use or newly generated (such as a model-generated 'hard' tier), to see if wording is confounding difficulty. A smaller average gap is read as reassuring, meaning items measure substance not surface formatting; a larger gap indicates wording is compounding the measured difficulty.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. The benchmark paired each account-management task with a version containing irrelevant policy excerpts, historical tickets, and decoy URLs. ⟦TERM⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦TERM⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
2. ⟦TERM⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦TERM⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
3. A paired set of service-configuration tasks differed only in irrelevant operational context appended to the prompt. ⟦TERM⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦TERM⟧ preserved the same required configuration change, validator, and initial system state.
4. ⟦TERM⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦TERM⟧ preserved the same required configuration change, validator, and initial system state. Outputs from both task variants were then mixed into blinded grading pools.
5. The tool traces indicated that ⟦TERM⟧ changed navigation breadth more than final answer length.
6. Each task family included ⟦TERM⟧ with identical required actions and variable irrelevant context. ⟦TERM⟧ increased excess tool usage by 26% for the largest agent.