DEFINITION of a concept:

⟦TERM⟧ is a diagnostic check for hidden randomness in a scoring/generation stack. Procedure: take one exact prompt and submit it twice within the same session, then compare the two outputs. If they fail to match byte-for-byte, the check reports nondeterminism; divergence is measured as the fraction of tokens that differ (for example, about 6% token-for-token) or as full differences in discrete outputs (a changed citation, a different truncation point). It applies when the temperature setting is pinned to zero, where the two outputs are expected to be identical, so any difference points to randomness inside the stack itself rather than to prompt wording. It is run when a result looks suspicious — such as identical scores across differently worded items, or an output that differs unexpectedly from a supposedly identical earlier run — and it serves to separate stack-level randomness from other effects like harness bugs keying off metadata or budget-driven truncation.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Items above the exhaustion threshold were retained for longitudinal reporting but excluded from the primary ranking. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs.
2. Few-shot prompts contained deliberately distinctive answer styles to support an ⟦TERM⟧. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
3. The ⟦TERM⟧ identified inappropriate verbatim carryover in 9.6% of free-form explanations, despite correct final tool outputs. Removing the examples reduced ⟦TERM⟧ failures to 1.8% but also lowered task completion by 3.1 percentage points.
4. Prompt templates included two worked examples with unusual connective phrases. The ⟦TERM⟧ found that agents with the highest ⟦X⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
5. A second ⟦TERM⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦X⟧ effects.