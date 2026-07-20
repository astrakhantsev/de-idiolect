I've mapped every part of your system to established literature and opened multiple sources in full. Before the detail, the headline answer:

**This is a system for defeating the "vocabulary problem" / "jangle fallacy" across research communities in order to surface Swanson's "undiscovered public knowledge."** Its three parts are, in accepted terms: (1) **automatic term recognition + novel-sense / neologism detection**; (2) **definition generation ("definition modeling") written in a controlled defining vocabulary** (the Longman/Ogden/NSM tradition); (3) **ontology / vocabulary matching**, whose four labels are almost exactly the **SKOS mapping relations** (exact/broad/narrow/related) and the **S-Match** output. The "no shared master ontology, on-demand, pairwise" commitment is the **pay-as-you-go / dataspaces / emergent-semantics** philosophy. Every individual part predates 2015; I could **not** find the specific three-part integration — jargon-detection → neutral primes-only definition → use *that definition* (not the term) as the pairwise matching key, with an explicit no-global-ontology rule — built or proposed as one named artifact.

One safety note first, per how I fetch: `safefetch` flagged the W3C SKOS page with a HIGH "role_manipulation" finding (jailbreak keyword "no restriction") and stripped some content. That phrase is almost certainly benign W3C normative/legal boilerplate — a false positive — but I'm surfacing it as required. It did not affect the body text I quote below.

---

## What I read in full (body quotes)

**Source A — Natural Semantic Metalanguage (Wikipedia), fetched in full.** On the controlled-vocabulary definition idea (your Part 2):
> "The natural semantic metalanguage (NSM) theory attempts to reduce the semantics of all lexicons down to a restricted set of semantic primitives, or primes. Primes are universal in that they have the same translation in every language, and they are primitive in that they cannot be defined using other words. Primes are ordered together to form explications, which are descriptions of semantic representations consisting solely of primes."

and, on the "self-contained explanation" property:
> "A semantic analysis in the NSM approach results in a reductive paraphrase called an explication that captures the meaning of the concept explicated. … An ideal explication can be substituted for the original expression in context without change of meaning."

**Source B — W3C SKOS Reference (Miles & Bechhofer, W3C Recommendation, 18 Aug 2009), fetched in full.** On your Part-3 labels:
> "The properties `skos:broadMatch` and `skos:narrowMatch` are used to state a hierarchical mapping link between two concepts. The property `skos:relatedMatch` is used to state an associative mapping link between two concepts."

and on the cross-community bridging purpose:
> "The Simple Knowledge Organization System therefore aims to provide a bridge between different communities of practice … involved in the design and application of knowledge organization systems."

**Source C — Euzenat & Shvaiko, *Ontology Matching*, 2nd ed. (Springer, 2013), book site fetched in full.** On Part-3's relation labels and the heterogeneity motive:
> "Ontology matching aims at finding correspondences between semantically related entities of different ontologies. These correspondences may stand for equivalence as well as other relations, such as consequence, subsumption, or disjointness, between ontology entities."
> "in open or evolving systems, such as the semantic web, different parties would, in general, adopt different ontologies. Thus, merely using ontologies, like using XML, does not reduce heterogeneity: it just raises heterogeneity problems to a higher level."

(Two further items I could only get as **abstracts**, not bodies — flagged as such: Furnas et al. 1987, whose abstract states "In every case two people favored the same term with probability <0.20"; and Noraset et al. 2017, whose abstract states "We introduce definition modeling, the task of generating a definition for a given word and its embedding." The CACM full text was Cloudflare-blocked.)

---

## Q1–Q3, part by part

### The whole thing (the framing that owns all three)
- **Accepted names for the disease it treats:** the **vocabulary problem** / **vocabulary mismatch** (Furnas, Landauer, Gomez & Dumais 1987, *Communications of the ACM* 30(11):964–971 — pre-2015); the **jingle-jangle fallacy**, specifically the **jangle fallacy** = different words, same construct (Kelley 1927; the paired jingle fallacy traces to Thorndike 1904) — pre-2015; and **terminological fragmentation / "reinventing the wheel."**
- **Accepted name for the payoff:** **undiscovered public knowledge** and **literature-based discovery (LBD)** — Swanson, "Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge," *Perspectives in Biology and Medicine* 1986; and "Undiscovered Public Knowledge," *Library Quarterly* 1986 — pre-2015. Cross-field variant: **cross-domain / cross-disciplinary LBD**.
- **Field that would claim the whole:** no single owner. The closest umbrella is **information science / semantic interoperability** for research vocabularies, sitting on top of **NLP/computational linguistics** (Parts 1–2) and **Semantic Web / data integration** (Part 3). If you forced one label, "**cross-disciplinary literature-based discovery via definition-mediated semantic matching**."

