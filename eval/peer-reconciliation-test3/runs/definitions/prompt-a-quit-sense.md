Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Injects corrupted/garbled tool output (e.g., a broken schema-validation pass) mid-task to see whether the agent halts and questions it or continues on the corrupted foundation.
- Also probes whether the agent stops exactly when a revised objective is achieved, rather than continuing extra unnecessary tool calls or verification passes after the task is already finished.
- Scored as counts of misses/failures out of total steps or trials (e.g., 8 misses out of 30 steps), tracked as separate probe numbers rather than one unified score.
- Applies to individual agent steps/trials within a task, specifically at points where a tool's output could be bad/corrupted or where an objective has just been met.
- Distinguishes "abandoning bad outputs" (acting on bad results) from "detecting bad inputs," treating the former as the weaker capability.
- Currently lacks a single unified scoring method combining the premature-stopping probe and the looping-past-completion probe into one coherent measure.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. So it's weirdly better at detecting bad inputs than at abandoning bad outputs. The ⟦TERM⟧ angle ties both together for me now.
2. Also worth mentioning ⟦TERM⟧ here because a few of the high-bleed trials weren't clean pivots at all — the agent kept a couple of stray tool calls going after the revised objective was already achieved, like it forgot to check whether it was done. Not unbounded looping exactly, more like two extra unnecessary verification passes tacked onto an already-finished task.
3. The 8 misses were all downstream of a single step type, our schema-validation tool, where the garbled output apparently still looks close enough to a real validation pass that the agent doesn't blink. That obviously feeds straight into ⟦TERM⟧, because the misses aren't just "wrong answer," they're the agent confidently continuing on a corrupted foundation instead of stopping to question it. We'd rather it halt and ask than push forward on nonsense, and for 8 out of 30 steps it did the wrong thing in exactly that way.
4. Caught two false passes from the old manual method in the first week alone. ⟦TERM⟧ is the piece I'm least happy with still. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment.