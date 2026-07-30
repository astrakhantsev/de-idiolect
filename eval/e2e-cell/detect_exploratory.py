#!/usr/bin/env python3
"""detect_exploratory.py — EXPLORATORY variant of detect.py (NOT the frozen endpoint).

Two labeled deviations from the frozen config, run to diagnose the frozen MISS:
  1. excludes 30_reference/novelty-protocol.md from the background (it post-dates the
     discovery and contains the coinage — background contamination);
  2. reports the target's exact rank in the FULL candidate list, not just top-25.
Everything else identical to detect.py. Output: runs/detection_exploratory.json.
"""
import hashlib
import json
import os
import re
from pathlib import Path

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

# Same corpora as detect.py, same reason they are parameterized rather than
# hardcoded: the inputs are a private vault, and absolute paths disclosed the local
# layout while making this unrunnable elsewhere. See detect.py for the variables.
_VAULT = os.environ.get("DEIDIOLECT_VAULT")
FLF_DIR = Path(os.environ.get(
    "DEIDIOLECT_PROJECT_DIR",
    f"{_VAULT}/10_projects/minelit/flf" if _VAULT else "project-docs"))
BG_DIR = Path(os.environ.get(
    "DEIDIOLECT_BACKGROUND_DIR",
    f"{_VAULT}/30_reference" if _VAULT else "background-corpus"))
EXCLUDED_BG = {"novelty-protocol.md"}
OUT = Path(__file__).parent / "runs" / "detection_exploratory.json"
DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
CUTOFF = "2026-07-12"
TARGET = "operating requirement"


def main():
    project = sorted(
        p for p in FLF_DIR.glob("*.md")
        if (m := DATE_RE.match(p.name)) and "-".join(m.groups()) <= CUTOFF
    )
    background = sorted(p for p in BG_DIR.glob("*.md") if p.name not in EXCLUDED_BG)

    proj_texts = [p.read_text(errors="replace") for p in project]
    bg_texts = [p.read_text(errors="replace") for p in background]

    vec = TfidfVectorizer(ngram_range=(1, 3), lowercase=True,
                          stop_words="english", sublinear_tf=True)
    mat = vec.fit_transform(proj_texts + bg_texts)
    vocab = vec.get_feature_names_out()
    n_proj = len(proj_texts)
    bg_df = (mat[n_proj:] > 0).sum(axis=0).A1
    proj_max = mat[:n_proj].max(axis=0).toarray().ravel()

    cands = [(vocab[i], float(proj_max[i]))
             for i in range(len(vocab)) if bg_df[i] == 0 and proj_max[i] > 0]
    cands.sort(key=lambda t: (-t[1], t[0]))

    exact_rank = next((r for r, (t, _) in enumerate(cands, 1) if t == TARGET), None)
    contains_rank = next((r for r, (t, _) in enumerate(cands, 1) if TARGET in t), None)

    result = {
        "label": "EXPLORATORY — not the frozen endpoint; bg contamination excluded",
        "excluded_background": sorted(EXCLUDED_BG),
        "sklearn_version": sklearn.__version__,
        "n_candidates": len(cands),
        "target": TARGET,
        "exact_ngram_rank": exact_rank,
        "first_containing_ngram_rank": contains_rank,
        "top25": cands[:25],
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(f"exploratory: exact-ngram rank = {exact_rank}; "
          f"first containing ngram rank = {contains_rank}; "
          f"candidates = {len(cands)}")


if __name__ == "__main__":
    main()
