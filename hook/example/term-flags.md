## `misroute` — flagged 20260720T205608Z (trigger: manual)

- Source files: ENTRY.md
- Excerpts: 3 paragraphs, 502 words; prompt sha256 `63ca494c1ebd16f78127c4953273ed1e407ae4bf59db316be1b84e283fbc22b0`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 82s; manifest: /mnt/f/src/de-idiolect/hook/example/.term-check/manifests/20260720T205608Z-misroute-sonnet.txt)

## 1. What the term denotes

Given a coined or opaque expression, the project searches an established literature to find the concept/reference it "really" corresponds to. A "misroute" is what happens when that search process attaches the expression to the wrong destination — an unrelated field, paper, or document — instead of the correct original source, even though the wrong match may look superficially plausible.

## 2. Closest existing terms of art

1. **Entity linking / named-entity disambiguation** — Natural Language Processing / Computational Linguistics
2. **Record linkage** (false match / linkage error) — Statistics, Database research
3. **Author/citation disambiguation** — Bibliometrics, Digital Libraries
4. **Word sense disambiguation** — Computational Linguistics
5. **Call/intent misrouting** — Spoken Dialogue Systems, Conversational AI

## 3. Oldest treatments per candidate

1. **Entity linking**: Bunescu & Pasca, 2006 (ACL); Mihalcea & Csomai, "Wikify!", 2007; Milne & Witten, 2008 — mid-2000s is where the disambiguate-to-a-knowledge-base task is first formalized.
2. **Record linkage**: Newcombe et al., "Automatic Linkage of Vital Records," *Science*, 1959; Fellegi & Sunter, "A Theory for Record Linkage," *JASA*, 1969 — the foundational statistical treatment.
3. **Author/citation disambiguation**: Lawrence, Giles & Bollacker, CiteSeer, 1999; Han, Giles et al., "Two Supervised Learning Approaches for Name Disambiguation in Author Citations," 2004.
4. **Word sense disambiguation**: Weaver's 1949 MT memo raises the ambiguity problem; Lesk, "Automatic Sense Disambiguation Using Machine-Readable Dictionaries," 1986, is the classic operational treatment; Yarowsky, 1995, for corpus-based methods.
5. **Call/intent misrouting**: Gorin, Riccardi & Wright, "How May I Help You?", *Speech Communication*, 1997 — the origin of "call routing" as a named task, where errors are literally called misrouted calls. Later multi-skill/multi-domain voice-assistant routing papers (e.g., Xu & Sarikaya's contextual domain classification work, mid-2010s) reuse the same vocabulary for wrong-skill assignment.

## 4. Fit assessment

**Entity linking** is the closest structural match: an ambiguous mention is disambiguated against a set of candidate referents, and picking the wrong one is the exact shape of a "misroute" (compare "fusion promoted the misroute document" to a wrong-candidate ranking above the gold entity). But it doesn't fully cover this usage: the "mentions" here are abstract intellectual coinages (a jargon phrase, a symbol, a slogan) rather than named entities, and the goal is scholarly-priority attribution — whose literature actually owns this idea — which is closer to a "who coined this first" dispute in history-of-science than to linking a name string to a Wikipedia page.

**Call/intent misrouting** likely explains the word choice itself (routing a query to the wrong destination skill/domain is literally called misrouting in that literature), but the domain is unrelated — dialogue-system routing operates on live user utterances dispatched to system skills, not on retrospective attribution of coined terms to academic sources.

What doesn't fit any candidate cleanly: the explicit **fidelity-gate-before-retrieval architecture** (round-trip entailment check, external-name ban, verification required before a candidate can even be scored) is not itself a named construct in entity linking, record linkage, or WSD — those fields evaluate candidate ranking directly. It most resembles the "retrieve-then-verify" pattern in modern open-domain QA/fact-checking pipelines (e.g., FEVER-style evidence retrieval + claim verification), but even there the gate is normally applied *after* retrieval, not as a precondition restricting what may be retrieved at all — so this piece of the usage is closer to a bespoke pipeline design than an established term of art.

### Draw: opus (status: ok, 71s; manifest: /mnt/f/src/de-idiolect/hook/example/.term-check/manifests/20260720T205608Z-misroute-opus.txt)

## 1. What the term denotes

A **misroute** is the failure in which a concept — presented only through a locally invented label (or a paraphrase of it) — gets matched to the *wrong established body of knowledge*: the wrong field, the wrong literature, the wrong canonical originator. The surface form of the label points at a domain that does not actually own the concept (e.g., "audit unit" pulls toward accounting when the concept belongs to statistical decision theory), and the system follows that pointer to a plausible-but-incorrect destination.

Two adjacent failures the excerpts deliberately keep *separate* from misroute help fix its boundary: "definition drift" (the description no longer matches the construct) and "polarity inversion" (the description reverses the claim). Misroute is specifically the **wrong-destination / wrong-owner** error, distinct from wrong-content errors.

## 2. Established terms of art (closest first)

| Candidate | Owning field |
|---|---|
| **Entity linking / named-entity disambiguation error** (linking a mention to the wrong referent) | NLP / information retrieval |
| **Word-sense disambiguation (WSD) error** — here driven by cross-domain **homonymy/polysemy** | Computational linguistics |
| **The "vocabulary problem," polysemy side** (same string, different meanings across communities) | HCI / IR |
| **False match / false positive** (Type-I linkage error) | Record linkage / statistics; Cranfield-style IR evaluation |
| **False mapping in ontology/schema matching** — and, from translation, **"false friends" / false cognates** | Semantic Web & databases / linguistics |

## 3. Oldest / classic treatments I'd expect to exist

- **Entity linking / Wikification:** Bunescu & Paşca (2006); Cucerzan (2007); Mihalcea & Csomai, "Wikify!" (2007). Deeper root: cross-document coreference (Bagga & Baldwin, late 1990s).
- **WSD:** traces to the machine-translation era — Weaver's 1949 memorandum, Bar-Hillel's 1960 "box/pen" argument that MT founders on sense ambiguity; Lesk (1986); Yarowsky (1995).
- **The vocabulary problem:** Furnas, Landauer, Gomez & Dumais, CACM (1987).
- **False match in record linkage:** Newcombe et al. (Science, 1959); Fellegi & Sunter, JASA (1969). IR precision/recall framing: the Cranfield experiments (Cleverdon, 1960s) and Salton's SMART work.
- **Ontology/schema matching:** Rahm & Bernstein survey (2001); Euzénat & Shvaiko's later synthesis. **False friends:** a much older, informal staple of translation/lexicography (Koessler & Derocquigny coined *faux amis*, 1928).

## 4. Fit of the best candidate, and residue

**Best fit: entity-linking / disambiguation error under cross-domain homonymy.** The core mechanism the excerpts describe — a label whose surface tokens collide with a homonym in another field, so the mapping resolves to the wrong owner — is exactly what entity linking and WSD study, and the "vocabulary problem" names the underlying cause. If you want one phrase, *cross-domain disambiguation error* covers most of it; the "fusion promoted the misroute document" line is a textbook **false-positive retrieval** result, so the IR vocabulary already fully covers that part.

**What doesn't cleanly fit any candidate:**

- **The "owner" framing is attribution, not retrieval.** The target isn't just "the right document" but the *canonical originator* (Raiffa & Schlaifer 1961; Murphy 1973). Getting the field right but the priority/originator wrong is closer to **citation/attribution and scientific-priority** concerns (history of science) than to entity linking, which typically treats any correct-entity link as success.
- **The adversarial, "actively misleading label" quality** ("actively misrouted") is stronger than neutral ambiguity. That maligned-cue aspect resembles **false friends / false cognates** more than the value-neutral homonymy that WSD assumes.
- **The evaluation apparatus is project-specific, not a term of art:** working from a paraphrase *plus an explicit ban on uttering the external name*, with round-trip-entailment fidelity gates. No standard field packages "route from a definition while forbidding the canonical name" as a named task.

**Underdetermined by the excerpts:** they don't pin down whether "misroute" is scored at the *retrieval* step (wrong candidates fetched), the *linking/attribution* step (wrong owner assigned), or the *generation* step (a definition that leads retrieval astray) — the three are conflated in the fusion discussion. They also never state the granularity of a correct destination (field? sub-literature? exact reference?), and the whole thing is measured single-cell and answer-aware (§5.3), so how "misroute" behaves as a population-level error rate is simply not specified. If you need the mapping to a single established term, decide the destination granularity first — that choice picks between "entity-linking error" (document/entity level) and "misattribution/priority error" (originator level).

## `era-gated` — flagged 20260720T205842Z (trigger: manual)

- Source files: ENTRY.md
- Excerpts: 1 paragraphs, 96 words; prompt sha256 `3fbf84d277f084905b4c9c4986c0c5790f9b1c67d7d59ad59996f5240b3daa8e`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 40s; manifest: /mnt/f/src/de-idiolect/hook/example/.term-check/manifests/20260720T205842Z-era-gated-sonnet.txt)

