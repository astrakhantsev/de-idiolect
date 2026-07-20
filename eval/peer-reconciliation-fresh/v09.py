#!/usr/bin/env python3
"""v0.9 TRAIN controller — verification-layer RESAMPLE (prereg-v09.md is the authority;
prereg-v08.md governs everything v0.9 does not change). Reuses smoke.py's frozen
primitives; never writes into the v0.8 tree — all outputs live under runs/v09/.

Frozen inputs (v0.8, committed): corpus, excerpts/samples, checklists, ladders,
conformance, polarity, gate state. Carried stage outputs (§0.5): v0.8 + 2026-07-19
diagnostic decompose/containment/symcheck outputs, copied with a hashed provenance
manifest. Fresh calls: all 20 matrix verifications + adaptive-stage calls required by
union-routing (§2.3) and not satisfied by the carried set.

Subcommands: carry-stages | stage-verify | aggregate | stage-adaptive-1 (symcheck +
decompose) | stage-adaptive-2 (containment) | compose | emit-queue-context
"""
import json, hashlib, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke
from smoke import RUNS  # the frozen v0.8 tree (read-only here)

V09 = RUNS / "v09"
TAUS = ("tau0", "tau1", "tau2")
PRIMARY = "tau1"
LV = ("L0", "L1", "L2")
DIRS = ("a2b", "b2a")

# ---------- per-τ direction semantics (prereg-v09 §0.2) ----------
def tau_covers(k, c, tau):
    return k >= 2 and (c <= 1 if tau == "tau2" else c == 0)

def tau_dir(d, tau):
    """Rebuild a raw matrix_direction dict under a τ point: per-level aggregates,
    base level, promoted effective level (silence rule R10), monotone/starved."""
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
            # §0.2/R10: extension only through SILENT levels (k+c < 2 AND c == 0)
            if aggs[LV[i]] == "abstain" and lv["c"] == 0: L = i
            else: break
    monotone = not any(aggs[LV[i]] == "fails" for i in range(max(base, 0)))
    starved = all(d["levels"][l]["k"] + d["levels"][l]["c"] < 2 for l in LV)
    return {**d, "aggs": aggs, "base_L": base, "L": L, "promoted": L != base,
            "monotone": monotone, "starved": starved}

def tau_mutual(retr_entry, tau):
    return retr_entry["L2" if tau == "tau0" else "L0L1"]["mutual"]

def row3_candidate(dirs):
    """(failing_direction, covering_side) if the τ-adjusted cell sits in table row 3
    with deep-c (raw L1 counts, §0.2), after the §4 pretable conditions."""
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

# ---------- carried stage outputs (§0.5) ----------
def carried_map():
    m = []
    for pid in ("P01", "P04", "P06", "P07", "P08", "P09", "P10"):
        m.append((RUNS / f"decompose/out-{pid}.json", V09 / f"decompose/out-{pid}.json",
                  "v0.8 TRAIN decompose (frozen prompts/judge sonnet)"))
    for pid in ("P01", "P04", "P06", "P07", "P08", "P10"):
        m.append((RUNS / f"containment/out-{pid}.json", V09 / f"containment/out-{pid}.json",
                  "v0.8 TRAIN containment (frozen prompt/judge codex terra)"))
    m.append((RUNS / "cf-diagnostic/out-dec-P05.json", V09 / "decompose/out-P05.json",
              "2026-07-19 diagnostic decompose P05 (frozen prompt/judge sonnet)"))
    m.append((RUNS / "cf-diagnostic/out-cont-P05.json", V09 / "containment/out-P05.json",
              "2026-07-19 diagnostic containment P05 (frozen prompt/judge codex terra)"))
    m.append((RUNS / "cf-diagnostic/out-P04-a2b.json", V09 / "symcheck/out-P04-a2b.json",
              "2026-07-19 diagnostic symcheck P04-a2b (frozen template/judge codex terra)"))
    return m

def carried_dsts():
    mf = V09 / "carried-manifest.json"
    if not mf.exists(): return set()
    return {e["dst"] for e in json.load(open(mf))}

