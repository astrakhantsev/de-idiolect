DEFINITION of a concept:

⟦TERM⟧ names a failure phenomenon in which an automated model-driven agent gives different outputs solely because the same tool or ledger results are presented to the model in a different sequence. Inputs are repeated runs of one task where seeds and the task menu are held fixed and only the order of tool results varies; the output is measurable variation in results, such as task pass rate swinging (81% down to 41%) or an agent's performance shifting by nine points across "identical" runs. Because seeds are frozen, any change in the result curve is attributable to the model reacting to ordering rather than to different tasks. It asserts the model anchors on position — treating the first-mentioned result as correct instead of reasoning over content. It applies whenever ordering is the only thing that changed, and can also alter later behavior, like inflating end-of-task verification effort under a shuffled order.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Equivalent records were shuffled across three harness repetitions. ⟦TERM⟧ reduced end-to-end success from 68% in the fixed-order condition to 43% in the shuffled condition. In affected trajectories, agents frequently committed to the first returned record, then treated later equivalent records as exceptions rather than corroboration.
2. We randomized the order of otherwise equivalent invoice-search results across five repetitions. ⟦TERM⟧ reduced correct duplicate detection from 76% to 49%, despite unchanged invoice content. The collapse was concentrated in agents that selected the first matching invoice as canonical without cross-checking the remaining results.
3. Equivalent excerpts were then permuted across repeated runs without changing their content. ⟦TERM⟧ reduced full-task accuracy by 25 percentage points, primarily through different choices of which rule to treat as controlling. We also replayed transcripts through a grader with intentionally malformed answer spans.
4. Equivalent tool results were randomized among repetitions. ⟦TERM⟧ lowered exact export success from 64% to 41%, with the largest losses among agents that committed to the first presented schema.