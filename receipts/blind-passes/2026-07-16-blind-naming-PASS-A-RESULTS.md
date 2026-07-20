---
title: "Blind naming — the idiolect trap — PASS A RESULTS"
date: 2026-07-16
kind: research data
status: "evidence ledger — 3 blind runs complete. Contribution is the UNION of fields added, NOT a reversal of Pass B (see §1). Verification debt in §7."
prompt: 2026-07-16-blind-naming-PASS-A-PROMPT.md
sibling: 2026-07-16-targeted-prior-art-search-RESULTS.md (Pass B — verification; revised after its own Codex review 2026-07-16)
protocol: 30_reference/novelty-protocol.md §2 (two frozen passes) · §3 (reverse the question)
method: "Frozen brief (prompt lines 23–67) extracted verbatim, sha256 6f9fd68fbe782371b11d1c2bdd5806611972c67f1feb2fa0582de45ed62ef8f7. Run via headless `claude -p` from a neutral scratchpad cwd (no vault file access, no project docs, no CLAUDE.md inheritance), tools restricted to WebSearch + bare safefetch. Three runs across three models (default / opus / sonnet) — cross-model spread deliberate, to lower what the draws SHARE (feedback_fanout_agreement_not_independence)."
reviewed: "Codex doc-review 2026-07-16 → MAJOR REVISION, 9 findings, ALL accepted. The review caught that this file's entire §1 was benchmarked against a superseded Pass B (see §0). Every defect was in the synthesis layer; no agent datum was wrong."
note: "Absence claims here mean 'not found in the recorded searches' — never 'does not exist.' Convergence across runs is NOT independent confirmation (shared training corpus). The UNION of fields named is the payload, not the agreement count."
---

# Blind naming — Pass A results

**Why this pass exists.** Every field name in the Pass B investigation traced to one source: the orchestrator's own elicitation, produced while socialized into the project's framing. n_eff = 1 on candidate generation. Verification cannot repair that — it only checks candidates you already have. This pass tests whether an unprimed agent reaches the same anchors (corroboration) or somewhere else (the valuable outcome).

**Blindness attestation.** The brief was extracted mechanically from the frozen prompt (lines 23–67 — no frontmatter, no framing note) and piped to sessions started outside the vault with file tools denied. No project vocabulary, no candidate terms, no owners, no prior conclusions reached the runs. The runs could not read this vault, its CLAUDE.md, or the Pass B results. Three models: default, opus, sonnet. Verbatim outputs in `pass-a-raw/`.

---

## 0. ⚠ Read this first: the correction that reframes the whole file

**The first draft of this file claimed Pass A "killed Pass B's two central negative claims." That was wrong, and the way it was wrong matters more than the claim did.**

I read Pass B once at session start and built this entire synthesis against that snapshot. **Pass B was revised on disk while Pass A was running** — it went through its own Codex review (9 findings, 7 accepted in full, 2 narrowed), withdrew the exact sentence I was attacking, and — decisively — **obtained the Larsen & Bong 2016 full text**, which moved its novelty position further than anything Pass A found. I never re-read before writing claims about it. A Codex review of this file caught it at confidence 1.0.

**What Pass B's own primary-text read established, before Pass A ran** (all `primary-full`):

- **Vocabulary → search-recall failure → incomplete review**, under L&B's own heading *"Consequences of the Construct Identity Fallacy"*: *"When researchers search for a construct in an online repository of journal articles, the name of that construct can neither be trusted to elicit high recall (a consequence of jangle) nor high precision (a consequence of jingle). An incomplete understanding of the many names for a construct will lead to literature searches that are incomplete."*
- **Coined name → perceived novelty → reinvention:** *"The renaming of an existing construct (jangle fallacy) may increase the perceived novelty of a construct."* Plus Wilhelm (2009) quoted in a display box: *"If you commit a jangle fallacy your work is akin to the reinvention of the wheel."*
- **And it MEASURES the retrieval failure:** *"participants could detect relevant articles containing a specific construct on average only 9% of the time, and relevant articles containing a pair of common constructs on average only 3% of the time."* With their own novelty claim: *"We are aware of no other assessments in the literature regarding the human ability to find constructs."*
- **Explicitly extending Swanson:** *"We provide evidence that the search for knowledge is more complex than suggested by Swanson (1986)... we found the vast majority of discovered knowledge is hidden from the individual researcher by the very nature of the search process itself."*

**Consequences for this file, applied throughout:**

1. **Ginsburg 2001 does not "compose more of the loop than CIF 2016."** The reverse is true. L&B owns coined-name → failed-search → perceived-novelty → reinvention, **with numbers**. Ginsburg owns nomenclature-change → blameless invisibility, **diachronic, with no search step and no novelty inference**. L&B owns strictly more. §1.1 is rewritten accordingly.
2. **Pass A did not reverse Pass B's measurement null.** L&B's 9%/3% is *closer* to the mechanism→rate cell than anything Pass A found (Martyn measures generic duplication; Bramer measures systematic-review recall). Pass B's revised framing already accounts for this.
3. **Pass B's current framing is the better-evidenced one, and this file defers to it:** *"the composite is unnamed in the recorded searches, but it is much closer to owned than 'every part has an owner' suggests — Larsen & Bong 2016 owns the causal chain from coined name to failed search to reinvention, and measures it; what is left unclaimed is the null-as-evidence step, the self-referential case, and the agent twist. Anyone pitching this as new must clear Larsen & Bong 2016 first, by name and by number."*

**The lesson, and it is the file's own thesis eating the file for a third time:** Pass B's postscript records that *"five blind agents, ~200 tool calls, and a Codex review all failed to surface this, because none of them read the paper."* **Pass A's three blind runs also failed to read it** — all three had the L&B citation; none reached the body (verified: no run output contains the 9%/3% figures). **The citation was never the bottleneck. Reading was.** Fan-out does not substitute for reading the load-bearing source, and a fourth, fifth, and sixth agent did not help.

---

## 1. What Pass A actually contributes

**Not a reversal. A union.** Pass B's nulls were already withdrawn or narrowed by its own L&B read. Pass A's value is (a) corroborating that Pass B's named anchors are independently reachable, and (b) adding roughly a dozen fields Pass B never touched — which does not refute Pass B's nulls but **does further weaken the coverage confidence behind them**.

### 1.1 — Ginsburg 2001: a closer partial antecedent, not the composite

