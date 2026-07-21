#!/usr/bin/env python3
r"""clean_section.py — extract and lightly clean a prose slice from a raw fetched
paper for the collider demo working corpus.

The raw files come from three routes with different artifact profiles:
  - ar5iv -> pandoc gfm (G&M, Plaga): LaTeXML `<span class="ltx_...">` tags, inline
    `$...$`/`\(...\)` math, occasional MathML.
  - jina PDF-render (LSAG): OCR spacing artifacts ("dwar fs", "200 3").
  - pdftotext -layout (Ord): hard-wrapped columns, page numbers, hyphenation.

This does NOT try to be perfect — the goal is readable prose for term detection and
paragraph-level excerpting, with math and tag noise removed so it does not pollute
keyness/detection. Full fidelity lives in the gitignored raw files; the manifest
records provenance.

Usage:
  clean_section.py RAWFILE [--start-re REGEX] [--end-re REGEX] [--start-line N] [--end-line N]
  # prints cleaned text to stdout; select a slice by regex anchors or line numbers.
"""
import argparse, re, sys

def demojibake(text: str) -> str:
    # common CP1252-as-UTF8 artifacts from the jina PDF render (LSAG) and pdftotext.
    repl = {
        'â€™': "'", 'â€˜': "'", 'â€œ': '"', 'â€\x9d': '"', 'â€': '"',
        'â€”': '—', 'â€“': '–', 'â€¢': '•', 'â€¦': '…',
        'Â\xa0': ' ', 'Â ': ' ', '\xa0': ' ', 'Â': '',
        'Î¼': 'μ', 'â‰\x88': '≈', 'Ã—': '×', 'â†’': '→',
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    # jina/pdftotext OCR: rejoin spaced hyphens ("Cosmic -Ray" -> "Cosmic-Ray").
    text = re.sub(r'([A-Za-z]) -([A-Za-z])', r'\1-\2', text)
    return text

def strip_markup(text: str) -> str:
    # drop LaTeXML/HTML span & tag wrappers, keep inner text
    text = re.sub(r'</?span[^>]*>', '', text)
    text = re.sub(r'</?div[^>]*>', '', text)
    # MathML blocks -> drop entirely (they are rendered formulae, noise for prose)
    text = re.sub(r'<math[^>]*>.*?</math>', ' ', text, flags=re.DOTALL)
    # any other stray html tag
    text = re.sub(r'<[^>]+>', '', text)
    # html entities commonly seen
    for a, b in [('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&nbsp;', ' '),
                 ('&#39;', "'"), ('&quot;', '"')]:
        text = text.replace(a, b)
    return text

def collapse(text: str) -> str:
    out = []
    for line in text.splitlines():
        line = line.rstrip()
        # drop markdown table rows: in this corpus these are rendered display
        # equations / numbered-formula tables, pure noise for prose detection.
        if re.match(r'^\s*\|', line):
            continue
        # drop pandoc pipe-table separator / alignment lines
        if re.match(r'^\s*[-:|\s]+$', line) and '|' in line:
            continue
        # collapse runs of spaces (fixes pdftotext column gaps + jina spacing)
        line = re.sub(r'[ \t]{2,}', ' ', line)
        out.append(line)
    text = '\n'.join(out)
    # collapse 3+ blank lines to one
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('rawfile')
    ap.add_argument('--start-re')
    ap.add_argument('--end-re')
    ap.add_argument('--start-line', type=int)
    ap.add_argument('--end-line', type=int)
    a = ap.parse_args()
    lines = open(a.rawfile, encoding='utf-8', errors='replace').read().splitlines()

    lo, hi = 0, len(lines)
    if a.start_line: lo = a.start_line - 1
    if a.end_line: hi = a.end_line
    if a.start_re:
        for i, ln in enumerate(lines):
            if re.search(a.start_re, ln): lo = i; break
    if a.end_re:
        for i in range(lo + 1, len(lines)):
            if re.search(a.end_re, lines[i]): hi = i; break
    chunk = '\n'.join(lines[lo:hi])
    sys.stdout.write(collapse(strip_markup(demojibake(chunk))))

if __name__ == '__main__':
    main()
