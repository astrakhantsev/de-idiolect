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

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-4.jsonl

## Works to verify

### w-205
{
 "first_author": null,
 "authors": null,
 "year": 2024,
 "title": "Panel of LLM evaluators (PoLL)",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-257: attributed_claim = "Panel-of-LLM-evaluators approach to LLM-as-judge panels." (hedged=True); source quote: "I recall a paper nicknamed \"PoLL\" \u2014 Panel of LLM evaluators \u2014 from ~2024, though I can't give you author/venue with confidence"

### w-206
{
 "first_author": "Bowman",
 "authors": "Bowman et al.",
 "year": 2022,
 "title": "Measuring Progress on Scalable Oversight for Large Language Models",
 "venue": "Anthropic",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-258: attributed_claim = "Scalable oversight framing for judge/verification systems." (hedged=True); source quote: "and \"scalable oversight\" (Bowman et al., \"Measuring Progress on Scalable Oversight for Large Language Models,\" 2022, Anthropic \u2014 moderate confidence on this one) before falling back to the older statistics/psychometrics lineages I cited above."

### w-207
{
 "first_author": "Furnas",
 "authors": "Furnas, Landauer, Gomez & Dumais",
 "year": 1987,
 "title": "The vocabulary problem in human-system communication",
 "venue": "CACM 30(11)",
 "urls": [
  "https://dl.acm.org/doi/10.1145/32206.32212"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-296: attributed_claim = "The vocabulary problem: two people rarely choose the same term for the same thing." (hedged=False); source quote: "the **vocabulary problem** / **vocabulary mismatch** (Furnas, Landauer, Gomez & Dumais 1987, *Communications of the ACM* 30(11):964\u2013971 \u2014 pre-2015)"

### w-210
{
 "first_author": null,
 "authors": "W3C",
 "year": 2009,
 "title": "SKOS Reference, section 10.1",
 "venue": "W3C Recommendation",
 "urls": [
  "https://www.w3.org/TR/skos-reference/"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-263: attributed_claim = "Standardized mapping-relation inventory (exact/broad/narrow/related match) for typed pairwise concept correspondences." (hedged=False); source quote: "The [W3C SKOS Reference (2009), \u00a710.1](https://www.w3.org/TR/skos-reference/) says: \"The SKOS mapping properties are `skos:closeMatch`, `skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch` and `skos:relatedMatch`.\""

### w-213
{
 "first_author": null,
 "authors": "NLM",
 "year": 1986,
 "title": "UMLS Metathesaurus",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-354: attributed_claim = "Shared-master-list paradigm for concept normalization, the architectural opposite of the described tool's no-persistent-crosswalk design." (hedged=True); source quote: "**Concept normalization / entity linking to a metathesaurus (e.g., UMLS)** \u2014 this is the *shared-master-list* paradigm. ... *(Background knowledge; I did not fetch a UMLS source this session.)*"

### w-214
{
 "first_author": "Bourigault",
 "authors": "Bourigault",
 "year": 1992,
 "title": "Surface grammatical analysis for the extraction of terminological noun phrases",
 "venue": "COLING 1992",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-267: attributed_claim = "LEXTER: term-extraction algorithm via surface grammatical analysis." (hedged=True); source quote: "**Part 1.** Bourigault, \"Surface grammatical analysis for the extraction of terminological noun phrases,\" COLING 1992 (LEXTER)."

### w-219
{
 "first_author": "Renouf",
 "authors": "Renouf",
 "year": null,
 "title": "AVIATOR project",
 "venue": "Birmingham",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-272: attributed_claim = "Corpus monitoring of neologisms (early neologism detection)." (hedged=True); source quote: "Corpus monitoring of neologisms goes back to Renouf's AVIATOR project (early 1990s, Birmingham) \u2014 details hedged, not verified this session."

### w-222
{
 "first_author": "W\u00fcster",
 "authors": "W\u00fcster",
 "year": 1931,
 "title": "Internationale Sprachnormung in der Technik",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-280: attributed_claim = "Founds terminology science; later codified in ISO 704's terminological definition standard." (hedged=True); source quote: "Terminological definition-writing: W\u00fcster's 1931 *Internationale Sprachnormung in der Technik* founding terminology science, codified in ISO 704."

### w-225
{
 "first_author": "Niehoff",
 "authors": "Niehoff",
 "year": 1976,
 "title": "Development of an Integrated Energy Vocabulary",
 "venue": "Battelle Columbus Laboratories",
 "urls": [
  "https://files.eric.ed.gov/fulltext/ED247948.pdf"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-283: attributed_claim = "Grew into the Vocabulary Switching System for automated subject switching across databases indexed with different thesauri." (hedged=False); source quote: "the oldest engineered treatment I verified is [Niehoff's Battelle work](https://files.eric.ed.gov/fulltext/ED247948.pdf): *Development of an Integrated Energy Vocabulary\u2026*, Battelle Columbus Laboratories, 1976, which grew into the **Vocabulary Switching System** for \"automated subject switching\" acr"

### w-228
{
 "first_author": "Doan",
 "authors": "Doan, Madhavan, Domingos & Halevy",
 "year": 2002,
 "title": "GLUE",
 "venue": "WWW 2002",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-286: attributed_claim = "GLUE: schema/ontology matching system." (hedged=True); source quote: "Doan, Madhavan, Domingos & Halevy, GLUE, WWW 2002;"

### w-229
{
 "first_author": "Giunchiglia",
 "authors": "Giunchiglia, Shvaiko & Yatskevich",
 "year": 2004,
 "title": "S-Match",
 "venue": "ESWS 2004",
 "urls": [
  "https://link.springer.com/chapter/10.1007/978-3-540-74987-5_1"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-287: attributed_claim = "S-Match: semantic matching with typed relations (equivalence, more/less general)." (hedged=False); source quote: "[Giunchiglia, Shvaiko & Yatskevich, S-Match, ESWS 2004](https://link.springer.com/chapter/10.1007/978-3-540-74987-5_1) (typed relations: equivalence, more/less general);"

### w-230
{
 "first_author": "Euzenat",
 "authors": "Euzenat & Shvaiko",
 "year": 2007,
 "title": "Ontology Matching",
 "venue": "Springer",
 "urls": [
  "http://book.ontologymatching.org/"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-288: attributed_claim = "The ontology-matching field's textbook." (hedged=True); source quote: "Euzenat & Shvaiko, *Ontology Matching*, Springer, 2007 (the field's textbook; OAEI benchmark campaigns run since ~2004)."
- occ_id def-364: attributed_claim = "Ontology matching: finding correspondences (equivalence and other relations) between semantically related entities of different conceptualizations; already has an 'instance-based' matching category close in spirit to per-item matching." (hedged=False); source quote: "**Euzenat & Shvaiko, *Ontology Matching* (Springer, 2007; 2nd ed. 2013)** ... \"Ontology matching as a field is exactly 'finding correspondences between semantically related entities of different [conceptualizations]... equivalence as well as other relations, such as consequence, subsumption, or disj"
