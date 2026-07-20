One more confirmation didn't render through the extractor, so I'll be explicit below about which citations I opened versus which are convergent-but-unopened. I have enough to answer. Here's the verdict.

## Bottom line

**Not new.** Your "cold-start operating requirement for the audit unit" is a re-expression, in your project's private vocabulary, of a result that **at least four established literatures independently own** — and the core of it predates 2015 by decades. The precise object — "how noisy can an estimated per-case weight be before a fixed default beats it, expressed as a threshold on the estimator's error, past which the noisy estimate is *worse* than the default" — is the **bias–variance / shrinkage tradeoff**, and in the specific form you've built (a reliability threshold for weighting a per-case estimate against a fixed default) it is **credibility theory**, whose "full credibility standard" (Mowbray **1914**) is almost a word-for-word match to your "operating requirement." This is a **predated** result you can honestly frame as an extension/application — not a **foreclosed** one (there's no impossibility theorem killing your framing), but it is decisively not original.

## Decoding your vocabulary into the fields' words

| Your term | Standard term | Field |
|---|---|---|
| audit unit forming a credence from a starting credence × multiplier on pooled evidence | a **calibration/scoring model**: posterior log-odds = prior log-odds + coefficient × aggregated log-likelihood-ratio; the multiplier is an **inverse temperature** / **logit-scaling coefficient** | ML calibration; naive-Bayes weight-shrinkage |
| per-case tuned multiplier vs. fixed default | **estimated (heterogeneous) weight vs. pooled/shrinkage default** | statistics, forecasting |
| operating requirement (accuracy needed before estimate beats default) | **credibility / reliability threshold**; the **bias–variance crossover**; the **forecast-combination puzzle** boundary | actuarial science; econometrics; statistics |
| noise "manufactures overconfidence," making the estimate worse than the default | **proper-scoring-rule penalty on miscalibration**; sharpness↔calibration tradeoff | forecast verification |
| cold-start (no fitted default yet, only an assumed one) | **empirical-Bayes vs. prior**; "full credibility standard" — how much data before the individual estimate earns weight | actuarial science; Bayesian statistics |

## The established names, fields, and canonical citations

Ranked by how closely each matches your specific construction.

**1. Credibility theory (actuarial science) — the closest single match. Confidence: high (~0.9).**
The credibility estimate is R̂ = Z·X̄ + (1−Z)·M: individual estimate X̄ blended with a fixed "manual rate" M (your fixed default), where the **credibility weight Z∈[0,1]** is exactly "how much do we trust the per-case estimate vs. the default," driven by the estimate's noise — Z→0 when the per-case data is too variable (your "past ~1.0 the estimate is worse than the default"), Z→1 when it's reliable. The **"full credibility standard"** is *literally* a threshold of estimation accuracy that must be cleared before the per-case estimate is used over the default — your "operating requirement," and the cold-start version of it.
- **Mowbray, A.H. (1914)**, "How Extensive a Payroll Exposure Is Necessary to Give a Dependable Pure Premium," *PCAS* 1:24–30 — the full-credibility threshold. (Before 2015 ✔, oldest.)
- **Whitney, A.W. (1918)**, "The Theory of Experience Rating," *PCAS* 4:274–292 — the convex-combination-of-individual-and-collective form.
- **Bühlmann, H. (1967)**, "Experience rating and credibility," *ASTIN Bulletin* 4(3):199–207; **Bühlmann & Straub (1970)** — the modern least-squares ("greatest accuracy") credibility that makes Z the noise-driven reliability weight.
- *Verification:* I opened the Loss Data Analytics credibility chapter and confirmed the R̂=ZX̄+(1−Z)M formula, the manual-rate-as-default semantics, and the full-credibility-standard threshold directly. The 1914/1918/1967 attributions come from convergent secondary sources (I did not open those primaries — treat page numbers as ~high-confidence, not verified).

