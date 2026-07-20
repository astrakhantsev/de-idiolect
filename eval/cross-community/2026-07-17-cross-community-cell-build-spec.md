---
title: "Build spec — one cross-community cell (isolating vocabulary-neutrality; half-synthetic UMLS/MeSH + citation-walk corpus)"
date: 2026-07-17
kind: build spec (post-deadline / funded eval; demonstration-grade single cell)
status: BUILT + RUN + THRICE Codex-reviewed 2026-07-17. Results → `2026-07-17-cross-community-cell-RESULTS.md`. The frozen **Verdict-3 RULE triggered** on Photoreflexometry↔Photoplethysmography — but the threshold sits at chance, so it is a rule-trigger, NOT a supported "reconciled/redundant" finding. Three Codex MAJOR REVISIONs showed the cell supports NO retrieval claim (leaked naive baseline, model-confounded arms, application-mismatched corpora, unestablished Guard 2, two unbuilt guards, threshold at chance, a wrong descriptor id since fixed). Deviations vs this 6-guard/5-verdict spec (per-guard/per-verdict table in the RESULTS ledger): built Guards 1/3(Sonnet-only)/4a/4b; Guard 2 reconciliation-CHECK only (INSUFFICIENT DATA; backward-citation corpus-expansion NOT built); **Guard 5 (temporal holdout) and Guard 6 (direct-ask baseline) NOT built** → verdict 5 unevaluable, verdicts 1/2 unevaluable (post-outcome + confounded); secondary term-recovery metric NOT built; n=1. Durable value = one scoped Step-0 observation (this Sonnet sweep: 4 automatic survivor flags → 1 after reading) + a partial harness + three reviews.
targets: "the neutrality-vs-specificity confound (Codex entry-review #2): §4a shows a SPECIFICITY effect and cannot isolate vocabulary NEUTRALITY, because within-owner retrieval is the one regime where neutrality is designed to lose. This cell is the setup where neutrality can win or lose on the merits."
depends_on: "2026-07-17-external-test-feasibility.md (UMLS/MeSH = the human-asserted, non-circular source), 2026-07-17-constrained-vs-free-ablation-RESULTS.md (the within-owner ablation this extends), recall-extender prototype (harness to reuse)"
one_line: "One A↔B synonym pair (same UMLS CUI / MeSH descriptor, two community names, lexically dissimilar, memorization-screened), a corpus of real docs for each side (PubMed word-search + 1-hop backward-citation walk + distractors), and one measurement: a query built from ONE side only, does the NEUTRAL definition reach the OTHER side's docs better than that side's raw term or jargon description can? Primary metric = cross-community recall of B-docs; controls isolate neutrality from specificity; six guards keep the measured traps out (incl. temporal-holdout pair selection + a direct-model-query baseline re-measured each model generation)."
---

# Build spec — one cross-community cell

## 0. Why this exists (what it isolates that nothing built so far does)

`§4a` of the entry shows a **specificity** effect — re-specifying a vague lay question into a precise concept description reaches the owning literature the question buries. It **cannot** isolate vocabulary **neutrality**, because it retrieves the concept's *own* owner community, and within-owner retrieval is precisely where neutral vocabulary is *designed to lose* (jargon lexically matches the owner's docs; the §4c ablation showed free-text's larger margin is bought with exactly that owner-jargon overlap). Neutrality's whole payoff — a source-jargon-free key reaching a *second* community that names the same concept differently — is only visible **cross-community**. This cell builds that setup, at the smallest scale that is still honest: **one A↔B pair**, real docs, a constructed community partition ("half-synthetic": the papers are real, only the grouping is authored), with the controls that separate neutrality from specificity and the guards that keep out the memorization/circularity/reconciliation traps we have already measured.

**Scope of a "cell":** n = 1 pair is a **demonstration**, not a benchmark. It can show the mechanism *exists* (or fails) on one genuine cross-community case; it cannot estimate an effect size. A claim needs many pairs — that is the full funded eval this cell is the unit of.

## 1. The measurement

Build a corpus `C = docs_A ∪ docs_B ∪ distractors`, where `docs_A` are real papers using term A (community A's name for the concept), `docs_B` real papers using term B (community B's name for the *same* concept), and distractors are off-topic papers. Then, for each **direction** (A→B and B→A), generate the query from **one side's docs only, blind to the other side**, and measure how well it reaches the *other* side's docs.

**Query battery (direction A→B; symmetric for B→A), all generated from `docs_A` only:**

