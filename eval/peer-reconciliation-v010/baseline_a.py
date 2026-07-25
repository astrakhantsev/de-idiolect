#!/usr/bin/env python3
"""baseline_a.py — Baseline-A (bare-coinage naive-ask), v0.10 prereg §3.4.

Per-term INDEPENDENT presentation: each of the 10 A-terms is one call (the bare term as
the retrieval query + its top-3 B-docs), symmetric for the 10 B-terms (bidirectional) —
20 adjudication calls. NEVER two planted-partner terms in one prompt. Retrieval is the
frozen v0.8 §2.6 full-document unit reused VERBATIM, term as query. Each attempt (first
ask, re-ask) is a new isolated single-turn invocation via the frozen isolation wrapper
(run_calls.sh -> ../e2e-cell/run_isolated.sh), §3.6(e).

ANSWER-BLIND: reads pairs.json (term lists) + corpora only; never the sealed key. Parsing
(parser_adjudicator, shared grammar) + one re-ask + key-blind grounding happen here; the
COUNTERPART-IDENTITY ADAPTER, the two-direction combination, and grading are in
scorer_v010.py (the only key-bearing component).

Subcommands:
  retrieve   bare-term top-3 retrieval for all 20 terms   (NEEDS the BGE model + venv)
  prompts    assemble the 20 first-ask prompts + stage calls
  gate       parse outputs; stage <=1 re-ask per term; key-blind grounding; write records
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke_v010 as smoke
from assemble import assemble_baseline_a
from parser_adjudicator import parse_adjudication, RELATION_ENUM_A, POSITIVE, NEGATIVE, MALFORMED

OUT = BASE / "runs" / "baseline_a"
# frozen v0.8 §2.6 encoder snapshot (bound in H by its recorded v0.9 tree hash)
SNAPSHOT = Path("/home/nik/.cache/huggingface/hub/models--BAAI--bge-large-en-v1.5/"
                "snapshots/d4aa6901d3a41ba39fb536a557fa166f842b0e09")


def _load_corpus(side):
    docs = [(f"{side}/{f.stem}", f.read_text())
            for f in sorted((BASE / f"corpora/{side}").glob("[0-9][0-9].md"))]
    assert len(docs) == 11, f"corpus {side}: expected 11 docs, got {len(docs)}"
    return docs


def _term_dirs(pairs):
    """The 20 (side, term, direction, other_side) tuples. A-term -> direction a2b (queried
    against B corpus); B-term -> b2a. Order: all A terms then all B terms, in pair order."""
    out = []
    for p in pairs:
        out.append(("a", p["term_a"], "a2b", "b"))
    for p in pairs:
        out.append(("b", p["term_b"], "b2a", "a"))
    return out


def retrieve(pairs):
    """§2.6 verbatim, term as query. Bare term string -> other side's 11-doc corpus, top-3
    (rank_top3 = sort by (-sim, index)). Local, deterministic. NEEDS venv + BGE model."""
    from sentence_transformers import SentenceTransformer
    assert SNAPSHOT.is_dir(), f"bge snapshot not found at {SNAPSHOT}"
    model = SentenceTransformer(str(SNAPSHOT))
    corp = {"a": _load_corpus("a"), "b": _load_corpus("b")}
    emb = {s: model.encode([t for _, t in corp[s]], normalize_embeddings=True) for s in corp}
    res = {}
    for side, term, direction, oside in _term_dirs(pairs):
        q = model.encode([term], normalize_embeddings=True)[0]
        sims = [float(x) for x in (emb[oside] @ q)]
        top3 = smoke.rank_top3(sims)
        res[f"{side}:{term}"] = {"side": side, "term": term, "direction": direction,
                                 "other_side": oside,
                                 "top3": [[corp[oside][i][0], sims[i]] for i in top3]}
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(res, open(OUT / "retrieval.json", "w"), indent=1)
    print(f"baseline-A retrieval: {len(res)} terms -> {OUT/'retrieval.json'}")


def _doc_text(label):
    side, stem = label.split("/")
    return (BASE / f"corpora/{side}/{stem}.md").read_text()


def _out_path(side, term, r): return OUT / f"out-{side}-{smoke.slug(term)}-r{r}.txt"
def _manifest(side, term, r): return BASE / "runs" / "manifests" / f"baseline-a-{side}-{smoke.slug(term)}-r{r}.json"
def _prompt_path(side, term, r):
    tag = "" if r == 0 else "-reask"
    return OUT / f"prompt-{side}-{smoke.slug(term)}{tag}.md"


def prompts(pairs):
    retr = json.load(open(OUT / "retrieval.json"))
    OUT.mkdir(parents=True, exist_ok=True)
    (BASE / "runs" / "manifests").mkdir(parents=True, exist_ok=True)
    rows = []
    for side, term, direction, oside in _term_dirs(pairs):
        r = retr[f"{side}:{term}"]
        docs = [(label, _doc_text(label)) for label, _sim in r["top3"]]
        _prompt_path(side, term, 0).write_text(assemble_baseline_a(term, docs, reask=False))
        smoke.stage_call(rows, "claude", "claude-sonnet-5", _prompt_path(side, term, 0),
                         _out_path(side, term, 0), _manifest(side, term, 0))
    (OUT / "calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    print(f"baseline-A: {len(rows)} first-ask calls staged")


def _ground(fields, docs):
    """key-blind grounding (§3.4; BUG-1 fix — SINGLE-document): matched_term AND evidence
    must EACH be a contiguous substring of at least one INDIVIDUAL retrieved document's text
    under §9-F5 folding (smoke.norm). Grounding against the concatenation would falsely
    validate a span that crosses a document boundary (a fabrication present in no single
    document); §9-F5 quote validation is per the single text the judge saw. The two fields
    may live in different documents (each must be within some single doc); only a single span
    crossing a boundary fails."""
    mt, ev = smoke.norm(fields["matched_term"]), smoke.norm(fields["evidence"])
    if not (mt and ev):
        return False
    doc_hays = [smoke.norm(text) for _label, text in docs]
    return any(mt in h for h in doc_hays) and any(ev in h for h in doc_hays)


def gate(pairs):
    retr = json.load(open(OUT / "retrieval.json"))
    state_f = OUT / "state.json"
    state = json.load(open(state_f)) if state_f.exists() else {}
    reask_rows, records = [], {}
    for side, term, direction, oside in _term_dirs(pairs):
        key = f"{side}:{term}"
        st = state.setdefault(key, {"reask_used": 0, "final": None})
        if st["final"] is not None:
            records[key] = st["final"]; continue
        r = st["reask_used"]
        out_f, man_f = _out_path(side, term, r), _manifest(side, term, r)

        def _stage_reask():  # consume the ONE re-ask; stage a fresh r=1 isolated call
            st["reask_used"] = 1
            docs_re = [(label, _doc_text(label)) for label, _s in retr[key]["top3"]]
            _prompt_path(side, term, 1).write_text(assemble_baseline_a(term, docs_re, reask=True))
            smoke.stage_call(reask_rows, "claude", "claude-sonnet-5", _prompt_path(side, term, 1),
                             _out_path(side, term, 1), _manifest(side, term, 1))

        if not smoke.call_attempted(man_f):                    # never attempted -> stage, no budget
            smoke.stage_call(reask_rows, "claude", "claude-sonnet-5", _prompt_path(side, term, r), out_f, man_f)
            continue
        if not smoke.call_completed(out_f, man_f):
            if out_f.exists():                                 # interrupted -> re-exec SAME r, no budget
                out_f.unlink(); man_f.unlink()
                smoke.stage_call(reask_rows, "claude", "claude-sonnet-5", _prompt_path(side, term, r), out_f, man_f)
                continue
            # attempted-and-FAILED (run_calls deleted the output) -> frozen failure policy
            if st["reask_used"] == 0:
                _stage_reask(); continue
            rec = {"term": term, "side": side, "direction": direction,
                   "final": "no-assertion", "final_reason": "call-failed-after-reask"}
            st["final"] = rec; records[key] = rec; continue
        parsed = parse_adjudication(out_f.read_text(), RELATION_ENUM_A)
        docs = [(label, _doc_text(label)) for label, _s in retr[key]["top3"]]
        rec = {"term": term, "side": side, "direction": direction,
               "classification": parsed["classification"], "reason": parsed["reason"],
               **parsed["fields"]}
        if parsed["classification"] == MALFORMED:
            if st["reask_used"] == 0:
                _stage_reask(); continue
            rec["final"] = "no-assertion"; rec["final_reason"] = "malformed-after-reask"
        elif parsed["classification"] == NEGATIVE:
            rec["final"] = "negative"
        else:  # POSITIVE -> grounding
            if _ground(parsed["fields"], docs):
                rec["final"] = "positive"; rec["grounded"] = True
            else:
                rec["final"] = "no-assertion"; rec["final_reason"] = "grounding-failed"; rec["grounded"] = False
        st["final"] = rec
        records[key] = rec
    (OUT / "reask-calls.tsv").write_text("\n".join(reask_rows) + ("\n" if reask_rows else ""))
    json.dump(state, open(state_f, "w"), indent=1)
    json.dump(records, open(OUT / "records.json", "w"), indent=1)
    done = sum(1 for r in records.values() if isinstance(r, dict))
    print(f"baseline-A gate: {done}/20 finalized; {len(reask_rows)} re-ask/pending rows staged")


def main():
    cmd = sys.argv[1]
    pairs = smoke.load_pairs()
    {"retrieve": retrieve, "prompts": prompts, "gate": gate}[cmd](pairs)


if __name__ == "__main__":
    main()
