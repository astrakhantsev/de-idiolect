#!/usr/bin/env python3
"""Human-review utility over a completed FROZEN v0.9 run (prereg-v09 §0.4; reads
runs/v09/results.json + review-context.json, cross-checked — never a reconstruction).

The operating point τ is a USER-LEVEL setting (runs/review/tau-setting.json): it selects
the operational lens — which verdicts are asserted vs land in the human review queue.
It never changes the frozen scientific scoring: every run computes ALL τ points; the
pre-registered PRIMARY = τ1 alone gates E1/TEST.

  τ0 = frozen v0.8 rules (covers k>=2 & c=0; no promotion; L2-query retrieval)
  τ1 = + evidence-exhausted promotion + L0+L1-query retrieval   <- PRIMARY
  τ2 = τ1 + one-dissent covers (k>=2 & c<=1)                    <- exploratory

Subcommands:
  set-tau tau0|tau1|tau2   persist the user-level operating point
  list                     all pairs x all τ verdicts; queue markers at the active τ
  queue                    only pairs needing a human decision at the active τ
  show <PID> [--reveal-key]   full dossier to the terminal
  dossiers [--out FILE] [--reveal-key]   markdown dossier doc for the queue
  decide <PID> confirm|override:<relation>|defer [--notes "..."]
                           append the human disposition to runs/review/decisions.jsonl
                           (append-only; NEVER read by any scoring path); broadnarrow
                           overrides carry the side: override:broadnarrow(a) or (b)

The answer key stays HIDDEN unless --reveal-key: the dossier mimics the real decision
surface (decide first, compare after). Raw excerpts are shown UNMASKED — masking exists
to blind the model judges, not the human adjudicator.

DATA SOURCE (prereg-v09 §0.4/§2.5): the FROZEN per-τ artifacts written by the v0.9
controller — runs/v09/results.json + runs/v09/review-context.json — never a
counterfactual reconstruction. Requires a completed `run_v09.sh` run.
"""
import datetime
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke
from smoke import RUNS

V09 = RUNS / "v09"
TAU_MODES = {"tau0": None, "tau1": None, "tau2": None}  # keys = valid setting values
TAU_DESC = {"tau0": "frozen v0.8 rules (max precision)",
            "tau1": "evidence-exhausted promotion + L0+L1 retrieval (PRIMARY)",
            "tau2": "tau1 + one-dissent covers (exploratory)"}
SETTING = RUNS / "review" / "tau-setting.json"

def get_tau():
    if SETTING.exists(): return json.load(open(SETTING))["tau"]
    return "tau1"  # default = the pre-registered primary

def set_tau(t):
    if t not in TAU_MODES: sys.exit(f"unknown tau {t!r} (choose from {sorted(TAU_MODES)})")
    SETTING.parent.mkdir(parents=True, exist_ok=True)
    json.dump({"tau": t, "note": TAU_DESC[t]}, open(SETTING, "w"), indent=1)
    print(f"active operating point -> {t} ({TAU_DESC[t]})")

def build_all():
    """Load the frozen per-τ verdicts + contexts, CROSS-CHECKED against results.json
    (round-2 F6: a results/context mismatch is corruption, not something to render)."""
    cf_, rf = V09 / "review-context.json", V09 / "results.json"
    if not (cf_.exists() and rf.exists()):
        sys.exit("no frozen v0.9 artifacts at runs/v09/ — run run_v09.sh first")
    context, results = json.load(open(cf_)), json.load(open(rf))
    for t in TAU_MODES:
        for pid, e in context[t].items():
            rv = results[t]["per_pair"][pid]["verdict"]
            cv = {k: e["verdict"].get(k) for k in rv}
            if cv != rv:
                sys.exit(f"ARTIFACT MISMATCH: {t}/{pid} differs between results.json and review-context.json")
    return {t: {pid: {"verdict": e["verdict"], "ctx": e} for pid, e in context[t].items()}
            for t in TAU_MODES}

def needs_review(v):
    return v["status"] in ("review_required", "insufficient_evidence", "config_fail")

def pair_by_id(pid):
    p = next((x for x in smoke.load_pairs() if x["pair_id"] == pid), None)
    if p is None: sys.exit(f"unknown pair {pid}")
    return p

def cmd_list():
    tau = get_tau()
    built = build_all()
    print(f"active τ = {tau} ({TAU_DESC[tau]}); Q = in review queue at active τ\n")
    print(f"{'pair':<5}" + "".join(f"{t:<44}" for t in TAU_MODES))
    for pid in sorted(built["tau0"]):
        row = f"{pid:<5}"
        for t in TAU_MODES:
            v = built[t][pid]["verdict"]
            mark = " Q" if (t == tau and needs_review(v)) else ""
            row += f"{smoke.display(v) + mark:<44}"
        print(row)

def cmd_queue():
    tau = get_tau()
    built = build_all()[tau]
    q = [pid for pid in sorted(built) if needs_review(built[pid]["verdict"])]
    print(f"review queue at {tau}: {len(q)} pair(s)")
    for pid in q:
        p = pair_by_id(pid)
        print(f"  {pid}: “{p['term_a']}” (A) vs “{p['term_b']}” (B) — {smoke.display(built[pid]['verdict'])}")
    if not q: print("  (empty — nothing needs a human decision at this operating point)")
    return q

