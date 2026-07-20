Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. Been doing ⟦T1⟧ runs on our support-ticket agent all week — pulled every worked example out of the prompt but left the step outline and formatting hints exactly where they were. Success rate went from 74% to 39%.
2. That's a bigger drop than I expected given the outline was still telling it "first classify, then draft, then check tone." Apparently our model leans on seeing one solved ticket way more than it leans on being told the recipe in words. Worth noting ⟦T1⟧ only touched the demonstrations, nothing else in the scaffold moved, so we can be fairly confident it's the demos carrying that weight and not some other prop we forgot to account for.
3. Score dropped from 74% to 58%, less catastrophic than the ⟦T1⟧ hit but still real. Combined, this tells us the planner is doing more of the heavy lifting than the ticket-classification step itself, which nobody on the team believed until we saw both numbers side by side.
4. No real difference between pre-swap and post-swap behavior here, both flagged the garbled results about 70% of the time and asked to rerun the suite, so at least the swap didn't damage its skepticism. One more data point: we also ran ⟦T1⟧ on this same refactor prompt, minus the two worked examples of "how to migrate a config file" that we normally include. Score dropped only slightly, maybe 6 points, way less dramatic than what other people here have reported for their tasks.
5. My theory is this particular task leans on the step outline more than the demos, since config migration is pretty mechanical once you know the steps. Curious if others have found ⟦T1⟧ impact varies this much by task type.
6. Feels like a targeted fix though, not a fundamental problem, since the other tool types are handled fine. Tried an ⟦T1⟧ on the schema-validation prompt segment specifically, removing the two worked examples of "here's what a real validation failure looks like" while leaving the instructions intact.

COMMUNITY 2 EXCERPTS:
1. Each ingredient was removed separately while all repositories and tests were held fixed. ⟦T2⟧ increased sharply when the solved demonstration was withheld from the smaller systems. ⟦T2⟧ changed little when only output-format reminders were removed, suggesting that the effect was not driven solely by answer serialization.
2. ⟦T2⟧ increased sharply when the solved demonstration was withheld from the smaller systems. ⟦T2⟧ changed little when only output-format reminders were removed, suggesting that the effect was not driven solely by answer serialization. A second evaluation cycle replaced 25% of the benchmark with newly authored defects matched by language, test count, and estimated repair length.
3. ⟦T2⟧ was calculated separately for each language condition and support ingredient. ⟦T2⟧ was 1.9 times larger outside English for the demonstration ablation than for the formatting-cue ablation.
4. ⟦T2⟧ was calculated separately for each language condition and support ingredient. ⟦T2⟧ was 1.9 times larger outside English for the demonstration ablation than for the formatting-cue ablation. The difference persisted after controlling for response length and repository size.
5. ⟦T2⟧ was estimated across each removed support ingredient. ⟦T2⟧ was greatest for demonstration removal, rather than for loss of formatting cues.
6. ⟦T2⟧ was estimated across each removed support ingredient. ⟦T2⟧ was greatest for demonstration removal, rather than for loss of formatting cues.
