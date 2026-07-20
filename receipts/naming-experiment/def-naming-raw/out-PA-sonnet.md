## Bottom line up front

This describes, part by part: **(1) automatic jargon/neologism detection** (computational lexicography — term extraction, word-sense induction, lexical semantic change detection), **(2) primitive-vocabulary gloss generation**, which is essentially **Natural Semantic Metalanguage (NSM) explication** or controlled-vocabulary definition, and **(3) ontology/schema matching with typed relations** (same/broader/narrower/related — the exact vocabulary of SKOS mapping properties and, decades earlier, thesaurus standards' BT/NT/RT/USE). Each part is well-established on its own, going back to 1974–1998 at the latest. I could **not** find evidence that anyone has built or explicitly proposed the full three-part pipeline as one system — especially the specific combination of "detect jargon → auto-generate a primitive-only gloss → use gloss-similarity (not a shared master ontology) for fully decentralized, pairwise ontology alignment." The closest analogues combine two of the three parts (e.g., LLM-based ontology matchers combine 2+3; peer-to-peer "emergent semantics" systems combine part of 1+3 but skip primitive-vocabulary constraints). Below is the detail, with sources quoted where I could fetch them in full, and hedges where I couldn't.

One process note: two safefetch calls came back with security-scan warnings. Fetching the W3C SKOS Reference triggered a **HIGH** "role_manipulation" flag on the phrase "no restriction" — I'm confident this is a false positive (it's ordinary OWL/RDF property-restriction terminology in a standards document, not an injection attempt). Fetching the PLOS ONE "De-jargonizer" paper triggered **9 CRITICAL** "data_exfil" flags on markdown image links — these all point at `journals.plos.org`'s own figure server (standard inline figure/thumbnail images in an open-access article), so I judge these false positives too, not real exfiltration attempts. Flagging both per policy; I did not treat either page's content as compromised.

---

## 1. What is this system, or each part, called?

**No single accepted name for the whole three-part pipeline.** It isn't a named system in any literature I found (see Q4). Each part, though, maps onto an established name:

- **Part 1 (notice a word being used in a group-specific way)** splits into two established sub-tasks that the field treats separately, because "brand-new word" and "old word, new sense" are handled by different tools:
  - New/rare vocabulary specific to a text or group: **terminology extraction / automatic term recognition (ATR)**, and, more generally, **keyness analysis** (comparing a target corpus against a reference corpus to find over-represented words).
  - Ordinary word, locally-special sense: **word sense induction/discrimination** and, when tracked as a shift, **lexical semantic change detection (LSCD)**.
  - There's no single accepted term that names "detect both coinages and repurposed ordinary words as group-specific" as one task — it's a gap I'll return to in Q4.