## 1. What the term denotes
It refers to restricting a document set to only those items that existed before some defining marker event tied to the subject being studied (here, before each coined term was "retracted"), so that whatever is drawn from that restricted set cannot have been influenced by knowledge of what happened after the marker.

## 2. Closest existing terms of art
- **Point-in-time (PIT) data / look-ahead-bias avoidance** — quantitative finance / econometrics
- **Temporal holdout (time-based train/test split)** — machine learning evaluation
- **Ex ante vs. ex post evaluation** — economics / forecasting theory
- **Knowledge cutoff / (training-)data contamination control** — NLP / LLM benchmarking
- **Chronological/date-based access embargo** — archival science, records management (weaker fit, see below)

## 3. Oldest expected treatments per candidate
- **PIT data / look-ahead bias**: backtesting literature in finance from the 1990s onward — e.g., survivorship-bias studies (Elton, Gruber, Blake, mid-1990s) and the development of point-in-time fundamentals databases (Compustat PIT, late 1980s–90s) as a response to exactly this problem.
- **Temporal holdout / time-series cross-validation**: rooted in classical forecasting-accuracy literature (e.g., Tashman, ~2000, on out-of-sample forecast testing) and later formalized as "walk-forward" validation in the algorithmic-trading/ML community.
- **Ex ante / ex post**: the distinction is classical in economics, traceable to Myrdal (1939) and standard in later forecasting-evaluation texts (e.g., Clements & Hendry, 1998).
- **Knowledge cutoff / contamination control**: a 2020s-era NLP concern, surfacing explicitly in discussions like the GPT-3 paper (Brown et al., 2020) and subsequent "test set contamination" studies.
- **Archival embargo**: standard practice in archives/records law (sealed records, classified-document release schedules), long-standing but organized around *release after* a date rather than *use only before* one — opposite polarity.

