---
title: "Prior-art search — the idiolect trap — PASS B (verification + citation-walk)"
date: 2026-07-16
kind: research prompt
status: ready to paste — NOT YET RUN
pass: "B — verification and citation-walk. This is NOT the blind pass."
parent: 20_areas/thinking/decisions/2026-07-16-flf-no-submit-judge-dependence-prior-art.md
protocol: 30_reference/novelty-protocol.md §2 (two frozen passes)
---

> **Which pass is this, and why it matters.** Per `30_reference/novelty-protocol.md` §2, a novelty check is **two frozen passes**: **Pass A** (blind naming — the agent gets *only* the phenomenon in plain operational language, no candidate terms, no prior conclusions) and **Pass B** (verification + citation-walk — may receive Pass A's candidates).
>
> **This is a Pass B prompt.** It hands over candidate owners, adjacent papers, and a prior absence conclusion, and tells the agent not to re-derive them. It therefore **cannot demonstrate that a blind agent independently found the field's vocabulary** — it is free of *minelit* vocabulary but not of the prior sweep's ontology. Do not cite its output as evidence of a blind pass.
>
> **Pass A already ran** (2026-07-16, two-agent sweep, stripped-language brief) and is what produced the candidates below: Furnas 1987, Kelley 1927, Swanson 1986, the patent-lexicographer angle. Those results are **secondary-sourced and unverified** — verifying them is precisely this pass's job.

# Paste everything below the line into a fresh session

---

You are running a targeted prior-art search. Your output is raw data for synthesis, not a report. Assume every claim you cannot verify against primary text is wrong until verified.

## The phenomenon (stated deliberately in plain terms — this is the whole brief you get)

A research project coins its own terms for the things it studies. Novelty and prior-art searches then run using those coined terms. The searches return nothing, and "nothing found" is read as "nobody has done this," when it actually means "not reachable from this vocabulary." The prior art exists, usually decades old, under an established field's name for the same concept. The result is a *confident* false-novelty conclusion — confident precisely because the null was clean.

The AI-specific twist: when the searchers are LLM agents briefed from the project's own documents, they are socialized into the coined vocabulary at spawn time. They inherit the blind spot rather than correcting it, and multiple agents agree with each other because they share the brief, not because the answer is right.

## What is already established (do NOT re-derive — verify or extend)

A prior sweep found these owners. Some are verified, some are not:
- **Furnas, Landauer, Gomez & Dumais 1987, CACM 30(11):964–971** — "the vocabulary problem"; two people reportedly pick the same term for the same thing <20% of the time. *Verified only via a secondary page.*
- **Kelley 1927** (jingle-jangle fallacies; jangle = assuming two things differ because they are named differently). *Verified via Wikipedia only.*
- **Swanson 1986** — undiscovered public knowledge / literature-based discovery; disjoint, mutually non-citing literatures. *Verified via secondary.*
- **Patent practice** — "applicant as own lexicographer" (MPEP 2173.05(a)); CPC/IPC classification search indexes by function/structure rather than words, as the professional countermeasure to vocabulary variance. *Unverified.*
- **Carpineto & Romano 2012**, ACM Computing Surveys 44(1) — query expansion as the IR countermeasure. *Unverified, fetch-blocked.*
- **Larsen & Bong 2016**, MIS Quarterly 40(3):529–551 — a tool for construct identity / construct proliferation. *Unverified.*

## Your tasks, in priority order

**1. Verify the load-bearing anchors against primary text.** Furnas 1987 (get the actual measured agreement rate and what was measured — do not trust the <20% figure until you see it), Larsen & Bong 2016, Carpineto & Romano 2012, and the MPEP/CPC classification-search claim. For each: quote the sentence that carries the claim. If a PDF resists extraction, say so plainly — a failed fetch is not evidence of absence.

**2. Close an absence claim as rigorously as you can.** The prior sweep concluded that the specific loop — *project coins vocabulary → search runs inside that vocabulary → confident null → false novelty* — is **not named anywhere in the 2023–2026 AI-research-agent literature**, and that only adjacent failures are named (keyword-retrieval brittleness in the Sakana AI Scientist critique, arXiv 2502.14297; "different phrasing → misclassified as novel," arXiv 2506.22026; LLM judges' "novelty mirage," arXiv 2606.12071; recency bias in LLM rerankers, arXiv 2509.11353). **Try hard to refute that absence claim.** Search LessWrong, the EA Forum, the Alignment Forum, Hacker News, research blogs, and workshop papers — not just arXiv. If it is named somewhere, that is the single most valuable thing you can return.

**3. Search these angles the prior sweep never ran.** For each, name the field, its canonical term, and the oldest treatment you would expect to exist:
- **Sociology / STS:** boundary objects (Star & Griesemer 1989), trading zones (Galison), and any work on cross-field translation failure causing duplicated work.
- **Bibliometrics:** quantitative studies of redundant publication, independent rediscovery, or "reinvention" attributed to terminology divergence between fields. Does anyone *measure* this?
- **The countermeasure field:** ontology alignment / schema matching / entity resolution (OAEI campaigns). Is "detect that two differently-worded claims are the same claim" a solved, benchmarked problem? Who owns it and since when?
- **The dependence application (highest value if open):** does anyone use *shared vocabulary or shared framing* as a proxy for **non-independence between sources** — i.e., discounting apparently-corroborating sources because they share a conceptual lineage rather than a citation? Look in information cascades/herding, meta-analysis dependence corrections, stemmatics, and expert-aggregation literature. State plainly whether this is (a) unbuilt, (b) built, or (c) foreclosed by a theorem.

**4. For every kill you find, classify it:** *predated* (someone did it first; an extension remains possible) vs **foreclosed** (it is a theorem or definitional; no experiment can make it a contribution). This distinction matters more than the citation itself.

## Method

Use WebSearch for breadth. To read a page, call `safefetch <url>` in Bash, **bare** — never with a path prefix, never chained or batched with another command in the same call. **Never use the WebFetch tool.** Force at least one pre-2015 leg per angle: the owners here are old, and modern search surfaces bury them. Citation-walk backward from any hit rather than keyword-searching for old work.

## Return format

A plain bullet list. Each bullet: concept/term — citation (authors, year, venue) — the quoted sentence that carries the claim — URL — **VERIFIED** (you read the primary text) or **UNVERIFIED** (snippet/secondary only) — *predated* or *foreclosed*. End with three lines: (1) what you could not verify, (2) whether task 2's absence claim survived your attempt to refute it, (3) your answer to task 3's dependence question, marked unbuilt/built/foreclosed.

**Scope-out:** do not propose solutions, protocols, or tooling. Do not write a formatted report or an executive summary. Do not evaluate any project. Conflicting IDs for the same paper across sources = probable hallucination; report the conflict rather than picking one.