- **Part 2 (self-contained explanation in a small, fixed vocabulary of plain words plus math notation)**: closest accepted names are **Natural Semantic Metalanguage (NSM) explication** (Wierzbicka/Goddard) and, in lexicographic practice, a **defining vocabulary** (as used by learner's dictionaries). In NLP specifically this is **definition generation / definition modeling**. In knowledge representation, the general idea of writing definitions in a restricted, controlled subset of natural language is a **controlled natural language (CNL)**.
- **Part 3 (store explanations, use them instead of words to find cross-group matches, label pairs as same/broader/narrower/related)**: this is **ontology matching / ontology alignment** in Semantic Web terms, or **schema matching / schema integration** in the older database lineage, or **terminology mapping** in biomedical informatics (UMLS Metathesaurus). The specific four-way label set (same · more general · more specific · related) is, essentially verbatim, the **SKOS mapping vocabulary**: `skos:exactMatch`, `broadMatch`, `narrowMatch`, `relatedMatch` — itself inherited from much older **thesaurus standards'** USE/BT/NT/RT relations.
- **The "no shared master list, on-demand pairwise" design commitment** has its own name in the decentralized-systems literature: **emergent semantics** (Aberer et al.) or, in database terms, **pay-as-you-go data integration** / **dataspaces** (a term I did not verify a primary source for this session — flagging as unverified).

## 2. Which fields own each part, and which field would claim the whole?

- **Part 1**: computational linguistics / corpus linguistics / computational lexicography (term extraction, word-sense induction, semantic-change detection all live in ACL-adjacent NLP venues); **terminology science** (a linguistics-adjacent applied field, see Q3) also explicitly claims detection of specialized "terms" vs. general-language words.
- **Part 2**: linguistic semantics/lexicography (NSM, defining vocabularies) and knowledge representation/logic (controlled natural language, conceptual graphs, description logics) jointly own it — NSM is a linguistics research program, but "write a gloss in a restricted symbol set" is equally a KR concern.
- **Part 3**: database/information systems (schema matching — the oldest lineage), Semantic Web/knowledge engineering (ontology matching), library and information science (thesaurus construction — actually the oldest lineage of all, see Q3), and biomedical informatics (UMLS) all own pieces of it.
- **Whole pipeline**: my best-supported guess is **terminology science** (in the Wüster/ISO sense) is the field whose self-description most closely matches all three parts together — it explicitly studies (a) how special-language communities create/repurpose terms, (b) concept analysis via genus-differentia definition, and (c) concept equivalence across languages/domains (ISO 704's "concept systems"). A defensible second answer is **knowledge engineering / ontology engineering**, which owns 2 and 3 natively and increasingly absorbs 1 via automated ontology learning. I hold this with only moderate confidence — I did not find a field that names this exact three-stage pipeline as its own turf.

## 3. Oldest treatments per part (author, year, venue)

**Part 1** (oldest computational treatments; the phenomenon itself is older — see Kuhn below):
- Bourigault, D. (1992). "Surface grammatical analysis for the extraction of terminological noun phrases." *COLING '92*, pp. 977–981. (Oldest term-extraction algorithm I found.)
- Justeson, J. S. & Katz, S. M. (1995). "Technical terminology: some linguistic properties and an algorithm for identification in text." *Natural Language Engineering* 1(1).
- Scott, M. (1997). "PC analysis of key words — and key key words." *System* 25(2), pp. 233–245. (Formalizes "unusual relative to a reference corpus" — the operational core of detecting group-specific vocabulary.)
- Schütze, H. (1998). "Automatic Word Sense Discrimination." *Computational Linguistics* 24(1), pp. 97–123. (Oldest computational treatment of "ordinary word, distinct local sense," via context clustering in "Word Space.")
- Non-computational conceptual ancestor: Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press — the incommensurability thesis that different communities' lexicons "divide up the world" differently is exactly the phenomenon Part 1 tries to detect automatically, though Kuhn proposes no detection mechanism.

**Part 2**:
- Ogden, C. K. (1930). *Basic English: A General Introduction with Rules and Grammar*. Kegan Paul, Trench, Trubner & Co. (Oldest fixed-small-vocabulary controlled-language project — 850 words.)
- Wierzbicka, A. (1972). *Semantic Primitives*. Athenäum, Frankfurt. (Origin of NSM; proposed 14 semantic primes, later expanded to ~65 by Wierzbicka & Goddard.) Per the NSM Wikipedia page I fetched in full: *"Wierzbicka's 1972 study proposed 14 semantic primes... Primes are universal in that they have the same translation in every language, and they are primitive in that they cannot be defined using other words."* This is close to the task's "plain, common words drawn from a fixed small list" requirement, though NSM allows no math notation, so it's a partial match, not identical.

**Part 3**:
- Batini, C., Lenzerini, M., & Navathe, S. B. (1986). "A comparative analysis of methodologies for database schema integration." *ACM Computing Surveys* 18(4), pp. 323–364. (Oldest systematic treatment I found of matching independently-developed schemas describing the same underlying things — the database-world predecessor of ontology matching, predating it by ~20 years.)
- ANSI/NISO Z39.19-1974 and, in parallel, ISO 2788:1974 ("Guidelines for the establishment and development of monolingual thesauri") — these standardized the exact four-way relation vocabulary (BT/NT/RT plus USE for equivalence) that Part 3's "same · more general · more specific · related" labels reproduce almost exactly, arguably the oldest source for that specific taxonomy. One search result noted the BT/NT/RT tags themselves predate even these standards, tracing to 1960s practice such as the *Thesaurus of Engineering and Scientific Terms* — I could not verify a specific author/year for that claim, so treat it as a hedge, not a citation.
- Later but foundational to *ontology* matching specifically: Rahm, E. & Bernstein, P. A. (2001). "A survey of approaches to automatic schema matching." *VLDB Journal* 10, pp. 334–350; and Euzenat, J. & Shvaiko, P. (2007). *Ontology Matching* (1st ed.), Springer — both post-2015-cutoff-irrelevant since they're well before 2015 anyway, included for completeness of the lineage.

## 4. Has the whole three-part system been built or proposed as one thing?

**I did not find it.** Nothing I could locate combines (a) automatic detection of group-specific term *and* sense use, (b) generation of a primitive/controlled-vocabulary gloss for it, and (c) using gloss-similarity — with no persistent shared master vocabulary — to do pairwise cross-group relation labeling. The closest partial matches, each missing a piece:

- **LLMs4OM** (Giglou et al., 2024, *ESWC 2024 Satellite Events*, arXiv:2404.10317) and follow-ups like **MILA** and **KROMA** do (2)+(3) — they use LLM-generated natural-language concept descriptions and LLM judgment to align ontology pairs — but they operate on *existing*, human-authored ontology entities; they don't do Part 1 (they don't discover that a term is being used in a locally special way in unstructured text first), and their glosses aren't constrained to a fixed small plain-word vocabulary.
- **Aberer, Cudré-Mauroux, & Hauswirth (2003), "The Chatty Web: Emergent Semantics Through Gossiping"** (WWW 2003) implements the "no shared master list, pairwise, on-demand" design commitment for Part 3 — quoting the paper directly: *"In our approach, no explicit representation of a globally shared agreement will be required, but agreements are implicit and result from the way our (social) mechanism works... Establishing local agreements is a less challenging task than establishing global agreements by means of globally agreed schemas or shared ontologies."* This is a strong precedent for the decentralization commitment, but it matches schemas via human-provided pairwise translations, not auto-generated primitive-vocabulary glosses, and has no Part 1 or Part 2 analogue.
- **Rakedzon et al. (2017), "Automatic jargon identifier..."** (*PLOS ONE*) is a real, deployed Part-1 system (the "De-jargonizer"), but by its own account it only catches rare/low-frequency words, not ordinary words carrying a special local sense — quoting the paper directly: *"Limitations of the program include cases in which the same word holds a different meaning for scientists and layperson. For example, the jargon identifier marked fatigue as mid frequency... but a closer look at the text showed that it referred to the technical meaning of the word in material and mechanical engineering. Further research could include a list of terms that differ from lay to professional audiences..."* — i.e., the authors themselves flag the "ordinary word, special local meaning" half of Part 1 as unsolved future work, in 2017.

**If some part has never been done, which one, and what would I check first?** My working conclusion is that **Part 1, taken exactly as specified (both new coinages AND ordinary-words-with-special-local-meaning, detected together, automatically, per-group), is the weakest link** — existing tools solve the "new/rare word" half well but explicitly haven't solved the "same word, different community sense" half at production quality (see the De-jargonizer's own limitations section above). I'd check this first by searching ACL Anthology / arXiv directly (not just web search) for the intersection of "word sense induction" + "domain-specific" + "polysemy across communities," since that's a narrower, more targeted query than what I ran, and by checking whether any 2023–2026 LLM-based jargon detectors (which I did not specifically search for) have closed this gap using in-context sense discrimination.

