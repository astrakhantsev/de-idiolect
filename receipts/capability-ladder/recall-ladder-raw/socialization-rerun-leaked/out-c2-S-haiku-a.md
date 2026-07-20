Based on my comprehensive web search, **I cannot find prior art that directly describes your "cold-start operating requirement for the audit unit" concept under that name or any established standard name.** Here's what I found:

## Search Results Summary

**Confidence: MODERATE** on the claim that this is novel, with important caveats below.

I searched extensively using multiple angles:
1. Direct terminology ("cold-start operating requirement", "audit unit")
2. Related concepts: "credence calibration", "evidence pooling", "multiplier" + Bayesian estimation
3. Selective prediction/abstention literature (when to use a model vs. abstain)
4. Shrinkage estimation and when estimators beat baselines (Stein-type results)
5. Meta-calibration and uncertainty estimation thresholds
6. Empirical Bayes and default priors

## What I Found (and What It Means)

**Closely related work** exists in these areas:

1. **Selective Prediction / Learning to Defer** (2024-2026): Recent papers like "Knowing When to Defer" (Mitton et al., 2025) and "Calibrated Triage" (Khanmohammadi et al., 2026) address when to *abstain from* or *defer* predictions based on confidence. This shares your core insight—that there's a threshold of estimate quality—but they decide binary (predict/don't predict), not how accurate an estimate must be to *beat a specific fallback*.

2. **Shrinkage Estimation Theory** (classical, e.g., Stein): Dating to Stein (1956), this field characterizes when shrinking estimates toward a default beats the unshrunken version. The bias-variance tradeoff is well-studied, but I didn't find a standard framework that **characterizes the RMSE-of-log error tolerance in cold-start regimes** the way you describe.

3. **Structure-Prior Adaptive Decision Estimation (SPADE)** (Wang, 2026): Decides whether to impose a structure/prior using a specification test and data-adaptive shrinkage. Conceptually similar (when does prior help?) but applied to physical constraints, not credence multipliers.

## The Key Gap

The core novelty in your framework appears to be:
- **Deriving an error schedule by synthetic injection** (you specify: "We derive the schedule by injecting synthetic error of known size")
- **Characterizing cold-start specifically** (before the estimator is fitted against real data, only an assumed default exists)
- **The multiplier-on-log-RMSE metric** as the operating requirement's measurement (RMSE of log of estimated multiplier)

These specifics don't appear under a unified name in the literature I could access. The closest intellectual neighbors are shrinkage theory and selective prediction, but neither names or standardizes the cold-start regime the way you have.

## Confidence Caveats

- **Limitation 1:** ArXiv and accessible Google Scholar cannot be fully exhaustively searched (coverage of domain-specific venues may be incomplete).
- **Limitation 2:** If this concept exists in the econometrics, forecasting, or judgment-and-decision-making literature under a different name, my searches may not have hit it.
- **Limitation 3:** Work published in textbooks or technical reports (not preprints) would be missed.

**Bottom line:** I found no established prior name for this concept and no papers deriving the cold-start operating requirement schedule in the way you describe. You may well have something novel—or if it exists, it's known by a name outside my search reach.
