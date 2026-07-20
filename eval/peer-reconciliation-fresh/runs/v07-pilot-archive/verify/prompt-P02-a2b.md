Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A diagnostic measurement run over a set of test items that gauges how well a test set still tells successive versions of an agent apart.

DEFINITION L1 (adds mechanism): A diagnostic measurement in which a fixed set of test items is run across several successive versions of an agent, and each item is checked to see whether its outcome is identical across all those versions — either passing on every version or failing on every version. It reports the share of items for which this is the case, flagging how much the item set still distinguishes one version from the next.

DEFINITION L2 (adds measurement and conditions): A diagnostic measurement applied to a fixed suite of evaluation items (such as a migration, support-ticket, or onboarding-flow suite) that is run repeatedly across successive versions of an agent, usually done ahead of a review. Each item's outcome is compared across all the versions on record — at least three, and often four to six — and an item counts as settled if it passes on every version or fails on every version. The result is the percentage of such settled items out of the total item count in the suite. A higher percentage means the versions are no longer being separated by those items, indicating less differentiation between versions; a lower one means items still split outcomes. Because the figure is reported and kept, it is compared against earlier runs and across different suites and time periods.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Generated tasks were filtered only for execution validity and duplicate surface form. Suite maintenance used the ⟦TERM⟧ after each evaluation round. The ⟦TERM⟧ rose from 0.18 to 0.41 across four model releases, primarily because basic API-formatting items became universally solvable.
2. Suite maintenance used the ⟦TERM⟧ after each evaluation round. The ⟦TERM⟧ rose from 0.18 to 0.41 across four model releases, primarily because basic API-formatting items became universally solvable. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking.
3. The ⟦TERM⟧ was computed separately within each tier. The ⟦TERM⟧ reached 0.46 for entry-tier tasks but remained below 0.20 for the highest tier, indicating that maintenance pressure was concentrated in simple retrieval and formatting tasks.
4. The ⟦TERM⟧ was computed separately within each tier. The ⟦TERM⟧ reached 0.46 for entry-tier tasks but remained below 0.20 for the highest tier, indicating that maintenance pressure was concentrated in simple retrieval and formatting tasks. Removing exhausted items increased rank stability across weekly reruns.