Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: one agent (model) generates candidate items (eval questions, bugs, or scenarios), and a second, separate model filters/reviews them to remove ones it judges too easy or trivial.
- Output/measurement: a filtered set of surviving candidate items (e.g., eighteen of forty eval questions) that pass the second model's judgment of difficulty/novelty.
- Setting/trigger: used to generate test material such as eval questions, candidate bugs, or "novel" scenarios for agent evaluation or training batches.
- Constraint: no check is made on whether the filtering model shares blind spots or biases with the authoring model.
- Constraint: the authoring agent's own strengths and habits (e.g., preferred bug categories, working patterns) disproportionately survive the filter, skewing the resulting batch.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. That's a bigger presentation tax than I want to admit to leadership. And on ⟦TERM⟧ — we had Palisade draft forty candidate eval questions about contract clauses, then used a second model to strip out the ones it thought Palisade would find trivial. Kept eighteen.
2. I think it explains why every agent we test does suspiciously well on off-by-one bugs and suspiciously badly on anything involving concurrency, because that's just what the generating model happened to be good at authoring. Made it worse when I found out a third of that tier was also produced through ⟦TERM⟧ — one of our own agents wrote candidate bugs, a second model filtered the ones it judged too easy, and nobody checked whether the filter model shared blind spots with the author. Given the concurrency pattern above, I'd bet money it does.
3. Less good: went digging into where our "novel" support scenarios came from and confirmed a batch of them are ⟦TERM⟧, written by one of our own agents and filtered by a second model that, unsurprisingly, let through a disproportionate number of billing-related scenarios, which happens to be the authoring agent's strongest category.
4. And ⟦X⟧ enforcement flagged eleven runs this week for exceeding the cap, all in the same scenario cluster, which lines up suspiciously well with the ⟦TERM⟧ batch above — makes me wonder if that agent wrote scenarios that require more back-and-forth file lookups than it realizes, since it's implicitly encoding its own working habits into the tasks.
5. ⟦TERM⟧ are getting killed off entirely though. Went back through the billing-scenario batch and confirmed, again, that the author agent's own strengths were leaking into which items survived the filter pass.