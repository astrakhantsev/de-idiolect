Two communities each use their own term for practices that are known to be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Question: comparing the SETS of situations the two communities' excerpts describe —

- "t1_within_t2": everything ⟦T1⟧'s excerpts describe is also an instance of what ⟦T2⟧'s excerpts describe; ⟦T2⟧ additionally covers situations ⟦T1⟧'s excerpts do not (⟦T1⟧ is a special case of ⟦T2⟧).
- "t2_within_t1": the mirror case (⟦T2⟧ is a special case of ⟦T1⟧).
- "partial_overlap": the two share a common core, but EACH side also covers situations the other side's excerpts do not.
- "unclear": the excerpts do not support any of the above.

Judge only from the excerpts. A shared purpose is not containment — attend to the concrete mechanisms and conditions each side commits to.

Output ONLY JSON: {"relation": "t1_within_t2" | "t2_within_t1" | "partial_overlap" | "unclear", "justification": "one or two sentences citing the decisive difference"}

COMMUNITY 1 EXCERPTS:
1. Set a ⟦T1⟧ of three on the new codebase-navigation benchmark, figuring it'd force the agent to actually hold file contents in working memory instead of treating disk as free scratch space. First real run, agent fails outright — opened auth.py four times chasing down a decorator it kept forgetting the signature of.
2. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦T1⟧ it ignores rereads that would help it finish, but under ⟦X⟧ it also doesn't compress. Not a great week for this benchmark.
3. Spent Monday convinced our ⟦T1⟧ enforcement had silently broken, because three agents that used to pass the file-navigation suite started failing en masse.
4. Capped the day off by setting a ⟦T1⟧ on the onboarding suite for the first time, since half of what's inflating the pass-everything bucket in that census looks like agents brute-forcing through repeated file opens instead of actually reasoning. Ration of three, rerunning tomorrow, expecting the pass-everything number to finally move.

COMMUNITY 2 EXCERPTS:
1. Items carried a ⟦T2⟧ assigned independently by two annotators before deployment. The ⟦T2⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation.
2. Items carried a ⟦T2⟧ assigned independently by two annotators before deployment. The ⟦T2⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation. Disagreements were concentrated in items involving chained browser actions rather than answer extraction.
3. Results therefore exclude halted ⟦X⟧ batches and report only items whose ⟦T2⟧ was stable across adjudicators.
4. The evaluation suite contained 3,050 tasks spanning three capability tiers and two execution environments. Every item received a ⟦T2⟧ before model results were inspected. The ⟦T2⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
5. Every item received a ⟦T2⟧ before model results were inspected. The ⟦T2⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
6. Removing exhausted items increased rank stability across weekly reruns. Failures below an agent’s ⟦T2⟧ were flagged for audit rather than treated as ordinary misses. The ⟦T2⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states.
