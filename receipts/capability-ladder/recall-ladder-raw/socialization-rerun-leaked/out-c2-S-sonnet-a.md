## Bottom line

The core phenomenon you're calling the "cold-start operating requirement" — *a per-case estimate must clear an accuracy bar before it beats a fixed default, and the bar is set by how the estimator's error trades off against the achievable gain* — is **not new as a general statistical principle**. It's well-established under at least three different names in three different fields, with canonical treatments well before 2015. What I could **not** find prior art for is your *specific packaging*: an RMSE-of-log-multiplier–indexed schedule (0.3→~85% of gain, 0.6→~50%, ~1.0→breakeven) with an explicit "cold-start vs. warm-start" bar distinction. That exact formalization looks like your own contribution layered on top of an old principle, not a rediscovery of an existing named result.

## Prior art, by field

**1. Shrinkage estimation / empirical Bayes (Statistics) — high confidence this is the closest general-principle match**
This is the direct ancestor of your framework: don't trust a noisy per-case estimate over a fixed pooled value unless the per-case signal-to-noise ratio clears a threshold; below it, shrink fully to the default.
- Stein, C. (1956), *Inadmissibility of the usual estimator for the mean of a multivariate normal distribution*, Proc. 3rd Berkeley Symposium.
- James, W. & Stein, C. (1961), *Estimation with quadratic loss*, Proc. 4th Berkeley Symposium.
- Efron, B. & Morris, C. (1975), *Data Analysis Using Stein's Estimator and its Generalizations*, JASA 70(350):311–319 — the canonical applied treatment (the "baseball paper"), pre-2015 ✓.
Confidence: **high** that this general principle predates your work; **medium** on whether your team already knew of it (you may well have — I'm reporting what's findable, not what's in your heads).

**2. Credibility theory (Actuarial science) — high confidence, and this one explicitly has a "cold-start" case**
Actuarial "credibility" is literally: `estimate = Z·(case experience) + (1−Z)·(class/manual default rate)`, where Z is a multiplier on the case-specific signal, and there is a formal theory of how much data/precision is needed before Z should be pushed toward 1 rather than 0. Crucially, actuaries have a named regime for a brand-new class with **no prior experience to fit the default against** — exactly your cold-start case.
- Mowbray, A.H. (1914), *How Extensive a Payroll Exposure Is Necessary to Give a Dependable Pure Premium?*, Proceedings of the Casualty Actuarial and Statistical Society of America, Vol. 1 — the origin of "full credibility standard," pre-2015 ✓ (and pre-1950).
- Whitney, A.W. (1918), *The Theory of Experience Rating*, Proceedings of the CAS 4:274–292.
- Bühlmann, H. (1967), *Experience Rating and Credibility*, ASTIN Bulletin 4(3):199–207 — puts it on a least-squares/Bayesian footing ("greatest accuracy credibility theory").
Confidence: **high** on the citations and dates (corroborated by multiple independent search hits); **medium** on how tightly this maps to your log-multiplier/RMSE framing specifically, since credibility theory's Z is a linear weight, not quite your multiplicative log-odds scaler.

**3. Correction for attenuation (Psychometrics/classical test theory) — the oldest treatment I found**
Spearman, C. (1904), *The Proof and Measurement of Association Between Two Things*, American Journal of Psychology 15:72–101. This is the oldest quantitative link between "how much error/unreliability is in your measure" and "how much of the true relationship/gain survives" — the direct conceptual ancestor of a gain-retention-vs-error curve.
Confidence: **high** on citation; **medium-low** on whether this is what you'd want to cite, since it's about correlation attenuation, not decision-theoretic breakeven against a fixed default.

**4. Clinical vs. statistical (actuarial) prediction (Psychology/decision science) — closest in framing, weaker in quantification**
Meehl, P.E. (1954), *Clinical Versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence*, University of Minnesota Press. Directly asks "when does an individualized judgment beat a fixed formula?" — your question, rephrased — but gives qualitative/empirical-survey answers, not an RMSE-indexed schedule.
Confidence: **high** citation is real and canonical; **medium** on relevance since it doesn't quantify an error threshold the way you do.

**5. Forecast-aggregation "extremizing" (Forecasting/decision analysis) — closest in actual math structure**
Your `final = start + multiplier × pooled_evidence_lean` is structurally identical to extremizing a pooled forecast's log-odds away from a prior: `log-odds(final) = d × mean(log-odds_i)` or the baseline-relative variant `log-odds(final) = log-odds(baseline) + d[mean(log-odds_i) − log-odds(baseline)]`. The literature explicitly worries about the multiplier `d` being poorly estimated and hurting rather than helping — your exact operating-requirement question, but applied to *this* multiplier.
- Baron, J., Mellers, B., Tetlock, P., Stone, E., & Ungar, L. (2014), *Two Reasons to Make Aggregated Probability Forecasts More Extreme*, Decision Analysis 11(2):133–145 (2014, pre-2015 ✓ by one year).
- Satopää, V.A., Baron, J., Foster, D.P., Mellers, B.A., Tetlock, P.E., & Ungar, L.H. (2014), *Combining Multiple Probability Predictions Using a Simple Logit Model*, International Journal of Forecasting 30(2):344–356.
Confidence: **high** on the structural match to your math; **low-medium** that these specific 2014 papers give your RMSE-schedule — the explicit "how wrong can the estimated factor be before it hurts" discussion I found is from later work (e.g., Neyman & Roughgarden 2021, post-2015), building on the 2014 base.

**6. Estimation error in portfolio optimization (Finance) — same phenomenon, different domain, worth knowing**
Chopra, V.K. & Ziemba, W.T. (1993), *The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice*, Journal of Portfolio Management 19(2):6–11 — quantifies how estimation error erodes the benefit of an "optimized"/individualized choice over a naive fixed default, in log-space-adjacent risk terms. Related: Michaud (1989) on "estimation-error maximization."
Confidence: **high** on citation; **low** on direct relevance to your multiplier-on-a-credence setup — it's the same *shape* of problem, not the same object.

## What I did NOT find

I ran targeted searches for the exact quantitative packaging — "RMSE of log multiplier," "fraction of gain retained," "cold-start operating requirement," combined with shrinkage/credibility/forecasting terms — and found no single source that publishes a schedule like yours (specific numbers: ~85% of gain at RMSE≈0.3, ~50% at ≈0.6, crossover to worse-than-default at ≈1.0), nor a standard name for "cold-start operating requirement" as a term of art. **Confidence: medium** that this absence is real rather than a search-coverage gap — I searched multiple phrasings across statistics, actuarial science, forecasting, and portfolio theory, but I did not do a systematic literature-database search (e.g., Google Scholar citation-chasing from Efron-Morris or Bühlmann forward), which is the appropriate follow-up before you finalize a novelty claim either way.

**My recommendation for your writeup:** frame the *underlying principle* as an instance of shrinkage/credibility theory (cite Efron & Morris 1975 and/or Bühlmann 1967) rather than claim it as newly discovered — but the *specific RMSE-of-log-multiplier schedule with an explicit cold-start bar*, derived via injected synthetic error, does look like it could be your own original quantification of an old principle. That's a defensible and more precise claim than "we discovered this phenomenon."

Sources:
- [James–Stein estimator - Wikipedia](https://en.wikipedia.org/wiki/James%E2%80%93Stein_estimator)
- [Data Analysis Using Stein's Estimator and its Generalizations (Efron & Morris 1975)](https://www.tandfonline.com/doi/abs/10.1080/01621459.1975.10479864)
- [Introduction to Bühlmann credibility](https://mathmodelsblog.wordpress.com/2010/02/02/introduction-to-buhlmann-credibility/)
- [Credibility theory - Wikipedia](https://en.wikipedia.org/wiki/Credibility_theory)
- [Study Note on Bühlmann Credibility (CAS)](https://thecasinstitute.org/wp-content/uploads/2019/01/Exam-3-Study-Note-Credibility01162019.pdf)
- [Disattenuating Correlation Coefficients (Spearman 1904)](https://www.rasch.org/rmt/rmt101g.htm)
- [Clinical Versus Statistical Prediction: The Contribution of Paul E. Meehl](https://www.researchgate.net/publication/7703351_Clinical_Versus_Statistical_Prediction_The_Contribution_of_Paul_E)
- [Principled extremizing of aggregated forecasts — EA Forum](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts) (contains full citations for Baron et al. 2014 and Satopää et al. 2014)
- [The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice (Chopra & Ziemba 1993)](https://jpm.pm-research.com/content/19/2/6)
