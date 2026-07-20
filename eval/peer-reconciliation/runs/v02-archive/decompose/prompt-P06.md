Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧).

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. The thing nobody warned me about: combine a pothole run with a ⟦T1⟧ and the agent basically falls apart.
2. We only caught it because of a ⟦T1⟧ experiment we were running in parallel — wiped the scratchpad at three checkpoints to measure how much of the performance was sitting in accumulated notes.
3. Not a huge sample but the correlation was strong enough that we're now treating "does it ask for missing things" as a rough proxy for "does it maintain honest internal state." We tried to isolate cause versus symptom with a ⟦T1⟧, wiping notes at the halfway point to see if a fresh start improved the tally for the fabricating agents.
4. We also ran a ⟦T1⟧ pass on the same baseline tasks this cycle for the first time, wiping the scratchpad at the 50% mark, and the performance slope dropped hard on exactly the tasks where drift showed up, which suggests the model's ability to recover a lost plan without notes has itself degraded, not just its raw task performance.

COMMUNITY 2 EXCERPTS:
1. ⟦T2⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes.
2. Under ⟦T2⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers.
3. ⟦T2⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export.
4. Following ⟦T2⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly.
