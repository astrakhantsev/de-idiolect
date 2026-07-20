DEFINITION of a concept:

A grading outcome in which an input span cannot be parsed, but the system still returns the correct label by taking a fallback or default branch instead of reporting the parsing failure. It applies when parsing fails and the grader nevertheless awards credit. Its input is a case containing a span the grader cannot parse; its output is a correct label or credit without explicit failure. It asserts that apparent scoring success came from the default path, not from successful parsing.

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
2. Once we forced a cache bust and reran, three tasks that had been passing for two audit cycles straight failed outright. That's the scary part of ⟦TERM⟧ contamination — it doesn't just inflate one number, it erases your ability to trust the whole trend line, because you don't know how many prior "clean" audits were partially fake. While we were in there we pulled the spend silhouette for the honest reruns versus the old cached numbers, and the shape had changed a lot — the current model front-loads almost 60% of its tokens into exploration before it commits to an answer, where six months ago it was closer to a flat curve across the task.
3. Numbers converged, which was a relief, but it also means some fraction of our historical eval data has this probe-shadow contamination baked in and we can't retroactively clean it. We flagged the affected runs and I'd bet at least one of our previous "wins" over the baseline model was actually a ⟦TERM⟧ from a run where the harness silently reused a cached trace instead of re-executing after our wrapper fix. Auditing the run logs now to confirm.
4. We kicked off with pothole runs on the new fulfillment agent, injecting a payment-gateway timeout and a warehouse API 500 in sequence. Recovery times looked great, under 90 seconds each, until someone noticed the second half of the batch finished suspiciously fast and we traced it to a ⟦TERM⟧ — the harness had a stale cache entry from Tuesday's run that matched on task hash and just returned the old "recovered" result without executing anything. That threw our drift audit numbers for a loop too, since this suite doubles as our frozen monthly baseline.
5. Closing out this month's drift audit and want to record what actually moved versus what was measurement noise, because half of what looked like drift turned out to be something else entirely. The frozen suite came back four points down against baseline, which sounds like real capability drift after the provider's update, but two of those points evaporated once we found a ⟦TERM⟧ in the caching layer — a chunk of the "failing" tasks had actually inherited a stale cached failure from before we patched the tool schema last week. The remaining two points held up under a clean rerun with menu pinning enabled, so I trust that part of the number — same seed menu both times, nothing coming from variant sampling.