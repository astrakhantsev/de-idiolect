#!/usr/bin/env python3
"""Peer-reconciliation v0.10 TRAIN/TEST controller — HARDENED generation stack.

Derived by COPYING the frozen v0.9 controller (smoke.py, VERSION "v0.8") and modifying
ONLY the generation controller: H1 feedback-guided regeneration, H2 split regen budget
(total cap 2, semantic sub-cap 1), H3 word-budget emphasis (in the base ladder prompt),
H4 cumulative-extension generation (in the base ladder prompt). Everything else — the
mechanical validators, the leak check, the semantic-conformance gate, the polarity gate,
excerpt extraction, matrix aggregation, the composition table, the surface-similarity
flag, resume bookkeeping — is carried UNCHANGED (byte-identical) from the v0.9 code path.
`scripts/verify_gate_fidelity.py` proves the unchanged gate functions are byte-identical
to the frozen source.

v0.10 CUSTODY CHANGE (see README §"Answer-blindness"): this controller NEVER reads the
sealed `key/answer_key.json`. It reads an answer-blind `pairs.json` = {"pairs": [{pair_id,
term_a, term_b}]} — the QUESTION (which term pairs to adjudicate), not the ANSWER (the
relation classes). All 10 pairs are adjudicated regardless of class, so the pairing does
not reveal which are matches. The relation classes (`expected`/`broader_side`) live only
in the sealed key and are read ONLY by scorer_v010.py at the single authorized scoring
read (the SPEND, prereg §4.2 step 9). See make_pairs_manifest.py for how pairs.json is
produced answer-blind.

prereg-v08.md / prereg-v09.md (frozen v0.9 instrument) + the v0.10 FREEZE-CANDIDATE prereg
(2026-07-23-v010-generation-hardening-PREREG-DRAFT.md) are the authorities; section
references (§) point to the v0.10 prereg unless prefixed v08/v09. Model calls happen in
run_calls.sh via the e2e isolation runner, never here.

Subcommands (staging and gating only):
  excerpts            extract windows, build verification samples (pool = all 11 docs)
  manifests           regenerate corpus manifests to exactly docs 01-11
  prompts-checklist   stage checklist calls
  gate-checklists     checklist gates: generate -> mechanical -> leak (H1/H2 regen policy)
  prompts-def         stage ladder calls (H3/H4 base prompt = gen-definition-v010.md)
  gate-ladders        ladder mechanical+leak gates (H1/H2 regen policy)
  prompts-conformance stage semantic conformance batch per side per generation index
  gate-conformance    apply conformance verdicts / batch re-run / run-halt (H1/H2 regen)
  prompts-polarity    stage polarity batches
  gate-polarity       validate polarity output; one re-run then side-scoped configFail
  prompts-verify      stage matrix verification calls
  aggregate           parse+aggregate matrix outputs -> runs/agg.json
  prompts-symcheck    stage symmetry checks for table row 3
  prompts-decompose   stage decompose for path-P pairs with mutual hit
  prompts-containment stage containment v2 for decompose successes
  assert-resolved     exit nonzero unless every artifact is passed or configFail
"""
VERSION = "v0.10"
import json, re, sys, hashlib, subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
RUNS = BASE / "runs"
# v0.10: answer-blind pairs manifest (NOT the sealed answer key). See module docstring.
PAIRS_MANIFEST = BASE / "pairs.json"
N_SAMPLE, MIN_EXC, POOL_MAX_DOC = 6, 4, 11
MASK = "⟦TERM⟧"
VERDICT_ENUM = {"instantiates", "contradicts", "insufficient"}
CONTAIN_ENUM = {"t1_within_t2", "t2_within_t1", "partial_overlap", "no_relation", "unclear"}
HARD_MATCH = ("exactMatch", "broadnarrow", "relatedMatch")
NO_MATCH = ("noMatch", "noMatchDespiteSimilarity")
# H2 regen budget (v0.10 prereg §5 "Regeneration state machine")
TOTAL_REGEN_CAP = 2
SEMANTIC_REGEN_CAP = 1

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
def norm(s):
    s = s.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "—": "-", "–": "-"}))
    return re.sub(r"\s+", " ", s.lower()).strip()

