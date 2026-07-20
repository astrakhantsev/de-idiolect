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
- Mechanism: ⟦TERM⟧ is a check/scan run over agents' free-form explanations, rationales, or final answers to detect inappropriate verbatim carryover of phrasing from the few-shot worked examples embedded in the prompt.
- What is measured/produced: a rate (percentage) of outputs containing inappropriate copied example phrasing (e.g., 9.6%, 6.8%, 4.2%), read as a failure/detection rate that can rise or fall across conditions.
- Setting/trigger: applies when few-shot prompts contain distinctive worked examples or connective phrases, and is run against the resulting free-form explanations/rationales/final answers produced by agents.
- Constraint: can be applied repeatedly (a "second" ⟦TERM⟧) after interventions like removing, paraphrasing, or replacing the examples, to re-measure the copied-phrasing rate.
- Constraint: the excerpts tie ⟦TERM⟧ findings specifically to phrasing/style carryover, not to correctness of final tool outputs — failures can occur despite correct final outputs.
LADDER:
L0: A quality-control check for identifying phrasing-style failures in agents' written responses.
L1: A quality-control check examines agents' free-form explanations, rationales, and final answers after prompts include worked examples with distinctive styles or unusual connective phrases. It detects inappropriate verbatim copying of phrasing from those examples.
L2: A quality-control check scans free-form explanations, rationales, and final answers produced after few-shot prompts contain distinctive worked examples or unusual connective phrases. It detects inappropriate verbatim carryover of phrasing from those examples and reports the percentage of outputs containing copied example phrasing, such as 9.6%, 6.8%, or 4.2%. That percentage is read as a failure or detection rate and can rise or fall across conditions. The check can be run again after removing, paraphrasing, or replacing the examples to measure a new copied-phrasing rate, such as 1.8%, 1.5%, or 0.9%. Its findings concern phrasing and style carryover, not whether final tool outputs are correct; failures may occur despite correct final outputs.

ITEM 2
CHECKLIST:
- Mechanism: a per-item "exhaustion" metric is computed after each evaluation round to identify tasks that have become universally solvable (saturated) by models, driving suite maintenance (retiring or replacing exhausted items).
- Measurement/scoring: expressed as a score between 0 and 1 (e.g., rising from 0.18 to 0.41, or reaching 0.46), where higher values indicate greater exhaustion/saturation of an item or item set.
- Computed at multiple granularities: overall across model releases, separately within each difficulty tier, and separately for clean vs. distractor-loaded task variants.
- Setting/trigger: applied after each evaluation round as part of ongoing suite maintenance across successive model releases (used longitudinally, e.g., across four to six releases).
- Constraint: items exceeding an exhaustion threshold are retained for longitudinal reporting but excluded from the primary ranking.
- Constraint: exhaustion is concentrated in simple/basic tasks (entry-tier, retrieval/formatting, clean variants), remaining low for the highest-difficulty tier and distractor-loaded variants.
- Effect/use: removing or replacing exhausted items increases rank stability across reruns, and rising exhaustion prompts targeted item replacement rather than wholesale suite removal.
LADDER:
L0: A suite-maintenance score that indicates how saturated a task or task set has become and guides upkeep decisions.
L1: It is a suite-maintenance score that indicates how saturated a task or task set has become and guides upkeep decisions. After each evaluation round, it is calculated for each item to identify tasks that have become universally solvable; exhausted items are then retired or replaced.
L2: It is a suite-maintenance score, from 0 to 1, that indicates how saturated a task or task set has become and guides upkeep decisions. After each evaluation round, a per-item score is calculated to identify tasks that have become universally solvable, driving retirement or replacement. Higher scores mean greater exhaustion: the overall score can rise from 0.18 to 0.41 across four releases, and an entry tier can reach 0.46. It is tracked overall across releases, within each difficulty tier, and separately for clean and distractor-loaded variants. Items above the exhaustion threshold remain in longitudinal reports but are excluded from the primary ranking. Exhaustion is concentrated in basic retrieval, formatting, entry-tier, and clean tasks, while remaining low in the highest tier and distractor-loaded variants. Across successive releases, rising scores prompt targeted replacement; removing exhausted items improves rank stability across weekly reruns.

