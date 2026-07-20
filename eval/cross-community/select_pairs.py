#!/usr/bin/env python3
"""Step 0 - pair selection (guards 1, 4a, 0, 3).  The hard part.

Produce candidate A<->B synonym pairs: same concept (human-asserted by MeSH indexers,
Guard 1), two *lexically dissimilar* community names (Guard 4a), that the EMBEDDER does not
already bridge (Guard 0, the bge cross-cosine pre-filter), and where the naive term A does NOT
lead a frontier model to term B (Guard 3, the memorization/misroute screen).

Guard 0 (added 2026-07-18) is the lesson from the first cell: definition-mediated retrieval only
helps when raw-term retrieval FAILS, i.e. when the embedder does not already place the two names
next to each other. That is checkable in one cheap batch of embeddings BEFORE the expensive
`claude -p` screen — so by default the screen runs only on Guard-0 passers (embedder-hard pairs).

We seed a BROAD, multi-domain list of MeSH concepts and let the guards select. The seed is
deliberately wide and not tuned to any known-good answer; the filters, not the author, pick
the surviving pairs.

  python select_pairs.py                 # pull + Guard 4a + Guard 0, write candidate_pairs.json
  python select_pairs.py --screen        # + memorization screen (Guard 3) on Guard-0 passers
  python select_pairs.py --screen --screen-all      # screen every pair, not just Guard-0 passers
  python select_pairs.py --no-guard0                # skip the cross-cosine pre-filter

Output: candidate_pairs.json (one row per pair, with cross_cosine + guard0 + screen verdicts).
Nothing here touches retrieval or the corpus; this only nominates pairs for Step 1.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import mesh_client as mc
from llm_backend_xc import claude

HERE = Path(__file__).parent
OUT = HERE / "candidate_pairs.json"

EMB_MODEL = "BAAI/bge-large-en-v1.5"
# Guard 0: cross-cosine BELOW this = embedder does not bridge the two names = tool-relevant (PASS).
# Reference (bge-large): unrelated terms ~0.51; cell-1's embedder-bridged pair 0.75; near-identical
# synonyms > 0.85. Model-specific — recalibrate if the embedding model changes.
GUARD0_LOW = 0.65

# ---------------------------------------------------------------------------
# A broad seed of MeSH concepts spanning many sub-fields. Chosen to be wide, not
# to guarantee a winner: diseases with lay/clinical/eponym splits, molecules with
# common/systematic names, methods, and cross-discipline phenomena. The lexical +
# citation + memorization guards decide which (if any) survive.
SEED_CONCEPTS = [
    # disease eponym / descriptive / lay splits
    "myocardial infarction", "takotsubo cardiomyopathy", "granulomatosis with polyangiitis",
    "complex regional pain syndrome", "amyotrophic lateral sclerosis", "leprosy",
    "pompe disease", "celiac disease", "tetralogy of fallot", "kawasaki disease",
    "hidradenitis suppurativa", "pseudoxanthoma elasticum", "glycogen storage disease type II",
    "erythema migrans", "molluscum contagiosum", "tinnitus", "presbycusis",
    # molecules / biochemistry with common vs systematic names
    "ascorbic acid", "cholecalciferol", "acetaminophen", "epinephrine",
    "thiamine", "riboflavin", "niacin", "folic acid", "cobalamin",
    # methods / statistics / measurement (cross-discipline naming)
    "principal component analysis", "logistic models", "propensity score",
    "receiver operating characteristic", "kaplan-meier estimate", "bland-altman",
    "cluster analysis", "markov chains",
    # physiology / mechanism concepts with divergent field names
    "apoptosis", "autophagy", "hypoxia", "oxidative stress", "insulin resistance",
    "endoplasmic reticulum stress", "epithelial-mesenchymal transition",
    "long-term potentiation", "circadian rhythm", "gut microbiome",
    # imaging / signal
    "magnetic resonance imaging", "positron emission tomography",
    "electroencephalography", "photoplethysmography",
]

STOP = {"the", "of", "a", "an", "and", "or", "in", "on", "to", "for", "with",
        "by", "type", "disease", "syndrome", "disorder", "acute", "chronic",
        "wall", "cell", "cells"}


def _norm_tokens(term: str) -> set[str]:
    """Content-word stems of a term, for lexical-similarity comparison.

    Lowercase, strip punctuation, drop stopwords, crude singularize (trailing 's').
    Catches permutations/inversions/plurals ("Infarction, Inferior Myocardial" vs
    "Inferior Myocardial Infarction") as HIGH overlap, so Guard 4a can reject them.
    """
    words = re.split(r"[^a-z0-9]+", term.lower())
    out = set()
    for w in words:
        if not w or w in STOP or len(w) <= 2:
            continue
        if w.endswith("ies") and len(w) > 4:
            w = w[:-3] + "y"
        elif w.endswith("es") and len(w) > 4:
            w = w[:-2]
        elif w.endswith("s") and len(w) > 3:
            w = w[:-1]
        out.add(w)
    return out


def lexical_overlap(a: str, b: str) -> float:
    """Jaccard of content-word stem sets. 0 = fully disjoint words, 1 = same words."""
    ta, tb = _norm_tokens(a), _norm_tokens(b)
    if not ta or not tb:
        return 1.0
    return len(ta & tb) / len(ta | tb)


def candidate_pairs_for(concept: str, max_overlap: float = 0.34) -> list[dict]:
    """For one seed concept: fetch the MeSH descriptor + entry terms, and return
    (descriptor, entry_term) pairs whose lexical overlap is below `max_overlap`."""
    rec = mc.mesh_concept(concept)
    if not rec or not rec["descriptor"]:
        return []
    desc = rec["descriptor"]
    # Reject esearch false-matches: keep the concept only if the seed phrase actually appears
    # in the descriptor or in the entry term (else esearch returned a related enzyme/receptor,
    # e.g. acetaminophen -> "Arylsulfotransferase", cholecalciferol -> "Receptors, Calcitriol").
    seed_toks = _norm_tokens(concept)
    desc_toks = _norm_tokens(desc)
    pairs = []
    seen = set()
    for et in rec["entry_terms"]:
        et_toks = _norm_tokens(et)
        if not (seed_toks <= desc_toks or seed_toks <= et_toks):
            continue
        ov = lexical_overlap(desc, et)
        if ov >= max_overlap:
            continue
        # dedup lexically-equivalent entry terms among themselves
        key = frozenset(_norm_tokens(et))
        if key in seen or not key:
            continue
        seen.add(key)
        pairs.append({
            "seed_concept": concept,
            "mesh_uid": rec["uid"],
            "descriptor": desc,          # community-B "official" name (arbitrary; test is symmetric)
            "entry_term": et,            # community-A alternate name
            "lexical_overlap": round(ov, 3),
            "scope_note": (rec["scope_note"] or "")[:400],
        })
    # keep the most lexically-distant few per concept
    pairs.sort(key=lambda p: p["lexical_overlap"])
    return pairs[:3]


# ---------------------------------------------------------------------------
# Guard 3 - memorization / misroute screen. Give a blind model term A alone; if it
# names term B or B's community, the model's prior (not the tool) crosses the seam -> VOID.
SCREEN_PROMPT = """You are given a single technical term. Answer briefly and concretely.

