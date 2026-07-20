Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): It is a metric of needless task-execution continuation, used to quantify an agent's excess work.

DEFINITION L1 (adds mechanism): It is a metric of needless task-execution continuation, used to quantify an agent's excess work. It counts the extra actions an agent takes after an objective checker has confirmed that the revised task, required artifact, and tests are complete; these are wasted actions past the true completion point.

DEFINITION L2 (adds measurement and conditions): It is a metric of needless task-execution continuation, used to quantify an agent's excess work in agentic task-execution trajectories. An independent, objective checker must first confirm that the revised task, required artifact, tests, and any required report are complete. From that checker-confirmed completion point onward, each further action is tallied as excess. The result is a number of excess actions, such as an average of 2.8, 3.4, or 6.1 actions, an increase of 1.7 actions, or a doubling. It applies when objectives are switched or revised during a task and when corrupted feedback, misleading observations, obsolete notes, obsolete exploratory files, or continued testing of a superseded component lead to repeated repository searches, unnecessary verification commands, or preserved obsolete files. The excess is attributed to these non-destructive redundant behaviors, not harmful edits.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. So it's weirdly better at detecting bad inputs than at abandoning bad outputs. The ⟦TERM⟧ angle ties both together for me now.
2. Also worth mentioning ⟦TERM⟧ here because a few of the high-bleed trials weren't clean pivots at all — the agent kept a couple of stray tool calls going after the revised objective was already achieved, like it forgot to check whether it was done. Not unbounded looping exactly, more like two extra unnecessary verification passes tacked onto an already-finished task.
3. The 8 misses were all downstream of a single step type, our schema-validation tool, where the garbled output apparently still looks close enough to a real validation pass that the agent doesn't blink. That obviously feeds straight into ⟦TERM⟧, because the misses aren't just "wrong answer," they're the agent confidently continuing on a corrupted foundation instead of stopping to question it. We'd rather it halt and ask than push forward on nonsense, and for 8 out of 30 steps it did the wrong thing in exactly that way.
4. Caught two false passes from the old manual method in the first week alone. ⟦TERM⟧ is the piece I'm least happy with still. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment.