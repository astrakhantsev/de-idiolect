#!/usr/bin/env python3
"""scorer_v010.py — the ONE deterministic, non-LLM scorer (v0.10 prereg §4.2 step 9, §5).

This is the ONLY component that references the sealed answer key, and it does so ONLY via
PATH PARAMETERS (--key-dir, --recorded-hashes) — nothing resolves during build/test. Its
first read of the sealed answer material is the SPEND (§4.4). Everything else in the
workspace is answer-blind.

Extends the v0.9 aggregate-scoring code path (smoke.score / is_correct, copied here) with:
  * the COUNTERPART-IDENTITY ADAPTER for the baselines (case-fold + v0.8 §9-F5 folding;
    a non-partner positive becomes no-assertion BEFORE E1, and is excluded from coverage);
  * the directional relation mapping + two-direction combination table (§3.4/§3.5);
  * the inherited coverage numerator C (§5);
  * the full §5 decision-table classification (fixed / second miss) for the tool arm at τ1;
  * the E1-plus-stricter P = 1.00 detection-precision guardrail.

At its first authorized read it VERIFIES the sealed-answer file hashes against their
RECORDED values (from --recorded-hashes, i.e. the freeze-manifest.txt lines bound into H) —
it never re-hashes to DISCOVER the truth; a mismatch aborts before any grading.

Two subcommands (round-8):
  score          the sealed-key scoring read (THE SPEND). Verifies the pre-claim gates (per-H
                 spend log + cross-run custody ledger), key-file existence, and the step-7
                 output-manifest binding BEFORE the atomic claim; writes AGGREGATE-ONLY
                 scores.json and an EMBARGOED per-pair artifact (hash-bound into scores.json,
                 never released here).
  export-embargo NO-KEY exporter: releases the embargoed per-pair diagnostics ONLY after a real
                 post-commit addendum (Q7) — verifies the commit carries the E5.1 marker.

Usage:
  scorer_v010.py score --key-dir <dir> --recorded-hashes <file> --pairs <pairs.json>
                 --H <runs/H.json> --spend-log <log> [--custody-ledger <ledger>]
                 --output-manifest <runs/output-manifest.json>
                 [--tool-verdicts ...] [--baseline-a ...] [--baseline-b ...] --out <scores.json>
  scorer_v010.py export-embargo --repo <repo> --commit <sha> --out <released.json>

--recorded-hashes format: one "sha256␠␠relpath" line per sealed answer file (sha256sum
format), covering at least key/answer_key.json and key/concepts.json.
"""
import json, sys, hashlib, argparse, subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke_v010 as smoke  # sim_flag, norm, HARD_MATCH, NO_MATCH, display
import attest               # load_and_verify_H (H self-consistency)
import spend                # locked one-shot spend gate

HARD_MATCH = smoke.HARD_MATCH               # (exactMatch, broadnarrow, relatedMatch)
NO_MATCH = smoke.NO_MATCH                   # (noMatch, noMatchDespiteSimilarity)
MATCH_CLASS = set(HARD_MATCH)               # planted-positive classes
PRIMARY = "tau1"

# ============================================================================
# 0. sealed-answer custody: verify recorded hashes, then read the key (THE SPEND).
# ============================================================================
def _parse_recorded(recorded_file):
    """sha256sum-format lines -> {relpath: sha256}. relpath is the last whitespace field;
    we key on its basename-tail (key/answer_key.json, key/concepts.json)."""
    recorded = {}
    for line in Path(recorded_file).read_text().splitlines():
        line = line.strip()
        if not line or " " not in line: continue
        h, rel = line.split(None, 1)
        rel = rel.strip()
        if len(h) == 64 and all(c in "0123456789abcdef" for c in h.lower()):
            recorded[rel] = h.lower()
    return recorded

