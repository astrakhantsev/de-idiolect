#!/usr/bin/env python3
"""p2_retrieve.py — EXPLORATORY retrieval ranks for the gate-passing guided definitions
on the frozen 18-doc corpus (same model + serialization as the frozen retrieve.py)."""
import hashlib
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

HERE = Path(__file__).parent
E2E = (HERE / ".." / ".." / "e2e-cell").resolve()
records = [json.loads(l) for l in (E2E / "records" / "corpus_records.jsonl").read_text().splitlines() if l.strip()]
owners = {r["id"] for r in records if r["set"] == "owner"}
setof = {r["id"]: r["set"] for r in records}

queries = {}
for m in ("sonnet", "opus"):
    f = HERE / "runs" / f"guided-{m}-ACCEPTED.txt"
    if f.exists():
        queries[f"G-{m}"] = f.read_text().strip()

model = SentenceTransformer("BAAI/bge-large-en-v1.5")
doc_emb = model.encode([f"{r['title']}. {r['abstract']}" for r in records], normalize_embeddings=True)

results = {}
for qid, qtext in queries.items():
    q = model.encode([qtext], normalize_embeddings=True)[0]
    sims = doc_emb @ q
    order = sorted(range(len(records)), key=lambda i: (-float(sims[i]), records[i]["id"]))
    ranked = [records[i]["id"] for i in order]
    first = next(rank for rank, d in enumerate(ranked, 1) if d in owners)
    hits5 = sum(1 for d in ranked[:5] if d in owners)
    top5 = [(d, setof[d], round(float(sims[[r['id'] for r in records].index(d)]), 4)) for d in ranked[:5]]
    results[qid] = {"query_sha256": hashlib.sha256(qtext.encode()).hexdigest(), "first_owner_rank": first, "hits_at_5": hits5, "top5": top5, "ranked": ranked}
    print(f"{qid}: first-owner rank {first}  hits@5 {hits5}  top5 {top5}")

payload = {"label": "EXPLORATORY (spec P2): retrieval of gate-passing guided definitions; chance rank-1 p=0.167, E[hits@5]=0.83", "results": results}
(HERE / "runs" / "p2_retrieval.json").write_text(json.dumps(payload, indent=2))
print("written:", HERE / "runs" / "p2_retrieval.json")
