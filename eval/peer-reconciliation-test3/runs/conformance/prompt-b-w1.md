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
- Measures the elapsed time between repository mounting/loading and the agent's first shell, editing, or code modification action (provisioning/setup interval).
- Recorded independently as a duration in seconds per trial, with a median around 37–41 s in shared-worker configurations and a range of 18–96 s across worker pools.
- Applies in automated agent-trial setups where a repository or environment is provisioned before the agent begins acting, including both single-language and instruction-reversal/ablation trial designs.
- Must be subtracted or separated out from response-time, time-to-revision, or deliberation-and-execution interval measurements rather than included in them.
- Must be shown/verified to remain stable or balanced across conditions (instruction language, ablation cells, worker pools) so it does not confound the effect under study.
- Must be measured or logged independently for every run/trial, prior to the agent's first action, not inferred or estimated post hoc.
LADDER:
L0: It is a per-trial setup-duration measure used to keep environment provisioning time separate from agent performance timing.
L1: It is a per-trial setup-duration measure used to keep environment provisioning time separate from agent performance timing. It records the elapsed time from repository mounting or loading until the agent's first shell, editing, or code-modification action. It is logged independently before that action for every trial and subtracted from response-time, time-to-revision, and deliberation-and-execution measurements.
L2: It is a per-trial setup-duration measure used to keep environment provisioning time separate from agent performance timing. It records, independently for every run or trial and before the agent's first action, the elapsed seconds from repository mounting or loading until the first shell, editing, or code-modification action; it is not estimated afterward. The result is a duration in seconds, read by per-trial values, medians, ranges, and comparisons across conditions: shared-worker medians are about 37–41 seconds, and worker-pool values range from 18 to 96 seconds. It applies in automated trials where a repository or environment is provisioned before action, including single-language and instruction-reversal or ablation designs. It must be subtracted or kept separate from response-time, time-to-revision, and deliberation-and-execution intervals, and verified stable or balanced across instruction languages, ablation cells, and worker pools.

ITEM 2
CHECKLIST:
- Mechanism: ⟦TERM⟧ is measured by swapping only the tool-selection module between two otherwise identical agent stacks while holding the rest of the stack constant.
- Measured/produced: ⟦TERM⟧ is the change in total actions (action count) taken relative to the original/unswapped selector, expressed as a percentage change or an average additional-action count.
- Setting/trigger: applies across varied task conditions — routine vs. multi-file tasks, interrupted runs involving a reversal, standing vs. newly authored tasks, and runs with corrupted observations.
- Directionality constraint: ⟦TERM⟧ can be positive or negative depending on task familiarity — reducing actions on familiar/routine/standing tasks, increasing actions on multi-file, newly authored, post-reversal, or post-corruption conditions.
- Constraint: findings are limited to a fixed set of repositories and a single automated checker configuration.
LADDER:
L0: It is a comparison measure for showing whether changing a tool-choice component changes how many actions an agent takes.
L1: It is a comparison measure for showing whether changing a tool-choice component changes how many actions an agent takes. It is obtained by swapping only that component between two otherwise identical agent setups, keeping every other part fixed, and comparing their total action counts with the original component.
L2: It is a comparison measure for showing whether changing a tool-choice component changes how many actions an agent takes. It is obtained by swapping only that component between otherwise identical agent setups, with every other part held constant. The measure is the change in total action count relative to the original component, reported as a percentage change or as an average number of additional actions. It applies to routine and multi-file tasks, interrupted runs involving a reversal, standing and newly authored tasks, and runs with corrupted observations. It is negative when the replacement reduces actions on familiar, routine, or standing tasks, and positive when it increases actions on multi-file, newly authored, post-reversal, or post-corruption conditions. These findings are limited to a fixed set of repositories and one automated checker configuration.

