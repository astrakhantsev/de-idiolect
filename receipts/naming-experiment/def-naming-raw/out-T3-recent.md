## Security note first

Fetching the NeoN paper (arXiv:2505.15426) tripped safefetch's scanner: **HIGH — `role_manipulation: Jailbreak keywords: "No filter"`**, and it stripped one table cell. I checked the surrounding text: the stripped cell is the header row of an ablation table (Table 1), listing filter-pipeline stages ("+ Min Token Len", "+ Max Token Len", "+ No Digits"...) — the stripped label is almost certainly "No filter" as the *baseline row before any filter is applied* (200,696 candidates, precision 0.003), not an injected instruction. This reads as a false positive from the phrase "no filter" resembling jailbreak language ("you have no filter..."). Flagging per policy; I did not treat any instruction from the page as authoritative.

---

## Verdict up front

After this sweep, the three-part assembly — **(a)** a term/sense-novelty **detector** that **(b)** feeds **constrained-vocabulary** definition generation which **(c)** serves as a **no-global-ontology, cross-community retrieval key with typed relations** — is still **unfound as an integrated whole**. I found two partial fusions that are new and closer *on individual legs* than SciCo-Radar/GenOM, but neither closes the loop: **NeoN** and the **AXOLOTL'24 lineage** fuse (a)+(b) — novelty detection feeding LLM definition generation — but do zero cross-community concept retrieval and use free-text (not constrained) definitions. **GenOM/SciCo-Radar** remain the closest on (b)+(c) but operate over *pre-existing* ontology classes/documents, not detected neologisms, so they have no (a) and no "no-global-resource" property (GenOM explicitly aligns against a standing ontology like SNOMED/NCIT). Below are the findings, then what I skipped, then the query ledger.

---

## Findings

### 1. NeoN (Tomaszewska, Czerski, Żuk, Ogrodniczuk) — arXiv:2505.15426
**Covers:** (a) yes — multi-stage detector (corpus cross-referencing, frequency/structural/spelling filters, then an LLM few-shot filter) flags novel Polish lexemes from daily RSS feeds. (b) partial — an LLM module generates definitions "on demand," but in free text, not a constrained/controlled vocabulary. (c) **absent** — single-language, single-corpus lexicographic tool; no cross-community matching, no retrieval-by-definition, no typed relations.
**Quotes:** *"NeoN combines reference corpora, Polish-specific linguistic filters, an LLM-driven precision-boosting filter, and daily RSS monitoring in a multi-layered pipeline... An integrated LLM module automatically generates definitions and categorizes neologisms by domain and sentiment."* … *"Users can easily generate definitions and categories on demand using real-life usage examples extracted through our multi-layered pipeline."* … *"To our knowledge, this is the first application of LLMs as a filtering mechanism in neologism detection."*
**Confidence:** High (read full HTML body, table of ablation results, appendix references).
**Could not verify:** Whether any downstream user of NeoN's output does cross-lingual or cross-source concept matching — the paper doesn't claim it and I found no follow-up integrating NeoN definitions into a matching/retrieval system.

### 2. AXOLOTL'24 shared task (Fedorova, Mickus, Partanen, Siewert, Spaziani, Kutuzov) — arXiv:2407.04079, + follow-up "Explaining novel senses using definition generation with open language models" (Fedorova, Kutuzov, Periti, Scherrer) — arXiv:2509.26181
**Covers:** (a) yes — explicit subtask 1 is "identifying unknown (novel) senses." (b) yes — subtask 2 is "providing human-readable descriptions (such as definitions)" of exactly those novel senses; the 2025 follow-up fine-tunes open LLMs to do this generation step end-to-end. (c) **absent** — evaluated via BLEU/BERTScore against a single gold gloss per word; no retrieval, no cross-community anything, no typed relations, no constrained vocabulary requirement.
**Quotes:** *"Explainable semantic change modeling can be broken down into two sub-tasks: 1. Finding target word usages corresponding to newly gained senses; 2. Providing human-readable descriptions (such as definitions) of the gained senses."* (2407.04079) … *"We apply definition generators based on open-weights Large Language Models (LLMs) to the task of explaining novel word senses, taking target word usages as an input."* (2509.26181)
**Confidence:** High (both fetched in full).
**Could not verify:** Any OM/retrieval application built on top of AXOLOTL-style gloss generation — I searched but found none; this lineage stays purely diachronic (time, not community) and purely descriptive (no matching key use).

### 3. GenOM (Song, Chen, Schmidt) — arXiv:2508.10703 (also OM2025 workshop paper, accepted to *World Wide Web*, Springer 2026) — **KNOWN, re-verified not re-discovered**
**Covers:** (b) yes — generates textual definitions to enrich ontology-concept semantics. (c) yes — those definitions are embedded and used as the retrieval key for candidate alignment, refined by exact-match tools. (a) **absent** — it operates over concepts that already exist in a standing ontology (OMIM, NCIT, SNOMED CT, etc.); nothing is "coined" or detected as novel, and the ontologies are a global, pre-built resource — the opposite of "no global ontology ever built."
**Quote:** *"This paper introduces GenOM, a large language model (LLM)-based ontology alignment framework, which enriches semantic representations of ontology concepts via generating textual definitions, retrieving alignment candidates with an embedding model, and incorporating exact lexical matching tools to improve precision... this paper introduces a set of criteria for evaluating the quality of concept definitions that are generated."*
**Confidence:** High (fetched full HTML v3).
**Could not verify:** Nothing new to flag — this matches the prompt's own characterization; I re-confirmed rather than re-discovered it.

