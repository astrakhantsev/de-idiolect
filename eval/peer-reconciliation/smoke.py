#!/usr/bin/env python3
"""Peer-reconciliation v0.2 smoke test orchestrator (prereg.md is the authority).
Subcommands: split | excerpts | prompts-def | prompts-verify | prompts-polarity |
aggregate | compose | records. Model calls happen in run_calls.sh, never here."""
import json, re, sys, hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
RUNS = BASE / "runs"
KEY = json.load(open(BASE / "key/answer_key.json"))
PAIRS = KEY["pairs"]
A_TERMS = sorted({p["term_a"] for p in PAIRS})
B_TERMS = sorted({p["term_b"] for p in PAIRS})
N_SAMPLE, MIN_EXC = 6, 4
MASK = "⟦TERM⟧"

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
def norm(s):
    s = s.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "—": "-", "–": "-"}))
    return re.sub(r"\s+", " ", s.lower()).strip()

# ---------- corpus ----------
def split_corpus(side, raw_file):
    txt = open(raw_file).read()
    parts = re.split(r"<<<DOC (\d+)>>>", txt)
    docs = {}
    for i in range(1, len(parts) - 1, 2):
        nn, body = parts[i].zfill(2), parts[i + 1].strip()
        (BASE / f"corpora/{side}/{nn}.md").write_text(body + "\n")
        docs[nn] = sha(body)
    json.dump(docs, open(BASE / f"corpora/{side}/manifest.json", "w"), indent=1)
    print(f"{side}: {len(docs)} docs")

SENT = re.compile(r"(?<=[.?!])\s+(?=[A-Z“\"(])")
def sentences(text):
    body = " ".join(l.strip() for l in text.splitlines() if l.strip() and not l.startswith("#"))
    return [s.strip() for s in SENT.split(body) if s.strip()]

def extract():
    out = {}
    for side, terms in (("a", A_TERMS), ("b", B_TERMS)):
        out[side] = {}
        for term in terms:
            tre = re.compile(re.escape(term), re.I)
            other_res = [re.compile(re.escape(t), re.I) for t in terms if t != term]
            dev, held = [], []
            for f in sorted((BASE / f"corpora/{side}").glob("[0-9][0-9].md")):
                nn = f.stem
                sents = sentences(f.read_text())
                for idx, s in enumerate(sents):
                    if tre.search(s):
                        # v0.4 window: prev/next sentence included ONLY if it contains no
                        # other same-side coined term (neighbor-contamination fix)
                        win = [s]
                        if idx > 0 and not any(o.search(sents[idx - 1]) for o in other_res):
                            win.insert(0, sents[idx - 1])
                        if idx + 1 < len(sents) and not any(o.search(sents[idx + 1]) for o in other_res):
                            win.append(sents[idx + 1])
                        exc = " ".join(win)
                        (dev if int(nn) <= 8 else held).append({"doc": nn, "idx": idx, "text": exc})
            out[side][term] = {"dev": dev, "held": held}
            print(f"{side} '{term}': dev={len(dev)} held={len(held)}")
    json.dump(out, open(RUNS / "excerpts.json", "w"), indent=1)

def load_exc(): return json.load(open(RUNS / "excerpts.json"))

def mask_text(text, side, term, mask=MASK):
    # v0.4: mask the target term AND every other same-side coined term (as ⟦X⟧)
    text = re.compile(re.escape(term), re.I).sub(mask, text)
    for t in (A_TERMS if side == "a" else B_TERMS):
        if t != term: text = re.compile(re.escape(t), re.I).sub("⟦X⟧", text)
    return text

def sample_of(entry):
    s, enc = entry["dev"][:N_SAMPLE], False
    if len(s) < MIN_EXC:
        s, enc = s + entry["held"][: N_SAMPLE - len(s)], True
    return s, enc, len(s) >= MIN_EXC

def numbered(sample, side, term, mask=MASK):
    return "\n".join(f"{i+1}. {mask_text(e['text'], side, term, mask)}" for i, e in enumerate(sample))

