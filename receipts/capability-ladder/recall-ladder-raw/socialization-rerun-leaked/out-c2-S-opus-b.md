## Bottom line

**It is not new.** Every component of the "cold-start operating requirement for the audit unit" is established prior art, in at least four fields that discovered it independently. Your "multiplier" is the **calibration slope** (equivalently: shrinkage factor, extremization factor, inverse temperature); your "operating requirement" is the standard **bias–variance crossover for a noisy shrinkage estimate**; and the cold-start variant — extremizing away from an *assumed* baseline rather than a *fitted* one — is explicitly treated in the forecast-aggregation literature. There is a canonical pre-2015 lineage running Spearman 1904 → Bancroft 1944 → Dawes 1979 → Copas 1983 → van Houwelingen & Le Cessie 1990.

I also tested your quantitative schedule directly. A 15-line simulation with no audit-unit-specific content reproduces it:

| true log-multiplier spread | gain retained @ err 0.3 | @ 0.6 | @ 1.0 |
|---|---|---|---|
| s = 0.8 | 0.84 | 0.32 | −1.11 |
| s = 1.0 | 0.89 | 0.56 | −0.44 |
| s = 1.3 | 0.93 | 0.71 | 0.06 |
| **your notes** | **0.85** | **~0.50** | **0.00** |

Your schedule sits inside that bracket for signal spread ≈ 0.8–1.3. The generating law is just `gain retained ≈ 1 − (noise variance / signal variance)`, with the crossover at **noise SD ≈ signal SD (SNR = 1)** — which is the attenuation/reliability law, not a property of your pipeline.

## The translation

| Your vocabulary | Established name | Field |
|---|---|---|
| multiplier scaling the pooled evidence lean | **calibration slope**; **shrinkage factor**; **extremization factor** `d`; inverse temperature | biostatistics; forecast aggregation; ML calibration |
| fixed default multiplier | uniform shrinkage factor; `d = 1` (no extremizing) | — |
| starting credence / final credence | prior and posterior log-odds | Bayesian decision theory |
| pooled evidence lean | sum of log-likelihood ratios ("weight of evidence") | — |
| operating requirement | dominance condition / bias–variance crossover / reliability threshold | statistical decision theory |
| cold-start regime | extremizing from an assumed vs. fitted baseline | forecast aggregation |

## Prior art by field

**1. Clinical prediction modelling — owns this most directly.** *(confidence: high)* The multiplier is literally called the calibration slope, and a slope < 1 means exactly your "manufactured overconfidence." Steyerberg & Vergouwe's ABCD framework makes "B: calibration slope" one of four core validation measures, and in their worked example reports a slope of 0.70 against an expected "shrinkage factor 0.82" — your two quantities, side by side, as routine practice. Canonical: **Copas, "Regression, Prediction and Shrinkage," JRSS-B 45(3), 1983** (the founding treatment; note sources disagree on the page range, 311–335 vs. 311–354 — I could not open the full text, Cloudflare blocked it); **van Houwelingen & le Cessie, "Predictive value of statistical models," Statistics in Medicine 9(11):1303–1325, 1990** (the heuristic shrinkage formula); **Copas, Stat Methods Med Res 6(2):167–183, 1997**. The slope-as-diagnostic traces to **Cox 1958** *(confidence: medium — reported consistently by secondary sources, which also note Cox called it "spread," not calibration; I did not read Cox)*.

**2. Your exact negative result is published.** *(confidence: high)* **Van Calster, van Smeden, De Cock & Steyerberg, "Regression shrinkage methods for clinical prediction models do not guarantee improved performance," Stat Methods Med Res, 2020** finds that estimated shrinkage often *increased* between-sample calibration-slope variability versus plain maximum likelihood, and that estimated shrinkage correlated *negatively* with optimal shrinkage. That is your ">1.0 is worse than the fixed default," empirically. The positive-direction analogue of your "operating requirement" is the **Riley et al. minimum-sample-size criteria**, which set a required sample size by targeting expected calibration slope ≥ 0.9 — a published accuracy requirement on this exact parameter.

