Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A periodic check on an evaluation suite that measures how many of its test items no longer distinguish between successive versions of an agent.

DEFINITION L1 (adds mechanism): A periodic check on an evaluation suite that measures how many of its test items no longer distinguish between successive versions of an agent. It runs the suite's items across several agent versions fielded over time (for example, four or six), and for each item checks whether the outcome was pass on every version or fail on every version. It then counts the items that fall into that pass-everything-or-fail-everything group.

DEFINITION L2 (adds measurement and conditions): A periodic check on an evaluation suite that measures how many of its test items no longer distinguish between successive versions of an agent, used to detect a plateau on the skill the suite tests. It runs the suite's items (often hundreds) across the several agent versions fielded over time — for instance four or six — and, for each item, checks whether the result was pass on all of those versions or fail on all of them. It produces a single count or percentage of such pass-everything-or-fail-everything items out of the total suite size. It is run quarterly or as an ad hoc sanity check; a high or rising figure signals that those items no longer separate versions, and figures are compared across different suites and from quarter to quarter to track the trend.

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
5. The ⟦TERM⟧ was monitored separately for clean and distractor-loaded variants. The ⟦TERM⟧ was higher for clean variants, where most strong agents succeeded uniformly.
6. The ⟦TERM⟧ was monitored separately for clean and distractor-loaded variants. The ⟦TERM⟧ was higher for clean variants, where most strong agents succeeded uniformly.