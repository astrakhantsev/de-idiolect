---
title: "Peer reconciliation — revision analysis: 17 findings distilled, v0.2 minimal design, synthetic smoke test, implementation sketch"
date: 2026-07-19
status: "ANALYSIS + DESIGN PROPOSAL — response to the 2026-07-19 joint Codex review (MAJOR REVISION, 17 findings). Nothing here is built. v0.2 and the smoke test are PROPOSALS awaiting user approval; findings distillation is descriptive. Markers: [R-Fn] = the review demands it (finding n); [P] = my proposal, one defensible choice among several."
relates_to: "2026-07-19-peer-reconciliation-REVIEW.md (authoritative findings text) · 2026-07-18-peer-reconciliation-SPEC.md · 2026-07-18-peer-reconciliation-completion-ADDENDUM.md · entry/FLF-entry-recall-extender.md §3–§4, §8 (frozen intended properties) · 2026-07-18-e2e-cell-SPEC.md (G3 isolation, leakcheck, retrieve.py reused)"
---

# Peer reconciliation — revision analysis (v0.2 proposal + synthetic smoke test)

**Intended-properties audit (read first).** The FLF entry freezes six intended properties: (1) blind cross-family definition generation per side, (2) bilateral verification of each definition against the OTHER side's usage — never definition-vs-definition, (3) jingle "no match despite surface similarity" as a first-class verdict, (4) three artifacts (typed relation, shared core, residues) and never a winning term, (5) attestation dates as data with no priority computed, (6) screening gate first with zero-survivor itself informative. **All six survive this revision.** None is violated by any fix below. Two are narrowed: property 5 survives *strengthened* by the F16 rename (`earliest_found_in_search` + search-scope fields makes "dates as data, no priority" enforceable rather than aspirational); property 6 survives *scoped* — zero-survivor is informative about the frozen candidate frame/models/screens only, not about field-wide reconciliation speed [R-F15], and the gate now gates only the wild discovery track, not verifier qualification [R-F12]. The entry's phrasing "each definition against the other side's usage" is direction-neutral, so adopting the addendum's entailment direction (§2a below) does not contradict the frozen entry text.

## 1. Findings distilled

Severity: **blocking** = build produces invalid results or unimplementable artifacts as specced; **material** = wrong claims or wasted work but a build could mechanically proceed; minor = none — the review contains no cosmetic findings. Blocking count: **9** (F1, F2, F3, F4, F7, F8, F10, F11, F12).

### Group A — verifier logic (F1, F2, F9)

- **F1 · Entailment direction reverses between docs — BLOCKING.** SPEC says definition⇒usage, addendum says usage-instantiates-definition; no per-excerpt proposition, no aggregation rule, so one cherry-picked quote can approve a relation or flip broad/narrow. Fix: pick ONE direction (§2a: the addendum's), formalize per-excerpt with `instantiates | contradicts | insufficient`, frozen aggregation + abstention [R-F1].
- **F2 · Composition table doesn't identify the claimed relations — BLOCKING.** Mutual coverage ≠ exactMatch (only "observationally equivalent on these excerpts"); retrieval-hit + double-fail ≠ partial overlap (co-occurring concepts retrieve each other); no outcomes for mixed evidence, insufficiency, polarity failure, or no/no/no without surface similarity. Fix: outputs become `proposed_relation` candidates only, add `insufficientEvidence` and plain `noMatch`, overlap requires shared-core evidence, breadth requires cited counterexamples [R-F2].
- **F9 · SKOS broad/narrow direction ambiguous — material.** `relation` + `relation_direction` never fix the SKOS subject, so two conforming builds emit opposite triples. Fix: store only `broader_side: a|b` and derive `(narrower, skos:broadMatch, broader)` deterministically [R-F9].

### Group B — schema & commons (F3, F6, F7, F8, F16)

- **F3 · exactMatch-candidate vs final `relation` field inconsistent — BLOCKING.** The table emits candidates; the schema has only one final field, so provisional machine judgments publish as final commons entries. Fix: `proposed_relation` + `adjudicated_relation` + `status` + adjudicator provenance + rejection/abstention states [R-F3].
- **F6 · One-entry schema doesn't implement the three-artifact contract — material.** Three artifacts live as unversioned fields in one record; cardinality undefined (no-match would carry a manufactured shared core, exactMatch nonsense residues). Fix: declare them components of one immutable record (revising the SPEC's wording — the review explicitly offers this branch) + per-relation required/null rules; no-match emits rejection evidence, never a shared core [R-F6].
- **F7 · Content-addressed ID breaks versioning and fork coexistence — BLOCKING.** `sha256(term_a, term_b, relation, shared_core.text)` at 8 hex: changed evidence reuses the same ID, identical text from different provenance collapses, self-supersede possible, 32-bit collision space. Fix: stable `pair_key` separate from immutable `version_id` = sha256 over canonical serialization of the complete record, ≥128 bits [R-F7].
- **F8 · Disputes/forks asserted but not representable — BLOCKING (for the commons claim).** `disputes: []` has no link schema; `supersedes` is single-parent; no append-only rule — so "forks coexist, no write-lock" is aspiration, not property. Fix: typed immutable link records, multi-parent `derived_from`, append-only index, and actually DEMO two coexisting incompatible mappings before claiming the property [R-F8].
- **F16 · `earliest_attested` performs implicit credit adjudication — material.** A single displayed date without search ledger reads as a priority result despite no computed field. Fix: rename `earliest_found_in_search`, store search scope/date/coverage + competing attestations, prohibit priority inference in the record itself [R-F16].