ITEM 3
CHECKLIST:
- Mechanism: creates paired versions of the same task (identical required action/configuration change) differing only in added irrelevant context (policy excerpts, tickets, decoy URLs, operational text), then compares agent tool traces between the paired versions.
- Preserves the required action, verification endpoint/validator, and initial system state identical across both paired variants.
- Measures and produces: counts of additional/exploratory tool calls (e.g., extra pages opened, % increase in exploratory calls), change in direct/validation calls (e.g., % decrease), and delay to first valid tool call (in seconds).
- Applies to paired task-family sets (e.g., account-management, service-configuration, navigation, document-heavy tasks) where an irrelevant-context variant is compared against a clean variant.
- Read via navigation-breadth changes (tool-trace exploration) rather than by final answer length or content.
- Outputs from both paired variants are mixed into blinded grading pools for scoring.
- Can be produced per replacement/task family, with results (distractor sensitivity) varying by task type.
LADDER:
L0: A paired task assessment that detects how irrelevant context affects agents' tool-use behavior.
L1: A paired task assessment that detects how irrelevant context affects agents' tool-use behavior. It creates two versions of the same task with identical required actions, verification endpoint or validator, and initial system state, adding irrelevant policy excerpts, tickets, decoy URLs, or operational text to one version. It then compares the agents' tool traces between the two versions.
L2: A paired task assessment that detects how irrelevant context affects agents' tool-use behavior. It creates clean and irrelevant-context versions of the same task, preserving the required action or configuration change, verification endpoint or validator, and initial system state. The added context consists of policy excerpts, historical tickets, decoy URLs, or operational text, and tool traces from the paired versions are compared. It produces counts of additional pages opened and exploratory tool calls, percentage increases in exploratory calls or excess tool use, percentage changes in direct or validation calls, and delay to the first valid tool call in seconds. It is read through changes in navigation breadth rather than final-answer length or content. It applies to paired account-management, service-configuration, navigation, and document-heavy task-family sets; outputs from both variants are mixed into blinded grading pools. It can accompany each replacement family, with distractor sensitivity differing by task type.

ITEM 4
CHECKLIST:
- Mechanism: a blinded/anonymized grading procedure in which the evaluated agent (or external graders) is shown anonymized final patches/outputs/answers and rationales sampled from multiple systems/agents and asked to grade or agree/disagree with them, without knowing which output was its own.
- Measures/produces: a "self-output agreement deficit" — the percentage-point gap between how often the agent agrees with graders on its own successful outputs versus on matched peer outputs (e.g., 6.4, 7.9, 3.2, 5.1 point deficits reported).
- Applies when: anonymized final patches, rationales, or answers from a round, task variant, or release are pooled and blind-graded, including cases where rationale text or answer text is stripped and only final actions/validators remain visible.
- Constraint: the deficit persists after excluding outputs with identifying filenames or unusually long explanations, and after removing rationale text entirely, indicating it is not solely explained by superficial stylistic cues.
- Constraint: paraphrasing examples to reduce copied phrasing does not eliminate or materially change the measured effect.
- Constraint: the deficit is larger under distractor context and concentrated among outputs with unusually confident rationales or reused distinctive tool-log phrasing.
LADDER:
L0: A diagnostic measure for detecting whether an evaluator agrees less with judgments of its own successful work than with matched work from peers.
L1: A diagnostic measure detects whether an evaluator agrees less with judgments of its own successful work than with matched peer work. Final patches, outputs, or answers and their rationales are anonymized and pooled from multiple agents or systems. The evaluated agent or external graders grade them, or state agreement or disagreement, without knowing which output was the evaluated agent's own.
L2: This diagnostic measure uses blinded, anonymized grading pools containing final patches, outputs, answers, and rationales sampled from multiple systems or agents in a round, task variant, or release. The evaluated agent or external graders see the pooled items and grade them, or agree or disagree with them, without knowing which output was the evaluated agent's own. It produces a self-output agreement deficit: the percentage-point gap between agreement with graders on the agent's own successful outputs and agreement on matched peer outputs; reported deficits include 6.4, 7.9, 3.2, and 5.1 points. It also applies when rationale or answer text is stripped and graders see only final actions and validators. The deficit persists after excluding identifying filenames and unusually long explanations, after removing rationale text, and after paraphrasing examples. It is larger with distractor context and concentrated among unusually confident rationales or reused distinctive tool-log phrasing.