def verify_and_load_key(key_dir, recorded_file):
    """THE SPEND. Verify each sealed answer file against its RECORDED hash, then read
    answer_key.json for grading. Abort on any mismatch/missing recorded hash."""
    key_dir = Path(key_dir)
    recorded = _parse_recorded(recorded_file)
    def recorded_for(name):
        for rel, h in recorded.items():
            if rel == name or rel.endswith("/" + name) or Path(rel).name == name:
                return h
        return None
    for name in ("answer_key.json", "concepts.json"):
        f = key_dir / name
        if not f.exists():
            sys.exit(f"SEALED FILE MISSING: {f}")
        want = recorded_for(name)
        if want is None:
            sys.exit(f"NO RECORDED HASH for {name} in --recorded-hashes — cannot bind by "
                     f"recorded value (prereg §4.2 forbids re-hashing to discover truth)")
        got = hashlib.sha256(f.read_bytes()).hexdigest()
        if got != want:
            sys.exit(f"SEALED-HASH MISMATCH for {name}: recorded {want} != on-disk {got} "
                     f"— aborting before grading (drift / wrong key)")
    ak = json.load(open(key_dir / "answer_key.json"))
    key = {}
    for p in ak["pairs"]:
        key[p["pair_id"]] = {"term_a": p["term_a"], "term_b": p["term_b"],
                             "expected": p["expected"], "broader_side": p.get("broader_side")}
    return key

# ============================================================================
# 1. scoring primitives (copied from the frozen v0.9 smoke.score / is_correct + coverage/P).
#    A verdict dict: {proposed_relation, status, broader_side}. status in
#    {asserted, review_required, insufficient_evidence, config_fail, no_assertion}.
# ============================================================================
def _display(v):
    """Local, tolerant renderer (the frozen smoke.display requires a 'reason' key the lean
    scorer verdicts do not carry)."""
    if v["status"] == "no_assertion": return "no-assertion"
    if v["status"] == "asserted":
        rel = v["proposed_relation"]
        return rel + (f"({v['broader_side']})" if rel == "broadnarrow" else "")
    label = {"review_required": "reviewRequired", "insufficient_evidence": "insufficientEvidence",
             "config_fail": "configFail"}.get(v["status"], v["status"])
    return label + (f"({v['reason']})" if v.get("reason") else "")

def is_correct(kp, v):
    if v["status"] != "asserted": return False       # reviewRequired / no-assertion never correct
    if v["proposed_relation"] != kp["expected"]: return False
    if kp["expected"] == "broadnarrow" and v.get("broader_side") != kp.get("broader_side"):
        return False
    return True

def is_positive(v):
    return v["status"] == "review_required" or (v["status"] == "asserted"
                                                and v["proposed_relation"] in HARD_MATCH)
def is_negative(v):
    return v["status"] == "asserted" and v["proposed_relation"] in NO_MATCH
def is_covered(v):
    # decided = one of the 5 hard relations OR reviewRequired (§5). no_assertion / insuff /
    # configFail excluded.
    return v["status"] == "review_required" or (v["status"] == "asserted"
           and v["proposed_relation"] in (HARD_MATCH + NO_MATCH))

def score_arm(key, verdicts):
    """key: {pid: keypair}; verdicts: {pid: verdict}. Returns S/P/C/jingle/E1b + per_pair.
    Pairs missing from `verdicts` are treated as no_assertion (uncovered abstain)."""
    per = {}
    NA = {"proposed_relation": None, "status": "no_assertion", "broader_side": None}
    for pid, kp in key.items():
        v = verdicts.get(pid, NA)
        per[pid] = {"expected": kp["expected"] + (f"({kp['broader_side']})" if kp["expected"] == "broadnarrow" else ""),
                    "verdict": v, "display": _display(v),
                    "correct": is_correct(kp, v), "positive": is_positive(v),
                    "covered": is_covered(v)}
    S = sum(r["correct"] for r in per.values())
    tp = sum(1 for pid, kp in key.items() if is_positive(per[pid]["verdict"]) and kp["expected"] in MATCH_CLASS)
    fp = sum(1 for pid, kp in key.items() if is_positive(per[pid]["verdict"]) and kp["expected"] in NO_MATCH)
    P = None if (tp + fp) == 0 else round(tp / (tp + fp), 4)
    C = round(sum(r["covered"] for r in per.values()) / len(key), 4)
    jingle = sum(1 for pid, kp in key.items()
                 if kp["expected"] == "noMatchDespiteSimilarity"
                 and per[pid]["verdict"]["status"] == "asserted"
                 and per[pid]["verdict"]["proposed_relation"] == "noMatchDespiteSimilarity")
    # promotions / false-escalations (reported; the P guardrail subsumes them)
    promotions = [pid for pid, kp in key.items() if kp["expected"] in NO_MATCH
                  and per[pid]["verdict"]["status"] == "asserted"
                  and per[pid]["verdict"]["proposed_relation"] in HARD_MATCH]
    false_esc = [pid for pid, kp in key.items() if kp["expected"] in NO_MATCH
                 and per[pid]["verdict"]["status"] == "review_required"]
    return {"S": S, "P": P, "C": C, "jingle_specific": jingle,
            "detection": {"tp": tp, "fp": fp},
            "promotions": promotions, "false_escalations": false_esc, "per_pair": per}

