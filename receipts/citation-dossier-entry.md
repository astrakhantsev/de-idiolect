---
title: "Citation verification dossier — FLF recall-extender entry"
date: 2026-07-18
status: COMPLETE — 47 citations checked, 44 VERIFIED, 3 PARTIAL, 0 MISMATCH, 0 UNREACHABLE
scope: "Every citation in FLF-entry-recall-extender.md. Items already covered by citation-audit-2026-07-17.md are copied forward as 'per 07-17 audit' with one spot-check; NOT re-audited from scratch. All other citations verified fresh in this pass."
tools: "safefetch (bash, foreground) for web pages; Read for local PDFs in idiolect/sources/; WebSearch for locating sources."
---

# Citation verification dossier

Method note: verdicts are VERIFIED / PARTIAL / UNREACHABLE / MISMATCH. For items already
checked in the 07-17 audit, the prior verdict is copied forward with the note "per 07-17
audit" and one spot-checked detail is re-verified fresh in this pass (marked "spot-check").

---

## Larsen & Bong (2016), *MIS Quarterly* 40(3):529–551 — "A Tool for Addressing Construct Identity in Literature Reviews and Meta-Analyses"

**Why re-verified in full rather than spot-checked**: this is the one citation the 07-17 audit found fabricated (a quote wrapped in quotation marks that did not appear in the paper, since fixed in §1) and the entry adds substantial new content drawing on it beyond the 07-17 fix (§1 Swanson extension, §7 CID description, §8 the 90.5%/precision/recall figures). Given the known defect and the added material, this citation gets full fresh verification, not a spot-check, using the local PDF `idiolect/sources/larsen-bong-2016-construct-identity-AM.pdf` (converted to text via `pdftotext -layout` for grepping) plus a Crossref lookup for bibliographic details.

**Entry locations and claims checked:**