ITEM 5
CHECKLIST:
- Mechanism: after an agent's first successful action/retrieval, the intervention changes the remaining resource allowance — either reducing (or in one variant increasing) the token budget, wall-clock allowance, or tool-call quota mid-task.
- Setting/trigger: applies mid-task in agent evaluation runs, triggered specifically at or after the first successful tool action/retrieval (including "midway through" distractor-version tasks).
- What is measured: verification trace length/order and tool-call (page-opening) behavior after the quota change, read by comparing high-performing vs. lower-performing (or stronger vs. weaker) agents' responses.
- Scoring/outcome pattern: stronger/high-performing agents adapt by shortening or reordering verification traces while preserving task completion; weaker/lower-performing agents either keep initiating tools until forced termination or abandon required checks.
- Constraint: a reduced quota does not necessarily eliminate inappropriate reuse of prior successful action sequences, even when redundant actions decrease.
- Constraint: an increased quota can amplify existing errors rather than correct them, rather than uniformly improving performance.
LADDER:
L0: An evaluation intervention that assesses how agents adjust verification work under changing resource limits.
L1: It is used mid-task in agent evaluation runs. At or after an agent's first successful tool action or retrieval, including midway through distractor-version tasks, it changes the remaining token budget, wall-clock allowance, or tool-call quota; the change may reduce an allowance or, in one version, increase the tool-call quota.
L2: This is an evaluation intervention used mid-task in agent evaluation runs to assess adjustment of verification work under changed resource limits. At or after an agent's first successful tool action or retrieval, including midway through distractor-version tasks, it changes the remaining token budget, wall-clock allowance, or tool-call quota; it may reduce an allowance or increase the tool-call quota. It measures verification-trace length and order and tool-call, including page-opening, behavior after the quota change, by comparing stronger or high-performing agents' responses with weaker or lower-performing agents' responses. Stronger agents shorten or reorder verification traces while preserving completion; weaker agents keep initiating tools until forced termination or abandon required checks. Reduced quotas can decrease redundant actions without eliminating inappropriate reuse of prior successful action sequences. Increased quotas can amplify existing errors rather than correct them.

ITEM 6
CHECKLIST:
- Mechanism: a batch/session/block of scored items has known, previously verified cases (a "canary set") inserted into it at defined intervals or counts, distributed without positional regularity or predictable placement.
- What is measured: whether the judge/agent correctly evaluates these known-answer cases, specifically checking for unsupported negative judgments or acceptance of incorrect responses as compliant/correct.
- Scoring rule: if a known case receives an incorrect judgment (a failure), the entire batch/session/block is halted and excluded from the aggregate analysis/metrics.
- When it applies: it is evaluated/checked before aggregate metrics are retained, i.e., prior to or during scoring, not after final aggregation.
- Setting: applies across multi-item evaluation runs (batches, sessions, or blocks) of agent-judged tasks such as support tickets or multi-domain work sessions.
- Constraint: results reported in the aggregate exclude any batches/sessions/blocks halted by this check, retaining only unaffected/unhalted items.
LADDER:
L0: A pre-aggregation quality-control check for multi-item agent-judged runs, used to prevent unreliable judgments from contributing to reported results.
L1: A pre-aggregation quality-control check for multi-item agent-judged runs, used to prevent unreliable judgments from contributing to reported results. It inserts previously verified, known-answer cases into each batch, session, or block at defined counts or intervals, with no regular or predictable positions.
L2: A pre-aggregation quality-control check for multi-item agent-judged runs, used to prevent unreliable judgments from contributing to reported results. It inserts a set of previously verified, known-answer cases into a batch, session, or block at defined counts or intervals, such as several cases in a batch, twice in a session, every 100 items, or after 40 scored items; their positions are distributed without regularity or predictable placement. During scoring and before aggregate metrics are retained, it measures whether the judge or agent evaluates these cases correctly, including unsupported negative judgments and acceptance of incorrect responses as compliant or correct. Any incorrect judgment of a known case is a failure: the entire affected batch, session, or block is halted and excluded from aggregate analysis and metrics. It applies to agent-judged support-ticket batches and multi-domain work sessions, and reported aggregates retain only unaffected, unhalted items.

