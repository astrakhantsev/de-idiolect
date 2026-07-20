I have enough to answer confidently. I ran active searches and confirmed every structural primitive against real sources; the one thing I could *not* find is any named/canonical status for the specific numeric schedule, which tells me it's bespoke. Here's the identification.

## 1. What this concept is called

Strip away the obfuscated vocabulary ("audit unit," "credence," "pooled evidence lean," "accuracy score") and the operation is exact and standard:

> **final log-odds = starting log-odds + (multiplier) × (aggregate weight of the evidence)**

That is **log-odds (logit) Bayesian updating with a calibration coefficient**, and the "multiplier that scales the pooled evidence lean" is a single, named scalar that recurs under four names across four fields — all the *same* number (a linear coefficient on the log-odds evidence term):

- **Calibration slope** (a.k.a. shrinkage factor / discounting factor) — biostatistics & clinical prediction. Slope = 1 is ideal; slope < 1 shrinks over-extreme evidence; slope > 1 extremizes. Fitting it is **logistic recalibration** (≈ **Platt scaling**).
- **Inverse temperature** (1/T) — machine-learning confidence calibration. "Fixed default vs. tuned-per-question" is precisely **global temperature scaling vs. per-instance/adaptive temperature**.
- **Extremizing coefficient** — judgmental-forecasting / opinion-pooling literature (the single parameter `a` in logit pooling of forecasts).
- **Weight of evidence** (I. J. Good) is the name for the thing the multiplier scales — the summed log-likelihood-ratio / log-Bayes-factor, i.e. your "pooled evidence lean."

