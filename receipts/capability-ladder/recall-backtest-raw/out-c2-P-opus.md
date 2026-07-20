I have enough to answer confidently. The description is a paraphrase-obfuscated account of **probability calibration via a scalar on log-odds evidence**, with the "operating requirement" being a precision/error tolerance for adapting that scalar per-item versus using a fixed default. Here is the identification.

---

## 1. What the concept is called

The description has two layers. The **mechanism** it describes is standard and well-named; the **specific "operating requirement" schedule** is (as far as I can find) bespoke, not a named result. Taking the pieces in turn:

**(a) The "multiplier that scales the pooled evidence lean."** This is a **calibration slope** (equivalently the **inverse temperature** of temperature scaling; equivalently a **shrinkage / discount factor on the summed log-likelihood-ratios**). The setup — final logit = prior logit + β·(sum of evidence log-odds) — is exactly **logistic recalibration**: `logit(p_calibrated) = α + β · logit(p_raw)`. The "fixed default" the text refers to is **β = 1** (use the evidence as-is), or a single **globally-fitted** β. A multiplier **< 1** is precisely the classic remedy for **overconfidence** (evidence "too extreme"), and a noisy per-item β that occasionally lands **> 1** is what "manufactures overconfidence." Because the multiplier is a *scale* parameter, multiplicative noise is additive in the log, which is why the natural error metric is **RMSE of log(multiplier)** — i.e. RMSE of the log-temperature. **(Confidence: high.)**

**(b) The evidence-pooling picture.** Aggregating independent evidence by summing log-likelihood ratios and then discounting the sum is the **weight-of-evidence** tradition (I. J. Good / Turing), and the discount specifically corrects the **overconfidence of a naïve-Bayes-style independence assumption**. In forensic/speaker-ID work the same object appears as calibrating log-likelihood-ratios (the C_llr cost). **(Confidence: high on the naming; the specific "pooled" framing is a paraphrase, medium.)**

**(c) The "cold-start operating requirement" itself** — a schedule saying how small the estimator's error must be for the per-item multiplier to beat the default, keyed to RMSE(log β) (≈0.3 → keep ~85% of the achievable proper-score gain; ≈0.6 → ~half; >~1.0 → worse than default). I could **not** find this as a named, canonical result. It is best described as an **error-budget / precision-tolerance (break-even) analysis for a plug-in calibration parameter**, and it instantiates two established ideas: the **bias–variance / overfitting tradeoff in recalibration** (a noisily estimated recalibration coefficient can do worse than not adapting), and the **empirical-Bayes "borrow strength until you have enough data, then switch" rule** (use the default until you have resolved cases to fit against — exactly the cold-start point). **(Confidence: high that it's an instance of these; medium-high that it is *not* a standardly-named schedule — treat "it's bespoke" as my considered read, not a certainty.)**

**One-line answer:** it's the **minimum accuracy (log-scale error tolerance) an estimated calibration slope / temperature must meet for per-item recalibration to beat a fixed-default (β=1 or global) recalibration** — a precision requirement stated on the calibration-slope/temperature.

## 2. Field(s) that own it

- **Probability calibration in machine learning / statistics** — temperature scaling, Platt scaling, recalibration. *(primary)*
- **Biostatistics / clinical prediction-model methodology** — "calibration slope," shrinkage, overfitting. *(primary; this field is where the slope-and-shrinkage vocabulary is most developed)*
- **Bayesian decision theory / epistemology and forensic likelihood-ratio science** — weight of evidence, calibration of LRs, proper scoring rules.
- **Surface framing only:** the "audit unit outputs a credence" vocabulary matches recent **AI-safety auditing / control** evaluation work (auditors emit a credence that a codebase was sabotaged, etc.). I'm **medium** confidence the passage was authored in that setting; the underlying concept is the calibration machinery above regardless.

## 3. Oldest / canonical treatments (real citations)