def _check_slugs(pairs):
    """P2: distinct terms must produce distinct, non-empty slugs within each side, else
    prompt/output/manifest paths collide and one artifact silently overwrites another.
    Halt BEFORE any staging."""
    for side, keyf in (("a", "term_a"), ("b", "term_b")):
        seen = {}
        for p in pairs:
            t = p[keyf]; s = slug(t)
            if not s:
                sys.exit(f"REFUSING pairs.json: term {t!r} (side {side}) has an EMPTY slug — "
                         f"would produce empty artifact filenames")
            if s in seen and seen[s] != t:
                sys.exit(f"REFUSING pairs.json: slug collision {s!r} for {seen[s]!r} and {t!r} "
                         f"(side {side}) — distinct terms sharing a slug would overwrite artifacts")
            seen[s] = t

def load_pairs():
    """v0.10: read the ANSWER-BLIND pairs manifest — STRICT WHITELIST schema, symlink-safe.
    Per record EXACTLY {pair_id, term_a, term_b}; top-level EXACTLY {count, pairs} with
    count == len(pairs); ANY extra field anywhere -> refuse (a blacklist could miss an
    arbitrarily-named answer field). The file must NOT be a symlink and its resolved path
    must lie OUTSIDE any key/ directory (so pairs.json cannot be an indirection to the sealed
    answer key that json.load would follow before the schema check)."""
    p = PAIRS_MANIFEST
    if p.is_symlink():
        sys.exit(f"REFUSING pairs.json: {p} is a symlink — no indirection to sealed material")
    resolved = p.resolve()
    if any(part == "key" for part in resolved.parts):
        sys.exit(f"REFUSING pairs.json: resolved path {resolved} lies under a key/ directory")
    obj = json.load(open(resolved))
    if set(obj) != {"count", "pairs"}:
        sys.exit(f"REFUSING pairs.json: top-level keys {sorted(obj)} != {{count, pairs}} (strict whitelist)")
    pairs = obj["pairs"]
    if not isinstance(pairs, list) or obj["count"] != len(pairs):
        sys.exit(f"REFUSING pairs.json: count {obj.get('count')} != len(pairs) {len(pairs) if isinstance(pairs, list) else 'n/a'}")
    for rec in pairs:
        if not isinstance(rec, dict) or set(rec) != {"pair_id", "term_a", "term_b"}:
            sys.exit(f"REFUSING pairs.json: record keys {sorted(rec) if isinstance(rec, dict) else rec} "
                     f"!= {{pair_id, term_a, term_b}} (strict whitelist)")
    _check_slugs(pairs)
    return pairs

def side_terms(pairs):
    return {"a": sorted({p["term_a"] for p in pairs}), "b": sorted({p["term_b"] for p in pairs})}

# ================================================================================
# UNCHANGED FROM v0.9 (byte-identical; verified by scripts/verify_gate_fidelity.py) —
# mechanical validators, strict schemas, excerpts, corpus manifests.
# ================================================================================

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

# ================================================================================
# HARDENED artifact gate state machine (v0.10 §5 "Regeneration state machine").
#   H2: total_regens cap 2, semantic_regens sub-cap 1; mechanical+leak share the budget
#       of 2, semantic is capped at 1 within it; max 3 generations/artifact (g0,g1,g2).
#   H1: on regen, a FEEDBACK prompt (failing gate + measured value + violated cap) is
#       written per generation index (prompts/regen-feedback.md), NOT the blind base prompt.
# The GATES themselves (checklist_mech_issues, ladder_mech_issues, leak_ok, the semantic
# conformance validator, polarity) are UNCHANGED — only the regen COUNTERS and the regen
# PROMPT change.
# ================================================================================
# states: awaiting_output -> (gates) -> passed | pending_regen -> (gates) -> passed | configFail
# ladders pass mech+leak into awaiting_semantic, then conformance -> passed.
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

# ---------- call-attempt bookkeeping (round-3 F2; UNCHANGED from v0.9) ----------
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

def gen_path(kind, side, term, g, ext): return RUNS / {"chk": "checklists", "lad": "definitions"}[kind] / f"out-{side}-{slug(term)}-g{g}.{ext}"
def canon_path(kind, side, term, ext): return RUNS / {"chk": "checklists", "lad": "definitions"}[kind] / f"out-{side}-{slug(term)}.{ext}"

