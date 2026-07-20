Two of the fetches triggered safefetch findings worth flagging before I present anything: the UPenn DSpace repository page had a HIGH "hidden_content" hit (an HTML comment fragment `<!----></ds-admin-sidebar>...`), and the W3C SKOS spec had a HIGH "role_manipulation" hit on the phrase "no restriction." Both look like framework/boilerplate false positives (Angular admin-panel markup and W3C's document-license text, respectively) rather than real injection attempts — I did not act on any instructions from either page.

Here's the research. Short version up front: no one has published all three components as one system. The closest 2023–2026 work (GenOM, LLMs4OM, KROMA) generates LLM definitions and uses them for embedding retrieval + pairwise LLM verification, but all three assume a *fixed, pre-existing* set of ontology concepts — none of them detect that a term was just coined or reused in a new sense, none constrain the definition to a fixed defining vocabulary, and all restrict output to binary equivalence rather than the equivalent/broader/narrower/related typing your proposal wants (that typed-relation vocabulary is much older — it's the BT/NT/RT/USE convention from thesaurus science, formalized in SKOS). The "generate lazily, no global resource ever built" architectural stance is well-established, but in the database/Semantic Web literature (Peer Data Management Systems, Emergent Semantics), not in the terminology or LLM literature.

---

## Q1 — Closest published systems

**GenOM**
· Song, Chen & Schmidt (U. Manchester), 2025 — arXiv:2508.10703; OM2025 workshop (CEUR-WS Vol-4144); World Wide Web Journal (Springer)
· Quote 1 (Introduction): *"we develop GenOM, an ontology matching framework that leverages LLMs for semantic enrichment, candidate generation, and mapping judgement... employs an LLM-driven description generation module to produce semantically enriched textual definitions for each concept. These enriched descriptions are then embedded into a vector space to support efficient retrieval of semantically similar candidates, while an LLM-based mapping judgement component and a lightweight exact-matching module jointly refine the alignments."*
· Quote 2 (Task Formulation): *"In this study, the focus is restricted to the equivalence problem, where the objective is to determine concept pairs that denote an identical meaning across the source and target ontologies."*
· Covers: (2) LLM definition generation, (3) embedding-based retrieval + pairwise verification. Does **not** cover: (1) — concepts come from existing SNOMED-CT/NCIT/FMA ontologies, nothing is "coined" or detected; typed relations — output is binary equivalence only, not broader/narrower/related; (d) — the prompt asks for a "concise, alignment-friendly definition," not a fixed constrained vocabulary.
· Confidence: high (fetched and read in full). Could not verify: performance claims beyond what's quoted; I did not run the code.

**LLMs4OM**
· Babaei Giglou, D'Souza, Engel & Auer, ESWC 2024 — arXiv:2404.10317
· Quote: *"LLMs4OM employs a dual-module strategy: first, using the Retrieval-Augmented Generation (RAG)... for candidate selection for a given query $C_{source}$ from a knowledge base of $C_{target}$, and then LLM-based matching, in a second module, for finer accuracy."*
· Quote 2: *"$C_{s}\in C_{source}$, possible $C_{t}\in C_{target}$ that $(C_{s},C_{t},S_{C_{s}\equiv C_{t}})$, where $S\in[0,1]$ represents the likelihood of equivalence."*
· Covers: (3) retrieval + LLM verification. Does **not** cover: (2) — retrieval is over raw label/parent/child text, no generated definitions at all; (1); typed relations beyond equivalence.
· Confidence: high (fetched and read in full).

**KROMA**
· Nguyen, Barcelos, French & Wu, 2025 — arXiv:2507.14032
· From abstract (not body — I could not get past the JS-rendered PDF): *"harnesses Large Language Models (LLMs) within a Retrieval-Augmented Generation (RAG) pipeline to dynamically enrich the semantic context of OM tasks with structural, lexical, and definitional knowledge."*
· Covers: something close to (2)+(3) via "definitional knowledge" enrichment; adds "bisimilarity-based concept matching" for efficiency. Does not appear to cover (1) or typed relations (unverified — I only have the abstract).
· Confidence: low/medium — abstract-only, could not verify body claims.

