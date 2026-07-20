I have enough to answer with confidence. Here's my identification.

## Bottom line

The description has **two layers**, and they identify very differently:

- **The update mechanism + the "multiplier"** is a well-established, multiply-named concept. It's a **log-odds (logit) Bayesian update with an extremization / calibration coefficient** — a scalar applied to pooled evidence (the sum of log-likelihood-ratios, i.e. the pooled deviation from the prior). This is standard and old.
- **The "operating requirement" itself** — the tolerance *schedule* mapping the estimator's error (RMSE of the log-multiplier) to the fraction of achievable score-gain retained, with a break-even point past which the estimate is net-harmful — does **not** correspond to a canonically named concept that I can find. It is a **bias–variance / plug-in-estimation-error analysis of a calibration parameter**, and the specific packaging reads as bespoke (most likely lifted from a particular technical report and anonymized). I'll flag that honestly rather than invent a name.

---

## 1. Standard name(s)

**The multiplier (the scalar on the pooled evidence lean).** Same object, different field names:

- **Extremizing / extremization coefficient (or factor / parameter)** — forecast-aggregation literature. Value >1 pushes the pooled forecast toward 0/1 ("extremize"); <1 shrinks toward the prior ("de-extremize"/anti-extremize). This is the closest match to your description of "a multiplier that scales the pooled evidence lean, tunable per question or left at a default."
- **Inverse temperature (temperature scaling); Platt slope** — machine-learning calibration. A single scalar on the logits before the softmax/sigmoid is *exactly* your multiplier; T=1 (β=1) is "trust the evidence as-is."
- **Calibration slope** — clinical-prediction / biostatistics. A fitted slope <1 on the linear predictor signals overfit, overconfident predictions needing shrinkage; this is the same quantity viewed as a diagnostic.
- **Recalibration / sharpening parameter** in logarithmic (log-linear) opinion pooling.
- **Conservatism coefficient** (older psychology framing) — a sub-1 exponent on the likelihood ratio, i.e. under-updating relative to Bayes.

**The update rule.** "Posterior log-odds = prior log-odds + a·(pooled log-likelihood-ratio)" is **log-odds / logit-form Bayesian updating** (a.k.a. **weight-of-evidence** updating in the Good–Turing/Jaynes tradition), with **extremization about the prior** as the recalibration step.

**The "operating requirement."** No established proper name. What it *is*, in standard terms: a **bias–variance tradeoff for a plug-in calibration parameter** — quantifying when a noisy per-item estimate of the coefficient is dominated by (worse than) a fixed constant default. The break-even insight ("past RMSE≈1.0 the estimate's noise manufactures overconfidence, making it worse than the default") is the well-known phenomenon that **mis-estimated extremization/over-shrinkage degrades a proper score**; the framing as an accuracy *budget* keyed to synthetic-noise injection is bespoke.

## 2. Field(s) that own it

- **Forecast aggregation / judgment & decision making** (extremizing; the primary owner of your exact framing).
- **Statistics — opinion pooling & probability-forecast recalibration** (logarithmic/beta-transformed pools).
- **Machine-learning calibration** (temperature/Platt scaling; owns the "scalar-on-logits" view and the "when does a fitted temperature beat T=1" question).
- **Clinical-prediction modeling / biostatistics** (calibration slope, shrinkage).
- **Cognitive psychology of belief revision** (conservatism — the historical root of "a multiplier on the evidence").

## 3. Oldest / most canonical treatments (verified via search)

Pre-2015 anchors:

- **Edwards, W. (1968).** "Conservatism in Human Information Processing." In B. Kleinmuntz (ed.), *Formal Representation of Human Judgment*, Wiley. — The origin of "people update as if applying a multiplier <1 to the evidence." *(Chapter/venue detail partly from memory; the 1968 attribution and content are confirmed.)*
- **Genest, C. & Zidek, J. V. (1986).** "Combining Probability Distributions: A Critique and an Annotated Bibliography." *Statistical Science* 1(1), 114–135. — The canonical review; establishes logarithmic opinion pooling and its properties.
- **Ranjan, R. & Gneiting, T. (2010).** "Combining Probability Forecasts." *JRSS Series B* 72(1), 71–91. — Proves that averaging calibrated forecasts *decalibrates* them, so pooled forecasts require a recalibration transform (the beta-transformed linear pool) — the formal justification for the multiplier.
- **Satopää, V., Baron, J., Foster, D., Mellers, B., Tetlock, P., Ungar, L. (2014).** "Combining Multiple Probability Predictions Using a Simple Logit Model." *International Journal of Forecasting* 30(2), 344–356. — The aggregator with **a single interpretable extremizing parameter**; the paper most directly matching "a tunable multiplier on pooled log-odds."
- **Baron, J., Mellers, B., Tetlock, P., Stone, E., Ungar, L. (2014).** "Two Reasons to Make Aggregated Probability Forecasts More Extreme." *Decision Analysis* 11(2), 133–145. doi:10.1287/deca.2014.0293. — The canonical "why extremize" paper.

