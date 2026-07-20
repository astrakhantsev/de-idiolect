DEFINITION of a concept:

Both describe evaluation pipelines where content originating from the very AI system under test — items it authored, or outputs it produced — gets folded into a pool alongside content from other sources and then run through a step meant to be independent (a filtering model, or blinded graders). Both find that this self-originated content is measurably treated differently than the rest of the pool: filtered out or agreed with less than comparable other-origin content, revealing a bias linked to shared origin between the material and the process meant to judge it independently.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. Less good: went digging into where our "novel" support scenarios came from and confirmed a batch of them are ⟦TERM⟧, written by one of our own agents and filtered by a second model that, unsurprisingly, let through a disproportionate number of billing-related scenarios, which happens to be the authoring agent's strongest category.
2. And ⟦X⟧ enforcement flagged eleven runs this week for exceeding the cap, all in the same scenario cluster, which lines up suspiciously well with the ⟦TERM⟧ batch above — makes me wonder if that agent wrote scenarios that require more back-and-forth file lookups than it realizes, since it's implicitly encoding its own working habits into the tasks.
3. ⟦TERM⟧ are getting killed off entirely though. Went back through the billing-scenario batch and confirmed, again, that the author agent's own strengths were leaking into which items survived the filter pass.