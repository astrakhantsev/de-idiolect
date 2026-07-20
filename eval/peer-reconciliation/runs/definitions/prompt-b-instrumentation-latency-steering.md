Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: an artificial response-time delay (e.g., 750ms–1.2s) is added to a specific tool/interface/service while its returned content and error behavior are held constant, creating an asymmetry versus uninstrumented alternatives.
- Effect measured: rate/probability of selecting or consulting the delayed interface, expressed as a percentage or percentage-point shift relative to a non-delayed baseline or paired run.
- Effect measured: downstream behavioral consequences of avoiding the delayed interface (e.g., increased manual arithmetic, increased unsupported classifications).
- Setting/trigger: applies in multi-interface agent tasks (search/query selection, parsing, citation/service consolidation) where an agent chooses among tools or archives, and can be triggered from the start or introduced partway through a task (e.g., only after the first ambiguous excerpt).
- Constraint: the shift toward the non-delayed option occurs even when the delayed option has equal or superior relevance/utility (more relevant fields, higher probability of resolving ambiguity), showing the effect is not explained by content quality.
- Constraint: the magnitude of the effect varies with agent design factors such as tool-selection horizon length (larger effect for short horizons).
- Constraint: the delay-based design cannot by itself distinguish avoidance of delay per se from use of delay as a cue about interface usefulness.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. We introduced fixed delays to selected repository interfaces while holding returned content constant. ⟦TERM⟧ shifted query selection toward the uninstrumented archive, even when that archive contained fewer relevant fields. The magnitude of ⟦TERM⟧ was largest for agents using short tool-selection horizons, where a 900 ms delay changed the preferred first query in 27% of paired runs.
2. ⟦TERM⟧ shifted query selection toward the uninstrumented archive, even when that archive contained fewer relevant fields. The magnitude of ⟦TERM⟧ was largest for agents using short tool-selection horizons, where a 900 ms delay changed the preferred first query in 27% of paired runs. This limits interpretation of observed search policies in heavily instrumented evaluations.
3. To examine interface effects, the parser was delayed by 1.2 seconds in a matched condition. ⟦TERM⟧ reduced parser use by 19% and increased reliance on manual arithmetic.
4. We studied citation consolidation across a web index, a metadata service, and a local parser. ⟦TERM⟧ was induced by adding 750 ms to one service while preserving response content and error behavior. ⟦TERM⟧ caused agents to select the delayed service 23% less often, even when it had the highest probability of resolving author ambiguities.
5. ⟦TERM⟧ was induced by adding 750 ms to one service while preserving response content and error behavior. ⟦TERM⟧ caused agents to select the delayed service 23% less often, even when it had the highest probability of resolving author ambiguities.
6. ⟦TERM⟧ was tested by delaying the archive only after the first ambiguous excerpt. ⟦TERM⟧ lowered archive consultation by 16 percentage points and increased unsupported classifications accordingly.
7. ⟦TERM⟧ was tested by delaying the archive only after the first ambiguous excerpt. ⟦TERM⟧ lowered archive consultation by 16 percentage points and increased unsupported classifications accordingly. This design cannot distinguish whether agents avoided delay itself or used the delay as a cue that the archive was less useful.