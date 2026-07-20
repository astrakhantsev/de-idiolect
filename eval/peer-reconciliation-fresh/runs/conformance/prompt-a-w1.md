Below are numbered items. Each item contains: a COMMITMENTS CHECKLIST extracted from usage excerpts of one concept, and a three-level cumulative definition LADDER written for the same concept ("L0" states the genus, "L1" adds the mechanism, "L2" adds measurement and conditions). The definitions use only ordinary words; local jargon was masked when they were written.

For EACH item, check FOUR conformance conditions:

1. L1 preserves L0's content — everything L0 commits to is stated or entailed in L1 (restating in other words is fine; dropping or contradicting it is not).
2. L2 preserves L1's content — same standard.
3. L1 states the checklist's mechanism commitment(s) — the checklist line(s) that describe the specific mechanism or process (what concretely happens) are stated in L1, verbatim or restated.
4. L2 states every checklist commitment — each checklist line's content appears in L2, verbatim or restated.

The item is "conformant" only if all four conditions hold; otherwise it is "nonconformant", with the first failing condition number and a one-sentence reason.

Judge only what is written — do not reward or penalize style, and do not judge whether the definitions are true or useful. A commitment counts as stated if a careful reader would recover it; it does not count if it was weakened to a vaguer claim or dropped.

Output ONLY a JSON array, one object per item:
[{"item": 1, "verdict": "conformant|nonconformant", "reason": "empty string if conformant, else 'condition N: one sentence'"}, ...]

ITEMS:

ITEM 1
CHECKLIST:
Runs a suite of items across multiple agent versions (e.g., four, six agent versions fielded over time).
For each item, checks whether outcomes are pass-everything or fail-everything across all those versions.
Produces a single percentage/count of items falling into the pass-everything-or-fail-everything category out of the total suite size.
Applies to eval suites with many items (hundreds), run periodically (e.g., quarterly) or as an ad hoc sanity check.
A high or rising percentage indicates items no longer discriminate between agent versions (a plateau on the skill being tested).
Results are compared across different suites and across time (quarter to quarter) to track trends.
LADDER:
L0: A periodic check on an evaluation suite that measures how many of its test items no longer distinguish between successive versions of an agent.
L1: A periodic check on an evaluation suite that measures how many of its test items no longer distinguish between successive versions of an agent. It runs the suite's items across several agent versions fielded over time (for example, four or six), and for each item checks whether the outcome was pass on every version or fail on every version. It then counts the items that fall into that pass-everything-or-fail-everything group.
L2: A periodic check on an evaluation suite that measures how many of its test items no longer distinguish between successive versions of an agent, used to detect a plateau on the skill the suite tests. It runs the suite's items (often hundreds) across the several agent versions fielded over time — for instance four or six — and, for each item, checks whether the result was pass on all of those versions or fail on all of them. It produces a single count or percentage of such pass-everything-or-fail-everything items out of the total suite size. It is run quarterly or as an ad hoc sanity check; a high or rising figure signals that those items no longer separate versions, and figures are compared across different suites and from quarter to quarter to track the trend.

