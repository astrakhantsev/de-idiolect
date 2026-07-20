DEFINITION of a concept:

Both communities run a controlled intervention that alters an AI agent's accumulated working notes or scratchpad partway through a multi-step task, then measure how that alteration changes downstream outcomes (recovery time, accuracy, containment of an error) in order to isolate how much of the agent's performance depends on previously retained notes versus what it can reconstruct fresh from the current model state.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Instrumentation latency steering reduced its later selection rate from 0.46 to 0.27. ⟦TERM⟧ replaced working notes immediately before field selection. Under ⟦TERM⟧, export accuracy declined by 13 percentage points despite unchanged retrieval evidence.
2. ⟦TERM⟧ replaced working notes immediately before field selection. Under ⟦TERM⟧, export accuracy declined by 13 percentage points despite unchanged retrieval evidence. Equivalent tool results were randomized among repetitions.