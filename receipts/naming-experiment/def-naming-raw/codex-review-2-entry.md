## Verdict
needs-attention

## Summary
The reported ranks—naive 5/4/8, definition 1/1/1, gains +4/+3/+7—and fixture disclosures match the code and `results.json`. The central problem is that §4a calls the prototype end-to-end and cross-community, while the code bypasses detection, starts from manually supplied specialist concepts and owners, and retrieves documents from those same owner communities.

## Findings

### [critical] The prototype does not execute the advertised end-to-end, cross-community route
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §4a and §6; `../src/minelit/flf-epistack/eval/recall-extender/recall_extender.py` — `load()`, detection, and concept loop; `10_projects/minelit/idiolect/2026-07-17-recall-extender-prototype-results.md` — “What is real vs fixture”
- **Problem**: The entry says the prototype implements the Ingestion+Structure path “end-to-end” and that detection is part of the measured path. In fact, detection is disconnected from the evaluated concepts, and retrieval routes an already-known specialist definition back to documents from its already-known owning community—not from one community to another.
- **Evidence**: `recall_extender.py` loads the three terms and their `owning_community` directly from `concepts.json`. `keyness = step1_detection(corpus)` is only recorded and printed; it never selects the concepts processed by `for c in concepts`. The definition context is then constructed from `owner_ids`, and success is explicitly the best-ranked document in that same owner community. The detection output does not surface the three target terms intact. Nevertheless, the entry says “implements the Ingestion+Structure path end-to-end” and “Detection and retrieval run for real.”
- **Impact**: A judge would reasonably infer that the prototype demonstrates detection → definition → cross-community matching. It actually demonstrates only that an answer-aware, manually supplied definition of a known specialist concept retrieves that specialist community’s seeded documents. It performs neither lay-question-to-concept discovery nor cross-community concept matching.
- **Fix**: Either relabel §4a everywhere as a conditional within-corpus owner-retrieval test, removing “end-to-end,” “cross-community,” and detection from the measured claim, or wire detected terms into definition generation and evaluate matches in a different community while excluding source-community documents.
- **Confidence**: 1.0

### [high] Ho et al. is falsely attributed to the experiment’s single clean cell
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §4b and §6; `10_projects/minelit/idiolect/2026-07-16-definition-mediated-naming-EXPERIMENT.md` — §§7.4–7.5
- **Problem**: The entry says the “single clean cell” produced both the Raiffa–Schlaifer result and the Ho, Hull & Srihari discovery. Ho came from C4, one of the three explicitly confounded cells.
- **Evidence**: The experiment identifies C2 as the sole clean cell and its result as Raiffa & Schlaifer 1961. It says C4 was confounded by construct drift and a mis-mapped answer key; §7.5 separately verifies that C4’s rewritten definition matched Ho’s set-combination mechanics. The entry instead says, “the single clean cell also produced … Ho, Hull & Srihari,” and §6 again associates the cross-domain and 31-year-old owners with “its single clean cell.”
- **Impact**: This upgrades an interesting but confounded candidate-discovery result into clean comparative evidence for the generator. That is stronger than the experiment permits.
- **Fix**: Keep C2/Raiffa–Schlaifer as the only clean-cell result. Present Ho separately as a primary-verified owner surfaced from confounded C4, explicitly noting that it cannot support the arm-level definition-versus-term comparison.
- **Confidence**: 1.0

### [high] The open novelty claims have not cleared the ledger’s own stop rule
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §5; `10_projects/minelit/idiolect/novelty-position.md` — “Search ledger,” assembly row, and programme-level note
- **Problem**: The entry carries the controlled-vocabulary strip and fused assembly as `open (candidate)`, but the novelty ledger remains `draft` because its verification stop rule has not been satisfied.
- **Evidence**: The ledger requires every load-bearing nearest neighbour for an open strip to be verified against primary text, then says, “Neither condition has been reached.” Its final note identifies the remaining gap as primary verification of the Microsoft patent family, NeoN, and Confluence Define documentation. The entry acknowledges these as unopened but still makes the open-candidate contribution central.
- **Impact**: Ceding priority is insufficient if a primary read could reveal that one of these neighbours covers more of the assembly than the run-level summary reports. This leaves the submission’s novelty-bearing claim exposed under the project’s own pre-registered standard.
- **Fix**: Open and claim-check the named primary neighbours before submission, then update the ledger and entry. If that cannot be completed, remove the assembly’s open-status contribution or state explicitly that the novelty gate remains unresolved.
- **Confidence**: 1.0

