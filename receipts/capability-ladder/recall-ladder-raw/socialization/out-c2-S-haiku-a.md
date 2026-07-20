Based on my systematic web search, here's what I found:

## Summary

**Your "cold-start operating requirement for the audit unit" does not appear to be an established concept in the literature under that name.** However, the underlying ideas connect to several related established frameworks. I found **no prior art that combines all the specific elements** of your framework (starting credence + estimated multiplier + RMSE of log multiplier + synthetic error injection to derive operating thresholds + cold-start regime).

## Related Prior Art (Ranked by Relevance)

### Most Relevant

**1. Propensity Score Positivity/Overlap Literature** 
- **What it addresses:** When inverse probability weighting becomes unreliable due to estimation error or model misspecification, making the weighted estimator *worse* than no adjustment.
- **Key papers:** 
  - Li & Thomas, "Addressing Extreme Propensity Scores via the Overlap Weights" (*American Journal of Epidemiology*, 2019) — develops quantitative criteria (overlap bounds) for when weighting helps vs. harms
  - Zhang et al., "Propensity score weighting under limited overlap and model misspecification" (arXiv:2006.04038, 2020)
- **Conceptual overlap:** Like your framework, this defines when an estimation procedure beats doing nothing, with explicit error thresholds.
- **Confidence:** 80% this is the closest conceptual predecessor

**2. "To Adjust or Not to Adjust? Sensitivity Analysis of M-Bias and Butterfly-Bias"**
- **Authors:** Vansteelandt & Bekaert
- **Published:** *Journal of Causal Inference*, 2014
- **What it does:** Provides formal sensitivity analysis showing when covariate adjustment *increases* bias more than it reduces it
- **Conceptual overlap:** Directly addresses the question "when does correction make things worse?"
- **Key limitation:** Focuses on causal structure (M-bias, colliders), not estimation error thresholds
- **Confidence:** 75% relevance

**3. Information Threshold Concept**
- **Author:** Balayla, J.
- **Title:** "Information Threshold, Bayesian Inference and Decision-Making"
- **Published:** arXiv:2206.02266 (2022)
- **What it does:** Defines a threshold beyond which additional information doesn't meaningfully improve posterior inference; prior and posterior become nearly identical
- **Conceptual overlap:** Addresses when more data/adjustment stops helping; threshold concept is similar to your operating requirement
- **Key limitation:** Focused on prior-data balance, not multiplier error
- **Confidence:** 65% relevance

### Moderately Relevant

**4. Bayesian Model Misspecification Literature**
- **Key papers:** Multiple studies show when adjustment based on incorrectly specified models increases bias (e.g., "Model misspecification and bias for inverse probability weighting estimators," Waernbaum 2023)
- **What it addresses:** When a misspecified adjustment model harms more than helps
- **Gap:** Doesn't provide quantitative operating requirement schedules

**5. Empirical Bayes & Shrinkage Estimation**
- **Concept:** James-Stein and empirical Bayes methods show when shrinking toward a default mean beats using raw estimates
- **Recent finding:** Chen (2024, Yale Economics) shows empirical Bayes can underperform when the independence assumption (parameters independent from standard errors) is violated
- **Gap:** Addresses when defaults beat estimates, but inverse direction from your framework

**6. Cochrane Meta-Analysis Methodology**
- **Standard:** Cochrane Handbook guidance on when *not* to pool studies
- **Concept:** Heterogeneity (I² statistic) used to decide whether pooling helps, but thresholds are deliberately soft (not binding)
- **Gap:** No specific operating requirement framework

**7. Indiscriminate Adjustment Literature**
- **Key paper:** Sinha & Raamana, "Indiscriminate adjustment for confounders is worse than you think" (2025)
- **Finding:** Adding covariates can increase prediction error; confounding bias for each adjustment set should be quantified
- **Gap:** No quantitative operating requirement schedule

**8. Reliability Coefficient Thresholds**
- **Established standard:** ICC > 0.70 for adequate reliability (psychometric literature)
- **Gap:** Fixed thresholds, not a derived operating requirement schedule

**9. Operating Characteristic Functions**
- **What it is:** Established statistical concept describing how a test's properties (power, Type I error) vary with true parameter value
- **Conceptual connection:** "Operating requirement" echoes this terminology, but your framework is inverse: characterizing when an estimator *fails*
- **Confidence:** 40% direct relevance

## What I Could Not Find

- **No literature explicitly on "cold-start" + "operating requirement" + "multiplier"** in the evidence synthesis / credence formation context
- **No quantitative framework matching your schedule** (RMSE of log multiplier → 0.3 keeps 85%, 0.6 keeps 50%, 1.0 worse than default)
- **No prior work using synthetic error injection** to characterize when an estimated multiplier becomes harmful

## My Assessment

**Novelty verdict:** Your framework appears **novel in its specific integrated form**, though it synthesizes ideas from multiple established literatures (propensity scores, Bayesian misspecification, shrinkage estimation, sensitivity analysis).

**Caveats & Hedge:**
1. **Confidence: 70–75%** that this is truly novel. It's possible someone has done similar work under different terminology (e.g., in causal inference or meta-analysis) that my searches didn't catch, especially in pre-2015 or non-English literature.
2. **Search limitations:** I focused on English-language academic literature via arXiv, Google Scholar, and PubMed. Specialized methodological communities (audit, accounting, intelligence analysis) might have parallel frameworks I didn't access.
3. **Terminology matters:** If prior work uses phrases like "adjustment reliability threshold," "prior-posterior reliability gap," or "multiplier validity schedule," I may have missed it.

## Recommendation Before Publishing

**Before claiming novelty:**
1. Search the **causal inference** literature (Pearl, Robins, VanderWeele) for similar frameworks under different names
2. Check **meta-analysis methodology** papers (Higgins, Thompson) for operating requirements around effect size multipliers
3. Look at **epidemiology** literature on when covariate adjustment succeeds/fails (last search before ~2010)
4. If your work cites propensity score or empirical Bayes literature, confirm those haven't already derived your schedule

**Most conservative framing:** Position it as an extension of propensity score positivity work (Li & Thomas) to the "audit unit" / credence-formation setting, rather than claiming it's entirely new.

---

**Sources Consulted:**
- [To Adjust or Not to Adjust? Sensitivity Analysis of M-Bias and Butterfly-Bias](https://www.degruyterbrill.com/document/doi/10.1515/jci-2013-0021/html?lang=en)
- [Propensity score weighting under limited overlap and model misspecification](https://arxiv.org/abs/2006.04038)
- [Information Threshold, Bayesian Inference and Decision-Making](https://arxiv.org/abs/2206.02266)
- [Model misspecification and bias for inverse probability weighting estimators](https://onlinelibrary.wiley.com/doi/full/10.1002/bimj.202100118)
- [Indiscriminate adjustment for confounders is worse than you think](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11715647/)
- [Addressing Extreme Propensity Scores via the Overlap Weights](https://academic.oup.com/aje/article/188/1/250/5090958)
- [Cochrane Handbook Chapter 10: Analysing data and undertaking meta-analyses](https://training.cochrane.org/handbook/current/chapter-10)
- [James-Stein Shrinkage Estimator: When to Use and When Not To](https://stat210a.berkeley.edu/fall-2024/reader/jamesstein.html)
