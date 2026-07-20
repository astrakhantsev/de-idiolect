# What the described tool would be called, and its nearest relatives

## Security note first
One fetch (`safefetch https://www.w3.org/TR/skos-reference/`) flagged a HIGH finding — "Jailbreak keywords: no restriction." I checked the surrounding text directly: it's ordinary W3C spec language, unrelated to my task and containing no directive aimed at me. I'm treating it as a false positive and did not act on any instruction from the page.

## 1. Accepted names for the closest established framings

There is no single existing name for this exact three-step pipeline — I could not find one system that does detection → controlled-vocabulary glossing → relation-labeled matching, end to end, while explicitly refusing to keep a persistent cross-community index. But each piece, and the whole's shape, maps onto established framings that different fields would each claim a piece of:

- **The problem it solves** is what Information Retrieval/HCI calls **"the vocabulary problem"** — the empirical finding that independent people/groups rarely converge on the same word for the same thing, so single-vocabulary search misses relevant material. Furnas, Landauer, Gomez & Dumais, "The Vocabulary Problem in Human-System Communication," *Communications of the ACM* 30(11):964–971 (Nov. 1987).
- **The architecture** — do nothing globally up front, resolve mappings lazily, one instance at a time, and let anything stored be disposable/re-derivable — is exactly the **"pay-as-you-go" / dataspaces** paradigm from the database/data-integration field. As a secondary source summarizing the primary Halevy et al. work puts it (quoting the book chapter directly):

  > "A dataspace is an emerging approach to data management that recognises that in large-scale integration scenarios, involving thousands of data sources, it is difficult and expensive to obtain an upfront unifying schema across all sources (Franklin, Halevy and Maier, 2005)... Instead, data is integrated on an 'as-needed' basis with the labour-intensive aspects of data integration postponed until they are required." (Curry, *Fundamentals of Real-time Linked Dataspaces*, excerpted at [dataspaces.info](https://dataspaces.info/principles-and-practices/))

- **The matching/labeling step (step 3)** is squarely **ontology/schema matching** (Semantic Web / Knowledge Representation), and its output vocabulary — "same thing / more general / more specific / related" — is *literally* the SKOS mapping-property set. Quoting the W3C Recommendation body directly:

  > "The SKOS mapping properties are `skos:closeMatch`, `skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch` and `skos:relatedMatch`. These properties are used to state mapping (alignment) links between SKOS concepts in different concept schemes... The properties `skos:broadMatch` and `skos:narrowMatch` are used to state a hierarchical mapping link... The property `skos:relatedMatch` is used to state an associative mapping link." ([W3C SKOS Reference](https://www.w3.org/TR/skos-reference/), §10.1)

  `exactMatch` ≈ *same thing*, `broadMatch`/`narrowMatch` ≈ *more general*/*more specific*, `relatedMatch` ≈ *related* — the correspondence is exact.

**Fields that would each claim a piece:** Information Retrieval / HCI (the problem statement), Databases (the lazy/no-global-schema architecture), Semantic Web & Knowledge Representation (the matching + relation labels), Computational Linguistics/Lexical Semantics (gloss-based sense resolution and controlled-vocabulary definition), and Library & Information Science (the practitioner-facing version of cross-vocabulary search improvement, called "terminology mapping" or "crosswalking").

## 2. Closest existing things, with relation labels

| Item | Relation | Why |
|---|---|---|
| **Furnas, Landauer, Gomez & Dumais, "The Vocabulary Problem in Human-System Communication," CACM 1987** | related | Names and quantifies exactly the failure mode the tool exists to fix (two people choose the same term with probability <0.20), but its proposed fix is statistical "unlimited aliasing" (index everything under many synonyms), not per-instance detection + gloss generation + relation labeling. |
| **Franklin, Halevy & Maier, "From Databases to Dataspaces" (SIGMOD Record 2005); Halevy, Franklin & Maier, "Principles of Dataspace Systems" (PODS 2006)** | more general | "Pay-as-you-go," on-demand, no-upfront-global-schema integration is the broader abstraction; the described tool reads like a specific instantiation of it for jargon in scientific writing rather than a novel architecture. |
| **Euzenat & Shvaiko, *Ontology Matching* (Springer, 2007; 2nd ed. 2013)** | more general | Ontology matching as a field is exactly "finding correspondences between semantically related entities of different [conceptualizations]... equivalence as well as other relations, such as consequence, subsumption, or disjointness" ([book.ontologymatching.org](http://book.ontologymatching.org/)) — the field the tool's step 3 belongs to, but the field doesn't specify jargon-detection or primitive-vocabulary gloss generation as its input mechanism (that's what this proposal adds). Notably the book's own taxonomy already has a category called "instance-based" matching — close in spirit to "run one item at a time." |
| **SKOS mapping vocabulary (W3C, 2009)** | related | Supplies the *exact* four-way relation vocabulary used in step 3, but is only a representation standard for links between already-existing concept schemes on both sides — it does nothing like steps 1–2. |
| **Lesk, "Automatic Sense Disambiguation Using Machine Readable Dictionaries..." (1986)** | related | Established the core trick of matching via *definitions* rather than *words* (gloss overlap) — the same move step 3 makes — but disambiguates one word in one text against a pre-existing dictionary, not group-local jargon against freshly generated glosses across corpora. |
| **UMLS Metathesaurus (concept normalization via Concept Unique Identifiers)** | related | Solves the identical practical problem (synonymous biomedical terms across 200+ vocabularies) with the identical goal (better retrieval), but does it by building and maintaining exactly the kind of persistent shared master list (CUIs) the described tool is explicitly designed to avoid. |
| **GESIS "cross-concordances" / KoMoHe project** (Mayr et al.; e.g. arXiv:0806.3765, arXiv:1009.5352) | related | The closest domain-level analogue: manually built crosswalks between social-science thesauri from different disciplines, labeled with equivalence/hierarchy/association relations, explicitly to raise recall in cross-disciplinary literature search. But per the search synthesis, these crosswalks are intellectually (manually) created and stored at scale (513,000+ relations across 64 crosswalks) as a persistent shared resource — the architectural opposite of "never builds... a shared master list." |
| **Swanson's literature-based discovery / ABC model (1986)**, e.g. the fish-oil/Raynaud's link | related | Same overarching goal (surface latent connections between literatures developed in isolation), but the mechanism is co-occurrence through a shared intermediate term B, not gloss generation or explicit relation labeling. |
| **Hope, Chan, Kittur & Shahaf, "SOLVENT" (CSCW 2018), and related analogy-mining work** | related | Same instinct — represent by function (Background/Purpose/Mechanism/Finding) rather than surface words to bridge domains — but applied to whole papers/ideas for analogical retrieval, with humans annotating the facets, not automatic per-term jargon detection with formal type/IO/assertion definitions. |
| **Star & Griesemer, "boundary objects" (1989)** | related | Supplies the sociological justification for the tool's design constraint ("without asking any group to change its words or agree"). Quoting the original definition (via Wikipedia, itself quoting p.393): "objects which are both plastic enough to adapt to local needs... yet robust enough to maintain a common identity across sites... a means of translation." It's a descriptive concept from Science & Technology Studies, not an engineered system. |
| **Natural Semantic Metalanguage / semantic primes / "Minimal English" (Wierzbicka, Goddard)** | related | The closest existing precedent for "write the explanation using only plain, common words from a fixed small list": NSM explications use ~65 universal semantic primes. Per Wikipedia: "Primes are universal in that they have the same translation in every language, and they are primitive in that they cannot be defined using other words." But NSM targets universal cross-*language* meaning in linguistics/anthropology, not cross-*community* jargon bridging for literature search, and has no notion of type/input/output/applicability-condition structure or mathematical notation. |
| **Guo et al., "Personalized Jargon Identification for Enhanced Interdisciplinary Communication," NAACL 2024 (arXiv:2311.09481)** | related | The most directly relevant recent NLP work for step 1 specifically. Quoting the abstract directly: "Current methods of jargon identification mainly use corpus-level familiarity indicators... However, researchers' familiarity of a term can vary greatly based on their own background." This personalizes jargon detection to an individual reader's background, not to a *group's* local sense of a word — a narrower, differently-scoped problem than step 1 as described. |

No single item earns "same thing" — the description reads as a deliberate synthesis of pieces from several fields rather than a paraphrase of one existing named system.

## 3. What a practitioner community would call it

Using only established field vocabulary (no coinages):

1. **"Pay-as-you-go ontology alignment"** (or "...terminology mapping") — grafts the databases field's established "pay-as-you-go"/dataspaces term onto the Semantic Web field's "ontology alignment."
2. **"On-demand instance-based ontology matching"** — "instance-based" is literally one of Euzenat & Shvaiko's own technique categories (§4.3.1/§8.2 of *Ontology Matching*); "on-demand" signals the lazy, no-upfront-schema property.
3. **"Just-in-time crosswalking"** (or "dynamic cross-concordance generation") — "crosswalk"/"cross-concordance" is the library-science term of art for a mapping between two controlled vocabularies (as used by GESIS's KoMoHe project); "just-in-time" marks that, unlike GESIS's crosswalks, nothing is precomputed or retained.

## 4. Confidence and what I could not verify

**High confidence, directly verified from primary/near-primary body text:** SKOS mapping properties (W3C spec body); the dataspaces/pay-as-you-go definition (quoted excerpt of Curry 2020, itself citing Franklin/Halevy/Maier 2005 and Halevy/Franklin/Maier 2006); Euzenat & Shvaiko's *Ontology Matching* scope and taxonomy (official book site); the Star & Griesemer 1989 boundary-object definition (quoted verbatim via Wikipedia, citing p.393); NSM/semantic primes mechanics (Wikipedia body).

**Medium confidence, verified only via secondary search summaries, not primary full text (fetches were blocked or dead):**
- Furnas et al. 1987 — I obtained the verbatim **abstract** (via dret.net) but could not reach the CACM body (Cloudflare-blocked), Academia.edu copy (Cloudflare-blocked), Semantic Scholar page (bot-check), or the original author PDF (dead link at umich.edu). The core facts (probability <0.20, 80–90% failure rate, "unlimited aliasing") are quoted directly from the abstract, so I'm confident in them, but I have not read the paper's argument in full.
- Lesk 1986, Swanson 1986, UMLS Metathesaurus mechanics, and the SOLVENT/analogy-mining paper — known to me and cross-checked against multiple independent search summaries, but I was not able to fetch primary full text for any of them in this session (PDF fetches to huji.ac.il and arXiv 0806.3765/2505.16227 both returned empty renders).
- GESIS cross-concordances scale figures (513,000 relations, 64 crosswalks) — from a search-engine synthesis of secondary sources, not a fetched primary document; I'd treat the specific numbers as a hedged pointer rather than a confirmed citation.

**What I could not verify at all:** whether a single named system implementing this *exact* three-step pipeline exists somewhere I didn't find it — possibly a recent (2025–2026) preprint given how active this space currently is (jargon detection alone has multiple 2024–2025 papers). I found nothing that claims all three steps together plus the no-persistent-index constraint, but I can't rule out its existence with confidence given search-engine coverage gaps.

## Oldest sources found
Two items tie at **1986**: Lesk's gloss-overlap word-sense-disambiguation paper and Swanson's literature-based-discovery/ABC-model work (including the fish-oil–Raynaud's paper). Furnas et al.'s "vocabulary problem" paper follows in **November 1987**.

## What I did NOT search
- Non-English-language literature (German library-science sources on cross-concordances beyond GESIS's English outputs, French/Polish NSM sources, etc.)
- Native interfaces of ACM Digital Library, IEEE Xplore, or ACL Anthology (relied on general web search plus opportunistic fetches; several direct ACM/SAGE/Academia.edu fetches were blocked by Cloudflare bot-detection)
- Patent databases, beyond incidental hits
- A systematic sweep of 2025–2026 preprints specifically for an exact match to this three-step pipeline — I ran targeted queries but did not do an exhaustive recent-arXiv sweep
- OSF, SSRN, or other preprint servers outside arXiv

## Query ledger (verbatim, in order)
1. `Furnas Landauer Gomez Dumais "vocabulary problem" human-system communication 1987`
2. `dataspaces "pay-as-you-go" data integration Franklin Halevy Maier`
3. `SKOS mapping properties exactMatch broadMatch narrowMatch relatedMatch`
4. `ontology matching Euzenat Shvaiko equivalence subsumption overlap relations survey`
5. `safefetch https://www.w3.org/TR/skos-reference/`
6. `safefetch https://dataspaces.info/principles-and-practices/`
7. `safefetch https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication/`
8. `Lesk algorithm 1986 gloss overlap word sense disambiguation dictionary definitions`
9. `Swanson "undiscovered public knowledge" literature-based discovery ABC model 1986`
10. `UMLS Metathesaurus concept normalization synonymy biomedical CUI`
11. `Hope Chan Kittur Shahaf analogical search research papers purpose mechanism SOLVENT`
12. `"boundary object" Star Griesemer 1989 different social worlds shared understanding`
13. `safefetch https://www.academia.edu/33266533/The_Vocabulary_Problem_in_Human_System_Communication`
14. `safefetch http://book.ontologymatching.org/`
15. `safefetch https://journals.sagepub.com/doi/10.1177/030631289019003001`
16. `safefetch https://en.wikipedia.org/wiki/Boundary_object`
17. `safefetch https://www.semanticscholar.org/paper/The-Vocabulary-Problem-in-Human-System-an-Analysis-Furnas-Landauer/27fa6ede8c9ffc305d06c9307e47321b41540e11`
18. `safefetch https://www.cs.huji.ac.il/w~dshahaf/analogy-cscw18.pdf`
19. `safefetch https://dl.acm.org/doi/10.1145/32206.32212`
20. `safefetch http://dret.net/biblio/reference/fur87`
21. `safefetch http://www.si.umich.edu/~furnas/Papers/vocab.paper.pdf`
22. `"on-the-fly ontology" OR "just-in-time ontology" construction matching per-term local sense`
23. `domain-specific word sense induction jargon detection scientific text NLP`
24. `controlled natural language restricted defining vocabulary semantic primes Wierzbicka NSM definitions`
25. `cross-domain literature search query expansion terminology mismatch recall interdisciplinary`
26. `safefetch https://arxiv.org/pdf/0806.3765`
27. `safefetch https://en.wikipedia.org/wiki/Semantic_primes`
28. `GESIS "cross-concordance" heterogeneity thesauri controlled vocabularies information retrieval definition`
29. `jargon term detection generate plain-language definition cross-community literature search recall LLM agent 2025`
30. `"same thing" "more general" "more specific" "related" concept matching relation labels tool`
31. `controlled vocabulary primitive definitions jargon detection related work discovery without shared ontology paper`
32. `Guo 2024 interdisciplinary jargon detection benchmark scholar annotations GPT-4 personalized`
33. `safefetch https://arxiv.org/pdf/2505.16227`
34. `safefetch https://arxiv.org/abs/2311.09481`
