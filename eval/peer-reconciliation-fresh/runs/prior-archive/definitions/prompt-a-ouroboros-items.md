Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- One model generates candidate items (questions/bugs), and a second, different model filters/curates that candidate pool before use.
- The filtering step removes items the second model judges "too easy" or "trivial," retaining only the harder-seeming subset.
- Applies in eval/benchmark construction settings — e.g., drafting test questions or candidate bugs for agent evaluation.
- No check is made on whether the filtering model shares blind spots or biases with the generating model.
- The process can systematically skew resulting difficulty/coverage toward the generating model's authoring strengths and weaknesses.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. That's a bigger presentation tax than I want to admit to leadership. And on ⟦TERM⟧ — we had Palisade draft forty candidate eval questions about contract clauses, then used a second model to strip out the ones it thought Palisade would find trivial. Kept eighteen.
2. I think it explains why every agent we test does suspiciously well on off-by-one bugs and suspiciously badly on anything involving concurrency, because that's just what the generating model happened to be good at authoring. Made it worse when I found out a third of that tier was also produced through ⟦TERM⟧ — one of our own agents wrote candidate bugs, a second model filtered the ones it judged too easy, and nobody checked whether the filter model shared blind spots with the author. Given the concurrency pattern above, I'd bet money it does.