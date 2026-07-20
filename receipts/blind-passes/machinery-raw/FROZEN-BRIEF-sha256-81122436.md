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
