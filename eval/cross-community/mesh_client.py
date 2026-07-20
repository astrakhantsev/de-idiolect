#!/usr/bin/env python3
"""Thin, disk-cached, rate-limited clients for the three open APIs this cell uses.

- NCBI E-utilities (esearch / efetch / esummary) over the `mesh` and `pubmed` dbs
  -> candidate synonym pairs (MeSH descriptor + Entry Terms) and real title+abstract docs.
- OpenAlex (`works/pmid:...` -> `referenced_works`) -> the backward-citation walk and
  the reconciliation (citation-disjointness) check.

Everything is stdlib urllib (no `requests` dependency), polite-throttled, and cached to
`.http-cache/` keyed by URL so re-runs are offline and byte-stable. Delete the cache dir
to force a refetch.

Rate limits respected: E-utilities <=3 req/s without an API key; OpenAlex is generous but
we still throttle and send a mailto UA (the "polite pool").
"""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / ".http-cache"
CACHE.mkdir(exist_ok=True)

MAILTO = "terms@astrakhantsev.com"
UA = f"minelit-flf-epistack/0.1 (mailto:{MAILTO})"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OPENALEX = "https://api.openalex.org"

# polite throttle: seconds between requests per host family
_LAST = {"eutils": 0.0, "openalex": 0.0}
_MIN_GAP = {"eutils": 0.34, "openalex": 0.11}


def _throttle(host: str) -> None:
    # NOTE: uses a monotonic-ish wall clock only to space requests; never for logic/seeds.
    gap = _MIN_GAP[host]
    dt = time.time() - _LAST[host]
    if dt < gap:
        time.sleep(gap - dt)
    _LAST[host] = time.time()


def _cache_path(url: str) -> Path:
    h = hashlib.sha256(url.encode()).hexdigest()[:24]
    return CACHE / f"{h}.txt"


def _get(url: str, host: str, use_cache: bool = True) -> str:
    cp = _cache_path(url)
    if use_cache and cp.exists():
        return cp.read_text(encoding="utf-8")
    _throttle(host)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last_err = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                body = r.read().decode("utf-8", "replace")
            cp.write_text(body, encoding="utf-8")
            return body
        except Exception as e:  # noqa: BLE001 - transient network; retry with backoff
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after retries: {url}\n  {type(last_err).__name__}: {last_err}")


# ---------------------------------------------------------------- E-utilities

def esearch(db: str, term: str, retmax: int = 20) -> list[str]:
    """Return a list of UIDs for a term in a db (mesh or pubmed)."""
    q = urllib.parse.urlencode({"db": db, "term": term, "retmode": "json",
                                "retmax": retmax, "email": MAILTO, "tool": "minelit"})
    body = _get(f"{EUTILS}/esearch.fcgi?{q}", "eutils")
    return json.loads(body)["esearchresult"].get("idlist", [])


def mesh_record(uid: str) -> str:
    """Full ASCII MeSH record for a descriptor UID (contains Entry Terms)."""
    q = urllib.parse.urlencode({"db": "mesh", "id": uid, "rettype": "full",
                                "retmode": "text", "email": MAILTO, "tool": "minelit"})
    return _get(f"{EUTILS}/efetch.fcgi?{q}", "eutils")


_ENTRY_RE = re.compile(r"^Entry Terms?:\s*$", re.M)


def parse_mesh(record: str) -> dict:
    """Parse the ASCII MeSH `efetch` record into {descriptor, entry_terms, scope_note}.

    The text format looks like:
        1: Myocardial Infarction
        ...
        Entry Terms:
                    Cardiovascular Stroke
                    Heart Attack
                    ...
        ...
    """
    lines = record.splitlines()
    descriptor = ""
    # first line is like "1: Myocardial Infarction"
    for ln in lines:
        m = re.match(r"^\d+:\s+(.*)$", ln)
        if m:
            descriptor = m.group(1).strip()
            break
    scope = ""
    for i, ln in enumerate(lines):
        if ln.strip().startswith("Scope Note:"):
            # scope note may spill onto following indented lines
            first = ln.split("Scope Note:", 1)[1].strip()
            buf = [first] if first else []
            for j in range(i + 1, len(lines)):
                if lines[j].startswith((" ", "\t")) and lines[j].strip():
                    buf.append(lines[j].strip())
                else:
                    break
            scope = " ".join(buf).strip()
            break
    entry_terms: list[str] = []
    m = _ENTRY_RE.search(record)
    if m:
        # Entry terms are a CONTIGUOUS block of indented lines right after the header.
        # The block is terminated by the first blank line; a following indented tree
        # hierarchy ("    All MeSH Categories ...") must NOT be swallowed.
        tail = record[m.end():].splitlines()
        started = False
        for ln in tail:
            if ln.startswith((" ", "\t")) and ln.strip():
                entry_terms.append(ln.strip())
                started = True
            elif started:
                # first blank / non-indented line AFTER the block ends it -> do not
                # swallow the indented tree hierarchy that follows a separating blank line
                break
            # else: leading blank right after the "Entry Terms:" header -> keep skipping
    return {"uid": "", "descriptor": descriptor, "entry_terms": entry_terms, "scope_note": scope}


