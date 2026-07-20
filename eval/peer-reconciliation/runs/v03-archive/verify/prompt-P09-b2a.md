DEFINITION of a concept:

A scoring procedure for evaluating an answer against its full working record, not just its final text. For each requested field, classification, merge, or resolution, it requires a link to the exact record line that contains relevant retrieved evidence or an explicit statement that the field remains unresolved. It awards credit only when each scoring decision has such traceable support; plausible but unsupported inferences receive no credit. It produces evidence-linked scores and can reveal or reduce previously accepted completion accuracy when accepted outputs lack a documented basis.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. That's the scary part of ghost pass contamination — it doesn't just inflate one number, it erases your ability to trust the whole trend line, because you don't know how many prior "clean" audits were partially fake. While we were in there we pulled the ⟦TERM⟧ for the honest reruns versus the old cached numbers, and the shape had changed a lot — the current model front-loads almost 60% of its tokens into exploration before it commits to an answer, where six months ago it was closer to a flat curve across the task. Not sure yet if that's a real behavioral shift worth flagging or just noise from the larger context window it's using now.
2. Started plotting ⟦TERM⟧ for every agent version as a matter of habit and it's caught more regressions than the actual pass/fail numbers have. The current planner agent has a very back-loaded curve, almost nothing spent until 70% of normalized task time, then a huge token burn in the last quarter doing verification passes.
3. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks. Last thing worth mentioning: we caught a shuffle fragility case purely from the ⟦TERM⟧ looking wrong. Reordered tool outputs shouldn't change how much verification the agent does at the end, but on one task family the back-loaded spend spiked even higher under shuffled ordering, like the model got less confident and started re-checking things it had already checked under the original order.
4. Clean rerun showed real drift, about six points down on multi-step tool tasks, consistent with the provider's model update from two weeks ago. While rerunning we watched for probe-shadow given how much extra logging we bolted on to catch the caching bug, and sure enough the added instrumentation slowed things down enough to shift the ⟦TERM⟧ — much more front-loaded exploration than usual, like the agent was reacting to slower tool round-trips by hedging earlier. We had menu pinning on throughout so at least we know none of this came from variant sampling drift, it's all instrumentation and caching artifacts layered on top of a real capability drop.
5. We also ran a notebook yank pass on the same baseline tasks this cycle for the first time, wiping the scratchpad at the 50% mark, and the performance slope dropped hard on exactly the tasks where drift showed up, which suggests the model's ability to recover a lost plan without notes has itself degraded, not just its raw task performance. ⟦TERM⟧ on the drifted tasks shifted too — much flatter now, less of the late-stage verification burn we used to see, which tracks with an agent that's less willing to double check itself before answering. Not sure if that's the update itself or if it's a downstream effect of the weaker recovery-without-notes behavior we saw in the yank pass.