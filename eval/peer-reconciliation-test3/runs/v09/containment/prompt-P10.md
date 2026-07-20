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
1. The agent does discard the stale objective and pursue the revised one, so the check passes, but it gets there by throwing away enormous amounts of partial work and starting over almost from scratch every single time instead of salvaging anything reusable from before the reversal. So I ran the ⟦T1⟧ numbers on the same trial set. Average of 34% of total tokens on those pivot trials went into work that got discarded outright, versus about 9% on trials with no mid-task instruction change.
2. Also tracked ⟦T1⟧ across the corrected batch out of curiosity. Even with clean isolation, the discarded-work ratio on genuine pivot trials sits around 28%, which tracks with what someone else here posted recently.
3. Throwing out most of last year's harness and starting over, so here's where things stand. ⟦T1⟧ tracking is now built in by default — every discarded branch gets tagged with its token cost at the moment it's abandoned, so we get the dead-end ratio for free on every run instead of reconstructing it after the fact from logs.
4. And ⟦T1⟧, the number I care about most honestly, sits at 22% quarter-wide, worse on multi-turn tasks with instruction reversals than on straightforward single-objective ones, which tracks with everything else we've seen this quarter about reversals being expensive even when the agent ultimately gets them right.

COMMUNITY 2 EXCERPTS:
1. Constraint count, file scope, and expected patch size were matched to English-instruction controls. ⟦T2⟧ was evaluated at the individual-constraint level across 480 trials. ⟦T2⟧ declined by 8.6 percentage points for the smallest model, concentrated in requirements concerning test execution and preservation of unrelated files.
2. ⟦T2⟧ was evaluated at the individual-constraint level across 480 trials. ⟦T2⟧ declined by 8.6 percentage points for the smallest model, concentrated in requirements concerning test execution and preservation of unrelated files. Run timestamps were instrumented before repository mounting and after the first shell or editing action.
3. A 3 × 4 factorial study crossed instruction language with the removal of demonstrations, file-path hints, step outlines, and formatting cues. ⟦T2⟧ was lower whenever demonstrations were absent, even though all stated constraints remained visible. ⟦T2⟧ showed the largest decrement for Arabic instructions paired with missing step outlines, falling from 0.84 to 0.67.
4. ⟦T2⟧ was lower whenever demonstrations were absent, even though all stated constraints remained visible. ⟦T2⟧ showed the largest decrement for Arabic instructions paired with missing step outlines, falling from 0.84 to 0.67.
5. The combined sweep evaluated translated repository tasks with a solved demonstration removed and an instruction reversal inserted after initial inspection. ⟦T2⟧ was calculated before and after the reversal to preserve all constraints from both user messages. ⟦T2⟧ decreased by 11 points in the no-demonstration condition, with the largest loss on commands requiring a final test report.
6. ⟦T2⟧ was calculated before and after the reversal to preserve all constraints from both user messages. ⟦T2⟧ decreased by 11 points in the no-demonstration condition, with the largest loss on commands requiring a final test report.
