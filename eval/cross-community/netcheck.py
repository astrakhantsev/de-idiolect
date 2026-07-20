#!/usr/bin/env python3
"""Connectivity probe for the three open APIs this cell depends on.

Run before anything else: if any of these fail, the corpus cannot be built from
real records and the cell must not be faked with synthetic documents.
"""
from __future__ import annotations
import json
import urllib.request
import urllib.error

UA = "minelit-flf-epistack/0.1 (mailto:terms@astrakhantsev.com)"

PROBES = [
    ("MeSH E-utilities esearch",
     "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
     "?db=mesh&term=myocardial+infarction&retmode=json&retmax=2"),
    ("PubMed E-utilities esearch",
     "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
     "?db=pubmed&term=hyperlipidemia&retmode=json&retmax=2"),
    ("OpenAlex work",
     "https://api.openalex.org/works/W2741809807"),
]


def probe(name: str, url: str) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read(400).decode("utf-8", "replace")
        print(f"[OK  ] {name}: HTTP {r.status} :: {body[:180]!r}")
    except Exception as e:  # noqa: BLE001 - probe reports whatever it hits
        print(f"[FAIL] {name}: {type(e).__name__}: {e}")


if __name__ == "__main__":
    for n, u in PROBES:
        probe(n, u)