# ---------- prompt builders ----------
def prompts_checklist():
    tmpl = (BASE / "prompts/checklist-extract.md").read_text()
    exc = load_exc(); calls = []
    for side in ("a", "b"):
        for term in (A_TERMS if side == "a" else B_TERMS):
            body = tmpl + "\n" + numbered(exc[side][term]["dev"], side, term)
            p = RUNS / f"checklists/prompt-{side}-{slug(term)}.md"; p.parent.mkdir(exist_ok=True)
            p.write_text(body)
            calls.append(f"claude\tsonnet\t{p}\t{RUNS}/checklists/out-{side}-{slug(term)}.txt\t{RUNS}/manifests/chk-{side}-{slug(term)}.json")
    (RUNS / "checklists/calls.tsv").write_text("\n".join(calls) + "\n")
    print(f"{len(calls)} checklist calls staged")

def prompts_def():
    tmpl = (BASE / "prompts/gen-definition-v04.md").read_text()
    exc = load_exc(); calls, index = [], []
    for side, kind, model in (("a", "claude", "opus"), ("b", "codex", "gpt-5.6-terra")):
        for term in (A_TERMS if side == "a" else B_TERMS):
            chk = (RUNS / f"checklists/out-{side}-{slug(term)}.txt").read_text().strip()
            body = tmpl.replace("{CHECKLIST}", chk) + "\n" + numbered(exc[side][term]["dev"], side, term)
            p = RUNS / f"definitions/prompt-{side}-{slug(term)}.md"; p.write_text(body)
            o = RUNS / f"definitions/out-{side}-{slug(term)}.txt"
            m = RUNS / f"manifests/def-{side}-{slug(term)}.json"
            calls.append(f"{kind}\t{model}\t{p}\t{o}\t{m}")
            index.append({"side": side, "term": term, "out": str(o)})
    (RUNS / "definitions/calls.tsv").write_text("\n".join(calls) + "\n")
    json.dump(index, open(RUNS / "definitions/index.json", "w"), indent=1)
    print(f"{len(calls)} definition calls staged")

def read_def(side, term):
    return (RUNS / f"definitions/out-{side}-{slug(term)}.txt").read_text().strip()

def prompts_verify():
    tmpl = (BASE / "prompts/verify-pair.md").read_text()
    exc = load_exc(); calls = []; meta = {}
    for p in PAIRS:
        for d, dside, eside, eterm, kind, model in (
            ("a2b", "a", "b", p["term_b"], "claude", "opus"),
            ("b2a", "b", "a", p["term_a"], "codex", "gpt-5.6-terra")):
            samp, enc, ok = sample_of(exc[eside][eterm])
            meta[f"{p['pair_id']}-{d}"] = {"n": len(samp), "encroached": enc, "sufficient": ok,
                                            "excerpts": samp, "term": eterm}
            if not ok: continue
            defin = read_def(dside, p["term_a"] if dside == "a" else p["term_b"])
            body = tmpl.replace("{DEFINITION}", defin) + "\n" + numbered(samp, eside, eterm)
            pf = RUNS / f"verify/prompt-{p['pair_id']}-{d}.md"; pf.write_text(body)
            calls.append(f"{kind}\t{model}\t{pf}\t{RUNS}/verify/out-{p['pair_id']}-{d}.json\t{RUNS}/manifests/verify-{p['pair_id']}-{d}.json")
    (RUNS / "verify/calls.tsv").write_text("\n".join(calls) + "\n")
    json.dump(meta, open(RUNS / "verify/meta.json", "w"), indent=1)
    print(f"{len(calls)} verify calls staged")

