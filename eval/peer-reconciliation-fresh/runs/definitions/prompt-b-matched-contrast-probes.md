Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Mechanism: creates paired versions of the same task (identical required action/configuration change) differing only in added irrelevant context (policy excerpts, tickets, decoy URLs, operational text), then compares agent tool traces between the paired versions.
- Preserves the required action, verification endpoint/validator, and initial system state identical across both paired variants.
- Measures and produces: counts of additional/exploratory tool calls (e.g., extra pages opened, % increase in exploratory calls), change in direct/validation calls (e.g., % decrease), and delay to first valid tool call (in seconds).
- Applies to paired task-family sets (e.g., account-management, service-configuration, navigation, document-heavy tasks) where an irrelevant-context variant is compared against a clean variant.
- Read via navigation-breadth changes (tool-trace exploration) rather than by final answer length or content.
- Outputs from both paired variants are mixed into blinded grading pools for scoring.
- Can be produced per replacement/task family, with results (distractor sensitivity) varying by task type.

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
6. Each task family included ⟦TERM⟧ with identical required actions and variable irrelevant context. ⟦TERM⟧ increased excess tool usage by 26% for the largest agent.
7. Each task family included ⟦TERM⟧ with identical required actions and variable irrelevant context. ⟦TERM⟧ increased excess tool usage by 26% for the largest agent.
8. After example paraphrasing, the ⟦X⟧ rate fell to 1.5% without materially changing ⟦TERM⟧ or ⟦X⟧.
9. ⟦TERM⟧ accompanied each replacement family. ⟦TERM⟧ showed that distractor sensitivity declined for navigation tasks but increased for document-heavy tasks.
10. ⟦TERM⟧ accompanied each replacement family. ⟦TERM⟧ showed that distractor sensitivity declined for navigation tasks but increased for document-heavy tasks.