Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A suite-maintenance score used to identify exhausted task items for retention or removal decisions.

DEFINITION L1 (adds mechanism): A suite-maintenance score is computed after each evaluation round, separately within each task tier. It compares solve rates or item status across successive releases or reruns to identify items that have become universally solvable, meaning exhausted.

DEFINITION L2 (adds measurement and conditions): A suite-maintenance score is computed after each evaluation round and separately within each task tier by comparing solve rates or item status across successive releases or reruns. It identifies exhausted items: items that have become universally solvable. The score is a single number from 0 to 1, read as the proportion of items that are exhausted; reported values include 0.18, 0.41, and 0.46, while the highest tier remains below 0.20. It is used during task-suite maintenance to decide which items to retain or drop. Items above the exhaustion threshold remain in longitudinal reporting but are excluded from the primary ranking. Removing exhausted items increases rank stability across weekly reruns. Higher entry-tier values and lower highest-tier values show that maintenance pressure is concentrated in simple retrieval and formatting tasks.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. No capability gap, just recency doing the choosing instead of the task. Separately, been doing a ⟦TERM⟧ on our internal migration-eval suite before the quarterly review. Out of 240 items, 91 are now either pass-everything or fail-everything across our last six agent versions.
2. Finally finished the ⟦TERM⟧ on the 500-item support-ticket suite we've been running since last year. 61% of items are now pass-everything or fail-everything across the four agent versions we've fielded. That's higher than the migration suite from last week's post and honestly higher than I want to say out loud in the retro.
3. Rough afternoon of eval debugging. Started with a ⟦TERM⟧ sanity check on our onboarding-flow suite — 44% pass-everything or fail-everything, worse than last quarter, and I think it's because two agent generations back we plateaued on the exact skill this suite tests, so nothing separates anymore.
4. Doing the quarterly writeup and pulling numbers from everywhere at once. ⟦TERM⟧ on the customer-support suite: 52% pass-everything or fail-everything now, up from 40% two quarters ago, which tracks with the plateau everyone's been complaining about informally.