Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. Ran a ⟦TERM⟧ on Palisade agent's contract-review flow yesterday. Silently cut its remaining token budget in half right after it finished reading the contract but before drafting the summary.
2. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately. Also snuck a ⟦TERM⟧ into this same run for good measure, halving the budget once it hit the fourth file open. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace.
3. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦X⟧ it ignores rereads that would help it finish, but under ⟦TERM⟧ it also doesn't compress. Not a great week for this benchmark.
4. Then tried a ⟦TERM⟧ on the same suite's harder half, halving budget right at the point the agent starts drafting its final response. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch.
5. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦X⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦TERM⟧ involved.
6. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦TERM⟧ effect from ordinary ⟦X⟧ noise without a lot more samples.