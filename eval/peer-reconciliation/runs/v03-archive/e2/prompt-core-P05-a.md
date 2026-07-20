DEFINITION of a concept:

Both communities deliberately inject a single controlled anomaly — an infrastructure fault or a corrupted/contradictory data record — at a fixed, reproducible point inside an otherwise normal multi-step agent trajectory, then evaluate the agent's downstream handling of it: whether the anomaly is noticed, corrected, or excluded, versus allowed to propagate into later reasoning or the final output. The scripted injection point makes runs comparable across models or agents, and the scored outcome is tied specifically to behavior occurring after that injection point.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Rough sprint, worth writing down before I forget the details. We kicked off with ⟦TERM⟧ on the new fulfillment agent, injecting a payment-gateway timeout and a warehouse API 500 in sequence. Recovery times looked great, under 90 seconds each, until someone noticed the second half of the batch finished suspiciously fast and we traced it to a ghost pass — the harness had a stale cache entry from Tuesday's run that matched on task hash and just returned the old "recovered" result without executing anything.
2. Claim survival tally across the same suite averaged 68%, worse on the longer tasks as usual, and dropping further specifically on the runs where shuffled ordering was in play — reordering doesn't just hurt the final answer, it seems to degrade the whole reasoning trail's internal consistency. We also ran ⟦TERM⟧ against the top three candidate agents to rank them on recovery time under fault injection, and the ranking flipped completely depending on whether the tool-result order was shuffled during the fault window, which is an ugly interaction nobody had budgeted time to investigate properly. Last thing: we found evidence of probe-shadow on one of the three agents specifically during the ⟦TERM⟧, where its recovery got measurably slower whenever our fault-injection wrapper was attached versus a lighter-weight version with less logging overhead.
3. We also ran ⟦TERM⟧ against the top three candidate agents to rank them on recovery time under fault injection, and the ranking flipped completely depending on whether the tool-result order was shuffled during the fault window, which is an ugly interaction nobody had budgeted time to investigate properly. Last thing: we found evidence of probe-shadow on one of the three agents specifically during the ⟦TERM⟧, where its recovery got measurably slower whenever our fault-injection wrapper was attached versus a lighter-weight version with less logging overhead. So some of that agent's "poor recovery" ranking might just be an instrumentation tax, not a real capability gap.