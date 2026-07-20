Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: replaces a portion of the standing benchmark's items (roughly 25–30%) with newly authored, difficulty/language-matched problems, substituted at the item level, without exposing item identities to model operators or annotators.
- Measures/produces: a completion or success score (e.g., aggregate completion rate or point score) compared before vs. after substitution, expressed as a point drop or completion-rate decrease.
- Applies in: benchmark evaluation cycles for code-repair/defect-fixing tasks, using untouched/unreplaced tasks as within-cycle controls.
- Constraint: new items must be matched to replaced items on language, test count, and/or estimated repair length (or nominal difficulty), preserving the original language distribution.
- Constraint: item identities are concealed from model operators and annotators during application.
- Effect pattern: produces a measurable score decline that varies by model (larger for legacy/less-tuned checkpoints, smaller for instruction-tuned ones) and can increase cross-seed variance, indicating reduced apparent generalization.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. A second evaluation cycle replaced 25% of the benchmark with newly authored defects matched by language, test count, and estimated repair length. ⟦TERM⟧ was applied without exposing item identities to model operators or annotators. ⟦TERM⟧ produced a 14.1-point score drop for the legacy checkpoint, whereas the instruction-tuned checkpoint dropped 3.7 points.
2. ⟦TERM⟧ was applied without exposing item identities to model operators or annotators. ⟦TERM⟧ produced a 14.1-point score drop for the legacy checkpoint, whereas the instruction-tuned checkpoint dropped 3.7 points. On the substituted subset, ⟦TERM⟧ also increased variance across random seeds, consistent with less reliable generalization than aggregate scores implied.
3. ⟦TERM⟧ produced a 14.1-point score drop for the legacy checkpoint, whereas the instruction-tuned checkpoint dropped 3.7 points. On the substituted subset, ⟦TERM⟧ also increased variance across random seeds, consistent with less reliable generalization than aggregate scores implied. The new defects were authored by the same internal team that maintained the standing suite, so stylistic continuity may have reduced the magnitude of the replacement effect.
4. A refreshed benchmark cycle replaced 30% of standing tasks while preserving language distribution and nominal difficulty. ⟦TERM⟧ was randomized at the item level, and untouched tasks remained available as within-cycle controls. ⟦TERM⟧ reduced aggregate completion from 0.76 to 0.69 for the model with the longest pretraining window.
5. ⟦TERM⟧ was randomized at the item level, and untouched tasks remained available as within-cycle controls. ⟦TERM⟧ reduced aggregate completion from 0.76 to 0.69 for the model with the longest pretraining window. The decline was concentrated in build-system repairs rather than in documentation tasks.
6. ⟦TERM⟧ supplied newly authored items to half of the final evaluation block. ⟦TERM⟧ produced an additional 6-point completion decline, but confidence intervals overlapped those from the language condition.
7. ⟦TERM⟧ supplied newly authored items to half of the final evaluation block. ⟦TERM⟧ produced an additional 6-point completion decline, but confidence intervals overlapped those from the language condition. The factorial design was not powered to identify interactions among all six factors.
8. ⟦TERM⟧ replaced one quarter of items in the last cycle with matched new problems. ⟦TERM⟧ lowered success by 9.8 points and increased the gap between intact and ablated prompts.
9. ⟦TERM⟧ replaced one quarter of items in the last cycle with matched new problems. ⟦TERM⟧ lowered success by 9.8 points and increased the gap between intact and ablated prompts.