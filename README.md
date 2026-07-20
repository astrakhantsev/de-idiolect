# de-idiolect

Code and receipts for **"The vocabulary seam: why cross-community knowledge doesn't compound, and a lazy way to bridge it"** — an FLF Epistemic Case Study Competition entry. *De-idiolect* (verb): produce a description of a concept with the community's local vocabulary removed, and use that — not the term — as the retrieval key.

**Status: draft package.** The entry itself is published separately and links here; the interactive architecture diagram is pending realignment.

## Entry companions (repo root)

- `CLAIMS.md` — the claims register: every load-bearing claim, one line each, with evidence grade and support.
- `GLOSSARY.md` — the entry's terms.
- `EXPERIMENT-LOG.md` — protocol-level detail behind the entry's §5 (endpoints, operating characteristics, bounds).

## Code and run receipts

- `prototype/` — the runnable recall-extender prototype on FLF's eggs case (entry §5.1): detection (TF-IDF keyness), constrained-definition generation (pluggable LLM backend), retrieval by `bge-large-en-v1.5`, SKOS relation typing. Committed offline run is deterministic; see its README. Includes the prototype results doc and the vocabulary-ablation results (log E1a).
- `eval/cross-community/` — the curated-vocabulary cross-community cell (§5.2; pre-registration + three review logs) with its build spec, results, and the second-cell search addendum. Pre-registered negative.
- `eval/e2e-cell/` — the end-to-end cell on the project's own coinage (§5.3; frozen spec + hashes, per-record corpus hashes, isolation manifests, fidelity judgments, failed primary + grounded baseline), plus the detection-demo spec. Pre-registered negative.
- `eval/measurements/` — the follow-up frozen measurement set (§5.4 + §4.2's provenance yield): P1 fidelity-gate calibration, P2 checklist-guided generation, P3 citation-provenance yield, P4 union-of-keys fusion.
- `eval/peer-reconciliation*/` — the continuation evaluation (§5.5), design and full execution record: specs v0.2–v0.9, adversarial review rounds, per-version verdicts, the sealed held-out test (`-test3`), key-authoring protocol (`-harness`), precision/recall operating points (`-fresh`, incl. `pr-curve.svg`); design docs, reviews, and the program summary in `eval/peer-reconciliation-docs/`.

## Receipts (the §2 record and the checking layer)

- `receipts/idiolect-trap-case-study.md` — the case study: event reconstruction, graded term ledger, test-case assessment.
- `receipts/novelty-position.md` — per-claim novelty ledger + auditable search record.
- `receipts/novelty-protocol.md` — the checking protocol (the entry's appendix: "how this entry was checked").
- `receipts/citation-audit-2026-07-17.md`, `receipts/citation-dossier-entry.md`, `receipts/citation-dossier-casestudy.md` — the citation-verification chain.
- `receipts/blind-passes/` — the blind naming/machinery/assembly/self-application passes with frozen briefs, hashes, contamination greps, and raw draws (`pass-a-raw/`, `machinery-raw/`), plus the targeted (Pass-B) prior-art searches.
- `receipts/naming-experiment/` — the definition-mediated naming experiment (§2's pilot): frozen inputs, sealed predictions, raw outputs (`def-naming-raw/`).
- `receipts/capability-ladder/` — the recall backtest + model ladder (§1's measured leg) and the socialization probes (the "not shown" result), with raw draws.

Some published artifacts carry in-place redaction notes (`[redacted…]` placeholders, and a `redaction_note` key in `eval/e2e-cell/runs/detection.json`) where personal content from the private workspace was removed; hashes in frozen manifests are unchanged and remain verifiable.
