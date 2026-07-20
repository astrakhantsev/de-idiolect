#!/usr/bin/env python3
"""sensitivity_p3.py — post-hoc review-fold sensitivity analyses for P3 (all labeled,
none replaces the amended-primary 66/100). Adjudications are persisted here as data.

S1 eligibility: 12 mechanically-flagged sampled occurrences hand-adjudicated against the
frozen owner-candidate definition; 9 INELIGIBLE (author+year-only shells, nickname-only
systems, resource mentions, no-year hedges), 3 ELIGIBLE via stable-ID (arXiv) or
corporate-author identification (interpretation note: the frozen enumeration of
identifiability forms was non-exhaustive; a stable ID identifies more strongly).
S2 strict-primary receipts: exists=yes works whose receipt page is a SECONDARY source
(encyclopedia, bookseller, blog explainer, R-doc, textbook page, essay-about) downgraded;
abstract-indexer pages (RePEc, OpenAIRE, EPA HERO, PubMed) and author/venue/repository
copies kept as acceptable abstract-page equivalents.
S3 cap-compliant: exists=yes works whose fetches_used exceeded the frozen stop rule
(2 fetches + 1 Wayback = 3) downgraded — over-fetching CAN inflate survival (the extra
attempts are what produced some receipts), correcting an earlier wrong claim.
S4 = S1+S2+S3 combined floor.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

INELIGIBLE_OCCS = {
    "def-027": "Chow/Schwartz BBN c.1989-90 — no title, no venue, no year ('exact citation' absent in source)",
    "def-056": "Murphy 'mid-to-late-1980s MWR paper' — no year, no title",
    "def-177": "OLaLa — nickname only inside cited related-work, no authors/venue/year",
    "def-185": "Bilac et al. 2004 — no title, no venue",
    "def-206": "Neyman & Pearson (1933) — author+year only",
    "def-225": "Platt (1999) — author+year only",
    "def-257": "'PoLL ~2024, can't give authors' — explicitly unidentifiable by frozen forms",
    "def-354": "UMLS — resource mention, no authors/year in occurrence",
    "def-377": "Lusicky 2015 — author+year only",
}
ELIGIBLE_NOTED = {
    "def-122": "no authors but stable arXiv ID 2503.20793 — stable-ID identification",
    "def-308": "LDOCE 1978 — corporate author (Longman) + title + year",
    "def-359": "no authors but stable arXiv ID 1711.06004 — stable-ID identification",
}
SECONDARY_RECEIPT_WORKS = {
    "w-115": "en.wikipedia (ALPAC)", "w-135": "en.wikipedia (Ogden)", "w-137": "en.wikipedia (LDOCE)",
    "w-222": "en.wikipedia", "w-258": "en.wikipedia (Ogden)", "w-275": "en.wikipedia (NSM)",
    "w-284": "en.wikipedia", "w-024": "abebooks bookseller listing", "w-182": "transferlab.ai blog explainer",
    "w-170": "rdrr.io R-doc citation", "w-173": "rdrr.io R-doc citation", "w-023": "research.ibm.com page, not the IEEE primary",
    "w-189": "opentext.ku.edu textbook page", "w-114": "beyondintractability.org essay-about", "w-219": "bcu.ac.uk project page",
}
OVER_CAP_YES = {"w-007", "w-024", "w-036", "w-139", "w-168", "w-170", "w-189"}

rows = [json.loads(l) for l in open(HERE / "occ_rows.jsonl")]


def rate(rs):
    s = sum(1 for r in rs if r["survived"])
    return f"{s}/{len(rs)} = {s/len(rs):.3f}"


def downgraded(r, bad_works):
    return {**r, "survived": r["survived"] and r["work_id"] not in bad_works}


base = rows
s1 = [r for r in rows if r["occ_id"] not in INELIGIBLE_OCCS]
s2 = [downgraded(r, set(SECONDARY_RECEIPT_WORKS)) for r in rows]
s3 = [downgraded(r, OVER_CAP_YES) for r in rows]
s4 = [downgraded(r, set(SECONDARY_RECEIPT_WORKS) | OVER_CAP_YES) for r in s1]

out = {
    "amended_primary": rate(base),
    "S1_eligibility_filtered": rate(s1),
    "S2_strict_primary_receipts": rate(s2),
    "S3_cap_compliant": rate(s3),
    "S4_combined_floor": rate(s4),
    "ineligible_occurrences": INELIGIBLE_OCCS,
    "eligible_noted": ELIGIBLE_NOTED,
    "secondary_receipt_works": SECONDARY_RECEIPT_WORKS,
    "over_cap_exists_yes_works": sorted(OVER_CAP_YES),
}
(HERE / "p3_sensitivity.json").write_text(json.dumps(out, indent=2))
for k in ("amended_primary", "S1_eligibility_filtered", "S2_strict_primary_receipts", "S3_cap_compliant", "S4_combined_floor"):
    print(f"{k}: {out[k]}")
