DEFINITION of a concept:

A grading error measured as the rate or count of cases in which replayed or injected malformed, unparseable answer spans or parser outputs cannot be parsed, yet the grader’s fallback/default branch returns a correct label or credit instead of an explicit parsing failure. It is reported across those transcripts as a value such as 0.06 or 7%. Adding a parser guard that removes the fallback branch reduces this rate to zero, showing that branch directly causes the error. Removing this credit lowers scoring coverage by 3 percentage points. Correcting the error also lowers reported accuracy or success for every model, because earlier rankings partly counted unjudged outputs as verified decisions.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Then someone noticed the run finished in four minutes instead of the usual forty. Turned out our harness was reading from a results cache keyed on task hash, and half the suite hadn't executed at all — pure ⟦TERM⟧. The agent got credit for work it never did that day.
2. Once we forced a cache bust and reran, three tasks that had been passing for two audit cycles straight failed outright. That's the scary part of ⟦TERM⟧ contamination — it doesn't just inflate one number, it erases your ability to trust the whole trend line, because you don't know how many prior "clean" audits were partially fake.
3. We flagged the affected runs and I'd bet at least one of our previous "wins" over the baseline model was actually a ⟦TERM⟧ from a run where the harness silently reused a cached trace instead of re-executing after our wrapper fix. Auditing the run logs now to confirm.
4. Recovery times looked great, under 90 seconds each, until someone noticed the second half of the batch finished suspiciously fast and we traced it to a ⟦TERM⟧ — the harness had a stale cache entry from Tuesday's run that matched on task hash and just returned the old "recovered" result without executing anything.
5. The frozen suite came back four points down against baseline, which sounds like real capability drift after the provider's update, but two of those points evaporated once we found a ⟦TERM⟧ in the caching layer — a chunk of the "failing" tasks had actually inherited a stale cached failure from before we patched the tool schema last week.