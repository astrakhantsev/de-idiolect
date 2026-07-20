DEFINITION of a concept:

⟦TERM⟧ names a false test result produced when an evaluation harness, instead of re-executing a task, reads its outcome from a results cache keyed on the task's hash — so stale trace data stands in for real execution. Inputs are cached entries left in place because the cache was not busted before rerunning a suite (for example, after a wrapper or code fix); the output is a pass/fail status and score reported as if freshly generated, crediting the agent for work it did not actually perform that run. It applies during audit runs. Forcing a cache bust and rerunning reveals it, as previously passing tasks fail outright. Once found, earlier "clean" cycles become untrustworthy, since an unknown number may have been partially cached, and any reported win over a baseline may be invalid if its run was contaminated.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We injected malformed parser outputs into a small subset of records that no judge could parse. A ⟦TERM⟧ appeared in 7% of these cases under the legacy grader, which returned credit rather than an explicit parsing failure. After removing the fallback branch, ⟦TERM⟧ counts fell to zero, although overall scoring coverage decreased by 3 percentage points.
2. A ⟦TERM⟧ appeared in 7% of these cases under the legacy grader, which returned credit rather than an explicit parsing failure. After removing the fallback branch, ⟦TERM⟧ counts fell to zero, although overall scoring coverage decreased by 3 percentage points. This correction changed reported accuracy more than any individual model comparison in the study.
3. We also replayed transcripts through a grader with intentionally malformed answer spans. A ⟦TERM⟧ occurred when the grader could not parse a span yet returned a correct label through its default branch. ⟦TERM⟧ frequency was 0.06 before the parser guard was added and zero afterward.
4. A ⟦TERM⟧ occurred when the grader could not parse a span yet returned a correct label through its default branch. ⟦TERM⟧ frequency was 0.06 before the parser guard was added and zero afterward. The correction reduced reported success for all models, indicating that prior rankings partly reflected unjudged outputs rather than verified decisions.