**3. Forecast aggregation — the closest structural match, including cold-start.** *(confidence: high)* Extremizing is `log Ô = d · mean(log Oᵢ)`, and Neyman & Roughgarden's version is `log Ô = log O_baseline + d[mean(log Oᵢ) − log O_baseline]` — identical to your "starting credence + multiplier × pooled evidence lean." Critically, the standard commentary notes this reduces to classical extremizing "when we assume `log O_baseline = 0`," and recommends the fitted-historical-baseline version only where resolution rates are stable. **That assumed-vs-fitted baseline distinction is your cold-start regime, already in print.** The overfitting worry about `d` is stated explicitly too ("results where an optimal extremizing factor is derived in hindsight risk overfitting this parameter"). Cites: **Baron, Mellers, Tetlock, Stone & Ungar, "Two Reasons to Make Aggregated Probability Forecasts More Extreme," Decision Analysis, 2014**; **Satopää et al., "Combining multiple probability predictions using a simple logit model," Int. J. Forecasting, 2014** (optimal `d` ∈ [1.161, 3.921]); **Neyman & Roughgarden, "Are You Smarter Than a Random Expert?", arXiv:2111.03153 / EC 2022**.

**4. Psychometrics — where the schedule itself comes from.** *(confidence: high for the principle, medium for exact bibliographic details)* The reliability coefficient (true variance / observed variance) is precisely "how much of the achievable gain a noisy estimate retains," and **Kelley's 1923 regression equation** gives the optimal response: shrink the noisy per-case estimate toward the default by its reliability — ρ = 0 collapses to the group default, ρ = 1 uses the estimate raw. That is the principled generalization of your three-point schedule. **Spearman, Am. J. Psychology 15:72–101, 1904** (correction for attenuation). *I did not verify Kelley's exact book title/publisher — cite it yourself before publishing.*

**5. Statistical decision theory.** *(confidence: high for existence, medium for exactness of fit)* **Preliminary-test estimation** — Bancroft 1944 — is formally "should I use the estimate, or the assumed value θ = θ₀?", which is your question stated abstractly. Adjacent: James–Stein shrinkage toward an arbitrary fixed guess, and empirical Bayes. *Hedge: pretest estimation is a discrete choose-one framing; yours is continuous, so it's structurally analogous rather than the same theorem.*

**6. Judgment/decision-making and finance — same crossover, different dress.** *(confidence: high)* **Dawes, "The robust beauty of improper linear models in decision making," American Psychologist 34(7):571–582, 1979**: fixed unit weights beat estimated weights when estimation noise is large — your finding, for regression coefficients, in 1979. **DeMiguel, Garlappi & Uppal, Review of Financial Studies 22(5):1915–1953, 2009**: no optimizing rule beat naive 1/N, because "the gain from optimal diversification is more than offset by estimation error"; they even quantify the requirement as an estimation window (~3000 months at 25 assets). That is an operating requirement in sample-size units.

**7. ML calibration.** *(confidence: medium)* Per-instance temperature scaling failing to beat a single global temperature is the modern restatement; recent work reports instance-wise temperature failing in all 8 settings tested and sometimes degrading ECE. Results here are mixed and design-dependent, so treat this as supporting, not load-bearing.

## What you can still claim

Honestly: not "one of our more original contributions." What survives is narrower but real — **the calibrated constants for your specific pipeline**, and the noise-injection methodology that makes the requirement estimator-agnostic. I'd reframe as: *"we instantiate the known shrinkage-noise tradeoff (Copas 1983; van Houwelingen & le Cessie 1990) for our setting, and quantify the crossover for the cold-start case where only an assumed default is available (cf. Neyman & Roughgarden 2021)."* That's defensible and citable.

