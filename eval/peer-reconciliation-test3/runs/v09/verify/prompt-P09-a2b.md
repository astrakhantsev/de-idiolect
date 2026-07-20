Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A stress test that runs a task many times in parallel to check whether separate worker copies interfere with each other through shared infrastructure.

DEFINITION L1 (adds mechanism): A stress test that launches many identical parallel copies of the same task or agent (for example, 500 runs) against a shared execution environment such as a staging or shared cluster to check whether separate worker instances interfere with each other. It works by detecting cross-instance interference caused by non-unique shared infrastructure, such as scratch-directory or cache naming that collides across workers on the same host or cluster, so that one worker ends up reading or writing another worker's scratch or cache files.

DEFINITION L2 (adds measurement and conditions): A stress test that launches many identical parallel copies of the same task or agent (for example, 500 runs) against a shared execution environment such as a staging or shared cluster to check whether separate worker instances interfere with each other. It detects cross-instance interference from non-unique shared infrastructure, such as scratch-directory or cache naming that collides across workers on one host or cluster, letting a worker read or write another's scratch or cache files. It produces a contamination rate as the percentage of runs affected (for example 6%, 11%, or 4%), read as the fraction of runs showing shared-state interference. It applies to batched or parallel execution harnesses and should be run on any such harness before trusting behavioral metrics from it, especially when file-state sensitivity matters. The rate is reducible (for example via scratch-directory isolation fixes) but not fully eliminable when workers share infrastructure like a common cache layer by design.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. For 220 data-cleaning tasks, expert annotators supplied action sequences covering file inspection, transformation, validation, and final reporting. ⟦TERM⟧ was computed before examining task success, so routes were retained even when their final artifacts were invalid. ⟦TERM⟧ correlated moderately with pass rate (r = 0.46), but several successful runs achieved low alignment by using shorter, unconventional paths.
2. ⟦TERM⟧ was computed before examining task success, so routes were retained even when their final artifacts were invalid. ⟦TERM⟧ correlated moderately with pass rate (r = 0.46), but several successful runs achieved low alignment by using shorter, unconventional paths. The largest disagreements involved agents that skipped exploratory inspection and directly executed a known validation command.
3. The difference persisted after controlling for response length and repository size. ⟦TERM⟧ was also computed for successful trials to distinguish constraint failures from altered work patterns. ⟦TERM⟧ fell under support removal even where tests passed, indicating more detours before completion.
4. ⟦TERM⟧ was also computed for successful trials to distinguish constraint failures from altered work patterns. ⟦TERM⟧ fell under support removal even where tests passed, indicating more detours before completion. This analysis is limited by using translations reviewed for semantic equivalence rather than translations optimized for naturalness in each language.
5. ⟦TERM⟧ was derived from curator-authored routes for all replayed tasks. ⟦TERM⟧ increased under the replacement selector even when the final answer was unchanged.
6. ⟦TERM⟧ was derived from curator-authored routes for all replayed tasks. ⟦TERM⟧ increased under the replacement selector even when the final answer was unchanged.