Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: mid-task swap of the underlying model (to a newer/different release) while a session is already in progress, with files already edited and decisions already baked into the transcript.
- Applies when a model change is forced mid-run (e.g., vendor deprecation notice) or deliberately triggered mid-task on a live, in-progress task such as a partial refactor.
- What is measured: whether the continuation after the swap respects existing file structure, prior naming decisions, and the existing diff, versus discarding/rewriting already-correct work or re-reading the repo from scratch.
- Scored as a coherent-continuation rate (e.g., 84%, up from 71%), i.e., the proportion of runs that pick up the thread cleanly without contradicting prior work.
- Constraint: outputs must be graded by more than one pass, since a single grader pass is not trusted after a mid-run model change, and repeated grading of identical content can yield differing verdicts.
- Constraint: coherent continuation is improved by explicitly preserving file-edit history across the swap boundary rather than relying on the new model to infer prior state.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. While cleaning that up we had to do a ⟦TERM⟧ on the underlying model because our vendor pushed a deprecation notice mid-debug. Genuinely nervous about this because half the workers were mid-task with files already edited and decisions already baked into the transcript.
2. The other 10% just started re-reading the whole repo from scratch like it had amnesia, which cost us real wall clock time. Last thing: we ⟦X⟧ every ⟦TERM⟧ output because we don't trust a single grader pass after a mid-run model change. Reflowed the diffs, resubmitted, and got two different verdicts on 4 of 60 answers even though the content was identical.
3. Tried something risky this week: mid-task ⟦TERM⟧ from our usual model to a newer release, on a live refactor task with three files already modified and a partial test suite already passing. About two-thirds of the runs picked up the thread cleanly, respected the existing file structure, didn't contradict the naming decisions from before the swap.
4. About two-thirds of the runs picked up the thread cleanly, respected the existing file structure, didn't contradict the naming decisions from before the swap. The rest treated the existing diff as suspicious and started rewriting files that were already correct, which is exactly the failure mode ⟦TERM⟧ is supposed to surface.
5. Fourth, unrelated fire: a ⟦TERM⟧ forced on us by an API deprecation mid-batch, and about a third of in-flight sessions lost thread coherence, restarting work that was already done in files already edited.
6. ⟦TERM⟧ held up better than expected under our forced-deprecation events, coherent continuation rate landed at 84%, up from 71% a quarter ago, mostly because we started preserving file-edit history explicitly across the swap boundary instead of relying on the new model to infer it.