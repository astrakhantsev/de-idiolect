## What this concept is

**My reading of the note.** A "panel of judges" here emits two kinds of output per judge: (a) a *vote/verdict* — a pass/fail, a preference, or a score — and (b) an *enumeration* — the specific list of issues/defects/reasons that judge surfaced. "Read the enumerations, not the votes" is the claim that the useful signal lives in the **union of the distinct items the judges enumerated**, not in the aggregate tally of their verdicts. That is a real, well-established methodological principle, and it long predates LLM-judge panels.

### 1. Standard name(s)

- **Union-based aggregation of evaluators' findings** (a.k.a. "aggregate the union of unique problems," "problem-merging"), motivated by the **evaluator effect** — the empirical fact that independent evaluators overlap surprisingly little, so consensus/agreement metrics *discard* true signal that the union preserves. This is the tightest match to "read the enumerations, not the votes."
- **Capture–recapture (mark–recapture) defect estimation** — the formal extension: use the overlap *between* evaluators' enumerations to estimate how many items the union still missed. (Overlap is used as an estimator input, not as a filter — the opposite of voting.)
- Two adjacent, looser framings that also fit the phrase:
  - **Analytic vs. holistic scoring** (read the per-criterion enumerated marks, not the single overall score).
  - **Formative vs. summative evaluation** (the enumeration is the formative/diagnostic output; the vote is the summative verdict).

### 2. Which field(s) own it

- **Human–computer interaction / usability engineering** — home of the evaluator effect and union-of-problems aggregation (heuristic evaluation, usability inspection methods). *Primary owner.*
- **Software engineering (software inspection / review)** — same union logic plus the capture–recapture formalism for defect-content estimation. *Co-owner.*
- **Educational measurement / evaluation theory** — analytic-vs-holistic scoring and formative-vs-summative (adjacent).
- The modern restatement lives in **LLM-as-a-judge / "panel of LLM evaluators" (PoLL)** work, but there the *dominant* practice is vote/score aggregation — your note reads as a corrective *against* that default, which is exactly what the HCI/SE literature established decades earlier.

### 3. Oldest / most canonical treatments (real citations)

- **Nielsen, J., & Molich, R. (1990). "Heuristic Evaluation of User Interfaces." *Proc. ACM CHI '90*, Seattle, pp. 249–256.** (DOI 10.1145/97243.97281.) The canonical source for "different evaluators find different problems, so combine multiple evaluators" — i.e., aggregate the enumerations, don't trust any single verdict. *Pre-2015. High confidence in citation.*
- **Hertzum, M., & Jacobsen, N. E. "The Evaluator Effect: A Chilling Fact About Usability Evaluation Methods." *International Journal of Human–Computer Interaction*.** Originally 2001, **13(4), 421–443**; reprinted/corrected 2003, **15(1), 183–204**. The definitive statement of *why* votes/agreement mislead (any-2 agreement often 5–65%). *Pre-2015. High confidence on authors/title/journal; moderate confidence on the exact year/issue split — I'd double-check whether you want to cite the 2001 or 2003 version.*
- **Eick, S. G., Loader, C. R., Long, M. D., Votta, L. G., & Vander Wiel, S. A. (1992). "Estimating Software Fault Content Before Coding." *Proc. 14th ICSE*, Melbourne, pp. 59–65.** The seminal application of capture–recapture to inspection — the formal machinery behind "use the overlap between enumerations to estimate what's still missing." *Pre-2015. High confidence in citation; ~95% on exact page numbers.*
- **Scriven, M. (1967). "The Methodology of Evaluation." In *Perspectives of Curriculum Evaluation* (AERA Monograph Series on Curriculum Evaluation, No. 1), pp. 39–83. Chicago: Rand McNally.** Origin of the formative/summative distinction (enumeration = formative/diagnostic; vote = summative). *Pre-2015. High confidence on authorship/year/venue; moderate confidence on exact page range.*

For the analytic-vs-holistic-scoring framing I did not verify a specific seminal citation this pass, so I'm not going to assert one — the distinction itself is standard in writing-assessment/educational-measurement texts, but treat the "canonical source" for it as **unverified** here.

### 4. Confidence and hedges

- **That the note corresponds to union-of-findings + the evaluator effect: ~75%.** The structural fit ("read the enumerated findings across a panel, not the vote tally") is very clean, and it's specifically about *how to use multiple evaluators' outputs*, which is exactly the note's framing.
- **Residual ambiguity (~25%) I want to flag honestly.** The note is one line of coined vocabulary. "Enumerations" could instead mean *per-criterion rubric items from a single judge* → then the best match is **analytic vs. holistic scoring**, not panel aggregation. Or it could be a narrower LLM-eval claim ("use judges' rationales/checklists, discard the preference vote"), which is recent and not "canonical." If you can tell me whether "enumerations" are *per-judge issue-lists across a panel* (my assumption) vs. *per-criterion sub-scores within one judge*, I can collapse this to a single answer.
- **The capture–recapture link is an extension, not a synonym** — cite it only if your claim actually uses inter-judge overlap to estimate coverage; if you're purely saying "take the union and read it," Nielsen & Molich + Hertzum & Jacobsen are the load-bearing sources.
- I could not find a single named "coined term" that captures the whole phrase verbatim — it's a principle assembled from the above, not a one-word term of art. If you were hoping for a crisp single label, the closest is **"the evaluator effect (and the union-of-findings response to it)."**

Sources:
- [Nielsen & Molich 1990, CHI '90 (ACM DL)](https://dl.acm.org/doi/10.1145/97243.97281) · [CHI'90 PDF](https://concreta.com.uy/wp-content/uploads/nielsenheuristicsCHI.pdf)
- [Nielsen, "Theory Behind Heuristic Evaluations" (NN/g)](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/)
- [Hertzum & Jacobsen, "The Evaluator Effect" (Taylor & Francis, IJHCI 15(1))](https://www.tandfonline.com/doi/abs/10.1207/S15327590IJHC1501_14) · [full-text PDF](https://files01.core.ac.uk/download/pdf/188869846.pdf)
- [Evaluator effect / any-2 agreement (union vs intersection), MeasuringU](https://measuringu.com/examining-the-evaluator-effect-in-unmoderated-usability-testing/)
- [Capture–recapture in software inspections, 10-years review (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0164121203000906) · [14th ICSE 1992 program (dblp)](https://dblp.org/db/conf/icse/icse92.html)
- [Formative vs. summative / Scriven 1967 (NN/g)](https://www.nngroup.com/articles/formative-vs-summative-evaluations/)
- [Analytic vs. holistic rubrics (DePaul Teaching Commons)](https://resources.depaul.edu/teaching-commons/teaching-guides/feedback-grading/rubrics/Pages/types-of-rubrics.aspx)
- Modern restatement (LLM panels): [PoLL "panel of LLM evaluators" write-up](https://medium.com/@techsachin/replacing-judges-with-juries-llm-generation-evaluations-with-panel-of-llm-evaluators-d1e77dfb521e) · [Apple ML, "Nine Judges, Two Effective Votes"](https://machinelearning.apple.com/research/correlated-llm-evaluation-panels)
