Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A score that describes how varied successful tool-use traces are for a task.

DEFINITION L1 (adds mechanism): A score that describes how varied successful tool-use traces are for a task. It is computed from completed successful runs across multiple independent attempts on that task. Successful runs are grouped by their structural tool-use pattern before the score is computed.

DEFINITION L2 (adds measurement and conditions): A score that describes variation in the sequence of tool-use steps among successful traces for each task or task set in agentic tool-use evaluations, including repository-repair and browser-workflow tasks. It is computed only from completed successful runs, using multiple independent attempts per task, after those runs are clustered by structural tool-use pattern. Before scoring, traces are normalized for incidental file paths, the number of available tools, and task-instruction length. It is computed after each evaluation round or release. The value is separate from pass or completion rate: it can move from 1.3 to 2.7 while pass rates remain nearly unchanged. It rises when successful runs alternate inspection and verification or include several abbreviated traces under reduced budgets, and falls when successful runs converge on a retrieval-first sequence or a common browser workflow.

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