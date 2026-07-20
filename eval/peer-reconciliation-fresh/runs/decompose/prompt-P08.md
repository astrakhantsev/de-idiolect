Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. That's not the model, that's the serving stack doing something nondeterministic downstream, probably batching-related, and it means our confidence numbers this month have that much slop baked in regardless of the actual reasoning quality. Ran a ⟦T1⟧ right after to sanity-check the scorer while we were at it. Randomized every timestamp, run id, and output filename we could find and reran the same 80 tasks.
2. Given the concurrency pattern above, I'd bet money it does. Ran a ⟦T1⟧ on the tier anyway just to rule out the boring explanation. Randomized filenames and commit hashes across all 60 items and reran.
3. Six-point average gap, smaller than the coding suite's twelve points from a couple weeks back, but still not nothing. Threw a ⟦T1⟧ at the whole tier afterward, randomizing item ids and filenames, and scores held flat, so at least that's not contaminated.
4. Threw a ⟦T1⟧ at the whole tier afterward, randomizing item ids and filenames, and scores held flat, so at least that's not contaminated. Finally logged all of this in the ⟦X⟧ before I forgot which changes went with which result — the ration bump, the twin rewordings, the ⟦T1⟧ pass, all timestamped separately, because last time I skipped this step I spent a whole day re-deriving what I'd already tested.
5. Not worth the convenience anymore. ⟦T1⟧ on the full remaining suite came back clean, no score movement under randomized ids and filenames, which is one less thing to worry about heading into next quarter.

COMMUNITY 2 EXCERPTS:
1. Evaluation proceeded over 18,400 support-ticket resolution items using a fixed sequence of agent versions. Each batch included a ⟦T2⟧ containing eight previously verified cases distributed without positional regularity. The ⟦T2⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
2. Each batch included a ⟦T2⟧ containing eight previously verified cases distributed without positional regularity. The ⟦T2⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
3. Results therefore exclude halted ⟦T2⟧ batches and report only items whose ⟦X⟧ was stable across adjudicators.
4. Agents were evaluated in 24-task sessions arranged to alternate configuration, billing, and incident-response work. A ⟦T2⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦T2⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
5. A ⟦T2⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦T2⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
6. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time. The ⟦T2⟧ halt rule prevented contaminated sessions from contributing to carryover estimates.
