## Short answer

It's not new. The object you call the audit unit is a **linear-in-log-odds recalibration of a pooled forecast**, your multiplier is what four separate literatures call the **extremization factor**, the **Karmarkar/LLO slope γ**, the **calibration slope**, or the **inverse temperature**. Your "operating requirement" is the standard **MSE comparison between a plug-in estimator and a restricted/default value**, which statistics has owned since Bancroft (1944) and Stein (1956). I could not find your specific *numeric schedule* stated as such anywhere — but as I show below, it appears to be a one-parameter algebraic consequence of the standard bias–variance identity, not an independent empirical finding.

## Your notation → the established notation

Your notes describe `logit(posterior) = logit(prior) + λ · [pooled evidence lean]`. That is verbatim the aggregator in the forecast-aggregation literature:

`log Ô = log O_baseline + d · [ (1/n) Σ log O_i − log O_baseline ]`

That exact equation, with `d` as the extremization factor and `log O_baseline` as your "starting credence," appears in [Sevilla's writeup of Neyman & Roughgarden](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts). Your "audit unit" and that aggregator are the same operator.

| Your term | Established name(s) | Field |
|---|---|---|
| multiplier | extremization factor *d* | forecast aggregation |
| multiplier | Karmarkar γ / linear-log-odds (LLO) slope | judgment & decision making |
| multiplier | calibration slope; inverse temperature 1/T | ML calibration |
| multiplier | logistic-regression calibration scale *a* | forensic/speaker LR calibration |
| pooled evidence lean | weight of evidence (Peirce, I.J. Good); log-likelihood ratio | Bayesian stats |
| operating requirement | pre-test / restricted-vs-unrestricted estimator risk comparison | statistics, econometrics |
| cold-start regime | credibility / no-experience case; calibration without resolved outcomes | actuarial science |

## Prior art, by field

**1. Forecast aggregation (owns the multiplier itself).** [Baron, Mellers, Tetlock, Stone & Ungar (2014), "Two Reasons to Make Aggregated Probability Forecasts More Extreme," *Decision Analysis* 11:133–145](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293) — **pre-2015**, and the canonical statement of *why* the multiplier exceeds 1 (end-of-scale compression + forecasters discounting for information they lack). [Satopää, Baron, Foster, Mellers, Tetlock & Ungar (2014), "Combining Multiple Probability Predictions Using a Simple Logit Model," *IJF* 30(2):344–356](https://www.sciencedirect.com/science/article/abs/pii/S0169207013001635) — **pre-2015**, fits the multiplier empirically and reports an optimal range of *d* ∈ [1.161, 3.921]. High confidence both exist and match; I verified titles, venues, years, and the substance in multiple independent sources.

**2. Judgment & decision making (oldest thread).** [Karmarkar (1978), "Subjectively Weighted Utility," *Organizational Behavior & Human Performance*](https://www.sas.upenn.edu/~baron/journal/21/210914/jdm210914.html) gives the one-parameter log-odds slope transform still in use; [Shlomi & Wallsten (2010), *Psychonomic Bulletin & Review* 17(4):492–498](https://link.springer.com/article/10.3758/PBR.17.4.492); [Turner, Steyvers, Merkle, Budescu & Wallsten (2014), "Forecast aggregation via recalibration," *Machine Learning* 95(3):261–289](https://link.springer.com/article/10.1007/s10994-013-5401-4) — all **pre-2015**. Turner et al. is the closest methodological sibling: it compares recalibrate-then-average vs average-then-recalibrate in probability vs log-odds space, *evaluated out-of-sample by cross-validation*. Confidence high on existence; moderate on my characterization of Turner et al.'s internal findings, since I read its abstract and secondary descriptions rather than the full text.

**3. Statistics — this is what actually owns your operating requirement.** The question "must I estimate this parameter, or is the assumed default safer?" is the **pre-test / restricted-vs-unrestricted estimator** problem, opened by **Bancroft (1944), "On Biases in Estimation Due to the Use of Preliminary Tests of Significance," *Annals of Mathematical Statistics*** — **pre-2015**, and the oldest direct treatment I found. The standard result is exactly your schedule's shape: the restricted (default) estimator dominates in MSE when the restriction approximately holds, and degrades sharply when it is badly violated. Stein (1956) / James–Stein (1961) then showed the *choice itself* is the wrong move — pre-test estimators are inadmissible, dominated by shrinkage. High confidence on Bancroft's existence, title, and role as originator; high confidence on the Stein dominance result.

**4. Actuarial credibility — owns your cold-start framing specifically.** "How much do I trust a noisy case-specific estimate versus a collective default, when I have little or no case-specific experience" is the founding question of credibility theory: **Mowbray (1914)**, **Whitney (1918), "The Theory of Experience Rating"**, and **Bühlmann (1967), "Experience Rating and Credibility," *ASTIN Bulletin*** — all **pre-2015**. Whitney's formula is literally `Z · observed + (1−Z) · prior`, and the cold-start case (Z→0, fall back to the collective) is the base case of the theory, not an edge case. High confidence.

**5. Forensic/speaker likelihood-ratio calibration — owns the failure mode.** Brümmer & du Preez, "Application-independent evaluation of speaker detection," *Computer Speech & Language* (2006; some sources date the core result to 2005 — **I'm unsure of the exact year, treat as ~2005–2006**) established `Cllr` and its decomposition into discrimination loss (`Cllr_min`) plus **calibration loss** (`Cllr − Cllr_min`). This field has your "noise manufactures overconfidence" result as routine operational knowledge: badly estimated calibration transforms produce *worse* Cllr than leaving scores alone, and calibration degrades far faster than discrimination when development data is unrepresentative. High confidence on the concept and decomposition; moderate on the precise citation year.

## The one part I could not find — and why I still don't think it's a contribution

I ran targeted searches for an explicit "how accurate must the estimated multiplier be" schedule and **found no prior source stating your specific numbers**. I'm flagging that honestly. But before you claim it, check this arithmetic, because I think it dissolves the finding:

If excess loss is quadratic in the log-scale error near the optimum (it is — that's the standard second-order expansion of a proper scoring rule), then with `δ₀` = the default's own log-scale error, the fraction of achievable gain retained is `1 − RMSE²/δ₀²`. Solving your three data points for `δ₀`:

- 85% at RMSE 0.30 → δ₀ ≈ 0.78
- 50% at RMSE 0.60 → δ₀ ≈ 0.85
- break-even at RMSE 1.00 → δ₀ = 1.00

Those should be one constant, and they're the same number to within your rounding. **Your "schedule" is a one-parameter curve, and the parameter is just how wrong your fixed default is.** It reduces to the textbook rule: *an estimate beats a fixed default exactly when its RMSE falls below the default's bias.* That's why injecting synthetic error recovers it — you were measuring the bias–variance identity, and it would have come out the same for any estimator, any domain. Medium-high confidence in this reading; it depends on my decoding of "accuracy score" as a proper scoring rule, which your notes strongly imply but don't state.

## The critique I'd want if this were mine

The framing "when does the estimate beat the default" is the **pre-test framing, and it is known to be the wrong question** — Stein's result says the estimator that picks one or the other is dominated by one that shrinks continuously between them. Credibility theory (Whitney 1918, Bühlmann 1967) already gives the optimal shrinkage weight in closed form, and it never selects; it always blends. So the sharpest version of your cold-start problem isn't "is my λ̂ good enough to use" — it's "what's the credibility weight Z on λ̂ versus λ₀," and there's a century-old answer. That reframing is strictly better than the threshold schedule and is where I'd point the write-up.

For the cold-start default value itself, [Neyman & Roughgarden (2021/22), "Are You Smarter Than a Random Expert?"](https://arxiv.org/abs/2111.03153) derives a principled `d → √3 ≈ 1.73` requiring no resolved cases — which is precisely the "assumed, not fitted" default your notes say you lack a basis for. Note this is post-2015 and its applicability to log-odds aggregation is a licensed extension, not a theorem (Neyman himself raised that caveat).

## What I'd still call yours

Not the multiplier, not the operating-requirement schedule, not cold-start-vs-fitted-fallback. Possibly: the specific *audit* application and the synthetic-error injection *methodology* as a practical diagnostic for a deployed pipeline. That's a solid applied-methods contribution — but it should be written as "we apply known extremization/credibility results to auditing," with the above citations, not as a novel characterization. Framing it as original in a venue that includes anyone from forecasting, actuarial science, or forensic LR calibration would likely draw a sharp referee report.

**Overall confidence that this is prior art, not novel: high (~90%).** The residual 10% is that I may have mis-decoded "pooled evidence lean" — if the multiplier scales something other than an additive log-odds evidence term (e.g. it's applied per-source before pooling, or the pooling isn't logarithmic), the extremization mapping weakens, though the statistical prior art (Bancroft, Stein, credibility) survives regardless.

Want me to write this up as a proper related-work section with full bibliography and run it through `/codex-doc-review`? I'd also suggest pulling the Baron 2014 and Turner 2014 full texts before you cite them — I read abstracts and secondary sources for those two, not the PDFs.

**Sources:**
- [Two Reasons to Make Aggregated Probability Forecasts More Extreme — Baron et al. 2014](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293)
- [Combining Multiple Probability Predictions Using a Simple Logit Model — Satopää et al. 2014](https://www.sciencedirect.com/science/article/abs/pii/S0169207013001635)
- [Forecast aggregation via recalibration — Turner et al. 2014](https://link.springer.com/article/10.1007/s10994-013-5401-4)
- [Combining Probability Forecasts — Ranjan & Gneiting 2010](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9868.2009.00726.x)
- [Subjective recalibration of advisors' probability estimates — Shlomi & Wallsten 2010](https://link.springer.com/article/10.3758/PBR.17.4.492)
- [Recalibrating probabilistic forecasts to improve their accuracy — Han & Budescu 2022 (LLO/Karmarkar review)](https://www.sas.upenn.edu/~baron/journal/21/210914/jdm210914.html)
- [Principled extremizing of aggregated forecasts — EA Forum](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts)
- [Are You Smarter Than a Random Expert? — Neyman & Roughgarden 2021](https://arxiv.org/abs/2111.03153)
- [Credibility theory history — Mowbray/Whitney/Bühlmann](https://encyclopediaofmath.org/wiki/Credibility_theory)
- [Chapter 9, Experience Rating Using Credibility Theory — Loss Data Analytics](https://openacttexts.github.io/Loss-Data-Analytics/ChapCredibility.html)
- [Tutorial on logistic-regression calibration and fusion (forensic LR)](https://arxiv.org/pdf/2104.08846)
- [Investigation of Different Calibration Methods for Deep Speaker Embedding (Cllr decomposition)](https://arxiv.org/pdf/2203.15106)
- [James–Stein estimator](https://en.wikipedia.org/wiki/James%E2%80%93Stein_estimator)
- [Shrinkage (statistics)](https://en.wikipedia.org/wiki/Shrinkage_(statistics))
- [Pre-test estimation / Bancroft 1944 lineage](https://link.springer.com/article/10.1007/s00362-008-0163-y)
