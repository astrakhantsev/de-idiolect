A note before the findings: fetching the Yuxi Liu essay on Cyc (`yuxi-liu-wired.github.io`) tripped safefetch's scanner — 1 HIGH finding (`role_manipulation`: an embedded "I want you to be..." instruction override) and 1 LOW (invisible unicode). The suspicious span was stripped automatically and I did not follow any embedded instructions from it; I only used its abstract (Cyc: 40 years, ~$200M, 2,000 person-years, 30M assertions, no AGI breakthrough) as background color, not as a quoted source below.

Here is the research. I opened and quoted from the bodies of six primary sources (Shirky 2003, Doctorow 2001, Hoekstra 2010, Star & Griesemer 1989, Bowker & Star 1999, and Wikipedia's presentation of Harnad 1990/ALPAC 1966), well past the 3-source minimum.

## Q1 — Why this class of projects fails: named explanations

**1. "No natural or universal classification system" (infrastructural/political account)**
· Owner: Geoffrey C. Bowker & Susan Leigh Star, *Sorting Things Out: Classification and Its Consequences*, MIT Press, 1999 (drawing on Lakoff 1987, Latour 1987)
· Quotes (verbatim, from the book body, fetched directly):
> "A consistent finding of the history of science is that there is no such thing as a natural or universal classification system... Classifications that appear natural, eloquent, and homogeneous within a given human context appear forced and heterogeneous outside of that context."
> "Towers of Babel are perhaps the rule, not the exception. To classify is human and all cultures at all times have produced classification systems."
· Confidence: High — verbatim, primary source, full book text obtained.
· Could not verify: Whether this exact framing predates 1999 in Bowker/Star's own earlier papers; I didn't chase their 1990s conference-paper prehistory.

**2. The Semantic Web as "a machine for creating syllogisms" — worldview-mismatch critique**
· Owner: Clay Shirky, "The Semantic Web, Syllogism, and Worldview," Networks, Economics, and Culture mailing list, Nov 7, 2003 (oldest treatment I found of this specific argument; it in turn cites Drew McDermott's 1987 "Critique of Pure Reason," *Computational Intelligence* 3:151-237 — my pre-2015 source)
· Quotes:
> "Any attempt at a global ontology is doomed to fail, because meta-data describes a worldview... It is not possible to neatly map these two systems onto one another, or onto other classification schemes—they describe different kinds of worlds."
> "[Like] many visions that project future benefits but ignore present costs, it requires too much coordination and too much energy to effect in the real world, where deductive logic is less effective and shared worldview is harder to create than we often want to admit."
· Confidence: High — full essay fetched, verbatim.
· Could not verify: Direct citation details of McDermott 1987 beyond what Shirky quotes.

**3. "Metacrap" — seven structural obstacles to reliable shared metadata**
· Owner: Cory Doctorow, "Metacrap: Putting the torch to seven straw-men of the meta-utopia," 26 Aug 2001
· Quotes:
> "A world of exhaustive, reliable metadata would be a utopia. It's also a pipe-dream, founded on self-delusion, nerd hubris and hysterically inflated market opportunities."
> "Any hierarchy of ideas necessarily implies the importance of some axes over others... The conceit that competing interests can come to easy accord on a common vocabulary totally ignores the power of organizing principles in a marketplace." (obstacle 5, "Schemas aren't neutral")
· Confidence: High — full essay fetched, verbatim.
· Could not verify: nothing significant; this is a well-preserved primary text.

**4. The symbol grounding problem**
· Owner: Stevan Harnad, "The Symbol Grounding Problem," *Physica D* 42(1-3):335-346, 1990 — the oldest treatment I found for this specific mechanism-level explanation (predates the Semantic Web and most knowledge-base critiques by over a decade)
· Quote (Harnad's own words, as preserved in Wikipedia's citation apparatus — I could not get the primary PDF to render through safefetch or curl):
> "How can the semantic interpretation of a formal symbol system be made intrinsic to the system, rather than just parasitic on the meanings in our heads? How can the meanings of the meaningless symbol tokens... be grounded in anything but other meaningless symbols?"
· Confidence: Medium — the quote is attributed correctly per multiple corroborating sources (Wikipedia, PhilPapers, ScienceDirect abstract), but I did not open Harnad's own PDF body directly; treat as high-confidence secondhand rather than my own primary-source read.
· Could not verify: Full argument structure beyond the problem statement; I did not read past the abstract-level formulation.

**5. Boundary objects — communities don't converge on one ontology, they build translation devices instead**
· Owner: Susan Leigh Star & James R. Griesemer, "Institutional Ecology, 'Translations' and Boundary Objects," *Social Studies of Science* 19(3):387-420, 1989 — the single most-cited paper in that journal, and (per my search) the oldest of the sources I found specifically targeting the coordination-across-communities problem
· Quote (verbatim, from the fetched PDF body):
> "Scientific work is heterogeneous, requiring many different actors and viewpoints. It also requires cooperation. The two create tension between divergent viewpoints and the need for generalizable findings... Extending the Latour-Callon model of interessement, two major activities are central for translating between viewpoints: standardization of methods, and the development of 'boundary objects.'"
· Confidence: High — verbatim, primary source.
· Note: This paper is arguably the most important one for the user's underlying question — it's a 1989 answer to "how do you recognize that two differently-named things are the same concept, across communities" that explicitly rejects the single-universal-representation approach in favor of locally-negotiated, only-partially-shared objects. It reframes "failure to build one universal thing" as "success looks different than what was attempted."

**6. Cognitive overhead of formalization ("Which Semantic Web?")**
· Owner: Catherine C. Marshall & Frank M. Shipman, "Which Semantic Web?," ACM Conference on Hypertext and Hypermedia, 2003
· Quote (via AcaWiki/search summary, not independently verified against the primary PDF): noted to argue that learning a knowledge-representation language requires understanding "the representation's methods of abstraction and their effect on reasoning" in a way plain HTML authoring never demanded, and that treats several Semantic Web goals as unrealistic.
· Confidence: Medium — paraphrase from a summary source (AcaWiki/search snippet), not a direct fetch of the ACM paper body.
· Could not verify: exact verbatim wording; the ACM DL copy is paywalled and I did not attempt to bypass that.

## Q2 — Named economic/organizational bottlenecks

**7. The (Feigenbaum) knowledge acquisition bottleneck**
· Owner: Edward A. Feigenbaum. Earliest attribution found: IJCAI 1977 keynote/paper "The Art of Artificial Intelligence"; the version I could pin down and quote is Feigenbaum, "Knowledge Engineering: The Applied Side of Artificial Intelligence," *Annals of the New York Academy of Sciences* 426:91-107, 1984 (itself noted as "Original publication in 1980 as report of the Stanford department of Computer Science" — per Hoekstra 2010's own bibliography, which I fetched)
· Quote (as reproduced verbatim inside Hoekstra 2010, itself directly fetched):
> "The problem of knowledge acquisition is the critical bottleneck problem in artificial intelligence." — Feigenbaum 1984, p.93, quoted in Hoekstra 2010
· Confidence: High for the concept and its 1977-1984 vintage; Medium on pinning the exact original 1977 wording, since I only reached it at second hand through Hoekstra's citation, not Feigenbaum's own 1977/1984 text directly.
· This is the canonical name for cost of knowledge acquisition.

**8. The knowledge reengineering bottleneck (cost of maintenance/keeping current)**
· Owner: Rinke Hoekstra, "The Knowledge Reengineering Bottleneck," *Semantic Web* 1(1), 2010 — explicitly coined as a sequel/contrast to Feigenbaum's bottleneck
· Quotes (verbatim, fetched directly):
> "In contrast, the knowledge reengineering bottleneck refers to the general difficulty of the correct and continuous reuse of preexisting knowledge for a new task... Traditional ex ante methodologies do not provide any guidelines for this ex post knowledge reengineering. Semantic web developers therefore resort to ad hoc measures and manual labour."
> "Although the dream of unhindered 'knowledge reuse' is a technical reality, it has come at the cost of control... data is 'dirty'; it may not be the latest version, it may be inconsistent, it may use multiple identifiers for the same resource, it may have gaps in coverage, or be redundant."
· Confidence: High — verbatim, primary source, full text obtained.
· This is the canonical name for the maintenance/keeping-current cost, distinct from acquisition cost.

**9. Network externalities / coordination failure in standards adoption**
· Owner: Michael L. Katz & Carl Shapiro, "Network Externalities, Competition, and Compatibility," *American Economic Review* 75(3):424-440, 1985
· Confidence: Medium — I did not fetch the primary paper's body; this is search-snippet-derived. Established economics literature describes their model as showing markets "may fail to adopt a superior technology due to coordination failure" and that standards choice is a coordination game — this is the canonical citation economists use for why shared-vocabulary/standard adoption stalls even when everyone would benefit from convergence, but I have not verified exact wording.
· Could not verify: any direct quote from the 1985 AER text itself.

**10. Knowledge commons / contributor incentive problems**
· Owner: Charlotte Hess & Elinor Ostrom (eds.), *Understanding Knowledge as a Commons: From Theory to Practice*, MIT Press, 2007 — extends Ostrom's *Governing the Commons* (1990) collective-action framework to information resources
· Confidence: Medium — search-snippet-derived, not a direct fetch. The documented finding (per multiple secondary summaries) is that contributors to knowledge commons are driven more by reputational/reciprocity and intrinsic motivation than direct monetary reward, and that — unlike Ostrom's physical commons — the *content* is non-rival but the curation/maintenance labor is subtractable and congestible, which is exactly the gap that stalls volunteer-maintained ontologies once initial enthusiasm fades.
· Could not verify: direct verbatim quote from the book itself.

## Q3 — Documented sociological effect on the field

**11. ALPAC 1966 → explicitly named as the start of "the first AI winter"**
· Owner: Automatic Language Processing Advisory Committee (chaired by John R. Pierce), *Language and Machines — Computers in Translation and Linguistics*, National Academy of Sciences/National Research Council, 1966
· Quote (from Wikipedia's summary, fetched directly — the primary 1966 report itself I did not fetch, only located its archive link):
> "Its report, issued in 1966, gained notoriety for being very skeptical of research done in machine translation so far... this eventually caused the U.S. government to reduce its funding of the topic dramatically. This marked the beginning of the first AI winter."
· Confidence: Medium-High for the funding-collapse fact (well corroborated across multiple independent sources I found — IEEE Xplore's *The 1966 ALPAC Report and Its Consequences*, Hutchins & Hays "ALPAC: The (In)Famous Report"); Medium for the specific "first AI winter" framing, since that phrasing is Wikipedia's own characterization rather than a quote from a named academic source I verified directly.
· This is the strongest documented case of a real "winter": interlingua-style universal semantic representation for MT was explicitly the target criticized, and U.S. federal MT funding was cut for roughly two decades as a direct result.
· What I could not find: a specifically-named "ontology winter" or "knowledge-representation winter" as a distinct academic term parallel to "AI winter" — several searches turned up general AI-winter discourse that *includes* Cyc/expert-systems/knowledge-representation but no source coined a separate, specific term for this narrower phenomenon. This looks like a genuine terminology gap rather than something I failed to find — treat that absence itself as a finding.

**12. Cyc as the field's cautionary tale (softer, informal stigma rather than a "winter")**
· Owner: Doug Lenat & Gary Marcus, "Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc," arXiv, 2023; and Gary Marcus's obituary essay for Lenat (Substack, Sept 2023, fetched directly)
· Quote (verbatim, fetched directly):
> "Cyc has been neither a success nor a failure, but somewhere in between: I see it as a ground-breaking, clarion experiment that never fully gelled... Most young AI researchers have never even heard about it."
· Confidence: High that this reflects genuine field-level neglect/write-off (corroborated independently by the Yuxi Liu essay's framing — used only for its non-injected abstract — describing Cyc as costing "$200 million and 2,000 person-years" without achieving its stated aim); Medium on calling this a documented "stigma" in the formal sense the question asks about, since Marcus's is a personal reflection, not a sociology-of-science study measuring funding or publication rates before/after Cyc.
· Could not verify: any bibliometric study quantifying reduced funding/publication for hand-built commonsense KBs specifically attributable to Cyc's reputation (as distinct from the general 1980s-90s AI winter). I did not find one.

## Q4 — What serious post-mortems say would need to change

- **Hoekstra 2010** (fetched, verbatim): the fix isn't better upfront ("ex ante") design methodology but tooling for continuous *ex post* reengineering — provenance tracking, versioning regimes, and "a continuous relation of trust between a knowledge provider and its 'clients'" rather than one-time knowledge transfer. Confidence: High.
- **Star & Griesemer 1989** (fetched, verbatim, implicit answer): stop treating convergence-on-one-representation as the goal; the empirically observed successful mechanism is boundary objects — artifacts "adaptable to different viewpoints and robust enough to maintain identity across them" — plus local standardization of methods, not global standardization of meaning. Confidence: High that this is what the paper argues; Medium on whether later authors explicitly frame this as a "post-mortem lesson" for universal-ontology projects specifically — that connection is my synthesis, not a claim any source made outright.
- **Implicit contrast from search results (Wikidata vs. Cyc/Semantic Web)**: several secondary sources (search-snippet only, not fetched in full) attribute Wikidata's comparative traction to crowdsourced, incremental, low-commitment contribution (aligned with Hess & Ostrom's reputational/intrinsic-incentive point above) versus Cyc's centralized expert-encoding model and the Semantic Web's demand for upfront formal ontological commitment. Confidence: Low-Medium — I could not find a single rigorous comparative post-mortem making this argument explicitly; this is my synthesis across several thinner sources, not one strong citation.

## Three oldest relevant sources found
1. ALPAC Report, *Language and Machines*, National Academy of Sciences, **1966** — earliest documented case of a universal-representation project (interlingua machine translation) triggering an actual, named funding "winter."
2. Star & Griesemer, "Institutional Ecology, 'Translations' and Boundary Objects," *Social Studies of Science*, **1989**.
3. Harnad, "The Symbol Grounding Problem," *Physica D*, **1990** (Feigenbaum's bottleneck is arguably older — 1977 — but I could only pin down and quote the 1980/1984 republication directly, so I'm listing what I actually verified).

## What I did NOT search (honest coverage gaps)
- The ~350-year historical end of the timeline: I did not open primary or secondary sources on Leibniz's *characteristica universalis*, John Wilkins' philosophical language, or Roget's Thesaurus — only got Eco's 1995 *The Search for the Perfect Language* via search snippets, never fetched the book itself.
- WordNet-specific critique literature (its known gaps as a "general semantic substrate") — not searched at all.
- ISO/TC 37 and the prescriptive-terminology-standardization literature (Wüster's Vienna School and its critics) — searched once, got only thin, low-confidence results; did not fetch any primary terminology-theory text.
- Any non-English-language sources or venues — everything above is English-language only.
- Bibliometric/citation-trend studies that would let me *quantify* claims like "the field stalled" or "funding collapsed" for Semantic Web/ontology research specifically (as opposed to the well-documented 1966 ALPAC/MT case) — I did not run citation-count or funding-database searches.
- Primary texts for Feigenbaum 1977/1980, Katz & Shapiro 1985, Hess & Ostrom 2007, and Marshall & Shipman 2003 — for all four I relied on search snippets or secondary quotation rather than opening and reading the source body myself, which I've flagged per-item above.
- I did not search for a formally named "ontology winter" or "knowledge winter" beyond the two queries I ran; it's possible a niche paper coins this and I simply didn't surface it.