# ============================================================================
# 2. counterpart-identity adapter + directional mapping + combination (§3.4/§3.5).
# ============================================================================
def _adapt_direction(rec, planted_partner):
    """rec: a baseline direction record with final in {positive, negative, no-assertion}
    and (for positives) matched_term/relation. Returns 'NA' | ('negative') |
    ('positive', mapped_relation, broader_side_or_None). The COUNTERPART-IDENTITY ADAPTER:
    a positive whose matched_term does not fold-equal the planted partner -> NA."""
    final = rec.get("final")
    if final == "no-assertion" or final is None: return ("NA",)
    if final == "negative": return ("negative",)
    # positive: adapter check (case-fold + §9-F5 folding == smoke.norm)
    if smoke.norm(rec.get("matched_term") or "") != smoke.norm(planted_partner):
        return ("NA",)  # non-partner positive -> no-assertion before E1, excluded from C
    return ("positive", rec["relation"])

# relation -> (proposed_relation, broader_side) by arm+direction
def _map_relation(relation, arm, direction):
    """Directional relation mapping, positives only, post-adapter (§3.4/§3.5)."""
    r = relation.lower()
    if r == "exact": return ("exactMatch", None)
    if r == "partial-overlap": return ("relatedMatch", None)
    if arm == "A" and direction == "a2b":
        if r == "term-broader": return ("broadnarrow", "a")
        if r == "corpus-broader": return ("broadnarrow", "b")
    if arm == "A" and direction == "b2a":
        if r == "term-broader": return ("broadnarrow", "b")
        if r == "corpus-broader": return ("broadnarrow", "a")
    if arm == "B":  # a2b only; enum {exact, A-broader, B-broader, partial-overlap}
        if r == "a-broader": return ("broadnarrow", "a")
        if r == "b-broader": return ("broadnarrow", "b")
    raise ValueError(f"unmapped relation {relation!r} for arm {arm} dir {direction}")

def _neg_verdict(kp):
    flag = smoke.sim_flag(kp["term_a"], kp["term_b"])
    return {"proposed_relation": "noMatchDespiteSimilarity" if flag else "noMatch",
            "status": "asserted", "broader_side": None}

def _positive_verdict(mapped):
    rel, side = mapped
    return {"proposed_relation": rel, "status": "asserted", "broader_side": side}

def _combine_two(a2b, b2a, kp):
    """§3.4 two-direction combination table (exhaustive; first matching row wins).
    a2b/b2a are ('NA',) | ('negative',) | ('positive', mapped_rel_tuple)."""
    ta, tb = a2b[0], b2a[0]
    if ta == "positive" and tb == "positive":
        va, vb = a2b[1], b2a[1]  # mapped (rel, side)
        if va == ("exactMatch", None) and vb == ("exactMatch", None):
            return {"proposed_relation": "exactMatch", "status": "asserted", "broader_side": None}
        if va[0] == "broadnarrow" and vb[0] == "broadnarrow" and va[1] == vb[1]:
            return {"proposed_relation": "broadnarrow", "status": "asserted", "broader_side": va[1]}
        return {"proposed_relation": "relatedMatch", "status": "asserted", "broader_side": None}
    if ta == "positive" and tb == "negative": return _neg_verdict(kp)
    if ta == "negative" and tb == "positive": return _neg_verdict(kp)
    if ta == "negative" and tb == "negative": return _neg_verdict(kp)
    if ta == "positive" and tb == "NA": return {"proposed_relation": None, "status": "no_assertion", "broader_side": None}
    if ta == "NA" and tb == "positive": return {"proposed_relation": None, "status": "no_assertion", "broader_side": None}
    if ta == "negative" and tb == "NA": return _neg_verdict(kp)
    if ta == "NA" and tb == "negative": return _neg_verdict(kp)
    return {"proposed_relation": None, "status": "no_assertion", "broader_side": None}  # NA/NA

