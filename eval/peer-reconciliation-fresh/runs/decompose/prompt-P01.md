Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. Blew away someone's WIP branch. Classic ⟦T1⟧, and the tell was obvious in hindsight: clear the session, hand it the same ticket cold, and it picks the correct merge strategy first try. No capability gap, just recency doing the choosing instead of the task.
2. Going to rerun at five before we conclude anything. While debugging that I also caught a ⟦T1⟧ case in the same log. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately.
3. Would've spent the whole day debugging the wrong thing without that log. While in there I also noticed a ⟦T1⟧ case buried in the failure logs from the same batch. One of the agents had aced a similar-looking task earlier in the day by opening a config file, patching one line, and closing it — well within the ration — then tried the identical open-patch-close move on a task that actually needed cross-referencing two files simultaneously, tripped the ration, failed.
4. Long morning. Corvid replayed a ⟦T1⟧ pattern on the deploy-verification task — it had just passed a task where restarting the service twice fixed a flaky health check, then tried restart-twice on a completely unrelated networking failure that needed an actual config fix. Cleared history, it diagnosed the real cause immediately, so same story as always: recency, not reasoning.

COMMUNITY 2 EXCERPTS:
1. Session logs also exposed ⟦T2⟧ following successful billing-repair tasks. ⟦T2⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states.
2. Session logs also exposed ⟦T2⟧ following successful billing-repair tasks. ⟦T2⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance.
3. Under the ⟦X⟧, agents reduced redundant page openings but retained ⟦T2⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
4. The same sessions were examined for ⟦T2⟧ after high-confidence successes. ⟦T2⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems.
5. The same sessions were examined for ⟦T2⟧ after high-confidence successes. ⟦T2⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time.
6. After removing halted sessions, ⟦T2⟧ remained associated with prior trace length rather than prior answer correctness. The analysis is limited by the fixed task ordering; a fully randomized schedule may yield a smaller effect.
