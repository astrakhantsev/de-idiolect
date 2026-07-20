#!/usr/bin/env python3
"""Peer-reconciliation v0.8 TRAIN controller. prereg-v08.md is the sole authority;
section references (§) below point there. Model calls happen in run_calls.sh via the
e2e isolation runner, never here. Subcommands (staging and gating only):

  excerpts            extract windows, build verification samples (pool = all 11 docs, §2.1/§9-F3)
  manifests           regenerate corpus manifests to exactly docs 01-11 (§1/§8)
  prompts-checklist   stage checklist calls (§2.2)
  gate-checklists     checklist gates: generate -> mechanical -> leak (§1 state machine, §9-F5)
  prompts-def         stage ladder calls (§2.3)
  gate-ladders        ladder mechanical+leak gates (§2.4a, §9-F5)
  prompts-conformance stage semantic conformance batch per side (§2.4b)
  gate-conformance    apply conformance verdicts / batch re-run / run-halt (§9-F4)
  prompts-polarity    stage polarity batches (§2.5)
  gate-polarity       validate polarity output; one re-run then side-scoped configFail (§9-F4)
  prompts-verify      stage matrix verification calls (§2.7)
  aggregate           parse+aggregate matrix outputs -> runs/agg.json (§2.7)
  prompts-symcheck    stage symmetry checks for table row 3 (§2.8, §5)
  prompts-decompose   stage decompose for path-P pairs with mutual hit (§2.9, §5)
  prompts-containment stage containment v2 for decompose successes (§2.10)
  compose             terminals (§4) -> total table (§5) -> E1/E1b/E1c (§6) -> results.json
  assert-resolved     exit nonzero unless every artifact is passed or configFail
"""
VERSION = "v0.8"
import json, re, sys, hashlib, subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
RUNS = BASE / "runs"
KEYF = BASE / "key" / "answer_key.json"
N_SAMPLE, MIN_EXC, POOL_MAX_DOC = 6, 4, 11
MASK = "⟦TERM⟧"
VERDICT_ENUM = {"instantiates", "contradicts", "insufficient"}
CONTAIN_ENUM = {"t1_within_t2", "t2_within_t1", "partial_overlap", "no_relation", "unclear"}
HARD_MATCH = ("exactMatch", "broadnarrow", "relatedMatch")
NO_MATCH = ("noMatch", "noMatchDespiteSimilarity")

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
def norm(s):
    s = s.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "—": "-", "–": "-"}))
    return re.sub(r"\s+", " ", s.lower()).strip()

def load_pairs(): return json.load(open(KEYF))["pairs"]
def side_terms(pairs):
    return {"a": sorted({p["term_a"] for p in pairs}), "b": sorted({p["term_b"] for p in pairs})}

# ---------- mechanical validators (§9-F5) ----------
def w(s): return len(s.split())

def sentence_count(s):
    # §9-F5: segments produced by splitting on [.?!] followed by space+capital,
    # after stripping the trailing terminator.
    s = re.sub(r"[.?!]+\s*$", "", s.strip())
    if not s: return 0
    return len(re.split(r"(?<=[.?!])\s+(?=[A-Z])", s))

def ladder_mech_issues(obj):
    if not isinstance(obj, dict): return ["not-a-json-object"]
    issues = [f"{l}-missing-or-empty" for l in ("L0", "L1", "L2")
              if not isinstance(obj.get(l), str) or not obj.get(l, "").strip()]
    if issues: return issues
    L0, L1, L2 = (obj[l].strip() for l in ("L0", "L1", "L2"))
    if sentence_count(L0) != 1: issues.append("L0-not-1-sentence")
    if w(L0) > 45: issues.append("L0-over-45-words")
    if not 2 <= sentence_count(L1) <= 4: issues.append(f"L1-sentences={sentence_count(L1)}-not-2-4")
    if not 60 <= w(L2) <= 160: issues.append(f"L2-words={w(L2)}-not-60-160")
    if not w(L0) < w(L1) < w(L2): issues.append("word-counts-not-strictly-increasing")
    return issues

def checklist_mech_issues(text):
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    issues = []
    if not 4 <= len(lines) <= 7: issues.append(f"lines={len(lines)}-not-4-7")
    if any(w(l) > 40 for l in lines): issues.append("line-over-40-words")
    return issues

