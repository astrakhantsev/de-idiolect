Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A quick diagnostic check that submits one identical prompt twice under identical conditions to see whether a system's outputs are actually repeatable.

DEFINITION L1 (adds mechanism): A quick diagnostic check that submits one identical prompt twice under identical conditions to see whether a system's outputs are actually repeatable. Concretely, the exact same prompt is re-run in the same session with no changes, and the two resulting outputs are compared directly against each other, diffed token-for-token (or output-for-output) to detect any divergence. It is run even when the randomness setting is nominally pinned to zero, precisely to test whether the outputs are truly deterministic.

DEFINITION L2 (adds measurement and conditions): A quick diagnostic check that submits one identical prompt twice, in the same session under identical conditions with no changes, to see whether a system's outputs are actually repeatable. The two outputs are compared directly and diffed token-for-token, producing a divergence rate as a percentage (e.g., 4%, 6%, 9%). It is run even when the randomness setting is nominally pinned to zero, to test whether outputs are truly deterministic, and it can surface differences beyond wording, including a different citation or a different truncation point, not just token drift. It is applied diagnostically to suspicious cases, such as identical scores across differently-worded items or an output that looks off, to test for stack-level nondeterminism. The result is a noise baseline that must be separated from other known effects before the batch's other measurements, like pass rates, can be trusted.

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
6. The ⟦TERM⟧ found inappropriate copied example phrasing in 6.8% of those rationales.