### Part 1 — detect a word used in a group-specific way
- **Accepted names.** For made-up words: **neologism detection**. For the umbrella of spotting specialized vocabulary: **automatic term recognition (ATR) / automatic term extraction (ATE) / terminology extraction** (the sub-notions **termhood** and **unithood**). For an *ordinary* word carrying a special local sense: **novel word-sense detection**, **word sense induction (WSI)**, **lexical semantic change / semantic shift detection**, and **sense specialization** (a **sublanguage / domain-specific sense**). The jingle-fallacy angle (same word, two meanings) is the theoretical framing.
- **Fields.** Computational linguistics / NLP; **terminology science (terminography)**; corpus linguistics; lexicography.
- **Oldest treatments (all pre-2015).**
  - Justeson & Katz, "Technical terminology: some linguistic properties and an algorithm for identification in text," *Natural Language Engineering* 1(1):9–27, **1995**.
  - Frantzi, Ananiadou & Mima, "Automatic recognition of multi-word terms: the C-value/NC-value method," *Int'l Journal on Digital Libraries* 3(2):115–130, **2000** (earlier as ECDL '98).
  - Novel-sense / WSI root: Schütze, "Automatic Word Sense Discrimination," *Computational Linguistics* 24(1), **1998**; and Lau, Cook, McCarthy, Newman & Baldwin, "Word Sense Induction for Novel Sense Detection," *EACL* **2012**.
  - Deep conceptual root for "an ordinary word acquires a new meaning": Michel Bréal, *Essai de Sémantique*, **1897** (historical semantics). *(Hedge: I did not find a single canonical pre-2015 "neologism-detection" landmark of the Justeson-Katz stature; that subtask is real but more diffuse.)*

### Part 2 — auto-write a self-contained, controlled-vocabulary definition
- **Accepted names for the generation task.** **Definition modeling / definition generation** (produce a gloss from a representation) — the newest term. Its older sibling is **definition extraction** (find a definition already in text). The output structure "what kind of thing it is (genus), what distinguishes it (differentia)" is the classical **genus–differentia (Aristotelian) definition**. "Its inputs and outputs, what it asserts or does, when it applies" is, depending on framing, a **semantic frame** (Fillmore's frame semantics / FrameNet), a **type signature**, or a **contract / pre- and post-conditions** (Hoare 1969; Meyer's design-by-contract).
- **Accepted names for the "plain words from a fixed small list, no proper names" constraint.** **Controlled defining vocabulary** (the **Longman Defining Vocabulary**, ~2,000 words); **Basic English** (Ogden); **controlled natural language**; **Simplified Technical English (ASD-STE100)**; and — the tightest fit for "fixed small list + no names of people/methods/fields" — the **Natural Semantic Metalanguage / semantic primes** and its **reductive paraphrase / explication**, later packaged as **Minimal English**. The no-eponym rule makes the definition **community-neutral** so it can act as a **pivot / interlingua**.
- **Fields.** Lexicography and computational lexicography; NLP; **controlled natural language**; linguistic semantics (NSM); knowledge representation (formal definitions).
- **Oldest treatments (all pre-2015).**
  - Aristotle, genus–differentia definition (*Topics / Categories*), antiquity.
  - Ogden, *Basic English*, **1930** (850-word core).
  - Wierzbicka, *Semantic Primitives*, **1972**; Longman Dictionary of Contemporary English defining vocabulary, **1978**.
  - Fillmore, frame semantics (e.g., "Frame Semantics," **1982**) for the input/output/role structure.
  - Klavans & Muresan, **DEFINDER** (extraction), *JCDL* **2001**; Navigli & Velardi, "Learning Word-Class Lattices for Definition and Hypernym Extraction," *ACL* **2010**.
  - The generative version, Noraset, Liang, Birnbaum & Downey, "Definition Modeling," *AAAI* **2017**, is *post*-2015 — so for Part 2 the pre-2015 anchor is extraction + the controlled-vocabulary/lexicographic tradition, not neural generation.

