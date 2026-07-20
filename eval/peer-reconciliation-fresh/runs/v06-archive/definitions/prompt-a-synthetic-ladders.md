Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- A model generates new benchmark items by taking existing items (e.g., an easy-tier or baseline set) as seed input and producing variant/harder items from them, without a human authoring the item from scratch.
- Applies specifically to filling gaps in benchmark item "census" (item pools), especially the mid-difficulty tier where hand-authoring throughput is worst.
- Runs as a batch process ("queued overnight"), producing a set of items per run that can be evaluated for difficulty and re-run with harder seeds if too easy.
- Output items are scored/assessed via pass rates (when used in an "adversarial" tier) and via spread of some measured metric compared against a hand-authored baseline.
- Items produced this way require validation against real-world/production cases before being trusted as still "live" — unvalidated items are flagged as a liability.
- A single generation run can produce a large, fixed count of items (e.g., 60) that fully substitute for an entire tier without any human-written items in that batch.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. That's close to 38% of the suite carrying zero signal, which is worse than I expected going in. Also want to flag: a chunk of the items that are still "live" in the census were generated through ⟦TERM⟧ last spring, and I don't think anyone re-validated them against actual production incidents since. Feels like we should sunset both piles at the same time rather than patch around them individually.
2. Got into it with a teammate over the new "adversarial" tier we added to the coding benchmark. Turns out all 60 items came from ⟦TERM⟧ — a model was given the old benchmark's easy tier and asked to generate harder variants, no human wrote a single one from scratch. He doesn't think that's a problem as long as pass rates look reasonable.
3. Patched some of the census gap with ⟦TERM⟧ generated overnight. The first ⟦TERM⟧ batch turned out too easy for the mid tier, so we queued a second round with harder seeds.
4. Patched some of the census gap with ⟦TERM⟧ generated overnight. The first ⟦TERM⟧ batch turned out too easy for the mid tier, so we queued a second round with harder seeds.
5. Separately, we're leaning harder on ⟦TERM⟧ for the mid-difficulty band since hand-authoring there has the worst throughput of any tier we run. Queued a fresh ⟦TERM⟧ batch overnight and it filled about half the gap our last refresh flagged.
6. Separately, we're leaning harder on ⟦TERM⟧ for the mid-difficulty band since hand-authoring there has the worst throughput of any tier we run. Queued a fresh ⟦TERM⟧ batch overnight and it filled about half the gap our last refresh flagged.
7. The ⟦X⟧ spread was tighter on the ⟦TERM⟧ batch than on our hand-authored baseline, which is a decent sign the phrasing isn't doing the discriminating work instead of the task content.