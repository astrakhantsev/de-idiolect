Two communities each use their own term for practices that may be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Produce three artifacts:
1. "core" — in ordinary words (60–120), the largest SPECIFIC common core practice/phenomenon that BOTH sets of excerpts genuinely support. Must be more specific than generic evaluation practice ("testing agents", "measuring quality" do NOT count).
2. "residue_1" — what community 1's usage commits to that community 2's does NOT (in ordinary words, 20–60).
3. "residue_2" — what community 2's usage commits to that community 1's does NOT (20–60).

Core discipline: include quantifiers or restrictive details (e.g. "a single", "exactly one", "always", "binary") ONLY if BOTH communities' excerpts support them; do not use generalizing catch-all phrases ("or otherwise", "or any similar", "in any way"); anything supported by only one community belongs in that community's residue, NOT in the core.

Each artifact needs a verbatim supporting quote: "quote_core_1" and "quote_core_2" (one from each community supporting the core), "quote_residue_1" (from community 1), "quote_residue_2" (from community 2).

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON:
{"core": "...", "quote_core_1": "...", "quote_core_2": "...", "residue_1": "...", "quote_residue_1": "...", "residue_2": "...", "quote_residue_2": "..."}

COMMUNITY 1 EXCERPTS:
1. Genuinely impressive, first agent on our roster to pass that cleanly. Less happy about our ⟦T1⟧ results this week. Same underlying task, one variant phrased as a casual Slack message ("hey can you check this contract real quick"), the other as a formal request with numbered requirements.
2. We kept a suite alive for a year that stopped telling us anything for probably the last four months of it. Tried to console myself by running ⟦T1⟧ on the surviving 39%, pairing each item with a reworded twin — same ask, different formatting, bullet list versus prose. Gap was smaller than I expected, only 4 points on average, which is actually reassuring since it means the items still doing work aren't just measuring who parses markdown better.

COMMUNITY 2 EXCERPTS:
1. The benchmark paired each account-management task with a version containing irrelevant policy excerpts, historical tickets, and decoy URLs. ⟦T2⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦T2⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
2. ⟦T2⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦T2⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
3. A paired set of service-configuration tasks differed only in irrelevant operational context appended to the prompt. ⟦T2⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦T2⟧ preserved the same required configuration change, validator, and initial system state.
4. ⟦T2⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦T2⟧ preserved the same required configuration change, validator, and initial system state. Outputs from both task variants were then mixed into blinded grading pools.
5. The tool traces indicated that ⟦T2⟧ changed navigation breadth more than final answer length.
