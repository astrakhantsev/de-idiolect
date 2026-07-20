Based on my active web search, I found **well-established related literature**, but your specific concept of a "cold-start operating requirement for the audit unit" does **not appear as a standard named framework** in published work. However, it is a formalization of several interconnected and classic findings. Here's what I found:

## Closest Prior Art: The Forecast Combination Puzzle

Your concept is most directly related to the **forecast combination puzzle**, a well-studied phenomenon in forecasting literature:

**Most relevant:** Claeskels, Magnus, Vasnev, & Wang (2016). "The forecast combination puzzle: A simple theoretical explanation." *International Journal of Forecasting*, 32(3), 754–762. [[PDF](https://research.vu.nl/en/publications/the-forecast-combination-puzzle-a-simple-theoretical-explanation-2)]

This paper explains why simple equal-weight forecast combinations often outperform estimated optimal weights. **The key insight:** when weights must be estimated from data, the estimation error itself can be so large that it outweighs the theoretical optimality of the estimated weights. The combined forecast becomes biased and has higher variance than under fixed weights—sometimes performing worse than the original individual forecasts.

**Foundational work:**
- Bates & Granger (1969). "The combination of forecasts." *Operational Research Quarterly*, 20(4), 451–468. — Introduced the principle of optimal weighted combinations by minimizing forecast error variance.
- Newbold & Granger (1974). Extended Bates & Granger to more than two forecasts.
- Clemen & Winkler (1986). Empirical evidence that equal weights often beat estimated optimal weights in combining economic forecasts. [[PDF](https://people.duke.edu/~clemen/bio/Published%20Papers/03.EconForecasts-Clemen&Winkler-JBES-86.pdf)]

## Related Frameworks

**Bias-Variance Tradeoff in Shrinkage Estimation:**
Your "operating requirement threshold" is fundamentally a characterization of the bias-variance tradeoff. When an estimator's variance grows too large, the mean squared error rises above that of a simpler baseline. This is the classical framework underlying James-Stein shrinkage (Stein, 1955) and modern applications.

**Recent formalization of the tradeoff:**
- Liu (2024). "Solving the Forecast Combination Puzzle Using Double Shrinkages." *Oxford Bulletin of Economics and Statistics*, 86(6). [[Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/obes.12590)] — Addresses how much to shrink estimated weights toward equal weights.

- Lee & Lee (recent). "Solving the Forecast Combination Puzzle" (multiple versions across 2015–2024). [[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5733863)] — Proposes methods to improve over equal weights while accounting for estimation uncertainty.

## What I Could NOT Find

I conducted targeted searches for:
- The specific numerical schedule you describe (0.3 RMSE keeping 85% gain; 0.6 keeping 50%; >1.0 becoming worse) — **not found in literature**.
- "Operating requirement" as standard terminology for this threshold — **not standard**.
- "Cold-start operating requirement" applied to audit-unit designs — **not found**.

## Assessment

**Confidence Levels:**

- **HIGH (95%+):** Your concept is a formal application/extension of the forecast combination puzzle and shrinkage estimation literature. The core principle (when does an adjustment hurt more than help?) is definitively established.

- **MEDIUM (70%):** The specific framing as an "audit unit" with a "multiplier" on "starting credence" is novel phrasing. It may map to existing concepts (hierarchical Bayes, two-stage estimation, calibration procedures), but I found no direct match.

- **LOW (20%):** Your specific quantitative schedule (the 0.3/0.6/1.0 thresholds and corresponding gain percentages) appears to be **original to your framework**. This could be a novel contribution if you derived it rigorously.

## Recommendation Before Publishing

Before claiming novelty, I'd suggest:
1. **Verify** against the Claeskels et al. (2016) and Lee & Lee papers—check if they derive similar threshold curves.
2. **Search within** the shrinkage/regularization literature (ridge regression, elastic net) for anyone characterizing "when does regularization help?" quantitatively.
3. **Check** the decision theory and scoring rules literature (Gneiting & Raftery, 2007 on proper scoring rules) for related frameworks.

The framework itself (cold-start when data is limited, trade bias vs. variance, find the operating threshold) is **established and classical**. Your specific contribution is likely either: (a) a new application domain, or (b) a novel derivation of the threshold schedule for your particular audit-unit setup.

Sources:
- [Claeskels et al., 2016 – The forecast combination puzzle](https://ideas.repec.org/a/eee/intfor/v32y2016i3p754-762.html)
- [Bates & Granger, 1969 – Combining forecasts](https://www.jstor.org/stable/2984049)
- [Clemen & Winkler, 1986 – Combining Economic Forecasts](https://people.duke.edu/~clemen/bio/Published%20Papers/03.EconForecasts-Clemen&Winkler-JBES-86.pdf)
- [Lee & Lee – Solving the Forecast Combination Puzzle](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5733863)
- [Liu, 2024 – Double Shrinkages](https://onlinelibrary.wiley.com/doi/abs/10.1111/obes.12590)
- [Forecast combinations: 50-year review](https://arxiv.org/pdf/2205.04216)
