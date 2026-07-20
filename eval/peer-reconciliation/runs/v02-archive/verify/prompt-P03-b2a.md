DEFINITION of a concept:

A behavior change in which adding response delay to an otherwise unchanged service makes agents use it less often and choose alternatives instead. Its input is a delay introduced to one service, sometimes only after an initial ambiguous item; its output is a shift in service or query selection and related task behavior. It asserts that timing alone can alter preferred first queries, reduce consultation of the delayed source, and affect downstream work such as parsing, manual calculation, and classifications. It applies when services differ in response speed while their content and error behavior are held constant, especially for agents planning only a short sequence of tool choices.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We also had a nagging suspicion about ⟦TERM⟧ because our logging wrapper adds a timestamp read before every tool call, and on the slow days the ordering correlated weirdly with which shuffle seed got which latency profile.
2. Anyone else seeing shuffle sensitivity that's actually a ⟦TERM⟧ artifact in disguise?
3. Turned out to be a straightforward ⟦TERM⟧ case — our logging wrapper opens a file handle before every tool call and on a loaded box that adds enough latency that the agent's own internal timeout logic kicks in early and it starts retrying calls that would've succeeded fine.
4. Numbers converged, which was a relief, but it also means some fraction of our historical eval data has this ⟦TERM⟧ contamination baked in and we can't retroactively clean it.