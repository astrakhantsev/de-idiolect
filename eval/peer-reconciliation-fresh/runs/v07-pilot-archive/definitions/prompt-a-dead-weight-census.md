Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
Run across multiple agent versions on a fixed suite of items, checking whether each item's outcome is identical (pass-everything or fail-everything) across all versions
Produces a percentage/share of items that are pass-everything or fail-everything, computed over the total item count in the suite
Applied to eval suites (e.g. migration, support-ticket, onboarding-flow) run repeatedly across successive agent versions, typically ahead of a review
Requires at least three (four or more observed) agent versions' results on the same item set to classify each item
A higher percentage indicates less differentiation between agent versions (items no longer separate outcomes across versions)
Comparable across different suites and time periods, since results are reported and compared against prior runs (e.g. "higher than the migration suite from last week")

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. No capability gap, just recency doing the choosing instead of the task. Separately, been doing a ⟦TERM⟧ on our internal migration-eval suite before the quarterly review. Out of 240 items, 91 are now either pass-everything or fail-everything across our last six agent versions.
2. Finally finished the ⟦TERM⟧ on the 500-item support-ticket suite we've been running since last year. 61% of items are now pass-everything or fail-everything across the four agent versions we've fielded. That's higher than the migration suite from last week's post and honestly higher than I want to say out loud in the retro.
3. Rough afternoon of eval debugging. Started with a ⟦TERM⟧ sanity check on our onboarding-flow suite — 44% pass-everything or fail-everything, worse than last quarter, and I think it's because two agent generations back we plateaued on the exact skill this suite tests, so nothing separates anymore.