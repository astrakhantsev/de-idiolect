I have everything I need — three sources opened in full with genuine body quotes (SKOS Reference, the Swanson/LBD review, and the EDC paper), plus grounded abstracts for the rest. Here's the analysis.

---

## What the description actually is

Stripped of the obfuscation, the tool is: **a recall-boosting literature/prior-art search aid for terminologically-siloed research communities that, per-term and on demand, (1) detects when a word is being used in a community-local sense, (2) writes a name-free "grounded definition" of it in a restricted defining vocabulary + light math notation, and (3) uses that definition — not the word — as a language-independent pivot to retrieve, pairwise-verify, and relation-type matches in other communities (same · broader · narrower · related), without ever building or persisting a shared cross-community master list.**

That maps cleanly onto several established framings. No single published system I could find *is* this exact composition — so treat this as a **novel recombination of well-established components**, which is what makes the naming question answerable but the "same thing" question come up empty.

---

## 1. What it would be called in established research; which fields claim it

There is no one canonical name for the *whole*, but the whole sits at the intersection of these accepted framings:

- **The vocabulary (mismatch) problem / the "vocabulary gap"** — the canonical name for the underlying failure the tool attacks. This is the *problem*, of which the tool is one *solution instance*. Fields: **Information Retrieval (IR)** and **HCI**.
- **Concept-based (vs. term-based) retrieval / semantic interoperability across knowledge-organization systems**, specifically the **ontology-free / instance-based** flavor — matching *concepts* through generated glosses rather than shared controlled vocabularies. Fields: **Library & Information Science / Knowledge Organization**, **Semantic Web**.
- **Literature-based discovery (LBD) / "undiscovered public knowledge"** — bridging *complementary but disjoint literatures*. The tool is a **recall-oriented cousin** (find the same known thing under another name) rather than the classic hypothesis-generation goal. Fields: **information science, biomedical informatics, science-of-science / scientometrics**.
- **Definition modeling / definition generation** (step 2) and **reverse-dictionary / definition-based retrieval** (step 3), plus **novel-sense (lexical semantic change) detection & word-sense disambiguation** (step 1). Fields: **NLP / Computational Linguistics**.
- The output typology is literally **SKOS mapping relations** (`exactMatch / broadMatch / narrowMatch / relatedMatch`) — the standard name for "same thing · more general · more specific · related." Field: **Semantic Web / knowledge organization**.

The best short umbrella phrasings drawn from the literature: **"definition-mediated cross-vocabulary retrieval"**, **"ontology-free concept alignment for cross-terminology search"**, or, in the LBD idiom, **"bridging disjoint literatures by concept rather than by term."**

The **W3C SKOS Reference** body pins the typology exactly (attributed quote, W3C SKOS Reference §10, Miles & Bechhofer eds., 2009):

> "The SKOS mapping properties are `skos:closeMatch`, `skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch` and `skos:relatedMatch`. These properties are used to state mapping (alignment) links between SKOS concepts in different concept schemes… The properties `skos:broadMatch` and `skos:narrowMatch` are used to state a hierarchical mapping link between two concepts. The property `skos:relatedMatch` is used to state an associative mapping link between two concepts."

Note the deliberate mismatch that supports "ontology-free": SKOS also warns that strong logical identity (`owl:sameAs`) is "typically… inappropriate for linking SKOS concepts in different concept schemes, because the formal consequences that follow could be undesirable" — which is precisely why the tool's *ephemeral, per-pair* labels, rather than a persistent merged ontology, fit the SKOS philosophy.

---

## 2. Closest existing things (author / year / venue), each with a relation label

**On the underlying problem**
- **Vocabulary mismatch problem** — Furnas, Landauer, Gomez & Dumais, "The Vocabulary Problem in Human-System Communication," *CACM* 30(11):964–971, 1987. → **more general** (the tool solves a special case). From the paper's own abstract (Furnas et al., 1987): *"the system must recognize terms that will be chosen spontaneously… In every case two people favored the same term with probability <0.20."*
- **Query expansion / pseudo-relevance feedback** (Rocchio lineage; and its modern LLM/generative variants) — the standard IR remedy for that gap. → **related** (different remedy: it augments the *query* with co-occurring *terms*, staying inside surface vocabulary, rather than pivoting through a name-free definition).

**On connecting siloed literatures**
- **Literature-based discovery / "undiscovered public knowledge" / the A-B-C model** — Swanson, 1986; reviewed in Smalheiser, "Rediscovering Don Swanson," *J. Data & Information Science* 2(4):43–64, 2017. → **related** (shares the disjoint-communities motivation; classic goal is *new A–C hypotheses*, not same-thing-different-name recall). Attributed body quote (Smalheiser 2017): *"The most novel and fruitful type of undiscovered public knowledge… occurs when information is not explicitly discussed in any single article at all. Rather, different assertions and findings need to be assembled across documents…"* — and, tellingly for step 1, Smalheiser notes *"word sense disambiguation, i.e., to separate different senses of the same word as used in different instances, can improve performance of discovery systems."*
- **Analogy mining via purpose/mechanism schemas** — Hope, Chan, Kittur & Shahaf, "Accelerating Innovation Through Analogy Mining," *KDD '17* (best-paper). → **related** (closest in *spirit*: it abstracts away surface terms to match across domains, but retrieves *same-purpose–different-mechanism analogies*, whereas the tool retrieves *same/broader/narrower/related* concepts). Abstract, attributed: *"'problem schemas', which specify the purpose of a product and the mechanisms by which it achieves that purpose… find analogies with higher precision and recall than traditional information-retrieval methods."*

