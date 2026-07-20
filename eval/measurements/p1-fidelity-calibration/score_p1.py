#!/usr/bin/env python3
"""score_p1.py — score P1 calibration verdicts against the frozen rule + expected matrix.

Frozen failure rule (fidelity-checklist.md): any of i-iv not PRESERVED, or v not PASS,
or vi names-not-in-excerpts non-empty -> config FAILS. Judge JSON may arrive fenced;
vi key names vary across judge outputs (names_found/named_items etc.) - both handled.
Malformed JSON is reported as MALFORMED (frozen rule: one re-ask then conservative FAIL;
re-asks are run manually and logged if needed).
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
IDS = ["A1", "A2", "A3", "A4", "S-a", "S-b", "S-c", "S-d", "S-e"]
FAITHFUL = {"A1", "A2", "A3", "A4"}
PLANTED = {"S-a": "iii", "S-b": "iv", "S-c": "iv", "S-d": "vi", "S-e": "v"}
ACCEPTABLE_SECONDARY = {"S-e": {"vi"}}


def parse(raw):
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def item_verdicts(obj):
    """Return (failed_items:set, detail:dict)."""
    failed = set()
    detail = {}

    def verdict_text(v):
        # judge outputs vary: flat "PRESERVED — ..." strings OR nested
        # {"verdict": "PRESERVED", "justification": "..."} objects
        if isinstance(v, dict) and "verdict" in v:
            return str(v["verdict"])
        return v if isinstance(v, str) else json.dumps(v)

    for k in ("i", "ii", "iii", "iv"):
        txt = verdict_text(obj.get(k, ""))
        detail[k] = txt[:120]
        if not txt.strip().upper().startswith("PRESERVED"):
            failed.add(k)
    txt5 = verdict_text(obj.get("v", ""))
    detail["v"] = txt5[:120]
    if not txt5.strip().upper().startswith("PASS"):
        failed.add("v")
    vi = obj.get("vi", {})
    bad_names = []
    if isinstance(vi, dict):
        for key in ("names_not_in_excerpts", "not_in_notes", "names_not_in_notes"):
            if vi.get(key):
                bad_names = vi[key]
                break
    elif isinstance(vi, list):
        bad_names = vi
    detail["vi"] = json.dumps(bad_names)
    if bad_names:
        failed.add("vi")
    return failed, detail


rows = {}
for cid in IDS:
    f = HERE / "runs" / f"fidelity-{cid}.json"
    if not f.exists():
        rows[cid] = {"status": "MISSING"}
        continue
    obj = parse(f.read_text())
    if obj is None:
        rows[cid] = {"status": "MALFORMED"}
        continue
    failed, detail = item_verdicts(obj)
    rows[cid] = {"status": "FAIL" if failed else "PASS", "failed_items": sorted(failed), "detail": detail}

fp = sum(1 for c in FAITHFUL if rows[c].get("status") in ("FAIL", "MALFORMED"))
det = sum(1 for c in PLANTED if rows[c].get("status") in ("FAIL", "MALFORMED"))
attr = sum(1 for c, item in PLANTED.items() if rows[c].get("status") == "FAIL" and item in rows[c].get("failed_items", []))
strict = sum(
    1 for c, item in PLANTED.items()
    if rows[c].get("status") == "FAIL"
    and set(rows[c]["failed_items"]) <= ({item} | ACCEPTABLE_SECONDARY.get(c, set()))
    and item in rows[c]["failed_items"]
)

out = {
    "per_config": rows,
    "preregistered": {
        "fp_rate_faithful": f"{fp}/4",
        "detection_rate_seeded": f"{det}/5",
        "attribution_rate_seeded": f"{attr}/5",
    },
    "exploratory": {"strict_isolation_catches": f"{strict}/5"},
}
(HERE / "runs" / "p1_scores.json").write_text(json.dumps(out, indent=2))
for cid in IDS:
    r = rows[cid]
    print(f"{cid:4s} {r.get('status'):9s} failed={r.get('failed_items', '-')}")
print(f"\nPRE-REGISTERED: FP {fp}/4 faithful; detection {det}/5; attribution {attr}/5  (strict isolation {strict}/5)")
print(f"written: {HERE/'runs'/'p1_scores.json'}")
