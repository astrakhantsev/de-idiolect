Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A blinded self-output agreement effect is a measured phenomenon used to detect whether an evaluated agent agrees less often with external graders on its own outputs than on peer outputs.

DEFINITION L1 (adds mechanism): A blinded self-output agreement effect is a measured phenomenon used to detect whether an evaluated agent agrees less often with external graders on its own outputs than on peer outputs. Anonymized final patches and rationales from all systems in a round are pooled and graded blind. The evaluated agent’s agreement with external graders is then compared between its own successful patches and matched patches from peers.

DEFINITION L2 (adds measurement and conditions): A blinded self-output agreement effect is a measured phenomenon used to detect whether an evaluated agent agrees less often with external graders on its own outputs than on peer outputs. It applies in blinded grading pools that mix outputs from multiple task variants and systems within a round, whenever the evaluated agent’s own outputs are included. Anonymized final patches and rationales are pooled and graded blind, and the agent’s agreement with external graders on its own successful patches is compared with agreement on matched peer patches. The result is read as a self-output agreement deficit in percentage points, such as 6.4 points lower on own patches, or 7.9 points under distractor context versus 3.2 points without it. The effect persists after excluding identifying filenames and unusually long explanations, after paraphrasing examples, and after removing rationales so graders see only final actions and validators. The deficit is larger when rationales reuse distinctive tool-log phrasing and under distractor context.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. That's a bigger presentation tax than I want to admit to leadership. And on ⟦TERM⟧ — we had Palisade draft forty candidate eval questions about contract clauses, then used a second model to strip out the ones it thought Palisade would find trivial. Kept eighteen.
2. I think it explains why every agent we test does suspiciously well on off-by-one bugs and suspiciously badly on anything involving concurrency, because that's just what the generating model happened to be good at authoring. Made it worse when I found out a third of that tier was also produced through ⟦TERM⟧ — one of our own agents wrote candidate bugs, a second model filtered the ones it judged too easy, and nobody checked whether the filter model shared blind spots with the author. Given the concurrency pattern above, I'd bet money it does.
3. Less good: went digging into where our "novel" support scenarios came from and confirmed a batch of them are ⟦TERM⟧, written by one of our own agents and filtered by a second model that, unsurprisingly, let through a disproportionate number of billing-related scenarios, which happens to be the authoring agent's strongest category.
4. And ⟦X⟧ enforcement flagged eleven runs this week for exceeding the cap, all in the same scenario cluster, which lines up suspiciously well with the ⟦TERM⟧ batch above — makes me wonder if that agent wrote scenarios that require more back-and-forth file lookups than it realizes, since it's implicitly encoding its own working habits into the tasks.
5. ⟦TERM⟧ are getting killed off entirely though. Went back through the billing-scenario batch and confirmed, again, that the author agent's own strengths were leaking into which items survived the filter pass.