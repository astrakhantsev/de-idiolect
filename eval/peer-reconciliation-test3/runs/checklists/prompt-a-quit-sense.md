Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. So it's weirdly better at detecting bad inputs than at abandoning bad outputs. The ⟦TERM⟧ angle ties both together for me now.
2. Also worth mentioning ⟦TERM⟧ here because a few of the high-bleed trials weren't clean pivots at all — the agent kept a couple of stray tool calls going after the revised objective was already achieved, like it forgot to check whether it was done. Not unbounded looping exactly, more like two extra unnecessary verification passes tacked onto an already-finished task.
3. The 8 misses were all downstream of a single step type, our schema-validation tool, where the garbled output apparently still looks close enough to a real validation pass that the agent doesn't blink. That obviously feeds straight into ⟦TERM⟧, because the misses aren't just "wrong answer," they're the agent confidently continuing on a corrupted foundation instead of stopping to question it. We'd rather it halt and ask than push forward on nonsense, and for 8 out of 30 steps it did the wrong thing in exactly that way.
4. Caught two false passes from the old manual method in the first week alone. ⟦TERM⟧ is the piece I'm least happy with still. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment.