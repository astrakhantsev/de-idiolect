Working from term-matching against established literature, not from any knowledge of this specific project — treat the citations below as pointers to verify, not settled facts. I'm most confident about the *fields*, less confident about the *exact papers*, and I'll flag anything I'm reconstructing from memory rather than citing solidly.

## TERM-1: "m*" — per-question critical count of judge audits

**Canonical term(s):** No single universal name — this sits at the intersection of several established problems: "sample size / stopping-rule determination," "optimal number of labels per item" (crowdsourcing), or "audit sample size" (statistical auditing). If your project is drawing on election/financial audit statistics, the closest canonical term is **risk-limiting audit sample size**; if drawing on crowdsourcing/label-aggregation, it's **optimal redundancy per item**.

**Fields:** Statistics (sequential analysis, survey/audit sampling), machine learning (crowdsourcing/truth inference), psychometrics (generalizability theory).

**Oldest treatments:**
- Wald, A. (1945). "Sequential Tests of Statistical Hypotheses." *Annals of Mathematical Statistics*, 16(2), 117–186. — origin of sequential/stopping-rule sample-size theory. High confidence this is real and correctly dated.
- Cronbach, L.J., Gleser, G.C., Nanda, H., & Rajaratnam, N. (1972). *The Dependability of Behavioral Measurements* (Wiley). — generalizability theory; addresses how many raters/observations per subject are needed for reliable measurement. High confidence.
- Dawid, A.P. & Skene, A.M. (1979). "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm." *JRSS Series C*, 28(1), 20–28. — foundational noisy-labeler aggregation model. High confidence.
- Sheng, V.S., Provost, F., & Ipeirotis, P.G. (2008). "Get Another Label? Improving Data Quality and Data Mining Using Multiple, Noisy Labelers." *KDD 2008*. — directly addresses "how many labels does each item need," which is the closest analogue I know of to "m* per question." Moderate-high confidence on the citation, worth checking title/venue exactly.
- If it's audit-sampling-flavored specifically: Stark, P.B. (2008). "Conservative Statistical Post-Election Audits." *Annals of Applied Statistics*, 2(2), 550–581. Moderate confidence — I recall this paper existing and being foundational to risk-limiting audits, but I'm less sure of exact volume/page numbers.

**Confidence:** Low-moderate on which family is actually the right ancestor — "m*" and "critical count" language could come from any of sequential testing, crowdsourcing, or audit sampling, and I can't tell which without seeing how the project defines the audit process. **Verify first:** whether the "judge audits" are more like repeated noisy labels (→ crowdsourcing/Dawid-Skene lineage) or more like confirmatory sampling against a margin/error bound (→ audit-sampling/SPRT lineage) — that distinction picks the field.

## TERM-2: "the operating requirement" — cold-start operating requirement for the audit unit

**Canonical term(s):** **Cold-start problem** is the well-established term, but almost always paired with a *domain* (cold-start in recommender systems, cold-start in reinforcement learning/bandits). "Operating requirement" itself isn't a term I recognize as canonical — it reads like local project vocabulary for what the literature would call a **burn-in / warm-up requirement** or **minimum baseline sample size**.

**Fields:** Machine learning / recommender systems (cold-start), statistical process control (Phase I baseline requirements), reliability engineering (burn-in period), Bayesian computation (warm-up/burn-in in MCMC).