def prompts_polarity():
    tmpl = (BASE / "prompts/polarity-check.md").read_text()
    exc = load_exc(); calls = []
    for side, judge_kind, judge_model in (("a", "codex", "gpt-5.6-terra"), ("b", "claude", "opus")):
        items, terms = [], (A_TERMS if side == "a" else B_TERMS)
        for i, term in enumerate(terms):
            samp, _, _ = sample_of(exc[side][term])
            items.append(f"ITEM {i+1}\nEXCERPTS:\n{numbered(samp, side, term)}\nDEFINITION:\n{read_def(side, term)}\n")
        pf = RUNS / f"polarity/prompt-{side}.md"; pf.parent.mkdir(exist_ok=True)
        pf.write_text(tmpl + "\n" + "\n".join(items))
        calls.append(f"{judge_kind}\t{judge_model}\t{pf}\t{RUNS}/polarity/out-{side}.json\t{RUNS}/manifests/polarity-{side}.json")
    (RUNS / "polarity/calls.tsv").write_text("\n".join(calls) + "\n")
    (RUNS / "polarity/terms.json").write_text(json.dumps({"a": A_TERMS, "b": B_TERMS}))
    print("2 polarity calls staged")

# ---------- aggregation / composition ----------
def parse_json_out(path):
    t = Path(path).read_text().strip()
    t = re.sub(r"^```(json)?|```$", "", t, flags=re.M).strip()
    m = re.search(r"[\[{].*[\]}]", t, re.S)
    return json.loads(m.group(0)) if m else None

def direction_verdict(rows, sample, side, term):
    # quotes are validated against the fully-masked excerpt text — what the judge saw
    n = len(sample); k = c = u = 0; downgrades = []
    for r in rows:
        i = int(r["excerpt"]) - 1
        v, q = r.get("verdict", "insufficient"), norm(r.get("quote", ""))
        if v in ("instantiates", "contradicts"):
            if not q or q not in norm(mask_text(sample[i]["text"], side, term)):
                downgrades.append(i + 1); v = "insufficient"
        k += v == "instantiates"; c += v == "contradicts"; u += v == "insufficient"
    # v0.3 rule (prereg amendment): decidable-count abstention
    dec = k + c
    if dec < 2: agg = "abstain"
    else:
        agg = "covers" if (k >= 2 and c == 0) else "fails" if (c >= 2 or k / dec <= 0.3) else "mixed"
    return {"n": n, "k": k, "c": c, "u": u, "agg": agg, "quote_downgrades": downgrades}

def trigrams(s):
    s = re.sub(r"\W", "", s.lower()); return {s[i:i+3] for i in range(max(0, len(s) - 2))}
def sim_flag(ta, tb):
    if norm(ta) == norm(tb): return True
    A, B = trigrams(ta), trigrams(tb)
    return bool(A) and len(A & B) / len(A | B) >= 0.5

def polarity_fails():
    bad = {"a": set(), "b": set()}
    terms = json.load(open(RUNS / "polarity/terms.json"))
    for side in ("a", "b"):
        rows = parse_json_out(RUNS / f"polarity/out-{side}.json") or []
        for r in rows:
            if r.get("verdict") == "inverted":
                bad[side].add(terms[side][int(r["item"]) - 1])
    return bad