**On the individual steps (components)**
- **Definition modeling** — Noraset et al., "Definition Modeling: Learning to Define Word Embeddings in Natural Language," *AAAI 2017*; and contextual-definition-generation successors. → **more specific** (this *is* step 2).
- **Reverse dictionary / definition→concept retrieval** — Hill, Cho, Korhonen & Bengio, "Learning to Understand Phrases by Embedding the Dictionary," *TACL* 4:17–30, 2016. → **more specific** (this *is* the step-3 mechanism). Abstract, attributed: *"reverse dictionaries that return the name of a concept given a definition or description… the effectiveness of… definition-based training."*
- **Novel-sense / lexical semantic change detection** — SemEval-2020 Task 1 (Schlechtweg et al., 2020) and definition-generation-for-sense-representation (e.g., Giulianelli et al., 2023, arXiv:2305.11993). → **more specific** (steps 1–2, but aimed at diachronic sense analysis, not cross-community retrieval).

**On the three-step skeleton and the output typology**
- **Extract-Define-Canonicalize (EDC)** — Zhang, Soh et al., "Extract, Define, Canonicalize: An LLM-based Framework for Knowledge Graph Construction," *EMNLP 2024* (arXiv:2404.03868). → **related**, and the *closest structural twin*: near-identical three-move skeleton with definitions as the matching pivot. Attributed body quotes: *"a three-phase framework named Extract-Define-Canonicalize (EDC): open information extraction followed by schema definition and post-hoc canonicalization… in the latter case, it constructs a schema automatically and applies self-canonicalization"*; and *"The definitions are used to find the closest entity/relation type candidates (via a vector similarity search) that the LLM can then reference to canonicalize a component."* Key divergence: EDC *builds and persists a KG schema* within one corpus — exactly the "shared master list" the described tool refuses — so it's a twin of the *mechanism*, not of the *no-persistent-crosswalk, cross-community* purpose.
- **Ontology alignment / matching** — Euzenat & Shvaiko, *Ontology Matching* (Springer, 2007/2013). → **related** (same output relations — equivalence/subsumption — but presupposes and maintains ontologies; the tool is the on-demand, ontology-free counterpart).
- **Concept normalization / entity linking to a metathesaurus (e.g., UMLS)** — this is the *shared-master-list* paradigm. → **related, by contrast** (it does exactly what the tool forbids: map variants to persistent canonical concept IDs). *(Background knowledge; I did not fetch a UMLS source this session.)*

**On the "fixed small list of plain common words" defining vocabulary**
- **Natural Semantic Metalanguage / semantic primes** — Wierzbicka (from the early 1970s) and Goddard; "reductive paraphrase" into ~65 indefinable primes. → **related** (the linguistics ancestor of "define using only a small fixed set of plain words, no proper names"). Also related: controlled defining vocabularies like **Ogden's Basic English** and the **Longman Defining Vocabulary**. *(NSM date from a secondary source; see caveats.)*

**"Same thing"?** — I found **none**. No single published system combines all of {per-term lazy jargon detection · name-free restricted-vocabulary grounded definition · definition-as-pivot cross-community retrieval · SKOS-style relation typing · explicitly no persistent crosswalk}. The description is best read as an original composition of the above.

---

## 3. Candidate names in a practitioner community's own words

Built only from established field wording:

1. **Definition-mediated cross-vocabulary retrieval** (a.k.a. *definition-pivot concept matching*) — foregrounds the "gloss as interlingua pivot" mechanism.
2. **Ontology-free (just-in-time) concept normalization for cross-terminology search** — foregrounds the lazy, per-term, no-shared-master-list design.
3. **Concept-based bridging of disjoint literatures** — the LBD-flavored name, emphasizing recall across siloed communities.

