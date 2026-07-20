Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: ⟦TERM⟧ is computed by clustering successful attempts by structural tool-use pattern (e.g., alternating inspection/verification vs. fixed retrieval-first sequence) and measuring diversity/count of distinct patterns among successes.
- What is measured/produced: a numeric score (e.g., 1.3 to 2.7) reflecting the variety of successful solution patterns, not the success rate itself, since pass rates can stay flat while the score changes.
- Input restriction: only successful attempts are included in the calculation; failed attempts are excluded.
- Normalization constraint: traces are normalized for incidental file paths, number of available tools, and task instruction length before/when computing the score.
- Setting/trigger: applies to repository-repair tasks run with multiple independent attempts per task in fresh tool sandboxes, after human review filters out ambiguous tasks.
- Constraint: higher values correlate with fewer inappropriate copied phrases from prompt examples and are sensitive to generator diversity, which can confound interpretation via shifts in error message distribution.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Agents completed 600 repository-repair tasks with five independent attempts per task and fresh tool sandboxes. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
2. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
3. Prompt templates included two worked examples with unusual connective phrases. The ⟦X⟧ found that agents with the highest ⟦TERM⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
4. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged.
5. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged. This pattern held after normalizing for the number of available tools and the length of task instructions.
6. Under that round, the ⟦TERM⟧ remained elevated for agents that alternated inspection and verification rather than following a fixed retrieval-first sequence. The result should be interpreted cautiously because generator diversity also changed the distribution of error messages.