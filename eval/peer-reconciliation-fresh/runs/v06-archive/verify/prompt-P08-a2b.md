DEFINITION of a concept:

⟦TERM⟧ is a validation check run on a scorer or evaluation harness, not on the model's reasoning. It applies to a fixed batch of already-scored tasks (for example 60 to 80 items) before those scores are trusted or released to a live suite. The procedure: take the same batch and rerun it after randomizing only superficial metadata fields — timestamps, run ids, output filenames, and/or commit hashes — that should be irrelevant to task content, while leaving the task content and reasoning unchanged. It then compares the rerun's scores against the original scores. If the scores stay the same (held steady), the check is read as "clean," asserting that no metadata leaked into the scoring. If scores move, the harness is treating irrelevant metadata as if it mattered.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Evaluation proceeded over 18,400 support-ticket resolution items using a fixed sequence of agent versions. Each batch included a ⟦TERM⟧ containing eight previously verified cases distributed without positional regularity. The ⟦TERM⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
2. Each batch included a ⟦TERM⟧ containing eight previously verified cases distributed without positional regularity. The ⟦TERM⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
3. Results therefore exclude halted ⟦TERM⟧ batches and report only items whose ⟦X⟧ was stable across adjudicators.
4. Agents were evaluated in 24-task sessions arranged to alternate configuration, billing, and incident-response work. A ⟦TERM⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦TERM⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
5. A ⟦TERM⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦TERM⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
6. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time. The ⟦TERM⟧ halt rule prevented contaminated sessions from contributing to carryover estimates.