## 4. Coverage assessment
The best fit is **point-in-time data / look-ahead-bias avoidance**, with **temporal holdout / contamination control** as a close second — both name exactly the same discipline: excluding any source material generated after the moment whose outcome you're trying to predict blind, so the evaluation can't leak the answer backward in time. The excerpt's usage matches this cleanly: excerpts are filtered so a model naming/defining a coined term can't have "seen" its retraction.

What doesn't fit neatly: the cutoff here is **per-item and event-relative** (each term has its own retraction date gating its own excerpts) rather than a single global cutoff applied uniformly to a whole corpus or model, which is how "knowledge cutoff" and most PIT-data usage are typically framed. It's closer to running many small, independently-dated PIT slices within one document set than to a single dataset-wide holdout — a detail established terminology doesn't usually need to distinguish, since finance/ML applications rarely gate per-entity by an entity-specific event date within the same corpus. That's the one respect in which "era-gated" as used here is slightly more specific than any single candidate term normally implies, though it's still just an instance of the same general practice, not a distinct concept.

### Draw: opus (status: ok, 48s; manifest: /mnt/f/src/de-idiolect/hook/example/.term-check/manifests/20260720T205842Z-era-gated-opus.txt)

## 1. What the term denotes

"Era-gated" appears to mean **filtered by a time boundary so that only source material dated before a specified cutoff is admitted** — here, only documents predating each coinage's retraction, so that later material (which contains the answer) cannot leak into the input. In short: a temporal admissibility filter that enforces "nothing from after the cutoff."