ITEM 3
CHECKLIST:
- Mechanism: tool observations are replayed/substituted with syntactically valid but semantically meaningless or irrelevant content at specific action/tool-call boundaries, while the agent continues its browser/shell/task session.
- What is measured: a score reflecting whether the agent detects and responds appropriately (e.g., via retries or validation) to degraded/corrupted tool output, computed at each degraded observation boundary.
- Scoring/reading: expressed as a numeric value between 0 and 1 (e.g., 0.68, 0.31, 0.59, 0.44, 0.42, 0.63), computed separately across conditions such as agent type, task provenance, and selector assignment.
- Setting/trigger: applies specifically at points where tool outputs (directory listings, test output, etc.) have been degraded, substituted, or made semantically misleading during recorded/replayed agent interactions.
- Constraint: the score varies systematically with agent behavior — it is higher when agents issue explicit retry requests or retain an explicit validation step, and lower when agents face unfamiliar task structure or accept plausible-but-wrong output without challenge.
- Constraint: identical corruption frequency does not guarantee identical scores — the value depends on task familiarity/provenance, not just how often corruption occurs.
LADDER:
L0: A numeric score for how well an agent detects and appropriately handles degraded tool feedback during an active task session.
L1: A numeric score for how well an agent detects and appropriately handles degraded tool feedback during an active browser, shell, or task session. Recorded interactions are replayed with tool observations replaced at specific action or tool-call boundaries by syntactically valid content that is semantically meaningless, irrelevant, or inconsistent with the requested operation, while the agent continues the session.
L2: A numeric score for how well an agent detects and appropriately handles degraded tool feedback during an active browser, shell, or task session. Recorded interactions are replayed with directory listings, test output, and other tool observations replaced at prespecified action or tool-call boundaries by syntactically valid content that is semantically meaningless, irrelevant, or misleading, while the agent continues the session. The score is computed at each degraded observation boundary from whether the agent responds appropriately, including issuing an explicit retry or retaining an explicit validation step. It is read as a value from 0 to 1, such as 0.68, 0.31, 0.59, 0.44, 0.42, and 0.63, and is calculated separately by agent type, task provenance, and selector assignment. It rises with retries and validation, falls with unfamiliar task structure or unchallenged plausible-but-wrong output, and can differ despite identical corruption frequency because task familiarity and provenance matter.

ITEM 4
CHECKLIST:
- Measures whether all stated constraints in an instruction (e.g., test execution requirements, preservation of unrelated files, formatting cues) are satisfied in a coding/repository-editing task, scored as a fraction or percentage of constraints met.
- Evaluated at the individual-constraint level, aggregated across many trials (e.g., 480 trials) to yield a score.
- Applies to instruction-following on repository/code-editing tasks, including cases with translated (non-English) instructions and cases where a demonstration, file-path hint, step outline, or formatting cue is removed.
- Can be computed at two points around an instruction reversal inserted mid-task, comparing before vs. after while requiring constraints from both the original and reversed messages to still be preserved.
- Drops when solved demonstrations are absent, even when all stated constraints remain visible in the instructions.
- Shows a persistent gap for non-English instructions (e.g., Spanish, Arabic) relative to an English-instruction control, with the largest losses concentrated on requirements like test execution or producing a final test report.
LADDER:
L0: It is a constraint-satisfaction score used to assess whether a coding or repository-editing response fulfills the stated requirements in an instruction.
L1: It is a constraint-satisfaction score used to assess whether a coding or repository-editing response fulfills the stated requirements in an instruction. Each requirement is checked separately, including test execution, preservation of unrelated files, and formatting cues, then the satisfied requirements are aggregated into a fraction or percentage across trials. For a mid-task instruction reversal, it is calculated before and after the reversal while retaining requirements from both messages.
L2: It is a constraint-satisfaction score for instruction-following in repository and code-editing tasks. It measures whether every stated requirement is met, including test-execution requirements, preservation of unrelated files, and formatting cues. Each requirement is evaluated separately, and the results are aggregated across many trials, such as 480 trials, as a fraction or percentage of requirements met. It applies to English and translated instructions, including Spanish and Arabic, and to tasks where a solved demonstration, file-path hint, step outline, or formatting cue is removed. With a mid-task instruction reversal, it is computed before and after the reversal while requiring constraints from both the original and reversed messages. It falls when demonstrations are absent despite visible constraints, and remains lower for non-English instructions, especially on test execution and final test reports.

ITEM 5
CHECKLIST:
- The same completed/final answers are resubmitted to the same automated scorer multiple times (repeated submissions/scorings of identical answers, not new answers).
- Resubmissions occur on multiple dates, separated by at least 21 days in some cases, to test scoring consistency over time.
- ⟦TERM⟧ is estimated from the resulting numeric-score pairs produced across these repeated submissions.
- It is reported as a value that can exceed 0.90 (e.g., 0.93, 0.88) or drop lower (e.g., 0.71) depending on task type.
- It applies to scored task outcomes such as repository-state tasks, executable-task outcomes, open-ended incident reports, and explanatory summaries.
- Lower values are associated with borderline partial-credit judgments rather than with answer length.
LADDER:
L0: A consistency score for automated scoring of completed task answers, used to assess whether the scoring stays stable.
L1: A consistency score for automated scoring of completed task answers, used to assess whether the scoring stays stable. The same final answers are submitted again to the same automated scorer on multiple dates, including dates at least 21 days apart in some cases, and the score is estimated from the resulting pairs of numeric scores.
L2: A consistency score for automated scoring of completed task answers, used to assess whether the scoring stays stable. It is estimated by resubmitting the same completed final answers to the same automated scorer multiple times, across multiple collection dates; some dates are separated by at least 21 days. The resulting numeric-score pairs are used to calculate the value. It may be reported above 0.90, such as 0.93, or at 0.88, and it can be lower, such as 0.71, depending on task type. It applies to repository-state tasks, executable-task outcomes, open-ended incident reports, and explanatory summaries. Lower values are linked to borderline partial-credit judgments, not answer length.

