I have enough to answer confidently. Here is my identification.

## 1. What this concept is called

The defining move — each rater, instead of committing to one pick, **lists every candidate they find acceptable/defensible, and you aggregate over those approved sets rather than over single picks** — is the textbook definition of **approval voting** (a.k.a. **approval balloting**, "approve as many as you like"). What you've described is specifically its use to recover a *correct* answer rather than a *preferred* one, which is the sub-area called **epistemic (truth-tracking) approval voting** / **approval voting as a maximum-likelihood estimator**.

Two adjacent labels the same construction travels under, depending on field:
- The general framing "pool the *sets* raters put forward, not their single votes, and you can beat plurality/majority voting and even the best individual" is the **epistemic social choice / Condorcet-jury** tradition ("wisdom of crowds").
- In ML/NLP annotation, the mechanical step "take the **union** of each annotator's candidate label-set, then apply a fixed decision rule" is usually described plainly as **union aggregation of set-valued (multi-label) annotations** — but that literature has no crisp single coined name; it is approval voting re-derived for annotation.

The one feature that pins it down is set-valued ballots (list all defensible) + aggregation over those sets + a pre-committed selection rule + full coverage + the comparative accuracy claim against single-pick voting. That is approval voting, in an epistemic setting.

## 2. Which field(s) own it

- **Social choice theory / voting theory** (political science, economics, theoretical CS) — owns approval voting proper.
- **Epistemic social choice / computational social choice** — owns the truth-tracking accuracy claim (the "beats plurality, can beat the best member" part). Condorcet-jury-theorem lineage.
- **Crowdsourcing / human computation / NLP annotation aggregation** — where the "raters, items, labels, union" instantiation lives.

## 3. Oldest and most canonical treatments (real citations)

**Approval voting — canonical, pre-2015:**
- Brams, S. J., & Fishburn, P. C. (1978). "Approval Voting." *American Political Science Review*, 72(3), 831–847. — The founding paper; introduces "vote for as many candidates as you approve of." (Confirmed via APSR/Cambridge Core.)
- Brams, S. J., & Fishburn, P. C. (1983). *Approval Voting.* Birkhäuser (2nd ed. Springer, 2007). — The canonical book-length treatment.

**Epistemic / truth-tracking lineage (the "match or beat the best member" claim):**
- Condorcet, M. de (1785). *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix.* — Origin of the jury-theorem "aggregation can beat the individual" idea (uncertain that the author intends this as *the* source, but it is the historical root).
- Procaccia, A. D., & Shah, N. (2015). "Is Approval Voting Optimal Given Approval Votes?" *NeurIPS/NIPS 2015.* — Treats approval voting as a maximum-likelihood estimator of the objectively best alternative; the direct formalization of "use the approved sets to pick the correct answer." (2015, so it does not by itself satisfy the pre-2015 requirement — Brams & Fishburn 1978 does.)
- Caragiannis, I., Nath, S., Procaccia, A. D., & Shah, N. (2017). "Truthful Univariate Estimators" / and the line "Truth-tracking via Approval Voting: Size Matters" (Fernández Peters et al., AAAI 2022) — the modern truth-tracking-approval-voting subfield, including the "smaller/more selective ballots are more reliable" refinement.

**Conitzer & Sandholm** (2005), "Common Voting Rules as Maximum Likelihood Estimators," *UAI 2005* — pre-2015 anchor for viewing voting rules (approval among them) as estimators of a hidden true answer.

## 4. Confidence and hedges

- **High confidence** that the core concept is **approval voting / approval balloting** and that its distinguishing feature (list all acceptable candidates; aggregate over the sets, not the single picks) is exactly what your description operationalizes. This is the one claim I'd stand behind firmly.
- **High confidence** on the Brams & Fishburn 1978/1983 citations (verified in APSR/Cambridge Core and Springer) — these are the canonical, pre-2015 sources.
- **Medium-high confidence** that the *accuracy* framing ("can match or beat the best individual rater; single-pick voting falls short") is the **epistemic/truth-tracking approval-voting + Condorcet-jury** literature (Procaccia & Shah 2015; Conitzer & Sandholm 2005). I'm confident about the mapping; I'm **less sure which of these the concept's author would treat as canonical**, and Procaccia & Shah is 2015, not before it.
- **Deliberate hedge:** your description is written in domain-neutral "rater/item/label/S(item)/don't-pad/one-line-per-candidate/the-list-is-the-response" language that reads like a **modern (likely LLM-era) annotation or LLM-as-judge methods section reinventing approval balloting for answer extraction**. If that's the origin, it may carry its own coined name I could not locate — my searches for the specific "list all defensible readings → union → fixed rule → beats best annotator" phrasing returned nothing with a distinct established term. So: **the underlying established concept is approval voting (epistemic variant); a specific paper-local name, if one exists, I could not identify** and would flag as unknown rather than guess.
- **Lower confidence / explicitly uncertain:** the single-rater edge case ("one or more raters," so it works with just one) is *not* approval voting proper (which is inherently multi-voter). With one rater it's better described as **set-valued elicitation + a fixed decision rule**; this is a real but less-cleanly-named idea, and I'd mark any single crisp citation for it as uncertain.

Sources:
- [Brams & Fishburn (1978), "Approval Voting," APSR 72:831 — SciRP reference](https://www.scirp.org/reference/referencespapers?referenceid=2663586)
- [Approval Voting — American Political Science Review (Cambridge Core)](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/approval-voting/7CE5DEEE235794B0B12F76ADAE621482)
- [Procaccia & Shah (2015), "Is Approval Voting Optimal Given Approval Votes?" NeurIPS](https://papers.nips.cc/paper/2015/hash/a2137a2ae8e39b5002a3f8909ecb88fe-Abstract.html)
- [Fernández Peters et al., "Truth-tracking via Approval Voting: Size Matters" (arXiv)](https://arxiv.org/pdf/2112.04387)
- [Caragiannis et al., "Learning a Ground Truth Ranking Using Noisy Approval Votes" (IJCAI 2017)](https://www.ijcai.org/proceedings/2017/0022.pdf)
- [Conitzer & Sandholm, "Common Voting Rules as Maximum Likelihood Estimators" (Semantic Scholar)](https://www.semanticscholar.org/paper/Common-Voting-Rules-as-Maximum-Likelihood-Conitzer-Sandholm/3fb66e141e6a09d1de9ba387d1570a240f8f450a)
- [Epistemic Approval Voting thesis (HAL) — survey of the truth-tracking-approval literature](https://theses.hal.science/tel-04164259/document)

**Bottom line:** It's **approval voting** — set-valued/"approve-all-defensible" ballots aggregated over the approved sets — used in its **epistemic, truth-tracking** mode. Founding citation: **Brams & Fishburn, "Approval Voting," APSR 72(3):831–847, 1978** (book, 1983). The "beats plurality, can beat the best member" property is the epistemic-social-choice/Condorcet-jury reading of it (Procaccia & Shah 2015; Conitzer & Sandholm 2005). If your source is a recent LLM-annotation paper, it is most likely reinventing approval balloting under a local name I could not find.
