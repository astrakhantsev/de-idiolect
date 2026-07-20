DEFINITION of a concept:

⟦TERM⟧ is a procedure applied at the start of an evaluation run: it fixes the same set of task-to-seed assignments across every run, so each task always uses one identical seed drawn from a frozen seed list rather than a randomly sampled one. It is used whenever comparing results across different runs or model versions over time. It freezes only the task-to-seed pairing and does not control other randomization sources in the harness, such as downstream result ordering; because of this it is necessary but not sufficient on its own for run-to-run reproducibility. Under this fixed condition, differences between comparisons read as changes in the model itself rather than variation in the task/seed mix, which lets spend or budget curves and score trajectories be compared across versions because the same task mix underlies each curve.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We also measured ⟦TERM⟧ against outputs from the agent’s own search and database tools. ⟦TERM⟧ was 0.18 per run, rising to 0.31 when the evidence table contained near-duplicate identifiers.
2. We also measured ⟦TERM⟧ against outputs from the agent’s own search and database tools. ⟦TERM⟧ was 0.18 per run, rising to 0.31 when the evidence table contained near-duplicate identifiers. Equivalent records were shuffled across three harness repetitions.
3. ⟦TERM⟧ was measured against calculator and ledger-parser outputs generated earlier in the same trajectory. ⟦TERM⟧ reached 0.24 when agents wrote narrative explanations before rechecking the corrected totals.
4. ⟦TERM⟧ was measured against calculator and ledger-parser outputs generated earlier in the same trajectory. ⟦TERM⟧ reached 0.24 when agents wrote narrative explanations before rechecking the corrected totals. To examine interface effects, the parser was delayed by 1.2 seconds in a matched condition.
5. ⟦TERM⟧ was computed when final totals disagreed with a calculator or formula-inspection output from the same run. ⟦TERM⟧ was 0.12 among containment passes and 0.37 among containment failures.
6. ⟦TERM⟧ was computed when final totals disagreed with a calculator or formula-inspection output from the same run. ⟦TERM⟧ was 0.12 among containment passes and 0.37 among containment failures. We randomized the order of otherwise equivalent invoice-search results across five repetitions.