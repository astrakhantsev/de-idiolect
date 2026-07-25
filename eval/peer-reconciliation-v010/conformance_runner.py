#!/usr/bin/env python3
"""conformance_runner.py — the frozen conformance runner (v0.10 prereg §3.6(f)). It executes
the golden fixtures (fixtures/*.json) against the FROZEN implementation (serializers.py,
assemble.py, parser_adjudicator.py, the baseline grounding) and MUST PASS. Its pass/fail is
part of BOTH attestation points (§4.2 steps 6 and 8): a spec whose conformance runner does
not pass cannot freeze and cannot generate on key-3.

Each fixture is one oracle: an explicit input paired with expected raw assembled bytes AND/OR
expected parser classification (machine-checkable). Fixture schema (per file, a JSON object):

  {"kind": <see below>, "name": "...", "why": "what §3.6(c) case this covers", ...inputs..., ...expected...}

kinds:
  parse                     {reply, arm:"A"|"B", expect_classification, [expect_fields:{...}]}
  serialize_a_excerpts      {excerpts:[...], expect:"<bytes>"}
  serialize_b_corpus        {docs:[[label,text],...], expect:"<bytes>"}
  serialize_baseline_a_docs {ranked_docs:[[label,text],...], expect:"<bytes>"}
  assemble_baseline_a       {reask:bool, term, ranked_docs:[[label,text],...], expect:"<bytes>"}
  assemble_baseline_b       {reask:bool, term_a, excerpts:[...], docs:[[label,text],...], expect:"<bytes>"}
  ground                    {arm:"A"|"B", matched_term, evidence, docs:[[label,text],...], expect_grounded:bool}

The runner is authored by the CORE agent (interface + seed fixtures); the AUTHORITATIVE
golden-fixture oracle is authored by the fixture agent, extending fixtures/ to cover EVERY
§3.6(c) case (whitespace/case variants; duplicate fields; extra prose; an invalid enum; a
malformed re-ask reply; a_excerpts at 4/5/6; b_corpus first-doc labeling + terminal newline;
document-boundary-spanning grounding; end-to-end assembled first-ask AND re-ask for BOTH
arms). This runner does not need to change when fixtures are added.
"""
import json, sys, re
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import serializers as ser
import assemble as asm
import parser_adjudicator as pa
import baseline_a, baseline_b  # for the arm-specific grounding functions (module-level, no side effects)
import make_pairs_manifest as mpm  # pairs_manifest fixture kind (schema + opaque-id + shuffle)

FIX = BASE / "fixtures"


def _tuples(rows):
    return [tuple(r) for r in rows]


def run_one(fx):
    kind = fx["kind"]
    if kind == "parse":
        enum = pa.enum_for_arm(fx["arm"])
        r = pa.parse_adjudication(fx["reply"], enum)
        if r["classification"] != fx["expect_classification"]:
            return False, f"classification {r['classification']} != {fx['expect_classification']}"
        for k, v in fx.get("expect_fields", {}).items():
            if r["fields"].get(k) != v:
                return False, f"field {k}={r['fields'].get(k)!r} != {v!r}"
        return True, ""
    if kind == "serialize_a_excerpts":
        got = ser.serialize_a_excerpts(fx["excerpts"])
        return (got == fx["expect"]), _diff(got, fx["expect"])
    if kind == "serialize_b_corpus":
        got = ser.serialize_b_corpus(_tuples(fx["docs"]))
        return (got == fx["expect"]), _diff(got, fx["expect"])
    if kind == "serialize_baseline_a_docs":
        got = ser.serialize_baseline_a_docs(_tuples(fx["ranked_docs"]))
        return (got == fx["expect"]), _diff(got, fx["expect"])
    if kind == "assemble_baseline_a":
        got = asm.assemble_baseline_a(fx["term"], _tuples(fx["ranked_docs"]), reask=fx.get("reask", False))
        return (got == fx["expect"]), _diff(got, fx["expect"])
    if kind == "assemble_baseline_b":
        got = asm.assemble_baseline_b(fx["term_a"], fx["excerpts"], _tuples(fx["docs"]), reask=fx.get("reask", False))
        return (got == fx["expect"]), _diff(got, fx["expect"])
    if kind == "ground":
        fields = {"matched_term": fx["matched_term"], "evidence": fx["evidence"]}
        gr = baseline_a._ground if fx["arm"] == "A" else baseline_b._ground
        got = gr(fields, _tuples(fx["docs"]))
        return (got == fx["expect_grounded"]), f"grounded={got} != {fx['expect_grounded']}"
    if kind == "pairs_manifest":
        # §3.6 committed schema for the answer-blind pairs.json: build_payload(term_pairs) must
        # produce top-level {count, pairs}, each record EXACTLY {pair_id(16-hex), term_a, term_b},
        # pair_id = sha256(term_a||NUL||term_b)[:16], sorted by pair_id (key-independent shuffle).
        got = mpm.build_payload([tuple(tp) for tp in fx["term_pairs"]])
        errs = []
        if set(got) != {"count", "pairs"}:
            errs.append(f"top-level {sorted(got)} != {{count,pairs}}")
        if got.get("count") != len(got.get("pairs", [])):
            errs.append("count != len(pairs)")
        ids = [r.get("pair_id") for r in got.get("pairs", [])]
        for r in got.get("pairs", []):
            if set(r) != {"pair_id", "term_a", "term_b"}:
                errs.append(f"record keys {sorted(r)} != {{pair_id,term_a,term_b}}")
            if not re.match(r"^[0-9a-f]{16}$", r.get("pair_id", "")):
                errs.append(f"pair_id {r.get('pair_id')!r} not 16-hex")
        if ids != sorted(ids):
            errs.append("pairs not sorted by opaque id (key-independent shuffle)")
        if errs:
            return False, "; ".join(errs)
        return (got == fx["expect"]), _diff(json.dumps(got, sort_keys=True), json.dumps(fx["expect"], sort_keys=True))
    return False, f"unknown fixture kind {kind!r}"


def _diff(got, expect):
    if got == expect:
        return ""
    return f"bytes differ (got {len(got)}B, expected {len(expect)}B); got={got!r}"


def main():
    fixtures = sorted(FIX.glob("*.json"))
    if not fixtures:
        print("NO FIXTURES found in fixtures/ — the conformance runner cannot pass (§3.6f)")
        sys.exit(1)
    n_pass = n_fail = 0
    for f in fixtures:
        fx = json.load(open(f))
        ok, msg = run_one(fx)
        tag = "PASS" if ok else "FAIL"
        if ok: n_pass += 1
        else: n_fail += 1
        print(f"  {tag} [{fx.get('kind')}] {f.name}: {fx.get('name','')}" + ("" if ok else f"  -- {msg}"))
    print(f"\nconformance: {n_pass} passed, {n_fail} failed, across {len(fixtures)} fixtures")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