def baseline_a_verdicts(key, records):
    """records keyed by 'side:term' (from baseline_a.py). For pair P: a2b = ('a', term_a),
    b2a = ('b', term_b). Adapter partner: a2b's partner = term_b; b2a's partner = term_a."""
    out = {}
    for pid, kp in key.items():
        ra = records.get(f"a:{kp['term_a']}")
        rb = records.get(f"b:{kp['term_b']}")
        a2b = _adapt_direction(ra, kp["term_b"]) if ra else ("NA",)
        b2a = _adapt_direction(rb, kp["term_a"]) if rb else ("NA",)
        a2b = ("positive", _map_relation(a2b[1], "A", "a2b")) if a2b[0] == "positive" else a2b
        b2a = ("positive", _map_relation(b2a[1], "A", "b2a")) if b2a[0] == "positive" else b2a
        out[pid] = _combine_two(a2b, b2a, kp)
    return out

def baseline_b_verdicts(key, records):
    """records keyed by pair_id (from baseline_b.py); unidirectional A->B. Partner = term_b."""
    out = {}
    for pid, kp in key.items():
        rec = records.get(pid)
        adapted = _adapt_direction(rec, kp["term_b"]) if rec else ("NA",)
        if adapted[0] == "NA":
            out[pid] = {"proposed_relation": None, "status": "no_assertion", "broader_side": None}
        elif adapted[0] == "negative":
            out[pid] = _neg_verdict(kp)
        else:
            out[pid] = _positive_verdict(_map_relation(adapted[1], "B", "a2b"))
    return out

def tool_verdicts_at(tool_verdicts_json, tau):
    """Read the answer-blind composed verdicts.json and reshape τ records into scoring
    verdict dicts."""
    data = json.load(open(tool_verdicts_json))
    recs = data[tau]
    out = {}
    for pid, r in recs.items():
        out[pid] = {"proposed_relation": r.get("proposed_relation"),
                    "status": r["status"], "broader_side": r.get("broader_side")}
    return out

# ============================================================================
# 3. §5 decision table (tool arm at τ1) + P = 1.00 guardrail.
# ============================================================================
def decision_label(sc):
    """sc = score_arm(...) for the tool arm at τ1. Exhaustive; matches the §5 table."""
    S, P, C, jingle = sc["S"], sc["P"], sc["C"], sc["jingle_specific"]
    if P is None:
        return "second miss (reported)", "P = n/a (zero positive assertions; S<=4<7)"
    if P < 1.00:
        # aggregate COUNTS only — no pair-id lists (Q7 embargo)
        return "second miss (reported)", (f"P<1.00 (promotions={len(sc['promotions'])}, "
                                          f"false_escalations={len(sc['false_escalations'])})")
    if S < 7:
        return "second miss (reported)", f"P=1.00 but S={S}<7"
    if jingle == 0:
        return "second miss (reported)", "P=1.00, S>=7 but jingle-specific=0 (inherited E1 jingle clause unmet)"
    if C >= 0.8:
        return "fixed", f"P=1.00, S={S}>=7, jingle>=1, C={C}>=0.8"
    if abs(C - 0.7) < 1e-9:
        return "fixed", f"P=1.00, S={S}>=7, jingle>=1, C=0.7 (mechanism-check shortfall noted; Q1 coverage subordinate)"
    return "second miss (reported)", f"anomaly: P=1.00, S={S}>=7, jingle>=1, C={C} (<0.7 is impossible when S>=7)"

