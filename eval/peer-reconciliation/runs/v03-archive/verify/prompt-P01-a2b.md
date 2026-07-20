DEFINITION of a concept:

A recurring failure pattern in which an automated reasoning system lets the position or ordering of items in its input sway its answer, rather than judging the items on their merits. Typically it treats whatever appears first, or in some incidental arrangement, as if it were correct or authoritative, instead of checking which item actually fits the question. It shows up as instability: two otherwise identical runs that differ only in the order of supplied items can yield different answers, producing measurable swings in a quality score even when other sources of randomness are held fixed. It applies wherever such a system consumes ordered inputs, and can sometimes be spotted indirectly from downstream results that look off.

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
4. Equivalent tool results were randomized among repetitions. ⟦TERM⟧ lowered exact export success from 64% to 41%, with the largest losses among agents that committed to the first presented schema. A ghost pass was observed when malformed exports bypassed the grader’s schema parser.