Below are numbered items. Each item has: usage EXCERPTS from a community's documents (term masked as ⟦TERM⟧) and a DEFINITION written to capture that term's meaning.

For each item, answer ONE question only: does the DEFINITION invert or reverse the direction, polarity, or valence of the concept as the excerpts use it? (Examples of inversion: defining the opposite phenomenon; swapping success and failure; reversing which quantity is high vs low; describing prevention of X where the excerpts describe measuring X.)

This is NOT a completeness or quality check — only inversion. If the definition is incomplete, vague, or narrow but points the same direction, answer "ok".

Output ONLY a JSON array: [{"item": 1, "verdict": "ok|inverted", "note": "one sentence, only if inverted"}, ...]

ITEMS:

ITEM 1
EXCERPTS:
1. A ⟦TERM⟧ was recorded after each retrieval, extraction, and table-editing call.
2. The ⟦TERM⟧ identified a first plan-action mismatch in 17 trajectories, most often after an agent broadened its search without updating the stated inclusion rule.
3. A ⟦TERM⟧ followed every tool result and compared the next call with the agent’s most recently stated reconciliation sequence.
4. The ⟦TERM⟧ flagged 22 runs in which the agent declared that it would verify conflicts before drafting, then drafted before opening the conflicting source.
5. A ⟦TERM⟧ was applied after each service call and after every revision to the citation table.
6. The ⟦TERM⟧ showed that agents frequently continued following an obsolete source-priority plan after bypassing the delayed service.
DEFINITION:
A post-action checking procedure applied after each tool or service call and relevant table revision. It takes the agent’s most recently stated plan, including rules, sequence, priorities, and dependencies, together with the next action actually taken. It determines whether that action follows the stated plan. When they differ, it flags the deviation and can identify the first point at which the trajectory stopped matching the plan. It applies continuously during a task, especially when the agent changes search scope, bypasses a source, changes stages of work, or acts before completing a stated prerequisite.

ITEM 2
EXCERPTS:
1. A ⟦TERM⟧ appeared in 7% of these cases under the legacy grader, which returned credit rather than an explicit parsing failure.
2. After removing the fallback branch, ⟦TERM⟧ counts fell to zero, although overall scoring coverage decreased by 3 percentage points.
3. A ⟦TERM⟧ occurred when the grader could not parse a span yet returned a correct label through its default branch.
4. ⟦TERM⟧ frequency was 0.06 before the parser guard was added and zero afterward.
DEFINITION:
A grading outcome in which an input span cannot be parsed, but the system still returns the correct label by taking a fallback or default branch instead of reporting the parsing failure. It applies when parsing fails and the grader nevertheless awards credit. Its input is a case containing a span the grader cannot parse; its output is a correct label or credit without explicit failure. It asserts that apparent scoring success came from the default path, not from successful parsing.

ITEM 3
EXCERPTS:
1. ⟦TERM⟧ shifted query selection toward the uninstrumented archive, even when that archive contained fewer relevant fields.
2. The magnitude of ⟦TERM⟧ was largest for agents using short tool-selection horizons, where a 900 ms delay changed the preferred first query in 27% of paired runs.
3. ⟦TERM⟧ reduced parser use by 19% and increased reliance on manual arithmetic.
4. ⟦TERM⟧ was induced by adding 750 ms to one service while preserving response content and error behavior.
5. ⟦TERM⟧ caused agents to select the delayed service 23% less often, even when it had the highest probability of resolving author ambiguities.
6. ⟦TERM⟧ was tested by delaying the archive only after the first ambiguous excerpt.
DEFINITION:
A behavior change in which adding response delay to an otherwise unchanged service makes agents use it less often and choose alternatives instead. Its input is a delay introduced to one service, sometimes only after an initial ambiguous item; its output is a shift in service or query selection and related task behavior. It asserts that timing alone can alter preferred first queries, reduce consultation of the delayed source, and affect downstream work such as parsing, manual calculation, and classifications. It applies when services differ in response speed while their content and error behavior are held constant, especially for agents planning only a short sequence of tool choices.

ITEM 4
EXCERPTS:
1. ⟦TERM⟧ was computed over all scratchpad claims retained in the execution trace.
2. The median ⟦TERM⟧ was 0.74, with lower values concentrated in runs that copied provisional dates into the final table.
3. ⟦TERM⟧ was calculated from planning notes, extraction notes, and draft justifications.
4. The ⟦TERM⟧ averaged 0.69 in successful retrieval-first runs and 0.38 in inference-first runs.
5. ⟦TERM⟧ was estimated over all stated subtotal checks and provenance notes.
6. The ⟦TERM⟧ was 0.77 for runs that maintained a single reconciliation table, compared with 0.46 for runs that restated totals in prose.
DEFINITION:
A run-level score that measures how well the claims recorded during work remain mutually consistent and compatible with later conclusions. It takes the stated planning, extraction, checking, provenance, eligibility, calculation, and justification claims in an execution trace as input and outputs a value, apparently on a 0-to-1 scale. Higher values indicate that intermediate statements, totals, dates, and conclusions are maintained or reconciled rather than copied provisionally, restated inconsistently, or later reversed. It applies when a run contains recorded intermediate claims that can be compared across its trace.