TERM: "{term}"

1. What does this term mean / what does it name?
2. What field(s) or research communities study it?
3. What ELSE is this same thing called? List any synonyms or alternative names you know.

If you do not recognize the term, say so plainly. Do not speculate wildly."""


def screen_pair(pair: dict, model: str) -> dict:
    """Run the memorization probe on term A (the entry_term). PASS if the model does NOT
    surface term B (the descriptor) or its distinctive words."""
    term_a = pair["entry_term"]
    term_b = pair["descriptor"]
    resp = claude(SCREEN_PROMPT.format(term=term_a), model=model, timeout=120)
    verdict = {"screen_model": model, "screen_response": resp}
    if not resp:
        verdict["screen_verdict"] = "ERROR"
        return {**pair, **verdict}
    low = resp.lower()
    b_tokens = _norm_tokens(term_b)
    # leak if the model names term B (all its content stems appear) — that means it
    # already bridges A->B from its prior, so the tool would be redundant on this pair.
    leaked_b = bool(b_tokens) and all(t in low for t in b_tokens)
    # partial signal: any distinctive B stem present
    b_hits = sorted(t for t in b_tokens if t in low)
    verdict["b_full_leak"] = leaked_b
    verdict["b_stem_hits"] = b_hits
    verdict["screen_verdict"] = "VOID" if leaked_b else "SURVIVES"
    return {**pair, **verdict}


def guard0_cross_cosine(pairs: list[dict], threshold: float = GUARD0_LOW) -> list[dict]:
    """Guard 0 - bge cross-cosine between the two names, annotated in place.

    LOW cosine (< threshold) => the embedder does NOT already bridge the pair, so raw-term
    retrieval fails and definition-mediated retrieval has room => `guard0: "pass"`.
    HIGH cosine => the bare term already reaches the far side => the tool is likely redundant
    => `guard0: "fail"`. Cheap (one batched embedding of all unique names); run it BEFORE the
    expensive memorization screen so `claude -p` is spent only on embedder-hard candidates.
    """
    if not pairs:
        return pairs
    import os
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMB_MODEL)
    names = sorted({p["entry_term"] for p in pairs} | {p["descriptor"] for p in pairs})
    vecs = model.encode(names, normalize_embeddings=True, show_progress_bar=False, batch_size=64)
    vec = {n: v for n, v in zip(names, vecs)}
    for p in pairs:
        cos = float(vec[p["entry_term"]] @ vec[p["descriptor"]])
        p["cross_cosine"] = round(cos, 4)
        p["guard0"] = "pass" if cos < threshold else "fail"
    return pairs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--screen", action="store_true", help="run the memorization screen (Guard 3)")
    ap.add_argument("--screen-all", action="store_true", help="screen ALL pairs, not just Guard-0 passers")
    ap.add_argument("--no-guard0", action="store_true", help="skip the cross-cosine pre-filter")
    ap.add_argument("--guard0-threshold", type=float, default=GUARD0_LOW)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--max-overlap", type=float, default=0.34)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()

    all_pairs: list[dict] = []
    for concept in SEED_CONCEPTS:
        try:
            ps = candidate_pairs_for(concept, args.max_overlap)
        except Exception as e:  # noqa: BLE001 - one bad concept shouldn't kill the sweep
            print(f"  [skip] {concept}: {type(e).__name__}: {e}")
            continue
        for p in ps:
            print(f"  [pair] {p['seed_concept']:34s}  {p['entry_term']:32s} <-> {p['descriptor']:32s}  ov={p['lexical_overlap']}")
        all_pairs.extend(ps)

    print(f"\n{len(all_pairs)} lexically-dissimilar candidate pairs from {len(SEED_CONCEPTS)} seed concepts.")

    # --- Guard 0: cross-cosine pre-filter (embedder-hard = tool-relevant) ---
    if not args.no_guard0:
        print(f"\nGuard 0 - bge cross-cosine pre-filter (threshold {args.guard0_threshold})...")
        guard0_cross_cosine(all_pairs, args.guard0_threshold)
        npass = sum(1 for p in all_pairs if p["guard0"] == "pass")
        print(f"  {npass}/{len(all_pairs)} pairs PASS Guard 0 (cross-cosine < {args.guard0_threshold} "
              f"= embedder does not bridge = tool-relevant). Lowest-cosine:")
        for p in sorted(all_pairs, key=lambda r: r["cross_cosine"])[:10]:
            print(f"    {p['cross_cosine']:.3f} [{p['guard0']:4s}]  {p['entry_term'][:30]} <-> {p['descriptor'][:30]}")

    if args.screen:
        screen_everything = args.screen_all or args.no_guard0
        idxs = [i for i, p in enumerate(all_pairs)
                if screen_everything or p.get("guard0") == "pass"]
        scope = "all pairs" if screen_everything else f"{len(idxs)} Guard-0 passers"
        print(f"\nRunning memorization/misroute screen (Guard 3) on {scope}...")
        for n, i in enumerate(idxs, 1):
            all_pairs[i] = screen_pair(all_pairs[i], args.model)
            r = all_pairs[i]
            print(f"  [{n:2d}/{len(idxs)}] {r['entry_term'][:34]:34s} -> {r['screen_verdict']}"
                  f"  (cos {r.get('cross_cosine')}, B-stem hits: {r.get('b_stem_hits')})")
        for p in all_pairs:
            p.setdefault("screen_verdict", "not_screened_guard0_fail")
        n_surv = sum(1 for p in all_pairs if p.get("screen_verdict") == "SURVIVES")
        n_sweet = sum(1 for p in all_pairs
                      if p.get("screen_verdict") == "SURVIVES" and p.get("guard0") == "pass")
        print(f"\n{n_surv} pairs SURVIVE the screen; {n_sweet} are SWEET-SPOT (Guard-0 pass AND "
              f"screen SURVIVES). NB the whole-token screen over-counts survivors — READ responses.")

    Path(args.out).write_text(json.dumps({"max_overlap": args.max_overlap,
                                          "n_seed": len(SEED_CONCEPTS),
                                          "guard0_threshold": None if args.no_guard0 else args.guard0_threshold,
                                          "embedding_model": None if args.no_guard0 else EMB_MODEL,
                                          "pairs": all_pairs}, indent=2))
    print(f"[done] {args.out}")


if __name__ == "__main__":
    main()