**Oldest treatments:**
- Schein, A.I., Popescul, A., Ungar, L.H., & Pennock, D.M. (2002). "Methods and Metrics for Cold-Start Recommendations." *SIGIR 2002*. — moderate confidence, this is the paper I associate with formalizing "cold-start" in recommenders, but double-check title/authorship order.
- Metropolis, N. et al. (1953) / Hastings, W.K. (1970) — origin of MCMC and, informally, the "burn-in" concept, though "burn-in" as a named requirement is more a folk term that solidified later (often attributed loosely to Gelman et al.'s *Bayesian Data Analysis*, first edition 1995). Low confidence on precise attribution of the term itself.
- Montgomery, D.C. *Introduction to Statistical Quality Control* (various editions since 1985) — standard reference for Phase I/Phase II control chart minimum-sample requirements. Moderate confidence this is the right textbook, low confidence on edition/year to cite.

**Confidence:** Low. This is the weakest match of the four — "operating requirement" doesn't pattern-match cleanly onto one canonical term, so I'm inferring the *concept* (minimum data/time before a system can be trusted) rather than recognizing a named result. **Verify first:** what "operating" means mechanically here — is the audit unit a statistical estimator that needs a minimum n before its guarantees kick in (→ cold-start/burn-in lineage), or is it closer to a control/monitoring system needing a baseline period (→ SPC Phase I lineage)? That determines which literature actually applies.

## TERM-3: "the signal, not the cut, is the bottleneck" — gate over judge credences

**Canonical term(s):** This is a restatement of the **calibration/discrimination distinction** in forecasting and classifier evaluation, or equivalently the **sensitivity vs. criterion (threshold)** distinction in **Signal Detection Theory**. The claim "no threshold fixes a weak underlying score" is essentially "discrimination is threshold-invariant and is the ceiling on performance; the operating point (cut) only trades off error types along that ceiling." This is a strong, well-matched claim.

**Fields:** Psychophysics/psychology (signal detection theory), statistics/meteorology (forecast verification — calibration vs. resolution), machine learning (ROC/AUC analysis).

**Oldest treatments:**
- Peterson, W.W., Birdsall, T.G., & Fox, W.C. (1954). "The Theory of Signal Detectability." *IRE Professional Group on Information Theory*. — the earliest formal SDT treatment I'm aware of. Moderate confidence on exact venue name, high confidence it's roughly right (1954, radar detection theory origin).
- Green, D.M. & Swets, J.A. (1966). *Signal Detection Theory and Psychophysics*. Wiley. — the canonical textbook that established sensitivity (d′) vs. criterion (β/c) as separate, orthogonal quantities. High confidence.
- Murphy, A.H. (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology*, 12(4), 595–600. — decomposes forecast skill into calibration (reliability) and resolution/discrimination components, giving a statistical rather than psychophysical version of the same claim. Moderate-high confidence.
- Fawcett, T. (2006). "An Introduction to ROC Analysis." *Pattern Recognition Letters*, 27(8), 861–874. — modern ML statement that AUC (threshold-independent discrimination) is separate from, and upstream of, any particular threshold choice. High confidence.

**Confidence:** Moderate-high on the field and framing; moderate on the specific citations (Peterson/Birdsall/Fox venue details are the shakiest). **Verify first:** confirm the project's "gate" is literally a threshold on a scalar judge credence (score/probability) — if so this is squarely SDT/calibration territory and Green & Swets is the right anchor text to cite as the origin of the sensitivity-vs-criterion vocabulary.

## TERM-4: "read the enumerations, not the votes" — using panel judge outputs

**Canonical term(s):** Maps onto **process-level vs. outcome-level supervision** in the recent LLM-judge/verifier literature, and more broadly onto **analytic vs. holistic scoring** in assessment, and **structured content coding vs. summary rating** in content analysis. The core claim — that itemized/structured output carries more signal than the final aggregate judgment — has independent, older roots in measurement/assessment theory as well as a very current instantiation in LLM evaluation.

**Fields:** NLP/ML (LLM-as-judge, process supervision), educational measurement (writing assessment, rubric scoring), communication research/social science (content analysis).

**Oldest treatments:**
- Cooper, C.R. (1977). "Holistic Evaluation of Writing," in *Evaluating Writing* (NCTE). — early formal discussion of holistic vs. analytic (itemized) scoring in writing assessment. Low-moderate confidence on exact citation details, but the holistic/analytic distinction in writing assessment is genuinely that old.
- Krippendorff, K. *Content Analysis: An Introduction to Its Methodology* (Sage, 1980; multiple later editions). — foundational text on coding structured content categories rather than relying on holistic ratings. High confidence the book and rough date are right.
- Cobbe, K. et al. (2021). "Training Verifiers to Solve Math Word Problems." arXiv (OpenAI, GSM8K paper). — early instance of using structured/step-level signals over final-answer votes in ML verification. Moderate-high confidence this exists and is roughly dated correctly.
- Lightman, H. et al. (2023). "Let's Verify Step by Step." OpenAI/arXiv (later appeared at ICLR 2024). — the most directly analogous modern paper: shows process-level (itemized, step-by-step) supervision beats outcome-level (final vote/label) supervision. Moderate-high confidence on content and rough date, lower confidence on exact venue/year of formal publication (arXiv 2023 vs. conference 2024).

**Confidence:** Moderate. The pre-2015 anchor here (Cooper 1977, or Krippendorff 1980) is weaker than I'd like — I'm reconstructing rough vintage and thrust rather than quoting specifics, and "holistic vs. analytic scoring" is a large literature I can't pin to one originating paper with confidence. The post-2020 anchor (Lightman/Cobbe) is the stronger, more directly relevant match but doesn't satisfy "before 2015." **Verify first:** whether "enumerations" means itemized reasoning/error lists (→ process supervision / analytic scoring lineage, my best guess) or literally means calibrated probability outputs versus discrete votes (→ soft-voting vs. hard-voting in ensemble learning instead) — those are different literatures and the term is genuinely ambiguous between them from the gloss alone.

---

**Overall caveat:** all four terms have a strong "LLM-as-judge panel / scalable-oversight audit system" flavor (2023–2025 vintage), which is itself a live, fast-moving research area I can't search right now. If that's the actual home field, the most useful next step is checking recent arXiv work on "LLM judge panels," "panel of LLM evaluators" (I recall a paper nicknamed "PoLL" — Panel of LLM evaluators — from ~2024, though I can't give you author/venue with confidence), and "scalable oversight" (Bowman et al., "Measuring Progress on Scalable Oversight for Large Language Models," 2022, Anthropic — moderate confidence on this one) before falling back to the older statistics/psychometrics lineages I cited above.