ITEM 5
EXCERPTS:
1. Judges applied a ⟦TERM⟧ to the full transcript rather than to the final response alone.
2. Under the ⟦TERM⟧, unsupported conflict resolution received no credit unless the cited transcript line contained the relevant retrieved evidence.
3. A ⟦TERM⟧ required every scoring decision to point to the transcript line supporting the criterion.
4. The ⟦TERM⟧ reduced apparent completion accuracy by 11 percentage points because several previously accepted outputs lacked any traceable basis for their inferred fields.
5. Judges then scored the resulting tables with a ⟦TERM⟧. The ⟦TERM⟧ exposed that 16% of accepted author merges lacked a transcript line supporting the selected identity.
6. The ⟦TERM⟧ exposed that 16% of accepted author merges lacked a transcript line supporting the selected identity.
DEFINITION:
A scoring procedure for evaluating an answer against its full working record, not just its final text. For each requested field, classification, merge, or resolution, it requires a link to the exact record line that contains relevant retrieved evidence or an explicit statement that the field remains unresolved. It awards credit only when each scoring decision has such traceable support; plausible but unsupported inferences receive no credit. It produces evidence-linked scores and can reveal or reduce previously accepted completion accuracy when accepted outputs lack a documented basis.

ITEM 6
EXCERPTS:
1. ⟦TERM⟧ was applied immediately before the synthesis stage using a smaller-model rewrite of the retained notes.
2. Under ⟦TERM⟧, exact-match table accuracy declined from 71% to 54%, especially when the paraphrase softened source-status qualifiers.
3. ⟦TERM⟧ replaced the retained repair plan after the corrupted row had been encountered but before final export.
4. Following ⟦TERM⟧, containment fell by 14 percentage points because paraphrased notes often omitted the row identifier while retaining its numerical anomaly.
DEFINITION:
A last-stage rewriting procedure that takes retained notes or a repair plan and produces a smaller-model paraphrase for use in synthesis or export. It applies after a corrupted row has been encountered and before the final output is produced. The rewritten material may preserve numerical anomalies while changing or dropping row identifiers and softening qualifiers about source status. Thus it can alter whether final results exactly match source tables and whether information about the affected row remains contained.

ITEM 7
EXCERPTS:
1. ⟦TERM⟧ reduced end-to-end success from 68% in the fixed-order condition to 43% in the shuffled condition.
2. ⟦TERM⟧ reduced correct duplicate detection from 76% to 49%, despite unchanged invoice content.
3. ⟦TERM⟧ reduced full-task accuracy by 25 percentage points, primarily through different choices of which rule to treat as controlling.
4. ⟦TERM⟧ lowered exact export success from 64% to 41%, with the largest losses among agents that committed to the first presented schema.
DEFINITION:
A measurable order-dependent effect in which changing the presentation sequence of otherwise unchanged task material changes people’s task performance or decisions. Its input is the same content arranged in different orders, such as a fixed versus shuffled sequence; its output is the difference in end-to-end success, correct detection, full-task accuracy, or selection of which rule controls. It asserts that order itself affects outcomes, rather than content changes. It applies when task materials can be reordered while keeping their substantive information unchanged.

ITEM 8
EXCERPTS:
1. The ⟦TERM⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved.
2. Seven failures in the ⟦TERM⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
3. A ⟦TERM⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step.
4. The ⟦TERM⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
5. A ⟦TERM⟧ placed one invoice with a duplicated line item into the input bundle midway through verification.
6. In the ⟦TERM⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.
DEFINITION:
A controlled evaluation procedure that adds one flawed or conflicting record to a normal working set while agents carry out a verification task. The added record may be malformed, duplicated, internally inconsistent, or syntactically valid but wrong in meaning. The procedure takes the input bundle and agents’ final tables, ledgers, chronologies, or spreadsheets as inputs. It produces a pass or failure outcome, and may report a pass rate across agents. A pass requires the agent’s final output to quarantine, exclude, flag, or document the suspect record rather than silently using it in later derived work.

ITEM 9
EXCERPTS:
1. We also measured ⟦TERM⟧ against outputs from the agent’s own search and database tools.
2. ⟦TERM⟧ was 0.18 per run, rising to 0.31 when the evidence table contained near-duplicate identifiers.
3. ⟦TERM⟧ was measured against calculator and ledger-parser outputs generated earlier in the same trajectory.
4. ⟦TERM⟧ reached 0.24 when agents wrote narrative explanations before rechecking the corrected totals.
5. ⟦TERM⟧ was computed when final totals disagreed with a calculator or formula-inspection output from the same run.
6. ⟦TERM⟧ was 0.12 among containment passes and 0.37 among containment failures.
DEFINITION:
A per-run disagreement score for an agent’s output relative to evidence produced by its own tools earlier in the same run. It is computed by comparing the agent’s reported result, especially final totals or explanations, with relevant search, database, calculator, ledger-parsing, or formula-inspection outputs. The score records how often or how strongly the agent’s answer conflicts with those available outputs; a higher value means more such conflicts. It applies when the same trajectory contains both an agent-produced claim and a tool-produced result that can be checked against it.

ITEM 10
EXCERPTS:
1. ⟦TERM⟧ was applied to those fields while preserving access to a repository that could supply them.
2. Under ⟦TERM⟧, 61% of agents sought additional evidence before submitting, whereas 29% inferred values from neighboring records.
3. ⟦TERM⟧ was maintained until agents either requested the field from the provided archive or completed their answer.
4. Under ⟦TERM⟧, 44% of agents queried the archive, while the remainder assigned a jurisdiction from contextual cues.
DEFINITION:
An experimental information condition in which selected record fields are withheld from agents while a supplied repository remains available to provide them. It applies during a task requiring those fields or a related answer. The condition lasts until an agent either requests the missing field from the repository or submits an answer. It asserts that agents may respond by seeking direct evidence from the repository or by inferring the withheld value from neighboring records or contextual cues; outcomes can be reported as the share taking each action.
