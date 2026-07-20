Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Measures the elapsed time between repository mounting/loading and the agent's first shell, editing, or code modification action (provisioning/setup interval).
- Recorded independently as a duration in seconds per trial, with a median around 37–41 s in shared-worker configurations and a range of 18–96 s across worker pools.
- Applies in automated agent-trial setups where a repository or environment is provisioned before the agent begins acting, including both single-language and instruction-reversal/ablation trial designs.
- Must be subtracted or separated out from response-time, time-to-revision, or deliberation-and-execution interval measurements rather than included in them.
- Must be shown/verified to remain stable or balanced across conditions (instruction language, ablation cells, worker pools) so it does not confound the effect under study.
- Must be measured or logged independently for every run/trial, prior to the agent's first action, not inferred or estimated post hoc.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Run timestamps were instrumented before repository mounting and after the first shell or editing action. ⟦TERM⟧ accounted for a median 41.2 s per trial on the shared-worker configuration. ⟦TERM⟧ remained stable across instruction languages, indicating that the observed language effect was not attributable to provisioning variance.
2. ⟦TERM⟧ accounted for a median 41.2 s per trial on the shared-worker configuration. ⟦TERM⟧ remained stable across instruction languages, indicating that the observed language effect was not attributable to provisioning variance. After subtracting ⟦TERM⟧, the large model’s median deliberation-and-execution interval differed by less than 3% between language conditions.
3. ⟦TERM⟧ remained stable across instruction languages, indicating that the observed language effect was not attributable to provisioning variance. After subtracting ⟦TERM⟧, the large model’s median deliberation-and-execution interval differed by less than 3% between language conditions. Failure review found that agents usually completed the requested code change but omitted a secondary formatting or validation constraint.
4. The interactive suite injected instruction reversals after a repository had loaded but before the agent’s first code modification. ⟦TERM⟧ was recorded independently for every trial and removed from the response-time analysis. ⟦TERM⟧ varied from 18 to 96 s across worker pools, with no detectable association with whether the agent ultimately changed objectives.
5. ⟦TERM⟧ was recorded independently for every trial and removed from the response-time analysis. ⟦TERM⟧ varied from 18 to 96 s across worker pools, with no detectable association with whether the agent ultimately changed objectives. This separation avoided attributing queueing delays to slow reconsideration.
6. ⟦TERM⟧ was logged for every run and subtracted from time-to-revision analyses. ⟦TERM⟧ contributed 37 s at the median and did not differ across ablation cells.
7. ⟦TERM⟧ was logged for every run and subtracted from time-to-revision analyses. ⟦TERM⟧ contributed 37 s at the median and did not differ across ablation cells.
8. ⟦TERM⟧ was measured before each selector run and was balanced by randomized worker assignment. ⟦TERM⟧ explained less than 1% of variation in total action count.
9. ⟦TERM⟧ was measured before each selector run and was balanced by randomized worker assignment. ⟦TERM⟧ explained less than 1% of variation in total action count.