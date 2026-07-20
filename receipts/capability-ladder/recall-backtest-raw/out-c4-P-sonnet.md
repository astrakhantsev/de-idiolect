## Identification

**This is not a single, already-named concept with one canonical citation.** It's a specific combination of two independently well-established ideas, neither of which alone covers the whole described protocol. I'll give both, plus the closest adjacent literatures, and flag confidence throughout.

### 1. Standard name(s)

**(a) The "enumerate, then take the union" step → generalizes the "Oracle" (oracle accuracy / oracle score) from ensemble learning.** In classifier-ensemble theory, the *oracle* is the hypothetical combiner that gets an item right if **at least one** ensemble member's output is correct — it is used specifically as an upper bound to show that ensembles have far more latent correct coverage than their actual combiner (majority vote) realizes. Your description generalizes this from "each member outputs one label" to "each member outputs a whole set of defensible labels," but the core mathematical object — union of per-member candidate sets, recall of the true label in that union vs. recall of the tallied single vote — is the same construction. **Confidence: high** that this is the closest existing named concept for the recall/coverage half of your claim.

**(b) The "ask for every defensible option, not a forced single pick" elicitation → Approval Voting.** In social choice theory, an approval ballot lets each voter mark every candidate they find acceptable rather than committing to one favorite; results are then tallied by a fixed rule. This matches your "enumerate every defensible reading… in some versions not to cast a single final vote at all" almost exactly as a ballot format. **Confidence: high** as the closest named match for the elicitation/ballot structure, **medium** as a match for your specific aggregation step (classic approval voting tallies approval *counts* per candidate across voters, whereas your protocol pools into a set and then applies a separate fixed selection rule — a related but not identical aggregation).

**(c) Adjacent, not a direct match:** IR test-collection "pooling" (union of top-ranked document sets from many systems, so that judging effort concentrates on the union rather than the full corpus) — same "union of committee outputs as a working candidate set" structure, but for documents, not labels. **Confidence: medium**, offered as a structural analogy only.

**(d) Adjacent, not a direct match:** "pass@k" / best-of-N coverage in LLM sampling evaluation (does at least one of k samples solve the problem), and the annotator-disagreement literature ("CrowdTruth," "human label variation") which argues against collapsing multiple defensible interpretations into one gold label. Both share DNA with your description but neither describes the specific enumerate→pool→fixed-rule pipeline. **Confidence: medium-low** as direct matches; they're context, not identification.

I could not find any single paper or field that names the *entire* pipeline you describe (per-judge enumeration → union pooling across a panel → fixed pre-decided selection rule → forced decision on every item, benchmarked against single-vote tallying) as one coherent, established technique. That composite appears to be a project-level synthesis of (a) and (b), not itself a term of art. **Confidence: high that no single established name for the whole pipeline exists** (based on the searches run; I can't rule out a niche paper I didn't surface).

### 2. Owning field(s)

- Pattern recognition / machine learning — ensemble learning, multiple classifier systems, dynamic classifier/ensemble selection (for the "oracle" concept).
- Computational social choice / voting theory (for approval voting).
- Information retrieval (for pooling, as a structural analogy).
- More recently, NLP/ML evaluation methodology for "LLM-as-judge" panels, and annotation/ground-truth methodology in NLP (perspectivism, human label variation) — these are where a technique like yours would likely eventually get its own name if it hasn't already.

### 3. Oldest / most canonical treatments

**Oracle (ensemble learning), pre-2015:**
- Woods, K., Kegelmeyer, W.P., & Bowyer, K. (1997). "Combination of multiple classifiers using local accuracy estimates." *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 19(4), 405–410.
- Giacinto, G., & Roli, F. (2001). "Dynamic classifier selection based on multiple classifier behaviour." *Pattern Recognition*, 34(9), 1879–1881.
- Kuncheva, L.I. (2004). *Combining Pattern Classifiers: Methods and Algorithms*. Wiley. (Standard textbook treatment; a 2nd edition exists from 2014.) Related: Kuncheva, L.I., & Whitaker, C.J. (2003). "Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy." *Machine Learning*, 51, 181–207.
*(Confidence: high on Woods et al. 1997 and Giacinto & Roli 2001 as genuinely early/foundational; I did not personally verify the "oracle" term appears verbatim in the 1997 paper vs. being retroactively applied to it by later surveys — flag as medium-high, not certain.)*

