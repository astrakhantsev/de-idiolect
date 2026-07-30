#!/usr/bin/env python3
"""link_ledger.py — P3: link citation OCCURRENCES to canonical WORK records (spec P3, frozen).

Inputs: the two subagent extraction JSONLs (occurrence-level, verbatim quotes).
Work key rule (frozen): DOI/arXiv ID when parseable from url, else
first_author + normalized title (+ year cluster with ±1 tolerance);
titleless candidates key on first_author + venue + year.
Outputs: ledger.jsonl (occurrences, each linked to work_id), works.jsonl (canonical works).
Also prints the seeded extraction-recall audit file selection (seed 20260719).
"""
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
SCRATCH = Path("/tmp/claude-1000/-mnt-f-hub/7cf8eca8-8b45-4981-a8f0-e531ee482f7f/scratchpad")
INPUTS = {
    "def-naming": SCRATCH / "p3-extract-defnaming.jsonl",
    "recall-backtest": SCRATCH / "p3-extract-backtest.jsonl",
}


def norm_title(t):
    if not t:
        return None
    t = re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def stable_id(url):
    if not url:
        return None
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url)
    if m:
        return f"arxiv:{m.group(1)}"
    m = re.search(r"doi\.org/(10\.[^\s?#]+)", url)
    if m:
        return f"doi:{m.group(1).rstrip('/')}"
    return None


occurrences = []
for exp, path in INPUTS.items():
    for i, line in enumerate(path.read_text().splitlines()):
        if not line.strip():
            continue
        row = json.loads(line)
        row["experiment"] = exp
        row["occ_id"] = f"{exp[:3]}-{i:03d}"
        occurrences.append(row)

# cluster into works
works = {}  # work_id -> record
by_soft = defaultdict(list)  # (first_author_lower, norm_title) -> [work_id]
for occ in occurrences:
    sid = stable_id(occ.get("url"))
    fa = (occ.get("first_author") or "").lower().strip()
    nt = norm_title(occ.get("title"))
    yr = occ.get("year")
    wid = None
    if sid and sid in works:
        wid = sid
    elif nt:
        for cand in by_soft.get((fa, nt), []):
            wy = works[cand].get("year")
            if wy is None or yr is None or abs(wy - yr) <= 1:
                wid = cand
                break
    else:
        key = (fa, (occ.get("venue") or "").lower(), yr)
        for cand_id, w in works.items():
            if w.get("_titleless_key") == key:
                wid = cand_id
                break
    if wid is None:
        wid = sid or f"w-{len(works):03d}"
        works[wid] = {
            "work_id": wid,
            "first_author": occ.get("first_author"),
            "authors": occ.get("authors"),
            "year": yr,
            "title": occ.get("title"),
            "venue": occ.get("venue"),
            "urls": [],
            "n_occurrences": 0,
            "_titleless_key": (fa, (occ.get("venue") or "").lower(), yr) if not nt else None,
        }
        if nt:
            by_soft[(fa, nt)].append(wid)
    w = works[wid]
    w["n_occurrences"] += 1
    if occ.get("url") and occ["url"] not in w["urls"]:
        w["urls"].append(occ["url"])
    if w.get("year") is None and yr is not None:
        w["year"] = yr
    if not w.get("venue") and occ.get("venue"):
        w["venue"] = occ.get("venue")
    occ["work_id"] = wid

with (HERE / "ledger.jsonl").open("w") as f:
    for occ in occurrences:
        f.write(json.dumps(occ) + "\n")
with (HERE / "works.jsonl").open("w") as f:
    for w in works.values():
        w.pop("_titleless_key", None)
        f.write(json.dumps(w) + "\n")

print(f"occurrences: {len(occurrences)}  unique works: {len(works)}")
hedged = sum(1 for o in occurrences if o.get("hedged"))
print(f"hedged occurrences: {hedged}")
for exp in INPUTS:
    n = sum(1 for o in occurrences if o['experiment'] == exp)
    print(f"  {exp}: {n} occurrences")

# seeded extraction-recall audit selection.
# These pointed at the author's private vault by absolute path. The SAME raw
# outputs are committed in this repo under receipts/, so they now resolve in-repo:
# the selection is unchanged (same seed, same sorted basenames) and it runs from a
# fresh checkout instead of only on one machine.
_RECEIPTS = Path(__file__).resolve().parents[3] / "receipts"
rng = random.Random(20260719)
for exp, d in (("def-naming", _RECEIPTS / "naming-experiment" / "def-naming-raw"),
               ("recall-backtest",
                _RECEIPTS / "capability-ladder" / "recall-backtest-raw")):
    files = sorted(p.name for p in Path(d).glob("out-*.md"))
    print(f"recall-audit files for {exp}: {rng.sample(files, 2)}")
