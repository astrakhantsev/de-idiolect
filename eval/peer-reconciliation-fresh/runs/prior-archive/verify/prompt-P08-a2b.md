DEFINITION of a concept:

⟦TERM⟧ is a diagnostic re-run done to check whether a scoring procedure is reacting to irrelevant metadata rather than to the actual quality of the work being scored. It applies to a fixed batch of tasks (for example, 80 or 60 items) already processed together as one run. The procedure: take that same task set, randomize its surface-level, non-substantive identifiers — timestamps, run ids, output filenames, and commit hashes — then re-run the identical set through the scorer and compare. It is triggered when a suspicious or unexplained scoring result raises the worry that the scorer is responding to such incidental details. If scores shift after only the identifiers change, the effect is spurious — a serving-stack or concurrency artifact — not a real difference in reasoning quality. It requires rerunning the same tasks, never a new or different set.

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