---
title: "Machinery against name-blind search — blind PASS A RESULTS"
date: 2026-07-16
kind: research data
status: "COMPLETE — 3 valid blind draws (c1/c2/c3, reads blocked). Run 1 INVALID (dashboard contamination, §0). Blair & Maron 1985 verified by orchestrator against primary. 4 of 5 pre-registered predictions wrong or mis-scoped."
prompt: 2026-07-16-machinery-blind-PASS-A-PROMPT.md
siblings: 2026-07-16-blind-naming-PASS-A-RESULTS.md · 2026-07-16-targeted-prior-art-search-RESULTS.md
method: "Frozen brief (prompt lines 25–79) extracted verbatim, sha256 8112243692ca8d0f298a1e8276bd02f82859ca6cefe829d89d161aa3956a6372. Leakage-checked: 0 hits for any candidate term from prior passes. Run via headless `claude -p` from a neutral scratchpad cwd (no vault access, no project docs, no CLAUDE.md inheritance), tools restricted to WebSearch + bare safefetch. Three models: default / opus / sonnet."
note: "Absence claims mean 'not found in the recorded searches.' Convergence across runs is NOT independent confirmation (shared training corpus). Item 4 of the brief is SEMI-BLIND — see §0."
---

# Machinery against name-blind search — Pass A results

**The question, and why it is new.** Neither prior pass asked what *machinery* exists for machine searchers. Pass B asked an absence question ("is the composite named in the AI literature?"). Pass A (naming) asked "what is this called?". **"What has been built against this, and does it work?"** is a positive question that surfaces different objects — and it is the one that bears on whether the residue is buildable.

**Why a positive question is the right shape here.** This session has now watched three negative claims fail (`feedback_search_field_vocabulary`). Positive, checkable claims are the protocol's §3 prescription precisely because *a null cannot hide in them* — an agent either names a system or it does not.

---

## 0. ⚠⚠ BLINDNESS FAILED — run 1 is INVALID as a blind draw

**The attestation below was wrong. Run 1 read the vault dashboard, and the dashboard names four of run 1's key findings.**

**How it happened.** The runs were started from a neutral cwd outside the vault with `--allowedTools "WebSearch,Bash(safefetch:*)"`. That is not sufficient. **`/home/nik/.claude/CLAUDE.md` is a *user-level* instruction file — it loads in every session regardless of cwd** — and its first directive is: *"At session start, read `/mnt/f/hub/_dashboard.md`."* Run 1 obeyed it. Its output opens by reporting my overdue [redacted-employer-term] reminder back to me, which is how this was caught at all.

**The contamination is direct and severe.** `_dashboard.md` line 121 contains the project's own prior-art candidate list:

> *"Before any public novelty claim, also do the iteration-2 missed-terminology sweep (**stemmatics / Leinster–Cobbold / design-effect**) + the full-text reads"*
> *"closest cousins observational/analytic/elicited — K\* 2602.03794, **Broomell-Budescu 2009, Lorenz PNAS 2011** — never interventional-for-effective-N"*

And line 95 names **Clemen & Winkler 1985**. Grep of dashboard-vs-output:

| Term | in `_dashboard.md` | in run 1 output |
|---|---|---|
| Lorenz | ✓ | ✓ (its single most on-target agreement finding) |
| Broomell | ✓ | ✓ (§A "from knowledge") |
| Kish / design effect | ✓ | ✓ (§A "from knowledge") |
| stemmatics | ✓ | ✓ (§A "from knowledge") |
| Clemen & Winkler | ✓ | ✓ (§A "from knowledge") |

**Five of run 1's items — including three in its "from knowledge, before searching" section and its headline agreement finding (Lorenz PNAS 2011) — are named in a file it read at session start.** Those are not independent draws. They are reading, relabeled as recall.

**This is the protocol's own warning, realized through an unanticipated channel:** *"Briefing an agent on project context socializes it into the idiolect at spawn time and destroys the fresh-eyes function."* I controlled the brief and the cwd and believed that was enough. The socialization came through the user-level config, underneath both.

**Verdict on run 1:** **INVALID as a blind draw.** Its *verification* work remains useful (it read seven primaries and produced real corrections — see §2), but **nothing in it may be counted as an independent draw, and its §A "from knowledge" section is worthless as evidence about where the concept lives.** Per `feedback_fanout_agreement_not_independence`, any later agreement with run 1 on these five items is now a *shared-source* artifact, not corroboration.

**The fix for a genuinely blind run:** `--disallowedTools "Read,Glob,Grep,Task,Agent"` — so the run *cannot* open the dashboard even when its own config tells it to. Re-running on that basis.

**⚠ This retroactively puts the naming-pass Pass A (`2026-07-16-blind-naming-PASS-A-RESULTS.md`) under suspicion.** Same launch pattern, same user-level config. Those runs' outputs do not mention the dashboard and do not contain Lorenz / Kish / stemmatics / Broomell — so they were probably clean, or read it and got nothing useful for a naming question. **"Probably" is not an attestation.** That file's blindness claim must be downgraded to *unverified* until re-run with reads blocked.

---

## 0b. The original attestation (superseded — kept for the audit trail)

**Brief-level, and this part held:** brief extracted mechanically (lines 25–79, no frontmatter, no design notes), leakage-checked with a grep for every candidate term from the prior passes (`larsen|bong|furnas|swanson|kelley|jangle|jingle|ginsburg|garfield|martyn|mesh|cpc|ipc|oeis|onomasiol|kohli|idiolect|vocabulary problem|construct identity|disregard`) → **0 hits**. The brief was clean. **The session was not.** Controlling the prompt is not controlling the context.

**Deliberate design choice:** the brief says **"machine searchers," not "LLM agents."** Saying "LLM agent" would socialize the runs into the 2025–26 arXiv bubble and recreate the correlated-context problem one stage later. If the AI literature owns this, an unprimed run should find it on its own — and whether it does is itself a datum.

**⚠ Item 4 is SEMI-BLIND and must not be counted as an independent draw.** "Do any approaches sidestep wording entirely?" is informed by a prior run's content-addressed-retrieval finding (OEIS / CAS Registry / BLAST). It names no owner, but it primes a direction. **Any hit on item 4 is a confirmation, not a discovery.**

**The main methodological fix over both prior passes:** the brief mandates opening **at least four sources in full** and quoting **from the body, not the abstract**, with a six-level evidence grade. The shared failure of the last two passes was that eight agents assessed everything from abstracts and snippets, and the single load-bearing paper (Larsen & Bong 2016) was never opened by any of them. Whether this fix works is the second thing this pass tests.

---

## 1. Pre-registered predictions (written BEFORE any run returned)

Recorded so the runs cannot be retrofitted, and so a miss is visible. **These are my expectations from the prior passes' evidence — they are exactly the socialized priors the blind runs are meant to bypass.** Where a run contradicts these, the run wins.

**I expect the runs to find (already known to me):**

