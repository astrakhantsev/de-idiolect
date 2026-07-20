## Verdict

Your "cold-start operating requirement" is not new as a *general principle* — it's one of the most independently-rediscovered results in applied statistics: "an estimated per-case adjustment has to clear an accuracy bar before it beats a fixed default, and beyond that bar the estimate's own noise makes it actively worse (overconfidence)." I found it under different names in at least five separate fields, several with canonical treatments well before 2015 (one from 1914). What I could **not** find anywhere, after ~12 searches across the adjacent literatures, is your *exact* quantitative schedule (RMSE-of-log-multiplier ≈0.3 → ~85% of gain retained, ≈0.6 → ~50%, ≈1.0 → break-even/negative). That specific numeric instantiation may be a legitimate, modest original contribution — an extension of an old idea, not a new idea — but I can't rule out it exists in a sub-literature my searches didn't surface. Confidence on "the general shape is prior art": high. Confidence on "the exact schedule is prior art": low/unverified (absence of evidence, not evidence of absence).

## Closest structural match: generalized ("tempered"/"safe") Bayesian inference

This is the closest mechanistic analog to your setup — a scalar **learning-rate multiplier η applied to the likelihood before updating a prior into a posterior**, motivated by exactly your logic: full-strength updating (η=1) is overconfident when the evidence signal is unreliable/misspecified, so you temper it. Grünwald's "SafeBayes" explicitly frames this as choosing η, not just fixing it.

- Grünwald, P. (2012), *The Safe Bayesian — Learning the Learning Rate via the Mixability Gap*, Algorithmic Learning Theory (ALT 2012). Pre-2015, foundational.
- Follow-on: de Heide, Kirichenko, Grünwald et al., *Safe-Bayesian Generalized Linear Regression* (arXiv:1910.09227); Grünwald & van Ommen on generalized Bayes under misspecification.
- Field: Bayesian statistics / statistical learning theory.
- Confidence: medium-high that this is the best mechanistic fit; I did not find an explicit "RMSE of log-η" break-even schedule in this literature, only that η is *chosen* to avoid overconfidence — I didn't exhaustively read the follow-on papers, so I'm not certain none contains your exact schedule.

## Closest terminological + structural match: actuarial credibility theory

"Multiplier" ≈ the **credibility factor Z** that blends a case-specific ("individual") estimate with a class/fixed ("manual"/collective) default. Your "cold-start regime" maps almost exactly onto the **full credibility standard** — the data threshold below which you must partially or fully fall back to the fixed default rather than trust the case estimate. This field even shares your vocabulary root ("credibility" / your "credence") — striking, though I think coincidental rather than a direct lineage.

- Mowbray, A.H. (1914), "How Extensive a Payroll Exposure is Necessary to Give a Dependable Pure Premium," *Proceedings of the Casualty Actuarial Society*, Vol. 1 — the founding paper of credibility/full-credibility-standard theory. Pre-2015 by 111 years.
- Bühlmann, H. (1967), "Experience Rating and Credibility," *ASTIN Bulletin* 4(3):199–207 — the canonical "greatest-accuracy" linear-credibility formulation (Z-weighted blend), later extended by Bühlmann & Straub (1970).
- Field: actuarial science / insurance ratemaking.
- Confidence: high that this is real, canonical prior art for the *mechanism*; medium-low that it's what you actually had in mind (I'm pattern-matching vocabulary, not confirming intent).

## Three more independent hits on the same general phenomenon

- **Forecast combination puzzle** (econometrics/forecasting): estimated-optimal combination weights are repeatedly beaten by fixed/equal weights because weight-estimation variance overwhelms the theoretical gain. Founding: Bates, J.M. & Granger, C.W.J. (1969), "The Combination of Forecasts," *Operational Research Quarterly* 20(4):451–468 (pre-2015). Modern formalization: Smith, J. & Wallis, K.F. (2009), *Oxford Bulletin of Economics and Statistics* 71(3):331–355; Claeskens et al. (2016), *International Journal of Forecasting*.
- **Portfolio optimization vs. naive 1/N** (finance): Michaud, R.O. (1989), "The Markowitz Optimization Enigma," *Financial Analysts Journal* 45(1):31–42, coined "estimation-error maximization" (pre-2015). Quantified crossover: DeMiguel, Garlappi & Uppal (2009), *Review of Financial Studies* 22(5):1915–1953 — showed the data window needed for optimized weights to beat naive equal-weighting can run to thousands of months.
- **Kelly-criterion edge estimation / fractional Kelly** (gambling/quant finance): Kelly, J.L. (1956), "A New Interpretation of Information Rate," *Bell System Technical Journal* 35(4):917–926 (pre-2015, foundational); MacLean, Thorp & Ziemba, eds. (2011), *The Kelly Capital Growth Investment Criterion*, World Scientific — formalizes how edge-estimation error causes overbetting and can flip growth rate negative, motivating fractional Kelly.
- Confidence on all three: high that the phenomenon and citations are real (I read search-result summaries plus, for the extremizing/recalibration papers, fetched and confirmed primary arXiv abstract pages directly).

