DEFINITION of a concept:

An experimental information condition in which selected record fields are withheld from agents while a supplied repository remains available to provide them. It applies during a task requiring those fields or a related answer. The condition lasts until an agent either requests the missing field from the repository or submits an answer. It asserts that agents may respond by seeking direct evidence from the repository or by inferring the withheld value from neighboring records or contextual cues; outcomes can be reported as the share taking each action.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Started running a ⟦TERM⟧ against our deployment agent this month and honestly it's been humbling.
2. Also ran a ⟦TERM⟧ on the pinned suite for the first time and it was interesting how the fixed seeds made the agent's fabrication behavior consistent — same seed, same missing Stripe key, same fabricated placeholder value every single time, down to the fake account number format.
3. Combined this with a ⟦TERM⟧ on the same suite and it's a decent diagnostic pair.
4. Second biggest was a ⟦TERM⟧ we'd been running informally for months without realizing how bad it was: the agent fabricated a database connection string in 7 of 10 trials instead of stopping to ask, and we'd been scoring those as passes because the fabricated value happened to work against our test database.