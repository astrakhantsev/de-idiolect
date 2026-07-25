# Golden fixtures — the independent oracle for the v0.10 baseline byte-level behavior

These fixtures are the machine-checkable **oracle** the v0.10 pre-registration (`2026-07-23-v010-generation-hardening-PREREG-DRAFT.md`, §3.6) freezes. `python3 conformance_runner.py` (run from the workspace dir) executes every `fixtures/*.json` against the frozen implementation (`serializers.py`, `assemble.py`, `parser_adjudicator.py`, `baseline_{a,b}._ground`) and is part of both attestation points (§4.2 steps 6 and 8).

**Independence.** Every expectation here was hand-derived from the spec prose and the literal template files (`prompts/baseline-{a,a-reask,b,b-reask}.md`) by a second agent, **without calling the implementation's `assemble`/`serializers`/`parse`/`_ground`**. The generator (`scratchpad/oracle_gen.py`, not committed) reimplements the §3.6(d) serialization rules and the §3.6(b) substitution semantics independently. The conformance runner then cross-checks the implementation against these oracles; **every divergence is a finding**, pinned as a fixture, not papered over by copying code output.

Every fixture is labeled `"oracle": "independent"`. The 9 files that were originally `"regression-seed"` (implementation-derived bytes) were re-derived by hand; all 9 matched byte-for-byte (no finding there), and are now relabeled `independent`.

## Current state: 97 fixtures, 97 pass, 0 FAILs (runner exit 0)

Per-kind (live): parse 57 · ground 15 · serialize_a_excerpts 5 · serialize_b_corpus 5 · serialize_baseline_a_docs 4 · assemble_baseline_a 3 · assemble_baseline_b 5 · pairs_manifest 3 = **97**.

> **Update (2026-07-25, core agent):** BUG-1 (single-document grounding) and BUG-2 (single-pass substitution) are FIXED; the 3 originally-pinned fixtures now pass as ordinary assertions (`expected_failure_pending_fix` removed; `bug_ref` annotated `[RESOLVED]`). Added since: 2 mixed-wrapper parse fixtures (round-5 quote-strip refinement — only genuinely matched ASCII `"…"` / curly `“…”` pairs are stripped) and 3 `pairs_manifest` fixtures (the §3.6 answer-blind pairs.json schema: opaque id `sha256(term_a || NUL || term_b)[:16]`, key-independent shuffle). **The "three expected-failures" inventory table + BUG-1/BUG-2 sections below are HISTORICAL** — the fixture agent's original findings, retained as the provenance record; all are resolved and the live total is 97/97.

The three originally-failing fixtures each carried `"expected_failure_pending_fix": true` and a `bug_ref`. Per §3.6(f) a spec whose conformance runner does not pass cannot freeze — so these **forced the two implementation fixes before freeze**. (Resolved; see the update above.)

### Inventory by kind

| kind | count | expected_failures |
|---|---|---|
| `parse` | 55 | 0 |
| `ground` | 15 | 2 (BUG-1) |
| `serialize_a_excerpts` | 5 | 0 |
| `serialize_b_corpus` | 5 | 0 |
| `serialize_baseline_a_docs` | 4 | 0 |
| `assemble_baseline_a` | 3 | 0 |
| `assemble_baseline_b` | 5 | 1 (BUG-2) |
| **total** | **92** | **3** |

## Findings (implementation bugs — REPORT, do not fix in fixtures)

### BUG-1 (HIGH) — boundary-spanning grounding accepts cross-document fabrications

**Fixtures:** `ground_boundary_spanning_false.json`, `ground_boundary_spanning_singleword_false.json` (control: `ground_distinct_docs_true.json`).

`baseline_{a,b}._ground` checks each field against `serializers.concat_docs_text(docs)` = the document bodies joined by `"\n\n"`, then `smoke.norm` collapses every whitespace run (incl. that `"\n\n"`) to a single space. So a quote that ends in one document and continues in the next validates as a contiguous substring of the concatenation, even though it appears in **no single document**.

Repro:

```python
import baseline_b
baseline_b._ground({"matched_term":"alpha","evidence":"beta gamma"},
                   [("b/01","alpha beta"),("b/02","gamma delta")])   # -> True; MUST be False
```

Spec basis for "must fail": §3.4/§3.5 grounding exists to reject fabricated evidence; §9-F5 quote validation is defined against "the … text the judge saw" (a single document in the tool arm) and "admits no word-level alteration … so fabricated or edited evidence still fails." A span synthesized by gluing two documents is exactly such a fabrication. §3.4 flags "(boundary-spanning cases per §3.6)" as a distinct case precisely because it is not an ordinary substring hit. **Correct fix:** ground each field against some *single* document (per-document substring), not the concatenation. Note `ground_distinct_docs_true` shows `matched_term` and `evidence` living in *different* documents is fine — each field is individually within one doc; only a *single span crossing a boundary* must fail.

Counter-reading for round-5: §3.4's literal words "a contiguous substring of the concatenated retrieved documents" can be read as licensing the concatenation check. If round-5 adopts that reading, resolve by amending the spec to state boundary-spanning is permitted and flipping these two fixtures to `expect_grounded: true` (delete the `expected_failure` marker). Either way the decision is now forced and explicit; the seed `ground_B_boundary_spanning_true.json` (which silently pinned the code's `true`) was removed.

### BUG-2 (LOW) — Baseline-B assembly re-substitutes placeholder tokens that appear in data

**Fixture:** `assemble_baseline_b_placeholder_injection.json` (control: `assemble_baseline_a_placeholder_in_doc.json`, which passes).

