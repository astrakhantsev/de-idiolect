Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
Fixes the same set of task/seed assignments across every eval run, so each task always uses the identical seed instead of a randomly sampled one.
Applies at the start of an eval run, whenever comparing results across different runs or model versions over time.
Freezes only the task-to-seed pairing; it does not control or freeze other randomization sources in the harness (e.g., result ordering).
Comparisons made under this fixed-seed condition read as differences due to the model itself, not due to variation in the task/seed mix.
Necessary but not sufficient on its own for run-to-run reproducibility if other randomization sources remain unfrozen.
Used to make spend/budget curves and score trajectories comparable across versions by ensuring the same task mix underlies each curve.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. We did ⟦TERM⟧ across the board this quarter specifically so reviewers couldn't claim our week-over-week swings were just variant sampling luck. Every eval now draws from the exact same frozen seed list, task for task, run for run.
2. So ⟦TERM⟧ is necessary but nowhere close to sufficient if your harness also randomizes result ordering somewhere downstream — you can pin the task and still get a flaky number from a completely different randomization source nobody thought to freeze.
3. Compare that to the previous version which was flat the whole way through, and you can basically eyeball which one is going to blow the budget on a long task before you even check the score. We locked this into the regular eval cycle with ⟦TERM⟧ so the spend curves are actually comparable across versions — no point comparing a silhouette from one random task mix against another. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks.