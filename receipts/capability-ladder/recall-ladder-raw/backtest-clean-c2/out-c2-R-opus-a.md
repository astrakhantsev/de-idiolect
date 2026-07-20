## Bottom line up front

There is **no single established name for the exact packaged specification you describe** — a schedule mapping an estimator's log-RMSE to the fraction of Brier skill retained, with a "harmful above ~1.0" threshold, derived by synthetic-noise injection and benchmarked against a fitted constant. That precise object reads as a **bespoke construction** (plausibly from applied forecasting / an internal methods write-up), not a named theorem. But every component it is assembled from is a standard, named concept, and the whole is best described as **a break-even accuracy requirement (error-tolerance specification) for a plug-in parameter estimator**. I'll name the parts, since that is what you can actually cite.

## 1. Standard name(s) for the concept and its parts

- **The overall thing — "how good must the estimate be before using it beats a default":** this is a *break-even / minimum-useful-accuracy* condition. Its formal home is **value of information (VOI)**, specifically the value of *imperfect/sample* information, and — because the estimate is substituted directly ("plugged in") without correcting for its own noise — the **plug-in estimation penalty**. In measurement science the same idea is **fitness for purpose / target measurement uncertainty** ("a measurement can be traceable yet not fit for purpose if its uncertainty is too large").
- **The output axis — "fraction of the maximum achievable improvement in prediction accuracy":** a **skill score**, here the **Brier Skill Score** (BSS = 1 − BS/BS_ref), with the fixed fallback as the reference and the oracle setting as the ceiling. The "standard accuracy measure for probability forecasts" is the **Brier score** (a proper scoring rule).
- **Why a noisy per-case estimate becomes *worse* than a constant (the >1.0 harmful regime):** the **bias–variance tradeoff**, and in its sharpest classical form the **inadmissibility / shrinkage (Stein, James–Stein) phenomenon** — a biased constant can dominate a noisy unbiased estimate. Your "estimate separately for each case vs. one fixed value" is exactly **no pooling vs. complete pooling** (with the good answer usually **partial pooling / shrinkage / empirical Bayes**). "Noise manufactures unwarranted confidence" is **overfitting-induced miscalibration / overconfidence**.
- **The concrete instantiation — "a multiplier that scales pooled evidence":** this most likely refers to an **extremizing coefficient** in probability-forecast aggregation (a multiplier on pooled log-odds), estimated per-question vs. a fixed default. *(Medium confidence on this specific mapping — see hedges.)*
- **The method — "inject synthetic errors of a given size, not run a particular estimator":** **Monte-Carlo perturbation / sensitivity (error-injection) analysis** — it characterizes an *error level*, not a method. No canonical single name beyond "sensitivity analysis."

## 2. Fields that own it

Statistical **decision theory / value-of-information analysis**; **forecast verification** (meteorology, and judgmental/probabilistic forecasting); **statistical estimation theory** (shrinkage, empirical Bayes, hierarchical/multilevel modeling); **machine-learning calibration**; and, for the "how-good-is-good-enough" framing, **metrology / analytical chemistry** (fitness for purpose).

## 3. Oldest / most canonical treatments (real citations)

- **Brier, G. W. (1950).** "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review* 78(1): 1–3. — the accuracy measure. *(High confidence.)*
- **Murphy, A. H. (1973).** "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology* 12(4): 595–600. — skill/reliability/resolution decomposition behind "fraction of achievable gain." *(High confidence.)*
- **Stein, C. (1956).** "Inadmissibility of the Usual Estimator for the Mean of a Multivariate Normal Distribution." *Proc. Third Berkeley Symposium* 1: 197–206; and **James, W. & Stein, C. (1961).** "Estimation with Quadratic Loss." *Proc. Fourth Berkeley Symposium* 1: 361–379. — the constant-beats-noisy-estimate result. *(High confidence.)*
- **Raiffa, H. & Schlaifer, R. (1961).** *Applied Statistical Decision Theory.* Harvard. — value of imperfect information / "gather only if it changes the decision." *(High confidence.)*
- **Efron, B. & Morris, C. (1977).** "Stein's Paradox in Statistics." *Scientific American* 236(5): 119–127 (technical version: *JASA* 70 (1975): 311–319). — shrinkage/empirical-Bayes exposition. *(High confidence.)*
- **Gneiting, T. & Raftery, A. E. (2007).** "Strictly Proper Scoring Rules, Prediction, and Estimation." *JASA* 102(477): 359–378. — modern proper-scoring-rule foundation. *(High confidence.)*
- **Gelman, A. & Hill, J. (2007).** *Data Analysis Using Regression and Multilevel/Hierarchical Models.* Cambridge Univ. Press. — no-pooling vs. complete-pooling vs. partial-pooling. *(High confidence.)*
- **Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E. & Ungar, L. H. (2014).** "Two Reasons to Make Aggregated Probability Forecasts More Extreme." *Decision Analysis* 11(2): 133–145. — the extremizing coefficient (the "multiplier that scales pooled evidence"). *(High confidence on the citation; medium confidence it's the intended instantiation.)*
- Metrology framing: **Eurachem/CITAC guide "Setting Target Measurement Uncertainty"** and the *VIM* definition of *target measurement uncertainty*; see also Ramsey & Ellison, *Accred. Qual. Assur.* (2012), "Using target measurement uncertainty to determine fitness for purpose." *(High confidence the concept exists; medium that it's the framing you intend.)*

## 4. Confidence and explicit hedges

- **High confidence:** the description does not correspond to one canonical named concept; it is a composite of Brier skill scoring + value of information + bias–variance/shrinkage + pooling, packaged as a break-even accuracy requirement. All the citations above are ones I stand behind.
- **Medium confidence:** that "a multiplier that scales pooled evidence" = *extremizing coefficient* in forecast aggregation. It fits "pooled evidence" (log-odds pooling) and "multiplier" well, but it could instead be, e.g., a **covariance/variance-inflation factor** (ensemble data assimilation) or a **temperature-scaling / logit-scaling parameter** (ML calibration) — both are also "a multiplier scaling pooled evidence you can estimate per-case or fix." I can't disambiguate from the description alone.
- **Lower confidence / cannot verify:** that any published source presents *this specific schedule* (≈0.3→85%, ≈0.6→50%, >1.0 harmful) as a named result. My searches surfaced the ingredients (BSS baselines, negative skill, shrinkage never-harmful-when-optimally-shrunk, extremizing) but not this exact quantitative table. If it appeared verbatim somewhere, it's likely a specific technical report or internal methods note rather than a standard-textbook concept — if you can tell me where you encountered it, I can try to trace the primary source.

Sources:
- [Brier score — Wikipedia](https://en.wikipedia.org/wiki/Brier_score)
- [Brier Skill Score — EmergentMind](https://www.emergentmind.com/topics/brier-skill-score-bss)
- [Strictly Proper Scoring Rules, Prediction, and Estimation (Gneiting & Raftery) — DTIC PDF](https://apps.dtic.mil/sti/pdfs/ADA454828.pdf)
- [James–Stein estimator — Wikipedia](https://en.wikipedia.org/wiki/James%E2%80%93Stein_estimator)
- [Stein's Paradox and Empirical Bayes — Austin Rochford](https://austinrochford.com/posts/2013-11-30-steins-paradox-and-empirical-bayes.html)
- [Value of Information Analysis: Introduction (ISPOR) — Value in Health](https://www.valueinhealthjournal.com/article/S1098-3015(20)30027-9/fulltext)
- [Using target measurement uncertainty to determine fitness for purpose — Springer](https://link.springer.com/article/10.1007/s00769-012-0899-x)
- [Setting Target Measurement Uncertainty — Eurachem](https://www.eurachem.org/index.php/publications/guides/gd-stmu)
- [Two Reasons to Make Aggregated Probability Forecasts More Extreme (Baron et al. 2014) — Decision Analysis](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293)
- [Combining multiple probability predictions using a simple logit model (Satopää et al.) — ResearchGate](https://www.researchgate.net/publication/260030454_Combining_multiple_probability_predictions_using_a_simple_logit_model)
- [A Primer on Bayesian Methods for Multilevel Modeling (pooling) — PyMC](https://www.pymc.io/projects/examples/en/2022.12.0/case_studies/multilevel_modeling.html)
