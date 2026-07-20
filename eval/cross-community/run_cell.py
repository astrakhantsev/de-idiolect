#!/usr/bin/env python3
"""Steps 2-3 - query generation + cross-community retrieval metrics.

The measurement (§1 of the build spec): for each direction, build the query battery from ONE
side's docs only (blind to the other side) and measure how well each query form reaches the
OTHER side's docs. Neutrality (the candidate) is supported only if the jargon-free key reaches
the far community better than BOTH the raw term and a jargon description built from the same side.

Two phases:
  # phase 1: generate + FREEZE the query battery (live claude -p; non-deterministic)
  python run_cell.py --generate --k 3 --models sonnet,opus
  # phase 2: embed + score (deterministic, offline, seeded bootstrap)
  python run_cell.py

Query forms per direction A->B (symmetric for B->A), generated from clean docs_A only:
  raw_term_A     : the term itself          (floor: A's word is absent from B's docs)
  jargon_A       : docs_A, jargon allowed, term A forbidden   (THE CONTROL)
  neutral_A      : docs_A, jargon-free,   term A forbidden     (THE CANDIDATE)
  raw_term_B     : held out                 (ceiling: B's own word on B's docs)
  naive_question : lay question             (floor)

Metrics (query built from A, retrieved against C), reported in TWO conditions:
  inclusive : full corpus, target = all docs_B
  clean     : cross-term-containing docs removed from corpus AND target
              (removes the leak where term A appears in a docs_B target and lets raw_term_A
               reach it by surface match -> fake lift)
Per query: rank_of_first_target_doc, recall@5, recall@10, count_target_in_top_k, plus reach
into the query's OWN side as a sanity floor. Bootstrap CIs (seeded) on the arm contrasts.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path

import numpy as np

from llm_backend_xc import claude, JARGON_PROMPT, NEUTRAL_PROMPT

HERE = Path(__file__).parent
CORPUS = HERE / "corpus.json"
QUERIES = HERE / "queries.json"
RESULTS = HERE / "results.json"
EMB_MODEL = "BAAI/bge-large-en-v1.5"
BGE_Q = "Represent this sentence for searching relevant passages: "
BOOT_SEED = 0          # fixed -> reproducible CIs (never time-seeded)
BOOT_N = 5000
CTX_MAX_DOCS = 6       # generation context: sample up to this many clean docs (symmetric)
CTX_PER_DOC = 350      # ... capped at this many chars EACH, so one long doc can't monopolise
TARGET_SENTENCES = 4   # nominal length target for the two generated arms (char length reported)


def _term_root(term: str) -> str:
    """Distinctive morphological root of a term, for leak detection that catches inflections
    (so 'photoplethysmography' also catches 'photoplethysmographic'). Exact-substring was the
    Codex-flagged bug that let a jargon draw recover the far term unnoticed."""
    t = re.sub(r"[^a-z0-9]", "", term.lower())
    for suf in ("ical", "ies", "ic", "es", "s", "y"):
        if t.endswith(suf) and len(t) - len(suf) >= 7:
            return t[: len(t) - len(suf)]
    return t


def _leaks(text: str, term: str) -> bool:
    """True if the term (any inflection of its root) appears in text."""
    return _term_root(term) in re.sub(r"[^a-z0-9]", "", text.lower())


def _chance_baseline(n_docs: int, n_targets: int, ks=(5, 10)) -> dict:
    """Analytical random-ranking expectations for the SAME corpus/target sizes, so an observed
    metric can be read against chance (Codex finding 1: recall@10 >= 0.5 is ~chance when half
    the corpus is targets). Under a uniform random permutation of n_docs with n_targets targets:
      E[recall@k]         = min(k, n_docs) / n_docs
      E[first-target rank]= (n_docs + 1) / (n_targets + 1)
    """
    out = {"n_docs": n_docs, "n_targets": n_targets,
           "exp_first_target_rank": round((n_docs + 1) / (n_targets + 1), 3) if n_targets else None}
    for k in ks:
        out[f"exp_recall_at_{k}"] = round(min(k, n_docs) / n_docs, 3) if n_docs else None
    return out


def _load_corpus():
    c = json.loads(CORPUS.read_text())
    docs = c["documents"]
    return c, docs


def _side(docs, community):
    return [d for d in docs if d["community"] == community]


def _clean_context(docs_side, char_budget):
    """Sample the docs that do NOT contain the other side's term (blind-to-other), taking a
    CAPPED slice from EACH of up to CTX_MAX_DOCS docs. Per-doc capping is deliberate (Codex
    finding 3): filling one char budget front-to-back let a single long abstract monopolise the
    whole B-side context, so B->A queries were effectively generated from ONE document. Returns
    (context, n_clean_available, n_docs_actually_used)."""
    clean = [d for d in docs_side if not d["contains_other_term"]]
    use = (clean or docs_side)[:CTX_MAX_DOCS]  # fall back if everything co-mentions
    parts = [d["text"][:CTX_PER_DOC] for d in use]
    return " ".join(parts), len(clean), len(use)


def generate(k: int, models: list[str], term_a: str, term_b: str, seed_concept: str):
    _, docs = _load_corpus()
    dirs = {
        "A_to_B": {"src": "A", "term": term_a, "far_term": term_b},
        "B_to_A": {"src": "B", "term": term_b, "far_term": term_a},
    }
    out = {"k": k, "models": models, "embedding_model": EMB_MODEL,
           "seed_concept": seed_concept, "term_a": term_a, "term_b": term_b,
           "target_sentences": TARGET_SENTENCES, "directions": {}}

    # one naive lay question about the general area (floor), shared by both directions
    naive_prompt = (f"A non-expert wants to look up the general topic related to '{seed_concept}'. "
                    "Write the one short, plain-language question they would type into a search box. "
                    "Output ONLY the question.")
    naive_q = claude(naive_prompt, model=models[0]) or f"what is {seed_concept}"

    for dname, d in dirs.items():
        src_docs = _side(docs, d["src"])
        context, n_clean, n_used = _clean_context(src_docs, None)
        rec = {"src_community": d["src"], "term": d["term"], "far_term": d["far_term"],
               "gen_context_clean_docs": n_clean, "gen_context_docs_used": n_used,
               "naive_question": naive_q, "jargon": [], "neutral": []}
        for arm, prompt in (("jargon", JARGON_PROMPT), ("neutral", NEUTRAL_PROMPT)):
            for model in models:
                for i in range(k):
                    p = prompt.format(term=d["term"], context=context, n_sent=TARGET_SENTENCES)
                    text = claude(p, model=model, timeout=180)
                    if not text:
                        raise SystemExit(f"claude -p returned nothing: dir={dname} arm={arm} "
                                         f"model={model} i={i}. Re-run (transient/quota).")
                    # stem-based leak detection (catches inflections like 'photoplethysmographic')
                    leak_own = _leaks(text, d["term"])
                    leak_far = _leaks(text, d["far_term"])
                    rec[arm].append({
                        "model": model, "sample": i, "text": text,
                        "leaks_own_term": leak_own, "leaks_far_term": leak_far,
                        "n_chars": len(text),
                    })
                    flag = (" **LEAKS OWN**" if leak_own else "") + (" **LEAKS FAR**" if leak_far else "")
                    print(f"  [{dname}] {arm:8s} {model:6s} s{i}: {len(text):4d} chars{flag}")
        out["directions"][dname] = rec
    QUERIES.write_text(json.dumps(out, indent=2))
    print(f"\n[frozen] {QUERIES}")
    return out


# --------------------------------------------------------------------- scoring

def _embed(model, texts, is_query):
    pre = [BGE_Q + t for t in texts] if is_query else texts
    return np.asarray(model.encode(pre, normalize_embeddings=True, show_progress_bar=False))


def _metrics_for_query(qvec, doc_emb, doc_ids, target_ids, own_ids):
    """rank of first target doc, recall@5/@10, count in top-k, + rank of first own-side doc."""
    sims = doc_emb @ qvec
    order = np.argsort(-sims)
    ranked = [doc_ids[j] for j in order]
    pos = {d: r for r, d in enumerate(ranked, start=1)}
    tgt_ranks = sorted(pos[i] for i in target_ids if i in pos)
    own_ranks = sorted(pos[i] for i in own_ids if i in pos)
    def recall_at(kk):
        top = set(ranked[:kk])
        return sum(1 for i in target_ids if i in top) / len(target_ids) if target_ids else 0.0
    return {
        "rank_first_target": tgt_ranks[0] if tgt_ranks else None,
        "recall_at_5": round(recall_at(5), 3),
        "recall_at_10": round(recall_at(10), 3),
        "count_target_top10": sum(1 for i in target_ids if i in set(ranked[:10])),
        "rank_first_own": own_ranks[0] if own_ranks else None,
    }


def _boot_ci(a_vals, b_vals, rng, n=BOOT_N):
    """Bootstrap CI for mean(a) - mean(b) over independent draws. None-safe (drops Nones)."""
    a = [v for v in a_vals if v is not None]
    b = [v for v in b_vals if v is not None]
    if not a or not b:
        return None
    a, b = np.array(a, float), np.array(b, float)
    diffs = np.array([a[rng.integers(0, len(a), len(a))].mean()
                      - b[rng.integers(0, len(b), len(b))].mean() for _ in range(n)])
    ci5, ci95 = round(float(np.percentile(diffs, 5)), 3), round(float(np.percentile(diffs, 95)), 3)
    # excludes_0 on the ROUNDED bounds (Codex finding 5: raw float noise flagged a -0.0/-0.0
    # contrast as excluding 0). A CI that rounds to touch 0 does not exclude it.
    return {"delta_mean": round(float(a.mean() - b.mean()), 3), "ci5": ci5, "ci95": ci95,
            "excludes_0": bool(ci5 > 0 or ci95 < 0),
            "note": "descriptive resampling-stability of THESE k draws pooled over 2 fixed models; "
                    "NOT population/cross-pair/cross-model uncertainty"}


def measure():
    corpus, docs = _load_corpus()
    q = json.loads(QUERIES.read_text())
    doc_ids = [d["id"] for d in docs]
    comm = {d["id"]: d["community"] for d in docs}
    contains_other = {d["id"]: d["contains_other_term"] for d in docs}

    from sentence_transformers import SentenceTransformer
    print(f"[load] {EMB_MODEL}")
    model = SentenceTransformer(EMB_MODEL)
    doc_emb = _embed(model, [d["text"] for d in docs], is_query=False)
    rng = np.random.default_rng(BOOT_SEED)

    results = {"embedding_model": EMB_MODEL, "term_a": q["term_a"], "term_b": q["term_b"],
               "seed_concept": q["seed_concept"], "conditions": ["inclusive", "clean"],
               "directions": {}}

    for dname, rec in q["directions"].items():
        src = rec["src_community"]
        far = "B" if src == "A" else "A"
        own_ids_all = [d for d in doc_ids if comm[d] == src]
        far_ids_all = [d for d in doc_ids if comm[d] == far]
        # clean: drop cross-term docs from corpus AND target
        clean_mask = [not contains_other[d] for d in doc_ids]
        clean_doc_ids = [d for d, keep in zip(doc_ids, clean_mask) if keep]
        clean_idx = [i for i, keep in enumerate(clean_mask) if keep]
        clean_emb = doc_emb[clean_idx]
        far_ids_clean = [d for d in far_ids_all if not contains_other[d]]
        own_ids_clean = [d for d in own_ids_all if not contains_other[d]]

        def score_arm(texts):
            per_cond = {"inclusive": [], "clean": []}
            if not texts:
                return per_cond
            qemb = _embed(model, texts, is_query=True)
            for qv in qemb:
                per_cond["inclusive"].append(
                    _metrics_for_query(qv, doc_emb, doc_ids, far_ids_all, own_ids_all))
                per_cond["clean"].append(
                    _metrics_for_query(qv, clean_emb, clean_doc_ids, far_ids_clean, own_ids_clean))
            return per_cond

        # A draw that leaks the forbidden own term (both arms) or the far term (neutral must be
        # blind to it) violates the design and is NOT a valid query. Drop such draws and report
        # how many, rather than scoring an invalid definition. (Deterministic; no regeneration,
        # so no selection bias — every leaking draw goes, whatever its metric.)
        def clean_draws(arm_name):
            kept, dropped = [], 0
            for s in rec[arm_name]:
                if s.get("leaks_own_term") or s.get("leaks_far_term"):
                    dropped += 1
                else:
                    kept.append(s["text"])
            return kept, dropped

        jargon_texts, jargon_dropped = clean_draws("jargon")
        neutral_texts, neutral_dropped = clean_draws("neutral")
        arms = {
            "raw_term": score_arm([rec["term"]]),
            "naive_question": score_arm([rec["naive_question"]]),
            "raw_term_far_CEILING": score_arm([rec["far_term"]]),
            "jargon": score_arm(jargon_texts),
            "neutral": score_arm(neutral_texts),
        }

        def agg(arm, cond, field):
            vals = [m[field] for m in arms[arm][cond]]
            vals = [v for v in vals if v is not None]
            return round(statistics.mean(vals), 3) if vals else None

        dir_out = {"far_target_docs_inclusive": len(far_ids_all),
                   "far_target_docs_clean": len(far_ids_clean),
                   "n_jargon_draws": len(jargon_texts), "jargon_draws_dropped_leak": jargon_dropped,
                   "n_neutral_draws": len(neutral_texts), "neutral_draws_dropped_leak": neutral_dropped,
                   "chance_baseline": {
                       "inclusive": _chance_baseline(len(doc_ids), len(far_ids_all)),
                       "clean": _chance_baseline(len(clean_doc_ids), len(far_ids_clean))},
                   "arms": {}, "contrasts": {}}
        for arm in arms:
            dir_out["arms"][arm] = {
                cond: {f: agg(arm, cond, f) for f in
                       ("rank_first_target", "recall_at_5", "recall_at_10",
                        "count_target_top10", "rank_first_own")}
                for cond in ("inclusive", "clean")}

        # contrasts: neutral vs {raw_term, jargon} on rank_first_target and recall_at_10
        for cond in ("inclusive", "clean"):
            for base in ("raw_term", "jargon"):
                for field in ("rank_first_target", "recall_at_10"):
                    nv = [m[field] for m in arms["neutral"][cond]]
                    bv = [m[field] for m in arms[base][cond]]
                    dir_out["contrasts"][f"neutral_minus_{base}.{field}.{cond}"] = _boot_ci(nv, bv, rng)
        results["directions"][dname] = dir_out

    RESULTS.write_text(json.dumps(results, indent=2))
    _report(results)
    return results


def _report(results):
    print("\n==== CROSS-COMMUNITY CELL - retrieval report ====")
    print(f"pair: A={results['term_a']!r}  B={results['term_b']!r}\n")
    for dname, d in results["directions"].items():
        print(f"--- {dname}  (far target docs: {d['far_target_docs_inclusive']} inclusive / "
              f"{d['far_target_docs_clean']} clean) ---")
        cb = d["chance_baseline"]["clean"]
        print(f"  CHANCE (clean, random ranking): first-rank≈{cb['exp_first_target_rank']}  "
              f"recall@5≈{cb['exp_recall_at_5']}  recall@10≈{cb['exp_recall_at_10']}  "
              f"[gen ctx docs used: jargon/neutral built from src side]")
        hdr = f"  {'arm':22s} {'cond':9s} {'rank1st':>8s} {'rec@5':>6s} {'rec@10':>7s} {'#top10':>7s} {'ownRk':>6s}"
        print(hdr)
        for arm, cc in d["arms"].items():
            for cond in ("inclusive", "clean"):
                m = cc[cond]
                print(f"  {arm:22s} {cond:9s} {str(m['rank_first_target']):>8s} "
                      f"{str(m['recall_at_5']):>6s} {str(m['recall_at_10']):>7s} "
                      f"{str(m['count_target_top10']):>7s} {str(m['rank_first_own']):>6s}")
        print("  contrasts (neutral - base; rank: negative=neutral better; recall: positive=better):")
        for key, ci in d["contrasts"].items():
            if ci:
                star = "  *excl0*" if ci["excludes_0"] else ""
                print(f"    {key:48s} Δ={ci['delta_mean']:+.3f} [{ci['ci5']:+.3f},{ci['ci95']:+.3f}]{star}")
        print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generate", action="store_true")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--models", default="sonnet,opus")
    args = ap.parse_args()
    if args.generate:
        c, _ = _load_corpus()
        p = c["pair"]
        generate(args.k, args.models.split(","), p["term_a"], p["term_b"], p["seed_concept"])
    measure()


if __name__ == "__main__":
    main()
