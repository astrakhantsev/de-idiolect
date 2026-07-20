---
title: "Peer reconciliation — completion addendum: crosswalk data model, verifier design, screening gate, frozen-endpoint checklist"
date: 2026-07-18
status: "DESIGN DRAFT — NOT BUILD-READY. Joint Codex review with the SPEC (2026-07-19): MAJOR REVISION, 17 findings. Load-bearing ones: entailment direction REVERSED vs SPEC §2.4 (usage⇒definition here, definition⇒usage there — fix before anything else); composition table promotes binary judgments into SKOS claims with no abstention/adjudication states (add proposed_relation vs adjudicated_relation); content-addressed ID breaks versioning + fork coexistence (hash the full immutable record, ≥128 bits; separate pair-key from version-id); disputes/supersedes not actually representable as specced; decoy calibration circular/gameable; shared-core + residue GENERATION stage missing from the build plan entirely; human key not frozen or independent (verifier-selected quotes = circular); screening conflates discovery-lift with typing evaluation (separate strata + separate pair sources); §1/§5 overstate prior guard reusability and screening denominators (Guard 2 insufficient, Guard 3 Sonnet-only, Guards 5-6 unbuilt; OLS: 18 of 524 low-cosine pairs examined, not 1488 screened); budget incompatible with endpoints. Full review text archived at `2026-07-19-peer-reconciliation-REVIEW.md` (the authoritative source for the revision); revision is the first post-deadline design action, BEFORE the step-1 screening run. Entry fold: CANCELLED — the entry's 'part of the unbuilt design' language stays, correctly."
relates_to: "2026-07-18-peer-reconciliation-SPEC.md (the design this completes) · entry/FLF-entry-recall-extender.md §4 (commons versioning 'part of the unbuilt design'), §8/appendix (the promised funded evaluation: enforced word list, disjoint corpora, true A↔B pairs, community-identity probe) · 2026-07-18-e2e-cell-SPEC.md (G3 isolation harness reused; relation typing deferred there TO this study) · 2026-07-18-SESSION-SYNTHESIS.md (screens + attrition priors) · glossary.md (coin-time rows added 2026-07-18)"
---

# Peer reconciliation — completion addendum

## 1. Why this cell completes the system (the map)

The entry's component table has two rows that are neither measured nor instantiated: **relation typing** ("interface only; no live measured run") and the **commons** ("a design, not a prototype"). The e2e spec explicitly deferred relation typing as "a separate study — it needs concept pairs and frozen gold labels." The peer-reconciliation cell **is** that study by construction: its output is typed relations over concept pairs, scored against a frozen human-adjudicated key. And its output artifact — the crosswalk entry (§2 below) — **is** the commons entry format v0, including the versioning fields entry §4 names as "part of the unbuilt design." It is also, clause for clause, the funded evaluation the entry's appendix promises: *enforced word list, disjoint corpora, true A↔B pairs, a community-identity probe*. So after the e2e cell (anchoring regime) and this cell (peer regime), every box in the architecture has at least one measured run or one concretely-specced, instantiated artifact — that is the sense in which this "completes the system."

## 2. The crosswalk entry — the merge artifact, specced (data model v0)

The SPEC's §2.5 says "emit three artifacts, never one term" but does not spec the container. This is it. One entry per verified pair; the schema doubles as the commons cache-entry format (entry §4's regenerable-cache versioning: source hashes, generator+prompt identity, verifier provenance, regeneration lineage, forks-as-links).

```yaml
crosswalk_entry:
  id: cw-<hash8>                # content-addressed: sha256 over (term_a, term_b, relation, shared_core.text)
  pair:
    a: {term: "...", community: "...", corpus_manifest_sha256: ..., earliest_attested: {date, source}}
    b: {term: "...", community: "...", corpus_manifest_sha256: ..., earliest_attested: {date, source}}
  relation: skos:exactMatch | skos:broadMatch | skos:narrowMatch | skos:relatedMatch | noMatchDespiteSimilarity
  relation_direction: a-broader | b-broader | n/a        # populated only for broad/narrow
  shared_core:                  # the manufactured boundary object; SUPPLEMENTS both terms, replaces neither
    text: "<constrained definition that both sides' frozen usage satisfies>"
    wordlist_version: ...
  residue_a: {text: "...", evidence: [quote-refs into A's frozen excerpts]}   # what A covers that the core doesn't
  residue_b: {text: "...", evidence: [quote-refs into B's frozen excerpts]}
  evidence:
    a_def_vs_b_usage: {verdict: covers|fails, quotes: [...], polarity_check: pass|fail}
    b_def_vs_a_usage: {verdict: covers|fails, quotes: [...], polarity_check: pass|fail}
    retrieval: {a_to_b: {rank, chance}, b_to_a: {rank, chance}, corpus_sizes: {a, b}}
  provenance:
    generators: {a: {family, model, prompt_sha256}, b: {family, model, prompt_sha256}}   # cross-family enforced (SPEC §2.2)
    verifier: {family, model, prompt_sha256}         # third family where available; never the generating family of the side it judges
    excerpt_manifests: {a: sha256, b: sha256}
    pipeline_version: ...
  disputes: []                  # typed links to counter-entries filed by either side; never resolved in place
  supersedes: null              # regeneration lineage — a regenerated entry links its predecessor, never overwrites it
```

