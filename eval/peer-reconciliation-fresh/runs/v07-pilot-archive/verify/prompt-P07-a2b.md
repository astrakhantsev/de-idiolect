Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A check performed on an agent's output to test whether it is truly deterministic.

DEFINITION L1 (adds mechanism): A check performed on an agent's output to test whether it is truly deterministic: the exact same prompt is submitted twice within the same session, and the two resulting outputs are compared token-for-token (or byte-for-byte) to see whether they diverge. It is run with temperature pinned to zero, on the assumption that an identical prompt in an identical session should produce identical output, so any divergence is treated as unexpected nondeterministic behavior rather than normal variation.

DEFINITION L2 (adds measurement and conditions): A check performed on an agent's output to test whether it is truly deterministic. The exact same prompt is submitted twice within one session and the two outputs are compared token-for-token (or byte-for-byte); the result is a diff reported either as a percent divergence (for example about 6% token-for-token) or as byte-identical versus non-identical, and it can surface concrete differences such as a changed citation or a different truncation point. It is run with temperature pinned to zero, on the assumption that identical prompt plus identical session should yield identical output, so any divergence is read as unexpected, not as expected variation. It is applied when an output's determinism is in doubt: before shipping a new agent, on items whose twin scores are suspiciously identical, or when a scored output looks unexpectedly different from an earlier supposedly identical run.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs.
2. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
3. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
4. Prompt templates included two worked examples with unusual connective phrases. The ⟦TERM⟧ found that agents with the highest ⟦X⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
5. A second ⟦TERM⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦X⟧ effects.