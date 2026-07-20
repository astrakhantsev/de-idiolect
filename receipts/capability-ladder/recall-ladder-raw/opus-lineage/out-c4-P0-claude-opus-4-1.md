## What this concept is

**Short version:** "read the enumerations, not the votes" is a (re-)statement of a well-established combining principle for panels of evaluators: **when several judges each produce (a) an enumerated list of specific findings/issues and (b) a verdict or score, the informative signal lives in the *union of the enumerated findings*, not in the *vote tally*.** Different evaluators reliably surface *largely non-overlapping* true problems, so aggregating by majority vote/average discards real findings that only a minority flagged. The correct combination is disjunctive (pool the sets), not majoritarian. It's a coverage/recall argument dressed as coined vocabulary.

Below, in the order you asked.

### 1. Standard name(s)

There is no single universal label — it's the same insight named differently by the fields that own it:

- **"Different evaluators find different problems" / aggregation of inspection findings by pooling (union), not voting.** (HCI/usability term of art.)
- **Defect pooling in software inspection**, and its statistical cousin **capture–recapture defect estimation** (which works *precisely because* it reads each reviewer's enumerated defect set and its overlap, not a vote). (Software-engineering term.)
- **Disjunctive / "OR" combination rule** (a.k.a. recall-maximizing fusion; union of detections) in **classifier/decision fusion**. Contrast with majority-vote/"AND" rules that maximize precision. (Pattern-recognition term.)
- Loosely related, and worth naming because it captures the "reasons vs. votes" phrasing: **reason-/premise-based vs. outcome-/conclusion-based aggregation**, from the **doctrinal paradox / discursive dilemma** in **judgment aggregation**. (Weaker match — see confidence note.)
- In the project's own likely domain (LLM evaluation), the contemporary instantiation is **"error analysis / critiques over aggregate metrics"** and the **panel-of-LLM-judges (PoLL) / LLM-jury** literature.

### 2. Field(s) that own it

Primary owners (strongest fit): **Human–Computer Interaction / usability engineering** and **software engineering (quality assurance / inspection)**. Formal cousin: **pattern recognition / machine learning (ensemble methods & decision fusion)**. Conceptual cousin: **social choice theory / jurisprudence (judgment aggregation)**. Modern re-derivation: **NLP / LLM evaluation**.

### 3. Oldest and most canonical treatments (real citations; several pre-2015)

- **Fagan, M. E. (1976).** "Design and code inspections to reduce errors in program development." *IBM Systems Journal* 15(3), 182–211. — The seminal software-inspection paper; inspectors produce enumerated defect lists that are pooled. ([ACM/IBM](https://dl.acm.org/doi/10.1147/sj.153.0182))
- **Nielsen, J., & Molich, R. (1990).** "Heuristic evaluation of user interfaces." *Proc. ACM CHI '90*, 249–256. — Establishes that multiple evaluators are needed because each finds a *different subset* of problems. ([NN/g theory page](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/))
- **Nielsen, J., & Landauer, T. K. (1993).** "A mathematical model of the finding of usability problems." *Proc. INTERACT '93 / CHI '93*, 206–213. — Formalizes problem-finding as a Poisson process over pooled findings (the "different people find different problems, so union them" result). ([ACM DL](https://dl.acm.org/doi/10.1145/169059.169166))
- **Eick, S. G., Loader, C. R., Long, M. D., Votta, L. G., & Vander Wiel, S. (1992).** "Estimating software fault content before coding." *Proc. 14th ICSE*, 59–65. — First to bring **capture–recapture** to inspections; the method literally reads the *overlap of enumerated defect sets* across reviewers rather than a vote. ([dblp ICSE '92](https://dblp.org/db/conf/icse/icse92.html))

Secondary/related canon (for the "reasons vs. votes" and fusion facets):

- **Kittler, J., Hatef, M., Duin, R. P. W., & Matas, J. (1998).** "On combining classifiers." *IEEE TPAMI* 20(3), 226–239. — Canonical treatment of combination rules including the disjunctive/OR (union) rule vs. majority vote. *(Citation recalled and consistent with what I found on disjunctive fusion, but I did not open this specific paper in this session — treat as uncertain on exact page numbers.)*
- **List, C., & Pettit, P. (2002).** "Aggregating sets of judgments: An impossibility result." *Economics and Philosophy* 18(1), 89–110; building on **Kornhauser, L. A., & Sager, L. G. (1986)**, "Unpacking the court," *Yale Law Journal* 96, 82–117 (the "doctrinal paradox"). — Formalize that aggregating *reasons* (premises) vs. *outcomes* (the vote) can diverge. *(The Kornhauser–Sager citation is from memory; I confirmed the doctrinal-paradox/discursive-dilemma concept and the List–Pettit line via search but did not verify the Yale L.J. page range this session — mark uncertain.)*

Modern instantiation in the project's likely domain (all post-2015, given for grounding, not as "canonical origins"):

- **Verga, P., et al. (2024).** "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models" (Panel of LLM evaluators, "PoLL"). ([arXiv](https://arxiv.org/html/2404.18796v1))
- **"Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels"** (Apple ML Research) — empirical case *against* over-trusting vote aggregation in judge panels, which is the same lesson pointing you toward the enumerated content. ([Apple ML](https://machinelearning.apple.com/research/correlated-llm-evaluation-panels))

### 4. Confidence and hedges

- **High confidence** that the *mechanism* the phrase describes — pool the union of distinct enumerated findings rather than tally votes, because evaluators find non-overlapping true items — is a genuine, decades-old, well-cited principle. The usability-inspection (Nielsen & Molich 1990; Nielsen & Landauer 1993) and software-inspection (Fagan 1976; Eick et al. 1992) citations are solid and directly on point.
- **Medium confidence** on *which* discipline's label the project intends. Because this is the project's coined vocabulary, I'm matching by meaning, and the same insight has several homes (usability, SE inspection, decision fusion). I'd lead with the inspection/usability framing and treat "disjunctive/OR fusion" as the formal statistical version.
- **Lower confidence / partial match:** the **doctrinal paradox / judgment aggregation** ("reasons vs. votes") is thematically the closest to your exact wording, but it's fundamentally about *logical inconsistency* of majority verdicts, not about the *coverage/information-richness of enumerations*. Related, not the same claim — flagging it so you can decide if that's the resonance you meant.
- **Unverified citations** (flagged above): Kittler et al. (1998) exact pagination and Kornhauser & Sager (1986) exact pagination were recalled, not opened this session.
- One caveat on interpretation: I read "enumerations" as *the itemized list of issues/reasons a judge emits* and "votes" as *its verdict/score aggregated across the panel*. If your "enumerations" instead means something narrower (e.g., per-rubric line-item pass/fails), the same disaggregation principle still applies, but I'd want to confirm the reading.

Sources:
- [Fagan 1976 — Design and code inspections (IBM Systems Journal)](https://dl.acm.org/doi/10.1147/sj.153.0182)
- [Nielsen & Molich / heuristic-evaluation theory (NN/g)](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/)
- [Nielsen & Landauer 1993 — Mathematical model of finding usability problems (ACM)](https://dl.acm.org/doi/10.1145/169059.169166)
- [ICSE '92 proceedings (Eick et al., capture–recapture)](https://dblp.org/db/conf/icse/icse92.html)
- [Capture–recapture in software inspections after 10 years (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0164121203000906)
- [Doctrinal paradox / discursive dilemma (Wikipedia)](https://en.wikipedia.org/wiki/Discursive_dilemma)
- [Verga et al. 2024 — Replacing Judges with Juries (arXiv)](https://arxiv.org/html/2404.18796v1)
- [Nine Judges, Two Effective Votes (Apple ML Research)](https://machinelearning.apple.com/research/correlated-llm-evaluation-panels)
