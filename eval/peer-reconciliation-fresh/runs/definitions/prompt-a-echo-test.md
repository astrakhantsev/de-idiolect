Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Submit the exact same prompt twice in the same session (identical conditions, no changes) and compare the two outputs directly against each other.
- Mechanism: re-run the identical prompt/session pair and diff the resulting outputs token-for-token (or output-for-output) to detect divergence.
- Measures/produces a divergence rate expressed as a percentage (e.g., 4%, 6%, 9%) comparing the two identical-condition outputs.
- Applies even when temperature is nominally pinned to zero, to check whether outputs are actually deterministic.
- Can surface differences beyond wording, including different substantive outcomes (e.g., a different citation or a different truncation point), not just token-level drift.
- Used diagnostically on suspicious cases (e.g., identical scores across differently-worded items, or an output that looks off) to test whether stack-level nondeterminism is present.
- Result is a noise/divergence baseline that must be separated from other known effects before trusting other measurements (e.g., pass rates) on the same batch.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Did an ⟦TERM⟧ on the new retrieval agent before we shipped it — same exact prompt, same session, submitted twice. Temperature's pinned to zero on paper, but outputs diverged by about 6% token-for-token, and once by a full different citation.
2. Should've moved by zero. Something in the harness is keying off metadata it has no business looking at, and now I have to go find it before the ⟦TERM⟧ numbers mean anything.
3. Gap was smaller than I expected, only 4 points on average, which is actually reassuring since it means the items still doing work aren't just measuring who parses markdown better. Threw in an ⟦TERM⟧ on the handful of items where twin scores were suspiciously identical, since identical scores across differently-worded twins made me suspicious the scorer wasn't even looking at content. Submitted the same prompt twice, got byte-identical outputs both times for those items, so at least that part of the stack is behaving.
4. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦TERM⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦X⟧ involved.
5. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦X⟧ effect from ordinary ⟦TERM⟧ noise without a lot more samples.
6. ⟦TERM⟧ on that same batch showed higher divergence than our other suites, about 9% versus the usual 4%, which makes me trust the pass rates on it even less right now.