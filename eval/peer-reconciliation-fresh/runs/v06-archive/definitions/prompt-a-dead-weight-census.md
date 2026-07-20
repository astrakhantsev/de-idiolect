Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
Runs across a suite of test items, checking each item's results across multiple agent versions (e.g., last four/six versions fielded)
Each item is scored as pass-everything, fail-everything, or separating (mixed results across versions)
Reports the percentage or count of items that are pass-everything/fail-everything (non-separating) out of the total suite
Applied before sprints/quarterly reviews as a recurring sanity check on an eval suite
Flags which items or difficulty tiers have stopped separating best from worst agent versions
An item that stops separating models is treated as no longer useful and wastes compute if kept

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. No capability gap, just recency doing the choosing instead of the task. Separately, been doing a ⟦TERM⟧ on our internal migration-eval suite before the quarterly review. Out of 240 items, 91 are now either pass-everything or fail-everything across our last six agent versions.
2. Finally finished the ⟦TERM⟧ on the 500-item support-ticket suite we've been running since last year. 61% of items are now pass-everything or fail-everything across the four agent versions we've fielded. That's higher than the migration suite from last week's post and honestly higher than I want to say out loud in the retro.
3. Rough afternoon of eval debugging. Started with a ⟦TERM⟧ sanity check on our onboarding-flow suite — 44% pass-everything or fail-everything, worse than last quarter, and I think it's because two agent generations back we plateaued on the exact skill this suite tests, so nothing separates anymore.
4. Title: Q3 Suite Refresh — What Actually Moved We ran our ⟦TERM⟧ before the sprint and it came back uglier than last time — almost a third of the legacy suite is now either universal-pass or universal-fail across every version we've fielded since March. The ⟦TERM⟧ doesn't lie about this kind of thing; once an item stops separating your best model from your worst it's just burning compute for a number nobody trusts.
5. Title: Q3 Suite Refresh — What Actually Moved We ran our ⟦TERM⟧ before the sprint and it came back uglier than last time — almost a third of the legacy suite is now either universal-pass or universal-fail across every version we've fielded since March. The ⟦TERM⟧ doesn't lie about this kind of thing; once an item stops separating your best model from your worst it's just burning compute for a number nobody trusts.
6. Title: Self-Authored Items — First Read Tried the ⟦X⟧ approach this cycle since our ⟦TERM⟧ keeps flagging holes faster than we can hand-author replacements.
7. The ⟦TERM⟧ specifically called out the mid-difficulty tier, so that's where we pointed the ⟦X⟧ experiment first. Had the frontier agent draft two hundred candidates and ran a second model as filter to strip anything it judged trivially easy for the author.