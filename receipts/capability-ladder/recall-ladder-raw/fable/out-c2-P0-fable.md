I've identified the concept with direct confirmation from primary sources. Here is the report.

## 1. What the concept is called in established fields

The "cold-start operating requirement for the audit unit" corresponds to the **"experienced auditor" test** (also called the **experienced-auditor standard**) in audit documentation standards: the requirement that audit working papers contain sufficient information to enable **"an experienced auditor, having no previous connection with the engagement"** to understand the work performed, the evidence obtained, and the conclusions reached — i.e., a reviewer starting completely cold must be able to operate from the record alone. The PCAOB's own basis-for-conclusions names the underlying principle the **"reviewability standard"** ([AS 3 Appendix A, ¶A13](https://pcaobus.org/oversight/standards/archived-standards/details/Auditing_Standard_3_Appendix_A)). The matching practice term for the reviewer themselves is a **"cold review" / "cold file review"** — a post-issuance quality review performed by someone unconnected with the engagement, as opposed to a pre-signing "hot review" ([CCS explainer](https://ccs-co.com/post/what-are-a-hot-and-a-cold-file-review/), [ICAEW helpsheet](https://www.icaew.com/technical/tas-helpsheets/practice/cold-file-audit-compliance-review)). The mapping is nearly word-for-word: "cold-start" ↔ "no previous connection with the engagement" (a "cold" reviewer); "operating requirement" ↔ documentation-sufficiency requirement; "audit unit" ↔ the audit file/reviewing auditor.

## 2. Which fields own it

**Financial auditing / public accountancy** (auditing standard-setting and audit-quality regulation), with its documented origin specifically in **government auditing** (GAGAS, the GAO "Yellow Book"). It now sits in the professional standards of the PCAOB, IAASB, AICPA, and GAO.

## 3. Oldest and most canonical treatments

- **U.S. General Accounting Office, *Government Auditing Standards: 1994 Revision* (GAO/OCG-94-4, June 1994)** — the oldest codification I could pin down. A contemporaneous account confirms the 1994 revision introduced, as an additional GAGAS field-work standard, that working papers be sufficient "to enable an experienced auditor having no previous connection with the audit subsequently to ascertain from them the evidence that supports the auditors' significant conclusions and judgments" (Brown, Melchin & Raghunandan, ["The 1994 revisions to 'Government Auditing Standards'"](http://archives.cpajournal.com/old/16641856.htm), *The CPA Journal*, Feb. 1995). The GAO's rationale: government audits have long been reviewed by GAO auditors who did not participate in the original audit. See also the [2003 Revision (GAO-03-673G)](https://www.gao.gov/assets/gao-03-673g.pdf), ¶4.22 — the version the PCAOB cites.
- **PCAOB Auditing Standard No. 3, *Audit Documentation* (Release No. 2004-006, June 2004; effective Nov. 15, 2004)**, now codified as [AS 1215](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1215), ¶.06A — I verified the exact text: "Audit documentation must contain sufficient information to enable an experienced auditor, having no previous connection with the engagement…" Its [Appendix A](https://pcaobus.org/oversight/standards/archived-standards/details/Auditing_Standard_3_Appendix_A) explicitly adapts the GAO standard and links it to the **Panel on Audit Effectiveness, *Report and Recommendations* (Public Oversight Board, Aug. 31, 2000)**, which recommended documentation sufficient for reviewers outside the firm.
- **IAASB, ISA 230 (Revised), *Audit Documentation* (effective for periods beginning on/after June 15, 2006; redrafted 2008)**, ¶8 — the international version, widely taught as ["the experienced auditor test"](https://ciferi.com/blog/isa-230-audit-documentation-guide) ([IAASB project page](https://www.iaasb.org/consultations-projects/audit-documentation-isa-230), [IFAC handbook text](https://www.ifac.org/system/files/publications/files/A012%202012%20IAASB%20Handbook%20ISA%20230.pdf)).
- The AICPA equivalent for U.S. private-company audits is SAS No. 103, *Audit Documentation* (2005), today AU-C 230 — **uncertain**: cited from background knowledge; I did not open this one directly.

## 4. Confidence

- That the coined phrase maps to the experienced-auditor / reviewability standard: **high (~90%)**. The three distinctive elements (cold start, an operating requirement, an audit unit) align almost term-for-term, and the profession independently uses "cold" for exactly this kind of no-prior-connection review. Residual uncertainty: the snippet is one line, and if the project's "audit unit" is actually a software component required to boot statelessly, the nearer analog would be statelessness/crash-only design from systems engineering — but nothing in the wording favors that reading.
- PCAOB AS 1215 ¶.06A text and the AS 3 Appendix A "reviewability standard"/GAO lineage: **high** — fetched and quoted directly.
- 1994 Yellow Book as the oldest codification: **high** that the language is in the 1994 revision (contemporaneous CPA Journal quote; the article implies it was new in 1994, i.e., not in the 1988 edition — **moderately confident** it's genuinely the first appearance; I could not grep the GAO PDF itself, as safefetch returned no text for it).
- ISA 230 dates and ¶8 wording: **high**, from multiple corroborating sources, though I read the text via secondary pages rather than the IFAC PDF itself.

One safety note: the CCS hot/cold-review page triggered a LOW safefetch finding — two invisible Unicode variation selectors, which were stripped. That's a benign artifact (emoji encoding), not a prompt injection; content was otherwise clean.

Sources:
- [AS 1215: Audit Documentation | PCAOB](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1215)
- [Auditing Standard No. 3, Appendix A: Background and Basis for Conclusions | PCAOB](https://pcaobus.org/oversight/standards/archived-standards/details/Auditing_Standard_3_Appendix_A)
- [Government Auditing Standards: 1994 Revision | U.S. GAO](https://www.gao.gov/products/ocg-94-4)
- [GAO-03-673G, Government Auditing Standards (2003 Revision)](https://www.gao.gov/assets/gao-03-673g.pdf)
- [The 1994 revisions to 'Government Auditing Standards' — The CPA Journal, Feb. 1995](http://archives.cpajournal.com/old/16641856.htm)
- [Audit Documentation - ISA 230 | IAASB](https://www.iaasb.org/consultations-projects/audit-documentation-isa-230)
- [ISA 230 (2012 IAASB Handbook) | IFAC](https://www.ifac.org/system/files/publications/files/A012%202012%20IAASB%20Handbook%20ISA%20230.pdf)
- [ISA 230: The Experienced Auditor Test and File Assembly | ciferi](https://ciferi.com/blog/isa-230-audit-documentation-guide)
- [What are a 'Hot' and a 'Cold' file Review? | CCS](https://ccs-co.com/post/what-are-a-hot-and-a-cold-file-review/)
- [Cold file audit compliance review | ICAEW](https://www.icaew.com/technical/tas-helpsheets/practice/cold-file-audit-compliance-review)