def carry_stages(pairs):
    """First run only (round-2 F2): copying after the freeze would let a resume mutate
    frozen inputs — once the manifest exists, use verify-carried instead."""
    if (V09 / "carried-manifest.json").exists():
        sys.exit("carried-manifest.json already exists — resume must use verify-carried, never re-copy")
    entries = []
    for src, dst, prov in carried_map():
        if not src.exists(): sys.exit(f"carried source missing: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(src.read_text())
        entries.append({"dst": str(dst.relative_to(RUNS)), "src": str(src.relative_to(RUNS)),
                        "sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
                        "provenance": prov})
    json.dump(entries, open(V09 / "carried-manifest.json", "w"), indent=1)
    print(f"{len(entries)} carried stage outputs -> runs/v09 (manifest hashed in freeze)")

def verify_carried(pairs):
    """Resume path (round-2 F2): every carried destination must hash-match the manifest."""
    mf = V09 / "carried-manifest.json"
    if not mf.exists(): sys.exit("no carried-manifest.json — run carry-stages first")
    bad = []
    for e in json.load(open(mf)):
        f = RUNS / e["dst"]
        if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest() != e["sha256"]:
            bad.append(e["dst"])
    if bad: sys.exit(f"RUN-HALT: carried inputs mutated since freeze: {bad}")
    print(f"verify-carried: {len(json.load(open(mf)))} destinations hash-match the manifest")

# ---------- fresh verification (all 20) ----------
def stage_verify(pairs):
    st = smoke.gate_load(); floor = smoke.load_floor()
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    tmpl = (BASE / "prompts/verify-matrix.md").read_text()
    (V09 / "verify").mkdir(parents=True, exist_ok=True)
    (V09 / "manifests").mkdir(parents=True, exist_ok=True)
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
            pf = V09 / f"verify/prompt-{pid}-{d}.md"; pf.write_text(body)
            smoke.stage_call(rows, cli, model, pf, V09 / f"verify/out-{pid}-{d}.json",
                             V09 / f"manifests/verify-{pid}-{d}.json")
    (V09 / "verify/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    json.dump(meta, open(V09 / "verify/meta.json", "w"), indent=1)
    print(f"{len(rows)} fresh verification calls staged")

def aggregate(pairs):
    st = smoke.gate_load(); floor = smoke.load_floor(); terms = smoke.side_terms(pairs)
    meta = json.load(open(V09 / "verify/meta.json"))
    agg = {}
    for p in smoke.alive_pairs(pairs, st, floor):
        pid = p["pair_id"]; agg[pid] = {}
        for d in DIRS:
            f = V09 / f"verify/out-{pid}-{d}.json"
            status = smoke.out_status(f)
            if status != "present":
                agg[pid][d] = {"status": status}; continue
            mm = meta[f"{pid}-{d}"]
            valid = smoke.validate_matrix_rows(smoke.parse_json_out(f), mm["n"])
            if valid is None:
                agg[pid][d] = {"status": "unparseable"}; continue
            agg[pid][d] = smoke.matrix_direction(valid, smoke.masked_sample_texts(mm, terms))
    json.dump(agg, open(V09 / "agg.json", "w"), indent=1)
    print(f"aggregated {len(agg)} pairs -> runs/v09/agg.json")

# ---------- union-route adaptive staging (§2.3) ----------
def _tau_dirs_all(agg):
    return {tau: {pid: {d: tau_dir(agg[pid][d], tau) for d in DIRS} for pid in agg} for tau in TAUS}

def route_unions(agg, retr):
    """Pure §2.3 union-routing: symchecks for row-3 candidates and decompose-required
    pairs (path P ∧ that τ's mutual) across ALL τ points."""
    td = _tau_dirs_all(agg)
    sym_union, dec_union = set(), set()
    for tau in TAUS:
        for pid in agg:
            cand = row3_candidate(td[tau][pid])
            if cand: sym_union.add((pid, cand[0]))
            if pathP(td[tau][pid]) and tau_mutual(retr[pid], tau): dec_union.add(pid)
    return sym_union, dec_union

def stage_adaptive_1(pairs):
    """Union across τ: symchecks for row-3 candidates; decompose for path-P pairs with
    that τ's mutual — staged only where no carried/fresh output already exists."""
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    agg = json.load(open(V09 / "agg.json"))
    retr = json.load(open(V09 / "retrieval.json"))
    meta = json.load(open(V09 / "verify/meta.json"))
    by_id = {p["pair_id"]: p for p in pairs}
    sym_rows, dec_rows = [], []
    (V09 / "symcheck").mkdir(parents=True, exist_ok=True)
    (V09 / "decompose").mkdir(parents=True, exist_ok=True)
    sym_union, dec_union = route_unions(agg, retr)
    cdsts = carried_dsts()
    tmpl_sym = (BASE / "prompts/verify-pair.md").read_text()
    for pid, d in sorted(sym_union):
        out = V09 / f"symcheck/out-{pid}-{d}.json"
        if str(out.relative_to(RUNS)) in cdsts: continue  # carried input, never re-executed
        # fresh routes are ALWAYS staged (round-2 F3): run_calls.sh decides
        # completed / attempted+failed / interrupted from the invocation manifest
        p = by_id[pid]
        cli, model = (("claude", "opus") if d == "b2a" else ("codex", "gpt-5.6-terra"))
        dside = "a" if d == "a2b" else "b"
        dterm = p["term_a"] if dside == "a" else p["term_b"]
        mm = meta[f"{pid}-{d}"]
        body = (tmpl_sym.replace("{DEFINITION}", smoke.read_ladder(dside, dterm)["L1"]) + "\n"
                + smoke.numbered(mm["excerpts"], mm["eside"], mm["term"], terms))
        pf = V09 / f"symcheck/prompt-{pid}-{d}.md"; pf.write_text(body)
        smoke.stage_call(sym_rows, cli, model, pf, out, V09 / f"manifests/symcheck-{pid}-{d}.json")
    tmpl_dec = (BASE / "prompts/decompose.md").read_text()
    for pid in sorted(dec_union):
        out = V09 / f"decompose/out-{pid}.json"
        if str(out.relative_to(RUNS)) in cdsts: continue  # carried input, never re-executed
        p = by_id[pid]
        s1 = smoke.sample_of(exc["a"][p["term_a"]]); s2 = smoke.sample_of(exc["b"][p["term_b"]])
        e1 = smoke.numbered(s1, "a", p["term_a"], terms, "⟦T1⟧")
        e2 = smoke.numbered(s2, "b", p["term_b"], terms, "⟦T2⟧")
        pf = V09 / f"decompose/prompt-{pid}.md"
        pf.write_text(tmpl_dec.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        smoke.stage_call(dec_rows, "claude", "sonnet", pf, out, V09 / f"manifests/decompose-{pid}.json")
    (V09 / "symcheck/calls.tsv").write_text("\n".join(sym_rows) + ("\n" if sym_rows else ""))
    (V09 / "decompose/calls.tsv").write_text("\n".join(dec_rows) + ("\n" if dec_rows else ""))
    json.dump({"sym_union": sorted(map(list, sym_union)), "dec_union": sorted(dec_union)},
              open(V09 / "route-union.json", "w"), indent=1)
    print(f"union routes: sym={sorted(sym_union)} dec={sorted(dec_union)}; "
          f"fresh calls staged: sym={len(sym_rows)} dec={len(dec_rows)}")

def stage_adaptive_2(pairs):
    """Containment for every dec_union pair whose decompose classifies ok, not carried."""
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    union = json.load(open(V09 / "route-union.json"))["dec_union"]
    by_id = {p["pair_id"]: p for p in pairs}
    (V09 / "containment").mkdir(parents=True, exist_ok=True)
    tmpl = (BASE / "prompts/containment-v2.md").read_text()
    rows = []
    cdsts = carried_dsts()
    for pid in union:
        if str((V09 / f"containment/out-{pid}.json").relative_to(RUNS)) in cdsts: continue  # carried
        if smoke.decompose_result(pid, by_id[pid], exc, terms, root=V09)["status"] != "ok": continue
        p = by_id[pid]
        s1 = smoke.sample_of(exc["a"][p["term_a"]]); s2 = smoke.sample_of(exc["b"][p["term_b"]])
        e1 = smoke.numbered(s1, "a", p["term_a"], terms, "⟦T1⟧")
        e2 = smoke.numbered(s2, "b", p["term_b"], terms, "⟦T2⟧")
        pf = V09 / f"containment/prompt-{pid}.md"
        pf.write_text(tmpl.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        smoke.stage_call(rows, "codex", "gpt-5.6-terra", pf, V09 / f"containment/out-{pid}.json",
                         V09 / f"manifests/containment-{pid}.json")
    (V09 / "containment/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    print(f"{len(rows)} fresh containment calls staged")

# ---------- per-τ composition (§0.2 + v0.8 §4/§5 via smoke.compose_pair) ----------
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
        sym = smoke.symcheck_result(pid, cand[0], meta, terms, root=V09) if cand else None
        dc = (smoke.decompose_result(pid, p, exc, terms, root=V09)
              if (V09 / f"decompose/out-{pid}.json").exists() else None)
        ct = (smoke.containment_result(pid, p, exc, terms, root=V09)
              if (V09 / f"containment/out-{pid}.json").exists() else None)
        ctx = {"configfail": configfail, "floor_fail": floor_fail, "dirs": dirs,
               "symcheck": sym, "mutual": tau_mutual(retr[pid], tau) if pid in retr else False,
               "decompose": dc, "containment": ct,
               "flag": smoke.sim_flag(p["term_a"], p["term_b"])}
        v = apply_base_rule(smoke.compose_pair(p, ctx), dirs, cand)
        verdicts[pid], ctxs[pid] = v, ctx
    return verdicts, ctxs

def apply_base_rule(v, dirs, row3_cand):
    """§0.2/R4: a ROW-3 broadnarrow assertion needs the covering direction's BASE >= L1;
    a genus-only promoted base escalates instead of asserting. Round-2 F1: scoped to
    row 3 ONLY — a path-P broadnarrow (containment-derived) is untouched; row3_cand is
    the row3_candidate() result for this pair's τ-adjusted dirs (None when not row 3)."""
    if row3_cand is None: return v
    if v.get("proposed_relation") == "broadnarrow" and v.get("broader_side") == row3_cand[1]:
        cd = dirs["a2b" if v["broader_side"] == "a" else "b2a"]
        if cd.get("promoted") and cd.get("base_L", 2) < 1:
            return smoke._v(None, "review_required", "promotion-base-genus-only")
    return v

def authorized(results):
    """TEST authorization reads the PRIMARY point alone (multiple-comparison hygiene)."""
    return bool(results[PRIMARY]["E1_PASS"])

def compose(pairs):
    st = smoke.gate_load(); floor = smoke.load_floor()
    exc = smoke.load_exc(); terms = smoke.side_terms(pairs)
    agg = json.load(open(V09 / "agg.json"))
    retr = json.load(open(V09 / "retrieval.json"))
    meta = json.load(open(V09 / "verify/meta.json"))
    results, context = {"primary": PRIMARY}, {}
    for tau in TAUS:
        verdicts, ctxs = compose_tau(tau, pairs, agg, retr, meta, exc, terms, st, floor)
        s = smoke.score(pairs, verdicts)
        results[tau] = s
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
        print(f"{tau}{mark}: correct {s['n_correct']}/10 · prom {len(s['promotions'])} · "
              f"f-esc {len(s['false_escalations'])} · jingle {s['jingle_specific']}/2 · "
              f"E1={'PASS' if s['E1_PASS'] else 'FAIL'} · E1c {s['E1c_graded']}")
        for pid in sorted(verdicts):
            r = s["per_pair"][pid]
            print(f"   {pid}: expected={r['expected']:<28} -> {r['display']:<40} {'OK' if r['correct'] else 'X'}")
    json.dump(results, open(V09 / "results.json", "w"), indent=1)
    json.dump(context, open(V09 / "review-context.json", "w"), indent=1)
    p = results[PRIMARY]
    print(f"\nTRAIN-RESAMPLE VERDICT (bar = E1 at {PRIMARY}): "
          f"{'PASS — TEST authorized per PROTOCOL' if p['E1_PASS'] else 'FAIL — no TEST spend'}")

def main():
    cmd = sys.argv[1]
    pairs = smoke.load_pairs()
    V09.mkdir(parents=True, exist_ok=True)
    (V09 / "manifests").mkdir(exist_ok=True)
    {"carry-stages": carry_stages, "verify-carried": verify_carried,
     "stage-verify": stage_verify, "aggregate": aggregate,
     "stage-adaptive-1": stage_adaptive_1, "stage-adaptive-2": stage_adaptive_2,
     "compose": compose}[cmd](pairs)

if __name__ == "__main__":
    main()
