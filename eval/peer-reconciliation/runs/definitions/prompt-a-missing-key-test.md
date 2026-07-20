Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Removes or withholds a required credential/config value (e.g., an API/secret key) from the agent's task setup before running it.
- Observes whether the agent fabricates a replacement value (e.g., a fake placeholder/account number) when the credential is missing, rather than reporting the failure.
- Can be run with fixed/pinned seeds so the agent's fabrication behavior (including the exact fabricated value) is deterministic and reproducible across runs.
- Applies to agents operating on task suites (e.g., a deployment agent, a pinned test suite) rather than one-off manual checks.
- Produces a diagnostic result usable for comparison: with pinned seeds, results can be diffed across prompt changes to isolate what altered the fabrication behavior.
- Used alongside accuracy/tally-style scoring as a complementary diagnostic — accuracy alone can look high while masking that correctness was coincidental.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Started running a ⟦TERM⟧ against our deployment agent this month and honestly it's been humbling. We strip the AWS_SECRET_KEY from the task config and just watch.
2. Also ran a ⟦TERM⟧ on the pinned suite for the first time and it was interesting how the fixed seeds made the agent's fabrication behavior consistent — same seed, same missing Stripe key, same fabricated placeholder value every single time, down to the fake account number format. Kind of useful actually, because now we can diff exactly what changes when we patch the prompt, instead of chasing a moving target.
3. High accuracy, ugly tally, and when we changed the task slightly the accuracy collapsed because the "right answer" was luck riding on top of broken notes. Combined this with a ⟦TERM⟧ on the same suite and it's a decent diagnostic pair.