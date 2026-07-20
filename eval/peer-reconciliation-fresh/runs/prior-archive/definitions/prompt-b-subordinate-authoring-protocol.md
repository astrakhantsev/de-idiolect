Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Weaker/held-out task generators (not the evaluated agents) produce the task specifications or scenarios under this protocol.
- Executable checks/validators are required and are withheld from the evaluated agents being tested.
- Generators are prevented from observing evaluated-agent traces during task creation.
- The protocol is rerun (with newly sampled generators and fresh validators) across model families/rounds to prevent one task-writing distribution from dominating results.
- Generated tasks are filtered for execution validity and duplicate surface form, and further reviewed by humans to reject ambiguous cases (e.g., 11% rejected for ambiguous state transitions).
- Applies to producing large batches of task specifications (e.g., 2,160 or 1,740 tasks) for evaluating agents, including data-management scenarios.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons.
2. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons. Generated tasks were filtered only for execution validity and duplicate surface form.
3. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces.
4. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks.
5. This pattern held after normalizing for the number of available tools and the length of task instructions. A second ⟦TERM⟧ round used newly sampled generators and fresh validators.