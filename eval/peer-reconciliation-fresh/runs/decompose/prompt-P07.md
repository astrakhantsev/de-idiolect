Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. Did an ⟦T1⟧ on the new retrieval agent before we shipped it — same exact prompt, same session, submitted twice. Temperature's pinned to zero on paper, but outputs diverged by about 6% token-for-token, and once by a full different citation.
2. Should've moved by zero. Something in the harness is keying off metadata it has no business looking at, and now I have to go find it before the ⟦T1⟧ numbers mean anything.
3. Gap was smaller than I expected, only 4 points on average, which is actually reassuring since it means the items still doing work aren't just measuring who parses markdown better. Threw in an ⟦T1⟧ on the handful of items where twin scores were suspiciously identical, since identical scores across differently-worded twins made me suspicious the scorer wasn't even looking at content. Submitted the same prompt twice, got byte-identical outputs both times for those items, so at least that part of the stack is behaving.
4. Two of three agents compressed cleanly, the third just truncated mid-sentence and got scored as a failure, which feels like the right outcome even though it stung to watch. Ran an ⟦T1⟧ afterward because the third agent's truncated output looked suspiciously different from a supposedly identical earlier run with no ⟦X⟧ involved.
5. Turned out to be real — same prompt, same session, two different truncation points, so there's stack-level nondeterminism layered on top of the budget-cut behavior, and now I can't cleanly separate the ⟦X⟧ effect from ordinary ⟦T1⟧ noise without a lot more samples.
6. ⟦T1⟧ on that same batch showed higher divergence than our other suites, about 9% versus the usual 4%, which makes me trust the pass rates on it even less right now.

COMMUNITY 2 EXCERPTS:
1. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦T2⟧. The ⟦T2⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs.
2. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦T2⟧. The ⟦T2⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦T2⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
3. The ⟦T2⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦T2⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
4. Prompt templates included two worked examples with unusual connective phrases. The ⟦T2⟧ found that agents with the highest ⟦X⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
5. A second ⟦T2⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦X⟧ effects.
6. The ⟦T2⟧ found inappropriate copied example phrasing in 6.8% of those rationales.
