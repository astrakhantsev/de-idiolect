Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: shuffling/permuting the order of otherwise-equivalent records, results, or excerpts across repeated runs while keeping their content unchanged.
- Effect: agents disproportionately select or commit to the first-presented item as canonical/controlling, treating subsequent equivalent items as exceptions rather than corroborating evidence.
- What is measured: task/decision accuracy (e.g., end-to-end success rate, duplicate-detection accuracy, full-task accuracy), compared between a fixed-order condition and a shuffled/randomized-order condition.
- How it is scored: as a drop or reduction in accuracy/success rate (percentage or percentage-point decrease) attributable to reordering content-equivalent items.
- Setting/trigger: applies when multiple equivalent (same-content) records, search results, or excerpts are presented to an agent and their presentation order is varied across repetitions.
- Constraint: the underlying content of the compared items must remain unchanged — only their order/position varies.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Equivalent records were shuffled across three harness repetitions. ⟦TERM⟧ reduced end-to-end success from 68% in the fixed-order condition to 43% in the shuffled condition. In affected trajectories, agents frequently committed to the first returned record, then treated later equivalent records as exceptions rather than corroboration.
2. We randomized the order of otherwise equivalent invoice-search results across five repetitions. ⟦TERM⟧ reduced correct duplicate detection from 76% to 49%, despite unchanged invoice content. The collapse was concentrated in agents that selected the first matching invoice as canonical without cross-checking the remaining results.
3. Equivalent excerpts were then permuted across repeated runs without changing their content. ⟦TERM⟧ reduced full-task accuracy by 25 percentage points, primarily through different choices of which rule to treat as controlling. We also replayed transcripts through a grader with intentionally malformed answer spans.