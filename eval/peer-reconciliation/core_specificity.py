#!/usr/bin/env python3
"""v0.4 core-specificity gate (prereg amendment): a decompose core passes iff BOTH of
its own pair's per-term masked DEV bundles rank in the top 3 of all 20 bundle cosines.
Covers composition decompose outputs (runs/decompose/out-P*.json) and E2 decompose-full
outputs (runs/e2/out-dfull-P*.json, keyed dfull-P*)."""
import json, re
from pathlib import Path
from sentence_transformers import SentenceTransformer
from smoke import parse_json_out, load_exc, mask_text, A_TERMS, B_TERMS, PAIRS

BASE = Path(__file__).resolve().parent
exc = load_exc()
model = SentenceTransformer("BAAI/bge-large-en-v1.5")

bundles = []
for side, terms in (("a", A_TERMS), ("b", B_TERMS)):
    for term in terms:
        text = " ".join(mask_text(e["text"], side, term) for e in exc[side][term]["dev"])
        bundles.append((side, term, text))
emb = model.encode([t for _, _, t in bundles], normalize_embeddings=True)

out = {}
def gate(key, core, term_a, term_b):
    q = model.encode([core], normalize_embeddings=True)[0]
    sims = emb @ q
    order = sims.argsort()[::-1]
    ranked = [(bundles[i][0], bundles[i][1], float(sims[i])) for i in order]
    top3 = {(s, t) for s, t, _ in ranked[:3]}
    ok = ("a", term_a) in top3 and ("b", term_b) in top3
    out[key] = {"pass": ok, "top5": ranked[:5]}

for p in PAIRS:
    for key, path in ((p["pair_id"], BASE / f"runs/decompose/out-{p['pair_id']}.json"),
                       (f"dfull-{p['pair_id']}", BASE / f"runs/e2/out-dfull-{p['pair_id']}.json")):
        if not path.exists(): continue
        obj = parse_json_out(path)
        if obj and obj.get("core"): gate(key, obj["core"], p["term_a"], p["term_b"])
json.dump(out, open(BASE / "runs/core_specificity.json", "w"), indent=1)
print(json.dumps({k: v["pass"] for k, v in out.items()}, indent=1))
