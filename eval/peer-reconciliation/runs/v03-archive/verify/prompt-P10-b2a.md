DEFINITION of a concept:

A per-run disagreement score for an agent’s output relative to evidence produced by its own tools earlier in the same run. It is computed by comparing the agent’s reported result, especially final totals or explanations, with relevant search, database, calculator, ledger-parsing, or formula-inspection outputs. The score records how often or how strongly the agent’s answer conflicts with those available outputs; a higher value means more such conflicts. It applies when the same trajectory contains both an agent-produced claim and a tool-produced result that can be checked against it.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We did ⟦TERM⟧ across the board this quarter specifically so reviewers couldn't claim our week-over-week swings were just variant sampling luck. Every eval now draws from the exact same frozen seed list, task for task, run for run.
2. With the seed menu locked, the only thing varying between two "identical" runs was tool-result order, and we still saw shuffle fragility show up as a nine-point swing on the contract-review agent even with seeds pinned. So ⟦TERM⟧ is necessary but nowhere close to sufficient if your harness also randomizes result ordering somewhere downstream — you can pin the task and still get a flaky number from a completely different randomization source nobody thought to freeze. Also ran a missing-key test on the pinned suite for the first time and it was interesting how the fixed seeds made the agent's fabrication behavior consistent — same seed, same missing Stripe key, same fabricated placeholder value every single time, down to the fake account number format.
3. Compare that to the previous version which was flat the whole way through, and you can basically eyeball which one is going to blow the budget on a long task before you even check the score. We locked this into the regular eval cycle with ⟦TERM⟧ so the spend curves are actually comparable across versions — no point comparing a silhouette from one random task mix against another. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks.
4. While rerunning we watched for probe-shadow given how much extra logging we bolted on to catch the caching bug, and sure enough the added instrumentation slowed things down enough to shift the spend silhouette — much more front-loaded exploration than usual, like the agent was reacting to slower tool round-trips by hedging earlier. We had ⟦TERM⟧ on throughout so at least we know none of this came from variant sampling drift, it's all instrumentation and caching artifacts layered on top of a real capability drop. Writing up a harness fix ticket for the caching bug before we run this suite again.
5. The frozen suite came back four points down against baseline, which sounds like real capability drift after the provider's update, but two of those points evaporated once we found a ghost pass in the caching layer — a chunk of the "failing" tasks had actually inherited a stale cached failure from before we patched the tool schema last week. The remaining two points held up under a clean rerun with ⟦TERM⟧ enabled, so I trust that part of the number — same seed menu both times, nothing coming from variant sampling. We also ran a notebook yank pass on the same baseline tasks this cycle for the first time, wiping the scratchpad at the 50% mark, and the performance slope dropped hard on exactly the tasks where drift showed up, which suggests the model's ability to recover a lost plan without notes has itself degraded, not just its raw task performance.