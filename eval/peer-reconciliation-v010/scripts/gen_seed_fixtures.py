#!/usr/bin/env python3
"""gen_seed_fixtures.py — emit the SEED golden-fixture set into fixtures/. These prove the
conformance runner works and DEFINE the fixture format for the fixture-oracle agent, who
will EXTEND fixtures/ with the authoritative, independently-authored oracle covering every
§3.6(c) case.

Independence status per kind (honest labeling, carried in each fixture's "oracle" field):
  parse, ground        -> "independent": expected is HAND-SPECIFIED here (what the grammar
                          SHOULD return); the generator asserts the impl agrees before writing.
  serialize_*, assemble_* -> "regression-seed": expected bytes are the CURRENT impl output
                          (a change-detector). The fixture agent must add INDEPENDENT byte
                          oracles (hand-authored expected) for full §3.6(c) coverage.
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))
import serializers as ser
import assemble as asm
import parser_adjudicator as pa

FIX = BASE / "fixtures"
FIX.mkdir(exist_ok=True)


def write(name, obj):
    json.dump(obj, open(FIX / f"{name}.json", "w"), indent=1)


# ---- parse fixtures (independent: hand-specified classification/fields) ----
PARSE = [
    ("parse_positive_A", "match: yes\nmatched_term: gadget alpha prime\nrelation: exact\nevidence: some verbatim span",
     "A", pa.POSITIVE, {"match": "yes", "relation": "exact", "matched_term": "gadget alpha prime"}),
    ("parse_negative_A", "match: no\nmatched_term: none\nrelation: n/a\nevidence: none",
     "A", pa.NEGATIVE, {"match": "no"}),
    ("parse_case_and_whitespace", "  MATCH : No \n Matched_Term :  none \n RELATION : N/A \n Evidence : none ",
     "A", pa.NEGATIVE, None),
    ("parse_extra_prose_ignored",
     "Reasoning: I looked...\nmatch: yes\nmatched_term: gadget beta prime\nrelation: partial-overlap\nevidence: a span here\nDone.",
     "A", pa.POSITIVE, None),
    ("parse_code_fence_ignored", "```\nmatch: no\nmatched_term: none\nrelation: n/a\nevidence: none\n```",
     "A", pa.NEGATIVE, None),
    ("parse_duplicate_field_malformed", "match: no\nmatch: yes\nmatched_term: none\nrelation: n/a\nevidence: none",
     "A", pa.MALFORMED, None),
    ("parse_missing_field_malformed", "match: no\nmatched_term: none\nrelation: n/a",
     "A", pa.MALFORMED, None),
    ("parse_invalid_relation_enum", "match: yes\nmatched_term: x\nrelation: superMatch\nevidence: y",
     "A", pa.MALFORMED, None),
    ("parse_invalid_match_enum", "match: maybe\nmatched_term: none\nrelation: n/a\nevidence: none",
     "A", pa.MALFORMED, None),
    ("parse_negative_crossfield_violation", "match: no\nmatched_term: gadget alpha prime\nrelation: n/a\nevidence: none",
     "A", pa.MALFORMED, None),
    ("parse_positive_crossfield_relation_na", "match: yes\nmatched_term: x\nrelation: n/a\nevidence: y",
     "A", pa.MALFORMED, None),
    ("parse_wrapper_quotes_stripped", 'match: yes\nmatched_term: "gadget gamma small"\nrelation: exact\nevidence: "quoted span"',
     "A", pa.POSITIVE, {"matched_term": "gadget gamma small", "evidence": "quoted span"}),
    ("parse_malformed_reask_reply", "I still cannot decide, sorry.",
     "A", pa.MALFORMED, None),  # a malformed second (re-ask) reply -> pair/direction no-assertion
    ("parse_arm_b_positive_Abroader", "match: yes\nmatched_term: gadget gamma small\nrelation: A-broader\nevidence: span",
     "B", pa.POSITIVE, {"relation": "a-broader"}),
    ("parse_arm_b_rejects_A_enum", "match: yes\nmatched_term: x\nrelation: term-broader\nevidence: y",
     "B", pa.MALFORMED, None),  # term-broader is arm-A vocabulary, invalid under arm B
]

# ---- ground fixtures (independent: hand-specified boolean) ----
GROUND = [
    ("ground_A_both_present_true", "A", "gadget alpha prime", "the gadget alpha prime metric",
     [["b/01", "we compute the gadget alpha prime metric each run"], ["b/02", "other"], ["b/03", "more"]], True),
    ("ground_A_evidence_absent_false", "A", "gadget alpha prime", "totally fabricated span not present",
     [["b/01", "we compute the gadget alpha prime metric each run"], ["b/02", "x"], ["b/03", "y"]], False),
    ("ground_B_boundary_spanning_true", "B", "alpha", "beta gamma",
     [["b/01", "alpha beta"], ["b/02", "gamma delta"]], True),  # span crosses the "\n\n"->" " join
    ("ground_B_case_fold_true", "B", "GADGET Delta", "Wide TOY concept",
     [["b/01", "a wide toy concept named gadget delta here"]], True),
]

# ---- serializer + assemble fixtures (regression-seed: expected = current impl output) ----
DOC3 = [["b/07", "doc seven body   "], ["b/03", "doc three body"], ["b/09", "doc nine body"]]
DOC2 = [["b/01", "alpha body"], ["b/02", "beta body"]]
EXC = {4: [f"excerpt number {i}" for i in range(4)],
       5: [f"excerpt number {i}" for i in range(5)],
       6: [f"excerpt number {i}" for i in range(6)]}
DOC11 = [[f"b/{i:02d}", f"corpus doc {i} body"] for i in range(1, 12)]


def main():
    for name, reply, arm, cls, fields in PARSE:
        r = pa.parse_adjudication(reply, pa.enum_for_arm(arm))
        assert r["classification"] == cls, f"SEED MISSPEC {name}: impl {r['classification']} != {cls}"
        if fields:
            for k, v in fields.items():
                assert r["fields"].get(k) == v, f"SEED MISSPEC {name}: {k}={r['fields'].get(k)!r} != {v!r}"
        obj = {"kind": "parse", "name": name, "oracle": "independent",
               "why": "parser total-grammar branch", "reply": reply, "arm": arm,
               "expect_classification": cls}
        if fields: obj["expect_fields"] = fields
        write(name, obj)

    for name, arm, mt, ev, docs, exp in GROUND:
        import baseline_a, baseline_b
        gr = baseline_a._ground if arm == "A" else baseline_b._ground
        got = gr({"matched_term": mt, "evidence": ev}, [tuple(d) for d in docs])
        assert got == exp, f"SEED MISSPEC {name}: impl grounded={got} != {exp}"
        write(name, {"kind": "ground", "name": name, "oracle": "independent",
                     "why": "key-blind grounding incl. boundary-spanning", "arm": arm,
                     "matched_term": mt, "evidence": ev, "docs": docs, "expect_grounded": exp})

    for k in (4, 5, 6):
        write(f"serialize_a_excerpts_{k}", {"kind": "serialize_a_excerpts",
              "name": f"a_excerpts at {k}", "oracle": "regression-seed",
              "why": "{a_excerpts} at 4/5/6 excerpts", "excerpts": EXC[k],
              "expect": ser.serialize_a_excerpts(EXC[k])})
    write("serialize_b_corpus_2", {"kind": "serialize_b_corpus", "name": "b_corpus 2-doc",
          "oracle": "regression-seed", "why": "first-document labeling + no terminal newline + rstrip",
          "docs": DOC2, "expect": ser.serialize_b_corpus([tuple(d) for d in DOC2])})
    write("serialize_baseline_a_docs_3", {"kind": "serialize_baseline_a_docs", "name": "top-3 block",
          "oracle": "regression-seed", "why": "Baseline-A retrieved top-3 block, rank labels",
          "ranked_docs": DOC3, "expect": ser.serialize_baseline_a_docs([tuple(d) for d in DOC3])})
    for reask in (False, True):
        tag = "reask" if reask else "first"
        write(f"assemble_baseline_a_{tag}", {"kind": "assemble_baseline_a",
              "name": f"Baseline-A assembled {tag}-ask", "oracle": "regression-seed",
              "why": f"end-to-end assembled {tag}-ask bytes, arm A", "reask": reask,
              "term": "widget alpha", "ranked_docs": DOC3,
              "expect": asm.assemble_baseline_a("widget alpha", [tuple(d) for d in DOC3], reask=reask)})
        write(f"assemble_baseline_b_{tag}", {"kind": "assemble_baseline_b",
              "name": f"Baseline-B assembled {tag}-ask", "oracle": "regression-seed",
              "why": f"end-to-end assembled {tag}-ask bytes, arm B (11-doc corpus join + terminal newline)",
              "reask": reask, "term_a": "widget alpha", "excerpts": EXC[5], "docs": DOC11,
              "expect": asm.assemble_baseline_b("widget alpha", EXC[5], [tuple(d) for d in DOC11], reask=reask)})
    print(f"seed fixtures written -> {FIX} ({len(list(FIX.glob('*.json')))} files)")


if __name__ == "__main__":
    main()
