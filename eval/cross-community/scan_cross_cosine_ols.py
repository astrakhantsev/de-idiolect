#!/usr/bin/env python3
"""UMLS-proxy cross-vocabulary cross-cosine scan via OLS4 (open, no key).

True UMLS needs a UTS API key (see scan_cross_cosine_umls.py). As an open stand-in for the
same question — *do cross-SOURCE-vocabulary synonym pairs (same concept, names from different
communities) land in the LOW-cosine, embedder-hard regime the tool needs?* — this uses EBI's
Ontology Lookup Service (OLS4), which aggregates synonyms for a concept across many vocabularies
(SNOMED, NCIT, MONDO, ORDO, HP, MeSH, ...). That cross-ontology synonym set is a good proxy for
UMLS cross-SAB atoms and is richer in genuinely different-community names (eponym vs descriptive
vs mechanism) than MeSH Entry Terms alone.

For each seed concept: gather the concept's labels+synonyms across OLS ontologies, form
lexically-dissimilar name pairs (same Guard-4a filter as the MeSH scan), and compute bge
cross-cosine. Stores cross_cosine_ols_proxy.json sorted ascending. LOW cosine (< 0.65) = the
regime the tool could help; those are the candidates a memorization screen should then vet.
"""
from __future__ import annotations

import itertools
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import numpy as np
from sentence_transformers import SentenceTransformer

from select_pairs import lexical_overlap, _norm_tokens  # reuse Guard 4a

HERE = Path(__file__).parent
EMB_MODEL = "BAAI/bge-large-en-v1.5"
UA = "minelit-flf/0.1 (mailto:terms@astrakhantsev.com)"
OLS = "https://www.ebi.ac.uk/ols4/api/search"
LOW = 0.65
MAX_OVERLAP = 0.34

# Broad, multi-area seed concepts (diseases/phenotypes/processes with plausible cross-community
# naming). Wide, not tuned to a known answer; the filters decide.
SEEDS = [
    "takotsubo cardiomyopathy", "granulomatosis with polyangiitis", "pseudoxanthoma elasticum",
    "amyotrophic lateral sclerosis", "complex regional pain syndrome", "hidradenitis suppurativa",
    "pompe disease", "fabry disease", "wilson disease", "behcet disease", "kawasaki disease",
    "ehlers danlos syndrome", "marfan syndrome", "sarcoidosis", "amyloidosis", "vitiligo",
    "narcolepsy", "fibromyalgia", "endometriosis", "psoriatic arthritis", "sjogren syndrome",
    "myasthenia gravis", "guillain barre syndrome", "multiple sclerosis", "lupus nephritis",
    "hemochromatosis", "cystic fibrosis", "phenylketonuria", "gaucher disease", "tay sachs disease",
    "insulin resistance", "oxidative stress", "epithelial mesenchymal transition", "apoptosis",
    "long qt syndrome", "atrial fibrillation", "restless legs syndrome", "trigeminal neuralgia",
]


def _clean_name(n: str) -> str | None:
    """Reject OLS junk in the synonym field: cross-reference URIs and pure database codes
    (VAMAS1, LQT10, NCI_C85181). Keep real names, incl. short all-alpha abbreviations (GPA, TTS)."""
    n = (n or "").strip()
    if not n or n.lower().startswith("http") or "://" in n:
        return None
    if len(n) < 3 or len(n) > 60:
        return None
    if " " not in n and any(c.isdigit() for c in n):  # single-token code with a digit
        return None
    return n


