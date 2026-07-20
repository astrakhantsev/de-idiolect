Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A fixed numeric limit set on an agent benchmark run that caps how many times the agent may open or reread a single file's contents, so it can't lean on disk as free scratch space.

DEFINITION L1 (adds mechanism): A fixed numeric cap on how many times an agent may open or reread the same file's contents during a benchmark run. It is set as a count of allowed file-open actions (for example, three) applied per file. Once that count is reached, any further reread of that file—even one that would help the agent finish—is ignored or blocked instead of granted.

DEFINITION L2 (adds measurement and conditions): A fixed numeric limit, set as a count of allowed file-open or reread actions (for example, three) applied per file, on how many times an agent may reopen the same file's contents during a benchmark run. It applies while an agent reads files as it works through benchmark suites such as codebase-navigation, file-navigation, and onboarding tasks. Each reopen of a given file counts against that file's allowance; once the count is reached, further rereads are ignored or blocked rather than granted, so an agent still needing to reread cannot proceed. Exceeding the allowance triggers the agent's failure or cuts the task off mid-run. It is read purely as a pass-or-fail gate: the agent does not compress or adapt its reading in response—it keeps reading at the same pace until it fails or is cut off.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation.
2. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation. Disagreements were concentrated in items involving chained browser actions rather than answer extraction.
3. Results therefore exclude halted ⟦X⟧ batches and report only items whose ⟦TERM⟧ was stable across adjudicators.
4. The evaluation suite contained 3,050 tasks spanning three capability tiers and two execution environments. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
5. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
6. Removing exhausted items increased rank stability across weekly reruns. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states.