#!/usr/bin/env python3
"""Recall-extender prototype — a runnable pipeline for the FLF EpiStack entry.

Implements the Ingestion + Structure layers of the proposed workflow on a small
eggs-case corpus:

  Step 1  DETECTION  : surface community-local terms by TF-IDF keyness across
                       community sub-corpora (deterministic, offline).
  Step 2  DEFINE     : generate a community-neutral constrained definition of a
                       detected term (LLM via llm_backend; frozen fixtures when the
                       batch backend is quota-blocked).
  Step 3  MATCH      : embed each definition with a real local model
                       (bge-large-en-v1.5) and retrieve cross-community documents.
                       The load-bearing MEASUREMENT: rank the owning sub-field's
                       documents under three query forms — the naive question, the
                       raw term, and the constrained definition — to show the
                       definition routes to the owner that the naive question misses.
  Step 3b TYPE       : label the concept<->top-match relation with a SKOS mapping
                       relation (LLM via llm_backend; fixtures fallback).

Retrieval (step 3) is the deterministic, non-fixture heart of the demo: it needs no
LLM and no network. Only the generative steps (2, 3b) use the LLM interface.

Usage:
  python recall_extender.py --backend fixtures      # offline, reproducible (default)
  python recall_extender.py --backend claude        # live LLM steps (needs quota)
"""
from __future__ import annotations
import os, json, argparse
from pathlib import Path

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
# NOTE: we do NOT force HF offline mode — a clean checkout without the cached model
# must be able to download bge-large-en-v1.5 on first run. Set HF_HUB_OFFLINE=1 yourself
# to run fully offline once the model is cached.

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

HERE = Path(__file__).parent
BGE_QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "
EMB_MODEL = "BAAI/bge-large-en-v1.5"


def load(corpus_path=None, concepts_path=None):
    """corpus_path/concepts_path default to the shipped eggs files, so calling load() with no
    arguments (the historical signature) reproduces the original behavior byte-for-byte.

    Validates the corpus (required fields present, ids unique) so a malformed custom --corpus
    fails loudly here rather than silently misattributing results later (e.g. a duplicate id
    would make doc_comm/doc_text overwrite while the embedding matrix keeps both rows, scoring
    the wrong document under the shared id)."""
    corpus_path = Path(corpus_path) if corpus_path else HERE / "corpus.json"
    concepts_path = Path(concepts_path) if concepts_path else HERE / "concepts.json"
    corpus = json.loads(corpus_path.read_text())["documents"]
    concepts = json.loads(concepts_path.read_text())["concepts"]

    seen_ids = set()
    for i, d in enumerate(corpus):
        missing = [k for k in ("id", "community", "text") if not d.get(k)]
        if missing:
            raise ValueError(
                f"{corpus_path}: document at index {i} is missing required field(s) {missing} "
                f"(every document needs non-empty 'id', 'community', 'text'; got keys {list(d.keys())})"
            )
        if d["id"] in seen_ids:
            raise ValueError(
                f"{corpus_path}: duplicate document id {d['id']!r} -- ids must be unique within a "
                f"corpus (a duplicate would silently misattribute scored results)."
            )
        seen_ids.add(d["id"])

    return corpus, concepts


def step1_detection(corpus):
    """TF-IDF keyness across community sub-corpora: which terms are community-local."""
    comms = {}
    for d in corpus:
        comms.setdefault(d["community"], []).append(d["text"])
    names = list(comms)
    docs = [" ".join(comms[c]) for c in names]
    vec = TfidfVectorizer(ngram_range=(1, 3), stop_words="english", sublinear_tf=True)
    X = vec.fit_transform(docs).toarray()
    vocab = np.array(vec.get_feature_names_out())
    out = {}
    for i, c in enumerate(names):
        top = vocab[np.argsort(-X[i])[:8]]
        out[c] = list(top)
    return out


