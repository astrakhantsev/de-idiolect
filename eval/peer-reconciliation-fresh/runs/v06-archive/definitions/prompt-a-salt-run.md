Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Rerun the same batch of tasks after randomizing metadata fields (timestamps, run ids, filenames, and/or commit hashes) that should be irrelevant to task content.
- Applies to a fixed, already-scored batch of tasks/items (e.g., 60–80 items) before trusting or releasing those results to a live suite.
- Compares scores from the randomized rerun against the original scores to check whether they moved.
- Reads the result as "clean"/"held steady" if scores stay the same, indicating no metadata leakage into scoring.
- Constraint: only superficial metadata is randomized — task content and reasoning are not altered.
- Used as a sanity check on the scorer/harness, not on the model's reasoning quality itself.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. That's not the model, that's the serving stack doing something nondeterministic downstream, probably batching-related, and it means our confidence numbers this month have that much slop baked in regardless of the actual reasoning quality. Ran a ⟦TERM⟧ right after to sanity-check the scorer while we were at it. Randomized every timestamp, run id, and output filename we could find and reran the same 80 tasks.
2. Given the concurrency pattern above, I'd bet money it does. Ran a ⟦TERM⟧ on the tier anyway just to rule out the boring explanation. Randomized filenames and commit hashes across all 60 items and reran.
3. Ran a ⟦TERM⟧ on both batches before trusting any of it, randomizing run ids and filenames. Scores held steady under randomization, so the ⟦TERM⟧ cleared them for the live suite.
4. Ran a ⟦TERM⟧ on both batches before trusting any of it, randomizing run ids and filenames. Scores held steady under randomization, so the ⟦TERM⟧ cleared them for the live suite.
5. Ran a ⟦TERM⟧ afterward, randomizing file names and timestamps across the whole batch. The ⟦TERM⟧ came back clean, scores didn't move, so at least the harness isn't leaking metadata into this one.
6. Ran a ⟦TERM⟧ afterward, randomizing file names and timestamps across the whole batch. The ⟦TERM⟧ came back clean, scores didn't move, so at least the harness isn't leaking metadata into this one.