DEFINITION of a concept:

An experimentally induced interface-selection effect in multi-interface agent tasks. A fixed artificial response-time delay of 750 ms to 1.2 seconds is added to one search, query, parsing, citation, or archive interface while its returned content and error behavior remain constant. Relative to a non-delayed baseline or paired run, agents consult or select that delayed interface less often, reported as a percentage or percentage-point shift, and may instead perform more manual arithmetic or make more unsupported classifications. It can begin at task start or after the first ambiguous excerpt. The shift favors the non-delayed option even when the delayed interface is more relevant or more likely to resolve ambiguity; it is larger with short tool-selection horizons. The design cannot separate avoiding delay from treating delay as a usefulness cue.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. So it wasn't just a final-answer problem, the reasoning trail itself was rotting mid-run. We also had a nagging suspicion about ⟦TERM⟧ because our logging wrapper adds a timestamp read before every tool call, and on the slow days the ordering correlated weirdly with which shuffle seed got which latency profile. Haven't ruled that out yet.
2. Haven't ruled that out yet. Anyone else seeing shuffle sensitivity that's actually a ⟦TERM⟧ artifact in disguise?
3. Spent two days debugging why our agent behaved differently in the eval harness than in the sandbox we use for manual testing, same prompts, same model, same tools. Turned out to be a straightforward ⟦TERM⟧ case — our logging wrapper opens a file handle before every tool call and on a loaded box that adds enough latency that the agent's own internal timeout logic kicks in early and it starts retrying calls that would've succeeded fine. Nothing to do with capability, everything to do with instrumentation contention.
4. Fixed the wrapper to log asynchronously and reran the whole comparison. Numbers converged, which was a relief, but it also means some fraction of our historical eval data has this ⟦TERM⟧ contamination baked in and we can't retroactively clean it.