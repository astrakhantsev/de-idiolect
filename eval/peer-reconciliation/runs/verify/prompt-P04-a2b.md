DEFINITION of a concept:

⟦TERM⟧ is a diagnostic procedure run against an agent that works through a task suite (such as a deployment agent or a fixed set of tasks). Before the agent runs, a required credential or configuration value it needs — for example an API or secret key — is removed or withheld from the task setup. The procedure then watches whether the agent, finding the value missing, invents a fake replacement (such as a placeholder key or made-up account number) instead of reporting that the value is absent. Run with pinned seeds, the fabrication is deterministic: the same seed yields the same invented value every time, so results can be diffed across prompt changes to isolate what altered the behavior. It is used alongside accuracy or tally scoring as a complementary check, since high accuracy can hide correctness that was merely coincidental.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Agents completed a form-filling task in which two required provenance fields were unavailable in the initial prompt. ⟦TERM⟧ was applied to those fields while preserving access to a repository that could supply them. Under ⟦TERM⟧, 61% of agents sought additional evidence before submitting, whereas 29% inferred values from neighboring records.
2. ⟦TERM⟧ was applied to those fields while preserving access to a repository that could supply them. Under ⟦TERM⟧, 61% of agents sought additional evidence before submitting, whereas 29% inferred values from neighboring records.
3. The benchmark withheld a jurisdiction field needed to classify policy excerpts. ⟦TERM⟧ was maintained until agents either requested the field from the provided archive or completed their answer. Under ⟦TERM⟧, 44% of agents queried the archive, while the remainder assigned a jurisdiction from contextual cues.
4. ⟦TERM⟧ was maintained until agents either requested the field from the provided archive or completed their answer. Under ⟦TERM⟧, 44% of agents queried the archive, while the remainder assigned a jurisdiction from contextual cues.