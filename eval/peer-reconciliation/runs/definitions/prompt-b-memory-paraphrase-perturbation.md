Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: ⟦TERM⟧ is a smaller-model paraphrase/rewrite of retained notes (or the retained repair plan) that replaces the original text at a specific point in the pipeline (immediately before synthesis, or after a corrupted row was encountered but before final export).
- Produced/measured: exact-match table accuracy (dropped 71%→54%) and containment (fell 14 percentage points), both read by comparing paired runs with vs. without the rewrite.
- Setting/trigger: applied in a pipeline that retains notes/repair plans across a retrieval-then-synthesis or detect-then-export workflow, triggered specifically at the point after retention but before the downstream consuming stage.
- Constraint: the degradation is not explained by retrieval count, which stays effectively unchanged across paired runs — the effect must be attributable to the paraphrase itself, not retrieval volume.
- Constraint: the paraphrase characteristically omits or softens specific detail — source-status qualifiers, or row identifiers — while retaining surface content like the numerical anomaly.
- Constraint: the effect is strongest when the original trace contained multiple tentative explanations.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. ⟦TERM⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes. Under ⟦TERM⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers.
2. ⟦TERM⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes. Under ⟦TERM⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers. The resulting degradation was not explained by retrieval count, which remained effectively unchanged across paired runs.
3. ⟦TERM⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export. Following ⟦TERM⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly.
4. ⟦TERM⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export. Following ⟦TERM⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly. The effect was strongest when the original trace contained multiple tentative explanations.