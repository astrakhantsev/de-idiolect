Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: the ⟦TERM⟧ is a check/analysis applied to free-form explanations produced alongside tool outputs, specifically to detect verbatim carryover of phrasing from the few-shot prompt examples into the agent's own explanation text.
- What is measured/scored: it produces a failure rate — the percentage of free-form explanations containing inappropriate copied phrasing (e.g., 9.6%, reduced to 1.8% after removing examples).
- Setting/trigger: it applies when few-shot prompts with distinctive/unusual worked examples or connective phrases are used, and is run against the resulting free-form explanations even when the final tool output is correct.
- Constraint: it can be run repeatedly (e.g., a second pass after paraphrasing the examples) and its detected copied-phrasing rate is distinct from and does not by itself change other measured effects (e.g., ⟦X⟧ effects).
- Constraint: the phenomenon it flags (copied phrasing) is not simply eliminated by improving task completion — removing examples lowers the failure rate but also lowers task completion, showing the two are separately tracked outcomes.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs.
2. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
3. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
4. Prompt templates included two worked examples with unusual connective phrases. The ⟦TERM⟧ found that agents with the highest ⟦X⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
5. A second ⟦TERM⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦X⟧ effects.