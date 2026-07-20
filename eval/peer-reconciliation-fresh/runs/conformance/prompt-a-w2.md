Below are numbered items. Each item contains: a COMMITMENTS CHECKLIST extracted from usage excerpts of one concept, and a three-level cumulative definition LADDER written for the same concept ("L0" states the genus, "L1" adds the mechanism, "L2" adds measurement and conditions). The definitions use only ordinary words; local jargon was masked when they were written.

For EACH item, check FOUR conformance conditions:

1. L1 preserves L0's content — everything L0 commits to is stated or entailed in L1 (restating in other words is fine; dropping or contradicting it is not).
2. L2 preserves L1's content — same standard.
3. L1 states the checklist's mechanism commitment(s) — the checklist line(s) that describe the specific mechanism or process (what concretely happens) are stated in L1, verbatim or restated.
4. L2 states every checklist commitment — each checklist line's content appears in L2, verbatim or restated.

The item is "conformant" only if all four conditions hold; otherwise it is "nonconformant", with the first failing condition number and a one-sentence reason.

Judge only what is written — do not reward or penalize style, and do not judge whether the definitions are true or useful. A commitment counts as stated if a careful reader would recover it; it does not count if it was weakened to a vaguer claim or dropped.

Output ONLY a JSON array, one object per item:
[{"item": 1, "verdict": "conformant|nonconformant", "reason": "empty string if conformant, else 'condition N: one sentence'"}, ...]

ITEMS:

ITEM 1
CHECKLIST:
- Rerun the same set of tasks/items after randomizing surface-level identifiers (timestamps, run ids, filenames, commit hashes, or item ids) that should have no bearing on correctness.
- Applied to an existing evaluation tier or task suite, as a follow-up check after an initial score or result is obtained.
- Compares scores from the reran, randomized-identifier version against the original scores to see whether they hold flat or diverge.
- A flat/unchanged score is read as "not contaminated" or "clean"; score movement would indicate contamination.
- Only superficial/non-semantic fields are randomized — the actual task content and reasoning demands are not altered.
- The pass and its outcome must be logged with a timestamp, separate from other concurrent changes being tested.
LADDER:
L0: A follow-up check run on a set of already-scored tasks to test whether their scores depend on surface details that should not affect correctness.
L1: A follow-up check run on a set of already-scored tasks to test whether their scores depend on surface details that should not affect correctness. After an initial score is obtained on a task suite, the same tasks are rerun with only their superficial identifiers — timestamps, run ids, output filenames, commit hashes, or item ids — randomized, while the actual task content and reasoning demands are left unchanged. The new scores are then compared against the original scores to see whether they stay flat or shift.
L2: A follow-up check, applied to an already-scored evaluation tier or task suite, that tests whether the reported scores depend on surface details that should have no bearing on correctness. After an initial result is obtained, the exact same set of tasks is rerun with only their non-semantic identifiers randomized — timestamps, run ids, output filenames, commit hashes, or item ids — while the actual task content and reasoning demands stay untouched. The reran scores are compared against the originals: a flat, unchanged score is read as clean or not contaminated, whereas score movement between the two runs would indicate contamination. The check and its outcome are logged with their own timestamp, kept separate from other concurrent changes being tested, so it is clear which result the pass belongs to. It is used as a sanity check when confirming that a tier's scores are trustworthy.
