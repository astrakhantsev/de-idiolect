#!/usr/bin/env python3
"""v0.10 verification + composition layer — derived by COPYING the frozen v0.9 controller
(v09.py) and modifying: (1) imports the hardened smoke_v010 primitives; (2) NO carried
stage outputs (key-3 and each confirmatory draw are fresh — every call is a fresh call,
matching run_test_v09.sh's empty carried-manifest); (3) compose is ANSWER-BLIND — it
produces per-τ per-pair verdict records (proposed_relation / status / broader_side / La /
Lb / terminal) and WRITES them, but does NOT grade against the key. Grading (E1/E1b/
coverage, the §5 decision table, the P=1.00 guardrail) is done ONLY by scorer_v010.py,
which is the sole component that reads the sealed answer key (the SPEND, prereg §4.2 step 9).

The τ machinery (tau_dir, row3_candidate, pathP, tau_mutual, apply_base_rule, route_unions,
compose_tau) is carried UNCHANGED from v0.9 — it operates on aggregates + pipeline stage
outputs, never on the answer key.

Subcommands: stage-verify | aggregate | stage-adaptive-1 | stage-adaptive-2 | compose
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke_v010 as smoke
from smoke_v010 import RUNS

V010 = RUNS / "v010"
TAUS = ("tau0", "tau1", "tau2")
PRIMARY = "tau1"
LV = ("L0", "L1", "L2")
DIRS = ("a2b", "b2a")

# ---------- per-τ direction semantics (prereg-v09 §0.2; UNCHANGED) ----------
def tau_covers(k, c, tau):
    return k >= 2 and (c <= 1 if tau == "tau2" else c == 0)

def tau_dir(d, tau):
    if d.get("status") != "ok": return d
    aggs = {}
    for l in LV:
        k, c = d["levels"][l]["k"], d["levels"][l]["c"]
        dec = k + c
        if dec >= 2 and tau_covers(k, c, tau): a = "covers"
        elif dec < 2: a = "abstain"
        elif c >= 2 or k / dec <= 0.3: a = "fails"
        else: a = "mixed"
        aggs[l] = a
    base = max((i for i, l in enumerate(LV) if aggs[l] == "covers"), default=-1)
    L = base
    if tau != "tau0" and base >= 0:
        for i in range(base + 1, 3):
            lv = d["levels"][LV[i]]
            if aggs[LV[i]] == "abstain" and lv["c"] == 0: L = i
            else: break
    monotone = not any(aggs[LV[i]] == "fails" for i in range(max(base, 0)))
    starved = all(d["levels"][l]["k"] + d["levels"][l]["c"] < 2 for l in LV)
    return {**d, "aggs": aggs, "base_L": base, "L": L, "promoted": L != base,
            "monotone": monotone, "starved": starved}

def tau_mutual(retr_entry, tau):
    return retr_entry["L2" if tau == "tau0" else "L0L1"]["mutual"]

def row3_candidate(dirs):
    A, B = dirs["a2b"], dirs["b2a"]
    if A.get("status") != "ok" or B.get("status") != "ok": return None
    if not (A["monotone"] and B["monotone"]): return None
    if A["starved"] and B["starved"]: return None
    if A.get("collapsed") or B.get("collapsed"): return None
    if A["L"] == 2 and B["L"] <= 0 and smoke.deep_c(B): return ("b2a", "a")
    if B["L"] == 2 and A["L"] <= 0 and smoke.deep_c(A): return ("a2b", "b")
    return None

def pathP(dirs):
    A, B = dirs["a2b"], dirs["b2a"]
    if A.get("status") != "ok" or B.get("status") != "ok": return False
    if not (A["monotone"] and B["monotone"]): return False
    if A["starved"] and B["starved"]: return False
    if A.get("collapsed") or B.get("collapsed"): return False
    return A["L"] != 2 and B["L"] != 2

# ---------- fresh verification (all 20; UNCHANGED except run tree = V010) ----------
def stage_verify(pairs):
    st = smoke.gate_load(); floor = smoke.load_floor()
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    tmpl = (BASE / "prompts/verify-matrix.md").read_text()
    (V010 / "verify").mkdir(parents=True, exist_ok=True)
    (V010 / "manifests").mkdir(parents=True, exist_ok=True)
    rows, meta = [], {}
    for p in smoke.alive_pairs(pairs, st, floor):
        pid = p["pair_id"]
        for d, dside, eside, cli, model in (("a2b", "a", "b", "claude", "opus"),
                                            ("b2a", "b", "a", "codex", "gpt-5.6-terra")):
            dterm = p["term_a"] if dside == "a" else p["term_b"]
            eterm = p["term_b"] if eside == "b" else p["term_a"]
            samp = smoke.sample_of(exc[eside][eterm])
            meta[f"{pid}-{d}"] = {"n": len(samp), "excerpts": samp, "term": eterm, "eside": eside}
            lad = smoke.read_ladder(dside, dterm)
            body = (tmpl.replace("{D0}", lad["L0"]).replace("{D1}", lad["L1"])
                        .replace("{D2}", lad["L2"]) + "\n" + smoke.numbered(samp, eside, eterm, terms))
            pf = V010 / f"verify/prompt-{pid}-{d}.md"; pf.write_text(body)
            smoke.stage_call(rows, cli, model, pf, V010 / f"verify/out-{pid}-{d}.json",
                             V010 / f"manifests/verify-{pid}-{d}.json")
    (V010 / "verify/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    json.dump(meta, open(V010 / "verify/meta.json", "w"), indent=1)
    print(f"{len(rows)} fresh verification calls staged")

def aggregate(pairs):
    st = smoke.gate_load(); floor = smoke.load_floor(); terms = smoke.side_terms(pairs)
    meta = json.load(open(V010 / "verify/meta.json"))
    agg = {}
    for p in smoke.alive_pairs(pairs, st, floor):
        pid = p["pair_id"]; agg[pid] = {}
        for d in DIRS:
            f = V010 / f"verify/out-{pid}-{d}.json"
            status = smoke.out_status(f)
            if status != "present":
                agg[pid][d] = {"status": status}; continue
            mm = meta[f"{pid}-{d}"]
            valid = smoke.validate_matrix_rows(smoke.parse_json_out(f), mm["n"])
            if valid is None:
                agg[pid][d] = {"status": "unparseable"}; continue
            agg[pid][d] = smoke.matrix_direction(valid, smoke.masked_sample_texts(mm, terms))
    json.dump(agg, open(V010 / "agg.json", "w"), indent=1)
    print(f"aggregated {len(agg)} pairs -> runs/v010/agg.json")

# ---------- union-route adaptive staging (§2.3; UNCHANGED, minus carried skipping) ----------
def _tau_dirs_all(agg):
    return {tau: {pid: {d: tau_dir(agg[pid][d], tau) for d in DIRS} for pid in agg} for tau in TAUS}

def route_unions(agg, retr):
    td = _tau_dirs_all(agg)
    sym_union, dec_union = set(), set()
    for tau in TAUS:
        for pid in agg:
            cand = row3_candidate(td[tau][pid])
            if cand: sym_union.add((pid, cand[0]))
            if pathP(td[tau][pid]) and tau_mutual(retr[pid], tau): dec_union.add(pid)
    return sym_union, dec_union

def stage_adaptive_1(pairs):
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    agg = json.load(open(V010 / "agg.json"))
    retr = json.load(open(V010 / "retrieval.json"))
    meta = json.load(open(V010 / "verify/meta.json"))
    by_id = {p["pair_id"]: p for p in pairs}
    sym_rows, dec_rows = [], []
    (V010 / "symcheck").mkdir(parents=True, exist_ok=True)
    (V010 / "decompose").mkdir(parents=True, exist_ok=True)
    sym_union, dec_union = route_unions(agg, retr)
    tmpl_sym = (BASE / "prompts/verify-pair.md").read_text()
    for pid, d in sorted(sym_union):
        out = V010 / f"symcheck/out-{pid}-{d}.json"
        p = by_id[pid]
        cli, model = (("claude", "opus") if d == "b2a" else ("codex", "gpt-5.6-terra"))
        dside = "a" if d == "a2b" else "b"
        dterm = p["term_a"] if dside == "a" else p["term_b"]
        mm = meta[f"{pid}-{d}"]
        body = (tmpl_sym.replace("{DEFINITION}", smoke.read_ladder(dside, dterm)["L1"]) + "\n"
                + smoke.numbered(mm["excerpts"], mm["eside"], mm["term"], terms))
        pf = V010 / f"symcheck/prompt-{pid}-{d}.md"; pf.write_text(body)
        smoke.stage_call(sym_rows, cli, model, pf, out, V010 / f"manifests/symcheck-{pid}-{d}.json")
    tmpl_dec = (BASE / "prompts/decompose.md").read_text()
    for pid in sorted(dec_union):
        out = V010 / f"decompose/out-{pid}.json"
        p = by_id[pid]
        s1 = smoke.sample_of(exc["a"][p["term_a"]]); s2 = smoke.sample_of(exc["b"][p["term_b"]])
        e1 = smoke.numbered(s1, "a", p["term_a"], terms, "⟦T1⟧")
        e2 = smoke.numbered(s2, "b", p["term_b"], terms, "⟦T2⟧")
        pf = V010 / f"decompose/prompt-{pid}.md"
        pf.write_text(tmpl_dec.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        smoke.stage_call(dec_rows, "claude", "sonnet", pf, out, V010 / f"manifests/decompose-{pid}.json")
    (V010 / "symcheck/calls.tsv").write_text("\n".join(sym_rows) + ("\n" if sym_rows else ""))
    (V010 / "decompose/calls.tsv").write_text("\n".join(dec_rows) + ("\n" if dec_rows else ""))
    json.dump({"sym_union": sorted(map(list, sym_union)), "dec_union": sorted(dec_union)},
              open(V010 / "route-union.json", "w"), indent=1)
    print(f"union routes: sym={sorted(sym_union)} dec={sorted(dec_union)}; "
          f"fresh calls staged: sym={len(sym_rows)} dec={len(dec_rows)}")

def stage_adaptive_2(pairs):
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    union = json.load(open(V010 / "route-union.json"))["dec_union"]
    by_id = {p["pair_id"]: p for p in pairs}
    (V010 / "containment").mkdir(parents=True, exist_ok=True)
    tmpl = (BASE / "prompts/containment-v2.md").read_text()
    rows = []
    for pid in union:
        if smoke.decompose_result(pid, by_id[pid], exc, terms, root=V010)["status"] != "ok": continue
        p = by_id[pid]
        s1 = smoke.sample_of(exc["a"][p["term_a"]]); s2 = smoke.sample_of(exc["b"][p["term_b"]])
        e1 = smoke.numbered(s1, "a", p["term_a"], terms, "⟦T1⟧")
        e2 = smoke.numbered(s2, "b", p["term_b"], terms, "⟦T2⟧")
        pf = V010 / f"containment/prompt-{pid}.md"
        pf.write_text(tmpl.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        smoke.stage_call(rows, "codex", "gpt-5.6-terra", pf, V010 / f"containment/out-{pid}.json",
                         V010 / f"manifests/containment-{pid}.json")
    (V010 / "containment/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    print(f"{len(rows)} fresh containment calls staged")

# ---------- per-τ composition (§0.2 + v0.8 §4/§5 via smoke.compose_pair; UNCHANGED logic) ----------
def compose_tau(tau, pairs, agg, retr, meta, exc, terms, st, floor):
    verdicts, ctxs = {}, {}
    cf_terms = smoke.configfail_terms(st); inv = smoke.polarity_inverted(st)
    for p in pairs:
        pid = p["pair_id"]
        configfail = None
        if st.get("polarity_side_fail"): configfail = "polarity-batch-failure"
        elif p["term_a"] in inv["a"] or p["term_b"] in inv["b"]: configfail = "polarity-inversion"
        elif p["term_a"] in cf_terms["a"] or p["term_b"] in cf_terms["b"]: configfail = "artifact-gate-exhaustion"
        floor_fail = "; ".join(floor["dead_pairs"].get(pid, [])) or None
        dirs = {d: (tau_dir(agg[pid][d], tau) if pid in agg else {"status": "missing"}) for d in DIRS}
        cand = row3_candidate(dirs) if not (configfail or floor_fail) else None
        sym = smoke.symcheck_result(pid, cand[0], meta, terms, root=V010) if cand else None
        dc = (smoke.decompose_result(pid, p, exc, terms, root=V010)
              if (V010 / f"decompose/out-{pid}.json").exists() else None)
        ct = (smoke.containment_result(pid, p, exc, terms, root=V010)
              if (V010 / f"containment/out-{pid}.json").exists() else None)
        ctx = {"configfail": configfail, "floor_fail": floor_fail, "dirs": dirs,
               "symcheck": sym, "mutual": tau_mutual(retr[pid], tau) if pid in retr else False,
               "decompose": dc, "containment": ct,
               "flag": smoke.sim_flag(p["term_a"], p["term_b"])}
        v = apply_base_rule(smoke.compose_pair(p, ctx), dirs, cand)
        verdicts[pid], ctxs[pid] = v, ctx
    return verdicts, ctxs

def apply_base_rule(v, dirs, row3_cand):
    """§0.2/R4 (UNCHANGED): a ROW-3 broadnarrow needs the covering direction's BASE >= L1."""
    if row3_cand is None: return v
    if v.get("proposed_relation") == "broadnarrow" and v.get("broader_side") == row3_cand[1]:
        cd = dirs["a2b" if v["broader_side"] == "a" else "b2a"]
        if cd.get("promoted") and cd.get("base_L", 2) < 1:
            return smoke._v(None, "review_required", "promotion-base-genus-only")
    return v

