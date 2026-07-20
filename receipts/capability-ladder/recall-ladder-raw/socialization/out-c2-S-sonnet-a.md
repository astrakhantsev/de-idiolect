## Bottom line

The core idea is not new — it's one of the best-established results in statistics, independently rediscovered under several field-specific names, with the oldest canonical treatment dating to **1914**. I found no evidence the exact term "cold-start operating requirement" (or your specific RMSE-of-log-multiplier schedule with 0.3/0.6/1.0 breakpoints) exists anywhere in the literature — that quantitative parameterization may be genuinely new — but the underlying framework ("a case-specific correction beats a fixed default only once its estimation error clears a threshold, and the bar is different when there's no fitted default yet to fall back on") is decades-old and has a standard name in at least one field. Recommend framing this as an **extension/application**, not a novel contribution, per your own calibration norm.

## Best match: actuarial credibility theory

This is the tightest terminological and structural fit — striking enough that I'd flag it as very likely the concept your framework rediscovered:

- **"Credibility"** is literally the field's term (your "credence" ≈ their "credibility").
- The **credibility factor Z** (0 ≤ Z ≤ 1) is exactly your "multiplier": `estimate = Z × individual experience + (1−Z) × class/population default`.
- **"Full credibility standard"** is literally the name for your "operating requirement" — the threshold (originally stated in required claim counts, later generalized) at which the individual/per-case estimate is trusted over the fixed class rate.
- **Cold start is explicitly handled**: a brand-new risk with no experience data gets the class/manual rate outright (Z=0); the Bühlmann–Straub extension (1970) generalizes this to varying/near-zero exposure.

Canonical, pre-2015 sources:
- **Mowbray, A.H. (1914)**, "How Extensive a Payroll Exposure Is Necessary to Give a Dependable Pure Premium?", *Proceedings of the Casualty Actuarial Society*, Vol. 1, pp. 24–30 — the founding paper of "full credibility," oldest citation found. **Confidence: medium-high** — I could not fetch this directly (pre-digital-era proceedings, not open online), so I'm relying on consistent secondary citation across multiple independent sources (actuary.org, Medium/ACAS author, standard actuarial exam notes).
- **Bühlmann, H. (1967)**, "Experience Rating and Credibility," *ASTIN Bulletin* — derives Z as the MSE-minimizing linear blend (partial credibility). **Confidence: high** (converging secondary sources, standard textbook result).
- **Bühlmann, H. & Straub, E. (1970)** — extends to heterogeneous/varying exposure, i.e. the cold-start case. **Confidence: medium** — venue/year confirmed by multiple sources, didn't read primary text (German-language original, hard to access).

## Independently-converging matches in other fields

The same structural result — "your per-case estimate loses to the fixed default once its noise exceeds some level" — was independently derived at least three more times, in unrelated fields, which is itself evidence this is a general theorem-class, not a niche fact:

- **Empirical Bayes / James–Stein shrinkage** (statistics). **James, W. & Stein, C. (1961)**, "Estimation with Quadratic Loss," *Proc. 4th Berkeley Symposium*; popularized with the exact "per-case MLE loses to shrunk estimate under noise" framing by **Efron, B. & Morris, C. (1975)**, "Data Analysis Using Stein's Estimator and its Generalizations," *JASA* 70(350):311–319 (the famous baseball batting-average example). **Confidence: high** — I attempted to fetch the primary PDF directly but it rendered empty via safefetch; relying on 5+ consistent independent secondary sources (JSTOR/Tandfonline, RAND, multiple university course PDFs) for venue/pages, which is solid but not a first-hand read.
- **"Forecast combination puzzle"** (econometrics). **Bates, J.M. & Granger, C.W.J. (1969)**, "The Combination of Forecasts," *Operational Research Quarterly* 20(4):451–468 — shows a fixed equal-weight combination beats data-estimated "optimal" weights once weight-estimation error is large. **Confidence: high** on citation (5 independent sources agree on venue/pages); I could not get past a paywall to read the original, so I'm trusting secondary characterization of its content.
- **Shrinkage/calibration-slope in prediction-model validation** (biostatistics) — the closest structural analogue to "multiplier on pooled log-odds evidence," since it's literally a scalar applied to a linear predictor. **Copas, J.B. (1983)**, "Regression, Prediction and Shrinkage," *JRSS-B* 45(3):311–354, and **Van Houwelingen, J.C. & Le Cessie, S. (1990)**, "Predictive Value of Statistical Models," *Statistics in Medicine* 9(11):1303–1325. Notably, this literature has already documented your exact "cold-start" caveat: van Calster et al. (2020, building on Copas) found the *estimated* shrinkage factor is often *inversely* correlated with the *true* optimal shrinkage when data are scarce — i.e., trying to estimate the correction when you can't yet do it reliably actively hurts. **Confidence: medium-high** — Wiley/Cloudflare blocked my direct fetch of Copas 1983, so this rests on abstract/metadata plus multiple consistent secondary summaries, not a primary read.
- **Bayesian dynamic borrowing / power priors** (clinical trials) — the best match for the "no fitted default exists yet" cold-start sub-case specifically. **Ibrahim, J.G. & Chen, M.-H. (2000)**, "Power Prior Distributions for Regression Models," *Statistical Science* 15(1):46–60, introduces a discount parameter controlling how much pooled/historical evidence to borrow. Later literature (2015–2026, not pre-2015) explicitly documents that this discount parameter can't be reliably estimated from a single current + single historical dataset — structurally identical to your cold-start claim. **Confidence: medium** — solid on the 2000 paper's existence and role, but I did not confirm that paper itself (rather than its descendants) states an error threshold like yours.

