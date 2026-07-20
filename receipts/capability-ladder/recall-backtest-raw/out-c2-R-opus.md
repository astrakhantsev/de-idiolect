I've identified the concept with high confidence. Here is my report.

## Bottom line up front

What you've described is **not a single named theorem with a standard textbook label**. It is a bespoke engineering *specification* (the specific "0.3 → 85% / 0.6 → 50% / 1.0 → harmful" schedule is almost certainly project-local, not canonical) that is an instance of **three well-established concepts that meet at exactly this point**: (1) **forecast skill / skill scores relative to a reference forecast** from forecast-verification theory; (2) the statistical-decision-theory question of **when a noisy plug-in estimator is dominated by a fixed constant** — i.e. *estimation risk*, cured by *shrinkage / empirical-Bayes partial-vs-complete pooling*; and (3) **value of information / "do-no-harm" net benefit**. I'll take each of your four questions in turn.

---

### 1. What is this concept called?

There is no one term that packages the whole thing, but each moving part has a standard name:

- **The output metric — "fraction retained of the maximum achievable improvement, measured by a proper accuracy measure for probability forecasts."** This is a **skill score**, specifically a **Brier skill score (BSS)** form: `(S_ref − S) / (S_ref − S_perfect)`. Your "standard accuracy measure for probability forecasts" is the **Brier score** (a *proper scoring rule*). "Beyond ~1.0 the estimator is actively harmful → worse than the fallback" is exactly **negative skill**. *(High confidence — this is the tightest match to what you described.)*

- **The benchmark language.** "A fixed value chosen by fitting to already-resolved cases" is, in verification vocabulary, the **climatology reference forecast** (the base-rate/unconditional forecast). Comparing a forecast to climatology is *the* canonical skill baseline; when there are no resolved outcomes to fit, you fall back to an **assumed / naive reference forecast**. *(High confidence.)*

- **The input — "RMSE of the log of the estimate vs. its truth," and the finding that a noisy estimate is worse than a constant.** In statistics this is **estimation risk** and the **bias–variance tradeoff**: a data-driven **plug-in estimator** can be **dominated by a fixed constant** when its variance is too large. The "estimate per case *or* use one fixed value for all cases" dichotomy is precisely **no-pooling vs. complete pooling**, and the principled middle ground is **shrinkage / partial pooling (empirical Bayes / James–Stein)**. Your "noise manufactures unwarranted confidence" is the classic **overconfidence / miscalibration-from-estimation-error** phenomenon (excess *sharpness* without *calibration*). *(High confidence.)*

- **The overall "how good must it be before it's worth using at all" framing.** This is the spirit of **value of information (VoI)** in decision analysis, and — in the clinical-prediction world, where "better than not using it at all" is the literal test — **net benefit / decision curve analysis** (a model must beat the default "treat-all/treat-none" strategies or it has negative net benefit). *(Medium confidence these are the intended frame — they capture "worth using vs. not," but their native metrics (EVPI, net benefit) are not the Brier-retained-gain schedule you described, so they are analogies rather than the exact object.)*

- **The methodology — "inject synthetic errors of a given size rather than run any particular estimator."** That is a **Monte-Carlo sensitivity / perturbation (noise-injection / degradation) analysis**; characterizing an *error level* rather than a *method* is standard in such studies. *(High confidence on the description; "noise-injection study" is a descriptive label, not a proper noun.)*

A note on "a multiplier that scales pooled evidence": that object is most likely an **extremizing / tempering / evidence-pooling weight** (a scalar applied to aggregated log-odds or pooled evidence, à la temperature scaling / logarithmic opinion pooling). Your question is about the *accuracy-threshold specification*, not the multiplier, so I keep the focus there — but flag this in case it points you to the source domain.

### 2. Which field(s) own it?

No single owner; it sits at the intersection of:

- **Forecast verification / probabilistic forecasting** (atmospheric science, and now ML calibration) — this owns the *output* vocabulary (proper scoring rules, Brier/skill scores, climatology reference, calibration vs. sharpness). If I had to name the one field whose vocabulary most exactly matches the described object, it's this one.
- **Statistical decision theory / Bayesian statistics** — owns the *input/logic* (estimation risk, admissibility/domination, shrinkage, empirical Bayes, partial-vs-complete pooling).
- **Decision analysis / health economics & clinical prediction** — owns the *"worth using at all"* framing (value of information; net benefit / decision curve analysis).

### 3. Oldest and most canonical treatments (verified citations)

Proper scoring rules & forecast skill (pre-2015):
- **Brier, G. W. (1950).** "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review* 78(1): 1–3. — origin of the Brier score. *(Verified.)*
- **Murphy, A. H. (1973).** "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology* 12(4): 595–600. — the reliability/resolution/uncertainty decomposition; formalizes skill relative to the climatology (uncertainty) term. *(Verified.)*
- **Gneiting, T. & Raftery, A. E. (2007).** "Strictly Proper Scoring Rules, Prediction, and Estimation." *Journal of the American Statistical Association* 102(447): 359–378. — the modern reference for proper scoring rules. *(Verified.)*
- **Gneiting, T., Balabdaoui, F. & Raftery, A. E. (2007).** "Probabilistic Forecasts, Calibration and Sharpness." *JRSS Series B* 69(2): 243–268. — the calibration-vs-sharpness framing behind "noise manufactures unwarranted confidence." *(High confidence; not re-fetched this session — treat exact page numbers as *uncertain*.)*

