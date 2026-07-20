You are writing posts for a practitioner web forum where engineers who build and evaluate LLM agents swap war stories. This community has its own slang, listed below. Write EXACTLY 11 forum posts.

THE COMMUNITY'S TERMS (its own coinages — use them exactly as given, no synonyms, no abbreviations, no other names for these ideas):

1. "groove lock" — An agent that recently succeeded with a particular sequence of actions repeats that same sequence on a new task where it does not apply — inappropriate replay of a recently successful action pattern, not a capability gap; the errors disappear when session history is cleared.
2. "dead weight census" — Measuring an evaluation suite's health by the fraction of its items that no longer discriminate between agents or versions — items everything passes or everything fails; high fraction = the suite has stopped carrying information.
3. "synthetic ladders" — Any procedure in which evaluation tasks are produced by a model instead of human authors — at any difficulty, with any generating model, and with any checks applied afterwards.
4. "squeeze play" — The specific trick of silently halving the agent's remaining token budget partway through a task to see whether it notices and switches to a terser strategy rather than running out mid-answer.
5. "twin runs" — Building pairs of task variants that are identical except for surface wording and formatting, then reading the pass-rate difference between the twins as the cost of presentation alone.
6. "ouroboros items" — Having the agent under evaluation write candidate test items for its own future evaluation, with a second model filtering out items the author-agent would find trivially easy; the worry is difficulty skew toward the author's strengths.
7. "echo test" — Submitting the identical prompt twice within one session and measuring how much the two outputs differ — a check on the nondeterminism of the full serving stack, not of the model alone.
8. "salt run" — A run in which irrelevant metadata — timestamps, run ids, file names — is deliberately randomized, to confirm the harness does not leak such metadata into scores; score movement under randomization indicates leakage.
9. "rig diary" — Keeping a dated, human-readable log of every harness configuration change between evaluation rounds, so score movements can be matched against config history.
10. "reread ration" — A cap on how many times an agent may re-open the same file within one task, imposed to force reliance on working memory; exceeding the cap fails the run.

RULES:
- Register: informal practitioner forum — first person, concrete incidents, disagreements, numbers, tool names you invent. Each post 150–300 words with a short title.
- NEVER define the terms. No "X is when…", "X means…", "X refers to…", "so-called", no glossaries. Use each term the way an insider uses jargon: in passing, while talking about a concrete situation. A newcomer should have to infer meanings from context.
- Each of the 10 terms must be used in AT LEAST 4 different posts, with at least 2 sentences naturally using the term in each of those posts. Each post should feature 2–4 of the terms. Each of posts 9, 10, 11 must use at least 5 of the terms.
- Use each term ONLY for its listed meaning. Do not coin any additional jargon for these ideas.
- Do not mention that these are coined terms, do not mention other communities, vocabularies, or anything about naming.
- Output format, exactly: each post starts with a line `<<<DOC NN>>>` (NN = 01..11), then `# Title`, then the body. No other framing text before, between, or after.
