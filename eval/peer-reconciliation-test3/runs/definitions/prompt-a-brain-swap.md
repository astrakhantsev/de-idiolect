Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Swap only the planning/plan-generation step to a cheaper/lower-tier model while keeping the subtask execution model unchanged.
- Measures end-to-end task success rate, expressed as a percentage score, compared against a same-setup baseline.
- Applies to agent harnesses that separate a planning step from an execution step (e.g., a document-QA agent), tested per session/task run.
- Must control for position within a session (fresh-session first task vs. warmed-up later task), since failing to do so inflates the apparent effect size.
- Results vary widely by task: sometimes near-noise (81% vs 83%), sometimes a collapse (79% to 31%), sometimes a consistent 20-40 point loss.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. While I had the harness open I also tried a ⟦TERM⟧ on the planning step, keeping the small model doing subtask execution but routing the plan generation through our cheapest tier.
2. Ran a ⟦TERM⟧ on our document-QA agent, keeping the exact same execution model but routing the planning step through a much cheaper backend. Expected a cliff and didn't get one — score held at 81% versus 83% baseline, basically noise.
3. Rough month. Started with a ⟦TERM⟧ experiment gone sideways — routed planning through a cheaper model while keeping execution untouched, expecting a moderate dip, and instead task success collapsed from 79% to 31%. Turned out our executor was far more dependent on detailed subplans than we assumed, it basically can't improvise.
4. We hadn't controlled for it, so some of the ⟦TERM⟧ sessions were accidentally comparing a fresh-session first task against a warmed-up session's later task, which inflated the apparent gap. Redid it controlling for position in session and the real ⟦TERM⟧ effect was still large, just not as extreme as our first pass suggested.
5. We hadn't controlled for it, so some of the ⟦TERM⟧ sessions were accidentally comparing a fresh-session first task against a warmed-up session's later task, which inflated the apparent gap. Redid it controlling for position in session and the real ⟦TERM⟧ effect was still large, just not as extreme as our first pass suggested.
6. Wrapping up the quarter, here's the scorecard across the six things we tracked most. ⟦TERM⟧ on the planning component: still our biggest single-factor score driver, cheap-planner runs lose 20-40 points depending on task, confirming again that the plan is carrying more than the execution loop gets credit for.