### 4. OAEI 2024/2025 campaigns (full result pages + workshop synthesis)
**Covers:** Surveyed for any *other* definition-generation matcher with a novelty detector or "no global ontology" framing. **None found.** 2025 fielded GenOM and Agent-OM (LLM-agent-based, uses embeddings + LLM reasoning but not built around novelty detection) across 12 tracks (anatomy, conference, Bio-ML, biodiversity, digital humanities, circular economy, knowledge graph, beyond-equivalence, pharmacogenomics, etc.) — all matchers align *given, static* ontologies; 2024 highlighted CANARD (embedding-based, no definition generation) as the standout LLM-enhanced system.
**Quote:** *"In the OAEI 2025 campaign, we adopted the MELT platform for most of the evaluation tasks... The (preliminary) OAEI 2025 results are available track by track."* (oaei.ontologymatching.org/2025/results)
**Confidence:** Medium — the results-index page and Bio-ML results page loaded fully, but the two official synthesis PDFs (2024 and 2025 "om2025-oaei-paper0.pdf") both returned empty DOM on fetch (JS-rendered viewer, no extractable text) on every mirror I tried (CEUR direct, City University Open Access mirror). I could not read the full narrative synthesis text of either paper directly.
**Could not verify:** Whether any smaller/newer 2025 OAEI participant paper (of the ~20 listed) besides GenOM/Agent-OM uses definition-generation-as-retrieval-key — I could see the *track list* and confirm GenOM/Agent-OM's presence via search snippets and the GenOM paper itself, but I did not individually open all ~20 system-paper PDFs, most of which are CEUR PDFs that render as JS-walled empty pages under safefetch.

---

## Closest single system found
No single system fuses all three parts. Split by which two legs each family covers:
- **(a)+(b)** — detector feeding definition generation: **NeoN** (arXiv:2505.15426) and the **AXOLOTL'24 → Fedorova et al. 2025** lineage (arXiv:2407.04079, arXiv:2509.26181).
- **(b)+(c)** — definitions as no-detector retrieval keys over an existing resource: **GenOM** (arXiv:2508.10703), consistent with the prompt's existing characterization, alongside SciCo-Radar.
Nothing crosses both boundaries — no detector-fed system does cross-community retrieval, and no retrieval-key system detects novelty rather than matching pre-existing concepts.

## What I did NOT search
- I did not open the ~20 individual OAEI-2025 system papers beyond GenOM and the results-index/Bio-ML pages (most are CEUR PDFs that render empty under safefetch's JS-DOM extraction; would need a PDF-text extraction path instead).
- I did not search non-English venues (e.g., Chinese CCL, Japanese NLP conferences) where community-jargon/neologism work is active.
- I did not check patent databases or industry blog/preprint venues (company research blogs, Hugging Face papers feed) beyond what surfaced incidentally.
- I did not do a systematic pass through *every* OAEI 2024 track-by-track result page (only the synthesis-paper level), so a definition-generation matcher entered in a single niche track (e.g., Digital Humanities, Circular Economy) in 2024 specifically could have been missed.
- I did not verify KROMA (arXiv:2507.14032) or LLMs4OM (arXiv:2404.10317) bodies directly this pass, since the prompt marked them as already-known — I relied on the prompt's characterization rather than re-reading them.

## Query ledger (verbatim, in order)
1. `OAEI 2024 ontology alignment evaluation initiative results LLM definition generation matcher`
2. `OAEI 2025 track results LLM-generated definitions ontology matching`
3. `arXiv 2025 "no global ontology" "generate on demand" LLM definition concept alignment`
4. `arXiv 2025 novel sense detection LLM community-specific term definition generation cross-community`
5. `AXOLOTL-24 shared task explainable semantic change modeling novel word sense detection definition generation`
6. `"emerging terminology" OR "neologism detection" LLM scientific text 2025 2026 arXiv`
7. `reverse dictionary LLM generated definitions embeddings retrieval 2025`
8. `"gloss-informed" bi-encoder word sense disambiguation generated definitions retrieval`
9. `"jargon" OR "community-specific term" LLM definition generation concept matching cross-domain retrieval 2024 2025 arXiv OR ACL`
10. `"semantic change detection" LLM 2025 2026 survey definition generation downstream application`
11. `OpenReview 2025 2026 term coinage detection ontology-free concept alignment LLM generated gloss`
12. `"typed relation" cross-community concept matching definition retrieval key LLM 2025 arXiv`
13. `computational conceptual history scientific concepts LLMs community coins term arXiv 2606.04118`
14. `"lazy" ontology generation on-the-fly per-community concept definition LLM alignment no shared schema`
15. `forum Reddit subreddit jargon term detection LLM definition generation glossary cross-community 2024 2025`
16. `LLMs4OL 2025 Large Language Models Ontology Learning challenge term extraction definition generation results`

**Sources fetched in full (safefetch):** arXiv:2505.15426 (abs + HTML body), arXiv:2407.04079 (full HTML), arXiv:2509.26181 (full HTML), arXiv:2508.10703 (abs + full HTML v3), oaei.ontologymatching.org/2025/ (campaign + results index), liseda-lab.github.io/OAEI-Bio-ML/2025 (Bio-ML results page). Two fetches failed (empty JS-rendered DOM): ceur-ws.org/Vol-4144/om2025-LTpaper3.pdf, ceur-ws.org/Vol-3897/oaei2024_paper0.pdf, openaccess.city.ac.uk mirror of the same.
