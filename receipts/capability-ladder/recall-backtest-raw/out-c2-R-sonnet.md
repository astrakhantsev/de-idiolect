## Findings

**No single canonical name exists for the whole packaged schedule** ("RMSE-of-log-multiplier → fraction of Brier-skill retained, with 0.3/0.6/1.0 breakpoints"). I ran ~10 targeted searches (direct phrase matches, numeric-schedule matches, AI-control/audit-jargon matches) and found no publication presenting this exact curve as a named result. It reads as a bespoke sensitivity/break-even analysis — most plausibly from AI-control/auditing work (the "audit unit" framing in this project's own notes), built by injecting synthetic noise, not published as a textbook theorem. I should flag: this project directory (`recall-backtest`) already contains a prior model run (Opus) on this exact prompt, which independently reached the same "no canonical single name" conclusion via a different search path — I verified its key citations myself rather than just trusting it.

That said, every component of the description maps cleanly onto established, separately-named concepts:

**1. Standard names (by component)**

| Piece of the description | Established name |
|---|---|
| Output: "fraction retained of achievable improvement in a probability-forecast accuracy measure" | **Brier Skill Score** (a proper-scoring-rule skill score) |
| "Multiplier that scales pooled evidence" (a scalar on summed log-odds/evidence) | **Calibration slope** / **temperature** (temperature scaling) / **shrinkage (discount) factor on weight of evidence** |
| "Estimate per case vs. fixed value for all cases" | **No pooling vs. complete pooling**; principled middle ground = **shrinkage / partial pooling (empirical Bayes)** |
| A noisy plug-in estimate doing worse than a fixed constant | **Estimation risk**; the estimator is **dominated** by the fixed constant (decision-theory sense) |
| "Fixed value fit to resolved cases" vs. "merely assumed value" | **Climatology reference forecast** (fitted vs. naive/assumed climatology) in forecast verification |
| Schedule built via injected synthetic error rather than a specific estimator | **Monte Carlo noise-injection / perturbation sensitivity analysis** (a method label, not a proper noun) |

**2. Fields that own it**
- **Forecast verification / probabilistic forecasting** (meteorology → now ML calibration) — owns Brier score, skill score, climatology reference.
- **Statistical decision theory / Bayesian statistics** — owns estimation risk, domination, shrinkage, empirical Bayes.
- **Probability calibration (ML) / clinical prediction modeling (biostatistics)** — owns calibration slope, temperature scaling, shrinkage-factor practice.
- **Decision analysis** (value of information / "better than not using it at all") is a loose match in spirit only — its native metrics (EVPI, net benefit) don't match the Brier-retention curve described, so I'd call this an analogy, not an owner.

**3. Oldest/canonical treatments (all verified via search this session)**
- Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review* 78(1): 1–3. — origin of the Brier score.
- Murphy, A. H. (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology* 12(4): 595–600. — reliability/resolution/uncertainty decomposition underlying skill-vs-climatology.
- Gneiting, T. & Raftery, A. E. (2007). "Strictly Proper Scoring Rules, Prediction, and Estimation." *JASA* 102(477): 359–378.
- James, W. & Stein, C. (1961). "Estimation with Quadratic Loss." *Proc. 4th Berkeley Symposium on Mathematical Statistics and Probability* 1: 361–379. — a plug-in per-case estimate being inadmissible/dominated by a shrunk-toward-fixed estimate.
- Copas, J. B. (1983). "Regression, Prediction and Shrinkage." *JRSS B* 45(3): 311–354. — shrinkage factor as slope of actual-on-predicted, the clinical-prediction lineage of "calibration slope."
- DeMiguel, V., Garlappi, L., Uppal, R. (2009). "Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy?" *Review of Financial Studies* 22(5): 1915–1953. — the closest published applied demonstration of "an estimated setting is beaten by a fixed default because estimation error swamps the theoretical gain," structurally the same shape as this schedule.

**4. Confidence**
- **High**: Brier Skill Score, calibration-slope/shrinkage terminology, and the James-Stein/estimation-risk framing are correct and well-established; all six citations above are verified (author/year/venue/pages checked against independent sources this session).
- **High**: no established, single named result matches the *entire packaged schedule* (the specific 0.3/0.6/1.0 → 85%/50%/harmful numbers) — I searched directly for this and found no hit; absence of evidence isn't proof, but it's a genuine gap after real search.
- **Low/unconfirmed**: any specific attribution to an AI-control/auditing paper — the "audit unit," "cold-start," "pooled evidence" phrasing strongly suggests that origin (consistent with your own project notes), but I could not locate the specific source document.
