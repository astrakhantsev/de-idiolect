Working through each of these as an aggregation/decision-theory puzzle rather than a literature lookup (I have no browsing available), so treat citation years/venues below as best-recollection, not verified quotes.

## CONCEPT-1: breakeven multiplier in logit-linear evidence pooling

**1. Canonical term(s).** The overall machinery — averaging per-source log-odds "leans" and adding a scaled sum to a prior logit — is what the forecasting-aggregation literature calls **logit-linear pooling / "extremizing"** (λ is literally called the extremizing parameter there). The specific quantity asked about, λ* solved so the posterior logit exactly meets a threshold, doesn't have one universally-agreed name that I can point to with confidence; the closest standard framings are a **"breakeven" or "critical" likelihood-ratio/odds multiplier**, i.e., the scaling of accumulated log-odds evidence needed to cross a decision boundary. I'd describe it in an answer as "the critical extremization factor" rather than assert that's an established fixed term.

**2. Fields.** Judgment-and-decision-making / forecasting-aggregation statistics (this is the home of "extremizing"); Bayesian decision theory and evidential reasoning more broadly (weight-of-evidence, threshold-of-proof framings); a looser tie to legal probabilism (Bayesian burden-of-proof thresholds).

**3. Oldest treatments.**
- I.J. Good, *Probability and the Weighing of Evidence* (Griffin, 1950) — origin of log-odds "weight of evidence" as an additive quantity; Good also has a later survey, "Weight of Evidence: A Brief Survey" (in *Bayesian Statistics 2*, ~1985) — hedge on exact pagination.
- Ward Edwards, "Conservatism in Human Information Processing," in B. Kleinmuntz (ed.), *Formal Representation of Human Judgment* (Wiley, 1968) — models human updating as scaling the ideal log-odds increment by a coefficient below 1 ("conservatism"), the closest pre-2015 analogue to λ<1 vs λ>1 here.
- On the pooling side specifically: Satopää, Baron, Foster, Mellers, Tetlock & Ungar, "Combining Multiple Probability Predictions Using a Simple Logit Model," *International Journal of Forecasting*, 2014; and Baron, Mellers, Tetlock, Ungar & Ramos, "Two Reasons to Make Aggregated Probability Forecasts More Extreme," *Decision Analysis*, 2014 — both introduce λ as an extremizing multiplier on pooled log-odds, which is very close to this setup's λ. I'm fairly but not fully confident on volume/issue numbers.
- Broader review of opinion pooling: Genest & Zidek, "Combining Probability Distributions: A Critique and an Annotated Bibliography," *Statistical Science*, 1986.

**4. Confidence / what to verify first.** Medium. I'm confident the "extremizing λ on pooled logits" framework is a real, named literature (Satopää/Baron/Tetlock/Ungar line); I'm not confident that "λ*" itself, as a solved breakeven value, is a term anyone has published under a fixed name — it may be original to whatever source this question is drawn from. I'd verify by pulling the Satopää et al. 2014 and Baron et al. 2014 papers directly and checking whether they discuss a threshold-crossing λ, and separately check whether this is actually from a specific (possibly non-academic) forecasting write-up rather than peer-reviewed literature.

## CONCEPT-2: minimum estimator accuracy for a setting to beat a fixed fallback

**1. Canonical term(s).** This is a **value-of-information** question: how much of the **expected value of perfect information (EVPI)** is captured by an imperfect/noisy estimate, as a function of estimation error, versus a fixed benchmark value. "A standard accuracy measure for probability forecasts" is almost certainly the **Brier score** (or a **Brier skill score**, which is literally defined as a fraction of achievable improvement over a reference forecast — that phrasing matches "fraction retained of the maximum achievable improvement" closely).

**2. Fields.** Decision analysis (value-of-information theory); meteorological/statistical forecast verification (proper scoring rules, skill scores).

**3. Oldest treatments.**
- Ronald A. Howard, "Information Value Theory," *IEEE Transactions on Systems Science and Cybernetics*, 1966 — foundational EVPI/EVSI framing.
- Raiffa & Schlaifer, *Applied Statistical Decision Theory* (Harvard Business School, 1961) — earlier decision-analytic treatment of the value of sample vs. perfect information.
- Brier, "Verification of Forecasts Expressed in Terms of Probability," *Monthly Weather Review*, 1950 — origin of the Brier score, the ancestor of "skill score" (fraction of achievable improvement) framings.
- Gneiting & Raftery, "Strictly Proper Scoring Rules, Prediction, and Estimation," *JASA*, 2007 — modern canonical treatment of Brier score and proper scoring rules generally, useful for the "standard accuracy measure" language.

**4. Confidence / what to verify first.** Medium-high on the general framework (VoI / EVPI-fraction-retained, Brier skill score), low on the specific numeric schedule (RMSE≲0.3→~85%, ≈0.6→~50%, ≥1.0→harmful). That schedule reads as a bespoke simulation result from whatever paper this question is drawn from, not something already sitting in the literature under a name — the concept description itself says it's established "by injecting synthetic errors" rather than citing prior work, which is a signal it's original to the source. I'd verify by checking whether "Brier skill score" is indeed the accuracy measure intended, and separately search for the exact numeric breakpoints to see if they trace to a specific named paper (I don't recognize them as a known result).

## CONCEPT-3: attributing a performance shortfall to selection, not generation

