#!/usr/bin/env python3
"""make_verify_batches.py — P3: shard works.jsonl into verification batch briefs.

Each batch file contains the full protocol + the batch's works with their
occurrences' attributed claims. Batches of ~12 works, deterministic order
(work_id sort). Output: batches/batch-<k>.md
"""
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
BATCH_SIZE = 12

works = [json.loads(l) for l in (HERE / "works.jsonl").read_text().splitlines() if l.strip()]
occs = [json.loads(l) for l in (HERE / "ledger.jsonl").read_text().splitlines() if l.strip()]

# AMENDMENT M2: verify only the seeded sample's induced works, and list only
# sampled occurrences under each (sample-occ-ids.json).
sample = json.loads((HERE / "sample-occ-ids.json").read_text())
sample_occ_ids = set(sample["occ_ids"])
sample_work_ids = set(sample["induced_work_ids"])
works = [w for w in works if w["work_id"] in sample_work_ids]
occs = [o for o in occs if o["occ_id"] in sample_occ_ids]

occ_by_work = defaultdict(list)
for o in occs:
    occ_by_work[o["work_id"]].append(o)

works.sort(key=lambda w: w["work_id"])
outdir = HERE / "batches"
outdir.mkdir(exist_ok=True)

PROTOCOL = """You are verifying model-proposed citations against primary sources for a provenance study. For EACH work below, follow this frozen protocol:

1. Locate the primary source: up to 3 search queries (WebSearch) + up to 2 page fetches per work. Fetch pages with the BARE `safefetch <url>` command via Bash — never WebFetch, never curl. If the natural page is unreachable, try the Wayback Machine (https://web.archive.org/web/2024/<url>). Then stop.
2. Grade three facets:
   - exists: "yes" | "no" | "unverifiable" — does a published work matching this citation exist?
   - biblio: "full" (authors + venue + year all match; year exactly) | "minor" (year off by 1, OR journal-vs-proceedings variant, OR subtitle truncation — note which) | "major" (wrong venue, wrong authors, or year off by more than 1) | null if exists != yes
   - per-occurrence claim_support: "supported" (the attributed claim is plausibly present at abstract/title level of the located primary) | "not_locatable" (work exists but the claim is not visible at abstract/title level) | "contradicted" (the abstract/title actively contradicts the attribution) — one verdict per occurrence listed under the work.
3. Receipts REQUIRED: for every exists=yes verdict, record the URL you fetched and a VERBATIM snippet (title line or abstract sentence) from the fetched page that supports your biblio + claim verdicts. No snippet = downgrade to unverifiable.
4. Do NOT judge whether the work truly "owns" the concept — only existence, bibliography, and whether the attributed claim is plausibly in it.

Append your verdicts as JSON lines to the output file given below, one line per work, schema:
{"work_id": "...", "exists": "...", "biblio": "...", "biblio_notes": "...", "primary_url": "...", "evidence_snippet": "...", "occurrences": [{"occ_id": "...", "claim_support": "...", "note": "..."}], "queries_used": N, "fetches_used": N}

Work through the list IN ORDER, writing each verdict line as you complete it (append as you go — do not batch at the end). Your final report: counts by exists/biblio grade + the output file path.
"""

for k in range(0, len(works), BATCH_SIZE):
    batch = works[k // BATCH_SIZE * BATCH_SIZE : k + BATCH_SIZE]
    idx = k // BATCH_SIZE
    lines = [PROTOCOL, f"\nOUTPUT FILE: {HERE}/verify-batch-{idx}.jsonl\n", "\n## Works to verify\n"]
    for w in batch:
        lines.append(f"\n### {w['work_id']}\n")
        lines.append(json.dumps({key: w[key] for key in ("first_author", "authors", "year", "title", "venue", "urls")}, indent=1) + "\n")
        lines.append("Occurrences (verify each attributed claim):\n")
        for o in occ_by_work[w["work_id"]]:
            lines.append(f"- occ_id {o['occ_id']}: attributed_claim = {json.dumps(o['attributed_claim'])} (hedged={o.get('hedged')}); source quote: {json.dumps(o['quote'][:300])}\n")
    (outdir / f"batch-{idx}.md").write_text("".join(lines))
    print(f"batch-{idx}.md: {len(batch)} works, {sum(len(occ_by_work[w['work_id']]) for w in batch)} occurrences")
print(f"total: {len(works)} works, {len(occs)} occurrences, {len(range(0, len(works), BATCH_SIZE))} batches")
