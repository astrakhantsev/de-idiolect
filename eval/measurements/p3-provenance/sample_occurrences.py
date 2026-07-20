#!/usr/bin/env python3
"""sample_occurrences.py — AMENDMENT M2 (logged pre-verification): the frozen
three-facet protocol is applied to a seeded random sample of 100 occurrences
(seed 20260719) instead of the full 539-occurrence universe, which came in 3-5x
larger than the planning estimate. Size-driven scope cap, decided before any
verification ran; the unsampled remainder is reported as not-verified.
Primary endpoint becomes: occurrence-level survival on the sample, with a 95%
Wilson interval. Work-level stats on the induced work set are exploratory
(popularity-biased by construction — disclosed).
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
N = 100

occs = [json.loads(l) for l in (HERE / "ledger.jsonl").read_text().splitlines() if l.strip()]
rng = random.Random(20260719)
sample = rng.sample(occs, N)
sample_ids = sorted(o["occ_id"] for o in sample)
work_ids = sorted({o["work_id"] for o in sample})
(HERE / "sample-occ-ids.json").write_text(json.dumps({"seed": 20260719, "n": N, "occ_ids": sample_ids, "induced_work_ids": work_ids}, indent=2))
print(f"sampled {N} occurrences -> {len(work_ids)} induced works")
print(f"hedged in sample: {sum(1 for o in sample if o.get('hedged'))}")
by_exp = {}
for o in sample:
    by_exp[o["experiment"]] = by_exp.get(o["experiment"], 0) + 1
print("by experiment:", by_exp)