(If one word is wanted: an *"on-the-fly semantic crosswalk"* — using "crosswalk" in its LIS sense, with "on-the-fly" marking that it's rebuilt per query rather than maintained.)

---

## 4. Confidence and what I could not verify

**High confidence:** the mapping of each component and of the output labels to named literatures — SKOS mapping relations (verified verbatim from the W3C body), the vocabulary-mismatch framing (Furnas 1987), LBD/undiscovered public knowledge (Swanson via Smalheiser 2017 body), reverse dictionary (Hill 2016), definition modeling (Noraset 2017), analogy mining (Hope 2017), and the EDC three-move skeleton (verified from the paper body). Author/year/venue for these are solid.

**Medium confidence:** that no single "same thing" system exists. I searched the obvious framings but cannot rule out a niche or very recent (2025–2026) preprint that is the exact composition; absence of evidence isn't proof. Treat "novel composition" as my best read, not a certainty.

**Lower confidence / could not verify:**
- The **NSM founding date (early 1970s)** and the ~65-prime count come from a secondary search snippet (Wikipedia/Grokipedia-adjacent), not a fetched primary Wierzbicka text.
- I did **not** find any IR system that actually uses **semantic primes / a controlled defining vocabulary as its retrieval metalanguage** — the "fixed small list of plain common words + math notation" constraint is my *inference* linking NSM/Basic-English/Longman to the tool, not a documented pairing. Hedged pointer, not a confident citation.
- Two intended full-text fetches **failed**: the *CACM* Furnas page (Cloudflare block) and the arXiv PDF of "Remedies against the Vocabulary Gap in IR" (arXiv:1711.06004) — so for Furnas I quoted the abstract/BibTeX from a mirror, and for the vocabulary-gap remedies paper I have only the search snippet, not its body. I did not invent any quote from either.

---

### Oldest sources found
- **Wierzbicka's NSM**, early **1970s** (semantic primes; secondary-source date — see caveats).
- **Popper's "World III"**, **1978** (referenced *inside* Swanson's UPK framing).
- **Swanson, "undiscovered public knowledge," 1986**; **Furnas et al., "vocabulary problem," 1987** — the two oldest I grounded directly to text.
- (Older lineage I flag but did not fetch: **Ogden's Basic English, 1930**, and the **Longman Defining Vocabulary, 1978**, as ancestors of the "restricted defining vocabulary" idea.)

### What I did NOT search
Commercial/vendor semantic-search and patent-prior-art products; non-English-language literature; the deep LIS crosswalk/thesaurus-mapping literature (beyond the SKOS spec); UMLS Metathesaurus primary docs; cross-lingual IR / interlingua-pivot MT primary papers; and any 2025–2026 preprints that might be the exact proposal. I also did not attempt to identify the withheld local name of the tool.

### Query ledger (verbatim, in order)
1. `vocabulary problem in human-system communication Furnas 1987`
2. `undiscovered public knowledge Swanson literature-based discovery disjoint literatures`
3. `definition modeling generating definitions from word embeddings Noraset 2017`
4. `SKOS mapping relations exactMatch broadMatch narrowMatch relatedMatch`
5. `accelerating innovation through analogy mining Hope 2017 purpose mechanism cross-domain`
6. `Natural Semantic Metalanguage semantic primes reductive paraphrase Wierzbicka Goddard`
7. `novel word sense detection lexical semantic change SemEval 2020 emerging senses corpora`
8. `bridging vocabulary gap interdisciplinary literature search jargon barrier scientific silos retrieval`
9. `reverse dictionary learning to understand phrases by embedding the dictionary Hill 2016`
10. `LLM on-the-fly jargon normalization cross-domain retrieval ontology-free grounded definition prior art`
11. `Extract Define Canonicalize EDC ontology-free knowledge graph construction LLM schema canonicalization`
12. `query expansion vocabulary mismatch concept normalization pseudo-relevance feedback information retrieval survey`

(Pages fetched in full via `safefetch`: W3C SKOS Reference; PMC "Rediscovering Don Swanson"; arXiv:2404.03868 EDC HTML; arXiv:1706.05585 abstract; ACL Q16-1002 landing; honnef.co Furnas BibTeX. Failed fetches: cacm.acm.org Furnas page — Cloudflare block; arXiv:1711.06004 PDF and its ar5iv HTML — empty/fatal-error.)

**Sources:**
- [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
- [Furnas et al. 1987, The Vocabulary Problem (CACM)](https://dl.acm.org/doi/10.1145/32206.32212) · [mirror](https://honnef.co/notes/references/furnasvocabularyproblemhumansystem1987/)
- [Smalheiser 2017, Rediscovering Don Swanson (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5771422/)
- [Hope et al. 2017, Accelerating Innovation Through Analogy Mining (arXiv)](https://arxiv.org/abs/1706.05585)
- [Noraset et al. 2017, Definition Modeling (AAAI)](https://ojs.aaai.org/index.php/AAAI/article/view/10996)
- [Hill et al. 2016, Learning to Understand Phrases by Embedding the Dictionary (TACL)](https://aclanthology.org/Q16-1002/)
- [SemEval-2020 Task 1, Unsupervised Lexical Semantic Change Detection](https://aclanthology.org/2020.semeval-1.30/)
- [Zhang et al. 2024, Extract-Define-Canonicalize (arXiv)](https://arxiv.org/abs/2404.03868)
- [Natural Semantic Metalanguage (Wikipedia)](https://en.wikipedia.org/wiki/Natural_semantic_metalanguage)
- [Remedies against the Vocabulary Gap in IR (arXiv, fetch failed)](https://arxiv.org/abs/1711.06004)
