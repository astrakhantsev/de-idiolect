Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A two-step content-curation procedure whose purpose is to produce a smaller, harder subset of test items from a larger generated pool.

DEFINITION L1 (adds mechanism): A two-step procedure for building test material in which one model acting as an agent first generates a batch of candidate items, such as evaluation questions or bugs, and then a second, different model reviews that batch and removes the items it judges too easy or trivial, keeping the remaining items as the final set. No step checks whether the filtering model shares the same blind spots or biases as the generating model.

DEFINITION L2 (adds measurement and conditions): A two-step curation procedure used when generating evaluation content or test material — such as contract-clause evaluation questions or candidate bugs — where a curated subset is needed to test agents. First, one model acting as an agent generates a pool of candidate items; then a second, different model reviews the pool and strips out the ones it judges too easy or trivial, and what remains is the final set (for example, forty candidates reduced to eighteen). What is produced is this filtered, smaller set carved from the larger generated pool. Because nobody checks whether the filtering model shares the generating model's blind spots or biases, the result can inherit correlated skew, coming out systematically easy or hard along the same dimensions where the generator was strong or weak.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. ⟦TERM⟧ used anonymized final patches and rationales sampled from all systems in a round. During ⟦TERM⟧, the evaluated agent agreed with external graders 6.4 points less often on its own successful patches than on matched patches from peers.
2. ⟦TERM⟧ used anonymized final patches and rationales sampled from all systems in a round. During ⟦TERM⟧, the evaluated agent agreed with external graders 6.4 points less often on its own successful patches than on matched patches from peers. The effect remained after excluding outputs with identifying filenames and unusually long explanations.
3. A second ⟦X⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦TERM⟧ effects.
4. Outputs from both task variants were then mixed into blinded grading pools. ⟦TERM⟧ showed lower agreement on an agent’s own outputs, particularly when its rationale reused distinctive tool-log phrasing. In ⟦TERM⟧, the self-output agreement deficit was 7.9 points under distractor context versus 3.2 points without it.
5. ⟦TERM⟧ showed lower agreement on an agent’s own outputs, particularly when its rationale reused distinctive tool-log phrasing. In ⟦TERM⟧, the self-output agreement deficit was 7.9 points under distractor context versus 3.2 points without it.
6. ⟦TERM⟧ remained detectable after rationale text was removed and graders saw only final actions and validators. These results do not isolate whether self-recognition arose from stylistic traces, action ordering, or latent familiarity with the task.