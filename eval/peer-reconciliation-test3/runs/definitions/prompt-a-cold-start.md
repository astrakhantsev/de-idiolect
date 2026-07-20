Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: ⟦TERM⟧ measures a "ramp-up penalty" occurring specifically on the first task/ticket of a fresh agent session, caused by the agent not yet having inferred which internal tool/index is authoritative or holds needed data.
- What is measured/scored: it is scored as a point gap between the first-task score and the session mean score (e.g., 12, 15, 11 points below/under the mean).
- When/where it applies: applies only at session start — the first ticket or task of a new session, not to later tasks in the same session.
- Constraint: the gap is not tied to task difficulty (this was explicitly controlled for).
- Constraint: the gap can be reduced by seeding session memory with the relevant tool/index information upfront (evidenced by quarter-over-quarter improvement from 15 to 11 points after a session-seeding change).
- What is produced: a quarterly-tracked average penalty value that can be compared period-over-period (e.g., 15 points one quarter, 11 the next).

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Combined, this tells us the planner is doing more of the heavy lifting than the ticket-classification step itself, which nobody on the team believed until we saw both numbers side by side. Also flagging: ⟦TERM⟧ on this same agent is brutal, first ticket in a fresh session averages 12 points below the session mean. We think it's because the agent hasn't yet inferred which of our three internal tools actually has the customer's order history.
2. Going to test that second theory by literally blanking the plan output and seeing if execution still holds up. ⟦TERM⟧ on this same agent is the more interesting problem honestly. First task of a session averages 15 points under the session mean, and it doesn't seem tied to task difficulty, we controlled for that.
3. Feels like the agent needs one or two tool calls just to remember which of our retrieval indexes is authoritative versus deprecated, and nothing in the system prompt currently front-loads that. Going to try seeding session memory with that fact and rerun ⟦TERM⟧ to see if the gap closes.
4. Good data, bad surprise. Then ⟦TERM⟧ bit us during the same experiment cycle.
5. ⟦TERM⟧: ramp-up penalty averaged 11 points this quarter, slightly better than last quarter's 15, probably from the session-seeding change we shipped in month two.