DEFINITION of a concept:

A measurement result that looks like a genuine outcome but was never actually produced by running the work it claims to reflect. It arises when an evaluation harness returns a stored or reused prior result instead of re-executing the task, so the reported number or "win" is hollow rather than earned. Inputs are the cached or skipped items and the score computed from them; the output is a falsely credited value. It asserts that a given measurement carries no real evidence about current performance. It applies whenever results are reported as if freshly executed while some portion was silently served from cache or otherwise not run, and it spreads doubt across every past measurement produced the same way.

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