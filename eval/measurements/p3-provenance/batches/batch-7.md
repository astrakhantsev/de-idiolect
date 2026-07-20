You are verifying model-proposed citations against primary sources for a provenance study. For EACH work below, follow this frozen protocol:

1. Locate the primary source: up to 3 search queries (WebSearch) + up to 2 page fetches per work. Fetch pages with the BARE `safefetch <url>` command via Bash — never WebFetch, never curl. If the natural page is unreachable, try the Wayback Machine (https://web.archive.org/web/2024/<url>). Then stop.
2. Grade three facets:
   - exists: "yes" | "no" | "unverifiable" — does a published work matching this citation exist?
   - biblio: "full" (authors + venue + year all match; year exactly) | "minor" (year off by 1, OR journal-vs-proceedings variant, OR subtitle truncation — note which) | "major" (wrong venue, wrong authors, or year off by more than 1) | null if exists != yes
   - per-occurrence claim_support: "supported" (the attributed claim is plausibly present at abstract/title level of the located primary) | "not_locatable" (work exists but the claim is not visible at abstract/title level) | "contradicted" (the abstract/title actively contradicts the attribution) — one verdict per occurrence listed under the work.
3. Receipts REQUIRED: for every exists=yes verdict, record the URL you fetched and a VERBATIM snippet (title line or abstract sentence) from the fetched page that supports your biblio + claim verdicts. No snippet = downgrade to unverifiable.
4. Do NOT judge whether the work truly "owns" the concept — only existence, bibliography, and whether the attributed claim is plausibly in it.

Append your verdicts as JSON lines to the output file given below, one line per work, schema:
{"work_id": "...", "exists": "...", "biblio": "...", "biblio_notes": "...", "primary_url": "...", "evidence_snippet": "...", "occurrences": [{"occ_id": "...", "claim_support": "...", "note": "..."}], "queries_used": N, "fetches_used": N}

Work through the list IN ORDER, writing each verdict line as you complete it (append as you go — do not batch at the end). Your final report: counts by exists/biblio grade + the output file path.

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-7.jsonl

## Works to verify

### w-376
{
 "first_author": "Sp\u00e4rck Jones",
 "authors": "Sp\u00e4rck Jones, K., & van Rijsbergen, C.J.",
 "year": 1975,
 "title": "Report on the need for and provision of an 'ideal' information retrieval test collection.",
 "venue": "British Library Research and Development Report No. 5266, Computer Laboratory, University of Cambridge",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-066: attributed_claim = "Originating report for IR 'pooling' \u2014 union of top-ranked document sets from many systems for judging." (hedged=True); source quote: "Sp\u00e4rck Jones, K., & van Rijsbergen, C.J. (1975). \"Report on the need for and provision of an 'ideal' information retrieval test collection.\" British Library Research and Development Report No. 5266, Computer Laboratory, University of Cambridge. Confidence: medium \u2014 well corroborated as the originati"

### w-382
{
 "first_author": "Hertzum",
 "authors": "Hertzum, M., & Jacobsen, N. E.",
 "year": 2001,
 "title": "The Evaluator Effect: A Chilling Fact About Usability Evaluation Methods.",
 "venue": "International Journal of Human-Computer Interaction, 13(4), 421-443 (orig. 2001); reprinted/corrected 15(1), 183-204 (2003)",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-072: attributed_claim = "Definitive statement of why votes/agreement among evaluators mislead \u2014 inter-evaluator agreement is often only 5-65%." (hedged=True); source quote: "**Hertzum, M., & Jacobsen, N. E. \"The Evaluator Effect: A Chilling Fact About Usability Evaluation Methods.\" *International Journal of Human\u2013Computer Interaction*.** Originally 2001, 13(4), 421\u2013443; reprinted/corrected 2003, 15(1), 183\u2013204. The definitive statement of why votes/agreement mislead (an"

### w-383
{
 "first_author": "Eick",
 "authors": "Eick, S. G., Loader, C. R., Long, M. D., Votta, L. G., & Vander Wiel, S. A.",
 "year": 1992,
 "title": "Estimating Software Fault Content Before Coding.",
 "venue": "Proc. 14th ICSE, Melbourne, pp. 59\u201365",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-073: attributed_claim = "Seminal application of capture-recapture statistics to software inspection, using overlap between evaluators' enumerations to estimate undetected defects." (hedged=True); source quote: "**Eick, S. G., Loader, C. R., Long, M. D., Votta, L. G., & Vander Wiel, S. A. (1992). \"Estimating Software Fault Content Before Coding.\" *Proc. 14th ICSE*, Melbourne, pp. 59\u201365.** The seminal application of capture\u2013recapture to inspection \u2014 the formal machinery behind \"use the overlap between enumer"

### w-388
{
 "first_author": "Conitzer",
 "authors": "Conitzer & Sandholm",
 "year": 2005,
 "title": "Common Voting Rules as Maximum Likelihood Estimators",
 "venue": "UAI 2005",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-086: attributed_claim = "Pre-2015 anchor viewing voting rules, including approval voting, as maximum-likelihood estimators of a hidden true answer." (hedged=False); source quote: "**Conitzer & Sandholm** (2005), \"Common Voting Rules as Maximum Likelihood Estimators,\" *UAI 2005* \u2014 pre-2015 anchor for viewing voting rules (approval among them) as estimators of a hidden true answer."

### w-390
{
 "first_author": "Coombs",
 "authors": "Coombs, C. H.",
 "year": 1953,
 "title": "On the use of objective examinations.",
 "venue": "Educational and Psychological Measurement, 13(2), 308\u2013310",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-088: attributed_claim = "Instructs test-takers to cross out wrong alternatives rather than commit to one \u2014 list every defensible remaining candidate." (hedged=False); source quote: "Coombs, C. H. (1953). \"On the use of objective examinations.\" *Educational and Psychological Measurement*, 13(2), 308\u2013310. \u2014 explicitly instructs test\u2011takers to \"cross out all the alternatives which they consider wrong,\" i.e., list every defensible remaining candidate rather than commit to one."

### w-395
{
 "first_author": "Wells",
 "authors": "Wells, W. F.",
 "year": 1934,
 "title": "On air-borne infection: Study II. Droplets and droplet nuclei.",
 "venue": "American Journal of Hygiene, 20(3), 611\u2013618",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-106: attributed_claim = "Foundational physics paper establishing the evaporation-falling curve and the actual ~100 micron size cutoff." (hedged=False); source quote: "Wells WF. **\"On air-borne infection. Study II: Droplets and droplet nuclei.\"** *American Journal of Hygiene*, 1934, 20(3):611\u2013618. \u2014 Foundational physics paper; establishes the evaporation-falling curve and the actual ~100 \u03bcm size cutoff. (Confidence: high \u2014 verified via Oxford Academic listing and "

### w-398
{
 "first_author": "Chapin",
 "authors": "Chapin, C. V.",
 "year": 1910,
 "title": "The Sources and Modes of Infection",
 "venue": "New York: John Wiley & Sons",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-099: attributed_claim = "Historical root of the contact/droplet paradigm that entrenched resistance to recognizing airborne transmission." (hedged=True); source quote: "**Chapin, C. V. (1910). *The Sources and Modes of Infection*. New York: John Wiley & Sons.** \u2014 The historical root of the contact/droplet paradigm that entrenched resistance to airborne transmission (the \"Chapin paradigm\" the debunkers blame). (Confidence: high on relevance; medium that you'd cite i"

### w-403
{
 "first_author": "Bourouiba",
 "authors": "Bourouiba, L.",
 "year": 2020,
 "title": "Turbulent Gas Clouds and Respiratory Pathogen Emissions: Potential Implications for Reducing Transmission of COVID-19.",
 "venue": "JAMA, 323(18), 1837\u20131838",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-104: attributed_claim = "Widely cited 'up to ~8 meters' gas-cloud argument against the fixed 1-2m droplet-fall rule." (hedged=False); source quote: "**Bourouiba, L. (2020). \"Turbulent Gas Clouds and Respiratory Pathogen Emissions: Potential Implications for Reducing Transmission of COVID-19.\" *JAMA*, 323(18), 1837\u20131838.** \u2014 The widely cited \"up to ~8 m\" gas-cloud argument against the 1\u20132 m rule. (Confidence: high.)"
- occ_id rec-113: attributed_claim = "Shows droplets travel inside a turbulent gas cloud up to ~7-8 meters, undermining the fixed-distance droplet/airborne dichotomy." (hedged=False); source quote: "Bourouiba L. **\"Turbulent Gas Clouds and Respiratory Pathogen Emissions: Potential Implications for Reducing Transmission of COVID-19.\"** *JAMA*, 2020, 323(18):1837\u20131838. doi:10.1001/jama.2020.4756. \u2014 Shows droplets travel inside a gas cloud up to ~7\u20138 m, undermining the fixed-distance droplet/airbo"
