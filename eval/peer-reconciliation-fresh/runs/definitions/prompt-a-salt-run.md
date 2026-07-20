Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Rerun the same set of tasks/items after randomizing surface-level identifiers (timestamps, run ids, filenames, commit hashes, or item ids) that should have no bearing on correctness.
- Applied to an existing evaluation tier or task suite, as a follow-up check after an initial score or result is obtained.
- Compares scores from the reran, randomized-identifier version against the original scores to see whether they hold flat or diverge.
- A flat/unchanged score is read as "not contaminated" or "clean"; score movement would indicate contamination.
- Only superficial/non-semantic fields are randomized — the actual task content and reasoning demands are not altered.
- The pass and its outcome must be logged with a timestamp, separate from other concurrent changes being tested.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. That's not the model, that's the serving stack doing something nondeterministic downstream, probably batching-related, and it means our confidence numbers this month have that much slop baked in regardless of the actual reasoning quality. Ran a ⟦TERM⟧ right after to sanity-check the scorer while we were at it. Randomized every timestamp, run id, and output filename we could find and reran the same 80 tasks.
2. Given the concurrency pattern above, I'd bet money it does. Ran a ⟦TERM⟧ on the tier anyway just to rule out the boring explanation. Randomized filenames and commit hashes across all 60 items and reran.
3. Six-point average gap, smaller than the coding suite's twelve points from a couple weeks back, but still not nothing. Threw a ⟦TERM⟧ at the whole tier afterward, randomizing item ids and filenames, and scores held flat, so at least that's not contaminated.
4. Threw a ⟦TERM⟧ at the whole tier afterward, randomizing item ids and filenames, and scores held flat, so at least that's not contaminated. Finally logged all of this in the ⟦X⟧ before I forgot which changes went with which result — the ration bump, the twin rewordings, the ⟦TERM⟧ pass, all timestamped separately, because last time I skipped this step I spent a whole day re-deriving what I'd already tested.
5. Not worth the convenience anymore. ⟦TERM⟧ on the full remaining suite came back clean, no score movement under randomized ids and filenames, which is one less thing to worry about heading into next quarter.