**2. Bias–variance tradeoff & shrinkage / Stein estimation (statistics) — owns the governing principle. Confidence: high (~0.9).**
"A fixed value can beat a noisy individual estimate; use the estimate only when its error is small enough" *is* the bias–variance tradeoff, and its sharpest classical form is Stein's dominance of shrinkage over the raw estimate.
- **Stein, C. (1956)**, "Inadmissibility of the usual estimator for the mean of a multivariate normal distribution," *Proc. 3rd Berkeley Symp.* — (oldest of this branch ✔).
- **James, W. & Stein, C. (1961)**, "Estimation with quadratic loss," *Proc. 4th Berkeley Symp.* 1:361–379.
- **Efron, B. & Morris, C. (1973/1975)** — empirical-Bayes interpretation (relevant to your cold-start/assumed-default point).
- **Geman, Bienenstock & Doursat (1992)**, "Neural networks and the bias/variance dilemma," *Neural Computation* 4(1):1–58 — canonical modern statement.

**3. The forecast-combination puzzle (econometrics/forecasting) — closest match to the *crossover* specifically. Confidence: high (~0.85).**
The recurring finding that a **fixed simple default (equal weights) beats estimated "optimal" weights** because estimation error in the weights swamps their theoretical benefit — i.e., the estimated multiplier is worse than the default once its noise is large enough. This is your crossover, in the weights-of-a-combination setting.
- **Bates, J.M. & Granger, C.W.J. (1969)**, "The Combination of Forecasts," *Operational Research Quarterly* 20(4):451–468 — (oldest ✔).
- **Clemen, R.T. (1989)**, "Combining forecasts: A review and annotated bibliography," *Int. J. Forecasting* 5(4):559–583.
- **Stock, J. & Watson, M. (2004)**, *J. Forecasting* 23:405–430 (equal weights hard to beat); **Smith, J. & Wallis, K. (2009)**, *Oxford Bull. Econ. Stat.* — named "the forecast combination puzzle"; **Claeskens, Magnus, Vasnev & Wang (2016)**, *Int. J. Forecasting* — the theoretical explanation via estimation-induced bias/variance in random weights.
- *Verification:* The arXiv 50-year review PDF (Wang & Hyndman 2205.04216) would not render through my extractor, so the Bates–Granger/Clemen bibliographic details here are from **convergent search summaries, not a primary I opened**. They are canonical enough that I'm confident, but I'm flagging it.

**4. Calibration / (adaptive) temperature scaling (ML) — owns the *object* being scaled. Confidence: high on the object, medium on it being your intended frame.**
Your "multiplier that scales the pooled evidence lean" is an **inverse temperature on the logits**; a per-case multiplier is **adaptive/sample-dependent temperature scaling**. The "noise manufactures overconfidence" observation is the standard motivation for scaling logits toward less confidence.
- **Platt, J. (1999)**, "Probabilistic outputs for SVMs…" — logistic scaling of scores (before 2015 ✔).
- **Guo, Pleiss, Sun & Weinberger (2017)**, "On Calibration of Modern Neural Networks," *ICML* — temperature scaling, the standard reference.
- **Joy et al. (2023, AAAI)**, "Sample-dependent Adaptive Temperature Scaling" — the *per-case* multiplier, your "tuned per case." (Post-2015; shows the per-case variant is itself already a named published thing.)

**5. Why noise → worse-than-default: proper scoring rules & the calibration↔sharpness tradeoff (forecast verification). Confidence: high (~0.85).**
The mechanism — injecting noise into probabilities strictly worsens a proper score because you lose calibration faster than you gain sharpness — is the **calibration-refinement / Murphy decomposition** of proper scores.
- **Murphy, A.H. (1973)**, "A new vector partition of the probability score," *J. Applied Meteorology* 12:595–600 — reliability/resolution decomposition (before 2015 ✔).
- **DeGroot & Fienberg (1983)**, "The comparison and evaluation of forecasters," *The Statistician* 32:12–22 — calibration/refinement.
- **Gneiting, Balabdaoui & Raftery (2007)**, "Probabilistic forecasts, calibration and sharpness," *JRSS-B* 69:243–268 — the canonical modern statement of the tradeoff you're implicitly invoking.

