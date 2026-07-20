## Identification

**1. Standard name(s)**

This is the **extremizing (or "extremization") transformation of aggregated/pooled probability forecasts**, applied to the **log-odds** (logit) of a pooled forecast. The general form is:

log-odds(final) = log-odds(baseline) + *d* · [log-odds(pooled evidence) − log-odds(baseline)]

where *d* is the **extremizing factor** (your "multiplier") and the bracketed term is exactly what the prompt calls the "pooled evidence lean." Using a fixed, pre-chosen *d* vs. an estimated, question-specific *d* is a live methodological debate in this literature — which is what the "operating requirement" (how accurately must you estimate *d* per-question before it beats a fixed default) is about. — **Confidence: high** that this is extremizing/log-odds pooling; the "audit unit" / cold-start / RMSE-of-log-multiplier framing in the prompt is a paraphrase I could not trace to a specific named framework (see caveat below).

**2. Field(s) that own it**

Judgment and decision-making / psychology of forecasting, and statistical forecast aggregation — chiefly the "**wisdom of crowds**" and **geopolitical forecasting tournament** research tradition (Good Judgment Project / IARPA ACE program), with a supporting statistics literature on combining probability forecasts (opinion pooling). — **Confidence: high.**

**3. Oldest / most canonical treatments**

- **Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., & Ungar, L. H. (2014).** "Two Reasons to Make Aggregated Probability Forecasts More Extreme." *Decision Analysis*, 11(2), 133–145. https://doi.org/10.1287/deca.2014.0293 — the founding empirical/conceptual justification for extremizing pooled forecasts. **Confidence: high** (verified via the Wharton faculty PDF and the EA Forum bibliography).
- **Satopää, V. A., Baron, J., Foster, D. P., Mellers, B. A., Tetlock, P. E., & Ungar, L. H. (2014).** "Combining Multiple Probability Predictions Using a Simple Logit Model." *International Journal of Forecasting*, 30(2), 344–356. https://doi.org/10.1016/j.ijforecast.2013.09.009 — derives an empirically fitted extremizing factor (found optimal *d* ∈ [1.161, 3.921] on Good Judgment Project data) and is the paper most concerned with *how well you can estimate the extremizing parameter*, which is the closest canonical antecedent to the "operating requirement" idea in your prompt. **Confidence: high** (both papers pre-2015, satisfying your requirement).
- A more recent theoretical grounding — **Neyman, E., & Roughgarden, T. (2021).** "Are You Smarter Than a Random Expert? The Robust Aggregation of Substitutable Signals." arXiv:2111.03153 (later ACM EC 2022) — derives a principled extremizing factor as a function of the number of forecasters *n*, and is discussed at length, with worked formulas and a Metaculus validation, in Jaime Sevilla's EA Forum post "**Principled Extremizing of Aggregated Forecasts**" (2021), which is a good secondary/applied source for the tradeoffs around fixed vs. estimated extremizing factors. **Confidence: medium-high** on relevance, but this is 2021/post-2015, so it does not itself satisfy your "before 2015" ask — it supplements, not replaces, the two 2014 papers above.

**4. Confidence and explicit hedge**

I am confident in points 1–3 as an identification of the *general statistical mechanism* being described (extremizing/log-odds-multiplier aggregation) and in the citations given. I am **not confident** about the specific packaging in your prompt: the terms "audit unit," "cold-start operating requirement," and the precise numeric schedule (RMSE of log-multiplier ≈0.3 → ~85% of achievable gain retained; ≈0.6 → ~50%; >~1.0 → net negative vs. fixed default) did not surface in any source I could find across roughly a dozen targeted searches (forecasting-aggregation literature, EA Forum/LessWrong epistemics writing, and AI-control/monitoring literature such as Redwood Research's work, where "audit" is also a term of art). That specific schedule reads like it comes from a synthetic-noise-injection sensitivity analysis — plausible as an appendix/robustness-check in the Satopää et al. or Neyman–Roughgarden line of work, or as an applied/internal writeup (e.g., calibrating an LLM forecasting system) — but I could not locate or verify the actual source, so I'm flagging that piece as **unconfirmed** rather than asserting a citation for it.

Sources:
- [Two Reasons to Make Aggregated Probability Forecasts More Extreme (Baron et al. 2014, PDF)](https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---two-reasons-to-make-aggregated-probability-forecasts_1.pdf)
- [Combining Multiple Probability Predictions Using a Simple Logit Model (Satopää et al. 2014)](https://www.sciencedirect.com/science/article/abs/pii/S0169207013001635)
- [Are You Smarter Than a Random Expert? (Neyman & Roughgarden 2021)](https://arxiv.org/abs/2111.03153)
- [Principled Extremizing of Aggregated Forecasts — EA Forum (Sevilla, 2021)](https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe/principled-extremizing-of-aggregated-forecasts)
- [Combining and Extremizing Real-Valued Forecasts (Satopää et al.)](https://arxiv.org/pdf/1506.06405)
- [Combining Probability Forecasts and Understanding Probability Extremizing through Information Diversity](https://arxiv.org/pdf/1501.06943)
- [Alignment Problems With Current Forecasting Platforms](https://arxiv.org/pdf/2106.11248)