**Approval voting:**
- Brams, S.J., & Fishburn, P.C. (1978). "Approval Voting." *American Political Science Review*, 72(3), 831–847. **Confidence: high** — this citation is well corroborated across multiple independent sources.

**IR pooling (structural analogy), pre-2015:**
- Spärck Jones, K., & van Rijsbergen, C.J. (1975). "Report on the need for and provision of an 'ideal' information retrieval test collection." British Library Research and Development Report No. 5266, Computer Laboratory, University of Cambridge. **Confidence: medium** — well corroborated as the originating report for pooling, but I have not read the primary document myself, only secondary citations of it.

**Adjacent/context, not origin:**
- Chen, M. et al. (2021). "Evaluating Large Language Models Trained on Code." arXiv:2107.03374. (pass@k formalization.)
- Aroyo, L., & Welty, C. (2013). "Crowd Truth: Harnessing disagreement in crowdsourcing a relation extraction gold standard." Web Science 2013 / *Human Computation* 1(1), 2014. And Aroyo, L., & Welty, C. (2015). "Truth Is a Lie: CrowdTruth and the Seven Myths of Human Annotation." *AI Magazine*, 36(1), 15–24.
- Very recent, directly on-topic for the *pathology* your claim's second half describes (single-vote tallying falling short of the best panelist): "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels," arXiv:2605.29800 (2026, Apple Research). This is 2026 work, not a canonical/old source, and it studies score-voting panels, not enumeration — cited as strong supporting context, not as the origin of your technique. **Confidence: high on the paper's existence and content as reported; low as a claim about who first proposed your specific technique.**

### 4. Summary confidence table
- "Oracle"/coverage as the name for the recall-of-union half: **high**.
- Approval voting as the name for the enumerate-not-vote elicitation half: **high**.
- No single field/paper names the full combined pipeline: **high**.
- Exact wording of the 1997/2001 papers using "oracle": **medium-high** (not independently read primary text).
- Pooling/1975 report as precise citation: **medium** (secondary-sourced).
- Any of this being what your project's authors actually drew on: **unknown** — I have no evidence either way of intent.

Sources:
- [On the Characterization of the Oracle for Dynamic Classifier Selection](https://www.researchgate.net/publication/314179021_On_the_Characterization_of_the_Oracle_for_Dynamic_Classifier_Selection)
- [Combining Pattern Classifiers: Methods and Algorithms](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118914564)
- [Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy](https://www.researchgate.net/publication/220344230_Measures_of_Diversity_in_Classifier_Ensembles_and_Their_Relationship_with_the_Ensemble_Accuracy)
- [Approval Voting | American Political Science Review | Cambridge Core](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/approval-voting/7CE5DEEE235794B0B12F76ADAE621482)
- [THE TEXT RETRIEVAL CONFERENCES (TRECS) — Voorhees, Harman](https://aclanthology.org/X98-1031.pdf)
- [Bias and the limits of pooling for large collections | Discover Computing](https://link.springer.com/article/10.1007/s10791-007-9032-x)
- [Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels](https://arxiv.org/abs/2605.29800)
- [Human Computation (2014) — CrowdTruth, Aroyo & Welty](https://hcjournal.org/index.php/jhc/article/download/34/8/116)
- [Truth Is a Lie: Crowd Truth and the Seven Myths of Human Annotation — AI Magazine](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v36i1.2564)
- [Notes on "Evaluating Large Language Models Trained on Code"](https://www.andrelizardo.com/p/notes-on-evaluating-large-language)
