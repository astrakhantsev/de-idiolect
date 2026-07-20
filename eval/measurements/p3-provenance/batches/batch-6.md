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

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-6.jsonl

## Works to verify

### w-301
{
 "first_author": "Temmerman",
 "authors": "Rita Temmerman",
 "year": 2000,
 "title": "Towards New Ways of Terminology Description: The Sociocognitive Approach",
 "venue": "John Benjamins",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-389: attributed_claim = "Definitions arise locally from discourse/specialist-text descriptions rather than being stipulated globally; owns the non-universal/variable/user-dependent definition thesis, the critique of W\u00fcster's univocity prescriptivism." (hedged=True); source quote: "**Owner + citation:** Rita Temmerman, *Towards New Ways of Terminology Description: The Sociocognitive Approach* (John Benjamins, 2000). ... \"\u2026definitions of the entity intron, the activity blotting and the collective category biotechnology do not originate as stipulations from outside for isolated "

### w-304
{
 "first_author": "Cabr\u00e9",
 "authors": "Cabr\u00e9",
 "year": 1993,
 "title": "La terminolog\u00eda",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-392: attributed_claim = "Definition typology in terminology science, cited by Faber." (hedged=True); source quote: "**Cabr\u00e9, *La terminolog\u00eda* \u2014 1993** (definition typology, cited by Faber)"

### w-319
{
 "first_author": null,
 "authors": "Collibra",
 "year": null,
 "title": "Collibra AI for asset descriptions",
 "venue": "productresources.collibra.com",
 "urls": [
  "https://productresources.collibra.com/docs/collibra/latest/Content/CollibraAI/to_auto-descr.htm"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-407: attributed_claim = "Accelerates creation of descriptions for data assets, always human-approved suggestions; covers definition generation only, not jargon detection or cross-team matching." (hedged=False); source quote: "Native \"Collibra AI for asset descriptions\" covers (b) only... \"Collibra AI helps you accelerate the creation of descriptions for your assets in Collibra... The AI provided descriptions are always considered suggestions.\""

### w-324
{
 "first_author": null,
 "authors": "Informatica",
 "year": null,
 "title": "Informatica CLAIRE",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-412: attributed_claim = "Auto-suggests/auto-generates glossary terms and definitions from technical metadata." (hedged=True); source quote: "**Informatica CLAIRE**, **DvSum** \u2014 both reportedly auto-suggest/auto-generate glossary terms and definitions from technical metadata (per search-engine synthesis only...)"

### w-326
{
 "first_author": null,
 "authors": "Atlassian",
 "year": 2023,
 "title": "Confluence Define (Atlassian Intelligence)",
 "venue": "GA launch",
 "urls": [
  "https://community.atlassian.com/forums/Confluence-articles/Introducing-Define-terms-using-Atlassian-Intelligence-in/ba-p/2556585"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-414: attributed_claim = "Zero-setup, lazy, on-demand definition generation for company-specific terms by analyzing usage across accessible pages; no dedicated glossary view; does not do cross-space/cross-team definition matching." (hedged=False); source quote: "**Confluence \u2014 Atlassian Intelligence \"Define\"** (GA, launched 2023)... \"The AI instantly generates a definition by analyzing how that term is used across all the pages you have permission to see.\" ... \"No setup or maintenance is required, and it immediately starts learning from your existing conten"

### w-338
{
 "first_author": "DeGroot",
 "authors": "DeGroot, M. H., & Fienberg, S. E.",
 "year": 1983,
 "title": "The comparison and evaluation of forecasters.",
 "venue": "The Statistician 32(1\u20132): 12\u201322",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-006: attributed_claim = "Establishes calibration/refinement decomposition and proper scoring for forecast evaluation." (hedged=False); source quote: "**DeGroot, M. H., & Fienberg, S. E. (1983).** \"The comparison and evaluation of forecasters.\" *The Statistician* 32(1\u20132): 12\u201322. \u2014 calibration/refinement and proper scoring."

### w-343
{
 "first_author": "Brier",
 "authors": "Brier",
 "year": 1950,
 "title": null,
 "venue": "Monthly Weather Review 78: 1\u20133",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-011: attributed_claim = "Proper scoring rule foundation explaining why noisy overconfidence is penalized." (hedged=False); source quote: "Proper scoring foundations (why noisy overconfidence is penalized): **Brier (1950)**, *Monthly Weather Review* 78: 1\u20133;"

### w-364
{
 "first_author": "Vickers",
 "authors": "Vickers, A. J. & Elkin, E. B.",
 "year": 2006,
 "title": "Decision Curve Analysis: A Novel Method for Evaluating Prediction Models.",
 "venue": "Medical Decision Making 26(6): 565\u2013574",
 "urls": [
  "https://journals.sagepub.com/doi/10.1177/0272989X06295361"
 ]
}
Occurrences (verify each attributed claim):
- occ_id rec-042: attributed_claim = "Establishes that a model has value only when it beats the default of not using it (net benefit / decision curve analysis)." (hedged=True); source quote: "**Vickers, A. J. & Elkin, E. B. (2006).** \"Decision Curve Analysis: A Novel Method for Evaluating Prediction Models.\" *Medical Decision Making* 26(6): 565\u2013574. \u2014 \"a model has value only when it beats the default of not using it.\" (Verified title/authors/venue; page numbers from memory \u2014 slightly unc"

### w-369
{
 "first_author": "Uma",
 "authors": "Uma, A., Fornaciari, T., Hovy, D., Paun, S., Plank, B., & Poesio, M.",
 "year": 2021,
 "title": "Learning from Disagreement: A Survey.",
 "venue": "Journal of Artificial Intelligence Research, 72, 1385\u20131470",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-058: attributed_claim = "Standard survey of learning from annotator disagreement / human label variation." (hedged=False); source quote: "Uma, A., Fornaciari, T., Hovy, D., Paun, S., Plank, B., & Poesio, M. (2021). \"Learning from Disagreement: A Survey.\" *Journal of Artificial Intelligence Research*, 72, 1385\u20131470. \u2014 the standard survey. (High.)"

### w-371
{
 "first_author": "Dawid",
 "authors": "Dawid & Skene",
 "year": 1979,
 "title": null,
 "venue": "JRSS-C",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-060: attributed_claim = "Aggregates multiple noisy observers' votes toward one latent truth (background/contrast citation, opposite mechanism to the target claim)." (hedged=False); source quote: "(Earlier annotation-uncertainty roots exist too \u2014 e.g., Dawid & Skene, 1979, *JRSS-C*, on aggregating multiple noisy observers \u2014 but that aggregates votes toward one latent truth, the opposite of \"keep the enumerations,\" so I list it only as background.)"

### w-372
{
 "first_author": "Woods",
 "authors": "Woods, K., Kegelmeyer, W.P., & Bowyer, K.",
 "year": 1997,
 "title": "Combination of multiple classifiers using local accuracy estimates.",
 "venue": "IEEE Transactions on Pattern Analysis and Machine Intelligence, 19(4), 405\u2013410",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-061: attributed_claim = "Genuinely early/foundational treatment of the ensemble oracle-style combination concept, using local accuracy estimates." (hedged=True); source quote: "Woods, K., Kegelmeyer, W.P., & Bowyer, K. (1997). \"Combination of multiple classifiers using local accuracy estimates.\" *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 19(4), 405\u2013410."

### w-374
{
 "first_author": "Kuncheva",
 "authors": "Kuncheva, L.I.",
 "year": 2004,
 "title": "Combining Pattern Classifiers: Methods and Algorithms",
 "venue": "Wiley",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-063: attributed_claim = "Standard textbook treatment of combining pattern classifiers (ensemble oracle concept)." (hedged=False); source quote: "Kuncheva, L.I. (2004). *Combining Pattern Classifiers: Methods and Algorithms*. Wiley. (Standard textbook treatment; a 2nd edition exists from 2014.)"
