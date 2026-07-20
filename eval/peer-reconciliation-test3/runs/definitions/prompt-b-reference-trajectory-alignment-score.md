Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: ⟦TERM⟧ is computed by comparing an agent's actual action sequence (e.g., inspection, transformation, validation, reporting steps) against an expert- or curator-authored reference route for the same task.
- Mechanism: it is computed/derived independently of and prior to checking final task success or answer correctness, so it can be scored even when outcomes are invalid or unchanged.
- What is measured: it produces an alignment score between the executed path and the reference route, expressed as a degree of match (e.g., "low alignment," "fell under support removal") rather than a pass/fail outcome.
- Scoring behavior: taking a shorter or unconventional path, skipping exploratory steps, or adding detours before completion lowers the score, even when the run succeeds.
- Setting/trigger: it is computed per completed run/trial in multi-step task execution (e.g., data-cleaning tasks, replayed tasks with swapped/replaced items).
- Constraint: it must be reported separately for successful and unsuccessful trials, since it is used to distinguish genuine constraint failures from mere changes in work pattern.
- Constraint: it correlates only moderately with pass rate, so it is not interchangeable with a success/correctness metric.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. For 220 data-cleaning tasks, expert annotators supplied action sequences covering file inspection, transformation, validation, and final reporting. ⟦TERM⟧ was computed before examining task success, so routes were retained even when their final artifacts were invalid. ⟦TERM⟧ correlated moderately with pass rate (r = 0.46), but several successful runs achieved low alignment by using shorter, unconventional paths.
2. ⟦TERM⟧ was computed before examining task success, so routes were retained even when their final artifacts were invalid. ⟦TERM⟧ correlated moderately with pass rate (r = 0.46), but several successful runs achieved low alignment by using shorter, unconventional paths. The largest disagreements involved agents that skipped exploratory inspection and directly executed a known validation command.
3. The difference persisted after controlling for response length and repository size. ⟦TERM⟧ was also computed for successful trials to distinguish constraint failures from altered work patterns. ⟦TERM⟧ fell under support removal even where tests passed, indicating more detours before completion.
4. ⟦TERM⟧ was also computed for successful trials to distinguish constraint failures from altered work patterns. ⟦TERM⟧ fell under support removal even where tests passed, indicating more detours before completion. This analysis is limited by using translations reviewed for semantic equivalence rather than translations optimized for naturalness in each language.
5. ⟦TERM⟧ was derived from curator-authored routes for all replayed tasks. ⟦TERM⟧ increased under the replacement selector even when the final answer was unchanged.
6. ⟦TERM⟧ was derived from curator-authored routes for all replayed tasks. ⟦TERM⟧ increased under the replacement selector even when the final answer was unchanged.
7. ⟦TERM⟧ was assessed independently of final success for all completed runs. ⟦TERM⟧ declined after hot-swapped items, even among passing trajectories.
8. ⟦TERM⟧ was assessed independently of final success for all completed runs. ⟦TERM⟧ declined after hot-swapped items, even among passing trajectories.