# ============================================================================
# 4. driver
# ============================================================================
def _join_opaque(sealed_key, pairs_file):
    """P0/scorer join: the tool verdicts + baseline_b records are keyed by the OPAQUE pair_id
    from pairs.json (no P01–P10 positional semantics); the sealed key is keyed by its own pids.
    Join on the TERM PAIR (term_a, term_b) to produce a grading map keyed by the opaque id.
    Refuse on any pairing mismatch (a term pair in pairs.json not present in the sealed key,
    a duplicated term pair, or a count mismatch)."""
    pairs = json.load(open(pairs_file))["pairs"]
    sealed_by_tp = {}
    for pid, kp in sealed_key.items():
        tp = (kp["term_a"], kp["term_b"])
        if tp in sealed_by_tp:
            sys.exit(f"PAIRS/KEY: duplicate term pair {tp} in the sealed key — cannot join")
        sealed_by_tp[tp] = kp
    if len(pairs) != len(sealed_by_tp):
        sys.exit(f"PAIRS/KEY: count {len(pairs)} != sealed {len(sealed_by_tp)}")
    key_opaque, seen = {}, set()
    for p in pairs:
        tp = (p["term_a"], p["term_b"])
        if tp not in sealed_by_tp:
            sys.exit(f"PAIRS/KEY MISMATCH: term pair {tp} (opaque {p['pair_id']}) not in the sealed key")
        if tp in seen:
            sys.exit(f"PAIRS/KEY: duplicate term pair {tp} in pairs.json")
        seen.add(tp)
        kp = sealed_by_tp[tp]
        key_opaque[p["pair_id"]] = {"term_a": kp["term_a"], "term_b": kp["term_b"],
                                    "expected": kp["expected"], "broader_side": kp.get("broader_side")}
    return key_opaque

EMBARGO_PATH = BASE / "runs/scoring/.embargo/per-pair.json"


