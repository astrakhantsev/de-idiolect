#!/usr/bin/env python3
"""Cross-corpus retrieval for the peer smoke test (prereg §Composition: mutual-hit rule).
Query = each side's definition against the OTHER side's 11 docs; hit iff >=1 of top-3
docs contains the partner term string. Also reports the corpus-centroid cosine diagnostic."""
import json, re, sys
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE = Path(__file__).resolve().parent
KEY = json.load(open(BASE / "key/answer_key.json"))
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

model = SentenceTransformer("BAAI/bge-large-en-v1.5")
docs = {}
for side in ("a", "b"):
    docs[side] = [(f.stem, f.read_text()) for f in sorted((BASE / f"corpora/{side}").glob("[0-9][0-9].md"))]
emb = {side: model.encode([t for _, t in docs[side]], normalize_embeddings=True) for side in docs}

out = {}
for p in KEY["pairs"]:
    res = {}
    for d, dside, tside, term in (("a2b", "a", "b", p["term_b"]), ("b2a", "b", "a", p["term_a"])):
        dt = (BASE / f"runs/definitions/out-{dside}-{slug(p['term_a'] if dside == 'a' else p['term_b'])}.txt").read_text()
        q = model.encode([dt], normalize_embeddings=True)[0]
        sims = emb[tside] @ q
        top3 = sims.argsort()[::-1][:3]
        hit = any(term.lower() in docs[tside][i][1].lower() for i in top3)
        res[d] = {"hit": bool(hit), "top3": [[docs[tside][i][0], float(sims[i])] for i in top3]}
    out[p["pair_id"]] = {"a2b": res["a2b"], "b2a": res["b2a"],
                          "a2b_hit": res["a2b"]["hit"], "b2a_hit": res["b2a"]["hit"],
                          "mutual": res["a2b"]["hit"] and res["b2a"]["hit"]}
cent = {s: emb[s].mean(0) for s in emb}
for s in cent: cent[s] = cent[s] / (cent[s] ** 2).sum() ** 0.5
out["_diagnostic_corpus_centroid_cosine"] = float(cent["a"] @ cent["b"])
json.dump(out, open(BASE / "runs/retrieval.json", "w"), indent=1)
print(json.dumps({k: (v if k.startswith("_") else {"mutual": v["mutual"]}) for k, v in out.items()}, indent=1))
