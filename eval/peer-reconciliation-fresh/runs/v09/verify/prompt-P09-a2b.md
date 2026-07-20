Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A running log kept over time in which each change to a task's settings is recorded, so that later observed results can be traced back to what was changed.

DEFINITION L1 (adds mechanism): A running log in which each change to a setting or parameter — such as a naming scheme, a cap value, a ration increase, or a set of rewordings — is written down as its own separate entry, timestamped, at the moment it is made, noting what changed and when. When an unexpected or worse-than-expected result later appears, the log is read back through, entry by entry, to find the specific change that actually produced it. Every change is entered, even ones that seem too small to matter, and each is recorded the same day it happens so the tie between a change and its effect is not forgotten.

DEFINITION L2 (adds measurement and conditions): A running log in which each change to a task's configuration or parameters — a naming scheme, a cap value, a ration increase, a wording change, and so on — is written as a separate, timestamped entry the moment it is made, stating exactly what changed and when so distinct changes stay individually attributable to distinct outcomes. What it produces is an ordered, dated record; it is 'read' by scrolling back through the entries to locate the one change responsible for an observed result. It is consulted whenever an unexpected result or a regression shows up, to tell a genuine change in ability apart from an artifact of the setup, and it must be updated the same day a change is made rather than deferred, or the causal link is lost. Every change is logged, including ones that feel too minor to matter, because those are the ones most easily forgotten.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Agents completed 600 repository-repair tasks with five independent attempts per task and fresh tool sandboxes. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
2. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
3. Prompt templates included two worked examples with unusual connective phrases. The ⟦X⟧ found that agents with the highest ⟦TERM⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
4. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged.
5. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged. This pattern held after normalizing for the number of available tools and the length of task instructions.
6. Under that round, the ⟦TERM⟧ remained elevated for agents that alternated inspection and verification rather than following a fixed retrieval-first sequence. The result should be interpreted cautiously because generator diversity also changed the distribution of error messages.