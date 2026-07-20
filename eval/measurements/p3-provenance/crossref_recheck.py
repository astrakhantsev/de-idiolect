#!/usr/bin/env python3
"""crossref_recheck.py — EXPLORATORY (labeled, post-hoc): resolve the access-unverifiable
works against the Crossref bibliographic API. Settles exists+biblio only (claim_support
stays unmeasured for these — disclosed). Not part of the pre-registered endpoint.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
works = {json.loads(l)["work_id"]: json.loads(l) for l in open(HERE / "works.jsonl")}
verdicts = {}
for f in sorted(HERE.glob("verify-batch-*.jsonl")):
    for line in f.read_text().splitlines():
        if line.strip():
            v = json.loads(line)
            verdicts[v["work_id"]] = v
unver = [w for w, v in verdicts.items() if v.get("exists") == "unverifiable"]


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


results = []
for wid in sorted(unver):
    w = works[wid]
    q = " ".join(str(x) for x in (w.get("title"), w.get("first_author"), w.get("year")) if x)
    url = "https://api.crossref.org/works?rows=3&query.bibliographic=" + urllib.parse.quote(q)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "provenance-check/1.0 (mailto:terms@astrakhantsev.com)"})
        data = json.loads(urllib.request.urlopen(req, timeout=30).read())
        items = data["message"]["items"]
    except Exception as e:
        results.append({"work_id": wid, "crossref": "API_ERROR", "error": str(e)[:80]})
        time.sleep(1)
        continue
    best = None
    for it in items:
        t = norm((it.get("title") or [""])[0])
        ct = norm(w.get("title"))
        yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        fam = [a.get("family", "") for a in it.get("author", [])][:1]
        author_ok = w.get("first_author") and fam and norm(w["first_author"]) in norm(fam[0]) or norm(fam[0] if fam else "") in norm(w.get("first_author") or "")
        title_ok = ct and (ct in t or t in ct or len(set(ct.split()) & set(t.split())) >= max(3, len(ct.split()) // 2))
        year_ok = w.get("year") is None or yr is None or abs(int(yr) - int(w["year"])) <= 1
        if title_ok and year_ok:
            best = {"doi": it.get("DOI"), "title": (it.get("title") or [""])[0][:80], "year": yr, "container": (it.get("container-title") or [""])[0][:50], "author_ok": bool(author_ok)}
            break
    results.append({"work_id": wid, "cited": {"t": (w.get("title") or "")[:60], "a": w.get("first_author"), "y": w.get("year")}, "crossref_match": best})
    time.sleep(1)

(HERE / "crossref_recheck.json").write_text(json.dumps(results, indent=2))
matched = sum(1 for r in results if r.get("crossref_match"))
print(f"unverifiable works: {len(unver)}; crossref bibliographic match: {matched}")
for r in results:
    m = r.get("crossref_match")
    status = f"MATCH doi:{m['doi']} ({m['year']}, {m['container']})" if m else ("API_ERROR" if r.get("crossref") else "NO MATCH")
    print(f"  {r['work_id']}: {status}")
