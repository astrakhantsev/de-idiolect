DEFINITION of a concept:

A numeric score, roughly from 0 to 1, computed from retained scratchpad claims, planning and extraction notes, draft justifications, subtotal checks, provenance notes, and provisional conclusions recorded during a multi-step agent run. It applies when the run retrieves, extracts, or verifies external material before producing its final answer. The score asserts how consistently those intermediate claims are reconciled as the run proceeds: it falls when provisional dates are copied into a final table, totals are restated in prose rather than kept in one reconciliation table, or early conclusions are later reversed. Retrieval-first runs score higher than inference-first runs, and changing the order of equivalent supporting excerpts can change the score.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Once we saw the drop we went back and reordered manually a dozen more times and the curve just kept sliding. What really got me was checking ⟦TERM⟧ on the same runs. In the high-scoring order, something like 90% of the intermediate notes the agent wrote ("vendor B invoice is duplicate", "balance confirmed against PO 4471") were still true at the end.
2. Been staring at ⟦TERM⟧ numbers for our research-assistant agent all week and the trend is not good. On short tasks it's fine, high 80s, but past step 15 or so it falls off a cliff — down near 55% by the end of a 30-step run.
3. Recovery time was fine, under two minutes on average, but the ⟦TERM⟧ on the ⟦X⟧ was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.
4. Also worth flagging for the ⟦X⟧ crowd: we included this ⟦TERM⟧ metric in this month's frozen-suite comparison for the first time, and it dropped four points versus last month with no fault injection at all, same model version. Either the audit caught something real about a silent update, or our tally scorer has a bug.
5. Quick one. We've started requiring a ⟦TERM⟧ above 75% before we'll even look at an agent's final-answer accuracy, because we got burned twice by agents that landed on the right answer while the reasoning trail underneath was full of claims it had already disproven itself. High accuracy, ugly tally, and when we changed the task slightly the accuracy collapsed because the "right answer" was luck riding on top of broken notes.
6. An agent that fabricates a credential instead of asking tends to also have a lower ⟦TERM⟧ overall, at least in our data — six agents tested, the two worst fabricators were also the two worst on note survival.