### Group C — evaluation validity (F4, F5, F10, F11)

- **F4 · Decoy calibration circular and gameable — BLOCKING.** "Reject a verifier that never says no-match" passes an always-no-match verifier; famous decoys let the model answer from memorized pair identities; the decoys themselves are unscreened candidates. Fix: frozen, anonymized, independently labeled, class-balanced calibration with full confusion matrix — which the synthetic smoke test provides by construction (§2c, §3) [R-F4].
- **F5 · Community-identity endpoint rewards semantic erasure — material.** At-chance identification is only valid with semantic content held constant; on broad/narrow/partial pairs faithful definitions SHOULD be identifiable, and vacuous ones ace the test. Fix: restrict to content-matched exact-match cases and gate jointly on fidelity + retrieval, or drop as endpoint (v0.2 drops it, §2 cuts) [R-F5].
- **F10 · Shared-core/residue generation absent from the build plan — BLOCKING.** The distinctive output has no generating step, prompt, fidelity gate, or evidence rule; residue evaluation reuses the derivation corpus (circular via topical cues). Fix: explicit decomposition stage with frozen prompts + abstention, evaluated on held-out side documents + far-side exclusion [R-F10].
- **F11 · Human key neither frozen nor independent — BLOCKING.** Adjudication happens after verifier execution, from verifier-selected quotes — the verifier controls the evidence used to judge itself. Fix: freeze excerpts + labels before verifier output, independent blind adjudication, calibration/dev/held-out disjoint; in v0.2 the constructed synthetic key replaces human adjudication entirely [R-F11].

### Group D — regime & strata scoping (F12, F13, F15)

- **F12 · Screening conflates discovery redundancy with typing evaluation — BLOCKING.** Guard 0 / co-mention / memorization screens are discovery-lift filters; applied to typing they discard the best gold-labeled cases while admitting unconfirmed pairs, and nothing establishes that survivors actually co-refer ("true A↔B pairs" have no acquisition procedure). Fix: separate a discovery-lift track from a typing/artifact track; typing pairs come from controlled construction or expert nomination with independently frozen positive labels [R-F12].
- **F13 · Strata don't consistently target the no-canonical regime — material.** Addendum strata silently replace SPEC strata; private×public is an anchoring case; cross-language lacks translation control; the synthetic "same referent" design yields only exact-match ground truth. Fix: one normative stratum table with eligibility/confounds/allowable claims; never pool regimes; synthetic must plant ALL relation classes, not just exact (§3 does) [R-F13].
- **F15 · Zero-survivor cannot support the "reconciles within months" conclusion — material.** The attrition evidence is curated medical synonyms; the alignment candidate list is small and convenience-selected; screen failures have non-semantic causes (embedder, probe error). Fix: scope any zero result to the frozen candidate frame; field-wide temporal claims need a separate sampling study [R-F15].

