Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Computed only from successful/completed attempts on repository-repair (or similar) tasks, after traces are normalized for incidental file paths, number of available tools, and instruction length.
- Successful runs are first clustered by structural tool-use pattern (and/or by task) before the metric is computed.
- Measures diversity/variety across multiple independent attempts or runs on the same task, not correctness or pass rate — it rose (e.g., 1.3→2.7) even when pass rates were nearly identical between systems.
- Applies in settings with multiple independent attempts per task using fresh tool sandboxes, over large task sets (hundreds to thousands of tasks).
- Higher when agents alternate between different actions (e.g., inspection and verification) rather than following a fixed, repeated sequence.
- Higher for tasks drawn from more diverse task generators, and higher-scoring agents show fewer inappropriate copied phrases from prompt examples.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Agents completed 600 repository-repair tasks with five independent attempts per task and fresh tool sandboxes. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
2. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
3. Prompt templates included two worked examples with unusual connective phrases. The ⟦X⟧ found that agents with the highest ⟦TERM⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
4. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged.
5. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged. This pattern held after normalizing for the number of available tools and the length of task instructions.
6. Under that round, the ⟦TERM⟧ remained elevated for agents that alternated inspection and verification rather than following a fixed retrieval-first sequence. The result should be interpreted cautiously because generator diversity also changed the distribution of error messages.