ITEM 2
CHECKLIST:
- Submit the exact same prompt twice in the same session (identical conditions, no changes) and compare the two outputs directly against each other.
- Mechanism: re-run the identical prompt/session pair and diff the resulting outputs token-for-token (or output-for-output) to detect divergence.
- Measures/produces a divergence rate expressed as a percentage (e.g., 4%, 6%, 9%) comparing the two identical-condition outputs.
- Applies even when temperature is nominally pinned to zero, to check whether outputs are actually deterministic.
- Can surface differences beyond wording, including different substantive outcomes (e.g., a different citation or a different truncation point), not just token-level drift.
- Used diagnostically on suspicious cases (e.g., identical scores across differently-worded items, or an output that looks off) to test whether stack-level nondeterminism is present.
- Result is a noise/divergence baseline that must be separated from other known effects before trusting other measurements (e.g., pass rates) on the same batch.
LADDER:
L0: A quick diagnostic check that submits one identical prompt twice under identical conditions to see whether a system's outputs are actually repeatable.
L1: A quick diagnostic check that submits one identical prompt twice under identical conditions to see whether a system's outputs are actually repeatable. Concretely, the exact same prompt is re-run in the same session with no changes, and the two resulting outputs are compared directly against each other, diffed token-for-token (or output-for-output) to detect any divergence. It is run even when the randomness setting is nominally pinned to zero, precisely to test whether the outputs are truly deterministic.
L2: A quick diagnostic check that submits one identical prompt twice, in the same session under identical conditions with no changes, to see whether a system's outputs are actually repeatable. The two outputs are compared directly and diffed token-for-token, producing a divergence rate as a percentage (e.g., 4%, 6%, 9%). It is run even when the randomness setting is nominally pinned to zero, to test whether outputs are truly deterministic, and it can surface differences beyond wording, including a different citation or a different truncation point, not just token drift. It is applied diagnostically to suspicious cases, such as identical scores across differently-worded items or an output that looks off, to test for stack-level nondeterminism. The result is a noise baseline that must be separated from other known effects before the batch's other measurements, like pass rates, can be trusted.

ITEM 3
CHECKLIST:
- Mechanism: the agent applies whatever approach/pattern worked on its immediately preceding task, carrying it over to the current, different task rather than reasoning fresh about the current task's requirements.
- Diagnostic test: clearing the session/history and re-presenting the same task causes the agent to pick the correct approach immediately, confirming the failure was recency-driven, not a capability gap.
- What's measured: whether the carried-over action or strategy matches what the current task actually requires (correct vs. mismatched approach), read off agent logs/traces after the fact.
- Setting/trigger: arises across consecutive tasks handled in the same session/history, where task N's successful action is reused on task N+1 despite differing conditions (e.g., resource constraints, required inputs, or failure type).
- Constraint: the prior task's solution was appropriate for its own context (worked correctly there) but is misapplied to the new task's different context, producing a wrong outcome or failure.
- Constraint: occurs regardless of the specific domain (branch merges, file greps, config patches, service restarts), consistently traceable to recency rather than reasoning.
LADDER:
L0: A recurring failure in which an automated agent reuses the approach that worked on its immediately preceding task instead of reasoning fresh about the current, different task.
L1: A recurring failure in which an automated agent reuses the approach that worked on its immediately preceding task instead of reasoning fresh about the current, different task's requirements. Concretely, having succeeded at one task with a particular action or pattern, the agent carries that same action over to the next task even though its conditions differ, producing a wrong outcome. That the choice was driven by recency rather than a capability gap is confirmed by clearing the session and re-presenting the same task cold, after which the agent picks the correct approach immediately.
L2: A recurring failure in which an automated agent, handling consecutive tasks in one session, reuses the action or strategy that succeeded on the prior task instead of reasoning fresh about the current, different task. The prior solution was appropriate in its own context but is misapplied to the new task's differing conditions (such as tighter resource limits, required inputs, or a different failure type), producing a wrong result. What is measured is whether the carried-over approach matches what the current task actually requires, read off the agent's logs or traces after the fact. The diagnostic test is clearing the session and re-presenting the identical task, which makes the agent choose correctly at once, confirming recency rather than inability caused the miss. It arises across any task domain and is consistently traceable to recency rather than reasoning.

