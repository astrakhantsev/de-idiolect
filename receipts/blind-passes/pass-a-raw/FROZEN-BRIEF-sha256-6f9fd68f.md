You are a research librarian with broad cross-disciplinary reach. I am going to describe a phenomenon in plain operational terms. I want you to tell me **what it is called and who owns it.**

Do not search first. **Answer from your own knowledge first**, then verify.

## The phenomenon

A group working on a problem invents its own names for the things it studies. Those names are internally clear and get used consistently across the group's documents.

Later, the group tries to establish whether its findings are new. It searches using its own names. The searches return nothing relevant. The group concludes the area is unoccupied.

The conclusion is false. The phenomena had already been studied — often decades earlier, sometimes settled as theorems — under different names, in fields the group did not think to search. The prior work was reachable the entire time, but not from the group's vocabulary. Because the searches were clean and returned nothing, the false conclusion arrived with *high confidence*.

A related structural feature: the people doing the searching had been briefed using the group's documents, and so had absorbed the group's names before they began searching. Several searchers, briefed the same way, agreed with each other and were wrong together.

## What I want

**1. Name it.** What is this phenomenon called? Give me every name it has in every field that has one. I expect it has several names in several fields, because that would be the phenomenon describing itself. For each name: which field, the canonical citation (authors, year, venue), and one line on what that work actually establishes.

**2. Date it.** For each name: what is the **oldest** treatment you would expect to exist? Do not restrict yourself to recent work, or to computer science, or to anything about AI or language models. If the oldest thing you can think of is from the 1920s, say so.

**3. Who has to solve this professionally?** Some occupations cannot afford this failure and have built machinery against it. Which ones, what machinery, and does it work?

**4. Is it measured?** Has anyone quantified how often this happens, or how badly? Any empirical study of the phenomenon rather than commentary on it.

**5. Adjacent but distinct.** Name phenomena that are close to this but are **not** the same thing, and say precisely what separates them. I want the boundaries, because I am at risk of collapsing distinct things into one story.

**6. Where would you look that I would not?** Which literatures are non-obvious homes for this? Name fields whose connection is not apparent from the description above.

## Method

Answer from your own knowledge first and mark that section clearly — I want to see what you reach for before you search, because that is data about where the concept lives.

Then verify. Use WebSearch for breadth. To read a page, call `safefetch <url>` in Bash, **bare** — never with a path prefix, never chained or batched with another command in one call. **Never use the WebFetch tool.**

Verify against **primary text** wherever possible, and quote the sentence that carries the claim. Do not trust an abstract to represent a paper. If you cannot retrieve something, say "could not retrieve" — a failed fetch is not evidence of anything. If you find conflicting identifiers for the same work, report the conflict rather than picking one.

## Return format

A plain bullet list, no headers, no prose report, no executive summary. Two clearly separated sections: **(A) from knowledge, before searching** and **(B) after verification.**

Each bullet: name of the concept — field — citation (authors, year, venue) — the quoted sentence carrying the claim — URL — **VERIFIED** (read primary text) / **SECONDARY** (read a summary of it) / **UNVERIFIED** (search snippet only) / **RECALLED** (from knowledge, not checked).

End with two lines: (1) the single oldest thing you found, and (2) the field you think is the *true* home of this phenomenon, if you had to pick one.

**Scope-out:** do not propose solutions, protocols, tooling, or countermeasures beyond task 3. Do not ask me for context about my project — the description above is deliberately all you get. Do not evaluate whether my situation is an instance of this; just tell me what the thing is called.
