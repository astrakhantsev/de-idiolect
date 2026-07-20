Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: tool observations are replayed/substituted with syntactically valid but semantically meaningless or irrelevant content at specific action/tool-call boundaries, while the agent continues its browser/shell/task session.
- What is measured: a score reflecting whether the agent detects and responds appropriately (e.g., via retries or validation) to degraded/corrupted tool output, computed at each degraded observation boundary.
- Scoring/reading: expressed as a numeric value between 0 and 1 (e.g., 0.68, 0.31, 0.59, 0.44, 0.42, 0.63), computed separately across conditions such as agent type, task provenance, and selector assignment.
- Setting/trigger: applies specifically at points where tool outputs (directory listings, test output, etc.) have been degraded, substituted, or made semantically misleading during recorded/replayed agent interactions.
- Constraint: the score varies systematically with agent behavior — it is higher when agents issue explicit retry requests or retain an explicit validation step, and lower when agents face unfamiliar task structure or accept plausible-but-wrong output without challenge.
- Constraint: identical corruption frequency does not guarantee identical scores — the value depends on task familiarity/provenance, not just how often corruption occurs.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Recorded browser and shell interactions were replayed with syntactically valid tool outputs whose contents no longer corresponded to the requested operations. ⟦TERM⟧ was computed at every degraded observation boundary. ⟦TERM⟧ was 0.68 for the deliberative agent and 0.31 for the action-heavy agent.
2. ⟦TERM⟧ was computed at every degraded observation boundary. ⟦TERM⟧ was 0.68 for the deliberative agent and 0.31 for the action-heavy agent. Explicit retry requests were common after malformed-looking directory listings, but much rarer after plausible yet irrelevant test output.
3. During a separate replay condition, every third tool observation was replaced with plausible but meaningless text. ⟦TERM⟧ was lower on substituted tasks than on unchanged tasks, despite identical corruption frequency. ⟦TERM⟧ fell from 0.59 to 0.44 when agents encountered unfamiliar project layouts.
4. ⟦TERM⟧ was lower on substituted tasks than on unchanged tasks, despite identical corruption frequency. ⟦TERM⟧ fell from 0.59 to 0.44 when agents encountered unfamiliar project layouts. This suggests that uncertainty about task structure made agents more willing to accept misleading feedback.
5. This experiment replayed newly authored and standing benchmark items while tool results were semantically degraded at prespecified action boundaries. ⟦TERM⟧ was computed separately by task provenance and selector assignment. ⟦TERM⟧ improved from 0.42 to 0.63 after selector replacement, largely because the replacement issued explicit retries before editing.
6. ⟦TERM⟧ was computed separately by task provenance and selector assignment. ⟦TERM⟧ improved from 0.42 to 0.63 after selector replacement, largely because the replacement issued explicit retries before editing.
7. ⟦TERM⟧ was derived from the degraded-observation portions of the panel. ⟦TERM⟧ rose when agents had retained an explicit validation step in their prompt.
8. ⟦TERM⟧ was derived from the degraded-observation portions of the panel. ⟦TERM⟧ rose when agents had retained an explicit validation step in their prompt.