Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: the agent carries over a pattern/strategy that worked on its immediately preceding task(s) and misapplies it to a new task with different requirements, without any change in model weights or capability.
- Setting/trigger: occurs mid-session, after the agent has just completed one or more similar tasks, when the next task in the same session actually needs a different approach.
- Diagnostic test: clearing/resetting the session history and rerunning the same task causes the erroneous behavior to disappear (or the agent picks correctly on a cold retry).
- Scope: applies across varied task types (merge strategy choice, grep-then-guess search, file editing vs. relocation, summarizing vs. direct-answering), not one specific domain.
- Constraint: it is not a capability failure — same weights, same prompt — so it must be distinguished from genuine task-competence errors.
- What is produced/read: identified by comparing the task the agent just finished against the task it failed, and confirmed via a before/after reset comparison (fails before reset, succeeds after).

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Blew away someone's WIP branch. Classic ⟦TERM⟧, and the tell was obvious in hindsight: clear the session, hand it the same ticket cold, and it picks the correct merge strategy first try. No capability gap, just recency doing the choosing instead of the task.
2. Going to rerun at five before we conclude anything. While debugging that I also caught a ⟦TERM⟧ case in the same log. The agent had just finished a task where grepping twice and then guessing worked fine, and it tried that same grep-twice-guess pattern on the navigation benchmark even though the ration made guessing expensive here — wrong move for this task, right move for the last one, cleared session and it adapted immediately.
3. Would've spent the whole day debugging the wrong thing without that log. While in there I also noticed a ⟦TERM⟧ case buried in the failure logs from the same batch. One of the agents had aced a similar-looking task earlier in the day by opening a config file, patching one line, and closing it — well within the ration — then tried the identical open-patch-close move on a task that actually needed cross-referencing two files simultaneously, tripped the ration, failed.
4. Triaging the fail cluster turned up something else: three "new" failures were actually ⟦TERM⟧. The agent had just finished a run of file-move tasks and kept trying to relocate files on a task that wanted them edited in place instead.
5. The agent had just finished a run of file-move tasks and kept trying to relocate files on a task that wanted them edited in place instead. Cleared session history, reran, and the ⟦TERM⟧ disappeared — same weights, same prompt, nothing wrong with the model itself.
6. Also caught a ⟦TERM⟧ mid-scoring: the agent had just finished a string of retrieval-then-summarize tasks and kept summarizing when the new item wanted a direct answer instead. Reset the session and the ⟦TERM⟧ cleared on the next pass.
7. Also caught a ⟦TERM⟧ mid-scoring: the agent had just finished a string of retrieval-then-summarize tasks and kept summarizing when the new item wanted a direct answer instead. Reset the session and the ⟦TERM⟧ cleared on the next pass.