**Ginsburg, I. 2001, "The Disregard Syndrome: A Menace to Honest Science," *The Scientist* 15(24):51 — I read the full primary myself** (https://www.the-scientist.com/the-disregard-syndrome-a-menace-to-honest-science-53924). Run 1 found it; all three of its quotes are real and verbatim. Ginsburg's third of three types:

> *"An unintentional lack of regard for relevant literature due to ignorance of a change of nomenclature."*

Type-specimen: *"In 1975, the chemical structure of SF was identified and renamed 'lipoteichoic acid' (LTA). Since the introduction of the new nomenclature, the pioneering papers on SF have rarely been cited in the vast literature on LTA (more than 200 publications)."* Consequence: *"There is a growing concern that the disregard syndrome has already contributed to the disappearance of whole lines of research from the awareness of investigators."*

**What Ginsburg owns:** nomenclature change → unintentional, **blameless** literature invisibility → rediscovery. The blameless framing is a genuine addition — Pass B's nearest relatives (negligence, amnesia) all impute fault, which is exactly why Ginsburg split this out as a separate type.

**What Ginsburg does NOT own:** the group's own coinage as cause; the search-returns-nothing step; the clean-null → confident-novelty inference. **Two boundaries, both from the primary:**

- **Diachronic, not synchronic.** SF→LTA is one field renaming its own molecule in 1975, after which its own earlier papers stop being cited. The project's phenomenon is a group's endogenous coinage diverging from *another field's live vocabulary at the same time*. Related, not identical.
- **His causal story is referee overload, not the searcher's vocabulary:** *"expert referees nominated by journal editorial boards are unable to cover the vast literature to prevent duplications of already published data."*

**Net: L&B 2016 > Ginsburg 2001 > everything else Pass A found, as coverage of the composite.** Ginsburg's contribution is the blameless/lexical *type* and a 2001 date; he does not displace L&B.

**On the "disregard syndrome" coinage — unresolved, and I overstated it.** Ginsburg writes: *"the unethical and self-defeating 'disregard syndrome,' discussed in 1991 by Eugene Garfield."* I fetched Garfield 1991 in full: **the phrase is not in it** — Garfield's terms are *"bibliographic negligence"* and, quoting Merton, *"citation amnesia,"* and he never mentions nomenclature. **But "discussed" is not "named," so Ginsburg's citation is not defective** — he is plausibly attributing the *phenomenon's discussion* to Garfield, which is accurate. My first draft called this a defective citation and counted it as a third kill-verification hit. **Both claims are withdrawn.** What is supportable: *Ginsburg 2001 is the earliest use of the phrase found in the recorded searches; Garfield 1991 discusses the phenomenon under a different name and without the nomenclature mechanism; actual coinage is unresolved.*

**What does survive, and it is still notable:** one phenomenon carries at least three names across Merton → Garfield (1991) → Ginsburg (2001), none citing a shared term. That is the naming-fragmentation pattern, observed — but it is *not* a documented misattribution, and it should not be filed alongside the Aikins→Thorndike→Kelley chain, where the standard credit demonstrably is wrong.

### 1.2 — The measurement question: Pass B's null holds; Pass A adds adjacent measurements it lacked

**Pass B's null, current wording:** the mechanism-specific cell is empty *"in what was reachable,"* the null is *"weak evidence,"* and patent analytics + MeSH evaluation are named as unreached. **That is a properly qualified null and Pass A does not defeat it.** My first draft claimed Pass B *"declared the space mapped"* and was *"blind to the two fields most likely to own it."* Both withdrawn — Pass B stated its own limits.

**What Pass A adds — adjacent, not the cell:**

- **Martyn, J. 1964, *New Scientist* No. 377 (6 Feb 1964), p. 338** — `primary-full` (run 1). 647 scientists surveyed; *"144 of them (22 per cent)"* had discovered literature they wished they had had at the start; of 245 instances, **43 revealed unintentional duplication**; costed at *"about £6 million"* per year, *"equivalent to paying about 750 scientists to do nothing."* — http://garfield.library.upenn.edu/papers/martynjnewscientist1964.pdf. **Measures the OUTCOME (duplication from retrieval failure), not the vocabulary mechanism** — Suber notes Martyn focused on carelessness. **Does not fill the cell.**
- **Bramer, Rethlefsen, Kleijnen & Franco 2017, *Systematic Reviews* 6:245** — `primary-full`, read independently by runs 1 and 2. *"We estimate that 60% of published systematic reviews do not retrieve 95% of all available relevant references."* P(100% recall) = 23%. Expert information specialists conceding the mechanism about their own searches: *"our search strategies, like any other search strategy, still missed some relevant references because relevant terms had not been used in the search."* **Measures retrieval recall, not duplication.** Does not fill the cell.
- **Garfield 1991** — `primary-full` (me). *"At present, there is no way to document support for the assertion that bibliographic negligence is increasingly widespread."*

**Ranking against what Pass B already had: L&B's 9%/3% construct-recall measurement is closer to the cell than either of these**, because it measures *vocabulary-driven retrieval failure for scientific constructs specifically*. Martyn and Bramer are wider and less on-target. **Pass A did not improve on Pass B here.**

**⚠ On "unobservable by construction" — withdrawn.** My draft promoted Martyn's *"we cannot measure this 'iceberg'"* and Garfield's *"no way to document support"* into a structural impossibility claim. **That inference does not hold**: both are statements about the evidence available to those authors, not identification results, and Garfield is not even discussing the lexical mechanism. The honest version: **estimating a mechanism→rate figure faces a real censoring/identification problem — you cannot directly count duplications nobody noticed — and two authors in this literature hit that wall. That is a scoped difficulty, not a proof of impossibility.** Anyone proposing to measure it needs an identification argument; anyone declaring it unmeasurable needs one too.

### 1.3 — Bacon 1620: an older antecedent of the naming half, scoped

**Bacon, *Novum Organum* (1620), Book I, Aphorism LIX (Spedding trans.) — `primary-full`** (run 2) — the Idols of the Market-place (*idola fori*):

> *"Now words, being commonly framed and applied according to the capacity of the vulgar, follow those lines of division which are most obvious to the vulgar understanding. And whenever an understanding of greater acuteness or a more diligent observation would alter those lines to suit the true divisions of nature, words stand in the way and resist the change."*

— https://en.wikisource.org/wiki/Novum_Organum/Book_I_(Spedding). Aphorism LX adds *"names of things which exist, but yet confused and ill-defined."*

**Scoped honestly (my draft overstated this as a "clean kill" and "off by 307 years"):** Bacon is an **adjacent philosophical antecedent of the vocabulary-obstructs-thought half only.** He says nothing about prior-art retrieval, search nulls, rediscovery, or false novelty. What is supportable: *on the naming-obstruction axis, an antecedent exists 307 years before Pass B's oldest anchor (Kelley 1927) — and it states the non-obvious form of the claim (a community's words actively resist correction), not merely that words are vague.* It is not prior art for the composite. **"Clean kill" withdrawn.**

---

## 2. Corroboration audit — per run, pre-search vs post-search

My first draft conflated pre-search recall with post-search discovery and miscounted. Codex caught it. Rebuilt as an audit table against the raw outputs. **"Recalled" = named in the run's own section (A), from knowledge, before searching.**

| Anchor | Run 1 (default) | Run 2 (opus) | Run 3 (sonnet) | Recalled by |
|---|---|---|---|---|
| Furnas 1987 (vocabulary problem) | recalled, `<0.20` | recalled, `<20%` | recalled, **"far less than half"** — got `<0.20` only after search | **3/3 recalled; 2/3 with the exact figure** |
| Kelley 1927 jangle / Thorndike 1904 | recalled | recalled | recalled | 3/3 |
| Swanson 1986 (UPK) | recalled | recalled | recalled | 3/3 |
| Ogburn & Thomas 1922 + Merton 1961 | recalled, flagged adjacent | recalled | recalled, flagged adjacent | 3/3 recalled; **2/3 flagged adjacent pre-search** |
| Ke et al. 2015 (sleeping beauties) | recalled | recalled | recalled (post-search detail) | 3/3 |
| Kuhn 1962 (incommensurability) | — | recalled | recalled | 2/3 |
| Schema matching / ontology alignment | recalled | — (content-addressed instead) | — | 1/3 |
| **Larsen & Bong 2016 (CIF)** | **not reached at all** | **post-search only** — run 2: *"the sharpest task-3 machinery I found, and I did not expect it"* | **post-search only**, via Wikipedia's reference list | **0/3 recalled** |
| Patent prior-art / examiner search | recalled (CPC/IPC classification) | recalled (CPC/IPC classification) | **post-search only, and as citation behaviour (Cotropia 2013) — never CPC/IPC classification** | **2/3 recalled; classification 2/3** |

**Corrections to my first draft, all accepted:** Larsen & Bong was **0/3 from knowledge**, not "2 of 3" — and both runs that found it did so *after* searching, one calling it unexpected. "Patent classification (all 3)" was wrong: 2/3. Furnas's exact `<0.20` was 2/3, not 3/3. "Flagged adjacent **unprompted**" is wrong on its face — **the frozen brief's task 5 explicitly asks for "Adjacent but distinct,"** so adjacency flagging was *solicited*; what is mildly notable is that two runs did it in their *pre-search* section.

**What the audit still supports:** Pass B's core anchors (Furnas, Kelley/Thorndike, Swanson, Merton/Ogburn, Ke) are **independently reachable from knowledge alone by unprimed agents across three models**. The n_eff=1 worry about *what Pass B named* is answered. **What it does not support:** any claim that agreement across runs confirms anything — same training corpus, correlated draws.

**★ The most informative row is the L&B row: 0/3 recalled, 0/3 body read.** The single most load-bearing source in the entire investigation was invisible to blind recall and unread by every agent in both passes. That is the finding.

---

## 3. The two-Swanson-papers problem — independently reproduced

**Pass A reached this independently, by a different route than Pass B.** Run 1, by grepping the *Library Quarterly* primary:

> *"The 'complementary but disjoint / noninteractive literatures' vocabulary belongs to the fish-oil paper and later LBD work — I grepped the Library Quarterly text and the words 'disjoint' and 'noninteractive' do not appear in it."*

Pass B reached the same conclusion via L&B's bibliography (*"Larsen & Bong's bibliography reads 'Swanson, D. R. 1986. Fish oil, Raynaud's syndrome, and undiscovered public knowledge, Perspectives in biology and medicine (30:1), pp. 7-18' — not the Library Quarterly 56(2):103–118 that this sweep and `novelty-protocol.md` cite"*).

**Two independent routes, same defect. This is the one place Pass A genuinely corroborates rather than merely adds** — and it means `novelty-protocol.md` currently cites the wrong Swanson paper.

**Status: hypothesis, not settled** (my draft called it "resolved" and then "unresolved" two paragraphs later — Codex caught the contradiction). The papers:

- *"Undiscovered Public Knowledge,"* **Library Quarterly** 56(2):103–118 — the epistemology of search incompleteness. Run 1's `primary-full` quotes: *"The above-stated hypothesis about a search function, in short, can never be verified. In that sense, an information search is essentially incomplete, or, if it were complete, we could never know it."* / *"The impossibility of verification amounts to a fundamental limitation... the mistaken idea appears to be widespread that one can somehow... insure that all relevant information will be found."*
- *"Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge,"* **Perspectives in Biology and Medicine** 30(1):7–18 — the combinatorial ABC case.

**⚠ Unresolved conflict:** run 2 attributes the Raynaud/fish-oil case and *"the two literatures appear to be remarkably isolated from one another"* to the **Library Quarterly** paper; run 1 says that material belongs to the fish-oil paper. **Both read the same PDF URL.** Needs a direct side-by-side check of both primaries before the split is relied on.

**If the split holds,** the LQ paper supplies the *null-confidence epistemology* and the fish-oil paper the *combinatorial ABC model* — which would dissolve the runs' own disagreement (run 3 made "Swanson" the true home; run 2 called that the biggest risk because UPK is combinatorial and this phenomenon is duplicative). Run 2's independent finding that **Swanson never uses "vocabulary," "terminology," "jargon," or "specialization" anywhere in the LQ paper** is consistent with the split. **But L&B 2016 explicitly extends Swanson and is the better anchor regardless** — see §0.

---

## 4. The union: fields Pass B never reached

This is Pass A's actual contribution. Each is absent from Pass B (checked against the current revision).

- **★★ Biomedical research ethics — Ginsburg 2001, "disregard syndrome" type 3.** `primary-full` (me). §1.1. The blameless nomenclature type. **Ranks below L&B 2016 on composite coverage.**
- **★★ Information science's duplication-cost literature** — **Martyn 1964** (`primary-full`, the £6M/yr outcome measurement); **Garfield 1991, "Bibliographic Negligence"** (`primary-full`, me — via curl+pdftotext; safefetch returned an empty DOM) — *"the omission of pertinent references—what Columbia University sociologist Robert K. Merton once described as 'citation amnesia'"*, plus Pass B's own task-3 answer stated unprompted: *"no responsible scientist would file a patent application without conducting a prior search... The same stringency should be applied in journal publishing."* **Verified in the primary: Garfield never mentions nomenclature or vocabulary** — his mechanism is negligence/padding, so he is *not* an owner of the lexical link. **Garfield 1980, "From Citation Amnesia to Bibliographic Plagiarism"** (`primary-full`, run 1) — *"if the author is not known to you, it is possible that he or she is not familiar with your work. This can happen when the paper is from a different field."*
- **★★ Evidence synthesis / systematic-review methodology** — **Bramer 2017** (`primary-full` ×2), MeSH/Emtree, PRESS, PRISMA-S, Cochrane, hand-searching, citation chaining. Supporting: Rethlefsen et al. 2015, *J. Clin. Epi.* 68(6):617–626 — `snippet-only`, and run 2 flags it establishes *"correlation with reported search quality, not with recall of true prior work — weaker than it is usually cited for."*
- **★★ Philosophy — Bacon 1620, *idola fori*** (`primary-full`). §1.3, scoped. Run 2's older candidate, flagged honestly and **not** relied on: *"Aristotle, Categories (~350 BC), on homonymy and synonymy... I recalled this but did not check it, so do not quote me."*
- **★ Terminology science / onomasiology vs. semasiology** — Wüster 1931, Vienna School → ISO TC 37. *"Onomasiology starts from the concept and asks what names it; semasiology starts from the word. A group searching its own words is doing semasiology when it needs onomasiology."* Reached independently by runs 1 and 2; run 2: *"the cleanest formal statement of your problem I know of, and it predates every IR framing of it."* `secondary-only`.
- **★ Reliability engineering — common-cause failure** (run 2). Why N redundant channels give ~zero extra protection when they share an input — *"comes with quantitative models (beta-factor, IEC 61508) that the social-science framings lack."* `recalled`. Pass B had Kohli 2026 (needs ground truth) and Broomell & Budescu 2009 (latent cues) but not this field.
- **★ Biological nomenclature — ICZN Art. 23.1/23.2, Principle of Priority** (`primary-full`, run 1). *"The valid name of a taxon is the oldest available name applied to it..."* — and the nuance: priority *"is not intended to be used to upset a long-accepted name in its accustomed meaning by the introduction of a name that is its senior synonym"* — *"the profession that solved this best also decided that sometimes the older name should lose."* Strickland Code 1842 date **unverified**.
- **★ Content-addressed retrieval as the escape hatch** (run 2) — *"the fields that actually beat it did so by deleting names from the index"*: OEIS, CAS Registry/InChI, BLAST. `recalled`, citations unverified by the run's own admission.
- **★ Cognitive psychology — Gick & Holyoak 1980**, *Cognitive Psychology* 12(3):306–355: **20% spontaneous transfer, 92% with a hint**. `secondary-only`. Also Einstellung (Luchins 1942), functional fixedness (Duncker 1935/45), streetlight effect (Kaplan 1964).
- **★ Library science — Taylor 1968, question negotiation / the reference interview**, *College & Research Libraries* 29(3):178–194. `recalled`. Plus **Cutter 1876** (authority control / collocation objective).
- **★ Tai 1994** — the trapezoidal rule published as a novel "mathematical model" in *Diabetes Care* 17(2):152–154, rebutted by Monaco & Anderson 17(10):1224–1225. The type specimen of high-confidence reinvention surviving peer review. `snippet-only`.
- **Swales 1990, discourse community** — specialized lexis as a *defining criterion* of a research community: *"your vocabulary isn't a bug of the group, it's constitutive of it."*
- **Intelligence analysis — Heuer 1999, ACH.** Efficacy contested; Dhami et al. 2019 (doi:10.1002/acp.3550) **could not retrieve** — run 2: *"I will not characterize its verdict from the title."*
- **Garvey 1979** — *"in some disciplines, it is easier to repeat an experiment than it is to determine that the experiment has already been done."* `secondary-only` (via Suber).
- Also: LBD as a field (Swanson & Smalheiser); **Stigler's law** (1980); **NIH syndrome** (Katz & Allen 1982 — **conflict**: pp. 7–19 vs 7–20); **prematurity** (Stent 1972); **construct proliferation** (Shaffer, DeGeest & Li 2016); **hidden profile** (Stasser & Titus 1985); **groupthink** (Janis 1972); **Altman & Bland 1995**, *BMJ* 311:485; West Key Number System; Aarne–Thompson–Uther tale-type index; obliteration by incorporation; Robinson & Goodman 2011; ethnoscience/folk taxonomy; cross-lingual IR; Wikipedia's redirect/merge apparatus.

