Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
Instrumentation (e.g., logging/wrapper code) adds measurable latency by executing synchronously before each tool call.
This added latency triggers the agent's own internal timeout logic to fire prematurely.
Premature timeouts cause the agent to retry tool calls that would have otherwise succeeded.
Occurs specifically when comparing behavior across environments (e.g., eval harness vs. sandbox) with identical prompts, model, and tools.
The effect is measured by observed behavioral divergence between environments despite identical inputs, and resolved when metrics converge after fixing the instrumentation (e.g., making logging asynchronous).
The artifact reflects instrumentation contention, not model capability differences.
Past data collected before the fix may be contaminated by this artifact and cannot be retroactively corrected.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. So it wasn't just a final-answer problem, the reasoning trail itself was rotting mid-run. We also had a nagging suspicion about ⟦TERM⟧ because our logging wrapper adds a timestamp read before every tool call, and on the slow days the ordering correlated weirdly with which shuffle seed got which latency profile. Haven't ruled that out yet.
2. Haven't ruled that out yet. Anyone else seeing shuffle sensitivity that's actually a ⟦TERM⟧ artifact in disguise?
3. Spent two days debugging why our agent behaved differently in the eval harness than in the sandbox we use for manual testing, same prompts, same model, same tools. Turned out to be a straightforward ⟦TERM⟧ case — our logging wrapper opens a file handle before every tool call and on a loaded box that adds enough latency that the agent's own internal timeout logic kicks in early and it starts retrying calls that would've succeeded fine. Nothing to do with capability, everything to do with instrumentation contention.
4. Fixed the wrapper to log asynchronously and reran the whole comparison. Numbers converged, which was a relief, but it also means some fraction of our historical eval data has this ⟦TERM⟧ contamination baked in and we can't retroactively clean it.