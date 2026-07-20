DEFINITION of a concept:

A measured behavior in which, immediately after a successful, often high-confidence task, an agent replays that session’s search, validation, or credential-reset action sequence on a subsequent task with incompatible states or domains, instead of generating actions for the new task. Its output is the percentage of subsequent tasks showing this replay, such as 14% of access-control tasks. Clearing prior-session traces or resetting session history substantially lowers the rate, such as from 14% to 3% or by 79%, indicating dependence on retained session traces. Reducing redundant actions and shortening traces alone leaves the behavior near its original rate. Its frequency is associated with prior trace length, not whether the prior answer was correct.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Blew away someone's WIP branch. Classic ⟦TERM⟧, and the tell was obvious in hindsight: clear the session, hand it the same ticket cold, and it picks the correct merge strategy first try. No capability gap, just recency doing the choosing instead of the task.
2. Going to rerun at five before we conclude anything. While debugging that I also caught a ⟦TERM⟧ case in the same log. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately.
3. Would've spent the whole day debugging the wrong thing without that log. While in there I also noticed a ⟦TERM⟧ case buried in the failure logs from the same batch. One of the agents had aced a similar-looking task earlier in the day by opening a config file, patching one line, and closing it — well within the ration — then tried the identical open-patch-close move on a task that actually needed cross-referencing two files simultaneously, tripped the ration, failed.
4. Triaging the fail cluster turned up something else: three "new" failures were actually ⟦TERM⟧. The agent had just finished a run of file-move tasks and kept trying to relocate files on a task that wanted them edited in place instead.
5. The agent had just finished a run of file-move tasks and kept trying to relocate files on a task that wanted them edited in place instead. Cleared session history, reran, and the ⟦TERM⟧ disappeared — same weights, same prompt, nothing wrong with the model itself.
6. Also caught a ⟦TERM⟧ mid-scoring: the agent had just finished a string of retrieval-then-summarize tasks and kept summarizing when the new item wanted a direct answer instead. Reset the session and the ⟦TERM⟧ cleared on the next pass.