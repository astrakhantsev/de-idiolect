Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A robustness check that measures how much an agent's score on a task changes when the task's wording or formatting is altered.

DEFINITION L1 (adds mechanism): A robustness check that measures how much an agent's score on a task changes when only its wording or formatting is altered. For each item, a twin version is created that keeps the same underlying task or ask but varies only the surface phrasing or formatting, such as casual versus formal wording or a bullet list versus prose. Both versions are run through the agent under test, and their scores are compared.

DEFINITION L2 (adds measurement and conditions): A robustness check that measures how much an agent's score on a task shifts when only its surface wording or formatting changes rather than the underlying task itself. Each item is paired with a twin that preserves the same ask but varies only presentation, such as a casual message versus a formal numbered request, or a bullet list versus prose; both are run through the agent under test. What is produced is the performance gap between an item and its reworded twin, reported as an average point difference across the set. It is applied when evaluating agent results on a suite or roster of tasks, including on a reduced surviving subset of items. A smaller average gap is read as reassurance that the surviving items are testing genuine substance rather than the agent's ability to parse a particular format or phrasing.

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