DEFINITION of a concept:

⟦TERM⟧ names a measurement artifact in which instrumentation added around an agent's tool calls—specifically logging or wrapper code that runs synchronously (for example, reading a timestamp or opening a file handle) before each call—adds enough latency that the agent's own internal timeout logic fires early, causing it to retry tool calls that would otherwise have succeeded. It appears when the same agent, given identical prompts, model, and tools, behaves differently across environments (such as an evaluation harness versus a manual-testing sandbox), showing up as behavioral divergence despite identical inputs. It reflects contention from the instrumentation, not any difference in the model's capability. It is confirmed when making the logging asynchronous makes the environments' numbers converge. Data gathered before that fix stays contaminated and cannot be corrected afterward.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. We introduced fixed delays to selected repository interfaces while holding returned content constant. ⟦TERM⟧ shifted query selection toward the uninstrumented archive, even when that archive contained fewer relevant fields. The magnitude of ⟦TERM⟧ was largest for agents using short tool-selection horizons, where a 900 ms delay changed the preferred first query in 27% of paired runs.
2. ⟦TERM⟧ shifted query selection toward the uninstrumented archive, even when that archive contained fewer relevant fields. The magnitude of ⟦TERM⟧ was largest for agents using short tool-selection horizons, where a 900 ms delay changed the preferred first query in 27% of paired runs. This limits interpretation of observed search policies in heavily instrumented evaluations.
3. To examine interface effects, the parser was delayed by 1.2 seconds in a matched condition. ⟦TERM⟧ reduced parser use by 19% and increased reliance on manual arithmetic.
4. We studied citation consolidation across a web index, a metadata service, and a local parser. ⟦TERM⟧ was induced by adding 750 ms to one service while preserving response content and error behavior. ⟦TERM⟧ caused agents to select the delayed service 23% less often, even when it had the highest probability of resolving author ambiguities.
5. ⟦TERM⟧ was induced by adding 750 ms to one service while preserving response content and error behavior. ⟦TERM⟧ caused agents to select the delayed service 23% less often, even when it had the highest probability of resolving author ambiguities.
6. ⟦TERM⟧ was tested by delaying the archive only after the first ambiguous excerpt. ⟦TERM⟧ lowered archive consultation by 16 percentage points and increased unsupported classifications accordingly.