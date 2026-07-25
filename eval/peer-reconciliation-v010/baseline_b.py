#!/usr/bin/env python3
"""baseline_b.py — Baseline-B (equal-information direct ask), v0.10 prereg §3.5, Q2=YES.

10 calls (unidirectional A->B covers all 10 pairs). Each prompt = {term_a} (raw A-side
term) + {a_excerpts} (the tool arm's verification sample: first-k pool excerpts in (doc,
position) order, k=min(6,pool), 4<=k<=6, UNMASKED) + {b_corpus} (the 11 B docs in filename
order, UNMASKED, joined by the serializers.py separator). A term with <4 excerpts is
terminal (v0.8 §4) -> its Baseline-B pair = no-assertion. Each attempt (first ask, re-ask)
is a NEW isolated single-turn invocation (§3.6(e)).

ANSWER-BLIND: reads pairs.json (term list) + excerpts.json + B corpus only; never the key.
matched_term validation against corpus text (grounding) is key-blind and lives here; the
COUNTERPART-IDENTITY ADAPTER + grading are in scorer_v010.py.

Subcommands:
  prompts   assemble the 10 first-ask prompts + stage calls
  gate      parse outputs; stage <=1 re-ask per pair; key-blind grounding; write records
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import smoke_v010 as smoke
from assemble import assemble_baseline_b
from parser_adjudicator import parse_adjudication, RELATION_ENUM_B, POSITIVE, NEGATIVE, MALFORMED

OUT = BASE / "runs" / "baseline_b"


def _b_corpus_docs():
    return [(f"b/{f.stem}", f.read_text())
            for f in sorted((BASE / "corpora/b").glob("[0-9][0-9].md"))]


def _out_path(pid, r): return OUT / f"out-{pid}-r{r}.txt"
def _manifest(pid, r): return BASE / "runs" / "manifests" / f"baseline-b-{pid}-r{r}.json"
def _prompt_path(pid, r):
    return OUT / f"prompt-{pid}{'' if r == 0 else '-reask'}.md"


def prompts(pairs):
    exc = smoke.load_exc()
    OUT.mkdir(parents=True, exist_ok=True)
    (BASE / "runs" / "manifests").mkdir(parents=True, exist_ok=True)
    bdocs = _b_corpus_docs()
    rows, terminal = [], {}
    for p in pairs:
        pid, term_a = p["pair_id"], p["term_a"]
        sample = smoke.sample_of(exc["a"][term_a])
        if len(sample) < smoke.MIN_EXC:            # v0.8 §4 floor -> terminal no-assertion
            terminal[pid] = f"a-excerpts<4:n={len(sample)}"; continue
        _prompt_path(pid, 0).write_text(
            assemble_baseline_b(term_a, [e["text"] for e in sample], bdocs, reask=False))
        smoke.stage_call(rows, "claude", "claude-sonnet-5", _prompt_path(pid, 0),
                         _out_path(pid, 0), _manifest(pid, 0))
    (OUT / "calls.tsv").write_text("\n".join(rows) + ("\n" if rows else ""))
    json.dump(terminal, open(OUT / "terminal.json", "w"), indent=1)
    print(f"baseline-B: {len(rows)} first-ask calls staged; terminal(floor)={terminal or 'none'}")


def _ground(fields, bdocs):
    """key-blind grounding (§3.5; BUG-1 fix — SINGLE-document): matched_term AND evidence
    must EACH be a contiguous substring of at least one INDIVIDUAL B-corpus document's text
    under §9-F5 folding (smoke.norm) — never of the concatenation (which would falsely
    validate a boundary-spanning fabrication). The two fields may live in different B docs;
    only a single span crossing a boundary fails."""
    mt, ev = smoke.norm(fields["matched_term"]), smoke.norm(fields["evidence"])
    if not (mt and ev):
        return False
    doc_hays = [smoke.norm(text) for _label, text in bdocs]
    return any(mt in h for h in doc_hays) and any(ev in h for h in doc_hays)


def gate(pairs):
    exc = smoke.load_exc()
    terminal = json.load(open(OUT / "terminal.json"))
    bdocs = _b_corpus_docs()
    state_f = OUT / "state.json"
    state = json.load(open(state_f)) if state_f.exists() else {}
    reask_rows, records = [], {}
    for p in pairs:
        pid, term_a = p["pair_id"], p["term_a"]
        if pid in terminal:
            records[pid] = {"pair_id": pid, "direction": "a2b", "final": "no-assertion",
                            "final_reason": terminal[pid]}
            continue
        st = state.setdefault(pid, {"reask_used": 0, "final": None})
        if st["final"] is not None:
            records[pid] = st["final"]; continue
        r = st["reask_used"]
        out_f, man_f = _out_path(pid, r), _manifest(pid, r)

        def _stage_reask():  # consume the ONE re-ask; stage a fresh r=1 isolated call
            st["reask_used"] = 1
            sample = smoke.sample_of(exc["a"][term_a])
            _prompt_path(pid, 1).write_text(
                assemble_baseline_b(term_a, [e["text"] for e in sample], bdocs, reask=True))
            smoke.stage_call(reask_rows, "claude", "claude-sonnet-5", _prompt_path(pid, 1),
                             _out_path(pid, 1), _manifest(pid, 1))

        if not smoke.call_attempted(man_f):                    # never attempted -> stage, no budget
            smoke.stage_call(reask_rows, "claude", "claude-sonnet-5", _prompt_path(pid, r), out_f, man_f)
            continue
        if not smoke.call_completed(out_f, man_f):
            if out_f.exists():                                 # interrupted -> re-exec SAME r, no budget
                out_f.unlink(); man_f.unlink()
                smoke.stage_call(reask_rows, "claude", "claude-sonnet-5", _prompt_path(pid, r), out_f, man_f)
                continue
            # attempted-and-FAILED (run_calls deleted the output) -> frozen failure policy
            if st["reask_used"] == 0:
                _stage_reask(); continue
            rec = {"pair_id": pid, "term_a": term_a, "direction": "a2b",
                   "final": "no-assertion", "final_reason": "call-failed-after-reask"}
            st["final"] = rec; records[pid] = rec; continue
        parsed = parse_adjudication(out_f.read_text(), RELATION_ENUM_B)
        rec = {"pair_id": pid, "term_a": term_a, "direction": "a2b",
               "classification": parsed["classification"], "reason": parsed["reason"],
               **parsed["fields"]}
        if parsed["classification"] == MALFORMED:
            if st["reask_used"] == 0:
                _stage_reask(); continue
            rec["final"] = "no-assertion"; rec["final_reason"] = "malformed-after-reask"
        elif parsed["classification"] == NEGATIVE:
            rec["final"] = "negative"
        else:
            if _ground(parsed["fields"], bdocs):
                rec["final"] = "positive"; rec["grounded"] = True
            else:
                rec["final"] = "no-assertion"; rec["final_reason"] = "grounding-failed"; rec["grounded"] = False
        st["final"] = rec
        records[pid] = rec
    (OUT / "reask-calls.tsv").write_text("\n".join(reask_rows) + ("\n" if reask_rows else ""))
    json.dump(state, open(state_f, "w"), indent=1)
    json.dump(records, open(OUT / "records.json", "w"), indent=1)
    print(f"baseline-B gate: {len(records)}/10 finalized; {len(reask_rows)} re-ask/pending rows staged")


def main():
    cmd = sys.argv[1]
    pairs = smoke.load_pairs()
    {"prompts": prompts, "gate": gate}[cmd](pairs)


if __name__ == "__main__":
    main()
