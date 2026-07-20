Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A recurring failure mode in which an agent reuses on a new task the approach that just worked on a recent prior one, instead of choosing what the new task requires.

DEFINITION L1 (adds mechanism): A recurring failure mode in which an agent, having just succeeded on a recent task, repeats that same successful action or strategy unchanged on a new and different task without re-checking whether it fits. It happens when two tasks are handled close together and the earlier one's winning approach superficially resembles the new one, so the recent success drives the choice rather than the current task's demands. The reused strategy then breaks a constraint the new task requires respecting. The tell is diagnostic: clear the session and hand the agent the same task in isolation and it chooses correctly, showing the mistake was carryover, not inability.

DEFINITION L2 (adds measurement and conditions): A recurring failure mode in which an agent reuses on a new task the exact action or strategy that just succeeded on a recent prior task, applying it unchanged without re-evaluating fit. It arises when two tasks are handled close together in the same session or batch and the earlier task's successful approach superficially resembles the new one, so recent success rather than the current task drives the choice. The carried-over strategy then exceeds or mismatches a task-specific constraint the new task actually requires respecting, such as a resource ration or cost budget. What is read from the failure or session logs is whether the reused strategy was well-suited (constraint respected, correct choice) or ill-suited (constraint tripped, task failed). The confirming test is to clear the session and re-present the same task alone: the agent then chooses correctly, showing the error stems from recency bias in picking the strategy, not from any deficit in its underlying ability to solve the new task.

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