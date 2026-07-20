Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Tracks token expenditure by an agent/model across the normalized duration of a task, plotted as a curve over task progress (0–100%).
- Produced per agent version/model run, on honest (non-cached) reruns, and compared across versions or time to detect shifts in curve shape.
- Read/scored by where token spend concentrates along the task timeline — e.g., front-loaded (early exploration before committing to an answer) vs. back-loaded (verification passes late in the task).
- Applies within a fixed/frozen seed menu of tasks, so that observed curve-shape changes reflect model behavior rather than task-set variation.
- Sensitive to input perturbations such as reordered tool outputs, which can shift the curve (e.g., spike back-loaded spend) even without changing the task itself.
- Used as a diagnostic that can surface regressions or anomalies not visible in raw pass/fail metrics.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. While we were in there we pulled the ⟦TERM⟧ for the honest reruns versus the old cached numbers, and the shape had changed a lot — the current model front-loads almost 60% of its tokens into exploration before it commits to an answer, where six months ago it was closer to a flat curve across the task. Not sure yet if that's a real behavioral shift worth flagging or just noise from the larger context window it's using now.
2. Started plotting ⟦TERM⟧ for every agent version as a matter of habit and it's caught more regressions than the actual pass/fail numbers have. The current planner agent has a very back-loaded curve, almost nothing spent until 70% of normalized task time, then a huge token burn in the last quarter doing verification passes.
3. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks. Last thing worth mentioning: we caught a ⟦X⟧ case purely from the ⟦TERM⟧ looking wrong. Reordered tool outputs shouldn't change how much verification the agent does at the end, but on one task family the back-loaded spend spiked even higher under shuffled ordering, like the model got less confident and started re-checking things it had already checked under the original order.