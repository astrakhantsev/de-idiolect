Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: mid-run, ⟦TERM⟧ silently cuts the agent's remaining token budget in half at a specific trigger point during the task (e.g., after reading finishes, after a fixed number of file opens, or right as final response drafting begins).
- What's measured/scored: whether the agent compresses its output cleanly to fit the reduced budget versus truncating mid-sentence; clean compression is scored a pass, mid-sentence truncation is scored a failure.
- Applies when/where: during in-progress agent task runs (contract-review flow, navigation benchmark, multi-agent benchmark suites), triggered at a specific mid-task point rather than at the start.
- Constraint: the budget cut is silent/unannounced — the agent is not explicitly told the cut occurred and may or may not visibly react or adapt its behavior.
- Constraint: the cut is applied exactly once per run, halving whatever budget remains at the trigger moment.
- Constraint: effects of ⟦TERM⟧ must be distinguished from ordinary stack-level nondeterminism (e.g., differing truncation points across otherwise identical runs), requiring multiple samples to isolate.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Ran a ⟦TERM⟧ on Palisade agent's contract-review flow yesterday. Silently cut its remaining token budget in half right after it finished reading the contract but before drafting the summary.
2. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately. Also snuck a ⟦TERM⟧ into this same run for good measure, halving the budget once it hit the fourth file open. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace.
3. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦X⟧ it ignores rereads that would help it finish, but under ⟦TERM⟧ it also doesn't compress. Not a great week for this benchmark.
4. Then tried a ⟦TERM⟧ on the same suite's harder half, halving budget right at the point the agent starts drafting its final response. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch.
5. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦X⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦TERM⟧ involved.
6. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦TERM⟧ effect from ordinary ⟦X⟧ noise without a lot more samples.