def score(args):
    # round-11 finding 2: in RUNTIME mode the custody ledger is FIXED to the out-of-tree canonical —
    # a --custody-ledger override is REFUSED (it could point at a fresh ledger and bypass a canonical
    # spent/forfeited). --test permits an override for the offline suite ONLY. Checked FIRST, before
    # any H/key work, so the refusal is unambiguous.
    if not args.test:
        if args.custody_ledger and args.custody_ledger != spend.CANONICAL_CUSTODY_LEDGER:
            sys.exit("SCORER-REFUSE: --custody-ledger override is not permitted in runtime mode "
                     "(the canonical out-of-tree ledger is fixed); use --test for the offline suite")
        ledger = spend.CANONICAL_CUSTODY_LEDGER
    else:
        ledger = args.custody_ledger or spend.CANONICAL_CUSTODY_LEDGER
    hobj = attest.load_and_verify_H(args.H)
    run_H = hobj["H"]
    # (a) PRE-CLAIM gate (per-H spend log + cross-run custody ledger): refuse before ANY key/H
    #     work unless the current-H log has exactly one structure:read + an in-range attempt and
    #     no claim/terminal, AND the durable ledger shows the key is not spent/forfeited.
    spend.assert_scoring_allowed(args.spend_log, run_H, custody_ledger=ledger)
    # (a2) key files must EXIST as regular files (no content read) BEFORE claiming (finding 6).
    kd = Path(args.key_dir)
    for name in ("concepts.json", "answer_key.json"):
        f = kd / name
        if not f.is_file() or f.is_symlink():
            sys.exit(f"SCORER-REFUSE (pre-claim): sealed key file {f} missing/not-a-regular-file")
    # (b) bind H + the recorded-hashes file.
    bound = hobj["manifest_of_manifests"].get("recorded_manifest_sha256")
    got = hashlib.sha256(Path(args.recorded_hashes).read_bytes()).hexdigest()
    if bound != got:
        sys.exit(f"RECORDED-HASHES not bound in H: H has {bound} but --recorded-hashes hashes {got}")
    # (b2) OUTPUT-MANIFEST binding (round-9 finding 4): the output-manifest bytes must hash-match
    #     the value bound into the attestation-2 receipt (catches a manifest+input swapped between
    #     attestation-2 and the claim), and EVERY file listed in the manifest — not just the three
    #     scorer inputs — must be present + hash-match. H must bind.
    om = json.load(open(args.output_manifest))
    if om.get("H") != run_H:
        sys.exit(f"output-manifest H {om.get('H')} != attested H {run_H} — abort pre-claim")
    a2 = json.load(open(args.attest2_receipt))
    if a2.get("H") != run_H:
        sys.exit(f"attestation-2 receipt H {a2.get('H')} != attested H {run_H} — abort pre-claim")
    om_sha = hashlib.sha256(Path(args.output_manifest).read_bytes()).hexdigest()
    if a2.get("output_manifest_sha256") != om_sha:
        sys.exit("output-manifest bytes != the hash bound in the attestation-2 receipt — abort pre-claim (unspent)")
    run_root = Path(args.run_root)                          # base the manifest's relpaths resolve against
    for rel, h in om["files"].items():
        p = run_root / rel
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != h:
            sys.exit(f"step-7 output {rel} MISSING/drifted vs the bound output-manifest — abort pre-claim (unspent)")
    # the three direct scorer inputs must be members of that (now verified) manifest.
    def _tail(p):
        return "/".join(Path(p).parts[-2:])
    for path in (args.tool_verdicts, args.baseline_a, args.baseline_b):
        if path and not any(_tail(r) == _tail(path) for r in om["files"]):
            sys.exit(f"scorer input {path} not in the output-manifest — abort pre-claim (unspent)")

    # (c) ONE FAIL-CLOSED ATOMIC CLAIM (round-9 finding 2): under BOTH locks (custody ledger THEN
    #     spend log) re-check availability + the per-H gate, record the cross-run SPEND and the
    #     per-H claim together, immediately before the first key byte. A persistence failure raises.
    spend.atomic_claim(args.spend_log, ledger, run_H, notes="scorer about to read the sealed key")
    sealed_key = verify_and_load_key(args.key_dir, args.recorded_hashes)  # THE SPEND (first key byte)
    key = _join_opaque(sealed_key, args.pairs)

    def aggregate_only(sc, decision=None):
        d = {"S": sc["S"], "P": sc["P"], "C": sc["C"], "jingle_specific": sc["jingle_specific"],
             "detection": {"tp": sc["detection"]["tp"], "fp": sc["detection"]["fp"]},
             "promotions_count": len(sc["promotions"]),
             "false_escalations_count": len(sc["false_escalations"])}
        if decision:
            d["decision"], d["decision_reason"] = decision
        return d
    result = {"tau": args.tau, "H": run_H, "spend": "sealed answer material read (§4.4)"}
    per_pair_export = {}
    if args.tool_verdicts:
        sc = score_arm(key, tool_verdicts_at(args.tool_verdicts, args.tau))
        result["tool_arm"] = aggregate_only(sc, decision_label(sc)); per_pair_export["tool_arm"] = sc["per_pair"]
    if args.baseline_a:
        sc = score_arm(key, baseline_a_verdicts(key, json.load(open(args.baseline_a))))
        result["baseline_a"] = aggregate_only(sc); per_pair_export["baseline_a"] = sc["per_pair"]
    if args.baseline_b:
        sc = score_arm(key, baseline_b_verdicts(key, json.load(open(args.baseline_b))))
        result["baseline_b"] = aggregate_only(sc); per_pair_export["baseline_b"] = sc["per_pair"]
    # (d) during the SINGLE authorized read, write the EMBARGOED per-pair artifact (finding 5) and
    #     bind its hash into the AGGREGATE-ONLY scores.json. It is NOT released here.
    EMBARGO_PATH.parent.mkdir(parents=True, exist_ok=True)
    embargo = {"H": run_H, "per_pair": per_pair_export,
               "note": "EMBARGOED (Q7): release ONLY via `scorer_v010.py export-embargo` with a real "
                       "addendum-commit receipt; the scorer never re-enters the spend gate post-commit."}
    EMBARGO_PATH.write_text(json.dumps(embargo, indent=1))
    result["embargo_sha256"] = hashlib.sha256(EMBARGO_PATH.read_bytes()).hexdigest()
    result["embargo_path"] = str(EMBARGO_PATH.relative_to(BASE))
    json.dump(result, open(args.out, "w"), indent=1)   # AGGREGATE-ONLY (no per_pair/expected/ids)
    spend.complete_authorized_read(args.spend_log, run_H, notes=f"scores -> {args.out}")
    for arm in ("tool_arm", "baseline_a", "baseline_b"):
        if arm in result:
            a = result[arm]
            line = f"{arm}: S={a['S']}/10 P={a['P']} C={a['C']} jingle={a['jingle_specific']}/2"
            if arm == "tool_arm": line += f" -> {a['decision']} ({a['decision_reason']})"
            print(line)
    print(f"\nscores (aggregate-only) -> {args.out}  (per-pair EMBARGOED at {EMBARGO_PATH.relative_to(BASE)})")


