Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A diagnostic measure for detecting whether an evaluator agrees less with judgments of its own successful work than with matched work from peers.

DEFINITION L1 (adds mechanism): A diagnostic measure detects whether an evaluator agrees less with judgments of its own successful work than with matched peer work. Final patches, outputs, or answers and their rationales are anonymized and pooled from multiple agents or systems. The evaluated agent or external graders grade them, or state agreement or disagreement, without knowing which output was the evaluated agent's own.

DEFINITION L2 (adds measurement and conditions): This diagnostic measure uses blinded, anonymized grading pools containing final patches, outputs, answers, and rationales sampled from multiple systems or agents in a round, task variant, or release. The evaluated agent or external graders see the pooled items and grade them, or agree or disagree with them, without knowing which output was the evaluated agent's own. It produces a self-output agreement deficit: the percentage-point gap between agreement with graders on the agent's own successful outputs and agreement on matched peer outputs; reported deficits include 6.4, 7.9, 3.2, and 5.1 points. It also applies when rationale or answer text is stripped and graders see only final actions and validators. The deficit persists after excluding identifying filenames and unusually long explanations, after removing rationale text, and after paraphrasing examples. It is larger with distractor context and concentrated among unusually confident rationales or reused distinctive tool-log phrasing.

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