def ols_synonyms(concept: str, rows: int = 10) -> list[str]:
    q = urllib.parse.urlencode({"q": concept, "rows": rows,
                                "fieldList": "label,ontology_name,obo_id,synonym"})
    try:
        body = urllib.request.urlopen(
            urllib.request.Request(f"{OLS}?{q}", headers={"User-Agent": UA}), timeout=30).read()
    except Exception:  # noqa: BLE001 - one bad concept shouldn't kill the sweep
        return []
    docs = json.loads(body)["response"]["docs"]
    raw: list[str] = []
    for d in docs:
        if d.get("label"):
            raw.append(d["label"])
        for s in (d.get("synonym") or []):
            raw.append(s)
    names = [n for n in (_clean_name(x) for x in raw) if n]
    # dedup case-insensitively, keep first surface form
    seen, out = set(), []
    for n in names:
        k = n.lower().strip()
        if k and k not in seen:
            seen.add(k)
            out.append(n.strip())
    return out


def dissimilar_pairs(names: list[str]) -> list[tuple[str, str]]:
    pairs = []
    for a, b in itertools.combinations(names, 2):
        # drop trivial variants (plurals/inversions/substrings) and near-duplicates
        if lexical_overlap(a, b) >= MAX_OVERLAP:
            continue
        if _norm_tokens(a) <= _norm_tokens(b) or _norm_tokens(b) <= _norm_tokens(a):
            continue
        pairs.append((a, b))
    return pairs


MAX_SYN = 12  # cap synonyms per concept to avoid combinatorial blow-up


def main() -> None:
    model = SentenceTransformer(EMB_MODEL)
    # 1) gather names + pairs per concept (network only)
    concept_pairs = []
    all_names = set()
    for concept in SEEDS:
        names = ols_synonyms(concept)[:MAX_SYN]
        if len(names) < 2:
            continue
        pr = dissimilar_pairs(names)
        for a, b in pr:
            all_names.add(a)
            all_names.add(b)
            concept_pairs.append((concept, a, b))
    # 2) embed every unique name ONCE (batch), then look up cosines (fast)
    uniq_names = sorted(all_names)
    vecs = model.encode(uniq_names, normalize_embeddings=True, show_progress_bar=False,
                        batch_size=64)
    vec = {n: v for n, v in zip(uniq_names, vecs)}
    rows = []
    for concept, a, b in concept_pairs:
        rows.append({"seed_concept": concept, "term_a": a, "term_b": b,
                     "cross_cosine": round(float(vec[a] @ vec[b]), 4),
                     "lexical_overlap": round(lexical_overlap(a, b), 3)})
    # dedup identical name pairs across seeds
    seen, uniq = set(), []
    for r in sorted(rows, key=lambda r: r["cross_cosine"]):
        key = frozenset((r["term_a"].lower(), r["term_b"].lower()))
        if key in seen:
            continue
        seen.add(key)
        uniq.append(r)

    out = {"source": "OLS4 (open proxy for UMLS cross-source-vocabulary)", "embedding_model": EMB_MODEL,
           "n_seeds": len(SEEDS), "n_pairs": len(uniq), "low_threshold": LOW,
           "reference_cosines": {"unrelated": 0.509, "cell1_photoreflex_ppg": 0.750,
                                 "racemic_epi_racepinephrine": 0.859},
           "note": "cross_cosine only; memorization screen NOT yet run — low-cosine pairs are the "
                   "candidates to screen next. True UMLS (cross-SAB) needs a UTS key.",
           "pairs": uniq}
    (HERE / "cross_cosine_ols_proxy.json").write_text(json.dumps(out, indent=2))

    print(f"==== OLS4 cross-vocabulary cross-cosine (n={len(uniq)} pairs, {len(SEEDS)} seeds) ====")
    low = [r for r in uniq if r["cross_cosine"] < LOW]
    print(f"lowest 25 (LOW = embedder-hard = the regime the tool needs):")
    for r in uniq[:25]:
        print(f"  {r['cross_cosine']:.3f}  {r['term_a'][:34]:34s} <-> {r['term_b'][:34]}")
    print(f"\nlow-cosine (<{LOW}): {len(low)} of {len(uniq)}  ({round(100*len(low)/len(uniq)) if uniq else 0}%)")
    print(f"[done] -> cross_cosine_ols_proxy.json")


if __name__ == "__main__":
    main()
