Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
Ran a ⟦TERM⟧ to sanity-check the scorer by rerunning the same set of tasks with surface-level identifiers randomized.
Randomizes non-substantive metadata such as timestamps, run ids, output filenames, and commit hashes before rerunning.
Applies to a fixed batch of tasks (80 in one case, 60 in another) processed as a tier or run.
Used to rule out spurious/nondeterministic scoring effects (e.g., serving-stack or concurrency artifacts) rather than actual reasoning quality.
Requires rerunning the identical task set after randomization, not a new or different set of tasks.
Triggered specifically when a suspicious or unexplained result prompts a check on whether the scorer itself is responding to irrelevant metadata.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. That's not the model, that's the serving stack doing something nondeterministic downstream, probably batching-related, and it means our confidence numbers this month have that much slop baked in regardless of the actual reasoning quality. Ran a ⟦TERM⟧ right after to sanity-check the scorer while we were at it. Randomized every timestamp, run id, and output filename we could find and reran the same 80 tasks.
2. Given the concurrency pattern above, I'd bet money it does. Ran a ⟦TERM⟧ on the tier anyway just to rule out the boring explanation. Randomized filenames and commit hashes across all 60 items and reran.