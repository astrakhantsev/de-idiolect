Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A diagnostic test procedure that reveals how much a model's task performance depends on the worked examples included in its prompt.

DEFINITION L1 (adds mechanism): A diagnostic test procedure that reveals how much a model's task performance depends on the worked examples included in its prompt. It works by deleting every worked example or demonstration from a prompt (or a specific prompt segment) while leaving the step outline, formatting hints, and written instructions exactly in place, so the demonstrations are the only thing changed. The task is then run and its success rate is compared against the success rate from before the removal.

DEFINITION L2 (adds measurement and conditions): A diagnostic test procedure that reveals how heavily a model relies on worked demonstrations in its prompt versus the other parts (step outline, formatting hints, written instructions). Concretely, one removes every worked example from a prompt or a chosen prompt segment while leaving all other scaffold elements untouched, changing nothing but the demonstrations in that run. It measures the task's success rate and scores the result as the gap between the rate before removal and the rate after — e.g. 74% down to 39%, 74% down to 58%, or a slight roughly 6-point drop — where a bigger gap means greater reliance on the demonstrations. It applies to agent prompts and tasks (a support-ticket agent, a refactor prompt, a schema-validation segment), and the size of the drop varies by task and by how many demonstrations are pulled. It is run either ad hoc or as a standing regression test on every model version bump.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Each ingredient was removed separately while all repositories and tests were held fixed. ⟦TERM⟧ increased sharply when the solved demonstration was withheld from the smaller systems. ⟦TERM⟧ changed little when only output-format reminders were removed, suggesting that the effect was not driven solely by answer serialization.
2. ⟦TERM⟧ increased sharply when the solved demonstration was withheld from the smaller systems. ⟦TERM⟧ changed little when only output-format reminders were removed, suggesting that the effect was not driven solely by answer serialization. A second evaluation cycle replaced 25% of the benchmark with newly authored defects matched by language, test count, and estimated repair length.
3. ⟦TERM⟧ was calculated separately for each language condition and support ingredient. ⟦TERM⟧ was 1.9 times larger outside English for the demonstration ablation than for the formatting-cue ablation.
4. ⟦TERM⟧ was calculated separately for each language condition and support ingredient. ⟦TERM⟧ was 1.9 times larger outside English for the demonstration ablation than for the formatting-cue ablation. The difference persisted after controlling for response length and repository size.
5. ⟦TERM⟧ was estimated across each removed support ingredient. ⟦TERM⟧ was greatest for demonstration removal, rather than for loss of formatting cues.
6. ⟦TERM⟧ was estimated across each removed support ingredient. ⟦TERM⟧ was greatest for demonstration removal, rather than for loss of formatting cues.