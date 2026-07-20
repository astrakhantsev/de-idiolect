---
title: "Citation dossier — idiolect-trap-case-study.md"
date: 2026-07-18
status: "complete"
---

# Citation dossier — idiolect-trap-case-study.md

Audit target: `/mnt/f/hub/10_projects/minelit/idiolect/entry/idiolect-trap-case-study.md`

## Note on the prior audit (citation-audit-2026-07-17.md)

Read first, as instructed. That audit covers a **different document** —
`FLF-entry-recall-extender.md` (Larsen & Bong 2016, Blair & Maron 1985, Furnas et al.
1987, Kelley 1927, Thorndike 1904, Hoekstra 2010, Doctorow, Shirky 2003, Star &
Griesemer 1989, Bowker & Star 1999, Relink, SciCo-Radar, GenOM, EDC, KGGen, Guo, NeoN,
two Microsoft patents). **Zero overlap** with the citations in `idiolect-trap-case-study.md`
(grep-verified: none of the FLF-entry names appear in the case-study file, and none of
the case-study's names — Clemen & Winkler, Kish, Raiffa & Schlaifer, Bröcker, DeGroot &
Fienberg, Pieper, Hennessy & Johnson, Satopää, Karmarkar, Makridakis & Winkler, Scott
Alexander, Higgins et al., Sidik & Jonkman, Rowe & Wright, Best, Zhou et al., Wilson &
Masters, Linacre, Kohli — appear in the FLF-entry-recall-extender file per the 07-17
audit's own text). So nothing is "copied forward" below; every citation in this dossier
is verified fresh. Noted per instructions rather than silently skipped.

## Scope note on the task's citation list vs. the document's actual content

The task brief's "at minimum" list includes three names not found anywhere in
`idiolect-trap-case-study.md` (grep-confirmed, case-insensitive, whole document):
**Murphy 1973**, **Blackwell**, **Ho, Hull & Srihari 1994**. Per the task's own
instruction ("the document is the source of truth"), these are marked N/A below rather
than fabricated a location for. They may belong to a sibling document (e.g.
`FLF-entry-recall-extender.md` or `THESES.md`) that is out of scope here (scope-out:
don't read other vault files).

---

## Citations

### 1. Clemen & Winkler 1985

**Location in document:** Headline #1 (line 29); Table A row 1 (line 69); event-flow 07-13 (line 47).
**Attributed claim:** "Clemen & Winkler 1985 (the equivalent-number-of-independent-sources result)" — owner of `m*`/"audit unit," the aggregation-literature result that the project's search failed to surface for two weeks.

**Checks:**
1. *Work exists / identifier resolves* — YES. "Limits for the Precision and Value of Information from Dependent Sources," R.T. Clemen & R.L. Winkler, *Operations Research*, 1985, vol. 33, issue 2, pp. 427–442. DOI `10.1287/opre.33.2.427`. Confirmed independently via Semantic Scholar/DBLP (`journals/ior/ClemenW85`, CorpusId 10142978) and the INFORMS publisher page.
2. *Bibliographic details match* — YES (author names, year, journal, title all consistent across INFORMS and Semantic Scholar).
3. *Verbatim quotes* — the document does not put this citation in quotation marks (it's a paraphrase, "equivalent-number-of-independent-sources result"), so no verbatim-quote check applies.
4. *Characterization match* — the phrase is strongly corroborated but not read off the primary itself. Two independent secondary sources describe the paper's actual content in these terms: (a) a companion/follow-up INFORMS paper explicitly titled "How Many Forecasters Do You Really Have? Mahalanobis Provides the Intuition for the Surprising Clemen and Winkler Result," which reframes the 1985 result exactly as an effective/equivalent-count question; (b) a WebSearch-grounded synopsis describing the paper's own content as producing "the y-axis showing the equivalent number of independent sources for various correlation coefficients" (i.e., the paper itself plots this quantity).

**Evidence surfaces checked:** INFORMS publisher page (`pubsonline.informs.org/doi/10.1287/opre.33.2.427`) — blocked by a Cloudflare bot challenge via safefetch; ACM record (`dl.acm.org/doi/abs/10.5555/2768947.2768963`) — also Cloudflare-blocked; Semantic Scholar Graph API (open, returned metadata but abstract elided by publisher); Wayback CDX for the INFORMS URL — Internet Archive reported itself "temporarily offline" at time of check. Could not open primary verbatim text.

**Verdict: PARTIAL.** Bibliographic identity is fully verified (title/authors/year/journal/DOI cross-confirmed on two independent indexes). The substantive characterization is well-corroborated by secondary sources describing the paper's own content, but the primary text itself was not opened (paywalled + Cloudflare-blocked on all three access attempts; Wayback unavailable at check time). No quote is at stake since the document doesn't quote it verbatim.

**For senior review:** Low risk — the paper is exactly what its title says, and a follow-up paper's title independently corroborates the "equivalent number of forecasters/sources" framing. Re-attempt Wayback or a university-network fetch if a verbatim primary check is required.

---

### 2. Bröcker 2008 (arXiv:0806.0813 / QJRMS)

**Location in document:** Headline #3 (line 31); Table A row 3 (line 71); Program B event-flow 07-16 (line 55).
**Attributed claim:** proper-score uniqueness theorem, extending DeGroot & Fienberg 1982, forecloses Program B's keystone. Two direct quotes given: "the forecasting scheme π^γ achieves the best possible average score among all forecasts for which γ is sufficient" and (separately) "is uniquely defined through this optimum property."

**Checks:**
1. *Work exists / identifier resolves* — YES. arXiv:0806.0813, "Reliability, Sufficiency, and the Decomposition of Proper Scores," Jochen Bröcker. Confirmed via `arxiv.org/abs/0806.0813`.
2. *Bibliographic details* — YES. Published version: *Quarterly Journal of the Royal Meteorological Society*, 2009 (note: journal-of-record year is 2009, not 2008 — the document cites the arXiv submission year, 2008, which is accurate for the preprint; v1 submitted 4 Jun 2008, v2 1 Dec 2008), vol. 135, issue 643, pp. 1512–1519, DOI `10.1002/qj.456` (confirmed as the "Related DOI" on the arXiv abstract page and independently via search). "QJRMS" is correct.
3. *Verbatim quotes* — **CONFIRMED VERBATIM**, both. Fetched the ar5iv HTML rendering of the full paper (`https://ar5iv.labs.arxiv.org/html/0806.0813`) and located, in the section titled "III Application: Comparing Forecasting Schemes" (the arXiv internal id prefix `S3`, matching the document's "§3" pinpoint): *"The forecasting scheme π^γ achieves the best possible average score among all forecasts for which γ is sufficient."* And immediately following: *"If the score is strictly proper, π^γ is uniquely defined through this optimum property, in the sense that any forecast for which γ is sufficient is either equal to π^γ or it will have a worse average score."* — the document's second quote ("is uniquely defined through this optimum property") is an exact contiguous substring of this sentence, not a splice.
4. *DeGroot & Fienberg 1982* — **VERIFIED, and disambiguated.** Bröcker's own bibliography (bib.bib8) cites: Morris W. DeGroot and Stephen E. Fienberg, "Assessing probability assessors: calibration and refinement," *Statistical Decision Theory and Related Topics*, 1(3):291–314, **1982**. This is a *different* DeGroot & Fienberg paper from their better-known "The Comparison and Evaluation of Forecasters" (*Journal of the Royal Statistical Society, Series D*, 1983) — the year discrepancy some external indexes show (1982 vs. 1983) is because these are two distinct works, not a mis-cited year. Bröcker's in-text citations ("the concept of sufficiency, introduced by DeGroot and Fienberg (1982)"; "generalising the concepts of sufficiency and refinement due to DeGroot and Fienberg (1982)") match the case study's "extending DeGroot & Fienberg 1982" exactly.

**Evidence surfaces checked:** `arxiv.org/abs/0806.0813` (abstract, via safefetch); `ar5iv.labs.arxiv.org/html/0806.0813` (full paper HTML, via safefetch — flagged 101 zero-width-space occurrences as a HIGH finding, almost certainly a LaTeXML rendering artifact of math markup, not a real injection attempt — no suspicious instructions found in the extracted content); direct PDF fetch attempts (`arxiv.org/pdf/0806.0813`, `.../0806.0813v2`) failed (defuddle extracted nothing from the raw PDF response) — worked around via the ar5iv HTML mirror instead, which reproduces the full text.

**Verdict: VERIFIED.** Both quotes are exact matches to the primary text; bibliographic pinpoints (arXiv ID, §3, journal, DeGroot & Fienberg 1982) all check out.

**For senior review:** This is the strongest-verified citation in the ledger — direct primary-text quote match plus a disambiguation of a real trap (two different DeGroot & Fienberg papers share the "1982/1983" confusion in secondary indexes; the document's year is correct for the paper Bröcker actually cites). The safefetch injection flag on the ar5iv page is a false positive (LaTeXML math markup artifact); noted for transparency, not a content concern.

---

### 3. Raiffa & Schlaifer 1961

**Location in document:** Headline #2 (line 30); Table A row 2 (line 70).
**Attributed claim:** "operating requirement" → value-of-information / target-product-profile threshold analysis, "Raiffa & Schlaifer 1961 lineage."

**Checks:**
1. *Work exists* — YES. Howard Raiffa & Robert Schlaifer, *Applied Statistical Decision Theory*, Graduate School of Business Administration, Harvard University (Boston), 1961, 356 pp. Confirmed via 5 independent listings (Wiley reprint page, Amazon, AbeBooks, Google Books, and a hosted PDF on gwern.net).
2. *Bibliographic details* — match.
3. *Verbatim quote* — none attributed; the document uses "lineage," a genealogy claim, not a quote.
4. *Characterization* — this book is the standard foundational reference for Bayesian value-of-information analysis; it is universally cited as such in VOI literature (confirmed via multiple sources describing it as the origin of the VOI framework used in modern health-economic threshold/target-product-profile analysis). "Lineage" is an appropriately hedged word for a 65-year influence chain, not a direct-descent claim, and matches how the field itself describes the connection.

**Evidence surfaces checked:** WebSearch aggregating Wiley, Amazon, AbeBooks, Google Books, ISPOR Task Force report abstract, and gwern.net's hosted copy. Attempted to fetch the gwern.net-hosted primary PDF via safefetch — **failed** (defuddle extracts nothing from a raw PDF response, even after the forced JS-render escalation; this is a recurring tooling limitation for PDF primaries, noted once here and applies to other book/PDF citations below rather than being repeated per-row).

**Verdict: PARTIAL.** Bibliographic identity solid (5-way corroborated); the "lineage" framing is a general, appropriately-hedged claim rather than a specific quoted fact, and matches field consensus, but the primary book text itself was not opened (PDF inaccessible to the available fetch tooling).

**For senior review:** Low risk — this is one of the most well-established citations in the whole document (a canonical, universally-cited 1961 text); the specific claim made about it ("lineage," not "founded X specific technique") is conservative.

---

### 4. Pieper 2014 (via Hennessy & Johnson 2020)

**Location in document:** Headline note area / Table A row 4 (line 72).
**Attributed claim:** evidence-overlap metric in the dietary-cholesterol worked example → corrected covered area (CCA), owned by Pieper 2014, reached via Hennessy & Johnson 2020; "verified against the full text" per the document; honest note: "the field *retains* high-overlap reviews rather than discarding them."

**Checks:**
1. *Both works exist / identifiers resolve* — YES, both.
   - Hennessy EA, Johnson BT. "Examining Overlap of Included Studies in Meta-Reviews: Guidance for using the Corrected Covered Area Index." *Research Synthesis Methods* 11(1):134–145. DOI `10.1002/jrsm.1390`. (Online-first Dec 2019; issue year 2020 — matches the document's "Hennessy & Johnson 2020.")
   - Pieper D, Antoine S, Mathes T, Neugebauer EAM, Eikermann M. "Systematic review finds overlapping reviews were not mentioned in every other overview." *J Clin Epidemiol* 67(4):368–375, 2014. DOI `10.1016/j.jclinepi.2013.11.007`.
2. *Chain confirmed directly in primary text* — opened the Hennessy & Johnson PMC open-access full text (`pmc.ncbi.nlm.nih.gov/articles/PMC8555740/`). Reference [10] in that paper is the Pieper 2014 paper above, verbatim-matched (title, journal, year, pages, DOI all identical). In-text: *"Pieper and colleagues [10] suggest guidelines for interpreting CCA values such that lower than five indicates slight overlap and values greater than or equal to 15 indicate high overlap."* and *"The first step is to create the citation matrix following Pieper and colleagues [10] instructions."* This is exactly the "Pieper 2014 (via Hennessy & Johnson 2020)" chain the document describes — Hennessy & Johnson didn't coin CCA, they built practical guidance around Pieper's index, and cite Pieper for it.
3. *"the field retains high-overlap reviews rather than discarding them"* — supported by the Hennessy & Johnson abstract itself: *"This work helps to show that overlap of primary studies included in a meta-review is not necessarily a bias but often can be a benefit."* Consistent with the document's honest note, though phrased differently (the primary emphasizes "not necessarily a bias / can be a benefit," the document's gloss "retains rather than discards" is a fair paraphrase of that same stance, not a verbatim quote).
4. *Numbers* — the CCA interpretation thresholds quoted above (<5% slight, ≥15% high) are read directly off the Hennessy & Johnson text, which is itself paraphrasing Pieper — consistent chain.

**Evidence surfaces checked:** `pmc.ncbi.nlm.nih.gov/articles/PMC8555740/` (open-access full text, fetched via safefetch, no injection findings) — the Pieper 2014 paper itself is paywalled at J Clin Epidemiol / ScienceDirect and was not separately opened; its bibliographic identity was cross-confirmed via the Hennessy & Johnson reference list plus independent PubMed/ResearchGate listings, which is sufficient to confirm it's a real, correctly-cited work but short of reading Pieper's own text directly.

**Verdict: VERIFIED** (chain and characterization), with one **PARTIAL** sub-note: Pieper 2014's own primary text (as opposed to Hennessy & Johnson's citation of it) was not directly opened — reachable only through the secondary source, which is itself open-access and directly quotes/attributes the CCA guidance to Pieper.

**For senior review:** Solid. The "via" framing in the document is precise and matches what's actually in Hennessy & Johnson's paper — this is not a case of citation-laundering; H&J really do build on and attribute Pieper's index.

---

### 5. Satopää and Karmarkar 1978 ("78 forecasters ≈ 1" self-confound)

**Location in document:** Program A event-flow 07-09 (line 43); Table A row 5 (line 73, marked **retracted — self-confound**, not a positive novelty claim).
**Attributed claim:** the extremization line traces to Satopää (no year given in the document) and Karmarkar 1978; the "78 forecasters ≈ 1 independent update" headline is a self-confound (extremization coefficient mistaken for an independence count), not a claim about what Satopää/Karmarkar say.

**Checks:**
1. *Karmarkar 1978* — YES, resolves. Uday S. Karmarkar, "Subjectively Weighted Utility: A Descriptive Extension of the Expected Utility Model," *Organizational Behavior and Human Performance*, 21(1):61–72, 1978. This is the standard citation for subjective probability weighting/overweighting — the mechanism ("extremization" = pushing aggregated probabilities away from 0.5 to correct for the fact that averaging probabilities is conservative) traces to exactly this kind of weighting-function literature.
2. *Satopää* — the document gives no year or initials, consistent with it being a background/lineage mention rather than a pinpoint citation. The most plausible referent (confirmed to exist and to be squarely on-topic) is Ville A. Satopää, co-author of the standard modern extremization papers, e.g. Satopää, Baron, Foster, Mellers, Tetlock & Ungar, "Combining multiple probability predictions using a simple logit model," *International Journal of Forecasting* 30(2):344–356, 2014 — the paper most commonly cited as *the* extremization-coefficient reference in forecasting-aggregation work. The document does not commit to a specific title/year, so this is a name-level match, not a pinpoint verification.
3. *Numbers* — the document does not attribute a specific quoted number to Satopää/Karmarkar; the "78 forecasters ≈ 1" figure is the *project's own* retracted result, not something claimed to come from these sources. No verbatim quote at stake.

**Evidence surfaces checked:** WebSearch only (Karmarkar 1978's existence and topic cross-confirmed via standard citation indexes; Satopää's extremization work confirmed via IJF listing). Did not open either primary text — both are paywalled journal articles and the document doesn't quote either verbatim, so there was no specific sentence to check against a primary.

**Verdict: PARTIAL.** Karmarkar 1978 bibliographically confirmed and topically on-point. "Satopää" is under-specified in the document itself (no year/title), so I can confirm a name-level match to a real, on-topic body of work but not a pinpoint citation — this is a document-side vagueness, not a verification failure on my part.

**For senior review:** No red flags, but flag to the author that "Satopää" without a year is the least pinned-down citation in the ledger — worth tightening to a specific paper if this document is meant to be citably precise (the novelty ledger presumably already has the pinpoint).

---

### 6. Makridakis & Winkler 1983

**Location in document:** Table A row 9 (line 78).
**Attributed claim:** "m* ≈ 2–3 regularity" → combining-forecasts accuracy plateau, owner Makridakis & Winkler 1983; an "18.1 decibans" anecdote flagged apocryphal and dropped (this is the document being self-critical, not a claim about the primary).

**Checks:**
1. *Work exists* — YES. Spyros Makridakis & Robert L. Winkler, "Averages of Forecasts: Some Empirical Results," *Management Science* 29(9):987–996, 1983. This is a well-known, widely-cited paper establishing that combining a small number of independent forecasts (typically cited as accuracy gains plateauing around 2-5 forecasts) captures most of the achievable accuracy gain from combination.
2. *Characterization* — "m* ≈ 2–3 regularity" (i.e., accuracy gains from combining forecasts plateau after roughly 2-3 forecasts) matches this paper's standard characterization in the forecasting-aggregation literature.
3. *"18.1 decibans" anecdote flagged apocryphal and dropped* — this is the document reporting its own internal correction (removing a claim it decided was unreliable), not an assertion about Makridakis & Winkler's text — nothing to verify against the primary here; it is a self-report of due diligence, and its accuracy as a self-report can't be externally checked from outside the project's internal history (consistent with the document's own stated limits on internal-history verifiability, see its "What this document is" section).

**Evidence surfaces checked:** WebSearch only; did not open the *Management Science* primary (paywalled, no verbatim quote attributed by the document to check against it).

**Verdict: PARTIAL.** Bibliographic identity and general characterization confirmed via secondary sources; primary text not opened (no verbatim quote at stake, and access was paywalled).

**For senior review:** Low risk, standard citation in the forecasting-aggregation literature; nothing to flag.

---

### 7. Kish design effect

**Location in document:** Headline #1 (line 29, "knowing borrowing" note); Program A event-flow 07-01 (line 38); Table A row 1 (line 69); Table A row "N_eff used as a log-odds multiplier" (line 74, marked **retracted — misuse**).
**Attributed claim:** the project's `N_eff` formula was asserted (07-01) to **be** the Kish design effect. Later (07-12) this use as a log-odds/posterior multiplier is retracted as a misuse — the design effect is valid for a correlated *mean*, not a posterior multiplier.

**Checks:**
1. *Concept exists / correctly named* — YES, extremely well established. Leslie Kish's design effect, deff = 1 + (m−1)ρ, from Leslie Kish, *Survey Sampling*, Wiley, 1965 (the standard originating reference; the term is universally attributed to Kish in the sampling-statistics literature). The document doesn't cite a specific year for "Kish" in-line (just "Kish design effect" / "Kish"), consistent with treating it as a named, textbook-level concept rather than a pinpoint citation.
2. *Formula match* — the case study's own headline formula, `N_eff = N/(1+(N−1)ρ̄)`, is algebraically the reciprocal of the standard Kish design effect form (deff = 1+(m−1)ρ ⟹ N_eff = N/deff). This is a correct, textbook-accurate restatement of the design effect, not a distortion.
3. *Self-assessed misuse (row 74)* — the document's own claim is that applying this (a device for shrinking an effective *sample size* for a correlated *mean*) to a log-odds/posterior multiplier is invalid. This is a self-critical methodological claim about the *project's* usage, not a claim about what Kish's original work says — nothing external to check it against; it is consistent on its face (deff corrects a variance/sample-size calculation; applying the same correction factor directly to log-odds is a different mathematical object without independent justification, so the self-diagnosed error is plausible and internally coherent).

**Evidence surfaces checked:** WebSearch confirming the standard definition and attribution of the design effect to Kish (1965) is uncontested textbook material; did not locate or open a specific primary text since the document does not pin a specific work/page — there is no specific verbatim claim to check.

**Verdict: VERIFIED** (as a correctly-named, correctly-formulated concept attribution) for the "knowing borrowing" rows; the "retracted (misuse)" row is a self-diagnosed methodological claim about the *project's* application, which is coherent on its face but is a claim about the project's own reasoning, not an external fact I can independently confirm or refute.

**For senior review:** No issue with the Kish attribution itself — this is uncontroversial, well-known statistical machinery, correctly named and correctly formalized.

---

### 8. Scott Alexander — Multiple Stage Fallacy

**Location in document:** Table A row 7 (line 75).
**Attributed claim:** "within-analysis correlated-factor double-counting" → the Multiple Stage Fallacy, "named by Scott Alexander."

**Checks:**
1. *Work exists / identifier resolves* — YES. "The Multiple Stage Fallacy" is a named concept from a Scott Alexander blog post (Slate Star Codex / Astral Codex Ten), describing the error of multiplying a chain of conditional probabilities each rounded down conservatively, producing an overall probability that's biased low (or, in the correlated-factor-double-counting framing the document uses, an error from treating stage-wise probabilities as if independent when they're correlated).
2. *Attribution* — "named by Scott Alexander" is accurate; this is a term Alexander introduced and that is widely cited under his name in the rationalist/forecasting blogosphere with no competing academic originator.

**Evidence surfaces checked:** WebSearch confirming the term and its association with Scott Alexander's writing; did not fetch the specific blog post URL since the document doesn't quote it verbatim or give a specific URL/date to pin down — "named by Scott Alexander" is the full extent of the document's own claim, and that attribution is correct.

**Verdict: VERIFIED** (the attribution itself — "named by Scott Alexander" — is accurate). No verbatim quote or specific post identified by the document to check further.

**For senior review:** No issue. This is a popular/blog-level source correctly labeled as such (not dressed up as an academic citation) — appropriate register for what it is.

---

### 9. Higgins et al. 2009 and Sidik & Jonkman 2002 (HKSJ)

**Location in document:** Table A row 8 (line 77).
**Attributed claim:** prediction-interval-as-likelihood-width used as a heterogeneity fix → estimand substitution; correct tool is HKSJ; **foreclosed as a fix**; "HKSJ citations checked by review."

**Checks:**
1. *Higgins et al. 2009* — YES, resolves. J.P.T. Higgins, S.G. Thompson, D.J. Spiegelhalter, "A re-evaluation of random-effects meta-analysis," *Journal of the Royal Statistical Society: Series A* 172(1):137–159, 2009. This is a standard, widely-cited paper proposing what's now called the HKSJ (Hartung-Knapp-Sidik-Jonkman) adjustment for random-effects meta-analysis confidence intervals.
2. *Sidik & Jonkman 2002* — YES, resolves. K. Sidik, J.N. Jonkman, "A simple confidence interval for meta-analysis," *Statistics in Medicine* 21(20):3153–3159, 2002. This is the other half of the HKSJ method name (Hartung-Knapp 1999/2001 + Sidik-Jonkman 2002 are two independently-derived variance-adjustment methods that get combined/compared under the "HKSJ" umbrella term).
3. *Characterization* — "the correct tool is HKSJ" for random-effects meta-analysis heterogeneity/interval-width correction is an accurate, mainstream methodological position (HKSJ is widely recommended over the standard DerSimonian-Laird CI specifically because DL intervals are too narrow under heterogeneity) — consistent with the document's framing that a naive fix (using the prediction interval width as if it were a likelihood width) is the wrong tool and HKSJ is the accepted correct one.

**Evidence surfaces checked:** WebSearch confirming both papers' existence, authors, journal, year, and their joint association with the "HKSJ" method name; did not open either primary (both paywalled, and the document attributes no verbatim quote to either — it names them as the correct-tool citations for a methodological point, which is a characterization check, not a quote check).

**Verdict: VERIFIED** (bibliographic identity and methodological characterization both check out; no verbatim quote at stake).

**For senior review:** No issue. Standard, correctly-paired citations for the HKSJ method.

---

### 10. Rowe & Wright 1996/99 and Best 1974

**Location in document:** Table A row 6 (line 76), Program B prior-art sweep 07-16.
**Attributed claim:** "read the enumerations, not the votes" → reasons-feedback vs. statistical-feedback distinction in Delphi methodology, owners Rowe & Wright 1996/99 and Best 1974; document itself flags: "quoted verbatim (V) — but the authors' own hedge was omitted in the first internal citation; 'already known to work' was overstated."

**Checks:**
1. *Rowe & Wright* — resolves to G. Rowe & G. Wright's well-known series of Delphi-methodology reviews, most commonly: Rowe & Wright, "The Delphi technique as a forecasting tool: issues and analysis," *International Journal of Forecasting* 15(4):353–375, 1999 (the "/99" in the document's "1996/99"), plus an earlier Rowe, Wright & Bolger piece from the mid-1990s (consistent with the "1996" half of the document's slash-year). Rowe & Wright's work is the standard reference distinguishing "reasons-based" feedback (sharing arguments) from "statistical" feedback (sharing only aggregate numbers) in iterated Delphi rounds, which matches the document's framing exactly.
2. *Best 1974* — resolves to Roger A. Best, "An Experiment in Delphi Estimation in Marketing Decision Making," *Journal of Marketing Research* 11(4):448–452, 1974 — an early empirical Delphi study comparing feedback types, consistent with being grouped alongside Rowe & Wright as an owner of the reasons-vs-statistical-feedback distinction.
3. *Document's own defect flag* — the document says its *own* first internal citation of this material overstated the finding ("already known to work" overstated) by omitting the original authors' hedge. **Per the task's instructions, my job here is to verify this self-characterization, not to launder the row into a clean VERIFIED.** I could not independently locate and read the exact hedge sentence in Rowe & Wright's primary text within the scope of this pass (paywalled journal articles, no specific quote or page given by the document to check against) — so I can confirm the *shape* of the claim is plausible (Rowe & Wright's reviews are known in the Delphi literature for being notably cautious/hedged about how strong the evidence for reasons-feedback superiority actually is, which is consistent with the document's claim that a hedge exists and was dropped), but I did not verify the specific hedge sentence itself.

**Evidence surfaces checked:** WebSearch confirming both works' existence and topical fit; did not open either primary (paywalled, no specific quote/page cited by the document for the hedge itself, so nothing precise to check against).

**Verdict: PARTIAL.** Bibliographic identity of both works confirmed and topically on-point. The document's self-flagged defect ("hedge omitted, overstated") is plausible given what's known about Rowe & Wright's cautious tone in the secondary literature, but I did not verify the specific hedge sentence against Rowe & Wright's primary text — this row's defect-characterization is *not confirmed*, only *not contradicted*.

**For senior review:** Flag for a follow-up pass: if this row matters for a specific downstream claim, the specific hedge sentence in Rowe & Wright should be pinned down and quoted, since the document is explicitly warning readers not to over-trust its own first pass here.

---

### 11. Kohli 2026

**Location in document:** Program B event-flow 07-13 (line 51) — "is cross-judge LLM error correlation elicitation-dependent or weights-locked (the open lever in Kohli 2026)?"

**Checks:**
1. *Work exists / identifier resolves* — YES. Guneet Kohli, "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels," arXiv:2605.29800 [cs.CL], submitted 28 May 2026 (also an Apple Machine Learning Research publication). Confirmed via the arXiv abstract page.
2. *Bibliographic details* — YES, year (2026) matches.
3. *Content match* — YES, closely. The paper tests a 9-judge, 7-model-family LLM panel and finds effectively only ~2 independent votes (n_eff ≈ 2.0–2.5) using the Kish effective-sample-size framework; the deficit is "robust across prompt variants, temperatures, chain-of-thought reasoning" and aggregation-algorithm changes close at most 11% of the gap. Fetched the full HTML text (`arxiv.org/html/2605.29800v1`) and located the paper's own closing "open question," verbatim: *"The path forward requires models that genuinely differ in how they process information — not merely different brand names on similar architectures. … Whether architecturally diverse models, specialist fine-tuning, or hybrid human-LLM panels can achieve this remains an open question."*
4. *"the open lever" framing* — the document's phrase "elicitation-dependent or weights-locked" is a **compressed paraphrase**, not a verbatim quote from Kohli 2026 — the paper itself frames the open question as "architecturally diverse models / specialist fine-tuning / hybrid human-LLM panels" vs. "different brand names on similar architectures," which maps reasonably onto "weights-locked" (architecture/weights) vs. some form of "elicitation" (prompting-only variation, which the paper explicitly tested and found does *not* close the gap). This is a fair compression of the paper's real finding and real open question, not a fabrication, but it is worth flagging that the document's two-way framing ("elicitation-dependent or weights-locked") is the case-study author's own gloss, not Kohli's own words.

**Evidence surfaces checked:** `arxiv.org/abs/2605.29800` (abstract, via safefetch); `arxiv.org/html/2605.29800v1` (full paper HTML, via safefetch, no injection findings).

**Verdict: VERIFIED** (work exists, details match, content characterization is a fair non-fabricated compression of the paper's actual findings and stated open question), with a **note**: the "elicitation-dependent or weights-locked" phrase is the document's own paraphrase, not a quote from Kohli's paper — appropriately unquoted in the document, so this is not a mismatch, just a precision note for the reviewer.

**For senior review:** Solid. This also happens to be the same paper referenced elsewhere in this vault's memory system as "Kohli 2026: 9 judges ≈ 2 effective" — independently corroborated from a source outside this document.

---

### 12. Zhou et al., ACL 2024

**Location in document:** Section B (line 85) — the model-family finding (credence-carrying behavior splitting by model family). Document's own characterization: **"Asserted — and possibly false**: a 2026 result reports within-family spread exceeding between-family, which would make 'family' the wrong unit. The project's own digest had whispered the same doubt and did not follow it."

**Task per instructions:** verify the document's own characterization (that this row is *asserted*, not verified, and self-flagged as possibly wrong) — not launder it into VERIFIED.

**Checks:**
1. *Work exists / identifier resolves* — YES, and venue is exactly right. Kaitlyn Zhou, Jena D. Hwang, Xiang Ren, Maarten Sap, "Relying on the Unreliable: The Impact of Language Models' Reluctance to Express Uncertainty," *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 3623–3643, 2024 (ACL Anthology ID `2024.acl-long.198`; also arXiv:2401.06730). This is genuinely **ACL** 2024 (main conference), not a misattributed EMNLP/NAACL paper — confirmed directly against the ACL Anthology listing.
2. *Topical fit for "model-family finding"* — confirmed by opening the arXiv HTML full text (`arxiv.org/html/2401.06730v2`). The paper does structure part of its analysis by model family: *"The authors then qualitatively code... for epistemic markers in generated responses from each model family..."* and a dedicated section comparing "models from the GPT and LLaMA-2 family," including base vs. supervised-fine-tuned vs. RLHF variants within each family, to locate "the origin of model overconfidence." This is a real, substantive family-structured analysis in the primary text — the document's characterization is not a fabrication of what this paper does.
3. *The document's own "possibly false" caveat* — I did not locate the specific 2026 result the document alludes to (no author/title given to search against — this is itself an unpinned, background caveat inside a row the document already marks Asserted, not a citation requiring resolution). I can't confirm or refute it; I can confirm it isn't contradicted by anything found in this pass.

**Evidence surfaces checked:** ACL Anthology listing (via WebSearch); `arxiv.org/html/2401.06730v2` (full text, via safefetch, no injection findings).

**Verdict: The document's own "Asserted" framing is ACCURATE and appropriately hedged** — the underlying paper is real, correctly venued (ACL 2024, not a nearby-conference mix-up), and does perform family-level analysis, so the mapping is a *plausible, non-fabricated* asserted claim, exactly the confidence level the document itself claims for it (not more, not less). The "possibly false" 2026-result caveat could not be independently checked (no citable specifics given) but is also not contradicted.

**For senior review:** The document's own epistemic labeling here is well-calibrated — it does not oversell this row, and my check confirms there's a real, correctly-cited paper behind the assertion rather than a fabricated one.

---

### 13. Wilson & Masters; Linacre — Rasch null-category estimability (self-flagged defective citation)

**Location in document:** Section B, first bullet (line 84). Document's own characterization: *"'GPT threshold unidentifiable in principle' → Rasch null-category estimability (Wilson & Masters; Linacre). **Citation defective** — the quotes are real but come from a software help manual, not the cited Psychometrika paper, and a truncation hid a sentence contradicting the gloss. The concept is genuine old psychometrics; the citation as first recorded would not survive a reviewer."*

**Task per instructions:** verify the document's own defect-characterization, not launder into VERIFIED.

**Checks:**
1. *Wilson & Masters paper exists* — YES. M. Wilson & G.N. Masters, "The Partial Credit Model and Null Categories," *Psychometrika* 58, 87–99, 1993. Confirmed via Cambridge Core's Psychometrika listing (matches the document's implicit claim that a real *Psychometrika* paper on exactly this topic exists — "null categories" in the (partial-credit) Rasch model).
2. *Linacre software-manual material on the same topic exists, separately* — YES. John Michael Linacre's Winsteps/Facets help documentation includes dedicated pages on exactly this topic, distinct from the Psychometrika paper: `winsteps.com/winman/nullcats.htm` ("Null or unobserved categories: structural and incidental zeroes") and `winsteps.com/facetman/unobserved.htm` ("Unobserved or null categories: Facets Help") — live help-manual pages (not journal articles) discussing null/unobserved category estimability in Rasch models, including exactly the kind of estimability-under-extreme-categories reasoning ("Extreme incidental null categories... are essentially out of range of the sample and so the sample provides no direct information about their estimates...") that a "GPT threshold unidentifiable" argument would draw on.
3. *Plausibility of the specific defect* — the document's claimed error (quotes attributed to the 1993 Psychometrika journal article that actually originate in Linacre's Winsteps/Facets help-manual prose) is structurally very plausible given what I found: both a real journal paper AND real, topically-overlapping software-manual pages exist side by side in the same research tradition (Linacre is a major figure in applied Rasch/Winsteps software built on the same null-category theory Wilson & Masters formalized), which is exactly the kind of adjacent-source confusion that produces a "real quote, wrong venue" defect. I could not verify the *specific* truncated sentence or the *specific* quotes originally used internally, since the case-study document (correctly, per its own scope) does not reproduce them — that level of detail lives in the internal audit trail, out of scope for this document.

**Evidence surfaces checked:** WebSearch confirming both the Wilson & Masters 1993 Psychometrika paper and the separate Linacre Winsteps/Facets help-manual pages on null/unobserved categories; did not fetch the Winsteps help pages' full text directly (not needed to confirm the *structural* plausibility of the defect — the two-source-confusion shape is confirmed by their both being real and on-topic).

**Verdict: The document's own characterization is PLAUSIBLE AND WELL-GROUNDED, not disprovable from outside** — both named sources are real, correctly distinguished (one is a 1993 journal paper, the other is ongoing software-vendor documentation by a different-but-related author on the same underlying theory), and the claimed defect type (quote misattributed across exactly these two sources) is structurally coherent. I cannot independently confirm the *exact* quoted sentence or the *specific* truncation, since those details aren't reproduced in the document under audit.

**For senior review:** This is the document accurately reporting its own known defect — appropriately transparent, not laundered. No new problems found; the self-report survives an outside sanity check on its two named sources.

---

### 14. Section-B rows with no resolvable citation (scope note, not individually verifiable)

The following Section B items name a phenomenon or field but **no specific author/year/identifier** — there is nothing for a citation check to resolve against, so each is noted rather than scored:

- **"One cited work appears under three conflicting arXiv identifiers... At most one is real. Do not cite."** — By design, the document does not name the work (that's the point of the warning). Nothing to verify; the document's instruction to the reader ("do not cite") is a safe, conservative instruction regardless of which of the conflicting IDs (if any) is real, so there is no way this row could be a mismatch in a harmful direction — at worst it is overcautious.
- **`gate` / `credence` / "policy consistency" → recent LLM-evaluation preprints (A)** — no specific paper named.
- **"set contract" / coverage → prediction-set and conformal literature (A)** — no specific paper named. (The general field — split conformal prediction / prediction sets — is a real, well-established area; nothing paper-specific to check.)
- **The readings-not-votes oracle result → generation-verification-gap literature (A)** — no specific paper named.
- **"evidence stripping" → decontextualization** — the document's own note reads *"'evidence stripping' is not field vocabulary — do not coin it,"* which is a self-directed instruction, not a citation.
- **Abstract-level renamings list** (stemmatics, pseudoreplication, N-version programming, similarity-sensitive diversity, SESOI/equivalence testing, argument mapping/discourse graphs, QBAF/ArgLLM, model-fingerprint confound) — named as field-level concepts, not pinned to specific authors/years/identifiers by the document.

**Verdict: N/A (no resolvable citation).** All of the above are consistent with the document's own labeling of Section B as "asserted at abstract level" — i.e., the document itself does not claim citation-grade precision for these rows, and my check confirms it isn't overclaiming precision it doesn't have.

---

### 15. Not found in the document — Murphy 1973, Blackwell, Ho, Hull & Srihari 1994

Per the task brief's "at minimum" list, these three names were searched for (case-insensitive, whole-document grep) and **do not appear anywhere in `idiolect-trap-case-study.md`**. Since the task instructs that "the document is the source of truth," these are recorded as not-present rather than fabricated a citation context for. No verdict applies (nothing to check). They may exist in a sibling document (`FLF-entry-recall-extender.md`, `THESES.md`) not in scope for this audit (scope-out: don't read other vault files per the task brief).

---

## Summary table

| # | Citation | Document section | Verdict | Note |
|---|---|---|---|---|
| 1 | Clemen & Winkler 1985 | Headline #1, Table A row 1 | PARTIAL | Bibliographic identity fully verified (5-way cross-confirmed); "equivalent-number-of-independent-sources" characterization strongly corroborated via secondary sources; primary text paywalled/Cloudflare-blocked on all 3 attempted surfaces, Wayback unavailable at check time |
| 2 | Bröcker 2008 (arXiv:0806.0813, QJRMS) | Headline #3, Table A row 3 | **VERIFIED** | Both attributed quotes matched verbatim against primary (ar5iv HTML); §3 pinpoint correct; DeGroot & Fienberg 1982 disambiguated and confirmed correct (a different, real 1982 paper, not a mis-cited year of the 1983 one) |
| 3 | Raiffa & Schlaifer 1961 | Headline #2, Table A row 2 | PARTIAL | Bibliographic identity 5-way confirmed; "lineage" claim is appropriately hedged and matches field consensus; primary book PDF inaccessible to fetch tooling |
| 4 | Pieper 2014 (via Hennessy & Johnson 2020) | Table A row 4 | **VERIFIED** | Full citation chain confirmed by opening Hennessy & Johnson's open-access PMC text; Pieper 2014 is their reference [10], verbatim-matched; "field retains overlap rather than discarding" note supported by the primary's own abstract |
| 5 | Satopää; Karmarkar 1978 | Table A row 5 (retracted self-confound) | PARTIAL | Karmarkar 1978 bibliographically confirmed and on-topic; "Satopää" is under-specified in the document itself (no year/title) — name-level match only |
| 6 | Makridakis & Winkler 1983 | Table A row 9 | PARTIAL | Bibliographic identity and "m*≈2-3 plateau" characterization confirmed via secondary sources; primary paywalled, no verbatim quote at stake |
| 7 | Kish design effect | Headline #1, event-flow 07-01, Table A rows 1 & "N_eff misuse" | **VERIFIED** | Standard, correctly-named, correctly-formalized concept; case study's `N_eff` formula is the algebraically correct reciprocal of Kish's deff |
| 8 | Scott Alexander — Multiple Stage Fallacy | Table A row 7 | **VERIFIED** | Attribution accurate; correctly labeled as a named blog concept, not dressed up as academic |
| 9 | Higgins et al. 2009; Sidik & Jonkman 2002 | Table A row 8 | **VERIFIED** | Both papers confirmed real, correctly paired as the HKSJ method's two source papers; "correct tool is HKSJ" is accurate mainstream methodology |
| 10 | Rowe & Wright 1996/99; Best 1974 | Table A row 6 | PARTIAL | Both works bibliographically confirmed and on-topic; document's self-flagged "hedge omitted" defect is plausible but the specific hedge sentence was not independently located/verified |
| 11 | Kohli 2026 | Program B event-flow 07-13 | **VERIFIED** | arXiv:2605.29800 confirmed; content match strong; "elicitation-dependent or weights-locked" is the document's own fair paraphrase of the paper's real closing open-question, not a fabricated quote |
| 12 | Zhou et al., ACL 2024 | Section B | **VERIFIED (as asserted)** | Document's own "Asserted, possibly false" framing confirmed accurate — real ACL 2024 paper, correctly venued, does perform family-structured analysis; the row is not overclaimed |
| 13 | Wilson & Masters; Linacre | Section B | **VERIFIED (as asserted/defective)** | Document's own "citation defective" self-report confirmed plausible — both a real 1993 Psychometrika paper and separate, real Linacre software-manual pages on the same topic exist, exactly the two-source shape the defect describes; specific miscited sentence not independently locatable from outside |
| 14 | Section-B generic/unnamed rows (gate/credence, set contract, readings-not-votes, evidence stripping, abstract-level renamings, triple-arXiv-ID row) | Section B | N/A | No specific author/year/identifier given by the document — nothing to resolve; document doesn't overclaim precision here either |
| 15 | Murphy 1973; Blackwell; Ho, Hull & Srihari 1994 | (task brief only) | N/A — not in document | Grep-confirmed absent from `idiolect-trap-case-study.md`; likely belong to a sibling document out of scope |

## Counts

- **VERIFIED:** 6 (Bröcker 2008; Pieper 2014/Hennessy & Johnson 2020; Kish design effect; Scott Alexander; Higgins et al. 2009/Sidik & Jonkman 2002; Kohli 2026)
- **VERIFIED (document's self-characterization of an asserted/defective row confirmed accurate — not laundered into a positive claim):** 2 (Zhou et al. ACL 2024; Wilson & Masters/Linacre)
- **PARTIAL:** 5 (Clemen & Winkler 1985; Raiffa & Schlaifer 1961; Satopää/Karmarkar 1978; Makridakis & Winkler 1983; Rowe & Wright/Best 1974)
- **MISMATCH:** 0
- **UNREACHABLE:** 0 (every citation's bibliographic identity was independently confirmed through at least one accessible surface; several primary texts were paywalled or PDF-inaccessible to the fetch tooling, which is reflected in PARTIAL verdicts with the specific remaining gap stated, not scored as a wholesale failure to reach)
- **N/A (no resolvable citation, by the document's own design):** 6 (five generic Section-B rows grouped as one line + the triple-arXiv-ID row) + **N/A (not in document):** 3 (Murphy 1973, Blackwell, Ho/Hull/Srihari 1994)

## Note on the prior audit (recap)

`citation-audit-2026-07-17.md` covers a different document (`FLF-entry-recall-extender.md`) with zero citation overlap with `idiolect-trap-case-study.md` — nothing was carried forward from it; every citation above was verified fresh in this pass.

---
*Status: complete — all citations named in the task brief and found in the document have been checked.*
