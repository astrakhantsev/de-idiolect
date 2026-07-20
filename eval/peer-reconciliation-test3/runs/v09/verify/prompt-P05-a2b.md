Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A controlled test that swaps only an agent's plan-generation step to a cheaper, lower-tier model to measure how much end-to-end task success depends on the quality of the planning step.

DEFINITION L1 (adds mechanism): A controlled test that swaps only an agent's plan-generation step to a cheaper, lower-tier model to measure how much end-to-end task success depends on the planning step. In an agent harness that separates a planning step from an execution step, the planning step is routed through a cheaper backend while the execution model is left unchanged. Task success is then run and compared against a same-setup baseline where both steps use the normal model.

DEFINITION L2 (adds measurement and conditions): A controlled test, applied to agent harnesses that separate a planning step from an execution step (such as a document-question-answering agent), that swaps only the plan-generation step to a cheaper, lower-tier model while keeping the subtask execution model unchanged, to measure how much end-to-end success depends on planning. It is run per session or task, and produces an end-to-end task success rate as a percentage, compared against a same-setup baseline. Position within a session must be controlled (a fresh-session first task versus a warmed-up later task), since failing to do so inflates the apparent effect. Results vary widely by task: sometimes near-noise (81% versus 83%), sometimes a collapse (79% down to 31%), and sometimes a consistent 20-to-40-point loss.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. The tool-selection module was then exchanged between two otherwise identical agent stacks. ⟦TERM⟧ was reported as the change in total actions relative to the original selector. ⟦TERM⟧ favored the compact selector on routine tasks, reducing action use by 18%, while increasing action use by 9% on multi-file tasks.
2. ⟦TERM⟧ was reported as the change in total actions relative to the original selector. ⟦TERM⟧ favored the compact selector on routine tasks, reducing action use by 18%, while increasing action use by 9% on multi-file tasks. The substituted selector made fewer redundant searches but issued more premature edits.
3. Agents that failed commonly retained a correct implementation of the original request and appended an incomplete revision. ⟦TERM⟧ was measured by replacing only the tool-selection module during the same interrupted runs. ⟦TERM⟧ was positive for the replacement selector, which consumed 4.3 additional actions on average after a reversal.
4. ⟦TERM⟧ was measured by replacing only the tool-selection module during the same interrupted runs. ⟦TERM⟧ was positive for the replacement selector, which consumed 4.3 additional actions on average after a reversal. The added actions were primarily repository searches used to re-establish context.
5. ⟦TERM⟧ was negative on standing tasks, reducing total actions by 12%, but positive on newly authored tasks by 5%. ⟦TERM⟧ therefore depended on whether the selector encountered familiar task structure.
6. ⟦TERM⟧ was negative on standing tasks, reducing total actions by 12%, but positive on newly authored tasks by 5%. ⟦TERM⟧ therefore depended on whether the selector encountered familiar task structure.