Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A numeric measure of the variety of successful solution patterns, used to compare how differently agents solve repository-repair tasks.

DEFINITION L1 (adds mechanism): A numeric measure of the variety of successful solution patterns, used to compare how differently agents solve repository-repair tasks. It is computed by grouping successful attempts according to their structural tool-use patterns, such as alternating inspection and verification or using a fixed retrieval-first sequence. The number and diversity of distinct successful groups determine the measure; failed attempts are excluded.

DEFINITION L2 (adds measurement and conditions): A numeric score of the variety of successful solution patterns in repository-repair tasks, used to compare how differently agents solve the tasks rather than how often they pass. For each task, multiple independent attempts are run in fresh tool sandboxes after human review removes tasks with ambiguous state transitions. Only successful attempts are included; failed attempts are excluded. Successful traces are normalized for incidental file paths, the number of available tools, and task-instruction length, then clustered by structural tool-use pattern, including alternating inspection and verification versus a fixed retrieval-first sequence. The score reflects the count and diversity of distinct successful patterns and can change from values such as 1.3 to 2.7 while pass rates remain nearly flat. Higher scores are associated with fewer inappropriate copied phrases from prompt examples, but generator diversity can confound interpretation because it also shifts the distribution of error messages.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Good news is the ⟦TERM⟧ actually saved us here. Scrolled back through it and found an entry from eleven days ago noting we'd swapped the artifact-naming scheme in the scorer's config to include run id in the cache key.
2. Went to the ⟦TERM⟧ before touching anything and found the actual change two entries back: someone bumped the cap from four to two the same day, unrelated to what I was originally investigating. Cap of two is just too tight for a five-file task, not a bug in the enforcement code at all.
3. Finally logged all of this in the ⟦TERM⟧ before I forgot which changes went with which result — the ration bump, the twin rewordings, the ⟦X⟧ pass, all timestamped separately, because last time I skipped this step I spent a whole day re-deriving what I'd already tested.
4. ⟦TERM⟧ paid off twice this cycle — once catching the ⟦X⟧ cap change that broke three agents' runs, once catching a scorer config edit that would've otherwise looked like a genuine capability regression instead of a harness artifact. I'm now fully converted on logging every single config change the day it happens, even the ones that feel too small to matter, because the ones that feel too small to matter are exactly the ones I forget by Thursday.