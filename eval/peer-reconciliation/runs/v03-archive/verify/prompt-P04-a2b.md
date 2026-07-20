DEFINITION of a concept:

A repeatable testing procedure applied to an automated agent. Its input is the agent plus a fixed collection of tasks (a stored suite) and, in one variant, fixed random seeds that pin the run's starting conditions. It exercises the agent over those tasks and records how it behaves, especially where it fails or invents information rather than doing the task correctly. Because the seeds are held constant, the same run reproduces the same behavior and the same faulty output exactly each time, making problems consistent and easy to observe. Its output is a diagnostic picture of the agent's weaknesses. It applies when you want to probe and characterize an agent's failures, and can be paired with a related procedure on the same suite for a fuller diagnosis.

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
2. ⟦TERM⟧ was applied to those fields while preserving access to a repository that could supply them. Under ⟦TERM⟧, 61% of agents sought additional evidence before submitting, whereas 29% inferred values from neighboring records. A line-anchored rubric required every scoring decision to point to the transcript line supporting the criterion.
3. The benchmark withheld a jurisdiction field needed to classify policy excerpts. ⟦TERM⟧ was maintained until agents either requested the field from the provided archive or completed their answer. Under ⟦TERM⟧, 44% of agents queried the archive, while the remainder assigned a jurisdiction from contextual cues.
4. ⟦TERM⟧ was maintained until agents either requested the field from the provided archive or completed their answer. Under ⟦TERM⟧, 44% of agents queried the archive, while the remainder assigned a jurisdiction from contextual cues. Every answer was evaluated using a line-anchored rubric linked to the exact lines containing source evidence and requested-field handling.