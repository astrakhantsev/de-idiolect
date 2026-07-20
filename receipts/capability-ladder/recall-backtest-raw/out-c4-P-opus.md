I've verified the citations I need. Here's my identification.

## Short version

There is **no single universally-adopted term for this exact end-to-end pipeline** — it's a composite that reinvents, and sits at the intersection of, three well-established ideas from three different fields. But the operational core maps very cleanly onto named concepts, and the tightest single anchor is **approval voting** (for the aggregation) combined with **set-valued / non-deterministic prediction** (for the per-judge output). I'm confident about the component identifications and their canonical sources; I'm hedging only on the claim that any one name covers the *whole* recipe (it doesn't).

## 1. What it's called (standard names)

Decompose the recipe into its two moves — "each judge emits a *set* of admissible labels" and "pool the sets (union) and pick one by a fixed rule, and this beats single-vote tallies" — and each move has an established name:

- **The per-judge output (enumerate every defensible reading, don't commit to one):**
  - **Set-valued prediction** / **non-deterministic classification** — the ML/statistics name for a predictor that returns a *set* of admissible labels instead of an argmax. (Confidence: high.)
  - **Prediction sets / conformal prediction** — the statistics name when the set carries a coverage guarantee. (High.)
  - In annotation/NLP: **human label variation**, **perspectivism**, **"plausible label set"**, **crowd truth** — the practice of recording *all defensible readings* rather than forcing one gold label. "Told to enumerate every defensible reading, one line each" is almost verbatim the perspectivist / crowd-truth annotation protocol. (High.)

- **The aggregation (set ballots, union, fixed rule; beats single-vote tally):**
  - **Approval voting** (vs. **plurality / first-past-the-post voting**) — the social-choice name for exactly "each voter submits a *set* of approved options rather than one." Your central claim — *set ballots can beat what single committed votes deliver, and plurality can fall short* — is the canonical argument *for* approval voting over plurality. (High that this is the right social-choice anchor; medium that your specific union-then-fixed-rule tie-break is literally "approval voting" rather than an approval-*style* rule — see caveat below.)
  - **Ensemble / committee combination**, and specifically the result that **the combination can beat the best individual member** while a naïve **majority vote can underperform the best member** — the machine-learning name for the performance claim. The union-of-candidate-sets is the ensemble **"coverage" / "oracle" upper bound**, which is ≥ any single member *by construction*. (High.)
  - Distant cousin worth knowing: **pooling** in information-retrieval evaluation (union the candidate sets from many systems so the correct item is almost surely *in the pool*, then judge) — this is the "union to maximize recall" logic your project directory name (`recall-backtest`) hints at. (Medium relevance.)

The one honest caveat on naming: your fixed rule operates on the **union** and can be *any* pre-decided selection (e.g., a priority ordering over labels), whereas textbook approval voting's rule is specifically "most approvals wins." So the precise term for your variant is **set-valued / approval-*style* aggregation**, of which approval voting is the best-known instance. I'd flag "it's exactly approval voting" as **only medium confidence**; "it's in the approval-voting / set-valued-aggregation family" is **high confidence**.

## 2. Which fields own it

- **Social choice / voting theory** (economics, political science) — owns approval vs. plurality and the Condorcet-jury lineage.
- **Machine learning / statistics** — owns set-valued/non-deterministic prediction, conformal prediction, and ensemble/committee combination (incl. "beats the best base learner").
- **NLP annotation, crowdsourcing, HCI** — owns human label variation / perspectivism / crowd truth (enumerate all plausible readings; reject single ground truth).
- **Information retrieval** (secondary) — owns pooling / recall-oriented union of candidate sets.

## 3. Oldest / most canonical treatments (real citations)

**Social choice — set ballots beat single-choice ballots (pre-2015):**
- Brams, S. J., & Fishburn, P. C. (1978). "Approval Voting." *American Political Science Review*, 72(3), 831–847. — the founding paper. (Verified.)
- Brams, S. J., & Fishburn, P. C. (1983). *Approval Voting*. Birkhäuser (2nd ed., Springer, 2007). — the canonical monograph. (Verified as a real title; edition detail medium.)
- Condorcet, M. de (1785). *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix.* — the **Condorcet Jury Theorem** root of "a panel can beat its members." (Note: this concerns *votes*, not sets, so it's the lineage for your performance claim, not for the set-ballot mechanism. Confidence high on existence/relevance.)

**Machine learning — set-valued prediction & ensemble-beats-best-member (pre-2015):**
- Hansen, L. K., & Salamon, P. (1990). "Neural Network Ensembles." *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 12(10), 993–1001. — foundational "a committee outperforms its individual members." (Verified.)
- Kittler, J., Hatef, M., Duin, R. P. W., & Matas, J. (1998). "On Combining Classifiers." *IEEE TPAMI*, 20(3), 226–239. — canonical classifier-combination framework. (Verified as real; page/vol high confidence.)
- Dietterich, T. G. (2000). "Ensemble Methods in Machine Learning." *Multiple Classifier Systems (MCS 2000)*, LNCS 1857, 1–15. — the standard "why ensembles beat the best member" reference. (High.)
- del Coz, J. J., Díez, J., & Bahamonde, A. (2009). "Learning Nondeterministic Classifiers." *Journal of Machine Learning Research*, 10, 2273–2293. — canonical **set-valued/"predict a set of labels"** treatment, explicitly framed with **recall/IR** loss functions (directly parallels your union-for-recall move). (Verified.)
- Vovk, V., Gammerman, A., & Shafer, G. (2005). *Algorithmic Learning in a Random World.* Springer. — the canonical **conformal prediction** (prediction-set) book. (High.)

**NLP annotation — enumerate all plausible readings, reject single gold (one pre-2015, plus the modern canon):**
- Aroyo, L., & Welty, C. (2015). "Truth Is a Lie: Crowd Truth and the Seven Myths of Human Annotation." *AI Magazine*, 36(1), 15–24. — the canonical "don't collapse to one truth; record the crowd's full set of interpretations." (Verified; 2015, at your pre-2015 boundary.)
- Uma, A., Fornaciari, T., Hovy, D., Paun, S., Plank, B., & Poesio, M. (2021). "Learning from Disagreement: A Survey." *Journal of Artificial Intelligence Research*, 72, 1385–1470. — the standard survey. (High.)
- Plank, B. (2022). "The 'Problem' of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation." *EMNLP 2022*. — coined/popularized "human label variation." (High.)

(Earlier annotation-uncertainty roots exist too — e.g., Dawid & Skene, 1979, *JRSS-C*, on aggregating multiple noisy observers — but that aggregates *votes* toward one latent truth, the opposite of "keep the enumerations," so I list it only as background.)

## 4. Confidence summary

- **High:** the recipe decomposes into (a) set-valued/non-deterministic prediction + (b) approval-style set-ballot aggregation + (c) the ensemble/jury result that a pooled panel can match/beat its best member while naïve single-vote majority can fall short; and that the "enumerate every defensible reading, don't pad" instruction is the perspectivist/crowd-truth annotation protocol. The citations above are real and verified.
- **Medium:** that any *single* name covers your full end-to-end pipeline. It doesn't cleanly — this reads as an independent reinvention/recombination. Closest single label: **approval voting** (social choice) or **set-valued/approval-style aggregation** (ML).
- **Low / flagged uncertain:** that your specific "union then fixed pre-decided rule" is *literally* approval voting rather than an approval-*style* rule (approval voting's canonical rule is max-approvals, not union-plus-arbitrary-tie-break); and exact page numbers on the Kittler and Brams–Fishburn *book* editions (titles/venues are right; I'd double-check pagination before quoting).

If you want, I can pull the full PDFs of del Coz et al. (2009) and the Brams–Fishburn 1978 paper to confirm the exact framing and lock down the pagination.

Sources:
- [Brams & Fishburn 1978, APSR (ref)](https://www.scirp.org/reference/referencespapers?referenceid=2663586) · [Approval Voting, Cambridge Core](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/approval-voting/7CE5DEEE235794B0B12F76ADAE621482) · [Approval voting (Wikipedia)](https://en.wikipedia.org/wiki/Approval_voting) · [Plurality voting (Wikipedia)](https://en.wikipedia.org/wiki/Plurality_voting)
- [Hansen & Salamon 1990 (ref)](https://www.scirp.org/reference/referencespapers?referenceid=1484253) · [Neural Network Ensembles (Semantic Scholar)](https://www.semanticscholar.org/paper/Neural-Network-Ensembles-Hansen-Salamon/257dc8ae2a8353bb2e86c1b7186e7d989fb433d3)
- [del Coz, Díez & Bahamonde 2009, "Learning Nondeterministic Classifiers," JMLR](https://www.jmlr.org/papers/v10/delcoz09a.html)
- [Set-valued classification — unified framework (survey)](https://arxiv.org/pdf/2102.12318)
- [Aroyo & Welty 2015, "Truth Is a Lie," AI Magazine](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2564)
- [Plank 2022, "The 'Problem' of Human Label Variation"](https://aclanthology.org/2022.emnlp-main.731.pdf) · [awesome-human-label-variation (Uma/Plank refs)](https://github.com/mainlp/awesome-human-label-variation)