---

## 5. Boundary work — the runs' sharpest output

- **Multiple discovery** — simultaneity + independence are definitional; *"your case has neither — the prior work is decades old and reachable."*
- **Prematurity (Stent)** — *"a premature discovery stays lost under perfect search; yours was one synonym away."* Conceptual gap vs. lexical gap.
- **Incommensurability (Kuhn)** — *"claims terms cannot be translated across paradigms. Yours translate fine; nobody tried. Boundary: impossibility vs. omission. Kuhn is a much stronger and more contested claim — borrowing it inflates your situation."* Both runs that reached Kuhn marked it adjacent; **run 2 supplies the reason to leave it unrun**, answering Pass B's flagged "untouched upstream node."
- **NIH syndrome** — *"they found the prior work and rejected it."* Appraisal vs. retrieval.
- **Citation amnesia / bibliographic negligence (Garfield)** — *"imputes fault or sloppiness; the terminology case is a blameless miss, which is exactly why Ginsburg split it out as a separate type."* Confirmed in the Garfield primary: no nomenclature discussion at all, so the blameless/lexical type really is Ginsburg's addition.
- **Sleeping beauties** — reception vs. reachability. **Streetlight effect** — *"you know the keys are elsewhere and search where it's easy anyway. Yours: the group has no idea an 'elsewhere' exists."*
- **Groupthink** — *"yours needs no suppression: the searchers sincerely and independently agreed because they shared a premise."* Social pressure vs. common-cause correlated inputs. **Hidden profile** — the group *holds* the missing info; yours: nobody does.
- **Stigler's law** — naming vs. finding. **Filter bubble** — exogenous vs. endogenous. **Reinventing the wheel** — names the outcome, silent on mechanism. *(Note: L&B 2016 quotes Wilhelm connecting jangle directly to "reinvention of the wheel" — so this boundary is weaker than the runs thought.)*

