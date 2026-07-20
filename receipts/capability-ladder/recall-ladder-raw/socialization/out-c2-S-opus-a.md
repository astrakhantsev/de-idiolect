## Bottom line

**Not new.** Your "cold-start operating requirement for the audit unit" is a re-derivation, in your own vocabulary, of a result that three or four adjacent fields already own. Once decoded, your "audit unit" is a **post-hoc probability recalibration** step, your "multiplier that scales the pooled evidence lean" is the **calibration slope** (biostatistics) / **global (uniform) shrinkage factor** (Copas–van Houwelingen) / **inverse temperature** (ML) / **extremization coefficient** (forecast aggregation), and your "operating requirement" is the long-known **bias–variance / shrinkage crossover**: an *estimated* scaling coefficient beats a *fixed* default only when its estimation variance is small enough; past a threshold its own noise makes calibration worse (your "manufactures overconfidence"). The general form of this is close to theorem-territory (Stein), so I'd treat the *concept* as **foreclosed, not merely predated** — you cannot present it as a novel contribution. Confidence: **~0.9** that the core idea is established prior art.

Where genuine residual novelty might survive is narrow and I'll flag it at the end.

## The term-for-term decode (this is what makes the prior art visible)

| Your vocabulary | Standard name(s) | Field that owns it |
|---|---|---|
| audit unit forming a final credence from a starting credence | post-hoc **recalibration** / **logistic recalibration model**: `logit(final) = a + b·logit(prior)` | biostatistics, ML calibration |
| **multiplier** scaling the pooled evidence lean | **calibration slope `b`** = **global/uniform shrinkage factor `S`** = **inverse temperature `1/T`** = **extremization coefficient** = scale of the log-LR | clinical prediction, ML, forecast aggregation, forensic LR |
| fixed **default** multiplier | no shrinkage (`S=1`) or a preset/heuristic shrinkage factor | all of the above |
| **operating requirement** (accuracy the estimate needs to beat the default) | the **shrinkage-estimation-error / bias–variance crossover**; "does the plug-in estimate dominate the fixed constant?" | shrinkage estimation (Stein), clinical prediction |
| noise **manufactures overconfidence** past error ~1.0 | high between-sample variance of the estimated slope degrades the reliability term | forecast verification / calibration |
| gain in the **accuracy score** | the **reliability component** of a proper score (Brier/log) | forecast verification |
| **cold-start** (no fitted default, only an assumed one) | recalibration/shrinkage **before any validation data exists**, using a **closed-form heuristic** shrinkage factor | clinical prediction modeling |

I verified the structural identity against a primary source: the recalibration equation `logit(final) = α* + S·logit(p̂)` and the statement that `S_opt` is *the value minimizing prediction MSE* / giving calibration-slope 1, and that when no validation data exist you fall back to a **closed-form heuristic** (your cold-start assumed default) — appear verbatim in the shrinkage literature.

## Standard names, fields, and canonical citations (real; several pre-2015)

**Origin of the "multiplier" as calibration slope (pre-2015, canonical):**
- **Cox, D.R. (1958). "Two further applications of a model for binary regression." *Biometrika* 45(3–4):562–565.** This is the origin of the calibration-slope / logistic-recalibration model — your audit unit's exact form. Confidence **high** (verified title/venue/pages).

**Origin of "estimated scaling can be worse than a fixed default" (pre-2015, canonical — this is your operating requirement):**
- **Stein, C. (1956)** and **James & Stein (1961)** — shrinkage dominance: a shrunk/scaled estimator beats the plug-in only under variance conditions. This is the deep theorem your requirement is a special case of. Confidence **high**.
- **Copas, J.B. (1983). "Regression, Prediction and Shrinkage (with discussion)." *JRSS-B* 45(3):311–354.** Stein-type predictors give lower prediction MSE than least squares *when* anticipated correctly; the fit to new data is "nearly always worse." Confidence **high** (verified).
- **van Houwelingen, J.C. & le Cessie, S. (1990). "Predictive value of statistical models." *Statistics in Medicine* 9(11):1303–1325.** The **heuristic closed-form shrinkage factor** — literally the "assumed default multiplier used before you have resolved cases," i.e., your **cold-start** fallback. Confidence **high** (verified).

**"Gain in the accuracy score" = reliability component (pre-2015, canonical):**
- **Murphy, A.H. (1973). "A new vector partition of the probability score." *J. Applied Meteorology* 12:595–600.** Brier = reliability + resolution + uncertainty; recalibration's benefit *is* the reliability term. Confidence **high** on the result; **medium** on exact pages.
- **DeGroot, M.H. & Fienberg, S.E. (1983). "The comparison and evaluation of forecasters." *The Statistician* 32:12–22.** Calibration/refinement decomposition of proper scores. Confidence **high** on existence; **medium** on exact pages. (Note: **Bröcker 2009** generalized this — the same Bröcker line your notes elsewhere flag as a foreclosure risk; worth a glance to be safe.)

**ML calibration version (Platt/temperature — pre-2015 origin, post-2015 for the overconfidence result):**
- **Platt, J. (1999). "Probabilistic outputs for support vector machines."** — Platt scaling; your two-parameter version. Confidence **high**.
- **Guo et al. (2017). "On calibration of modern neural networks." *ICML*.** — temperature scaling; the canonical "networks are overconfident, a single scalar fixes it, and over-flexible recalibration on small data hurts" result. Confidence **high**.

