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

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-2.jsonl

## Works to verify

### w-085
{
 "first_author": "Hoekstra",
 "authors": "Rinke Hoekstra",
 "year": 2010,
 "title": "The Knowledge Reengineering Bottleneck",
 "venue": "Semantic Web 1, IOS Press",
 "urls": [
  "https://www.semantic-web-journal.net/sites/default/files/swj32.pdf"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-126: attributed_claim = "Prescribes ex post knowledge-engineering methodologies: reuse is a continuous relation of trust, not a copy-paste operation." (hedged=False); source quote: "Hoekstra's prescription: knowledge engineering needs *ex post* methodologies \u2014 provenance, trust between provider and consumers, tolerance of \"dirty data\" \u2014 because \"reuse is not a copy-and-paste operation, but rather a continuous relation of trust.\""

### w-090
{
 "first_author": "Doctorow",
 "authors": "Cory Doctorow",
 "year": 2001,
 "title": "Metacrap: Putting the torch to seven straw-men of the meta-utopia",
 "venue": null,
 "urls": [
  "https://hermiene.net/essays-trans/metacrap.html"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-120: attributed_claim = "Names the contributor-incentive problem: accurate voluntary metadata annotation is under-supplied or adversarially gamed." (hedged=False); source quote: "4. **Contributor-incentive problem** \u2014 Doctorow (Explanation C): \"People lie / People are lazy.\" Metadata sits \"in a competitive world,\" so accurate voluntary annotation is under-supplied (lazy) or adversarially gamed (lie). Owner: Doctorow 2001."
- occ_id def-134: attributed_claim = "Seven structural obstacles to reliable shared metadata." (hedged=False); source quote: "Owner: Cory Doctorow, \"Metacrap: Putting the torch to seven straw-men of the meta-utopia,\" 26 Aug 2001"

### w-093
{
 "first_author": "Liu",
 "authors": "Yuxi Liu",
 "year": 2025,
 "title": "Cyc",
 "venue": "self-published essay",
 "urls": [
  "https://yuxi-liu-wired.github.io/essays/posts/cyc/"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-121: attributed_claim = "Organizational lock-in/product-differentiation bottleneck: maintainers cannot abandon the manual approach their product differentiation depends on." (hedged=False); source quote: "5. **Organizational lock-in / product-differentiation** (an incentive bottleneck specific to the *maintainers*) \u2014 from the Cyc post-mortem, an Upton-Sinclair-style observation: \"It can be very hard to get someone to understand something, when their product differentiation depends on them not underst"

### w-097
{
 "first_author": null,
 "authors": null,
 "year": 2025,
 "title": "Semantic Web and Software Agents \u2014 A Forgotten Wave of Artificial Intelligence?",
 "venue": "arXiv:2503.20793",
 "urls": [
  "https://arxiv.org/html/2503.20793v1"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-122: attributed_claim = "Bibliometric documentation that the Semantic Web failed to become a mainstream AI paradigm and is now a 'forgotten wave', erased even from AI-history retrospectives." (hedged=True); source quote: "The most concrete documented sociological claim I read in full is the 2025 bibliometric paper \"Semantic Web and Software Agents \u2014 A Forgotten Wave of Artificial Intelligence?\" (arXiv:2503.20793): \"Despite initial momentum, the Semantic Web failed to become a mainstream AI paradigm.\" \u2014 arXiv:2503.207"

### w-100
{
 "first_author": "Marcus",
 "authors": "Marcus & Davis",
 "year": 2015,
 "title": "Commonsense Reasoning and Commonsense Knowledge in Artificial Intelligence",
 "venue": "CACM",
 "urls": [
  "https://cacm.acm.org/magazines/2015/9/191169-commonsense-reasoning-and-commonsense-knowledge-in-artificial-intelligence/fulltext"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-125: attributed_claim = "Argues the path forward for common-sense knowledge is a combination of logic, hand-built KBs, web mining, and crowdsourcing." (hedged=True); source quote: "Marcus & Davis's 2015 CACM survey reportedly argues the path forward is a *combination* \u2014 logic + hand-built KBs + web mining + crowdsourcing \u2014 with commonsense still the unsolved core. *(This last is from the article's abstract/search summary only \u2014 ACM's full text was Cloudflare-blocked, so I did "

### w-108
{
 "first_author": "Star",
 "authors": "Susan Leigh Star & James R. Griesemer",
 "year": 1989,
 "title": "Institutional Ecology, 'Translations' and Boundary Objects",
 "venue": "Social Studies of Science 19(3):387-420",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-151: attributed_claim = "Prescribes boundary objects and local standardization of methods instead of convergence on one global representation." (hedged=False); source quote: "**Star & Griesemer 1989** (fetched, verbatim, implicit answer): stop treating convergence-on-one-representation as the goal; the empirically observed successful mechanism is boundary objects \u2014 artifacts \"adaptable to different viewpoints and robust enough to maintain identity across them\" \u2014 plus loc"

### w-111
{
 "first_author": "Feigenbaum",
 "authors": "Edward A. Feigenbaum",
 "year": 1984,
 "title": "Knowledge Engineering: The Applied Side of Artificial Intelligence",
 "venue": "Annals of the New York Academy of Sciences 426:91-107",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-139: attributed_claim = "The problem of knowledge acquisition is the critical bottleneck problem in artificial intelligence." (hedged=True); source quote: "the version I could pin down and quote is Feigenbaum, \"Knowledge Engineering: The Applied Side of Artificial Intelligence,\" *Annals of the New York Academy of Sciences* 426:91-107, 1984 ... \"The problem of knowledge acquisition is the critical bottleneck problem in artificial intelligence.\" \u2014 Feigen"

### w-114
{
 "first_author": "Ostrom",
 "authors": "Elinor Ostrom",
 "year": 1990,
 "title": "Governing the Commons",
 "venue": null,
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-143: attributed_claim = "Collective-action framework for commons, later extended to information/knowledge commons." (hedged=True); source quote: "extends Ostrom's *Governing the Commons* (1990) collective-action framework to information resources"

### w-115
{
 "first_author": "Automatic Language Processing Advisory Committee",
 "authors": "Automatic Language Processing Advisory Committee (chaired by John R. Pierce)",
 "year": 1966,
 "title": "Language and Machines \u2014 Computers in Translation and Linguistics",
 "venue": "National Academy of Sciences/National Research Council",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-144: attributed_claim = "Skeptical report on machine translation research that caused US government to dramatically cut funding, marking the beginning of the first AI winter." (hedged=True); source quote: "Owner: Automatic Language Processing Advisory Committee (chaired by John R. Pierce), *Language and Machines \u2014 Computers in Translation and Linguistics*, National Academy of Sciences/National Research Council, 1966 ... the primary 1966 report itself I did not fetch, only located its archive link"

### w-118
{
 "first_author": "Lenat",
 "authors": "Doug Lenat & Gary Marcus",
 "year": 2023,
 "title": "Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc",
 "venue": "arXiv",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-147: attributed_claim = "Cyc is neither a success nor failure; a ground-breaking experiment that never fully gelled, now largely unknown to young AI researchers." (hedged=False); source quote: "Owner: Doug Lenat & Gary Marcus, \"Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc,\" arXiv, 2023; and Gary Marcus's obituary essay for Lenat (Substack, Sept 2023, fetched directly) ... \"Cyc has been neither a success nor a failure, but somewhere in between: I see it as a "

### w-119
{
 "first_author": "Marcus",
 "authors": "Gary Marcus",
 "year": 2023,
 "title": "obituary essay for Lenat",
 "venue": "Substack",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-148: attributed_claim = "Cyc is neither a success nor failure; reflects genuine field-level neglect of the project." (hedged=False); source quote: "Gary Marcus's obituary essay for Lenat (Substack, Sept 2023, fetched directly)"

### w-127
{
 "first_author": "Sch\u00fctze",
 "authors": "Sch\u00fctze",
 "year": 1998,
 "title": "Automatic Word Sense Discrimination",
 "venue": "Computational Linguistics 24(1)",
 "urls": [
  "https://aclanthology.org/J98-1004/"
 ]
}
Occurrences (verify each attributed claim):
- occ_id def-327: attributed_claim = "Oldest computational treatment of an ordinary word carrying a distinct local sense, via context clustering." (hedged=False); source quote: "Sch\u00fctze, H. (1998). \"Automatic Word Sense Discrimination.\" *Computational Linguistics* 24(1), pp. 97\u2013123. (Oldest computational treatment of \"ordinary word, distinct local sense,\" via context clustering in \"Word Space.\")"
