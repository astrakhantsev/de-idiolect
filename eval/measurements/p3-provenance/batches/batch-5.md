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

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-5.jsonl

## Works to verify

### w-235
{
 "first_author": "Miles",
 "authors": "Miles & Bechhofer",
 "year": 2009,
 "title": "SKOS Reference",
 "venue": "W3C Recommendation",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-294: attributed_claim = "Standardizes broadMatch/narrowMatch/relatedMatch mapping relations between concepts across knowledge organization systems." (hedged=False); source quote: "**Source B \u2014 W3C SKOS Reference (Miles & Bechhofer, W3C Recommendation, 18 Aug 2009), fetched in full.** On your Part-3 labels: \"The properties `skos:broadMatch` and `skos:narrowMatch` are used to state a hierarchical mapping link between two concepts.\""

### w-242
{
 "first_author": "Br\u00e9al",
 "authors": "Michel Br\u00e9al",
 "year": 1897,
 "title": "Essai de S\u00e9mantique",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-304: attributed_claim = "Deep conceptual root for an ordinary word acquiring a new meaning (historical semantics/semantic change)." (hedged=True); source quote: "Deep conceptual root for \"an ordinary word acquires a new meaning\": Michel Br\u00e9al, *Essai de S\u00e9mantique*, **1897** (historical semantics). *(Hedge: I did not find a single canonical pre-2015 \"neologism-detection\" landmark of the Justeson-Katz stature; that subtask is real but more diffuse.)*"

### w-247
{
 "first_author": "Noraset",
 "authors": "Noraset, Liang, Birnbaum & Downey",
 "year": 2017,
 "title": "Definition Modeling",
 "venue": "AAAI 2017",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-312: attributed_claim = "Neural/generative definition modeling task." (hedged=True); source quote: "The generative version, Noraset, Liang, Birnbaum & Downey, \"Definition Modeling,\" *AAAI* **2017**, is *post*-2015"

### w-253
{
 "first_author": "Lenzerini",
 "authors": "Lenzerini",
 "year": 2002,
 "title": "Data Integration: A Theoretical Perspective",
 "venue": "PODS 2002",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-321: attributed_claim = "Classic mediated-schema/global-as-view/local-as-view data-integration paradigm, the opposite of the pay-as-you-go/emergent-semantics commitment." (hedged=False); source quote: "This is the deliberate opposite of the classic **mediated-schema** / **global-as-view / local-as-view** data-integration paradigm (Lenzerini, \"Data Integration: A Theoretical Perspective,\" *PODS* 2002)."

### w-258
{
 "first_author": "Ogden",
 "authors": "Ogden, C.K.",
 "year": 1930,
 "title": "Basic English: A General Introduction with Rules and Grammar",
 "venue": "Kegan Paul, Trench, Trubner & Co.",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-329: attributed_claim = "Oldest fixed-small-vocabulary controlled-language project (850 words)." (hedged=False); source quote: "Ogden, C. K. (1930). *Basic English: A General Introduction with Rules and Grammar*. Kegan Paul, Trench, Trubner & Co. (Oldest fixed-small-vocabulary controlled-language project \u2014 850 words.)"

### w-259
{
 "first_author": "Batini",
 "authors": "Batini, C., Lenzerini, M. & Navathe, S.B.",
 "year": 1986,
 "title": "A comparative analysis of methodologies for database schema integration",
 "venue": "ACM Computing Surveys 18(4), pp. 323-364",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-331: attributed_claim = "Oldest systematic treatment of matching independently-developed schemas describing the same underlying things." (hedged=False); source quote: "Batini, C., Lenzerini, M., & Navathe, S. B. (1986). \"A comparative analysis of methodologies for database schema integration.\" *ACM Computing Surveys* 18(4), pp. 323\u2013364. (Oldest systematic treatment I found of matching independently-developed schemas describing the same underlying things.)"

### w-271
{
 "first_author": "Hill",
 "authors": "Hill, Cho, Korhonen & Bengio",
 "year": 2016,
 "title": "Learning to Understand Phrases by Embedding the Dictionary",
 "venue": "TACL 4:17-30",
 "urls": [
  "https://aclanthology.org/Q16-1002/"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-349: attributed_claim = "Reverse dictionaries return the name of a concept given a definition/description, the mechanism for using a definition as a retrieval pivot." (hedged=False); source quote: "**Reverse dictionary / definition\u2192concept retrieval** \u2014 Hill, Cho, Korhonen & Bengio, \"Learning to Understand Phrases by Embedding the Dictionary,\" *TACL* 4:17\u201330, 2016. Abstract, attributed: \"reverse dictionaries that return the name of a concept given a definition or description\u2026 the effectiveness"

### w-273
{
 "first_author": "Giulianelli",
 "authors": "Giulianelli et al.",
 "year": 2023,
 "title": "definition-generation-for-sense-representation",
 "venue": "arXiv:2305.11993",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-351: attributed_claim = "Definition generation as a sense representation for diachronic semantic change analysis." (hedged=False); source quote: "**Novel-sense / lexical semantic change detection** \u2014 SemEval-2020 Task 1 (Schlechtweg et al., 2020) and definition-generation-for-sense-representation (e.g., Giulianelli et al., 2023, arXiv:2305.11993)."

### w-275
{
 "first_author": "Wierzbicka",
 "authors": "Wierzbicka and Goddard",
 "year": null,
 "title": "Natural Semantic Metalanguage / semantic primes",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-355: attributed_claim = "Reductive paraphrase into a fixed set of indefinable universal semantic primes, the linguistics ancestor of defining with only a small fixed set of plain words." (hedged=True); source quote: "**Natural Semantic Metalanguage / semantic primes** \u2014 Wierzbicka (from the early 1970s) and Goddard; \"reductive paraphrase\" into ~65 indefinable primes. ... *(NSM date from a secondary source; see caveats.)*"

### w-281
{
 "first_author": "Mayr",
 "authors": "Mayr et al.",
 "year": null,
 "title": "cross-concordances / KoMoHe project",
 "venue": "arXiv:0806.3765, arXiv:1009.5352",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-368: attributed_claim = "Manually built crosswalks between social-science thesauri from different disciplines (513,000+ relations across 64 crosswalks), labeled with equivalence/hierarchy/association relations to raise cross-disciplinary recall." (hedged=True); source quote: "**GESIS \"cross-concordances\" / KoMoHe project** (Mayr et al.; e.g. arXiv:0806.3765, arXiv:1009.5352) ... these crosswalks are intellectually (manually) created and stored at scale (513,000+ relations across 64 crosswalks) as a persistent shared resource"

### w-284
{
 "first_author": "Star",
 "authors": "Star & Griesemer",
 "year": 1989,
 "title": "boundary objects",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-371: attributed_claim = "Supplies the sociological justification for the tool's design constraint of not requiring any group to change its words or agree; boundary objects adapt to local needs while maintaining a common identity across sites." (hedged=False); source quote: "**Star & Griesemer, \"boundary objects\" (1989)** ... Quoting the original definition (via Wikipedia, itself quoting p.393): \"objects which are both plastic enough to adapt to local needs... yet robust enough to maintain a common identity across sites... a means of translation.\""

### w-290
{
 "first_author": "Lusicky",
 "authors": "Lusicky and Wissik",
 "year": 2015,
 "title": null,
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-377: attributed_claim = "Source classification of TOT (terminology-oriented translation) work into ad hoc vs pro-active types." (hedged=True); source quote: "Broadly speaking, there are two types of TOT work: (1) ad hoc terminology work and (2) pro-active terminology work (Lusicky and Wissik 2015)."
