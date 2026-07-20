Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A checking procedure that resubmits a scored answer unchanged except for reformatting to test whether the grader gives a consistent verdict.

DEFINITION L1 (adds mechanism): A checking procedure that tests a grader's consistency by resubmitting an already-scored answer with only its line breaks or whitespace reflowed and no change to the actual content. The reformatted answer is sent back through the same grader that scored it originally, and its new verdict is compared against the verdict from the first submission. When the two otherwise-identical submissions receive different verdicts, that answer is counted as having flipped.

DEFINITION L2 (adds measurement and conditions): A checking procedure for grader or scorer passes over question-answer or model-produced answers that tests whether the grader returns a consistent verdict when nothing meaningful has changed. An already-scored answer is resubmitted through the same grader with only its line breaks or whitespace reflowed or reformatted, the content held identical. The original verdict is then compared against the verdict on the reformatted resubmission, and a difference between the two is read as a flip. It is applied especially after a mid-run change of the model producing the answers, or when the grader seems inconsistent on long-form responses. What it produces is a flip rate — the count of answers whose verdict changed out of the total resubmitted — which is reported as a measure of grader noise.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. The same completed answers were then submitted to the scorer on four dates separated by at least 21 days. ⟦TERM⟧ was estimated from the resulting numeric-score pairs across 600 answers. ⟦TERM⟧ was 0.93 for repository-state tasks and 0.71 for open-ended incident reports.
2. ⟦TERM⟧ was estimated from the resulting numeric-score pairs across 600 answers. ⟦TERM⟧ was 0.93 for repository-state tasks and 0.71 for open-ended incident reports. Lower stability coincided with borderline partial-credit judgments rather than with answer length.
3. The automated scorer was repeated one month later; ⟦TERM⟧ remained above 0.90 for these task outcomes. The experiment cannot determine whether substitution effects arise from prior exposure or from unmeasured differences in the newly authored tasks.
4. ⟦TERM⟧ was estimated from repeated submissions of every final answer across two collection dates. ⟦TERM⟧ was 0.88, indicating that the observed recovery difference was not explained by unstable scoring alone.
5. ⟦TERM⟧ was estimated from repeated submissions of every final answer across two collection dates. ⟦TERM⟧ was 0.88, indicating that the observed recovery difference was not explained by unstable scoring alone.
6. ⟦TERM⟧ was computed over four scorer submissions per answer. ⟦TERM⟧ exceeded 0.90 for executable-task outcomes but was lower for explanatory summaries.