def _matrix_rows(pid, d):
    meta = json.load(open(V09 / "verify/meta.json"))
    mm = meta.get(f"{pid}-{d}")
    if not mm: return None, None
    rows = smoke.validate_matrix_rows(smoke.parse_json_out(V09 / f"verify/out-{pid}-{d}.json"), mm["n"])
    return mm, rows

def dossier(pid, built_all, reveal=False):
    """Markdown dossier for one pair — everything a human needs for a full decision."""
    p = pair_by_id(pid)
    tau = get_tau()
    L = []
    v_active = built_all[tau][pid]["verdict"]
    L.append(f"## {pid} — “{p['term_a']}” (community A, forum register) vs “{p['term_b']}” (community B, preprint register)")
    L.append("")
    L.append(f"**Pipeline verdict at active {tau}: {smoke.display(v_active)}** · all points: " +
             " · ".join(f"{t}: {smoke.display(built_all[t][pid]['verdict'])}" for t in TAU_MODES))
    L.append("")
    exc = smoke.load_exc()
    for side, term, reg in (("a", p["term_a"], "A"), ("b", p["term_b"], "B")):
        try:
            lad = smoke.read_ladder(side, term)
            L.append(f"**Ladder {reg} (“{term}”):** L0: {lad['L0']} · L1: {lad['L1']} · L2: {lad['L2']}")
        except FileNotFoundError:
            L.append(f"**Ladder {reg} (“{term}”):** not generated (gate-failed or pair dead)")
        L.append("")
    for d, desc in (("a2b", "A's ladder judged against B's excerpts"),
                    ("b2a", "B's ladder judged against A's excerpts")):
        dctx = built_all[tau][pid]["ctx"]["dirs"][d]
        if dctx.get("status") != "ok":
            L.append(f"**Direction {d}** ({desc}): {dctx.get('status')}"); L.append(""); continue
        lv = dctx["levels"]
        counts = " · ".join(f"{l}: k{lv[l]['k']} c{lv[l]['c']} u{lv[l]['u']}"
                            + (f" (quote-downgraded: {lv[l]['quote_downgrades']})" if lv[l]['quote_downgrades'] else "")
                            for l in ("L0", "L1", "L2"))
        # v09-review F7: promoted effective levels must be visibly distinct from evidenced base
        if dctx.get("promoted"):
            lvl_str = f"base L={dctx['base_L']} → PROMOTED L†={dctx['L']} (levels above base are pure-abstain, not evidenced)"
        else:
            lvl_str = f"L={dctx['L']}" + (f" (base, no promotion)" if "base_L" in dctx else "")
        L.append(f"**Direction {d}** ({desc}): {lvl_str} · {counts} · monotone={dctx['monotone']} starved={dctx['starved']}")
        mm, rows = _matrix_rows(pid, d)
        if mm and rows:
            L.append(f"Judged sample ({mm['n']} excerpts of “{mm['term']}”, community {mm['eside'].upper()}), decided verdicts with the judge's quotes:")
            for i in sorted(rows):
                e = mm["excerpts"][i - 1]
                decided = [f"{l}={rows[i][l]['verdict']}" + (f" (“{rows[i][l]['quote']}”)" if rows[i][l]['quote'] else "")
                           for l in ("L0", "L1", "L2") if rows[i][l]["verdict"] != "insufficient"]
                flag = " ⚠ CONTRADICTS" if any(rows[i][l]["verdict"] == "contradicts" for l in ("L0", "L1", "L2")) else ""
                L.append(f"- [{i}] (doc {e['doc']}){flag}: {e['text']}")
                L.append(f"  - judge: {'; '.join(decided) if decided else 'all insufficient'}")
        L.append("")
    ctx = built_all[tau][pid]["ctx"]
    retrf = V09 / "retrieval.json"
    L.append(f"**Retrieval:** mutual@active-τ = {ctx['mutual']}")
    if retrf.exists():
        rr = json.load(open(retrf)).get(pid, {})
        for q in ("L2", "L0L1"):
            if q not in rr: continue
            # round-2 F7: the ranked evidence, not just booleans
            parts = []
            for d in ("a2b", "b2a"):
                top = ", ".join(f"doc{doc}@{sim:.3f}" for doc, sim in rr[q][d]["top3"])
                parts.append(f"{d} {'HIT' if rr[q][d]['hit'] else 'miss'} [{top}]")
            L.append(f"  - query {q} (mutual={rr[q]['mutual']}): " + " · ".join(parts))
    dc, ct = ctx["decompose"], ctx["containment"]
    if dc is None:
        L.append("**Decompose:** not run (path not reached)")
    elif dc["status"] == "abstain":
        L.append("**Decompose:** ABSTAIN (no specific shared core)")
    else:
        L.append(f"**Decompose:** {dc['status']}" + (f" — core: {dc.get('core','')}" if dc.get('core') else ""))
        # v09-review F8: the validated side-specific evidence for the core
        if dc.get("quote_1"): L.append(f"  - evidence A (⟦T1⟧ side): “{dc['quote_1']}”")
        if dc.get("quote_2"): L.append(f"  - evidence B (⟦T2⟧ side): “{dc['quote_2']}”")
    if ct is not None:
        raw = smoke.parse_json_out(V09 / f"containment/out-{pid}.json") or {}
        L.append(f"**Containment:** {ct.get('relation', ct.get('detail'))} — {raw.get('justification', '')}")
        # round-2 F6: no reads outside the frozen v0.9 artifact set (probe files retired)
    else:
        L.append("**Containment:** not run (path not reached)")
    sym = ctx.get("symcheck")
    if sym: L.append(f"**Symmetry check:** {sym.get('status')} · confirms={sym.get('confirms')}")
    L.append("")
    if reveal:
        exp = p["expected"] + (f"(broader={p.get('broader_side')})" if p["expected"] == "broadnarrow" else "")
        L.append(f"**Planted answer (revealed):** {exp}")
    else:
        L.append("**Planted answer:** hidden — decide first, then re-render with --reveal-key")
    L.append("")
    L.append("**Human decision:** ☐ confirm pipeline verdict · ☐ override → relation: ______ · ☐ needs more evidence · notes: ______")
    L.append("")
    return "\n".join(L)

