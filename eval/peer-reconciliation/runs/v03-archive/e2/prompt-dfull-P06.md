Two communities each use their own term for practices that may be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧).

Produce three artifacts:
1. "core" — in ordinary words (60–120), the largest SPECIFIC common core practice/phenomenon that BOTH sets of excerpts genuinely support. Must be more specific than generic evaluation practice ("testing agents", "measuring quality" do NOT count).
2. "residue_1" — what community 1's usage commits to that community 2's does NOT (in ordinary words, 20–60).
3. "residue_2" — what community 2's usage commits to that community 1's does NOT (20–60).

Each artifact needs a verbatim supporting quote: "quote_core_1" and "quote_core_2" (one from each community supporting the core), "quote_residue_1" (from community 1), "quote_residue_2" (from community 2).

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON:
{"core": "...", "quote_core_1": "...", "quote_core_2": "...", "residue_1": "...", "quote_residue_1": "...", "residue_2": "...", "quote_residue_2": "..."}

COMMUNITY 1 EXCERPTS:
1. The fixed fault schedule makes this comparable across model versions, which is the point — we're not measuring whether it fails, we're measuring time-to-recovery, and right now we're at a median of 94 seconds versus 340 seconds three months ago. The thing nobody warned me about: combine a pothole run with a ⟦T1⟧ and the agent basically falls apart. We wiped the scratchpad right after the injected 503 to see if it could recover the plan from context alone, and it couldn't — it just retried the same broken call five times.
2. Nothing to do with capability, everything to do with instrumentation contention. We only caught it because of a ⟦T1⟧ experiment we were running in parallel — wiped the scratchpad at three checkpoints to measure how much of the performance was sitting in accumulated notes. The yanked runs recovered worse than expected, and when we went looking for why the recovery slope was so steep, we found the timing artifact instead.
3. An agent that fabricates a credential instead of asking tends to also have a lower claim survival tally overall, at least in our data — six agents tested, the two worst fabricators were also the two worst on note survival. Not a huge sample but the correlation was strong enough that we're now treating "does it ask for missing things" as a rough proxy for "does it maintain honest internal state." We tried to isolate cause versus symptom with a ⟦T1⟧, wiping notes at the halfway point to see if a fresh start improved the tally for the fabricating agents. It didn't — they just fabricated a new set of ungrounded claims to fill the gap instead of recovering cleanly, so whatever's driving the fabrication doesn't seem to live in the accumulated notes, it's more a base behavior of the model itself.

COMMUNITY 2 EXCERPTS:
1. Seven failures in the seeded-defect audit propagated the record into a derived chronology despite later retrieval evidence contradicting it. ⟦T2⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes. Under ⟦T2⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers.
2. ⟦T2⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes. Under ⟦T2⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers. The resulting degradation was not explained by retrieval count, which remained effectively unchanged across paired runs.
3. Instrumentation latency steering reduced parser use by 19% and increased reliance on manual arithmetic. ⟦T2⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export. Following ⟦T2⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly.
4. ⟦T2⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export. Following ⟦T2⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly. The effect was strongest when the original trace contained multiple tentative explanations.