def aggregate():
    meta = json.load(open(RUNS / "verify/meta.json"))
    agg = {}
    for p in PAIRS:
        agg[p["pair_id"]] = {}
        for d in ("a2b", "b2a"):
            mm = meta[f"{p['pair_id']}-{d}"]
            if not mm["sufficient"]:
                agg[p["pair_id"]][d] = {"agg": "abstain", "reason": "input-insufficient"}; continue
            rows = parse_json_out(RUNS / f"verify/out-{p['pair_id']}-{d}.json")
            eside = "b" if d == "a2b" else "a"
            agg[p["pair_id"]][d] = direction_verdict(rows, mm["excerpts"], eside, mm["term"]) if rows else {"agg": "abstain", "reason": "unparseable"}
    json.dump(agg, open(RUNS / "agg.json", "w"), indent=1)
    # stage decompose prompts for rule-5 candidates with mutual retrieval hit
    retr = json.load(open(RUNS / "retrieval.json"))
    exc = load_exc(); tmpl = (BASE / "prompts/decompose.md").read_text(); calls = []
    pol = polarity_fails()
    for p in PAIRS:
        a, b = agg[p["pair_id"]]["a2b"]["agg"], agg[p["pair_id"]]["b2a"]["agg"]
        if p["term_a"] in pol["a"] or p["term_b"] in pol["b"]: continue
        if a in ("fails", "mixed") and b in ("fails", "mixed") and retr[p["pair_id"]]["mutual"]:
            s1, _, _ = sample_of(exc["a"][p["term_a"]]); s2, _, _ = sample_of(exc["b"][p["term_b"]])
            e1 = numbered(s1, "a", p["term_a"], "⟦T1⟧")
            e2 = numbered(s2, "b", p["term_b"], "⟦T2⟧")
            pf = RUNS / f"decompose/prompt-{p['pair_id']}.md"
            pf.write_text(tmpl.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
            calls.append(f"claude\tsonnet\t{pf}\t{RUNS}/decompose/out-{p['pair_id']}.json\t{RUNS}/manifests/decompose-{p['pair_id']}.json")
    (RUNS / "decompose/calls.tsv").write_text("\n".join(calls) + ("\n" if calls else ""))
    print(f"aggregated; {len(calls)} decompose calls staged")

def decompose_ok(pid):
    f = RUNS / f"decompose/out-{pid}.json"
    if not f.exists(): return False, None
    t = f.read_text().strip()
    if "ABSTAIN" in t[:200] and "{" not in t[:20]: return False, "ABSTAIN"
    obj = parse_json_out(f)
    if not obj or not obj.get("core"): return False, None
    exc = load_exc()
    p = next(x for x in PAIRS if x["pair_id"] == pid)
    s1, _, _ = sample_of(exc["a"][p["term_a"]]); s2, _, _ = sample_of(exc["b"][p["term_b"]])
    q1 = norm(obj.get("quote_1", "")); q2 = norm(obj.get("quote_2", ""))
    # validate against the fully-masked text the decompose call saw
    ok1 = q1 and any(q1 in norm(mask_text(e["text"], "a", p["term_a"], "⟦T1⟧")) for e in s1)
    ok2 = q2 and any(q2 in norm(mask_text(e["text"], "b", p["term_b"], "⟦T2⟧")) for e in s2)
    # v0.4 core-specificity gate (prereg amendment): both own-pair bundles in top 3
    specf = RUNS / "core_specificity.json"
    spec_ok = False
    if specf.exists():
        spec_ok = json.load(open(specf)).get(pid, {}).get("pass", False)
    return (ok1 and ok2 and spec_ok), obj

def compose():
    agg = json.load(open(RUNS / "agg.json"))
    retr = json.load(open(RUNS / "retrieval.json"))
    pol = polarity_fails()
    results = {}
    for p in PAIRS:
        pid = p["pair_id"]; a = agg[pid]["a2b"]["agg"]; b = agg[pid]["b2a"]["agg"]
        ca, cb = agg[pid]["a2b"].get("c", 0), agg[pid]["b2a"].get("c", 0)
        flag = sim_flag(p["term_a"], p["term_b"]); note = ""
        if p["term_a"] in pol["a"] or p["term_b"] in pol["b"]: rel = "configFail"
        elif "abstain" in (a, b): rel = "insufficientEvidence"
        elif a == "covers" and b == "covers": rel = "exactMatch"
        # prereg rule 3: covers(D_X on partner's excerpts) + fails(D_Y on X's excerpts) with
        # c >= 2 in the FAILING direction => X is the broader side
        elif a == "covers" and b == "fails" and cb >= 2: rel, note = "broadnarrow", "broader_side=a"
        elif b == "covers" and a == "fails" and ca >= 2: rel, note = "broadnarrow", "broader_side=b"
        elif "covers" in (a, b): rel = "insufficientEvidence"
        else:
            ok, obj = decompose_ok(pid)
            if retr[pid]["mutual"] and ok: rel, note = "relatedMatch", (obj["core"][:100] if obj else "")
            elif flag: rel = "noMatchDespiteSimilarity"
            else: rel = "noMatch"
        exp = p["expected"]
        correct = rel == exp and (exp != "broadnarrow" or note == f"broader_side={p.get('broader_side')}")
        results[pid] = {"expected": exp + (f"({p.get('broader_side')})" if exp == "broadnarrow" else ""),
                        "proposed": rel + (f"({note})" if rel == "broadnarrow" else ""),
                        "a2b": a, "b2a": b, "sim_flag": flag, "mutual_hit": retr[pid]["mutual"],
                        "correct": correct, "note": note}
    n_correct = sum(r["correct"] for r in results.values())
    nomatch_promoted = [pid for pid, r in results.items()
                        if r["expected"].startswith("noMatch") and r["proposed"].split("(")[0] in ("exactMatch", "broadnarrow", "relatedMatch")]
    jingle_ok = sum(1 for pid in ("P07", "P08") if results[pid]["proposed"] == "noMatchDespiteSimilarity")
    e1 = n_correct >= 7 and not nomatch_promoted and jingle_ok >= 1
    summary = {"per_pair": results, "n_correct": n_correct, "nomatch_promoted": nomatch_promoted,
               "jingle_specific": jingle_ok, "E1_PASS": e1}
    json.dump(summary, open(RUNS / "results.json", "w"), indent=1)
    for pid, r in results.items():
        print(f"{pid}: expected={r['expected']:<28} proposed={r['proposed']:<28} "
              f"[a2b={r['a2b']} b2a={r['b2a']} sim={r['sim_flag']} hit={r['mutual_hit']}] {'OK' if r['correct'] else 'X'}")
    print(f"\nE1: correct {n_correct}/10 · noMatch promoted: {nomatch_promoted or 'none'} · "
          f"jingle-specific {jingle_ok}/2 · PASS={e1}")

# ---------- records + fork demo (E3) ----------
def canonical(o): return json.dumps(o, sort_keys=True, separators=(",", ":"))
def emit_records():
    results = json.load(open(RUNS / "results.json"))["per_pair"]
    agg = json.load(open(RUNS / "agg.json"))
    key_stamp = "synthetic-key-" + sha(open(BASE / "key/answer_key.json").read())[:8]
    index = []
    def prior_adjudicated(pk):
        d = BASE / f"records/{pk}"
        if not d.exists(): return []
        out = []
        for f in sorted(d.glob("*.json")):
            r = json.loads(f.read_text())
            if r.get("status") == "adjudicated": out.append(f.stem)
        return out
    def has_dispute(pk):
        d = BASE / f"records/{pk}"
        return d.exists() and any(json.loads(f.read_text()).get("record_type") == "dispute" for f in d.glob("*.json"))
    def file_record(rec):
        pk = rec["pair_key"]; body = dict(rec); body.pop("version_id", None)
        vid = sha(canonical(body)); rec["version_id"] = vid
        d = BASE / f"records/{pk}"; d.mkdir(parents=True, exist_ok=True)
        (d / f"{vid}.json").write_text(json.dumps(rec, indent=1))
        index.append(f"{pk}\t{vid}\t{rec.get('proposed_relation', rec.get('claim_type'))}")
        return vid
    vids = {}
    for p in PAIRS:
        pid = p["pair_id"]; r = results[pid]
        pk = sha(canonical(sorted([["a", p["term_a"]], ["b", p["term_b"]]])))[:16]
        rec = {"pair_key": pk, "pair_id": pid, "terms": {"a": p["term_a"], "b": p["term_b"]},
               "proposed_relation": r["proposed"], "evidence": agg[pid],
               "adjudicated_relation": r["expected"], "status": "adjudicated",
               "adjudicator": key_stamp, "correct": r["correct"],
               "provenance": {"gen_a": "claude-sonnet", "gen_b": "codex-gpt-5.6-terra",
                               "def_a": "claude-opus", "def_b": "codex-gpt-5.6-terra",
                               "verify_a2b": "claude-opus", "verify_b2a": "codex-gpt-5.6-terra"},
               "derived_from": prior_adjudicated(sha(canonical(sorted([["a", p["term_a"]], ["b", p["term_b"]]])))[:16]),
               "earliest_found_in_search": {"synthetic": True, "note": "no priority inference licensed"}}
        vids[pid] = (pk, file_record(rec))
    # E3: incompatible fork on P05 + dispute record (once; skip if already demonstrated)
    pk5, v1 = vids["P05"]
    if has_dispute(pk5):
        with open(BASE / "records/index.tsv", "a") as f: f.write("\n".join(index) + "\n")
        print(f"records emitted (derived_from links to prior versions); E3 fork demo already present under {pk5} — PASS (existing)")
        return
    fork = {"pair_key": pk5, "pair_id": "P05", "terms": {"a": "pothole runs", "b": "seeded-defect audit"},
            "proposed_relation": "exactMatch", "evidence": {"basis": "partisan-demo: community-a maintainer asserts identity"},
            "adjudicated_relation": None, "status": "proposed", "adjudicator": None,
            "provenance": {"source": "fork-demo"}, "derived_from": [v1],
            "earliest_found_in_search": {"synthetic": True, "note": "no priority inference licensed"}}
    v2 = file_record(fork)
    dispute = {"pair_key": pk5, "record_type": "dispute", "dispute_of": v2, "claimant": "community-b-demo",
               "claim_type": "rejects_relation", "evidence_quotes": ["scoring is binary on containment, not on speed"],
               "note": "fork-coexistence demo"}
    v3 = file_record(dispute)
    with open(BASE / "records/index.tsv", "a") as f: f.write("\n".join(index) + "\n")
    two = len(list((BASE / f"records/{pk5}").glob("*.json")))
    print(f"E3: pair_key {pk5} holds {two} coexisting records (orig {v1[:8]}, fork {v2[:8]}, dispute {v3[:8]}) — PASS={two >= 3}")

# ---------- E2 (prereg amendment v0.3) ----------
E2_PAIRS = ["P05", "P06"]

def prompts_dfull():
    tmpl = (BASE / "prompts/decompose-full.md").read_text()
    exc = load_exc(); calls = []
    for pid in E2_PAIRS:
        p = next(x for x in PAIRS if x["pair_id"] == pid)
        e1 = numbered(exc["a"][p["term_a"]]["dev"], "a", p["term_a"], "⟦T1⟧")
        e2 = numbered(exc["b"][p["term_b"]]["dev"], "b", p["term_b"], "⟦T2⟧")
        pf = RUNS / f"e2/prompt-dfull-{pid}.md"
        pf.write_text(tmpl.replace("{EXCERPTS_1}", e1).replace("{EXCERPTS_2}", e2))
        calls.append(f"claude\tsonnet\t{pf}\t{RUNS}/e2/out-dfull-{pid}.json\t{RUNS}/manifests/e2-dfull-{pid}.json")
    (RUNS / "e2/calls-dfull.tsv").write_text("\n".join(calls) + "\n")
    print("2 decompose-full calls staged")

def prompts_e2_verify():
    tmpl = (BASE / "prompts/verify-pair.md").read_text()
    exc = load_exc(); calls = []
    for pid in E2_PAIRS:
        p = next(x for x in PAIRS if x["pair_id"] == pid)
        core = parse_json_out(RUNS / f"e2/out-dfull-{pid}.json")["core"]
        for side, term, kind, model in (("a", p["term_a"], "codex", "gpt-5.6-terra"), ("b", p["term_b"], "claude", "opus")):
            held = exc[side][term]["held"]
            if not held: continue
            pf = RUNS / f"e2/prompt-core-{pid}-{side}.md"
            pf.write_text(tmpl.replace("{DEFINITION}", core) + "\n" + numbered(held, side, term))
            calls.append(f"{kind}\t{model}\t{pf}\t{RUNS}/e2/out-core-{pid}-{side}.json\t{RUNS}/manifests/e2-core-{pid}-{side}.json")
    (RUNS / "e2/calls-verify.tsv").write_text("\n".join(calls) + "\n")
    print(f"{len(calls)} core-check calls staged")

def e2_score():
    exc = load_exc(); resid = json.load(open(RUNS / "e2/residues.json")); res = {}
    for pid in E2_PAIRS:
        p = next(x for x in PAIRS if x["pair_id"] == pid)
        obj = parse_json_out(RUNS / f"e2/out-dfull-{pid}.json")
        entry = {"decompose": bool(obj and obj.get("core"))}
        if entry["decompose"]:
            s1 = exc["a"][p["term_a"]]["dev"]; s2 = exc["b"][p["term_b"]]["dev"]
            def q_in(q, ss, side, term, mask):
                qn = norm(q or ""); return bool(qn) and any(qn in norm(mask_text(e["text"], side, term, mask)) for e in ss)
            entry["quotes_ok"] = all([q_in(obj.get("quote_core_1"), s1, "a", p["term_a"], "⟦T1⟧"), q_in(obj.get("quote_core_2"), s2, "b", p["term_b"], "⟦T2⟧"),
                                       q_in(obj.get("quote_residue_1"), s1, "a", p["term_a"], "⟦T1⟧"), q_in(obj.get("quote_residue_2"), s2, "b", p["term_b"], "⟦T2⟧")])
            specf = RUNS / "core_specificity.json"
            entry["specificity"] = json.load(open(specf)).get(f"dfull-{pid}", {}).get("pass", False) if specf.exists() else False
        cc = {}
        for side, term in (("a", p["term_a"]), ("b", p["term_b"])):
            held = exc[side][term]["held"]; f = RUNS / f"e2/out-core-{pid}-{side}.json"
            if not held or not f.exists(): cc[side] = "no-heldout"; continue
            if f.read_text().lstrip().startswith("API Error"): cc[side] = "unscoreable-refusal"; continue
            v = direction_verdict(parse_json_out(f) or [], held, side, term)
            cc[side] = "pass" if (v["k"] >= 1 and v["c"] == 0) else f"fail(k{v['k']} c{v['c']} u{v['u']})"
        entry["core_check"] = cc
        entry["residues"] = resid.get(pid, {})
        skip = ("no-heldout", "unscoreable-refusal")
        entry["pass"] = bool(entry["decompose"] and entry.get("quotes_ok") and entry.get("specificity")
                              and all(x == "pass" for x in cc.values() if x not in skip)
                              and any(x == "pass" for x in cc.values())
                              and sum(1 for r in entry["residues"].values() if r.get("top1_own")) >= 1)
        res[pid] = entry
    res["E2_PASS"] = all(res[pid]["pass"] for pid in E2_PAIRS)
    json.dump(res, open(RUNS / "e2/e2-results.json", "w"), indent=1)
    print(json.dumps(res, indent=1))

if __name__ == "__main__":
    cmd = sys.argv[1]
    for d in ("definitions", "verify", "decompose", "manifests", "polarity", "e2"): (RUNS / d).mkdir(parents=True, exist_ok=True)
    if cmd == "split": split_corpus(sys.argv[2], sys.argv[3])
    elif cmd == "excerpts": extract()
    elif cmd == "prompts-checklist": prompts_checklist()
    elif cmd == "prompts-def": prompts_def()
    elif cmd == "prompts-verify": prompts_verify()
    elif cmd == "prompts-polarity": prompts_polarity()
    elif cmd == "aggregate": aggregate()
    elif cmd == "compose": compose()
    elif cmd == "records": emit_records()
    elif cmd == "prompts-dfull": prompts_dfull()
    elif cmd == "prompts-e2-verify": prompts_e2_verify()
    elif cmd == "e2-score": e2_score()
    else: sys.exit(f"unknown: {cmd}")
