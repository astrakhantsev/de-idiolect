DEFINITION of a concept:

⟦TERM⟧ is a numeric limit, set per benchmark run, on how many times an agent may reopen or reread the same file or resource during that run (for example, three). It is enforced live while the agent executes: once the agent opens a given file more times than the limit allows, the run fails or is cut off mid-trace rather than being permitted further rereads. It applies to codebase- or file-navigation benchmarks where an agent repeatedly reopens a file—say, to recheck a function's signature—instead of holding that content in working memory. Exceeding it counts as a failure on that run, which can be rerun after the setting is changed or re-verified. It constrains only rereads, not compression of held content, which is governed separately under ⟦X⟧. Applying or tightening it is expected to lower aggregate pass rates by failing agents that had been succeeding through repeated file opens.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation.
2. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation. Disagreements were concentrated in items involving chained browser actions rather than answer extraction.
3. Results therefore exclude halted ⟦X⟧ batches and report only items whose ⟦TERM⟧ was stable across adjudicators.
4. The evaluation suite contained 3,050 tasks spanning three capability tiers and two execution environments. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
5. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
6. Removing exhausted items increased rank stability across weekly reruns. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states.