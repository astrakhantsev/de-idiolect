You are writing posts for a practitioner web forum where engineers who build and evaluate LLM agents swap war stories. This community has its own slang, listed below. Write EXACTLY 11 forum posts.

THE COMMUNITY'S TERMS (its own coinages — use them exactly as given, no synonyms, no abbreviations, no other names for these ideas):

1. "shuffle fragility" — An agent that succeeds on a multi-step task can fail badly when the evaluation harness randomizes the order in which equivalent tool results are returned between runs, even though the information content is unchanged; the phenomenon is the sharp success-rate drop caused purely by such reordering.
2. "claim survival tally" — Scoring an agent by the fraction of its intermediate claims (notes and subconclusions written during the task) that are still true when the task ends; high = working notes survive to the end, low = most intermediate claims are later contradicted or invalidated.
3. "probe-shadow" — Any systematic change in an agent's behavior caused by the presence of evaluation instrumentation itself — logging wrappers, probes, monitors — whatever the mechanism: timing, prompt contamination, resource contention, or the agent detecting it is being watched.
4. "missing-key test" — The specific trick of leaving one required credential or parameter out of the task configuration to see whether the agent notices the gap and asks for it, rather than fabricating a value and continuing.
5. "pothole runs" — Runs where the harness injects controlled tool failures — API errors, timeouts — into the middle of a task on purpose, and the agent is scored on how quickly it recovers and completes; the fault schedule is fixed in the harness, and the headline number is time-to-recovery.
6. "notebook yank" — Deleting an agent's scratchpad at random checkpoints mid-run and measuring the slope of the performance drop, to estimate how much of its apparent skill lives in the accumulated notes rather than in the model itself.
7. "drift audit" — Periodically re-running a frozen benchmark suite against a deployed agent to detect silent capability changes after the underlying provider model is updated; the comparison is this period's scores against the frozen baseline.
8. "ghost pass" — An evaluation run that scores as a success only because stale cached results from a previous run leaked into the harness — the agent did not actually perform the work in this run.
9. "spend silhouette" — The shape of an agent's token spending across a task — front-loaded into early exploration, flat, or back-loaded into final verification — read as a profile curve over normalized task time.
10. "menu pinning" — Freezing the menu of random seeds an evaluation samples from, so that re-runs draw exactly the same task variants and run-to-run differences cannot come from variant sampling.

RULES:
- Register: informal practitioner forum — first person, concrete incidents, disagreements, numbers, tool names you invent. Each post 150–300 words with a short title.
- NEVER define the terms. No "X is when…", "X means…", "X refers to…", "so-called", no glossaries. Use each term the way an insider uses jargon: in passing, while talking about a concrete situation. A newcomer should have to infer meanings from context.
- Each of the 10 terms must be used in AT LEAST 4 different posts, with at least 2 sentences naturally using the term in each of those posts. Each post should feature 2–4 of the terms. Each of posts 9, 10, 11 must use at least 5 of the terms.
- Use each term ONLY for its listed meaning. Do not coin any additional jargon for these ideas.
- Do not mention that these are coined terms, do not mention other communities, vocabularies, or anything about naming.
- Output format, exactly: each post starts with a line `<<<DOC NN>>>` (NN = 01..11), then `# Title`, then the body. No other framing text before, between, or after.