Calibration slope & shrinkage (the multiplier):
- **Cox, D. R. (1958).** "Two further applications of a model for binary regression." *Biometrika* 45(3–4): 562–565. — origin of the slope-of-observed-on-predicted idea. *(Caveat, and it's a real one: Cox called it "spread," not "calibration"; the "calibration slope" name is later.)*
- **Copas, J. B. (1983).** "Regression, Prediction and Shrinkage." *JRSS Series B* 45(3): 311–354. — shrinkage as the slope of actual on predicted; Stein-type predictors.
- **Van Houwelingen, J. C., & le Cessie, S. (1990).** "Predictive value of statistical models." *Statistics in Medicine* 9(11): 1303–1325. — heuristic shrinkage factor.
- **Steyerberg, E. W. (2009).** *Clinical Prediction Models.* Springer. — textbook synthesis of calibration slope + shrinkage.

Weight of evidence / LR calibration (the pooled-evidence view):
- **Good, I. J. (1950).** *Probability and the Weighing of Evidence.* Charles Griffin. (See also **Good, 1985**, "Weight of evidence: a brief survey," *Bayesian Statistics 2*.)
- **DeGroot, M. H., & Fienberg, S. E. (1983).** "The comparison and evaluation of forecasters." *The Statistician* 32(1–2): 12–22. — calibration/refinement and proper scoring.
- **Brümmer, N., & du Preez, J. (2006).** "Application-independent evaluation of speaker detection." *Computer Speech & Language* 20(2–3): 230–275. — C_llr, calibration of log-likelihood-ratios.

Classifier calibration / temperature (the ML naming):
- **Platt, J. (1999).** "Probabilistic outputs for support vector machines…" in *Advances in Large Margin Classifiers.*
- **Niculescu-Mizil, A., & Caruana, R. (2005).** "Predicting good probabilities with supervised learning." *ICML 2005.* — documents naïve-Bayes overconfidence and recalibration.
- **Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017).** "On Calibration of Modern Neural Networks." *ICML 2017.* — temperature scaling (the modern name for the single-multiplier version); *post-2015, included as the canonical ML reference.*

Proper scoring foundations (why noisy overconfidence is penalized): **Brier (1950)**, *Monthly Weather Review* 78: 1–3; **Savage (1971)**, "Elicitation of personal probabilities and expectations," *JASA* 66: 783–801.

## 4. Confidence and hedges

- **High:** the multiplier = calibration slope / inverse temperature / log-odds shrinkage factor; the default is β=1 or a globally-fitted β; a <1 multiplier corrects overconfidence and noisy >1 excursions create it; RMSE-of-log is the natural error metric for a scale parameter. Field ownership and all pre-2015 citations above are ones I stand behind.
- **Medium-high:** that the specific **RMSE(log β) → fraction-of-gain schedule** (0.3/0.6/1.0 → 85%/50%/worse) is **not a standardly named result** but a bespoke error-budget analysis built by injecting synthetic Gaussian noise into log-temperature and reading off proper-score degradation. I searched for it directly and found the *ingredients* (bias–variance of recalibration, plug-in noise inflating log loss) but not this schedule as a named concept.
- **Medium / explicitly uncertain:** that the passage originates in AI-safety auditing/control evaluation. The "audit unit / credence / sabotage" vocabulary points there, but I did not locate the exact source document, so I can't attribute it. I'd flag that some of the very recent (2026) arXiv titles surfaced by search should be treated as unverified — I did not open and confirm them, and search-summary prose can confabulate.
- **What I could not do:** find a single crisp textbook name for "the accuracy an estimate must reach to beat a default." That break-even/usefulness-threshold framing is real (it's a value-of-information / dominance question) but I know of no canonical named theorem for it in this calibration context; I'd mark any single-name claim there as low confidence.

Sources:
- [Van Calster et al. (2019), "…what does the calibration slope really measure?" (JCE)](https://www.jclinepi.com/article/S0895-4356(19)30357-9/fulltext)
- [Recalibration methods for risk scores (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8977399/)
- [Copas, J. B. (1983), "Regression, Prediction and Shrinkage" (JRSS-B)](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.2517-6161.1983.tb01258.x)
- [Steyerberg, shrinkage in logistic regression (PDF)](http://www.yaroslavvb.com/papers/steyerberg-application.pdf)
- [Guo et al. (2017), "On Calibration of Modern Neural Networks" (ResearchGate record)](https://www.researchgate.net/publication/317591245_On_Calibration_of_Modern_Neural_Networks)
- [Niculescu-Mizil & Caruana (2005), "Predicting Good Probabilities…" (PDF)](https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf)
- [Tutorial on logistic-regression calibration and fusion (arXiv, forensic LR / weight of evidence)](https://arxiv.org/pdf/2104.08846)
- [Frontiers: "Likelihood Ratio as Weight of Forensic Evidence" (Good's weight of evidence lineage)](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2018.00224/full)
- [scikit-learn: Probability calibration (naïve-Bayes overconfidence, Platt/isotonic)](https://scikit-learn.org/0.21/modules/calibration.html)
