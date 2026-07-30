#!/usr/bin/env python3
"""detect.py — retrospective candidate-term surfacing demo (spec rev 2, section 2.1).

Frozen config, stated in the spec and implemented here verbatim:
  project docs  = flf/ files with filename dates <= 2026-07-12 (manifest + sha256 logged)
  background    = 30_reference/ *.md files (manifest logged)
  vectorizer    = sklearn TfidfVectorizer, ngram_range=(1,3), lowercase=True,
                  default tokenizer, english stopwords, sublinear_tf=True
  candidate set = ngrams with background document frequency == 0
  score         = max tf-idf over project docs; ranking descending, ties lexicographic
  endpoint      = exact string "operating requirement" in top-25

Label carried everywhere: RETROSPECTIVE demo — the vault is not version-controlled,
so pre-discovery file contents cannot be attested (spec rev-1 finding 9).
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer

# The corpora are the author's private research vault, which is not published (and
# is not version-controlled, hence the RETROSPECTIVE label above). These were
# hardcoded absolute paths on one machine, which disclosed the local layout and
# made the script unrunnable by anyone else. Point them at your own directories:
#
#     DEIDIOLECT_PROJECT_DIR=/path/to/project-docs \
#     DEIDIOLECT_BACKGROUND_DIR=/path/to/background-corpus python3 detect.py
#
# Behaviour is unchanged when these resolve to the original inputs. The committed
# run of record (runs/detection.json) is from the author's vault; its
# project-document basenames + sha256 are retained there, and the background
# paths are reduced to opaque ids by scripts/redact_detection_manifest.py.
_VAULT = os.environ.get("DEIDIOLECT_VAULT")
FLF_DIR = Path(os.environ.get(
    "DEIDIOLECT_PROJECT_DIR",
    f"{_VAULT}/10_projects/minelit/flf" if _VAULT else "project-docs"))
BG_DIR = Path(os.environ.get(
    "DEIDIOLECT_BACKGROUND_DIR",
    f"{_VAULT}/30_reference" if _VAULT else "background-corpus"))
OUT = Path(__file__).parent / "runs" / "detection.json"
DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
CUTOFF = "2026-07-12"


def manifest(paths):
    return [
        {"path": str(p), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
        for p in paths
    ]


def main():
    project = sorted(
        p for p in FLF_DIR.glob("*.md")
        if (m := DATE_RE.match(p.name)) and "-".join(m.groups()) <= CUTOFF
    )
    background = sorted(BG_DIR.glob("*.md"))
    if not project:
        sys.exit("no project docs matched the manifest rule")

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
    top25 = cands[:25]

    target = "operating requirement"
    hit = any(target == term or target in term for term, _ in top25)
    result = {
        "label": "RETROSPECTIVE detection demo (era-gating not attestable; non-git vault)",
        "cutoff": CUTOFF,
        "project_manifest": manifest(project),
        "background_manifest": [str(p) for p in background],
        "top25": top25,
        "endpoint_target": target,
        "endpoint_hit_top25": hit,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print(f"detection endpoint ('{target}' in top-25): {'HIT' if hit else 'MISS'}")
    for term, score in top25[:25]:
        print(f"  {score:.4f}  {term}")


if __name__ == "__main__":
    main()