def _seed_tokens(s: str) -> set[str]:
    return {w for w in re.split(r"[^a-z0-9]+", s.lower()) if len(w) > 2}


def mesh_concept(term: str, topk: int = 6) -> dict | None:
    """esearch a term in the mesh db, then pick the descriptor that ACTUALLY matches the
    seed (esearch relevance can rank a related descriptor first, e.g. niacin->Tryptophan).

    Match rule: the descriptor or one of its entry terms must contain all of the seed's
    content words (order-free). If nothing among the top-k matches, return None (reject the
    seed) rather than silently returning an off-concept descriptor.
    """
    uids = esearch("mesh", term, retmax=topk)
    if not uids:
        return None
    seed = _seed_tokens(term)
    best = None
    for uid in uids:
        rec = mesh_record(uid)
        parsed = parse_mesh(rec)
        parsed["uid"] = uid
        names = [parsed["descriptor"], *parsed["entry_terms"]]
        # exact-ish concept match: some name contains every seed content word
        for nm in names:
            toks = _seed_tokens(nm)
            if seed and seed <= toks:
                return parsed
        if best is None:
            best = parsed  # fallback to top hit only if no exact match anywhere
    # No top-k record contained the full seed phrase -> treat as no clean concept match.
    return None


def pubmed_search(term: str, retmax: int = 30, field: str = "tiab", phrase: bool = True) -> list[str]:
    """PMIDs whose title/abstract match `term` (field-restricted to avoid MeSH auto-mapping).

    Using [tiab] deliberately: it matches the literal surface text, NOT PubMed's MeSH
    auto-translation, so a `docs_A` search on term A does not silently pull in term-B docs via
    the shared MeSH heading. That is what keeps the two community corpora separable.

    phrase=True quotes the term (exact phrase, for the A/B community terms). phrase=False ANDs
    the words (for distractor topic queries, which are not exact phrases in any abstract).
    """
    q = f'"{term}"[{field}]' if phrase else " AND ".join(f"{w}[{field}]" for w in term.split())
    return esearch("pubmed", q, retmax=retmax)


def pubmed_fetch(pmids: list[str]) -> list[dict]:
    """Fetch title+abstract for a batch of PMIDs. Returns [{pmid,title,abstract}]."""
    if not pmids:
        return []
    q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids), "retmode": "xml",
                                "email": MAILTO, "tool": "minelit"})
    body = _get(f"{EUTILS}/efetch.fcgi?{q}", "eutils")
    out = []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return out
    for art in root.findall(".//PubmedArticle"):
        pmid = (art.findtext(".//PMID") or "").strip()
        title = "".join(art.find(".//ArticleTitle").itertext()).strip() if art.find(".//ArticleTitle") is not None else ""
        abst_parts = []
        for ab in art.findall(".//Abstract/AbstractText"):
            abst_parts.append("".join(ab.itertext()).strip())
        abstract = " ".join(p for p in abst_parts if p).strip()
        out.append({"pmid": pmid, "title": title, "abstract": abstract})
    return out


# ---------------------------------------------------------------- OpenAlex

def openalex_by_pmid(pmid: str) -> dict | None:
    """Fetch an OpenAlex work by PMID. Returns the raw JSON (or None if not found)."""
    url = f"{OPENALEX}/works/pmid:{pmid}?mailto={MAILTO}"
    try:
        body = _get(url, "openalex")
    except RuntimeError:
        return None
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def referenced_works(pmid: str) -> list[str]:
    """OpenAlex IDs of the works a paper (by PMID) cites (its backward citations)."""
    w = openalex_by_pmid(pmid)
    if not w:
        return []
    return w.get("referenced_works", []) or []


def openalex_id_by_pmid(pmid: str) -> str | None:
    w = openalex_by_pmid(pmid)
    return w.get("id") if w else None


if __name__ == "__main__":
    # smoke test
    import sys
    c = mesh_concept(sys.argv[1] if len(sys.argv) > 1 else "myocardial infarction")
    print(json.dumps({k: v for k, v in c.items() if k != "scope_note"}, indent=2) if c else "NOT FOUND")
    if c:
        print("scope:", (c["scope_note"] or "")[:200])