### Part 3 — store definitions, use them to find the same thing under other names; pairwise labels {same · more general · more specific · related}
- **Accepted names.** **Ontology matching / ontology alignment**, **schema matching**, **vocabulary/thesaurus mapping (crosswalks)**, **semantic matching**; when it's instances, **entity resolution / record linkage**. Deciding each pair's label is **semantic textual similarity** + **textual entailment / NLI**. Using the *generated definition/gloss* as the matching key is **gloss-based / description-based matching** (a live 2020s idea, e.g. "GenOM," which uses LLM-generated descriptions to drive ontology matching). "One pair at a time" = **pairwise matching**.
- **The four labels are a near-exact match to two standards.** **SKOS mapping relations**: `exactMatch` (same), `broadMatch`/`narrowMatch` (more general / more specific), `relatedMatch` (related) — your four labels verbatim. **S-Match** (semantic matching) returns {equivalence, more general, less general, disjointness} — same lattice minus "related," plus "disjoint."
- **Fields.** Semantic Web / knowledge representation; databases (schema matching, data integration); information science (KOS interoperability); NLP (STS, NLI).
- **Oldest treatments (all pre-2015).**
  - Rahm & Bernstein, "A survey of approaches to automatic schema matching," *VLDB Journal* 10(4), **2001**.
  - Giunchiglia, Shvaiko & Yatskevich, **S-Match**, *ESWS* **2004**.
  - **SKOS Mapping Vocabulary** draft **2004** → W3C Recommendation **2009**; ISO 2788 multilingual-thesaurus interoperability, **1986** (deep root).
  - Euzenat & Shvaiko, *Ontology Matching* (Springer), 1st ed. **2007**, 2nd ed. **2013**.

### The design commitment (no shared master list; on-demand, per-group, pairwise)
- **Accepted names.** **Pay-as-you-go data integration** and **dataspaces** — Franklin, Halevy & Maier, "From Databases to Dataspaces," *SIGMOD Record* **2005**. **Peer Data Management Systems (PDMS)** with **no global mediated schema** — Halevy, Ives, et al., **Piazza**, ~**2003–2004**. **Emergent semantics** — Aberer, Cudré-Mauroux et al., "The Chatty Web," *WWW* **2003**; "Emergent Semantics Principles and Issues," **2004**. This is the deliberate opposite of the classic **mediated-schema** / **global-as-view / local-as-view** data-integration paradigm (Lenzerini, "Data Integration: A Theoretical Perspective," *PODS* 2002). From the emergent-semantics literature (search snippet, attributed to the Aberer/Cudré-Mauroux line): "no explicit representation of a globally shared agreement will be required, but agreements are implicit and result from the way the mechanism works."

---

## Q4 — Has the whole three-part system been built as one thing?

**My finding: the parts are all mature and some *pairs* have been joined, but I did not find the specific end-to-end system — detect group-specific sense → auto-write an eponym-free, primes-only, controlled-vocabulary definition → use *that definition as the matching key* for pairwise, explicitly-no-global-ontology cross-community discovery — published or built as a single named artifact.** What exists near it:

- **Goal-complete but mechanism-different:** literature-based discovery (Swanson and successors) chases the same hidden cross-domain links, but via **co-occurring intermediate terms (the ABC model)**, not via generated neutral definitions used as pivots.
- **Parts 2+3 joined:** "description/definition-generation-based ontology matching" (e.g., GenOM, 2020s) generates descriptions and matches on them — but it aligns *given ontologies*, doesn't do jargon/novel-sense *detection* from free community text, doesn't impose a primes-only eponym-free defining vocabulary, and typically isn't framed as no-global-schema-by-design.
- **The Part-3 commitment exists on its own** (dataspaces, PDMS, emergent semantics) but was not paired with auto-definition-generation from detected jargon.

So the honest verdict: **the integration is, as far as I found, novel — most distinctively the insistence that the *generated, community-neutral definition* (not the surface term, not co-occurrence, not a shared ontology) is the unit of matching, produced on demand per group.** To confirm this negative I would check, in order: (1) the **OAEI (Ontology Alignment Evaluation Initiative)** tracks and recent proceedings for any "definition/description-generation" matcher; (2) **2023–2026 surveys of LLMs for ontology matching / terminology harmonization** (I saw "LLM-Assisted Vocabulary Harmonization," CEUR Vol-4177, and "GenOM" — closest neighbors); (3) **SemEval** tasks joining definition modeling with cross-domain sense alignment; (4) **post-2020 LBD surveys** for any "definition-pivot" variant; (5) a **patent search** (vocabulary-mapping patents exist). If none of those shows the full pipeline with the primes-only/no-global-schema constraints, the negative is safe.

