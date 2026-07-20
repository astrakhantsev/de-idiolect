Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. So it's weirdly better at detecting bad inputs than at abandoning bad outputs. The ⟦T1⟧ angle ties both together for me now.
2. Also worth mentioning ⟦T1⟧ here because a few of the high-bleed trials weren't clean pivots at all — the agent kept a couple of stray tool calls going after the revised objective was already achieved, like it forgot to check whether it was done. Not unbounded looping exactly, more like two extra unnecessary verification passes tacked onto an already-finished task.
3. The 8 misses were all downstream of a single step type, our schema-validation tool, where the garbled output apparently still looks close enough to a real validation pass that the agent doesn't blink. That obviously feeds straight into ⟦T1⟧, because the misses aren't just "wrong answer," they're the agent confidently continuing on a corrupted foundation instead of stopping to question it. We'd rather it halt and ask than push forward on nonsense, and for 8 out of 30 steps it did the wrong thing in exactly that way.
4. Caught two false passes from the old manual method in the first week alone. ⟦T1⟧ is the piece I'm least happy with still. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment.

COMMUNITY 2 EXCERPTS:
1. An objective checker was run after every executable action and marked the earliest point at which the revised task was fully satisfied. ⟦T2⟧ averaged 2.8 for trajectories that had correctly switched objectives. ⟦T2⟧ was higher, at 6.1, when an agent retained obsolete notes or continued testing the superseded component.
2. ⟦T2⟧ averaged 2.8 for trajectories that had correctly switched objectives. ⟦T2⟧ was higher, at 6.1, when an agent retained obsolete notes or continued testing the superseded component. The excess was largely attributable to repeated repository searches rather than destructive edits.
3. This suggests that uncertainty about task structure made agents more willing to accept misleading feedback. ⟦T2⟧ was evaluated only after a checker confirmed that the requested artifact and tests were complete. ⟦T2⟧ increased by 1.7 actions under corrupted feedback, mostly through unnecessary verification commands.
4. ⟦T2⟧ was evaluated only after a checker confirmed that the requested artifact and tests were complete. ⟦T2⟧ increased by 1.7 actions under corrupted feedback, mostly through unnecessary verification commands.
5. ⟦T2⟧ was tallied from the checker-confirmed completion point for the revised objective. ⟦T2⟧ doubled when agents preserved obsolete exploratory files.
6. ⟦T2⟧ was tallied from the checker-confirmed completion point for the revised objective. ⟦T2⟧ doubled when agents preserved obsolete exploratory files.
