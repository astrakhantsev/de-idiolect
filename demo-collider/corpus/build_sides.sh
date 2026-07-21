#!/usr/bin/env bash
# build_sides.sh — assemble the three per-side working-corpus files for the
# collider demo from cleaned prose slices of the raw fetched papers.
#
# The side files are the WORKING corpus the tools run over (scan/term-check).
# They are gitignored (_work/): they carry substantial third-party paper prose.
# Committed instead are the manifest, this script + clean_section.py, and the
# tools' own paragraph-level excerpt receipts. Each slice is tagged with its
# source paper + section so demo-collider/corpus/sides.md can record the map.
#
# Sides (argument-type within the LHC safety case, NOT one paper each):
#   A theory  — black-hole production, Hawking/decay, accretion MECHANISM
#   B bounds  — cosmic-ray survival + white-dwarf + neutron-star empirical bounds
#   C critique— Plaga (physics objection) + Ord/Hillerbrand/Sandberg (methodology)
set -euo pipefail
cd "$(dirname "$0")"
RAW=_work/raw
OUT=_work
CLEAN="python3 clean_section.py"

GM="$RAW/0806.3381-giddings-mangano.md"
LSAG="$RAW/0806.3414-lsag.md"
PLAGA="$RAW/0808.1415-plaga.md"
ORD="$RAW/0810.5515-ord-hillerbrand-sandberg.md"

slice() { # file start end label -> cleaned slice with a provenance header
  local f="$1" s="$2" e="$3" label="$4"
  printf '\n\n===== [%s] =====\n\n' "$label"
  $CLEAN "$f" --start-line "$s" --end-line "$e" 2>/dev/null
}

# ---- Side A: theory (production, Hawking/decay, accretion mechanism) ----
{
  echo "# Side A — theory-side sections of the LHC black-hole safety case"
  echo "# WORKING CORPUS (gitignored). Cleaned prose slices; provenance tags inline."
  slice "$GM"   185  239 "Giddings & Mangano 2008 (arXiv:0806.3381) sec 2.1 — Instability of microscopic black holes"
  slice "$GM"   558  604 "Giddings & Mangano 2008 sec 4.1 — Accretion basics"
  slice "$GM"   872  980 "Giddings & Mangano 2008 sec 4.3 — Macroscopic (Bondi) accretion in Earth"
  slice "$GM"  1100 1142 "Giddings & Mangano 2008 sec 4.5 — An Eddington limit?"
  slice "$GM"  1196 1330 "Giddings & Mangano 2008 sec 5.1-5.2 — Production kinematics; stopping of neutral black holes"
} > "$OUT/sideA-theory.md"

# ---- Side B: astrophysical bounds (cosmic rays, white dwarfs, neutron stars) ----
{
  echo "# Side B — astrophysical-bounds sections of the LHC black-hole safety case"
  echo "# WORKING CORPUS (gitignored). Cleaned prose slices; provenance tags inline."
  slice "$LSAG"  259  344 "LHC Safety Assessment Group 2008 (arXiv:0806.3414) sec 2 — LHC compared with cosmic-ray collisions (jina PDF render; residual OCR)"
  slice "$GM"    239  295 "Giddings & Mangano 2008 sec 2.2 — Cosmic ray collisions on Earth"
  slice "$GM"   1881 1929 "Giddings & Mangano 2008 sec 7.2 — Bondi accretion (white dwarf)"
  slice "$GM"   1963 2044 "Giddings & Mangano 2008 sec 7.4 — Summary of white dwarf constraints"
  slice "$GM"   2171 2317 "Giddings & Mangano 2008 sec 8.2 — Catalysis of neutron star decay"
} > "$OUT/sideB-bounds.md"

# ---- Side C: critique (physics objection + methodology critique) ----
{
  echo "# Side C — critique-side documents of the LHC black-hole safety case"
  echo "# WORKING CORPUS (gitignored). Cleaned prose slices; provenance tags inline."
  slice "$PLAGA"  29  120 "Plaga 2009 (arXiv:0808.1415 v3) sec 2-4 — metastable mBH / Eddington-limit Hawking risk / white-dwarf gap"
  slice "$ORD"    82  232 "Ord, Hillerbrand & Sandberg 2010 (arXiv:0810.5515) sec 2 — Probability estimates and the chance an argument is flawed"
  slice "$ORD"   479  724 "Ord, Hillerbrand & Sandberg 2010 sec 4 — Applying the analysis to particle-physics risks (RHIC/LHC, cosmic-ray argument)"
} > "$OUT/sideC-critique.md"

# Reproduction self-check. The slices above select prose by LINE NUMBER, which is only
# valid for the specific committed extraction. fetch.sh deliberately re-extracts with
# different tools (pdftotext vs the committed Jina/pandoc renders), so a reflow could
# shift offsets and make a slice select unrelated prose while every command still exits 0.
# Assert each side file contains its expected anchor phrases; warn loudly if not.
check_anchors() { # file  anchor...
  local f="$1"; shift
  for a in "$@"; do
    grep -qiF -- "$a" "$f" || echo "build_sides: WARNING — $(basename "$f") is missing expected anchor '$a'; line-offset slices may have drifted and the corpus may be wrong." >&2
  done
}
check_anchors "$OUT/sideA-theory.md"   "capture radius" "Bondi"      "Eddington"    "evaporate"
check_anchors "$OUT/sideB-bounds.md"   "cosmic"         "white dwarf" "neutron star" "Bondi"
check_anchors "$OUT/sideC-critique.md" "microcanonical" "argument"    "cosmic ray"

# Prose-only variants = the actual TOOL inputs (scan detection + term-check
# excerpting). Strip the assembled `# Side`/`===== [...] =====` scaffolding AND
# the papers' own section headings (`### 2.1 Instability...` etc.) so that
# concept-naming heading lines cannot leak into a term's assembled excerpts.
# Residual owner-vocabulary in the PROSE is handled per-term by the contamination
# check. These *-prose.md files are what the tools point at.
for s in A B C; do
  src=$(ls "$OUT"/side${s}*-*.md | grep -v -- '-prose.md' | head -1)
  dst="$OUT/side${s}-prose.md"
  grep -vE '^\s*#|^\s*=====' "$src" > "$dst"
done

echo "built side files:"
for s in A B C; do
  f=$(ls "$OUT"/side${s}*-*.md | grep -v -- '-prose.md' | head -1)
  p="$OUT/side${s}-prose.md"
  printf '  side %s: %6s words (full)  %6s words (prose-only tool input)\n' "$s" "$(wc -w < "$f")" "$(wc -w < "$p")"
done
