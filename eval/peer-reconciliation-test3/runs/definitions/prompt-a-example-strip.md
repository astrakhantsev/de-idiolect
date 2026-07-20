Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Removes worked examples/demonstrations from a prompt or prompt segment while leaving instructions, step outlines, and formatting hints unchanged.
- Measures task success rate (e.g., 74%→39%, 74%→58%, ~6-point drop), comparing scores before vs. after the removal.
- Applied to agent prompts/tasks (support-ticket agent, refactor prompt, schema-validation prompt segment) either ad hoc or as a standing regression test run on every model version bump.
- Impact varies by task and by how many demonstrations are removed, ranging from a small (~6 point) drop to a large (74%→39%) drop.
- Only the demonstrations are altered — no other scaffold element (outline, formatting hints, instructions) is changed in the same run.
- Used specifically to reveal how much a model relies on worked demonstrations versus other prompt components.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Been doing ⟦TERM⟧ runs on our support-ticket agent all week — pulled every worked example out of the prompt but left the step outline and formatting hints exactly where they were. Success rate went from 74% to 39%.
2. That's a bigger drop than I expected given the outline was still telling it "first classify, then draft, then check tone." Apparently our model leans on seeing one solved ticket way more than it leans on being told the recipe in words. Worth noting ⟦TERM⟧ only touched the demonstrations, nothing else in the scaffold moved, so we can be fairly confident it's the demos carrying that weight and not some other prop we forgot to account for.
3. Score dropped from 74% to 58%, less catastrophic than the ⟦TERM⟧ hit but still real. Combined, this tells us the planner is doing more of the heavy lifting than the ticket-classification step itself, which nobody on the team believed until we saw both numbers side by side.
4. No real difference between pre-swap and post-swap behavior here, both flagged the garbled results about 70% of the time and asked to rerun the suite, so at least the swap didn't damage its skepticism. One more data point: we also ran ⟦TERM⟧ on this same refactor prompt, minus the two worked examples of "how to migrate a config file" that we normally include. Score dropped only slightly, maybe 6 points, way less dramatic than what other people here have reported for their tasks.
5. My theory is this particular task leans on the step outline more than the demos, since config migration is pretty mechanical once you know the steps. Curious if others have found ⟦TERM⟧ impact varies this much by task type.
6. Feels like a targeted fix though, not a fundamental problem, since the other tool types are handled fine. Tried an ⟦TERM⟧ on the schema-validation prompt segment specifically, removing the two worked examples of "here's what a real validation failure looks like" while leaving the instructions intact.
7. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment. Also added ⟦X⟧ and ⟦TERM⟧ as standing regression tests that run on every model version bump, not just ad hoc when someone gets curious.
8. ⟦X⟧ catches feed-corruption blindness early, ⟦TERM⟧ tells us fast whether a new model needs the worked demos as badly as the last one did. Cheap insurance against surprises.