**Run 1's proposed name for the briefed-searchers feature: "shared vocabulary priming"** — *"where the correlated error is lexical and the searchers' agreement is an artifact of a common briefing rather than independent confirmation."*

---

## 6. "True home" — all three converged, and that is the weakest evidence here

**All three runs picked information science / LIS.** Per `feedback_fanout_agreement_not_independence`, three same-corpus runs agreeing ≈ far fewer than three votes. **Do not report this as 3/3 confirmation.** Run 1's *reasoning* is the strongest:

> *"Not because it has the best name — 'the disregard syndrome' and 'the jangle fallacy' are both sharper — but because it is the only field that owns the whole object rather than a face of it: Swanson supplies the epistemology of why a clean null cannot license a conclusion, Furnas supplies the measured lexical mechanism, Martyn and Bramer supply the cost and the rate, and Taylor's reference interview and the MeSH/thesaurus tradition supply the countermeasure. **Everyone else — taxonomists, examiners, psychometricians, lawyers — has independently built a partial defence against it, which is itself the phenomenon operating one level up.**"*

Run 2's dissent, preserved: *"a pick under duress: no field owns the compound you described, no field has named it, and the closest thing to a professional home is not a discipline but an occupation — research librarianship, which treats it as a craft problem rather than a research object."* **Both runs were reasoning without L&B's body**, which puts a serious contender in *information systems* (MISQ) rather than LIS. Treat the "true home" verdict as unsettled.

Run 2's unprompted headline is the best one-line statement in the corpus: *"I reached for roughly six unrelated clusters in six literatures, none of which cite each other, and none of which owns the compound. That is itself the answer to 'who owns it': nobody. The phenomenon is distributed across vocabularies in exactly the way it describes."*

---

## 7. Verification debt + integrity notes

**Verified by me, in full primary, this session:** **Ginsburg 2001**, **Garfield 1991**. Both produced corrections to run 1's account (§1.1) — and to my own first draft.

**`primary-full` by the runs:** Bacon 1620; Swanson 1986 LQ (2 runs; plus verified-by-absence for "disjoint"/"noninteractive"); Martyn 1964; Garfield 1980; Bramer 2017 (2 runs independently); ICZN Art. 23; Petersen 2021 (as a correction).

**⚠ The "3-for-3 kill-verification" claim is withdrawn.** My draft counted Ginsburg as a third instance of *"real quote, defective citation."* **It is not a defective citation** — Ginsburg says the syndrome was *"discussed"* by Garfield, not named by him, and Garfield did discuss the phenomenon under another name. The protocol's record stands at **2-for-2**, not 3-for-3. What survives is narrower and still worth acting on: **run 1 got the finding right and the *framing* wrong** (presenting Ginsburg as owning the composite when he owns a diachronic subtype). Do not relay a subagent's owner-attribution without reading the primary — especially when the finding is exciting.

**⚠ Furnas 1987 primary could not be retrieved by any blind run** — run 1: Unpaywall confirms `has_repository_copy: false`; sole OA location `dl.acm.org` is Cloudflare-blocked; no HathiTrust/archive.org copy. All three refused to treat the abstract as the paper. **Pass B did read it** (PSU course mirror). Anchor is fine.

**Priority reads:** (1) **The two Swanson 1986 papers side by side** (§3) — settles run 1 vs run 2, and `novelty-protocol.md` currently cites the wrong one. (2) **Martyn 1964 case-level detail** — what fraction of the 43 duplication cases involve naming? The only thing that could move the mechanism→rate cell; Martyn's iceberg caveat predicts it cannot be recovered from his data. (3) **Gick & Holyoak 1980**, **Wüster/onomasiology**, **common-cause failure**, **Tai 1994**.

**Conflicts reported-not-resolved:** Thorndike p. 10–11 vs 14; Thorndike title *"...Social Measurements"* vs *"...Social Measures"*; Bramer 2017 internal (abstract *"291 / 16%"* vs body *"292 (17%)"*); Katz & Allen pp. 7–19 vs 7–20; Garfield essay volume 1979–80 vs reprint 1980; ICZN Strickland-Code 1842 date; run 1 vs run 2 on Swanson LQ contents.

