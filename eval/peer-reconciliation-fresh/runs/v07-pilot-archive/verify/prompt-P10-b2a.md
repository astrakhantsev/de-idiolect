Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A per-item evaluation label that sets an expected capability boundary for interpreting agent failures.

DEFINITION L1 (adds mechanism): For each item, two annotators independently assign the label before deployment and before model results are inspected. It may later be revised when hidden dependencies, such as unavailable credentials, are found. An agent’s actual performance is compared with the item’s assigned boundary to identify failures that warrant audit.

DEFINITION L2 (adds measurement and conditions): The label is a preassigned, revisable per-item capability boundary for an evaluation suite spanning three capability tiers and two execution environments. Two annotators independently assign it to every item before deployment and before model results are inspected; 4.7% of assignments were later revised after hidden dependencies on unavailable credentials were discovered. It is used to predict failures, correctly identifying 71% of observed failures among lower-tier agents. Results are read by comparing actual agent performance with the assigned boundary: failures below it are flagged for audit rather than counted as ordinary misses. Reporting retains only items whose assignments are stable across adjudicators and excludes unstable items. This exhaustion analysis does not establish one monotonic capability scale, because an agent can complete higher-tier items through narrow memorized procedures while failing lower-tier tasks that require unfamiliar tool states.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Set a ⟦TERM⟧ of three on the new codebase-navigation benchmark, figuring it'd force the agent to actually hold file contents in working memory instead of treating disk as free scratch space. First real run, agent fails outright — opened auth.py four times chasing down a decorator it kept forgetting the signature of.
2. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦TERM⟧ it ignores rereads that would help it finish, but under ⟦X⟧ it also doesn't compress. Not a great week for this benchmark.
3. Spent Monday convinced our ⟦TERM⟧ enforcement had silently broken, because three agents that used to pass the file-navigation suite started failing en masse.
4. Capped the day off by setting a ⟦TERM⟧ on the onboarding suite for the first time, since half of what's inflating the pass-everything bucket in that census looks like agents brute-forcing through repeated file opens instead of actually reasoning. Ration of three, rerunning tomorrow, expecting the pass-everything number to finally move.