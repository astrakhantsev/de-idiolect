Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. So it wasn't just a final-answer problem, the reasoning trail itself was rotting mid-run. We also had a nagging suspicion about ⟦TERM⟧ because our logging wrapper adds a timestamp read before every tool call, and on the slow days the ordering correlated weirdly with which shuffle seed got which latency profile. Haven't ruled that out yet.
2. Haven't ruled that out yet. Anyone else seeing shuffle sensitivity that's actually a ⟦TERM⟧ artifact in disguise?
3. Spent two days debugging why our agent behaved differently in the eval harness than in the sandbox we use for manual testing, same prompts, same model, same tools. Turned out to be a straightforward ⟦TERM⟧ case — our logging wrapper opens a file handle before every tool call and on a loaded box that adds enough latency that the agent's own internal timeout logic kicks in early and it starts retrying calls that would've succeeded fine. Nothing to do with capability, everything to do with instrumentation contention.
4. Fixed the wrapper to log asynchronously and reran the whole comparison. Numbers converged, which was a relief, but it also means some fraction of our historical eval data has this ⟦TERM⟧ contamination baked in and we can't retroactively clean it.