def cmd_show(pid, reveal):
    print(dossier(pid, build_all(), reveal))

def cmd_dossiers(out=None, reveal=False):
    tau = get_tau()
    built = build_all()
    q = [pid for pid in sorted(built[tau]) if needs_review(built[tau][pid]["verdict"])]
    doc = [f"# Peer-reconciliation review queue — active τ = {tau} ({TAU_DESC[tau]})", ""]
    doc.append(f"{len(q)} pair(s) need a human decision. Generated by `review_pairs.py dossiers` from the frozen v0.9 artifacts (runs/v09/); the τ setting is operational only — frozen scoring always reports all points, with the pre-registered primary (τ1) gating E1/TEST.")
    doc.append("")
    for pid in q:
        doc.append(dossier(pid, built, reveal))
    out = Path(out) if out else RUNS / "review" / f"queue-{tau}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(doc))
    print(f"wrote {out} ({len(q)} dossiers)")
    return out

HARD_OR_NONE = set(smoke.HARD_MATCH) | set(smoke.NO_MATCH)

def parse_override(decision):
    """round-2 F8: 'override:<relation>' with broadnarrow REQUIRING a side —
    override:broadnarrow(a) / override:broadnarrow(b). Returns (relation, broader_side)."""
    import re
    body = decision.split(":", 1)[1]
    m = re.fullmatch(r"broadnarrow\(([ab])\)", body)
    if m: return "broadnarrow", m.group(1)
    if body == "broadnarrow":
        sys.exit("broadnarrow override must carry the side: override:broadnarrow(a) or (b)")
    if body not in HARD_OR_NONE:
        sys.exit(f"override relation must be broadnarrow(a|b) or one of {sorted(HARD_OR_NONE - {'broadnarrow'})}")
    return body, None

def cmd_decide(pid, decision, notes):
    """Append-only human disposition. NEVER read by any scoring path
    (guarded by test: smoke.py/v09.py contain no reference to this file)."""
    if decision != "confirm" and decision != "defer" and not decision.startswith("override:"):
        sys.exit("decision must be confirm | defer | override:<relation>")
    rel = side = None
    if decision.startswith("override:"):
        rel, side = parse_override(decision)
    p = pair_by_id(pid)
    tau = get_tau()
    shown = smoke.display(build_all()[tau][pid]["verdict"])
    rec = {"pair_id": pid, "term_a": p["term_a"], "term_b": p["term_b"], "tau": tau,
           "verdict_shown": shown,
           "decision": "override" if rel else decision,
           "relation": rel, "broader_side": side, "notes": notes,
           "ts": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    f = SETTING.parent / "decisions.jsonl"
    f.parent.mkdir(parents=True, exist_ok=True)
    with open(f, "a") as fh:
        fh.write(json.dumps(rec) + "\n")
    print(f"recorded: {pid} @ {tau} shown={shown} decision={decision}")

def main():
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    reveal = "--reveal-key" in rest
    rest = [a for a in rest if a != "--reveal-key"]
    if cmd == "set-tau": set_tau(rest[0])
    elif cmd == "list": cmd_list()
    elif cmd == "queue": cmd_queue()
    elif cmd == "show": cmd_show(rest[0], reveal)
    elif cmd == "dossiers":
        out = rest[rest.index("--out") + 1] if "--out" in rest else None
        cmd_dossiers(out, reveal)
    elif cmd == "decide":
        notes = rest[rest.index("--notes") + 1] if "--notes" in rest else ""
        cmd_decide(rest[0], rest[1], notes)
    else: sys.exit(f"unknown subcommand {cmd}")

if __name__ == "__main__":
    main()
