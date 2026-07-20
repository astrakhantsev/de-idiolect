## Identification

**Bottom line up front:** The *building blocks* of this concept are standard and well-named, but the specific packaged deliverable you describe — an **error-tolerance schedule** mapping an estimator's log-RMSE to the fraction of Brier-score gain it retains, with a break-even point past which the estimate is worse than a fixed fallback — is **not** a single canonically named concept. It is a bespoke sensitivity/robustness analysis assembled from three established ideas. The "multiplier that scales pooled evidence" is unmistakably the **extremizing coefficient** of forecast aggregation, and the framing tracks very closely to recent LLM-forecasting work (the AIA Forecaster technical report, Nov 2025), which uses exactly this machinery — but that report uses a *fixed* √3 coefficient and does not, as far as I can find, publish your specific 0.3/0.6/1.0 schedule. Details and confidence below.

### 1. Standard name(s)

The concept decomposes into three named pieces:

- **The setting being tuned** — "a multiplier that scales pooled evidence" — is the **extremizing coefficient** (also *extremization factor*, *log-odds extremizing parameter* `a`/`d`, or the slope of a **linear-log-odds (LLO)** / **Platt-scaling** recalibration applied to a pooled forecast). "Pooled evidence" = the summed/averaged log-odds (equivalently the geometric mean of forecasts); the multiplier extremizes that pool. *(High confidence.)*
- **The mechanism** — a noisy per-case *estimate* of that coefficient being beaten by a fixed constant, because its noise "manufactures unwarranted confidence" — is the **bias–variance / shrinkage** phenomenon of plug-in estimation (a biased constant can dominate a noisy unbiased estimate in mean-squared error; **Stein's paradox** is the classic instance). In forecasting terms, over-extremizing degrades the **calibration/reliability** term of the Brier decomposition. *(Medium-high confidence this is the right conceptual home.)*
- **The evaluation and benchmark** — "fraction of the maximum achievable improvement retained," scored by a "standard accuracy measure for probability forecasts," measured against a named reference — is a **Brier score** analysis expressed as a **skill score** (Brier Skill Score) relative to a reference forecast. Your two-benchmark caveat (a fixed value *fit to resolved outcomes* vs. a *merely assumed* value when no outcomes exist) is exactly the **in-sample/leave-one-out-optimal reference vs. a prior/default reference** distinction. *(Medium-high confidence.)*

If you need a short descriptive label for the *whole* object, the most honest one is an **"error-tolerance (break-even reliability) curve for a plug-in extremization coefficient."** I could not find that as a term of art; treat it as descriptive, not canonical. *(Low confidence that any single established name exists — I believe none does.)*

### 2. Field(s) that own it

- **Forecast aggregation / probabilistic forecasting / calibration** (the extremization coefficient, Brier scoring, recalibration). This is the primary owner.
- **Judgment & decision making** (the experimental extremization literature: Tetlock/Mellers/Baron et al.).
- **Statistics — estimation theory** (bias–variance, shrinkage, plug-in estimation error; the "noisy estimate vs. constant" mechanism).
- **Decision analysis** loosely supplies the "is it worth using at all" framing (value of information), though that analogy is imperfect — see hedge below.

### 3. Oldest and most canonical treatments (real citations)

Pre-2015, foundational:

- **Brier, G. W. (1950).** "Verification of forecasts expressed in terms of probability." *Monthly Weather Review* 78(1): 1–3. — the scoring measure. *(High confidence.)*
- **Murphy, A. H. (1973).** "A new vector partition of the probability score." *Journal of Applied Meteorology* 12: 595–600. — calibration/refinement (reliability–resolution) decomposition and the skill-score-vs-reference logic; explains *why* over-extremizing hurts. *(High confidence.)*
- **Stein, C. (1956)** and **James, W. & Stein, C. (1961),** "Estimation with quadratic loss," *Proc. 4th Berkeley Symposium* 1: 361–379. — the mechanism by which a fixed/shrunken value beats a noisy estimate. *(High confidence this is the right root for the mechanism; medium that the author intended this framing.)*
- **Ranjan, R. & Gneiting, T. (2010).** "Combining probability forecasts." *Journal of the Royal Statistical Society, Series B* 72(1): 71–91. — proves the linear opinion pool is under-confident and must be recalibrated/extremized; the theoretical root of "extremize the pool." *(High confidence.)*
- **Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., & Ungar, L. H. (2014).** "Two reasons to make aggregated probability forecasts more extreme." *Decision Analysis* 11(2): 133–145. — the canonical treatment of the extremizing coefficient in judgmental forecasting, including estimating it (per-forecaster vs. pooled). *(High confidence.)*
- **Satopää, V. A., Baron, J., Foster, D. P., Mellers, B. A., Tetlock, P. E., & Ungar, L. H. (2014).** "Combining multiple probability predictions using a simple logit model." *International Journal of Forecasting* 30(2): 344–356. — the log-odds/logit model with the extremizing parameter `a`. *(High confidence.)*
- Older still, for the log-odds transform itself: **Karmarkar, U. S. (1978)** (subjective probability weighting) and **Platt, J. (1999/2000)**, "Probabilistic outputs for support vector machines," for "Platt scaling." *(Medium confidence these are the intended lineage vs. just adjacent.)*
- For the "worth using at all" logic: **Howard, R. A. (1966).** "Information value theory." *IEEE Trans. Systems Science and Cybernetics* 2(1): 22–26. — *(Cited as a loose analogy; see hedge.)*

Most directly matching your operational framing (recent, likely the proximate context):

- **Neyman, E. & Roughgarden, T. (2022).** "Are You Smarter Than a Random Expert? The Robust Aggregation of Substitutable Signals." *ACM EC 2022* (arXiv:2111.03153). — derives the **fixed** extremizing factor `d → √3 ≈ 1.73`; this is the "single fixed value used for every case." *(High confidence on the citation.)*
- **AIA Forecaster: Technical Report (2025),** arXiv:2511.07678. — uses log-odds extremization / Platt scaling of the pooled (geometric-mean) forecast, contrasts a **fixed √3 coefficient** against a **learned coefficient fit leave-one-out on resolved questions** (in-distribution) vs. fit out-of-distribution, all scored by Brier — i.e., every structural element of your description. I did **not** find your specific numeric schedule (0.3→85%, 0.6→50%, >1.0 harmful) or an explicit synthetic-noise-injection experiment in the v1 text. *(High confidence it's the closest published analog; low-to-medium confidence it is the actual source of the schedule.)*

### 4. Confidence and explicit hedges

- **High:** "the multiplier that scales pooled evidence" = the extremizing coefficient / log-odds extremization / Platt slope; the accuracy measure = Brier score; the fixed-fit-on-resolved-cases-vs-assumed-value distinction = in-sample-optimal reference vs. assumed default.
- **Medium-high:** the harmful-noise mechanism is the bias–variance/shrinkage phenomenon, and the benchmark logic is a Brier skill score relative to a reference forecast.
- **Low / explicit hedge:** that the *packaged specification* (the specific error→gain schedule, derived by injecting synthetic log-scale errors) has any single established academic name. I searched actively and found none; I believe it is a **bespoke robustness/sensitivity analysis**, not a named concept. If it has a home, it is an appendix-style analysis in the LLM-forecasting/extremization literature rather than a classical result.
- **Hedge on "value of information":** I invoked VoI only as an analogy for "worth using at all." It is technically imperfect here: for a *Bayesian who models the noise*, imperfect information has non-negative value; the harm in your description arises specifically from **plug-in** use of a point estimate as if exact, which is a shrinkage/bias-variance failure, not a VoI failure. Don't lean on the VoI label as the primary name.
- **Hedge on exact citation details:** I'm confident in authors/years/venues for Brier (1950), Murphy (1973), Ranjan & Gneiting (2010), Baron et al. (2014), Satopää et al. (2014), and Neyman & Roughgarden (2022). Exact page numbers for the Stein/James–Stein and Karmarkar/Platt items I'm giving from standard reference memory and would double-check before formal citation.

If you can tell me where you encountered this (a paper, an appendix, a platform's methodology doc), I can likely pin the exact origin of the 0.3/0.6/1.0 schedule — that specific triplet is the one piece I could not source.

Sources:
- [Ranjan & Gneiting (2010), *JRSS-B*](https://academic.oup.com/jrsssb/article/72/1/71/7076442)
- [Baron, Mellers, Tetlock, Stone, Ungar (2014), *Decision Analysis*](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293)
- [Satopää et al. (2014) / related logit aggregation work](https://arxiv.org/pdf/1406.2148)
- [Neyman & Roughgarden (2022), "Robust Aggregation of Substitutable Signals"](https://arxiv.org/abs/2111.03153)
- [AIA Forecaster: Technical Report (2025)](https://arxiv.org/html/2511.07678v1)
- [Recalibrating probabilistic forecasts (Baron et al.), *JDM*](https://www.sas.upenn.edu/~baron/journal/21/210914/jdm210914.html)
- [Principled extremizing of aggregated forecasts — EA Forum](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts)