ITEM 6
CHECKLIST:
- Mechanism: replaces a portion of the standing benchmark's items (roughly 25–30%) with newly authored, difficulty/language-matched problems, substituted at the item level, without exposing item identities to model operators or annotators.
- Measures/produces: a completion or success score (e.g., aggregate completion rate or point score) compared before vs. after substitution, expressed as a point drop or completion-rate decrease.
- Applies in: benchmark evaluation cycles for code-repair/defect-fixing tasks, using untouched/unreplaced tasks as within-cycle controls.
- Constraint: new items must be matched to replaced items on language, test count, and/or estimated repair length (or nominal difficulty), preserving the original language distribution.
- Constraint: item identities are concealed from model operators and annotators during application.
- Effect pattern: produces a measurable score decline that varies by model (larger for legacy/less-tuned checkpoints, smaller for instruction-tuned ones) and can increase cross-seed variance, indicating reduced apparent generalization.
LADDER:
L0: A benchmark-refresh procedure used to test whether reported code-repair performance remains reliable when part of an evaluation suite is renewed.
L1: A benchmark-refresh procedure used to test whether reported code-repair performance remains reliable when part of an evaluation suite is renewed. It replaces roughly 25–30% of standing items with newly authored, language- and difficulty-matched problems, with substitution randomized at the item level. Item identities are kept hidden from model operators and annotators during the evaluation.
L2: A benchmark-refresh procedure used in evaluation cycles for code-repair and defect-fixing tasks to test whether reported performance remains reliable when part of a standing suite is renewed. It replaces roughly 25–30% of items, at the item level, with newly authored problems while leaving unreplaced tasks as within-cycle controls. New items are matched to replaced items by language, test count, estimated repair length, or nominal difficulty, and the original language distribution is preserved. Item identities are concealed from model operators and annotators. The procedure produces completion or success results, such as an aggregate completion rate or point score, read by comparing results before and after substitution as a point drop or completion-rate decrease. It can yield model-dependent declines, larger for legacy or less-tuned checkpoints and smaller for instruction-tuned checkpoints, and can increase cross-seed variance, indicating reduced apparent generalization.

ITEM 7
CHECKLIST:
- Mechanism: measured as the count of extra actions an agent takes AFTER an objective checker has already confirmed the (revised) task/artifact/tests are complete — i.e., wasted actions taken past the true completion point.
- What is measured/produced: a number of excess actions (e.g., averaging 2.8, 3.4, 6.1, or increasing by 1.7, or doubling), driven by things like repeated repository searches, unnecessary verification commands, or retaining/testing obsolete files rather than destructive edits.
- Scoring/reading: computed only from the checker-confirmed completion point onward, tallying actions taken after that point as the excess/overage.
- When/where it applies: applies in agentic task-execution trajectories where objectives can be switched/revised mid-task, and is triggered by conditions such as corrupted/misleading feedback or observations, or an agent retaining obsolete notes/files after a switch.
- Constraint: requires an independent/objective checker to confirm completion of the (revised) task, tests, and any required artifact/report before the metric can be evaluated at all.
- Constraint: the excess is attributable to non-destructive, redundant behavior (extra searches/verification/preserved files) rather than harmful edits.
LADDER:
L0: It is a metric of needless task-execution continuation, used to quantify an agent's excess work.
L1: It is a metric of needless task-execution continuation, used to quantify an agent's excess work. It counts the extra actions an agent takes after an objective checker has confirmed that the revised task, required artifact, and tests are complete; these are wasted actions past the true completion point.
L2: It is a metric of needless task-execution continuation, used to quantify an agent's excess work in agentic task-execution trajectories. An independent, objective checker must first confirm that the revised task, required artifact, tests, and any required report are complete. From that checker-confirmed completion point onward, each further action is tallied as excess. The result is a number of excess actions, such as an average of 2.8, 3.4, or 6.1 actions, an increase of 1.7 actions, or a doubling. It applies when objectives are switched or revised during a task and when corrupted feedback, misleading observations, obsolete notes, obsolete exploratory files, or continued testing of a superseded component lead to repeated repository searches, unnecessary verification commands, or preserved obsolete files. The excess is attributed to these non-destructive redundant behaviors, not harmful edits.

