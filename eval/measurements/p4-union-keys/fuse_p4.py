#!/usr/bin/env python3
"""fuse_p4.py — P4 union-of-keys RRF fusion (measurement spec P4).

Inputs: frozen e2e retrieval.json rankings (K1, K2, N, D-sonnet, D-opus) plus E =
the raw excerpt-pool key, recomputed to a full 18-doc ranking with the same
model + serialization as the frozen retrieve.py. Sanity gate: recomputed E top-5
must equal the archived probe_extractive_key.json top-5 (the probe script was not
persisted, so the query text is reconstructed; variants tried are logged and the
matching one is frozen into the output).

Fusion (pre-registered): RRF score(d) = sum over keys of 1/(60 + rank_k(d)),
ties by doc id ascending. Fusions: U3s={K1,N,D-sonnet}, U3o={K1,N,D-opus},
U5={K1,K2,N,D-sonnet,D-opus}, U6=U5+E. Comparison: each fusion vs its BEST
single constituent (lowest first-owner rank, ties by higher hits@5).
"""
import json
import hashlib
import re
import sys
from pathlib import Path

from sentence_transformers import SentenceTransformer

HERE = Path(__file__).parent
E2E = (HERE / ".." / ".." / "e2e-cell").resolve()
OUT = HERE / "runs"
OUT.mkdir(exist_ok=True)

K_RRF = 60

records = [json.loads(l) for l in (E2E / "records" / "corpus_records.jsonl").read_text().splitlines() if l.strip()]
owners = {r["id"] for r in records if r["set"] == "owner"}
setof = {r["id"]: r["set"] for r in records}
retrieval = json.loads((E2E / "runs" / "retrieval.json").read_text())
probe = json.loads((E2E / "runs" / "probe_extractive_key.json").read_text())
probe_top5 = [t[0] for t in probe["top5"]]

model = SentenceTransformer("BAAI/bge-large-en-v1.5")
doc_emb = model.encode([f"{r['title']}. {r['abstract']}" for r in records], normalize_embeddings=True)


def rank_query(qtext):
    q = model.encode([qtext], normalize_embeddings=True)[0]
    sims = doc_emb @ q
    order = sorted(range(len(records)), key=lambda i: (-float(sims[i]), records[i]["id"]))
    return [records[i]["id"] for i in order], {records[i]["id"]: round(float(sims[i]), 4) for i in order}


excerpts_full = (E2E / "runs" / "c2-excerpts.md").read_text()
# variant order per spec + AMENDMENT M1 (logged pre-run in the results doc): the two
# spec variants failed the ID-level gate; a logged sweep found markdown-stripped
# variants reproduce the archived top-5 ID ranking exactly (sims differ uniformly
# ~0.01 — disclosed; RRF consumes ranks only). Gate stays: top-5 ID equality.
body_lines = [l for l in excerpts_full.splitlines() if l.strip() and not l.startswith("#") and not l.startswith("source:")]
variants = {
    "full-file": excerpts_full,
    "bodies-only": "\n".join(body_lines),
    "full-nobold": excerpts_full.replace("**", ""),
    "full-stripmd": re.sub(r"[*_`]", "", excerpts_full),
}

e_ranked = None
e_variant = None
e_sims = None
for name, text in variants.items():
    ranked, sims = rank_query(text)
    if ranked[:5] == probe_top5:
        e_ranked, e_variant, e_sims = ranked, name, sims
        break
if e_ranked is None:
    print("SANITY FAIL: no reconstruction variant reproduces the archived probe top-5", file=sys.stderr)
    for name, text in variants.items():
        ranked, _ = rank_query(text)
        print(f"  {name}: top5 = {ranked[:5]} (archived: {probe_top5})", file=sys.stderr)
    sys.exit(1)


def metrics(ranked):
    first = next(i for i, d in enumerate(ranked, 1) if d in owners)
    hits5 = sum(1 for d in ranked[:5] if d in owners)
    fp5 = {"misroute": sum(1 for d in ranked[:5] if setof[d] == "misroute"),
           "distractor": sum(1 for d in ranked[:5] if setof[d] == "distractor")}
    return {"first_owner_rank": first, "hits_at_5": hits5, "fp_top5": fp5, "top5": ranked[:5]}


rankings = {k: retrieval["results"][k]["ranked"] for k in ("K1", "K2", "N", "D-sonnet", "D-opus")}
rankings["E"] = e_ranked


def rrf(keys):
    scores = {}
    for k in keys:
        for rank, d in enumerate(rankings[k], 1):
            scores[d] = scores.get(d, 0.0) + 1.0 / (K_RRF + rank)
    return sorted(scores, key=lambda d: (-scores[d], d))


FUSIONS = {
    "U3s": ["K1", "N", "D-sonnet"],
    "U3o": ["K1", "N", "D-opus"],
    "U5": ["K1", "K2", "N", "D-sonnet", "D-opus"],
    "U6": ["K1", "K2", "N", "D-sonnet", "D-opus", "E"],
}

singles = {k: metrics(v) for k, v in rankings.items()}
fusions = {}
for fname, keys in FUSIONS.items():
    fused = rrf(keys)
    m = metrics(fused)
    best = min(keys, key=lambda k: (singles[k]["first_owner_rank"], -singles[k]["hits_at_5"]))
    bm = singles[best]
    m["constituents"] = keys
    m["best_constituent"] = best
    m["beats_or_ties_best"] = (m["first_owner_rank"] <= bm["first_owner_rank"] and m["hits_at_5"] >= bm["hits_at_5"])
    m["strictly_better_on_one"] = (m["first_owner_rank"] < bm["first_owner_rank"] or m["hits_at_5"] > bm["hits_at_5"])
    fusions[fname] = m

# frozen rule (spec P4): BOTH U3 fusions weakly dominate their best constituent,
# AND at least one strict improvement across the four (fusion x metric) comparisons
# (review fold: an earlier revision wrongly required a strict improvement in EACH fusion)
supported = (
    all(fusions[f]["beats_or_ties_best"] for f in ("U3s", "U3o"))
    and any(fusions[f]["strictly_better_on_one"] for f in ("U3s", "U3o"))
)

payload = {
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "rrf_k": K_RRF,
    "e_key_variant": e_variant,
    "e_sanity_top5_matches_probe": True,
    "e_full_ranking": e_ranked,
    "e_sims": e_sims,
    "chance": {"P_first_owner_rank1": 3 / 18, "E_hits_at_5": 5 * 3 / 18},
    "singles": singles,
    "fusions": fusions,
    "preregistered_verdict_union_beats_single": supported,
}
(OUT / "p4_fusion.json").write_text(json.dumps(payload, indent=2))
for name in ("K1", "K2", "N", "D-sonnet", "D-opus", "E"):
    m = singles[name]
    print(f"single {name:9s} first-owner {m['first_owner_rank']:2d}  hits@5 {m['hits_at_5']}  top5 {m['top5']}")
for fname, m in fusions.items():
    print(f"fusion {fname:8s} first-owner {m['first_owner_rank']:2d}  hits@5 {m['hits_at_5']}  top5 {m['top5']}  best-const {m['best_constituent']}  ok {m['beats_or_ties_best']}/{m['strictly_better_on_one']}")
print(f"PRE-REGISTERED VERDICT (union beats single, both U3): {supported}")
print(f"written: {OUT/'p4_fusion.json'}")
