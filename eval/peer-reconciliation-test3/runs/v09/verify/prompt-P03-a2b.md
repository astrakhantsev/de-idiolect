Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A test of whether an autonomous agent stops at the right moment while working through a task.

DEFINITION L1 (adds mechanism): A test of whether an autonomous agent stops at the right moment while working through a task. It works by injecting corrupted or garbled tool output (such as a broken schema-validation pass) partway through a task to see whether the agent halts and questions the bad result or keeps building on the corrupted foundation, and separately by checking whether the agent stops as soon as a revised objective has been met rather than adding extra unnecessary tool calls or verification passes. It treats acting on bad results (abandoning bad outputs) as a weaker capability than noticing bad inputs.

DEFINITION L2 (adds measurement and conditions): A test of whether an autonomous agent stops at the right moment while working through a task, checked step by step at points where a tool's output could be corrupted or where an objective has just been met. One probe injects garbled tool output (for example a broken schema-validation pass) mid-task to see whether the agent halts and questions it or confidently continues on a corrupted foundation; a second probe checks whether the agent stops once a revised objective is achieved instead of running extra unnecessary tool calls or verification passes. It distinguishes abandoning bad outputs from detecting bad inputs, treating the former as the weaker capability. Results are recorded as counts of misses or failures out of total steps or trials (for example 8 misses out of 30 steps), kept as separate probe numbers; there is currently no single unified score combining the premature-stopping probe and the looping-past-completion probe into one measure.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. An objective checker was run after every executable action and marked the earliest point at which the revised task was fully satisfied. ⟦TERM⟧ averaged 2.8 for trajectories that had correctly switched objectives. ⟦TERM⟧ was higher, at 6.1, when an agent retained obsolete notes or continued testing the superseded component.
2. ⟦TERM⟧ averaged 2.8 for trajectories that had correctly switched objectives. ⟦TERM⟧ was higher, at 6.1, when an agent retained obsolete notes or continued testing the superseded component. The excess was largely attributable to repeated repository searches rather than destructive edits.
3. This suggests that uncertainty about task structure made agents more willing to accept misleading feedback. ⟦TERM⟧ was evaluated only after a checker confirmed that the requested artifact and tests were complete. ⟦TERM⟧ increased by 1.7 actions under corrupted feedback, mostly through unnecessary verification commands.
4. ⟦TERM⟧ was evaluated only after a checker confirmed that the requested artifact and tests were complete. ⟦TERM⟧ increased by 1.7 actions under corrupted feedback, mostly through unnecessary verification commands.
5. ⟦TERM⟧ was tallied from the checker-confirmed completion point for the revised objective. ⟦TERM⟧ doubled when agents preserved obsolete exploratory files.
6. ⟦TERM⟧ was tallied from the checker-confirmed completion point for the revised objective. ⟦TERM⟧ doubled when agents preserved obsolete exploratory files.