Adjacent/foundational for the synonyms:
- **Platt, J. (1999)** "Probabilistic outputs for support vector machines" (Platt scaling) and **Guo, C. et al. (2017)** "On Calibration of Modern Neural Networks" (temperature scaling) — the ML-calibration lineage; the "when does a fitted temperature beat T=1" question is the closest existing analogue to your operating requirement. **Cox, D. R. (1958)** "Two further applications of a model for binary regression," *Biometrika* — root of the calibration slope *(cited from memory; not re-verified this session — treat as uncertain)*.

The "extremize vs. anti-extremize, and when" question is treated directly in **Satopää et al. (2016), "Bayesian Ensembles of Binary-Event Forecasts: When Is It Appropriate to Extremize or Anti-Extremize?"** (arXiv:1705.02391) — the nearest thing to a formal treatment of *when the coefficient should deviate from a default*, though still not your synthetic-error-schedule framing.

## 4. Confidence, with explicit hedges

- **High (≈0.9):** The core object is a log-odds update with an extremization/calibration coefficient, and "extremizing coefficient / temperature / calibration slope / conservatism coefficient" are the cross-field names. The five verified citations above are real and correctly attributed (venues/years confirmed by search).
- **High (≈0.85):** The field owners are forecast aggregation, opinion-pooling statistics, and ML calibration.
- **Moderate–High (≈0.8):** The specific **"operating requirement"** — the RMSE-of-log-multiplier tolerance schedule with an ~1.0 break-even where noise makes the estimate worse than the default — has **no established proper name**; it's a bias–variance/plug-in analysis. I searched several phrasings and found the *principle* everywhere but the *packaged schedule* nowhere.
- **Speculative (≈0.4), flagged:** The terms "audit unit," "credence," and "cold-start" suggest this was **anonymized from a specific recent AI-forecasting technical report** (the "AIA Forecaster" technical report, arXiv:2511.07678, surfaced repeatedly and matches the vocabulary). I did not open it to confirm; treat the source attribution as a lead, not a finding. If you want, I can fetch it and check whether the exact schedule (0.3→85%, 0.6→50%, 1.0→break-even) appears there.
- **Uncertain:** The Edwards (1968) chapter pagination and the Cox (1958) calibration-slope citation are from memory, not re-verified this session.

The one thing I'd push back on if you expected a single tidy term: **there isn't one for the whole construct.** The mechanism is textbook; the "operating requirement" is a custom engineering criterion built on top of it.

Sources:
- [Satopää et al. 2014 — Combining multiple probability predictions using a simple logit model (IJF)](https://ideas.repec.org/a/eee/intfor/v30y2014i2p344-356.html)
- [Baron et al. 2014 — Two Reasons to Make Aggregated Probability Forecasts More Extreme (Decision Analysis)](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293)
- [Ranjan & Gneiting 2010 — Combining Probability Forecasts (JRSS-B)](https://academic.oup.com/jrsssb/article/72/1/71/7076442)
- [Genest & Zidek 1986 — Combining Probability Distributions: A Critique and an Annotated Bibliography (Statistical Science)](https://projecteuclid.org/journals/statistical-science/volume-1/issue-1/Combining-Probability-Distributions-A-Critique-and-an-Annotated-Bibliography/10.1214/ss/1177013825.full)
- [Edwards 1968 — Conservatism in human information processing (Semantic Scholar)](https://www.semanticscholar.org/paper/Judgment-under-uncertainty:-Conservatism-in-human-Edwards/ec0678d405fdbc1c30e30274c9b84229c787cfd2)
- [Conservatism (belief revision) — Wikipedia overview](https://en.wikipedia.org/wiki/Conservatism_(belief_revision))
- [Satopää et al. 2016 — When Is It Appropriate to Extremize or Anti-Extremize? (arXiv:1705.02391)](https://arxiv.org/pdf/1705.02391)
- [Guo et al. 2017 lineage — temperature scaling / Platt scaling (AWS Prescriptive Guidance summary)](https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-quantifying-uncertainty/temp-scaling.html)
- [Principled extremizing of aggregated forecasts (EA Forum, practitioner overview)](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts)
- [AIA Forecaster Technical Report — possible anonymized source (arXiv:2511.07678)](https://arxiv.org/pdf/2511.07678)
