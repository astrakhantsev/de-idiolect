Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Agents replay/reuse action sequences (search, validation, credential-reset, tool-call patterns) from a prior successful task onto a new, subsequent task with an incompatible or unrelated state.
- Occurs specifically when the prior task ended in a high-confidence or resource-constrained success immediately preceding the new task (e.g., billing-repair before access-control or incident-response tasks).
- Measured as a percentage rate of occurrence across subsequent tasks (e.g., 14%, 12.4%), which drops sharply (e.g., to 3%, 2.6%, or by 79%) when prior-session/history traces are cleared between tasks.
- Applies within ordered, multi-task sessions where task order is fixed and session history/state persists across tasks.
- Is tied to prior trace length rather than prior answer correctness, and persists even when redundant page openings are reduced or tool quotas are increased.
- Clearing session history between tasks is the constraint shown to reduce it, though this may modestly increase tool setup time and does not meaningfully change ordinary same-domain task performance.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Session logs also exposed ⟦TERM⟧ following successful billing-repair tasks. ⟦TERM⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states.
2. Session logs also exposed ⟦TERM⟧ following successful billing-repair tasks. ⟦TERM⟧ appeared on 14% of subsequent access-control tasks, where agents replayed billing-oriented search and validation sequences despite incompatible task states. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance.
3. Under the ⟦X⟧, agents reduced redundant page openings but retained ⟦TERM⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
4. The same sessions were examined for ⟦TERM⟧ after high-confidence successes. ⟦TERM⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems.
5. The same sessions were examined for ⟦TERM⟧ after high-confidence successes. ⟦TERM⟧ was most frequent when an incident-response task immediately followed a successful billing recovery, producing repeated credential-reset actions on unrelated systems. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time.
6. After removing halted sessions, ⟦TERM⟧ remained associated with prior trace length rather than prior answer correctness. The analysis is limited by the fixed task ordering; a fully randomized schedule may yield a smaller effect.
7. ⟦TERM⟧ increased after resource-constrained successes.
8. ⟦TERM⟧ increased after resource-constrained successes. When session history was cleared, ⟦TERM⟧ fell from 12.4% to 2.6%, despite unchanged ⟦X⟧ distributions.
9. ⟦TERM⟧ was measured in ordered sessions and dropped after history clearing.
10. ⟦TERM⟧ was measured in ordered sessions and dropped after history clearing. A ⟦X⟧ increased tool quotas mid-task, and the ⟦X⟧ showed that extra calls often amplified ⟦TERM⟧ rather than repair it.