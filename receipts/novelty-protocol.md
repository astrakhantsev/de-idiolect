---
title: "Novelty protocol — defeating the idiolect trap"
kind: reference
scope: cross-cutting; applies to all research work, any agent
created: 2026-07-16
revised: 2026-07-16 (major revision after Codex review — see §Revision note)
status: "active — §\"What the phenomenon is called\" verified against primary text 2026-07-16. Owners, oldest first: Blair & Maron 1985 (believed 75%, got 20%; names the confidence mechanism) · Larsen & Bong 2016 (coined-name→failed-search→reinvention, measured 9%/3%). Patent leg run 2026-07-16: both halves measured (Magdy 12% zero-overlap; Yelderman 89% miss), causal join unowned, and the outcome-owning literature reaches for examiner myopia (Cotropia et al.) rather than wording without testing wording — a novelty claim here must beat myopia, not fill an empty cell. Clear Blair & Maron and Larsen & Bong by name and number before any novelty claim. Swanson 1986 still unverified (and there are two of them)."
source: 20_areas/thinking/decisions/2026-07-16-flf-no-submit-judge-dependence-prior-art.md · 10_projects/minelit/judge-dependence/lit/2026-07-16-prior-art-position-sweep.md · memory `feedback_search_field_vocabulary`
applies_to: any research programme, public artifact, grant/competition entry, or "is this novel?" question
---

# Novelty protocol — defeating the idiolect trap

**The one-line rule:** a search runs on *words*. Words invented inside a project return nothing, and "no prior art found" then gets read as "unoccupied" when it means **"not findable from here."** Establish the novelty position **before** the programme, **in the field's vocabulary**, via a **blind-briefed** refuter — then verify the kills against primary text, because a false kill costs as much as a false null.

## Why this exists — the receipts

**The three trials.** The denominator is **three novelty-check episodes** on the minelit judge-dependence programme (2026-06 → 07). Selection rule: every occasion on which the programme asked "is this novel?" These are all of them, not a selected subset.

| # | episode | what it concluded | what actually happened |
|---|---|---|---|
| 1 | **2026-06-29** — 9-agent same-model fan-out | "**No prior art found** doing the full target; 6/6 CLOSE-BUT-GAP" | Confident null. Overturned later. |
| 2 | **2026-07-13** — refuter across different literatures | `m*` is novel | **Killed in ~5 minutes** by Clemen & Winkler (1985) |
| 3 | **2026-07-16** — 4 disjoint-literature agents + refuter | the replacement direction is novel | **Killed.** Keystone foreclosed by Bröcker (2008) |

**3-for-3: every episode searched in the project's own vocabulary and returned a confident null that did not survive.** Cost: six weeks, ~7,000 primary calls, and the runway a better direction needed.

**Corroborating observations** (mappings *within* those three episodes — **not** eight independent replications):

| our word | the field's word | the owner | status |
|---|---|---|---|
| "the signal, not the cut, is the bottleneck" | sufficiency ordering + proper-score decomposition | **Bröcker (2008)**, arXiv:0806.0813 §3 p.8 | **PRIMARY VERIFIED** — foreclosed *for the exact claim*, see §6 |
| `m*` (per-question critical count) | equivalent number of independent sources | Clemen & Winkler (1985) | UNVERIFIED against primary text |
| "operating requirement" | Value of Information / preposterior analysis | Schlaifer & Raiffa (1961) | UNVERIFIED |
| "gate" / "threshold over credences" | policy consistency | RiskEval (2601.07767) | UNVERIFIED |
| "coverage" / "the answer is in the set" | prediction sets · generation-verification gap | Li (2603.22966) · Weaver (2506.18203) | UNVERIFIED |
| "family credence expression" | verbal-confidence validity | Zhou (ACL 2024), 9 models / 125,244 queries | quote verified in the decision doc |
| ~~"family credence expression" → Rasch null categories~~ | ~~Wilson & Masters (1991)~~ | — | **❌ WITHDRAWN — DEFECTIVE.** Quotes were real but came from a **software help manual**, not the *Psychometrika* paper they were attributed to; the truncation cut immediately before *"All its infinitude of thresholds are estimable because they are asserted to have a specific form"* — which **contradicts** the unidentifiability gloss it was used for. |
| "read the enumerations, not the votes" | reasons- vs statistical-feedback | Rowe & Wright (1996/99) | **PRIOR ART STANDS** (head-to-head comparison run in 1996; reasons won *in that study*). **But NOT "settled positively"** — one study, plus Best (1974) at **1/2 items**, on a feedback form the authors call rare, with the authors **explicitly declining** the strong claim. |
| "evidence stripping" | decontextualization | Choi (TACL 2021) | UNVERIFIED |
| "S-arm" / emitted-set union over judges (the *mechanics* of "read the enumerations") | class set reduction (union method); set-level multiple-classifier combination | **Ho, Hull & Srihari 1994**, *IEEE TPAMI* 16(1):66–75 | **PRIMARY VERIFIED 2026-07-17** (full read). Owns the pool-candidate-sets-by-union + decide-downstream architecture; does NOT cover the elicitation contract (declared defensible-readings sets, no training data) or the correlated-error-in-what-sources-offer diagnosis. Found by the definition-mediated blind naming experiment (`idiolect/2026-07-16-definition-mediated-naming-EXPERIMENT.md` §7.5) — two blind draws named it; three prior human-audited passes had not. Note the Rowe & Wright row above covers the *feedback-format* reading of the same coinage, not these mechanics — one coinage, two distinct field owners. |

