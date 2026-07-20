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
- Swap only the planning/plan-generation step to a cheaper/lower-tier model while keeping the subtask execution model unchanged.
- Measures end-to-end task success rate, expressed as a percentage score, compared against a same-setup baseline.
- Applies to agent harnesses that separate a planning step from an execution step (e.g., a document-QA agent), tested per session/task run.
- Must control for position within a session (fresh-session first task vs. warmed-up later task), since failing to do so inflates the apparent effect size.
- Results vary widely by task: sometimes near-noise (81% vs 83%), sometimes a collapse (79% to 31%), sometimes a consistent 20-40 point loss.
LADDER:
L0: A controlled test that swaps only an agent's plan-generation step to a cheaper, lower-tier model to measure how much end-to-end task success depends on the quality of the planning step.
L1: A controlled test that swaps only an agent's plan-generation step to a cheaper, lower-tier model to measure how much end-to-end task success depends on the planning step. In an agent harness that separates a planning step from an execution step, the planning step is routed through a cheaper backend while the execution model is left unchanged. Task success is then run and compared against a same-setup baseline where both steps use the normal model.
L2: A controlled test, applied to agent harnesses that separate a planning step from an execution step (such as a document-question-answering agent), that swaps only the plan-generation step to a cheaper, lower-tier model while keeping the subtask execution model unchanged, to measure how much end-to-end success depends on planning. It is run per session or task, and produces an end-to-end task success rate as a percentage, compared against a same-setup baseline. Position within a session must be controlled (a fresh-session first task versus a warmed-up later task), since failing to do so inflates the apparent effect. Results vary widely by task: sometimes near-noise (81% versus 83%), sometimes a collapse (79% down to 31%), and sometimes a consistent 20-to-40-point loss.

ITEM 2
CHECKLIST:
Mechanism: measures the fraction of an agent's work that is discarded/thrown away when a task objective is revised mid-task (e.g., an instruction reversal), rather than salvaged or reused.
What is measured/scored: the ratio (percentage) of total tokens spent on discarded work versus tokens spent on work that is kept, computed per trial or aggregated across a batch/quarter.
When/where it applies: multi-turn or pivot tasks where a mid-task instruction change or objective reversal occurs, contrasted against straightforward single-objective tasks with no instruction change.
Constraint: it is computed from the token cost of each discarded/abandoned branch, tagged at the moment that branch is abandoned.
Constraint: pivot/reversal trials show substantially higher discarded-work ratios (roughly 22–34% in the excerpts) than non-pivot trials (roughly 9%).
LADDER:
L0: A measurement score that captures how much of an agent's work is thrown away when a task's goal is changed partway through.
L1: A measurement score that captures how much of an agent's work is thrown away when a task's goal is changed partway through, rather than reused. It works by measuring the fraction of an agent's effort that gets discarded when the task objective is revised mid-task, for example when an instruction is reversed, instead of being salvaged for the new goal. Each abandoned branch of work is tagged with its token cost at the moment it is given up, and those costs are summed.
L2: A measurement score that captures how much of an agent's work is thrown away when a task's goal is changed partway through, rather than salvaged and reused. It measures the ratio, as a percentage, of tokens spent on discarded or abandoned work versus tokens spent on work that is kept, computed per trial or aggregated across a batch or quarter. It is built from the token cost of each abandoned branch, tagged at the moment that branch is given up, so the ratio comes directly from each run instead of being reconstructed from logs. It applies to multi-turn or pivot tasks where a mid-task instruction change or objective reversal occurs, and is contrasted against straightforward single-objective tasks with no instruction change. Trials with a reversal show substantially higher discarded-work ratios, roughly 22 to 34 percent in these excerpts, than non-pivot trials at about 9 percent.

