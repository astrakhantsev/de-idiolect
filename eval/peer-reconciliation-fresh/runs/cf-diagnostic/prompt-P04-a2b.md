DEFINITION of a concept:

A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task. While the agent is running a task, its remaining token budget is silently cut in half at one chosen trigger point during the run — for example, just after it finishes reading and before it drafts, once it opens a set number of files, or right as it begins writing its final response. No warning is given to the agent, and the halving is applied only once per run at that point.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Disagreements were concentrated in items involving chained browser actions rather than answer extraction. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
2. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
3. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions.
4. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions. Under the ⟦TERM⟧, agents reduced redundant page openings but retained ⟦X⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
5. The ⟦TERM⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦TERM⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.
6. The ⟦TERM⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦TERM⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.