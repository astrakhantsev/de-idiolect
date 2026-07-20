#!/usr/bin/env python3
"""Mechanical rubric metrics for socialization-MVP draws: word_count + hedge_density.
Hedge lexicon is FROZEN per spec §3. Multi-word markers matched as phrases.
Usage: score-metrics.py <file> [<file> ...]
"""
import re, sys, os

HEDGES = [
    "might", "may", "possibly", "perhaps", "unclear", "uncertain",
    "i think", "seems", "appears", "likely", "unsure", "cannot confirm",
    "not certain", "tentative", "hard to say",
]

def analyze(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    low = text.lower()
    # word count: whitespace-delimited tokens on raw text
    words = len(text.split())
    counts = {}
    total_h = 0
    for h in HEDGES:
        # word-boundary match; \b works for phrases too at the ends
        n = len(re.findall(r"\b" + re.escape(h) + r"\b", low))
        counts[h] = n
        total_h += n
    dens = (total_h / words * 100) if words else 0.0
    return words, total_h, dens, counts

def main():
    print(f"{'file':55} {'words':>6} {'hedges':>6} {'per100w':>8}")
    for p in sys.argv[1:]:
        w, h, d, c = analyze(p)
        name = os.path.basename(p)
        print(f"{name:55} {w:6d} {h:6d} {d:8.2f}")
        nz = {k: v for k, v in c.items() if v}
        if nz:
            print("    " + ", ".join(f"{k}={v}" for k, v in sorted(nz.items(), key=lambda x: -x[1])))

if __name__ == "__main__":
    main()
