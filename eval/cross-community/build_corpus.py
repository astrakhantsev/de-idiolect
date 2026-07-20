#!/usr/bin/env python3
"""Step 1 - corpus construction + the two reconciliation signals (guards 2, 4b).

For a chosen A<->B pair, build C = docs_A u docs_B u distractors from REAL PubMed records,
and compute two independent "is this seam already reconciled?" signals so a redundant pair is
discarded before any retrieval number is produced:

  Guard 2  (citation reconciliation)  : do docs_A and docs_B cite each other / share
             references?  Measured via OpenAlex backward citations. Disjoint => unreconciled
             => the tool is non-redundant on this pair.
  Guard 4b (lexical reconciliation)   : how often does term B occur in the term-A search set
             (and vice versa)?  We MEASURE and REPORT this co-mention rate rather than silently
             dropping the offending docs -- per the design note, the rate is itself the signal:
               low  => genuinely separable communities (tool-relevant),
               high => the communities already lexically bridge each other (tool LESS
                       applicable; an honest downgrade, not something to hide).
             Every doc is TAGGED `contains_other_term` so the retrieval step (run_cell.py) can
             report cross-community recall BOTH inclusive (nothing dropped) and clean (cross-term
             docs removed). The dangerous leak is term A appearing in the *target* docs_B: it lets
             the raw_term_A floor reach B by surface match and fakes lift -- tagging makes it visible.

  python build_corpus.py --pair-index 0            # use candidate_pairs.json[pairs][0]
  python build_corpus.py --a "Product-Limit Method" --b "Kaplan-Meier Estimate" --seed "..."
  python build_corpus.py ... --n-seed 10 --n-distract 8 --walk    # +backward-citation walk

Writes corpus.json (frozen, with per-doc provenance + tags) and prints the guard verdicts.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import mesh_client as mc

HERE = Path(__file__).parent
CAND = HERE / "candidate_pairs.json"
OUT = HERE / "corpus.json"

# Off-topic distractor topics (unrelated biomedical subfields that reliably have PubMed
# abstracts) so retrieval isn't trivially easy, mirroring the eggs corpus's distractor
# community E. Fixed list -> deterministic. Searched as AND-of-words (phrase=False).
DISTRACTOR_QUERIES = [
    "malaria transmission mosquito", "Alzheimer amyloid plaque",
    "antibiotic resistance Escherichia coli", "diabetic retinopathy screening",
    "melanoma immunotherapy checkpoint", "Parkinson dopamine neuron",
    "asthma inhaler corticosteroid", "osteoporosis bone density",
    "hepatitis antiviral treatment", "influenza vaccine efficacy",
]


def _contains_term(text: str, term: str) -> int:
    """Number of times a term (as a whole-phrase, case-insensitive) occurs in text.

    Uses word boundaries on the whole phrase so 'PET' does not match 'competition'. Hyphens and
    runs of whitespace in the term are treated flexibly (so 'Product-Limit' matches 'product limit').
    """
    parts = [re.escape(w) for w in re.split(r"[\s\-]+", term.strip()) if w]
    if not parts:
        return 0
    pat = r"\b" + r"[\s\-]+".join(parts) + r"\b"
    return len(re.findall(pat, text, flags=re.IGNORECASE))


def _fetch_side(term: str, n: int, phrase: bool = True) -> list[dict]:
    pmids = mc.pubmed_search(term, retmax=n * 3, field="tiab", phrase=phrase)  # over-fetch; some lack abstracts
    docs = mc.pubmed_fetch(pmids)
    keep = [d for d in docs if d.get("abstract")]  # need real text to embed
    return keep[:n]


def _mk_doc(d: dict, community: str, term_self: str, term_other: str) -> dict:
    text = f"{d['title']} {d['abstract']}".strip()
    other_hits = _contains_term(text, term_other)
    self_hits = _contains_term(text, term_self)
    return {
        "id": f"{community}_{d['pmid']}",
        "pmid": d["pmid"],
        "community": community,
        "title": d["title"],
        "text": text,
        "self_term_hits": self_hits,
        "other_term_hits": other_hits,
        "contains_other_term": other_hits > 0,
    }


def _citation_reconciliation(docs_a: list[dict], docs_b: list[dict], walk: bool) -> dict:
    """Guard 2: OpenAlex backward-citation disjointness between the two communities."""
    if not walk:
        return {"ran": False, "note": "citation walk skipped (--walk not set)"}
    def refs_and_ids(docs):
        oa_ids, refsets = {}, {}
        for d in docs:
            oid = mc.openalex_id_by_pmid(d["pmid"])
            if oid:
                oa_ids[d["pmid"]] = oid
            refsets[d["pmid"]] = set(mc.referenced_works(d["pmid"]))
        return oa_ids, refsets
    a_ids, a_refs = refs_and_ids(docs_a)
    b_ids, b_refs = refs_and_ids(docs_b)
    a_id_set, b_id_set = set(a_ids.values()), set(b_ids.values())
    # reference-data COVERAGE: how many docs actually have a non-empty reference list in
    # OpenAlex. Without this, "0 shared references" is ambiguous between genuinely-disjoint and
    # no-data. A low-coverage cell cannot be called UNRECONCILED on citation grounds.
    a_cov = sum(1 for r in a_refs.values() if r)
    b_cov = sum(1 for r in b_refs.values() if r)
    # direct cross citations: does any A-doc cite any B-doc (or vice versa)?
    a_cites_b = sum(1 for p, r in a_refs.items() if r & b_id_set)
    b_cites_a = sum(1 for p, r in b_refs.items() if r & a_id_set)
    # shared references (common foundations)
    all_a = set().union(*a_refs.values()) if a_refs else set()
    all_b = set().union(*b_refs.values()) if b_refs else set()
    shared = all_a & all_b
    jacc = len(shared) / len(all_a | all_b) if (all_a | all_b) else 0.0
    low_cov = a_cov < 3 or b_cov < 3
    if low_cov:
        verdict = "INSUFFICIENT DATA (too few docs with references in OpenAlex; cannot judge)"
    elif (a_cites_b + b_cites_a) > 0 or jacc > 0.15:
        verdict = "RECONCILED (discard: communities cite/share heavily)"
    else:
        verdict = "UNRECONCILED (usable: citation-disjoint seam)"
    return {
        "ran": True,
        "a_docs_resolved_in_openalex": len(a_id_set),
        "b_docs_resolved_in_openalex": len(b_id_set),
        "a_docs_with_references": a_cov,
        "b_docs_with_references": b_cov,
        "direct_A_cites_B": a_cites_b,
        "direct_B_cites_A": b_cites_a,
        "shared_reference_count": len(shared),
        "reference_jaccard": round(jacc, 4),
        "verdict": verdict,
    }


def build(term_a: str, term_b: str, seed: str, n_seed: int, n_distract: int,
          walk: bool, uid: str = "") -> dict:
    print(f"[build] A={term_a!r}  B={term_b!r}  seed={seed!r}")
    docs_a_raw = _fetch_side(term_a, n_seed)
    docs_b_raw = _fetch_side(term_b, n_seed)
    print(f"  fetched {len(docs_a_raw)} A-docs, {len(docs_b_raw)} B-docs (with abstracts)")

    docs_a = [_mk_doc(d, "A", term_a, term_b) for d in docs_a_raw]
    docs_b = [_mk_doc(d, "B", term_b, term_a) for d in docs_b_raw]

    # Guard 4b census: co-mention rates (report, do not silently drop).
    def census(docs, side_from, side_to):
        n = len(docs)
        with_other = sum(1 for d in docs if d["contains_other_term"])
        total_hits = sum(d["other_term_hits"] for d in docs)
        return {"n_docs": n, "docs_containing_other_term": with_other,
                "doc_rate": round(with_other / n, 3) if n else 0.0,
                "total_mentions": total_hits,
                "note": f"how often term {side_to} appears in the term-{side_from} search set"}
    comention = {
        "B_in_A": census(docs_a, "A", "B"),
        "A_in_B": census(docs_b, "B", "A"),
    }
    lex_rate = max(comention["B_in_A"]["doc_rate"], comention["A_in_B"]["doc_rate"])
    comention["lexical_reconciliation_verdict"] = (
        "HIGH co-mention (communities lexically bridge; tool LESS applicable here)"
        if lex_rate > 0.34 else
        "LOW co-mention (separable communities; tool-relevant)")

    # distractors
    distractors = []
    for q in DISTRACTOR_QUERIES[:n_distract]:
        got = _fetch_side(q, 1, phrase=False)  # topic AND-of-words, not an exact phrase
        for d in got:
            distractors.append(_mk_doc(d, "E", q, ""))
    print(f"  fetched {len(distractors)} distractor docs")

    citation = _citation_reconciliation(docs_a, docs_b, walk)

    corpus = {
        "_note": "Cross-community cell corpus (half-synthetic: real PubMed records, authored "
                 "A/B/E grouping). docs_A use term A, docs_B use term B for the SAME MeSH concept; "
                 "E = off-topic distractors. Every doc tagged contains_other_term so retrieval can "
                 "be scored inclusive AND clean. Built by build_corpus.py.",
        "pair": {"term_a": term_a, "term_b": term_b, "seed_concept": seed, "mesh_uid": uid},
        "guards": {"citation_reconciliation_G2": citation,
                   "comention_census_G4b": comention},
        "documents": docs_a + docs_b + distractors,
    }
    return corpus


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair-index", type=int, default=None, help="row in candidate_pairs.json")
    ap.add_argument("--a", help="term A (overrides --pair-index)")
    ap.add_argument("--b", help="term B")
    ap.add_argument("--seed", default="", help="seed concept label")
    ap.add_argument("--uid", default="")
    ap.add_argument("--n-seed", type=int, default=10)
    ap.add_argument("--n-distract", type=int, default=8)
    ap.add_argument("--walk", action="store_true", help="run OpenAlex backward-citation Guard 2")
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()

    guard0 = None
    if args.a and args.b:
        term_a, term_b, seed, uid = args.a, args.b, args.seed, args.uid
    else:
        cand = json.loads(CAND.read_text())["pairs"]
        idx = args.pair_index if args.pair_index is not None else 0
        p = cand[idx]
        term_a, term_b = p["entry_term"], p["descriptor"]
        seed, uid = p["seed_concept"], p.get("mesh_uid", "")
        guard0 = {"cross_cosine": p.get("cross_cosine"), "guard0": p.get("guard0")}

    # Guard 0 gate (from select_pairs annotation): building a corpus for an embedder-BRIDGED pair
    # is likely wasted — the bare term already reaches the far side, so definition-mediated
    # retrieval has no room. Warn loudly but do not hard-stop (a demonstration may still want it).
    if guard0 and guard0.get("guard0") == "fail":
        print(f"\n  ⚠ GUARD 0 WARNING: cross_cosine={guard0['cross_cosine']} >= threshold — the "
              f"embedder already bridges {term_a!r}<->{term_b!r}. Raw-term retrieval will likely "
              f"reach the far side unaided, so the tool is probably REDUNDANT on this pair. "
              f"(This is what happened to cell 1.) Prefer a Guard-0 'pass' pair.")

    corpus = build(term_a, term_b, seed, args.n_seed, args.n_distract, args.walk, uid)
    corpus["pair_guard0"] = guard0
    Path(args.out).write_text(json.dumps(corpus, indent=2))

    g = corpus["guards"]
    print("\n==== GUARD REPORT ====")
    print("Guard 2 (citation reconciliation):")
    for k, v in g["citation_reconciliation_G2"].items():
        print(f"    {k}: {v}")
    print("Guard 4b (co-mention census):")
    cm = g["comention_census_G4b"]
    for side in ("B_in_A", "A_in_B"):
        c = cm[side]
        print(f"    {side}: {c['docs_containing_other_term']}/{c['n_docs']} docs "
              f"(rate {c['doc_rate']}), {c['total_mentions']} total mentions")
    print(f"    verdict: {cm['lexical_reconciliation_verdict']}")
    print(f"\n[done] {args.out}  ({len(corpus['documents'])} docs)")


if __name__ == "__main__":
    main()
