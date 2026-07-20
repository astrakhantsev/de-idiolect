You are writing short excerpts from method-and-results sections of preprints by a research group that studies the evaluation of LLM agents. This group has its own technical vocabulary, listed below. Write EXACTLY 11 excerpts.

THE GROUP'S TERMS (its own coinages — use them exactly as given, no synonyms, no abbreviations, no other names for these ideas):

1. "drift audit" — Checking after every tool call that an agent's stated plan still matches what it actually just did, and flagging the first step where action and stated plan diverge.
2. "intermediate assertion persistence ratio" — Scoring an agent by the fraction of its intermediate claims (notes and subconclusions written during the task) that are still true when the task ends; high = working notes survive to the end, low = most intermediate claims are later contradicted or invalidated.
3. "line-anchored rubric" — A scoring rubric rule requiring every judge criterion to cite the specific transcript line it is scored from, so that no criterion can be scored from overall impression.
4. "seeded-defect audit" — An assessment where a corrupted data artifact is planted mid-task in the agent's inputs on purpose, and the agent passes only if its final output quarantines or flags the corruption rather than silently propagating it; scoring is binary on containment, not on speed.
5. "self-contradiction incidence" — Counting how often an agent's final answer contradicts the output of a tool it itself called earlier in the same run — a per-run incidence of contradiction against its own evidence.
6. "instrumentation latency steering" — The specific effect where latency added by evaluation instrumentation changes which tool an agent selects — slower instrumented tools get picked less often, so the measured tool-choice distribution is an artifact of the instrumentation's added delay.
7. "memory paraphrase perturbation" — Replacing an agent's working memory mid-run with a paraphrase produced by a weaker model, then measuring how far the agent's subsequent actions diverge from the unperturbed run; the divergence quantifies how much capability depends on the exact stored wording rather than on the model.
8. "permutation sensitivity collapse" — An agent that succeeds on a multi-step task can fail badly when the evaluation harness randomizes the order in which equivalent tool results are returned between runs, even though the information content is unchanged; the phenomenon is the sharp success-rate drop caused purely by such reordering.
9. "ghost pass" — A grader configuration bug where items that no judge can parse are silently marked correct instead of being flagged, inflating scores with items that were never actually judged.
10. "specification occlusion" — Deliberately withholding part of a task's relevant information from the agent — any part, through any channel — to measure whether and how the agent seeks the missing information rather than proceeding on assumptions.

RULES:
- Register: impersonal preprint prose — setup, procedure, quantitative results, limitations. Invented datasets, model names, and numbers are fine. Each excerpt 150–300 words with a short section-style title.
- NEVER define the terms. No "X is defined as…", "X refers to…", "we call this X", no glossaries, no introduction-of-terminology sentences. Use each term as established in-group vocabulary while reporting concrete procedures and findings. A newcomer should have to infer meanings from context.
- Each of the 10 terms must be used in AT LEAST 4 different excerpts, with at least 2 sentences naturally using the term in each of those excerpts. Each excerpt should feature 2–4 of the terms. Each of excerpts 9, 10, 11 must use at least 5 of the terms.
- Use each term ONLY for its listed meaning. Do not coin any additional vocabulary for these ideas.
- Do not mention other communities, vocabularies, or anything about naming.
- Output format, exactly: each excerpt starts with a line `<<<DOC NN>>>` (NN = 01..11), then `# Title`, then the body. No other framing text before, between, or after.