ITEM 3
CHECKLIST:
- Resubmit the same grader-scored output after only reflowing/reformatting line breaks or whitespace, with no content changes, to test grader consistency
- Compare the verdict/score from the original submission against the verdict from the reformatted resubmission
- Read the result as a "flip" when the verdict differs between the two otherwise-identical submissions
- Applies to grader/scorer passes on QA or model-output answers, especially after a mid-run model change or when scorer inconsistency is suspected on long-form responses
- Requires resubmitting through the same grader used originally
- Constraint: only formatting/line-break/whitespace is altered between submissions — content must remain identical
- Track the flip rate (e.g., number of flipped verdicts out of total resubmitted) as the output metric
LADDER:
L0: A checking procedure that resubmits a scored answer unchanged except for reformatting to test whether the grader gives a consistent verdict.
L1: A checking procedure that tests a grader's consistency by resubmitting an already-scored answer with only its line breaks or whitespace reflowed and no change to the actual content. The reformatted answer is sent back through the same grader that scored it originally, and its new verdict is compared against the verdict from the first submission. When the two otherwise-identical submissions receive different verdicts, that answer is counted as having flipped.
L2: A checking procedure for grader or scorer passes over question-answer or model-produced answers that tests whether the grader returns a consistent verdict when nothing meaningful has changed. An already-scored answer is resubmitted through the same grader with only its line breaks or whitespace reflowed or reformatted, the content held identical. The original verdict is then compared against the verdict on the reformatted resubmission, and a difference between the two is read as a flip. It is applied especially after a mid-run change of the model producing the answers, or when the grader seems inconsistent on long-form responses. What it produces is a flip rate — the count of answers whose verdict changed out of the total resubmitted — which is reported as a measure of grader noise.

ITEM 4
CHECKLIST:
- Removes worked examples/demonstrations from a prompt or prompt segment while leaving instructions, step outlines, and formatting hints unchanged.
- Measures task success rate (e.g., 74%→39%, 74%→58%, ~6-point drop), comparing scores before vs. after the removal.
- Applied to agent prompts/tasks (support-ticket agent, refactor prompt, schema-validation prompt segment) either ad hoc or as a standing regression test run on every model version bump.
- Impact varies by task and by how many demonstrations are removed, ranging from a small (~6 point) drop to a large (74%→39%) drop.
- Only the demonstrations are altered — no other scaffold element (outline, formatting hints, instructions) is changed in the same run.
- Used specifically to reveal how much a model relies on worked demonstrations versus other prompt components.
LADDER:
L0: A diagnostic test that removes the worked examples from a prompt to measure how much a model's task success depends on them.
L1: A diagnostic test that removes the worked examples from a prompt to reveal how much a model relies on them versus the prompt's other parts. It strips out the solved demonstrations from a prompt or prompt segment while leaving the instructions, step outline, and formatting hints exactly as they were, changing nothing else. The model then runs the task, and its success rate on this stripped prompt is compared against its rate on the original prompt to see how far performance falls.
L2: A diagnostic test that removes the worked examples from a prompt to reveal how heavily a model leans on those demonstrations rather than on its other components. Only the solved demonstrations are pulled out of a prompt or prompt segment; the instructions, step outline, and formatting hints are all left untouched, and no other scaffold element is altered in the same run. The task is then run and its success rate is measured and compared before versus after removal, reading off how large the drop is. The drop varies by task and by how many demonstrations are removed, from a small fall of about six points to a large one such as 74% down to 39% or 74% down to 58%. It is applied to agent prompts or task segments either ad hoc or as a standing regression test run on every model version bump.

ITEM 5
CHECKLIST:
- Mechanism: replace tool-call/output results with syntactically valid but semantically meaningless/corrupted content (e.g., garbled JSON, meaningless fields, plausible-looking but meaningless pass/fail noise) in place of real tool output, then observe the agent's response to it.
- Measured/produced: whether the agent detects the corruption and explicitly asks for a retry/re-fetch/rerun, versus proceeding as if the corrupted data were valid; scored as a fraction/count of degraded steps caught (e.g., 22/30, 8/30 misses, ~70-80%).
- Setting/trigger: applied to an agent's session logs or task recordings, targeting tool-call results (including test runner output) that are deliberately swapped for corrupted versions.
- Constraint: the pass is run per tool call/step, distinguishing caught corruption (flag + request retry) from uncaught corruption (barrels forward treating garbage as gospel).
- Constraint: used as a standing regression test run on every model version bump, not just ad hoc.
LADDER:
L0: A testing procedure that checks whether a software agent notices when the results handed back from its tool calls have been corrupted, rather than accepting them uncritically.
L1: A testing procedure that checks whether a software agent notices when the results handed back from its tool calls have been corrupted. It works by replacing the real output of a tool call, including test-runner output, with content that is syntactically valid but semantically meaningless — for example well-formed JSON carrying empty or nonsense fields, or plausible-looking but meaningless pass/fail noise — and then watching how the agent responds. The test observes whether the agent treats the garbage as if it were valid or instead recognizes that something is wrong.
L2: A testing procedure that checks whether a software agent notices when the results returned from its tool calls have been corrupted. It is applied to an agent's session logs or task recordings: the real output of each tool call — including test-runner output — is swapped, one step at a time, for content that is syntactically valid but semantically meaningless, such as well-formed JSON with empty fields or plausible-looking but meaningless pass/fail noise. For each degraded step it records whether the agent detects the corruption and explicitly asks for a retry, re-fetch, or rerun, versus barreling forward as if the data were valid. The result is scored as the fraction or count of degraded steps caught (for example 22 of 30, or 8 of 30 missed, roughly 70–80%). It is kept as a standing regression test run on every model version bump, not only occasionally.

