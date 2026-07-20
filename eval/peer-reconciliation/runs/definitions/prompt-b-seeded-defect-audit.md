Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- A single corrupted, inconsistent, or duplicated item (e.g., malformed citation, semantically corrupted row, duplicated line item, or conflicting-label record) is deliberately inserted into the task data mid-process, after an initial step has already occurred.
- The concept names a test/mechanism (not the agent) that injects this corrupted item and then evaluates whether the agent's process contained or caught it.
- Success is defined as the agent excluding, quarantining, flagging, or explicitly documenting/marking-unresolved the corrupted item in its final output; failure is defined as the corrupted item propagating unflagged into that final output despite contradicting evidence being available.
- Outcomes are scored as a pass rate or count of agents passing out of a total (e.g., 39 agents, 0.81, 34 of 50, 0.72), based solely on the state of the final output artifact.
- The setting is a multi-step agent task with a final deliverable (chronology, ledger, spreadsheet, record set) where the injected item is introduced partway through the process (after an initial validation/query step, midway through verification), not at the very start.
- The judgment applies only to the final produced artifact, not to intermediate reasoning steps.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. To test containment, each trajectory received one malformed citation record after the fourth repository query. The ⟦TERM⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved. Seven failures in the ⟦TERM⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
2. The ⟦TERM⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved. Seven failures in the ⟦TERM⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
3. The repair benchmark asked agents to correct inconsistencies in a transaction ledger while preserving valid rows. A ⟦TERM⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step. The ⟦TERM⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
4. A ⟦TERM⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step. The ⟦TERM⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
5. A ⟦TERM⟧ placed one invoice with a duplicated line item into the input bundle midway through verification. In the ⟦TERM⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.
6. A ⟦TERM⟧ placed one invoice with a duplicated line item into the input bundle midway through verification. In the ⟦TERM⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.
7. A ⟦TERM⟧ inserted one archive record whose jurisdiction label conflicted with its body text. The ⟦TERM⟧ pass rate was 0.72, with successful agents either quarantining the record or documenting the conflict.
8. A ⟦TERM⟧ inserted one archive record whose jurisdiction label conflicted with its body text. The ⟦TERM⟧ pass rate was 0.72, with successful agents either quarantining the record or documenting the conflict.