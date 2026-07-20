## `transparency gradient` — flagged 20260720T230830Z (trigger: scan)

- Source files: ENTRY.md receipts/idiolect-trap-case-study.md
- Excerpts: 4 paragraphs, 887 words; prompt sha256 `07a59c8b5443d1a97969e90bb6be23ab79b2eff56313422d374c442280ea888b`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 57s; manifest: /mnt/f/src/de-idiolect/hook/example-scan/.term-check/manifests/20260720T230830Z-transparency-gradient-sonnet.txt)

## 1. What the term denotes (excerpt-only, no jargon reuse)

Across the excerpts, the phrase tracks a boundary condition on when a "translate an invented term into the field's own words, then search" step actually pays off. The payoff is concentrated on cases where the invented term's own wording gives no hint of the underlying, already-established idea *and* the discipline that owns that idea is not obvious — in those cases, supplying the underlying meaning (not just the coined word) is what makes the right prior work findable. Where the invented wording already reveals the underlying idea, or where the owning discipline was already known at the time of coining, the extra step adds nothing.

## 2. Closest terms of art

- **Semantic transparency** (of compounds/coinages) — psycholinguistics & morphology
- **Term transparency / motivation** — terminology science (terminography, standardized term formation)
- **Motivated vs. arbitrary sign** — structural linguistics / semantics
- **The vocabulary problem** — information science / human-computer interaction
- **Incommensurability / "obliteration by incorporation"** (independent naming of the same idea across paradigms or fields) — philosophy and sociology of science

## 3. Oldest expected treatments

- Semantic transparency: Bloomfield's *Language* (1933) already distinguishes transparent from opaque compounds; the modern experimental literature is 1990s psycholinguistics (e.g., Zwitserlood, Libben on compound processing).
- Term transparency/motivation: Eugen Wüster and the Vienna School of terminology, 1930s (his standardization program treats "motivation"/transparency as a criterion for good term formation); later codified in ISO 704 and in Sager's *A Practical Course in Terminology Processing* (1990) and Cabré's *Terminology: Theory, Methods and Applications* (1999).
- Motivated/arbitrary sign: Saussure, *Cours de linguistique générale* (1916); Ullmann, *Semantics: An Introduction to the Science of Meaning* (1962).
- Vocabulary problem: Furnas, Landauer, Gomez & Dumais, "The Vocabulary Problem in Human-System Communication," *CACM* (1987), building on late-1970s/80s indexing work.
- Incommensurability / multiple discovery: Kuhn, *The Structure of Scientific Revolutions* (1962); Merton on multiple independent discovery, *American Sociological Review* (1957).

## 4. Coverage by the best candidate, and the gap

The best single match is **term/semantic transparency** — that literature is exactly about whether a term's meaning can be recovered from its surface form, which is one half of what's described here (the "opaque coinage" vs. "transparent slogan" distinction). What it does *not* cover is the other half of the usage: this is not a claim about term form in the abstract, but an applied, tool-specific finding — that a particular retrieval/bridging method's *return on effort* is gated jointly by (a) surface opacity of the coinage and (b) how non-obvious the owning field is, the latter being closer to the vocabulary-problem / independent-discovery literature than to transparency research proper. No single established term names that joint gradient tied to a tool's payoff; the excerpts' "transparency gradient" is a local coinage that borrows the linguistic property as one ingredient of a two-factor, tool-evaluation claim that classical transparency work doesn't itself make.

## `misroute document` — flagged 20260720T230927Z (trigger: scan)

- Source files: ENTRY.md
- Excerpts: 2 paragraphs, 350 words; prompt sha256 `301c466156dea9a9d1f2080540482ee34857a9f68952e65368983ad30e45bd5a`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 50s; manifest: /mnt/f/src/de-idiolect/hook/example-scan/.term-check/manifests/20260720T230927Z-misroute-document-sonnet.txt)

## 1. What it denotes

A specific candidate document that, when retrieval/ranking signals are combined, outscores the correct target document — causing the system to attribute a term to the wrong source instead of its true defining source. It's a known, recurring false-positive competitor to the correct answer, not just any irrelevant hit.

## 2. Closest established terms of art

| Candidate | Field |
|---|---|
| **False drop** | Information retrieval / library & information science (classic, pre-digital IR) |
| **Hard negative** | Machine learning / dense retrieval & learning-to-rank |
| **False match** (or "conflation") | Record linkage / entity resolution |
| **Distractor** | Psychometrics / test design (also QA-benchmark construction) |
| **Confusable class** | Pattern recognition / speech & handwriting recognition |

## 3. Oldest expected treatments

- **False drop** — 1950s–60s automatic-indexing literature; associated with Mortimer Taube's Uniterm coordinate-indexing debates, Calvin Mooers' critiques, and formalized in Cleverdon's Cranfield studies and Salton's IR textbooks (late 1960s–70s).
- **Hard negative** — object-detection "bootstrapping" negatives (Sung & Poggio, early-mid 1990s face detection), later hard-negative mining in detection (Felzenszwalb et al., ~2008–2010) and metric learning (Schroff et al., FaceNet, 2015).
- **False match** — Fellegi & Sunter, "A Theory for Record Linkage" (1969), the foundational probabilistic record-linkage paper.
- **Distractor** — early-20th-century multiple-choice testing literature, formalized in mid-century educational-measurement/psychometrics work (ETS-adjacent).
- **Confusable class** — mid-20th-century signal detection theory (1950s) and speech-recognition confusability studies (1960s–70s); the confusion-matrix concept descends from the same lineage.

