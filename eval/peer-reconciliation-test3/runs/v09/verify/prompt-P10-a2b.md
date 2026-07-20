Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A measurement score that captures how much of an agent's work is thrown away when a task's goal is changed partway through.

DEFINITION L1 (adds mechanism): A measurement score that captures how much of an agent's work is thrown away when a task's goal is changed partway through, rather than reused. It works by measuring the fraction of an agent's effort that gets discarded when the task objective is revised mid-task, for example when an instruction is reversed, instead of being salvaged for the new goal. Each abandoned branch of work is tagged with its token cost at the moment it is given up, and those costs are summed.

DEFINITION L2 (adds measurement and conditions): A measurement score that captures how much of an agent's work is thrown away when a task's goal is changed partway through, rather than salvaged and reused. It measures the ratio, as a percentage, of tokens spent on discarded or abandoned work versus tokens spent on work that is kept, computed per trial or aggregated across a batch or quarter. It is built from the token cost of each abandoned branch, tagged at the moment that branch is given up, so the ratio comes directly from each run instead of being reconstructed from logs. It applies to multi-turn or pivot tasks where a mid-task instruction change or objective reversal occurs, and is contrasted against straightforward single-objective tasks with no instruction change. Trials with a reversal show substantially higher discarded-work ratios, roughly 22 to 34 percent in these excerpts, than non-pivot trials at about 9 percent.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Constraint count, file scope, and expected patch size were matched to English-instruction controls. ⟦TERM⟧ was evaluated at the individual-constraint level across 480 trials. ⟦TERM⟧ declined by 8.6 percentage points for the smallest model, concentrated in requirements concerning test execution and preservation of unrelated files.
2. ⟦TERM⟧ was evaluated at the individual-constraint level across 480 trials. ⟦TERM⟧ declined by 8.6 percentage points for the smallest model, concentrated in requirements concerning test execution and preservation of unrelated files. Run timestamps were instrumented before repository mounting and after the first shell or editing action.
3. A 3 × 4 factorial study crossed instruction language with the removal of demonstrations, file-path hints, step outlines, and formatting cues. ⟦TERM⟧ was lower whenever demonstrations were absent, even though all stated constraints remained visible. ⟦TERM⟧ showed the largest decrement for Arabic instructions paired with missing step outlines, falling from 0.84 to 0.67.
4. ⟦TERM⟧ was lower whenever demonstrations were absent, even though all stated constraints remained visible. ⟦TERM⟧ showed the largest decrement for Arabic instructions paired with missing step outlines, falling from 0.84 to 0.67.
5. The combined sweep evaluated translated repository tasks with a solved demonstration removed and an instruction reversal inserted after initial inspection. ⟦TERM⟧ was calculated before and after the reversal to preserve all constraints from both user messages. ⟦TERM⟧ decreased by 11 points in the no-demonstration condition, with the largest loss on commands requiring a final test report.
6. ⟦TERM⟧ was calculated before and after the reversal to preserve all constraints from both user messages. ⟦TERM⟧ decreased by 11 points in the no-demonstration condition, with the largest loss on commands requiring a final test report.