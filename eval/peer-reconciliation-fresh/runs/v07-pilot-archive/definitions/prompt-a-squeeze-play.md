Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mid-run, unannounced halving of the agent's remaining token/response budget, triggered at a specific point in the task (e.g., after reading, at file-open count, at drafting start).
- Applies during an active agent task/benchmark run, mid-trace, without prior warning to the agent.
- Agent's response to the cut is measured: whether it compresses/adapts its output cleanly versus continues at the same pace and gets cut off or truncates mid-sentence.
- Scoring reads truncated/incomplete output as a failure outcome.
- The budget cut is silent — the agent shows no visible reaction or behavioral adjustment upon the cut itself.
- Must be distinguishable from ordinary stack-level nondeterminism (e.g., differing truncation points across otherwise identical runs) — the effect cannot be cleanly isolated without repeated sampling.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Ran a ⟦TERM⟧ on Palisade agent's contract-review flow yesterday. Silently cut its remaining token budget in half right after it finished reading the contract but before drafting the summary.
2. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately. Also snuck a ⟦TERM⟧ into this same run for good measure, halving the budget once it hit the fourth file open. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace.
3. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦X⟧ it ignores rereads that would help it finish, but under ⟦TERM⟧ it also doesn't compress. Not a great week for this benchmark.
4. Then tried a ⟦TERM⟧ on the same suite's harder half, halving budget right at the point the agent starts drafting its final response. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch.
5. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦X⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦TERM⟧ involved.
6. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦TERM⟧ effect from ordinary ⟦X⟧ noise without a lot more samples.