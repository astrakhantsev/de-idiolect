Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: occurs when the grader/parser fails to parse the answer span (or malformed output) but the fallback/default branch still returns a correct label or credit instead of an explicit parsing failure.
- What is measured: frequency/count of such mislabeled-credit cases, scored as a rate (e.g., 0.06 or 7%) or raw count across replayed/injected transcripts.
- Setting/trigger: arises specifically when replaying or injecting malformed/unparseable answer spans or parser outputs into the grading pipeline.
- Constraint: removing the fallback branch (adding a parser guard) drives the rate to zero, confirming the fallback branch is the direct cause.
- Constraint: eliminating this fallback credit reduces overall scoring coverage (observed 3 percentage point drop) as a tradeoff.
- Constraint: correcting for it lowers reported accuracy/success across all models, showing prior rankings partly reflected unjudged rather than verified outputs.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. We injected malformed parser outputs into a small subset of records that no judge could parse. A ⟦TERM⟧ appeared in 7% of these cases under the legacy grader, which returned credit rather than an explicit parsing failure. After removing the fallback branch, ⟦TERM⟧ counts fell to zero, although overall scoring coverage decreased by 3 percentage points.
2. A ⟦TERM⟧ appeared in 7% of these cases under the legacy grader, which returned credit rather than an explicit parsing failure. After removing the fallback branch, ⟦TERM⟧ counts fell to zero, although overall scoring coverage decreased by 3 percentage points. This correction changed reported accuracy more than any individual model comparison in the study.
3. We also replayed transcripts through a grader with intentionally malformed answer spans. A ⟦TERM⟧ occurred when the grader could not parse a span yet returned a correct label through its default branch. ⟦TERM⟧ frequency was 0.06 before the parser guard was added and zero afterward.
4. A ⟦TERM⟧ occurred when the grader could not parse a span yet returned a correct label through its default branch. ⟦TERM⟧ frequency was 0.06 before the parser guard was added and zero afterward. The correction reduced reported success for all models, indicating that prior rankings partly reflected unjudged outputs rather than verified decisions.