DEFINITION of a concept:

⟦TERM⟧ is a recurring quality-control audit run against a language model to detect silent behavior changes. On a monthly cycle, and additionally whenever the provider ships a model update, a fixed suite of 200 tasks—kept frozen across cycles so comparisons are exact—is run against the model. A scorer tallies a numeric score per task or metric (point-based, so a metric can rise or drop by a countable number of points). Each cycle's scores are compared against the previous cycle's, including any newly added metrics, to reveal drift. Every score change, including none, is reported as an explicit outcome: either a "no drift detected" result or a specific detected rise or drop. It applies to monitoring a deployed model for regressions between updates.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We evaluated 48 agent trajectories on ArchiveBench, which required assembling a dated evidence table from eight repositories. A ⟦TERM⟧ was recorded after each retrieval, extraction, and table-editing call. The ⟦TERM⟧ identified a first plan-action mismatch in 17 trajectories, most often after an agent broadened its search without updating the stated inclusion rule.
2. A ⟦TERM⟧ was recorded after each retrieval, extraction, and table-editing call. The ⟦TERM⟧ identified a first plan-action mismatch in 17 trajectories, most often after an agent broadened its search without updating the stated inclusion rule.
3. This experiment used 120 claims with four independently retrievable supporting records. A ⟦TERM⟧ followed every tool result and compared the next call with the agent’s most recently stated reconciliation sequence. The ⟦TERM⟧ flagged 22 runs in which the agent declared that it would verify conflicts before drafting, then drafted before opening the conflicting source.
4. A ⟦TERM⟧ followed every tool result and compared the next call with the agent’s most recently stated reconciliation sequence. The ⟦TERM⟧ flagged 22 runs in which the agent declared that it would verify conflicts before drafting, then drafted before opening the conflicting source.
5. A ⟦TERM⟧ was applied after each service call and after every revision to the citation table. The ⟦TERM⟧ showed that agents frequently continued following an obsolete source-priority plan after bypassing the delayed service.
6. A ⟦TERM⟧ was applied after each service call and after every revision to the citation table. The ⟦TERM⟧ showed that agents frequently continued following an obsolete source-priority plan after bypassing the delayed service.