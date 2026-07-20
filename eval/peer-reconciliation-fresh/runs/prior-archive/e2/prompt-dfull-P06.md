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
1. That's a bigger presentation tax than I want to admit to leadership. And on ⟦T1⟧ — we had Palisade draft forty candidate eval questions about contract clauses, then used a second model to strip out the ones it thought Palisade would find trivial. Kept eighteen.
2. I think it explains why every agent we test does suspiciously well on off-by-one bugs and suspiciously badly on anything involving concurrency, because that's just what the generating model happened to be good at authoring. Made it worse when I found out a third of that tier was also produced through ⟦T1⟧ — one of our own agents wrote candidate bugs, a second model filtered the ones it judged too easy, and nobody checked whether the filter model shared blind spots with the author. Given the concurrency pattern above, I'd bet money it does.

COMMUNITY 2 EXCERPTS:
1. ⟦T2⟧ used anonymized final patches and rationales sampled from all systems in a round. During ⟦T2⟧, the evaluated agent agreed with external graders 6.4 points less often on its own successful patches than on matched patches from peers.
2. ⟦T2⟧ used anonymized final patches and rationales sampled from all systems in a round. During ⟦T2⟧, the evaluated agent agreed with external graders 6.4 points less often on its own successful patches than on matched patches from peers. The effect remained after excluding outputs with identifying filenames and unusually long explanations.
3. A second ⟦X⟧ after paraphrasing the examples reduced copied phrasing without changing ⟦T2⟧ effects.
4. Outputs from both task variants were then mixed into blinded grading pools. ⟦T2⟧ showed lower agreement on an agent’s own outputs, particularly when its rationale reused distinctive tool-log phrasing. In ⟦T2⟧, the self-output agreement deficit was 7.9 points under distractor context versus 3.2 points without it.
5. ⟦T2⟧ showed lower agreement on an agent’s own outputs, particularly when its rationale reused distinctive tool-log phrasing. In ⟦T2⟧, the self-output agreement deficit was 7.9 points under distractor context versus 3.2 points without it.
6. ⟦T2⟧ remained detectable after rationale text was removed and graders saw only final actions and validators. These results do not isolate whether self-recognition arose from stylistic traces, action ordering, or latent familiarity with the task.
