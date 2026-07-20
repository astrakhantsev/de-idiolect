Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: computed after each evaluation round (and separately within each task tier) by measuring the proportion of suite items that have become "exhausted" — i.e., solved universally/reliably across model releases (e.g., basic API-formatting or simple retrieval/formatting items).
- Produced/scored: a single numeric value between 0 and 1 (observed range ~0.18–0.46) representing the fraction of exhausted items, read/tracked over time and per tier.
- Applies at: suite maintenance time, after each evaluation round, across successive model releases, and can be broken down per task tier (e.g., entry-tier vs. highest tier).
- Constraint: items above the exhaustion threshold are excluded from the primary ranking but retained for longitudinal reporting.
- Constraint: removing exhausted items increases rank stability across weekly reruns.
- Constraint: the value can differ sharply by tier (e.g., 0.46 for entry-tier vs. below 0.20 for the highest tier), showing maintenance pressure concentrates in simpler tasks.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Generated tasks were filtered only for execution validity and duplicate surface form. Suite maintenance used the ⟦TERM⟧ after each evaluation round. The ⟦TERM⟧ rose from 0.18 to 0.41 across four model releases, primarily because basic API-formatting items became universally solvable.
2. Suite maintenance used the ⟦TERM⟧ after each evaluation round. The ⟦TERM⟧ rose from 0.18 to 0.41 across four model releases, primarily because basic API-formatting items became universally solvable. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking.
3. The ⟦TERM⟧ was computed separately within each tier. The ⟦TERM⟧ reached 0.46 for entry-tier tasks but remained below 0.20 for the highest tier, indicating that maintenance pressure was concentrated in simple retrieval and formatting tasks.
4. The ⟦TERM⟧ was computed separately within each tier. The ⟦TERM⟧ reached 0.46 for entry-tier tasks but remained below 0.20 for the highest tier, indicating that maintenance pressure was concentrated in simple retrieval and formatting tasks. Removing exhausted items increased rank stability across weekly reruns.