## The theoretical "why": proper-scoring-rule decomposition

This is the deepest grounding for *why* such a schedule must exist for any accuracy score: a finer/case-specific estimate only helps if the reliability (calibration) cost it introduces doesn't outweigh the resolution gain.

- Murphy, A.H. (1973), "A New Vector Partition of the Probability Score," *Journal of Applied Meteorology* 12(4):595–600 — original reliability/resolution/uncertainty decomposition (pre-2015).
- DeGroot, M.H. & Fienberg, S.E. (1982), "The Comparison and Evaluation of Forecasters," *The Statistician* 32(1–2):12–22.
- Bröcker, J. (2009), "Reliability, Sufficiency, and the Decomposition of Proper Scores," *QJRMS* 135(643):1512–1519 (arXiv:0806.0813, submitted 2008) — generalizes the decomposition to any proper score.
- Confidence: high these are real and directly relevant to the *reason* the schedule shape exists; this is general theory, not a specific "multiplier RMSE" result.

## Weaker/partial match: "cold start" the term itself

The term "cold start" is owned by recommender systems, not by any of the above: Schein, A.I., Popescul, A., Ungar, L.H. & Pennock, D.M. (2002), "Methods and Metrics for Cold-Start Recommendations," SIGIR 2002, pp. 253–260 (pre-2015). It's about missing interaction data for new users/items, not about a multiplier-accuracy threshold — a weaker match than credibility theory's "full credibility standard," which I'd treat as the more load-bearing analog for your specific cold-start framing.

## What this means for your write-up

I'd frame the contribution as: not "we discovered that estimation error can erode/reverse an adaptive correction's advantage over a fixed default" (that's old — five fields, one over a century old) but, if it holds up, "we give a quantified RMSE-of-log-multiplier schedule for this tradeoff in the specific Bayesian-credence-update setting, including its cold-start form" — an extension in the [[feedback_search_field_vocabulary]] sense, not a foreclosed claim. Given how close the actuarial credibility and generalized-Bayes literatures sit to your exact setup, before submitting I'd want someone to specifically check those two subfields for a closed-form or empirical version of your schedule — I did not do exhaustive reading of either.

Sources:
- [The Safe Bayesian — Learning the Learning Rate via the Mixability Gap](https://www.semanticscholar.org/paper/The-Safe-Bayesian-Learning-the-Learning-Rate-via-Gr%C3%BCnwald/8123e6bb00c2683bc0e7fbfe98f62e60e3c09cae)
- [Safe-Bayesian Generalized Linear Regression (arXiv:1910.09227)](https://arxiv.org/abs/1910.09227)
- [Credibility theory — Grokipedia](https://grokipedia.com/page/Credibility_theory)
- [Bühlmann model — Wikipedia](https://en.wikipedia.org/wiki/B%C3%BChlmann_model)
- [An Introduction to Credibility Theory (Longley-Cook, CAS Proceedings)](https://www.casact.org/sites/default/files/database/proceed_proceed62_62194.pdf)
- [Another look at forecast trimming for combinations (cites Bates & Granger 1969)](https://arxiv.org/pdf/2208.00139)
- [R: Bates/Granger (1969) Forecast Combination Approach](https://search.r-project.org/CRAN/refmans/ForecastComb/html/comb_BG.html)
- [The forecast combination puzzle: A simple theoretical explanation](https://www.researchgate.net/publication/304335922_The_forecast_combination_puzzle_A_simple_theoretical_explanation)
- [Optimal Versus Naive Diversification (DeMiguel, Garlappi, Uppal 2009)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1376199)
- [The Markowitz Optimization Enigma (Michaud 1989)](https://www.researchgate.net/publication/247883727_The_Markowitz_Optimization_Enigma_Is_'Optimized'_Optimal)
- [Kelly Criterion Formula Explained: Inputs, Edge, and Fractional Kelly](https://quantmatter.com/kelly-criterion-formula/)
- [Full Kelly Vs. Fractional Kelly: Which Is Right For You?](https://astuteinvestorscalculus.com/full-kelly-vs-fractional-kelly/)
- [Methods and Metrics for Cold-Start Recommendations (Schein et al. 2002)](https://repository.upenn.edu/cis_papers/135/)
- [Reliability, Sufficiency, and the Decomposition of Proper Scores (arXiv:0806.0813)](https://arxiv.org/abs/0806.0813)
- [Modeling Probability Forecasts via Information Diversity (Satopää et al., arXiv:1406.2148)](https://arxiv.org/abs/1406.2148)
- [Parameter uncertainty in forecast recalibration (Siegert et al., arXiv:1509.07102)](https://arxiv.org/abs/1509.07102)
- [Corrected Forecast Combinations (arXiv:2601.09999)](https://arxiv.org/html/2601.09999)
