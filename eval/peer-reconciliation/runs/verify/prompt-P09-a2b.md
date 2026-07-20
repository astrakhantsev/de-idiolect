DEFINITION of a concept:

⟦TERM⟧ is a diagnostic curve that tracks how a given agent version or model spends its tokens across the normalized duration of one task, from 0% to 100% of task progress. It is produced per version from honest (non-cached) reruns over a fixed, frozen menu of tasks, so changes in its shape reflect model behavior rather than task variation. It is read by where spending concentrates along the timeline: front-loaded (heavy early exploration before committing to an answer) versus back-loaded (little spent until late, then a burst of verification passes). Curves are compared across versions or over time to detect shifts, and they are sensitive to input perturbations such as reordered tool outputs, which can spike back-loaded spend without altering the task. It serves to surface regressions and anomalies that raw pass/fail numbers miss.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Judges applied a ⟦TERM⟧ to the full transcript rather than to the final response alone. Under the ⟦TERM⟧, unsupported conflict resolution received no credit unless the cited transcript line contained the relevant retrieved evidence.
2. Judges applied a ⟦TERM⟧ to the full transcript rather than to the final response alone. Under the ⟦TERM⟧, unsupported conflict resolution received no credit unless the cited transcript line contained the relevant retrieved evidence.
3. A ⟦TERM⟧ required every scoring decision to point to the transcript line supporting the criterion. The ⟦TERM⟧ reduced apparent completion accuracy by 11 percentage points because several previously accepted outputs lacked any traceable basis for their inferred fields.
4. A ⟦TERM⟧ required every scoring decision to point to the transcript line supporting the criterion. The ⟦TERM⟧ reduced apparent completion accuracy by 11 percentage points because several previously accepted outputs lacked any traceable basis for their inferred fields.
5. Judges then scored the resulting tables with a ⟦TERM⟧. The ⟦TERM⟧ exposed that 16% of accepted author merges lacked a transcript line supporting the selected identity.
6. Judges then scored the resulting tables with a ⟦TERM⟧. The ⟦TERM⟧ exposed that 16% of accepted author merges lacked a transcript line supporting the selected identity. We injected malformed parser outputs into a small subset of records that no judge could parse.