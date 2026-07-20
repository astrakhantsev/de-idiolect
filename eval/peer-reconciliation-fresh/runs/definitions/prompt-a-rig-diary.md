Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Records each config or parameter change (e.g., naming scheme, cap value, ration bump, rewordings) as a separate, timestamped entry as it happens.
- Entries specify what changed and when, so distinct changes can be individually attributed to distinct outcomes.
- Consulted retrospectively (by scrolling/going back through entries) to identify which change actually caused an observed result.
- Applies whenever an unexpected result or regression appears, to distinguish genuine capability changes from harness/config artifacts.
- Must be updated the same day a change is made, not deferred, or the causal link is lost.
- Logging should occur for every change, including ones that seem too minor to matter.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Good news is the ⟦TERM⟧ actually saved us here. Scrolled back through it and found an entry from eleven days ago noting we'd swapped the artifact-naming scheme in the scorer's config to include run id in the cache key.
2. Went to the ⟦TERM⟧ before touching anything and found the actual change two entries back: someone bumped the cap from four to two the same day, unrelated to what I was originally investigating. Cap of two is just too tight for a five-file task, not a bug in the enforcement code at all.
3. Finally logged all of this in the ⟦TERM⟧ before I forgot which changes went with which result — the ration bump, the twin rewordings, the ⟦X⟧ pass, all timestamped separately, because last time I skipped this step I spent a whole day re-deriving what I'd already tested.
4. ⟦TERM⟧ paid off twice this cycle — once catching the ⟦X⟧ cap change that broke three agents' runs, once catching a scorer config edit that would've otherwise looked like a genuine capability regression instead of a harness artifact. I'm now fully converted on logging every single config change the day it happens, even the ones that feel too small to matter, because the ones that feel too small to matter are exactly the ones I forget by Thursday.