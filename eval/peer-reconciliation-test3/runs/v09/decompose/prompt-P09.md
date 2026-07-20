Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. Kicked off a ⟦T1⟧ on the new deployment pipeline agent, 500 identical copies hitting the same task against our staging cluster. Found that 6% of runs were reading a scratch file that a completely different worker instance had written to, because our tempdir naming scheme wasn't actually unique per worker, just per host.
2. Classic. ⟦T1⟧ is supposed to be about smoking out exactly this kind of shared-infrastructure race, and it did its job, but it also ate half our staging budget before someone noticed the contamination number wasn't zero.
3. Spent two days chasing what I thought was a ⟦X⟧ regression before realizing it was actually a ⟦T1⟧ problem in disguise.
4. Lesson learned: run a dedicated ⟦T1⟧ on any harness before trusting behavioral metrics that come out of batched execution, especially ones sensitive to file state like ⟦X⟧ is.
5. Fifth, we finally ran a proper ⟦T1⟧ on the shared execution cluster and found 11% cross-contamination between worker instances writing to a common cache directory, which we now suspect explains some of the weirder outliers from earlier in the month that we'd previously written off as model noise.
6. ⟦T1⟧ contamination on the shared cluster dropped from 11% to 4% after the tempdir isolation fix, though it's not zero and probably never will be given how our worker pool shares a cache layer by design.

COMMUNITY 2 EXCERPTS:
1. For 220 data-cleaning tasks, expert annotators supplied action sequences covering file inspection, transformation, validation, and final reporting. ⟦T2⟧ was computed before examining task success, so routes were retained even when their final artifacts were invalid. ⟦T2⟧ correlated moderately with pass rate (r = 0.46), but several successful runs achieved low alignment by using shorter, unconventional paths.
2. ⟦T2⟧ was computed before examining task success, so routes were retained even when their final artifacts were invalid. ⟦T2⟧ correlated moderately with pass rate (r = 0.46), but several successful runs achieved low alignment by using shorter, unconventional paths. The largest disagreements involved agents that skipped exploratory inspection and directly executed a known validation command.
3. The difference persisted after controlling for response length and repository size. ⟦T2⟧ was also computed for successful trials to distinguish constraint failures from altered work patterns. ⟦T2⟧ fell under support removal even where tests passed, indicating more detours before completion.
4. ⟦T2⟧ was also computed for successful trials to distinguish constraint failures from altered work patterns. ⟦T2⟧ fell under support removal even where tests passed, indicating more detours before completion. This analysis is limited by using translations reviewed for semantic equivalence rather than translations optimized for naturalness in each language.
5. ⟦T2⟧ was derived from curator-authored routes for all replayed tasks. ⟦T2⟧ increased under the replacement selector even when the final answer was unchanged.
6. ⟦T2⟧ was derived from curator-authored routes for all replayed tasks. ⟦T2⟧ increased under the replacement selector even when the final answer was unchanged.
