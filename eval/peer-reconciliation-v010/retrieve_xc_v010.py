#!/usr/bin/env python3
"""v0.10 cross-corpus retrieval — derived by COPYING the frozen v0.9 retrieve_xc.py and
modifying: (1) --v010 writes runs/v010/retrieval.json; (2) --no-determinism skips the
frozen-baseline determinism check (key-3 and each confirmatory draw are FRESH — this first
execution IS the retrieval record, matching the frozen key-3 TEST harness's
retrieve_xc.py --no-determinism, run_test_v09.sh header note). The §2.6/§9-F7 retrieval
ALGORITHM is byte-identical to v0.9 (encoder, snapshot, tokenization/truncation, cosine,
(-sim, index) ranking via smoke.rank_top3, hit@3, mutual, both L2 and L0+L1 queries).

Encoder: BAAI/bge-large-en-v1.5 from the EXPLICIT local snapshot path (no hub resolution);
snapshot tree hash goes into the freeze manifest via --snapshot-hash.
"""
import json, sys, hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
from smoke_v010 import rank_top3  # single frozen definition of the ranking rule

SNAPSHOT = Path("/home/nik/.cache/huggingface/hub/models--BAAI--bge-large-en-v1.5/snapshots/d4aa6901d3a41ba39fb536a557fa166f842b0e09")

def tree_hash(d):
    """§9-F7: sha256 over the sorted list of (relative path, file sha256) pairs."""
    entries = []
    for p in sorted(x for x in d.rglob("*") if x.is_file()):
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        entries.append(f"{p.relative_to(d)} {h}")
    return hashlib.sha256("\n".join(entries).encode()).hexdigest()

def main():
    assert SNAPSHOT.is_dir(), f"bge snapshot not found at {SNAPSHOT}"
    if "--snapshot-hash" in sys.argv:
        print(f"bge_snapshot_path: {SNAPSHOT}")
        print(f"bge_snapshot_tree_sha256: {tree_hash(SNAPSHOT)}")
        return
    v010 = "--v010" in sys.argv           # both queries (L2 for τ0, L0+L1 for τ1/τ2)
    no_determinism = "--no-determinism" in sys.argv
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(SNAPSHOT))
    alive = json.load(open(BASE / "runs/alive-pairs.json"))
    docs = {}
    for side in ("a", "b"):
        docs[side] = [(f.stem, f.read_text()) for f in sorted((BASE / f"corpora/{side}").glob("[0-9][0-9].md"))]
        assert len(docs[side]) == 11, f"corpus {side}: expected exactly 11 docs, got {len(docs[side])}"
    emb = {side: model.encode([t for _, t in docs[side]], normalize_embeddings=True) for side in docs}
    queries = {"L2": lambda lad: lad["L2"], "L0L1": lambda lad: lad["L0"] + " " + lad["L1"]}
    if not v010: queries = {"L2": queries["L2"]}
    out = {}
    for pid, info in sorted(alive.items()):
        entry = {}
        for qname, qf in queries.items():
            res = {}
            for d, dside, tside, partner in (("a2b", "a", "b", info["term_b"]),
                                             ("b2a", "b", "a", info["term_a"])):
                lad = json.loads(Path(info[f"L2_{dside}"]).read_text())
                q = model.encode([qf(lad)], normalize_embeddings=True)[0]
                sims = [float(s) for s in (emb[tside] @ q)]
                top3 = rank_top3(sims)
                hit = any(partner.lower() in docs[tside][i][1].lower() for i in top3)
                res[d] = {"hit": bool(hit), "top3": [[docs[tside][i][0], sims[i]] for i in top3]}
            entry[qname] = {"a2b": res["a2b"], "b2a": res["b2a"],
                            "mutual": res["a2b"]["hit"] and res["b2a"]["hit"]}
        out[pid] = entry if v010 else {**entry["L2"]}
    cent = {s: emb[s].mean(0) for s in emb}
    for s in cent: cent[s] = cent[s] / (cent[s] ** 2).sum() ** 0.5
    out["_diagnostic_corpus_centroid_cosine"] = float(cent["a"] @ cent["b"])
    dest = BASE / ("runs/v010/retrieval.json" if v010 else "runs/retrieval.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(dest, "w"), indent=1)
    if v010 and not no_determinism:
        frozen = json.load(open(BASE / "runs/retrieval.json"))
        for pid in alive:
            for d in ("a2b", "b2a"):
                new, old = out[pid]["L2"][d], frozen[pid][d]
                same = (new["hit"] == old["hit"]
                        and [x[0] for x in new["top3"]] == [x[0] for x in old["top3"]]
                        and all(abs(a[1] - b[1]) < 1e-8 for a, b in zip(new["top3"], old["top3"])))
                if not same:
                    raise SystemExit(f"RUN-HALT: retrieval determinism check failed on {pid}/{d}")
            if out[pid]["L2"]["mutual"] != frozen[pid]["mutual"]:
                raise SystemExit(f"RUN-HALT: retrieval determinism check failed on {pid}/mutual")
        print("determinism check vs frozen retrieval: OK (full L2 objects)")
    elif v010:
        print("determinism check SKIPPED (--no-determinism: fresh key, first execution is the record)")
    print(json.dumps({k: v for k, v in out.items() if k.startswith("_")}, indent=1))

if __name__ == "__main__":
    main()
