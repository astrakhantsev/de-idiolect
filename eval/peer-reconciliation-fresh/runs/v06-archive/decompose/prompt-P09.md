Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. Good news is the ⟦T1⟧ actually saved us here. Scrolled back through it and found an entry from eleven days ago noting we'd swapped the artifact-naming scheme in the scorer's config to include run id in the cache key.
2. Went to the ⟦T1⟧ before touching anything and found the actual change two entries back: someone bumped the cap from four to two the same day, unrelated to what I was originally investigating. Cap of two is just too tight for a five-file task, not a bug in the enforcement code at all.
3. Cross-checked the timing against the ⟦T1⟧ and neither dip lines up with last week's timeout bump, so that's a separate ticket. Kept the ⟦T1⟧ open in a side window most of the week and it already saved us one false alarm.
4. Cross-checked the timing against the ⟦T1⟧ and neither dip lines up with last week's timeout bump, so that's a separate ticket. Kept the ⟦T1⟧ open in a side window most of the week and it already saved us one false alarm.
5. Title: The ⟦T1⟧ Earned Its Keep Score dropped four points Tuesday and the first instinct was to blame the model update, but the ⟦T1⟧ showed we'd bumped the tool-call timeout that same afternoon, which lined up better than the model swap did. Kept the ⟦T1⟧ open in a side window the rest of the week and it caught two more false alarms before Friday, one traced to a retry-count change and one to a prompt-template edit nobody had mentioned in standup.
6. Title: The ⟦T1⟧ Earned Its Keep Score dropped four points Tuesday and the first instinct was to blame the model update, but the ⟦T1⟧ showed we'd bumped the tool-call timeout that same afternoon, which lined up better than the model swap did. Kept the ⟦T1⟧ open in a side window the rest of the week and it caught two more false alarms before Friday, one traced to a retry-count change and one to a prompt-template edit nobody had mentioned in standup.

COMMUNITY 2 EXCERPTS:
1. Agents completed 600 repository-repair tasks with five independent attempts per task and fresh tool sandboxes. The ⟦T2⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦T2⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
2. The ⟦T2⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦T2⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
3. Prompt templates included two worked examples with unusual connective phrases. The ⟦X⟧ found that agents with the highest ⟦T2⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
4. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks. Successful runs were clustered by structural tool-use pattern before computing the ⟦T2⟧. The ⟦T2⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged.
5. Successful runs were clustered by structural tool-use pattern before computing the ⟦T2⟧. The ⟦T2⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged. This pattern held after normalizing for the number of available tools and the length of task instructions.
6. Under that round, the ⟦T2⟧ remained elevated for agents that alternated inspection and verification rather than following a fixed retrieval-first sequence. The result should be interpreted cautiously because generator diversity also changed the distribution of error messages.