The **"cold-start operating requirement" itself** — *how small the estimator's error must be for a tuned multiplier to beat the fixed default* — is not, as far as I can find, a named theorem. It is a **bias–variance / plug-in-vs-default decision** (use the noisy estimate only when its variance cost is smaller than the bias of the default — a James–Stein-flavored shrinkage argument), presented as an **error budget / tolerance (sensitivity) analysis**. The specific mechanism whereby a *noisy* multiplier is worse than a fixed one — "its noise manufactures overconfidence" — is the standard **Jensen's-inequality effect**: random error in a log-odds/temperature multiplier inflates expected extremity and hence expected proper-scoring-rule loss, even when the multiplier is right on average. That the schedule is "built by injecting synthetic error of a given size" confirms it characterizes an **error level**, not an estimator — i.e. it is a bespoke Monte-Carlo perturbation study, not a citable named result. (High confidence it's bespoke; I searched its distinctive numeric signature — 0.3→85%, 0.6→50%, 1.0→break-even — and found nothing.)

## 2. Which fields own it

No single owner — it's genuinely multi-field, and that's the honest answer:

- **Biostatistics / clinical prediction modeling** — calibration slope, recalibration, shrinkage (the most direct home of "a multiplier on the log-odds").
- **Machine learning — confidence/probability calibration** — temperature scaling, Platt scaling, fixed-vs-adaptive temperature.
- **Bayesian statistics & information theory** — weight of evidence / log-Bayes-factor updating.
- **Judgmental forecasting / decision analysis** — extremizing and logit opinion pools.

## 3. Oldest & most canonical treatments (real citations)

Pre-2015:

- **I. J. Good (1950).** *Probability and the Weighing of Evidence.* Griffin / Hafner. — Establishes **weight of evidence** = log Bayes factor as the additive log-odds evidence unit. (See also Good, "Weight of Evidence: A Brief Survey," *Bayesian Statistics 2*, 1985, pp. 249–270.) *Confidence: high.*
- **D. R. Cox (1958).** "Two further applications of a model for binary regression." *Biometrika* 45(3–4): 562–565. — Canonical **origin of the calibration slope/intercept**: regress the outcome on the predicted log-odds; slope = 1, intercept = 0 is perfect calibration. *Confidence: high.*
- **J. C. van Houwelingen & S. le Cessie (1990).** "Predictive value of statistical models." *Statistics in Medicine* 9(11): 1303–1325. — Canonical **heuristic shrinkage factor** (a fitted <1 multiplier that de-extremizes over-confident predictions). *Confidence: high.*
- **J. Platt (1999).** "Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods." In *Advances in Large Margin Classifiers.* — **Platt scaling**, the ML instantiation of fitting a slope/intercept on scores. *Confidence: high.*
- **Satopää, Baron, Foster, Mellers, Tetlock & Ungar (2014).** "Combining multiple probability predictions using a simple logit model." *International Journal of Forecasting* 30(2): 344–356. — The **single-parameter extremizing coefficient** on pooled logits ("tuned per question or left at a default" maps onto fitting vs. fixing this parameter). Companion: **Baron, Mellers, Tetlock, Stone & Ungar (2014)**, "Two reasons to make aggregated probability forecasts more extreme," *Decision Analysis* 11(2): 133–145. *Confidence: high on citations; medium that this is the framing the source intended vs. the biostatistics one.*
- **E. W. Steyerberg (2009).** *Clinical Prediction Models.* Springer. — Standard synthesis tying together calibration slope, recalibration, and shrinkage. *Confidence: high.*

Post-2015 but the canonical ML reference (for completeness): **Guo, Pleiss, Sun & Weinberger (2017),** "On calibration of modern neural networks," *ICML* — **temperature scaling**, i.e. the fixed-default single-multiplier version.

## 4. Confidence and hedges

- **The underlying object (a scalar multiplier on aggregated log-odds evidence, i.e. calibration slope / inverse temperature / extremizing coefficient): high confidence.** The math in the description is unambiguous.
- **Which field "owns" it: deliberately hedged — it doesn't have one owner.** I'm confident it's the calibration-slope/temperature/extremizing family; I'm *not* confident which of those the source author had in mind, because the operational description is field-neutral.
- **The specific operating-requirement schedule (0.3→~85% of gain, 0.6→~half, >1.0→worse-than-default): high confidence it is NOT an established, named result.** It reads as a bespoke synthetic-noise sensitivity analysis from whatever (likely recent, AI-evaluation-flavored) source is being paraphrased. The *ingredients* it rests on are canonical (bias–variance/shrinkage; Jensen-inequality overconfidence from a noisy log-scale multiplier; proper scoring rules), but the schedule itself I could not match to any literature.
- **Caveat on the paraphrase:** "audit unit / credence / accuracy score" is non-standard, AI-eval-style terminology, so there's residual risk the source frames this as something more specialized (e.g. a particular auditing-agent calibration protocol). If you can share the source text or where it came from, I can tighten the field attribution.

Sources:
- [Cox (1958), "Two further applications of a model for binary regression" (Semantic Scholar)](https://www.semanticscholar.org/paper/Two-further-applications-of-a-model-for-binary-Cox/7064e4567cd25101f59fb2c597a2d975695e99d1)
- [Validation of clinical prediction models: what does the "calibration slope" really measure? (J Clin Epidemiol)](https://www.sciencedirect.com/science/article/pii/S0895435619303579)
- [Calibration slope & intercept from logistic recalibration (MetricGate)](https://metricgate.com/docs/calibration-slope-intercept-logistic/)
- [Van Houwelingen & le Cessie (1990), "Predictive value of statistical models" (Wiley)](https://onlinelibrary.wiley.com/doi/abs/10.1002/sim.4780091109)
- [Van Houwelingen, "Shrinkage and penalized likelihood as methods to improve predictive accuracy" (PDF)](http://yaroslavvb.com/papers/houwelingen-shrinkage.pdf)
- [Satopää et al. (2014), "Combining multiple probability predictions using a simple logit model" (IDEAS/RePEc)](https://ideas.repec.org/a/eee/intfor/v30y2014i2p344-356.html)
- [Baron et al. (2014)-related forecasting/extremizing discussion (JDM, U. Penn)](https://www.sas.upenn.edu/~baron/journal/21/210914/jdm210914.pdf)
- [I. J. Good, "Weight of Evidence: A Brief Survey" (PDF, Tufts archive)](https://www.cs.tufts.edu/~nr/cs257/archive/jack-good/weight-of-evidence.pdf)
- [Guo et al. (2017)-lineage temperature/adaptive scaling comparison (arXiv 2508.08547)](https://arxiv.org/pdf/2508.08547)
- [Calibrating Language Models with Adaptive Temperature Scaling (arXiv 2409.19817)](https://arxiv.org/abs/2409.19817)
