#!/usr/bin/env python3
"""POST-HOC v0.9-CANDIDATE PROBES on the completed v0.8 TRAIN run (TRAIN diagnosis;
not part of the frozen package; cannot fire the sealed TEST). Three probes:

  P-RET  retrieval query-variant sweep (LOCAL ONLY, zero model calls): for every alive
         pair-direction, rank of the best partner-term doc under query = L0 / L1 / L2 /
         L0+L1, hit@3 and hit@5. Question: which variant recovers P05-b2a (and P02-b2a)
         without closing measured-good behavior elsewhere.
  P-CONT dual-family containment: opus re-judges the VERBATIM v0.8 containment prompts
         for P06 (target) and P07/P08/P10 (no-match controls). Question: does a second
         family flip P06 to partial_overlap while the controls stay no_relation
         (unanimity), i.e. is disagreement-escalation informative here.
  P-BUND bundle-level verification tiebreaker pilot: the starvation-mode judge sees the
         whole sample TOGETHER and judges each ladder level with quotes allowed from
         different excerpts. Targets P03-a2b (opus) + P03-b2a (codex, both starved,
         planted broadnarrow) and control P08-b2a (codex, starved, planted jingle —
         a bundle 'covers' here would be a promotion-risk red flag). Judges match the
         original direction judges so the MODE is the only change.

Subcommands: stage | retrieval | score
"""
import json, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke
from smoke import RUNS

DIAG = RUNS / "cf-diagnostic"

BUNDLE_TMPL = """Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): {D0}

DEFINITION L1 (adds mechanism): {D1}

DEFINITION L2 (adds measurement and conditions): {D2}

Below are numbered excerpts from one community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧). All excerpts use the SAME term from the SAME community.

For EACH definition level INDEPENDENTLY, judge whether the excerpts TAKEN TOGETHER support that the referent of ⟦TERM⟧, as used across these excerpts, is an instance of that level's concept:

- "covers" — the combined excerpts collectively instantiate the definition: each element that level commits to (kind; mechanism; measurement and conditions, as applicable) is evidenced SOMEWHERE in the set, and no excerpt contradicts it. Requires 2-4 verbatim quotes, each copied exactly from one numbered excerpt and prefixed with its number ("3: quoted text"), jointly carrying the evidence. Different quotes may come from different excerpts — evidence may accumulate across the set.
- "contradicts" — at least one excerpt is incompatible with that level's definition (the referent has a property the definition excludes, or lacks one it requires). Requires the verbatim quote of the incompatible fragment, number-prefixed.
- "insufficient" — even taken together, the excerpts do not decide for that level.

Do not infer beyond what is written; a level's extra commitments need actual textual evidence, not plausibility.

Output ONLY JSON:
[{"level": "L0", "verdict": "covers|contradicts|insufficient", "quotes": ["1: ...", "5: ..."]},
 {"level": "L1", "verdict": "...", "quotes": ["..."]},
 {"level": "L2", "verdict": "...", "quotes": ["..."]}]

EXCERPTS:
"""

CONT_TARGETS = ["P06", "P07", "P08", "P10"]
BUND_TARGETS = [("P03", "a2b", "claude", "opus"), ("P03", "b2a", "codex", "gpt-5.6-terra"),
                ("P08", "b2a", "codex", "gpt-5.6-terra")]

def stage():
    pairs = smoke.load_pairs()
    terms = smoke.side_terms(pairs)
    meta = json.load(open(RUNS / "verify/meta.json"))
    DIAG.mkdir(exist_ok=True)
    rows = []
    for pid in CONT_TARGETS:  # verbatim v0.8 prompts, second family = opus
        src = RUNS / f"containment/prompt-{pid}.md"
        rows.append(f"claude\topus\t{src}\t{DIAG}/out-cont2-{pid}.json\t{DIAG}/manifest-cont2-{pid}.json")
    for pid, d, cli, model in BUND_TARGETS:
        p = next(x for x in pairs if x["pair_id"] == pid)
        dside = "a" if d == "a2b" else "b"
        dterm = p["term_a"] if dside == "a" else p["term_b"]
        lad = smoke.read_ladder(dside, dterm)
        mm = meta[f"{pid}-{d}"]
        body = (BUNDLE_TMPL.replace("{D0}", lad["L0"]).replace("{D1}", lad["L1"])
                .replace("{D2}", lad["L2"])
                + smoke.numbered(mm["excerpts"], mm["eside"], mm["term"], terms))
        pf = DIAG / f"prompt-bundle-{pid}-{d}.md"; pf.write_text(body)
        rows.append(f"{cli}\t{model}\t{pf}\t{DIAG}/out-bundle-{pid}-{d}.json\t{DIAG}/manifest-bundle-{pid}-{d}.json")
    (DIAG / "probe-calls.tsv").write_text("\n".join(rows) + "\n")
    print(f"{len(rows)} probe calls staged -> {DIAG}/probe-calls.tsv")

