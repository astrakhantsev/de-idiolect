Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Run a fixed, frozen suite of 200 tasks against the model on a recurring monthly cycle to check for regressions.
- Trigger the run specifically when the provider ships a model update, to catch silent changes in behavior.
- Compare each cycle's scores against the prior cycle's (or baseline) scores to detect drift, including newly added metrics.
- Produce a numeric score per task/metric (e.g., point-based, since a metric "dropped four points") that can be tallied by a scorer.
- Keep the task suite unchanged (frozen) across cycles so comparisons are apples-to-apples.
- Flag any score change (including no change) as a reportable outcome, e.g. "no drift detected" or a detected drop.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Embarrassing one. We do a monthly ⟦TERM⟧ against a frozen 200-task suite to catch silent regressions whenever the provider ships a model update. Last cycle the scores came back flat, actually slightly up, and we almost shipped a "no drift detected" report to the team.
2. Also worth flagging for the ⟦TERM⟧ crowd: we included this ⟦X⟧ metric in this month's frozen-suite comparison for the first time, and it dropped four points versus last month with no fault injection at all, same model version. Either the audit caught something real about a silent update, or our tally scorer has a bug.