**OLaLa** (mentioned inside GenOM/LLMs4OM's related work, not independently fetched)
· Described by LLMs4OM as: *"OLaLa [21] utilizes LLaMA-2 models and BERT retrievers to extract top-k matches from target ontologies for LLM prompts, refining final alignments with a precision matcher and filters."* Same gap pattern: fixed ontologies, no coinage detection, no constrained vocabulary.
· Confidence: low — secondhand via GenOM/LLMs4OM's citations, not independently read.

**Harnessing LLMs for Scientific Novelty Detection** (arXiv:2505.24615, 2025)
· The one system in this set that does something like component (1) — detecting whether an *idea* is new — but at the granularity of research ideas, not terms, and it doesn't generate constrained definitions or produce typed cross-domain relations. Included because it's the closest thing to "novelty detection" I found in the LLM era.
· Confidence: low — not fetched, search-summary only.

**What none of these five do**: detect that a term is newly coined or a familiar word is being used in a new project-local sense (component 1), constrain generated definitions to a fixed small vocabulary (component d), or output typed relations beyond binary equivalence.

---

## Q2 — Components, field terms, oldest owners

**(a) Detecting coined terms / novel senses**
· Field term: *neologism detection* (NLP/lexicography) sitting inside the broader field of *terminology science* (Terminologielehre) for the "specialized term in a domain" half of your description.
· Oldest owner (field-founding): Eugen Wüster, *Einführung in die allgemeine Terminologielehre und terminologische Lexikographie*, 1979 (roots in his 1931 dissertation) — established terminology as a discipline built on "terms as standardized labels for concepts within a structured system," per the secondary description I retrieved.
· Oldest owner (algorithmic detection, verified): Cabré & de Yzaguirre, *"Stratégie pour la détection semiautomatique des néologismes de presse,"* TTR: Traduction, Terminologie, Rédaction, 1995 — found directly in the NeoCrawler paper's own reference list (item 5) when I fetched its jbe-platform page.
· Confidence: medium — I confirmed the Cabré & de Yzaguirre citation exists (reference-list body text) but have not read that 1995 paper itself.

**(b) Automatic definition generation**
· Field term: *definition modeling* (the modern statistical/neural name) sitting inside *natural language generation from knowledge bases*.
· Oldest owner (pre-2015, and considerably older than I expected): Kathleen McKeown's **TEXT** system, ACL 1982 ("The TEXT System for Natural Language Generation: An Overview," ACL Anthology P82-1028; book form 1985) — its "Identification Schema" answered "What is X?" questions by generating class + attributes + example directly from a knowledge base. Per a secondary description: *"For McKeown's example of defining an entity or event (such as 'what is a ship?'), it is natural to first include the identification of the item as a member of a generic class, then describe the object's constituency or attributes, followed by a specific example."*
· Note: Noraset et al. (2016/2017, AAAI, arXiv:1612.00394) explicitly claim to be first at *statistical* definition generation — I fetched this in full: *"to the best of our knowledge none of the previous work has attempted \[to] create a generative model of definitions"* — but McKeown's rule-based system predates that by 34 years for the generation task itself.
· Confidence: high on Noraset (fetched in full); medium on McKeown (secondary description only, not the primary 1982/1985 text).

**(c) Definitions/glosses as the matching/retrieval representation**
· Field term: *gloss-based* (word sense) disambiguation / matching; also *reverse dictionary* (definition→word).
· Oldest owner: Michael Lesk, *"Automatic sense disambiguation using machine readable dictionaries: how to tell a pine cone from an ice cream cone,"* SIGDOC '86, ACM, 1986 — counts overlap between a word's dictionary gloss and its context to pick the right sense; this is the direct ancestor of using a definition as a searchable/matchable key rather than the term itself.
· Runner-up, closer to your exact framing (definition as *search key*): Bilac et al., 2004, first IR-based reverse-dictionary system — *"they first built a database based on available dictionaries. When a query came in, the system would find the closest definition in the database, then return the corresponding word."*
· Confidence: medium — I have Lesk's algorithm described in detail (via Wikipedia, itself citing Lesk 1986 directly) but did not read Lesk's original SIGDOC paper; Bilac 2004 is search-summary only.

**(d) Constrained/controlled defining vocabulary**
· Field term: *controlled defining vocabulary* (lexicography) / *semantic primes* or *Natural Semantic Metalanguage* (linguistics).
· Oldest owner: Anna Wierzbicka, *Semantic Primitives*, Athenäum, 1972 — proposed 14 universal, indefinable semantic primes as the substrate every other meaning must be paraphrased into. I fetched the Wikipedia NSM page directly: *"Primes are universal in that they have the same translation in every language, and they are primitive in that they cannot be defined using other words."* Predecessor in lexicography proper: the vocabulary-control movement of the 1920s–30s (Ogden's Basic English, 1930) that seeded modern learner's-dictionary defining vocabularies — older but less formally a "controlled vocabulary for writing definitions" than Wierzbicka's explicit program.
· Confidence: high on the NSM description (fetched in full); the 1930s lexicography claim is medium — from an earlier search summary, not independently read.

---

## Q3 — Is the "lazy, per-community, no global resource" stance articulated?

Yes, but not in the terminology or LLM literature — in **database schema integration** and **Semantic Web** research, roughly 20 years earlier:

**Peer Data Management Systems**
· Halevy, Ives, Suciu & Tatarinov, ICDE 2003 ("Schema Mediation in Peer Data Management Systems")
· Per search-derived description (I could not get past the JS-rendered PDF to quote verbatim, so treat this as paraphrase, not a verified quote): *"PDMSs propose the use of a decentralized, easily extensible data management architecture in which any user can contribute new data, schema information, or even mappings between other peers' schemas, representing a natural step beyond data integration systems by replacing their single logical schema with an interlinked collection of semantic mappings."*
· Confidence: low-medium — I did not verify this against the primary text.

**Emergent Semantics**
· Aberer et al., ICSNW 2004
· Per search-derived description (same caveat — PDF fetch failed, not verbatim): *"In contrast to mediated integration architectures, the decentralized integration architectures—such as Peer Data Management Systems—do not require the definition of any global schema or ontology, with the global semantics captured by considering the collection of conceptualizations as defined by the local databases and their interrelations."*
· This is the closest pre-2015 articulation I found of exactly your stance: meaning is constructed from pairwise local mappings, on demand, and no single shared ontology is ever built. Confidence: low-medium — same unverified-fetch caveat.

I found nothing in the 2023–2026 LLM/ontology-matching literature that explicitly argues *for* this stance (lazy, local, no global resource) as a design principle — GenOM, LLMs4OM, and KROMA all operate against pre-existing, already-materialized global ontologies (SNOMED-CT, NCIT, etc.), which is architecturally the opposite choice.

---

## Q4 — In the field's own vocabulary

An ontology-matching or terminology-science expert would likely call this: **a decentralized (peer-to-peer / no-global-schema) ontology-matching pipeline that substitutes LLM-generated glosses for missing terminological definitions, using them — Lesk-style — as the retrieval representation for cross-community concept alignment, and typing the resulting correspondences with the standard broader/narrower/related/exact-match relation set from thesaurus and SKOS mapping vocabulary, materialized just-in-time per project instead of via a maintained termbase or upper ontology.**

---

## Oldest sources found (by component)

- Ogden, *Basic English*, 1930 — defining-vocabulary movement (component d, lexicography thread)
- Wierzbicka, *Semantic Primitives*, Athenäum, 1972 — component (d), fetched/verified
- McKeown, "The TEXT System for Natural Language Generation," ACL 1982 (P82-1028) — component (b), oldest found, secondary-source verified
- Cabré & de Yzaguirre, TTR, 1995 — component (a), citation-verified via NeoCrawler's reference list
- Lesk, SIGDOC '86, 1986 — component (c), secondary-source verified
- ISO 2788:1986 / ANSI Z39.19 thesaurus standards (BT/NT/RT/USE) — the actual oldest owner of "typed relation: equivalent/broader/narrower/related," predating SKOS by over 20 years; **unverified-recall, not searched directly** — flagging as a gap below.

## What I did NOT search (honest gaps)

- I did not access ISO 2788, ANSI Z39.19, or any primary thesaurus-construction standard directly — the BT/NT/RT/USE claim above is from memory, not verified this session.
- I could not get past JS-rendering on several PDFs (NeoCrawler full text, the Halevy PDMS PDF, the Aberer Emergent Semantics PDF, the LLMs4OM ESWC-hosted PDF) — where I used content from these, I've marked it as secondary/unverified rather than a direct quote.
- I did not search non-English terminology-science literature (e.g., Wüster's own German-language corpus beyond secondary descriptions), Chinese/Japanese definition-modeling work, or the SemEval definition-modeling shared-task papers.
- I did not search patent-literature "novelty/prior-art via generated claims" systems, which might be a closer industrial analog to component (1)+(3) combined.
- I did not check GitHub/preprint servers outside arXiv (e.g., OpenReview, ACL Anthology directly) for 2026 work that may postdate what a generic web search surfaces.
- I did not verify any of the OAEI benchmark performance numbers reported in GenOM/LLMs4OM — treat those as the papers' self-reported claims only.
