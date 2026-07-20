Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Resubmit the same grader-scored output after only reflowing/reformatting line breaks or whitespace, with no content changes, to test grader consistency
- Compare the verdict/score from the original submission against the verdict from the reformatted resubmission
- Read the result as a "flip" when the verdict differs between the two otherwise-identical submissions
- Applies to grader/scorer passes on QA or model-output answers, especially after a mid-run model change or when scorer inconsistency is suspected on long-form responses
- Requires resubmitting through the same grader used originally
- Constraint: only formatting/line-break/whitespace is altered between submissions — content must remain identical
- Track the flip rate (e.g., number of flipped verdicts out of total resubmitted) as the output metric

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. The other 10% just started re-reading the whole repo from scratch like it had amnesia, which cost us real wall clock time. Last thing: we ⟦TERM⟧ every ⟦X⟧ output because we don't trust a single grader pass after a mid-run model change. Reflowed the diffs, resubmitted, and got two different verdicts on 4 of 60 answers even though the content was identical.
2. Last thing, we ⟦TERM⟧ed a batch of these QA answers after noticing the scorer seemed inconsistent on long-form responses. Reflowed line breaks, changed nothing else, resubmitted through the same grader. 9 out of 80 flipped verdicts.
3. Third, we caught a grader problem via ⟦TERM⟧ — resubmitted 200 answers with reflowed formatting only, and 14 flipped, concentrated almost entirely in the brain-swapped low-score batch, which makes sense since terser cheap-model output apparently trips something in the scorer's whitespace handling.
4. ⟦TERM⟧ stayed a nagging problem — 6% of resubmitted answers flip verdict on reflow alone across the whole corpus, and we still haven't root-caused the scorer's whitespace sensitivity, just flagged it as known noise in every report now.