- Terminology-aware retrieval for novelty agents — arXiv:2603.20884, *"standard semantic retrieval frequently fails to retrieve earlier or implicit works that use different terminology."*
- An adversarial/skeptical refuter for novelty claims — arXiv:2604.20622, *"it assumes the central claim is already known and tries to find the evidence."*
- The default-to-novel implementation bug — arXiv:2506.22026, *"If such a decision is not reached, the idea is automatically considered novel."*
- Paraphrase-blind novelty scoring, demonstrated — arXiv:2602.06054.
- Classical IR countermeasures: automatic query expansion (Carpineto & Romano 2012); ontology matching / OAEI (running since 2004, F≈0.94 anatomy, 0.74 conference); record linkage (Fellegi–Sunter 1969 → Newcombe 1959).
- Controlled vocabulary / thesauri (MeSH, authority control) and patent classification (CPC/IPC) as the human-side machinery.
- For item 6: LLM judge-panel dependence measured from co-errors — Kohli 2026, *"Nine Judges, Two Effective Votes"* — **requiring ground truth**.
- For item 4 (semi-blind): content-addressed retrieval — OEIS, CAS Registry/InChI, BLAST.

**What would be genuinely new, and what I am actually watching for:**

1. **An agent-side equivalent of a controlled vocabulary or a function classification.** Humans solved this with MeSH and CPC — concept-first indexes maintained by institutions. **Has anyone built that for machine idea-search?** I do not know of one. If a run names one, that is the highest-value hit in this pass.
2. **Item 3's answer** — decades-old human machinery nobody has automated. This is the question most likely to surface something none of us has considered, and no prior pass asked it.
3. **Item 6 without ground truth.** Every dependence estimator found so far needs labels (Kohli) or models dependence as a free parameter (Broomell & Budescu). **Does anything estimate lost independence from the searchers' inputs alone?** Prior passes say no; reliability engineering's beta-factor / IEC 61508 is the nearest general antecedent and nobody has aimed it at agents.
4. **Whether the runs reach the 2025–26 agent literature at all**, given the brief never says "AI" or "LLM." If they do not, that is evidence the field is not reachable from a neutral statement of the problem — which would be a finding about the field's own vocabulary.
5. **Benchmarks.** Item 5 asks for numbers. Prior passes found OAEI (a real, 20-year evaluation campaign) but nothing benchmarking *idea-level* novelty detection under vocabulary variance. If such a benchmark exists, it changes the picture.

**Standing prediction, stated so it can fail:** I expect the runs to confirm that the *retrieval* and *refuter* halves are built and published, and to find the *agreement-without-ground-truth* cell (item 6) still empty — with the general antecedent living in reliability engineering rather than anywhere in AI. **I expect at least one run to surface a field or system none of the prior eight agents reached.** Prior base rate for that: 2 for 2.

---

## 2. Runs

Raw outputs preserved under `machinery-raw/`.

### ⚠ Run 3 (sonnet) — FAILED on first attempt. Recorded, because it is a datum.

The run produced **one line** and no research:

> *"The deep-research workflow is running in the background — it'll fan out search agents across your seven questions, fetch and adversarially verify sources, and synthesize the two-section bullet report you specified. I'll let you know when it lands."*

stderr: `Background tasks still running after 600s; terminating.`

**What happened:** the run delegated to a background fan-out and returned a status message instead of doing the work. `claude -p` is one-shot — the session exited, the delegated work died with it, and nothing was produced. This is `feedback_subagent_dead_waiter` exactly: *long-runner subagents must foreground-poll, never wait on background re-invocation.* Third instance recorded in this vault; the pattern is not rare.

**Fix applied (operational, not a brief change):** re-ran as **run 3b** with `--disallowedTools "Task,Agent"` and a prepended execution constraint — *"Do all of this work yourself, inline… Do NOT delegate to subagents, background tasks, workflows, or any deep-research harness — this is a one-shot session and delegated work is lost."* **The frozen brief is unchanged and the constraint contains no research content and no candidate terms**, so blindness is intact. Logged here rather than silently re-run.

**Why it is worth recording as a finding, not just plumbing.** The failure is a small live instance of this project's own subject: *the agent reported success on work it had not done, and the report was fluent and confident.* Had the output not been checked — had "the workflow is running" been taken at face value — a null or a thin result from a dead run would have entered the ledger as data. **An unread agent output and an unread PDF are the same failure.** The prior passes lost Larsen & Bong to exactly this class of error, at a different layer.

**Note on run 3's delegation instinct:** it read a seven-part research brief with a verification mandate and concluded the right move was to fan out. That is the same reflex both prior passes acted on — and the reflex that produced eight agents and zero primary reads. Blocking it here is not only an execution fix.

---

## 2b. ⛔ BLOCKED — monthly spend limit

**Four runs failed** (m2-opus, m3b-sonnet, c1-opus, c2-sonnet), all with the same one-line output:

> `You've hit your monthly spend limit · raise it at claude.ai/settings/usage`

**Diagnosis, verified not assumed.** The `.err` files show only a benign `Write(//tmp/**)` permission warning that was *also* present in the runs that succeeded — so that is not the cause. A control probe (`claude -p --model sonnet --allowedTools ""`) returned `PROBE_OK`, exit 0, confirming headless invocation still works. **The block is on spend, not on the harness, the config, or the models.** The likely driver is `WebSearch`, which is billed per search on top of the plan; the tool-less probe passed while every WebSearch-dependent run failed.

**Sequence:** the 3 naming-pass runs and machinery run 1 all completed with WebSearch. Everything after that failed. **The cap was consumed during this session.** This is `reference_max_plan_scheduling` (spread large bursts across days) and `feedback_max_cli_default` (CLI ops are ~free *within limits* — these exceeded them) hitting at once.

**What this costs:** the machinery pass has **zero valid blind draws.** Run 1 is disqualified by dashboard contamination (§0); runs 2–5 never executed. **The pass produced no usable blind evidence and must be re-run in full.**

