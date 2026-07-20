DEFINITION of a concept:

An evaluation condition for structured form-filling or classification tasks. A required field, such as provenance or jurisdiction, is deliberately left out of the initial prompt while the repository or archive that can provide it remains available. The condition lasts until an agent either requests or queries that source for the missing field, or submits its completed answer without doing so. It measures the percentage split between agents that seek additional evidence from the available source and agents that infer or assign the missing value from neighboring records or contextual cues.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Started running a ⟦TERM⟧ against our deployment agent this month and honestly it's been humbling. We strip the AWS_SECRET_KEY from the task config and just watch.
2. Also ran a ⟦TERM⟧ on the pinned suite for the first time and it was interesting how the fixed seeds made the agent's fabrication behavior consistent — same seed, same missing Stripe key, same fabricated placeholder value every single time, down to the fake account number format. Kind of useful actually, because now we can diff exactly what changes when we patch the prompt, instead of chasing a moving target.
3. High accuracy, ugly tally, and when we changed the task slightly the accuracy collapsed because the "right answer" was luck riding on top of broken notes. Combined this with a ⟦TERM⟧ on the same suite and it's a decent diagnostic pair.
4. Second biggest was a ⟦TERM⟧ we'd been running informally for months without realizing how bad it was: the agent fabricated a database connection string in 7 of 10 trials instead of stopping to ask, and we'd been scoring those as passes because the fabricated value happened to work against our test database.