Two things worth acting on beyond the naming question: (a) the **cold-start bar is derivable, not just empirical** — the crossover sits where estimator error ≈ spread of the true multiplier, so you can predict it rather than simulate it; (b) your framework's implicit choice is binary (per-case estimate *or* fixed default), but **Kelley's rule dominates both** — shrink the per-case estimate toward the default by its reliability, which never underperforms either endpoint. That's a genuine improvement your current framing leaves on the table.

## Caveats

- Everything rests on my reading that "multiplier scaling the pooled evidence lean" = a coefficient on a log-odds evidence sum. Your notes' phrasing ("starting credence," "scales the pooled evidence lean") makes this near-certain, but if the multiplier is not linear-in-log-odds, items 1–3 weaken.
- I was blocked by Cloudflare on the *Journal of Clinical Epidemiology* and Oxford Academic full texts, and the van Houwelingen PDF mirror returned empty. Claims about those papers come from abstracts, indexing records, and the Steyerberg/PMC article I did read in full — verify page numbers and exact wording before citing.
- I found no source stating your error→retained-gain curve in exactly your parameterization (RMSE of log-multiplier → % of achievable gain). The *law* is standard; that specific presentation may be novel packaging. I'd call it a presentational contribution, not a conceptual one.
- Bancroft 1944, Spearman 1904, and Kelley 1923 details come from secondary sources only.

Sources:
- [Steyerberg & Vergouwe, seven steps and ABCD validation (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4155437/)
- [Copas, Regression, Prediction and Shrinkage, JRSS-B 1983](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.2517-6161.1983.tb01258.x)
- [van Houwelingen & le Cessie, Predictive value of statistical models, 1990](https://pubmed.ncbi.nlm.nih.gov/2277880/)
- [Copas, Shrinkage and regression to the mean, 1997](https://pubmed.ncbi.nlm.nih.gov/9261914/)
- [Van Calster et al., Regression shrinkage methods do not guarantee improved performance, 2020](https://journals.sagepub.com/doi/abs/10.1177/0962280220921415)
- [On the variability of regression shrinkage methods (arXiv:1907.11493)](https://arxiv.org/abs/1907.11493)
- [Validation of clinical prediction models: what does the calibration slope really measure?](https://www.sciencedirect.com/science/article/pii/S0895435619303579)
- [Riley et al., minimum sample size for external validation](https://onlinelibrary.wiley.com/doi/full/10.1002/sim.9025)
- [Dawes, The robust beauty of improper linear models (PDF)](https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf)
- [DeMiguel, Garlappi & Uppal, Optimal versus naive diversification, RFS 2009](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901)
- [Baron et al., Two reasons to make aggregated probability forecasts more extreme (PDF)](https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---two-reasons-to-make-aggregated-probability-forecasts_1.pdf)
- [Satopää et al., Combining multiple probability predictions using a simple logit model](https://www.sciencedirect.com/science/article/abs/pii/S0169207013001635)
- [Neyman & Roughgarden, Are You Smarter Than a Random Expert? (arXiv:2111.03153)](https://arxiv.org/abs/2111.03153)
- [Principled extremizing of aggregated forecasts (EA Forum)](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts)
- [Kelley's Paradox, Wainer (PDF)](https://gwern.net/doc/statistics/bayes/regression-to-mean/2000-wainer.pdf)
- [Classical Test Theory and the Measurement of Reliability (PDF)](https://www.personality-project.org/r/book/Chapter7.pdf)
- [Preliminary test estimation in ULAN models (arXiv, for Bancroft 1944 lineage)](https://arxiv.org/pdf/1906.10967)
- [Calibration Attention: instance-wise temperature scaling (arXiv:2508.08547)](https://arxiv.org/html/2508.08547v1)

Two process notes: I skipped the `_dashboard.md` session-start read to stay on this task — say the word if you want me to check it for due reminders. And if you'd like, I can write this up as a proper related-work section and run `/codex-doc-review` over it before you build on it.
