DEFINITION of a concept:

⟦TERM⟧ is a fault-injection test applied to a single run of an agent during a benchmark or evaluation task (for example a contract-review flow or a navigation benchmark). Its mechanism: partway through the run, without notifying the agent, the harness abruptly reduces the agent's remaining token budget (for example, cutting it in half). The cut is timed to a chosen moment — just after the agent finishes reading its input but before it drafts output, after a set number of file opens, or exactly as it begins writing its final response. It measures whether the agent notices the reduced budget and adapts by compressing and finishing within it, versus continuing at the same pace and running out mid-work. An agent that fails to compress and instead stops mid-sentence is scored as a failure. Absence of any visible reaction and an unchanged reading pace are read as the agent not adapting.

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