def embed(model, texts, is_query=False):
    prompts = [BGE_QUERY_INSTRUCTION + t for t in texts] if is_query else texts
    v = model.encode(prompts, normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(v)


def ranks_of(owner_ids, ranked_ids):
    pos = {doc_id: r for r, doc_id in enumerate(ranked_ids, start=1)}
    rs = sorted(pos[i] for i in owner_ids)
    return rs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["fixtures", "claude"], default="fixtures")
    ap.add_argument("--model", default="sonnet", help="claude -p model for live backend")
    ap.add_argument("--out", default=str(HERE / "results.json"))
    ap.add_argument("--corpus", default=str(HERE / "corpus.json"),
                     help="path to a documents JSON (schema: prototype/templates/corpus-template.json). "
                          "Defaults to the shipped eggs corpus.")
    ap.add_argument("--concepts", default=str(HERE / "concepts.json"),
                     help="path to a concepts JSON (schema: prototype/templates/concepts-template.json). "
                          "Defaults to the shipped eggs concepts.")
    ap.add_argument("--define-only", action="store_true",
                     help="Run definitions + retrieval ranking only, with NO owner-rank scoring, "
                          "even if the concepts file happens to include 'owning_community'. Use this "
                          "when you have no answer key and just want to see what a definition retrieves.")
    args = ap.parse_args()

    from llm_backend import Backend
    from sentence_transformers import SentenceTransformer

    corpus, concepts = load(args.corpus, args.concepts)

    # A run counts as "custom" (own data, not the shipped eggs demo) if either input file was
    # overridden, or --define-only was requested. This gate exists so the shipped default
    # invocation's stdout AND results.json are untouched by anything below, while any other run
    # gets extra, clearly-labeled honesty banners/fields (see the prints and results["note"]
    # further down) plus a hard bypass of the eggs-only relation fixtures (see Backend below).
    is_custom_run = (
        Path(args.corpus).resolve() != (HERE / "corpus.json").resolve()
        or Path(args.concepts).resolve() != (HERE / "concepts.json").resolve()
        or args.define_only
    )
    backend = Backend(kind=args.backend, model=args.model, concepts_path=args.concepts,
                       custom_run=is_custom_run)

    if is_custom_run:
        print("\n[scope] Stage 1 (detect) is NOT wired into the concepts evaluated below -- owning "
              "communities are hand-supplied in the concepts file, not selected by detection. Stage 2 "
              "(define) and stage 3b (type) are the live-interface generative stages (--backend claude); "
              "only stage 3 (retrieval/matching) is the deterministic, offline, load-bearing measurement. "
              "See prototype/README.md.")
        print("[scope] CUSTOM DATA RUN: this corpus/concepts pair is not the shipped eggs demo. Any "
              "ranking below is a DEMONSTRATION that the retrieval interface runs on this data, not an "
              "independently verified measurement -- there is no answer key beyond what the concepts "
              "file itself hand-supplies (or omits, in --define-only mode).")

    # Validate owning_community references up front (before the expensive model load below), so a
    # scored concept naming a community with no matching document fails loudly with a clear message
    # instead of running for a while and then IndexError-ing deep inside the ranking code.
    communities_present = sorted({d["community"] for d in corpus})
    for c in concepts:
        owner = c.get("owning_community")
        if owner and not args.define_only and owner not in communities_present:
            raise ValueError(
                f"concept {c['term']!r}: owning_community {owner!r} does not match any document's "
                f"community in the corpus (communities present: {communities_present}). Fix the "
                f"concept's owning_community, add matching documents to the corpus, or omit "
                f"owning_community / pass --define-only to run this concept unscored."
            )

    # --- Step 1: detection ---
    keyness = step1_detection(corpus)

    # --- Step 3 setup: embed the corpus once (passages, no query instruction) ---
    print(f"[load] embedding model {EMB_MODEL} (offline)...")
    model = SentenceTransformer(EMB_MODEL)
    doc_ids = [d["id"] for d in corpus]
    doc_comm = {d["id"]: d["community"] for d in corpus}
    doc_text = {d["id"]: d["text"] for d in corpus}
    doc_emb = embed(model, [d["text"] for d in corpus], is_query=False)

    results = {"backend": args.backend, "embedding_model": EMB_MODEL,
               "keyness": keyness, "concepts": []}

    for c in concepts:
        term = c["term"]
        owner = c.get("owning_community")
        # Scored (owner-rank) path requires both an owning_community AND that the caller did not
        # force --define-only. Without an owner, there is nothing to score against -- that's the
        # "no answer key" case, and it's the same code from here on for either reason.
        scored = bool(owner) and not args.define_only
        owner_ids = [d for d in doc_ids if doc_comm[d] == owner] if owner else None

        # --- Step 2: constrained definition ---
        # Context for definition generation: the owner community's own documents when scored
        # (matches the original eggs behavior exactly); the whole corpus when there is no owner
        # to draw context from (define-only / no-answer-key path).
        context_ids = owner_ids if owner_ids else doc_ids
        context = " ".join(doc_text[i] for i in context_ids)
        definition, def_src = backend.define(term, context)

        # --- Step 3: retrieval under three query forms ---
        queries = {"naive_question": c["naive_question"], "raw_term": term,
                   "constrained_definition": definition}
        qtexts = list(queries.values())
        qemb = embed(model, qtexts, is_query=True)
        sims = qemb @ doc_emb.T  # (3, N), both normalized -> cosine
        per_query = {}
        for qi, qname in enumerate(queries):
            order = np.argsort(-sims[qi])
            ranked_ids = [doc_ids[j] for j in order]
            entry = {"top3": [(ranked_ids[k], round(float(sims[qi][order[k]]), 4))
                               for k in range(min(3, len(ranked_ids)))]}
            if scored:
                owner_ranks = ranks_of(owner_ids, ranked_ids)
                entry["owner_best_rank"] = owner_ranks[0]
                entry["owner_mean_rank"] = round(sum(owner_ranks) / len(owner_ranks), 2)
                entry["owner_ranks"] = owner_ranks
            per_query[qname] = entry

        # --- Step 3b: SKOS relation typing on the top retrieved doc per specialist community ---
        order = np.argsort(-sims[2])  # rank by the constrained-definition query
        top_doc_id = doc_ids[order[0]]
        label, reason, rel_src = backend.type_relation(definition, top_doc_id, doc_text[top_doc_id], term)

        concept_result = {
            "term": term, "owning_community": owner,
            "definition": definition, "definition_source": def_src,
            "retrieval": per_query,
        }
        if scored:
            concept_result["routing_gain_naive_to_definition"] = (
                per_query["naive_question"]["owner_best_rank"]
                - per_query["constrained_definition"]["owner_best_rank"]
            )
        concept_result["top_match"] = {"doc_id": top_doc_id, "skos_relation": label,
                                        "reason": reason, "source": rel_src}
        results["concepts"].append(concept_result)

    if is_custom_run:
        # Appended after all the original keys so the default (eggs, non-custom) run's JSON is
        # completely untouched -- these fields never appear unless --corpus/--concepts/--define-only
        # was actually used.
        results["run_mode"] = "define_only" if args.define_only else "custom_data"
        results["corpus_source"] = str(Path(args.corpus).resolve())
        results["concepts_source"] = str(Path(args.concepts).resolve())
        results["note"] = (
            "DEMONSTRATION run on user-supplied data, not a measurement: no independently verified "
            "answer key beyond what the concepts file itself hand-supplies (or omits). Stage 1 "
            "(detect) is not wired into the concepts above; stage 2 (define) and stage 3b (type) are "
            "the live-interface generative stages; only stage 3 (retrieval/matching) is deterministic "
            "and offline. See prototype/README.md's 2026-07-23 section."
        )

    Path(args.out).write_text(json.dumps(results, indent=2))

    # --- printed report ---
    print("\n==== RECALL-EXTENDER PROTOTYPE — run report ====")
    print(f"backend={args.backend}  embedding={EMB_MODEL}\n")
    print("STEP 1  keyness (top community-local terms):")
    for comm, terms in keyness.items():
        print(f"  {comm:24s}: {', '.join(terms[:5])}")
    scored_concepts = [r for r in results["concepts"] if "routing_gain_naive_to_definition" in r]
    unscored_concepts = [r for r in results["concepts"] if "routing_gain_naive_to_definition" not in r]
    if scored_concepts:
        print("\nSTEP 3  definition-mediated routing (rank of owning sub-field's docs; lower=better):")
        print(f"  {'concept':32s} {'owner':22s} {'naive_q':>8s} {'raw_term':>9s} {'defn':>6s} {'gain':>5s}")
        for r in scored_concepts:
            nq = r["retrieval"]["naive_question"]["owner_best_rank"]
            rt = r["retrieval"]["raw_term"]["owner_best_rank"]
            df = r["retrieval"]["constrained_definition"]["owner_best_rank"]
            print(f"  {r['term']:32s} {r['owning_community']:22s} {nq:>8d} {rt:>9d} {df:>6d} {r['routing_gain_naive_to_definition']:>+5d}")
    if unscored_concepts:
        print("\nSTEP 3  retrieval, NO ANSWER KEY (top match per query form; not a scored measurement):")
        for r in unscored_concepts:
            print(f"  {r['term']}:")
            for qname, entry in r["retrieval"].items():
                top1 = entry["top3"][0] if entry["top3"] else ("(none)", 0.0)
                print(f"    {qname:24s} top1={top1[0]} (cos={top1[1]})")
    print("\nSTEP 3b  SKOS relation typing (concept -> top retrieved doc):")
    for r in results["concepts"]:
        tm = r["top_match"]
        print(f"  {r['term']:32s} -> {tm['doc_id']}  [{tm['skos_relation']}] ({tm['source']})")
    n = len(results["concepts"])
    live_defs = sum(1 for r in results["concepts"] if r["definition_source"] == "live")
    live_rels = sum(1 for r in results["concepts"] if r["top_match"]["source"] == "live")
    print(f"\nBACKEND EFFECTIVE (requested={args.backend}): definitions {live_defs}/{n} live, relations {live_rels}/{n} live")
    if args.backend == "claude" and (live_defs < n or live_rels < n):
        print("  ⚠ WARNING: --backend claude requested but some generative stages fell back to FIXTURES")
        print("    (claude -p returned no usable output). The retrieval measurement is unaffected; the")
        print("    generated-definition claim is not. See per-concept 'source' fields in the results JSON.")
    print(f"\n[done] full results -> {args.out}")


if __name__ == "__main__":
    main()
