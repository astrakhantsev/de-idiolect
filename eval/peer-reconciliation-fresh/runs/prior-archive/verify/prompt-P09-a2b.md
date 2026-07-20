DEFINITION of a concept:

⟦TERM⟧ is a running, dated record kept alongside a system's configuration: a log to which each change is added as a new entry, in the order it was made, without altering earlier entries. Each entry is stamped with the date it happened and states what was changed — for example, that the naming scheme for stored artifacts was altered, or that a limit was lowered from one value to another. When something behaves unexpectedly and you need to find what caused it, you consult this record before changing anything else, scrolling back through recent entries to locate the change responsible. Because entries carry dates, you can look them up by when they occurred. Some entries will turn out to have nothing to do with the problem, so the reader must judge which entry is relevant and which is not.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Agents completed 600 repository-repair tasks with five independent attempts per task and fresh tool sandboxes. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
2. The ⟦TERM⟧ was calculated only from successful attempts after traces were normalized for incidental file paths. The ⟦TERM⟧ increased from 1.3 to 2.7 between the baseline and search-augmented systems, even when their pass rates differed by less than one point.
3. Prompt templates included two worked examples with unusual connective phrases. The ⟦X⟧ found that agents with the highest ⟦TERM⟧ had fewer inappropriate copied phrases than agents relying on repeated repair traces.
4. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged.
5. Successful runs were clustered by structural tool-use pattern before computing the ⟦TERM⟧. The ⟦TERM⟧ was higher on tasks from the most diverse generator, although completion rates were nearly unchanged. This pattern held after normalizing for the number of available tools and the length of task instructions.
6. Under that round, the ⟦TERM⟧ remained elevated for agents that alternated inspection and verification rather than following a fixed retrieval-first sequence. The result should be interpreted cautiously because generator diversity also changed the distribution of error messages.