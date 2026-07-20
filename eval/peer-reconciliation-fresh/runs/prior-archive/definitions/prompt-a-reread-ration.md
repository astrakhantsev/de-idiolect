Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Sets a numeric ⟦TERM⟧ limit (e.g., three) on how many times a file/resource may be reopened or reread by the agent.
- The mechanism enforces this cap during agent execution, causing failure (or a cut-off mid-trace) once the limit is exceeded rather than allowing further rereads.
- It applies to file-navigation-style benchmarks/suites where an agent repeatedly opens the same file (e.g., rechecking a function signature) instead of retaining that content in working memory.
- Exceeding the ⟦TERM⟧ is scored/read as a failure (or forced stop) on that benchmark run, and can be re-run after adjusting or re-verifying the setting.
- The constraint targets rereads specifically — it does not address or enforce any compression of held content (compression is governed separately, under ⟦X⟧).
- Applying or tightening the ⟦TERM⟧ is expected to change aggregate pass-rate metrics (e.g., reduce a "pass-everything" bucket) by failing agents that were succeeding via brute-force repeated file opens.

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