## Q5 — Confidence and what I could not verify

- **High confidence:** the accepted names, owning fields, and pre-2015 oldest works for each part (Furnas 1987; Swanson 1986; Justeson-Katz 1995; Frantzi et al. 2000; Ogden 1930; LDOCE 1978; Wierzbicka 1972; DEFINDER 2001; Navigli-Velardi 2010; Rahm-Bernstein 2001; S-Match 2004; Euzenat-Shvaiko 2007/2013; SKOS 2004/2009; dataspaces 2005). These are corroborated by fetched bodies (NSM, SKOS, Ontology Matching) plus multiple search corroborations.
- **Medium confidence / could not fully verify:** exact issue/page details of a few older items (Schütze 1998 issue; Bréal edition); I relied on abstracts, not bodies, for **Furnas 1987** and **Noraset 2017** (CACM full text was Cloudflare-blocked; I did not pay-wall-bypass the ACM PDF). The mapping of "inputs/outputs/asserts/applies" to frame semantics vs. type-signature/contract is **my synthesis**, not a single cited authority. The claim that the full three-part system is unbuilt is an **absence-of-evidence** result, not proof.
- **Not verified at all:** patents; non-English literature; anything behind paywalls beyond the abstracts quoted.

---

**Oldest sources I found (per strand):** Aristotle's genus–differentia (antiquity) and Bréal 1897 (semantic change) as deep roots; **Ogden, *Basic English*, 1930** and **Kelley 1927 (jangle fallacy)** as the oldest concrete named treatments; then **Swanson 1986**, **Furnas et al. 1987**, **Justeson & Katz 1995**, **Rahm & Bernstein 2001** as the oldest computational anchors.

**What I did NOT search:** patent databases; the OAEI proceedings and recent LLM-ontology-matching surveys in depth (named as the first thing to check for Q4, not yet run); non-English / non-web sources; full texts behind the ACM and Springer paywalls (only abstracts/book-front matter); SemEval task archives; and I did not exhaustively hunt a canonical neologism-detection landmark.

## Sources

