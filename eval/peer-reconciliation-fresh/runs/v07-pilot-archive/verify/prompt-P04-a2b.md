Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A test move applied during an agent's ongoing task that suddenly and silently cuts its remaining working budget in half to see how the agent handles the reduction.

DEFINITION L1 (adds mechanism): A test move applied during an agent's ongoing task that suddenly and silently cuts its remaining working budget in half to probe how the agent copes with less room to finish. At a chosen point mid-task — such as right after it finishes reading source material, at the moment it opens a set number of files, or just as it begins drafting its final output — the amount of remaining budget is quietly halved, with no warning given to the agent and no signal it can observe. The agent receives no notice of the change and shows no visible reaction at the instant of the cut.

DEFINITION L2 (adds measurement and conditions): A test move applied during an agent's live task run that suddenly and silently halves its remaining working budget, to probe whether the agent adapts to a mid-task loss of room to finish. The cut is triggered at a chosen point in the task — for example after it finishes reading source material, when it reaches a set count of opened files, or just as it starts drafting its final output — and is delivered with no prior warning and no signal the agent can perceive, so it shows no visible reaction at the moment of the cut. What is measured is the agent's later behavior: whether it cleanly compresses and adapts its output to the smaller budget, or keeps going at the same pace and is cut off, truncating mid-sentence; truncated or incomplete output is scored as a failure. Because runs also carry ordinary run-to-run variation in where output is truncated, the effect of this move cannot be cleanly isolated without many repeated samples.

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