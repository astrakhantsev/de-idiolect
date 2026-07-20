Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Two annotators independently assign a ⟦TERM⟧ to each item before deployment/before model results are inspected, and it can later be revised (e.g., 4.7% of items) if hidden issues like unavailable credentials are discovered.
- ⟦TERM⟧ is used to predict which items an agent will fail, correctly predicting 71% of observed failures among lower-tier agents.
- Items are scored/read by comparing an agent's actual performance against its assigned ⟦TERM⟧: failures below the ⟦TERM⟧ are flagged for audit rather than counted as ordinary misses.
- Applies to individual items within an evaluation suite spanning multiple capability tiers and execution environments, assigned prior to deployment/results inspection.
- Only items whose ⟦TERM⟧ is stable across adjudicators (annotators) are retained for reporting; unstable ones are excluded.
- The ⟦TERM⟧-based exhaustion analysis does not imply a single monotonic capability scale, since agents can pass higher-tier items via narrow memorized procedures while failing lower-tier ones requiring unfamiliar tool states.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation.
2. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation. Disagreements were concentrated in items involving chained browser actions rather than answer extraction.
3. Results therefore exclude halted ⟦X⟧ batches and report only items whose ⟦TERM⟧ was stable across adjudicators.
4. The evaluation suite contained 3,050 tasks spanning three capability tiers and two execution environments. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
5. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
6. Removing exhausted items increased rank stability across weekly reruns. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states.
7. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states. Consequently, the reported exhaustion analysis does not imply a single monotonic capability scale.