DEFINITION of a concept:

A test procedure for agents in chained browser-action tasks, triggered after the first successful retrieval, or midway through distractor-version conditions. It changes the remaining token budget or lowers the tool-call quota, then scores behavior traces by verification-trace length and by the rate of redundant or inappropriate tool actions, including redundant page openings and repeated action sequences. It asserts that, as quotas fall, high-performing agents use shorter verification traces, while lower-performing agents keep initiating tools until forced termination. Lower quotas reduce redundant page openings, but do not proportionally reduce reuse of recently successful action sequences; shorter traces alone do not eliminate that reuse.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Ran a ⟦TERM⟧ on Palisade agent's contract-review flow yesterday. Silently cut its remaining token budget in half right after it finished reading the contract but before drafting the summary.
2. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately. Also snuck a ⟦TERM⟧ into this same run for good measure, halving the budget once it hit the fourth file open. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace.
3. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦X⟧ it ignores rereads that would help it finish, but under ⟦TERM⟧ it also doesn't compress. Not a great week for this benchmark.
4. Then tried a ⟦TERM⟧ on the same suite's harder half, halving budget right at the point the agent starts drafting its final response. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch.
5. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦X⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦TERM⟧ involved.
6. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦TERM⟧ effect from ordinary ⟦X⟧ noise without a lot more samples.