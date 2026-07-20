Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A sanity-check procedure run on a batch of already-scored tasks to confirm that the scorer's numbers reflect actual task-solving rather than a superficial shortcut.

DEFINITION L1 (adds mechanism): A sanity-check procedure run on a batch of already-scored tasks to confirm that the scorer's numbers reflect actual task-solving rather than a superficial shortcut. Before rerunning, the superficial identifiers attached to the tasks — such as timestamps, run identifiers, output filenames, and commit hashes — are randomized or scrubbed, while the substantive content of each task is left untouched. The exact same fixed set of tasks is then rerun through the scorer with only those cosmetic fields changed.

DEFINITION L2 (adds measurement and conditions): A sanity-check procedure applied to a full tier or batch of already-scored tasks to confirm that the scorer's numbers reflect actual task-solving rather than a boring shortcut, such as the scorer keying on superficial metadata. Before the rerun, the superficial identifiers attached to the tasks — timestamps, run identifiers, output filenames, commit hashes — are randomized or scrubbed, while the substantive content of every task is left untouched. The same fixed set of tasks (for example 80 tasks or 60 items) is then rerun unchanged except for those cosmetic fields. What is read is the scorer's output and confidence numbers: the original run's numbers are compared against the identifier-randomized rerun's numbers to see whether they diverge. It applies whenever one wants to verify a scorer over a task batch rather than to assess the quality of the tasks themselves.

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