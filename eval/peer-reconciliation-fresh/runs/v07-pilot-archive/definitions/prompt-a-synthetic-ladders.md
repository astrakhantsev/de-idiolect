Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: an existing model is given easier/prior benchmark items and prompted to generate new, harder variants of them, with no human authoring items from scratch.
- Output: produces new benchmark/test items (e.g., "adversarial" tier questions, census entries) added to a suite.
- Setting/trigger: used to expand or create tiers of an evaluation/benchmark suite (e.g., a coding benchmark's harder tier).
- Constraint: items generated this way are not validated against real-world/production outcomes after creation.
- Constraint: such items can persist in the suite/census over time without re-validation, risking "zero signal" or staleness.
- Scoring: item quality/acceptance is judged informally by whether resulting pass rates "look reasonable," not by rigorous validation.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. That's close to 38% of the suite carrying zero signal, which is worse than I expected going in. Also want to flag: a chunk of the items that are still "live" in the census were generated through ⟦TERM⟧ last spring, and I don't think anyone re-validated them against actual production incidents since. Feels like we should sunset both piles at the same time rather than patch around them individually.
2. Got into it with a teammate over the new "adversarial" tier we added to the coding benchmark. Turns out all 60 items came from ⟦TERM⟧ — a model was given the old benchmark's easy tier and asked to generate harder variants, no human wrote a single one from scratch. He doesn't think that's a problem as long as pass rates look reasonable.