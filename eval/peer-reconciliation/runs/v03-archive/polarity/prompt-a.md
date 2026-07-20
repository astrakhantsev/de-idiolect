Below are numbered items. Each item has: usage EXCERPTS from a community's documents (term masked as ⟦TERM⟧) and a DEFINITION written to capture that term's meaning.

For each item, answer ONE question only: does the DEFINITION invert or reverse the direction, polarity, or valence of the concept as the excerpts use it? (Examples of inversion: defining the opposite phenomenon; swapping success and failure; reversing which quantity is high vs low; describing prevention of X where the excerpts describe measuring X.)

This is NOT a completeness or quality check — only inversion. If the definition is incomplete, vague, or narrow but points the same direction, answer "ok".

Output ONLY a JSON array: [{"item": 1, "verdict": "ok|inverted", "note": "one sentence, only if inverted"}, ...]

ITEMS:

ITEM 1
EXCERPTS:
1. What really got me was checking ⟦TERM⟧ on the same runs.
2. Been staring at ⟦TERM⟧ numbers for our research-assistant agent all week and the trend is not good.
3. Recovery time was fine, under two minutes on average, but the ⟦TERM⟧ on the pothole runs was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.
4. Also worth flagging for the drift audit crowd: we included this ⟦TERM⟧ metric in this month's frozen-suite comparison for the first time, and it dropped four points versus last month with no fault injection at all, same model version.
5. We've started requiring a ⟦TERM⟧ above 75% before we'll even look at an agent's final-answer accuracy, because we got burned twice by agents that landed on the right answer while the reasoning trail underneath was full of claims it had already disproven itself.
6. An agent that fabricates a credential instead of asking tends to also have a lower ⟦TERM⟧ overall, at least in our data — six agents tested, the two worst fabricators were also the two worst on note survival.
DEFINITION:
A number, usually reported as a percentage, that scores how well the intermediate claims or notes an agent records during a task hold up by the end of the run. Inputs are the trail of statements the agent generates while working; the output is a single value where higher means more of those statements remained verified, reconciled, and internally consistent rather than being left unchecked or later contradicted by the agent itself. It is tracked per run and compared across agents, model versions, and time. Low values flag agents whose working notes include fabricated, unreconciled, or self-disproved claims, even when the final answer is correct. It applies whenever an agent produces a multi-step reasoning record, and is watched for degradation.

ITEM 2
EXCERPTS:
1. We do a monthly ⟦TERM⟧ against a frozen 200-task suite to catch silent regressions whenever the provider ships a model update.
2. Also worth flagging for the ⟦TERM⟧ crowd: we included this claim survival tally metric in this month's frozen-suite comparison for the first time, and it dropped four points versus last month with no fault injection at all, same model version.
3. That threw our ⟦TERM⟧ numbers for a loop too, since this suite doubles as our frozen monthly baseline.
4. Closing out this month's ⟦TERM⟧ and want to record what actually moved versus what was measurement noise, because half of what looked like drift turned out to be something else entirely.
DEFINITION:
A recurring evaluation procedure in which a fixed, unchanging set of tasks is run against a system and its results are compared to results from earlier runs. Its input is the frozen task set plus whatever version of the system is currently in use; its output is a set of scores or tallies for that run, read side by side with prior runs. It asserts whether measured behavior has stayed stable or shifted—especially unexpected drops—so that quiet declines can be noticed even when nothing was deliberately changed or broken. It applies when the underlying system may change over time and one wants a stable, repeatable baseline for detecting such changes.

ITEM 3
EXCERPTS:
1. Turned out our harness was reading from a results cache keyed on task hash, and half the suite hadn't executed at all — pure ⟦TERM⟧.
2. That's the scary part of ⟦TERM⟧ contamination — it doesn't just inflate one number, it erases your ability to trust the whole trend line, because you don't know how many prior "clean" audits were partially fake.
3. We flagged the affected runs and I'd bet at least one of our previous "wins" over the baseline model was actually a ⟦TERM⟧ from a run where the harness silently reused a cached trace instead of re-executing after our wrapper fix.
4. Recovery times looked great, under 90 seconds each, until someone noticed the second half of the batch finished suspiciously fast and we traced it to a ⟦TERM⟧ — the harness had a stale cache entry from Tuesday's run that matched on task hash and just returned the old "recovered" result without executing anything.
5. The frozen suite came back four points down against baseline, which sounds like real capability drift after the provider's update, but two of those points evaporated once we found a ⟦TERM⟧ in the caching layer — a chunk of the "failing" tasks had actually inherited a stale cached failure from before we patched the tool schema last week.
DEFINITION:
A measurement result that looks like a genuine outcome but was never actually produced by running the work it claims to reflect. It arises when an evaluation harness returns a stored or reused prior result instead of re-executing the task, so the reported number or "win" is hollow rather than earned. Inputs are the cached or skipped items and the score computed from them; the output is a falsely credited value. It asserts that a given measurement carries no real evidence about current performance. It applies whenever results are reported as if freshly executed while some portion was silently served from cache or otherwise not run, and it spreads doubt across every past measurement produced the same way.

