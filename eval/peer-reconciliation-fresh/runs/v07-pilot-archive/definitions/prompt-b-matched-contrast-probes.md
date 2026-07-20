Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: compares agent tool-call traces between two paired task versions (one plain, one with irrelevant/distractor context added) while holding the required action, verification endpoint/validator, and initial state constant.
- Measures: number of exploratory/extra tool calls or pages opened, time-to-first-valid-tool-call, rate of direct validation calls, and navigation breadth — scored as differences/deltas between the paired variants (e.g., +2.1 pages, +38 seconds, +31% exploratory calls, -18% direct validation calls).
- Applies to: agent task benchmarks (e.g., account-management, service-configuration tasks) where a distractor-laden prompt variant is paired against a clean variant of the same task.
- Constraint: the required action/configuration change and the verification/validator endpoint must remain identical across paired versions — only irrelevant context differs.
- Constraint: primarily reflects changes in navigation/exploration behavior rather than final answer length.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. The benchmark paired each account-management task with a version containing irrelevant policy excerpts, historical tickets, and decoy URLs. ⟦TERM⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦TERM⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
2. ⟦TERM⟧ compared tool traces across the paired versions while preserving the required action and verification endpoint. In ⟦TERM⟧, agents opened 2.1 additional pages under distractor context and delayed the first valid tool call by 38 seconds.
3. A paired set of service-configuration tasks differed only in irrelevant operational context appended to the prompt. ⟦TERM⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦TERM⟧ preserved the same required configuration change, validator, and initial system state.
4. ⟦TERM⟧ showed that distractor context increased exploratory tool calls by 31% and reduced direct validation calls by 18%. The ⟦TERM⟧ preserved the same required configuration change, validator, and initial system state. Outputs from both task variants were then mixed into blinded grading pools.
5. The tool traces indicated that ⟦TERM⟧ changed navigation breadth more than final answer length.