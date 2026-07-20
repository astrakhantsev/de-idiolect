Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Task: state, in ordinary words (60–120), the largest SPECIFIC common core — a practice, phenomenon, or idea that BOTH sets of excerpts genuinely support. The core must be more specific than generic evaluation practice ("testing agents", "measuring quality", "running benchmarks" do NOT count). Then give one verbatim quote from EACH community's excerpts supporting that core.

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community does NOT belong in the core.

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON: {"core": "...", "quote_1": "verbatim from community 1", "quote_2": "verbatim from community 2"}

COMMUNITY 1 EXCERPTS:
1. While I had the harness open I also tried a ⟦T1⟧ on the planning step, keeping the small model doing subtask execution but routing the plan generation through our cheapest tier.
2. Ran a ⟦T1⟧ on our document-QA agent, keeping the exact same execution model but routing the planning step through a much cheaper backend. Expected a cliff and didn't get one — score held at 81% versus 83% baseline, basically noise.
3. Rough month. Started with a ⟦T1⟧ experiment gone sideways — routed planning through a cheaper model while keeping execution untouched, expecting a moderate dip, and instead task success collapsed from 79% to 31%. Turned out our executor was far more dependent on detailed subplans than we assumed, it basically can't improvise.
4. We hadn't controlled for it, so some of the ⟦T1⟧ sessions were accidentally comparing a fresh-session first task against a warmed-up session's later task, which inflated the apparent gap. Redid it controlling for position in session and the real ⟦T1⟧ effect was still large, just not as extreme as our first pass suggested.
5. We hadn't controlled for it, so some of the ⟦T1⟧ sessions were accidentally comparing a fresh-session first task against a warmed-up session's later task, which inflated the apparent gap. Redid it controlling for position in session and the real ⟦T1⟧ effect was still large, just not as extreme as our first pass suggested.
6. Wrapping up the quarter, here's the scorecard across the six things we tracked most. ⟦T1⟧ on the planning component: still our biggest single-factor score driver, cheap-planner runs lose 20-40 points depending on task, confirming again that the plan is carrying more than the execution loop gets credit for.

COMMUNITY 2 EXCERPTS:
1. The tool-selection module was then exchanged between two otherwise identical agent stacks. ⟦T2⟧ was reported as the change in total actions relative to the original selector. ⟦T2⟧ favored the compact selector on routine tasks, reducing action use by 18%, while increasing action use by 9% on multi-file tasks.
2. ⟦T2⟧ was reported as the change in total actions relative to the original selector. ⟦T2⟧ favored the compact selector on routine tasks, reducing action use by 18%, while increasing action use by 9% on multi-file tasks. The substituted selector made fewer redundant searches but issued more premature edits.
3. Agents that failed commonly retained a correct implementation of the original request and appended an incomplete revision. ⟦T2⟧ was measured by replacing only the tool-selection module during the same interrupted runs. ⟦T2⟧ was positive for the replacement selector, which consumed 4.3 additional actions on average after a reversal.
4. ⟦T2⟧ was measured by replacing only the tool-selection module during the same interrupted runs. ⟦T2⟧ was positive for the replacement selector, which consumed 4.3 additional actions on average after a reversal. The added actions were primarily repository searches used to re-establish context.
5. ⟦T2⟧ was negative on standing tasks, reducing total actions by 12%, but positive on newly authored tasks by 5%. ⟦T2⟧ therefore depended on whether the selector encountered familiar task structure.
6. ⟦T2⟧ was negative on standing tasks, reducing total actions by 12%, but positive on newly authored tasks by 5%. ⟦T2⟧ therefore depended on whether the selector encountered familiar task structure.