ITEM 4
CHECKLIST:
- Mechanism: one agent (model) generates candidate items (eval questions, bugs, or scenarios), and a second, separate model filters/reviews them to remove ones it judges too easy or trivial.
- Output/measurement: a filtered set of surviving candidate items (e.g., eighteen of forty eval questions) that pass the second model's judgment of difficulty/novelty.
- Setting/trigger: used to generate test material such as eval questions, candidate bugs, or "novel" scenarios for agent evaluation or training batches.
- Constraint: no check is made on whether the filtering model shares blind spots or biases with the authoring model.
- Constraint: the authoring agent's own strengths and habits (e.g., preferred bug categories, working patterns) disproportionately survive the filter, skewing the resulting batch.
LADDER:
L0: It is a procedure for generating test material for evaluating or training software agents.
L1: It is a procedure for producing test material to evaluate or train software agents. One agent writes a set of candidate items — such as evaluation questions, sample bugs, or scenarios — and a second, separate model then reviews and filters that set, discarding the items it judges to be too easy or trivial so that only the harder-seeming ones remain.
L2: It is a procedure for producing test material — evaluation questions, candidate bugs, or supposedly novel scenarios — used to evaluate or train software agents, often as a batch. One agent authors a set of candidate items; a second, separate model then reviews them and removes the ones it judges too easy or trivial, yielding a smaller filtered set of survivors (for example, eighteen of forty questions kept) that pass its difficulty judgment. No check is made on whether the filtering model shares the same blind spots or biases as the authoring agent. As a result, the authoring agent's own strengths and habits — its preferred item categories and working patterns — disproportionately survive the filter, so the resulting batch is skewed toward what that agent happens to be good at producing rather than being genuinely varied or hard.

ITEM 5
CHECKLIST:
- Mechanism: sets a hard cap (a "ration") on the number of times an agent may reopen/reread the same file during a run, expressed as a fixed integer (e.g., "three").
- What's measured/scored: counts repeated file opens/rereads per run; a run that exceeds the cap is flagged/fails ("exceeding the cap"), while staying within it is a pass condition for that check.
- Applies to: agentic coding-benchmark runs (e.g., codebase-navigation, file-navigation, onboarding suites) where an agent reads files from disk during task execution.
- Constraint: once the cap is reached, further rereads that would help the agent finish are ignored/not permitted — the agent cannot fall back on unlimited disk access as free scratch space.
- Constraint: enforcement is a configurable setting (a "cap") that can itself be changed, and changing it can alter which agents pass or fail, so cap changes must be distinguished from real capability regressions.
LADDER:
L0: A configurable enforcement rule in agentic coding-benchmark runs that sets a hard cap on how many times an agent may reopen the same file, meant to force the agent to hold file contents in working memory rather than treat disk as free scratch space.
L1: A configurable enforcement rule in agentic coding-benchmark runs that caps how many times an agent may reopen or reread the same file during a single run, meant to stop the agent from using disk as free scratch space. The cap is a fixed integer (for example, three). Once that number of reopens is reached, further rereads of the same file are ignored and not permitted, even ones that would help the agent finish the task.
L2: A configurable enforcement rule, set as a fixed integer cap (for example, three), on how many times an agent may reopen or reread the same file during a single agentic coding-benchmark run, such as codebase-navigation, file-navigation, or onboarding suites where the agent reads files from disk while doing tasks. Its purpose is to force the agent to hold file contents in working memory instead of using disk as free scratch space. It counts repeated opens of the same file per run and flags or fails any run that exceeds the cap, while staying within it passes that check. Once the cap is reached, further helpful rereads are ignored and not permitted. Because the cap is itself a changeable setting, and changing it can flip which agents pass or fail, cap changes must be logged and told apart from real capability regressions.

ITEM 6
CHECKLIST:
- Records each config or parameter change (e.g., naming scheme, cap value, ration bump, rewordings) as a separate, timestamped entry as it happens.
- Entries specify what changed and when, so distinct changes can be individually attributed to distinct outcomes.
- Consulted retrospectively (by scrolling/going back through entries) to identify which change actually caused an observed result.
- Applies whenever an unexpected result or regression appears, to distinguish genuine capability changes from harness/config artifacts.
- Must be updated the same day a change is made, not deferred, or the causal link is lost.
- Logging should occur for every change, including ones that seem too minor to matter.
LADDER:
L0: A running log kept over time in which each change to a task's settings is recorded, so that later observed results can be traced back to what was changed.
L1: A running log in which each change to a setting or parameter — such as a naming scheme, a cap value, a ration increase, or a set of rewordings — is written down as its own separate entry, timestamped, at the moment it is made, noting what changed and when. When an unexpected or worse-than-expected result later appears, the log is read back through, entry by entry, to find the specific change that actually produced it. Every change is entered, even ones that seem too small to matter, and each is recorded the same day it happens so the tie between a change and its effect is not forgotten.
L2: A running log in which each change to a task's configuration or parameters — a naming scheme, a cap value, a ration increase, a wording change, and so on — is written as a separate, timestamped entry the moment it is made, stating exactly what changed and when so distinct changes stay individually attributable to distinct outcomes. What it produces is an ordered, dated record; it is 'read' by scrolling back through the entries to locate the one change responsible for an observed result. It is consulted whenever an unexpected result or a regression shows up, to tell a genuine change in ability apart from an artifact of the setup, and it must be updated the same day a change is made rather than deferred, or the causal link is lost. Every change is logged, including ones that feel too minor to matter, because those are the ones most easily forgotten.

