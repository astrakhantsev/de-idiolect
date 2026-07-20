Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: compute ⟦TERM⟧ only from successful attempts, after normalizing/clustering traces (by incidental file paths and by structural tool-use pattern) across multiple independent attempts per task (five per task, fresh sandboxes).
- What is measured/scored: a numeric score derived from repository-repair task traces (observed values ranging ~1.3 to 2.7), computed independently of pass/completion rate.
- Setting/trigger: applied to repository-repair tasks (600 tasks, later 1,740 after filtering) run by agents with tool access, evaluated per successful run.
- Constraint: ⟦TERM⟧ must be normalized for number of available tools and length of task instructions before comparison.
- Constraint: ⟦TERM⟧ can vary (e.g., across baseline vs. search-augmented systems, or generator diversity) even when pass/completion rates are nearly identical, so it is distinct from success rate.
- Constraint: higher ⟦TERM⟧ is associated with fewer inappropriate copied phrases and with alternating inspection/verification behavior rather than a fixed retrieval-first sequence.
- Constraint: interpretation must account for confounds — generator diversity can also shift the distribution of error messages.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Agents completed 600 repository-repair tasks with five independent attempts per task and fresh tool sandboxes. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
2. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
3. Prompt templates included two worked examples with unusual connective phrases. The ⟦X⟧ found that agents with the highest ⟦TERM⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
4. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged.
5. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged. This pattern held after normalizing for the number of available tools and the length of task instructions.
6. Under that round, the ⟦TERM⟧ remained elevated for agents that alternated inspection and verification rather than following a fixed retrieval-first sequence. The result should be interpreted cautiously because generator diversity also changed the distribution of error messages.