**1. Canonical term(s).** This maps most cleanly onto the **discriminability vs. criterion (bias)** distinction in **signal detection theory** — "the information needed to discriminate is present; the decision criterion for committing vs. withholding is what's miscalibrated." In ML/NLP terms, the two-stage generate-then-decide structure is **selective prediction / classification with a reject option**, and the diagnostic technique described (candidate sets are rich; the filter is narrow) is the same move as comparing **oracle (best-of-candidates) accuracy** to **realized (1-best/selected) accuracy** — a standard gap-analysis technique in reranking/QA/MT literature, though I don't know one single canonical name for that specific comparison.

**2. Fields.** Psychophysics / signal detection theory; machine learning (selective classification, calibration, abstention); by extension, NLP evaluation methodology (N-best/oracle-vs-1-best analysis).

**3. Oldest treatments.**
- Green & Swets, *Signal Detection Theory and Psychophysics* (Wiley, 1966) — canonical origin of the sensitivity/criterion split.
- C.K. Chow, "On Optimum Recognition Error and Reject Tradeoff," *IEEE Transactions on Information Theory*, 1970 — classic reject-option classification result, the ML ancestor of "commit vs. hedge."
- Murphy, "A New Vector Partition of the Probability Score," *Journal of Applied Meteorology*, 1973 — calibration/refinement decomposition, relevant if the filter is confidence-threshold-based.
- More recent (post-2015, so just for context, not as the "oldest"): El-Yaniv & Wiener, "On the Foundations of Noise-Free Selective Classification," *JMLR*, 2010, is actually pre-2015 and a good formal treatment of selective classification specifically.

**4. Confidence / what to verify first.** Medium. I'm confident about signal detection theory and Chow's reject-option paper as the right conceptual homes; I'm not confident there's a single named term for "generation-not-the-bottleneck" as a diagnostic claim — it may just be argued informally in whatever domain paper this comes from (possibly LLM calibration/hedging research). I'd verify by checking Chow (1970) and El-Yaniv & Wiener (2010) for language matching "oracle richness vs. filter narrowness," and check recent (2023–2025) LLM-abstention/selective-QA papers, since the phrasing ("raters," "hedging," "ambiguous items") smells like it could be from recent work on LLM calibration rather than classical ML.

## CONCEPT-4: pooling raters' full candidate lists rather than their single picks

**1. Canonical term(s).** The closest well-established formal analogue is **approval voting** in social choice theory — each rater submits a *set* of acceptable options rather than one pick, sets are pooled, and a fixed rule selects a winner; approval voting is known to outperform plurality (single-choice) voting on various efficiency measures, which matches "beats voting over committed single answers." The two-stage architecture (generate many candidates, then filter/select) also matches the NLG **"overgenerate-and-rank"** paradigm. In ML/IR system-combination terms, pooling multiple systems' candidate/ranked lists and selecting via a fixed rule is the same shape as **rank/list fusion** methods.

**2. Fields.** Social choice / voting theory (approval voting); natural language generation (overgenerate-and-filter architectures); information retrieval / ASR system combination (list/rank fusion, ensembling); and, as the likely motivating domain given "ambiguous items" and "defensible readings," NLP annotation methodology on label variation/disagreement.

**3. Oldest treatments.**
- Brams & Fishburn, "Approval Voting," *American Political Science Review*, 1978 — foundational formal treatment of multi-candidate-per-voter aggregation outperforming single-choice voting.
- Langkilde & Knight, "Generation that Exploits Corpus-Based Statistical Knowledge," COLING-ACL, 1998 — origin of the "overgenerate and rank" NLG architecture.
- Fiscus, "A Post-Processing System to Yield Reduced Word Error Rates: Recognizer Output Voting Error Reduction (ROVER)," IEEE ASRU Workshop, 1997 — classic system-combination-by-voting result, though it pools single best outputs rather than candidate sets, so it's a looser match.
- Cormack, Clarke & Buettcher, "Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods," SIGIR, 2009 — closer mechanically (pooling ranked/candidate lists, fixed selection rule beating individual-list performance).
- For the motivating "ambiguous items, multiple defensible readings" framing specifically (likely post-2015 but worth naming): Aroyo & Welty, "Truth is a Lie: Crowd Truth and the Seven Myths of Human Annotation," *AI Magazine*, 2015, is right at the boundary and is the earliest I can place with any confidence in that specific sub-literature.

**4. Confidence / what to verify first.** Medium. Approval voting is a strong structural match and I'm fairly confident about the 1978 citation; the NLG/IR analogues are plausible but looser fits and I'm less sure they're what the source actually intends. I'd verify by checking whether the source frames this as a voting-theory result (search for "approval voting" + "candidate sets" together) versus an NLP-annotation-methodology result (search recent LLM-hedging/ambiguous-QA papers, since concepts 3 and 4 together read like they're describing the same underlying study).

**One general caveat across all four:** the very specific numeric details (β/λ formulas, the 85%/50%/1.0 schedule, "three-quarters"/"one-third" figures, "≥0.10 gap") strongly suggest these four concepts are paraphrased from a single specific (possibly recent, possibly non-peer-reviewed) source about LLM or human forecaster calibration and hedging — not independently well-known results. I'd treat my field/framework identifications as solid but treat any specific citation I gave as needing a direct check before you rely on it, per your rules.