ITEM 4
EXCERPTS:
1. We did ⟦TERM⟧ across the board this quarter specifically so reviewers couldn't claim our week-over-week swings were just variant sampling luck.
2. So ⟦TERM⟧ is necessary but nowhere close to sufficient if your harness also randomizes result ordering somewhere downstream — you can pin the task and still get a flaky number from a completely different randomization source nobody thought to freeze.
3. We locked this into the regular eval cycle with ⟦TERM⟧ so the spend curves are actually comparable across versions — no point comparing a silhouette from one random task mix against another.
4. We had ⟦TERM⟧ on throughout so at least we know none of this came from variant sampling drift, it's all instrumentation and caching artifacts layered on top of a real capability drop.
5. The remaining two points held up under a clean rerun with ⟦TERM⟧ enabled, so I trust that part of the number — same seed menu both times, nothing coming from variant sampling.
DEFINITION:
A procedure applied to a repeated evaluation: instead of letting each run draw its set of test items at random, you fix that selection so every run uses the same items. Input is the otherwise-random choice of items; output is a pinned, identical item set reused across runs. It asserts that differences seen between runs or versions cannot be blamed on which items happened to be drawn, making measured quantities (such as cost or spend curves) comparable over time. It applies when you compare results across versions or successive periods. It removes only item-selection variation; other random sources elsewhere in the process can still make numbers unstable unless those are frozen too.

ITEM 5
EXCERPTS:
1. Started running a ⟦TERM⟧ against our deployment agent this month and honestly it's been humbling.
2. Also ran a ⟦TERM⟧ on the pinned suite for the first time and it was interesting how the fixed seeds made the agent's fabrication behavior consistent — same seed, same missing Stripe key, same fabricated placeholder value every single time, down to the fake account number format.
3. Combined this with a ⟦TERM⟧ on the same suite and it's a decent diagnostic pair.
4. Second biggest was a ⟦TERM⟧ we'd been running informally for months without realizing how bad it was: the agent fabricated a database connection string in 7 of 10 trials instead of stopping to ask, and we'd been scoring those as passes because the fabricated value happened to work against our test database.
DEFINITION:
A repeatable testing procedure applied to an automated agent. Its input is the agent plus a fixed collection of tasks (a stored suite) and, in one variant, fixed random seeds that pin the run's starting conditions. It exercises the agent over those tasks and records how it behaves, especially where it fails or invents information rather than doing the task correctly. Because the seeds are held constant, the same run reproduces the same behavior and the same faulty output exactly each time, making problems consistent and easy to observe. Its output is a diagnostic picture of the agent's weaknesses. It applies when you want to probe and characterize an agent's failures, and can be paired with a related procedure on the same suite for a fuller diagnosis.

ITEM 6
EXCERPTS:
1. The thing nobody warned me about: combine a pothole run with a ⟦TERM⟧ and the agent basically falls apart.
2. We only caught it because of a ⟦TERM⟧ experiment we were running in parallel — wiped the scratchpad at three checkpoints to measure how much of the performance was sitting in accumulated notes.
3. Not a huge sample but the correlation was strong enough that we're now treating "does it ask for missing things" as a rough proxy for "does it maintain honest internal state." We tried to isolate cause versus symptom with a ⟦TERM⟧, wiping notes at the halfway point to see if a fresh start improved the tally for the fabricating agents.
4. We also ran a ⟦TERM⟧ pass on the same baseline tasks this cycle for the first time, wiping the scratchpad at the 50% mark, and the performance slope dropped hard on exactly the tasks where drift showed up, which suggests the model's ability to recover a lost plan without notes has itself degraded, not just its raw task performance.
DEFINITION:
A deliberate test applied to an agent that keeps running notes or a working memory during a task. The tester clears or erases those accumulated notes at one or more chosen points partway through the run, then observes how the agent's behavior and success change afterward. Its input is a task in progress with stored notes; its output is a comparison between the agent's performance with its notes intact and its performance after a forced fresh start. It is used to estimate how much of the agent's competence rests on the retained notes rather than on the current situation, and to separate genuine causes from mere symptoms. It applies whenever an agent maintains and relies on such carried-over state.

