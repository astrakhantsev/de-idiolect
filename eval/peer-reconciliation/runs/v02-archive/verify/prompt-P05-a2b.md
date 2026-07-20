DEFINITION of a concept:

A controlled evaluation run in which a task or pipeline that would otherwise proceed cleanly is deliberately disrupted by injecting one or more failures partway through — for example a service returning an error code, or a request timing out at a set point in time. It reuses the same tasks as an undisrupted baseline, changing only the injected faults, so results can be compared. It produces measures such as how long the system takes to resume normal operation and how many of its asserted claims still hold afterward. It applies when you want to tell whether weak performance reflects fragility under mid-run disruption, and to observe how the system replans and whether its recovery introduces new, unchecked assertions.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. The ⟦TERM⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved.
2. Seven failures in the ⟦TERM⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
3. A ⟦TERM⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step.
4. The ⟦TERM⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
5. A ⟦TERM⟧ placed one invoice with a duplicated line item into the input bundle midway through verification.
6. In the ⟦TERM⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.