DEFINITION of a concept:

⟦TERM⟧ is a robustness check run on paired test items before they are trusted (e.g., before publishing or merging). For each item you take one underlying task and produce two or more variants that reword or reformat it while keeping the actual ask constant — casual versus formal phrasing, plain text versus boilerplate formatting, bullet list versus prose. You score each variant and compute the gap, the average point difference between the paired variants' scores. A small gap (e.g., 4 points) means the items measure task capability; a large gap means presentation cost is inflating or depressing scores rather than skill. You compare the gap against a baseline control set (such as hand-authored items) to judge whether it is larger or smaller than expected (e.g., six points versus two).

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. The benchmark paired each account-management task with a version containing irrelevant policy excerpts, historical tickets, and decoy URLs. ⟦TERM⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦TERM⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
2. ⟦TERM⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦TERM⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
3. A paired set of service-configuration tasks differed only in irrelevant operational context appended to the prompt. ⟦TERM⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦TERM⟧ preserved the same required configuration change, validator, and initial system state.
4. ⟦TERM⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦TERM⟧ preserved the same required configuration change, validator, and initial system state. Outputs from both task variants were then mixed into blinded grading pools.
5. The tool traces indicated that ⟦TERM⟧ changed navigation breadth more than final answer length.