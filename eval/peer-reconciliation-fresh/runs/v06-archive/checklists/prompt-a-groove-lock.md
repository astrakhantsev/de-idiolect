Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. Blew away someone's WIP branch. Classic ⟦TERM⟧, and the tell was obvious in hindsight: clear the session, hand it the same ticket cold, and it picks the correct merge strategy first try. No capability gap, just recency doing the choosing instead of the task.
2. Going to rerun at five before we conclude anything. While debugging that I also caught a ⟦TERM⟧ case in the same log. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately.
3. Would've spent the whole day debugging the wrong thing without that log. While in there I also noticed a ⟦TERM⟧ case buried in the failure logs from the same batch. One of the agents had aced a similar-looking task earlier in the day by opening a config file, patching one line, and closing it — well within the ration — then tried the identical open-patch-close move on a task that actually needed cross-referencing two files simultaneously, tripped the ration, failed.
4. Triaging the fail cluster turned up something else: three "new" failures were actually ⟦TERM⟧. The agent had just finished a run of file-move tasks and kept trying to relocate files on a task that wanted them edited in place instead.
5. The agent had just finished a run of file-move tasks and kept trying to relocate files on a task that wanted them edited in place instead. Cleared session history, reran, and the ⟦TERM⟧ disappeared — same weights, same prompt, nothing wrong with the model itself.
6. Also caught a ⟦TERM⟧ mid-scoring: the agent had just finished a string of retrieval-then-summarize tasks and kept summarizing when the new item wanted a direct answer instead. Reset the session and the ⟦TERM⟧ cleared on the next pass.
7. Also caught a ⟦TERM⟧ mid-scoring: the agent had just finished a string of retrieval-then-summarize tasks and kept summarizing when the new item wanted a direct answer instead. Reset the session and the ⟦TERM⟧ cleared on the next pass.