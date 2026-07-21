# Reading guide — where the judge attention budget is best spent

> **Post-submission addition (2026-07-20), navigational only — no new claims.** The as-submitted state is tagged `flf-submission`; ENTRY.md is unchanged. The entry's own one-line-per-section **Reading map** (ENTRY.md, after the abstract) routes within the entry; this page extends it to the whole package, following the competition's format guidance: a ~10-page core, supporting material, and appendices judges dip into. Artifacts added after the deadline are marked **[post-submission]** here and dated where they live.

## Core — the ~10-page end-to-end read

The entry end-to-end is ~1.5× the core budget; this is the ~10-page path through it:

1. **Abstract + Reading map** (ENTRY.md top) — the whole argument in one page, including the honest status sentence ("workflow design, not a retrieval algorithm").
2. **§1 Diagnosis** — the measured failure, 1985 → 2016 → 2026: precision observable, recall not.
3. **§2 The case** — the entry's own line: "If you read one section, read §2." Three retracted novelty claims on the author's own project, each preceded by a confident null; the countermeasure piloted on the same record.
4. **§5.5** — the pipeline's first full run: sealed synthetic test, 5/10 against a pre-registered ≥7 bar, coverage the binding constraint.
5. **§7 Discussion** — FLF's four questions answered directly, plus "What this entry is" and the built / exploratory / not-built accounting.

## Supporting — read where you want depth

- **Rest of the entry**: §3 (why shared vocabularies failed before; what LLM economics changes), §4 (the workflow, outward and inward — the design decisions carry the §5.3–§5.4 lessons), §5.1–§5.4 (the positive routing check and the pre-registered negatives), §6 (prior work, credited by name; the bounded absence claim), §8 (contributions).
- **[CLAIMS.md](CLAIMS.md)** — every load-bearing claim, one line with grade and support; the grade legend is at the top. Fast audit path: the Diagnosis block (C01–C06), the Case block (C07–C13 — C08/C09 are the "knowing didn't help" core; C13 is the value-regime hypothesis), then the §5 rows for the pre-registered outcomes. Built to be machine-read — pointing an AI at it is a supported use, per the competition's note that AI-assisted reading is welcome.
- **[GLOSSARY.md](GLOSSARY.md)** — §A: the entry's own coinages, each with the field's nearest established term and owner (the coin-time practice applied to itself); §B: established terms for readers outside the fields.
- **[EXPERIMENT-LOG.md](EXPERIMENT-LOG.md)** — protocol depth behind §5; E1–E5 map to §5.1–§5.5. If you open two slices: **E5** (the sealed-key protocol and per-version record) and **E3** (the end-to-end negative, with the grounded direct-model baseline).
- **[PSEUDOCODE.md](PSEUDOCODE.md)** **[post-submission]** — the workflow in annotated pseudocode, at-submission grades on every element.

## Run it — the most informative invocations

1. **The hook, on this repo's own vocabulary** [post-submission]: `bash hook/term-check.sh "misroute" ENTRY.md` — then score the flag against GLOSSARY.md's *misroute* row. Committed runs with receipts: [`hook/example/`](hook/example/). Details: [`hook/README.md`](hook/README.md).
2. **Scan mode — seed a glossary for any project** [post-submission]: the detect → curate → check flow in [`hook/README.md`](hook/README.md); the committed self-application on this repo's own prose is [`hook/example-scan/`](hook/example-scan/).
3. **The prototype (§5.1), offline and deterministic**: follow [`prototype/README.md`](prototype/README.md) — the committed run reproduces the rank-of-owner table without an LLM or network (first run downloads the embedding model); its "What runs, and how honest each stage is" table is the per-stage truth-in-advertising.
4. **The operations on a second provided case (the LHC/collider safety case)** [post-submission]: [`demo-collider/`](demo-collider/) runs scan → term-check → a cross-side define-then-verify cell on parts of a second FLF-provided case (eggs is the first, §5.1). The payoff is [`demo-collider/cross-side/RESULTS.md`](demo-collider/cross-side/RESULTS.md): on two known-opposite pairs, the blind usage-based verify returns the answer-keyed result — *dependent* for two reassurances a reader counts as independent (a theoretical accretion analysis and an empirical white-dwarf survival bound, which the physics literature already established as sharing an accretion premise), and *no shared premise* for a control pair of genuinely alternative arguments. Demonstration-grade, answer-aware, changes no at-submission grade.

## Appendices — no reading budget assumed

- **[`receipts/`](receipts/)** — start with `idiolect-trap-case-study.md` (the §2 reconstruction and graded term ledger) and `novelty-position.md` (per-claim novelty ledger + auditable search record); then the blind passes, the naming experiment, the capability ladder, and the citation audit.
- **[`eval/`](eval/)** — per-experiment pre-registrations, frozen specs, run receipts, and adversarial review logs (E2–E5 directories; `eval/peer-reconciliation*` holds the §5.5 execution record and sealed held-out test).
- **[`prototype/`](prototype/)** — code, committed run outputs, and honest-scope notes.
