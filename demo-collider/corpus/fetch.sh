#!/usr/bin/env bash
# fetch.sh — reproduce the collider-demo local working corpus under _work/raw/.
#
# The full third-party paper texts are NOT committed (copyright boundary — see
# ../README.md). This script re-fetches them from arXiv and re-extracts text, then
# calls build_sides.sh to assemble the per-side working files the tools run over.
#
# PROVENANCE NOTE. The committed corpus was fetched 2026-07-20 via the author's
# `safefetch` wrapper (a defuddle/Jina extractor with an injection scanner). That
# wrapper is not public, so this script uses the same SOURCE URLs with standard
# tools (curl + pandoc + pdftotext). Text extraction is tool-dependent, so the
# re-extracted bytes may differ from the manifest's sha256 (a dated snapshot); the
# stable identity is the arXiv ID + version. Two 2008 papers have no arXiv HTML
# rendition, so they go PDF->text.
#
# Requires: curl, and (for HTML papers) pandoc, and (for PDF papers) pdftotext.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p _work/raw
cd _work/raw

need() { command -v "$1" >/dev/null 2>&1 || { echo "missing tool: $1" >&2; exit 2; }; }
need curl

html_to_md() { # arxiv_id outfile  (via ar5iv -> pandoc gfm)
  need pandoc
  # -f makes curl exit nonzero on a 4xx/5xx (so an error page is never piped into the
  # corpus); pipefail (set at top) propagates that through pandoc.
  curl -fsSL "https://ar5iv.labs.arxiv.org/html/$1" \
    | pandoc -f html -t gfm --wrap=none -o "$2"
  local w; w="$(wc -w < "$2")"
  [ "$w" -ge 2000 ] || { echo "  WARNING: $2 has only $w words — source may be unavailable/changed" >&2; }
  echo "  wrote $2 ($w words) from ar5iv"
}
pdf_to_text() { # arxiv_id outfile  (via arxiv pdf -> pdftotext -layout)
  need pdftotext
  curl -fsSL -A "Mozilla/5.0" "https://arxiv.org/pdf/$1" -o "_$1.pdf"
  pdftotext -layout "_$1.pdf" "$2"
  rm -f "_$1.pdf"
  local w; w="$(wc -w < "$2")"
  [ "$w" -ge 2000 ] || { echo "  WARNING: $2 has only $w words — source may be unavailable/changed" >&2; }
  echo "  wrote $2 ($w words) from arxiv pdf"
}

echo "1/4 LSAG 0806.3414 (no HTML rendition; PDF)"
pdf_to_text 0806.3414 0806.3414-lsag.md
echo "2/4 Giddings & Mangano 0806.3381 (ar5iv HTML)"
html_to_md 0806.3381 0806.3381-giddings-mangano.md
echo "3/4 Plaga 0808.1415 v3 (ar5iv HTML)"
html_to_md 0808.1415 0808.1415-plaga.md
echo "4/4 Ord/Hillerbrand/Sandberg 0810.5515 (PDF)"
pdf_to_text 0810.5515 0810.5515-ord-hillerbrand-sandberg.md

echo "assembling per-side working files..."
cd ..; cd ..
bash build_sides.sh
echo "done. NOTE: the committed LSAG corpus used a Jina PDF render (cleaner OCR)"
echo "than pdftotext; re-extraction differences are expected and harmless for the"
echo "demonstration (see manifest.md provenance note)."
