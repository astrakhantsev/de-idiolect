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

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-0.jsonl

## Works to verify

### arxiv:1506.06405
{
 "first_author": "Satop\u00e4\u00e4",
 "authors": "Satop\u00e4\u00e4 et al.",
 "year": null,
 "title": "Combining and Extremizing Real-Valued Forecasts",
 "venue": "arXiv",
 "urls": [
  "https://arxiv.org/pdf/1506.06405"
 ]
}
Occurrences (verify each attributed claim):
- occ_id rec-019: attributed_claim = "Additional treatment of combining and extremizing real-valued forecasts (listed as a source, not discussed in prose)." (hedged=False); source quote: "[Combining and Extremizing Real-Valued Forecasts (Satop\u00e4\u00e4 et al.)](https://arxiv.org/pdf/1506.06405)"

### arxiv:1711.06004
{
 "first_author": null,
 "authors": null,
 "year": 2017,
 "title": "Remedies against the Vocabulary Gap in IR",
 "venue": "arXiv:1711.06004",
 "urls": [
  "https://arxiv.org/abs/1711.06004"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-359: attributed_claim = "Surveys remedies against the vocabulary gap in information retrieval." (hedged=True); source quote: "the arXiv PDF of \"Remedies against the Vocabulary Gap in IR\" (arXiv:1711.06004) \u2014 so ... for the vocabulary-gap remedies paper I have only the search snippet, not its body."

### arxiv:2104.08809
{
 "first_author": "Cattan",
 "authors": "Cattan, Johnson, Weld, Dagan, Beltagy, Downey & Hope",
 "year": 2021,
 "title": "Hierarchical Cross-Document Coreference",
 "venue": "AKBC 2021 (Outstanding Paper)",
 "urls": [
  "https://arxiv.org/abs/2104.08809"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-292: attributed_claim = "Infers coreference clusters and a referential hierarchy between clusters of scientific concept mentions across documents." (hedged=False); source quote: "[SciCo (Cattan, Johnson, Weld, Dagan, Beltagy, Downey & Hope, AKBC 2021, Outstanding Paper)](https://arxiv.org/abs/2104.08809) \u2014 \"Hierarchical Cross-Document Coreference\" for scientific concepts."

### w-002
{
 "first_author": "Good",
 "authors": "Good",
 "year": 1950,
 "title": "Probability and the Weighing of Evidence",
 "venue": "Griffin",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-043: attributed_claim = "Origin of the additive log-odds/weight-of-evidence form." (hedged=False); source quote: "Good, *Probability and the Weighing of Evidence* (Griffin, 1950) for the additive log-odds/weight-of-evidence form, and *Good Thinking* (Univ. of Minnesota Press, 1983) for the \"device of imaginary results,\" which is the reverse-Bayes ancestor."
- occ_id def-085: attributed_claim = "Origin of log-odds weight of evidence as an additive quantity." (hedged=False); source quote: "I.J. Good, *Probability and the Weighing of Evidence* (Griffin, 1950) \u2014 origin of log-odds \"weight of evidence\" as an additive quantity;"

### w-006
{
 "first_author": "Ranjan",
 "authors": "Ranjan & Gneiting",
 "year": 2010,
 "title": null,
 "venue": "JRSS-B",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-006: attributed_claim = "Treats the lambda extremization parameter for pooling probability forecasts." (hedged=False); source quote: "For the \u03bb parameter specifically: Ranjan & Gneiting (2010), *JRSS-B*; Baron, Mellers, Tetlock, Ungar (2014), \"Two Reasons to Make Aggregated Probability Forecasts More Extreme,\" *Decision Analysis*; Satop\u00e4\u00e4 et al. (2014), \"Combining Multiple Probability Predictions Using a Simple Logit Model,\" *Inte"

### w-007
{
 "first_author": "Baron",
 "authors": "Baron, Mellers, Tetlock, Ungar",
 "year": 2014,
 "title": "Two Reasons to Make Aggregated Probability Forecasts More Extreme",
 "venue": "Decision Analysis",
 "urls": [
  "https://doi.org/10.1287/deca.2014.0293"
 ]
}
Occurrences (verify each attributed claim):
- occ_id rec-015: attributed_claim = "Founding empirical/conceptual justification for extremizing pooled probability forecasts." (hedged=False); source quote: "**Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., & Ungar, L. H. (2014).** \"Two Reasons to Make Aggregated Probability Forecasts More Extreme.\" *Decision Analysis*, 11(2), 133\u2013145. https://doi.org/10.1287/deca.2014.0293 \u2014 the founding empirical/conceptual justification for extremizing pooled f"

### w-016
{
 "first_author": "Thompson",
 "authors": "Thompson & Fearn",
 "year": 1996,
 "title": "What Exactly Is Fitness for Purpose in Analytical Measurement?",
 "venue": "Analyst",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-016: attributed_claim = "Defines fitness-for-purpose / target measurement uncertainty specification." (hedged=False); source quote: "Thompson & Fearn (1996), \"What Exactly Is Fitness for Purpose in Analytical Measurement?\", *Analyst*;"

### w-023
{
 "first_author": "Chow",
 "authors": "Chow",
 "year": 1970,
 "title": "On Optimum Recognition Error and Reject Tradeoff",
 "venue": "IEEE Transactions on Information Theory",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-068: attributed_claim = "Classic reject-option classification result: optimum error/reject tradeoff." (hedged=False); source quote: "Chow, \"An optimum character recognition system using decision functions,\" *IRE Trans. Electronic Computers* (1957), and \"On optimum recognition error and reject tradeoff,\" *IEEE Trans. Information Theory* 16(1) (1970)."

### w-024
{
 "first_author": "Green",
 "authors": "Green & Swets",
 "year": 1966,
 "title": "Signal Detection Theory and Psychophysics",
 "venue": "Wiley",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-218: attributed_claim = "Canonical book-length treatment of signal detection theory's sensitivity/criterion split." (hedged=False); source quote: "Green & Swets (1966), *Signal Detection Theory and Psychophysics* (Wiley) \u2014 the canonical book."
- occ_id def-250: attributed_claim = "Canonical textbook establishing sensitivity vs criterion as separate, orthogonal quantities." (hedged=False); source quote: "Green, D.M. & Swets, J.A. (1966). *Signal Detection Theory and Psychophysics*. Wiley. \u2014 the canonical textbook that established sensitivity (d\u2032) vs. criterion (\u03b2/c) as separate, orthogonal quantities. High confidence."

### w-027
{
 "first_author": "Schwartz",
 "authors": "Chow/Schwartz and colleagues at BBN",
 "year": null,
 "title": null,
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-027: attributed_claim = "Early N-best oracle analysis in ASR (best-of-list vs realized accuracy) attributed to Chow/Schwartz and colleagues at BBN circa 1989-1990." (hedged=True); source quote: "N-best oracle analyses from ASR circa 1989\u20131990 (Chow/Schwartz and colleagues at BBN \u2014 exact citation hedged);"

### w-028
{
 "first_author": "Collins",
 "authors": "Collins",
 "year": 2000,
 "title": null,
 "venue": "ICML",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-028: attributed_claim = "Discriminative reranking demonstrating oracle-vs-realized accuracy gap." (hedged=False); source quote: "Collins (2000), discriminative reranking, ICML;"

### w-031
{
 "first_author": "Kadavath",
 "authors": "Kadavath et al.",
 "year": 2022,
 "title": "Language Models (Mostly) Know What They Know",
 "venue": "arXiv",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-031: attributed_claim = "Calibration-of-abstention work showing models know more than they show." (hedged=False); source quote: "\"models know more than they show\" / calibration-of-abstention work (e.g., Kadavath et al. 2022, \"Language Models (Mostly) Know What They Know,\" arXiv)."
