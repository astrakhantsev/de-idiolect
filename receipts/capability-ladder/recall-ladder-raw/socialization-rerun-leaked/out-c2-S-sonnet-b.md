## Bottom line

The general phenomenon you're describing is **not new** — it has been independently discovered and formalized in at least three separate fields, with the oldest treatment dating to 1914. But the specific packaging you're using — "RMSE of the log of the estimated multiplier" as the yardstick, with a numeric schedule (≈0.3 → 85% of gain, ≈0.6 → 50%, ≈1.0 → break-even/net-negative) plus the explicit "cold-start" framing (no fitted default yet, only an assumed one) — I could not find published anywhere under that or any other name. So: **the underlying idea is old, the specific quantitative operationalization appears to be yours.**

## Standard names, by field, oldest → canonical

**1. Actuarial credibility theory — the closest structural match.**
Your setup (`final credence = default + multiplier × pooled-evidence-lean`) is algebraically identical to the actuarial credibility formula `C = zX + (1−z)M` (equivalently `M + z(X−M)`), where `z` is the "credibility factor," `X` is the individual/pooled experience estimate, and `M` is the manual/prior rate — your fixed default. Their "cold-start regime" is literally the pre-full-credibility regime, where you fall back to the manual rate rather than a fitted class rate.
- Oldest: Mowbray, A.H. (1914), "How Extensive a Payroll Exposure Is Necessary to Give a Dependable Pure Premium?", *Proceedings of the Casualty Actuarial Society*, Vol. 1 — the founding paper on "the standard for full credibility." Whitney, A.W. (1918), "The Theory of Experience Rating," *PCAS* 4, 274–292, is also original and explicitly Bayesian.
- Canonical modern formalization: Bühlmann, H. (1967), "Experience Rating and Credibility," *ASTIN Bulletin* 4(3) — derives the credibility factor `z` from the ratio of within-class to between-class variance.
- Confidence: **High** that this is genuine, on-point prior art for the structure of the problem (I verified the formula and framing directly via Wikipedia's credibility-theory article, which cites Bühlmann & Gisler's textbook). **Medium** on whether it uses your exact parameterization — credibility theory usually indexes the "how much data is enough" question by exposure/variance ratios, not by RMSE of a log-multiplier, though the two are related transformations of the same idea. I was not able to fetch the primary Mowbray/Bühlmann texts directly (PDF fetch failed); the citations above come from secondary sources (Wikipedia, actuarial course notes), not primary-text verification.

**2. Empirical Bayes / James–Stein shrinkage.**
Your "multiplier tuned per case vs. left at fixed default" is the shrinkage-vs-raw-estimate tradeoff, and the general result that a *noisily estimated* shrinkage/prior parameter can underperform a fixed one is a known concern in this literature.
- Canonical pre-2015: Efron, B. & Morris, C. (1975), "Data Analysis Using Stein's Estimator and Its Generalizations," *JASA* 70(350) (building on James & Stein 1961).
- Confidence: **High** that this field treats the identical general tradeoff; **Low-Medium** that it uses your specific RMSE-of-log-multiplier schedule — shrinkage-estimation-error is usually indexed by sample size/degrees of freedom, not that specific metric.

**3. Forecast combination / "extremizing."**
If your "multiplier" is applied to *pooled* (averaged) evidence in log-odds space, this is structurally what the forecasting literature calls extremizing.
- Oldest classic: Bates, J.M. & Granger, C.W.J. (1969), "The Combination of Forecasts," *Operational Research Quarterly* 20(4) — shows poorly estimated combination weights can underperform a naive fixed default (e.g., equal weighting).
- Closer terminological match: Satopää, V.A., Baron, J., Foster, D.P., Mellers, B.A., Tetlock, P.E., Ungar, L.H. (2014), "Combining Multiple Probability Forecasts... Extremizing," *International Journal of Forecasting* — a multiplicative factor applied to pooled forecast log-odds, with known overfitting/estimation-error concerns.
- Confidence: **Medium-High** for Bates & Granger as the oldest canonical case of "estimated weight has to be good enough or the default wins"; **Medium** that extremizing is a close terminological cousin. I could not fetch the Bates & Granger PDF directly (render failure) — relying on secondary summaries.