def retrieval_sweep():
    from sentence_transformers import SentenceTransformer
    from retrieve_xc import SNAPSHOT
    model = SentenceTransformer(str(SNAPSHOT))
    pairs = smoke.load_pairs()
    docs = {s: [(f.stem, f.read_text()) for f in sorted((BASE / f"corpora/{s}").glob("[0-9][0-9].md"))]
            for s in ("a", "b")}
    emb = {s: model.encode([t for _, t in docs[s]], normalize_embeddings=True) for s in docs}
    variants = ("L0", "L1", "L2", "L0+L1")
    out = {}
    for p in pairs:
        pid = p["pair_id"]; out[pid] = {}
        for d, dside, tside, partner in (("a2b", "a", "b", p["term_b"]), ("b2a", "b", "a", p["term_a"])):
            dterm = p["term_a"] if dside == "a" else p["term_b"]
            lad = smoke.read_ladder(dside, dterm)
            out[pid][d] = {}
            partner_docs = {i for i, (_, t) in enumerate(docs[tside]) if partner.lower() in t.lower()}
            for v in variants:
                q = " ".join(lad[x] for x in v.split("+"))
                qe = model.encode([q], normalize_embeddings=True)[0]
                sims = [float(s) for s in (emb[tside] @ qe)]
                order = sorted(range(len(sims)), key=lambda i: (-sims[i], i))
                best = min((order.index(i) + 1 for i in partner_docs), default=None)
                out[pid][d][v] = {"best_rank": best, "hit3": best is not None and best <= 3,
                                  "hit5": best is not None and best <= 5}
    json.dump(out, open(DIAG / "retrieval-sweep.json", "w"), indent=1)
    hdr = "pair dir  " + "  ".join(f"{v:>6}" for v in variants)
    print(hdr + "   (best partner-doc rank; * = hit@3, + = hit@5-only)")
    for pid in sorted(out):
        for d in ("a2b", "b2a"):
            cells = []
            for v in variants:
                r = out[pid][d][v]
                mark = "*" if r["hit3"] else ("+" if r["hit5"] else " ")
                cells.append(f"{str(r['best_rank']):>5}{mark}")
            print(f"{pid} {d:>4} " + "  ".join(cells))
    for v in variants:
        mut = {pid: out[pid]["a2b"][v]["hit3"] and out[pid]["b2a"][v]["hit3"] for pid in out}
        ei = {pid: out[pid]["a2b"][v]["hit3"] or out[pid]["b2a"][v]["hit3"] for pid in out}
        print(f"{v}: mutual@3 = {sorted(k for k, x in mut.items() if x)} | either@3 = {sorted(k for k, x in ei.items() if x)}")

def score():
    pairs = smoke.load_pairs()
    terms = smoke.side_terms(pairs)
    meta = json.load(open(RUNS / "verify/meta.json"))
    print("== P-CONT: dual-family containment (codex verdict -> opus verdict) ==")
    for pid in CONT_TARGETS:
        v8 = smoke.validate_containment(smoke.parse_json_out(RUNS / f"containment/out-{pid}.json"))
        f = DIAG / f"out-cont2-{pid}.json"
        obj = smoke.validate_containment(smoke.parse_json_out(f)) if f.exists() else None
        p = next(x for x in pairs if x["pair_id"] == pid)
        quotes_ok = None
        if obj and obj["relation"] != "unclear":
            r = smoke.containment_result.__name__  # noqa - inline validation below
            s1 = smoke.sample_of(smoke.load_exc()["a"][p["term_a"]])
            s2 = smoke.sample_of(smoke.load_exc()["b"][p["term_b"]])
            q1, q2 = smoke.norm(obj["quote_1"]), smoke.norm(obj["quote_2"])
            ok1 = bool(q1) and any(q1 in smoke.norm(smoke.mask_text(e["text"], "a", p["term_a"], terms, "⟦T1⟧")) for e in s1)
            ok2 = bool(q2) and any(q2 in smoke.norm(smoke.mask_text(e["text"], "b", p["term_b"], terms, "⟦T2⟧")) for e in s2)
            quotes_ok = ok1 and ok2
        agree = obj and v8 and obj["relation"] == v8["relation"]
        print(f"  {pid} (expected {p['expected']}): codex={v8['relation'] if v8 else '?'} -> opus="
              f"{obj['relation'] if obj else 'MISSING/unparseable'} quotes_ok={quotes_ok} {'AGREE' if agree else '** DISAGREE **'}")
        if obj: print(f"       opus justification: {obj['justification'][:160]}")
    print("\n== P-BUND: bundle-level verification (per-excerpt starved -> bundle verdicts) ==")
    for pid, d, _, _ in BUND_TARGETS:
        f = DIAG / f"out-bundle-{pid}-{d}.json"
        rows = smoke.parse_json_out(f) if f.exists() else None
        p = next(x for x in pairs if x["pair_id"] == pid)
        mm = meta[f"{pid}-{d}"]
        masked = smoke.masked_sample_texts(mm, terms)
        if not isinstance(rows, list):
            print(f"  {pid}-{d}: MISSING/unparseable"); continue
        print(f"  {pid}-{d} (expected {p['expected']}):")
        for r in rows:
            lvl, verdict = r.get("level"), r.get("verdict")
            qs = r.get("quotes") or []
            valid = 0
            for q in qs:
                m = re.match(r"^(\d+)\s*[:.]\s*(.*)$", str(q).strip(), re.S)
                if not m: continue
                i, txt = int(m.group(1)), smoke.norm(m.group(2))
                if 1 <= i <= len(masked) and txt and txt in smoke.norm(masked[i - 1]): valid += 1
            need = 0 if lvl == "L0" else (1 if verdict == "contradicts" else 2)
            ok = verdict == "insufficient" or valid >= need
            print(f"    {lvl}: {verdict:<13} quotes {valid}/{len(qs)} valid -> {'STANDS' if ok else 'FAILS-VALIDATION'}")

if __name__ == "__main__":
    {"stage": stage, "retrieval": retrieval_sweep, "score": score}[sys.argv[1]]()
