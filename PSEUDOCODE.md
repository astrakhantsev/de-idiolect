# Pseudocode — the de-idiolect workflow (algorithm + key decision points)

> **Post-submission addition (2026-07-20),** answering the competition's format guidance for code submissions (readable pseudocode capturing algorithm and key decision points). The as-submitted state is tagged `flf-submission`; ENTRY.md is unchanged. This page introduces no new claims and carries the entry's **at-submission** implementation grades throughout; the one post-submission artifact it mentions (the coin-time hook) is bracketed as such and changes no grade.

**Status labels** (ENTRY.md's "What is built and what is not"): `[P]` component implemented in the committed prototype · `[M]` measured (ENTRY §5 / EXPERIMENT-LOG) · `[U]` unbuilt proposal. **The composed pipelines below are `[U]`: the implemented components exist as separate pieces whose dataflow is not wired into an automatic system.** The two properties the architecture is built on — live cross-community matching and an enforced wordlist — are exactly the unrun ones.

## Outward: detect → define → match (ENTRY §4.1) — composition `[U]`

```
DE-IDIOLECT-OUTWARD(corpus_A, target_corpora):   # lazy, per-concept, on demand;
                                                 # no universal resource; corpora are
                                                 # SUPPLIED — community discovery [U], manual
  # 1. DETECTION                                 [P]; retrospective endpoint [M]: MISSED
  terms ← term-recognition(corpus_A               # prototype: TF-IDF keyness contrasting
            vs the other community sub-corpora)   # community sub-corpora; ranked the true
                                                  # e2e coinage ~224
  # 2. CONSTRAINED DEFINITION                    [P] generation behind an operational
  for t in terms:                                 #   interface; wordlist enforcement [U]
    excerpts ← passages of corpus_A using t       # frozen usage, nothing else
    keys_t ← retrieval keys for t                 # may be cheap, LOSSY, plural (term,
                                                  # restated question, definition); multi-key
                                                  # union conjectural — fusion cell null [M]
    rep_t ← faithful representation of t:         # self-contained, operational; ONLY a small
      kind-of-thing, inputs/outputs, what it      # fixed vocabulary of ordinary words +
      asserts, when it applies                    # simple notation; NO names of people,
                                                  # methods, or fields
    FIDELITY-GATE(rep_t, excerpts):               # round-trip entailment + external-name ban
      # gate calibrates [M]: passes 4/4 faithful, catches 5/5 seeded defects — on
      # author-constructed materials (non-degeneracy check, NOT a population FP rate);
      # checklist-guided regeneration passes 2/2 where unguided failed 0/2 (n=1/config,
      # stricter prospectivity reading arguably unmet)
      # DECISION (key/representation split): lossy keys may FETCH candidates, but no
      # mapping advances to verification or publication without a gate-passing rep_t;
      # fidelity-before-retrieval remains the default ordering.
      # DECISION: the generator is replaceable behind this contract (model / prompting /
      # extraction / human); no implementation has demonstrated full compliance.

  # 3. DEFINITION-MEDIATED MATCHING
  for t in terms:
    candidates ← search(target_corpora,           # retrieval [P] (bge-large-en-v1.5,
                        keys = keys_t)            #   offline, deterministic) — §5.1's
                                                  #   load-bearing measurement [M]
    for c in candidates:                          # pairwise verification: [M] on the §5.5
      relation ← verify-pairwise(rep_t, c)        #   SYNTHETIC harness only; [U] live;
        ∈ {skos:exactMatch, broadMatch,           # relation typing: [P] scaffold/interface
           narrowMatch, relatedMatch,             #   (author-frozen labels in the committed
           NO-MATCH, ABSTAIN}                     #   run), [M] synthetic §5.5 only
      # SKOS names verbatim — local names for standard relations would repeat the error
      # being fixed. ABSTAIN and "no match despite surface similarity" are first-class;
      # broad/narrow direction explicit (subject = narrower side).
    emit only gate-passed, verification-passed mappings, with provenance
      # commons write-back [U]: a derived, versioned, regenerable cache — forks allowed,
      # disagreement is a typed link, NEVER a canonical merge; verification judgments
      # and dispute records durable.
```

## Inward: the same stages at three workflow moments (ENTRY §4.2) — all `[U]` at submission

```
ON coin-time(term, usage_files):                                     [U] as graded
  excerpts ← passages(usage_files, term)          # information boundary: excerpts ONLY —
  restatement ← neutral definition of term        # no conclusions, no candidate owners
    from excerpts (stage-2 contract)              # the define stage, turned inward
  candidates ← nearest established terms + owning fields + oldest expected treatments,
    from an ISOLATED weights-only call            # reverse-dictionary direction — never
                                                  # "find prior art on X"
  flag as UNVERIFIED → open ≥1 primary per relied-on candidate
  # DECISION: a HOOK, not a standing instruction — instructions were installed during
  # the §2 record and the failure still occurred; a hook fires deterministically.
  # [post-submission, no grade change: a v1 of the MINIMAL hook — the isolated call
  # without the full detect→define→match mapping — now exists at hook/, with isolation
  # mechanics, manifests, and a self-application example; see hook/README.md]

ON claim-time(claim):                                                [U] proposal
  compare regenerate("what does this claim MEASURE?")
     with regenerate("what does the instrument COMPUTE?")
  if not mutually entailed: flag estimand drift    # the error class that inverted
                                                   # Program A's headline (§2)

ON cite-time(citation):                                              [U] as tooling
  open the primary; check the venue; read past the ellipsis
  if unreachable or mismatched: flag before shipping
  # The underlying MANUAL audit is measured [M]: 66/100 occurrences survive at the
  # lenient endpoint (43/91 strictest), zero confirmed fabrications among checkable,
  # ~1 search + 2 fetches per work — the automation of it is not built.
```

**Where the honest boundaries sit** (unchanged from the entry): detection missed its one retrospective endpoint; the wordlist constraint is designed but unenforced; the composed pipeline's only full run is §5.5's **synthetic sealed test — 5/10 planted pairs against a pre-registered bar of ≥7** (detection precision 1.00, zero false matches, all asserted relations typed correctly; **coverage 0.6 was the binding constraint**, lost at generation-quality gates) `[M synthetic]`; live-community deployment `[U]`; and on the one private-coinage cell an equal-information direct model ask matched or beat the pipeline's mechanical form (§5.3). The submission's case rests on workflow properties — deterministic triggering, blindness, verification, durable reuse — not on out-retrieving a frontier model with the same corpus access.