**⚠ Fabrication watch — 2 across both passes, both caught only by reading primary.** Pass B caught a search engine inventing a gwern quote. **Run 1 caught a search-engine summary attributing a "different terminology" claim to Petersen 2021, *Function* 2(4):zqab030 — the paper contains no such claim; the real source was Ginsburg 2001.** Run 1 fetched the primary and corrected it unprompted. Assume the same rate applies to everything marked `secondary-only`/`snippet-only` here. (Petersen's actual verified mechanism is worth separating: *"What is known about the history of a particular field can therefore effectively be determined by a single review article in a prominent journal"* — inherited error via review articles, not vocabulary mismatch.)

**safefetch injection flag — reviewed, false positive.** Run 1 reports safefetch flagged Peter Suber's page for prompt injection on *"pretend to be."* Run 1 checked context: Suber's own rhetorical framing (*"let me cast myself as a crank"*), nothing addressed to an agent. No action needed; recorded for the audit trail.

---

## 8. What this changes

1. **Pass A does not reverse Pass B.** Pass B's own L&B primary-text read moved its position further than Pass A did, and its current framing is the better-evidenced one. Pass A's contribution is a **union of ~12 unreached fields**, which does not refute Pass B's nulls but **further weakens the coverage confidence behind them** — a null whose coverage keeps turning out to be incomplete is a null nobody should lean on.
2. **The protocol worked, and the union was the payload.** Only run 1 found Ginsburg, Martyn and the Swanson grep; only run 2 found Bacon, onomasiology, common-cause failure and the Swanson-never-says-vocabulary limit. A same-model triple would have missed most of it. The three runs' *convergence* (true home = LIS) is the least informative thing in the file — and is probably wrong, since none of them read L&B.
3. **Novelty status: `open`, not established-novel.** My draft said the synchronic case and mechanism→rate link *"remain unowned"* and that *"there is"* a gap — repeating the exact confident-null error this file documents, two paragraphs after warning against it. **Corrected: not found in the recorded searches.** The recorded searches are exploratory, have no frozen query list or stop rule, and have now been shown incomplete twice.
4. **The measurement arm has a scoped identification problem, not an impossibility.** You cannot directly count duplications nobody noticed; Martyn and Garfield both hit that wall. Anyone proposing to measure the mechanism→rate link needs an identification strategy. **That is a hard-programme warning, not a no-go proof** — and my "unobservable by construction" framing is withdrawn.
5. **Direct input to the FLF go/no-go (2026-07-19 AoE) — user call, not mine.** The bar Pass B set stands and Pass A does not lower it: ***"Anyone pitching this as new must clear Larsen & Bong 2016 first, by name and by number."*** L&B owns coined-name → failed-search → perceived-novelty → reinvention **with 9%/3% recall numbers** and makes its own no-prior-assessments claim. The defensible residue is narrow: the **null-as-evidence step**, the **self-referential case**, and the **agent twist** (Pass B's list, not mine) — plus, from Pass A, the **synchronic vs. diachronic** distinction against Ginsburg. Whether that residue is worth a submission is a judgment about ambition and time, not about evidence.
6. **Coin-time tax — the glossary row, corrected.** *our "idiolect trap"* · *the field's names:* **construct identity fallacy / jangle** (Larsen & Bong 2016 — **the one to clear**), **disregard syndrome type 3** (Ginsburg 2001, diachronic), **the vocabulary problem** (Furnas 1987, the lexical mechanism), **undiscovered public knowledge** (Swanson 1986 LQ — *check which paper*, §3), **idola fori** (Bacon 1620, naming-obstruction half). **Martyn 1964 measures generic retrieval-failure duplication and its cost — NOT "the rate" for vocabulary divergence.** The right column is no longer empty.
7. **Method finding, and it is the sharpest thing here.** `feedback_unreviewed_artifact_assume_wrong` predicted this exactly: **zero agent data were wrong; every defect was in the synthesis layer — including, three times, my own.** I overclaimed §1.1, then §1.2, then benchmarked the entire file against a stale Pass B I never re-read. **New rule earned: re-read a file before making claims about it, even if you read it this session — concurrent revision is real** (`reference_vault_sync_no_git`: Syncthing, no git, no merge conflict to warn you). And: **fan-out does not substitute for reading the load-bearing source.** Between both passes, **eight blind agents and two Codex reviews** had the L&B citation; the two humans-in-the-loop moments that mattered were someone deciding to open the PDF, and a reviewer noticing a stale quote.
