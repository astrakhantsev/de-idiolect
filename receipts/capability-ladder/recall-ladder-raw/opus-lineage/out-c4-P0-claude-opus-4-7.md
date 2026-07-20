I have enough to answer. Here's what the notes-phrase maps to:

## 1. Standard name(s)

The claim "read the enumerations, not the votes — how to use panel judge outputs" maps most cleanly to the **premise-based** (a.k.a. **reason-based** / **issue-by-issue**) **procedure for judgment aggregation**, as opposed to the **conclusion-based** (a.k.a. **case-by-case** / **outcome-voting**) procedure. The underlying puzzle that makes the two procedures come apart is called the **doctrinal paradox** (Kornhauser & Sager) or, in its generalized form, the **discursive dilemma** (List & Pettit). *Medium-high confidence* — the fit is very tight: a panel of judges, each producing an enumerated set of sub-findings/reasons plus a bottom-line vote, and a normative claim about which layer to aggregate on.

A weaker, more speculative reading is that the note is about **LLM-as-a-judge panels** in AI evaluation, where recent papers argue that aggregating the *rationales* (structured reasoning) beats aggregating discrete votes/labels. This is the same shape of claim, translated to model evaluation. *Lower confidence*; this literature has no canonical pre-2015 treatment.

## 2. Field(s)

- **Social choice theory / judgment aggregation** (formal political theory & economics). Primary owner.
- **Analytic philosophy / political philosophy** (List, Pettit — heavy overlap with social choice).
- **Law & economics / jurisprudence of collegial courts** (where Kornhauser & Sager launched the puzzle).
- Secondary/derivative: **computational social choice** (CS side of the same field), and, if the AI reading applies, **AI/ML evaluation methodology (LLM-as-judge)**.

## 3. Oldest / most canonical treatments (real citations)

Pre-2015, high confidence in existence and details:

- **Kornhauser, L. A., & Sager, L. G. (1986). "Unpacking the Court." *Yale Law Journal*, 96(1), 82–117.** — the founding statement of the doctrinal paradox, in the setting of multi-judge panels: aggregating votes on the premises vs. on the conclusion can diverge.
- **List, C., & Pettit, P. (2002). "Aggregating Sets of Judgments: An Impossibility Result." *Economics and Philosophy*, 18(1), 89–110.** — generalizes the paradox into the *discursive dilemma* and proves the first Arrow-style impossibility theorem for judgment aggregation. This is the paper that founds the modern research area.
- **Pettit, P. (2001). "Deliberative Democracy and the Discursive Dilemma." *Philosophical Issues*, 11, 268–299.** — coined the term "discursive dilemma"; earlier philosophical statement of the same problem.
- **List, C., & Puppe, C. (2009). "Judgment Aggregation: A Survey."** In P. Anand, P. Pattanaike & C. Puppe (eds.), *The Handbook of Rational and Social Choice*, Oxford University Press. — the standard survey; lays out premise-based vs. conclusion-based procedures explicitly.
- **Grossi, D., & Pigozzi, G. (2014). *Judgment Aggregation: A Primer.* Morgan & Claypool (Synthesis Lectures on AI and ML).** — canonical textbook-length treatment; explicit chapter on premise- vs. conclusion-based rules.

Confidence: author names, years, and venues above are high-confidence and consistent across multiple sources I checked. Exact page ranges for the Pettit 2001 piece are from memory of the search results — treat page numbers as *uncertain*; author, year, and journal are solid.

If the note is really about **LLM-judge panels**, the closest analogue is the recent "rationale-based aggregation beats label-only majority vote" line of work (e.g., 2025–2026 arXiv preprints such as "Nine Judges, Two Effective Votes" and "RoPoLL: Robust Panel of LLM Judges"). No pre-2015 canonical citation exists for that reading — that's exactly why I lean toward the judgment-aggregation reading as the "established concept."

## 4. Overall confidence and hedges

- That the concept is **judgment aggregation, premise- vs. conclusion-based procedure, doctrinal paradox / discursive dilemma family**: *medium-high confidence*. The mapping "enumerations → premises/reasons, votes → conclusions, panel of judges → collegial court or judge panel" is direct.
- That it is *not* actually meant as the LLM-eval variant: *not fully sure* — the phrase "panel judge outputs" is generic enough to be AI-flavored. But absent any AI-specific tell, and given the historical priority of the legal/philosophical concept, the older concept is the safer identification.
- Kornhauser & Sager 1986 and List & Pettit 2002 as canonical: *high confidence*.
- Anything about specific page numbers or article subtitles: treat as *uncertain* unless you double-check the record.

Sources:
- [The doctrinal paradox, the discursive dilemma, and logical aggregation theory (Mongin) — MPRA](https://mpra.ub.uni-muenchen.de/37752/1/Mongin_LogicalAggregation_2012.pdf)
- [Belief Merging and Judgment Aggregation — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/belief-merging/)
- [An Introductory Course to Judgment Aggregation (arXiv 1607.03307)](https://arxiv.org/pdf/1607.03307)
- [Premise-based vs conclusion-based collective choice — Social Choice and Welfare](https://link.springer.com/article/10.1007/s00355-021-01319-w)
- [A Complete Conclusion-Based Procedure for Judgment Aggregation (Slavkovik)](https://slavkovik.com/adt09-techReport.pdf)
- [Aggregating Sets of Judgments: An Impossibility Result — LSE eprints (List & Pettit 2002)](https://eprints.lse.ac.uk/704/1/List_Econ&Phil_18(1).pdf)
- [Encyclopedia of Law & Economics — Kornhauser bibliography (FindLaw)](https://reference.findlaw.com/lawandeconomics/literature-reviews/lewis-a-kornhauser-professor-of-law.html)
- [Complex Collective Decisions and the Probability of the Doctrinal Paradox (Nuffield WP)](https://www.nuff.ox.ac.uk/economics/papers/2001/w23/doctrinal-wp.pdf)
- [Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels (arXiv 2605.29800)](https://arxiv.org/html/2605.29800) — for the LLM-panel reading only
