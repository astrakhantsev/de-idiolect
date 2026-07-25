#!/usr/bin/env python3
"""Mechanical corpus splitter for the TEST run (restores v0.2's split, which the v0.8
controller rewrite dropped): parses <<<DOC n>>> blocks from a generation output into
corpora/<side>/NN.md and writes the sha256 manifest (exactly the docs present).
Usage: split_corpus.py <side> <raw_generation_output>"""
import hashlib, json, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
side, raw = sys.argv[1], sys.argv[2]
txt = Path(raw).read_text()
parts = re.split(r"<<<DOC (\d+)>>>", txt)
docs = {}
d = BASE / f"corpora/{side}"
d.mkdir(parents=True, exist_ok=True)
for i in range(1, len(parts) - 1, 2):
    nn, body = parts[i].zfill(2), parts[i + 1].strip()
    (d / f"{nn}.md").write_text(body + "\n")
    docs[nn] = hashlib.sha256(body.encode()).hexdigest()
json.dump(docs, open(d / "manifest.json", "w"), indent=1)
print(f"{side}: {len(docs)} docs split, manifest written")
if len(docs) != 11:
    sys.exit(f"RUN-SCOPED FAULT: expected 11 docs for side {side}, got {len(docs)}")
