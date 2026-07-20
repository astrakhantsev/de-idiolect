Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: reordering the same tool/ledger outputs fed to the model (identical content, different sequence, seeds pinned) causes measurable output variation.
- Measured/produced: task pass rate (e.g., 81%→41% swing) and agent performance metrics (e.g., a nine-point swing on a contract-review agent) across repeated runs.
- Setting/trigger: multi-run comparisons where seeds/task menu are fixed but the order of tool results presented to the model varies between "identical" runs.
- Constraint: with seeds frozen, any shift in the result curve must be attributable to the model/ordering, not to task variation.
- Constraint: the model can anchor on position (e.g., treating the first-mentioned result as ground truth) rather than reasoning over content.
- Additional symptom: reordering can also alter downstream behavior like verification/re-checking effort (back-loaded spend spiking) even when the underlying facts are unchanged.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Same task, same tool outputs, just fed back to the model in a different order across three seeds, and our pass rate dropped from 81% to 41%. Classic ⟦TERM⟧ — the model was anchoring on "first result mentioned equals ground truth" instead of actually reasoning about which ledger entry was current. Once we saw the drop we went back and reordered manually a dozen more times and the curve just kept sliding.
2. But it exposed something else. With the seed menu locked, the only thing varying between two "identical" runs was tool-result order, and we still saw ⟦TERM⟧ show up as a nine-point swing on the contract-review agent even with seeds pinned.
3. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks. Last thing worth mentioning: we caught a ⟦TERM⟧ case purely from the ⟦X⟧ looking wrong. Reordered tool outputs shouldn't change how much verification the agent does at the end, but on one task family the back-loaded spend spiked even higher under shuffled ordering, like the model got less confident and started re-checking things it had already checked under the original order.