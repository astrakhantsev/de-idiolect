Before the full writeup: across ~15 fetches, safefetch flagged findings on 6 pages — all appear to be false positives (patent boilerplate like "act as a"/"function as a" triggering role-manipulation heuristics, a Microsoft responsible-AI FAQ discussing red-teaming triggering a "jailbreak" keyword hit, and ordinary `![...]` markdown images pointing to the sites' own CDNs triggering data-exfiltration heuristics). I read the surrounding content in each case and found no actual injected instructions directed at me — flagging per policy, but I did not act on any of it.

Here's the full research report.

## Summary verdict

No patent or product implements the proposed system's core novel step — **using an auto-generated plain-language definition as the matching key across teams with typed same/broader/narrower/related relations, without a mandated global glossary.** Patents and products separately cover pieces (a), (b), or a *different* form of (c), but never the specific combination:

- **Patents**: closest is Microsoft's US8589791B2/US10552522B2 family (2011/2013) — explicitly names the "different teams, different vocabularies" problem and auto-generates per-document definitions — but it never uses those definitions to match concepts *across* teams; each project's glossary stays local.
- **Enterprise products**: Atlan's "Sage" agent (2025-2026) is the closest real-world (c) analogue — it detects when two teams give **the same term** two different definitions — but it resolves this to one canonical/centralized answer (data governance ontology), the opposite philosophy of typed multi-relations with no global mandate.
- **KM tools**: Confluence's "Define" (Atlassian Intelligence, GA since 2023) and Slack's "hover for meaning" (announced 2025) are the closest matches to (a)+(b) together — lazy, on-demand, per-workspace definition generation from usage, with an explicit "no dedicated glossary, no setup" framing. Neither does cross-team matching at all.

---

## 1. Patents

**US9465792B2 — "Computer automated organization glossary generation systems and methods"**
SAP/SuccessFactors Inc. · filed 2014-12-30, granted 2016-10-11 · [patents.google.com/patent/US9465792B2](https://patents.google.com/patent/US9465792B2/en)
- **Covers**: (a) partial — extracts org-specific terminology from unstructured/semi-structured corporate documents (emails, PDFs, decks) via statistical n-gram (unigram/bigram/trigram) analysis with TF/IDF filtering, explicitly "customized" per organization.
- **Does not cover**: (b) — output is a list of *terms*, not generated definitions. (c) — no cross-team/cross-corpus matching; terms feed into one internal "learning graph."
- Quote: *"An organizational glossary...may include a large list of terms that are commonly used inside a particular organization...and that may have particular meaning and relationships to other terms or content inside the organization that may (or may not) be different than a generic meaning...to other organizations."*
- Confidence: **HIGH** (read full description directly).

**US8589791B2 (2011/2013) + continuation US10552522B2 (2013/2020) — "Automatically generating a glossary of terms for a given document or group of documents"**
Microsoft Corp / Microsoft Technology Licensing LLC · [US8589791B2](https://patents.google.com/patent/US8589791B2/en) · [US10552522B2](https://patents.google.com/patent/US10552522B2/en)
- **Covers**: (a) — parses documents for unfamiliar terms/acronyms/phrases; (b) — retrieves/generates candidate definitions from local and external sources, ranks them, and (crucially) **explicitly names the multi-team jargon problem** the proposed system targets.
- **Does not cover**: (c) — definitions are merged into a per-project/per-document glossary store; there is no mechanism comparing one team's generated definition against another team's to detect the same underlying concept. No typed relations.
- Quote (background section): *"Because the enterprise may be broken into various teams each of which may have its own unique vocabulary that is developed in association with its electronic content production"* [...] *"there is no one source a given user may access for definitions of such terms."*
- Quote (claims): definitions are *"stored in a project store for subsequent use in association with the documents"* — scoped to the project, not cross-referenced against other teams' stores.
- Confidence: **HIGH** (read abstract, background, and claims 1–20 directly for both).

**US8296651B2 — "Selecting terms for a glossary in a document processing system"**
IBM Corp · filed 2007 (priority 2006), granted 2012 · [patents.google.com/patent/US8296651B2](https://patents.google.com/patent/US8296651B2/en)
- **Covers**: (a) only — a probabilistic rule-based scorer (with an active-learning feedback loop from user accept/reject behavior) ranks candidate terms extracted from a document as glossary-worthy.
- **Does not cover**: (b) — definitions are entered manually by the user ("the user may be prompted to add a definition for the term"), not generated. (c) — no cross-document/cross-team matching.
- Quote: *"Glossaries are information repositories that hold information defining particular terms such as acronyms, specialist language or jargon."*
- Confidence: **HIGH**.

**US7885949B2 + family (US7363305B2, US7617232B2) — "Centralized terminology and glossary management"**
Microsoft Corp · filed 2004, granted 2011 (family spans 2004–2011) · [patents.google.com/patent/US7885949B2](https://patents.google.com/patent/US7885949B2/en)
- **Covers**: none of (a)/(b)/(c) — this is a manually-curated terminology database, not NLP-driven detection or generation.
- **Relevant to Q4 specifically as a direct counter-example**: it is the explicit *opposite* architecture from "lazy, per-team, no global glossary." Individual groups (ABC, XYZ, DMD in the patent's own example) keep local servers but must replicate every term to one **mandatory central database**, and the invention's stated goal is *"a single term corresponds to a single definition"* enterprise-wide.
- Quote: *"individual group members...may function independently of each other in designing their own terminology but still share their knowledge with other group members...allow[ing] consistent terminology usage across the organization such that a single term corresponds to a single definition."*
- Confidence: **HIGH**.

**US11922326B2 — "Data management suggestions from knowledge graph actions"**
Backoffice Associates LLC · priority 2021-09-02, granted 2024 · [patents.google.com/patent/US11922326B2](https://patents.google.com/patent/US11922326B2/en)
- **Covers**: (a) and a *different* mechanism for (c) — when a governed data asset changes, the system extracts candidate terms and compares them against existing terms elsewhere in the enterprise knowledge graph, surfacing either brand-new terms or existing terms newly relevant to that asset (suggesting new graph edges/relations).
- **Does not cover**: (b) — the "definition" shown to users is a pre-existing curated metadata field on a term node, not something the system generates. The matching key is **term-string identity + graph relationships**, not a generated natural-language definition used as the matching representation — the core distinguishing mechanism the proposed system relies on.
- Quote (abstract): *"comparing each candidate term with each of one or more existing terms from data assets of the knowledge graph...to obtain (i) one or more of the candidate terms that do not correspond to any existing term or (ii) one or more candidate terms that each corresponds to a respective existing term that is not related to the version node."*
- Confidence: **HIGH**.

**Tangential, lower relevance**: US10268752B2 (eBay, 2019) "Automatic taxonomy mapping using sequence semantic embedding" maps e-commerce listing content across differing category taxonomies using semantic embeddings — structurally similar to "match via a generated representation," but the representation is embedded *listing text*, not a generated definition, and the domain is product categorization, not organizational jargon. **Confidence: MEDIUM** (bibliographic data confirmed directly; description not fully read).

**Not independently verified**: US20250139088A1 (Alation, pending application, 2025) "Techniques and architecture for securing large language model assisted interactions with a data catalog." Per search-engine synthesis only — two direct-fetch attempts both failed (Google Patents served an unrendered JS shell). Described scope is about securing/orchestrating LLM-to-structured-query translation for querying a catalog, not jargon detection or definition generation — **likely low relevance to (a)/(b)/(c)**, but I flag this as **LOW confidence** since I could not read primary text myself.

---

## 2. Enterprise data-catalog / business-glossary products

**Atlan — Context Agents (Lexis, Sage, Nexus, Orion)** · [atlan.com/data-glossary](https://atlan.com/data-glossary/), [atlan.com/know/context-bootsrapping](https://atlan.com/know/context-bootsrapping/)
- **Lexis** ("Glossary Bootstrapping agent") covers (a)+(b): *"reads your existing definitions, column naming conventions, and domain patterns and builds the business glossary your team never finished. Every term defined, every asset documented, from signals that already exist in your systems."*
- **Sage** ("Metric Conflicts agent") is the closest thing to (c) I found anywhere, but inverted in mechanism and philosophy: *"finds where two teams define the same metric differently — 'MRR' in Finance vs. 'MRR' in Sales, 'active user' in Product vs. 'active user' in Marketing — and surfaces the conflict. Each conflict is routed to the relevant team stewards for resolution. Once a definition is approved...every AI agent that uses it inherits the certified answer."* This matches on **shared term-name, divergent definition** (opposite direction from the proposed system's same-definition/different-term matching), and resolves to **one governed canonical answer**, not typed same/broader/narrower/related relations preserving each team's framing.
- **Orion** ("Ontologist") is framed closer to context-sensitive multi-answer: *"maps every relationship between domains, terms, and assets — so when an agent asks what 'revenue' means, it gets the right answer for the right context."* No public documentation describes explicit relation typing (same/broader/narrower/related).
- **Explicitly NOT "lazy, no global glossary"**: the entire pitch is a single governed "context layer"/semantic layer delivered identically to every agent — *"One shared definition. Every agent."* This is architecturally centralized, the opposite of the proposed system's framing.
- Confidence: **HIGH** (read atlan.com/data-glossary/ and context-bootstrapping page directly, with attributed quotes).

**Collibra — Collibra AI (native) + Semantic Agents + Capgemini "Agentic Business Glossary Editor" (marketplace partner)**
- Native "Collibra AI for asset descriptions" covers (b) only, for column/table/dataset descriptions (not specifically jargon terms), always human-approved: *"Collibra AI helps you accelerate the creation of descriptions for your assets in Collibra... The AI provided descriptions are always considered suggestions."* [productresources.collibra.com/.../to_auto-descr.htm](https://productresources.collibra.com/docs/collibra/latest/Content/CollibraAI/to_auto-descr.htm) — **Confidence: HIGH** (read directly).
- "Semantic Model Generation Agent" (per search synthesis, primary blog page failed to render body text after two attempts due to safefetch stripping/JS issues) reads existing glossary + technical metadata to auto-generate a semantic layer with descriptions — **Confidence: MEDIUM** (secondary-source quote only).
- The Capgemini partner offering on Collibra Marketplace covers (a)+(b) directly and closely: *"The Agentic consists of an LLM and 5 AI Agents that identify CDEs from your system documentation, draft definitions, incorporate SME feedback, maps them to the data model...collect approvals and upload the definitions into Collibra where it also automatically hyperlinks the new entry to related pages."* Note this is a **third-party partner tool**, not native Collibra, and targets compliance-driven Critical Data Elements specifically, not general idiosyncratic team jargon. No (c). **Confidence: HIGH** (read marketplace listing directly).

**Microsoft Purview Unified Catalog — "Get suggested glossary terms" (private preview)**
Per Microsoft's own Responsible-AI FAQ page (opened directly): AI capabilities are described only at a high level — *"AI-assisted data product curation (preview)"* and glossary-term suggestion are named as in-scope but the FAQ gives no detection/matching mechanism detail, and access is restricted: *"This feature is currently only available to select early access customers"* (per a Microsoft Community forum reply). No evidence of (c). **Confidence: MEDIUM** (primary Microsoft page read directly, but it's a governance/responsible-AI overview, not a feature spec).

**Secoda** — per search-engine synthesis (I opened Secoda's static Glossary docs page directly, which describes only manual glossary CRUD; the AI-suggestion claims below come from a *different* Secoda docs page I did not independently open): *"Secoda AI identifies gaps in your glossary based on your data catalog and usage... pre-populates definitions to speed up knowledge standardization across teams."* Structurally per-team ("Each Team is able to have its own Glossary section"). Covers (a)+(b) if accurate; no (c) evidence. **Confidence: MEDIUM-LOW** (not independently verified from the primary AI-assistant doc page).

**Informatica CLAIRE**, **DvSum** — both reportedly auto-suggest/auto-generate glossary terms and definitions from technical metadata (per search-engine synthesis only; DvSum's tutorial URL returned 404 on direct fetch, Informatica pages not independently opened). Neither shows (c) evidence. **Confidence: LOW-MEDIUM**, un-verified by primary-source reading.

---

## 3. Knowledge-management / collaboration tools

**Confluence — Atlassian Intelligence "Define"** (GA, launched 2023) — the closest single artifact to (a)+(b) combined, with an explicit lazy/no-glossary framing.
[Official announcement](https://community.atlassian.com/forums/Confluence-articles/Introducing-Define-terms-using-Atlassian-Intelligence-in/ba-p/2556585) · [Comparison article](https://community.atlassian.com/forums/App-Central-articles/Glossary-vs-Confluence-AI-quot-Define-quot-What-s-the-Right/ba-p/3147189)
- Quote (official): *"it's now possible for you to define your company-specific terms, acronyms, project names, or statuses on a page in Confluence!"*
- Quote (mechanism): *"The AI instantly generates a definition by analyzing how that term is used across all the pages you have permission to see."*
- Quote (explicitly lazy/no-setup framing, matching Q4): *"For zero-effort setup: It's automatically enabled...No setup or maintenance is required, and it immediately starts learning from your existing content."* And on scope: *"Terms created with Atlassian Intelligence...don't have a dedicated glossary view."*
- **Does not cover (c)**: each "Define" is an isolated, ungoverned, non-persisted lookup — there's no structure matching one space's generated definition against another's.
- Confidence: **HIGH** (read both primary Atlassian community sources directly).

**Glosso** (third-party "Rovo Agent" marketplace app for Confluence, built by the same vendor as "Glossary for Confluence")
- Adds explicit (a): *"Glosso analyzes your Confluence page and suggests key terms based on usage and context. For each suggestion, it generates a draft definition along with relevant metadata such as synonyms, abbreviations, and labels."*
- Also does term-level duplicate avoidance (not cross-team definition-matching): *"If it isn't [already defined], Glosso drafts a definition...you can review and edit before adding it to your chosen glossary"* — checks are against **one shared glossary's existing terms**, not typed matching across independent per-team glossaries.
- Confidence: **HIGH** (read directly; one CRITICAL safefetch false-positive flag on ordinary prose, noted above).

**Slack — "AI in Slack: hover for meaning"** (announced July 2025 as "coming soon," per Slack's own blog; I could not verify current GA status as of today)
[Official Slack blog](https://slack.com/blog/news/ai-productivity-tools-slack)
- Quote: *"by simply hovering your cursor over any message, AI in Slack will provide an instant explanation on any message. It draws from your workspace's unique vocabulary and conversation history, giving you explanations for project names, internal tools, or team-specific shorthand."*
- Structurally scoped per-workspace, on-demand, no pre-built glossary — same lazy/per-team pattern as Confluence's Define. No (c) evidence.
- Confidence: **HIGH** for the announcement text itself; **MEDIUM** for current shipped status (dated to July 2025; not reconfirmed as GA a year later).

**Notion**: No auto-detect/auto-generate glossary feature found — only static, manually-authored Glossary templates. **Negative finding, HIGH confidence.**

**Glean**: No jargon-detection or per-org glossary-generation product feature found. Glean does publish its *own* static "AI Glossary" (marketing/educational content about AI terms), which is unrelated to auto-generating an organization's internal jargon. **Negative finding, HIGH confidence** — flagging explicitly since it's an easy false-positive to make from search snippets alone.

---

## Answering Q4 directly (vocabulary constraint / global-glossary framing)

None of the systems found constrain the definition to a controlled vocabulary — all use free-text LLM or NLP-generated prose. On the "avoids a global/central glossary" framing specifically, the field splits cleanly:
- **Explicitly centralizing** (opposite of the proposed system): Microsoft's 2004 "Centralized terminology" patent family, and Atlan's entire context-agent pitch ("One shared definition. Every agent.").
- **Explicitly lazy/no-glossary-required** (structurally aligned with the proposed system, but only for single-team/single-workspace definition generation, never cross-team matching): Confluence's "Define" and Slack's "hover for meaning."
- **Per-team but still converging to one canonical answer when conflicts arise**: Atlan's Sage, Secoda's per-team glossary sections.

No artifact combines "lazy per-team generation" with "typed same/broader/narrower/related relations across teams" as the proposed system does.

---

## Closest single artifact overall

**US8589791B2 / US10552522B2 (Microsoft, 2011–2020)** is the closest patent — it's the only prior-art document that explicitly frames the problem exactly as the proposed system does (different teams, different vocabularies, no single definition source) and auto-generates definitions in response. It falls short only on (c): it never compares one team's generated definition against another's.

**Confluence's "Define"** is the closest shipped product artifact for the (a)+(b) lazy/no-glossary mechanism, and **Atlan's Sage** is the closest for (c)-shaped conflict detection — but no single artifact does both.

## What I did NOT search

- Non-Google-Patents patent search surfaces (WIPO PatentScope, Espacenet advanced search, USPTO Patent Public Search) with native CPC/classification-based querying — I relied on Google-indexed web search as a proxy, which under-indexes patents with sparse metadata or non-English text.
- "Cited by" / "similar documents" citation graphs on the patents found, which could surface adjacent prior art.
- Additional data-catalog vendors: Ataccama, Talend/Qlik, IBM Watson Knowledge Catalog, AWS Glue/DataZone, Google Dataplex, Snowflake Horizon, Databricks Unity Catalog.
- Additional KM/collaboration tools: Guru, Slite, Coda, Microsoft SharePoint/Loop, Stack Overflow for Teams, Bloomfire.
- Re-confirmation of current (2026-07-17) shipped/GA status for Slack's "hover for meaning" and Microsoft Purview's private-preview glossary-suggestion feature (both were "preview"/"coming soon" as of their announcement dates).
- Academic literature (explicitly out of scope per your framing — already covered in a prior pass).

## Query ledger (verbatim, in order)

1. `patent automatic glossary generation jargon detection organization documents`
2. `patent "business glossary" automatic construction machine learning site:patents.google.com`
3. `site:patents.google.com Collibra glossary data catalog`
4. `site:patents.google.com Alation data catalog patent`
5. `patent "duplicate concept" OR "duplicate term" detection business glossary data catalog assignee`
6. `patent "jargon" detection natural language processing enterprise document assignee`
7. `patent "novel term" detection organization corpus generate definition large language model glossary 2023`
8. `patent matching concepts across documents using generated definitions description similarity entity resolution`
9. `patent "concept" matching "definition" generated across "teams" OR "departments" ontology alignment ambiguous terminology`
10. `patent "term extraction" "definition generation" enterprise knowledge graph 2021 2022 2023 assignee IBM Microsoft SAP`
11. `Collibra AI generated glossary definitions LLM "term" auto-detect documentation`
12. `Atlan AI glossary generation "auto-generate" business terms documentation`
13. `Microsoft Purview AI generated glossary term description "generate" documentation`
14. `Secoda AI glossary "auto-generate" descriptions business terms`
15. `Atlan Lexis "Glossary Bootstrapping" context agent business glossary`
16. `Atlan "Sage" agent "Metric Conflicts" "certified answer" two teams define metric differently`
17. `"atlan.com" Sage agent metric conflicts page url`
18. `US20250139088A1 Alation abstract "large language model" data catalog patent`
19. `Notion AI glossary "auto-detect" jargon terms wiki feature`
20. `Confluence Atlassian "glossary" auto-generate terms AI feature jargon`
21. `Glean AI enterprise search glossary jargon term definitions company-specific`
22. `patent OR product "same underlying concept" different terms "generated definition" embedding match cross-team taxonomy`
23. `"broader than" "narrower than" "related to" typed relation business glossary term matching cross corpus patent`
24. `"Automatic taxonomy mapping using sequence semantic embedding" patent number google patents`
25. `patent 2024 2025 "detecting" "new term" OR "neologism" organization document generate definition match across teams knowledge graph assignee`
26. `Informatica CLAIRE AI glossary auto-generate business term definitions data catalog`
27. `dvsum automatic business glossary generation ML data catalog`
28. `Slack AI glossary jargon detection auto-define terms feature workspace`
