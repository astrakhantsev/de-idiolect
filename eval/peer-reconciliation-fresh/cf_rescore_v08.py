#!/usr/bin/env python3
"""POST-HOC COUNTERFACTUAL DIAGNOSTIC on the completed v0.8 TRAIN run (NOT part of the
frozen package; cannot fire the sealed TEST). Rescores the SAME run outputs (runs/agg.json,
retrieval, decompose, containment) under relaxed L2/covers/abstain rules, per the
"should we relax the L2 requirement?" question. TRAIN diagnosis is free (PROTOCOL rule 1);
any adopted change requires a fresh v0.9 pre-registration, review, and clean run.

Variants (all reuse smoke.compose_pair / smoke.score so the table semantics stay frozen):
  v08     frozen rules (sanity: must reproduce the accepted 4/10)
  cfA     drop L2: ladder top = L1 (dir L = 2 if L1 covers, 0 if only L0 covers, else -1)
  cfB     c-tolerant covers: a level covers iff (k>=2 and c==0) or (c==1 and k>=4)
  cfC1    abstain-promotion, top level only: L2 pure-abstain promotes an L=1 base to 2
  cfC2    abstain-promotion through all pure-abstain levels above a covers base
  cfBC2   cfB and cfC2 combined (most permissive)

Row-3 cells that fire under a variant need a symmetry check that the frozen run never
staged. If runs/cf-diagnostic/out-<pid>-<dir>.json exists it is used (measured); otherwise
both branches are reported as bounds.

Subcommands: stage-p04 (write the one diagnostic symcheck call) | rescore
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke
from smoke import RUNS

def level_aggs(levels, covers_mode):
    """covers_mode: 'strict' k>=2 & c==0 (frozen) | 'k4c1' adds c==1 when k>=4 (cfB)
    | 'c1' one dissent tolerated: k>=2 & c<=1 (dial point tau2)."""
    out = {}
    for l in ("L0", "L1", "L2"):
        k, c = levels[l]["k"], levels[l]["c"]
        dec = k + c
        cov = (k >= 2 and c == 0) or (covers_mode == "k4c1" and c == 1 and k >= 4) \
              or (covers_mode == "c1" and k >= 2 and c <= 1)
        if dec >= 2 and cov: a = "covers"
        elif dec < 2: a = "abstain"
        elif c >= 2 or k / dec <= 0.3: a = "fails"
        else: a = "mixed"
        out[l] = a
    return out

MODE_COVERS = {"cfB": "k4c1", "cfBC2": "k4c1", "v09c": "c1"}
MODE_PROMOTE = {"cfC1": "top", "cfC2": "all", "cfBC2": "all", "v09": "all", "v09c": "all"}

def variant_dir(d, mode):
    """Rebuild a direction dict {L, monotone, starved, levels, ...} under a variant."""
    if d.get("status") != "ok": return d
    aggs = level_aggs(d["levels"], MODE_COVERS.get(mode, "strict"))
    order = ("L0", "L1", "L2")
    top = 1 if mode == "cfA" else 2
    cov = [i for i, l in enumerate(order[: top + 1]) if aggs[l] == "covers"]
    L = base_L = max(cov, default=-1)
    promote = MODE_PROMOTE.get(mode)
    if promote and L >= 0:
        # promote a covers base through pure-abstain levels above it
        hi = L
        for i in range(L + 1, 3):
            if aggs[order[i]] != "abstain": break
            hi = i
        if promote == "top":
            hi = 2 if (L == 1 and aggs["L2"] == "abstain") else L
        L = hi
    if mode == "cfA" and L == 1: L = base_L = 2  # present L1-top as the table's top level
    monotone = not any(aggs[order[i]] == "fails" for i in range(max(base_L if mode != "cfA" else min(base_L, 1), 0)))
    starved = all(d["levels"][l]["k"] + d["levels"][l]["c"] < 2 for l in order)
    return {**d, "L": L, "base_L": base_L, "promoted": L != base_L,
            "monotone": monotone, "starved": starved, "aggs": aggs}

def _sym_from(f, mm, terms):
    valid = smoke.validate_flat_rows(smoke.parse_json_out(f), mm["n"])
    if valid is None: return {"status": "unparseable"}
    lv = smoke.level_verdict(valid, smoke.masked_sample_texts(mm, terms), quote_required=True)
    return {"status": "ok", "confirms": lv["agg"] == "fails" and lv["c"] >= 2, "counts": lv}

def diag_stage_result(pid, kind, pair, exc, terms):
    """Classify a cf-diagnostic decompose/containment output with the frozen validation."""
    f = RUNS / f"cf-diagnostic/out-{'dec' if kind == 'decompose' else 'cont'}-{pid}.json"
    if not f.exists(): return None
    obj = smoke.parse_json_out(f)
    s1 = smoke.sample_of(exc["a"][pair["term_a"]]); s2 = smoke.sample_of(exc["b"][pair["term_b"]])
    def qok(q, ss, side, term, mask):
        qn = smoke.norm(q or "")
        return bool(qn) and any(qn in smoke.norm(smoke.mask_text(e["text"], side, term, terms, mask)) for e in ss)
    if kind == "decompose":
        # round-v09-review F9: the literal ABSTAIN is a valid semantic outcome, not unparseable
        import re as _re
        raw = _re.sub(r"^```(json)?\s*|```\s*$", "", f.read_text().strip(), flags=_re.M).strip()
        if raw == "ABSTAIN": return {"status": "abstain"}
        if not isinstance(obj, dict) or not obj.get("core"): return {"status": "fail", "detail": "unparseable"}
        if not (qok(obj.get("quote_1"), s1, "a", pair["term_a"], "⟦T1⟧")
                and qok(obj.get("quote_2"), s2, "b", pair["term_b"], "⟦T2⟧")):
            return {"status": "fail", "detail": "quote-validation"}
        return {"status": "ok", "core": obj["core"],
                "quote_1": obj.get("quote_1", ""), "quote_2": obj.get("quote_2", "")}
    obj = smoke.validate_containment(obj)
    if obj is None: return {"status": "fail", "detail": "unparseable"}
    if obj["relation"] != "unclear" and not (qok(obj["quote_1"], s1, "a", pair["term_a"], "⟦T1⟧")
                                             and qok(obj["quote_2"], s2, "b", pair["term_b"], "⟦T2⟧")):
        return {"status": "fail", "detail": "quote-validation"}
    return {"status": "ok", "relation": obj["relation"]}

def assemble(mode, branch="confirmed", needs_sym=None):
    """Build (ctx, verdict) per pair under a variant/τ. Returns {pid: {"ctx", "verdict"}}.
    Unmeasured symchecks take the given branch; measured cf-diagnostic outputs are used."""
    pairs = smoke.load_pairs()
    terms = smoke.side_terms(pairs)
    exc = smoke.load_exc()
    agg = json.load(open(RUNS / "agg.json"))
    retr = json.load(open(RUNS / "retrieval.json"))
    sweepf = RUNS / "cf-diagnostic/retrieval-sweep.json"
    sweep = json.load(open(sweepf)) if sweepf.exists() else None
    if mode.startswith("v09") and sweep is None:
        raise RuntimeError("run cf_probes_v08.py retrieval first")
    if needs_sym is None: needs_sym = []
    out = {}
    for p in pairs:
        pid = p["pair_id"]
        dirs = {d: (agg[pid][d] if mode == "v08" else variant_dir(agg[pid][d], mode))
                for d in ("a2b", "b2a")}
        # which direction fails if row 3 fires under this variant
        A, B = dirs["a2b"], dirs["b2a"]
        sym = None
        if A.get("status") == "ok" and B.get("status") == "ok":
            La, Lb = A["L"], B["L"]
            if (La == 2 and Lb <= 0 and smoke.deep_c(B)) or (Lb == 2 and La <= 0 and smoke.deep_c(A)):
                d_fail = "b2a" if La == 2 else "a2b"
                meta = json.load(open(RUNS / "verify/meta.json"))
                f = RUNS / f"cf-diagnostic/out-{pid}-{d_fail}.json"
                if f.exists():
                    sym = _sym_from(f, meta[f"{pid}-{d_fail}"], terms)
                    if pid not in [x[0] for x in needs_sym]: needs_sym.append((pid, d_fail, "measured"))
                else:
                    sym = {"status": "ok", "confirms": branch == "confirmed"}
                    if pid not in [x[0] for x in needs_sym]: needs_sym.append((pid, d_fail, "BOUNDED"))
        dc = smoke.decompose_result(pid, p, exc, terms) if (RUNS / f"decompose/out-{pid}.json").exists() else None
        ct = smoke.containment_result(pid, p, exc, terms) if (RUNS / f"containment/out-{pid}.json").exists() else None
        mutual = retr.get(pid, {}).get("mutual", False)
        if mode.startswith("v09"):
            # v0.9 candidate retrieval: L0+L1 query, mutual@3 (measured sweep);
            # newly opened paths use the measured cf-diagnostic stage outputs
            mutual = sweep[pid]["a2b"]["L0+L1"]["hit3"] and sweep[pid]["b2a"]["L0+L1"]["hit3"]
            if dc is None: dc = diag_stage_result(pid, "decompose", p, exc, terms)
            if ct is None: ct = diag_stage_result(pid, "containment", p, exc, terms)
        # populate real run state (round-v09-review F5: a configFail/floor pair must queue, not crash)
        st = smoke.gate_load(); floor = smoke.load_floor()
        cf_terms = smoke.configfail_terms(st); inv = smoke.polarity_inverted(st)
        configfail = None
        if st.get("polarity_side_fail"): configfail = "polarity-batch-failure"
        elif p["term_a"] in inv["a"] or p["term_b"] in inv["b"]: configfail = "polarity-inversion"
        elif p["term_a"] in cf_terms["a"] or p["term_b"] in cf_terms["b"]: configfail = "artifact-gate-exhaustion"
        floor_fail = "; ".join(floor["dead_pairs"].get(pid, [])) or None
        ctx = {"configfail": configfail, "floor_fail": floor_fail, "dirs": dirs, "symcheck": sym,
               "mutual": mutual, "decompose": dc, "containment": ct,
               "flag": smoke.sim_flag(p["term_a"], p["term_b"])}
        verdict = smoke.compose_pair(p, ctx)
        # round-v09-review F4: a promotion from a genus-only base (base_L=0 -> L†=2) may not
        # assert row-3 broadnarrow — the covering side never evidenced its mechanism.
        if verdict.get("proposed_relation") == "broadnarrow" and verdict.get("broader_side"):
            cover_dir = "a2b" if verdict["broader_side"] == "a" else "b2a"
            cd = dirs[cover_dir]
            if cd.get("promoted") and cd.get("base_L", 2) < 1:
                verdict = smoke._v(None, "review_required", "promotion-base-genus-only")
        out[pid] = {"ctx": ctx, "verdict": verdict}
    return out

def rescore():
    pairs = smoke.load_pairs()
    sweepf = RUNS / "cf-diagnostic/retrieval-sweep.json"
    sweep_ok = sweepf.exists()
    for mode in ("v08", "cfA", "cfB", "cfC1", "cfC2", "cfBC2", "v09", "v09c"):
        if mode.startswith("v09") and not sweep_ok:
            print(f"\n=== {mode} === (skipped: run cf_probes_v08.py retrieval first)"); continue
        results = {}
        needs_sym = []
        for branch in ("confirmed", "unconfirmed"):
            built = assemble(mode, branch, needs_sym)
            results[branch] = smoke.score(pairs, {pid: b["verdict"] for pid, b in built.items()})
            if not any(x[2] == "BOUNDED" for x in needs_sym): break  # branches identical
        lo, hi = results.get("unconfirmed", results["confirmed"]), results["confirmed"]
        line = lambda s: f"correct {s['n_correct']}/10 prom {len(s['promotions'])} fesc {len(s['false_escalations'])} jingle {s['jingle_specific']}/2 E1={'PASS' if s['E1_PASS'] else 'FAIL'} E1c {s['E1c_graded']}"
        print(f"\n=== {mode} ===")
        if lo is hi or line(lo) == line(hi):
            print("  " + line(hi))
        else:
            print(f"  sym-unconfirmed: {line(lo)}")
            print(f"  sym-confirmed:   {line(hi)}")
        for pid in sorted(hi["per_pair"]):
            r = hi["per_pair"][pid]
            alt = results.get("unconfirmed", {}).get("per_pair", {}).get(pid)
            tag = "" if not alt or alt["display"] == r["display"] else f"  [unconfirmed: {alt['display']}]"
            print(f"  {pid}: {r['expected']:<28} -> {r['display']:<42} {'OK' if r['correct'] else 'X'}{tag}")
        if needs_sym: print(f"  symcheck dependencies: {needs_sym}")

def stage_p04():
    """Stage the single diagnostic symcheck: P04 failing direction a2b (D_A 'squeeze play'
    L1 re-judged vs the E_B sample by the OTHER family = codex terra), verify-pair template."""
    pairs = smoke.load_pairs()
    terms = smoke.side_terms(pairs)
    p = next(x for x in pairs if x["pair_id"] == "P04")
    meta = json.load(open(RUNS / "verify/meta.json"))
    mm = meta["P04-a2b"]
    tmpl = (BASE / "prompts/verify-pair.md").read_text()
    d = RUNS / "cf-diagnostic"; d.mkdir(exist_ok=True)
    body = (tmpl.replace("{DEFINITION}", smoke.read_ladder("a", p["term_a"])["L1"]) + "\n"
            + smoke.numbered(mm["excerpts"], mm["eside"], mm["term"], terms))
    pf = d / "prompt-P04-a2b.md"; pf.write_text(body)
    (d / "calls.tsv").write_text(f"codex\tgpt-5.6-terra\t{pf}\t{d}/out-P04-a2b.json\t{d}/manifest-P04-a2b.json\n")
    print("staged 1 diagnostic call ->", d / "calls.tsv")

if __name__ == "__main__":
    {"rescore": rescore, "stage-p04": stage_p04}[sys.argv[1]]()
