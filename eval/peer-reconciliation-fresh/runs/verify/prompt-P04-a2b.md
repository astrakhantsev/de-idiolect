Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task.

DEFINITION L1 (adds mechanism): A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task. While the agent is running a task, its remaining token budget is silently cut in half at one chosen trigger point during the run — for example, just after it finishes reading and before it drafts, once it opens a set number of files, or right as it begins writing its final response. No warning is given to the agent, and the halving is applied only once per run at that point.

DEFINITION L2 (adds measurement and conditions): A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task, applied during live agent runs on benchmark task suites such as contract review, navigation, and multi-agent tasks. During the run, at one chosen mid-task trigger point — for instance just after reading and before drafting, once a set number of files have been opened, or right as the final response begins — the agent's remaining token budget is silently halved, with no warning and the cut applied only once per run. It then observes whether the agent adapts by switching to shorter, compressed output and finishing within the reduced budget, or fails to adjust by truncating mid-sentence, getting cut off mid-trace, or running past the limit. Each agent is scored as a success if it adapts and a failure if it does not.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Disagreements were concentrated in items involving chained browser actions rather than answer extraction. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
2. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
3. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions.
4. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions. Under the ⟦TERM⟧, agents reduced redundant page openings but retained ⟦X⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
5. The ⟦TERM⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦TERM⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.
6. The ⟦TERM⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦TERM⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.