## 5. Confidence and what I could not verify

- **High confidence**: the field names and canonical citations for Parts 1–3 individually (Bourigault 1992, Scott 1997, Schütze 1998, Ogden 1930, Wierzbicka 1972, Batini/Lenzerini/Navathe 1986, ANSI/ISO 1974, SKOS relations) — these are well-documented, cross-confirmed across multiple independent search results, and I fetched primary or near-primary sources for several.
- **Medium confidence**: the claim that no one has built the full three-part pipeline — this is an absence claim, always harder to establish than a presence claim; I searched targeted terms but a differently-worded system (e.g., under a "digital humanities," "science of science," or very recent 2025–2026 LLM-agent framing) could exist under vocabulary I didn't try.
- **Low confidence / unverified**: (a) I could not fetch Star & Griesemer (1989) directly — sagepub.com and worldpece.org both returned Cloudflare bot-challenges, and lchc.ucsd.edu's PDF returned empty content; I'm relying on secondary search-result descriptions for the "boundary object" concept, not a direct quote, so treat that citation as a hedged pointer, not a verified quote. (b) I could not fetch Gulordava & Baroni (2011) directly — marcobaroni.org and aclanthology.org both returned empty/JS-rendered-blank pages, and researchgate.net blocked access; again, relying on secondary descriptions only. (c) The claim that BT/NT/RT tags predate the 1974 standards (tracing to 1960s practice, e.g. the *Thesaurus of Engineering and Scientific Terms*) is unverified — I have no author/year for that specific work. (d) "Dataspaces"/"pay-as-you-go integration" as a name for the no-shared-master-list commitment is my own recollection, not something I verified with a search this session — flag it as such rather than treating it as confirmed.

