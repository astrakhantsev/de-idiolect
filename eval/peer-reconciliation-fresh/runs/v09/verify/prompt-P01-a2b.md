Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A recurring failure in which an automated agent reuses the approach that worked on its immediately preceding task instead of reasoning fresh about the current, different task.

DEFINITION L1 (adds mechanism): A recurring failure in which an automated agent reuses the approach that worked on its immediately preceding task instead of reasoning fresh about the current, different task's requirements. Concretely, having succeeded at one task with a particular action or pattern, the agent carries that same action over to the next task even though its conditions differ, producing a wrong outcome. That the choice was driven by recency rather than a capability gap is confirmed by clearing the session and re-presenting the same task cold, after which the agent picks the correct approach immediately.

DEFINITION L2 (adds measurement and conditions): A recurring failure in which an automated agent, handling consecutive tasks in one session, reuses the action or strategy that succeeded on the prior task instead of reasoning fresh about the current, different task. The prior solution was appropriate in its own context but is misapplied to the new task's differing conditions (such as tighter resource limits, required inputs, or a different failure type), producing a wrong result. What is measured is whether the carried-over approach matches what the current task actually requires, read off the agent's logs or traces after the fact. The diagnostic test is clearing the session and re-presenting the identical task, which makes the agent choose correctly at once, confirming recency rather than inability caused the miss. It arises across any task domain and is consistently traceable to recency rather than reasoning.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Session logs also exposed ⟦TERM⟧ following successful billing-repair tasks. ⟦TERM⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states.
2. Session logs also exposed ⟦TERM⟧ following successful billing-repair tasks. ⟦TERM⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance.
3. Under the ⟦X⟧, agents reduced redundant page openings but retained ⟦TERM⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
4. The same sessions were examined for ⟦TERM⟧ after high-confidence successes. ⟦TERM⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems.
5. The same sessions were examined for ⟦TERM⟧ after high-confidence successes. ⟦TERM⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time.
6. After removing halted sessions, ⟦TERM⟧ remained associated with prior trace length rather than prior answer correctness. The analysis is limited by the fixed task ordering; a fully randomized schedule may yield a smaller effect.