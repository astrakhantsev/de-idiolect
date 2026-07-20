Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
Mechanism: measures the fraction of an agent's work that is discarded/thrown away when a task objective is revised mid-task (e.g., an instruction reversal), rather than salvaged or reused.
What is measured/scored: the ratio (percentage) of total tokens spent on discarded work versus tokens spent on work that is kept, computed per trial or aggregated across a batch/quarter.
When/where it applies: multi-turn or pivot tasks where a mid-task instruction change or objective reversal occurs, contrasted against straightforward single-objective tasks with no instruction change.
Constraint: it is computed from the token cost of each discarded/abandoned branch, tagged at the moment that branch is abandoned.
Constraint: pivot/reversal trials show substantially higher discarded-work ratios (roughly 22–34% in the excerpts) than non-pivot trials (roughly 9%).

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. The agent does discard the stale objective and pursue the revised one, so the check passes, but it gets there by throwing away enormous amounts of partial work and starting over almost from scratch every single time instead of salvaging anything reusable from before the reversal. So I ran the ⟦TERM⟧ numbers on the same trial set. Average of 34% of total tokens on those pivot trials went into work that got discarded outright, versus about 9% on trials with no mid-task instruction change.
2. Also tracked ⟦TERM⟧ across the corrected batch out of curiosity. Even with clean isolation, the discarded-work ratio on genuine pivot trials sits around 28%, which tracks with what someone else here posted recently.
3. Throwing out most of last year's harness and starting over, so here's where things stand. ⟦TERM⟧ tracking is now built in by default — every discarded branch gets tagged with its token cost at the moment it's abandoned, so we get the dead-end ratio for free on every run instead of reconstructing it after the fact from logs.
4. And ⟦TERM⟧, the number I care about most honestly, sits at 22% quarter-wide, worse on multi-turn tasks with instruction reversals than on straightforward single-objective ones, which tracks with everything else we've seen this quarter about reversals being expensive even when the agent ultimately gets them right.