## 4. Fit assessment

No single candidate is a clean match. **False drop** is closest in spirit — it's the classic IR term for an observed, specific bad retrieval event rather than a general training category — but the term is archaic and doesn't carry any notion of competing against a *correct, canonical owner*. **Hard negative** captures the "outranks the true positive under fusion/scoring" mechanics well, matching the excerpt's fusion-of-keys framing, but that term is normally prospective/training-oriented (an example type you mine for a model), not a label for a specific document caught misbehaving in an evaluation. **False match** from record linkage captures the "wrong entity chosen as the attribution target" idea but is tied to matching two record sets, not term-to-definition retrieval.

What doesn't fit any candidate cleanly: the *routing* framing itself — that there's a canonical "owner" document a term should resolve to (like an entity-linking target), combined with the specific, recurring, singular character implied by "the misroute document" (definite article, cross-referenced instance rather than a general phenomenon). That composite — glossary/definition attribution + a specific known troublesome competitor — sits between hard-negative and false-match/entity-linking vocabulary without being fully named by either.

The excerpts don't say enough to tell whether "the misroute document" names one specific recurring document across the whole project or is being used generically for "whichever document caused misrouting in this cell" — that distinction matters for picking between "false drop" (event-specific) and "hard negative" (class of example) and isn't resolvable from what's given.

## `the commons` — flagged 20260720T231017Z (trigger: scan)

- Source files: ENTRY.md
- Excerpts: 4 paragraphs, 865 words; prompt sha256 `1314402587e7301f2b255b8de25bd748c5a74ec397037cf5179921e5235f9c84`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 58s; manifest: /mnt/f/src/de-idiolect/hook/example-scan/.term-check/manifests/20260720T231017Z-the-commons-sonnet.txt)

## 1. What the term denotes

A shared, persistent store of already-vetted translations between the specialized vocabularies of different communities — built up collectively so that once someone has checked that Community A's term X maps to Community B's term Y, no other user has to redo that verification. The store is meant to tolerate multiple simultaneous, possibly conflicting entries for the same mapping (when communities don't agree), recording the disagreement itself as a labeled relationship rather than forcing a single resolved answer.

## 2. Closest existing terms of art

1. **Ontology/schema alignment (mapping) repository** — Semantic Web / knowledge representation
2. **Authority control / authority file** — library & information science
3. **Terminology crosswalk / term bank** — terminology science, metadata standards
4. **Knowledge commons** — information-policy / commons theory
5. **Wiki-style versioned knowledge base with forking** — CSCW / distributed systems

## 3. Oldest expected treatments per candidate

1. **Ontology alignment**: roots in schema matching (Rahm & Bernstein, early 2000s survey); ontology-specific work like Noy & Musen's PROMPT (~2000); formalized as a subfield via the Ontology Alignment Evaluation Initiative (OAEI, mid-2000s onward).
2. **Authority control**: cataloging practice traces to early-20th-century library science (AACR-era rules); modern shared/networked form realized in projects like VIAF (2000s), but the underlying idea — a single verified authoritative form that many catalogers reuse instead of re-deciding — is much older.
3. **Terminology crosswalk / term bank**: grounded in Wüster's General Theory of Terminology (1930s–70s, Vienna school); institutionalized in early machine-readable term banks such as EURODICAUTOM (1970s) and later ISO terminology standards.
4. **Knowledge commons**: Ostrom's *Governing the Commons* (1990) on collectively managed shared resources, extended explicitly to informational/knowledge resources by Hess & Ostrom, *Understanding Knowledge as a Commons* (2007).
5. **Wiki / versioned knowledge base**: Ward Cunningham's original wiki (1995); the fork/merge-without-forced-consensus model is more explicitly theorized in distributed version control (practice from SCCS/RCS in the 1970s–80s, popularized by git in the mid-2000s).

## 4. Fit assessment

The *purpose* described — persist a verified cross-vocabulary mapping once so it can be reused instead of re-verified — is well covered by both **ontology alignment repositories** and **authority control**: both exist precisely to eliminate redundant reconciliation work across users. That's the strongest match for the "durable verified mapping... over repeated verification by each user" language.

What doesn't fit cleanly is the *governance model* layered on top: "forks coexist," disagreement is recorded as "a typed link" rather than resolved, and accumulation proceeds "without agreement." Classical ontology alignment and authority control both generally assume convergence toward one authoritative mapping (possibly confidence-scored, but not designed to hold permanently-unresolved forks as first-class citizens). That fork-tolerant, consensus-optional property is closer to the wiki/version-control tradition, or to argumentation-based knowledge models (e.g., IBIS-style issue/position/argument structures) that explicitly represent disagreement as structured data rather than requiring resolution.

So the excerpts describe something like an ontology-alignment/crosswalk *content* model wearing a wiki/commons-style *governance* model — no single established term of art owns that combination. Also worth flagging: the excerpts explicitly place this item under "Not built," so its data model (what a "typed link" actually consists of, how regeneration/caching works) is underspecified — the term may be doing double duty as both a described concept and an unimplemented design placeholder, which limits how precisely it can be mapped onto any one existing field's vocabulary.