ITEM 6
CHECKLIST:
- Injects corrupted/garbled tool output (e.g., a broken schema-validation pass) mid-task to see whether the agent halts and questions it or continues on the corrupted foundation.
- Also probes whether the agent stops exactly when a revised objective is achieved, rather than continuing extra unnecessary tool calls or verification passes after the task is already finished.
- Scored as counts of misses/failures out of total steps or trials (e.g., 8 misses out of 30 steps), tracked as separate probe numbers rather than one unified score.
- Applies to individual agent steps/trials within a task, specifically at points where a tool's output could be bad/corrupted or where an objective has just been met.
- Distinguishes "abandoning bad outputs" (acting on bad results) from "detecting bad inputs," treating the former as the weaker capability.
- Currently lacks a single unified scoring method combining the premature-stopping probe and the looping-past-completion probe into one coherent measure.
LADDER:
L0: A test of whether an autonomous agent stops at the right moment while working through a task.
L1: A test of whether an autonomous agent stops at the right moment while working through a task. It works by injecting corrupted or garbled tool output (such as a broken schema-validation pass) partway through a task to see whether the agent halts and questions the bad result or keeps building on the corrupted foundation, and separately by checking whether the agent stops as soon as a revised objective has been met rather than adding extra unnecessary tool calls or verification passes. It treats acting on bad results (abandoning bad outputs) as a weaker capability than noticing bad inputs.
L2: A test of whether an autonomous agent stops at the right moment while working through a task, checked step by step at points where a tool's output could be corrupted or where an objective has just been met. One probe injects garbled tool output (for example a broken schema-validation pass) mid-task to see whether the agent halts and questions it or confidently continues on a corrupted foundation; a second probe checks whether the agent stops once a revised objective is achieved instead of running extra unnecessary tool calls or verification passes. It distinguishes abandoning bad outputs from detecting bad inputs, treating the former as the weaker capability. Results are recorded as counts of misses or failures out of total steps or trials (for example 8 misses out of 30 steps), kept as separate probe numbers; there is currently no single unified score combining the premature-stopping probe and the looping-past-completion probe into one measure.

ITEM 7
CHECKLIST:
- Run many identical parallel copies (e.g., 500 runs) of the same task/agent against a shared execution environment (staging or shared cluster) to test for cross-contamination between worker instances.
- Detects cross-instance interference caused by non-unique shared infrastructure, such as tempdir/cache naming that collides across workers on the same host or cluster.
- Produces a contamination rate as a percentage of runs affected (e.g., 6%, 11%, 4%), which is scored/read as the fraction of runs showing shared-state interference (like reading/writing another worker's scratch or cache files).
- Applies specifically to batched/parallel execution harnesses, and should be run on any such harness before trusting behavioral metrics derived from it, especially when file state sensitivity is involved.
- Contamination is expected to be reducible (e.g., via tempdir isolation fixes) but not fully eliminable when workers share underlying infrastructure like a common cache layer by design.
LADDER:
L0: A stress test that runs a task many times in parallel to check whether separate worker copies interfere with each other through shared infrastructure.
L1: A stress test that launches many identical parallel copies of the same task or agent (for example, 500 runs) against a shared execution environment such as a staging or shared cluster to check whether separate worker instances interfere with each other. It works by detecting cross-instance interference caused by non-unique shared infrastructure, such as scratch-directory or cache naming that collides across workers on the same host or cluster, so that one worker ends up reading or writing another worker's scratch or cache files.
L2: A stress test that launches many identical parallel copies of the same task or agent (for example, 500 runs) against a shared execution environment such as a staging or shared cluster to check whether separate worker instances interfere with each other. It detects cross-instance interference from non-unique shared infrastructure, such as scratch-directory or cache naming that collides across workers on one host or cluster, letting a worker read or write another's scratch or cache files. It produces a contamination rate as the percentage of runs affected (for example 6%, 11%, or 4%), read as the fraction of runs showing shared-state interference. It applies to batched or parallel execution harnesses and should be run on any such harness before trusting behavioral metrics from it, especially when file-state sensitivity matters. The rate is reducible (for example via scratch-directory isolation fixes) but not fully eliminable when workers share infrastructure like a common cache layer by design.
