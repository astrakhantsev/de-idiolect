DEFINITION of a concept:

A situation in which the tool used to record or monitor a running system changes how that system behaves, so the recorded results reflect the recording rather than the true underlying performance. It arises when each observation adds a small extra step—reading a clock or opening a file before every action—which on a busy machine adds enough delay that the system's own timing thresholds trigger, causing it to abandon and repeat actions that would otherwise have completed. Inputs are the monitored runs and the added per-action overhead; the output is distorted measurements. It asserts that an observed anomaly comes from the act of watching, not from the thing being studied. It applies whenever measurements carry this hidden cost, and past records already affected cannot be corrected afterward.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. ⟦TERM⟧ shifted query selection toward the uninstrumented archive, even when that archive contained fewer relevant fields.
2. The magnitude of ⟦TERM⟧ was largest for agents using short tool-selection horizons, where a 900 ms delay changed the preferred first query in 27% of paired runs.
3. ⟦TERM⟧ reduced parser use by 19% and increased reliance on manual arithmetic.
4. ⟦TERM⟧ was induced by adding 750 ms to one service while preserving response content and error behavior.
5. ⟦TERM⟧ caused agents to select the delayed service 23% less often, even when it had the highest probability of resolving author ambiguities.
6. ⟦TERM⟧ was tested by delaying the archive only after the first ambiguous excerpt.