Design notes. (1) No field anywhere holds a "winning term" — the closest thing to a merge product is `shared_core`, and it is a definition, not a name; this is the refusal-to-canonicalize made structural rather than procedural. (2) `disputes` and `supersedes` are why forks coexist: disagreement and regeneration are both new entries plus links, so the commons never needs a write-lock or an adjudicator. (3) `earliest_attested` is recorded as data with no derived priority field — the SPEC's no-credit-adjudication rule, also made structural.

## 3. Verifier design (the one genuinely new component)

Everything else in the pipeline reuses built code (§5). The bilateral verifier is new, and it has four load-bearing choices:

1. **Usage-entailment, never definition-vs-definition.** Each side's definition is checked against the *other side's frozen usage excerpts*, exactly as the SPEC's §2.4 orders — and the reason deserves stating: definition-vs-definition similarity is **doubly confounded** in this design (both definitions are written in the same constrained wordlist, and both directions share one embedder), so it would manufacture overlap mechanically. Definition-vs-usage entailment shares neither confound. Definition-vs-definition cosine may be *logged* as a diagnostic; it may never feed a verdict.
2. **"Covers" is quote-gated.** "A's definition covers B's usage" = B's excerpts instantiate A's definition, and the verifier must return the instantiating quotes; a covers-verdict with no quote is invalid by rule (the 07-16 lesson that verdicts without evidence drift).
3. **Verdict composition table** (per pair, after both directions + retrieval):

| A-def covers B-usage | B-def covers A-usage | mutual retrieval hit | composed verdict |
|---|---|---|---|
| yes | yes | — | `skos:exactMatch` candidate |
| yes | no | — | A broader (B `skos:narrowMatch` of A) — *check the corpus-asymmetry hazard (§4) before accepting* |
| no | yes | — | B broader, symmetric |
| no | no | yes | partial overlap → `skos:relatedMatch` + shared-core + residues |
| no | no | no, but surface-similar | `noMatchDespiteSimilarity` — the jingle verdict |

