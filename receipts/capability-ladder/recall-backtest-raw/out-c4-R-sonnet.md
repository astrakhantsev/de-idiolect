## Identification: Approval voting (in its "subset‑selection" / partial‑knowledge‑elicitation form), applied to rater/label aggregation

**1. Standard name(s)**
The procedure is **approval voting** — specifically, the variant used for eliciting and aggregating labels/answers from raters rather than electing a political candidate. In the psychometrics literature this same underlying idea (list every option you can't rule out, rather than committing to one) is called **subset selection** or **elimination/partial‑knowledge scoring**. In modern crowdsourcing/ML papers it is described as an "approval‑voting interface" coupled with an incentive‑compatible aggregation rule.

**2. Owning field(s)**
- **Social choice theory / voting theory** (political science, economics, mathematics) — the formal "approval voting" rule itself.
- **Psychometrics / educational measurement** (psychology, statistics) — the older "subset selection"/"partial knowledge" scoring tradition that anticipated it by decades.
- **Computer science — crowdsourcing, mechanism design, and computational social choice** — the modern operationalization matching your description almost line‑for‑line (raters = crowd workers, items = labeling questions, the "contract" = an incentive‑compatible payment mechanism, S(item) = the elicited *support* of a worker's belief, union pooling, fixed selection rule).

**3. Canonical treatments**

*Psychometrics origin (partial‑knowledge / subset‑selection scoring), oldest first:*
- Horst, P. (1932). "The chance element in the multiple choice test item." *Journal of General Psychology*, 6(1), 209–211.
- Coombs, C. H. (1953). "On the use of objective examinations." *Educational and Psychological Measurement*, 13(2), 308–310. — explicitly instructs test‑takers to "cross out all the alternatives which they consider wrong," i.e., list every defensible remaining candidate rather than commit to one.
- Coombs, C. H., Milholland, J. E., & Womer, F. B. (1956). "The assessment of partial knowledge." *Educational and Psychological Measurement*, 16(1), 13–37.
- Collet, L. S. (1971). "Elimination scoring: An empirical evaluation." *Journal of Educational Measurement*, 8(3), 209–214.
- Gibbons, J. D., Olkin, I., & Sobel, M. (1979). "A subset selection technique for scoring items on a multiple choice test." *Psychometrika*, 44(3), 259–270.

*Voting‑theory origin of "approval voting" as a formal rule:*
- Brams, S. J., & Fishburn, P. C. (1978). "Approval Voting." *American Political Science Review*, 72(3), 831–847. (Canonical founding paper.)
- Brams, S. J., & Fishburn, P. C. (1983). *Approval Voting*. Birkhäuser. (Book‑length canonical treatment.)

*Modern computational treatment matching your description almost exactly (raters/items/"contract"/S(item)/union pooling/fixed selection rule/full coverage/comparison to best individual rater vs. plain single‑choice voting):*
- Shah, N. B., Zhou, D., & Peres, Y. (2015). "Approval Voting and Incentives in Crowdsourcing." *ICML 2015* (PMLR v37); arXiv:1502.05696; journal version in *ACM Transactions on Economics and Computation* (2020). I pulled and read the full text — it formalizes exactly this pipeline: workers select a *set* of defensible options ("elicit the support of the worker's belief"), a strictly‑proper/incentive‑compatible payment ("contract") is designed so the worker's dominant strategy is to report that support exactly — no padding, no under‑reporting — and it offers interface variants with and without a forced single final pick (its Figure 1a/1b).
- Procaccia, A. D., & Shah, N. (2015). "Is Approval Voting Optimal Given Approval Votes?" *NIPS 2015*. This is the piece that directly studies your last step: given the pooled (union) approval sets, is simply counting approvals the right fixed rule for picking the single best answer, and under what conditions does it match/beat picking any one individual's answer.

**4. Confidence**
- **High confidence** on the core identification (approval voting / subset‑selection scoring) and on the psychometrics lineage (Horst 1932 → Coombs 1953/1956 → Collet 1971 → Gibbons, Olkin & Sobel 1979) and the voting‑theory lineage (Brams & Fishburn 1978/1983) — these are well-established, frequently cross-cited, and the Shah/Zhou/Peres paper's own related-work section cites this exact chain as the ancestry of "approval voting" for elicitation.
- **Medium-high confidence** that Shah, Zhou & Peres (2015) and Procaccia & Shah (2015) are the closest match to your *specific* pipeline (per-item raters, "contract," S(item), union pooling, fixed selection rule, full coverage). I verified this against the actual paper text, not just an abstract.
- **Hedge:** I could not verify verbatim that your precise comparative claim ("pooled approval sets match/beat the best individual rater's accuracy, while pooling single committed picks by voting falls well short of the best member") is stated as a single quoted result in one paper — it's consistent with the motivating examples and theoretical framing in both papers above, but your phrasing reads as a paraphrase/composite rather than a direct quotation, so I can't point to one exact sentence as its source. Likewise "fixed line format, one line per candidate, with a short paraphrase" matches the *spirit* of these interfaces (e.g., Shah et al.'s "Select ALL options that could be..." checklist) but isn't a literal quote from any source I found — the puzzle description appears to be a deliberately genericized paraphrase of this literature rather than a direct citation of one paper's exact wording.

Sources:
- [Approval Voting and Incentives in Crowdsourcing (arXiv:1502.05696)](https://arxiv.org/abs/1502.05696)
- [Approval Voting and Incentives in Crowdsourcing (PDF, full text used for verification)](https://arxiv.org/pdf/1502.05696)
- [Is Approval Voting Optimal Given Approval Votes? (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/a2137a2ae8e39b5002a3f8909ecb88fe-Abstract.html)
- [Approval Voting and Incentives in Crowdsourcing (ICML 2015 proceedings page)](https://proceedings.mlr.press/v37/shaha15.html)
