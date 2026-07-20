Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: sets a hard cap (a "ration") on the number of times an agent may reopen/reread the same file during a run, expressed as a fixed integer (e.g., "three").
- What's measured/scored: counts repeated file opens/rereads per run; a run that exceeds the cap is flagged/fails ("exceeding the cap"), while staying within it is a pass condition for that check.
- Applies to: agentic coding-benchmark runs (e.g., codebase-navigation, file-navigation, onboarding suites) where an agent reads files from disk during task execution.
- Constraint: once the cap is reached, further rereads that would help the agent finish are ignored/not permitted — the agent cannot fall back on unlimited disk access as free scratch space.
- Constraint: enforcement is a configurable setting (a "cap") that can itself be changed, and changing it can alter which agents pass or fail, so cap changes must be distinguished from real capability regressions.

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
5. And ⟦TERM⟧ enforcement flagged eleven runs this week for exceeding the cap, all in the same scenario cluster, which lines up suspiciously well with the ⟦X⟧ batch above — makes me wonder if that agent wrote scenarios that require more back-and-forth file lookups than it realizes, since it's implicitly encoding its own working habits into the tasks.
6. ⟦X⟧ paid off twice this cycle — once catching the ⟦TERM⟧ cap change that broke three agents' runs, once catching a scorer config edit that would've otherwise looked like a genuine capability regression instead of a harness artifact. I'm now fully converted on logging every single config change the day it happens, even the ones that feel too small to matter, because the ones that feel too small to matter are exactly the ones I forget by Thursday.