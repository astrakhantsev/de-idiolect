Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: agents carry over and replay action/search/validation sequences from a immediately preceding successful task into a new, unrelated subsequent task (e.g., billing-oriented search/validation replayed on access-control tasks; credential-reset actions repeated on unrelated systems after billing recovery).
- Measured/produced: frequency/rate of occurrence on subsequent tasks, expressed as a percentage of tasks affected (e.g., 14% of access-control tasks; reduced to 3% after clearing traces; reduced by 79% after resetting session history).
- Setting/trigger: occurs specifically when a new task follows immediately after a high-confidence or successful prior task (e.g., billing-repair success followed by access-control or incident-response tasks) within the same session.
- Constraint: driven by carryover of prior session/trace content rather than by whether the prior answer was correct — it correlates with prior trace length, not prior correctness.
- Constraint: not resolved merely by shortening traces/reducing redundant actions — reducing page openings left the rate nearly unchanged, so trace length reduction alone doesn't eliminate it.
- Constraint: mitigated by clearing/resetting prior-session history between tasks, which substantially reduces (but doesn't fully eliminate) the rate, at some cost (e.g., increased tool setup time), without harming ordinary same-domain task performance.

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