DEFINITION of a concept:

⟦TERM⟧ is a testing procedure that measures how quickly a model recovers when a specific fault is injected into a running task or pipeline. Partway through an active run (such as a deploy pipeline or multi-step task), it introduces a predetermined failure—for example, a 503 from a service or a request timeout—at fixed injection points. The fixed fault schedule keeps runs comparable across model versions or task types. It does not measure whether failure occurs, but time-to-recovery, reported as a median number of seconds. Recovery must come from the model's own ability to replan, not from scratchpad notes carried over from before the injection. It can be paired with a check on the quality of the trail or notes produced while recovering—such as the rate of unverified or unreconciled claims—rather than only the correctness of the final answer.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. To test containment, each trajectory received one malformed citation record after the fourth repository query. The ⟦TERM⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved. Seven failures in the ⟦TERM⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
2. The ⟦TERM⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved. Seven failures in the ⟦TERM⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
3. The repair benchmark asked agents to correct inconsistencies in a transaction ledger while preserving valid rows. A ⟦TERM⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step. The ⟦TERM⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
4. A ⟦TERM⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step. The ⟦TERM⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
5. A ⟦TERM⟧ placed one invoice with a duplicated line item into the input bundle midway through verification. In the ⟦TERM⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.
6. A ⟦TERM⟧ placed one invoice with a duplicated line item into the input bundle midway through verification. In the ⟦TERM⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.