`assemble.assemble_baseline_b` chains `template.replace("{TERM_A}", …).replace("{A_EXCERPTS}", …).replace("{B_CORPUS}", …)`. Because `{B_CORPUS}` is replaced **after** the excerpts are inserted, an excerpt containing the literal token `{B_CORPUS}` gets re-substituted with the entire corpus (and `{A_EXCERPTS}` in `term_a` would be, likewise). §3.6(b) intent is verbatim insertion of serialized inputs.

Repro:

```python
import assemble
out = assemble.assemble_baseline_b("coin inj",
        ["contains {B_CORPUS} literally","ex one","ex two","ex three"],
        [("b/01","doc one body"),("b/02","doc two body")])
assert "{B_CORPUS}" in out   # FAILS: the token was replaced with the corpus
```

Baseline-A is **not** affected (`assemble_baseline_a_placeholder_in_doc` passes): its document text is inserted in the *last* `.replace`, so nothing re-scans it. **Severity LOW:** the trigger tokens (`{B_CORPUS}`, `{A_EXCERPTS}`, `{TERM_A}`) will never appear inside a real coinage term or corpus excerpt, so run-time risk is ~nil. **Correct fix:** single-pass substitution (replace all placeholders in one scan) so inserted data is never re-scanned. **Round-5 may waive** by deleting this fixture if the token-collision risk is judged impossible; it is pinned so the choice is explicit rather than silent.

## §3.6(c) coverage map

- whitespace/case variants → `parse_case_and_whitespace`, `parse_tab_after_colon_negative`, `parse_relation_uppercase_positive`, `parse_interior_whitespace_preserved_positive`, `parse_value_with_colon_positive`.
- duplicate fields → `parse_duplicate_field_malformed`, `parse_duplicate_identical_values_malformed`.
- extra prose → `parse_extra_prose_ignored`, `parse_code_fence_ignored`, `parse_prose_with_colon_ignored_negative`.
- invalid enum → `parse_invalid_match_enum`, `parse_invalid_relation_enum`, `parse_bad_match_enum_word`, `parse_arm_{a_rejects_B,b_rejects_corpus_broader}_enum`, `parse_arm_b_rejects_A_enum`.
- malformed second (re-ask) reply → `parse_malformed_reask_reply`, `parse_reask_still_malformed_prose`, `parse_reask_still_malformed_crossfield`; recovery → `parse_reask_recovers_positive`.
- truth-table rows → negatives (`parse_negative_{A,B}`); `match=no` with relation/evidence/matched_term present (`parse_no_with_*_malformed`); `match=yes` missing identifier/evidence/relation=n-a (`parse_yes_*_malformed`); each of the four positive relations per arm (`parse_positive_{A_exact,A_term_broader,A_corpus_broader,A_partial_overlap,B_exact,B_B_broader,B_partial_overlap}`).
- field-order / empty / partial → `parse_field_order_reversed_{negative,positive}`, `parse_empty_reply_malformed`, `parse_only_match_field_malformed`, `parse_missing_field_malformed`.
- wrapper-quote judgment call (deviation #2) — BOTH stripped and NOT-stripped → `parse_wrapper_quotes_{curly_stripped,single_not_stripped,unbalanced_leading_not_stripped,unbalanced_trailing_not_stripped,nested_inner_kept,empty_after_strip_malformed}`, `parse_quoted_none_{stripped_negative,yes_malformed}`, `parse_none_uppercase_negative`, seed `parse_wrapper_quotes_stripped`.
- `a_excerpts` at 4/5/6 → `serialize_a_excerpts_{4,5,6}`; strip + interior-newline edges → `serialize_a_excerpts_{strip,interior_newline}`.
- `b_corpus` first-doc labeling + terminal newline + rstrip → `serialize_b_corpus_{2,1_single_doc_labeled,rstrip,contains_separator,whitespace_only_first}` (no-terminal-newline is also pinned end-to-end by the assemble fixtures showing the template's single trailing `\n`).
- retrieved top-3 block → `serialize_baseline_a_docs_{3,rstrip,contains_separator,whitespace_only_middle}`.
- document-boundary-spanning grounding → BUG-1 fixtures + `ground_distinct_docs_true` control.
- folding-only matches (§9-F5) → `ground_fold_{curly_quotes,dash,whitespace_collapse}_true`; word-level alteration must fail → `ground_word_{alteration,inserted}_false`; header labels excluded → `ground_header_label_not_grounded_false`.
- end-to-end assembled first-ask AND re-ask, BOTH arms → `assemble_baseline_{a_first,a_reask,b_first,b_reask}`; substitution semantics → `assemble_baseline_a_placeholder_in_doc` (safe) + BUG-2 fixture; `k=4/6` end-to-end → `assemble_baseline_b_first_{4,6}excerpts`.

## Not covered by these fixtures (and why)

- **Counterpart-identity adapter, two-direction combination table, coverage/precision/decision table (§3.4/§3.5/§5).** These are key-bearing and live only in `scorer_v010.py` (the SPEND). They are out of scope for the key-blind §3.6 golden fixtures; they are exercised by the offline scorer unit tests against `toy-key/`.
- **§3.6(e) new-isolated-single-turn invocation.** A runtime property of the isolation wrapper, not a byte-level oracle — not expressible as a fixture.
- **`serialize_baseline_a_docs` doc-count validation.** The serializer does not enforce a count (unlike `serialize_a_excerpts`, which requires 4–6); the only production input is exactly the top-3, so only 3-doc cases are pinned.