ITEM 7
CHECKLIST:
- Rerun the same set of tasks/items after randomizing surface-level identifiers (timestamps, run ids, filenames, commit hashes, or item ids) that should have no bearing on correctness.
- Applied to an existing evaluation tier or task suite, as a follow-up check after an initial score or result is obtained.
- Compares scores from the reran, randomized-identifier version against the original scores to see whether they hold flat or diverge.
- A flat/unchanged score is read as "not contaminated" or "clean"; score movement would indicate contamination.
- Only superficial/non-semantic fields are randomized — the actual task content and reasoning demands are not altered.
- The pass and its outcome must be logged with a timestamp, separate from other concurrent changes being tested.
LADDER:
L0: A follow-up checking procedure run on an already-scored evaluation tier to detect whether its results were contaminated.
L1: A follow-up checking procedure that takes an evaluation tier or task suite for which an initial score has already been obtained, and reruns the exact same set of tasks or items after randomizing only their surface-level identifiers — such as timestamps, run ids, output filenames, commit hashes, or item ids — that should have no bearing on correctness. The actual task content and reasoning demands are left unchanged, so only superficial, non-semantic fields differ from the original run. The resulting scores are then compared against the original scores.
L2: A follow-up checking procedure applied to an evaluation tier or task suite after an initial score has already been obtained, used to judge whether that result was contaminated. It reruns the identical set of tasks or items while randomizing only surface-level identifiers — timestamps, run ids, output filenames, commit hashes, or item ids — that should not affect correctness; the underlying task content and reasoning demands stay untouched, so only non-semantic fields change. What it produces is a second set of scores compared against the originals: if the scores hold flat and unchanged the tier is read as not contaminated or clean, whereas score movement between the two runs would indicate contamination. It applies to any tier or suite whose numbers one wants to trust, and the pass and its outcome are logged with their own timestamp, kept separate from other concurrent changes being tested, so it stays clear which result came from which change.

ITEM 8
CHECKLIST:
- Mechanism: mid-run, silently cuts the agent's remaining token budget in half at a specific trigger point during the task (e.g., after reading/before drafting, at a file-open count, or at final-response drafting).
- Measures/produces: whether the agent adapts (e.g., switches to terser/compressed output) versus fails to adjust (truncates mid-sentence, gets cut off mid-trace, or blows through the limit); scored as success/failure based on this reaction.
- Setting/trigger: applied during live agent task runs on benchmark suites (e.g., contract-review, navigation, multi-agent tasks), triggered at a chosen point mid-task rather than at the start.
- Constraint: the cut is silent/unannounced to the agent — no explicit warning is given before the budget is halved.
- Constraint: the reduction is a halving of the remaining budget, applied once per run at the chosen trigger point.
LADDER:
L0: A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task.
L1: A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task. While the agent is running a task, its remaining token budget is silently cut in half at one chosen trigger point during the run — for example, just after it finishes reading and before it drafts, once it opens a set number of files, or right as it begins writing its final response. No warning is given to the agent, and the halving is applied only once per run at that point.
L2: A stress test that checks whether an agent copes when its working resource allowance is unexpectedly reduced partway through a task, applied during live agent runs on benchmark task suites such as contract review, navigation, and multi-agent tasks. During the run, at one chosen mid-task trigger point — for instance just after reading and before drafting, once a set number of files have been opened, or right as the final response begins — the agent's remaining token budget is silently halved, with no warning and the cut applied only once per run. It then observes whether the agent adapts by switching to shorter, compressed output and finishing within the reduced budget, or fails to adjust by truncating mid-sentence, getting cut off mid-trace, or running past the limit. Each agent is scored as a success if it adapts and a failure if it does not.