def base_prompt_path(kind, side, term):
    return RUNS / f"{GEN_DIR[kind]}/prompt-{side}-{slug(term)}.md"

def gen_prompt_path(kind, side, term, g):
    """H1: g0 uses the base (blind) prompt; g>=1 uses the per-index FEEDBACK prompt."""
    if g == 0: return base_prompt_path(kind, side, term)
    return RUNS / f"{GEN_DIR[kind]}/prompt-{side}-{slug(term)}-g{g}.md"

def gen_call_row(a, g):
    kind = a["kind"]
    cli, model = (("claude", "sonnet") if kind == "chk" else (a["cli"], a["model"]))
    prompt = gen_prompt_path(kind, a["side"], a["term"], g)
    return (f"{cli}\t{model}\t{prompt}\t"
            f"{gen_path(kind, a['side'], a['term'], g, GEN_EXT[kind])}\t"
            f"{manifest_for(kind, a['side'], a['term'], g)}")

def stage_call(tsv_rows, kind_cli, model, prompt, out, manifest):
    tsv_rows.append(f"{kind_cli}\t{model}\t{prompt}\t{out}\t{manifest}")

# ---------- H1: feedback-guided regeneration prompt ----------
_REGEN_TMPL = None
def _regen_template():
    global _REGEN_TMPL
    if _REGEN_TMPL is None:
        _REGEN_TMPL = (BASE / "prompts/regen-feedback.md").read_text()
    return _REGEN_TMPL

# The one place the failing gate's identity + measured value + violated cap are turned into
# human-readable feedback. The gate detail strings (e.g. "L2-words=168-not-60-160") already
# carry the measured value and the cap; the per-gate line names the cap in words too.
_GATE_CAP = {
    "mechanical": "L0 exactly 1 sentence and <=45 words; L1 2-4 sentences; L2 60-160 words; "
                  "and strictly increasing word counts w(L0) < w(L1) < w(L2). "
                  "Count the words in L2 explicitly and keep it at or under 160.",
    "leak": "the definition must not contain any coined term string or meta-vocabulary "
            "(match/broader/narrower/etc.) — use ordinary words only.",
    "semantic": "L1 must preserve L0 and state the checklist's mechanism commitment(s); "
                "L2 must preserve L1 and state EVERY checklist commitment. Build each level "
                "cumulatively: L1 = L0's text plus the mechanism; L2 = L1's text plus "
                "measurement/conditions.",
    "generate": "produce a single well-formed output in the exact requested format.",
}

def write_regen_prompt(kind, side, term, g, gate, detail):
    """H1: write the feedback prompt for generation index g (>=1). The base prompt (blind)
    is embedded verbatim after the feedback header so the regeneration keeps the original
    task and excerpts; the header states the failing gate, the measured value+cap (detail),
    and the cap in words."""
    base = base_prompt_path(kind, side, term).read_text()
    body = (_regen_template()
            .replace("{FAILING_GATE}", gate)
            .replace("{MEASURED_AND_CAP}", detail)
            .replace("{CAP_IN_WORDS}", _GATE_CAP.get(gate, _GATE_CAP["generate"]))
            .replace("{BASE_PROMPT}", base))
    gen_prompt_path(kind, side, term, g).write_text(body)

def _route_fail(st, a, gate, detail, regen_rows):
    """v0.10 §5 state machine (H2 + H1). failing class 'semantic' consumes the semantic
    sub-cap; mechanical/leak/generate consume only the total budget. Regenerate iff
    total_regens < 2 AND (class != semantic OR semantic_regens < 1); increment the
    counter(s); else -> configFail scoped to every pair involving the term. The regen
    prompt is the H1 FEEDBACK prompt (write_regen_prompt), not the blind base prompt."""
    is_semantic = (gate == "semantic")
    can_regen = (a["total_regens"] < TOTAL_REGEN_CAP
                 and (not is_semantic or a["semantic_regens"] < SEMANTIC_REGEN_CAP))
    if can_regen:
        a["total_regens"] += 1
        if is_semantic: a["semantic_regens"] += 1
        g = a["total_regens"]
        a["state"] = "pending_regen"
        write_regen_prompt(a["kind"], a["side"], a["term"], g, gate, detail)
        a["log"].append(f"gate-fail[{gate}] g{g-1}: {detail} -> feedback-regen g{g} staged "
                        f"(total_regens={a['total_regens']}, semantic_regens={a['semantic_regens']})")
        regen_rows.append(gen_call_row(a, g))
    else:
        a["state"] = "configFail"; a["failed_gate"] = gate
        a["log"].append(f"gate-fail[{gate}] g{a['total_regens']}: {detail} -> configFail "
                        f"(budget exhausted: total_regens={a['total_regens']}, "
                        f"semantic_regens={a['semantic_regens']})")

