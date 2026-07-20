#!/usr/bin/env python3
"""score_p3.py — P3 pre-registered endpoints from ledger + works + verify-batch outputs.

PRIMARY: occurrence-level survival = occurrences with work exists=yes AND biblio in
{full, minor} AND that occurrence's claim_support=supported / total occurrences.
SECONDARY: work-level validity (same rule, any occurrence supported).
Plus failure taxonomy on both levels; exploratory splits: hedged vs confident,
by source experiment.
"""
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    e = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - e) / d, (c + e) / d)


occs = [json.loads(l) for l in (HERE / "ledger.jsonl").read_text().splitlines() if l.strip()]
works = {w["work_id"]: w for w in (json.loads(l) for l in (HERE / "works.jsonl").read_text().splitlines() if l.strip())}

# AMENDMENT M2: endpoints computed over the seeded 100-occurrence sample only.
sample = json.loads((HERE / "sample-occ-ids.json").read_text())
occs = [o for o in occs if o["occ_id"] in set(sample["occ_ids"])]
works = {wid: w for wid, w in works.items() if wid in set(sample["induced_work_ids"])}
verdicts = {}
occ_support = {}
for f in sorted(HERE.glob("verify-batch-*.jsonl")):
    for line in f.read_text().splitlines():
        if not line.strip():
            continue
        v = json.loads(line)
        verdicts[v["work_id"]] = v
        for ov in v.get("occurrences", []):
            occ_support[ov["occ_id"]] = ov.get("claim_support")

missing_works = [w for w in works if w not in verdicts]

def work_ok(v):
    return v and v.get("exists") == "yes" and v.get("biblio") in ("full", "minor")

occ_rows = []
for o in occs:
    v = verdicts.get(o["work_id"])
    cs = occ_support.get(o["occ_id"])
    survived = bool(work_ok(v) and cs == "supported")
    if not v:
        fail = "unjudged"
    elif v.get("exists") == "no":
        fail = "nonexistent"
    elif v.get("exists") == "unverifiable":
        fail = "unverifiable"
    elif v.get("biblio") == "major":
        fail = "biblio_major"
    elif cs == "contradicted":
        fail = "claim_contradicted"
    elif cs == "not_locatable":
        fail = "claim_not_locatable"
    elif survived:
        fail = None
    else:
        fail = "other"
    occ_rows.append({**o, "survived": survived, "failure": fail})

n = len(occ_rows)
surv = sum(1 for r in occ_rows if r["survived"])
tax = Counter(r["failure"] for r in occ_rows if r["failure"])

work_rows = {}
for wid, v in verdicts.items():
    occ_ids = [o["occ_id"] for o in occs if o["work_id"] == wid]
    any_sup = any(occ_support.get(i) == "supported" for i in occ_ids)
    work_rows[wid] = {"valid": bool(work_ok(v) and any_sup), "exists": v.get("exists"), "biblio": v.get("biblio")}
wn = len(works)
wsurv = sum(1 for r in work_rows.values() if r["valid"])
wtax = Counter((r["exists"], r["biblio"]) for r in work_rows.values() if not r["valid"])

def split(rows, keyf):
    out = {}
    for r in rows:
        out.setdefault(keyf(r), [0, 0])
        out[keyf(r)][1] += 1
        if r["survived"]:
            out[keyf(r)][0] += 1
    return {k: f"{a}/{b} = {a/b:.2f}" for k, (a, b) in sorted(out.items())}

payload = {
    "preregistered": {
        "occurrence_survival": f"{surv}/{n} = {surv/n:.3f}" if n else "n/a",
        "occurrence_survival_wilson95": [round(x, 3) for x in wilson(surv, n)],
        "work_validity": f"{wsurv}/{wn} = {wsurv/wn:.3f}" if wn else "n/a",
        "occurrence_failure_taxonomy": dict(tax),
        "work_failure_taxonomy": {f"{k[0]}/{k[1]}": c for k, c in wtax.items()},
    },
    "exploratory": {
        "by_hedged": split(occ_rows, lambda r: f"hedged={bool(r.get('hedged'))}"),
        "by_experiment": split(occ_rows, lambda r: r["experiment"]),
    },
    "missing_work_verdicts": missing_works,
}
(HERE / "p3_scores.json").write_text(json.dumps(payload, indent=2))
with (HERE / "occ_rows.jsonl").open("w") as f:
    for r in occ_rows:
        f.write(json.dumps(r) + "\n")
print(json.dumps(payload["preregistered"], indent=2))
print("exploratory:", json.dumps(payload["exploratory"], indent=2))
if missing_works:
    print(f"WARNING: {len(missing_works)} works lack verdicts: {missing_works[:10]}")
print("written: p3_scores.json, occ_rows.jsonl")
