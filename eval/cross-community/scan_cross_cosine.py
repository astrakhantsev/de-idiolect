#!/usr/bin/env python3
"""Guard-0 probe: bge cross-cosine between the two names of each candidate pair.

The binding constraint the first cell exposed: definition-mediated retrieval only helps for a
pair the EMBEDDER does not already bridge. That is cheaply checkable BEFORE building any corpus
— just embed the two bare terms and take the cosine. LOW cosine = embedder does not bridge =
the regime the tool needs. HIGH cosine = raw term already reaches the far side = tool redundant
(the verdict-3 outcome).

Reference points (measured 2026-07-18): unrelated terms ≈ 0.51 (malaria vs group cohesion);
Photoreflexometry↔Photoplethysmography (cell 1, embedder-bridged) = 0.750; racemic
epinephrine↔racepinephrine = 0.859. So on THIS model, "low" means roughly < 0.65 and
genuinely-unrelated is ~0.5.

Reads candidate_pairs.json (66 MeSH pairs, with memorization screen_verdict) and writes
cross_cosine_mesh.json sorted ascending, flagging the sweet spot = low cosine AND survived the
memorization screen.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import numpy as np
from sentence_transformers import SentenceTransformer

HERE = Path(__file__).parent
EMB_MODEL = "BAAI/bge-large-en-v1.5"
LOW = 0.65  # below this = embedder does not strongly bridge (model-specific, see header)


def main() -> None:
    pairs = json.loads((HERE / "candidate_pairs.json").read_text())["pairs"]
    model = SentenceTransformer(EMB_MODEL)
    rows = []
    for p in pairs:
        a, b = p["entry_term"], p["descriptor"]
        va, vb = model.encode([a, b], normalize_embeddings=True)
        cos = float(va @ vb)
        rows.append({
            "seed_concept": p["seed_concept"],
            "term_a": a, "term_b": b,
            "cross_cosine": round(cos, 4),
            "lexical_overlap": p.get("lexical_overlap"),
            "screen_verdict": p.get("screen_verdict"),
            "b_full_leak": p.get("b_full_leak"),
        })
    rows.sort(key=lambda r: r["cross_cosine"])

    out = {"embedding_model": EMB_MODEL, "n_pairs": len(rows), "low_threshold": LOW,
           "reference_cosines": {"unrelated": 0.509, "cell1_photoreflex_ppg": 0.750,
                                 "racemic_epi_racepinephrine": 0.859},
           "pairs": rows}
    (HERE / "cross_cosine_mesh.json").write_text(json.dumps(out, indent=2))

    print(f"==== MeSH candidate cross-cosine scan (n={len(rows)}) ====")
    print(f"{'cos':>6s}  {'screen':>9s}  term_a  <->  term_b")
    for r in rows:
        print(f"{r['cross_cosine']:6.3f}  {str(r['screen_verdict']):>9s}  {r['term_a'][:30]} <-> {r['term_b'][:30]}")
    low = [r for r in rows if r["cross_cosine"] < LOW]
    sweet = [r for r in low if r["screen_verdict"] == "SURVIVES"]
    print(f"\nlow-cosine (<{LOW}): {len(low)} pairs")
    print(f"SWEET SPOT (low cosine AND survived memorization screen): {len(sweet)}")
    for r in sweet:
        print(f"   {r['cross_cosine']:.3f}  {r['term_a']} <-> {r['term_b']}")
    print(f"\n[done] -> cross_cosine_mesh.json")


if __name__ == "__main__":
    main()
