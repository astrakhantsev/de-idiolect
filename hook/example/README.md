# Committed example — term-check run on the entry's own coinages (2026-07-20)

Self-application demo: `term-check.sh` run on two terms this entry coined, with the entry's own [GLOSSARY.md](../../GLOSSARY.md) as the pre-existing answer key (its rows were written at submission time, before this tool existed). Everything the check call saw, and everything it answered, is committed here: frozen excerpts, prompts with hashes, per-draw isolation manifests (`.term-check/manifests/`), raw outputs (`.term-check/prompts/*.out`), the instrumentation log (`.term-check/log.jsonl`), and the assembled flags (`term-flags.md`).

## Protocol

From the repo root:

```
export TERM_CHECK_STATE=hook/example/.term-check
bash hook/term-check.sh -o hook/example/term-flags.md "misroute"  ENTRY.md
bash hook/term-check.sh -o hook/example/term-flags.md "era-gated" ENTRY.md
```

Term selection was answer-aware and criterion-driven, and the criterion is committed: the two coinages whose ENTRY.md usage paragraphs contain **none** of their glossary row's owner vocabulary ([contamination-check.txt](contamination-check.txt) — a hit would make recovery meaningless). The check also lists which *other* established names sit inside the misroute excerpts (owners of different terms, from the §2 table), so a reader can separate in-boundary material from weights-recovered candidates.

## Results against the answer key

| Term | Glossary's expected owner ("field's nearest") | sonnet draw | opus draw |
|---|---|---|---|
| `misroute` | vocabulary-mismatch retrieval failure (IR); early IR's "false drop" | **Neighborhood only**: entity linking, record-linkage false match, call-routing's literal "misrouting". The IR canon did not surface. | **Hit**: "the vocabulary problem" with the canonical citation (Furnas, Landauer, Gomez & Dumais, CACM 1987 — the glossary's owner for the parent failure), plus false match / false positive in Cranfield-style IR. "False drop" itself was not named. |
| `era-gated` | temporal split / time-based holdout; leakage control (ML evaluation) | **Hit**: temporal holdout (ML evaluation) + contamination control, plus look-ahead bias / point-in-time data (finance). | **Hit**: temporal data leakage / temporal split with the canonical reference (Kaufman, Rosset, Perlich & Stitelman, KDD 2011), plus bitemporal "as-of" semantics (databases) and contemporaneous-source criticism (historiography) — a cross-community neighbor the glossary does not have. |

Side payload, unprompted: both opus draws returned usable *critiques* of the coinages — misroute conflates retrieval-step, attribution-step, and generation-step errors and never fixes destination granularity; era-gated's cutoff is per-item and event-anchored, which none of the standard terms quite names ("era" also wrongly suggests discrete epochs). This is the flag doing coin-time work beyond naming: sharpening what the term should mean before it ossifies.

## How to read this

- 3 of 4 draws recovered the expected owner or its canonical family; the miss (sonnet on misroute) returned a plausible adjacent neighborhood — exactly the pattern the hook's README warns about: convergence across same-family draws is weak evidence, divergence is informative, and every candidate stays **UNVERIFIED** until a primary is opened.
- The `era-gated` case ran on a single 96-word paragraph — the thin-input stress case; the prompt's "say what is missing" clause produced explicit underdetermination notes instead of confident guesses in both draws.
- This is a 2-term, author-selected, answer-aware demonstration — a worked example of the protocol and its receipts, not a recall estimate. The entry's §5 measurements (and their negatives) remain the evidentiary record; nothing here upgrades them.