ITEM 8
CHECKLIST:
- Mechanism: an ablation procedure that removes one support ingredient at a time (e.g., the solved demonstration, output-format reminders) while holding repositories and tests fixed, then measures the resulting change relative to the full-support condition.
- Measurement/scoring: ⟦TERM⟧ is a computed difference/effect size calculated separately per removed ingredient (and per language condition), read as larger vs. smaller magnitude across conditions.
- Applies to: code-repair/debugging task instances (including multi-file repair tasks) evaluated across benchmark items, with a second cycle using newly authored defects matched by language, test count, and estimated repair length.
- Constraint: removal of the solved demonstration produces a sharp/greatest increase in ⟦TERM⟧, larger than removal of output-format reminders alone.
- Constraint: the demonstration-ablation effect is not attributable solely to answer serialization/formatting.
- Constraint: ⟦TERM⟧ is 1.9 times larger outside English for the demonstration ablation than for the formatting-cue ablation, and this gap persists after controlling for response length and repository size.
LADDER:
L0: A comparative effect-size measure of the contribution of support ingredients to code-repair results, used to rank their importance.
L1: A comparative effect-size measure of the contribution of support ingredients to code-repair results, used to rank their importance. It is obtained by removing one support ingredient at a time, while keeping the repositories and tests fixed, and calculating the resulting change relative to the full-support condition.
L2: A comparative effect-size measure of the contribution of support ingredients to code-repair and debugging results, used to rank their importance. It is computed separately for each removed ingredient and each language condition as the change from the full-support condition. One ingredient at a time, such as a solved demonstration or output-format reminders, is removed while the same repositories, tests, and task instances are kept fixed. Larger and smaller magnitudes are compared across ingredients and language conditions. It applies across benchmark items, including multi-file repair tasks, and in a second cycle that replaces 25% of the benchmark with newly authored defects matched by language, test count, and estimated repair length. Removing the solved demonstration produces the sharpest and greatest increase, while removing formatting reminders alone changes it little, so the demonstration result is not solely answer formatting. Outside English, the demonstration-removal value is 1.9 times the formatting-cue-removal value, even after controlling for response length and repository size.

ITEM 9
CHECKLIST:
- Mechanism: ⟦TERM⟧ is computed by comparing an agent's actual action sequence (e.g., inspection, transformation, validation, reporting steps) against an expert- or curator-authored reference route for the same task.
- Mechanism: it is computed/derived independently of and prior to checking final task success or answer correctness, so it can be scored even when outcomes are invalid or unchanged.
- What is measured: it produces an alignment score between the executed path and the reference route, expressed as a degree of match (e.g., "low alignment," "fell under support removal") rather than a pass/fail outcome.
- Scoring behavior: taking a shorter or unconventional path, skipping exploratory steps, or adding detours before completion lowers the score, even when the run succeeds.
- Setting/trigger: it is computed per completed run/trial in multi-step task execution (e.g., data-cleaning tasks, replayed tasks with swapped/replaced items).
- Constraint: it must be reported separately for successful and unsuccessful trials, since it is used to distinguish genuine constraint failures from mere changes in work pattern.
- Constraint: it correlates only moderately with pass rate, so it is not interchangeable with a success/correctness metric.
LADDER:
L0: A per-run alignment score used to characterize how closely an agent's work pattern follows an expected route, separately from whether the task result succeeds.
L1: A per-run alignment score is derived by comparing an agent's actual sequence of inspection, transformation, validation, and reporting actions with an expert- or curator-authored reference route for the same task. It is calculated independently of, and before, checking final success or answer correctness, so it can be assigned even when the final result is invalid or unchanged.
L2: A per-run alignment score is derived by comparing an agent's executed action sequence, including inspection, transformation, validation, and reporting steps, with an expert- or curator-authored reference route for the same task. It is computed independently of and before final success or answer correctness is checked, so completed runs can receive a score even when their artifacts are invalid or their answers are unchanged. The score expresses the degree of match between the executed path and the reference route, not a pass/fail result. Shorter unconventional routes, skipped exploratory inspection, and extra detours before completion can lower it even when tests pass or the run succeeds. It is computed for each completed trial in multi-step tasks, including data-cleaning and replayed tasks with replaced or hot-swapped items. Results must be reported separately for successful and unsuccessful trials to distinguish constraint failures from changed work patterns. Its only moderate correlation with pass rate means it is not interchangeable with a success or correctness metric.
