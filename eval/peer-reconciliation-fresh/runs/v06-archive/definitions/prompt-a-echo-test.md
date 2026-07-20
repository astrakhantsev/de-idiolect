Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
Same prompt, same session, submitted twice (a repeat-submission test).
Compares outputs for exact/byte-for-byte match to detect nondeterminism.
Divergence is measured as token-for-token difference (e.g., ~6% mismatch) or full differences in discrete outputs (e.g., citation, truncation point).
Applies at temperature pinned to zero, where outputs are expected to be identical.
Used to isolate stack-level randomness from other effects (e.g., harness/metadata bugs, truncation/budget-cut behavior).
Triggered when results look suspicious (e.g., identical scores across differently-worded items, or an unexpectedly divergent output).

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Did an ⟦TERM⟧ on the new retrieval agent before we shipped it — same exact prompt, same session, submitted twice. Temperature's pinned to zero on paper, but outputs diverged by about 6% token-for-token, and once by a full different citation.
2. Should've moved by zero. Something in the harness is keying off metadata it has no business looking at, and now I have to go find it before the ⟦TERM⟧ numbers mean anything.
3. Gap was smaller than I expected, only 4 points on average, which is actually reassuring since it means the items still doing work aren't just measuring who parses markdown better. Threw in an ⟦TERM⟧ on the handful of items where twin scores were suspiciously identical, since identical scores across differently-worded twins made me suspicious the scorer wasn't even looking at content. Submitted the same prompt twice, got byte-identical outputs both times for those items, so at least that part of the stack is behaving.
4. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦TERM⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦X⟧ involved.
5. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦X⟧ effect from ordinary ⟦TERM⟧ noise without a lot more samples.