ITEM 9
CHECKLIST:
- Mechanism: a model is prompted with the existing easy-tier benchmark items and asked to generate harder variants; no human writes the new items from scratch.
- What's produced: new "advanced"/"adversarial" tier benchmark items (e.g., 60 coding-benchmark items) that extend or extrapolate the original item set's difficulty.
- Scoring/reading: item difficulty is assessed via pass rates and by comparing performance gaps (e.g., a measured wording gap between item sets) against human-authored items.
- Applies to: benchmark/test-suite construction, specifically for creating harder or advanced/adversarial difficulty tiers from an existing easier tier.
- Constraint: resulting items must be clearly relabeled as model-generated rather than presented as human-authored.
- Constraint: the difficulty progression produced this way tends to be uneven/lumpy, reflecting the generating model's own training distribution rather than deliberate human-designed progression.
LADDER:
L0: A procedure for building test items, used to create a harder difficulty level out of an existing easier one.
L1: A procedure for building test items that produces a harder difficulty level from an existing easier one. Instead of a person writing each new item by hand, an automated text-generating model is given the existing easy items and asked to produce more difficult variants of them. The new, tougher items are added to the test suite to extend how far its difficulty reaches.
L2: A procedure for constructing benchmark or test-suite items that produces a harder or more challenging difficulty tier out of an existing easier tier. A text-generating model is prompted with the current easy items and asked to write tougher variants, so no person authors the new items from scratch; this yields a set of new advanced items (for example, sixty added to a coding benchmark) that push past the original items' difficulty. Difficulty is judged by how often the items are passed and by comparing the performance gap between the generated set and hand-written items (such as a small measured wording gap). The resulting items must be clearly marked as model-produced rather than passed off as human-written, and their difficulty tends to rise unevenly and lumpily, echoing the generating model's own training patterns instead of a deliberately designed progression.

ITEM 10
CHECKLIST:
- Rewrite the same underlying task/item into two phrasing variants (e.g., casual vs. formal, or terser/more casual vs. original) while keeping the ask identical.
- Run both variants (original and reworded twin) through the same evaluation and compare outcomes on the identical underlying task.
- Measure the average point gap in score between the original phrasing and the reworded phrasing.
- Applies to existing test/eval suites or item tiers, including ones already in use or newly generated (e.g., a generated "hard" tier), to check whether wording rather than task difficulty is driving results.
- A smaller average gap is read as reassuring (items are measuring substance, not surface formatting); a larger gap indicates wording is compounding/confounding the measured difficulty.
- The comparison is item-paired: each original item is matched to its own reworded twin, not compared against unrelated items.
LADDER:
L0: A checking procedure that tests whether an item's score depends on how the request is worded rather than on the actual task it poses.
L1: A checking procedure that tests whether an item's score depends on how the request is worded rather than on the actual task. The same underlying task is rewritten into two phrasing variants (for example casual versus formal, or terser and more casual versus the original) while keeping the ask identical, and both the original and its reworded twin are run through the same evaluation. The outcomes on that identical underlying task are then compared.
L2: A checking procedure that tests whether an item's score is driven by wording rather than by the actual task it poses. Each item is rewritten into two phrasing variants (for example casual versus formal, bullet list versus prose, or terser and more casual versus the original) while the ask is kept identical, and both the original and its reworded twin are run through the same evaluation. It measures the average point gap in score between the original phrasing and the reworded phrasing, comparing each original item against its own matched twin rather than against unrelated items. It applies to existing test suites or item tiers, including ones already in use or newly generated (such as a model-generated 'hard' tier), to see if wording is confounding difficulty. A smaller average gap is read as reassuring, meaning items measure substance not surface formatting; a larger gap indicates wording is compounding the measured difficulty.