**Two lessons from that table, both load-bearing:**
1. **The knowledge was in the weights the whole time.** A correctly-briefed refuter found Clemen & Winkler in five minutes. This is a **workflow bug, not a capability ceiling**.
2. **Every kill that was checked had a real quote and a defective citation** (2-for-2; Bröcker was the exception that held). **Subagents get the *idea* right and the *provenance* wrong** — wrong venue, dropped qualifiers, truncation exactly where the source turns against the claim. Hence §8.

## The mechanism — why agents make it worse

1. **Naming is cheap and happens early.** Coining crisp project-local terms aids internal communication, and crispness feels like understanding. By definition the coinage diverges from the field's name — if you knew the field's name, you would have used it.
2. **The idiolect colonizes every artifact** — state docs, digests, prompts. Then: **every agent spawned from those artifacts is socialized into the idiolect at spawn time.** A human collaborator brings their own vocabulary and asks "isn't this just Murphy decomposition?" — the fresh-eyes function. An agent's entire worldview arrives via your prompt. **The onboarding context that makes agents useful is what destroys their independence for novelty checks.**
3. **Shared context is a hidden correlator** stacked on shared training corpus. N agents briefed from the same docs are one searcher with variance. (`feedback_fanout_agreement_not_independence`.) Demonstrated live on 2026-07-16: agents 1–3, all searching post-2023 arXiv in overlapping vocabulary, **converged** on "the identifiability framing survives" — and the convergence was worth nothing, because a refuter tasked to hunt pre-LLM literature killed their survivor. (The *specific* 1991 citation that refuter used later proved defective — see the withdrawn row above — which only sharpens the point: convergence was worthless **and** the thing that broke it needed verifying too.)
4. **Models mirror your ontology rather than correct it.** Nothing in the interaction rewards an agent for volunteering the field's name unprompted. Sycophancy at the ontology level.
5. **Novelty is an absence claim** — exactly where convergence is worth nothing. So the null comes back **confident**.

## When this fires

Any of: a novelty or "is this new?" claim · entering a research programme or direction · a grant/competition entry · a public artifact asserting a contribution · coining a term for a phenomenon you intend to build on.

## The protocol

### 1. Coin-time tax — pay it the moment you mint a word

Every project-local term gets a row in **`<project>/glossary.md`** (canonical location; create on first coinage), written when the term is minted:

| our term | candidate field term(s) | owner / citation | verification | status / next action |
|---|---|---|---|---|

An empty `owner` column is **an open ticket, not evidence of novelty** — set `status: UNRESOLVED — needs blind naming pass` and put it in the project's README next-actions. Standing instruction to agents: *propose the nearest established field terms unprompted whenever a project-local term appears.*

### 2. Two frozen passes — never one

The blind pass and the verification pass are **separate, in this order, and must not be merged.** Merging them is how a "blind" check silently inherits the ontology it was supposed to test.

- **Pass A — blind naming/refutation.** The agent gets **only** the phenomenon restated in plain mathematical/operational language. **No project docs, no project vocabulary, no candidate terms, no prior conclusions, no preferred fields.** Ask it to name the concept and its owners cold. Freeze and archive this brief verbatim — it is the evidence that the pass was blind.
- **Pass B — verification and citation-walk.** *This* pass may receive Pass A's candidates, prior sweeps, and adjacent papers, and is tasked to verify against primary text and to citation-walk backward.

**A prompt that hands over candidate owners and prior conclusions is a Pass B prompt, whatever it is labelled.** It cannot demonstrate blindness, and it recreates the correlated-context problem one stage later.

#### ⚠ Blindness is a TOOL-LEVEL control, not a prompt-level one (measured 2026-07-16)

**Controlling the brief and the working directory is NOT sufficient, and believing it is has already produced one false attestation.** `~/.claude/CLAUDE.md` is a **user-level** file: it loads in *every* session regardless of cwd, and its first directive is *"At session start, read `/mnt/f/hub/_dashboard.md`."* A headless "blind" run obeyed it, read the dashboard — **which contains this project's own prior-art candidate list** (`stemmatics / Leinster–Cobbold / design-effect`; `Broomell-Budescu 2009, Lorenz PNAS 2011`; `Clemen & Winkler 1985`) — and returned five of those names, three of them in its *"from knowledge, before searching"* section. **That is reading, relabeled as recall.** It was caught only because the run helpfully reported an overdue reminder back to the orchestrator.

**The required launch shape for any Pass A run:**

```bash
claude -p --model <m> \
  --allowedTools "WebSearch,Bash(safefetch:*)" \
  --disallowedTools "Read,Glob,Grep,Task,Agent,Edit,Write" \
  < frozen-brief.md
```

- **`Read,Glob,Grep` denied** — the run *cannot* open the dashboard or any vault file even when its own config orders it to. This is the control that matters.
- **`Task,Agent` denied** — `claude -p` is one-shot; a run that delegates to a background fan-out returns a *status message* and dies with its children (observed: one run emitted only *"The deep-research workflow is running in the background…"*, hit a 600 s ceiling, produced nothing). **A fluent report of work not done is the same failure class as an unread PDF.**
- **Mandatory audit after every run:** grep the output against the dashboard's and project's candidate terms. If they appear, the draw is **invalid** — its verification work may survive; its recall section may not.
- **Never certify blindness from the brief alone.** The brief being clean is necessary and not sufficient. Attest at the *session* level or not at all.

#### The disjointness result — why 3 cross-model draws, not 5 same-briefed agents (measured 2026-07-16)

Three clean draws (opus / sonnet / default) on an *identical* frozen brief returned **near-disjoint bibliographies**: one found Blair & Maron 1985 + Knight & Leveson 1986 + TAR certification + CAPA + CiteME; one found climate science's effective-model-count + Dickersin 1994 + Spoor 1996; one found TREC pooling + the Idea Novelty Checker + Cutter 1876. **Overlap was thematic, not bibliographic.**

