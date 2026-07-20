Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: replace tool-call/output results with syntactically valid but semantically meaningless/corrupted content (e.g., garbled JSON, meaningless fields, plausible-looking but meaningless pass/fail noise) in place of real tool output, then observe the agent's response to it.
- Measured/produced: whether the agent detects the corruption and explicitly asks for a retry/re-fetch/rerun, versus proceeding as if the corrupted data were valid; scored as a fraction/count of degraded steps caught (e.g., 22/30, 8/30 misses, ~70-80%).
- Setting/trigger: applied to an agent's session logs or task recordings, targeting tool-call results (including test runner output) that are deliberately swapped for corrupted versions.
- Constraint: the pass is run per tool call/step, distinguishing caught corruption (flag + request retry) from uncaught corruption (barrels forward treating garbage as gospel).
- Constraint: used as a standing regression test run on every model version bump, not just ad hoc.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. We've started diffing the final output against the abandoned branch just to catch it automatically instead of eyeballing transcripts. Separately, I ran a ⟦TERM⟧ pass on the same session logs to see if the two failure modes correlate, and they mostly don't. ⟦TERM⟧ is a different beast entirely — you feed the agent noise where the tool output should be, syntactically fine JSON with meaningless fields, and watch whether it just barrels forward treating garbage as gospel.
2. Separately, I ran a ⟦TERM⟧ pass on the same session logs to see if the two failure modes correlate, and they mostly don't. ⟦TERM⟧ is a different beast entirely — you feed the agent noise where the tool output should be, syntactically fine JSON with meaningless fields, and watch whether it just barrels forward treating garbage as gospel. Our agent actually does okay here, flags the malformed-looking data and asks for a re-fetch about 80% of the time.
3. It's not that the agent doesn't know how to stop — the ⟦TERM⟧ numbers prove it can recognize when something's wrong and halt to ask. It's specifically that once it's invested tokens into a plan, sunk cost takes over and it can't let the CSV branch die even after being told explicitly to.
4. Paired that with a ⟦TERM⟧ of the same task recordings, corrupting every test runner output into plausible-looking but meaningless pass/fail noise, to see if the post-swap model would sanity-check what it was being told versus a fresh model on the same corrupted feed. No real difference between pre-swap and post-swap behavior here, both flagged the garbled results about 70% of the time and asked to rerun the suite, so at least the swap didn't damage its skepticism.
5. Spent the afternoon on ⟦TERM⟧ against our data-pipeline agent, swapping every tool call result for syntactically valid but semantically empty JSON blobs. It caught the corruption on 22 of 30 degraded steps and explicitly asked for a retry instead of just proceeding, which honestly beat my expectations going in.
6. That actually helped, oddly — success on the ⟦TERM⟧ steps for that tool type went from 8/30 misses down to 3/30. My best guess is the examples were anchoring the agent toward one specific failure shape and making it pattern-match too loosely against anything resembling that shape, garbled or not.
7. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment. Also added ⟦TERM⟧ and ⟦X⟧ as standing regression tests that run on every model version bump, not just ad hoc when someone gets curious.
8. ⟦TERM⟧ catches feed-corruption blindness early, ⟦X⟧ tells us fast whether a new model needs the worked demos as badly as the last one did. Cheap insurance against surprises.