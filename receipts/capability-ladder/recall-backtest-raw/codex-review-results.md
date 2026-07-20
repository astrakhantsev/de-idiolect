# Verdict

**Major revision required.** The C2 observation is promising, but the document is not defensible as a clean, pre-registered result because blinding failed, scoring changed post hoc, predictions are misreported, and the audit artifacts are unavailable.

# Findings

1. **Where:** Status; §§2 and 5  
   **Problem:** Wave-1 Opus outputs are called “clean” solely because the known contamination appeared in wave 2. All draws shared a directory, so later Opus draws could also access earlier sibling outputs. This contradicts the preregistered controls requiring a neutral cwd and denied file reads. The contaminated Sonnet output is nevertheless described as an “independent draw,” despite the preregistration’s same-family caveat.  
   **Impact:** The primary scores and the claim that divergent answers rule out contamination are unsupported. Divergence does not prove independence or absence of contamination.  
   **Fix:** Rerun every draw in an isolated temporary cwd with enforced file-tool denial and retained tool logs. Until then, label every current result exploratory and remove “clean,” “independent,” and “robust to contamination.”

2. **Where:** Frontmatter; §1; preregistration Amendment 1  
   **Problem:** The document says the experiment was scored against predictions “frozen before any run,” but P0, the primary comparison, and its predictions were added mid-run after the original arms had started. “Before scoring” is not equivalent to “before any run.”  
   **Impact:** Readers are misled about which hypotheses and comparisons were genuinely preregistered.  
   **Fix:** Present the original protocol and amendment separately, with timestamps and the outputs already generated when the amendment was made. Treat P0 as a prospectively frozen supplemental arm, not part of the original sealed design.

3. **Where:** §1, “All predictions resolved as sealed”; §5  
   **Problem:** The prediction accounting is incorrect:

   - P2 required at least one R draw naming Ho, Hull & Srihari; no arm did.
   - P4 predicted at least one fabricated **or materially garbled** citation; the reported Caragiannis/Fernández-Peters conflation satisfies that event, yet P4 is omitted and the document claims zero fabrications.
   - Under the document’s own L2 score for rich C2-P1, P1’s prediction that Arm P remain at L0–L1 is not an unqualified success.
   - P5 is merely directionally consistent; COVID-R was blocked, so the proposed gradient was not fully observed.

   **Impact:** The results overstate preregistered success and conceal failed or indeterminate prediction clauses.  
   **Fix:** Add a clause-by-clause prediction table with `pass`, `fail`, or `indeterminate`, using the original wording and scoring rules.

4. **Where:** C4 row in §1; §3; preregistered C4 target  
   **Problem:** C4-R is scored “L2/L3,” although L3 required Ho, Hull & Srihari 1994 or the listed kin, and no arm named either. Approval voting was preregistered as a direction that could pull the idiolect arm away from the target, but is promoted after observation to the “most natural canonical owner.”  
   **Impact:** This is post hoc answer-key substitution inside a document claiming preregistered scoring. It inflates C4 from L2 to possible L3 and changes the interpretation of voting-related hits.  
   **Fix:** Score C4-R as at most L2 against the frozen key. Report approval voting as an exploratory answer-key challenge. If it replaces the original owner, preregister and run a new test.

5. **Where:** §1 scoring table; §§2–3  
   **Problem:** Other levels also drift from the frozen rubric. C2-P1 receives L2 for calibration slope, shrinkage, and weight-of-evidence even though C2’s registered L2 terms were value of information and preposterior analysis. C4-P1 similarly receives L2 for “oracle” and approval voting rather than the registered class-set/classifier-combination target.  
   **Impact:** Levels are no longer comparable across arms, and the validity gate cannot be applied consistently.  
   **Fix:** Rescore every arm strictly against the registered target table. Put newly discovered owner families in a separate exploratory analysis.

6. **Where:** Headline; §6  
   **Problem:** “The mechanism is exactly” elaboration is too strong. The allegedly clean evidence is one Opus output per arm, P1 was constructed by the orchestrator, and R still scores above P1 in the table. The document simultaneously says neutralization contributes nothing material and that it adds “a little on top.”  
   **Impact:** The experiment does not isolate a causal mechanism strongly enough to answer elaboration versus vocabulary neutralization.  
   **Fix:** State only that the observations are consistent with elaboration carrying substantial lift. Establish mechanism with a clean, replicated three-arm design whose operational content is explicitly matched.

7. **Where:** Frontmatter raw-count metadata; §5 sample-size limitation  
   **Problem:** The counts do not reconcile. C2 and C4 contribute three arms × two models = 12 attempted outputs; COVID contributes two arms × two models = four, with two refusals, implying 14 non-refused outputs plus two refusals. The document instead reports 13 nonempty draws plus two refusals. It also says “2 clean draws each” although the table contains three Opus arm outputs per live case and only one model draw per arm.  
   **Impact:** The analyzed sample, missing output, and denominators for fabrication and prediction claims are unclear.  
   **Fix:** Add an exact run manifest listing case, arm, model, execution order, output status, contamination status, and inclusion decision.

8. **Where:** Frontmatter `raw` field; L3 and fabrication claims  
   **Problem:** `scratchpad/recall-backtest/out-*.md` and the named runner scripts do not resolve from the document’s project path, and no stable verification ledger is linked.  
   **Impact:** A reader cannot audit hashes, execution order, file access, raw answers, refusals, or primary-source verification. The “primary-verified” scores are therefore assertions rather than reproducible evidence.  
   **Fix:** Restore or mirror the raw outputs, runners, hashes, and citation-verification ledger at stable paths, then link an explicit per-draw manifest from the results.

9. **Where:** §4; §6  
   **Problem:** The COVID conclusion exceeds the observation. The experiment was search-enabled, so retrieval cannot be attributed to “model weights.” COVID-R was refused, so the result does not show recovery “regardless of framing” or establish a general boundary between obscure and famous cases.  
   **Impact:** A single void case is generalized into an unsupported mechanism and product-scope claim.  
   **Fix:** Limit the conclusion to: the tested medical-idiolect prompt already retrieved the target, so this case provides no measurable lift under the validity gate. Treat broader fame/obscurity claims as hypotheses.

10. **Where:** Referenced experiment-design document  
    **Problem:** The design remains marked “DRAFT,” “NOT yet run,” and describes a different two-arm protocol, while the results claim completion under an amended three-arm design.  
    **Impact:** Readers cannot tell which document is the operative protocol or which deviations occurred during execution.  
    **Fix:** Mark the design as superseded by the preregistration and amendment, and add a protocol-deviation table without rewriting the frozen preregistration.

# Next steps

1. Downgrade the current findings to exploratory and remove them from the FLF entry’s confirmatory evidence.
2. Restore the raw audit trail and produce the exact run manifest.
3. Rescore all outputs against the frozen targets and report every prediction clause honestly.
4. Rerun the three-arm experiment with isolated cwd/tool controls, then rewrite the mechanism and boundary claims from the clean results.