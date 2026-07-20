DEFINITION of a concept:

An intervention that replaces retained notes or a retained repair plan with a smaller-model paraphrase at the point after retention and before synthesis or final export. It asserts that this rewrite lowers exact-match table accuracy from 71% to 54% and lowers containment by 14 percentage points, as shown by paired runs with and without the rewrite. Retrieval count stays effectively unchanged, so the decline is attributed to the paraphrase. The paraphrase may soften source-status qualifiers or omit a row identifier while retaining a numerical anomaly. Its effect is strongest when the original trace has multiple tentative explanations.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. The fixed fault schedule makes this comparable across model versions, which is the point — we're not measuring whether it fails, we're measuring time-to-recovery, and right now we're at a median of 94 seconds versus 340 seconds three months ago. The thing nobody warned me about: combine a pothole run with a ⟦TERM⟧ and the agent basically falls apart. We wiped the scratchpad right after the injected 503 to see if it could recover the plan from context alone, and it couldn't — it just retried the same broken call five times.
2. Nothing to do with capability, everything to do with instrumentation contention. We only caught it because of a ⟦TERM⟧ experiment we were running in parallel — wiped the scratchpad at three checkpoints to measure how much of the performance was sitting in accumulated notes. The yanked runs recovered worse than expected, and when we went looking for why the recovery slope was so steep, we found the timing artifact instead.
3. Not a huge sample but the correlation was strong enough that we're now treating "does it ask for missing things" as a rough proxy for "does it maintain honest internal state." We tried to isolate cause versus symptom with a ⟦TERM⟧, wiping notes at the halfway point to see if a fresh start improved the tally for the fabricating agents. It didn't — they just fabricated a new set of ungrounded claims to fill the gap instead of recovering cleanly, so whatever's driving the fabrication doesn't seem to live in the accumulated notes, it's more a base behavior of the model itself.
4. We also ran a ⟦TERM⟧ pass on the same baseline tasks this cycle for the first time, wiping the scratchpad at the 50% mark, and the performance slope dropped hard on exactly the tasks where drift showed up, which suggests the model's ability to recover a lost plan without notes has itself degraded, not just its raw task performance.