def _gen_attempt_state(a, regen_rows):
    """Round-3 F2 preamble (UNCHANGED policy; H1/H2 aware). Returns the output path if the
    g-th call completed cleanly, else None after re-staging (never-attempted / interrupted,
    no budget) or routing (attempted-and-failed via _route_fail, budget). g = total_regens."""
    g = a["total_regens"]
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

def _new_artifact(kind, side, term, **extra):
    """v0.10 artifact record: the v0.9 single `regens_used` counter is replaced by the
    split counters total_regens/semantic_regens (§5)."""
    return {"kind": kind, "side": side, "term": term,
            "total_regens": 0, "semantic_regens": 0,
            "state": "awaiting_output", "log": [], **extra}

def prompts_checklist(pairs):
    st = gate_load(); floor = load_floor(); exc = load_exc(); terms = side_terms(pairs)
    tmpl = (BASE / "prompts/checklist-extract.md").read_text()
    (RUNS / "checklists").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in alive_pairs(pairs, st, floor, with_polarity=False):
        for side, term in (("a", p["term_a"]), ("b", p["term_b"])):
            a = st["artifacts"].setdefault(aid("chk", side, term), _new_artifact("chk", side, term))
            pf = base_prompt_path("chk", side, term)
            pf.write_text(tmpl + "\n" + numbered(exc[side][term]["pool"], side, term, terms))
            stage_call(rows, "claude", "sonnet", pf, gen_path("chk", side, term, 0, "txt"),
                       manifest_for("chk", side, term, 0))
    (RUNS / "checklists/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    gate_save(st)
    print(f"{len(rows)} checklist calls staged")

def gate_checklists(pairs):
    st = gate_load()
    regen_rows = []
    for k, a in st["artifacts"].items():
        if a["kind"] != "chk" or a["state"] not in ("awaiting_output", "pending_regen"): continue
        f = _gen_attempt_state(a, regen_rows)
        if f is None: continue
        g = a["total_regens"]
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
    # H3/H4: the base ladder prompt is the v0.10 hardened prompt (word-budget emphasis +
    # cumulative-extension). Byte-different from v0.9's gen-definition-v07.md by design.
    tmpl = (BASE / "prompts/gen-definition-v010.md").read_text()
    (RUNS / "definitions").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in alive_pairs(pairs, st, floor, with_polarity=False):
        for side, term, cli, model in (("a", p["term_a"], "claude", "opus"),
                                       ("b", p["term_b"], "codex", "gpt-5.6-terra")):
            if st["artifacts"].get(aid("chk", side, term), {}).get("state") != "passed": continue
            a = st["artifacts"].setdefault(aid("lad", side, term),
                _new_artifact("lad", side, term, cli=cli, model=model))
            chk = canon_path("chk", side, term, "txt").read_text().strip()
            pf = base_prompt_path("lad", side, term)
            pf.write_text(tmpl.replace("{CHECKLIST}", chk) + "\n"
                          + numbered(exc[side][term]["pool"], side, term, terms))
            stage_call(rows, cli, model, pf, gen_path("lad", side, term, 0, "json"),
                       manifest_for("lad", side, term, 0))
    (RUNS / "definitions/calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    gate_save(st)
    print(f"{len(rows)} ladder calls staged")

def gate_ladders(pairs):
    """§2.4a mechanical + leak; §1 order: generate -> JSON/mechanical -> leak -> semantic.
    Gate logic UNCHANGED; only the regen policy (_route_fail) is hardened."""
    st = gate_load()
    regen_rows = []
    for k, a in st["artifacts"].items():
        if a["kind"] != "lad" or a["state"] not in ("awaiting_output", "pending_regen"): continue
        f = _gen_attempt_state(a, regen_rows)
        if f is None: continue
        g = a["total_regens"]
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
    """§2.4b + v0.10 §5: exactly ONE ordered batch per side per artifact-generation index
    (g0, regen-1, regen-2), artifacts in term order.

    Round-5 anti-stranding fix: a side stages ONLY the LOWEST pending generation index's batch
    at a time, and NEVER while it already has an unresolved batch. So the g{k} batch is created
    only after g{k-1} resolves — by which point EVERY entrant at index k has coalesced (both
    mechanical g{k-1}->g{k} regens and semantic g{k-1}->g{k} regens), and none is stranded by a
    prematurely-created-and-resolved higher-index batch. (v0.9 keyed by wave; the earlier v0.10
    keyed by index with a `bid in conf_batches -> continue` skip that dropped late entrants.)"""
    st = gate_load()
    tmpl = (BASE / "prompts/ladder-conformance.md").read_text()
    (RUNS / "conformance").mkdir(parents=True, exist_ok=True)
    rows = []
    sides_with_unresolved = set()
    for bid, b in st["conf_batches"].items():
        if not b["resolved"]:
            sides_with_unresolved.add(json.load(open(RUNS / f"conformance/batch-{bid}.json"))["side"])
    for side in ("a", "b"):
        if side in sides_with_unresolved:
            continue  # wait for this side's in-flight batch to resolve before staging the next index
        cands = [a for a in st["artifacts"].values()
                 if a["kind"] == "lad" and a["side"] == side and a["state"] == "awaiting_semantic"]
        if not cands:
            continue
        g = min(a["total_regens"] for a in cands)          # LOWEST pending index only
        bid = f"{side}-g{g}"
        if bid in st["conf_batches"]:
            # index monotonically increases (regens only raise the index) with one in-flight
            # batch per side, so a batch for the lowest pending index cannot already exist;
            # if it somehow does, that is a bug — halt rather than silently strand entrants.
            sys.exit(f"RUN-HALT: conformance batch {bid} already exists while its index is still "
                     f"the lowest pending — unexpected (would strand entrants)")
        batch = sorted([a for a in cands if a["total_regens"] == g], key=lambda x: x["term"])
        items, members = [], []
        for i, a in enumerate(batch):
            lad = read_ladder(side, a["term"])
            chk = canon_path("chk", side, a["term"], "txt").read_text().strip()
            items.append(f"ITEM {i+1}\nCHECKLIST:\n{chk}\nLADDER:\nL0: {lad['L0']}\nL1: {lad['L1']}\nL2: {lad['L2']}\n")
            members.append(a["term"])
        pf = RUNS / f"conformance/prompt-{bid}.md"
        pf.write_text(tmpl + "\n" + "\n".join(items))
        json.dump({"side": side, "gen_index": g, "terms": members},
                  open(RUNS / f"conformance/batch-{bid}.json", "w"))
        st["conf_batches"][bid] = {"reruns_used": 0, "resolved": False}
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

# ---------- polarity (§2.5, §9-F4; UNCHANGED from v0.9) ----------
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

# ================================================================================
# UNCHANGED FROM v0.9 — matrix verification staging, aggregation, composition table,
# surface-similarity flag, retrieval ranking, symcheck/decompose/containment. These are
# used by v010.py (the verification/adaptive/compose layer) and scorer_v010.py.
# ================================================================================

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

# ---------- retrieval ranking (§2.6/§9-F7; imported by retrieve_xc_v010.py) ----------
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

# ---------- display (rendering only; no key access) ----------
def display(v):
    if v["status"] == "asserted":
        rel = v["proposed_relation"]
        return rel + (f"({v['broader_side']})" if rel == "broadnarrow" else "")
    return {"review_required": "reviewRequired", "insufficient_evidence": "insufficientEvidence",
            "config_fail": "configFail"}[v["status"]] + f"({v['reason']})"

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
        "prompts-containment": prompts_containment,
        "assert-resolved": assert_resolved,
    }
    if cmd not in dispatch: sys.exit(f"unknown: {cmd}")
    dispatch[cmd](pairs)

if __name__ == "__main__":
    main()
