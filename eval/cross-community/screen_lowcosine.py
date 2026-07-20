#!/usr/bin/env python3
"""Memorization screen on the LOW-cosine cross-vocabulary pairs — the sweet-spot test.

A valid second cell needs a pair that is BOTH embedder-hard (low bge cross-cosine, so raw-term
retrieval fails and the tool has room) AND opaque (a frontier model does not already bridge the
two names, so the tool is non-redundant). The cross-cosine scan found low-cosine cross-vocabulary
pairs; this screens them for opacity.

For each selected pair (a, b): probe BOTH terms with the Step-0 memorization prompt and use the
STEM-based leak check (catches inflections — the fix for the whole-token over-count). A direction
is a NON-BRIDGE if the model, given one term, does not surface the other. A pair is a SWEET-SPOT
candidate if at least one direction is a non-bridge with a DESCRIPTIVE (non-abbreviation) probe
term — i.e. the tool could genuinely help someone holding that name reach the other community.

  python screen_lowcosine.py --max-concepts 18
Reads cross_cosine_ols_proxy.json, writes lowcosine_screen.json.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from llm_backend_xc import claude
from run_cell import _term_root, _leaks
from select_pairs import SCREEN_PROMPT

HERE = Path(__file__).parent
LOW = 0.65


def _is_abbrev(term: str) -> bool:
    t = term.strip()
    return len(t) <= 5 and t.replace(".", "").isalpha() and t.upper() == t


def _probe(term: str, other: str, model: str) -> dict:
    resp = claude(SCREEN_PROMPT.format(term=term), model=model, timeout=120)
    if not resp:
        return {"term": term, "response": None, "bridged": None, "error": True}
    bridged = _leaks(resp, other)  # stem-based: does the model surface the other name's root?
    return {"term": term, "is_abbrev": _is_abbrev(term), "response": resp,
            "other_root": _term_root(other), "bridged": bridged}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--max-concepts", type=int, default=18)
    ap.add_argument("--out", default=str(HERE / "lowcosine_screen.json"))
    args = ap.parse_args()

    data = json.loads((HERE / "cross_cosine_ols_proxy.json").read_text())
    low = [p for p in data["pairs"] if p["cross_cosine"] < LOW]
    # dedupe: lowest-cosine pair per seed concept (diversity over redundant same-concept variants)
    by_concept: dict[str, dict] = {}
    for p in sorted(low, key=lambda r: r["cross_cosine"]):
        by_concept.setdefault(p["seed_concept"], p)
    selected = sorted(by_concept.values(), key=lambda r: r["cross_cosine"])[: args.max_concepts]
    print(f"screening {len(selected)} low-cosine pairs (1 per concept, lowest cosine each)\n")

    results = []
    for i, p in enumerate(selected, 1):
        a, b = p["term_a"], p["term_b"]
        pa = _probe(a, b, args.model)
        pb = _probe(b, a, args.model)
        # non-bridge in a direction where the probed term is descriptive (not a bare abbreviation)
        nb_a = pa.get("bridged") is False and not pa.get("is_abbrev")
        nb_b = pb.get("bridged") is False and not pb.get("is_abbrev")
        sweet = nb_a or nb_b
        verdict = "SWEET-SPOT?" if sweet else "void (both bridge / abbrev-only)"
        results.append({**p, "probe_a": pa, "probe_b": pb,
                        "nonbridge_a_descriptive": nb_a, "nonbridge_b_descriptive": nb_b,
                        "verdict": verdict})
        print(f"[{i:2d}/{len(selected)}] cos={p['cross_cosine']:.3f}  {a[:30]!r} <-> {b[:30]!r}")
        print(f"      probe({a[:24]!r}) bridges->{pb and pa['bridged']}   "
              f"probe({b[:24]!r}) bridges->{pb['bridged']}   => {verdict}")

    (Path(args.out)).write_text(json.dumps({"screen_model": args.model, "low_threshold": LOW,
                                            "n_screened": len(results), "results": results}, indent=2))
    sweet = [r for r in results if r["verdict"].startswith("SWEET")]
    print(f"\n==== {len(sweet)} of {len(results)} low-cosine pairs are SWEET-SPOT candidates "
          f"(low cosine AND a descriptive non-bridge direction) ====")
    for r in sweet:
        d = "a" if r["nonbridge_a_descriptive"] else "b"
        term = r["term_a"] if d == "a" else r["term_b"]
        other = r["term_b"] if d == "a" else r["term_a"]
        print(f"  cos={r['cross_cosine']:.3f}  opaque side={term!r}  -> does not reach {other!r}")
    print(f"\n[done] -> {args.out}")


if __name__ == "__main__":
    main()
