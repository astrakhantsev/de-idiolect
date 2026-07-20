DEFINITION of a concept:

A session-to-session error pattern in which, immediately after a high-confidence successful task, an agent replays that task’s action, search, and validation sequence on a subsequent task with an incompatible state. Its rate is the percentage of such subsequent tasks showing the replay: for example, 14% of access-control tasks after billing repair. It includes billing searches and validations reused on access-control work, and credential-reset actions repeated on unrelated incident-response systems after billing recovery. The pattern correlates with prior trace length, not prior answer correctness. Shortening traces without clearing history leaves it near its original rate; clearing prior-session traces or resetting session history substantially reduces it, with little effect on ordinary billing performance or a modest increase in tool setup time.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Blew away someone's WIP branch. Classic ⟦TERM⟧, and the tell was obvious in hindsight: clear the session, hand it the same ticket cold, and it picks the correct merge strategy first try. No capability gap, just recency doing the choosing instead of the task.
2. Going to rerun at five before we conclude anything. While debugging that I also caught a ⟦TERM⟧ case in the same log. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately.
3. Would've spent the whole day debugging the wrong thing without that log. While in there I also noticed a ⟦TERM⟧ case buried in the failure logs from the same batch. One of the agents had aced a similar-looking task earlier in the day by opening a config file, patching one line, and closing it — well within the ration — then tried the identical open-patch-close move on a task that actually needed cross-referencing two files simultaneously, tripped the ration, failed.
4. Long morning. Corvid replayed a ⟦TERM⟧ pattern on the deploy-verification task — it had just passed a task where restarting the service twice fixed a flaky health check, then tried restart-twice on a completely unrelated networking failure that needed an actual config fix. Cleared history, it diagnosed the real cause immediately, so same story as always: recency, not reasoning.