# ---------- strict output schemas (§9-F5: malformed = unparseable) ----------
def parse_json_out(path):
    try: t = Path(path).read_text().strip()
    except OSError: return None
    t = re.sub(r"^```(json)?\s*|```\s*$", "", t, flags=re.M).strip()
    m = re.search(r"[\[{].*[\]}]", t, re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except json.JSONDecodeError: return None

def out_status(path):
    """missing | refused | present — refusal heuristic: CLI error text in place of output."""
    p = Path(path)
    if not p.exists() or not p.read_text().strip(): return "missing"
    head = p.read_text().lstrip()[:200]
    if head.startswith("API Error") or head.startswith("Execution error"): return "refused"
    return "present"

def validate_matrix_rows(rows, n):
    """Exactly one row per excerpt, unique ids 1..n, all three levels, verdicts in enum.
    Returns {i: {L: {verdict, quote}}} or None (= unparseable)."""
    if not isinstance(rows, list) or len(rows) != n: return None
    out = {}
    for r in rows:
        if not isinstance(r, dict): return None
        try: i = int(r.get("excerpt"))
        except (TypeError, ValueError): return None
        if i in out or not 1 <= i <= n: return None
        row = {}
        for lvl in ("L0", "L1", "L2"):
            v = r.get(lvl)
            if isinstance(v, dict): verdict, quote = v.get("verdict"), v.get("quote", "")
            elif isinstance(v, str): verdict, quote = v, ""
            else: return None
            if verdict not in VERDICT_ENUM or not isinstance(quote, str): return None
            row[lvl] = {"verdict": verdict, "quote": quote}
        out[i] = row
    return out

def validate_flat_rows(rows, n, id_key="excerpt", enum=VERDICT_ENUM, extra=("quote",)):
    """verify-pair / symcheck rows: exact 1..n coverage, verdict in enum."""
    if not isinstance(rows, list) or len(rows) != n: return None
    out = {}
    for r in rows:
        if not isinstance(r, dict): return None
        try: i = int(r.get(id_key))
        except (TypeError, ValueError): return None
        if i in out or not 1 <= i <= n: return None
        if r.get("verdict") not in enum: return None
        row = {"verdict": r["verdict"]}
        for k in extra:
            if not isinstance(r.get(k, ""), str): return None
            row[k] = r.get(k, "")
        out[i] = row
    return out

def validate_containment(obj):
    """§9-F5 containment v2 schema: all four keys REQUIRED (round-3 F3); a missing key is
    malformed = unparseable. Quote CONTENT validation happens later; unclear quote-exempt."""
    if not isinstance(obj, dict) or obj.get("relation") not in CONTAIN_ENUM: return None
    for k in ("quote_1", "quote_2", "justification"):
        if k not in obj or not isinstance(obj[k], str): return None
    return {"relation": obj["relation"], "quote_1": obj["quote_1"],
            "quote_2": obj["quote_2"], "justification": obj["justification"]}

def validate_conformance_rows(rows, n):
    """Round-3 F4: dedicated conformance-batch validator. Exact 1..n coverage, verdict in
    enum, reason a string, and NONEMPTY for nonconformant — a bare nonconformant claim may
    not burn an artifact's only regeneration; malformed rows route to the batch re-run."""
    if not isinstance(rows, list) or len(rows) != n: return None
    out = {}
    for r in rows:
        if not isinstance(r, dict): return None
        try: i = int(r.get("item"))
        except (TypeError, ValueError): return None
        if i in out or not 1 <= i <= n: return None
        v = r.get("verdict")
        if v not in ("conformant", "nonconformant"): return None
        reason = r.get("reason")
        if not isinstance(reason, str): return None
        if v == "nonconformant" and not reason.strip(): return None
        out[i] = {"verdict": v, "reason": reason}
    return out

# ---------- excerpts (§2.1, §9-F3/B1: pool = all 11 docs, first-6 prefix sampling) ----------
SENT = re.compile(r"(?<=[.?!])\s+(?=[A-Z“\"(])")
def sentences(text):
    body = " ".join(l.strip() for l in text.splitlines() if l.strip() and not l.startswith("#"))
    return [s.strip() for s in SENT.split(body) if s.strip()]

def extract(pairs):
    terms = side_terms(pairs)
    out = {}
    for side in ("a", "b"):
        out[side] = {}
        for term in terms[side]:
            tre = re.compile(re.escape(term), re.I)
            other_res = [re.compile(re.escape(t), re.I) for t in terms[side] if t != term]
            pool = []
            for f in sorted((BASE / f"corpora/{side}").glob("[0-9][0-9].md")):
                nn = f.stem
                sents = sentences(f.read_text())
                for idx, s in enumerate(sents):
                    if tre.search(s):
                        win = [s]
                        if idx > 0 and not any(o.search(sents[idx - 1]) for o in other_res):
                            win.insert(0, sents[idx - 1])
                        if idx + 1 < len(sents) and not any(o.search(sents[idx + 1]) for o in other_res):
                            win.append(sents[idx + 1])
                        pool.append({"doc": nn, "idx": idx, "text": " ".join(win)})
            out[side][term] = {"pool": pool}
            print(f"{side} '{term}': pool={len(pool)}")
    json.dump(out, open(RUNS / "excerpts.json", "w"), indent=1)
    # floor check (§4: sample < 4 for either term -> pair-scoped insufficientEvidence)
    floor = {"terms": {}, "dead_pairs": {}}
    for p in pairs:
        for side, term in (("a", p["term_a"]), ("b", p["term_b"])):
            n = len(sample_of(out[side][term]))
            floor["terms"][f"{side}:{term}"] = n
            if n < MIN_EXC:
                floor["dead_pairs"].setdefault(p["pair_id"], []).append(f"sample<4:{side}:{term}:n={n}")
    json.dump(floor, open(RUNS / "floor.json", "w"), indent=1)
    print(f"floor: dead pairs = {floor['dead_pairs'] or 'none'}")

def load_exc(): return json.load(open(RUNS / "excerpts.json"))
def load_floor(): return json.load(open(RUNS / "floor.json"))

def sample_of(entry):
    """§2.1/§9-F3(B1): first 6 pool excerpts in (doc, position) order, pool = docs 01-11."""
    s = entry["pool"][:N_SAMPLE]
    for e in s:
        assert 1 <= int(e["doc"]) <= POOL_MAX_DOC, f"pool violation: sampled doc {e['doc']}"
    return s

def mask_text(text, side, term, all_terms, mask=MASK):
    text = re.compile(re.escape(term), re.I).sub(mask, text)
    for t in all_terms[side]:
        if t != term: text = re.compile(re.escape(t), re.I).sub("⟦X⟧", text)
    return text

def numbered(sample, side, term, all_terms, mask=MASK):
    return "\n".join(f"{i+1}. {mask_text(e['text'], side, term, all_terms, mask)}"
                     for i, e in enumerate(sample))

# ---------- corpus manifests (§1/§8: exactly docs 01-11) ----------
def regen_manifests():
    for side in ("a", "b"):
        d = BASE / f"corpora/{side}"
        files = sorted(d.glob("[0-9][0-9].md"))
        names = [f.stem for f in files]
        assert names == [f"{i:02d}" for i in range(1, 12)], f"corpus {side} is not exactly 01-11: {names}"
        mf = d / "manifest.json"
        old = json.load(open(mf)) if mf.exists() else {}
        new = {}
        for f in files:
            h = sha(f.read_text().strip())
            if f.stem in old and old[f.stem] != h:
                sys.exit(f"CORPUS DRIFT: {side}/{f.stem}.md hash changed vs manifest — aborting")
            new[f.stem] = h
        json.dump(new, open(mf, "w"), indent=1)
        print(f"corpora/{side}/manifest.json: exactly {len(new)} docs (01-11), hashes verified")

# ---------- artifact gate state machine (§1, §9-F4) ----------
# states: awaiting_output -> (gates) -> passed | pending_regen -> (gates) -> passed | configFail
# ladders pass mech+leak into awaiting_semantic, then conformance -> passed.
GATEF = None
def _gatef(): return RUNS / "gate-state.json"
def gate_load():
    f = _gatef()
    return json.load(open(f)) if f.exists() else {"artifacts": {}, "conf_batches": {},
                                                  "polarity": {}, "polarity_side_fail": []}
def gate_save(st): json.dump(st, open(_gatef(), "w"), indent=1)

def aid(kind, side, term): return f"{kind}:{side}:{term}"

def configfail_terms(st):
    out = {"a": set(), "b": set()}
    for k, a in st["artifacts"].items():
        if a["state"] == "configFail":
            _, side, term = k.split(":", 2)
            out[side].add(term)
    return out

def alive_pairs(pairs, st, floor, with_polarity=True):
    """Pairs not floor-dead and not configFail (gate exhaustion, polarity)."""
    cf = configfail_terms(st)
    inv = polarity_inverted(st) if with_polarity else {"a": set(), "b": set()}
    out = []
    for p in pairs:
        if p["pair_id"] in floor["dead_pairs"]: continue
        if p["term_a"] in cf["a"] or p["term_b"] in cf["b"]: continue
        if st.get("polarity_side_fail"): continue
        if p["term_a"] in inv["a"] or p["term_b"] in inv["b"]: continue
        out.append(p)
    return out

def leak_ok(path):
    r = subprocess.run([str(BASE / "leakcheck_peer.sh"), "def", str(path)],
                       capture_output=True, text=True)
    return r.returncode == 0, r.stdout.strip()

# ---------- call-attempt bookkeeping (round-3 F2: resume must not burn a queued retry) ----------
# run_isolated.sh writes the manifest BEFORE invoking the CLI and appends "out_sha256: ..."
# + "exit: 0" only on success. So: no manifest = never attempted (re-stage, no budget);
# manifest without clean exit + output present = interrupted (§4 run-scoped, re-exec, logged);
# manifest without clean exit + output missing = attempted-and-failed (route per §1/§9-F4).
def call_attempted(manifest): return Path(manifest).exists()

def call_completed(out, manifest):
    m, o = Path(manifest), Path(out)
    if not (m.exists() and o.exists()): return False
    txt = m.read_text()
    if not re.search(r"^exit: 0$", txt, re.M): return False
    h = re.search(r"^out_sha256: ([0-9a-f]{64})$", txt, re.M)
    return bool(h) and hashlib.sha256(o.read_bytes()).hexdigest() == h.group(1)

GEN_DIR = {"chk": "checklists", "lad": "definitions"}
GEN_EXT = {"chk": "txt", "lad": "json"}
def manifest_for(kind, side, term, g):
    tag = {"chk": "chk", "lad": "def"}[kind]
    return RUNS / f"manifests/{tag}-{side}-{slug(term)}-g{g}.json"

def gen_call_row(a, g):
    kind = a["kind"]
    cli, model = (("claude", "sonnet") if kind == "chk" else (a["cli"], a["model"]))
    prompt = RUNS / f"{GEN_DIR[kind]}/prompt-{a['side']}-{slug(a['term'])}.md"
    return (f"{cli}\t{model}\t{prompt}\t"
            f"{gen_path(kind, a['side'], a['term'], g, GEN_EXT[kind])}\t"
            f"{manifest_for(kind, a['side'], a['term'], g)}")

def gen_path(kind, side, term, g, ext): return RUNS / {"chk": "checklists", "lad": "definitions"}[kind] / f"out-{side}-{slug(term)}-g{g}.{ext}"
def canon_path(kind, side, term, ext): return RUNS / {"chk": "checklists", "lad": "definitions"}[kind] / f"out-{side}-{slug(term)}.{ext}"

def stage_call(tsv_rows, kind_cli, model, prompt, out, manifest):
    tsv_rows.append(f"{kind_cli}\t{model}\t{prompt}\t{out}\t{manifest}")

def prompts_checklist(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    tmpl = (BASE / "prompts/checklist-extract.md").read_text()
    (RUNS / "checklists").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in alive_pairs(pairs, st, floor, with_polarity=False):
        for side, term in (("a", p["term_a"]), ("b", p["term_b"])):
            a = st["artifacts"].setdefault(aid("chk", side, term),
                {"kind": "chk", "side": side, "term": term, "regens_used": 0,
                 "state": "awaiting_output", "log": []})
            pf = RUNS / f"checklists/prompt-{side}-{slug(term)}.md"
            pf.write_text(tmpl + "\n" + numbered(exc[side][term]["pool"], side, term, terms))
            stage_call(rows, "claude", "sonnet", pf, gen_path("chk", side, term, 0, "txt"),
                       RUNS / f"manifests/chk-{side}-{slug(term)}-g0.json")
    (RUNS / "checklists/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    gate_save(st)
    print(f"{len(rows)} checklist calls staged")

def _route_fail(st, a, gate, detail, regen_rows):
    """§1 state machine: first failure consumes the one regen budget; second -> configFail."""
    if a["regens_used"] == 0:
        a["regens_used"] = 1; a["state"] = "pending_regen"
        a["log"].append(f"gate-fail[{gate}] g0: {detail} -> regeneration staged")
        regen_rows.append(gen_call_row(a, a["regens_used"]))
    else:
        a["state"] = "configFail"; a["failed_gate"] = gate
        a["log"].append(f"gate-fail[{gate}] g{a['regens_used']}: {detail} -> configFail (budget exhausted)")

def _gen_attempt_state(a, regen_rows):
    """Round-3 F2 preamble. Returns the output path if the g-th call completed cleanly,
    else None after re-staging (never-attempted / interrupted, no budget) or routing
    (attempted-and-failed, budget)."""
    g = a["regens_used"]
    f = gen_path(a["kind"], a["side"], a["term"], g, GEN_EXT[a["kind"]])
    mf = manifest_for(a["kind"], a["side"], a["term"], g)
    if not call_attempted(mf):
        regen_rows.append(gen_call_row(a, g))
        a["log"].append(f"g{g} not yet executed -> staged (no budget consumed)")
        return None
    if not call_completed(f, mf):
        if f.exists():
            f.unlink(); mf.unlink()
            regen_rows.append(gen_call_row(a, g))
            a["log"].append(f"g{g} interrupted -> re-exec staged (§4 run-scoped, logged)")
            return None
        _route_fail(None, a, "generate", "call-failed", regen_rows)
        return None
    return f

def gate_checklists(pairs):
    st = gate_load()
    regen_rows = []
    for k, a in st["artifacts"].items():
        if a["kind"] != "chk" or a["state"] not in ("awaiting_output", "pending_regen"): continue
        f = _gen_attempt_state(a, regen_rows)
        if f is None: continue
        g = a["regens_used"]
        if out_status(f) != "present":
            _route_fail(st, a, "generate", out_status(f), regen_rows); continue
        issues = checklist_mech_issues(f.read_text())
        if issues:
            _route_fail(st, a, "mechanical", ";".join(issues), regen_rows); continue
        ok, leaks = leak_ok(f)
        if not ok:
            _route_fail(st, a, "leak", leaks, regen_rows); continue
        canon_path("chk", a["side"], a["term"], "txt").write_text(f.read_text())
        a["state"] = "passed"; a["log"].append(f"passed at g{g}")
    (RUNS / "checklists/regen-calls.tsv").write_text("\n".join(regen_rows) + ("\n" if regen_rows else ""))
    gate_save(st)
    n = {s: sum(1 for a in st["artifacts"].values() if a["kind"] == "chk" and a["state"] == s)
         for s in ("passed", "pending_regen", "configFail")}
    print(f"checklist gates: {n}; {len(regen_rows)} rows staged")

def prompts_def(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    tmpl = (BASE / "prompts/gen-definition-v07.md").read_text()
    (RUNS / "definitions").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in alive_pairs(pairs, st, floor, with_polarity=False):
        for side, term, cli, model in (("a", p["term_a"], "claude", "opus"),
                                       ("b", p["term_b"], "codex", "gpt-5.6-terra")):
            if st["artifacts"].get(aid("chk", side, term), {}).get("state") != "passed": continue
            a = st["artifacts"].setdefault(aid("lad", side, term),
                {"kind": "lad", "side": side, "term": term, "regens_used": 0,
                 "state": "awaiting_output", "log": [], "cli": cli, "model": model})
            chk = canon_path("chk", side, term, "txt").read_text().strip()
            pf = RUNS / f"definitions/prompt-{side}-{slug(term)}.md"
            pf.write_text(tmpl.replace("{CHECKLIST}", chk) + "\n"
                          + numbered(exc[side][term]["pool"], side, term, terms))
            stage_call(rows, cli, model, pf, gen_path("lad", side, term, 0, "json"),
                       RUNS / f"manifests/def-{side}-{slug(term)}-g0.json")
    (RUNS / "definitions/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    gate_save(st)
    print(f"{len(rows)} ladder calls staged")

def gate_ladders(pairs):
    """§2.4a mechanical + leak; §1 order: generate -> JSON/mechanical -> leak -> semantic."""
    st = gate_load()
    regen_rows = []
    for k, a in st["artifacts"].items():
        if a["kind"] != "lad" or a["state"] not in ("awaiting_output", "pending_regen"): continue
        f = _gen_attempt_state(a, regen_rows)
        if f is None: continue
        g = a["regens_used"]
        if out_status(f) != "present":
            _route_fail(st, a, "generate", out_status(f), regen_rows); continue
        obj = parse_json_out(f)
        issues = ladder_mech_issues(obj) if obj is not None else ["unparseable-json"]
        if issues:
            _route_fail(st, a, "mechanical", ";".join(issues), regen_rows); continue
        ok, leaks = leak_ok(f)
        if not ok:
            _route_fail(st, a, "leak", leaks, regen_rows); continue
        canon_path("lad", a["side"], a["term"], "json").write_text(
            json.dumps({l: obj[l].strip() for l in ("L0", "L1", "L2")}, indent=1))
        a["state"] = "awaiting_semantic"; a["log"].append(f"mech+leak passed at g{g}")
    (RUNS / "definitions/regen-calls.tsv").write_text("\n".join(regen_rows) + ("\n" if regen_rows else ""))
    gate_save(st)
    n = {s: sum(1 for a in st["artifacts"].values() if a["kind"] == "lad" and a["state"] == s)
         for s in ("awaiting_semantic", "passed", "pending_regen", "configFail")}
    print(f"ladder mech+leak gates: {n}; {len(regen_rows)} rows staged")

def read_ladder(side, term):
    return json.loads(canon_path("lad", side, term, "json").read_text())

def prompts_conformance(pairs):
    """§2.4b: one isolated sonnet call per side, batched over terms awaiting semantic check."""
    st = gate_load()
    tmpl = (BASE / "prompts/ladder-conformance.md").read_text()
    (RUNS / "conformance").mkdir(parents=True, exist_ok=True)
    rows = []
    inflight = set()  # resume guard: terms already in an unresolved batch are not re-staged
    for bid, b in st["conf_batches"].items():
        if not b["resolved"]:
            m = json.load(open(RUNS / f"conformance/batch-{bid}.json"))
            inflight.update((m["side"], t) for t in m["terms"])
    for side in ("a", "b"):
        batch = [a for a in st["artifacts"].values()
                 if a["kind"] == "lad" and a["side"] == side and a["state"] == "awaiting_semantic"
                 and (side, a["term"]) not in inflight]
        if not batch: continue
        wave = 1 + len(list((RUNS / "conformance").glob(f"batch-{side}-w*.json")))
        items, members = [], []
        for i, a in enumerate(sorted(batch, key=lambda x: x["term"])):
            lad = read_ladder(side, a["term"])
            chk = canon_path("chk", side, a["term"], "txt").read_text().strip()
            items.append(f"ITEM {i+1}\nCHECKLIST:\n{chk}\nLADDER:\nL0: {lad['L0']}\nL1: {lad['L1']}\nL2: {lad['L2']}\n")
            members.append(a["term"])
        pf = RUNS / f"conformance/prompt-{side}-w{wave}.md"
        pf.write_text(tmpl + "\n" + "\n".join(items))
        bid = f"{side}-w{wave}"
        json.dump({"side": side, "terms": members}, open(RUNS / f"conformance/batch-{bid}.json", "w"))
        st["conf_batches"].setdefault(bid, {"reruns_used": 0, "resolved": False})
        stage_call(rows, "claude", "sonnet", pf, RUNS / f"conformance/out-{bid}-r0.json",
                   RUNS / f"manifests/conf-{bid}-r0.json")
    (RUNS / "conformance/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    gate_save(st)
    print(f"{len(rows)} conformance batch calls staged")

def gate_conformance(pairs):
    st = gate_load()
    regen_rows, rerun_rows = [], []
    for bid, b in sorted(st["conf_batches"].items()):
        if b["resolved"]: continue
        meta = json.load(open(RUNS / f"conformance/batch-{bid}.json"))
        side, members = meta["side"], meta["terms"]
        r = b["reruns_used"]
        f = RUNS / f"conformance/out-{bid}-r{r}.json"
        mf = RUNS / f"manifests/conf-{bid}-r{r}.json"
        # round-3 F2: never-attempted / interrupted attempts are re-staged, no budget
        if not call_attempted(mf):
            stage_call(rerun_rows, "claude", "sonnet", RUNS / f"conformance/prompt-{bid}.md", f, mf)
            continue
        if not call_completed(f, mf) and f.exists():
            f.unlink(); mf.unlink()
            stage_call(rerun_rows, "claude", "sonnet", RUNS / f"conformance/prompt-{bid}.md", f, mf)
            print(f"conformance {bid} r{r}: interrupted -> re-exec staged (§4 run-scoped, logged)")
            continue
        rows = parse_json_out(f) if call_completed(f, mf) else None
        valid = validate_conformance_rows(rows, len(members)) if rows else None
        if valid is None:
            # §9-F4: conformance-judge batch failure -> one re-run, then run-halt
            if b["reruns_used"] == 0:
                b["reruns_used"] = 1
                f.unlink(missing_ok=True)
                stage_call(rerun_rows, "claude", "sonnet", RUNS / f"conformance/prompt-{bid}.md",
                           RUNS / f"conformance/out-{bid}-r1.json", RUNS / f"manifests/conf-{bid}-r1.json")
                continue
            gate_save(st)
            sys.exit(f"RUN-HALT: conformance batch {bid} failed twice (§9-F4)")
        b["resolved"] = True
        for i, term in enumerate(members, 1):
            a = st["artifacts"][aid("lad", side, term)]
            if valid[i]["verdict"] == "conformant":
                a["state"] = "passed"; a["log"].append(f"semantic conformant ({bid})")
            else:
                _route_fail(st, a, "semantic", valid[i]["reason"], regen_rows)
    (RUNS / "definitions/regen-calls.tsv").write_text("\n".join(regen_rows) + ("\n" if regen_rows else ""))
    (RUNS / "conformance/rerun-calls.tsv").write_text("\n".join(rerun_rows) + ("\n" if rerun_rows else ""))
    gate_save(st)
    n = {s: sum(1 for a in st["artifacts"].values() if a["kind"] == "lad" and a["state"] == s)
         for s in ("passed", "awaiting_semantic", "pending_regen", "configFail")}
    print(f"conformance gates: {n}; ladder regens: {len(regen_rows)}; batch rows: {len(rerun_rows)}")

def assert_resolved(pairs):
    st = gate_load()
    bad = {k: a["state"] for k, a in st["artifacts"].items()
           if a["state"] not in ("passed", "configFail")}
    if bad: sys.exit(f"UNRESOLVED ARTIFACTS after gate waves: {bad}")
    print("all artifacts resolved (passed or configFail)")

# ---------- polarity (§2.5, §9-F4) ----------
def prompts_polarity(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    tmpl = (BASE / "prompts/polarity-check.md").read_text()
    (RUNS / "polarity").mkdir(parents=True, exist_ok=True)
    rows, live = [], alive_pairs(pairs, st, floor, with_polarity=False)
    order = {"a": [], "b": []}
    for side, judge_cli, judge_model in (("a", "codex", "gpt-5.6-terra"), ("b", "claude", "opus")):
        items = []
        for p in live:
            term = p["term_a"] if side == "a" else p["term_b"]
            if st["artifacts"].get(aid("lad", side, term), {}).get("state") != "passed": continue
            samp = sample_of(exc[side][term])
            items.append(f"ITEM {len(items)+1}\nEXCERPTS:\n{numbered(samp, side, term, terms)}\n"
                         f"DEFINITION:\n{read_ladder(side, term)['L2']}\n")
            order[side].append(term)
        if not items: continue
        pf = RUNS / f"polarity/prompt-{side}.md"
        pf.write_text(tmpl + "\n" + "\n".join(items))
        st["polarity"].setdefault(side, {"reruns_used": 0, "resolved": False})
        stage_call(rows, judge_cli, judge_model, pf, RUNS / f"polarity/out-{side}-r0.json",
                   RUNS / f"manifests/polarity-{side}-r0.json")
    json.dump(order, open(RUNS / "polarity/terms.json", "w"))
    (RUNS / "polarity/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    gate_save(st)
    print(f"{len(rows)} polarity calls staged")

def gate_polarity(pairs):
    st = gate_load()
    order = json.load(open(RUNS / "polarity/terms.json"))
    rerun_rows = []
    judges = {"a": ("codex", "gpt-5.6-terra"), "b": ("claude", "opus")}
    verdicts = json.load(open(RUNS / "polarity/verdicts.json")) if (RUNS / "polarity/verdicts.json").exists() else {}
    for side, pstate in sorted(st["polarity"].items()):
        if pstate["resolved"]: continue
        r = pstate["reruns_used"]
        f = RUNS / f"polarity/out-{side}-r{r}.json"
        mf = RUNS / f"manifests/polarity-{side}-r{r}.json"
        cli, model = judges[side]
        # round-3 F2: never-attempted / interrupted attempts are re-staged, no budget
        if not call_attempted(mf):
            stage_call(rerun_rows, cli, model, RUNS / f"polarity/prompt-{side}.md", f, mf)
            continue
        if not call_completed(f, mf) and f.exists():
            f.unlink(); mf.unlink()
            stage_call(rerun_rows, cli, model, RUNS / f"polarity/prompt-{side}.md", f, mf)
            print(f"polarity {side} r{r}: interrupted -> re-exec staged (§4 run-scoped, logged)")
            continue
        rows = parse_json_out(f) if call_completed(f, mf) else None
        valid = validate_flat_rows(rows, len(order[side]), id_key="item",
                                   enum={"ok", "inverted"}, extra=()) if rows else None
        if valid is None:
            # §9-F4: polarity batch missing/unparseable/refused -> one re-run, then side-scoped configFail
            if pstate["reruns_used"] == 0:
                pstate["reruns_used"] = 1
                f.unlink(missing_ok=True)
                cli, model = judges[side]
                stage_call(rerun_rows, cli, model, RUNS / f"polarity/prompt-{side}.md",
                           RUNS / f"polarity/out-{side}-r1.json", RUNS / f"manifests/polarity-{side}-r1.json")
                continue
            pstate["resolved"] = True
            st["polarity_side_fail"].append(side)
            print(f"polarity side {side}: batch failed twice -> side-scoped configFail (§9-F4)")
            continue
        pstate["resolved"] = True
        verdicts[side] = {order[side][i-1]: valid[i]["verdict"] for i in valid}
    json.dump(verdicts, open(RUNS / "polarity/verdicts.json", "w"), indent=1)
    (RUNS / "polarity/rerun-calls.tsv").write_text("\n".join(rerun_rows) + ("\n" if rerun_rows else ""))
    gate_save(st)
    inv = polarity_inverted(st)
    print(f"polarity gates: inverted={ {s: sorted(v) for s, v in inv.items()} }; reruns: {len(rerun_rows)}")

def polarity_inverted(st):
    f = RUNS / "polarity/verdicts.json"
    v = json.load(open(f)) if f.exists() else {}
    return {s: {t for t, verdict in v.get(s, {}).items() if verdict == "inverted"} for s in ("a", "b")}

def emit_alive(pairs):
    st = gate_load(); floor = load_floor()
    live = alive_pairs(pairs, st, floor)
    out = {p["pair_id"]: {"term_a": p["term_a"], "term_b": p["term_b"],
                          "L2_a": str(canon_path("lad", "a", p["term_a"], "json")),
                          "L2_b": str(canon_path("lad", "b", p["term_b"], "json"))} for p in live}
    json.dump(out, open(RUNS / "alive-pairs.json", "w"), indent=1)
    print(f"{len(out)} alive pairs -> runs/alive-pairs.json")

# ---------- matrix verification (§2.7) ----------
def prompts_verify(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    tmpl = (BASE / "prompts/verify-matrix.md").read_text()
    (RUNS / "verify").mkdir(parents=True, exist_ok=True)
    rows, meta = [], {}
    for p in alive_pairs(pairs, st, floor):
        pid = p["pair_id"]
        # §2.7 direction identities (F3): a2b = D_A vs E_B (judge opus); b2a = D_B vs E_A (judge codex)
        for d, dside, eside, cli, model in (("a2b", "a", "b", "claude", "opus"),
                                            ("b2a", "b", "a", "codex", "gpt-5.6-terra")):
            dterm = p["term_a"] if dside == "a" else p["term_b"]
            eterm = p["term_b"] if eside == "b" else p["term_a"]
            samp = sample_of(exc[eside][eterm])
            meta[f"{pid}-{d}"] = {"n": len(samp), "excerpts": samp, "term": eterm, "eside": eside}
            lad = read_ladder(dside, dterm)
            body = (tmpl.replace("{D0}", lad["L0"]).replace("{D1}", lad["L1"])
                        .replace("{D2}", lad["L2"]) + "\n" + numbered(samp, eside, eterm, terms))
            pf = RUNS / f"verify/prompt-{pid}-{d}.md"; pf.write_text(body)
            stage_call(rows, cli, model, pf, RUNS / f"verify/out-{pid}-{d}.json",
                       RUNS / f"manifests/verify-{pid}-{d}.json")
    (RUNS / "verify/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    json.dump(meta, open(RUNS / "verify/meta.json", "w"), indent=1)
    print(f"{len(rows)} verify calls staged")

# ---------- aggregation (§2.7) ----------
def level_verdict(lrows, masked_texts, quote_required):
    """lrows: {i: {verdict, quote}} over 1..n; masked_texts[i-1] = what the judge saw."""
    k = c = u = 0; pre_decided = 0; downgrades = []
    for i in sorted(lrows):
        v, q = lrows[i]["verdict"], norm(lrows[i].get("quote", ""))
        if v in ("instantiates", "contradicts"):
            pre_decided += 1
            if quote_required and (not q or q not in norm(masked_texts[i-1])):
                downgrades.append(i); v = "insufficient"
        k += v == "instantiates"; c += v == "contradicts"; u += v == "insufficient"
    dec = k + c
    if dec < 2: agg = "abstain"
    elif k >= 2 and c == 0: agg = "covers"
    elif c >= 2 or k / dec <= 0.3: agg = "fails"
    else: agg = "mixed"
    return {"n": len(lrows), "k": k, "c": c, "u": u, "pre_decided": pre_decided,
            "agg": agg, "quote_downgrades": downgrades}

def matrix_direction(valid, masked_texts):
    levels = {lvl: level_verdict({i: valid[i][lvl] for i in valid}, masked_texts,
                                 quote_required=(lvl != "L0"))
              for lvl in ("L0", "L1", "L2")}
    order = ("L0", "L1", "L2")
    L = max((i for i, l in enumerate(order) if levels[l]["agg"] == "covers"), default=-1)
    monotone = not any(levels[l]["agg"] == "fails" for i, l in enumerate(order) if i < L)
    starved = all(levels[l]["k"] + levels[l]["c"] < 2 for l in order)
    collapsed = (starved and any(levels[l]["quote_downgrades"] for l in order)
                 and any(levels[l]["pre_decided"] >= 2 for l in order))
    return {"status": "ok", "levels": levels, "L": L, "monotone": monotone,
            "starved": starved, "collapsed": collapsed}

def masked_sample_texts(meta_entry, terms):
    side, term = meta_entry["eside"], meta_entry["term"]
    return [mask_text(e["text"], side, term, terms) for e in meta_entry["excerpts"]]

def aggregate(pairs):
    st = gate_load(); floor = load_floor(); terms = side_terms(pairs)
    meta = json.load(open(RUNS / "verify/meta.json"))
    agg = {}
    for p in alive_pairs(pairs, st, floor):
        pid = p["pair_id"]; agg[pid] = {}
        for d in ("a2b", "b2a"):
            f = RUNS / f"verify/out-{pid}-{d}.json"
            status = out_status(f)
            if status != "present":
                agg[pid][d] = {"status": status}; continue
            mm = meta[f"{pid}-{d}"]
            valid = validate_matrix_rows(parse_json_out(f), mm["n"])
            if valid is None:
                agg[pid][d] = {"status": "unparseable"}; continue
            agg[pid][d] = matrix_direction(valid, masked_sample_texts(mm, terms))
    json.dump(agg, open(RUNS / "agg.json", "w"), indent=1)
    print(f"aggregated {len(agg)} pairs -> runs/agg.json")

# ---------- pre-table terminal check (§4, order as written) ----------
def pretable_status(pair, ctx):
    """Returns (kind, reason) with kind in {'configFail','insufficientEvidence',None}."""
    if ctx.get("configfail"): return "configFail", ctx["configfail"]
    if ctx.get("floor_fail"): return "insufficientEvidence", ctx["floor_fail"]
    for d in ("a2b", "b2a"):
        s = ctx["dirs"][d].get("status", "missing")
        if s != "ok": return "insufficientEvidence", f"verify-{d}-{s}"
    for d in ("a2b", "b2a"):
        if ctx["dirs"][d]["collapsed"]: return "insufficientEvidence", f"quote-collapse-{d}"
    for d in ("a2b", "b2a"):
        if not ctx["dirs"][d]["monotone"]: return "insufficientEvidence", f"non-monotone-{d}"
    if ctx["dirs"]["a2b"]["starved"] and ctx["dirs"]["b2a"]["starved"]:
        return "insufficientEvidence", "both-directions-starved"
    return None, None

# ---------- composition (§5) ----------
def deep_c(dirres):
    """§5: deep-c = c >= 2 at L1 in the direction's matrix (L1-pinned, §0.5)."""
    return dirres["levels"]["L1"]["c"] >= 2

def _v(rel, status, reason=None, broader=None):
    out = {"proposed_relation": rel, "status": status, "reason": reason}
    if broader: out["broader_side"] = broader
    return out

def compose_pair(pair, ctx):
    """Pure §4+§5 composition. ctx: configfail, floor_fail, dirs{a2b,b2a}, symcheck,
    mutual, decompose, containment, flag. Lazily-staged stages may be None; the table
    decides whether they were required (missing-when-required -> insufficientEvidence)."""
    kind, reason = pretable_status(pair, ctx)
    if kind == "configFail": return _v(None, "config_fail", reason)
    if kind == "insufficientEvidence": return _v(None, "insufficient_evidence", reason)
    A, B = ctx["dirs"]["a2b"], ctx["dirs"]["b2a"]
    La, Lb = A["L"], B["L"]
    flag = ctx["flag"]
    if La == 2 and Lb == 2: return _v("exactMatch", "asserted")
    if (La, Lb) in ((2, 1), (1, 2)): return _v(None, "review_required", "detail-divergence")
    if (La == 2 and Lb <= 0) or (Lb == 2 and La <= 0):
        failing, covering = ("b2a", "a") if La == 2 else ("a2b", "b")
        if not deep_c(ctx["dirs"][failing]):
            return _v(None, "review_required", "unexplained-asymmetry")
        sc = ctx.get("symcheck")
        if sc is None or sc.get("status") != "ok":
            return _v(None, "insufficient_evidence",
                      f"symcheck-{sc.get('status') if sc else 'missing'}")
        if sc["confirms"]: return _v("broadnarrow", "asserted", broader=covering)
        return _v(None, "review_required", "asymmetry-unconfirmed")
    # path P — the remaining 9 cells: (1,1) (1,0) (0,1) (1,-1) (-1,1) (0,0) (0,-1) (-1,0) (-1,-1)
    if not ctx.get("mutual"):
        return _v("noMatchDespiteSimilarity" if flag else "noMatch", "asserted")
    dc = ctx.get("decompose")
    if dc is None or dc.get("status") == "fail":
        return _v(None, "insufficient_evidence",
                  f"decompose-{dc.get('detail', 'missing') if dc else 'missing'}")
    if dc["status"] == "abstain":
        return _v("noMatchDespiteSimilarity" if flag else "noMatch", "asserted")
    ct = ctx.get("containment")
    if ct is None or ct.get("status") != "ok":
        return _v(None, "insufficient_evidence",
                  f"containment-{ct.get('detail', 'missing') if ct else 'missing'}")
    rel = ct["relation"]
    if rel == "t1_within_t2": return _v("broadnarrow", "asserted", broader="b")
    if rel == "t2_within_t1": return _v("broadnarrow", "asserted", broader="a")
    if rel == "partial_overlap": return _v("relatedMatch", "asserted")
    if rel == "no_relation":
        return _v("noMatchDespiteSimilarity" if flag else "noMatch", "asserted")
    return _v(None, "review_required", "containment-unclear")  # unclear

# ---------- surface-similarity flag (§5, exact) ----------
def trigrams(s):
    s = re.sub(r"[^a-z0-9]", "", s)
    return {s[i:i+3] for i in range(max(0, len(s) - 2))}

def sim_flag(ta, tb):
    na, nb = norm(ta), norm(tb)
    if na == nb: return True
    Sa, Sb = re.sub(r"[^a-z0-9]", "", na), re.sub(r"[^a-z0-9]", "", nb)
    if len(Sa) < 3 or len(Sb) < 3: return False  # only clause (i) can fire
    A, B = trigrams(na), trigrams(nb)
    return bool(A) and len(A & B) / len(A | B) >= 0.5

# ---------- retrieval ranking (§2.6/§9-F7; imported by retrieve_xc.py) ----------
def rank_top3(sims):
    return sorted(range(len(sims)), key=lambda i: (-sims[i], i))[:3]

# ---------- symcheck / decompose / containment staging ----------
def _row3_candidate(pid, agg, pairs_by_id):
    """Returns (failing_direction, covering_side) if the pair sits in table row 3 with deep-c."""
    A, B = agg[pid]["a2b"], agg[pid]["b2a"]
    if A.get("status") != "ok" or B.get("status") != "ok": return None
    if not (A["monotone"] and B["monotone"]): return None
    if A["starved"] and B["starved"]: return None
    if A["collapsed"] or B["collapsed"]: return None
    La, Lb = A["L"], B["L"]
    if La == 2 and Lb <= 0 and deep_c(B): return ("b2a", "a")
    if Lb == 2 and La <= 0 and deep_c(A): return ("a2b", "b")
    return None

def prompts_symcheck(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    agg = json.load(open(RUNS / "agg.json"))
    meta = json.load(open(RUNS / "verify/meta.json"))
    tmpl = (BASE / "prompts/verify-pair.md").read_text()
    (RUNS / "symcheck").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in alive_pairs(pairs, st, floor):
        pid = p["pair_id"]
        cand = _row3_candidate(pid, agg, None)
        if not cand: continue
        d, _ = cand
        # §2.8: the failing direction's L1 definition, re-judged by the OTHER family
        # (b2a was judged by codex -> opus re-judges; a2b was judged by opus -> codex re-judges)
        cli, model = (("claude", "opus") if d == "b2a" else ("codex", "gpt-5.6-terra"))
        dside = "a" if d == "a2b" else "b"
        dterm = p["term_a"] if dside == "a" else p["term_b"]
        mm = meta[f"{pid}-{d}"]
        body = (tmpl.replace("{DEFINITION}", read_ladder(dside, dterm)["L1"]) + "\n"
                + numbered(mm["excerpts"], mm["eside"], mm["term"], terms))
        pf = RUNS / f"symcheck/prompt-{pid}-{d}.md"; pf.write_text(body)
        stage_call(rows, cli, model, pf, RUNS / f"symcheck/out-{pid}-{d}.json",
                   RUNS / f"manifests/symcheck-{pid}-{d}.json")
    (RUNS / "symcheck/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    print(f"{len(rows)} symcheck calls staged")

def symcheck_result(pid, d, meta, terms, root=None):
    """None if no output; {'status','confirms'} otherwise. Confirmation = fails with
    c >= 2 at L1 under the same aggregation (§2.8), quote-validated.
    root: alternate run tree (v0.9 resample passes runs/v09); default = the v0.8 tree."""
    f = (root or RUNS) / f"symcheck/out-{pid}-{d}.json"
    status = out_status(f)
    if status != "present": return {"status": status}
    mm = meta[f"{pid}-{d}"]
    valid = validate_flat_rows(parse_json_out(f), mm["n"])
    if valid is None: return {"status": "unparseable"}
    lv = level_verdict(valid, masked_sample_texts(mm, terms), quote_required=True)
    return {"status": "ok", "confirms": lv["agg"] == "fails" and lv["c"] >= 2, "counts": lv}

def _pathP_pairs(pairs, st, floor, agg):
    out = []
    for p in alive_pairs(pairs, st, floor):
        pid = p["pair_id"]
        A, B = agg[pid]["a2b"], agg[pid]["b2a"]
        if A.get("status") != "ok" or B.get("status") != "ok": continue
        if not (A["monotone"] and B["monotone"]): continue
        if A["starved"] and B["starved"]: continue
        if A["collapsed"] or B["collapsed"]: continue
        if A["L"] == 2 or B["L"] == 2: continue  # rows 1-5 handled elsewhere
        out.append(p)
    return out

def prompts_decompose(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    agg = json.load(open(RUNS / "agg.json"))
    retr = json.load(open(RUNS / "retrieval.json"))
    tmpl = (BASE / "prompts/decompose.md").read_text()
    (RUNS / "decompose").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in _pathP_pairs(pairs, st, floor, agg):
        pid = p["pair_id"]
        if not retr.get(pid, {}).get("mutual"): continue
        s1 = sample_of(exc["a"][p["term_a"]]); s2 = sample_of(exc["b"][p["term_b"]])
        e1 = numbered(s1, "a", p["term_a"], terms, "⟦T1⟧")
        e2 = numbered(s2, "b", p["term_b"], terms, "⟦T2⟧")
        pf = RUNS / f"decompose/prompt-{pid}.md"
        pf.write_text(tmpl.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        stage_call(rows, "claude", "sonnet", pf, RUNS / f"decompose/out-{pid}.json",
                   RUNS / f"manifests/decompose-{pid}.json")
    (RUNS / "decompose/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    print(f"{len(rows)} decompose calls staged")

def decompose_result(pid, pair, exc, terms, root=None):
    """§2.9: ABSTAIN = valid semantic outcome; unparseable/missing/failed-quote = infra fail."""
    f = (root or RUNS) / f"decompose/out-{pid}.json"
    status = out_status(f)
    if status != "present": return {"status": "fail", "detail": status}
    t = re.sub(r"^```(json)?\s*|```\s*$", "", f.read_text().strip(), flags=re.M).strip()
    if t == "ABSTAIN": return {"status": "abstain"}
    obj = parse_json_out(f)
    if not isinstance(obj, dict) or not isinstance(obj.get("core"), str) or not obj.get("core") \
       or not isinstance(obj.get("quote_1", ""), str) or not isinstance(obj.get("quote_2", ""), str):
        return {"status": "fail", "detail": "unparseable"}
    s1 = sample_of(exc["a"][pair["term_a"]]); s2 = sample_of(exc["b"][pair["term_b"]])
    q1, q2 = norm(obj.get("quote_1", "")), norm(obj.get("quote_2", ""))
    ok1 = bool(q1) and any(q1 in norm(mask_text(e["text"], "a", pair["term_a"], terms, "⟦T1⟧")) for e in s1)
    ok2 = bool(q2) and any(q2 in norm(mask_text(e["text"], "b", pair["term_b"], terms, "⟦T2⟧")) for e in s2)
    if not (ok1 and ok2): return {"status": "fail", "detail": "quote-validation"}
    return {"status": "ok", "core": obj["core"],
            "quote_1": obj.get("quote_1", ""), "quote_2": obj.get("quote_2", "")}

def prompts_containment(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    agg = json.load(open(RUNS / "agg.json"))
    retr = json.load(open(RUNS / "retrieval.json"))
    tmpl = (BASE / "prompts/containment-v2.md").read_text()
    (RUNS / "containment").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in _pathP_pairs(pairs, st, floor, agg):
        pid = p["pair_id"]
        if not retr.get(pid, {}).get("mutual"): continue
        if decompose_result(pid, p, exc, terms)["status"] != "ok": continue
        s1 = sample_of(exc["a"][p["term_a"]]); s2 = sample_of(exc["b"][p["term_b"]])
        e1 = numbered(s1, "a", p["term_a"], terms, "⟦T1⟧")
        e2 = numbered(s2, "b", p["term_b"], terms, "⟦T2⟧")
        pf = RUNS / f"containment/prompt-{pid}.md"
        pf.write_text(tmpl.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        stage_call(rows, "codex", "gpt-5.6-terra", pf, RUNS / f"containment/out-{pid}.json",
                   RUNS / f"manifests/containment-{pid}.json")
    (RUNS / "containment/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    print(f"{len(rows)} containment calls staged")

def containment_result(pid, pair, exc, terms, root=None):
    """§2.10: decided options need one machine-validated verbatim quote per side; unclear exempt."""
    f = (root or RUNS) / f"containment/out-{pid}.json"
    status = out_status(f)
    if status != "present": return {"status": "fail", "detail": status}
    obj = validate_containment(parse_json_out(f))
    if obj is None: return {"status": "fail", "detail": "unparseable"}
    if obj["relation"] != "unclear":
        s1 = sample_of(exc["a"][pair["term_a"]]); s2 = sample_of(exc["b"][pair["term_b"]])
        q1, q2 = norm(obj["quote_1"]), norm(obj["quote_2"])
        ok1 = bool(q1) and any(q1 in norm(mask_text(e["text"], "a", pair["term_a"], terms, "⟦T1⟧")) for e in s1)
        ok2 = bool(q2) and any(q2 in norm(mask_text(e["text"], "b", pair["term_b"], terms, "⟦T2⟧")) for e in s2)
        if not (ok1 and ok2): return {"status": "fail", "detail": "quote-validation"}
    return {"status": "ok", "relation": obj["relation"]}

# ---------- endpoints (§6) ----------
def display(v):
    if v["status"] == "asserted":
        rel = v["proposed_relation"]
        return rel + (f"({v['broader_side']})" if rel == "broadnarrow" else "")
    return {"review_required": "reviewRequired", "insufficient_evidence": "insufficientEvidence",
            "config_fail": "configFail"}[v["status"]] + f"({v['reason']})"

def is_correct(pair, v):
    if v["status"] != "asserted": return False  # reviewRequired is never correct (§3)
    if v["proposed_relation"] != pair["expected"]: return False
    if pair["expected"] == "broadnarrow" and v.get("broader_side") != pair.get("broader_side"):
        return False
    return True

def score(pairs, verdicts):
    per = {}
    for p in pairs:
        v = verdicts[p["pair_id"]]
        per[p["pair_id"]] = {"expected": p["expected"] + (f"({p.get('broader_side')})" if p["expected"] == "broadnarrow" else ""),
                             "verdict": v, "display": display(v), "correct": is_correct(p, v)}
    n_correct = sum(r["correct"] for r in per.values())
    nomatch = [p for p in pairs if p["expected"] in NO_MATCH]
    promotions = [p["pair_id"] for p in nomatch
                  if verdicts[p["pair_id"]]["status"] == "asserted"
                  and verdicts[p["pair_id"]]["proposed_relation"] in HARD_MATCH]
    false_escalations = [p["pair_id"] for p in nomatch
                         if verdicts[p["pair_id"]]["status"] == "review_required"]
    jingle = sum(1 for p in pairs if p["expected"] == "noMatchDespiteSimilarity"
                 and verdicts[p["pair_id"]]["status"] == "asserted"
                 and verdicts[p["pair_id"]]["proposed_relation"] == "noMatchDespiteSimilarity")
    e1 = n_correct >= 7 and not promotions and jingle >= 1 and len(false_escalations) <= 1
    det = {"tp": 0, "fn": 0, "tn": 0, "fp": 0, "abstain": 0}
    for p in pairs:
        v = verdicts[p["pair_id"]]; planted_pos = p["expected"] in HARD_MATCH
        if v["status"] in ("insufficient_evidence", "config_fail"): det["abstain"] += 1
        elif v["status"] == "review_required" or (v["status"] == "asserted" and v["proposed_relation"] in HARD_MATCH):
            det["tp" if planted_pos else "fp"] += 1
        else: det["tn" if not planted_pos else "fn"] += 1
    def grade(p):
        v = verdicts[p["pair_id"]]
        if is_correct(p, v): return 1.0
        if v["status"] == "insufficient_evidence": return 0.4
        if v["status"] == "review_required": return 0.7 if p["expected"] in HARD_MATCH else 0.2
        return 0.0
    e1c = round(sum(grade(p) for p in pairs), 2)
    return {"per_pair": per, "n_correct": n_correct, "promotions": promotions,
            "false_escalations": false_escalations, "jingle_specific": jingle,
            "E1_PASS": e1, "E1b_detection": det, "E1c_graded": e1c}

def compose(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    agg = json.load(open(RUNS / "agg.json"))
    retrf = RUNS / "retrieval.json"
    retr = json.load(open(retrf)) if retrf.exists() else {}
    meta = json.load(open(RUNS / "verify/meta.json")) if (RUNS / "verify/meta.json").exists() else {}
    cf = configfail_terms(st); inv = polarity_inverted(st)
    verdicts = {}
    for p in pairs:
        pid = p["pair_id"]
        # §4 configFail order: polarity inversion first, then artifact-gate exhaustion
        configfail = None
        if st.get("polarity_side_fail"):
            configfail = f"polarity-batch-failure-side-{','.join(st['polarity_side_fail'])}"
        elif p["term_a"] in inv["a"] or p["term_b"] in inv["b"]:
            bad = [f"a:{p['term_a']}"] if p["term_a"] in inv["a"] else []
            bad += [f"b:{p['term_b']}"] if p["term_b"] in inv["b"] else []
            configfail = f"polarity-inversion:{','.join(bad)}"
        elif p["term_a"] in cf["a"] or p["term_b"] in cf["b"]:
            for side, term in (("a", p["term_a"]), ("b", p["term_b"])):
                if term in cf[side]:
                    for kind in ("chk", "lad"):
                        art = st["artifacts"].get(aid(kind, side, term))
                        if art and art["state"] == "configFail":
                            configfail = f"artifact-gate-exhaustion:{kind}:{side}:{term}:{art.get('failed_gate')}"
                            break
                if configfail: break
        floor_fail = "; ".join(floor["dead_pairs"].get(pid, [])) or None
        dirs = {}
        for d in ("a2b", "b2a"):
            dirs[d] = agg.get(pid, {}).get(d, {"status": "missing"})
        cand = _row3_candidate(pid, agg, None) if pid in agg and not configfail and not floor_fail else None
        sym = symcheck_result(pid, cand[0], meta, terms) if cand else None
        dc = decompose_result(pid, p, exc, terms) if (RUNS / f"decompose/out-{pid}.json").exists() else None
        ct = containment_result(pid, p, exc, terms) if (RUNS / f"containment/out-{pid}.json").exists() else None
        ctx = {"configfail": configfail, "floor_fail": floor_fail, "dirs": dirs,
               "symcheck": sym, "mutual": retr.get(pid, {}).get("mutual", False),
               "decompose": dc, "containment": ct,
               "flag": sim_flag(p["term_a"], p["term_b"])}
        verdicts[pid] = compose_pair(p, ctx)
        verdicts[pid]["La"] = dirs["a2b"].get("L"); verdicts[pid]["Lb"] = dirs["b2a"].get("L")
    summary = score(pairs, verdicts)
    json.dump(summary, open(RUNS / "results.json", "w"), indent=1)
    for p in pairs:
        r = summary["per_pair"][p["pair_id"]]
        v = r["verdict"]
        print(f"{p['pair_id']}: expected={r['expected']:<30} proposed={r['display']:<40} "
              f"[La={v.get('La')} Lb={v.get('Lb')}] {'OK' if r['correct'] else 'X'}")
    print(f"\nE1: correct {summary['n_correct']}/10 · promotions: {summary['promotions'] or 'none'} · "
          f"false-escalations: {summary['false_escalations'] or 'none'} · "
          f"jingle {summary['jingle_specific']}/2 · PASS={summary['E1_PASS']}")
    print(f"E1b detection: {summary['E1b_detection']}")
    print(f"E1c graded: {summary['E1c_graded']}/10")

# ---------- main ----------
def main():
    cmd = sys.argv[1]
    pairs = load_pairs()
    for d in ("checklists", "definitions", "conformance", "polarity", "verify",
              "symcheck", "decompose", "containment", "manifests"):
        (RUNS / d).mkdir(parents=True, exist_ok=True)
    dispatch = {
        "excerpts": extract, "manifests": lambda _: regen_manifests(),
        "prompts-checklist": prompts_checklist, "gate-checklists": gate_checklists,
        "prompts-def": prompts_def, "gate-ladders": gate_ladders,
        "prompts-conformance": prompts_conformance, "gate-conformance": gate_conformance,
        "prompts-polarity": prompts_polarity, "gate-polarity": gate_polarity,
        "alive": emit_alive, "prompts-verify": prompts_verify, "aggregate": aggregate,
        "prompts-symcheck": prompts_symcheck, "prompts-decompose": prompts_decompose,
        "prompts-containment": prompts_containment, "compose": compose,
        "assert-resolved": assert_resolved,
    }
    if cmd not in dispatch: sys.exit(f"unknown: {cmd}")
    dispatch[cmd](pairs)

if __name__ == "__main__":
    main()
