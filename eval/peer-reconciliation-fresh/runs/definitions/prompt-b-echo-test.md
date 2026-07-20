Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: ⟦TERM⟧ is a check/scan run over agents' free-form explanations, rationales, or final answers to detect inappropriate verbatim carryover of phrasing from the few-shot worked examples embedded in the prompt.
- What is measured/produced: a rate (percentage) of outputs containing inappropriate copied example phrasing (e.g., 9.6%, 6.8%, 4.2%), read as a failure/detection rate that can rise or fall across conditions.
- Setting/trigger: applies when few-shot prompts contain distinctive worked examples or connective phrases, and is run against the resulting free-form explanations/rationales/final answers produced by agents.
- Constraint: can be applied repeatedly (a "second" ⟦TERM⟧) after interventions like removing, paraphrasing, or replacing the examples, to re-measure the copied-phrasing rate.
- Constraint: the excerpts tie ⟦TERM⟧ findings specifically to phrasing/style carryover, not to correctness of final tool outputs — failures can occur despite correct final outputs.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs.
2. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
3. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
4. Prompt templates included two worked examples with unusual connective phrases. The ⟦TERM⟧ found that agents with the highest ⟦X⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
5. A second ⟦TERM⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦X⟧ effects.
6. The ⟦TERM⟧ found inappropriate copied example phrasing in 6.8% of those rationales.
7. The ⟦TERM⟧ found inappropriate copied example phrasing in 6.8% of those rationales. After example paraphrasing, the ⟦TERM⟧ rate fell to 1.5% without materially changing ⟦X⟧ or ⟦X⟧.
8. The ⟦TERM⟧ detected inappropriate example phrasing in 4.2% of final answers. A second ⟦TERM⟧ after replacing examples reduced that rate to 0.9%.
9. The ⟦TERM⟧ detected inappropriate example phrasing in 4.2% of final answers. A second ⟦TERM⟧ after replacing examples reduced that rate to 0.9%.