**Resume conditions (user's call, and there is no hurry):**
1. **Wait for the monthly reset** — the recommended default. **FLF closed 2026-07-16 (NO SUBMIT); nothing in this line of work is time-critical.** There is no deadline argument for spending money to finish it tonight.
2. **Raise the cap** at claude.ai/settings/usage — only if the answer is wanted now, for its own sake.

**When resumed, the command is already fixed and staged** — `scratchpad/c1.sh` / `c2.sh`, using `--disallowedTools "Read,Glob,Grep,Task,Agent,Edit,Write"` so a run physically cannot open `_dashboard.md` even though user-level `~/.claude/CLAUDE.md` orders it to at session start. The frozen brief (sha256 `8112243692ca…`) and the pre-registered predictions (§1) are unchanged and still sealed — **the pass can resume without any loss of methodological standing.** That is the one thing that went right here: the predictions were written before any run returned, so they remain a live test rather than a retrofit.

**Two failures worth carrying forward, both cheap to prevent:**
- `saferun -f script.sh <args>` **does not forward positional arguments** → `$1` unbound under `set -u`. Two runs died on this before the spend limit was even reached. Write self-contained scripts; don't parameterize saferun invocations.
- **Tool-level denial is the only real blindness control.** cwd and prompt hygiene are not enough against user-level `CLAUDE.md`.

---

## 2c. ✅ Run c2 (sonnet, reads blocked) — VALID BLIND DRAW

**Spend limit reset; re-run with `--disallowedTools "Read,Glob,Grep,Task,Agent,Edit,Write"`.**

**Contamination check — PASSES.** Grep of c2's output: `dashboard` 0 · `[redacted-employer-term]` 0 · `reminder` 0. It could not and did not open `_dashboard.md`. **This is the pass's first valid blind draw.**

### ★ The natural experiment: run 1's items are NOT dashboard artifacts

c2, blind, independently reached **Lorenz PNAS 2011**, **Kish design effect**, **Clemen & Winkler 1985**, and **design effect** — four of the five items that disqualified run 1. **So those items are genuinely reachable from model knowledge; they were not read off the dashboard.** Run 1 remains procedurally invalid (it *did* read the file, so its draw cannot be trusted), but the **content** is corroborated by a clean draw. Two items did *not* reappear: **Broomell** (0) and **stemmatics** (0) — consistent with those two having been dashboard-driven in run 1, though one run cannot settle it.

**Caveat that must travel with this:** c2 and run 1 are both Claude-family. Per `feedback_fanout_agreement_not_independence`, their agreement ≈ shared-corpus, not independent confirmation. What is ruled out is specifically the *dashboard* channel.

### ★★ NEW field, reached by no prior agent in any pass: climate science

- **Pennell & Reichler 2011, "On the Effective Number of Climate Models," *J. Climate* 24(9):2358–2367.** Dozens of CMIP models **share code lineage**, so the effective independent count is far below the nominal count. Verified by reading the **body of a citing paper**: *"Studies by Pennell and Reichler… showed that GCM ensembles feature considerable model dependence, leading to a smaller effective ensembles size than the number of models in the ensemble"* (Mendlik & Gobiet, *Climatic Change* 135, 2015) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4922546/ — **PRIMARY-BODY** (via citing paper). The specific figure (≈7.5–9 effective of 24) is **SNIPPET only**, AMS blocked. **Conflicting identifier flagged not resolved:** DOI `10.1175/2010JCLI3814.1` date-stamps 2010; the issue is 2011.
- **Why it matters:** this is *"how much independence is lost when the sources share lineage,"* **measured, with a number, in a field with a 15-year literature on it** — and it is the closest structural analogue to the agent-panel question anywhere in this investigation. **Eight prior agents across two passes never reached climate science.**

### ★ More measurements the "cell is empty" null never saw

- **Dickersin, Scherer & Lefebvre, *BMJ* 1994;309:1286–91 — PRIMARY-FULL.** *"Weighted means for sensitivity across all studies were 51%, 77%, and 63%… The weighted mean for precision was 8%… sensitivity still remains unsatisfactory."* **MEDLINE-only search misses roughly half of eligible trials — measured in 1994.**
- **Spoor, Airey, Bennett, Greensill & Williams, *BMJ* 1996;313:342–3** — capture–recapture (Lincoln–Petersen) for literature-search completeness. **Independently corroborates run 1's capture-recapture finding by a different citation** (run 1 had Poorolajal 2010) **and pushes it back to 1996.** Two independent routes to the same machinery.
- **Grossman & Cormack 2011**, *Rich. J.L. & Tech.* 17(3) — TAR beats exhaustive manual review. **Honest failure recorded:** *"the specific recall percentages could not be verified in this session"* — every host blocked, dead, or unparseable. The claim is kept, the numbers are not repeated.

### ★ Item 4 (sidestep wording) and item 2 (built for machines) — answered, with a caveat

- **c2's pick for most on-target thing built for machine searchers: SPECTER** (Cohan, Feldman, Beltagy, Downey & Weld, AI2/UW, ACL 2020) — citation-graph-trained paper embeddings, *"pretraining a Transformer language model on a powerful signal of document-level relatedness: the citation graph."* Its reasoning: it is the only entry that **targets machine searchers specifically rather than being adapted from human practice**, and ships with a dedicated benchmark (SciDocs/BEIR).
- **⚠ But the benchmark is a caution, not a win.** **BEIR** (Thakur et al., NeurIPS 2021): *"BM25 is a robust baseline… dense and sparse-retrieval models are computationally more efficient but often underperform"* out-of-domain. c2's own gloss: *"this is a caution against oversold 'semantic search solves it,' not a confirmation."*
- **Wording-independent indexing, verified from primaries:** **USPTO MPEP §904 — PRIMARY-FULL:** *"it is rare that a text search alone will constitute a thorough search of patent documents. Some combination of text search with other search criteria (e.g., classification, chemical structure, or molecular sequence) would be a normal expectation in most technologies."* **This independently reproduces Pass B's own correction** — classification is primary *plus* keyword supplement, not "instead of words." **Cochrane Handbook — PRIMARY-FULL:** *"Searches for Cochrane reviews should use an appropriate combination of these two approaches, i.e. text words and controlled vocabulary."* Also **bibliographic coupling** (Kessler 1963) and **co-citation** (Small 1973) — relatedness by shared references, not shared words.

### ★ Item 6 — the honest state, and it contradicts my prediction

- **Kuncheva & Whitaker 2003**, *Machine Learning* 51:181–207 — *"measuring diversity is not straightforward because there is no generally accepted formal definition… results raise some doubts about the usefulness of diversity measures in building classifier ensembles."* c2's gloss: *"the field has metrics, but they are contested, not solved."*
- **⚠ c2 flagged a dispute run 1 did not:** Lorenz 2011 has a **2012 PNAS reply, "Social influence benefits the wisdom of individuals in the crowd," arguing the opposite under different conditions.** c2 flagged the disagreement rather than picking a side. **Run 1 presented Lorenz as settled.** The blind, more careful run is the more honest one.
- **Clemen & Winkler journal conflict, caught and resolved:** *"sometimes miscited as *Management Science*; confirmed here as *Operations Research*"* 33(2):427–442. (Matches `project_minelit`'s citation — good.)

### ★★ c2's gap statement — the phenomenon describing itself, one level up

> *"a single, named, cross-domain discipline that treats 'several independent-seeming searchers converging on the same wrong answer' as its own measured problem, with an agreed metric for how much independence was actually lost — **not found in these searches**. What exists is scattered across climate science (effective number of models), ensemble ML (diversity measures, of contested validity), decision analysis (dependent-source value-of-information), survey statistics (design effect), and intelligence tradecraft (sourcing corroboration) — **each with its own vocabulary, none citing the others**, and no evidence in these searches of a body of work that unifies them or that measures, specifically, how much independence multiple AI/LLM search agents lose when they derive queries from the same input wording."*

**"Each with its own vocabulary, none citing the others."** The countermeasure literature is itself fragmented by naming — the exact phenomenon under study, operating on its own remedies. Note the phrasing discipline: **"not found in these searches,"** exactly as the brief required.

### Scorecard against §1's pre-registered predictions

| Prediction | Outcome |
|---|---|
| Agreement-without-ground-truth cell **empty** | **WRONG.** Occupied — climate science (effective number of models), capture–recapture (needs overlap, not labels), Kish design effect, ensemble diversity measures. |
| General antecedent = **reliability engineering** | **WRONG.** Reliability engineering never appeared. The owners are climate science, ensemble ML, decision analysis, survey statistics, intel tradecraft. |
| An **agent-side MeSH/CPC** would be the highest-value hit | **NOT FOUND** — and c2's answer explains why: what exists for machines is *learned embeddings* (SPECTER), not a maintained concept authority. The human answer has **no machine port**. |
| Runs may **not reach the 2025–26 agent-novelty literature** from a neutral brief | **CONFIRMED for c2** — it reached retrieval (DPR/SPECTER/BEIR) but **no Sakana, no Beel, no AI Scientist**. That literature is not reachable from a plain statement of the problem. |
| **≥1 run surfaces a field no prior agent reached** | **HIT — climate science.** Base rate now **4-for-4**. |

**Three of five pre-registered predictions were wrong.** They were my socialized priors; the blind draw beat them. That is the pass working as designed.

### Integrity notes (c2)

- **safefetch injection flag — reviewed, false positive.** c2 reports safefetch raised a **HIGH-severity `role_manipulation`** finding on the Cochrane Handbook page, on the phrase *"No limitations."* c2 read the surrounding text and correctly called it benign — ordinary methodology prose about not applying date/language search limits, not an injection attempt. **Reported per CLAUDE.md's third-party-content rule.** Second false positive this session (run 1's was Suber's *"pretend to be"*).
- **Taylor 1968 (reference interview) reached independently by run 1 and c2**, both calling it human machinery with no machine equivalent.
- Evidence quality is honest but mostly mid-grade: 4 PRIMARY-FULL (MeSH preface, MPEP §904, Cochrane ch. 4, Dickersin 1994), 2 PRIMARY-BODY, the rest ABSTRACT-ONLY / SECONDARY / SNIPPET, each labeled. **Furnas 1987 primary blocked again** — SNIPPET only. That is now **~5 consecutive failures to open Furnas across every pass**; Pass B's PSU-mirror read remains the only one.

---

## 2d. ✅ Run c3 (default, reads blocked) — VALID BLIND DRAW, and the strongest run of the investigation

**Contamination check — PASSES.** `dashboard` 0 · `[redacted-employer-term]` 0 · `reminder` 0 · `FLF` 0. **And it reached NONE of the dashboard-named candidates** (Lorenz 0 · Broomell 0 · Kish 0 · design effect 0 · Clemen 0 · stemmatics 0). A completely disjoint draw from c2 — which is itself informative: **c2's reach of Lorenz/Kish/Clemen is one draw, not a consensus.** Two clean same-family runs share almost no specific sources.

### ★★★ THE ANSWER: the failure is measured, and the number is 5.17%

**Shahid, Radensky, Fok, Siangliulue, Weld & Hope (Microsoft / UW / Allen Institute for AI), "Literature-Grounded Novelty Assessment of Scientific Ideas," arXiv:2506.22026, June 2025 — PRIMARY-BODY.**

**Table 2, "Accuracy of predicting 'not novel'":**

| Method | Accuracy |
|---|---|
| Complete system (facet-based reranking) | **89.66%** |
| Relevance RankGPT | 13.79% |
| Embedding filtering | 10.34% |
| Snippet retrieval | 8.62% |
| **Keyword retrieval** (terms derived from the idea's own wording) | **5.17%** |

**A machine deriving search terms from an idea's own wording correctly recognises an already-published idea as "not novel" 5.17% of the time.** That is the machine analogue of Furnas's <0.20, measured, for precisely the machine the brief described.

**The caveats, taken from the body not the abstract** (c3 did this unprompted):
- **Small N:** the ablation used *"58 ideas (comprising 13 'not novel' instances from our test set and 45 NLP papers from the literature)"* → **5.17% is 3 of 58; 89.66% is 52 of 58.** Main test set smaller still: *"67 consensus-labeled examples (39 labeled as novel and 28 as non-novel)… (35 for training and 32 for testing)."*
- **Table 1 — machine novelty judges vs. experts (Cohen's Kappa):** **AI Scientist 0.47 accuracy / Kappa 0.05 — chance-level agreement.** AI Researcher (GPT-4o) 0.78 / 0.52. AI Researcher (Claude-3.5-Sonnet) 0.56 / 0.19. Best own system 0.81 / **0.59 — moderate at best.**
- **The abstract oversells:** *"approximately 13% higher agreement than existing approaches"* is a **relative Kappa gain (0.52→0.59) against one baseline only**, and is prompts-only — *"We compare only the prompts to assess novelty of these two approaches with ours, rather than the entire system."*
- **Prompt fragility:** *"prompt 3 (accuracy = 0) and prompt 9 (accuracy = 0.6)… subtle variations in wording and instruction framing can significantly impact the classification."*

### ★★ A material correction to Pass B, from the same paper's body

Pass B cites 2506.22026's *"If such a decision is not reached, the idea is automatically considered novel"* as **"the closest anything comes to null→novelty."** c3 read further and found the paper **contradicts itself on the direction of that default**:

- **§2:** *"the decision of novelty evaluation relies on string matching… If such a decision is not reached, the idea is automatically considered **novel**."*
- **§6.1:** *"It is important to note that AI Scientist defaults to **'not novel'** when it fails to reach a conclusion in novelty evaluation (18 out of 32 times), which may have impacted its agreement rates."*

c3's note: *"Two search engines each quoted one of these at me and appeared to disagree; both were quoting the paper accurately — the paper contradicts itself. The direction of that default IS the failure mode in question, and this paper states it both ways."* **Pass B's load-bearing quote is real but comes from a self-contradicting source and must be cited with the contradiction attached.**

### ★★ WHY the cell keeps coming up empty — the structural reason, from the primary

> *"we focus on the 'not novel' cases, since the ideas labeled novel in expert-labeled test data can vary with different retrieved paper sets."*

c3's gloss: **"Novelty is falsifiable only by finding the thing; 'absent' is not directly checkable, so the measurable quantity is always *recall of known-existing prior work*, never accuracy of a 'new' verdict."**

**This is the same wall Martyn 1964 hit (*"we cannot measure this 'iceberg'"*) and Garfield 1991 hit (*"no way to document support"*) — now stated as a design constraint by a 2025 benchmark team.** Three independent sources, three eras, one obstruction: **you cannot build ground truth for absence.** This is the correctly-scoped version of the claim my §1.2 draft overreached into "unobservable by construction" — it is an identification constraint on the *positive* direction only, and it explains why every benchmark measures one-directionally.

### ★★★ NEW field, reached by no agent in any pass: IR evaluation / TREC pooling

**Buckley, Dimmick, Soboroff & Voorhees (NIST), "Bias and the Limits of Pooling for Large Collections," *Information Retrieval*, 2007 — PRIMARY-FULL.** *This is the described experiment, already run, in 2007, at NIST.*

- The design: *"In pooling, a set of documents to be judged for a topic (the 'pool') is constructed by taking the union of the top λ documents retrieved for the topic by a variety of different retrieval methods… documents not in the pool are assumed to be irrelevant to that topic."*
- The load-bearing assumption: *"The crucial assumption of pooling is that the sample of relevant documents found by judging just the pool is unbiased with respect to different retrieval approaches."*
- **The failure:** *"pools created during the TREC 2005 workshop exhibit a specific bias in favor of relevant documents that contain topic title words. These documents are retrieved by systems that are behaving reasonably, in that they rank documents containing the topic words first. As the document set size grows, these documents fill the pool, squeezing out other kinds of relevant documents."*
- **★ Agreement masking the error — the single most on-target sentence found anywhere in this investigation for failure mode 2:** *"The terabyte collections' high titlestat rank values explain why the LOU test shows comparatively minor variations in scores: **all of the pool runs were at least implicitly targeting title-word-containing documents and so match the bias in the judgments** for the collection."*
- **★ The diversity defence was tried and it failed:** *"the diversity of the runs was expected to ensure a reliable sample of all types of relevant documents."*
- **The numbers:** 50 runs contributed to the AQUAINT pool. One run (`sab05ror1`) built its query from **relevance data rather than the topic's wording** — *"405 of these 2750 were uniquely relevant… the ratio of number uniquely relevant to the number contributed to the pool is higher than any other run in TREC's history for the major ad hoc collections."* Leave-one-out: *"if sab05ror1 had not contributed to the pool, its MAP score would have been 0.202 instead of 0.266."* `titlestat_rel` 0.588 (Disks4&5) vs 0.719 (AQUAINT), *"greater for the AQUAINT collection… for 48 of the 50 topics… (p = 6.25 · 10⁻¹⁰ according to a paired t-test)"*; terabyte 0.889/0.898 — *"any single title word occurred in nearly 9 out of 10 judged relevant documents on average."*

**Fifty searchers, deliberately diverse, all implicitly keyed on the query's own words, agreed — and the agreement *was* the bias. The one run that escaped did so by not using the query's wording. Measured, at NIST, in 2007.** Eight prior agents across two passes never reached IR evaluation.

### ★★ BEIR's independent rediscovery 14 years later — and a correction to c2

**Thakur, Reimers, Rücklé, Srivastava & Gurevych (UKP Lab), NeurIPS 2021 D&B — PRIMARY-BODY:**

> *"Many BEIR datasets are found to be subject to a lexical bias, i.e. a lexical based retrieval system like TF-IDF or BM25 has been used to retrieve the candidates for annotation… Such a lexical bias disfavours approaches that don't rely on lexical matching, like dense retrieval methods, as retrieved hits without lexical overlap are automatically assumed to be irrelevant, even though the hits might be relevant for a query."*

TREC-COVID Hole@10: BM25 **6.4%**, docT5query **2.8%**, DPR **30.6%**, TAS-B **31.8%**. After manually filling 980 missing judgements: ANCE **0.654 → 0.735** (6.7 points *above* BM25), while docT5query moved *"just from 0.713 to 0.714."*

**⚠ This corrects c2.** c2 cited BEIR's *"BM25 is a robust baseline… dense often underperform"* as a caution against oversold semantic search — from the **abstract**. c3 read the **body** and found BEIR itself says that headline is partly a lexical-bias artifact. c3's gloss: *"This is Buckley et al.'s 2007 prediction coming true fourteen years later, and it means BEIR's headline result that 'BM25 remains a strong baseline for zero-shot text retrieval' is partly an artifact of who built the benchmarks."* **Textbook abstract-vs-body: two blind runs, same paper, opposite readings — the one that opened the body wins.**

### ★★ The metric for lost independence exists — my prediction was wrong

**Bommasani, Creel, Jurafsky, Kumar & Liang (Stanford), "Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization?", NeurIPS 2022, arXiv:2211.13972 — PRIMARY-BODY.**

- The metric: *"we measure individual-level outcome homogenization… by **normalizing the observed rate of systemic failure by the expected rate of systemic failure**."*
- **★ Why accuracy cannot see it:** *"by looking at accuracy alone, these settings are indistinguishable, whereas they differ considerably in terms of the number of observed systemic failures. Our measures correctly identify discrepancies in these settings, even though the underlying error rates are the same."*
- **What it needs:** per-individual outcomes from every decision-maker, aligned item-by-item — *"we often lack individual-level information (e.g. due to privacy concerns)."* **Item-aligned outcomes, NOT ground-truth labels** — which is materially cheaper than Kohli 2026's requirement.
- Confirms shared inputs drive it: *"the use of the same training data leads to greater outcome homogenization than the use of different (but identically distributed) training data"* — with the caution *"data sharing alone does not fully characterize homogeneity."*
- Distinguishes itself from Kleinberg & Raghavan: *"their formalism considers harms experienced by decision-makers, whereas we center decision-subjects."*

### ★ Kleinberg & Raghavan — the same misreading caught twice, independently

c3 (PRIMARY-FULL, arXiv v2): *"narrower than its reputation and **not** a model of shared-query search agreement"*; mechanism is a Braess' paradox in hiring: *"for any θH, there exists θA > θH such that using the algorithmic ranking is a strictly dominant strategy for both firms, but social welfare would be higher if both firms used human evaluators."* And: *"The sentence usually quoted for the correlated-failure idea is actually its framing of **others'** concerns."*

**Run 1 and c3 independently read the body and reached the same correction.** Genuine corroboration (with the same-family caveat).

### ★★ Cutter 1876 — Ginsburg's type 3, stated 125 years earlier

**Cutter, *Rules for a Dictionary Catalogue*, Rules 101–103 — PRIMARY-BODY:**

- *"Of two exactly synonymous names choose one and make a reference from the other."*
- Naming the failure: *"there is no reason for increasing the evil by separating headings that are really synonymous, certainly not for **dividing a subject in this way for verbal causes and giving no hint that it has been divided**."*
- **★ And vocabulary drift over time — this is Ginsburg 2001's type 3, in 1876:** *"I am told that medical nomenclature has changed largely three times within the present century. How is the cataloguer, unless he happens to be a medical man, to escape occasionally putting works on one disease under three different heads?"*

**⚠ ID conflict flagged, not resolved:** the Gutenberg text is *"Rules for a Dictionary Catalogue," Third Edition*; the 1876 first edition was *"Rules for a **Printed** Dictionary Catalogue."* **Rules 101–103 were read in the Third Edition, not the 1876 text.**

### ★ Garfield 1955 — independently corroborated

c3 reached **PRIMARY-BODY** on Garfield 1955 and returned the *same* load-bearing quotes as run 1: *"even an ideal standardization of terminology and nomenclature will not solve the problem of subject analysis"*; *"Since 1873 the legal profession has been provided with an invaluable research tool known as Shepard's Citations."* **Two runs, one contaminated and one clean, same primary, same quotes.**

### ★ Forensic catches (c3's evidence hygiene is the best of any run this session)

- **★ Roget dating, by anachronism:** *"this Gutenberg text is credited to Roget and titled without an edition, but **it cannot be the 1852 text — it contains 'put in orbit, send into orbit, launch'. Roget died in 1869.** This is an unmarked later revision."* Roget's own 1852 preface: **could not retrieve.**
- **★ Third distortion caught this session.** A search engine rendered Furnas as *"on average 80% of the times different people (experts in the same field) will name the same thing differently."* c3: *"**that sentence is not in the abstract**, and it conflates two different figures: the <0.20 agreement rate, and the 80–90% figure, which is the **simulated failure rate of a design methodology**, not a rate of people disagreeing."* (Prior two: Pass B's fabricated gwern quote; run 1's Petersen 2021 misattribution.)
- **Furnas blocked again** — *"ACM returns Cloudflare 403 to both safefetch and direct download, and Semantic Scholar's listed open-access PDF resolves to that same blocked ACM URL. I have not read this paper's body and do not claim its methods."* **~6 consecutive failures across all passes.**
- Honest downgrades: PRESS *"named as a pointer, not as verified content"*; Soundex flagged for *"internally impossible"* source detail (*"Pittsburgh, Philadelphia"*); Zobel 1998 read only *through* Buckley's body, labelled SECONDARY.

### ★★ c3's gap statement — the precise, scoped answer

> *"I looked for and did not find **any benchmark, metric, or system that measures correlated failure across multiple machine novelty-checkers given the same idea in the same wording** — the second failure mode has owners in adjacent settings (Bommasani et al.'s homogenization metric; log-linear capture-recapture interaction terms; TREC's pooling diversity requirement) but I found none of them applied to novelty checking, and **no benchmark reports how many independent machine searchers agreed wrongly on the same idea**. Also not found: any automation of PRESS's second-librarian search peer review; any capture-recapture estimate of what a machine novelty-checker missed; and **any published measurement of whether ensembling novelty-checkers that share an embedding model or a Semantic Scholar backend buys real independence**."*

---

## 2e. ✅ Run c1 (opus, reads blocked) — VALID BLIND DRAW, and it found the paper that owns the whole thing

**Contamination check — PASSES.** `dashboard` 0 · `[redacted-employer-term]` 0 · `reminder` 0 · `FLF` 0. Reached Lorenz (1) and stemmatics (1); **0** for Kish, Broomell, Clemen, design-effect. **Third clean draw, and again near-disjoint** from c2 and c3 (see §3).

### ★★★ Blair & Maron 1985 — the entire phenomenon, measured, two years before Furnas. VERIFIED BY ME.

**Blair, D.C. & Maron, M.E., "An Evaluation of Retrieval Effectiveness for a Full-Text Document-Retrieval System," *CACM* 28(3):289–299, March 1985.**

**I downloaded the PDF and grepped the primary myself** (safefetch returned an empty DOM; `curl` + `pdftotext`, 11pp, 1228 lines). **Every load-bearing string c1 quoted is present and verbatim** — `air truck` ✓, `Roman circle` ✓, `wire warp` ✓, `impossibly difficult` ✓, `ran out of time` ✓, and the contexts match.

- **The general statement, verified in context:** *"Stated succinctly, it is **impossibly difficult for users to predict the exact words, word combinations, and phrases that are used by all (or most) relevant documents and only (or primarily) by those documents**, as can be seen in the following examples."*
- **The belief/reality gap — the headline:** the lawyers *"stipulated that they must be able to retrieve at least 75 percent of all the documents relevant to a given request."* Measurement began only once *"the lawyer stated in writing that he or she was satisfied with the search results for that particular query (i.e., in his or her judgment, more than 75 percent of the… documents had been retrieved)."* **They believed 75%. They were getting ~20%.**
- **★ The confidence mechanism, stated outright** — why the clean search felt conclusive: *"they will have seen only the retrieved set of documents and not the total corpus of relevant documents; that is, they have seen that the proportion of relevant documents in the retrieved set (i.e., Precision) is quite good (around 80 percent)."* **You see your precision; you cannot see your recall. So a clean, high-precision search reads as thorough.**
- **★ The vocabulary chain, verified in context:** relevant unretrieved documents called the same thing *"the 'wire warp'"*, then *"a third and novel way: the 'shunt correction system'"*, then *"the 'Roman circle method'"*, then — *"Further searching revealed that the system had been tested in another city, and all documents germane to those tests referred to the system as the **'air truck.'** At this point the search ended, **having consumed over an entire 40-hour week of on-line searching, but there is no reason to believe that we had reached the end of the trail; we simply ran out of time**."*
- **Scale of the miss:** one request had 3 key terms; the authors later found *"26 other words and phrases that retrieved additional relevant documents"*; another had 4 terms, later enlarged *"by 44 additional terms."*

**This is the composite — coined/divergent vocabulary → search misses → clean result → false confidence — measured, with the confidence mechanism explained, in 1985.** It predates Furnas 1987, and it owns *more* of the loop than Furnas does (Furnas measures naming variance; Blair & Maron measure the **belief/reality gap** *and* name why the searcher can't see it). **"We simply ran out of time"** is Martyn's 1964 iceberg, again, independently.

**No agent in any pass — eleven now — reached Blair & Maron.**

### ★★ Knight & Leveson 1986 — my "reliability engineering" prediction was RIGHT, and only 1 of 3 clean runs found it

**Knight, J.C. & Leveson, N.G., IEEE *TSE* SE-12(1):96–109, Jan 1986 — PRIMARY-BODY.** N-version programming: 27 independently-developed versions, one million tests.

> *"There were twenty seven versions (i.e. N = 27), one million tests were executed (i.e. n = 1,000,000), and the number of tests in which more than one version failed was 1255 (i.e. K = 1255). With these parameters, the statistic z has the value 100.51. This is greater than 2.33 which is the 99% point in the standard normal distribution, and so we reject the null hypothesis with a confidence level of 99%."*
> *"clearly the only potential problem with the model is that it is derived from the assumption of independent failures. **Thus, we reject this assumption**."*

**The independence assumption, destroyed experimentally, in 1986.** Independently-built versions fail together. This is the exact general form of failure mode 2 — and it is the **reliability engineering** antecedent I pre-registered in §1. **c1 found it; c2 and c3 did not.** My prediction was right about the field and wrong about the reachability: **1 of 3 clean draws.**

**★ Leveson's own archive annotation, which is the phenomenon at one more level up:** *"Our original paper that got us in such hot water for the next ten years until everyone who tried to show we were wrong, got the same results and grudgingly admitted we were right."*

**Two conflicts flagged, not resolved:** (1) UVA Libra dates it **1985**, *"Multi-Version"* hyphenated, authors *"Leveson, Nancy; Knight, John"*; IEEE TSE is **1986**, *"Multiversion"*, *"Knight, J.C.; Leveson, N.G."* — probably a tech-report/journal split, but the metadata disagrees. (2) **A widely-circulated KTH seminar summary reports z = 100.55; the paper says 100.51.** c1's note: *"The summary is wrong. Flagging because it is exactly the kind of number that propagates without anyone opening the source."*

### ★★ The stopping problem — certification exists, and cannot port to the open literature

**Lewis, D.D., Yang, E. & Frieder, O., *CIKM '21*, arXiv:2108.12746 — PRIMARY-BODY.**

- *"Most stopping rules for one-phase TAR workflows lack valid statistical guarantees"* and — *"with one narrow exception, previously proposed certification rules **fail to meet their purported statistical guarantees**."*
- They ship two that do: **QPET** and **QBCB**.
- **The precondition, which is the whole answer:** *"Certification rules… use a **random sample** to provide a formal statistical guarantee that the stopping point has been reached."* c1's gloss: *"That is the price of admission: a labeled random sample drawn from a **bounded, enumerable corpus**. It does not port to an open-web searcher, because **you cannot random-sample 'the published literature'**."*

**This is the sharpest statement of the identification constraint found anywhere.** "Nothing more is there" *is* certifiable — with a valid guarantee — **iff the corpus is bounded and enumerable.** The open literature is neither. That is why Martyn (1964), Garfield (1991), and Shahid et al. (2025) all hit the same wall, and it converts my withdrawn "unobservable by construction" into something precise and true: **the guarantee requires a sampling frame, and prior-art search has none.**

### ★★ The agreement problem in machines — measured twice, concurrently, and both need what a novelty verdict can't give

**CAPA — Goel, Strüber, Auzina, Chandra, Kumaraguru, Kiela, Prabhu, Bethge & Geiping (Tübingen/ELLIS/Stanford), arXiv:2502.04313, ICML 2025 — PRIMARY-BODY.** 130 models, similarity computed **only against models from different developers** (excludes distillation as a confounder).

- *"It could undermine benefits from using LM juries by compromising independence and amplifying collective biases. Most concerningly, our results indicate that **as model blind-spots get harder to detect, making us defer more to AI oversight, models also make more similar mistakes**, posing safety risks from correlated failures."*
- *"We find a significant (p<0.01) positive correlation (**average Pearson r=0.84**) between LLM-as-a-judge scores and model similarity."* — **judges prefer models similar to themselves.**
- **★ What it needs, and why it can't be used here:** *"Like much work on benchmarking, we had to limit to MCQ tasks as the science of precisely evaluating free-text is still evolving… **We hope the community takes up the challenge of designing similarity metrics for free-response text and reasoning**."* **CAPA requires per-item ground truth on multiple-choice. A novelty verdict and a search trajectory are free text.**
- **Internal conflict, reported not resolved:** the abstract expands CAPA as *"Chance Adjusted Probabilistic **Agreement**"*; the introduction says *"Chance Adjusted Probabilistic **Alignment**."* One occurrence each.

**Kim, Garg et al. (Cornell), arXiv:2506.07962, ICML 2025 — PRIMARY-BODY.** 350+ models.
- *"on Helm, pairs of models agree on average about **60% of the time when both models are incorrect** (choosing between incorrect answers uniformly at random would lead to an agreement rate of 1/3)."*
- *"**while within-model generative diversity is a concern, using multiple different models is not a panacea**."* / *"larger and more accurate models have highly correlated errors, even with distinct architectures and providers."*
- c1's note, worth keeping: *"This paper and Goel et al. are concurrent and cite each other, so they are two genuinely independent measurements agreeing — which, given the subject, is worth noting as ironic but real."*

### ★ Lorenz 2011 — c1 got the body; c2 only got a snippet

**PRIMARY-BODY, N=144:** *"the convergence of estimates significantly boosts individuals' confidence. **This confidence gain happens despite a lack of improvements, giving evidence for a psychological trap whereby individuals are led into the false belief of collective accuracy as a result of their convergence.**"* / *"social influence undermines the wisdom of crowds by **boosting the subjective and decreasing the objective reliability** of the crowd."*

**Note the division of labour across clean runs:** c1 read the body; **c2 read only a snippet but caught the 2012 PNAS rebuttal** (*"Social influence benefits the wisdom of individuals in the crowd"*) that c1 did not flag. **Neither run alone is right about Lorenz.**

### ★ CiteME — and why it cannot measure false novelty

**Press et al., *NeurIPS 2024 D&B*, arXiv:2407.12861 — PRIMARY-BODY.** *"CiteME reveals a large gap between frontier LMs and human performance, with **LMs achieving only 4.2-18.5% accuracy and humans 69.7%**"*; humans took *"an average of only 38.2 seconds."* CiteAgent (GPT-4o) 35.3%; Claude 3 Opus 27.7%.

**★ The error taxonomy (§5.1, n=50) is the on-target part:** **50% "Misunderstands the Excerpt"** — worked example: the agent searched `"Reed text-guided image generation conditional GAN"` when it should have searched `"conditional GAN"` — **i.e. deriving search terms from the input's own wording and picking the wrong ones.** 32% *"Understands the Excerpt but Stops Prematurely"*, of which *"in 12.5% of such cases, **the correct paper appeared in the search results but was not chosen**."* 18% finds the correct citation and still stops.

**The limit, from the body:** every instance *"has a correct answer by construction"*, so CiteME measures *failure to find* but **"never presents the machine with the option of correctly concluding 'not present.' It cannot measure a false-novelty rate."**

### ★ Beel et al. — independently corroborates run 1, and adds the footnote run 1 omitted

**PRIMARY-BODY, arXiv:2502.14297 §2.3:** *"To determine novelty, the AI Scientist queries the Semantic Scholar API… **If no clear matches are found, it assigns novel=True**."* Measured: *"the AI Scientist classified all 10 generated ideas and both seed ideas as novel, despite some being well-documented… micro-batching for SGD (Idea 7) is a known technique."* **12/12.**

**★ The authors' own hedge, which run 1 did not report:** *"In prior tests, the AI Scientist occasionally flagged some ideas as non-novel, **showing that it does not always default to a 'novel' classification**."* **The clean run is more honest about the headline than the contaminated one was.**

### ★ Fourth and fifth distortions caught this session

- **Fabricated quotes:** a search engine attributed to arXiv:2502.14297 the phrases *"shallow keyword search over abstracts via the Semantic Scholar API"* and *"routinely mislabels well-established ideas as novel."* c1: **"Neither string is in the paper (`grep -c` returns 0 for both)."** Actual wording: *"relying on simplistic keyword searches rather than profound synthesis"* / *"several generated research ideas were incorrectly classified as novel."* c1's verdict: ***"The gist survives; the quotes do not."***
- **arXiv retitling, three titles for one ID:** 2502.14297 is v1 *"An Evaluation of Sakana's AI Scientist… 'Artificial General Research Intelligence' (AGRI)?"*; v3 HTML body *"…'Artificial Research Intelligence' (ARI)?"*; current abs page *"Evaluating Sakana's AI Scientist: Bold Claims, Mixed Results, and a Promising Future?"* (Pass B logged the same pattern on 2603.20884.)
- **Furnas blocked for the ~7th time.** c1: *"OpenAlex reports `oa_status: bronze` with the only location being `dl.acm.org`, which is Cloudflare-blocked; `any_repository_has_fulltext: false`. So my recalled '<0.20' and '80–90% failure rates' figures remain **unverified against the body**."* Plus a Semantic Scholar duplicate-record conflict (journal vs tech-report version). **The most-cited number in this literature has been read exactly once across eleven agents — by Pass B, via a PSU course mirror.**

### ★ c1's unverified list, and one genuinely new name

c1 **explicitly enumerated everything it did not open** — Roget 1852, Cutter 1876, Index Medicus 1879, Beilstein 1881, Soundex 1918, Lancaster's MEDLARS 57.7%/50.4%, Cranfield II, Greenhalgh & Peacock 30%/51%, Saracevic & Kantor, Zhao & Callan 30–40% term mismatch, TRIZ, MAC/FAC, Swanson 1986, **Maas 1927 and *errores coniunctivi***, the Butler Review, covariance intersection, Ladha, Kuncheva & Whitaker, Kleinberg & Raghavan, Bommasani, MeSH/SKOS/ISO 25964, IPC/CPC/F-terms. *(Note: it recalled Maas/stemmatics independently — matching Pass B — but left it unverified.)*

**★ "Where I'd look that you would not," refined by what verification showed** — and this is a new name:
1. **Reliability engineering** — *"Knight & Leveson is not an analogy — it is the same claim, tested, with a z-score, and Leveson's own note records that the field spent a decade refusing it, **which is itself the agreement problem**."*
2. **Philology/stemmatics** — *"the only field I know that treats agreement as **evidence of dependence** rather than confirmation — shared error proves shared ancestry — which is the exact inversion your failure mode needs, and **I found no one applying it to machine searchers**."*
3. **★ Distributed data fusion — *"where this failure has a proper name — **'data incest'**."*** **A field-standard term for exactly this, reached by no prior agent in any pass.** RECALLED, unverified.
4. **Metrology's interlaboratory comparisons** — *"which exist to detect correlated bias across supposedly independent labs."* RECALLED.

---

## 3. Synthesis — COMPLETE (3 valid blind draws: c1, c2, c3)

### 3.1 — The near-disjointness is the headline methodological result

Three same-family clean draws on an identical frozen brief. **Bibliographic overlap between them is close to zero:**

| Source | c1 | c2 | c3 |
|---|---|---|---|
| Blair & Maron 1985 | ✓ | — | — |
| Knight & Leveson 1986 | ✓ | — | — |
| Lewis/Yang/Frieder (TAR certification) | ✓ | — | — |
| CAPA / Cornell correlated-errors | ✓ | — | — |
| CiteME | ✓ | — | — |
| Buckley et al. (TREC pooling) | — | — | ✓ |
| Shahid et al. (Idea Novelty Checker) | — | — | ✓ |
| Bommasani (homogenization) | ✓ (recalled, unverified) | — | ✓ (primary) |
| Pennell & Reichler (climate) | — | ✓ | — |
| Dickersin 1994 / Spoor 1996 | — | ✓ | — |
| Cutter 1876 | ✓ (recalled) | — | ✓ (primary) |
| Garfield 1955 | ✓ (secondary) | — | ✓ (primary) |
| capture–recapture | — | ✓ | ✓ |

**Each run found a different owner of the same phenomenon.** This is `feedback_fanout_agreement_not_independence` inverted into a *positive* result: **the union is the payload, and three draws produced three largely non-overlapping unions — meaning no draw is close to covering the space, and the "consensus" of any smaller fan-out would have been an artifact of which draw you happened to run.** Pass B's five same-briefed agents produced *one* union. Three blind cross-model draws produced three.

### 3.2 — Scorecard against §1's sealed predictions — FINAL

| Prediction | Outcome |
|---|---|
| Agreement-without-ground-truth cell **empty** | **WRONG broad / RIGHT narrow.** Metrics exist (CAPA, Cornell, Bommasani, capture–recapture log-linear, climate n_eff) — **but every one needs per-item ground truth or MCQ outcomes.** Goel et al. state outright that free-text similarity metrics *"do not yet exist."* **For free-text novelty verdicts sharing a query, the cell IS empty** — which is the correctly-scoped version of the claim. |
| General antecedent = **reliability engineering** | **RIGHT, and found by only 1 of 3 draws.** Knight & Leveson 1986 is the independence assumption killed experimentally (z=100.51). c2 and c3 never reached it. Had I run only c2/c3 I would have scored this prediction WRONG. |
| An **agent-side MeSH/CPC** exists | **NOT FOUND — 3/3 clean draws.** What exists for machines: learned embeddings (SPECTER), facet reranking, TAR certification. **No maintained concept authority. The human answer has no machine port.** |
| Runs **won't reach** the 2025–26 agent literature from a neutral brief | **WRONG — 2 of 3 reached it** (c1: Beel, Si, CiteME, CAPA, Cornell; c3: Shahid et al.). c2 didn't. **It is reachable, but not reliably.** |
| **≥1 run surfaces a field no prior agent reached** | **HIT, overwhelmingly.** Blair & Maron 1985, Knight & Leveson, TAR certification, CiteME, CAPA, Cornell, TREC pooling, climate science, data incest. Base rate **6-for-6**. |

**My priors were wrong or mis-scoped on 4 of 5.** The two that survive (reliability engineering; no agent-side MeSH) survive *because* the blind draws checked them — and one survived on a single draw out of three. **This is the strongest vindication of the two-frozen-passes protocol in the entire investigation**, and it only counts because §1 was sealed before any run returned.

### 3.3 — The answer, triple-confirmed by three independent routes

All three clean draws converged on the same gap **by different evidence**:

- **c1:** *"no metric of independence between search agents sharing a query — CAPA and the Cornell work both require per-item ground truth on multiple-choice benchmarks, and Goel et al. state outright that free-text similarity metrics do not yet exist."*
- **c2:** *"a single, named, cross-domain discipline that treats 'several independent-seeming searchers converging on the same wrong answer' as its own measured problem… not found. What exists is scattered across climate science, ensemble ML, decision analysis, survey statistics, intelligence tradecraft — **each with its own vocabulary, none citing the others**."*
- **c3:** *"no benchmark reports how many independent machine searchers agreed wrongly on the same idea… [nor] any published measurement of whether ensembling novelty-checkers that share an embedding model or a Semantic Scholar backend buys real independence."*

**And all three independently arrived at the one-directional-measurement constraint** — c3 from Shahid et al.'s design note (*"we focus on the 'not novel' cases"*), c1 from Lewis et al.'s sampling-frame requirement and CiteME's construction, c2 from capture–recapture's dependence assumption. **You cannot build ground truth for absence without a sampling frame, and prior-art search has no sampling frame.**

**The phenomenon, one level up:** the countermeasure literature is itself fragmented by naming — *"each with its own vocabulary, none citing the others"* — and the field that treats agreement as *evidence of dependence* rather than confirmation (stemmatics) has never been pointed at machine searchers. **The remedies have the disease.**

### Scorecard against §1's pre-registered predictions — updated

| Prediction | Outcome |
|---|---|
| Agreement-without-ground-truth cell **empty** | **WRONG, twice over.** Bommasani's homogenization ratio (needs item-aligned outcomes, not labels); capture–recapture log-linear interaction terms; TREC pooling diversity; climate science's effective model count. |
| General antecedent = **reliability engineering** | **WRONG.** Never reached by either clean run. Real owners: IR evaluation (NIST), ML monoculture, climate science, decision analysis, survey statistics. |
| An **agent-side MeSH/CPC** exists | **NOT FOUND — confirmed by both clean runs.** What exists for machines is learned embeddings (SPECTER) and facet-based reranking, not a maintained concept authority. **The human answer has no machine port.** |
| Runs **won't reach** the 2025–26 agent-novelty literature from a neutral brief | **MIXED — 1 of 2.** c2 didn't (no Sakana/Beel/AI Scientist). **c3 did**, and went straight to the best measurement in it. |
| **≥1 run surfaces a field no prior agent reached** | **HIT again** — IR evaluation / TREC pooling (c3), climate science (c2). Base rate now **5-for-5**. |

**Four of five pre-registered predictions were wrong or mixed.** They were my socialized priors; both blind draws beat them. **This is the strongest single vindication of the two-pass protocol in the whole investigation** — and it only worked because the predictions were sealed before any run returned.

### What the clean draws establish about c2 vs c3

**The two clean runs share almost no specific sources.** c2: climate science, Dickersin, Spoor, SPECTER, MeSH, Cochrane, MPEP §904. c3: TREC pooling, Idea Novelty Checker, Bommasani, Cutter, Roget, Garfield 1955. **Overlap is thematic, not bibliographic.** Per `feedback_fanout_agreement_not_independence` this is the useful outcome — **the union is the payload, and two same-family draws produced near-disjoint unions**, which is evidence the space is broad and neither draw is close to covering it.

**⚠ Consequence for run 1's rehabilitation:** c2 corroborated Lorenz/Kish/Clemen; **c3 reached none of them.** So those items are reachable but *not reliably* — one clean draw out of two. **Run 1 stays invalid, and its items are corroborated at 1-of-2, not confirmed.**

**No valid blind draws exist for this question.** Nothing in §2 may be reported as a blind-pass finding. Run 1's *verification* work (seven primaries read, including the Beel et al. 12/12-false-novel measurement and the Kleinberg & Raghavan boundary correction) is retained in `machinery-raw/` as **ordinary verified research, explicitly not as evidence about where the concept lives** — it read the project's own candidate list before answering.

**The pre-registered predictions in §1 remain unresolved and sealed.**