def compose(pairs):
    """ANSWER-BLIND. Produces per-τ per-pair verdict records (proposed_relation / status /
    broader_side / La / Lb / terminal) and writes them. Does NOT grade. The composed
    per-pair verdict records are part of the step-7 sealed-answer-material-blind inventory
    (prereg §4.2 step 7)."""
    st = smoke.gate_load(); floor = smoke.load_floor()
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    agg = json.load(open(V010 / "agg.json"))
    retr = json.load(open(V010 / "retrieval.json"))
    meta = json.load(open(V010 / "verify/meta.json"))
    verdicts_out = {"primary": PRIMARY}
    context = {}
    for tau in TAUS:
        verdicts, ctxs = compose_tau(tau, pairs, agg, retr, meta, exc, terms, st, floor)
        # record per-pair verdict (proposed_relation/status/broader_side/La/Lb/display/terminal)
        recs = {}
        for pid in sorted(verdicts):
            v = verdicts[pid]
            recs[pid] = {"proposed_relation": v.get("proposed_relation"),
                         "status": v["status"], "reason": v.get("reason"),
                         "broader_side": v.get("broader_side"),
                         "La": ctxs[pid]["dirs"]["a2b"].get("L"),
                         "Lb": ctxs[pid]["dirs"]["b2a"].get("L"),
                         "display": smoke.display(v),
                         "terminal": ctxs[pid]["configfail"] or ctxs[pid]["floor_fail"]}
        verdicts_out[tau] = recs
        context[tau] = {pid: {
            "verdict": verdicts[pid],
            "dirs": {d: {k: ctxs[pid]["dirs"][d].get(k) for k in
                         ("status", "L", "base_L", "promoted", "aggs", "levels", "monotone", "starved", "collapsed")}
                     for d in DIRS},
            "mutual": ctxs[pid]["mutual"], "flag": ctxs[pid]["flag"],
            "symcheck": ctxs[pid]["symcheck"], "decompose": ctxs[pid]["decompose"],
            "containment": ctxs[pid]["containment"],
            "terminal": ctxs[pid]["configfail"] or ctxs[pid]["floor_fail"]} for pid in verdicts}
        mark = " [PRIMARY]" if tau == PRIMARY else ""
        print(f"{tau}{mark}: " + " ".join(f"{pid}={recs[pid]['display']}" for pid in sorted(recs)))
    json.dump(verdicts_out, open(V010 / "verdicts.json", "w"), indent=1)
    json.dump(context, open(V010 / "review-context.json", "w"), indent=1)
    print("\nANSWER-BLIND compose complete -> runs/v010/verdicts.json (grading deferred to scorer_v010.py)")

def main():
    cmd = sys.argv[1]
    pairs = smoke.load_pairs()
    V010.mkdir(parents=True, exist_ok=True)
    (V010 / "manifests").mkdir(exist_ok=True)
    {"stage-verify": stage_verify, "aggregate": aggregate,
     "stage-adaptive-1": stage_adaptive_1, "stage-adaptive-2": stage_adaptive_2,
     "compose": compose}[cmd](pairs)

if __name__ == "__main__":
    main()
