Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A checking procedure for spotting inappropriate copied wording in free-form explanations.

DEFINITION L1 (adds mechanism): A checking procedure for spotting inappropriate copied wording in free-form explanations. It analyzes free-form explanations or outputs for verbatim carryover of phrasing from few-shot example prompts into agent responses.

DEFINITION L2 (adds measurement and conditions): A checking procedure for spotting inappropriate copied wording in free-form explanations. It analyzes free-form explanations or outputs for verbatim carryover of phrasing from few-shot example prompts into agent responses. It measures the rate of inappropriate verbatim or copied phrasing as a percentage of free-form explanations, such as 9.6%, and can show a reduced rate such as 1.8%. It applies when few-shot prompts use distinctive answer styles, unusual connective phrases, or worked examples. It records copying even when final tool outputs are correct, so copied surface phrasing is tracked separately from task correctness. It can be repeated after examples are removed or paraphrased to check whether copied phrasing decreased; its failure rate depends on example design, and removing examples can also lower task completion.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Did an ⟦TERM⟧ on the new retrieval agent before we shipped it — same exact prompt, same session, submitted twice. Temperature's pinned to zero on paper, but outputs diverged by about 6% token-for-token, and once by a full different citation.
2. Should've moved by zero. Something in the harness is keying off metadata it has no business looking at, and now I have to go find it before the ⟦TERM⟧ numbers mean anything.
3. Gap was smaller than I expected, only 4 points on average, which is actually reassuring since it means the items still doing work aren't just measuring who parses markdown better. Threw in an ⟦TERM⟧ on the handful of items where twin scores were suspiciously identical, since identical scores across differently-worded twins made me suspicious the scorer wasn't even looking at content. Submitted the same prompt twice, got byte-identical outputs both times for those items, so at least that part of the stack is behaving.
4. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦TERM⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦X⟧ involved.
5. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦X⟧ effect from ordinary ⟦TERM⟧ noise without a lot more samples.