---

### Oldest sources found (per part)
- Part 1: Bourigault 1992 (COLING); conceptual ancestor Kuhn 1962.
- Part 2: Ogden 1930 (*Basic English*), Wierzbicka 1972 (*Semantic Primitives*).
- Part 3: Batini, Lenzerini & Navathe 1986 (*ACM Computing Surveys*); ANSI Z39.19-1974 / ISO 2788:1974 for the same/broader/narrower/related relation vocabulary specifically.

### What I did NOT search
- ACL Anthology / arXiv direct search (I used general WebSearch, not a venue-scoped search) for very recent (2024–2026) LLM-based systems that might close the Part 1 gap or combine all three parts.
- Non-English-language literature (e.g., German terminology-science sources on Wüster, French INRIA ontology-matching literature) beyond what English-language search surfaced.
- Patent databases, which sometimes contain built-but-unpublished versions of exactly this kind of pipeline.
- Dataspaces / "pay-as-you-go" data integration primary sources (Franklin, Halevy, Maier) — mentioned from memory but not verified this session.
- Any dedicated search for "digital humanities" or "science of science" framings of cross-disciplinary jargon-bridging, which might be where a combined system is most likely to surface.

### Query ledger (verbatim, in order)
1. lexical semantic change detection survey word usage across communities
2. Gulordava Baroni 2011 distributional similarity semantic change Google Books Ngram
3. Natural Semantic Metalanguage Wierzbicka semantic primes list
4. ontology matching Euzenat Shvaiko book equivalence subsumption relation
5. SKOS broadMatch narrowMatch relatedMatch exactMatch W3C
6. Rahm Bernstein 2001 survey approaches automatic schema matching VLDB Journal
7. Star Griesemer 1989 boundary objects translations Berkeley Museum
8. Aberer Chatty Web emergent semantics gossiping peer to peer schema matching decentralized
9. UMLS Metathesaurus Lindberg 1993 Unified Medical Language System concept synonym mapping
10. Kuhn incommensurability different communities different vocabularies same phenomena terminology
11. automatic jargon detection scientific communities NLP paper cross-disciplinary
12. definition generation from word embeddings Noraset 2017 dictionary
13. Wüster terminology science founding father Vienna school General Theory of Terminology 1931
14. controlled natural language defining vocabulary Ogden Basic English 850 words
15. cross-domain analogy mining functional representation Hope Chan Kittur Shahaf 2017
16. Scott 1997 keyness key words WordSmith Tools comparing corpus to reference corpus
17. Bourigault 1992 terminology extraction surface grammatical analysis noun phrases COLING
18. Schütze 1998 automatic word sense discrimination Computational Linguistics
19. large language models automatic ontology alignment without shared vocabulary decentralized concept matching 2024
20. Universal Networking Language UNL interlingua universal words no proper nouns semantic relations
21. "boundary object" automatic detection NLP terminology across scientific fields identify align concepts
22. automatic terminology alignment across research communities without shared ontology jargon paraphrase primitive vocabulary
23. Sharon Baram-Tsabari 2014 "measuring mumbo jumbo" jargon science communication Public Understanding of Science
24. Batini Lenzerini Navathe 1986 "A comparative analysis of methodologies for database schema integration" ACM Computing Surveys
25. Ontology Alignment Evaluation Initiative OAEI founded 2004 first edition
26. Euzenat Shvaiko Ontology Matching first edition 2007 Springer

(In addition to these WebSearch queries, I fetched full page content via `safefetch` for: W3C SKOS Reference [success, quoted], Wikipedia's Natural Semantic Metalanguage page [success, quoted], the Aberer et al. Chatty Web paper [success, quoted], the Euzenat & Shvaiko book companion site [success], and the PLOS ONE De-jargonizer paper [success, quoted]; fetches of the Gulordava & Baroni PDF, Star & Griesemer paper via three different hosts, ResearchGate, and one ACL Anthology PDF all failed or were blocked, as noted above.)