### Group E — claims honesty & budget (F14, F17)

- **F14 · Prior results overstated — material (blocking for any published claim text).** Polarity-only check ≠ the multi-dimensional e2e fidelity gate; Guard 2 insufficient / Guard 3 Sonnet-only / Guards 5–6 unbuilt per the cross-community ledger; "OLS 1488→0" misstates 18-of-524 low-cosine pairs manually examined; MeSH passes conflated. Fix: exact ledger language everywhere (§2e) [R-F14].
- **F17 · Budget and sample plan mutually incompatible — material.** Per-class accuracy over five verdicts + held-out + decoy precision + fork testing cannot fit 8–12h or a one-survivor gate; implementors can't tell demo from study. Fix: freeze minimum cases per class, separate prototype/calibration/held-out phases, re-estimate after counts are fixed; v0.2 explicitly declares itself the prototype+calibration phase, retracting the 8–12h full-study claim (§2 cuts, §4 estimate) [R-F17].

## 2. Revised minimal design (v0.2) [P throughout, satisfying every [R] above]

**Scope declaration (answers F17's "demo, calibration set, or study?").** v0.2 is a **verifier-qualification prototype**: it builds the full pipeline (generate → retrieve → verify → compose → decompose → emit) and qualifies it on the synthetic smoke test of §3, whose planted key doubles as the frozen calibration set F4 demands. It makes NO wild-pair claims, NO discovery-lift claims, NO regime claims. The wild-pair study (screening run, strata table, human key, per-class counts, re-estimated budget) is a separate later phase, gated on smoke PASS.

### 2a. Entailment direction — resolved [R-F1]

**The correct direction is the addendum's: usage instantiates definition, evaluated per excerpt.** The SPEC's "A's definition entails B's usage" is logically incoherent: a definition is a class-level universal and cannot entail any particular usage statement — a judge asked to check it falls back to topical similarity, which inflates matches (exactly the mechanical-overlap failure the design exists to avoid). The review's own fix sketch (`usage_excerpt ⇒ candidate_definition`) endorses this direction. The entry's frozen phrasing ("each definition against the other side's usage") is direction-neutral and remains satisfied: the definition is still checked against usage excerpts, never against the other definition.

**Formalization (frozen in prereg before any run):**
- Tested proposition, per excerpt `e ∈ E_B` (a FIXED pre-registered sample of B's frozen usage excerpts, n per side fixed in prereg, [P] n=8): "the referent of term_b as used in `e` is an instance of the concept defined by `D_A`." Verdict `inst(e, D_A) ∈ {instantiates, contradicts, insufficient}`; `instantiates` and `contradicts` each require a verbatim quote from `e` (quote-gated, kept from addendum §3.2).
- Aggregation: let k = #instantiates, c = #contradicts, u = #insufficient over the n excerpts. If u > n/3 → **ABSTAIN** (insufficientEvidence). Else `covers` iff k/(n−u) ≥ 0.7 AND c = 0; `fails` iff k/(n−u) ≤ 0.3 OR c ≥ 2; anything between → **mixed** (insufficientEvidence). [P thresholds; frozen at prereg, and that freeze is what kills cherry-picking — one overlapping quote can no longer approve anything.]
- Breadth requires counterexamples [R-F2]: "A broader" additionally requires ≥2 cited excerpts in `E_A` that fail `D_B` (the counterexample set), plus the corpus-asymmetry check kept from addendum §4: the verifier must cite what A's corpus discusses inside `D_A` but outside `D_B`, with per-side corpus sizes printed.
- Polarity check per side runs before verification, labeled **polarity-only** — explicitly NOT "the same rule as the e2e fidelity gate," which covered multiple dimensions [R-F14]. Polarity failure → configFail for that side, a result not a retry.

### 2b. ID scheme — fork-coexistent [R-F7, R-F8]

- **`pair_key`** (stable grouping key, not an identity claim): sha256-16hex over canonical `sorted[(community_a, term_a), (community_b, term_b)]`. Groups all records about one pair; collisions merely group, so 64 bits suffices.
- **`version_id`** (immutable identity): full sha256 (64 hex, 256 bits ≥ the demanded 128) over a canonical JSON serialization of the COMPLETE record minus the id field itself — corpus manifests, all evidence, provenance (generator/verifier families + prompt hashes), residues, proposed_relation, adjudicated_relation, timestamps, `derived_from`. Any change to any field is a new version_id by construction; identical text from different provenance gets distinct ids; self-supersede is impossible (a record cannot contain its own hash in `derived_from`).
- **Storage: append-only.** `records/<pair_key>/<version_id>.json`; an index file only ever appends lines. `derived_from: [version_id, ...]` is a list (multi-parent reconciliation representable). **Disputes are their own immutable record type**: `{dispute_id, target_version_id, claimant, claim_type ∈ {rejects_relation, rejects_shared_core, rejects_residue, rejects_evidence}, evidence_quotes, timestamp}` — filed alongside, never editing the target.
- **The property is demonstrated, not asserted** [R-F8]: the smoke test's E3 endpoint (§3) files two incompatible records under one pair_key plus a dispute link and shows both render and coexist.
- Relation state [R-F3]: records carry `proposed_relation` (machine, from the composition stage), `adjudicated_relation` (null until an adjudication event, which is itself provenance-stamped), `status ∈ {proposed, adjudicated, rejected, abstained}`. In v0.2 smoke runs, adjudication = the planted key, stamped as `adjudicator: synthetic-key-<hash>`.
- Attestation [R-F16]: field renamed `earliest_found_in_search: {date, source, search_scope, search_date, coverage_note, competing_attestations: []}` with a fixed record-level note "no priority inference licensed." (In the synthetic smoke this field is exercised with generated dates to prove the schema, labeled synthetic.)

### 2c. Calibration — replaced, not patched [R-F4]

The famous-decoy calibration is **dropped entirely**. Both of its defects are unfixable in place: famous pairs are answerable from memorized identities (measured project-wide: curated synonyms are memorized by construction), and any one-sided rejection rule ("never says no-match → reject") is gameable by the opposite degenerate verifier. Replacement: **the synthetic smoke test IS the calibration** — its planted key is frozen before any verifier call, independently labeled (by construction), class-balanced across all six outcomes, and anonymized by construction (freshly coined terms have no memorized pair identities). Scoring is the full confusion matrix, so an always-no-match verifier fails on the planted match classes and an always-match verifier fails on planted no-match/jingle classes — no degenerate strategy passes. Any future wild-pair phase still needs its own frozen human key with dev/held-out separation [R-F11]; that is out of v0.2 scope and said so.

### 2d. Discovery vs typing — separated [R-F12, R-F13]

- **Track T (typing + artifacts) — what v0.2 runs.** Input pairs come from controlled construction (synthetic, §3) where co-reference and relation labels are frozen ground truth. Discovery screens do NOT gate this track — a bridged pair is fine here if typing is nontrivial. All Track-T results are labeled synthetic and never pooled with wild results [R-F13].
- **Track D (discovery lift) — deferred.** The wild screening run (Guard 0, co-mention, memorization probe over post-cutoff parallel coinages) remains the entry's screening-gate-first commitment, but it gates only Track D. Its zero-survivor outcome is reported scoped: "zero survivors among THIS frozen candidate list under THESE screens/models/corpora" [R-F15] — still informative (the entry's property 6 holds), but the "public alignment vocabulary reconciles within months" generalization is retracted as a claimable conclusion.
- The composition stage (verify → proposed_relation) and the decomposition stage (shared-core + residues) are now **explicit, separate pipeline stages** with their own prompts, abstention rules, and outputs [R-F10] — see stage list below.

### 2e. Prior-guard claims — weakened to the ledger [R-F14]

Defensible reuse statement, verbatim for all v0.2 docs: "Reused as **code**: the Guard 0 cross-cosine scanner, the e2e G3 isolation runner (`run_isolated.sh`), the frozen-pattern leakcheck mechanism (with a NEW pattern list), the bge retrieval harness (`retrieve.py` pattern), and the cross-community corpus-manifest pattern. NOT reused as validated guards: Guard 2 (ledger: insufficient), Guard 3 (ledger: Sonnet-only), Guards 5–6 (unbuilt). Attrition record cited exactly: MeSH 66→1 and →0 were separate passes; OLS: 18 of 524 low-cosine pairs manually examined out of 1488 total — the 1488 were never all screened. The polarity check is polarity-only, a strict subset of the e2e fidelity gate's dimensions."

### 2f. v0.2 pipeline (stages, in order)

1. **Freeze** — prereg.md: entailment proposition + thresholds (§2a), composition rules (below), endpoints (§3), leakcheck pattern list, excerpt samples, DEV/HELD-OUT split per side.
2. **Generate** — per side, cross-family, isolated (`run_isolated.sh`), constrained definition from own DEV excerpts only; leakcheck (other side's terms + key phrases); polarity-only gate.
3. **Retrieve** — bge cross-retrieval both directions, chance printed per actual corpus sizes (retrieve.py pattern).
4. **Verify** — per-excerpt instantiation over the other side's frozen DEV sample, both directions (§2a).
5. **Compose → `proposed_relation`** — replacing the v0.1 table [R-F2, R-F3]: covers/covers → proposed exactMatch; covers/fails + ≥2 counterexamples + asymmetry check → proposed broad/narrow with `broader_side` (SKOS triples derived deterministically as `(narrower_term, skos:broadMatch, broader_term)` [R-F9]); fails/fails + mutual retrieval hit + decomposition stage SUCCEEDS with quote evidence from both sides → proposed relatedMatch (retrieval alone never suffices); fails/fails + no mutual hit + surface-similarity flag (term-string edit/embedding similarity above prereg threshold) → proposed noMatchDespiteSimilarity with rejection evidence; fails/fails + no similarity → proposed noMatch; any ABSTAIN/mixed/polarity-fail → insufficientEvidence / configFail, never a relation.
6. **Decompose** [R-F10] — new stage, frozen prompt: shared-core (a constrained definition, quote-gated against BOTH sides' DEV excerpts) + per-side residues (quote-gated, wordlist-checked); abstention allowed and recorded; cardinality per relation [R-F6]: exactMatch → residues may be empty; broad/narrow → asymmetric residues required; relatedMatch → all three required; noMatch* → NO shared core, rejection evidence instead.
7. **Emit** — crosswalk record v0.2 (§2b), append-only.
8. **Score** — against the planted key: full confusion matrix; residues evaluated on HELD-OUT own-side docs + far-side exclusion (never the derivation corpus) [R-F10, R-F11].

### 2g. What v0.2 cuts from v0.1, and why each cut is safe

- **Famous-decoy calibration** → replaced by planted-class qualification (§2c). Safe: calibration was measuring rubric-following, which the synthetic key measures better and without memorized identities.
- **Community-identity probe as an endpoint** [R-F5] → cut; optionally logged as a diagnostic on exact-match planted pairs only (content-matched, so the confound is controlled), never a pass/fail. Safe: no v0.2 claim depends on neutrality measurement.
- **Enforced LDOCE wordlist checker** → downgraded to the existing pattern-based check + logged violation counts. Safe: only the identity probe made enforcement load-bearing; with the probe cut, logging suffices for v0.2.
- **Wild strata 1–3 (post-cutoff harvest, private×public, cross-language) + the screening run** → deferred behind smoke PASS. Safe: screening gates Track D only [R-F12]; verifier qualification does not need wild pairs, and running wild pairs through an unqualified verifier is exactly what the review forbids.
- **Per-class typing accuracy against a frozen human key** → deferred with the wild phase [R-F11, R-F17]. Safe: the constructed key replaces human adjudication at prototype stage; the human-key protocol (frozen-before-output, blind, disjoint dev/held-out) is specced but not executed.
- **"Completes the system" / funded-evaluation framing** (addendum §1) → weakened to "instantiates the crosswalk format and qualifies the verifier"; the funded evaluation requires the F17 re-estimate after class counts are frozen. Safe: this is a claims change, not a capability change — and it is the honest reading of F17.

## 3. Synthetic smoke test design [P]

**Construction.** One shared concept inventory of ~11 fictitious-but-coherent technical concepts (post-cutoff-flavored, e.g. invented agent-evaluation phenomena — content chosen so no real established term exists to collide with). Two synthetic communities, A ("forum register") and B ("preprint register"), each a corpus of 10–12 short documents (150–300 words) coining its own vocabulary over its assigned slice of the inventory. Term assignment is orchestrator-controlled: the orchestrator (not the generator models) decides every coined term, which is what makes jingle planting deterministic.

**Planted cells — 10 evaluation pairs (smoke-sized, all six outcome classes covered [R-F13]):**
- 2 × **exactMatch**: same concept, different coined terms in A and B.
- 2 × **broad/narrow** (one each direction): A's concept strictly contains B's (and vice versa for the second), with the containment written into the key as explicit membership conditions.
- 2 × **partial-overlap (relatedMatch)**: two concepts sharing a planted core with planted per-side residues — the decomposition test.
- 2 × **jingle**: the SAME orchestrator-assigned surface term used by both communities for two different planted concepts → expected noMatchDespiteSimilarity.
- 2 × **noMatch distractors**: unrelated concepts, surface-dissimilar terms → expected plain noMatch (tests that the pipeline does not force matches, and exercises F2's added no/no/no-without-similarity outcome).

**Leak discipline (how documents are generated without the key entering the pipeline):**
- The **key file** (concept descriptions, relation labels, planted residues, term assignments) is written first and lives OUTSIDE the corpus directories; the pipeline stages receive only document text, enforced by `run_isolated.sh` (fresh cwd/HOME, credentials only — the key physically cannot be read).
- **Generator calls**: family X writes A's docs given only (A's term assignments, A's concept descriptions, register instructions); family Y writes B's likewise. Neither generator sees the other community's terms, the relation labels, or the pair list. Generators are instructed to write **applied/incidental usage** (worked examples, disagreements, measurements) and explicitly NO definitional prose — mitigating the docs-as-key-paraphrase circularity below.
- **Grep leakchecks** (frozen pattern list, leakcheck_e2e.sh mechanism): (i) no coined term of one community appears in the other's docs (except the two planted jingle strings, whitelisted); (ii) no distinctive key phrase (pattern list built from the key's load-bearing nouns) appears verbatim in any doc; (iii) standard answer-vocabulary check on generated definitions.

**Pre-registered endpoints (frozen in prereg.md before any pipeline call; 3 load-bearing numbers, per probability discipline):**
- **E1 (typing):** full confusion matrix over the 10 pairs. PASS = ≥7/10 `proposed_relation` exactly correct AND 0 of the 4 planted no-match pairs (jingle + distractor) promoted to any match class AND ≥1 of 2 jingle pairs receives noMatchDespiteSimilarity specifically. (Chance under 6 classes ≈ 1.7/10; the bar is far above chance yet forgiving of 3 misses on n=10.)
- **E2 (decomposition):** for the 2 partial-overlap pairs — shared-core generated without abstention and satisfied by both sides' HELD-OUT excerpts (verifier check), and ≥1 of 2 residues passes far-side exclusion (own-side held-out retrieval above chance AND far-side held-out at/below chance). The failing case, if any, gets a written examination.
- **E3 (mechanics/fork demo):** two incompatible records filed under one pair_key coexist with distinct version_ids, plus one dispute record linking them; both render from the append-only index. Binary [R-F8].
- **FAIL on any endpoint = revise before any wild pair.** All per-class results are reported regardless of PASS/FAIL.

**What the smoke test CAN establish:** the pipeline runs end-to-end; the frozen aggregation rules discriminate planted classes well above chance on cooperative data; the jingle verdict is reachable in practice; the record/ID/fork machinery delivers the coexistence property; degenerate verifiers (always-match, always-no-match) are excluded. **What it CANNOT establish:** anything about wild pairs, discovery lift, the no-canonical regime claim, definition neutrality, or transfer — synthetic PASS is a floor, and the project's own 7/7 recipes-die-on-transfer record forbids reading it as more. Named circularity risks: (1) **generator-shared-with-judge** — a verifier from the same family that wrote the excerpts it judges shares paraphrase/style priors; mitigation: verifier family ≠ the family that generated the excerpts being judged (three families total if available; with two, cross-assign so each side's excerpts are judged by the family that did NOT write them). (2) **Docs as key paraphrases** — synthetic docs risk being near-restatements of the concept descriptions, making instantiation artificially easy; mitigation: the no-definitional-prose instruction + spot-check, and honesty that E1 difficulty is therefore a lower bound on wild difficulty. (3) **The main threat: single-family synthetic communities are trivially bridgeable** — memorization-free but style-shared, so retrieval and matching succeed on register statistics rather than content; **cheapest mitigation, mandatory: different model families generate A and B** (family X ≠ family Y), plus report Guard-0 cross-cosine between the coined term strings and between corpora as a difficulty diagnostic (high cosine = easy test, reported not gated).

## 4. Implementation sketch [P]

**Layout** under `/mnt/f/src/minelit/flf-epistack/eval/peer-reconciliation/`:

```
peer-reconciliation/
├── prereg.md                  # frozen: proposition, thresholds, composition rules, endpoints, pattern list
├── key/
│   ├── concepts.json          # inventory + relation labels + term assignments (NEVER readable by pipeline calls)
│   └── answer_key.json        # the 10 pairs with expected outcomes
├── corpora/{a,b}/*.md         # generated docs + manifest.json (sha256 per doc, build_corpus.py pattern)
├── prompts/                   # gen-community-{a,b}.md, gen-definition.md, verify-excerpt.md, decompose.md
├── leakcheck_peer.sh          # frozen patterns: cross-community coined terms + key phrases (leakcheck_e2e.sh mechanism)
├── gen_communities.py         # orchestrates community generation via run_isolated.sh (families X, Y)
├── gen_definitions.py         # per-side blind definition generation + polarity-only gate
├── retrieve_xc.py             # bge bidirectional retrieval + chance print (e2e retrieve.py adapted)
├── verify.py                  # per-excerpt instantiation calls + aggregation + composition → proposed_relation
├── decompose.py               # shared-core + residues, cardinality rules, abstention
├── emit_crosswalk.py          # record v0.2: pair_key/version_id, append-only records/, dispute record type
├── score.py                   # confusion matrix vs key, held-out residue eval, far-side exclusion, report
└── records/<pair_key>/<version_id>.json
```

**Reused machinery (confirmed present):** `e2e-cell/run_isolated.sh` (per-call isolation, credentials-only HOME — called in place, not copied); `e2e-cell/leakcheck_e2e.sh` (mechanism template for leakcheck_peer.sh with a new frozen pattern list); `e2e-cell/retrieve.py` (bge-large-en-v1.5 local snapshot, serialization + chance-print pattern); `cross-community/build_corpus.py` (manifest pattern); `cross-community/scan_cross_cosine*.py` pattern for the term-string difficulty diagnostic.

**Steps and hours (LLM-assisted pace, per feedback_time_estimates):** (1) prereg + concept inventory + answer key ~1h; (2) community generation + leakchecks ~1h (two families × ~11 short docs each, orchestrated calls); (3) definitions + retrieval ~0.5–1h (heavy reuse); (4) verify.py + composition — the new component — ~1.5–2h; (5) decompose.py + emit_crosswalk.py + fork demo ~1–1.5h; (6) score.py + run + write-up ~1h. **Total ≈ 5–7 focused hours** of agent time + ~15–30 min user spot-checks (key sanity, 2–3 doc reads, PASS/FAIL sign-off). Minimal same-day path ≈ 4h by deferring E2 (decomposition endpoint) to a second sitting — E1 + E3 alone already discharge F1/F2/F3/F4/F7/F8/F12; E2 discharges F10. This estimate covers the SMOKE TEST ONLY; the wild-pair study is re-estimated only after class counts are frozen [R-F17].
