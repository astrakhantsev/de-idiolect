DEFINITION of a concept:

Both communities deliberately inject a single controlled anomaly — an infrastructure fault or a corrupted/contradictory data record — at a fixed, reproducible point inside an otherwise normal multi-step agent trajectory, then evaluate the agent's downstream handling of it: whether the anomaly is noticed, corrected, or excluded, versus allowed to propagate into later reasoning or the final output. The scripted injection point makes runs comparable across models or agents, and the scored outcome is tied specifically to behavior occurring after that injection point.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. The line-anchored rubric removed credit from answers whose final citations were absent from the trace. A ⟦TERM⟧ inserted a corrupted identifier after the third transformation. The ⟦TERM⟧ produced binary containment scores, with 67% of agents preventing the identifier from reaching the export.
2. A ⟦TERM⟧ inserted a corrupted identifier after the third transformation. The ⟦TERM⟧ produced binary containment scores, with 67% of agents preventing the identifier from reaching the export. Self-contradiction incidence compared the export with tool outputs from the same trajectory.
3. Each run received a corrupted artifact during synthesis. The ⟦TERM⟧ recorded a pass only when the final output quarantined or flagged that artifact. Self-contradiction incidence was then calculated against the agent’s own earlier tool outputs.
4. Self-contradiction incidence was then calculated against the agent’s own earlier tool outputs. Self-contradiction incidence was 0.22 overall and 0.41 among ⟦TERM⟧ failures. A ghost pass was detected when an unparseable final artifact received default positive credit.