Note the cutoff is *per-item* — each of the four coinages has its own retraction date, so the gate is applied separately per term rather than as one global date.

## 2. Closest established terms of art

| Term of art | Field that owns it |
|---|---|
| **Look-ahead bias** (avoided via **point-in-time / as-of data**) | Quantitative finance, econometrics / backtesting |
| **(Temporal) data leakage** — prevented by a **temporal split / temporal holdout** | Machine learning, evaluation methodology |
| **Bitemporal / valid-time / transaction-time "as-of" query** | Database systems (temporal databases) |
| **Knowledge / training cutoff** | LLM / ML systems (recent, informal) |
| **Contemporaneous sources**, source criticism (*Quellenkritik*) | Historiography |

## 3. Oldest / classic treatments I'd expect

- **Look-ahead bias & point-in-time data** — practitioner and academic backtesting literature from the 1990s; closely adjacent is the data-snooping work of **Sullivan, Timmermann & White (1999)**. "Look-ahead bias" itself is folklore-attributed rather than tied to one founding paper.
- **Data leakage** — **Kaufman, Rosset, Perlich & Stitelman**, "Leakage in Data Mining: Formulation, Detection, and Avoidance" (KDD 2011 / ACM TKDD 2012) is the canonical reference.
- **Temporal databases (valid/transaction time)** — **Snodgrass & Ahn**, "A Taxonomy of Time in Databases" (1985); Snodgrass's **TSQL2** work (early–mid 1990s).
- **Contemporaneous-source criticism** — **Leopold von Ranke** and 19th-century German historical method; formalized in **Bernheim** and **Langlois & Seignobos** (*Introduction to the Study of History*, 1898).
- **Knowledge cutoff** — no classic; a 2020s LLM-era coinage.

(I've named only references I'm confident exist; I have not invented citations.)

## 4. How well the best candidate covers it, and what doesn't fit

The best fit is the **point-in-time / look-ahead-bias** framing from backtesting, essentially tied for coverage with **temporal data leakage** from ML. Both name exactly the operation here: restrict inputs to what was knowable before a cutoff so the outcome can't contaminate the input. The *per-item, as-of* character (a separate cutoff per coinage) maps almost perfectly onto **bitemporal "as-of" semantics**, where each record is retrieved as-of its own reference time. So the concept is well-covered; "era-gated" is a local coinage for a standard idea.

What doesn't cleanly fit any single candidate:

- **The cutoff is anchored to a semantic event (a term's "retraction"), not a calendar date or a train/test boundary.** Finance/ML temporal splits usually assume a fixed timeline; here the gate is defined by a domain event that differs per entity. Bitemporal "as-of" handles the per-entity part but is a query/storage notion, not an evaluation-hygiene notion.
- **The purpose is blind-evaluation integrity** (preventing the definition from "inheriting the answers"), which pulls in ML **leakage prevention** and blinding — but the word "gating" itself refers only to the temporal filter, not the blinding.
- **"Era" hints at discrete named periods**, not continuous timestamps. The excerpt doesn't say whether documents are bucketed into coarse eras and gated at era boundaries, or filtered by exact date. If it's genuinely era-bucketed, that's coarse-grained temporal partitioning rather than precise point-in-time selection — a nuance none of the candidates specifically names.

**Underdetermined:** whether "era" implies discrete epochs vs. continuous time, and whether the gate excludes *only* post-cutoff documents or also enforces a lower bound (a windowed era). If the latter, the closest term shifts toward a **windowed / epoch-based temporal partition** rather than a one-sided point-in-time cutoff.