When a noisy estimate is worse than a constant — shrinkage / estimation risk (pre-2015):
- **James, W. & Stein, C. (1961).** "Estimation with Quadratic Loss." *Proc. 4th Berkeley Symposium* 1: 361–379. — the naive per-case estimator is inadmissible; a shrunken estimator dominates. *(High confidence; standard citation, not re-fetched.)*
- **Efron, B. & Morris, C. (1975).** "Data Analysis Using Stein's Estimator and Its Generalizations." *JASA* 70(350): 311–319. — the applied empirical-Bayes / partial-pooling treatment. *(High confidence; not re-fetched.)*
- **DeMiguel, V., Garlappi, L. & Uppal, R. (2009).** "Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy?" *Review of Financial Studies* 22(5): 1915–1953. — the canonical *applied* demonstration that an *estimated/optimized* setting loses to a *fixed default* once estimation error is accounted for; the closest published analogue to your "beyond error X, the estimate is harmful." *(Verified.)*

Value of information / net benefit (pre-2015):
- **Raiffa, H. & Schlaifer, R. (1961).** *Applied Statistical Decision Theory.* Harvard. — origin of expected value of (perfect) information. *(High confidence; not re-fetched.)*
- **Howard, R. A. (1966).** "Information Value Theory." *IEEE Transactions on Systems Science and Cybernetics* 2(1): 22–26. *(High confidence; not re-fetched.)*
- **Vickers, A. J. & Elkin, E. B. (2006).** "Decision Curve Analysis: A Novel Method for Evaluating Prediction Models." *Medical Decision Making* 26(6): 565–574. — "a model has value only when it beats the default of not using it." *(Verified title/authors/venue; page numbers from memory — *slightly uncertain*.)*

### 4. Confidence and hedges

- **High confidence:** the described object is a **skill-score / forecast-verification framing** of an **estimate-vs-fixed-default** comparison, and simultaneously an instance of **estimation risk / shrinkage (no-pooling vs complete pooling)**. The Brier (1950), Murphy (1973), Gneiting–Raftery (2007), and DeMiguel et al. (2009) citations are verified this session and I stand behind them.
- **High confidence** there is **no standard canonical name** for the *specific packaged schedule* (the 0.3/0.6/1.0 → 85%/50%/harmful numbers). That reads as a **project-specific specification** (consistent with your "recall-backtest" working context), not a named result. I cannot prove a negative, so: *no established term found* rather than *no term exists*.
- **Medium confidence** that **value of information** and **decision curve analysis / net benefit** are the intended "worth using at all" frame — they match the *prose* ("better than not using it") but not the *metric* (Brier-retained-gain), so I offer them as adjacent, not identical.
- **Uncertain / from memory (not re-fetched):** the exact page numbers for Gneiting–Balabdaoui–Raftery (2007), James–Stein (1961), Efron–Morris (1975), Raiffa–Schlaifer (1961), Howard (1966), and Vickers–Elkin (2006). Author/year/venue for all are solid; verify pagination before quoting.
- I could **not** find any single source that presents your exact "error-of-log → fraction-of-Brier-gain-retained, benchmarked against oracle-climatology, established by noise injection" construct as a named, off-the-shelf concept. My honest read: it's a **legitimate synthesis** of the above, likely authored for your pipeline, best described as *"a minimum-accuracy (break-even) specification for a plug-in tuning-parameter estimator, expressed as a Brier skill-score retention curve versus estimator log-RMSE, benchmarked against a climatology oracle."*

Sources:
- [Brier score — Wikipedia scoring rule page (Brier 1950, Murphy 1973, Gneiting–Raftery 2007 footnotes)](https://en.wikipedia.org/wiki/Scoring_rule)
- [Murphy (1973), "A New Vector Partition of the Probability Score," J. Appl. Meteorol.](https://journals.ametsoc.org/view/journals/apme/12/4/1520-0450_1973_012_0595_anvpot_2_0_co_2.xml)
- [On Using "Climatology" as a Reference Strategy in the Brier and Ranked Probability Skill Scores, Mon. Wea. Rev. (2004)](https://journals.ametsoc.org/view/journals/mwre/132/7/1520-0493_2004_132_1891_oucaar_2.0.co_2.xml)
- [Brier Skill Score overview](https://www.emergentmind.com/topics/brier-skill-score)
- [DeMiguel, Garlappi & Uppal (2009), "Optimal Versus Naive Diversification," Rev. Financ. Stud.](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901)
- [Vickers & Elkin (2006), "Decision Curve Analysis," Medical Decision Making](https://journals.sagepub.com/doi/10.1177/0272989X06295361)
- [Value of Information Analysis (dampack / EVPI–EVSI)](https://cran.r-project.org/web/packages/dampack/vignettes/voi.html)
- [Value of Information Analysis introduction (ISPOR Task Force, Value in Health)](https://www.valueinhealthjournal.com/article/S1098-3015(20)30027-9/fulltext)
- [Hierarchical partial pooling / shrinkage (PyMC example gallery)](https://www.pymc.io/projects/examples/en/latest/case_studies/hierarchical_partial_pooling.html)
- [Understanding the Risks and Rewards of Combining Unbiased and Possibly Biased Estimators (arXiv)](https://arxiv.org/pdf/2205.10467)