## What I could not find prior art for

- The literal phrase "cold-start operating requirement" — no hits.
- Your specific quantitative schedule (RMSE of log-multiplier; 0.3→85% of gain retained, 0.6→~50%, 1.0→net negative) in that exact parameterization — no hits, across several phrasing attempts. I did not exhaustively search actuarial trade literature or forensic-science likelihood-ratio calibration journals, which are thinly indexed in general web search, so I can't rule out a close match there. **This is the one place where absence-of-evidence is weakest** — treat "not found" as "not found by me in ~12 searches," not as a proof of absence.
- One point worth flagging directly: a **2026 arXiv preprint**, "PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration," independently derives essentially the same cold-start threshold structure (population-level default beats per-case shrinkage below some data threshold, per-case wins above it) in a completely different application (RLHF reward models). It's post-2015 so doesn't satisfy your citation requirement, but it's evidence people are still actively re-deriving this pattern under fresh names in 2026 — so treat "we may not be the only ones minting a name for this concept right now" as a live risk, not just a historical one.

## Recommendation

Don't write this up as a novel contribution to the general framework. The honest framing is: your "audit unit" is an instance of credibility-weighted (or empirical-Bayes-shrunk, or shrinkage-recalibrated) estimation, and the "cold-start operating requirement" is your pipeline-specific instantiation of the classical full-credibility-standard / shrinkage-reliability question, characterized via a synthetic-noise-injection simulation — a standard methodology in the clinical-prediction-model shrinkage literature (e.g., Van Calster et al. 2020 uses the same technique). The plausibly original piece is narrow: your specific numeric schedule and units, applied to your specific pipeline. Given the "search-field-vocabulary" lesson from your own project history, I'd treat this as **predated, not foreclosed** — safe to build on and cite as prior art, not safe to claim as new.

Sources:
- [Bates & Granger 1969, "The Combination of Forecasts"](https://link.springer.com/article/10.1057/jors.1969.103)
- [Forecast combination puzzle — Smith & Wallis explanation](https://www.sciencedirect.com/science/article/abs/pii/S0169207016000327)
- [Copas 1983, "Regression, Prediction and Shrinkage"](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.2517-6161.1983.tb01258.x)
- [Van Houwelingen & Le Cessie 1990, "Predictive Value of Statistical Models"](https://onlinelibrary.wiley.com/doi/abs/10.1002/sim.4780091109)
- [Van Calster et al. 2020, shrinkage does not guarantee improved performance](https://journals.sagepub.com/doi/abs/10.1177/0962280220921415)
- [Ibrahim & Chen 2000, "Power Prior Distributions for Regression Models"](https://projecteuclid.org/journals/statistical-science/volume-15/issue-1/Power-prior-distributions-for-regression-models/10.1214/ss/1009212673.full)
- [Efron & Morris 1975, "Data Analysis Using Stein's Estimator"](https://www.tandfonline.com/doi/abs/10.1080/01621459.1975.10479864)
- [Bühlmann model — Wikipedia overview of credibility factor Z](https://en.wikipedia.org/wiki/B%C3%BChlmann_model)
- [Credibility theory — Wikipedia, full credibility standard](https://en.wikipedia.org/wiki/Credibility_theory)
- [Actuarial Credibility: Beyond the Numbers (Mowbray 1914 context)](https://medium.com/@alexfiliakov/actuarial-credibility-beyond-the-numbers-c1bd465d7339)
- [PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration (2026, independent recent reinvention)](https://arxiv.org/pdf/2606.27578)