**Forecast-aggregation version (this one is nearly your exact object — a coefficient multiplying pooled log-odds):**
- **Satopää, V. et al. (2014). "Combining multiple probability predictions using a simple logit model." *Int. J. Forecasting* 30(2):344–356.** — the **extremization coefficient** on pooled log-odds; and the well-documented "when does extremizing help vs. hurt" question is *precisely* your operating requirement in this field. (2014 — pre-2015.) Confidence **high** on existence; **medium** on exact page range.
- **Ranjan, R. & Gneiting, T. (2010). *JRSS-B*** — combining/recalibrating forecasts. Confidence **medium-high**.

**Empirical statements closest to your exact "estimate can be worse than default" schedule (post-2015):**
- **van Calster, B. et al. (2020). "Regression shrinkage methods for clinical prediction models do not guarantee improved performance." *Stat. Methods in Medical Research.*** — the title *is* your finding.
- **Riley, R.D. et al. (2021). "Penalization and shrinkage methods produced unreliable clinical prediction models especially when sample size was small." *J. Clin. Epidemiology.*** — noisy estimated shrinkage → miscalibration out of sample; the effect is worst exactly at your cold-start (small-n) regime.

## Predated vs. foreclosed — and where any novelty actually survives

- The **concept** — "an estimated calibration multiplier beats a fixed default only above an accuracy threshold; below it, noise manufactures overconfidence" — is **foreclosed** as a novel claim. Multiple fields state it; the general version follows from Stein. Do **not** frame this as original. Confidence **~0.9**.
- What I did **not** find published, after searching all five neighbouring literatures, is your *specific quantitative schedule* keyed to **RMSE of the log of the multiplier** (0.3 → ~85% of achievable score gain; 0.6 → ~half; ~1.0 → crossover), together with the **cold-start distinction that an *assumed* default changes the bar versus a *fitted* one.** That specific parameterization plausibly is yours. But two honest caveats: (a) absence of a search hit is **not** proof of novelty — the temperature-scaling and extremization literatures are large and I could easily have missed an equivalent "operating characteristic" curve; confidence it's genuinely unpublished is only **~0.4**. (b) Even if unpublished, it is an **extension / re-parameterization of a known tradeoff**, not a new phenomenon — so it should be written up as *"a quantitative operating characteristic for the known shrinkage crossover, specialized to the cold-start case,"* explicitly citing Cox 1958, Copas 1983, van Houwelingen & le Cessie 1990, and van Calster/Riley — never as the discovery of the requirement itself.

My recommendation: reframe the writeup from "one of our more original contributions" to "we give a cold-start operating characteristic for the classical calibration-slope / shrinkage-factor estimation problem." Lead with the prior art, position your schedule as the delta, and the claim becomes defensible instead of refutable.

If useful I can (a) pull the van Calster 2020 and Riley 2021 full texts to check whether either already states a log-RMSE-style schedule (the one thing that would collapse even your residual novelty), and (b) write this decode + citation map to a file in the minelit folder and run a doc-review over it.

Sources:
- [Cox 1958, Biometrika (record)](https://scholar.google.com/scholar_lookup?title=Two+further+applications+of+a+model+for+binary+regression&author=D.R.+Cox&publication_year=1958&journal=Biometrika&pages=562-565&doi=10.1093/biomet/45.3-4.562)
- [Copas 1983, "Regression, Prediction and Shrinkage," JRSS-B](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.2517-6161.1983.tb01258.x)
- [van Houwelingen & le Cessie 1990, "Predictive value of statistical models," Stat Med](https://onlinelibrary.wiley.com/doi/abs/10.1002/sim.4780091109)
- [Agreement between heuristic and optimal shrinkage factors — simulation study (Springer, verified primary source)](https://link.springer.com/article/10.1186/s41512-026-00222-1)
- [van Calster et al. — shrinkage methods do not guarantee improved performance (ResearchGate)](https://www.researchgate.net/publication/341362372_Regression_shrinkage_methods_for_clinical_prediction_models_do_not_guarantee_improved_performance_Simulation_study)
- [Riley et al. 2021 — penalization/shrinkage unreliable when sample size small (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8026952/)
- [Steyerberg — application of shrinkage techniques in logistic regression (mirror listing)](http://www.yaroslavvb.com/papers/steyerberg-application.pdf)
- [Guo et al. temperature scaling / Platt scaling overview (Wikipedia: Platt scaling)](https://en.wikipedia.org/wiki/Platt_scaling)
- [Satopää et al. 2014, "Combining multiple probability predictions using a simple logit model"](https://www.researchgate.net/publication/260030454_Combining_multiple_probability_predictions_using_a_simple_logit_model)
- [Bayesian ensembles: when to extremize or anti-extremize (arXiv)](https://arxiv.org/pdf/1705.02391)
- [Murphy 1973 Brier decomposition & DeGroot–Fienberg 1983 (generalization paper, Exeter ORE)](https://ore.exeter.ac.uk/articles/journal_contribution/Simplifying_and_generalising_Murphy_s_Brier_score_decomposition/29748851/1/files/56771708.pdf)
- [Forensic LR calibration tutorial (logistic-regression calibration & fusion, arXiv 2104.08846)](https://arxiv.org/pdf/2104.08846)
