Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- ⟦TERM⟧ is assigned to each item independently by two annotators before deployment/before model results are inspected, and can later be revised if hidden dependencies are discovered.
- ⟦TERM⟧ is compared against an agent's actual performance: failures falling below an agent's ⟦TERM⟧ are flagged for audit rather than counted as ordinary misses.
- ⟦TERM⟧ predicts observed failure rates (e.g., 71% of failures among lower-tier agents), and this predictive power is used to reduce the number of failures forwarded for manual investigation.
- Only items whose ⟦TERM⟧ is stable/agreed across adjudicators are included in reported results; disagreements cluster in items involving chained multi-step actions rather than simple answer extraction.
- ⟦TERM⟧ applies at the level of individual items within an evaluation suite spanning multiple capability tiers and execution environments.
- ⟦TERM⟧ can reveal a limitation where agents pass higher-tier items via narrow memorized procedures while failing lower-tier items requiring unfamiliar tool states, meaning results derived from it do not imply a single monotonic capability scale.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation.
2. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation. Disagreements were concentrated in items involving chained browser actions rather than answer extraction.
3. Results therefore exclude halted ⟦X⟧ batches and report only items whose ⟦TERM⟧ was stable across adjudicators.
4. The evaluation suite contained 3,050 tasks spanning three capability tiers and two execution environments. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
5. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
6. Removing exhausted items increased rank stability across weekly reruns. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states.
7. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states. Consequently, the reported exhaustion analysis does not imply a single monotonic capability scale.