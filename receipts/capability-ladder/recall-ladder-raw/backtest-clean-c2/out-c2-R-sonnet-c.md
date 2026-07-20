## Findings

I ran an extensive search (16+ distinct queries plus full-text fetches of the strongest candidate papers) across every domain that plausibly fits this description, and I want to be direct: **I could not pin the specific quantitative schedule (RMSE-of-log < 0.3 → ~85% retained; 0.6 → ~50%; >1.0 → harmful) to any citable, verifiable source.** I'm reporting what I found and did not find, rather than force-fitting a confident answer.

### 1–2. Candidate name and field (moderate confidence, not confirmed)

The qualitative structure — a scaling factor applied to *aggregated/pooled* probabilistic evidence, that can be estimated per-case or fixed globally, evaluated by Brier score, benchmarked against either an empirically-fit constant (from resolved cases) or a merely assumed one — maps most closely onto **"extremizing" in probabilistic forecast aggregation**, a concept in the **judgment-and-decision-making / forecasting literature** (management science, decision analysis, applied statistics). There, a multiplicative factor is applied to the log-odds of a pooled/averaged forecast to correct for underconfidence, and there is real published debate about whether that factor should be estimated per-question or fixed, and about the risk of it doing harm when misestimated.

I checked this hypothesis against the primary literature and it does **not** contain the specific numeric schedule in the prompt:
- Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., & Ungar, L. H. (2014). "Two Reasons to Make Aggregated Probability Forecasts More Extreme." *Decision Analysis*, 11(2), 133–145. (pre-2015, canonical)
- Satopää, V. A., Baron, J., Foster, D. P., Mellers, B. A., Tetlock, P. E., & Ungar, L. H. (2014). "Combining Multiple Probability Predictions Using a Simple Logit Model." *International Journal of Forecasting*, 30(2), 344–356. (pre-2015, canonical)
- Neyman, E., & Roughgarden, T. (2021). "Are You Smarter Than a Random Expert? The Robust Aggregation of Substitutable Signals." arXiv:2111.03153. (theoretical grounding for choosing the factor)
- Sevilla, J. (2021). "Principled Extremizing of Aggregated Forecasts." EA Forum. (closest match to the puzzle's *structure* — discusses a factor fit to historical resolved questions vs. an assumed baseline — but still no matching numeric table)

I also explicitly checked and ruled out several other domains that share the same abstract shape (an estimated multiplier vs. a fixed fallback, evaluated on binary-outcome accuracy):
- Meta-analysis heterogeneity/shrinkage (tau²) — doesn't use Brier score as its standard metric.
- Weather-ensemble spread-inflation factors — Brier score is standard there, and "injecting synthetic errors" is a real methodology (OSSE-style), but I found no matching schedule.
- Actuarial credibility theory (Bühlmann credibility factor) — same estimate-vs-fixed structure, no Brier-score-based schedule found.
- Polygenic risk score shrinkage (GCTA-SBLUP's λ = m(1/h²−1), derived from a heritability estimate) — a very close structural match (a multiplier scaling pooled/meta-analyzed GWAS evidence), and I fetched a 2026 benchmarking paper on this directly (arXiv:2604.02394) — it uses AUC, not Brier score or RMSE-of-log, and reports no such schedule.

### 3. Canonical citations
Given above — real, verifiable, and at least two predate 2015 as requested. I cannot offer a citation for the schedule itself because I never found it.

### 4. Confidence
- That this is describing *some* form of the general statistical idea "an estimator must clear an accuracy bar to beat a fixed/naive baseline" — **high confidence**, it's a coherent, well-posed statistical question.
- That the specific worked example ("multiplier scaling pooled evidence") is drawn from the forecast-extremizing literature specifically — **low-to-moderate confidence**; it's my best-supported guess, not a confirmed match.
- That the exact schedule (0.3/0.6/1.0 → 85%/50%/harmful) traces to a real citable source — **not confirmed**. I flag this as unresolved rather than guess a citation I can't stand behind.

If you have the original source text (a paper, blog post, or internal document) this was paraphrased from, sharing it would let me confirm this quickly rather than continue searching blind.
