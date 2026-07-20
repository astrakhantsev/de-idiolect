---
title: "Machinery against name-blind search — blind PASS A prompt"
date: 2026-07-16
kind: research prompt
status: "FROZEN — run 2026-07-16. Do not edit; this is the evidence the pass was blind."
pass: "A — blind. Contains NO candidate terms, NO owners, NO prior conclusions, NO preferred fields."
protocol: 30_reference/novelty-protocol.md §2 (two frozen passes) · §3 (reverse the question)
siblings: 2026-07-16-blind-naming-PASS-A-PROMPT.md · 2026-07-16-targeted-prior-art-search-PROMPT.md
question: "POSITIVE question ('what machinery exists?'), not an absence question. Neither prior pass asked this — Pass B task 2 asked only whether the composite was NAMED in the AI literature."
---

> **Why this exists.** Neither prior pass asked what *machinery* exists for machine searchers. Pass B asked an absence question ("is the composite named?"); Pass A asked a naming question ("what is this called?"). "What has been built against this, and does it work?" is a different question that would surface different objects — and it is decision-relevant.
>
> **Design notes for the audit trail (honest labeling):**
> - The brief says **"machine searchers," not "LLM agents"** — deliberately. Saying "LLM agent" socializes the run into the 2025–26 arXiv bubble and would recreate the correlated-context problem. If the AI literature owns this, an unprimed run will find it.
> - **Item 4 is semi-blind and must be labeled as such.** Asking "does anything sidestep wording entirely?" is informed by a prior run's content-addressed-retrieval finding. It names no owner, but it primes a direction. Do not count a hit on item 4 as an independent draw.
> - **The Method section is the main fix over the prior passes.** Their shared failure was that every source was assessed from an abstract or snippet and the one paper that mattered (Larsen & Bong 2016) was never opened by any of eight agents. This brief mandates reading bodies and grades evidence accordingly.
>
> **Freeze this brief verbatim.** Run in fresh sessions with no project context. Do not paste the frontmatter or this block.

# Paste everything below the line into a fresh session

---

You are a research librarian with broad cross-disciplinary reach. I am going to describe a task that a machine performs, and a way it fails. I want you to tell me **what has been built to stop it failing, who built it, and whether it works.**

Do not search first. **Answer from your own knowledge first**, then verify.

## The setting

A machine is given an idea stated in words. Its job is to decide whether that idea already exists somewhere in a large body of published work.

The machine searches using terms it derives from the idea's own wording. If the search returns nothing that matches, the machine reports the idea as new.

Two failure modes follow:

- The idea already exists in the published work, under different wording. The search does not reach it. The machine reports "new," and reports it confidently, because the search was clean.
- Several such machines, given the same idea in the same wording, search the same way and agree with each other. Their agreement is read as confirmation.

## What I want

**1. What has been built against this?** Machinery, systems, methods, standards, institutions — anything whose purpose is to stop a searcher concluding "not present" when the thing is present under other words. For each: what it is, who built it, when, and what it actually does.

**2. What has been built specifically for machine searchers**, as opposed to human ones? Name systems, papers, benchmarks. If this is an active area right now, say who is working on it and what they have actually shipped.

**3. What exists for human searchers that has NOT been ported to machines?** I am interested in machinery that works, is decades old, and that nobody appears to have automated.

**4. Do any approaches sidestep wording entirely**, rather than compensating for it? If so, name them and say what they index on instead.

**5. Is any of it measured?** Benchmarks, error rates, recall figures, evaluation campaigns. I want numbers and who reports them. Distinguish sharply between "measured in a benchmark" and "claimed in an abstract."

**6. The agreement problem specifically.** Is there machinery for the second failure mode — several searchers sharing an input, agreeing, and being wrong together? Who owns that? Does anything measure how much independence is actually lost, and what does it need in order to do so?

**7. Where would you look that I would not?** Fields whose connection is not apparent from the description above.

## Date rule

Do not restrict yourself to recent work, or to computer science, or to anything about AI or language models. If the oldest relevant machinery is from the 19th century, say so. For anything recent that you name, ask what it descends from and name that too.

## Method — read the actual thing

**This is the part I care most about.** A previous attempt at a related task failed because every source was assessed from its abstract or from a search-result snippet, and the one source that mattered was never opened by anyone.

- Answer from your own knowledge first and mark that section clearly.
- Then verify. Use WebSearch for breadth. To read a page, call `safefetch <url>` in Bash, **bare** — never with a path prefix, never chained or batched with another command in one call. **Never use the WebFetch tool.**
- **Open at least four sources in full and quote from the body, not the abstract.** An abstract does not represent a paper. If a claim is load-bearing, the sentence carrying it must come from the body.
- If you cannot retrieve something, say **"could not retrieve."** A failed fetch is evidence of nothing.
- If you find conflicting identifiers for the same work, report the conflict rather than picking one.
- If a search engine attributes a quote to a source, **verify the quote is actually in that source** before repeating it. If it is not there, say so explicitly.

## Return format

A plain bullet list. No headers, no prose report, no executive summary. Two clearly separated sections: **(A) from knowledge, before searching** and **(B) after verification.**

Each bullet: what the machinery is — field — who built it (authors/org, year, venue) — the quoted sentence carrying the claim — URL — evidence level, one of: **PRIMARY-FULL** (read the whole thing) / **PRIMARY-BODY** (read the relevant section, not just the abstract) / **ABSTRACT-ONLY** / **SECONDARY** / **SNIPPET** / **RECALLED**.

End with three lines: (1) the oldest machinery you found; (2) the single most on-target thing built specifically for machine searchers; (3) the gap — anything you looked for and did not find, stated as **"not found in these searches,"** never as "does not exist."

**Scope-out:** do not propose new solutions, designs, or countermeasures of your own. Do not ask me for context about my project — the description above is deliberately all you get. Do not evaluate whether my situation is an instance of this.
