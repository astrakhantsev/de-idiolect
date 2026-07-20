Two communities each use their own term for practices that may or may not be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧). Other local jargon is masked as ⟦X⟧.

Question: comparing the SETS of situations the two communities' excerpts describe —

- "t1_within_t2": everything ⟦T1⟧'s excerpts describe is also an instance of what ⟦T2⟧'s excerpts describe, and ⟦T2⟧ additionally covers situations ⟦T1⟧'s excerpts do not (⟦T1⟧ is a special case of ⟦T2⟧).
- "t2_within_t1": the mirror case (⟦T2⟧ is a special case of ⟦T1⟧).
- "partial_overlap": the two share a specific common core, but EACH side also covers situations the other side's excerpts do not.
- "no_relation": the two practices are not variants of one another — there is no specific common core beyond generic evaluation practice.
- "unclear": the excerpts do not decisively support any of the above.

Judge only from the excerpts. Do not assume the terms are related. A shared purpose is not containment — attend to the concrete mechanisms and conditions each side commits to.

For every answer EXCEPT "unclear", give one verbatim quote from EACH community's excerpts carrying the decisive evidence: "quote_1" copied exactly from community 1's excerpts, "quote_2" copied exactly from community 2's excerpts. For "unclear", leave both quotes as empty strings.

Output ONLY JSON:
{"relation": "t1_within_t2" | "t2_within_t1" | "partial_overlap" | "no_relation" | "unclear", "quote_1": "...", "quote_2": "...", "justification": "one or two sentences citing the decisive evidence"}

COMMUNITY 1 EXCERPTS:
1. The other 10% just started re-reading the whole repo from scratch like it had amnesia, which cost us real wall clock time. Last thing: we ⟦T1⟧ every ⟦X⟧ output because we don't trust a single grader pass after a mid-run model change. Reflowed the diffs, resubmitted, and got two different verdicts on 4 of 60 answers even though the content was identical.
2. Last thing, we ⟦T1⟧ed a batch of these QA answers after noticing the scorer seemed inconsistent on long-form responses. Reflowed line breaks, changed nothing else, resubmitted through the same grader. 9 out of 80 flipped verdicts.
3. Third, we caught a grader problem via ⟦T1⟧ — resubmitted 200 answers with reflowed formatting only, and 14 flipped, concentrated almost entirely in the brain-swapped low-score batch, which makes sense since terser cheap-model output apparently trips something in the scorer's whitespace handling.
4. ⟦T1⟧ stayed a nagging problem — 6% of resubmitted answers flip verdict on reflow alone across the whole corpus, and we still haven't root-caused the scorer's whitespace sensitivity, just flagged it as known noise in every report now.

COMMUNITY 2 EXCERPTS:
1. The same completed answers were then submitted to the scorer on four dates separated by at least 21 days. ⟦T2⟧ was estimated from the resulting numeric-score pairs across 600 answers. ⟦T2⟧ was 0.93 for repository-state tasks and 0.71 for open-ended incident reports.
2. ⟦T2⟧ was estimated from the resulting numeric-score pairs across 600 answers. ⟦T2⟧ was 0.93 for repository-state tasks and 0.71 for open-ended incident reports. Lower stability coincided with borderline partial-credit judgments rather than with answer length.
3. The automated scorer was repeated one month later; ⟦T2⟧ remained above 0.90 for these task outcomes. The experiment cannot determine whether substitution effects arise from prior exposure or from unmeasured differences in the newly authored tasks.
4. ⟦T2⟧ was estimated from repeated submissions of every final answer across two collection dates. ⟦T2⟧ was 0.88, indicating that the observed recovery difference was not explained by unstable scoring alone.
5. ⟦T2⟧ was estimated from repeated submissions of every final answer across two collection dates. ⟦T2⟧ was 0.88, indicating that the observed recovery difference was not explained by unstable scoring alone.
6. ⟦T2⟧ was computed over four scorer submissions per answer. ⟦T2⟧ exceeded 0.90 for executable-task outcomes but was lower for explanatory summaries.
