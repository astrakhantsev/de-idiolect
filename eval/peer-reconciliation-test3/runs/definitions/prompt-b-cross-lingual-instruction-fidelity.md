Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Measures whether all stated constraints in an instruction (e.g., test execution requirements, preservation of unrelated files, formatting cues) are satisfied in a coding/repository-editing task, scored as a fraction or percentage of constraints met.
- Evaluated at the individual-constraint level, aggregated across many trials (e.g., 480 trials) to yield a score.
- Applies to instruction-following on repository/code-editing tasks, including cases with translated (non-English) instructions and cases where a demonstration, file-path hint, step outline, or formatting cue is removed.
- Can be computed at two points around an instruction reversal inserted mid-task, comparing before vs. after while requiring constraints from both the original and reversed messages to still be preserved.
- Drops when solved demonstrations are absent, even when all stated constraints remain visible in the instructions.
- Shows a persistent gap for non-English instructions (e.g., Spanish, Arabic) relative to an English-instruction control, with the largest losses concentrated on requirements like test execution or producing a final test report.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Constraint count, file scope, and expected patch size were matched to English-instruction controls. ⟦TERM⟧ was evaluated at the individual-constraint level across 480 trials. ⟦TERM⟧ declined by 8.6 percentage points for the smallest model, concentrated in requirements concerning test execution and preservation of unrelated files.
2. ⟦TERM⟧ was evaluated at the individual-constraint level across 480 trials. ⟦TERM⟧ declined by 8.6 percentage points for the smallest model, concentrated in requirements concerning test execution and preservation of unrelated files. Run timestamps were instrumented before repository mounting and after the first shell or editing action.
3. A 3 × 4 factorial study crossed instruction language with the removal of demonstrations, file-path hints, step outlines, and formatting cues. ⟦TERM⟧ was lower whenever demonstrations were absent, even though all stated constraints remained visible. ⟦TERM⟧ showed the largest decrement for Arabic instructions paired with missing step outlines, falling from 0.84 to 0.67.
4. ⟦TERM⟧ was lower whenever demonstrations were absent, even though all stated constraints remained visible. ⟦TERM⟧ showed the largest decrement for Arabic instructions paired with missing step outlines, falling from 0.84 to 0.67.
5. The combined sweep evaluated translated repository tasks with a solved demonstration removed and an instruction reversal inserted after initial inspection. ⟦TERM⟧ was calculated before and after the reversal to preserve all constraints from both user messages. ⟦TERM⟧ decreased by 11 points in the no-demonstration condition, with the largest loss on commands requiring a final test report.
6. ⟦TERM⟧ was calculated before and after the reversal to preserve all constraints from both user messages. ⟦TERM⟧ decreased by 11 points in the no-demonstration condition, with the largest loss on commands requiring a final test report.
7. ⟦TERM⟧ was evaluated in a Spanish-instruction subset embedded in the same replay corpus. ⟦TERM⟧ remained 0.09 below the English control despite the recovery improvement.
8. ⟦TERM⟧ was evaluated in a Spanish-instruction subset embedded in the same replay corpus. ⟦TERM⟧ remained 0.09 below the English control despite the recovery improvement.