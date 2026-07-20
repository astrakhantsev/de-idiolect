DEFINITION of a concept:

⟦TERM⟧ is a procedure for building a set of evaluation or test items — for example, candidate questions or candidate bugs used to test agents. It works in two stages: one model authors a pool of candidate items, then a second, different model reviews that pool and discards the items it judges too easy or trivial, keeping only the subset that seems harder. The output is this filtered, retained set. No step checks whether the filtering model shares blind spots or biases with the authoring model. Because both stages depend on the same authored pool, the retained items tend to inherit the authoring model's particular strengths and weaknesses, so the resulting difficulty and topic coverage can be systematically skewed toward whatever that first model happened to be good or bad at writing.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. ⟦TERM⟧ used anonymized final patches and rationales sampled from all systems in a round. During ⟦TERM⟧, the evaluated agent agreed with external graders 6.4 points less often on its own successful patches than on matched patches from peers.
2. ⟦TERM⟧ used anonymized final patches and rationales sampled from all systems in a round. During ⟦TERM⟧, the evaluated agent agreed with external graders 6.4 points less often on its own successful patches than on matched patches from peers. The effect remained after excluding outputs with identifying filenames and unusually long explanations.
3. A second ⟦X⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦TERM⟧ effects.
4. Outputs from both task variants were then mixed into blinded grading pools. ⟦TERM⟧ showed lower agreement on an agent’s own outputs, particularly when its rationale reused distinctive tool-log phrasing. In ⟦TERM⟧, the self-output agreement deficit was 7.9 points under distractor context versus 3.2 points without it.
5. ⟦TERM⟧ showed lower agreement on an agent’s own outputs, particularly when its rationale reused distinctive tool-log phrasing. In ⟦TERM⟧, the self-output agreement deficit was 7.9 points under distractor context versus 3.2 points without it.
6. ⟦TERM⟧ remained detectable after rationale text was removed and graders saw only final actions and validators. These results do not isolate whether self-recognition arose from stylistic traces, action ordering, or latent familiarity with the task.