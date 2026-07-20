#!/usr/bin/env python3
"""TRUE UMLS cross-source-vocabulary cross-cosine scan (needs a free UTS API key).

This is the real version of the OLS proxy: for each concept it pulls the CUI and its atoms from
DIFFERENT source vocabularies (SAB) — e.g. a SNOMED clinical term vs an MSH research term vs a
nursing/lab vocabulary — which is UMLS's precise notion of "same concept, different-community
names." It forms lexically-dissimilar cross-SAB pairs and computes bge cross-cosine, exactly
like the MeSH scan, so the numbers are directly comparable.

Get a key (free, ~2 min): sign in at https://uts.nlm.nih.gov/uts/ -> Profile -> API key. Then:
    UMLS_API_KEY=xxxx ../../.venv/bin/python scan_cross_cosine_umls.py
Without the key it exits with these instructions (it does NOT fabricate numbers).

Writes cross_cosine_umls.json. LOW cosine (< 0.65) = embedder-hard = the regime the tool needs;
those are the pairs a memorization screen should then vet for the sweet spot.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

HERE = Path(__file__).parent
EMB_MODEL = "BAAI/bge-large-en-v1.5"
UA = "minelit-flf/0.1 (mailto:terms@astrakhantsev.com)"
UTS = "https://uts-ws.nlm.nih.gov/rest"
LOW = 0.65
MAX_OVERLAP = 0.34

# Same broad seed list as the OLS proxy, for comparability.
try:
    from scan_cross_cosine_ols import SEEDS
except Exception:  # noqa: BLE001
    SEEDS = ["takotsubo cardiomyopathy", "pompe disease", "fabry disease", "wilson disease"]


def _get(url: str, params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    body = urllib.request.urlopen(
        urllib.request.Request(f"{url}?{q}", headers={"User-Agent": UA}), timeout=30).read()
    return json.loads(body)


def cui_for(concept: str, key: str) -> str | None:
    r = _get(f"{UTS}/search/current", {"string": concept, "apiKey": key, "pageSize": 1})
    res = r.get("result", {}).get("results", [])
    return res[0]["ui"] if res and res[0].get("ui") != "NONE" else None


def atoms_by_sab(cui: str, key: str) -> dict[str, list[str]]:
    """Preferred strings grouped by source vocabulary (SAB), English only."""
    out: dict[str, list[str]] = {}
    page = 1
    while page <= 3:  # cap pages
        try:
            r = _get(f"{UTS}/content/current/CUI/{cui}/atoms",
                     {"apiKey": key, "language": "ENG", "pageNumber": page, "pageSize": 100})
        except Exception:  # noqa: BLE001
            break
        results = r.get("result", [])
        if not results:
            break
        for a in results:
            sab = a.get("rootSource", "?")
            name = (a.get("name") or "").strip()
            if name:
                out.setdefault(sab, [])
                if name not in out[sab]:
                    out[sab].append(name)
        if len(results) < 100:
            break
        page += 1
    return out


def main() -> None:
    key = os.environ.get("UMLS_API_KEY")
    if not key:
        sys.exit(__doc__.split("\n\n")[2])  # the "Get a key" paragraph
    from sentence_transformers import SentenceTransformer
    from select_pairs import lexical_overlap, _norm_tokens

    model = SentenceTransformer(EMB_MODEL)
    rows = []
    for concept in SEEDS:
        cui = cui_for(concept, key)
        if not cui:
            continue
        by_sab = atoms_by_sab(cui, key)
        # one representative name per SAB (the first), then cross-SAB lexically-dissimilar pairs
        reps = [(sab, names[0]) for sab, names in by_sab.items() if names]
        for (sab_a, a), (sab_b, b) in itertools.combinations(reps, 2):
            if lexical_overlap(a, b) >= MAX_OVERLAP:
                continue
            if _norm_tokens(a) <= _norm_tokens(b) or _norm_tokens(b) <= _norm_tokens(a):
                continue
            va, vb = model.encode([a, b], normalize_embeddings=True)
            rows.append({"seed_concept": concept, "cui": cui, "sab_a": sab_a, "sab_b": sab_b,
                         "term_a": a, "term_b": b, "cross_cosine": round(float(va @ vb), 4),
                         "lexical_overlap": round(lexical_overlap(a, b), 3)})
    rows.sort(key=lambda r: r["cross_cosine"])
    out = {"source": "UMLS Metathesaurus (cross-SAB atoms)", "embedding_model": EMB_MODEL,
           "n_seeds": len(SEEDS), "n_pairs": len(rows), "low_threshold": LOW, "pairs": rows}
    (HERE / "cross_cosine_umls.json").write_text(json.dumps(out, indent=2))
    low = [r for r in rows if r["cross_cosine"] < LOW]
    print(f"==== TRUE UMLS cross-SAB cross-cosine (n={len(rows)}) ====")
    for r in rows[:25]:
        print(f"  {r['cross_cosine']:.3f}  [{r['sab_a']}/{r['sab_b']}]  {r['term_a'][:28]} <-> {r['term_b'][:28]}")
    print(f"\nlow-cosine (<{LOW}): {len(low)} of {len(rows)}")
    print("[done] -> cross_cosine_umls.json")


if __name__ == "__main__":
    main()
