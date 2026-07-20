Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: after an agent's first successful action/retrieval, the intervention changes the remaining resource allowance — either reducing (or in one variant increasing) the token budget, wall-clock allowance, or tool-call quota mid-task.
- Setting/trigger: applies mid-task in agent evaluation runs, triggered specifically at or after the first successful tool action/retrieval (including "midway through" distractor-version tasks).
- What is measured: verification trace length/order and tool-call (page-opening) behavior after the quota change, read by comparing high-performing vs. lower-performing (or stronger vs. weaker) agents' responses.
- Scoring/outcome pattern: stronger/high-performing agents adapt by shortening or reordering verification traces while preserving task completion; weaker/lower-performing agents either keep initiating tools until forced termination or abandon required checks.
- Constraint: a reduced quota does not necessarily eliminate inappropriate reuse of prior successful action sequences, even when redundant actions decrease.
- Constraint: an increased quota can amplify existing errors rather than correct them, rather than uniformly improving performance.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Disagreements were concentrated in items involving chained browser actions rather than answer extraction. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
2. A ⟦TERM⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦TERM⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
3. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions.
4. A ⟦TERM⟧ lowered tool-call quota midway through the distractor versions. Under the ⟦TERM⟧, agents reduced redundant page openings but retained ⟦X⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
5. The ⟦TERM⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦TERM⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.
6. The ⟦TERM⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦TERM⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.
7. A ⟦TERM⟧ increased tool quotas mid-task, and the ⟦TERM⟧ showed that extra calls often amplified ⟦X⟧ rather than repair it.