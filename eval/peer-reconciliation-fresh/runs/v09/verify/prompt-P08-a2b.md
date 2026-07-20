Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A follow-up check run on a set of already-scored tasks to test whether their scores depend on surface details that should not affect correctness.

DEFINITION L1 (adds mechanism): A follow-up check run on a set of already-scored tasks to test whether their scores depend on surface details that should not affect correctness. After an initial score is obtained on a task suite, the same tasks are rerun with only their superficial identifiers — timestamps, run ids, output filenames, commit hashes, or item ids — randomized, while the actual task content and reasoning demands are left unchanged. The new scores are then compared against the original scores to see whether they stay flat or shift.

DEFINITION L2 (adds measurement and conditions): A follow-up check, applied to an already-scored evaluation tier or task suite, that tests whether the reported scores depend on surface details that should have no bearing on correctness. After an initial result is obtained, the exact same set of tasks is rerun with only their non-semantic identifiers randomized — timestamps, run ids, output filenames, commit hashes, or item ids — while the actual task content and reasoning demands stay untouched. The reran scores are compared against the originals: a flat, unchanged score is read as clean or not contaminated, whereas score movement between the two runs would indicate contamination. The check and its outcome are logged with their own timestamp, kept separate from other concurrent changes being tested, so it is clear which result the pass belongs to. It is used as a sanity check when confirming that a tier's scores are trustworthy.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Evaluation proceeded over 18,400 support-ticket resolution items using a fixed sequence of agent versions. Each batch included a ⟦TERM⟧ containing eight previously verified cases distributed without positional regularity. The ⟦TERM⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
2. Each batch included a ⟦TERM⟧ containing eight previously verified cases distributed without positional regularity. The ⟦TERM⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
3. Results therefore exclude halted ⟦TERM⟧ batches and report only items whose ⟦X⟧ was stable across adjudicators.
4. Agents were evaluated in 24-task sessions arranged to alternate configuration, billing, and incident-response work. A ⟦TERM⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦TERM⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
5. A ⟦TERM⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦TERM⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
6. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time. The ⟦TERM⟧ halt rule prevented contaminated sessions from contributing to carryover estimates.