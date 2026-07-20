## Bottom line

The description does not map onto a single, crisply-named theorem or standard term. What it describes is a **value-of-imperfect-information (break-even accuracy) analysis** applied to an estimated tuning parameter — and, given the specifics ("a multiplier that scales pooled evidence," Brier-type accuracy, error on the log scale, comparison against a fixed value), that tuning parameter is almost certainly the **extremizing coefficient** used in probability-forecast aggregation. The "concept" is really an intersection of four established ideas, dressed as an operational spec. I'll name each, and I'll be explicit that the exact packaged artifact (the 0.3 → ~85%, 0.6 → ~50%, >1.0 → harmful *schedule*, derived by synthetic-noise injection) reads as a **bespoke sensitivity analysis**, not a canonically-named result.

## 1. What it's called in established fields

No one standard name covers the whole thing. The closest established names, by component:

- **Value of imperfect / sample information (VoI, EVII/EVSI)** — decision theory. This is the "how good must a measurement be before using it beats not using it" idea, including the break-even point. Crucially, standard VoI is *non-negative because you can ignore the signal*; the moment you are **forced to plug the noisy estimate into the pipeline instead of falling back on a constant**, the value of that information can go **strictly negative** — which is exactly your "beyond ~1.0 the estimator is actively harmful." That constrained-VoI-can-be-negative result is the precise theoretical hook. *(High confidence this is the governing concept; medium confidence on which sub-label a given author would use.)*
- **Skill / skill score** — forecast verification. Your output ("fraction retained of the maximum achievable improvement over a fixed reference") is the definition of a **Brier Skill Score**, BSS = 1 − B/B_ref, where B_ref is a reference forecast. Your "fixed value fit to already-resolved cases" is the reference/climatology; your "merely assumed value" is a naïve reference. *(High confidence.)*
- **Bias–variance / shrinkage (Stein) rationale** — estimation theory. "A noisy per-case estimate can be beaten by a single fixed constant" is the Stein/shrinkage phenomenon; "noise manufactures unwarranted confidence" is the variance term degrading calibration. *(High confidence this is the mechanism; it's the *why*, not a name for your spec.)*
- **The object being tuned: the "extremizing coefficient" / "extremization parameter" / "systematic extremizing factor"** in judgmental forecast aggregation — the multiplier applied to pooled (summed/averaged log-odds) evidence, pushing the aggregate toward 0/1. This is what "a multiplier that scales pooled evidence" denotes, and measuring its error on the **log scale** is natural because it is multiplicative. *(High confidence on the identification; this is the domain instantiation.)*

A useful cousin worth flagging: in clinical prediction, **decision-curve analysis / net benefit** (Vickers & Elkin 2006) formalizes the same "is using this predictor better than a fixed default strategy?" question — your "the benchmark must be named" condition — though its object is a decision threshold, not an evidence multiplier. *(Medium confidence it's a deliberate parallel vs. coincidental.)*

## 2. Fields that own it

- **Decision analysis / decision theory** (value of information; imperfect information having negative value under forced action).
- **Statistics — forecast verification & proper scoring rules** (Brier score, skill scores, calibration/sharpness).
- **Estimation theory** (bias–variance tradeoff, shrinkage / Stein estimation).
- **Applied subfield: judgmental forecasting / forecast aggregation** (extremizing), where all of the above are combined.

## 3. Oldest and most canonical treatments (with real citations)

Value of information:
- **Raiffa, H., & Schlaifer, R. (1961).** *Applied Statistical Decision Theory.* Harvard Business School — preposterior analysis / value of sample (imperfect) information.
- **Howard, R. A. (1966).** "Information Value Theory." *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 22–26.

Scoring / skill:
- **Brier, G. W. (1950).** "Verification of forecasts expressed in terms of probability." *Monthly Weather Review*, 78(1), 1–3.
- **Murphy, A. H. (1973).** "A new vector partition of the probability score." *Journal of Applied Meteorology*, 12(4), 595–600 — the reliability/resolution/uncertainty decomposition and the "achievable improvement over a base-rate reference" framing behind skill scores.
- **Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007).** "Probabilistic forecasts, calibration and sharpness." *JRSS-B*, 69(2), 243–268 — the calibration-vs-sharpness lens ("noise manufacturing unwarranted confidence"). *(Post-2015? No — 2007. Included as canonical for the calibration angle.)*

Shrinkage (why a constant can beat a noisy estimate):
- **Stein, C. (1956)** / **James, W., & Stein, C. (1961).** "Estimation with quadratic loss." *Proc. 4th Berkeley Symposium*, 361–379.

The extremizing multiplier itself (the domain instantiation):
- **Satopää, V. A., Baron, J., Foster, D. P., Mellers, B. A., Tetlock, P. E., & Ungar, L. H. (2014).** "Combining multiple probability predictions using a simple logit model." *International Journal of Forecasting*, 30(2), 344–356 — the single tuning parameter that shifts pooled log-odds toward the extremes.
- **Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., & Ungar, L. H. (2014).** "Two Reasons to Make Aggregated Probability Forecasts More Extreme." *Decision Analysis*, 11(2), 133–145.

Parallel (test/measurement usefulness vs. a default):
- **Vickers, A. J., & Elkin, E. B. (2006).** "Decision curve analysis: a novel method for evaluating prediction models." *Medical Decision Making*, 26(6), 565–574.

## 4. Confidence and hedges

- **High confidence:** the operational description is about **estimating an evidence-pooling multiplier (extremizing coefficient) in probability forecasting**, and it is fundamentally a **value-of-(imperfect)-information / break-even-accuracy** statement expressed as a **skill curve**, with the harm-past-a-threshold behavior explained by **bias–variance/shrinkage** and calibration.
- **Explicitly uncertain / my main hedge:** I could **not** find a single established academic name for the exact packaged specification you describe — the quantitative *schedule* (≈0.3 → ~85% of gain, ≈0.6 → ~half, >~1.0 → net-harmful) keyed to the **RMSE-of-log** of the estimate and **established by injecting synthetic errors rather than running any estimator**. That methodology (characterizing an *error level*, not a method) and those specific numbers look like a **bespoke sensitivity / value-of-information analysis** from one particular source, not a named, citable theorem. If you have the source, I'd expect it to *use* the vocabulary above rather than introduce a new standard term. I searched actively and did not locate a canonical named result matching the schedule; treat "there is one standard name for this" as **unsupported**.
- **Lower confidence:** whether the intended object is specifically extremizing versus another multiplicative pooling weight (e.g., a variance-inflation/temperature-type factor). The forecast-aggregation reading fits best because the accuracy metric is a probability-forecast score (Brier), but I can't rule out a neighboring instantiation.

Sources:
- [Satopää et al. 2014, IJF (RePEc)](https://ideas.repec.org/a/eee/intfor/v30y2014i2p344-356.html)
- [Baron et al. 2014, "Two Reasons…", Decision Analysis](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293) · [author PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---two-reasons-to-make-aggregated-probability-forecasts_1.pdf)
- [Howard 1966, "Information Value Theory" (PDF)](https://www.scribd.com/document/320139530/Howard-1966-Information-Value-Theory)
- [Value of information — Wikipedia (VoI can be negative under forced action)](https://en.wikipedia.org/wiki/Value_of_information) · [Value of Imperfect Information (TreePlan)](https://treeplan.com/wp-content/uploads/value-of-imperfect-information.pdf)
- [Brier score / Brier Skill Score — Wikipedia](https://en.wikipedia.org/wiki/Brier_score)
- [Simplifying and generalising Murphy's Brier score decomposition (PDF)](https://ore.exeter.ac.uk/articles/journal_contribution/Simplifying_and_generalising_Murphy_s_Brier_score_decomposition/29748851/1/files/56771708.pdf)
- [Recalibrating probabilistic forecasts to improve their accuracy — JDM](https://www.sas.upenn.edu/~baron/journal/21/210914/jdm210914.html)