4. **The no-match floor is calibrated, not asserted.** Before any live pair, the verifier runs on a small frozen calibration set that includes **decoy pairs** — surface-similar, known-different referents — and its per-class behavior is recorded. A verifier that never reaches no-match on decoys is rejected before it touches live pairs. (Decoy candidates to screen, not assert: reward hacking ↔ reward shaping; alignment tax ↔ alignment faking. Famous *equivalent* calibration pairs are fine here even though they are memorized — calibration measures rubric-following, not recall — but the memorization direction is stated: it inflates match verdicts on famous pairs, which is why the decoys are what the floor is calibrated on.)
5. **Round-trip polarity check per side** (SPEC §2.4's named hazard): each definition is independently checked for silently inverting the direction/polarity of the claim its excerpts make, before it is used in either retrieval or entailment. A polarity failure fails that side's config — a result, not a retry (same rule as the e2e fidelity gate).

## 4. Hazards to add to the SPEC's §3 list

- **Wordlist-compression overlap inflation.** The constrained vocabulary itself compresses; two definitions squeezed through the same small wordlist look more alike than the concepts are. Mitigated structurally by §3.1 (verdicts come from usage-entailment, not definition similarity); reported as a diagnostic delta where visible.
- **Corpus asymmetry masquerading as broad/narrow.** One-direction retrieval or entailment failure can reflect corpus *coverage*, not concept breadth. Rule: broad/narrow verdicts require the verifier to cite what the narrower side's corpus *does* discuss that falls inside the broader definition; per-side corpus sizes and topic spans print next to every asymmetric verdict.
- **Shared embedder across directions.** Both retrieval directions use one embedder (bge), a residual correlation between the two "independent" directions. Note it; on any headline pair, cross-check retrieval with a second embedder as a robustness line only.
- **Synthetic-pair correlation (if the synthetic testbed of §5 is used).** Two agent-grown idiolects raised by the same model family will converge lexically and manufacture agreement — cross-family per side is mandatory there, and any synthetic cell is labeled synthetic and never pooled with wild pairs.

## 5. Screening first — the gate step, and where pairs actually come from

The next buildable action is not the pipeline; it is a ~1–2h **screening run** that decides whether a public peer cell exists at all. It reuses committed code: Guard 0 cross-cosine (`scan_cross_cosine*.py`), the memorization-probe pattern (recall-backtest), the co-mention screen (cross-community build spec). Frozen expectation, from this project's own attrition record (MeSH 66→1→0; OLS 1488→0): **most or all of the SPEC's named alignment pairs die in screening** — activation steering ↔ representation engineering, scheming ↔ deceptive alignment are heavily cross-cited and near-certainly bridged in weights. A 0-survivor outcome is a *structural finding, not a failure*: it would say public post-LLM alignment vocabulary reconciles in-corpus and in-weights within months, which sharpens the tool's regime claim exactly the way the curated-synonyms kill did.

Strata, in descending cleanliness:

1. **Post-cutoff parallel coinages (renewable).** Harvest pairs from the same short window — two groups naming the same phenomenon in the weeks before they cross-cite. This stratum has the strongest external-validity property available to this project: **the evaluation window and the deployment window coincide** — the tool's live job is precisely to catch parallel coinage during the not-yet-reconciled weeks, so testing there is testing the actual use case, not a proxy.
2. **Private × public.** One side a live public young idiolect, the other a private project idiolect (this vault's own, or another private corpus). Bridges directly to the demonstrated C2 regime; memorization-clean on the private side by construction.
3. **Cross-language young communities** (e.g., Chinese-language alignment discourse vs Alignment Forum) — genuinely weakly cross-cited, but adds a translation confound that must be named as such.
4. **Synthetic testbed (controlled, labeled synthetic).** Two isolated cross-family agent threads each given disjoint document sets about the same post-cutoff phenomenon, allowed to coin internal vocabulary, then reconciled. Ground truth exists by construction (you planted the same referent), which solves the no-ground-truth evaluation problem for *verifier development* — then transfer to wild pairs for any claim.

## 6. Endpoint checklist (to be frozen at build time — this list is not the freeze)

- Bidirectional retrieval: rank vs printed chance (per actual corpus sizes) and vs raw-term queries, both directions.
- Typing accuracy: composed verdicts vs a frozen human-adjudicated key (the user adjudicates from quoted evidence only) on all cells run, reported per verdict class; the decoy no-match class counts — precision on no-match matters as much as recall on match.
- Residue quality: each residue text, used as a query over its own side's corpus, retrieves side-only documents above chance (the SPEC's "does the residue retrieve A-only content," quantified).
- **Community-identity probe** — the neutrality measurement the entry promises and the ablation could not perform: a classifier (or blind model) tries to identify which community a constrained definition came from; at-chance identification = the wordlist actually strips idiolect; above-chance = neutrality failed and the wordlist needs enforcement, not prompting. This is the first place the **enforced** LDOCE-style checker (mechanical lexicon filter + rewrite loop, currently unimplemented) becomes load-bearing rather than aspirational — build it here.
- Equal-information frontier baseline F (both corpora handed to one frontier model, "align these vocabularies"), same quadrant logic as e2e §4. Honest prior: on small two-corpus cells F likely matches the pipeline on alignment quality; the pipeline's marginal claim is the *artifact* (versioned, quote-gated, typed, disputable crosswalk) plus firing at detection time — state that before running, so an F✓ result cannot be read as a surprise.
- Promotion ceiling: exploratory cell(s), no recipe claim before a fresh-pair held-out test (the recipes-die-on-transfer rule; 7/7 on this project's record).

## 7. Build plan, reuse map, budget

| step | what | reuses | new code | est. |
|---|---|---|---|---|
| 1 | Screening run over candidate strata → gate: ≥1 surviving pair (else write the structural-finding addendum and stop) | Guard 0 scanners, memorization probe, co-mention screen | candidate list only | 1–2h |
| 2 | Corpus assembly per surviving pair (frozen manifests, disjoint, size-reported) | cross-community `build_corpus.py` pattern | thin | 1–2h/pair |
| 3 | Cross-family blind definition generation + polarity gate | e2e G3 isolation harness, leak-check pattern | prompts + polarity gate | 1h |
| 4 | Enforced-wordlist checker (lexicon filter + rewrite loop) | — | small, new | 1–2h |
| 5 | Bidirectional retrieval | eggs/e2e bge harness | thin | <1h |
| 6 | Bilateral verifier + decoy calibration + composition table (§3) | — | **the new component** | 2–3h |
| 7 | Crosswalk emitter (§2 schema) + first real commons entries | — | small, new | 1h |
| 8 | Adjudication (user, quotes-only) + write-up | — | — | ~45min user + 1–2h |

Total ≈ 8–12 agent-hours + under an hour of user adjudication, at Claude-Code pace. Everything through step 1 is runnable stand-alone and cheap; the gate decides the rest.

## 8. Sequencing

Post-deadline queue, per the SPEC's own status line — nothing here touches the FLF submission, and the SPEC + this addendum together *are* the continuation-work / funded-evaluation design the entry references. Codex review of both docs is queued together after the deadline. Step 1 (screening) is the first post-deadline action; it is cheap, reuses committed code, and its outcome — surviving pairs or a structural null — decides whether steps 2–8 run at all.
