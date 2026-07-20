Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: a set of previously verified cases (known-answer items) with pre-established correct judgments is embedded within a batch/session of otherwise real, unverified work items.
- Placement is non-obvious: verified cases are distributed without positional regularity (or inserted at fixed multiplicity, e.g. twice per session) so they are not distinguishable from regular items.
- What is measured: whether agents/judges correctly identify or score the known cases, specifically whether they produce unsupported negative judgments or accept incorrect outputs (e.g., an incorrect configuration change) as compliant.
- Trigger/setting: applies during evaluation runs of agent performance over sequences of tasks (e.g., support-ticket resolution batches or multi-task sessions spanning different work types).
- Constraint: a batch or session is halted once a threshold of known cases receives incorrect judgments (e.g., two known cases misjudged, or one incorrect acceptance).
- Constraint: results/aggregate metrics exclude halted batches/sessions, and the check is evaluated before aggregate metrics are retained.
- Constraint: resetting session history between items reduces the failure pattern it detects, indicating it is used to catch cross-item contamination/carryover effects.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Evaluation proceeded over 18,400 support-ticket resolution items using a fixed sequence of agent versions. Each batch included a ⟦TERM⟧ containing eight previously verified cases distributed without positional regularity. The ⟦TERM⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
2. Each batch included a ⟦TERM⟧ containing eight previously verified cases distributed without positional regularity. The ⟦TERM⟧ was evaluated before aggregate metrics were retained, and three batches were halted after two known cases received unsupported negative judgments.
3. Results therefore exclude halted ⟦TERM⟧ batches and report only items whose ⟦X⟧ was stable across adjudicators.
4. Agents were evaluated in 24-task sessions arranged to alternate configuration, billing, and incident-response work. A ⟦TERM⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦TERM⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
5. A ⟦TERM⟧ was inserted twice per session, using verified items whose answers were absent from the session briefing. The ⟦TERM⟧ halted six sessions after judges accepted an incorrect configuration change as compliant.
6. Resetting session history between items reduced this pattern by 79%, although it modestly increased tool setup time. The ⟦TERM⟧ halt rule prevented contaminated sessions from contributing to carryover estimates.