#!/usr/bin/env python3
"""retrieve.py — frozen retrieval stage (spec rev 3 §2.7).

Pipeline frozen here (script sha256 is the config): bge-large-en-v1.5 from the
local HF cache (snapshot path+hash logged), document serialization =
title + ". " + abstract, cosine similarity on normalized embeddings, ranking
descending, ties by doc id ascending. Queries read from queries.json
(id -> text). Chance benchmarks (N=18, M=3) printed next to every rank.

Output: runs/retrieval.json
"""
import hashlib
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

HERE = Path(__file__).parent
RECORDS = HERE / "records" / "corpus_records.jsonl"
QUERIES = HERE / "queries.json"
OUT = HERE / "runs" / "retrieval.json"
MODEL_NAME = "BAAI/bge-large-en-v1.5"

CHANCE = {
    "P_first_owner_rank1": 3 / 18,          # 0.167
    "P_first_owner_le2": 1 - (105 / 153),   # 0.314
    "E_hits_at_5": 5 * 3 / 18,              # 0.833
}


def main():
    records = [json.loads(l) for l in RECORDS.read_text().splitlines() if l.strip()]
    assert len(records) == 18, f"expected 18 records, got {len(records)}"
    owners = {r["id"] for r in records if r["set"] == "owner"}
    assert len(owners) == 3, f"expected 3 owner records, got {len(owners)}"
    queries = json.loads(QUERIES.read_text())

    model = SentenceTransformer(MODEL_NAME)
    doc_texts = [f"{r['title']}. {r['abstract']}" for r in records]
    doc_emb = model.encode(doc_texts, normalize_embeddings=True)

    results = {}
    for qid, qtext in queries.items():
        q_emb = model.encode([qtext], normalize_embeddings=True)[0]
        sims = doc_emb @ q_emb
        order = sorted(range(len(records)), key=lambda i: (-float(sims[i]), records[i]["id"]))
        ranked = [records[i]["id"] for i in order]
        first_owner = next(rank for rank, did in enumerate(ranked, 1) if did in owners)
        hits5 = sum(1 for did in ranked[:5] if did in owners)
        results[qid] = {
            "query_sha256": hashlib.sha256(qtext.encode()).hexdigest(),
            "ranked": ranked,
            "sims": {records[i]["id"]: round(float(sims[i]), 4) for i in order},
            "first_owner_rank": first_owner,
            "hits_at_5": hits5,
        }
        print(f"{qid:10s} first-owner rank = {first_owner}  hits@5 = {hits5}  "
              f"(chance: rank-1 p={CHANCE['P_first_owner_rank1']:.3f}, "
              f"E[hits@5]={CHANCE['E_hits_at_5']:.2f})")

    payload = {
        "model": MODEL_NAME,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "records_sha256": hashlib.sha256(RECORDS.read_bytes()).hexdigest(),
        "chance_benchmarks": CHANCE,
        "results": results,
    }
    OUT.write_text(json.dumps(payload, indent=2))
    print(f"written: {OUT}")


if __name__ == "__main__":
    main()
