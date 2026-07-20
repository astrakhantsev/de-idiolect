I have five sources read in full plus corroborating searches. Two fetches failed and I'll flag them: the ACM full text of Marcus & Davis (2015) was Cloudflare-blocked, and the Warburton terminology-standardization paper rendered empty — so the prescriptive-terminology/ISO angle rests on search snippets only, not a body read. Here is the synthesis.

---

# Why universal shared-concept representations keep failing

A note on scope: I read in full and quote from **Borges (1942), Feigenbaum (via Hoekstra's reproduction), McDermott (via Shirky's reproduction), Doctorow (2001), Shirky (2003), Hoekstra (2010), the Cyc post-mortem (2025), and the "Forgotten Wave" bibliometric paper (2025)**. Where I quote a source I could not open directly (McDermott, Feigenbaum, Marcus & Davis), I say so explicitly.

## Part 1 — The established explanations (blocks)

### Explanation A — The knowledge-acquisition bottleneck
**Owner + citation:** Edward A. Feigenbaum, ~1977–1980 (the phrasing I quote is reproduced in Rinke Hoekstra, "The Knowledge Reengineering Bottleneck," *Semantic Web* 1 (2010), IOS Press, ref. [8], p.93). Oldest treatment: Feigenbaum's late-1970s "knowledge engineering" papers; canonized across the 1980s expert-systems literature.

**Verbatim quotes** (as reproduced in Hoekstra 2010, which I read in full via the PDF):
> "The problem of knowledge acquisition is the critical bottleneck problem in artificial intelligence." — Feigenbaum, quoted in Hoekstra 2010, p.2

> "If applied artificial intelligence is to be important in the decades to come, we must have more automatic means for replacing what is currently a very tedious, time-consuming and expensive procedure." — Feigenbaum, quoted in Hoekstra 2010, p.2

**Confidence:** High that this is the canonical, oldest-named economic explanation and that it is owned by Feigenbaum. **Could not verify:** the exact original venue/year/page of Feigenbaum's quote — I read it only as reproduced by Hoekstra, whose citation [8] I did not open. Stanford's Feigenbaum archive labels a 1982 item "Knowledge Acquisition: The Bottleneck," consistent with a ~1977–1982 origin.

### Explanation B — No classification of the universe is non-arbitrary (schemas encode a worldview)
**Owner + citation:** Jorge Luis Borges, "The Analytical Language of John Wilkins" (1942); pointing back to John Wilkins's *An Essay towards a Real Character and a Philosophical Language* (1668). This is the oldest treatment I found of the core argument, and the one that reaches the "~350 years" framing through its subject.

