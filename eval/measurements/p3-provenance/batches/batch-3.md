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

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-3.jsonl

## Works to verify

### w-135
{
 "first_author": "Ogden",
 "authors": "C. K. Ogden",
 "year": 1930,
 "title": "Basic English",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-187: attributed_claim = "Predecessor vocabulary-control movement that seeded modern learner's-dictionary defining vocabularies." (hedged=True); source quote: "Predecessor in lexicography proper: the vocabulary-control movement of the 1920s\u201330s (Ogden's Basic English, 1930) ... the 1930s lexicography claim is medium \u2014 from an earlier search summary, not independently read."
- occ_id def-275: attributed_claim = "Ancestral controlled natural language / defining vocabulary (850-word core)." (hedged=True); source quote: "Ogden, *Basic English*, 1930 (ancestral CNL)."

### w-137
{
 "first_author": null,
 "authors": null,
 "year": 1978,
 "title": "Longman Dictionary of Contemporary English",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-308: attributed_claim = "Controlled defining vocabulary (~2,000 words)." (hedged=False); source quote: "Longman Dictionary of Contemporary English defining vocabulary, **1978**."

### w-139
{
 "first_author": "Madhavan",
 "authors": "Madhavan et al.",
 "year": 2007,
 "title": "Web-scale Data Integration: You can only afford to Pay As You Go",
 "venue": "CIDR 2007",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-172: attributed_claim = "Web-scale data integration must be pay-as-you-go rather than upfront schema-complete." (hedged=True); source quote: "and Madhavan et al., \"Web-scale Data Integration: You can only afford to Pay As You Go,\" CIDR 2007."

### w-143
{
 "first_author": "Nguyen",
 "authors": "Nguyen, Barcelos, French & Wu",
 "year": 2025,
 "title": "KROMA",
 "venue": "arXiv:2507.14032",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-176: attributed_claim = "Uses LLMs within a RAG pipeline to dynamically enrich semantic context of ontology matching with structural, lexical, and definitional knowledge; adds bisimilarity-based concept matching." (hedged=True); source quote: "Nguyen, Barcelos, French & Wu, 2025 \u2014 arXiv:2507.14032 ... Confidence: low/medium \u2014 abstract-only, could not verify body claims."

### w-144
{
 "first_author": null,
 "authors": null,
 "year": null,
 "title": "OLaLa",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-177: attributed_claim = "Uses LLaMA-2 models and BERT retrievers to extract top-k ontology matches for LLM prompts, refined with a precision matcher and filters." (hedged=True); source quote: "**OLaLa** (mentioned inside GenOM/LLMs4OM's related work, not independently fetched) ... \"OLaLa [21] utilizes LLaMA-2 models and BERT retrievers to extract top-k matches from target ontologies for LLM prompts, refining final alignments with a precision matcher and filters.\" ... Confidence: low \u2014 sec"

### w-151
{
 "first_author": "Bilac",
 "authors": "Bilac et al.",
 "year": 2004,
 "title": null,
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-185: attributed_claim = "First IR-based reverse-dictionary system: finds the closest definition in a database and returns the corresponding word." (hedged=True); source quote: "Runner-up, closer to your exact framing (definition as *search key*): Bilac et al., 2004, first IR-based reverse-dictionary system \u2014 \"they first built a database based on available dictionaries. When a query came in, the system would find the closest definition in the database, then return the corre"

### w-168
{
 "first_author": "Neyman",
 "authors": "Neyman & Pearson",
 "year": 1933,
 "title": null,
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-206: attributed_claim = "Risk framing (Type I/II error) underlying operating characteristic curves." (hedged=False); source quote: "Neyman & Pearson (1933) for the risk framing;"

### w-170
{
 "first_author": "Stringer",
 "authors": "Stringer",
 "year": 1963,
 "title": null,
 "venue": "ASA Business and Economic Statistics Section proceedings (believed)",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-208: attributed_claim = "Statistical sampling method for audit risk (the Stringer bound), relating tolerable deviation rate and acceptable risk of overreliance." (hedged=True); source quote: "in auditing, Stringer's work on statistical sampling at Haskins & Sells from the early 1960s ... less sure of Stringer's exact venue, which I believe was an ASA Business and Economic Statistics Section proceedings paper around 1963 \u2014 verify before citing."

### w-173
{
 "first_author": "Clopper",
 "authors": "Clopper & Pearson",
 "year": 1934,
 "title": null,
 "venue": "Biometrika",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-211: attributed_claim = "Confidence interval width as a function of sample size n, for estimating a proportion." (hedged=False); source quote: "Oldest anchors: Wilson (1927, *JASA*) and Clopper\u2013Pearson (1934, *Biometrika*) for interval width as a function of n;"

### w-182
{
 "first_author": "Platt",
 "authors": "Platt",
 "year": 1999,
 "title": null,
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-225: attributed_claim = "Calibration method for classifier scores (Platt scaling), relevant to the discrimination-vs-calibration distinction." (hedged=False); source quote: "On the calibration side: Platt (1999), Zadrozny & Elkan (2002, KDD), Niculescu-Mizil & Caruana (2005, ICML)."

### w-189
{
 "first_author": "Stasser",
 "authors": "Stasser & Titus",
 "year": 1985,
 "title": "Pooling of unshared information in group decision making",
 "venue": "JPSP 48(6)",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-232: attributed_claim = "Hidden-profile paradigm: a scalar vote discards information the judge actually surfaced." (hedged=False); source quote: "Stasser & Titus (1985), \"Pooling of unshared information in group decision making,\" *JPSP* 48(6) \u2014 the hidden-profile paradigm, and the single best pointer if your claim is \"the vote hides what the judge knew.\""

### w-199
{
 "first_author": "Gelman",
 "authors": "Gelman et al.",
 "year": 1995,
 "title": "Bayesian Data Analysis",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-247: attributed_claim = "Popularized/solidified the 'burn-in' term as a named requirement." (hedged=True); source quote: "often attributed loosely to Gelman et al.'s *Bayesian Data Analysis*, first edition 1995. Low confidence on precise attribution of the term itself."
