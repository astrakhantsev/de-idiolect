Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Enforces a fixed numeric limit ("ration") on how many times an agent may open/reread the same file's contents during a run.
- Set as a count of allowed file-open/reread actions (e.g., a ⟦TERM⟧ of three), applied per file or per target resource.
- Applies during agent benchmark runs (e.g., codebase-navigation, file-navigation, onboarding suites) where an agent reads files while working.
- Once the limit is reached, further rereads that would help the agent finish are ignored/blocked rather than granted.
- Triggers agent failure or task cutoff when the agent exceeds the ration and cannot proceed without additional rereads.
- Does not cause the agent to compress or otherwise adapt its behavior in response to the limit—it simply keeps failing or gets cut off.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Set a ⟦TERM⟧ of three on the new codebase-navigation benchmark, figuring it'd force the agent to actually hold file contents in working memory instead of treating disk as free scratch space. First real run, agent fails outright — opened auth.py four times chasing down a decorator it kept forgetting the signature of.
2. Agent didn't visibly react at all, just kept reading files at the same pace until it got cut off mid-trace. So under the ⟦TERM⟧ it ignores rereads that would help it finish, but under ⟦X⟧ it also doesn't compress. Not a great week for this benchmark.
3. Spent Monday convinced our ⟦TERM⟧ enforcement had silently broken, because three agents that used to pass the file-navigation suite started failing en masse.
4. Capped the day off by setting a ⟦TERM⟧ on the onboarding suite for the first time, since half of what's inflating the pass-everything bucket in that census looks like agents brute-forcing through repeated file opens instead of actually reasoning. Ration of three, rerunning tomorrow, expecting the pass-everything number to finally move.