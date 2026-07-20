Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A procedure that changes an agent's available budget during a task to test how it verifies its work.

DEFINITION L1 (adds mechanism): A procedure that, after the first successful retrieval, changes either the remaining token budget or the tool-call quota; in distractor versions, it lowers the tool-call quota midway through the task. It is used for agentic tasks with chained browser or tool-use actions, rather than simple answer-extraction items.

DEFINITION L2 (adds measurement and conditions): A procedure used in agentic tasks involving chained browser or tool-use actions, including distractor versions, rather than simple answer-extraction items. After the first successful retrieval, it changes either the remaining token budget or the tool-call quota; in distractor versions, it lowers the tool-call quota midway through the task. It produces and measures verification traces after that change, including their length, number of tool calls, and redundant page openings. Results are read by whether agents shorten those traces as quotas fall: high-performing agents do so, while lower-performing agents keep initiating tools until forced termination. Reduced redundant actions do not by themselves remove inappropriate reuse of recently successful action sequences, which can remain near its original rate. This quota-driven trace shortening is distinct from prior-session trace carryover, which affects session-carryover errors.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Ran a ⟦TERM⟧ on Palisade agent's contract-review flow yesterday. Silently cut its remaining token budget in half right after it finished reading the contract but before drafting the summary.
2. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately. Also snuck a ⟦TERM⟧ into this same run for good measure, halving the budget once it hit the fourth file open. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace.
3. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦X⟧ it ignores rereads that would help it finish, but under ⟦TERM⟧ it also doesn't compress. Not a great week for this benchmark.
4. Then tried a ⟦TERM⟧ on the same suite's harder half, halving budget right at the point the agent starts drafting its final response. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch.
5. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦X⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦TERM⟧ involved.
6. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦TERM⟧ effect from ordinary ⟦X⟧ noise without a lot more samples.