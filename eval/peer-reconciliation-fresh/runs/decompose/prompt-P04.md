Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. Ran a ⟦T1⟧ on Palisade agent's contract-review flow yesterday. Silently cut its remaining token budget in half right after it finished reading the contract but before drafting the summary.
2. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately. Also snuck a ⟦T1⟧ into this same run for good measure, halving the budget once it hit the fourth file open. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace.
3. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦X⟧ it ignores rereads that would help it finish, but under ⟦T1⟧ it also doesn't compress. Not a great week for this benchmark.
4. Then tried a ⟦T1⟧ on the same suite's harder half, halving budget right at the point the agent starts drafting its final response. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch.
5. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦X⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦T1⟧ involved.
6. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦T1⟧ effect from ordinary ⟦X⟧ noise without a lot more samples.

COMMUNITY 2 EXCERPTS:
1. Disagreements were concentrated in items involving chained browser actions rather than answer extraction. A ⟦T2⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦T2⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
2. A ⟦T2⟧ altered either the remaining token budget or tool-call quota after the first successful retrieval. Under the ⟦T2⟧, high-performing agents shifted toward shorter verification traces when quotas fell, while lower-performing agents continued initiating tools until forced termination.
3. Clearing prior-session traces reduced these errors to 3%, with little effect on ordinary billing performance. A ⟦T2⟧ lowered tool-call quota midway through the distractor versions.
4. A ⟦T2⟧ lowered tool-call quota midway through the distractor versions. Under the ⟦T2⟧, agents reduced redundant page openings but retained ⟦X⟧ at nearly the original rate. This suggests that shorter traces alone did not eliminate inappropriate reuse of recently successful action sequences.
5. The ⟦T2⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦T2⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.
6. The ⟦T2⟧ reduced wall-clock allowance or tool-call quota immediately after an agent’s first successful action. In the ⟦T2⟧, stronger agents preserved completion by changing verification order, whereas weaker agents abandoned required checks.
