#!/usr/bin/env python3
"""E2 residue far-side exclusion (prereg amendment v0.3): each residue text embedded
against the 6 HELD-OUT docs (3 own-side + 3 far-side); residue passes iff the
top-ranked doc is own-side."""
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from smoke import parse_json_out, E2_PAIRS

BASE = Path(__file__).resolve().parent
model = SentenceTransformer("BAAI/bge-large-en-v1.5")
docs = [(s, f.stem, f.read_text()) for s in ("a", "b")
        for f in sorted((BASE / f"corpora/{s}").glob("*.md")) if f.stem in ("09", "10", "11")]
emb = model.encode([t for _, _, t in docs], normalize_embeddings=True)

out = {}
for pid in E2_PAIRS:
    obj = parse_json_out(BASE / f"runs/e2/out-dfull-{pid}.json")
    out[pid] = {}
    if not obj: continue
    for rk, own in (("residue_1", "a"), ("residue_2", "b")):
        q = model.encode([obj[rk]], normalize_embeddings=True)[0]
        sims = emb @ q
        order = sims.argsort()[::-1]
        ranking = [[docs[i][0], docs[i][1], float(sims[i])] for i in order]
        out[pid][rk] = {"own_side": own, "top1_own": docs[order[0]][0] == own, "ranking": ranking}
json.dump(out, open(BASE / "runs/e2/residues.json", "w"), indent=1)
print(json.dumps({p: {r: v["top1_own"] for r, v in d.items()} for p, d in out.items() if d}, indent=1))
