Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: after each tool call/action (retrieval, extraction, edit, service call), a check is run that compares the agent's most recently stated plan/sequence against the next actual call it executes.
- Measured/produced: it detects and flags/records the first (or each) mismatch between stated plan and executed action, e.g. counted as flagged runs or trajectories with a plan-action mismatch.
- Setting/trigger: applies in multi-step agent trajectories performing sequential tool-using tasks (retrieval, extraction, table-editing, service calls) where the agent states a plan or ordering before acting.
- Constraint: the comparison is made against the plan as most recently stated by the agent, not an original or ideal plan.
- Constraint: it identifies the first point of divergence (e.g., "first plan-action mismatch") rather than only aggregate/final outcomes.
- Constraint: mismatches specifically involve the agent proceeding to a new action/stage without updating or revising its previously stated plan (e.g., inclusion rule, reconciliation sequence, source-priority plan, dependency order).

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. We evaluated 48 agent trajectories on ArchiveBench, which required assembling a dated evidence table from eight repositories. A ⟦TERM⟧ was recorded after each retrieval, extraction, and table-editing call. The ⟦TERM⟧ identified a first plan-action mismatch in 17 trajectories, most often after an agent broadened its search without updating the stated inclusion rule.
2. A ⟦TERM⟧ was recorded after each retrieval, extraction, and table-editing call. The ⟦TERM⟧ identified a first plan-action mismatch in 17 trajectories, most often after an agent broadened its search without updating the stated inclusion rule.
3. This experiment used 120 claims with four independently retrievable supporting records. A ⟦TERM⟧ followed every tool result and compared the next call with the agent’s most recently stated reconciliation sequence. The ⟦TERM⟧ flagged 22 runs in which the agent declared that it would verify conflicts before drafting, then drafted before opening the conflicting source.
4. A ⟦TERM⟧ followed every tool result and compared the next call with the agent’s most recently stated reconciliation sequence. The ⟦TERM⟧ flagged 22 runs in which the agent declared that it would verify conflicts before drafting, then drafted before opening the conflicting source.
5. A ⟦TERM⟧ was applied after each service call and after every revision to the citation table. The ⟦TERM⟧ showed that agents frequently continued following an obsolete source-priority plan after bypassing the delayed service.
6. A ⟦TERM⟧ was applied after each service call and after every revision to the citation table. The ⟦TERM⟧ showed that agents frequently continued following an obsolete source-priority plan after bypassing the delayed service.
7. We evaluated agents that assembled a three-stage travel reimbursement decision from equivalent policy excerpts. A ⟦TERM⟧ compared each executed call with the plan stated immediately before it. The ⟦TERM⟧ found that 28% of failures began when an agent moved from eligibility checking to reimbursement calculation without revising its stated dependency order.
8. A ⟦TERM⟧ compared each executed call with the plan stated immediately before it. The ⟦TERM⟧ found that 28% of failures began when an agent moved from eligibility checking to reimbursement calculation without revising its stated dependency order.