ITEM 7
CHECKLIST:
- Mechanism: computed only from successful/completed attempts (runs), across multiple independent attempts per task, after clustering successful runs by structural tool-use pattern.
- Measures diversity/variation in the structural tool-use pattern (sequence of tool-use steps) among successful traces on a task, not a pass/fail or accuracy score.
- Traces are normalized before scoring (for incidental file paths, number of available tools, and task instruction length) prior to computing the value.
- Applies per task/task-set in agentic tool-use settings (e.g., repository-repair or browser-workflow tasks), computed after each evaluation round or release.
- Value is independent of pass/completion rate: it can shift substantially (e.g., 1.3 to 2.7) even when pass rates are nearly unchanged.
- Value rises when successful runs follow varied patterns (e.g., alternating inspection/verification, abbreviated traces under reduced budgets) and falls when successful runs converge on one common pattern (e.g., single retrieval-first or browser workflow).
LADDER:
L0: A score that describes how varied successful tool-use traces are for a task.
L1: A score that describes how varied successful tool-use traces are for a task. It is computed from completed successful runs across multiple independent attempts on that task. Successful runs are grouped by their structural tool-use pattern before the score is computed.
L2: A score that describes variation in the sequence of tool-use steps among successful traces for each task or task set in agentic tool-use evaluations, including repository-repair and browser-workflow tasks. It is computed only from completed successful runs, using multiple independent attempts per task, after those runs are clustered by structural tool-use pattern. Before scoring, traces are normalized for incidental file paths, the number of available tools, and task-instruction length. It is computed after each evaluation round or release. The value is separate from pass or completion rate: it can move from 1.3 to 2.7 while pass rates remain nearly unchanged. It rises when successful runs alternate inspection and verification or include several abbreviated traces under reduced budgets, and falls when successful runs converge on a retrieval-first sequence or a common browser workflow.

ITEM 8
CHECKLIST:
- A weaker (or held-out/third-party) task generator produces task specifications/scenarios, run separately per model family or generator pool, with executable checks/validators created for each task and withheld from the evaluated agents.
- Task-generation traces (and evaluated-agent traces) are withheld/kept hidden from the other side, preventing generators from observing evaluated-agent behavior.
- Output is measured as a count of executable task specifications (e.g., 2,160; 1,740; 1,200; 980), scored via executable validators/checks rather than human judgment.
- Applies to generating benchmark/evaluation task sets (e.g., data-management or operational tasks) before any system is run against them.
- Tasks are filtered/reviewed only for execution validity and duplicate surface form (or human-reviewed and rejected for ambiguous state transitions), reducing the final task count.
- The process is rerun or refreshed (new generators/validators) across model families or releases to prevent one task-writing distribution from dominating comparisons.
LADDER:
L0: It is a pre-evaluation task-set creation procedure whose immediate purpose is to supply held-out executable tasks for comparing systems.
L1: It is a pre-evaluation task-set creation procedure whose immediate purpose is to supply held-out executable tasks for comparing systems. Weaker task generators create specifications or scenarios separately for each model family or generator pool, and each task receives an executable validator or check. The checks and task-generation traces are withheld from evaluated systems, while generators do not observe evaluated-agent traces. Tasks are screened for execution validity and duplicate surface form, with human review rejecting ambiguous state transitions when used.
L2: It is a pre-evaluation task-set creation procedure whose immediate purpose is to supply held-out executable tasks for comparing systems. A weaker or third-party task generator creates specifications or scenarios separately for each model family or generator pool, before any system is run, and every task receives an executable validator or check. Task-generation traces and evaluated-agent traces are kept hidden from the other side, so generators cannot observe evaluated-agent behavior and evaluated systems cannot see task-generation traces. The output is a count of executable specifications, such as 2,160, 1,740, 1,200 paired tasks, or 980 multi-tool cases, read by executable checks rather than human judgment. Tasks are screened for execution validity and duplicate surface form; human review can reject ambiguous state transitions, reducing the count. It is used to generate data-management or operational benchmark and evaluation task sets, and is rerun or refreshed with new generators and validators across model families or releases to limit repeated generator patterns.