### [high] The published evidence package is not yet independently runnable or auditable
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — Appendix; `../src/minelit/flf-epistack/eval/recall-extender/README.md` — “Run it” and “Files”; `../src/minelit/flf-epistack/eval/recall-extender/recall_extender.py` — model initialization
- **Problem**: The package is runnable in the author’s prepared environment, but the documented public path lacks the prerequisites needed for a clean judge run. Evidence links are also still placeholders, and the corpus-provenance path is dead outside the author’s filesystem.
- **Evidence**: The README invokes `../../.venv/bin/python` without an installation or lockfile procedure. The code enables Hugging Face/Transformers offline mode before loading `BAAI/bge-large-en-v1.5`, so a clean machine without the cached model cannot obtain it. No model revision or dependency versions are pinned. The corpus source path `../../../../10_projects/...` does not resolve to the stated hub vault, while every Appendix receipt remains `‹URL›`.
- **Impact**: A judge following the supplied instructions may be unable to run the code, reproduce the table, or audit the paraphrased corpus sources. That directly undermines “small runnable prototype … with receipts.”
- **Fix**: Publish a self-contained evidence location; replace every placeholder; include pinned dependencies, model revision, initial model-download/cache instructions, and a tested clean-checkout command; and copy or correctly link the corpus source ledger into the public package.
- **Confidence**: 1.0

### [medium] The live backend silently falls back to fixtures while reporting `claude`
- **Where**: `../src/minelit/flf-epistack/eval/recall-extender/README.md` — live command; `../src/minelit/flf-epistack/eval/recall-extender/llm_backend.py` — `_claude()`, `define()`, and `type_relation()`; `../src/minelit/flf-epistack/eval/recall-extender/recall_extender.py` — report header
- **Problem**: The README describes `--backend claude` as regenerating the generative stages live, but any CLI error, missing executable, empty output, timeout, or invalid relation label silently triggers fixtures.
- **Evidence**: `_claude()` returns `None` on all such failures; `define()` and `type_relation()` then return fixture values without warning. The run still records and prints `backend=claude`, although per-record source fields may say `fixture`.
- **Impact**: A judge can request a live run, receive fixture output, and mistake it for live generation from the console report.
- **Fix**: Make `--backend claude` fail loudly unless live outputs succeed, or require an explicit `--allow-fixture-fallback` and print a prominent per-stage fallback banner. Record the effective backend, not merely the requested one.
- **Confidence**: 1.0

### [medium] The entry relies on an economic thesis whose required case matrix remains unbuilt
- **Where**: `10_projects/minelit/idiolect/2026-07-17-flf-recall-extender-criteria-first.md` — §2 claim 1; `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §§2 and 6
- **Problem**: The criteria-first specification says the universal+manual+build-once synthesis “requires the case matrix before the entry may rely on it.” The entry admits that matrix is unbuilt but makes this synthesis its “most developed” scalability argument.
- **Evidence**: The entry says “a full case matrix … is unbuilt” and later “a case matrix across projects is owed,” while still concluding that the reviewed cases died largely from marginal costs made cheap by generation.
- **Impact**: The submission’s answer to FLF’s scaling criterion rests on evidence that its own specification declared insufficient for public reliance.
- **Fix**: Build the case-by-case property/evidence matrix before submission, or reduce the section to a tentative research hypothesis and stop using it as the principal scaling argument.
- **Confidence**: 1.0

### [low] One novelty absence claim breaks the entry’s exact-language rule
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §5
- **Problem**: The introduction promises every absence claim will use “not found in the searches on record,” but §5 later says the blind pass “found no fused system.”
- **Evidence**: The latter is contextually bounded to one pass, but it does not use the submission’s promised formulation and reads more categorically than the ledger’s same-family, incomplete-coverage null.
- **Impact**: This is precisely the kind of wording a judge can quote back as stronger than the search record supports.
- **Fix**: Change it to “no fused system was found in the searches on record” and keep the same-family and coverage caveats adjacent.
- **Confidence**: 1.0

## Next Steps

- Rewrite §4a first so it describes exactly the conditional retrieval experiment the code performs.
- Correct the C2/C4 attribution in §4b and §6.
- Complete the ledger’s outstanding primary reads before retaining either `open (candidate)` claim.
- Publish and clean-test the evidence package, including fail-loud live execution and working provenance links.
- Either build the required graveyard case matrix or cut the economic thesis back to a tentative hypothesis.