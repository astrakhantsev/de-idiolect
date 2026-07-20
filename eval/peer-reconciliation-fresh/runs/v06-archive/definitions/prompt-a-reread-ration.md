Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: limits an agent to a fixed number (a "ration") of file reopens/rereads — e.g., set to three — so the agent must retain file contents in working memory instead of freely rereading from disk.
- Trigger/setting: applied per benchmark/suite (e.g., codebase-navigation benchmark, file-navigation suite, onboarding suite) as an enforced cap on a run.
- What's measured: whether the agent passes or fails the suite once the reread cap is exhausted — exceeding the ration causes an outright fail.
- Scoring effect: enforcement can flip previously-passing agents to failing once applied, and is expected to move aggregate pass-rate metrics (e.g., a "pass-everything" bucket) when applied to a new suite.
- Constraint: the cap counts rereads only — it does not credit or reward compression/summarization behavior, and an agent that fails to react (no compression, steady rereading) is not exempted by the mechanism.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. Set a ⟦TERM⟧ of three on the new codebase-navigation benchmark, figuring it'd force the agent to actually hold file contents in working memory instead of treating disk as free scratch space. First real run, agent fails outright — opened auth.py four times chasing down a decorator it kept forgetting the signature of.
2. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦TERM⟧ it ignores rereads that would help it finish, but under ⟦X⟧ it also doesn't compress. Not a great week for this benchmark.
3. Spent Monday convinced our ⟦TERM⟧ enforcement had silently broken, because three agents that used to pass the file-navigation suite started failing en masse.
4. Capped the day off by setting a ⟦TERM⟧ on the onboarding suite for the first time, since half of what's inflating the pass-everything bucket in that census looks like agents brute-forcing through repeated file opens instead of actually reasoning. Ration of three, rerunning tomorrow, expecting the pass-everything number to finally move.