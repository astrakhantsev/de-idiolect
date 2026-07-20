#!/usr/bin/env python3
"""Debug harness for mesh_concept / candidate_pairs_for.

Pass --fresh to wipe the HTTP cache first (off by default so it doesn't force a full refetch).
"""
import shutil
import sys
from pathlib import Path
import mesh_client as mc
import select_pairs as sp

if "--fresh" in sys.argv:
    cache = Path(mc.CACHE)
    if cache.exists():
        shutil.rmtree(cache)
    cache.mkdir(exist_ok=True)

for seed in ["kaplan-meier estimate", "photoplethysmography", "niacin", "leprosy",
             "complex regional pain syndrome"]:
    rec = mc.mesh_concept(seed)
    if not rec:
        print(f"{seed!r}: mesh_concept -> None")
        continue
    print(f"{seed!r}: desc={rec['descriptor']!r}  n_entry={len(rec['entry_terms'])}")
    print(f"   entry_terms: {rec['entry_terms'][:6]}")
    ps = sp.candidate_pairs_for(seed)
    print("   pairs:", [(p["entry_term"], round(p["lexical_overlap"], 2)) for p in ps])