Consequences, both load-bearing:
- **The union is the payload; the agreement count is noise.** Pass B's five same-briefed agents produced *one* union. Three blind cross-model draws produced three.
- **A single draw's null is worthless, and so is a single draw's hit.** The one *correct* pre-registered prediction that session (reliability engineering as the general antecedent → Knight & Leveson) was found by **1 of 3** draws. Running only the other two would have scored a right prediction as wrong.
- **Pre-register predictions before any run returns.** 4 of 5 were wrong or mis-scoped; the blind draws beat the orchestrator's socialized priors. Sealed predictions are what makes that visible instead of retrofittable.

### 3. Reverse the question (Pass A's framing)

Not *"search for prior art on X"* — that returns comfortable nulls. Instead: **"What is this called? In which fields does it live? Who owns it? Name the oldest treatments you would expect to exist."** This forces **positive, checkable claims** where a null cannot hide, and elicits from weights before touching the web.

### 4. Citation-walk backward; force an old leg

**Date rule: at least one source published before 2015, with no lower bound.** (Kelley 1927 and Blackwell 1953 both matter here; a "1950–2015 window" would wrongly exclude the former.) Old literature is reached by **graph-walking from a hit**, not keyword search — modern surfaces bury it. Every minelit scoop was pre-LLM: 1961, 1985, 2008, plus 1953/1973/1974/2001 in the 07-16 sweep.

### 5. The does-it-need-LLMs test — a prior, not an exemption

**If the claim can be stated without mentioning LLMs, expect a pre-2015 owner.** Generality equals age: a threshold on a score, information garbling, expert aggregation, correlated evidence — all owned decades ago.

**This never exempts anything from searching.** LLM-specific work (e.g. verifier-strength × extraction-richness interactions) is *relatively* more protected, but it must **still be searched for general antecedents** — the general form of an LLM-specific manipulation is usually the thing that owns it. Treating "it's LLM-specific" as a pass is how you build the next blind spot.

### 6. Classify the claim — and attach foreclosure to an *exact* claim

**Per claim or delta**, record `novelty_status: open | predated | foreclosed`. (`open` is a status, **not** a kind of kill — do not collapse them.) Then record a **separate, programme-level go/no-go**; a mixed programme must not be flattened into one verdict.

- **Predated** — someone got there first. Extension, measurement, or a new regime remains possible.
- **Foreclosed** — a theorem or definition settles **the exact claim, under stated assumptions**. Record both: *which* claim, and *which* assumptions.

**Foreclosure is narrow, and over-reading it is its own failure.** Bröcker (2008) forecloses "the signal, not the cut, is the bottleneck" **only for strictly proper scoring rules** — which is also why our Youden's-J analysis fell outside the theorem's scope entirely. A theorem killing a theoretical claim does **not** foreclose empirical validation, measurement in a new regime, boundary-condition tests, replication, or application. The 07-16 decision itself, having declared the keystone foreclosed, still identified a genuinely unrun manipulation. **Distinguish theoretical novelty from empirical/measurement/application/boundary novelty and classify each separately.**

### 7. Do not price novelty against the reviewer you expect

A domain expert reaches the scoop in seconds even when a reviewer from your own field never would. "An NLP reviewer wouldn't know Bröcker" is not a defense — a forecasting expert cites it first and the claim dies in the exchange.

### 8. Verify the kills — the mirror failure

**Measured 2-for-2 on this programme: every kill that was checked had a real quote and a defective citation.** A false kill costs as much as a false null. `feedback_verify_citations_primary_text` applies symmetrically:

- Read the load-bearing citation's **primary text yourself**. Check the **venue** actually matches (the withdrawn Wilson row was a software manual dressed as *Psychometrika*).
- **Read past the ellipsis.** Truncation lands exactly where the source turns against the claim.
- **Check for the authors' own hedges** before reporting a result as settled (Rowe & Wright disowned the strong reading their quotes were used for).
- Conflicting IDs for one paper across agents = **hallucination signature**; report the conflict, don't pick one.
- A small model's "NOT FOUND" on a math PDF is **worth nothing** — it returned false negatives on all three real Bröcker quotes.
- **★ A snippet that states your conclusion in perfect words is a fabrication signal, not a find.** Measured **2-for-2 in the 07-16 patent sweep**: a search engine attributed to gwern's "Internet Search Tips" a near-perfect statement of the loop's search half — **not on the page** (grep returned zero); and attributed *"patent applicants use vague and abstract terms…"* to Lupu & Hanbury 2013 — the 99-page survey has **zero** occurrences of "vague"/"obfuscat"/"intentional." Both read as exactly what the searcher hoped for; both were inventions. **When a quote lands too cleanly on your thesis, that is the moment to open the primary, not to celebrate.**

**Getting the primary when it's blocked — the retrieval toolkit (measured 4-for-4 on the 07-16 sweep).** §8 mandates reading the load-bearing primary; the usual objection is "it's paywalled." It almost never actually is. In priority order:

- **An aggregator's "closed / not open access" is NOT evidence of absence.** OpenAlex and Semantic Scholar both reported **Larsen & Bong 2016 CLOSED** — it was freely archived; Unpaywall reported **Alcácer & Gittelman 2006** as `oa_status: closed, oa_locations: []` — a live green copy existed. Two aggregators, two wrong "closed"s, one session. Treat their negative as unchecked.
- **The Wayback CDX index of the authors' OWN uploads is the best route.** `safefetch "http://web.archive.org/cdx/search/cdx?url=<host/path>*&output=text&fl=original,timestamp,statuscode,mimetype&limit=40"`, then fetch the original bytes via `https://web.archive.org/web/<timestamp>id_/<original-url>`. ResearchGate/academia/SSRN uploads are frequently archived there even when the live host is Cloudflare-walled. **This is how both Larsen & Bong (author's RG upload) and Alcácer (a now-dead host's green copy) were finally read.**
- **A repository's "full text" link can be a cover sheet.** UNIMAS's advertised full text of Larsen & Bong was a **2-page** ResearchGate cover sheet + p.529 — which is why every route "almost" worked. **Check the page count before believing you have the paper.**
- **Crossref exposes direct publisher PDF paths** search engines don't surface: `https://api.crossref.org/works?query.bibliographic=...&rows=3&mailto=<you>`.
- **Fetch mechanics:** `safefetch`'s renderer refuses raw PDFs; use `wget` + `pdftotext -layout` (write the script and run via `saferun -f` — a compound `wget && pdftotext` line is denied). `r.jina.ai/<url>` extracts some PDFs the renderer won't, but blocks `web.archive.org`. **The PDF's internal metadata title can confirm provenance** — Larsen & Bong's read `Round 5. INN Synonymy 20151217_Accepted`, i.e. the accepted manuscript.
- **Scanned/typeset article PDFs often have a near-empty text layer** (the UNIMAS cover sheet extracted to 6k chars of nothing). A `pdftotext` "not found" on such a file is a false negative — read the pages visually with the Read tool's `pages` before concluding anything is absent.

## The novelty position — a pre-registration sibling

Written **before** the programme, at **`<project>/novelty-position.md`**, gating entry. Same status as a pre-registration: if it is not written, the programme has not started.

```markdown
---
status: draft | survived | predated | foreclosed | killed
owner: <who ran it>
date: <when>
---
## Novelty position — <direction>

- **The claim, in the field's vocabulary:** <exact claim; no project-local terms permitted>
- **Fields it plausibly lives in:** <2-3 neighbouring — statistics, psychometrics, forecasting,
  epistemology, IR, decision theory...>

### Search ledger (auditable — a position without this is not a position)
- **Pass A blind brief (verbatim):** <the exact text the blind agent received>
- **Canonical terms tried:** <list>          - **Databases/venues searched:** <list>
- **Citation-walk path:** <hit -> its references -> ...>
- **Pre-2015 source found:** <citation, or "none — RED FLAG, not a green light">
- **Coverage limits / what was NOT searched:** <honest gaps>
- **Stop rule:** <what would have made you keep searching>

### Findings (one row per claim — never one verdict for the programme)
| claim / delta | nearest neighbour (cited) | novelty_status | verification | if foreclosed: exact claim + assumptions |
|---|---|---|---|---|

- **Does-it-need-LLMs:** yes / no  (if no -> expect an owner; search general antecedents anyway)
- **Pass B verification:** <who, when, which citations read in primary text>
- **Programme-level go/no-go:** <separate decision, with reasons>
```

**The cost asymmetry is the entire argument:** the refuter takes minutes; the programme it can kill takes weeks. There is no version of this that is not worth running.

## What the phenomenon is called

> **✅ VERIFICATION RAN 2026-07-16.** The prompt this section was waiting on has been executed — 5 blind-briefed agents, primary-text verification, results at `10_projects/minelit/idiolect/2026-07-16-targeted-prior-art-search-RESULTS.md` (Codex-reviewed → MAJOR REVISION → repaired; read its Review note before citing anything). **Three of the four anchors below now hold against primary text, with corrections. Two carried errors that this section had already propagated.** Remaining unverified items are marked inline and must not be cited publicly. The sweep also produced **its own instance of the trap**: a search engine attributed to gwern a near-perfect statement of the phenomenon that does not exist on the page — caught only by fetching the primary.

> **✅ SECOND VERIFICATION RAN 2026-07-16 (blind machinery pass).** Three genuinely blind cross-model draws (`--disallowedTools "Read,Glob,Grep,Task,Agent"`), results at `10_projects/minelit/idiolect/2026-07-16-machinery-blind-PASS-A-RESULTS.md`. **It found an owner older and more complete than everything below** — see the next entry. A fourth run was **invalidated for reading the vault dashboard**; that failure is why §2 now specifies tool-level denial.

- **★★ THE OLDEST AND MOST COMPLETE OWNER — Blair & Maron (1985), *CACM* 28(3):289–299**, "An Evaluation of Retrieval Effectiveness for a Full-Text Document-Retrieval System." **VERIFIED (`primary-full`) — PDF downloaded and grepped directly by the orchestrator 2026-07-16** (safefetch returned an empty DOM; `curl` + `pdftotext`, 11pp). **This owns the entire composite, two years before Furnas, and owns more of it than Furnas does.**
  - **The belief/reality gap, measured:** lawyers on a litigation-support corpus *"stipulated that they must be able to retrieve at least 75 percent of all the documents relevant to a given request"*, and measurement began only once *"the lawyer stated in writing that he or she was satisfied with the search results for that particular query."* **They believed 75%. They were retrieving ~20%.**
  - **★ The confidence mechanism — why a clean search feels conclusive, stated outright:** *"they will have seen only the retrieved set of documents and not the total corpus of relevant documents; that is, they have seen that the proportion of relevant documents in the retrieved set (i.e., Precision) is quite good (around 80 percent)."* **You can observe your precision. You cannot observe your recall. So a clean, high-precision search reads as thorough.** This is the null→confidence step with a mechanism, in 1985.
  - **★ The vocabulary chain, verbatim:** the same subject called *"the 'wire warp'"*, then *"a third and novel way: the 'shunt correction system'"*, then *"the 'Roman circle method'"*, then — *"all documents germane to those tests referred to the system as the **'air truck.'** At this point the search ended, **having consumed over an entire 40-hour week of on-line searching, but there is no reason to believe that we had reached the end of the trail; we simply ran out of time.**"*
  - **The general statement:** *"Stated succinctly, it is **impossibly difficult for users to predict the exact words, word combinations, and phrases that are used by all (or most) relevant documents and only (or primarily) by those documents**."* Scale: one request's 3 key terms grew by *"26 other words and phrases"*; another's 4 terms by *"44 additional terms."*
  - **Why it matters more than Furnas:** Furnas measures **naming variance** (people pick different words). Blair & Maron measure the **downstream epistemic failure** — searchers' *false confidence about their own coverage* — and name the reason it is invisible from inside. **"We simply ran out of time"** is Martyn's 1964 iceberg, independently.
  - **Eleven agents across three passes never reached this paper.** It is not obscure; it is one of the most cited papers in IR. It was unreachable from the project's vocabulary.
- **The vocabulary problem** — Furnas, Landauer, Gomez & Dumais (1987, *CACM* 30(11):964–971). **VERIFIED (`primary-full`).** The real numbers, from Table I ("probability of two people applying the same term to an object"): **.07 to .18** across six tasks — the paper's own abstract says *"In every case two people favored the same term with probability <0.20,"* and its consequence sentence is *"If one person assigns the name of an item, other untutored people will fail to access it on 80 to 90 percent of their attempts."* So the <20% figure survives contact with the primary.
  - **⚠ But know the base before leaning on it.** What was measured is **untrained people spontaneously naming everyday objects and operations**: main verbs from 48 typists describing text-editing, first content word for 50 common objects from 337 college students, superordinate categories for classified ads from 30 New Jersey homemakers, recipe keywords from 8 cooks. **It is not experts naming research constructs.** The figure transfers to the idiolect trap **by analogy, not by measurement** — which means this section's original reframe ("vocabulary divergence is the *base rate of human naming*… that turns the protocol from 'remember to be careful' into 'correct for a known base rate'") **is not underwritten by Furnas**. There is no measured base rate for expert coinage. Keep the weaker, supportable claim: **naming divergence is the documented default in every population anyone has measured, so an unexplained vocabulary match is the surprise, not a mismatch** — and treat the specific number as suggestive of magnitude, not as a rate to correct by. (An expert-coinage base rate would be a genuinely open measurement — see the empty cell in RESULTS §3b.)
- **The jangle fallacy** — **Kelley (1927), VERIFIED (`primary-full`, pp. 63–64)**: *"the use of two separate words or expressions covering in fact the same basic situation, but sounding different, as though they were in truth different. The doing of this latter the writer will call the 'jangle' fallacy."* Jangle — assuming two things differ because they are named differently — is the half that matters here, and it is Kelley's.
  - **⚠ Attribution corrected.** **Kelley coins only *jangle*.** *Jingle* is **Thorndike (1904, p. 14) quoting Aikins** — Kelley says so explicitly on the same page: *"Dr. Thorndike quotes Professor Aikins as describing this as the 'jingle' fallacy."* The prior "Kelley 1927 (jingle-jangle)" compression got the attribution wrong. Cite **Thorndike 1904 for jingle, Kelley 1927 for jangle**. Independently confirmed from Larsen & Bong's own primary text, which splits the attribution the same way: *"jingle (Thorndike 1904) and jangle (Kelley 1927) fallacies."*
- **★ THE CLOSEST OWNER — read the body before claiming anything is new here** — **Larsen & Bong (2016), *MIS Quarterly* 40(3):529–551. VERIFIED (`primary-full`, authors' accepted manuscript)**, obtained 2026-07-16 from the Wayback capture of their own ResearchGate upload (every other route was a near-miss: OpenAlex and Semantic Scholar both report it CLOSED — **both wrong**; the UNIMAS repository's advertised "full text" is a **2-page cover sheet**). They name the **construct identity fallacy (CIF)** and own the causal chain this protocol exists to prevent, **ten years before the AI framing and with an empirical measurement no 2023–2026 AI paper matches**:
  - **Coined name → failed search → incomplete review**, under their own heading *"Consequences of the Construct Identity Fallacy"*: *"When researchers search for a construct in an online repository of journal articles, the name of that construct can neither be trusted to elicit high recall (a consequence of jangle) nor high precision (a consequence of jingle). An incomplete understanding of the many names for a construct will lead to literature searches that are incomplete."*
  - **→ perceived novelty → reinvention:** *"The renaming of an existing construct (jangle fallacy) may increase the perceived novelty of a construct"*; and quoting Wilhelm (2009, p. 146): *"If you commit a jangle fallacy your work is akin to the reinvention of the wheel."*
  - **Measured:** *"participants could detect relevant articles containing a specific construct on average only 9% of the time, and relevant articles containing a pair of common constructs on average only 3% of the time"* — motivated PhD students, full-text search, two-journal corpus. And: *"the experiment only scratches the surface of how incredibly difficult it is to find existing research in an environment plagued by the CIF."*
  - **The sharpest line, extending Swanson:** *"While Swanson addressed undiscovered knowledge, we found the vast majority of discovered knowledge is hidden from the individual researcher by the very nature of the search process itself."*
  - **What is left unclaimed — and it is narrower than it first looked.** A second review caught that "the null-as-evidence step is unclaimed" contradicts the sweep's own citation of Shahid et al. (arXiv:2506.22026), which quotes AI Scientist's *"If such a decision is not reached, the idea is automatically considered novel"* — an **implemented** null→novel mapping. So:
    - **N1 — operational null/undecided → "novel" in a deployed system: `predated` (closed). Do not claim it.**
    - **N2 — explicit diagnosis of null-as-evidence as an epistemic failure *with a named cause*: open** (arXiv:2604.20622 names the outcome, no cause; 2506.22026 shows the behavior, no diagnosis). Narrow strip.
    - **N3 — the self-referential case: a project's own coinage blinding its own novelty check: open.**
    - **N4 — agent socialization: searchers briefed into the idiolect at spawn time inherit the blind spot: open.**
  - **Wording discipline:** describe L&B as **"construct renaming / name divergence,"** never "coined vocabulary" — the loose phrasing erases the self-reference distinction that N3 rests on.
  - **Operational rule: any novelty claim in this space must clear Larsen & Bong 2016 explicitly, by name and by number, AND state which of N2/N3/N4 it is claiming.** Their 9% is the number to beat or cite.
  - **⚠ Two Swanson 1986 papers exist and this document cites the other one.** L&B cite *"Fish oil, Raynaud's syndrome, and undiscovered public knowledge," Perspectives in Biology and Medicine* 30(1):7–18; the entry below cites *The Library Quarterly* 56(2):103–118. Both are real. **Always say which.**
- **Undiscovered public knowledge / literature-based discovery** — Swanson (1986, *The Library Quarterly* 56(2):103–118). Two public literatures that never cite each other jointly hold a discovery neither can see. **STILL UNVERIFIED (`snippet-only`)** — UChicago Cloudflare-blocked, JSTOR paywalled. Do not cite publicly.
- **"Applicant as own lexicographer"** — patent practice (MPEP 2173.05(a)). **VERIFIED (`primary-full`, uspto.gov)**, verbatim: *"a patentee or applicant is free to be his or her own lexicographer… may use terms in a manner contrary to or inconsistent with one or more of their ordinary meanings if the written description clearly redefines the terms."* And §2173.05(a)(I): *"Applicants need not confine themselves to the terminology used in the prior art."*
  - **⚠ The countermeasure claim overstated the record — softened.** "CPC/IPC classification codes indexing by function and structure **rather than** words" is **not** the official position. Verified: IPC is *"a hierarchical system of language independent symbols"* (WIPO), the *Guide to the IPC (2025)* ¶¶85–86 does define **function-oriented places**, and the USPTO's 7-step strategy is classification-driven at steps 2–6. **But** the same USPTO guide has examiners **supplementing** classification with keywords — *"U.S. patent examiners regularly supplement their classification searches with keyword searches"* — because *"a keyword search may simply turn up documents that were not well classified."* So professional practice is **classification plus keywords, not instead of them**, and "countermeasure to vocabulary variance" is **our inference, not any document's wording**. The supportable version: **vocabulary-independent indexing exists, is primary in professional search, and is still not trusted alone** — which is the same lesson as the retrieval caveat below, and a reason to keep §2–§3's hand-approximation *plus* the blind refuter rather than either alone.
- **★ THE PATENT LEG — run 2026-07-16 (3 blind agents + 3 primaries read by the orchestrator). Full data in RESULTS §3e.** This was the last-named unsearched literature behind the "nobody measures this" null, and it is the domain that *should* own the phenomenon: prior-art search is **professional, adversarial and legally consequential**, applicants **coin vocabulary by legal right**, and the misses get **denominated after the fact by someone paying to find them**. Verdict: **both halves are measured; the edge between them has never been drawn; and the one team that owns the outcome data considered wording and picked a different explanation.**
  - **The lexical floor, measured** — Magdy, Leveling & Jones (CLEF-IP 2009). **VERIFIED (`primary-full`, read directly).** *"surprisingly, 12% of the relevant documents for topics have no shared words in any field with the topics"* — base: 500-topic training set, stemmed, stop-words removed, "All Fields". **12% of known prior art is invisible to word-matching by construction.** Sharper still, and never propagated by the literature: *"the cosine measure between the top ranked non-relevant documents to the topic is nearly twice as high as for the relevant documents for all fields"* — **wording doesn't just fail, it points the ranker at the wrong documents.**
  - **The miss rate, denominated** — Yelderman (2019), *Iowa L. Rev.* 104:2705. **VERIFIED (`primary-full`, read directly).** *"89% of IPR invalidations relied on one or more references that were missing from the examination record"*, and ~74% of it sat in ordinary US patents/applications/books/journals. **⚠ Base is doubly selected** (challenged **and** invalidated, after an adversary spent ~$324k) — it is **conditional on invalidation, not an examiner miss rate**, and *Yelderman disclaims it himself*: *"none of this data should be used to fault line examiners… [it] does not tell us anything about the examiner error rate."* He attributes misses to **scope and cost, never wording.**
  - **Examiner-reported difficulty, federal, with CIs** — GAO-16-478SP (2016), q79c "Non-standard use of terms of art": **81.0%** say it makes a thorough prior-art search Much (32.3%) or Somewhat (48.7%) More Difficult; 76% want synonym/concept search. **`primary-full`.** **The strongest terminology number in existence — and it measures *reported difficulty*, not a miss rate.** GAO reaches only the modal *"may lead examiners to miss relevant prior art"* and **explicitly declines to count.**
  - **★ A well-evidenced COMPETING cause — the most decision-relevant thing the leg produced.** Cotropia, Lemley & Sampat (2013 WP, `primary-full`) own the outcome data and explain missed/unused prior art by **examiner myopia** — *"examiners tend to focus on references that they themselves identify"* — after rejecting a *claim-drafting* hypothesis: *"This is not simply because the applicants have 'drafted around' the art they submitted."* **⚠ Do NOT read this as "evidence against the vocabulary mechanism" (an earlier draft did — corrected 2026-07-17):** Cotropia never tests whether divergent *wording* hides prior art from a searcher; they test claim-drafting strategy and examiner citation-*use*. So this is a **rival explanation occupying the same outcome**, not a refutation — and it stands alongside Magdy's 12% zero-overlap, which is direct evidence the vocabulary gap is real. **The operational consequence: a novelty claim that "wording drives missed prior art" must now out-argue examiner myopia, not merely fill an empty cell.**
  - **★ The field's own name is 48 years old: "free text vs controlled vocabulary"** — Henzler 1978, Calkins 1980, Dubois 1987, Muddamalle 1998, Nijhof 2007 (all `secondary-only`, unread). **Reached only by citation-walking Adams (2010)'s reference list via Crossref — invisible to plain-English search.** The protocol's own §"force a pre-2015 leg, citation-walk backward" is what produced it.
  - **★★ The denominator trap — a worked example of "a number without its base is not a finding," inside ONE paper.** Alcácer & Gittelman (2006), *REStat* 88(4):774–779. **VERIFIED (`primary-full`, read directly).** Abstract: *"two-thirds of citations on the average patent are inserted by examiners."* Body, one sentence later: *"examiners account for some 40% of all citing-cited dyads; on the average patent, 63%."* **The headline 63% is a patent-level mean** (inflated by the 40% of patents where examiners add everything); **pooled, examiners supply only 40% of dyads — applicants supply ~60%.** Anyone reading "examiners add two-thirds of citations" as "applicants fail to find two-thirds of the art" **has silently swapped the denominator, and the paper hands you both numbers without flagging the switch.** The "two-thirds" is *not* a fabrication — it is the real abstract — but it must never carry an applicant-search-failure claim.
  - **Every patent-IR recall number is softer than it looks** — CLEF-IP best Recall@100 = **0.58**, TREC-CHEM **0.55**, but both are recall **against examiner citations**, and the organizers disclaim their own figures: *"we have incomplete recall bases which must be taken into account."* **EPO examination guidelines cap the citation list on purpose** — *"if the search results in several documents of equal relevance, the search report should normally contain no more than one of them."* **The gold standard is deliberately truncated.**
  - **⚠ FABRICATION #2, caught the same way as gwern.** A search engine attributed *"Patent applicants use vague and abstract terms in order to broaden the scope of their patent protection"* to **Lupu & Hanbury 2013**. The 99-page survey was retrieved in full and grepped: **zero occurrences of "vague," "obfuscat," "deliberate," "intentional," or "idiosyncratic."** False attribution. (The real version is Helmers et al. 2019, *PLOS One*, `primary-full`.) **Two fabricated quotes in one sweep, both stating the thesis in perfect words, both killed only by reading the primary. Treat any snippet that says exactly what you hoped as a positive indicator of fabrication.**
  - **The measurement series now available** — five independent domains, and the direction never reverses: **~20%** actual vs **75%** believed recall (Blair & Maron 1985, lawyers, litigation corpus) · **9%/3%** (Larsen & Bong 2016, PhD students, IS constructs) · **12%** zero lexical overlap (Magdy 2009, patents) · **61.2%** of eventually-cited art missed at first search (Wada 2016, 1.06M citation pairs) · **89%** of IPR invalidations on unseen art (Yelderman 2019). **Different fields, different decades, different searchers — nobody finds what they think they find.**
- **Retrieval caveat, stated carefully:** embedding-only semantic search is register- and era-local ("gate" in 2025 LLM-eval register does not neighbour "sufficiency" in 1982 forecasting register), and Shahid et al. (arXiv:2506.22026) report embedding-only failure — **but also substantial improvement from hybrid retrieval with facet reranking.** So: better retrieval genuinely helps, and **no retrieval method alone can establish an absence claim.** Structure and function are the search key; surface similarity is not.
- **In the AI-agent discourse (2023–26), the specific loop is not named in the recorded searches — but this survived a dedicated refutation attempt only in narrowed form.** A blind agent tasked with *refuting* the absence claim (arXiv + LessWrong + AF + EA Forum + HN + lab blogs, plus a forward citation-walk through 100 Sakana-critique citers) found **no composite** — but found that **every component has an owner**, which is a much weaker position than "unnamed":
  - **The outcome is already named, and our countermeasure already prescribed** — arXiv:2604.20622 (MIT, 2026): *"one of the most common failure modes of automated research is confident production of work that is, in fact, already established,"* countered by a literature agent whose *"default stance is skepticism… It is 'try to kill the novelty claim.'"* **That is §2's blind refuter, in print.** It assigns no cause — vocabulary is absent from its mechanism — which is where the remaining daylight is.
  - **A rival named trap exists** — the **"101st-paper trap"** (arXiv:2606.24177): the next idea after reading 100 papers may already be in the 101st. Cause is **saturation, not vocabulary** — a competing explanation for the same observations, and one that must be argued against rather than ignored.
  - **Same-content-different-words → judged novel is demonstrated experimentally** — arXiv:2602.06054 paraphrases an abstract and watches novelty scores rise. **The relabeling half is Kelley 1927 → construct-identity detection (Larsen & Bong 2016).** The vocabulary→retrieval-miss half is explicit for novelty agents in arXiv:2603.20884 and 2506.22026 — the latter's *"if such a decision is not reached, the idea is automatically considered novel"* being the closest published thing to null→novelty (as an implementation bug, not a named loop). The shared-brief→correlated-agreement twist is named informally (Paluch 2026).
  - **Negative results worth keeping:** the field's own survey (arXiv:2510.23045) and the *Nature* AI Scientist paper name **no** vocabulary failure mode at all.
  - **Standing (revised after the Larsen & Bong body was read):** *"the composite is unnamed **in the recorded searches** — but **Larsen & Bong 2016 owns the causal chain and measures it**, and what is left unclaimed is only the null-as-evidence step, the self-referential case, and the agent twist."* Never "unnamed." This sweep had no frozen query list, result counts, or stop rule; it is exploratory, so the null is weak evidence and **cannot be distinguished from incomplete coverage**. **This remains the weakest kind of claim this protocol recognizes.** Of the two literatures the sweep named and never searched, **patent/prior-art analytics has since been run** (see the patent-leg entry above — it did not empty the cell, but it surfaced a **well-evidenced rival cause** (examiner myopia) occupying the same outcome, which is a stronger obstacle than an empty cell). **MeSH/controlled-vocabulary indexing evaluation is still unsearched** — do not build a public novelty claim on this null before running it.
  - **⚠ The cautionary tale is this section's own history.** The §3b bibliometric null ("nobody measures vocabulary-driven duplication") was written by an agent that **had never read Larsen & Bong** — who measure the retrieval half and explicitly claim that measurement's novelty themselves. **Five blind agents, ~200 tool calls and a Codex review all missed it, because none of them read the paper; every one of them had the citation.** The citation was never the bottleneck. **A null written by agents who did not read the load-bearing source is not a null.**
  - **The patent leg (above) then re-ran that same null properly and it did NOT survive as written.** It went from *"nobody measures vocabulary-driven duplication"* to *"both halves are well measured by two literatures that never cite each other, and the outcome-owning team **rejects** the vocabulary explanation."* **The null was not merely under-evidenced — its sign was wrong on the part that matters.** Both times the fix was the same: read the paper.

## Revision note

**Updated 2026-07-16 (third pass): the Larsen & Bong 2016 full text was obtained and read.** It reverses a withdrawal, narrows the §3b null, and moves the novelty position. The paper owns **coined name → search fails on the name → incomplete review → "reinvention of the wheel"**, states that renaming *"may increase the perceived novelty of a construct,"* measures the retrieval failure at **9% / 3% recall** by motivated PhD students, and closes with *"the vast majority of discovered knowledge is hidden from the individual researcher by the very nature of the search process itself."* **Any novelty claim in this space must now clear Larsen & Bong 2016 by name and by number.** How it was found matters as much as what it says: OpenAlex and Semantic Scholar both reported it CLOSED (**both wrong**), the UNIMAS repository's "full text" was a **2-page cover sheet**, and the authors' own site lists but does not attach it — the copy was in the **Wayback CDX index of the authors' ResearchGate uploads**. *An aggregator's "not open access" is not evidence of absence; a repository's "full text" link can be a cover sheet.* **The meta-lesson, and the reason this sits in this document:** five blind agents and a Codex review all missed this because none of them read the paper — every one of them had the citation. **A null written by agents who did not read the load-bearing source is not a null.**

**Updated 2026-07-16 (second pass), after the primary-text verification prompt this document was waiting on actually ran** (5 blind agents → `10_projects/minelit/idiolect/2026-07-16-targeted-prior-art-search-RESULTS.md`, itself Codex-reviewed → MAJOR REVISION → repaired). §"What the phenomenon is called" is no longer provisional. **Three anchors verified against primary text; two carried errors this document had propagated:** (a) *jingle* was misattributed to Kelley — it is Thorndike 1904 quoting Aikins; Kelley coins only *jangle*; (b) "CPC/IPC indexes by function/structure **rather than** words" overstated the record — examiners' own documented practice is classification **plus** keyword supplement, and "countermeasure to vocabulary variance" was our inference, not any document's wording. **One load-bearing reframe was withdrawn:** Furnas's <20% is real (.07–.18, `primary-full`), but its base is **untrained people naming everyday objects**, not experts naming constructs — so "correct for a known base rate" was never underwritten by the citation, and the weaker supportable claim replaced it. The absence claim survived a dedicated refutation attempt **only in narrowed form** ("the composite is unnamed *in the recorded searches*, while every component has an owner"), and arXiv:2604.20622 turns out to already name the outcome and prescribe this protocol's blind refuter. **The pattern held again:** the verification's own first draft leaned a conclusion on a quote it had flagged as unverified, and headlined a date its own audit called undetermined — `feedback_unreviewed_artifact_assume_wrong`, twice, inside the document about this exact failure.

Rewritten 2026-07-16 (first pass) after a Codex review returned **MAJOR REVISION** on the first draft. The findings, all accepted: unverified citations were presented as settled evidence (the draft's own failure mode); "3-for-3" had no stated denominator; the novelty-position template was not auditable; the linked "blind" prompt was in fact a Pass-B prompt; the glossary was unimplementable; **foreclosure was defined too broadly** — the draft would have had readers discard valid empirical work because a theoretical proposition was old; and search heuristics were stated as exemptions rather than priors. The first draft of a document warning against laundering unverified subagent citations laundered unverified subagent citations. `feedback_unreviewed_artifact_assume_wrong`, on schedule.

## Related

`20_areas/thinking/decisions/2026-07-16-flf-no-submit-judge-dependence-prior-art.md` (the diagnosis) · `10_projects/minelit/judge-dependence/lit/2026-07-16-prior-art-position-sweep.md` (the sweep + its verification pass — the source for the withdrawn/corrected rows above) · `10_projects/minelit/idiolect/` (the Pass-B prompt + the FLF exploration) · memory: `feedback_search_field_vocabulary`, `feedback_research_calibration`, `feedback_fanout_agreement_not_independence`, `feedback_verify_citations_primary_text`, `feedback_unreviewed_artifact_assume_wrong`.