- [Furnas, Landauer, Gomez & Dumais 1987, *The Vocabulary Problem* (bibliographic record + abstract)](https://honnef.co/notes/references/furnasvocabularyproblemhumansystem1987/) · [CACM listing](https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication/) (full text Cloudflare-blocked)
- [Jingle-jangle fallacies (Wikipedia)](https://en.wikipedia.org/wiki/Jingle-jangle_fallacies)
- [Swanson — Fish Oil, Raynaud's & Undiscovered Public Knowledge (Semantic Scholar)](https://www.semanticscholar.org/paper/Fish-Oil,-Raynaud's-Syndrome,-and-Undiscovered-Swanson/43f4674bded8f35df66c3a6db9ca388735718872) · [LBD survey (arXiv 1203.3611)](https://arxiv.org/pdf/1203.3611)
- [Justeson & Katz 1995 (Cambridge Core)](https://www.cambridge.org/core/journals/natural-language-engineering/article/abs/technical-terminology-some-linguistic-properties-and-an-algorithm-for-identification-in-text/D5F076938C4E3F24B11EDC2E831216AF) · [PDF](https://brenocon.com/JustesonKatz1995.pdf)
- [Frantzi, Ananiadou & Mima 2000, C-value/NC-value (Springer)](https://link.springer.com/article/10.1007/s007999900023)
- [Lau, Cook, McCarthy, Newman & Baldwin 2012, WSI for Novel Sense Detection (ACL/DL)](https://dl.acm.org/doi/10.5555/2380816.2380886)
- [Natural Semantic Metalanguage (Wikipedia, fetched in full)](https://en.wikipedia.org/wiki/Natural_semantic_metalanguage)
- [Longman Defining Vocabulary / LDOCE (Wikipedia)](https://en.wikipedia.org/wiki/Longman_Dictionary_of_Contemporary_English) · [Defining vocabulary](https://en.wikipedia.org/wiki/Defining_vocabulary)
- [Klavans & Muresan, DEFINDER (Semantic Scholar)](https://www.semanticscholar.org/paper/DEFINDER:-Rule-based-Methods-for-the-Extraction-of-Klavans-Muresan/5e891175198418fddb02d1f77fa78747f50bbe42) · [Evaluation of DEFINDER, JCDL 2001](https://dl.acm.org/doi/10.1145/379437.379488)
- [Navigli & Velardi 2010, Word-Class Lattices (ACL Anthology)](https://www.aclweb.org/anthology/P10-1134)
- [Noraset et al. 2017, Definition Modeling (arXiv 1612.00394, abstract)](https://arxiv.org/abs/1612.00394)
- [W3C SKOS Reference (fetched in full)](https://www.w3.org/TR/skos-reference/)
- [Euzenat & Shvaiko, *Ontology Matching* 2nd ed. (book site, fetched in full)](http://book.ontologymatching.org/) · [S-Match / matching overview](https://www.inrialpes.fr/exmo/research/matching.html)
- [Dataspaces / pay-as-you-go integration (Franklin, Halevy & Maier lineage)](https://link.springer.com/chapter/10.1007/978-3-662-49192-8_7)
- [Aberer et al., Emergent Semantics Systems (CEUR / Springer)](https://ceur-ws.org/Vol-292/paper1.pdf) · [The Chatty Web (WWW 2003)](https://ra.ethz.ch/cdstore/www2003/papers/refereed/p471/471-aberer.html)
- [GenOM — ontology matching with description generation + LLMs (Springer, 2020s)](https://link.springer.com/article/10.1007/s11280-026-01413-y) · [LLM-Assisted Vocabulary Harmonization (CEUR Vol-4177)](https://ceur-ws.org/Vol-4177/paper2.pdf)
- [Daille, *Term Variation in Specialised Corpora* (Benjamins, 2017)](https://benjamins.com/catalog/tlrp.19)

---

## Appendix — Query Ledger (verbatim, in order)

**WebSearch queries**
1. `vocabulary problem human-system communication Furnas Landauer Gomez Dumais 1987`
2. `definition modeling generate dictionary definition word embeddings Noraset 2017`
3. `ontology matching alignment relations equivalence more general more specific related S-Match Giunchiglia`
4. `word sense induction novel sense detection ordinary word new meaning corpus`
5. `Natural Semantic Metalanguage semantic primes Wierzbicka Goddard reductive paraphrase definitions`
6. `Longman defining vocabulary controlled 2000 words dictionary definitions LDOCE`
7. `Swanson undiscovered public knowledge literature-based discovery fish oil Raynaud 1986`
8. `automatic term recognition C-value NC-value Frantzi Ananiadou Mima multi-word terms`
9. `definition extraction from text Navigli Velardi word-class lattices hypernym 2010`
10. `dataspaces pay-as-you-go data integration Franklin Halevy Maier no global schema`
11. `SKOS mapping relations exactMatch broadMatch narrowMatch relatedMatch W3C reference`
12. `jingle jangle fallacy same word different concepts different words same concept psychology`
13. `cross-disciplinary vocabulary alignment automatic definition generation LLM bridging scientific terminology different fields same concept`
14. `terminology variation synonym detection across research communities corpora bridging jargon information retrieval`
15. `semantic primitives decomposition interlingua concept representation language-neutral definition matching pivot`
16. `Justeson Katz 1995 technical terminology linguistic properties algorithm identification Natural Language Engineering`
17. `DEFINDER Klavans Muresan 2001 definition extraction text mining medical`
18. `emergent semantics peer-to-peer no global schema Aberer self-organizing meaning agreement`

**safefetch fetches (in order)**
1. `safefetch https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication/` — blocked (Cloudflare)
2. `safefetch https://en.wikipedia.org/wiki/Natural_semantic_metalanguage` — full body
3. `safefetch https://honnef.co/notes/references/furnasvocabularyproblemhumansystem1987/` — record + abstract
4. `safefetch https://www.w3.org/TR/skos-reference/` (with HIGH security finding flagged) — full body
5. `safefetch https://arxiv.org/abs/1612.00394` — abstract
6. `safefetch https://www.w3.org/TR/skos-reference/` (grep for mapping-relation definitions) — body extract
7. `safefetch https://arxiv.org/pdf/1203.3611` (grep for Swanson) — no text extracted
8. `safefetch http://book.ontologymatching.org/` — full front-matter/body