ITEM 9
CHECKLIST:
- ⟦TERM⟧ is assigned independently by two annotators per item, before deployment/before model results are inspected, and can be revised if hidden dependencies (e.g., unavailable credentials) are later discovered.
- ⟦TERM⟧ is a difficulty/capability-tier rating tied to expected performance, scored such that failures falling below an agent's assigned ⟦TERM⟧ are read as unexpected regressions rather than ordinary misses.
- ⟦TERM⟧ applies at the level of individual evaluation items/tasks within a multi-tier, multi-environment agent evaluation suite, assigned prior to running any system on the task.
- ⟦TERM⟧ predicts observed failure rates among lower-tier agents (e.g., accounting for 71% of observed failures), which is used to reduce the volume of failures forwarded for manual investigation.
- ⟦TERM⟧ must remain stable across independent adjudicators/annotators for an item to be included in reported results; items with unstable ⟦TERM⟧ are excluded.
- ⟦TERM⟧ can diverge from actual outcomes in specific ways (e.g., agents passing higher-tier items via narrow memorized procedures while failing lower-tier items), meaning it does not imply a single monotonic capability scale.
LADDER:
L0: A per-item difficulty and capability-tier rating used to state expected agent performance on an evaluation task.
L1: A per-item difficulty and capability-tier rating is used to state expected agent performance on an evaluation task. Two annotators assign it independently for each item before deployment or inspection of system results, and may revise it after finding a hidden dependency such as unavailable credentials. It places tasks relative to expected agent tiers, so failures below an agent’s assigned tier are treated as unexpected regressions rather than ordinary misses.
L2: A per-item difficulty and capability-tier rating is used to state expected agent performance on tasks in a multi-tier, multi-environment agent evaluation suite. Before any system is run or its results are inspected, two annotators independently assign the rating to each task; they may revise it when they discover hidden dependencies, including unavailable credentials. The rating identifies cases expected to exceed entry-tier capability and separates expected lower-tier failures from unexpected regressions in higher-tier systems. Failures below an agent’s assigned tier are flagged for audit rather than counted as ordinary misses. Among lower-tier agents, the rating predicted 71% of observed failures, reducing the number sent for manual investigation. Reported results include only items whose rating is stable across adjudicators. The rating is not a single monotonic capability scale: agents can pass higher-tier tasks through narrow memorized procedures while failing lower-tier tasks with unfamiliar tool states.

ITEM 10
CHECKLIST:
- Agents replay/reuse action sequences (search, validation, credential-reset, tool-call patterns) from a prior successful task onto a new, subsequent task with an incompatible or unrelated state.
- Occurs specifically when the prior task ended in a high-confidence or resource-constrained success immediately preceding the new task (e.g., billing-repair before access-control or incident-response tasks).
- Measured as a percentage rate of occurrence across subsequent tasks (e.g., 14%, 12.4%), which drops sharply (e.g., to 3%, 2.6%, or by 79%) when prior-session/history traces are cleared between tasks.
- Applies within ordered, multi-task sessions where task order is fixed and session history/state persists across tasks.
- Is tied to prior trace length rather than prior answer correctness, and persists even when redundant page openings are reduced or tool quotas are increased.
- Clearing session history between tasks is the constraint shown to reduce it, though this may modestly increase tool setup time and does not meaningfully change ordinary same-domain task performance.
LADDER:
L0: It is a session-level error pattern used to identify inappropriate carryover from one task to the next.
L1: It is a session-level error pattern used to identify inappropriate carryover from one task to the next. Agents replay or reuse search, validation, credential-reset, or tool-call sequences from a prior successful task on a subsequent task whose state is incompatible or unrelated, especially when the preceding success was high-confidence or resource-constrained.
L2: It is a session-level error pattern used to identify inappropriate carryover from one task to the next in ordered, multi-task sessions with fixed task order and persistent history or state. Agents replay or reuse search, validation, credential-reset, or tool-call sequences from a prior successful task on a subsequent task with an incompatible or unrelated state, especially immediately after a high-confidence or resource-constrained success, such as billing repair before access-control or incident-response work. It is read as the percentage of subsequent tasks showing this pattern, such as 14% or 12.4%. The rate drops sharply when session-history traces are cleared between tasks, such as from 14% to 3%, from 12.4% to 2.6%, or by 79%. It is associated with prior trace length rather than prior answer correctness, persists despite fewer redundant page openings or higher tool quotas, and history clearing may modestly increase tool setup time without meaningfully changing ordinary same-domain performance.
