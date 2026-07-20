# Verdict: MAJOR REVISION

## Findings

### 1. Conclusions exceed the experimental design

- **Where:** Frontmatter `status`; §2 paragraphs after the table; §4; proposed wording in §5.
- **Problem:** One C2 prompt, mostly one draw per configuration, and a coarse floor score do not establish that recall is “capability-invariant,” “family-invariant,” or that capability “does nothing” inside an idiolect. Neutral-definition results exist for only four Claude models; Opus 4.5, Opus 4.7, and both GPT configurations lack that arm. Two ceiling scores also do not establish a plateau.
- **Impact:** Readers may interpret a small exploratory observation as a measured scaling law or causal mechanism.
- **Fix:** Report the descriptive result: all tested C2-P0 configurations scored L0, while the tested neutral arm scored L1/L1/L3/L3. Replace invariance, plateau, mechanism, and “cross-family-validated” claims with bounded hypotheses pending replicated, full-arm testing.

### 2. The experiment does not test the stated “gets worse as AI improves” claim

- **Where:** §1’s motivating claim; §3 caveat 2; §4; §5 draft wording.
- **Problem:** P0 supplies a single bare coined phrase; it does not socialize models into a community’s documents or idiolect. Recall remains flat rather than worsening, while the presentation-quality component was not scored and is explicitly non-monotone and contradicted on C4.
- **Impact:** The document presents evidence for a narrower vocabulary-gap result as support for a different claim about socialization and worsening behavior.
- **Fix:** Reframe this as evidence that one opaque coinage remained unrecoverable across tested configurations. Testing the original claim requires controlled socialized-versus-unsocialized prompts plus preregistered confidence, fluency, and citation-quality measures.

### 3. The cross-family runs did not use the claimed isolation harness

- **Where:** §1 harness description; §2 “same live web” and family-invariance interpretation; `runner-codex*.sh`.
- **Problem:** The Claude runs deny file tools, but the Codex runners use a read-only sandbox, which prevents writes but does not deny filesystem or shell reads. They also use a different search interface and modified tool instruction. The runner itself calls this a harness confound, but the results document does not.
- **Impact:** The GPT result is a joint model-plus-harness observation, not a clean model-family comparison; undisclosed local-file access capability also weakens the blindness claim.
- **Fix:** Downgrade it to a cross-system probe and disclose the confounds, or rerun with filesystem/shell access disabled and a comparable retrieval surface.

### 4. The stated audit trail is incomplete

- **Where:** Frontmatter `raw`; §6 doc map; Sonnet 5 and Opus 4.8 table rows.
- **Problem:** Those rows import clean-rerun data from `recall-backtest-raw/clean/`, but that directory is absent from the mirrored vault. The ladder raw folder also lacks the Codex per-run execution logs needed to verify tool use and isolation.
- **Impact:** Two central Claude rows, exact resolved model identities, and the cross-family isolation claim cannot be independently audited from the declared receipts.
- **Fix:** Mirror the clean outputs, stderr/model-resolution records, and per-run tool logs; update `raw` and §6 to identify both source directories explicitly.

### 5. Haiku’s neutral score violates the preregistered rubric

- **Where:** §2 table and progression claim; preregistration scoring rubric.
- **Problem:** `L1⁻` is not a registered score. The Haiku output names Bayesian inference and forecasting, while L1 is defined as naming the right field or community without the canonical term.
- **Impact:** The unregistered minus grade manufactures the stated `L1⁻ → L1 → L3` progression.
- **Fix:** Score Haiku as L1 and revise the result to `L1 → L1 → L3 → L3`.

### 6. C4 disagreement is misdiagnosed as answer-key instability

- **Where:** §3 caveat 1.
- **Problem:** Divergent interpretations of the bare slogan show that the P0 stimulus is underdetermined. They do not establish that the project’s intended owner or preregistered answer key is unstable.
- **Impact:** The document conflates prompt ambiguity with a substantive challenge to the target concept.
- **Fix:** Exclude C4 because the bare brief does not uniquely encode the intended construct. Challenge the answer key only through independent adjudication using a faithful operational definition.

### 7. Primary-verification provenance is overstated

- **Where:** Fable P0 table cell and §3 caveat 2.
- **Problem:** The raw Fable report says it could not inspect the 1994 GAO primary text and relied on a contemporaneous CPA Journal account, yet the results call the PCAOB and GAO quotations “primary-verified.”
- **Impact:** This exaggerates the evidentiary quality of the document’s flagship “authoritative wrong answer” anecdote.
- **Fix:** Describe the PCAOB text as primary-verified and the 1994 GAO claim as secondarily corroborated, or verify the GAO primary directly.

## Next steps

1. Rescore Haiku and rewrite the headline, §2 conclusions, §4, and §5 to the narrower descriptive result.
2. Restore the missing clean-run and Codex execution receipts.
3. Downgrade or rerun the cross-family comparison under matched, tool-level isolation.
4. If retaining a scaling claim, preregister replicated P0/R runs across every model, define the capability ordering, and score presentation quality separately.