def export_embargo(args):
    """NO-KEY exporter (finding 5): release the embargoed per-pair diagnostics ONLY after a real
    addendum commit exists (Q7 post-commit). Verifies that `--commit` is a real commit in `--repo`
    whose tree contains the E5.1 addendum marker in `--addendum-file`; then copies the embargoed
    file to `--out`. Never touches any key path and never enters the spend gate."""
    emb = Path(args.embargo)
    if not emb.exists():
        sys.exit(f"export-embargo: embargoed file {emb} not present (score first)")
    # verify a REAL addendum commit: the commit exists AND its tree's addendum file contains the marker
    ok = subprocess.run(["git", "-C", args.repo, "cat-file", "-e", f"{args.commit}^{{commit}}"],
                        capture_output=True).returncode == 0
    if not ok:
        sys.exit(f"export-embargo REFUSE: {args.commit} is not a commit in {args.repo}")
    show = subprocess.run(["git", "-C", args.repo, "show", f"{args.commit}:{args.addendum_file}"],
                          capture_output=True, text=True)
    if show.returncode != 0 or args.addendum_marker not in show.stdout:
        sys.exit(f"export-embargo REFUSE: commit {args.commit[:12]} tree lacks the {args.addendum_marker!r} "
                 f"addendum in {args.addendum_file} — no genuine post-commit addendum")
    Path(args.out).write_text(emb.read_text())
    print(f"export-embargo: released per-pair diagnostics (addendum commit {args.commit[:12]} verified) -> {args.out}")


def main():
    import argparse as _a
    ap = _a.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("score")
    s.add_argument("--key-dir", required=True); s.add_argument("--recorded-hashes", required=True)
    s.add_argument("--pairs", required=True); s.add_argument("--H", required=True)
    s.add_argument("--spend-log", required=True)
    s.add_argument("--custody-ledger", help="runtime: MUST be the canonical path (or omitted); overridable only with --test")
    s.add_argument("--test", action="store_true", help="offline suite ONLY: permit a --custody-ledger override (round-11 finding 2)")
    s.add_argument("--tool-verdicts"); s.add_argument("--baseline-a"); s.add_argument("--baseline-b")
    s.add_argument("--output-manifest", required=True)
    s.add_argument("--attest2-receipt", default=str(BASE / "runs/attestation-point-2.json"),
                   help="the attestation-2 record binding output_manifest_sha256 (round-9 finding 4)")
    s.add_argument("--run-root", default=str(BASE),
                   help="base that the output-manifest's relpaths resolve against (default: the workspace)")
    s.add_argument("--tau", default=PRIMARY)
    s.add_argument("--out", required=True); s.set_defaults(fn=score)
    e = sub.add_parser("export-embargo")
    e.add_argument("--embargo", default=str(EMBARGO_PATH)); e.add_argument("--repo", required=True)
    e.add_argument("--commit", required=True); e.add_argument("--addendum-file", default="EXPERIMENT-LOG.md")
    e.add_argument("--addendum-marker", default="E5.1"); e.add_argument("--out", required=True)
    e.set_defaults(fn=export_embargo)
    args = ap.parse_args()
    if not getattr(args, "fn", None):
        ap.error("a subcommand is required: score | export-embargo")
    args.fn(args)


if __name__ == "__main__":
    main()
