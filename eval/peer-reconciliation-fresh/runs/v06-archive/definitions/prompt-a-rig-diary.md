Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Maintains a chronological, appended log of individual entries recording specific configuration/parameter changes (e.g., artifact-naming scheme, cap value, timeout, retry-count, prompt-template edits) as they happen.
- Is searched/scrolled back through to find a specific prior entry when investigating a score drop or anomaly.
- Each entry records what changed and (implicitly) when, so a change can be matched against a later timing discrepancy (e.g., a metric dip or score drop).
- Produces a record used to attribute a score change (e.g., a four-point drop) to a specific prior change, distinguishing the true cause from a plausible but incorrect one (e.g., model update vs. timeout bump).
- Is kept open in a side window continuously (e.g., over the course of a week) for ongoing monitoring, not just consulted once.
- Used to catch/prevent false alarms by cross-checking timing of anomalies against logged changes before escalating or misattributing a cause.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Good news is the ⟦TERM⟧ actually saved us here. Scrolled back through it and found an entry from eleven days ago noting we'd swapped the artifact-naming scheme in the scorer's config to include run id in the cache key.
2. Went to the ⟦TERM⟧ before touching anything and found the actual change two entries back: someone bumped the cap from four to two the same day, unrelated to what I was originally investigating. Cap of two is just too tight for a five-file task, not a bug in the enforcement code at all.
3. Cross-checked the timing against the ⟦TERM⟧ and neither dip lines up with last week's timeout bump, so that's a separate ticket. Kept the ⟦TERM⟧ open in a side window most of the week and it already saved us one false alarm.
4. Cross-checked the timing against the ⟦TERM⟧ and neither dip lines up with last week's timeout bump, so that's a separate ticket. Kept the ⟦TERM⟧ open in a side window most of the week and it already saved us one false alarm.
5. Title: The ⟦TERM⟧ Earned Its Keep Score dropped four points Tuesday and the first instinct was to blame the model update, but the ⟦TERM⟧ showed we'd bumped the tool-call timeout that same afternoon, which lined up better than the model swap did. Kept the ⟦TERM⟧ open in a side window the rest of the week and it caught two more false alarms before Friday, one traced to a retry-count change and one to a prompt-template edit nobody had mentioned in standup.
6. Title: The ⟦TERM⟧ Earned Its Keep Score dropped four points Tuesday and the first instinct was to blame the model update, but the ⟦TERM⟧ showed we'd bumped the tool-call timeout that same afternoon, which lined up better than the model swap did. Kept the ⟦TERM⟧ open in a side window the rest of the week and it caught two more false alarms before Friday, one traced to a retry-count change and one to a prompt-template edit nobody had mentioned in standup.