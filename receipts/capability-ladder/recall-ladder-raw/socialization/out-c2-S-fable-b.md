## Bottom line

**Your "cold-start operating requirement for the audit unit" is not new as a concept.** It is a recombination of three well-established bodies of work, and its central claim — *a noisy per-case scaling parameter only beats a fixed default once its estimation error falls below a threshold, and past a crossover the estimate is strictly worse because its variance manufactures overconfidence* — is a textbook bias–variance / estimation-error result, with a theorem-grade version (Stein) dating to 1956 and a near-exact applied analog (the "forecast combination puzzle") that has been studied under that name since the 2000s. The specific numeric schedule you derived (RMSE ≈ 0.3 → ~85% of gain, ≈ 0.6 → ~half, ≈ 1.0 → crossover) I did **not** find published as such — that particular curve may be a genuine empirical measurement of your pipeline. But the *thing it measures* is old and owned by several fields. This is **predated, not foreclosed** (you can present it as an extension/measurement), with one corner that is genuinely foreclosed by a theorem (see §2).

Let me decode the vocabulary to the standard terms, because the coinage is what's hiding the prior art (same pattern we've hit before).

## What each coined term maps to

**"Multiplier that scales the pooled evidence lean" (on a prior credence, in log-odds)** = a scalar coefficient on aggregated log-odds. This object has two established homes:

- **Extremizing / logit (log-odds) opinion pooling** — forecasting & decision analysis. Your "multiplier > 1 sharpens, the default is a fixed scale" is *exactly* the extremizing coefficient on a geometric-mean-of-odds pool.
- **Temperature scaling / Platt scaling** — ML calibration. A single global scalar on the logit is "fixed default"; a per-case scalar is "adaptive/instance-wise temperature scaling."

**"How accurate must the per-case multiplier be before it beats the fixed default, else its noise creates overconfidence"** = the **bias–variance / estimation-error tradeoff**, whose canonical instances are **shrinkage / Stein's paradox / empirical Bayes** and, most tightly, the **forecast combination puzzle** (estimated "optimal" weights lose to a fixed/equal default because of estimation variance).

**"Cold-start regime — fall back to an assumed default, not a fitted one"** = the **cold-start problem** (recommender systems) plus **empirical-Bayes shrinkage-to-prior when local data is scarce**.

## Prior art, by field, with canonical + pre-2015 citations