**Verbatim quotes** (read in full from the gwern-hosted PDF of Borges's essay):
> "obviously there is no classification of the universe that is not arbitrary and speculative. The reason is quite simple: we do not know what the universe is." — Borges 1942, p.231

> "The impossibility of penetrating the divine scheme of the universe cannot, however, dissuade us from planning human schemes, even though it is clear that they are provisional." — Borges 1942, p.231

**Confidence:** High that this is the oldest and most-cited statement of the arbitrariness objection; it is directly invoked by later critics (Shirky's "worldviews differ" section is the same argument, secularized). **Could not verify:** I did not open Wilkins (1668) or Umberto Eco's *The Search for the Perfect Language* (1995), which is the standard modern history of this failure lineage.

### Explanation C — Human-generated metadata is unreliable by construction (the seven obstacles)
**Owner + citation:** Cory Doctorow, "Metacrap: Putting the torch to seven straw-men of the meta-utopia," 26 August 2001.

**Verbatim quotes** (read in full):
> "A world of exhaustive, reliable metadata would be a utopia. It's also a pipe-dream, founded on self-delusion, nerd hubris and hysterically inflated market opportunities." — Doctorow 2001

> "The conceit that competing interests can come to easy accord on a common vocabulary totally ignores the power of organizing principles in a marketplace." — Doctorow 2001, "Schemas aren't neutral"

The seven named obstacles verbatim: "People lie," "People are lazy," "People are stupid," "Mission: Impossible — know thyself," "Schemas aren't neutral," "Metrics influence results," "There's more than one way to describe something." His well-poisoning line: "When poisoning the well confers benefits to the poisoners, the meta-waters get awfully toxic in short order."

**Confidence:** High. This is the canonical, most-cited essay-level explanation of why shared-metadata utopias fail, and it splits the failure into incentive (lie/lazy), cognitive (stupid/know-thyself), and structural (schemas/metrics/description) causes. **Could not verify:** it is a polemical essay, not peer-reviewed; the empirical claims (eBay typos, Napster tags) are illustrative anecdotes, not measured.

### Explanation D — Real knowledge is not amenable to deductive recombination
**Owner + citation:** Clay Shirky, "The Semantic Web, Syllogism, and Worldview" (7 November 2003), quoting Drew McDermott, "A Critique of Pure Reason," *Computational Intelligence* 3:151–237 (1987).

**Verbatim quotes** (read in full from the gwern archive of Shirky's essay):
> "The Semantic Web is a machine for creating syllogisms… Despite their appealing simplicity, syllogisms don't work well in the real world, because most of the data we use is not amenable to such effortless recombination." — Shirky 2003

> "It must be the case that a significant portion of the inferences we want [to make] are deductions, or it will simply be irrelevant how many theorems follow deductively from a given axiom set." — Drew McDermott, *A Critique of Pure Reason* (1987), as quoted by Shirky 2003

**Confidence:** High on Shirky's ownership of the popular form and on the McDermott quote as reproduced. **Could not verify:** I did not open McDermott (1987) directly — the quote is via Shirky. McDermott (1987) is likely the oldest *rigorous* AI treatment of this specific failure mode.

### Explanation E — A global ontology is doomed because you cannot manufacture agreement (the coordination/worldview objection)
**Owner + citation:** Clay Shirky, "The Semantic Web, Syllogism, and Worldview" (2003); the "Worldviews Differ For Good Reasons" and "Worse is Better" sections.

**Verbatim quotes** (read in full):
> "Any attempt at a global ontology is doomed to fail, because meta-data describes a worldview… You can't get a standard til you have an agreement, and you can't force an agreement to exist where none actually does." — Shirky 2003

> "it requires too much coordination and too much energy to effect in the real world, where deductive logic is less effective and shared worldview is harder to create than we often want to admit." — Shirky 2003

Shirky also names the adoption fallacy underlying such projects: "it is a short but fatal leap to conclude that a particular brand of unifying description will therefore be broadly and swiftly adopted (the 'this will work because it would be good if it did' fallacy.)"

**Confidence:** High. This is the most-cited single statement of the coordination-cost objection, and it maps directly onto the database-integration literature's "semantic heterogeneity / Tower of Babel" framing (which I saw only in search snippets, not a body read). **Could not verify:** Shirky is an essayist; the argument is analytical, not empirical.

### Explanation F — Hand-encoding common sense does not reach "escape velocity"; learning presupposes prior knowledge
**Owner + citation:** The primary object is Cyc (Douglas Lenat, 1984–2023). The post-mortem I read in full is Yuxi Liu, "Cyc" (2025, self-published essay, "based on extensive archival research"), which quotes Lenat's own papers.

**Verbatim quotes** (read in full):
> "The legendary Cyc project, Douglas Lenat's 40-year quest to build artificial general intelligence by scaling symbolic logic, has failed… Cyc grew to contain approximately 30 million assertions at a cost of $200 million and 2,000 person-years. Yet despite Lenat's repeated predictions of imminent breakthrough, it never came." — Liu 2025

> "Machine-learning common sense from scratch is impossible, because learning occurs at the fringe of what one already knows." — Liu 2025, summarizing Lenat's own doctrine (citing Lenat 1995b)

The essay's diagnosis of the trap: Lenat's plan was to "prime the knowledge pump" by hand and then have Cyc learn by reading, but "the last holdup was natural language understanding (NLU)" — and NLU itself needs the common sense the pump was supposed to bootstrap, i.e. a chicken-and-egg loop the manual approach never escaped.

**Confidence:** High that hand-encoding-doesn't-scale + bootstrap-circularity is the standard Cyc post-mortem; it is corroborated by the search-surfaced consensus (Wikidata/DBpedia/YAGO reached larger scale at a fraction of the labor; Hofstadter's fluid-analogy critique). **Could not verify:** Liu (2025) is a blog, not peer-reviewed, though heavily sourced to Lenat's primary papers; I did not independently open those primaries. Cycorp did not answer the author's questions, so some claims rest on inference.

---

## Part 2 — Named economic / organizational bottlenecks

1. **Knowledge-acquisition bottleneck** — Feigenbaum (see Explanation A). The cost-of-acquisition bottleneck: eliciting and formalizing expert knowledge is "tedious, time-consuming and expensive." Search-level corroboration (multiple sources): elicitation can consume 70–80% of an expert-system project's effort.

2. **Knowledge-reengineering bottleneck** — Rinke Hoekstra, *Semantic Web* 1 (2010). This is the canonical named **maintenance / keeping-current** bottleneck, and Hoekstra explicitly frames it as the successor to Feigenbaum's:
> "Although the dream of unhindered 'knowledge reuse' is a technical reality, it has come at the cost of control… Traditional ex ante methodologies do not provide any guidelines for this ex post knowledge reengineering; forcing developers to resort to ad hoc measures and manual labour: the knowledge reengineering bottleneck." — Hoekstra 2010, Abstract

His worked maintenance example (read in full): when the widely-used SIOC vocabulary renamed `sioc:User` to `sioc:UserAccount`, every downstream dataset silently went stale — "there is no guarantee that the ontologies… are used in the specified way… the data may be expressed in terms of an older version of a schema." This is the documented **cost-of-staying-current / schema-drift** problem. Confidence: high; this is the on-point pre-2015 academic source.

3. **Coordination / agreement problem** — Shirky (Explanation E): "you can't force an agreement to exist where none actually does." Owner of the popular form: Shirky 2003; the underlying database version is "semantic heterogeneity" (seen only in snippets: ResearchGate "Semantic Heterogeneity Issues on the Web"; the "Tower of Babel problem").

4. **Contributor-incentive problem** — Doctorow (Explanation C): "People lie / People are lazy." Metadata sits "in a competitive world," so accurate voluntary annotation is under-supplied (lazy) or adversarially gamed (lie). Owner: Doctorow 2001.

5. **Organizational lock-in / product-differentiation** (an incentive bottleneck specific to the *maintainers*) — from the Cyc post-mortem, an Upton-Sinclair-style observation:
> "It can be very hard to get someone to understand something, when their product differentiation depends on them not understanding it." — Liu 2025, on why Cycorp could not abandon the manual approach

Confidence: medium-high; it is a plausibly-argued organizational bottleneck but sourced to one essayist.

---

## Part 3 — Is there a documented sociological "winter"?

Yes, two documented layers.

**(a) The AI winter (expert systems, 1987–1993).** Well-documented: the specialized-hardware market "collapsed overnight" in 1987, IPTO leadership "dismissed expert systems as 'clever programming' and cut funding… deeply and brutally," and — per multiple secondary sources — "the word 'AI' had become so tainted that companies preferred to label their products 'machine learning' or 'data mining.'" The named proximate causes are exactly the two failure modes above: **brittleness** and the **knowledge-acquisition bottleneck**. (These are search-surfaced secondary summaries — Wikipedia "AI winter," Holloway, DataCamp — not a single canonical paper I read in full.)

**(b) The Semantic Web as a "forgotten wave" / trough of disillusionment.** The most concrete documented sociological claim I read in full is the 2025 bibliometric paper "Semantic Web and Software Agents — A Forgotten Wave of Artificial Intelligence?" (arXiv:2503.20793):
> "Despite initial momentum, the Semantic Web failed to become a mainstream AI paradigm." — arXiv:2503.20793 (2025)

> "All AI history illustrations known to the authors of this study depict the period from 2000 to 2010 as an AI winter rather than a time of substantial research advancements. These accounts consistently emphasize stagnation and minimal innovation, portraying this period as one characterized by diminished funding, waning public interest, and a general lack of transformative breakthroughs." — arXiv:2503.20793 (2025)

They document (Google Books Ngram + Google Scholar) that "Semantic Web" usage "peaks between 2005 and 2010" then declines — a measured funding/attention collapse, and, notably, a *retroactive erasure* (the field is now not even remembered as having been a wave). Search-level corroboration: Hendler's own self-critical retrospective ("Where are all the intelligent agents?") and Berners-Lee's 2006 pivot away from "deep ontologies" toward grass-roots "linked data."

**Confidence:** High that a funding/attention collapse is documented for both expert systems and the Semantic Web. **Could not verify:** a *named* "knowledge-base winter" as a term of art (the literature uses "AI winter" and "trough of disillusionment"/Gartner hype cycle, not a KB-specific coinage); and I could not confirm the authorship of arXiv:2503.20793 from what I fetched (I read its body but not a verified author list).

---

## Part 4 — What the serious post-mortems say would have to change

- **Replace manual acquisition with cheap/automatic acquisition.** The Cyc post-mortem's implicit prescription (and the ML consensus it reports): "the only feasible way to assemble knowledge at Cyc's intended scale was to learn it from data rather than encode it by hand." Web-mined KBs (Wikidata, DBpedia, YAGO) are cited as the existence proof that scale is reachable only when per-fact cost collapses — at the price of shallower assertions. (Liu 2025, read in full.)

- **Solve the bootstrap, not the schema.** Both Cyc and the Semantic Web put the effort on *representation* while the binding constraint was *acquisition + NLU*. Shirky's version: "This puts the stress on the wrong part of the problem — if the world were easy to describe, you could do it in Sanskrit." The feasibility precondition is machine reading good enough to acquire knowledge without humans — which for Cyc never arrived (NLU was "the last holdup"). Marcus & Davis's 2015 CACM survey reportedly argues the path forward is a *combination* — logic + hand-built KBs + web mining + crowdsourcing — with commonsense still the unsolved core. *(This last is from the article's abstract/search summary only — ACM's full text was Cloudflare-blocked, so I did not read its body and cannot quote it.)*

- **Abandon the global ontology; make semantics optional and bottom-up.** Shirky's explicit prescription: let meaning be "a side conversation between consenting adults," design for "simple implementation" (worse-is-better), and accept piecemeal, self-interested metadata — because "the big advantage of this bottom-up design and adoption is that it is actually working now." The feasibility change is dropping the universality requirement itself.

- **Treat reuse as continuous curation, not one-time design.** Hoekstra's prescription: knowledge engineering needs *ex post* methodologies — provenance, trust between provider and consumers, tolerance of "dirty data" — because "reuse is not a copy-and-paste operation, but rather a continuous relation of trust." The feasibility change is a maintenance model, funded indefinitely, rather than a build-once artifact.

Common thread across the serious post-mortems: the goal becomes feasible only if you either (i) drop universality (local, bottom-up, worse-is-better), or (ii) drop manual acquisition (learn from data), or (iii) fund perpetual re-curation. Every project that failed insisted on universal + manual + build-once.

---

## The 3 oldest relevant sources I found
1. **Jorge Luis Borges, "The Analytical Language of John Wilkins" (1942)** — the arbitrariness-of-all-classification argument; itself a commentary on John Wilkins's *Essay* (1668). Read in full.
2. **Edward Feigenbaum, "knowledge acquisition bottleneck" (~1977–1980)** — the founding economic bottleneck. Read only as reproduced in Hoekstra (2010); original not opened.
3. **Drew McDermott, "A Critique of Pure Reason," *Computational Intelligence* 3:151–237 (1987)** — the deductive-scaffolding-is-fatally-flawed argument. Read only as quoted by Shirky (2003).

(Then, pre-2015: Doctorow 2001, Shirky 2003, Shirky "Ontology is Overrated" 2005, Hoekstra 2010 — all satisfy the "before 2015" requirement; Hoekstra and Borges I read in full.)

## What I did NOT search / coverage gaps (honest)
- **Prescriptive terminology standardization (ISO/TC 37, Wüster's Vienna school).** My one targeted fetch (Warburton 2014) rendered empty, so this angle rests on search snippets only. I did **not** reach Rita Temmerman's *Towards New Ways of Terminology Description* (the standard sociocognitive critique of prescriptive terminology) or Cabré/Sager. This is my weakest-covered area.
- **WordNet-specific critiques.** Named in your phenomenon but I did not deep-dive its lexical-substrate limitations (e.g., sense-granularity / "fine-grained sense" critiques).
- **The philosophical-language history in depth.** I have Borges but not **Umberto Eco, *The Search for the Perfect Language* (1995)** or Leibniz's *characteristica universalis* / *lingua generalis* primary literature.
- **Marcus & Davis (2015) body.** Cloudflare-blocked; I have only the abstract/summary, so my Part-4 attribution to it is provisional.
- **The formal database-integration literature** (Halevy et al. on schema matching; "semantic heterogeneity") — seen only as search snippets, no body read.
- **Quantitative failure-base-rate studies** (how many such projects, what fraction stalled) — I found narrative post-mortems, not a systematic survey.
- **Non-English sources**, and anything behind paywalls (ACM DL, IOS Press article pages, ResearchGate PDFs) that I could not render.

**Sources (read in full):** [Borges, *The Analytical Language of John Wilkins* (1942), gwern PDF](https://gwern.net/doc/borges/1942-borges-johnwilkinsanalyticallanguage.pdf) · [Doctorow, *Metacrap* (2001)](https://hermiene.net/essays-trans/metacrap.html) · [Shirky, *The Semantic Web, Syllogism, and Worldview* (2003), gwern archive](https://gwern.net/doc/ai/2003-11-07-clayshirky-thesemanticwebsyllogismandworldview.html) · [Hoekstra, *The Knowledge Reengineering Bottleneck* (2010)](https://www.semantic-web-journal.net/sites/default/files/swj32.pdf) · [Liu, *Cyc* post-mortem (2025)](https://yuxi-liu-wired.github.io/essays/posts/cyc/) · [*Semantic Web and Software Agents — A Forgotten Wave of AI?* arXiv:2503.20793 (2025)](https://arxiv.org/html/2503.20793v1)
**Consulted via search only (not body-read):** [Shirky, *Ontology is Overrated* (2005)](http://itc.conversationsnetwork.org/shows/detail470.html) · [Marcus & Davis, CACM (2015) — blocked](https://cacm.acm.org/magazines/2015/9/191169-commonsense-reasoning-and-commonsense-knowledge-in-artificial-intelligence/fulltext) · [Warburton, terminology standardization (2014) — empty render](https://www.aeter.org/wp-content/uploads/2014/10/Warburton-AETER14.pdf) · [Stanford Feigenbaum archive, "Knowledge Acquisition: The Bottleneck" (1982)](https://exhibits.stanford.edu/feigenbaum/catalog/sq764cf8300) · [AI winter — Wikipedia](https://en.wikipedia.org/wiki/AI_winter)

One caveat worth flagging: three of my central sources (Doctorow, Shirky, Liu) are essays/blogs rather than peer-reviewed work — they are the *canonical* statements of these arguments and are widely cited, but if you need strictly academic citations for Part 1, the load-bearing peer-reviewed anchors are **Hoekstra (2010)**, **McDermott (1987)**, and **Feigenbaum (~1977–80)**, and I'd recommend I next chase down the terminology-standardization literature (Temmerman, Cabré) to close the one real gap.