**Weaker/partial analogs**, worth naming but not as close: control variates with an estimated coefficient in Monte Carlo simulation (known bias/variance break-even threshold beyond which the "correction" hurts); meta-analysis heterogeneity (τ) estimation with few studies, where a fixed-effect fallback is standard practice below ~5 studies (DerSimonian & Laird 1986 is the canonical pre-2015 reference, though the "few-studies problem" critique is mostly post-2015 literature); and probabilistic-forecast recalibration vs. climatology in meteorology (Murphy 1973 for the foundational reliability/resolution decomposition, pre-2015; the explicit "recalibration can be worse than climatology under parameter uncertainty" result I found is a 2015 arXiv paper, right at your cutoff and not clearly pre-2015).

## What I'm unsure of / explicit hedges
- My web search is not exhaustive and several primary sources (ASTIN Bulletin archives, JASA archives, the Bates & Granger PDF) did not load for direct verification — the citations above rest partly on secondary summaries, not my own reading of the primary text.
- I found no source using your exact metric (RMSE of log-multiplier) or your exact schedule (0.3/0.6/1.0 breakpoints). Absence of evidence from search is suggestive, not conclusive — a closer match could exist in a paywalled venue, an internal industry write-up (e.g., fraud/trust-and-safety calibration practice), or under vocabulary I haven't tried.
- I'm treating "audit unit," "case," "credence" as your own abstracted terms for whatever real system this is; if the underlying domain is more specific (e.g., ML classifier calibration under label scarcity, or forensic likelihood-ratio calibration), there may be a nearer match I didn't surface — I checked forensic-science Cllr calibration literature and found no explicit "cold start" treatment there, but that check was shallow.

**Recommendation for the write-up:** frame it as "we independently derived, via synthetic-error injection, a quantitative operating-requirement schedule for the classical credibility-theory / shrinkage-estimation cold-start problem" rather than claiming the problem itself is new — cite Mowbray (1914) and Bühlmann (1967) as the closest prior art and position your contribution as the specific RMSE-based schedule and its cold-start-specific derivation method.

Sources:
- [Credibility theory - Wikipedia](https://en.wikipedia.org/wiki/Credibility_theory)
- [A general optimal approach to Bühlmann credibility theory - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167668722000245)
- [Actuarial Credibility: Beyond the Numbers | Medium](https://medium.com/@alexfiliakov/actuarial-credibility-beyond-the-numbers-c1bd465d7339)
- [194 REPORT AN INTRODUCTION TO CREDIBILITY THEORY BY L. H. LONGLEY-COOK (CAS Proceedings, discusses Mowbray 1914)](https://www.casact.org/sites/default/files/database/proceed_proceed62_62194.pdf)
- [(PDF) Data Analysis Using Stein's Estimator and Its Generalizations](https://www.researchgate.net/publication/239061805_Data_Analysis_Using_Stein's_Estimator_and_Its_Generalizations)
- [Combining Probability Forecasts and Understanding Probability Extremizing through Information Diversity](https://www.researchgate.net/publication/262974382_Combining_Probability_Forecasts_and_Understanding_Probability_Extremizing_through_Information_Diversity)
- [Principled extremizing of aggregated forecasts — EA Forum](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts)
- [Forecast combinations: an over 50-year review (arXiv)](https://arxiv.org/pdf/2205.04216)
- [Control variates - Wikipedia](https://en.wikipedia.org/wiki/Control_variates)
- [Methods for evidence synthesis in the case of very few studies - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6175308/)
- [Parameter uncertainty in forecast recalibration (arXiv)](https://arxiv.org/pdf/1509.07102)