## What, if anything, could still be defensibly yours

Be precise about the distinction (this is the trap you flagged): the *principle* is predated, so honesty requires framing as an application/extension, not a discovery. What is plausibly **not** in the literature *verbatim* — and where I can't prove a negative, so **medium confidence (~0.6) that no one has published exactly this** — is:

- The **specific numeric schedule** (RMSE-of-log-multiplier ≈ 0.3 → keep ~85% of gain; ≈ 0.6 → ~50%; ≈ 1.0 → crossover) for a **calibration temperature on pooled evidence**, derived by synthetic-error injection. Credibility theory gives you *a* threshold; the forecast puzzle gives you *a* crossover; but this particular calibrated efficiency curve for this particular object may be a genuinely useful *characterization* even if the phenomenon is old.
- The **cold-start specialization** — that the bar changes when the default is *assumed* rather than *fitted*. That maps to the empirical-Bayes-vs-prior distinction and to Mowbray's full-credibility question, so it's an *application* of known ideas to your setting, not new theory.

Net: the phenomenon and its governing law are old and multiply-owned; a specific reusable *operating curve* for your calibration multiplier could be a modest contribution **if** you frame it as "credibility theory / the forecast-combination puzzle / temperature-scaling, instantiated and quantified for our audit unit's multiplier," and cite the above. Presenting it as a *novel* concept would very likely draw a "this is just shrinkage / credibility" referee response.

## Recommendation for the write-up

Lead with the connection, not against it: "We characterize a **credibility threshold** (in the sense of Mowbray 1914 / Bühlmann 1967) — equivalently the **bias–variance crossover** familiar from the **forecast-combination puzzle** (Bates & Granger 1969; Stock & Watson 2004) and **shrinkage estimation** (Stein 1956) — for the per-case multiplier of our audit unit, and quantify it as an error schedule." Then your synthetic-error curve and the cold-start wrinkle are the increment. Also verify the two things I couldn't open myself before you cite them: the **Bates–Granger 1969** page numbers and the **Mowbray/Whitney/Bühlmann** primaries (I confirmed the credibility *formula and threshold concept* from a live source, but not those three originals).

Sources:
- [Loss Data Analytics — Ch. 9, Credibility Theory (opened; confirmed Z-formula + full-credibility standard)](https://openacttexts.github.io/Loss-Data-Analytics/ChapCredibility.html)
- [Credibility theory overview — Grokipedia](https://grokipedia.com/page/Credibility_theory)
- [Forecast combinations: an over-50-year review (Wang & Hyndman, arXiv 2205.04216)](https://arxiv.org/pdf/2205.04216)
- [On the Forecast Combination Puzzle (MDPI Econometrics 7:39)](https://www.mdpi.com/2225-1146/7/3/39)
- [The forecast combination puzzle: a simple theoretical explanation (Claeskens et al., ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0169207016000327)
- [Stein's Paradox / James–Stein shrinkage — explainer](https://towardsdatascience.com/steins-paradox-ba493f46e181/)
- [James–Stein & Ridge (Efron & Hastie, CASI Ch. 7 PDF)](https://efron.ckirby.su.domains/other/CASI_Chap7_Nov2014.pdf)
- [Sample-dependent Adaptive Temperature Scaling (AAAI 2023)](https://ojs.aaai.org/index.php/AAAI/article/view/26742/26514)
- [Temperature scaling — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-quantifying-uncertainty/temp-scaling.html)
- [Probabilistic forecasts, calibration and sharpness (Gneiting et al., HAL PDF)](https://hal.science/hal-00363242/document)

One caution on my own confidence: the credibility-theory match I verified against a live primary; the forecast-puzzle and older statistics citations rest on convergent search summaries plus my prior knowledge, not primaries I opened this session — so treat exact page numbers as needing a citation check, while the *identification of the prior art itself* is high-confidence.
