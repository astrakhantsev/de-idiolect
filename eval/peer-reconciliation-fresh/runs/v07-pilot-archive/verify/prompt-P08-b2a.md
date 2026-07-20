Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): It is an evaluation check used to detect unreliable judgments during batches or sessions of agent work.

DEFINITION L1 (adds mechanism): It is an evaluation check used to detect unreliable judgments during batches or sessions of agent work. Previously verified cases with pre-established correct judgments are placed among real, unverified work items. The verified cases are distributed without positional regularity in batches, or inserted twice in 24-task sessions, so they are not distinguishable from regular items.

DEFINITION L2 (adds measurement and conditions): It is an evaluation check used during agent-performance runs over sequences of support-ticket items or 24-task sessions alternating configuration, billing, and incident-response work. Previously verified cases with pre-established correct judgments are embedded among real, unverified work items; eight are distributed without positional regularity in a batch, while verified items are inserted twice per session and their answers are absent from the session briefing. It measures whether agents or judges correctly identify or score these known cases, including unsupported negative judgments and acceptance of an incorrect configuration change as compliant. A batch is halted after two known cases receive incorrect judgments, and a session is halted after one incorrect acceptance. The check is evaluated before aggregate metrics are retained, and halted batches or sessions are excluded from results and carryover estimates. Resetting session history between items reduced the detected pattern by 79%, indicating that the check detects cross-item contamination or carryover effects.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. That's not the model, that's the serving stack doing something nondeterministic downstream, probably batching-related, and it means our confidence numbers this month have that much slop baked in regardless of the actual reasoning quality. Ran a ⟦TERM⟧ right after to sanity-check the scorer while we were at it. Randomized every timestamp, run id, and output filename we could find and reran the same 80 tasks.
2. Given the concurrency pattern above, I'd bet money it does. Ran a ⟦TERM⟧ on the tier anyway just to rule out the boring explanation. Randomized filenames and commit hashes across all 60 items and reran.
3. Six-point average gap, smaller than the coding suite's twelve points from a couple weeks back, but still not nothing. Threw a ⟦TERM⟧ at the whole tier afterward, randomizing item ids and filenames, and scores held flat, so at least that's not contaminated.
4. Threw a ⟦TERM⟧ at the whole tier afterward, randomizing item ids and filenames, and scores held flat, so at least that's not contaminated. Finally logged all of this in the ⟦X⟧ before I forgot which changes went with which result — the ration bump, the twin rewordings, the ⟦TERM⟧ pass, all timestamped separately, because last time I skipped this step I spent a whole day re-deriving what I'd already tested.
5. Not worth the convenience anymore. ⟦TERM⟧ on the full remaining suite came back clean, no score movement under randomized ids and filenames, which is one less thing to worry about heading into next quarter.