1. **§1** — "doctoral students using full-text search retrieved **9%** of the relevant constructs on average (per-task recall as low as **3%**)": paper (p.35 of AM, "the participants assigned to EBSCO retrieved 9% of the relevant constructs, even in such a small sample of articles") confirms the 9% figure attributed to EBSCO (the paper's full-text-search condition). The per-task low of 3% is confirmed at a different point ("recall under the full-text search condition (EBSCO) was at its peak, 19% (relative to 3%, 6%, and 7%)" — the four EBSCO per-task recall values across the paper's four tasks) — 3% is indeed the floor of those four. MATCH.
2. **§1** — quoted: "**83% of participants would arrive at the conclusion that the relationship had not been tested at all**": paper — "The meta-analytic approach employed in this article shows that 83% of participants would arrive at the conclusion that the relationship had not been tested at all." VERBATIM MATCH.
3. **§1** — "They frame this as extending Swanson (1986): '**the vast majority of discovered knowledge is hidden from the individual researcher by the very nature of the search process itself**.'": paper — "While Swanson addressed undiscovered knowledge, we found the vast majority of discovered knowledge is hidden from the individual researcher by the very nature of the search process itself." VERBATIM MATCH. The "extending Swanson (1986)" framing is also the paper's own language: "Third, extending Swanson's (1986) conclusions, we demonstrate that relationships need not be hidden in order to be inaccessible to researchers." MATCH.
4. **§1** — quoted: "**the renaming of an existing construct (jangle fallacy) may increase the perceived novelty of a construct**": paper — "The renaming of an existing construct (jangle fallacy) may increase the perceived novelty of a construct, whereas the reuse of an existing construct name to represent a different phenomenon (jingle fallacy) may increase the perceived novelty of a relationship..." VERBATIM MATCH.
5. **§7** — CID described as "construct-identity detection by semantic similarity over measurement *items*, with construct names explicitly set aside, thresholded candidate pairs for expert review, and automatic construct knowledge bases as the stated goal (Li & Larsen 2011/2013)": paper — designs operate over constructs' "measurement items"; "Such designs allow for detection of correspondent construct pairs regardless of the names of these constructs"; threshold-based candidate-pair assignment ("we assign any construct pair with a similarity score equal to or higher than the threshold as a correspondent-pair prediction"); stated goal — "necessary to make ontology learning possible and useful through automatic creation of construct knowledge bases, as proposed by Li and Larsen (2011; 2013)." All elements confirmed; "expert review" is a fair characterization of the paper's "evaluated against human expert decisions" / "supplement to expert efforts" framing (not a verbatim quote in the entry, so no verbatim bar applies). MATCH.
6. **§8** — "Larsen & Bong's follow-up studies, where their construct-identity detector outperformed all 36 human participants precisely on *uncommon* constructs — **90.5%** of their construct sample — while curated keyword search plus expert recall won on common ones": paper — "Here, CID1 outperformed all 36 human participants" (in the uncommon-construct "website familiarity" task); "314 (90.5%) fit our definition of uncommon." On common-construct tasks, INN ("Inter-Nomological Networks," a curated keyword-search engine over pre-extracted constructs, built on Lucene) outperforms both EBSCO and CID1 by a wide margin (e.g., F1 .45 vs .13/.23; precision 86–88%) — confirms "curated keyword search... won on common ones." MATCH.
7. **Appendix** — "precision **.68** vs **.46**, recall **.58** vs **.39** against full-text search": paper — "CID1 outperformed EBSCO on every assessment measure: average precision (.68 vs .46), average recall (.58 vs .39)..." VERBATIM MATCH (EBSCO = the paper's full-text-search condition).
8. **Bibliographic details** — "*MIS Quarterly* 40(3):529–551": confirmed via Crossref (`api.crossref.org/works/10.25300/MISQ/2016/40.3.01`) — container-title "MIS Quarterly", volume "40", issue "3", page "529-551", first author Kai R. Larsen. MATCH. (Publisher's own page, misq.umn.edu, and the DOI resolver both returned a Cloudflare bot-check page rather than content — worked around via Crossref's API, which is the canonical bibliographic record.)

**Verdict: VERIFIED.** All four verbatim quotes attributed to this paper are exact matches in primary text; all six numeric/statistical claims match; all paraphrased methodological characterizations are accurate; bibliographic details confirmed independently via Crossref.

**For senior review:** none — the one prior fabrication (the mis-quoted "9%/3%" sentence flagged in the 07-17 audit) is fixed, and the corrected text plus all newly-added Larsen & Bong material checks out clean against primary text.

---

## Batch: citations previously verified in the 07-17 audit — verdicts copied forward, one detail spot-checked fresh per item

Per the task's scope instruction, these are NOT re-audited from scratch; the 07-17 verdict is copied forward and one detail is independently re-checked in this pass (via Crossref bibliographic API, arXiv abstract pages, or Google Patents — safefetch throughout).

**Blair & Maron (1985), *CACM* 28(3):289–299.** Per 07-17 audit: VERIFIED (75% recall stipulation / ~20% measured recall / ~80% precision quotes all verbatim). Spot-check: Crossref record for DOI 10.1145/3166.3197 confirms title "An evaluation of retrieval effectiveness for a full-text document-retrieval system," authors David C. Blair and M. E. Maron, container-title "Communications of the ACM," volume 28, issue 3, **page 289-299** (exact match to entry's cited page range), and an abstract stating the system was "retrieving less than 20 percent of the documents relevant to a particular search." **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**Furnas, Landauer, Gomez & Dumais (1987), *CACM* 30(11):964–971.** Per 07-17 audit: VERIFIED (the .07–.18 range, confirmed off the results-table page image after OCR garbled the decimals). Spot-check: Crossref record for DOI 10.1145/32206.32212 confirms title "The vocabulary problem in human-system communication," authors G.W. Furnas, T.K. Landauer, L.M. Gomez, S.T. Dumais, container-title "Communications of the ACM," volume 30, issue 11, **page 964-971** (exact match). Abstract corroborates the phenomenon directly: "In every case two people favored the same term with probability <0.20." **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**Kelley (1927), pp. 63–64 — coins "jangle fallacy."** Per 07-17 audit: VERIFIED. Not independently re-fetched this pass (pre-1928 monograph, not indexed on Crossref/arXiv; the 07-17 audit's method — Wayback for blocked primaries — was already the strongest available route and its verdict is taken as-is). **Verdict: VERIFIED (per 07-17 audit; not independently re-checked this pass).**

**Thorndike (1904), credits Aikins for "jingle."** Per 07-17 audit: VERIFIED (p. 14). Not independently re-fetched this pass, same reasoning as Kelley 1927. **Verdict: VERIFIED (per 07-17 audit; not independently re-checked this pass).**

**Hoekstra (2010), *Semantic Web* 1(1).** Per 07-17 audit: VERIFIED ("a continuous relation of trust"; knowledge-reengineering bottleneck; extends Feigenbaum's acquisition bottleneck). Spot-check: Crossref record for DOI 10.3233/sw-2010-0004 confirms title "The knowledge reengineering bottleneck," author Rinke Hoekstra, container-title "Semantic Web," volume 1, issue "1,2" (the journal's first, combined issue — matches entry's "1(1)" citation), pages 111-115. **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**Doctorow, "Metacrap" (2001).** Per 07-17 audit: VERIFIED ("People are lazy" / "People lie"). Not independently re-fetched this pass (this is a well-known, stable, non-paywalled essay at the author's own site; the audit's direct read is taken as-is). **Verdict: VERIFIED (per 07-17 audit; not independently re-checked this pass).**

**Shirky, "The Semantic Web, Syllogism, and Worldview" (2003).** Per 07-17 audit: VERIFIED ("you can't force an agreement to exist where none actually does"). Not independently re-fetched this pass, same reasoning. **Verdict: VERIFIED (per 07-17 audit; not independently re-checked this pass).**

**Star & Griesemer (1989), *Social Studies of Science* 19(3).** Per 07-17 audit: VERIFIED (coined "boundary objects"; cooperation-without-consensus faithful — PARAPHRASE-OK). Spot-check: Crossref record for DOI 10.1177/030631289019003001 confirms title "Institutional Ecology, 'Translations' and Boundary Objects: Amateurs and Professionals in Berkeley's Museum of Vertebrate Zoology, 1907-39," authors Susan Leigh Star and James R. Griesemer, container-title "Social Studies of Science," volume 19, issue 3, pages 387-420. Abstract: "the development of 'boundary objects'... Boundary objects are both adaptable to different viewpoints and robust enough to maintain identity across them" — matches the entry's paraphrase that communities cooperate through shared translation devices without converging on one classification. **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**Bowker & Star (1999).** Per 07-17 audit: VERIFIED ("there is no such thing as a natural or universal classification system," verbatim, p. 131). Not independently re-fetched this pass (a well-known monograph, *Sorting Things Out*; the audit's page-level verbatim check is taken as-is). **Verdict: VERIFIED (per 07-17 audit; not independently re-checked this pass).**

**Relink (Huang et al., arXiv:2601.07192).** Per 07-17 audit: VERIFIED (title/authors/Jan-2026 date and the reason-and-construct-over-build-then-reason characterization confirmed). Spot-check: arXiv abstract page confirms title "Relink: Constructing Query-Driven Evidence Graph On-the-Fly for GraphRAG," authors Manzong Huang, Chenyang Bu, Yi He, Xingrui Zhuo, Xindong Wu; submitted 12 Jan 2026; abstract explicitly argues "for a *reason-and-construct* paradigm" against the "*build-then-reason* paradigm" of static pre-constructed KGs — matches entry's characterization exactly. **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**SciCo-Radar (arXiv:2409.15113).** Per 07-17 audit: VERIFIED (identifier resolves, description accurate). Spot-check: arXiv abstract page confirms title "Inferring Scientific Cross-Document Coreference and Hierarchy with Definition-Augmented Relational Reasoning," authors Lior Forer and Tom Hope (matches entry's "Forer & Hope" attribution in §7), abstract confirms LLM-generated context-dependent and relational definitions for cross-document coreference — matches entry's description. **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**GenOM (arXiv:2508.10703).** Per 07-17 audit: VERIFIED. Spot-check: arXiv abstract page confirms title "GenOM: Ontology Matching with Description Generation and Large Language Model," authors Yiping Song, Jiaoyan Chen, Renate A. Schmidt; abstract confirms "enriches the semantic representations of ontology concepts via generating textual definitions, retrieves alignment candidates with an embedding model" — matches entry's "definition-embedding as the retrieval key with pairwise LLM verification, over existing materialized ontologies." **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**EDC (Zhang & Soh, arXiv:2404.03868).** Per 07-17 audit: VERIFIED. Spot-check: arXiv abstract page confirms title "Extract, Define, Canonicalize: An LLM-based Framework for Knowledge Graph Construction," authors Bowen Zhang and Harold Soh; abstract confirms the three-phase "Extract-Define-Canonicalize (EDC)" framework — matches entry's "extract → define → canonicalize-by-definition-vector skeleton." **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**KGGen (arXiv:2502.09956, NeurIPS 2025).** Per 07-17 audit: VERIFIED ("aliases that Wikidata uses" quote and its EDC citation both confirmed). Spot-check: arXiv abstract page confirms title "KGGen: Extracting Knowledge Graphs from Plain Text with Language Models," submission Feb 2025 with a Nov 2025 revision (consistent with NeurIPS 2025 timing); abstract confirms entity clustering to reduce sparsity — matches entry's "selects one canonical representative per cluster." (The specific "aliases that Wikidata uses" verbatim quote lives in the paper body, not the abstract, so this spot-check confirms identifier/venue/author resolution only — the quote itself was already verified by the 07-17 audit's primary-text read.) **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**Guo et al. 2024, "Personalized Jargon Identification," arXiv:2311.09481.** Per 07-17 audit: VERIFIED. Spot-check: arXiv abstract page confirms title "Personalized Jargon Identification for Enhanced Interdisciplinary Communication," author Yue Guo (first), submitted 16 Nov 2023; abstract addresses jargon familiarity varying by individual researcher background — consistent with entry's use as a detection-step citation. Note: the entry cites this as "Guo et al. 2024" (§7's novelty list) while the arXiv submission date is Nov 2023 — this is very likely the paper's conference/journal publication year (common for a 2023 arXiv preprint to publish at a 2024 venue) rather than a factual error, but the entry does not state a venue for this one, so there is nothing to mismatch against. Flagged as a minor note, not a verdict-changing issue. **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**NeoN (arXiv:2505.15426).** Per 07-17 audit: VERIFIED, with a correction applied (NeoN is neologism detection in Polish, not novel-*sense* detection; AXOLOTL'24 carries the novel-sense claim). Spot-check: arXiv abstract page confirms title "NeoN: A Tool for Automated Detection, Linguistic and LLM-Driven Analysis of Neologisms in Polish," submitted 21 May 2025; abstract describes detecting/analyzing Polish neologisms with an "integrated LLM module [that] automatically generates definitions" — confirms both the neologism (not novel-sense) framing and the "detection triggers generated definitions" pattern the entry cites it for. The entry's current §7 text says "NeoN (arXiv:2505.15426; automated neologism detection feeding LLM-generated definitions)" — correctly uses "neologism," consistent with the 07-17 correction having been applied. **Verdict: VERIFIED (per 07-17 audit + spot-check).**

**Microsoft patents US8589791B2 / US10552522B2.** Per 07-17 audit: VERIFIED, with a correction applied (one continuation family, not two independent efforts). Spot-check: Google Patents pages for both confirm title "Automatically generating a glossary of terms for a given document or group of documents" on both; identical inventors (Nicholas Caldwell, Saliha Azzam, Courtney Anne O'Keefe, Tu Huy Phan) and identical priority date (2011-06-28) on both, with US10552522B2 filed 2013-11-19 as a later application against the same priority — confirms the continuation-family relationship. Assignee on both: Microsoft (Corp. / Technology Licensing LLC). **Verdict: VERIFIED (per 07-17 audit + spot-check).**

---

## New citations — full verification (not covered by the 07-17 audit)

### Sharma et al. (2023), arXiv:2310.13548 — "Towards Understanding Sycophancy in Language Models"

**Entry location/claim (§1):** two quoted fragments — "when a response matches a user's views, it is more likely to be preferred" and "both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time," cited as "abstract read."

**Checks:** arXiv abstract page fetched directly. Abstract text: "We find that when a response matches a user's views, it is more likely to be preferred." — VERBATIM MATCH. "Moreover, both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time." — VERBATIM MATCH. Title, authors (Mrinank Sharma et al.), and 2023 submission date (20 Oct 2023) all confirmed on the abstract page.

**Verdict: VERIFIED.** Both quotes verbatim in the abstract, which is the surface the entry claims to have read. **For senior review:** none.

### Perez et al. (2022), arXiv:2212.09251 — "Discovering Language Model Behaviors with Model-Written Evaluations"

**Entry location/claim (§1):** quoted "Larger LMs repeat back a dialog user's preferred answer ('sycophancy')," cited as one of the paper's inverse-scaling findings, "abstract read."

**Checks:** arXiv abstract page fetched directly. Abstract: "We generate 154 datasets and discover new cases of inverse scaling where LMs get worse with size. Larger LMs repeat back a dialog user's preferred answer ("sycophancy") and express greater desire to pursue concerning goals..." — VERBATIM MATCH, and it is explicitly presented in the same sentence as the paper's inverse-scaling discovery, confirming the entry's framing.

**Verdict: VERIFIED.** **For senior review:** none.

### CREPE — Yu, Min, Zettlemoyer & Hajishirzi, ACL 2023, arXiv:2211.17257 — "Open-Domain Question Answering with False Presuppositions"

**Entry location/claim (§1):** quoted "struggle when predicting whether a presupposition is factually correct," attributed "in large part … to difficulty in retrieving relevant evidence passages," cited as "abstract read."

**Checks:** arXiv abstract page fetched directly. Abstract: "...adaptations of existing open-domain QA models can find presuppositions moderately well, but struggle when predicting whether a presupposition is factually correct. This is in large part due to difficulty in retrieving relevant evidence passages from a large text corpus." First fragment VERBATIM MATCH. Second fragment: the entry's ellipsis stands in for the single word "due" (paper: "in large part **due** to difficulty..."; entry: "in large part **…** to difficulty..." ) — text before and after the ellipsis is exact and in original order; using an ellipsis to elide one connective word is stylistically unusual but not a misquote (the omitted word is not load-bearing to the claim). Author list confirmed via OpenAlex (DOI 10.18653/v1/2023.acl-long.583): Xinyan Yu, Sewon Min, Luke Zettlemoyer, Hannaneh Hajishirzi — exact match to entry's "Yu, Min, Zettlemoyer & Hajishirzi." Venue confirmed: ACL 2023 (Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers).

**Verdict: VERIFIED.** **For senior review:** none — the single-word ellipsis is a minor stylistic quirk, not a misquote; flagging only so a reviewer doesn't need to re-derive that it's benign.

### Bröcker (2008), arXiv:0806.0813 — "Reliability, Sufficiency, and the Decomposition of Proper Scores"

**Entry location/claim (§2 table, §8):** described as "a proper-score uniqueness theorem (extending DeGroot & Fienberg)"; this is the single citation the entry uses to mark Program B's central finding **foreclosed** ("for the theoretical claim under strictly proper scoring rules") — the highest-stakes citation in the entry, since a foreclosure verdict is much stronger than a "predated" verdict elsewhere in the same table.

**Checks:** Given the stakes, went beyond the abstract to the full text (arXiv PDF wouldn't render through safefetch/defuddle — tried directly and got an empty DOM; worked around via the ar5iv.labs.arxiv.org HTML mirror, which rendered the full paper). Confirmed:
- Title "Reliability, Sufficiency, and the Decomposition of Proper Scores," author Jochen Bröcker, arXiv:0806.0813 (also has a published version, DOI 10.1002/qj.456, *Quarterly Journal of the Royal Meteorological Society* — listed as "Related DOI" on the arXiv page).
- The uniqueness claim itself, in the paper's own words (Section on sufficiency): "If the score is strictly proper, π^γ is uniquely defined through this optimum property, in the sense that any forecast for which γ is sufficient is either equal to π^γ or it will have a worse average score." — this is a genuine uniqueness result gated on strict propriety, matching the entry's "uniqueness theorem... under strictly proper scoring rules" characterization precisely (including the "under strictly proper" qualifier the entry uses to scope the foreclosure narrowly).
- "Extending DeGroot & Fienberg": the paper's own reference list, item [8]: "Morris W. DeGroot and Stephen E. Fienberg. Assessing probability assessors: calibration and refinement. *Statistical Decision Theory and Related Topics*, 1(3):291–314, 1982." The paper also has a dedicated appendix titled "Sufficiency and refinement of DeGroot and Fienberg" formally relating its own sufficiency condition to theirs — confirms the "extending" relationship is not a loose citation but a worked-out formal connection.

**Verdict: VERIFIED.** The paper is real, resolves, and contains the specific uniqueness result under strictly proper scoring the entry hangs its "foreclosed" verdict on, with a genuine formal extension of DeGroot & Fienberg. **For senior review:** none on the citation itself — this note is scoped only to citation integrity, not to whether the entry's own theorem-to-claim mapping (i.e., whether Program B's actual metric was in fact non-proper, and whether that correctly keeps it outside the theorem, as the entry itself claims) is correct; that is a mathematical-argument question outside a citation audit's remit.

### DeGroot & Fienberg (1982) — cited as what Bröcker 2008 extends

**Entry location/claim (§2 table):** "Bröcker 2008... extending DeGroot & Fienberg." Not independently quoted elsewhere in the entry — cited only via its relationship to Bröcker 2008.

**Checks:** confirmed directly from Bröcker (2008)'s own reference list (see above): "[8] Morris W. DeGroot and Stephen E. Fienberg. Assessing probability assessors: calibration and refinement. *Statistical Decision Theory and Related Topics*, 1(3):291–314, 1982," plus a dedicated appendix in Bröcker 2008 titled "Sufficiency and refinement of DeGroot and Fienberg." Real work, correctly attributed as the paper Bröcker extends.

**Verdict: VERIFIED.** **For senior review:** none.

### Clemen & Winkler (1985) — "the equivalent-number-of-independent-sources result"

**Entry location/claim (§2 table):** the field's owner of the project's retracted coinage `m*` ("the audit unit"), described as "the equivalent-number-of-independent-sources result."

**Checks:** Crossref record for DOI 10.1287/opre.33.2.427 confirms title "Limits for the Precision and Value of Information from Dependent Sources," authors Robert T. Clemen and Robert L. Winkler, *Operations Research* 33(2):427–442, 1985. Abstract: "This paper investigates the impact of dependence on the precision and value of information... the limiting value of information as more sources are considered can be considerably less than the expected value of perfect information" — this is the paper's actual subject: how the value/precision of aggregated information saturates as dependent sources accumulate, which is the "equivalent number of independent sources" concept the entry attributes to it. Bibliographically real and topically matches.

**Verdict: VERIFIED.** **For senior review:** none.

### Raiffa & Schlaifer (1961) — "value-of-information threshold analysis... lineage"

**Entry location/claim (§2 table):** the field's owner of the project's retracted coinage "the operating requirement," described as "value-of-information threshold analysis (Raiffa & Schlaifer 1961 lineage)."

**Checks:** could not fetch the book itself (a 1961 monograph, not indexed as full text anywhere accessible), so verified via independent secondary citations: two book reviews indexed on OpenAlex both confirm the book's existence and exact title — "Howard Raiffa and Robert Schlaifer. Applied Statistical Decision Theory. Boston: Harvard Business School, 1961" (reviewed independently in *Behavioral Science* and *Psychometrika*, and again as the 1968 MIT Press reprint in *Biometrische Zeitschrift*). *Applied Statistical Decision Theory* is the canonical text founding Bayesian value-of-information analysis, which is the concept the entry attributes to it ("value-of-information threshold analysis... lineage" — the entry hedges with "lineage" rather than claiming a specific page-level result, appropriately given no primary-text page check was possible here).

**Verdict: VERIFIED (existence + topical match via independent secondary citations; primary text itself not directly opened).** **For senior review:** none — the entry's own hedge ("lineage," not a specific verbatim claim) matches the depth of verification available.

### Ho, Hull & Srihari (1994), *IEEE TPAMI* 16(1):66–75 — "Decision Combination in Multiple Classifier Systems"

**Entry location/claim (§2, the "read the enumerations, not the votes" cell; §8 "closest measured precedent").** Cited by author/year/venue only, no verbatim quote attributed.

**Checks:** Crossref record for DOI 10.1109/34.273716 confirms title "Decision combination in multiple classifier systems," authors Tin Kam Ho, J.J. Hull, S.N. Srihari, container-title "IEEE Trans. Pattern Anal. Machine Intell.," **volume 16, issue 1, page 66-75** — exact match to the entry's "*IEEE TPAMI* 16(1):66–75."

**Verdict: VERIFIED.** **For senior review:** none.

### Murphy (1973) — cited alongside Blackwell's comparison of experiments

**Entry location/claim (§2, the "the signal, not the cut…" naming-experiment cell):** "reached the owner's territory *from the slogan alone* (Murphy 1973; Blackwell's comparison of experiments)." Author/year only, no verbatim quote.

**Checks:** Crossref record for DOI 10.1175/1520-0450(1973)012<0595:anvpot>2.0.co;2 confirms title "A New Vector Partition of the Probability Score," author Allan H. Murphy, *Journal of Applied Meteorology* 12(4):595–600, 1973 — a real, well-known paper on decomposing forecast-verification scores into resolution/reliability terms, directly on-topic for the "signal vs. the cut" theme the entry attaches it to.

**Verdict: VERIFIED.** **For senior review:** none.

### Blackwell — "comparison of experiments"

**Entry location/claim:** same cell as Murphy 1973, "Blackwell's comparison of experiments." No year given in the entry text itself, no verbatim quote.

**Checks:** Crossref record for DOI 10.1214/aoms/1177729032 confirms title "Equivalent Comparisons of Experiments," author David Blackwell, *The Annals of Mathematical Statistics* 24(2):265–272, 1953 — the canonical Blackwell result on comparing statistical experiments by informativeness, matching the entry's shorthand "Blackwell's comparison of experiments" exactly (and directly related to the Bröcker 2008 lineage above, which itself engages the "sharpness principle" literature this Blackwell paper founded).

**Verdict: VERIFIED.** **For senior review:** none — note only that the entry never states a year for Blackwell in-line, so there's nothing to mismatch against, but a reviewer wanting a full citation would need "Blackwell (1953)."

### Franklin, Halevy & Maier (2005) — "pay-as-you-go dataspaces"

**Entry location/claim (§4):** "pay-as-you-go dataspaces (Franklin, Halevy & Maier 2005)... credited from secondary descriptions — I did not read their primary texts."

**Checks:** Crossref record for DOI 10.1145/1107499.1107502 confirms title "From databases to dataspaces: a new abstraction for information management," authors Michael Franklin, Alon Halevy, David Maier, *ACM SIGMOD Record* 34(4):27–33, December 2005 — exact match. Abstract explicitly proposes "dataspaces and their support systems as a new agenda for data management" for environments without one canonical schema — matches the entry's characterization. The entry does not claim to have read the primary text (states this explicitly), so verbatim-quote verification does not apply; existence + topical match is the correct bar and both are met.

**Verdict: VERIFIED.** **For senior review:** none.

### Aberer & Cudré-Mauroux (2004) — "emergent semantics"

**Entry location/claim (§4):** "emergent semantics (Aberer & Cudré-Mauroux 2004)... credited from secondary descriptions — I did not read their primary texts."

**Checks:** Crossref search located "Emergent Semantics Principles and Issues," a 2004 Springer book chapter (DOI 10.1007/978-3-540-24571-1_2, pages 25–38), authored by Karl Aberer, Philippe Cudré-Mauroux, Aris M. Ouksel, Tiziana Catarci, and additional co-authors (a multi-author position paper; the entry's "Aberer & Cudré-Mauroux" picks the two lead names, which is how this paper is conventionally shorthand-cited in the field). Real, correctly dated to 2004, and on-topic for "emergent semantics" as a named alternative to universal-ontology approaches. As with Franklin/Halevy/Maier, the entry does not claim primary-text reading, so existence + topical match is the applicable bar.

**Verdict: VERIFIED.** **For senior review:** none — note only that the paper has more than two authors; the entry's two-name shorthand is a defensible convention, not a misattribution, but a reviewer might want the full author list if precision matters here.

### Li & Larsen (2011; 2013) — cited within the CID discussion (§7)

**Entry location/claim (§7):** "automatic construct knowledge bases as the stated goal (Li & Larsen 2011/2013)."

**Checks:** confirmed directly from Larsen & Bong (2016)'s own reference list (local PDF, already opened for the Larsen & Bong verification above): "Li, J., and Larsen, K. R. 2011. 'Establishing Nomological Networks for Behavioral Science: A Natural Language Processing Based Approach,' in International Conference on Information Systems (ICIS), Shanghai, China" and "Li, J., and Larsen, K. R. 2013. 'Tracking Behavioral Construct Use through Citations: A Relation Extraction Approach,' ICIS, Milan, Italy." Both are real ICIS conference papers, both about extracting/tracking behavioral constructs — matching the "automatic construct knowledge bases" characterization exactly, and matching the in-text citation "as proposed by Li and Larsen (2011; 2013)" that appears verbatim in Larsen & Bong 2016 itself (verified above).

**Verdict: VERIFIED.** **For senior review:** none.

### ALPAC (1966) — "the standard marker for the end of interlingua-MT funding"

**Entry location/claim (§3):** "The ALPAC report (1966) is the standard marker for the end of interlingua-MT funding; cited as a historical datum, not from its primary text."

**Checks:** the entry explicitly disclaims reading the primary text, so a secondary-source existence + accuracy check is the right bar. Wikipedia's ALPAC entry confirms: a US government committee report issued in 1966, "gained notoriety for being very skeptical of research done in machine translation so far... this eventually caused the U.S. government to reduce its funding of the topic dramatically. This marked the beginning of the first AI winter." Matches the entry's characterization exactly.

**Verdict: VERIFIED.** **For senior review:** none.

### SKOS (`skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`)

**Entry location/claim (§4):** "The relation labels are taken verbatim from SKOS (`skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) rather than re-coined."

**Checks:** fetched the W3C SKOS Reference (`https://www.w3.org/TR/skos-reference/`, W3C Recommendation 18 August 2009). **Safefetch security scan note: this fetch triggered one HIGH-severity finding** — `role_manipulation: Jailbreak keywords: "no restriction"` — and the tool auto-stripped the flagged content before returning the page. Read in context, this is almost certainly a false positive: the phrase sits in the W3C document's ordinary legal/technical boilerplate (W3C specs routinely contain phrases like "no restriction of any kind" in licensing/copyright sections), not an attempt to redirect this agent's behavior; nothing in the returned content asked for a role change or instruction override, and the actual technical content (property definitions) came through intact. Flagging per instructions rather than silently passing over it. The document confirms all four properties as genuine SKOS mapping relations, each with its own W3C-assigned URI: `skos:exactMatch` (`http://www.w3.org/2004/02/skos/core#exactMatch`), `skos:broadMatch` (`...#broadMatch`, sub-property of `skos:broader`, inverse of `skos:narrowMatch`), `skos:narrowMatch` (`...#narrowMatch`, inverse of `skos:broadMatch`), and `skos:relatedMatch` (`...#relatedMatch`) — plus a fifth, `skos:closeMatch`, not cited by the entry. All four cited terms exist exactly as named.

**Verdict: VERIFIED.** **For senior review:** the SKOS fetch tripped a HIGH-severity safefetch injection-pattern match ("no restriction" boilerplate in the W3C legal text) — almost certainly a false positive on a standards document, but noting per the third-party-content-safety protocol so it doesn't get silently smoothed over.

### LDOCE (Longman Dictionary of Contemporary English) — "controlled defining wordlist"

**Entry location/claim (§4):** "an LDOCE-style controlled defining wordlist: static, domain-generic, maintenance-free."

**Checks:** Wikipedia's LDOCE entry confirms: "A key feature of the LDOCE is its utilization of the Longman Defining Vocabulary, a 2200-word controlled defining vocabulary used to write all of the definitions in the dictionary... developed from Michael West's *General Service List* of high-frequency words." First published 1978, now in its 6th edition — a genuinely static, decades-old, domain-generic controlled vocabulary, exactly matching the entry's characterization and its argument that "static generic wordlists have survived for decades largely because they need no curation."

**Verdict: VERIFIED.** **For senior review:** none.

### LAVOHA (CEUR Vol-4177)

**Entry location/claim (§7):** cited as read "in primary," grouped with the Vocabulary Switching System as an academic canonicalization effort — "both build merged canonical resources; neither has a detection trigger or generated neutral definitions."

**Checks:** fetched the CEUR-WS Vol-4177 table of contents directly. Vol-4177 is the proceedings of ONTOBRAS 2025 (18th Seminar on Ontology Research in Brazil). Paper 2 in the volume: **"LLM Assisted Vocabulary Harmonization"** (pages 23–37), authors Maria Claudia Reis Cavalcanti, Samir de Oliveira Ramos, Ronaldo Ribeiro Goldschmidt, and eight further co-authors. The paper's title initials (**L**LM **A**ssisted **VO**cabulary **HA**rmonization) spell **LAVOHA** — this is almost certainly the paper the entry means, and "vocabulary harmonization" is directly consistent with the entry's characterization "build merged canonical resources." Attempted to fetch the paper's own PDF for a full-text check but it did not render through safefetch/defuddle (empty DOM returned) — this is an infrastructure limitation of the fetch path for this particular CEUR PDF, not a sign of anything wrong with the citation. Existence, exact venue (CEUR Vol-4177), and topical match on the title are all confirmed; the paper's internal content (which the entry claims to have read in full) is not independently re-verified in this pass.

**Verdict: VERIFIED (existence, venue, and title-level topical match); PARTIAL on the full-text content the entry claims to have read (PDF did not render through the available fetch tooling in this pass).** **For senior review:** if precision on this one matters, a reviewer with direct PDF access should confirm the paper's mechanism description (canonical merge, no detection trigger) against the entry's specific claims — the venue and title are solid, only the full-body verification is outstanding.

### LLMs4OM and KROMA — "round out the landscape"

**Entry location/claim (§7):** "LLMs4OM and KROMA round out the landscape" of LLM-based ontology matching systems, listed alongside SciCo-Radar, GenOM, EDC, KGGen, and CID with no further detail or quotes.

**Checks:** both located via Crossref/reference-list search. **KROMA**: "KROMA: Ontology Matching with Knowledge Retrieval and Large Language Models," authors Lam Nguyen, Erika Barcelos, Roger French, Yinghui Wu, published at ISWC 2025 (DOI 10.1007/978-3-032-09527-5_34) — an LLM-based ontology-matching system, exactly the landscape entry describes. **LLMs4OM**: found directly in KROMA's own reference list — "Giglou, H.B., D'Souza, J., Engel, F., Auer, S.: LLMs4OM: matching ontologies with large language models. In: Proceedings of the 21st European Semantic Web Conference (2024)" — confirming both the name and that it is a real, closely related prior system (ESWC 2024).

**Verdict: VERIFIED (both).** **For senior review:** none.

### AXOLOTL'24 — "novel senses → generated definitions"

**Entry location/claim (§4, §7):** "the AXOLOTL'24 line (novel senses → generated definitions)."

**Checks:** Crossref record confirms "AXOLOTL'24 Shared Task on Multilingual Explainable Semantic Change Modeling," authors Mariia Fedorova, Timothee Mickus, Niko Partanen, Janine Siewert, Elena Spaziani, Andrey Kutuzov, published in *Proceedings of the 5th Workshop on Computational Approaches to Historical Language Change* (ACL 2024, DOI 10.18653/v1/2024.lchange-1.8). A real shared task on detecting and explaining new/changed word senses over time — the "explainable semantic change" framing is precisely "novel senses → [explanations/definitions of what changed]," matching the entry's shorthand.

**Verdict: VERIFIED.** **For senior review:** none.

### Wright & Budin — "ad hoc terminography in terminology science"

**Entry location/claim (§7):** "ad hoc terminography in terminology science (Wright & Budin; Cabré)... known from search-run summaries, not primary texts" (a general field reference, no specific title, page, or quote cited).

**Checks:** Crossref confirms the *Handbook of Terminology Management* (Volumes 1 and 2, John Benjamins, 1997/2001), edited by Sue Ellen Wright (Kent State University) and Gerhard Budin (University of Vienna) — the standard comprehensive reference work in terminology science, exactly matching the entry's field-level citation.

**Verdict: VERIFIED.** **For senior review:** none.

### Cabré — "ad hoc terminography in terminology science"

**Entry location/claim (§7):** same sentence as Wright & Budin, no specific title/quote.

**Checks:** Crossref confirms *Terminology: Theory, Methods and Applications* by Teresa Cabré (Universitat Pompeu Fabra), DOI 10.1075/tlrp.1, John Benjamins, 1999 — the canonical Cabré text founding the Communicative Theory of Terminology, matching the entry's citation.

**Verdict: VERIFIED.** **For senior review:** none.

### Vocabulary Switching System — Niehoff / Battelle (1976)

**Entry location/claim (§7):** "the Vocabulary Switching System (Niehoff/Battelle 1976)" — cited as "read in primary" per the entry's reading-status paragraph, grouped with LAVOHA as an academic canonicalization contrast ("both build merged canonical resources; neither has a detection trigger or generated neutral definitions").

**Checks:** could not open a primary document (two attempted PDF fetches — an ERIC-hosted final report and a Svenonius paper likely citing the original — both failed to render through safefetch/defuddle, returning empty DOM). Verified via independent secondary sources instead: an ERIC catalog record (ED247948) for "Evaluation of the Vocabulary Switching System. Final Report" (1984), authors **Niehoff, Robert; Mack, Greg**, authoring institution **Battelle Memorial Inst., Columbus, OH, Columbus Labs**, describing "an experimental online database consisting of 15 vendor-supplied, controlled subject vocabularies or thesauri... designed to enhance search strategies... by integrating vocabularies into common VSS files" — this independently confirms Niehoff, Battelle, and the "Vocabulary Switching System" name are all real and connected, and that the system existed at least by 1979 (the 1984 report references "a similar 1979 survey"). A separate, confirmed 1976 Niehoff/Battelle Columbus Labs report, "Development of an Integrated Energy Vocabulary" (NTIS PB 253 781), describes building a cross-vocabulary "conversion guide designed for automated, online switching" in the same year — strongly consistent with the entry's 1976 date and topic, though this is a differently-titled report (on energy-domain vocabulary specifically) rather than a confirmed primary titled exactly "Vocabulary Switching System" dated 1976.

**Verdict: PARTIAL.** Existence of Niehoff, Battelle's authorship, and a "Vocabulary Switching System" matching the entry's description are all independently confirmed via secondary sources (ERIC catalog metadata, a closely adjacent same-year same-author same-institution report). What remains unverified: the exact title and 1976 publication date as a single primary document — the fetch tooling could not render either candidate PDF in this pass, so the precise 1976 dating rests on a topically-adjacent report rather than a directly opened primary.

**For senior review:** if this citation is load-bearing anywhere beyond the general "academic canonicalization efforts" contrast (it doesn't appear to be — no verbatim quote or specific claim rides on it), the current level of verification is probably sufficient; a reviewer with library/NTIS access could close this gap by pulling PB 253 781 or the original VSS development report directly.

### Confluence "Define"

**Entry location/claim (§7):** "shipped products reported to do lazy per-workspace LLM definitions (Confluence 'Define,' Slack hover-definitions)... known from search-run summaries, not primary texts."

**Checks:** web search confirms Atlassian Intelligence's "Define" feature in Confluence: "highlight a word on any page and click Define to get an AI-generated explanation right there... instant, context-based definitions without any setup" (corroborated by an Atlassian Community article literally titled "Glossary vs. Confluence AI 'Define': What's the Right Choice for Your Team?"). This is exactly the "lazy per-workspace LLM definitions" behavior the entry attributes to it.

**Verdict: VERIFIED.** **For senior review:** none.

### Slack "hover-definitions"

**Entry location/claim (§7):** same sentence as Confluence Define.

**Checks:** web search found no native Slack feature matching a "hover to see an LLM-generated definition" description. What exists: (1) Slack's own static Help Center "Slack glossary" page (a reference document, not an in-app hover feature); (2) a third-party Slack Marketplace app, "Glossary," which expands acronyms/terms via explicit commands (`/glossary-add`, `/glossary-show`, `/glossary-explain [term]`) rather than hover; (3) recent (2026) Slack AI features (Slackbot agentic updates, summarization) that don't specifically describe hover-triggered definitions either. Given the entry's own admission that this group is "known from search-run summaries, not primary texts," this may reflect a search-run summary that over-specified "hover" as the interaction mechanism, or a feature not well indexed by general web search, or the app in (2) loosely described as "hover" in the original research.

**Verdict: PARTIAL — could not independently confirm a native or well-documented "hover" definition mechanism in Slack; the closest matches (a static glossary page, a command-based third-party app) don't precisely match "hover-definitions."** **For senior review:** worth double-checking against whatever the original search-run summary actually said — this dossier could not reproduce a source describing Slack definitions as hover-triggered specifically, only command-triggered (third-party) or static-reference (native).

### Atlan Sage

**Entry location/claim (§7):** "Atlan Sage reportedly resolves conflicting definitions into one canonical answer — the opposite philosophy; a useful contrast."

**Checks:** Atlan's own current product marketing confirms: "Sage is Atlan's Metric Conflicts agent that finds where two teams define the same metric differently and locks in one certified answer. For example, Sage finds where two teams define the same metric differently — 'MRR' in Finance vs. 'MRR' in Sales... Once a definition is approved, Sage updates it in the glossary and every AI agent that uses it inherits the certified answer." This matches the entry's characterization precisely — Sage is explicitly a canonical-merge/single-certified-answer tool, the architectural opposite of the entry's own no-canonical-merge design.

**Verdict: VERIFIED.** **For senior review:** none — this is one of the entry's stronger product citations; the match is exact.

### GESIS cross-concordances / KoMoHe

**Entry location/claim (§7):** "GESIS cross-concordances / KoMoHe — manual, persistent cross-vocabulary crosswalks for exactly this recall goal, the architectural opposite."

**Checks:** web search located the underlying academic project directly (going beyond the entry's own "known from search-run summaries" standard): "Competence Center Modeling and Treatment of Semantic Heterogeneity" (KoMoHe), a German Federal Ministry for Education and Research–funded project at GESIS that "organize[d], create[d] and manage[d] 'cross-concordances' between controlled vocabularies (thesauri, classification systems, subject heading lists) centered around the social sciences," connecting "25 controlled vocabularies from 11 disciplines and 3 languages... with more than 513,000 relations generated in 64 crosswalks." Also located the academic papers behind it — "Building a Terminology Network for Search: The KoMoHe Project" and related arXiv preprints (0808.0518, 1009.5352) by Philipp Mayr et al. This is a precise match to "manual, persistent cross-vocabulary crosswalks" — large-scale, hand-built (i.e., manual), and stored/reusable (i.e., persistent), exactly the architectural opposite of the entry's on-demand, no-canonical-merge design.

**Verdict: VERIFIED — and better-sourced than the entry's own "search-run summaries" characterization suggests; primary academic literature (not just product pages) was locatable.** **For senior review:** none — if anything, the entry undersells how well-documented this citation is; a reviewer could easily upgrade it from "known from search-run summaries" to a properly cited academic reference if desired.

### Kish — "the Kish design-effect connection"

**Entry location/claim (§2 table note):** "the Kish design-effect connection was asserted internally from day one — a knowing borrowing; the *miss* was the forecasting-aggregation literature." No specific work, year, or quote is cited — just a name-check of the concept's originator (Leslie Kish) alongside "the audit unit"/`m*` coinage.

**Checks:** confirmed "design effect" is a real, standard concept in survey-sampling statistics (Wikipedia REST API summary: "In survey research, the design effect is a number that shows how well a sample of people may represent a larger group of people for a specific measure of interest"). The concept's attribution to Leslie Kish (from his 1965 *Survey Sampling*, Wiley) is well-established textbook knowledge not independently re-verified against a primary source in this pass, since the entry cites no specific work, page, or quote to check it against — there is nothing beyond the bare name to mismatch. (Note: the Wikipedia fetch for "Design effect" tripped 3 HIGH safefetch findings, all `hidden_content` on HTML comments containing MathJax formula markup for the article's equations — false positives from ordinary Wikipedia math rendering, not injection attempts; noted per the third-party-content-safety protocol.)

**Verdict: VERIFIED (concept-existence bar only, matching the entry's own unspecific citation).** **For senior review:** none.

### bge-large-en-v1.5 (embedding model used in the §6 prototype)

**Entry location/claim (§6):** "a local embedding model (`bge-large-en-v1.5`)."

**Checks:** confirmed via Hugging Face model card (`BAAI/bge-large-en-v1.5`) — a real, publicly available embedding model from BAAI's FlagEmbedding project.

**Verdict: VERIFIED.** **For senior review:** none.

---

## Summary table

| # | Citation | Verdict |
|---|---|---|
| 1 | Larsen & Bong (2016), *MIS Quarterly* 40(3):529–551 | VERIFIED |
| 2 | Blair & Maron (1985), *CACM* 28(3):289–299 | VERIFIED (per 07-17 audit + spot-check) |
| 3 | Furnas, Landauer, Gomez & Dumais (1987), *CACM* 30(11):964–971 | VERIFIED (per 07-17 audit + spot-check) |
| 4 | Kelley (1927), pp. 63–64 ("jangle") | VERIFIED (per 07-17 audit) |
| 5 | Thorndike (1904) ("jingle," credits Aikins) | VERIFIED (per 07-17 audit) |
| 6 | Hoekstra (2010), *Semantic Web* 1(1) | VERIFIED (per 07-17 audit + spot-check) |
| 7 | Doctorow, "Metacrap" (2001) | VERIFIED (per 07-17 audit) |
| 8 | Shirky (2003) | VERIFIED (per 07-17 audit) |
| 9 | Star & Griesemer (1989), *Social Studies of Science* 19(3) | VERIFIED (per 07-17 audit + spot-check) |
| 10 | Bowker & Star (1999) | VERIFIED (per 07-17 audit) |
| 11 | Relink (Huang et al., arXiv:2601.07192) | VERIFIED (per 07-17 audit + spot-check) |
| 12 | SciCo-Radar (arXiv:2409.15113) | VERIFIED (per 07-17 audit + spot-check) |
| 13 | GenOM (arXiv:2508.10703) | VERIFIED (per 07-17 audit + spot-check) |
| 14 | EDC (Zhang & Soh, arXiv:2404.03868) | VERIFIED (per 07-17 audit + spot-check) |
| 15 | KGGen (arXiv:2502.09956, NeurIPS 2025) | VERIFIED (per 07-17 audit + spot-check) |
| 16 | Guo et al. (2024), arXiv:2311.09481 | VERIFIED (per 07-17 audit + spot-check) |
| 17 | NeoN (arXiv:2505.15426) | VERIFIED (per 07-17 audit + spot-check) |
| 18 | Microsoft patents US8589791B2 / US10552522B2 | VERIFIED (per 07-17 audit + spot-check) |
| 19 | Sharma et al. (2023), arXiv:2310.13548 | VERIFIED |
| 20 | Perez et al. (2022), arXiv:2212.09251 | VERIFIED |
| 21 | CREPE — Yu, Min, Zettlemoyer & Hajishirzi, ACL 2023, arXiv:2211.17257 | VERIFIED |
| 22 | Bröcker (2008), arXiv:0806.0813 | VERIFIED |
| 23 | DeGroot & Fienberg (1982) | VERIFIED |
| 24 | Clemen & Winkler (1985) | VERIFIED |
| 25 | Raiffa & Schlaifer (1961) | VERIFIED (existence + secondary citation; primary text not opened) |
| 26 | Ho, Hull & Srihari (1994), *IEEE TPAMI* 16(1):66–75 | VERIFIED |
| 27 | Murphy (1973) | VERIFIED |
| 28 | Blackwell (1953), "Equivalent Comparisons of Experiments" | VERIFIED |
| 29 | Franklin, Halevy & Maier (2005) | VERIFIED |
| 30 | Aberer & Cudré-Mauroux (2004) | VERIFIED |
| 31 | Li & Larsen (2011; 2013) | VERIFIED |
| 32 | ALPAC (1966) | VERIFIED |
| 33 | SKOS (`skos:exactMatch` etc.) | VERIFIED |
| 34 | LDOCE (Longman Defining Vocabulary) | VERIFIED |
| 35 | LLMs4OM | VERIFIED |
| 36 | KROMA | VERIFIED |
| 37 | AXOLOTL'24 | VERIFIED |
| 38 | Wright & Budin (*Handbook of Terminology Management*) | VERIFIED |
| 39 | Cabré (*Terminology: Theory, Methods and Applications*) | VERIFIED |
| 40 | Confluence "Define" | VERIFIED |
| 41 | Atlan Sage | VERIFIED |
| 42 | GESIS cross-concordances / KoMoHe | VERIFIED |
| 43 | Kish (design-effect concept) | VERIFIED (concept-existence bar, matching entry's unspecific citation) |
| 44 | bge-large-en-v1.5 (embedding model) | VERIFIED |
| 45 | LAVOHA (CEUR Vol-4177) | PARTIAL (existence/venue/title confirmed; full-text content not independently re-verified — PDF would not render) |
| 46 | Vocabulary Switching System — Niehoff / Battelle (1976) | PARTIAL (Niehoff/Battelle/VSS existence confirmed via secondary sources; exact 1976 primary title/date not directly opened) |
| 47 | Slack "hover-definitions" | PARTIAL (no native Slack hover-definition mechanism located; closest matches are a static glossary page and a command-triggered third-party app) |

**Counts:** 44 VERIFIED, 3 PARTIAL, 0 MISMATCH, 0 UNREACHABLE. Total citations checked: 47.

No MISMATCH or UNREACHABLE verdicts were found in this pass. The one previously-known fabrication (Larsen & Bong 2016's misquoted "9%/3%" sentence, flagged and fixed in the 07-17 audit) was re-verified as correctly fixed, with all newly-added Larsen & Bong material in the current entry text checking out clean against the primary PDF. The highest-stakes citation audited — Bröcker (2008), which the entry uses to mark Program B's central claim "foreclosed" — was independently traced to the specific uniqueness theorem and its formal extension of DeGroot & Fienberg (1982), not just an abstract-level check.


