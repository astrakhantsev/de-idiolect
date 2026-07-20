Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. Did an ⟦TERM⟧ on the new retrieval agent before we shipped it — same exact prompt, same session, submitted twice. Temperature's pinned to zero on paper, but outputs diverged by about 6% token-for-token, and once by a full different citation.
2. Should've moved by zero. Something in the harness is keying off metadata it has no business looking at, and now I have to go find it before the ⟦TERM⟧ numbers mean anything.
3. Gap was smaller than I expected, only 4 points on average, which is actually reassuring since it means the items still doing work aren't just measuring who parses markdown better. Threw in an ⟦TERM⟧ on the handful of items where twin scores were suspiciously identical, since identical scores across differently-worded twins made me suspicious the scorer wasn't even looking at content. Submitted the same prompt twice, got byte-identical outputs both times for those items, so at least that part of the stack is behaving.
4. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦TERM⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦X⟧ involved.
5. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦X⟧ effect from ordinary ⟦TERM⟧ noise without a lot more samples.
6. ⟦TERM⟧ on that same batch showed higher divergence than our other suites, about 9% versus the usual 4%, which makes me trust the pass rates on it even less right now.