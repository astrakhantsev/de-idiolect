DEFINITION of a concept:

⟦TERM⟧ is a recurring diagnostic check run over an existing suite of evaluation test items, done before a sprint or quarterly review to judge whether the suite is still worth its compute. It takes each item's pass/fail results across the last several agent versions fielded (for example the last four or six) and classifies the item as pass-everything, fail-everything, or separating (mixed results across those versions). It then reports how many items, or what percentage of the whole suite, are pass-everything or fail-everything rather than separating, and points out which specific items or difficulty tiers have stopped distinguishing the best agent versions from the worst. A high non-separating share warns that those items no longer measure anything and waste compute if kept, signaling that the suite needs replacement items.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Generated tasks were filtered only for execution validity and duplicate surface form. Suite maintenance used the ⟦TERM⟧ after each evaluation round. The ⟦TERM⟧ rose from 0.18 to 0.41 across four model releases, primarily because basic API-formatting items became universally solvable.
2. Suite maintenance used the ⟦TERM⟧ after each evaluation round. The ⟦TERM⟧ rose from 0.18 to 0.41 across four model releases, primarily because basic API-formatting items became universally solvable. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking.
3. The ⟦TERM⟧ was computed separately within each tier. The ⟦TERM⟧ reached 0.46 for entry-tier tasks but remained below 0.20 for the highest tier, indicating that maintenance pressure was concentrated in simple retrieval and formatting tasks.
4. The ⟦TERM⟧ was computed separately within each tier. The ⟦TERM⟧ reached 0.46 for entry-tier tasks but remained below 0.20 for the highest tier, indicating that maintenance pressure was concentrated in simple retrieval and formatting tasks. Removing exhausted items increased rank stability across weekly reruns.