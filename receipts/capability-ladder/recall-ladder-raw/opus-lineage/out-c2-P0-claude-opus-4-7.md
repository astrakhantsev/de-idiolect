## Honest verdict

I can't confidently identify a single established concept that maps to "the cold-start operating requirement for the audit unit" as a compound phrase. The wording is opaque enough — and the project explicitly describes it as coined vocabulary — that active searching returns partial matches for the pieces but no clean whole. I'll lay out the candidates I actually surfaced, with citations, ranked by fit, and flag confidence.

### Candidates (none of them a confident match)

**1. Auditable unit / audit universe (internal audit / GRC).** "Audit unit" is a real term of art in internal auditing: a discrete entity/process/function/system in the "audit universe" that can be subjected to an audit. If the project is borrowing this literally, then "cold-start operating requirement for the audit unit" would plausibly mean *the minimum conditions a new/uncovered auditable unit must satisfy to first come into scope or to be operable enough to audit*.
- Standard treatment: **IIA (Institute of Internal Auditors), *International Professional Practices Framework (IPPF)***, Standard 2010 – Planning (audit universe / auditable entities). Historical roots go back to Lawrence B. Sawyer, ***Sawyer's Internal Auditing*** (1st ed. IIA, 1973; later editions co-authored). *Uncertain* on the exact edition wording — I'm citing the work from general knowledge, not from a fetched source in this session.
- Confidence in this being the right frame: **low-to-medium.** "Audit unit" is a real term, but "cold-start operating requirement" is not standard vocabulary attached to it in the internal-audit literature I found.

**2. Cold-start problem (recommender systems / ML).** Established, well-defined problem: how to make useful predictions/recommendations for a new user or item with no history.
- Canonical citation: **Andrew I. Schein, Alexandrin Popescul, Lyle H. Ungar, David M. Pennock (2002), "Methods and Metrics for Cold-Start Recommendations," *Proceedings of SIGIR '02*, ACM.** Widely credited as the paper that coined the term in the recommender-systems literature.
- Confidence this is the intended concept: **low.** "Cold start" fits, but "operating requirement" and "audit unit" don't align well with the recsys usage (which frames it as a *problem*, not a *requirement*).

**3. Initial audit engagement — opening balances (financial audit).** The requirements imposed on an auditor undertaking a *first-time* ("cold") audit of an entity — essentially the auditor's cold-start obligations.
- Canonical citation: **International Auditing and Assurance Standards Board (IAASB), ISA 510 – *Initial Audit Engagements — Opening Balances***. The Redrafted version's Basis for Conclusions dates to 2009; the standard itself has earlier antecedents in IFAC's ISA series (pre-2004). ([iaasb.org][basis])
- Confidence: **low.** Matches "cold start" and "audit" thematically but not the phrasing "operating requirement for the audit unit" (ISA 510's requirements bind the auditor, not the auditee).

**4. Black-start capability (power systems).** A generating unit's ability to start without external grid power — a real "cold-start operating requirement" for a generation unit. Established in power engineering.
- Canonical treatment: **NERC's *Glossary of Terms Used in Reliability Standards* and NERC Standard EOP-005 (System Restoration from Blackstart Resources).** The concept and term predate 2015 in NERC and IEEE literature; specific first-use citation I did not pin down. *Uncertain* on the earliest attributable paper.
- Confidence: **very low** as a fit — nothing in the searches ties "audit unit" to power engineering.

**5. Threshold conditions (financial regulation, UK).** Statutory minimum conditions a firm must satisfy to be authorised and remain authorised — the sense of "the minimum to be operational."
- Citation: **Financial Services and Markets Act 2000 (FSMA), Schedule 6**, and the FCA's Threshold Conditions handbook (COND). Pre-2015. ([FCA handbook / FSMA 2000][fca])
- Confidence: **very low** as a fit for this specific phrase.

### What I would need to disambiguate

Whether "audit" here is being used in the internal-audit sense (an auditable entity), the security/logging sense (an audit trail / auditable event), the ML-evaluation sense (a benchmark run), or something else entirely. Without that, the phrase is under-constrained.

### Bottom line

I do not have a citation-supported identification. If forced to bet one field, I'd bet **internal audit / GRC**, with "audit unit" meaning *auditable entity in the audit universe* and "cold-start operating requirement" meaning something the project has coined itself (not standard). But I would not stand behind that guess without further context — treat it as a hypothesis, not an answer.

Sources:
- [Cold start (recommender systems) – Wikipedia](https://en.wikipedia.org/wiki/Cold_start_(recommender_systems))
- [More Accurate Audits with Auditable Units – Pirani](https://www.piranirisk.com/blog/auditable-units-audit)
- [Auditable unit – Auditor's dictionary](https://auditors.en-academic.com/125/auditable_unit)
- [ISA 510 – Initial Audit Engagements: Opening Balances (IFAC/IAASB PDF)](https://www.ifac.org/_flysystem/azure-private/publications/files/A026%202012%20IAASB%20Handbook%20ISA%20510.pdf)
- [Basis for Conclusions: ISA 510 (Redrafted), Initial Audit Engagements — Opening Balances (IAASB)](https://www.iaasb.org/publications/basis-conclusions-isa-510-redrafted-initial-audit-engagements-opening-balances)
- [NERC Reliability Guideline – Operating Reserve Management](https://www.nerc.com/comm/RSTC_Reliability_Guidelines/Reliability_Guideline_Template_Operating_Reserve_Management_Version_3.pdf)
- [Black Start Capability – Emissions-EUETS.com glossary](https://www.emissions-euets.com/internal-electricity-market-glossary/626-black-start-capability)
- [Understanding the FCA's Threshold Conditions – Complyport](https://complyport.com/understanding-the-fcas-threshold-conditions/)
- [FSMA threshold conditions – Practical Law (Thomson Reuters)](https://uk.practicallaw.thomsonreuters.com/8-201-3394)

[basis]: https://www.iaasb.org/publications/basis-conclusions-isa-510-redrafted-initial-audit-engagements-opening-balances
[fca]: https://complyport.com/understanding-the-fcas-threshold-conditions/
