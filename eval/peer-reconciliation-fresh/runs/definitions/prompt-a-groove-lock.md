Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: the agent applies whatever approach/pattern worked on its immediately preceding task, carrying it over to the current, different task rather than reasoning fresh about the current task's requirements.
- Diagnostic test: clearing the session/history and re-presenting the same task causes the agent to pick the correct approach immediately, confirming the failure was recency-driven, not a capability gap.
- What's measured: whether the carried-over action or strategy matches what the current task actually requires (correct vs. mismatched approach), read off agent logs/traces after the fact.
- Setting/trigger: arises across consecutive tasks handled in the same session/history, where task N's successful action is reused on task N+1 despite differing conditions (e.g., resource constraints, required inputs, or failure type).
- Constraint: the prior task's solution was appropriate for its own context (worked correctly there) but is misapplied to the new task's different context, producing a wrong outcome or failure.
- Constraint: occurs regardless of the specific domain (branch merges, file greps, config patches, service restarts), consistently traceable to recency rather than reasoning.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Blew away someone's WIP branch. Classic ⟦TERM⟧, and the tell was obvious in hindsight: clear the session, hand it the same ticket cold, and it picks the correct merge strategy first try. No capability gap, just recency doing the choosing instead of the task.
2. Going to rerun at five before we conclude anything. While debugging that I also caught a ⟦TERM⟧ case in the same log. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately.
3. Would've spent the whole day debugging the wrong thing without that log. While in there I also noticed a ⟦TERM⟧ case buried in the failure logs from the same batch. One of the agents had aced a similar-looking task earlier in the day by opening a config file, patching one line, and closing it — well within the ration — then tried the identical open-patch-close move on a task that actually needed cross-referencing two files simultaneously, tripped the ration, failed.
4. Long morning. Corvid replayed a ⟦TERM⟧ pattern on the deploy-verification task — it had just passed a task where restarting the service twice fixed a flaky health check, then tried restart-twice on a completely unrelated networking failure that needed an actual config fix. Cleared history, it diagnosed the real cause immediately, so same story as always: recency, not reasoning.