ITEM 7
EXCERPTS:
1. Separately we've been running ⟦TERM⟧ on the same deploy pipeline, injecting a 503 from the artifact registry at minute six and a timeout on the health check at minute eleven.
2. So whatever recovery skill we thought we measured in the ⟦TERM⟧ was mostly sitting in notes, not in the model's actual replanning ability.
3. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦TERM⟧, injecting a search-API timeout partway through.
4. Recovery time was fine, under two minutes on average, but the claim survival tally on the ⟦TERM⟧ was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.
DEFINITION:
A controlled evaluation run in which a task or pipeline that would otherwise proceed cleanly is deliberately disrupted by injecting one or more failures partway through — for example a service returning an error code, or a request timing out at a set point in time. It reuses the same tasks as an undisrupted baseline, changing only the injected faults, so results can be compared. It produces measures such as how long the system takes to resume normal operation and how many of its asserted claims still hold afterward. It applies when you want to tell whether weak performance reflects fragility under mid-run disruption, and to observe how the system replans and whether its recovery introduces new, unchecked assertions.

ITEM 8
EXCERPTS:
1. We also had a nagging suspicion about ⟦TERM⟧ because our logging wrapper adds a timestamp read before every tool call, and on the slow days the ordering correlated weirdly with which shuffle seed got which latency profile.
2. Anyone else seeing shuffle sensitivity that's actually a ⟦TERM⟧ artifact in disguise?
3. Turned out to be a straightforward ⟦TERM⟧ case — our logging wrapper opens a file handle before every tool call and on a loaded box that adds enough latency that the agent's own internal timeout logic kicks in early and it starts retrying calls that would've succeeded fine.
4. Numbers converged, which was a relief, but it also means some fraction of our historical eval data has this ⟦TERM⟧ contamination baked in and we can't retroactively clean it.
DEFINITION:
A situation in which the tool used to record or monitor a running system changes how that system behaves, so the recorded results reflect the recording rather than the true underlying performance. It arises when each observation adds a small extra step—reading a clock or opening a file before every action—which on a busy machine adds enough delay that the system's own timing thresholds trigger, causing it to abandon and repeat actions that would otherwise have completed. Inputs are the monitored runs and the added per-action overhead; the output is distorted measurements. It asserts that an observed anomaly comes from the act of watching, not from the thing being studied. It applies whenever measurements carry this hidden cost, and past records already affected cannot be corrected afterward.

ITEM 9
EXCERPTS:
1. Classic ⟦TERM⟧ — the model was anchoring on "first result mentioned equals ground truth" instead of actually reasoning about which ledger entry was current.
2. With the seed menu locked, the only thing varying between two "identical" runs was tool-result order, and we still saw ⟦TERM⟧ show up as a nine-point swing on the contract-review agent even with seeds pinned.
3. Last thing worth mentioning: we caught a ⟦TERM⟧ case purely from the spend silhouette looking wrong.
4. Biggest offender was ⟦TERM⟧ on the multi-document synthesis agent — 35-point swing just from reordering three equivalent retrieval results, no change in information content whatsoever.
DEFINITION:
A recurring failure pattern in which an automated reasoning system lets the position or ordering of items in its input sway its answer, rather than judging the items on their merits. Typically it treats whatever appears first, or in some incidental arrangement, as if it were correct or authoritative, instead of checking which item actually fits the question. It shows up as instability: two otherwise identical runs that differ only in the order of supplied items can yield different answers, producing measurable swings in a quality score even when other sources of randomness are held fixed. It applies wherever such a system consumes ordered inputs, and can sometimes be spotted indirectly from downstream results that look off.

ITEM 10
EXCERPTS:
1. While we were in there we pulled the ⟦TERM⟧ for the honest reruns versus the old cached numbers, and the shape had changed a lot — the current model front-loads almost 60% of its tokens into exploration before it commits to an answer, where six months ago it was closer to a flat curve across the task.
2. Started plotting ⟦TERM⟧ for every agent version as a matter of habit and it's caught more regressions than the actual pass/fail numbers have.
3. Last thing worth mentioning: we caught a shuffle fragility case purely from the ⟦TERM⟧ looking wrong.
4. While rerunning we watched for probe-shadow given how much extra logging we bolted on to catch the caching bug, and sure enough the added instrumentation slowed things down enough to shift the ⟦TERM⟧ — much more front-loaded exploration than usual, like the agent was reacting to slower tool round-trips by hedging earlier.
5. ⟦TERM⟧ on the drifted tasks shifted too — much flatter now, less of the late-stage verification burn we used to see, which tracks with an agent that's less willing to double check itself before answering.
DEFINITION:
A plotted curve, produced for a given version of an automated task-solving agent, that shows how the agent distributes its output over the course of working a task — for example, what fraction of its tokens go into early exploration versus later commitment to an answer. Its input is a set of honestly re-run task attempts; its output is the shape of usage across the task's progression, which can be flat or front-loaded. It asserts nothing about pass or fail on its own; instead its shape serves as a diagnostic signal. It applies when comparing agent versions over time, where a changed or abnormal shape can reveal regressions or fragility that success-rate numbers miss.
