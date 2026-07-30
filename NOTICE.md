# NOTICE — third-party material

[`LICENSE`](LICENSE) (MIT) covers the code, the entry, and the original documentation and receipts. Third-party material keeps its own terms. This file is the short index; each area's own manifest is authoritative and more detailed.

## What is deliberately NOT committed

**Full third-party paper texts.** The collider demonstration runs over four arXiv papers (the two CERN LHC-safety documents and two critiques), and none of their full texts are in this repository — a copyright boundary enforced in [`.gitignore`](.gitignore) (`demo-collider/corpus/_work/`). Committed instead: the provenance manifest, a `fetch.sh` that reproduces the local working corpus, the section→side map, and the tools' own paragraph-level excerpt receipts.

Per [`demo-collider/corpus/manifest.md`](demo-collider/corpus/manifest.md): *"none of the four arXiv abstract pages surfaced an explicit license line through the extractor … the arXiv default non-exclusive distribution license is assumed, and we do not redistribute the full texts — only paragraph-level excerpts for analysis and metadata."* Stable identity is the arXiv ID + version; the recorded `sha256` is a snapshot of the extracted text, not a canonical hash, because extraction is tool-dependent.

## Third-party material that IS committed

| Where | What | Terms |
|---|---|---|
| `prototype/corpus.json` | a demonstration corpus whose documents are **short paraphrases** of real sources (title + one representative snippet), not verbatim text, each with its source recorded | paraphrase + citation; see the file's own `_note` |
| `demo-collider/*/` excerpt receipts | paragraph-level excerpts from the four arXiv papers, retained so the scored runs are checkable | quotation for analysis; see the manifest above |
| `eval/` run receipts | rendered prompts and transcripts that quote the corpora above | as above |

Nothing in this repository vendors a licensed dataset, and no upstream code is copied in — dependencies are pip-installed (see [`requirements.txt`](requirements.txt)).

## Models

`BAAI/bge-large-en-v1.5` is downloaded from Hugging Face at run time and is not redistributed here. Model calls go through locally-authenticated `claude` / `codex` CLIs; **there are no API keys in this repository.**

## Redaction

Machine-local absolute paths were redacted from this export on 2026-07-29. 33 files deliberately retain a path prefix because each is bound by a hash that something else verifies — editing those bytes would break the attestation chain the receipts exist to provide. The per-file accounting, the exposure assessment, and the reusable scanner invocation are in [`REDACTION-NOTES.md`](REDACTION-NOTES.md).
