#!/usr/bin/env python3
"""Auditable post-hoc analysis for the constrained-vs-free ablation.

Addresses two Codex-review findings that the main harness left unauditable:
  (#5) the "free-text's margin is bought with owner jargon" mechanism was asserted from a
       throwaway overlap count -> here it is a saved, specified computation, and it ALSO
       reports NON-owner (distractor) overlap so the claim is a contrast, not a bare number;
  (#6) the term-leak audit only checked the full exact headword -> here we screen near-headword
       COMPONENTS and ALIASES (the forms that could improve owner retrieval by restatement).

Tokenization is stated explicitly: lowercase, regex [a-z]{4,} (content words >=4 chars),
set-based (unique types, not token counts), no stop-word list beyond the >=4-char floor.

Usage:  python ablation_analysis.py --defs ablation_definitions.json
"""
from __future__ import annotations
import re, json, argparse, statistics
from pathlib import Path

HERE = Path(__file__).parent

# Near-headword components + known aliases per concept (the forms a weak full-string leak
# check misses but that would directly help owner retrieval by restating the term).
ALIASES = {
    "hyper-responder": ["hyper-responder", "hyperresponder", "hyper responder", "responder",
                        "responders", "responsive", "responsiveness", "hyper-responsive",
                        "hypo-responsive", "hyporesponsive"],
    "apolipoprotein B particle number": ["apolipoprotein", "apob", "apo b", "apo-b",
                                         "particle number", "particle count", "ldl particle",
                                         "lipoprotein particle", "lipoprotein particles"],
    "isocaloric substitution model": ["isocaloric", "iso-caloric", "substitution", "substitute",
                                      "substituted", "substituting", "energy partition",
                                      "energy-partition"],
}


def toks(t: str) -> set[str]:
    return set(re.findall(r"[a-z]{4,}", t.lower()))


def alias_hits(text: str, aliases: list[str]) -> list[str]:
    low = text.lower()
    return [a for a in aliases if a in low]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--defs", default=str(HERE / "ablation_definitions.json"))
    args = ap.parse_args()
    defs = json.loads(Path(args.defs).read_text())
    corpus = json.loads((HERE / "corpus.json").read_text())["documents"]

    print(f"# analysis of {Path(args.defs).name}  (gen_model={defs['model']}, k={defs['k']})\n")
    print(f"{'concept':30s} {'arm':11s} {'owner_ov':>8s} {'distr_ov':>8s} {'alias_hits(mean)':>16s}")
    agg = {}
    for c in defs["concepts"]:
        owner = c["owning_community"]
        owner_words, distr_words = set(), set()
        for doc in corpus:
            if doc["community"] == owner:
                owner_words |= toks(doc["text"])
            elif doc["community"] != owner:
                distr_words |= toks(doc["text"])
        for arm in ("constrained", "free"):
            ov_o, ov_d, al = [], [], []
            for s in c[arm]:
                tk = toks(s["text"])
                ov_o.append(len(tk & owner_words))
                ov_d.append(len(tk & distr_words))
                al.append(len(alias_hits(s["text"], ALIASES[c["term"]])))
            agg.setdefault(arm, {"owner": [], "distr": [], "alias": []})
            agg[arm]["owner"].append(statistics.mean(ov_o))
            agg[arm]["distr"].append(statistics.mean(ov_d))
            agg[arm]["alias"].append(statistics.mean(al))
            print(f"{c['term'][:30]:30s} {arm:11s} {statistics.mean(ov_o):8.1f} "
                  f"{statistics.mean(ov_d):8.1f} {statistics.mean(al):16.1f}")
    print("\n# headline (mean over 3 concepts):")
    for arm in ("constrained", "free"):
        print(f"  {arm:11s} owner_overlap={statistics.mean(agg[arm]['owner']):.1f}  "
              f"distractor_overlap={statistics.mean(agg[arm]['distr']):.1f}  "
              f"alias/component_hits={statistics.mean(agg[arm]['alias']):.2f}")
    # show the actual alias hits per free sample (the leak evidence)
    print("\n# alias/component hits in FREE-TEXT samples (the near-headword forms a full-string check misses):")
    for c in defs["concepts"]:
        hits = sorted({h for s in c["free"] for h in alias_hits(s["text"], ALIASES[c["term"]])})
        print(f"  {c['term']:34s}: {hits if hits else '(none)'}")
    print("\n# same, CONSTRAINED samples:")
    for c in defs["concepts"]:
        hits = sorted({h for s in c["constrained"] for h in alias_hits(s["text"], ALIASES[c["term"]])})
        print(f"  {c['term']:34s}: {hits if hits else '(none)'}")


if __name__ == "__main__":
    main()
