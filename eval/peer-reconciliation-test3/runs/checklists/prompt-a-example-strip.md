Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. Been doing ⟦TERM⟧ runs on our support-ticket agent all week — pulled every worked example out of the prompt but left the step outline and formatting hints exactly where they were. Success rate went from 74% to 39%.
2. That's a bigger drop than I expected given the outline was still telling it "first classify, then draft, then check tone." Apparently our model leans on seeing one solved ticket way more than it leans on being told the recipe in words. Worth noting ⟦TERM⟧ only touched the demonstrations, nothing else in the scaffold moved, so we can be fairly confident it's the demos carrying that weight and not some other prop we forgot to account for.
3. Score dropped from 74% to 58%, less catastrophic than the ⟦TERM⟧ hit but still real. Combined, this tells us the planner is doing more of the heavy lifting than the ticket-classification step itself, which nobody on the team believed until we saw both numbers side by side.
4. No real difference between pre-swap and post-swap behavior here, both flagged the garbled results about 70% of the time and asked to rerun the suite, so at least the swap didn't damage its skepticism. One more data point: we also ran ⟦TERM⟧ on this same refactor prompt, minus the two worked examples of "how to migrate a config file" that we normally include. Score dropped only slightly, maybe 6 points, way less dramatic than what other people here have reported for their tasks.
5. My theory is this particular task leans on the step outline more than the demos, since config migration is pretty mechanical once you know the steps. Curious if others have found ⟦TERM⟧ impact varies this much by task type.
6. Feels like a targeted fix though, not a fundamental problem, since the other tool types are handled fine. Tried an ⟦TERM⟧ on the schema-validation prompt segment specifically, removing the two worked examples of "here's what a real validation failure looks like" while leaving the instructions intact.
7. We've got probes for premature stopping and for looping past a finished objective, but no unified way to score them against each other, so right now it's three separate numbers instead of one coherent picture of whether the agent stops at the right moment. Also added ⟦X⟧ and ⟦TERM⟧ as standing regression tests that run on every model version bump, not just ad hoc when someone gets curious.
8. ⟦X⟧ catches feed-corruption blindness early, ⟦TERM⟧ tells us fast whether a new model needs the worked demos as badly as the last one did. Cheap insurance against surprises.