| query | built from | tests | predicted reach into `docs_B` |
|---|---|---|--:|
| `raw_term_A` | — (the term itself) | "stuck in my own community" floor | poor — A's word ∉ B's docs |
| `jargon_A` | `docs_A`, jargon allowed, term A forbidden | does A's *content* alone cross? (the control) | ? |
| **`neutral_A`** | `docs_A`, jargon-free, term A forbidden | **the candidate — neutrality crosses the seam** | good, if the claim holds |
| `raw_term_B` | — (held out) | **ceiling** (B's own word on B's docs) | high by construction |
| `naive_question` | lay question about the general area | floor | poor |

k = 3 samples for the two generated queries (`jargon_A`, `neutral_A`); generators **sonnet + opus** (per [[feedback_test_model_opus_sonnet]]); freeze all outputs.

**Metrics (both are the user's; ordered by how memorization-exposed they are):**
- **Primary — cross-community recall (the user's "how many docs from the 2nd set are reached").** For a query built from A, retrieved against `C`: `recall@k` of `docs_B` (fraction of B's docs in the top k), `rank_of_first_B_doc`, and count of B-docs in the top k. Also report reach into `docs_A` as a sanity floor (every query should retrieve its own side well). This is a *retrieval* metric against a fixed frozen corpus — the least memorization-exposed.
- **Secondary — term recovery (the user's "can we find the other term").** From the top-retrieved B-doc(s), can a blind model read off term B? Do the **retrieval-grounded** version (name B from the surfaced doc), *not* open-generation naming from the definition alone — open naming is where memorization bites hardest (see Guard 3). Report separately; treat as elicitation (§4b's task), not the headline.

**The isolating comparison (the money result):** `raw_term_A` cannot reach `docs_B` (its word is absent there), but `neutral_A` does — that is the entry's thesis measured for the first time. The **decisive control is `jargon_A`**: if A's jargon description *also* reaches B, neutrality is **not** the lever (specificity/semantics suffices) — a publishable honest negative. Average over both directions and over k; report bootstrap CIs on `neutral − jargon` and `neutral − raw_term` for `rank_of_first_B_doc` and `recall@k`.

## 2. Pre-registered interpretation contract (freeze BEFORE running; [[feedback_recipes_die_on_transfer]])

Write this into the run's docstring/prereg file *before* any retrieval number is seen:
- **Neutrality SUPPORTED** iff `neutral_A` reaches `docs_B` at a better `rank_of_first_B_doc` than **both** `raw_term_A` and `jargon_A`, in **both** directions, with bootstrap CIs excluding 0.
- **Neutrality is NOT the lever (semantics suffices)** iff `jargon_A ≈ neutral_A` at reaching B (CI includes 0) while both beat `raw_term_A`. Honest negative — the definition helps, but the *vocabulary constraint* does not add cross-community reach.
- **Pair was reconciled / tool redundant** iff even `raw_term_A` reaches `docs_B` well — means Guard 4 failed (the communities already share vocabulary/citations); discard the cell, do not report it as a tool result. This is the COVID-VOID case in miniature.
- **Tool adds nothing over direct-ask** iff the no-tool direct-model-query (Guard 6) already reaches B as well as `neutral_A` retrieval does — the model already held the bridge; report as such and do **not** credit the tool, whatever the retrieval numbers. This gate rises with model capability and must be checked at the current tier every run.
- **Null / underpowered** iff nothing separates and `docs_B` is unreachable by any query including the `raw_term_B` ceiling — means the corpus construction failed (B's docs aren't retrievable at all); fix the corpus, not the interpretation.

## 3. Data pipeline

### Step 0 — pair selection (the hard part; screen several candidates to get one clean cell)
1. **Source (Guard 1 — human-asserted, never embedding-derived).** Pull candidate synonym pairs from **UMLS Metathesaurus** (same CUI, two atoms from *different* source vocabularies `SAB` — e.g. a SNOMED clinical term vs an MeSH research term) or **MeSH** (a descriptor and one of its lexically-distant *Entry Terms*). Both assert "same concept, different community names" by human indexers, independent of any embedding — this is what dodges the circularity trap that disqualified the open construct-similarity lists (feasibility doc §"circularity trap"). Larsen & Bong jangle pairs are the other clean source but are gated behind an email to Larsen — out of scope for a first cell.
2. **Lexical-dissimilarity filter (Guard 4a).** Drop pairs whose terms share content-word stems (normalized string overlap above a low threshold). This removes the trivial MeSH entry-terms that are spelling/abbreviation variants a naive search already bridges (feasibility doc's explicit caveat) — keep only the *opaque cross-community* subset.
3. **Memorization / misrouting screen (Guard 3; [[feedback_clean_testset_for_recall_tools]] #1–2).** Headless-probe the generator on **term A alone** ("what is this; what fields study it; what else is it called?") across sonnet + opus. **PASS only if it does NOT surface term B or B's community.** Bonus signal if term A actively *misroutes* the model to a wrong field (the "operating requirement → accounting" pattern) — that is the ideal opaque pair. Select by *naive-label opacity* (does the coined/local term misroute the model?), not by concept obscurity per se. **Prefer pairs whose concept/link post-dates the generator's training cutoff (Guard 5) — that *guarantees* non-memorization instead of arguing it, and stays clean as models improve.**
4. Output: **one** vetted pair. Expect to screen ~5–10 candidates per surviving cell.

### Step 1 — corpus construction
1. **Seed docs.** For term A, retrieve N ≈ 8–12 real docs (title + abstract) via **PubMed E-utilities** word-search on term A; same for term B. Enforce at the doc level: a `docs_A` paper must **not** contain term B (and vice versa) — else lexical leak (Guard 4b).
2. **Backward-citation walk (the user's move; serves corpus + Guard 2).** For each seed, add its **backward** citations (works it *references*, via OpenAlex `referenced_works` — open, no key), 1 hop only, as "first-pass lit-review" working docs. Backward (not forward) keeps you inside the community's own foundations and avoids later work that may already have bridged the seam. Filter shared *foundational* refs (a common stats/method ancestor cited by both sides) so deep roots don't create spurious A∩B overlap.
3. **Non-reconciliation check (Guard 2 — the validity gate).** Verify `docs_A` and `docs_B` citation neighborhoods are **disjoint**: no A→B (or B→A) citations, minimal shared references. Disjoint ⇒ genuinely *unreconciled* seam (the C2 case, tool-relevant). Overlapping ⇒ already reconciled (COVID-VOID) ⇒ discard the pair. *(This is why the backward-citation walk earns its place: it builds the corpus AND supplies the reconciliation signal in one pass.)*
4. **Distractors.** Add ~6–10 off-topic papers from unrelated fields (as the eggs corpus's `E` community does) so retrieval isn't trivially easy.
5. Freeze `C` with per-doc provenance (source URL / PMID / OpenAlex id) in a `corpus.json` mirroring the recall-extender format.

### Step 2 — query generation
Reuse the recall-extender `define()` interface + the ablation's constrained/free prompts, adding a `raw_term` and `naive_question` pass. Generate `jargon_A` and `neutral_A` from `docs_A` only (blind to B), k = 3, sonnet + opus; forbid term A in both; length-match the two arms (fixes the §4c length confound). Freeze to `queries.json`.

### Step 3 — retrieval + metrics
Embed `C` and the queries with `bge-large-en-v1.5` (same as the prototype), cosine rank, compute the §1 metrics with bootstrap CIs over k and directions. Deterministic + offline once frozen. Write `results.json` + a report.

### Step 4 — review + write-up
Codex doc-review the results ([[feedback_unreviewed_artifact_assume_wrong]] — budget it as a phase; the synthesis layer will overclaim). Fold. Only then decide whether the single cell is clean enough to reference.

## 4. The guards, in one place

0. **Cross-cosine pre-filter (embedder-hard), added 2026-07-18 — the lesson of cell 1.** Before spending anything on a corpus or the memorization screen, embed the two names and take the bge cross-cosine. **LOW** (< ~0.65 on bge-large; unrelated≈0.51, near-identical synonyms>0.85) = the embedder does *not* already bridge the pair, so raw-term retrieval fails and the tool has room (**PASS**). **HIGH** = the bare term already reaches the far side ⇒ the tool is likely redundant (**FAIL**) — this is exactly what sank cell 1 (Photoreflexometry↔Photoplethysmography, cos 0.75: opaque yet embedder-bridged). Cheapest guard; run it first so the `claude -p` screen is spent only on embedder-hard candidates. Built into `select_pairs.py` (annotates `cross_cosine`/`guard0`), gated in `build_corpus.py`. **Empirical (this session): Guard 0 and Guard 3 anti-correlate on curated vocabularies — a named synonym is either embedder-bridged or memorized; MeSH sweet-spot (pass+survive)=0/66, cross-vocabulary low-cosine eponyms all memorized on reading. See `2026-07-18-second-cell-search-ADDENDUM.md`.**
1. **Human-asserted pairs, never embedding-derived** (UMLS CUI / MeSH descriptor / Larsen & Bong) — or the whole test is circular.
2. **Non-reconciliation**, verified by citation disjointness — else the tool is redundant on that pair and the "reach" is trivial.
3. **Memorization / misrouting screen** on term A before use — else the model's prior, not the tool, is what crosses the seam.
4. **Lexical hygiene** — (a) terms lexically dissimilar; (b) docs on one side don't contain the other side's term; 1-hop backward citations, shared-foundational refs filtered.
5. **Temporal holdout — the memorization screen that *scales*.** Guard 3 (probe-the-model) degrades as models improve and must be re-run against the same-or-stronger model under test; it certifies non-memorization by *argument*. The version that does **not** degrade is selecting pairs whose concept/link post-dates the generator's **training cutoff** — then non-memorization is *guaranteed*, and there is always a fresh frontier, so post-cutoff literature is a renewable clean-test source across model generations. Prefer post-cutoff pairs; fall back to Guard 3's probe only for older ones. (This is also the durable form of the tool's *own* value story per the entry's §6: the tool concentrates on exactly the post-cutoff/unreconciled frontier that memorization cannot reach.)
6. **Direct-model-query baseline — re-measured every generation.** Add a **no-tool** arm: ask the generator directly ("is there prior work matching <neutral description>; what fields; what is it called?") and score whether it reaches B unaided, *without* retrieval. The tool's claim is **marginal over this baseline**, and the baseline rises with capability, so it must be measured at the *current* model tier on this run — never inherited from a past run. Report the tool's lift *over* direct-ask, not just absolute reach.

## 5. Tools / access

- **Pairs:** MeSH (fully open — descriptor + Entry Terms via NLM MeSH API / E-utilities) as the no-account path; UMLS Metathesaurus (richer cross-source-vocabulary CUIs) needs a free UTS account + API key.
- **Docs:** PubMed E-utilities (`esearch`/`efetch`, open; ≤3 req/s without a key). Title+abstract only (no full text needed).
- **Citations:** OpenAlex (`referenced_works`, open, no key) for the backward walk + reconciliation check; iCite/Semantic Scholar are fallbacks.
- **Generation:** `claude -p --model sonnet` + `--model opus` (per [[feedback_test_model_opus_sonnet]]; ~free within Max limits per [[feedback_max_cli_default]]).
- **Retrieval:** `bge-large-en-v1.5` (already cached in the prototype venv).

## 6. Cost, scope, honesty

- **One cell = demonstration.** Report it as "the mechanism does/does not appear on one genuine cross-community pair," never as an effect size. The claim-grade version is many pairs — the funded eval.
- **Effort (Claude-Code pace, [[feedback_time_estimates]]):** the *coding* is small — most of it reuses the recall-extender + ablation harness (retrieval, embedding, generation, metrics all exist). The **bottleneck is Step 0 pair-screening** (iterating candidates through the four guards), not code. Rough active-session estimate: half a day to a day, dominated by pair selection and the non-reconciliation check, plus one Codex review cycle.
- **Deadline:** this is **post-07-19 / funded work** (the feasibility doc already classified UMLS/MeSH as the real-but-post-deadline clean route). It is the concrete instantiation of the paid-work "how we'd measure it," not an entry item.

## 7. Code layout

New component `/mnt/f/src/minelit/flf-epistack/eval/cross-community/`, reusing from `../recall-extender/`:
- `select_pairs.py` — UMLS/MeSH pull + lexical-dissimilarity filter + memorization screen (Step 0, guards 1/3/4a).
- `build_corpus.py` — PubMed docs + OpenAlex backward-citation walk + reconciliation check + distractors (Step 1, guards 2/4b).
- `run_cell.py` — query generation (reuse `llm_backend`/ablation prompts) + bge retrieval + cross-community-recall metrics + CIs (Steps 2–3).
- `prereg.md` — the §2 interpretation contract, frozen before Step 3.
- Frozen artifacts: `corpus.json`, `queries.json`, `results.json`.

## 8. Cross-refs

- The confound this fixes: Codex entry-review #2 (in `entry/` review log) + the §4a→specificity reframe (queued).
- The within-owner ablation it extends: `2026-07-17-constrained-vs-free-ablation-RESULTS.md`.
- Source/access + trap analysis: `2026-07-17-external-test-feasibility.md`.
- Method memories: [[feedback_clean_testset_for_recall_tools]], [[feedback_recipes_die_on_transfer]], [[feedback_unreviewed_artifact_assume_wrong]], [[feedback_test_model_opus_sonnet]].
