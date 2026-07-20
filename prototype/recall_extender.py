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


def load():
    corpus = json.loads((HERE / "corpus.json").read_text())["documents"]
    concepts = json.loads((HERE / "concepts.json").read_text())["concepts"]
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
    args = ap.parse_args()

    from llm_backend import Backend
    from sentence_transformers import SentenceTransformer

    corpus, concepts = load()
    backend = Backend(kind=args.backend, model=args.model)

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
        owner = c["owning_community"]
        owner_ids = [d for d in doc_ids if doc_comm[d] == owner]

        # --- Step 2: constrained definition ---
        context = " ".join(doc_text[i] for i in owner_ids)
        definition, def_src = backend.define(term, context)

        # --- Step 3: retrieval under three query forms ---
        queries = {"naive_question": c["naive_question"], "raw_term": term,
                   "constrained_definition": definition}
        qtexts = list(queries.values())
        qemb = embed(model, qtexts, is_query=True)
        sims = qemb @ doc_emb.T  # (3, 15), both normalized -> cosine
        per_query = {}
        for qi, qname in enumerate(queries):
            order = np.argsort(-sims[qi])
            ranked_ids = [doc_ids[j] for j in order]
            owner_ranks = ranks_of(owner_ids, ranked_ids)
            per_query[qname] = {
                "top3": [(ranked_ids[k], round(float(sims[qi][order[k]]), 4)) for k in range(3)],
                "owner_best_rank": owner_ranks[0],
                "owner_mean_rank": round(sum(owner_ranks) / len(owner_ranks), 2),
                "owner_ranks": owner_ranks,
            }

        routing_gain = (per_query["naive_question"]["owner_best_rank"]
                        - per_query["constrained_definition"]["owner_best_rank"])

        # --- Step 3b: SKOS relation typing on the top retrieved doc per specialist community ---
        order = np.argsort(-sims[2])  # rank by the constrained-definition query
        top_doc_id = doc_ids[order[0]]
        label, reason, rel_src = backend.type_relation(definition, top_doc_id, doc_text[top_doc_id], term)

        results["concepts"].append({
            "term": term, "owning_community": owner,
            "definition": definition, "definition_source": def_src,
            "retrieval": per_query, "routing_gain_naive_to_definition": routing_gain,
            "top_match": {"doc_id": top_doc_id, "skos_relation": label,
                          "reason": reason, "source": rel_src},
        })

    Path(args.out).write_text(json.dumps(results, indent=2))

    # --- printed report ---
    print("\n==== RECALL-EXTENDER PROTOTYPE — run report ====")
    print(f"backend={args.backend}  embedding={EMB_MODEL}\n")
    print("STEP 1  keyness (top community-local terms):")
    for comm, terms in keyness.items():
        print(f"  {comm:24s}: {', '.join(terms[:5])}")
    print("\nSTEP 3  definition-mediated routing (rank of owning sub-field's docs; lower=better):")
    print(f"  {'concept':32s} {'owner':22s} {'naive_q':>8s} {'raw_term':>9s} {'defn':>6s} {'gain':>5s}")
    for r in results["concepts"]:
        nq = r["retrieval"]["naive_question"]["owner_best_rank"]
        rt = r["retrieval"]["raw_term"]["owner_best_rank"]
        df = r["retrieval"]["constrained_definition"]["owner_best_rank"]
        print(f"  {r['term']:32s} {r['owning_community']:22s} {nq:>8d} {rt:>9d} {df:>6d} {r['routing_gain_naive_to_definition']:>+5d}")
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
