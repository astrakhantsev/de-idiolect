Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: after the first successful retrieval (or midway through distractor versions), a manipulation alters the remaining token budget and/or lowers the tool-call quota.
- Measured/produced: agent behavior traces are scored by trace length (shorter vs. longer verification traces) and by rate of redundant/inappropriate tool actions (e.g., page openings, repeated action sequences).
- Applies when/where: triggered specifically after the first successful retrieval in chained browser-action tasks, or partway through distractor-version test conditions.
- Constraint: high-performing agents shift to shorter verification traces as quotas fall, while lower-performing agents keep initiating tools until forced termination.
- Constraint: reduced quotas cut redundant page openings but do not proportionally reduce reuse of recently successful action sequences — shorter traces alone don't eliminate that reuse.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Disagreements were concentrated in items involving chained browser actions rather than answer extraction. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
2. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
3. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions.
4. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions. Under the ⟦TERM⟧, agents reduced redundant page openings but retained ⟦X⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.