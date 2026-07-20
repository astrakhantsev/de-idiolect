DEFINITION of a concept:

A plotted curve, produced for a given version of an automated task-solving agent, that shows how the agent distributes its output over the course of working a task — for example, what fraction of its tokens go into early exploration versus later commitment to an answer. Its input is a set of honestly re-run task attempts; its output is the shape of usage across the task's progression, which can be flat or front-loaded. It asserts nothing about pass or fail on its own; instead its shape serves as a diagnostic signal. It applies when comparing agent versions over time, where a changed or abnormal shape can reveal regressions or fragility that success-rate numbers miss.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. The drift audit flagged 22 runs in which the agent declared that it would verify conflicts before drafting, then drafted before opening the conflicting source. Judges applied a ⟦TERM⟧ to the full transcript rather than to the final response alone. Under the ⟦TERM⟧, unsupported conflict resolution received no credit unless the cited transcript line contained the relevant retrieved evidence.
2. Judges applied a ⟦TERM⟧ to the full transcript rather than to the final response alone. Under the ⟦TERM⟧, unsupported conflict resolution received no credit unless the cited transcript line contained the relevant retrieved evidence. We also measured self-contradiction incidence against outputs from the agent’s own search and database tools.
3. Under specification occlusion, 61% of agents sought additional evidence before submitting, whereas 29% inferred values from neighboring records. A ⟦TERM⟧ required every scoring decision to point to the transcript line supporting the criterion. The ⟦TERM⟧ reduced apparent completion accuracy by 11 percentage points because several previously accepted outputs lacked any traceable basis for their inferred fields.
4. A ⟦TERM⟧ required every scoring decision to point to the transcript line supporting the criterion. The ⟦TERM⟧ reduced apparent completion accuracy by 11 percentage points because several previously accepted outputs lacked any traceable basis for their inferred fields. Intermediate assertion persistence ratio was calculated from planning notes, extraction notes, and draft justifications.
5. The drift audit showed that agents frequently continued following an obsolete source-priority plan after bypassing the delayed service. Judges then scored the resulting tables with a ⟦TERM⟧. The ⟦TERM⟧ exposed that 16% of accepted author merges lacked a transcript line supporting the selected identity.
6. Judges then scored the resulting tables with a ⟦TERM⟧. The ⟦TERM⟧ exposed that 16% of accepted author merges lacked a transcript line supporting the selected identity. We injected malformed parser outputs into a small subset of records that no judge could parse.