# P3 extraction-recall audit (seeded, spec P3; seed 20260719 → 2 files per dir)

Auditor: session agent, full personal re-read of each selected file, counting qualifying owner-candidate occurrences per the frozen definition and diffing against the extracted rows for that file.

| file | extracted | clear misses | borderline misses | audited recall |
|---|--:|--:|--:|--:|
| def-naming/out-PA-default.md | 35 | 3 (ISO 704; Star & Griesemer 1989; Newcombe et al. 1959) | 0 | 35/38 = 0.92 |
| def-naming/out-PA-opus.md | 30 | 3 (Hoare 1969; Swanson 1986 Library Quarterly as a second distinct work; Aberer et al. 2004 "Emergent Semantics Principles and Issues") | 3 (ASD-STE100 standard; Daille 2017 sources-list-only; LBD survey arXiv:1203.3611 sources-list-only) | 30/33 = 0.91 clear (30/36 = 0.83 incl. borderline) |
| recall-backtest/out-c2-R-sonnet.md | 6 | 0 | 0 | 6/6 = 1.00 |
| recall-backtest/out-covid-R-opus.md | 0 (API-error file) | 0 | 0 | trivially complete |
| **combined** | **71** | **6** | **3** | **≈0.89–0.92** |

**Reading.** Extraction recall on audited files is ~90%. The misses skew toward secondary mentions — standards cited as codifiers (ISO 704, ASD-STE100), second venues of an already-extracted author-year, sources-list entries without prose anchors, and inline parenthetical roots (Hoare 1969; Newcombe 1959) — not headline owner proposals. Direction of bias for the survival endpoint: missed items are plausibly LESS canonical than extracted ones, so the measured survival rate is, if anything, biased slightly upward by extraction misses. Disclosed in the results doc.

Consistency note: the extractors' exclusion calls on borderline items (named systems without authors, e.g. LLM4OM/LogMap-LLM; bare person names, e.g. Galison; concept names without works, e.g. Minimal English) matched the frozen definition in every audited instance.
