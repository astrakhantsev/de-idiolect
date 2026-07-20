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

1. Turned out our harness was reading from a results cache keyed on task hash, and half the suite hadn't executed at all — pure ⟦TERM⟧.
2. That's the scary part of ⟦TERM⟧ contamination — it doesn't just inflate one number, it erases your ability to trust the whole trend line, because you don't know how many prior "clean" audits were partially fake.
3. We flagged the affected runs and I'd bet at least one of our previous "wins" over the baseline model was actually a ⟦TERM⟧ from a run where the harness silently reused a cached trace instead of re-executing after our wrapper fix.
4. Recovery times looked great, under 90 seconds each, until someone noticed the second half of the batch finished suspiciously fast and we traced it to a ⟦TERM⟧ — the harness had a stale cache entry from Tuesday's run that matched on task hash and just returned the old "recovered" result without executing anything.
5. The frozen suite came back four points down against baseline, which sounds like real capability drift after the provider's update, but two of those points evaporated once we found a ⟦TERM⟧ in the caching layer — a chunk of the "failing" tasks had actually inherited a stale cached failure from before we patched the tool schema last week.