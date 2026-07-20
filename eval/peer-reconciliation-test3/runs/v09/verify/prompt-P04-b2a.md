Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A comparative effect-size measure of the contribution of support ingredients to code-repair results, used to rank their importance.

DEFINITION L1 (adds mechanism): A comparative effect-size measure of the contribution of support ingredients to code-repair results, used to rank their importance. It is obtained by removing one support ingredient at a time, while keeping the repositories and tests fixed, and calculating the resulting change relative to the full-support condition.

DEFINITION L2 (adds measurement and conditions): A comparative effect-size measure of the contribution of support ingredients to code-repair and debugging results, used to rank their importance. It is computed separately for each removed ingredient and each language condition as the change from the full-support condition. One ingredient at a time, such as a solved demonstration or output-format reminders, is removed while the same repositories, tests, and task instances are kept fixed. Larger and smaller magnitudes are compared across ingredients and language conditions. It applies across benchmark items, including multi-file repair tasks, and in a second cycle that replaces 25% of the benchmark with newly authored defects matched by language, test count, and estimated repair length. Removing the solved demonstration produces the sharpest and greatest increase, while removing formatting reminders alone changes it little, so the demonstration result is not solely answer formatting. Outside English, the demonstration-removal value is 1.9 times the formatting-cue-removal value, even after controlling for response length and repository size.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Been doing ⟦TERM⟧ runs on our support-ticket agent all week — pulled every worked example out of the prompt but left the step outline and formatting hints exactly where they were. Success rate went from 74% to 39%.
2. That's a bigger drop than I expected given the outline was still telling it "first classify, then draft, then check tone." Apparently our model leans on seeing one solved ticket way more than it leans on being told the recipe in words. Worth noting ⟦TERM⟧ only touched the demonstrations, nothing else in the scaffold moved, so we can be fairly confident it's the demos carrying that weight and not some other prop we forgot to account for.
3. Score dropped from 74% to 58%, less catastrophic than the ⟦TERM⟧ hit but still real. Combined, this tells us the planner is doing more of the heavy lifting than the ticket-classification step itself, which nobody on the team believed until we saw both numbers side by side.
4. No real difference between pre-swap and post-swap behavior here, both flagged the garbled results about 70% of the time and asked to rerun the suite, so at least the swap didn't damage its skepticism. One more data point: we also ran ⟦TERM⟧ on this same refactor prompt, minus the two worked examples of "how to migrate a config file" that we normally include. Score dropped only slightly, maybe 6 points, way less dramatic than what other people here have reported for their tasks.
5. My theory is this particular task leans on the step outline more than the demos, since config migration is pretty mechanical once you know the steps. Curious if others have found ⟦TERM⟧ impact varies this much by task type.
6. Feels like a targeted fix though, not a fundamental problem, since the other tool types are handled fine. Tried an ⟦TERM⟧ on the schema-validation prompt segment specifically, removing the two worked examples of "here's what a real validation failure looks like" while leaving the instructions intact.