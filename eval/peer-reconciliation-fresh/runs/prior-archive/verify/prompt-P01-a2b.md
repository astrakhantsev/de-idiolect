DEFINITION of a concept:

⟦TERM⟧ names a failure pattern in which a single agent session, working through consecutive tasks in the same batch, carries the specific action or strategy that worked on its immediately preceding task over to the current, different task and applies it without re-checking whether it fits. The carried-over move (for example, a merge strategy, a grep-twice-then-guess pattern, or an open-file-patch-close move) was correct for the earlier task but wrong here, and it especially matters when a resource limit governs the task: the reused action trips or ignores that limit and the task fails. It is confirmed by clearing the session to remove memory of the recent task and re-presenting the same task cold, whereupon the agent chooses the correct action. The cause is recency bias toward the just-finished task, not any lack of capability; it is typically found incidentally while reviewing logs for another problem.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Session logs also exposed ⟦TERM⟧ following successful billing-repair tasks. ⟦TERM⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states.
2. Session logs also exposed ⟦TERM⟧ following successful billing-repair tasks. ⟦TERM⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance.
3. Under the ⟦X⟧, agents reduced redundant page openings but retained ⟦TERM⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
4. The same sessions were examined for ⟦TERM⟧ after high-confidence successes. ⟦TERM⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems.
5. The same sessions were examined for ⟦TERM⟧ after high-confidence successes. ⟦TERM⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time.
6. After removing halted sessions, ⟦TERM⟧ remained associated with prior trace length rather than prior answer correctness. The analysis is limited by the fixed task ordering; a fully randomized schedule may yield a smaller effect.