**1. The scaling-the-pooled-log-odds object (confidence: high, ~0.9 it's not novel)**
- Ranjan & Gneiting (2010), "Combining probability forecasts," *JRSS-B* 72(1):71–91 — beta-transformed linear opinion pool; shows any average of distinct calibrated forecasts is under-sharp and needs recalibration. **Pre-2015.**
- Satopää, Baron, Foster, Mellers, Tetlock & Ungar (2014), "Combining multiple probability predictions using a simple logit model," *Int. J. Forecasting* 30(2):344–356 — geometric-mean-of-odds pool with **a single tuning parameter that shifts each probability toward its nearest extreme**. This is the closest published twin of your "multiplier." **Pre-2015.**
- Baron, Ungar, Mellers & Tetlock (2014), "Two reasons to make aggregated probability forecasts more extreme," *Decision Analysis* 11(2) — the underconfidence + information-diversity rationale for the coefficient. **Pre-2015.**
- Deeper root: Genest & Zidek (1986), "Combining probability distributions: a critique and annotated bibliography," *Statistical Science* — the logarithmic opinion pool. **Pre-2015.**
- ML-calibration home: Platt (1999), "Probabilistic outputs for SVMs…"; Guo, Pleiss, Sun & Weinberger (2017), "On calibration of modern neural networks," *ICML* (temperature scaling). Platt is **pre-2015**; per-instance temperature is 2022+ (post-dates you conceptually only in ML framing).

**2. The estimation-error crossover — "noisy estimate can be worse than the default" (confidence: high, ~0.85 it's not novel; theorem-grade)**
- **Stein (1956)**, "Inadmissibility of the usual estimator for the mean of a multivariate normal distribution," *3rd Berkeley Symposium*; **James & Stein (1961)**, "Estimation with quadratic loss," *4th Berkeley Symposium* — the shrinkage/pooling estimator *dominates* the raw per-item estimate. This is the **foreclosed** part: it is a proven theorem that using the noisy individual estimate can be uniformly worse than a fixed/shrunk target. Your ~1.0 crossover is a manifestation of this, not a new discovery. **Pre-2015.**
- Efron & Morris (1975), "Data analysis using Stein's estimator…," *JASA* 70; Robbins (1956), "An empirical Bayes approach to statistics" — the applied/empirical-Bayes rendering. **Pre-2015.**
- **Forecast combination puzzle** — the tightest applied match to your "operating requirement": Smith & Wallis (2009), "A simple explanation of the forecast combination puzzle," *Oxford Bull. Econ. & Stats* 71(3):331–355; Timmermann (2006), "Forecast combinations," *Handbook of Economic Forecasting* ch. 4; Claeskens, Magnus, Vasnev & Wang (2016), "The forecast combination puzzle: a simple theoretical explanation," *IJF* 32(3):754–762. These show precisely that *the estimated parameter beats the fixed default only when its estimation variance is small enough*; otherwise the fixed default wins. Roots: Bates & Granger (1969); Clemen (1989) review. **Smith–Wallis, Timmermann, Bates–Granger, Clemen all pre-2015.**
- General framing: Geman, Bienenstock & Doursat (1992), "Neural networks and the bias/variance dilemma," *Neural Computation*. **Pre-2015.**

**3. The cold-start / fall-back-to-assumed-default framing (confidence: medium, ~0.65)**
- Schein, Popescul, Ungar & Pennock (2002), "Methods and metrics for cold-start recommendations," *SIGIR* — origin of "cold-start." **Pre-2015.**
- The "before you've resolved cases, you shrink to an *assumed* prior rather than a fitted one" is the empirical-Bayes-with-few-observations regime (Robbins 1956; Efron–Morris). Hedge: your specific pairing of *cold-start* with an *extremizing-parameter tolerance* under one banner may be locally novel packaging even though both ingredients are old.

## What might actually be yours (confidence: medium, ~0.6)

I did **not** find a published curve of "fraction of achievable proper-score gain retained vs. RMSE of the log scaling parameter," with your specific breakpoints, derived by injecting synthetic error. That parameterization — treating the *tolerance schedule itself* as the deliverable and characterizing it independent of any one estimator — reads as a concrete empirical contribution for your setting. **Hedge:** absence of a targeted hit is not absence of the result. The calibration literature on estimation error in temperature/extremizing parameters is exactly where an equivalent tolerance curve could already exist; I ran searches at the field-vocabulary level but did not exhaustively read those full texts, so I'd put only ~0.6 on "the schedule is genuinely unpublished."

## Verification caveat (honesty about method)

I confirmed each paper's **existence, authorship, venue, and topical claim** via multiple independent indexes (ScienceDirect, RePEc/IDEAS, JRSS/OUP, Wharton, arXiv) and secondary summaries, and I read the arXiv abstract of the Wang–Hyndman 50-year forecast-combination review directly. I could **not** open several primary PDFs — the Wharton "Two reasons" PDF, the UW Ranjan–Gneiting tech report, and the MDPI puzzle paper were blocked or returned empty under `safefetch` (JS-rendered / access-denied). So my confidence rests on abstract- and index-level verification, not a full read of each source. Per our usual bar, if you're going to lean on any single one in the write-up, the two I'd open and read in full first are **Satopää et al. 2014** (closest twin of the "multiplier") and **Smith & Wallis 2009** (closest twin of the "operating requirement").

## Recommendation for the write-up

Frame it as: *"We characterize the estimation-error tolerance (a bias–variance / forecast-combination-puzzle crossover, in the sense of Stein 1956 and Smith–Wallis 2009) for an extremizing/temperature-style coefficient (Satopää et al. 2014; Guo et al. 2017) in the cold-start, shrink-to-prior regime (Schein et al. 2002; empirical Bayes)."* Claim novelty only for the **specific schedule/measurement**, not for the concept. Do not call the concept an original contribution — a reviewer from forecasting, statistics, or ML calibration will recognize it immediately, and the Stein result means the "estimate can be worse than the default" direction is provably known, not a finding.

Sources:
- [Satopää et al. 2014 — simple logit model (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0169207013001635) · [RePEc/IDEAS record](https://ideas.repec.org/a/eee/intfor/v30y2014i2p344-356.html)
- [Ranjan & Gneiting 2010 — Combining probability forecasts (JRSS-B)](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9868.2009.00726.x) · [UW tech report TR543](https://stat.uw.edu/sites/default/files/files/reports/2008/tr543.pdf)
- [Baron et al. 2014 — Two reasons to make aggregated forecasts more extreme (ResearchGate)](https://www.researchgate.net/publication/275937752_Two_Reasons_to_Make_Aggregated_Probability_Forecasts_More_Extreme)
- [James–Stein estimator (Wikipedia overview + primary refs)](https://en.wikipedia.org/wiki/James%E2%80%93Stein_estimator) · [Stein's paradox explainer](https://towardsdatascience.com/steins-paradox-ba493f46e181/)
- [On the Forecast Combination Puzzle (MDPI Econometrics)](https://www.mdpi.com/2225-1146/7/3/39) · [Claeskens et al. 2016 puzzle explanation (Lirias PDF)](https://lirias.kuleuven.be/retrieve/9b3a6fad-89a2-4e68-8cc5-bad8316e305b) · [Wang, Hyndman, Li, Kang — 50-year forecast-combination review (arXiv)](https://arxiv.org/abs/2205.04216)
- [Guo et al. 2017 temperature scaling — adaptive/instance-wise follow-ups (arXiv 2207.06211)](https://arxiv.org/abs/2207.06211)
- [Bayesian ensembles: when to extremize or anti-extremize (arXiv 1705.02391)](https://arxiv.org/pdf/1705.02391)
- [Empirical Bayes shrinkage / cold-start behavior (ebnm vignette)](https://cran.r-project.org/web/packages/ebnm/vignettes/shrink_intro.html)
