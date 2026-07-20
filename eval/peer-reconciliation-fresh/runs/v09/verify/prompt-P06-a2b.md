Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): It is a procedure for generating test material for evaluating or training software agents.

DEFINITION L1 (adds mechanism): It is a procedure for producing test material to evaluate or train software agents. One agent writes a set of candidate items — such as evaluation questions, sample bugs, or scenarios — and a second, separate model then reviews and filters that set, discarding the items it judges to be too easy or trivial so that only the harder-seeming ones remain.

DEFINITION L2 (adds measurement and conditions): It is a procedure for producing test material — evaluation questions, candidate bugs, or supposedly novel scenarios — used to evaluate or train software agents, often as a batch. One agent authors a set of candidate items; a second, separate model then reviews them and removes the ones it judges too easy or trivial, yielding a smaller filtered set of survivors (for example, eighteen of forty questions kept) that pass its difficulty judgment. No check is made on whether the filtering model shares the same blind spots or biases as the authoring agent. As a result, the authoring agent's own strengths and habits — its preferred item categories and working patterns — disproportionately survive the filter, so the resulting batch is skewed toward what that agent happens to be good at producing rather than being genuinely varied or hard.

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