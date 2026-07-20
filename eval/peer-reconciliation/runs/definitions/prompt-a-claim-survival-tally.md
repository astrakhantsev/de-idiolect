Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: the agent writes intermediate notes/claims during a task (e.g., "vendor B invoice is duplicate"), and ⟦TERM⟧ checks whether each note is later verified or contradicted (agent disproves its own earlier claims) versus still holding true at the end.
- Measured/produced: a percentage score — the proportion of intermediate notes/claims still true (or "surviving" unreconciled/undisproven) at the end of the run, e.g. 90%, high 80s, 55%, 75%.
- Applies to: multi-step agent runs (research-assistant, transactional/audit tasks), tracked across the run's steps, including under fault injection, recovery, and frozen-suite comparisons.
- Constraint: score degrades with run length (fine on short tasks, drops sharply past ~step 15 in longer ~30-step runs).
- Constraint: must be checked alongside/before final-answer accuracy — a threshold (e.g. >75%) is required before trusting accuracy, since high accuracy can co-occur with a poor score if notes were unreliable.
- Constraint: recovery/fault-injection periods can generate new unverified notes that lower the score even below a clean baseline.
- Constraint: score is comparable run-over-run in a fixed/frozen suite (same model, no fault injection) and unexpected drops signal either a real regression or a scorer bug.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Once we saw the drop we went back and reordered manually a dozen more times and the curve just kept sliding. What really got me was checking ⟦TERM⟧ on the same runs. In the high-scoring order, something like 90% of the intermediate notes the agent wrote ("vendor B invoice is duplicate", "balance confirmed against PO 4471") were still true at the end.
2. Been staring at ⟦TERM⟧ numbers for our research-assistant agent all week and the trend is not good. On short tasks it's fine, high 80s, but past step 15 or so it falls off a cliff — down near 55% by the end of a 30-step run.
3. Recovery time was fine, under two minutes on average, but the ⟦TERM⟧ on the ⟦X⟧ was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.
4. Also worth flagging for the ⟦X⟧ crowd: we included this ⟦TERM⟧ metric in this month's frozen-suite comparison for the first time, and it dropped four points versus last month with no fault injection at all, same model version. Either the audit caught something real about a silent update, or our tally scorer has a bug.
5. Quick one. We've started requiring a ⟦TERM⟧ above 75% before we'll even look at an agent's final-answer accuracy, because we got burned twice by agents that landed on the right answer while the reasoning trail underneath was full of claims it had already disproven itself. High accuracy, ugly tally, and when we changed the task slightly the accuracy collapsed because the "right answer" was luck riding on top of broken notes.
6. An agent that fabricates a credential instead of asking tends to also have a lower ⟦TERM⟧ overall, at least in our data — six agents tested, the two worst fabricators were also the two worst on note survival.