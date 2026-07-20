#!/usr/bin/env python3
"""Constrained-vocabulary vs free-text definition ablation (FLF recall-extender, "Option 1b").

WHAT THIS TESTS
---------------
The recall-extender novelty position (entry §5) cedes almost everything to prior art
and holds exactly ONE claim open as `open (candidate)` (strip 2):

    a *controlled defining vocabulary* for machine-generated cross-community definitions.

Every academic system and shipped product found in the searches on record uses FREE TEXT
for its generated definitions. So the one thing worth putting a number on is:

    Does constraining the definition's vocabulary (plain, jargon-free, community-neutral)
    help, hurt, or not matter for rank-of-owner retrieval, versus a free-text expert
    definition of the same term?

This is designed to try to FALSIFY the open claim, not to confirm it.

THE TWO CONDITIONS (NOT a clean one-variable ablation -- see CAVEATS)
--------------------------------------------------------------------
For each concept, both arms:
  - define the SAME term from the SAME owner-community context, same model;
  - are FORBIDDEN to use the exact term itself (standard lexicographic convention -- a headword
    is never part of its own defining vocabulary -- and it preserves the "lay asker lacks the
    term" premise that the whole tool is about).
They differ PRIMARILY in the defining vocabulary:
  - CONSTRAINED arm : plain/common English only, no field name, no proper names, no jargon.
                      NB this is a PROXY for strip 2's controlled-defining-vocabulary design --
                      it only PROMPTS for plain English; it does NOT supply or enforce a fixed
                      LDOCE-style word list. So it does not test strip 2 on its own terms.
  - FREE-TEXT arm   : natural expert prose, any standard field terminology allowed
                      (the predecessors' condition).
They ALSO differ in persona/purpose framing ("cross-community search key" vs "specialist
glossary") and in resulting length (free comes out ~1.3x longer), so this is not a clean
one-variable ablation. See ablation_analysis.py for the alias-leak + owner/distractor overlap
screen, and the RESULTS doc in the hub vault for the folded Codex-review caveats.

METRIC
------
For each generated definition, embed it with bge-large-en-v1.5 (same model as the main
prototype) and rank all corpus documents by cosine. Report, for the owning sub-field:
  - owner_best_rank : rank of the owner's best-matching doc (lower = better; 1 = top hit)
  - owner_mean_rank : mean rank over all of the owner's docs
  - margin          : (best cosine among owner docs) - (best cosine among non-owner docs).
                      Positive => the owner sits above every distractor. This has headroom
                      even when owner_best_rank saturates at 1, which it may on this easy case.
k samples per (concept, arm) so the constrained-vs-free difference is not a single-draw fluke.

ANCHORS (already measured in results.json): naive_question (floor), raw_term (ceiling).

CAVEATS (folded from a Codex MAJOR-REVISION doc-review, 2026-07-17)
------------------------------------------------------------------
- CIRCULAR: definitions are generated FROM the owner docs and retrieved AGAINST them, so
  absolute rank-1 is partly baked in (the between-arm contrast is still fair; the absolute
  number is not a generalization claim).
- best_rank SATURATES at 1 for both arms => "no difference" here is NOT equivalence.
- Retrieval is to the concept's OWN owner community only; there are no true A<->B cross-
  community pairs, so the cross-community-neutrality *benefit* is NOT measured -- only whether
  jargon-free vocabulary costs owner-recall vs jargon-rich free text.
- The full-headword leak check (term_leaked) is weak; free-text still restates near-headword
  aliases ("apolipoprotein", "particle number", ...). ablation_analysis.py screens those.
n = 3 concepts, 15 docs, one case, one embedding model. In-sample jargon-avoidance pilot.

USAGE (two phases; generation is non-deterministic, embedding is deterministic)
------------------------------------------------------------------------------
  # phase 1: generate + FREEZE definitions (live claude -p)
  python ablation_constrained_vs_free.py --generate --k 3 --model sonnet
  # phase 2: embed the frozen definitions + score (deterministic, offline)
  python ablation_constrained_vs_free.py
"""
from __future__ import annotations

import os, json, argparse, statistics
from pathlib import Path

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import numpy as np

from llm_backend import _claude
from recall_extender import EMB_MODEL, embed, load

HERE = Path(__file__).parent
DEFAULT_DEFS = HERE / "ablation_definitions.json"
DEFAULT_OUT = HERE / "ablation-results.json"

# Both prompts share structure, context, length target, and the "do not name the term" rule.
# They differ ONLY in the vocabulary constraint block. That is the ablated variable.
_SHARED_TASK = (
    "Write a short (3-5 sentence) definition of the term below, describing: what kind of "
    "thing it names, what goes in and what comes out, what it asserts or does, and when it "
    "applies."
)

CONSTRAINED_PROMPT = (
    "You are generating a community-neutral operational definition of a term as it is used by "
    "one research community, to be used as a cross-community search key.\n\n"
    f"{_SHARED_TASK}\n\n"
    "HARD CONSTRAINTS:\n"
    "- Use only plain, common English words plus simple mathematical notation.\n"
    "- Do NOT use the term itself, any proper name (person, method, product, dataset), or the "
    "name of any field of study.\n"
    "- Do NOT name the community. The definition must read the same to any community that works "
    "on the same underlying thing.\n\n"
    "TERM: {term}\n"
    "CONTEXT (how this community writes about it):\n{context}\n\n"
    "Output ONLY the definition text, nothing else."
)

FREE_PROMPT = (
    "You are writing a definition of a technical term as an expert in its field would write it, "
    "for a specialist glossary.\n\n"
    f"{_SHARED_TASK}\n\n"
    "Write naturally and precisely, using whatever standard terminology, field vocabulary, and "
    "technical language an expert in the relevant field would normally use.\n"
    "The ONLY constraint: do NOT use the term itself or restate it verbatim (define it without "
    "naming it).\n\n"
    "TERM: {term}\n"
    "CONTEXT (how this community writes about it):\n{context}\n\n"
    "Output ONLY the definition text, nothing else."
)

# Match the main pipeline's context construction (recall_extender.main): owner docs joined,
# shortened to 1200 chars, so the only difference from the prototype's define() is the prompt.
import textwrap


def _context_for(corpus, owner_community: str) -> str:
    owner_text = " ".join(d["text"] for d in corpus if d["community"] == owner_community)
    return textwrap.shorten(owner_text, 1200)


def generate(k: int, model: str, defs_file: Path) -> dict:
    corpus, concepts = load()
    out = {"model": model, "k": k, "embedding_model": EMB_MODEL,
           "note": "Live-generated via `claude -p`. Both arms forbid the term itself; they "
                   "differ only in the vocabulary constraint (constrained=plain/neutral, "
                   "free=expert jargon allowed). Frozen here for reproducible embedding.",
           "concepts": []}
    for c in concepts:
        term = c["term"]
        owner = c["owning_community"]
        context = _context_for(corpus, owner)
        rec = {"term": term, "owning_community": owner,
               "naive_question": c["naive_question"], "constrained": [], "free": []}
        for arm, prompt in (("constrained", CONSTRAINED_PROMPT), ("free", FREE_PROMPT)):
            for i in range(k):
                p = prompt.format(term=term, context=context)
                text = _claude(p, model=model, timeout=180)
                if not text:
                    raise SystemExit(
                        f"claude -p returned nothing for term={term!r} arm={arm} sample={i}. "
                        "Quota wall or transient failure -- re-run (see feedback_transient_spawn_failure)."
                    )
                # guard: a definition that leaks the exact term breaks the premise for BOTH arms.
                leaked = term.lower() in text.lower()
                rec[arm].append({"sample": i, "text": text, "term_leaked": leaked})
                print(f"  [{term[:24]:24s}] {arm:11s} sample {i}: {len(text):4d} chars"
                      f"{'  ** TERM LEAKED **' if leaked else ''}")
        out["concepts"].append(rec)
    defs_file.write_text(json.dumps(out, indent=2))
    print(f"\n[frozen] {defs_file}")
    return out


def _rank_and_margin(sims_row, doc_ids, owner_ids):
    """Given cosine sims for one query, return (best_rank, mean_rank, margin)."""
    order = np.argsort(-sims_row)
    ranked_ids = [doc_ids[j] for j in order]
    pos = {doc_id: r for r, doc_id in enumerate(ranked_ids, start=1)}
    owner_ranks = sorted(pos[i] for i in owner_ids)
    owner_sims = [sims_row[doc_ids.index(i)] for i in owner_ids]
    nonowner_sims = [sims_row[k] for k, d in enumerate(doc_ids) if d not in owner_ids]
    margin = float(max(owner_sims) - max(nonowner_sims))
    return owner_ranks[0], round(sum(owner_ranks) / len(owner_ranks), 3), round(margin, 4)


def _agg(values):
    return {"mean": round(statistics.mean(values), 3),
            "min": round(min(values), 3), "max": round(max(values), 3),
            "values": [round(v, 3) if isinstance(v, float) else v for v in values]}


def measure(out_path: Path, defs_file: Path):
    if not defs_file.exists():
        raise SystemExit(f"{defs_file} missing -- run with --generate first.")
    defs = json.loads(defs_file.read_text())
    corpus, _ = load()
    doc_ids = [d["id"] for d in corpus]
    doc_comm = {d["id"]: d["community"] for d in corpus}
    doc_text = [d["text"] for d in corpus]

    from sentence_transformers import SentenceTransformer
    print(f"[load] embedding model {EMB_MODEL} ...")
    model = SentenceTransformer(EMB_MODEL)
    doc_emb = embed(model, doc_text, is_query=False)

    results = {"embedding_model": EMB_MODEL, "gen_model": defs["model"], "k": defs["k"],
               "metric_note": "owner_best_rank lower=better (1=top); margin>0 => owner above all "
                              "distractors. Anchors: naive_question=floor, raw_term=ceiling.",
               "concepts": []}
    # accumulate per-arm deltas across concepts for the headline
    headline = {"constrained": {"best_rank": [], "mean_rank": [], "margin": []},
                "free": {"best_rank": [], "mean_rank": [], "margin": []}}

    for c in defs["concepts"]:
        term, owner = c["term"], c["owning_community"]
        owner_ids = [d for d in doc_ids if doc_comm[d] == owner]
        entry = {"term": term, "owning_community": owner, "arms": {}, "anchors": {}}

        # anchors: naive_question (floor), raw_term (ceiling) -- single deterministic queries
        for aname, qtext in (("naive_question", c["naive_question"]), ("raw_term", term)):
            qemb = embed(model, [qtext], is_query=True)
            sims = (qemb @ doc_emb.T)[0]
            br, mr, mg = _rank_and_margin(sims, doc_ids, owner_ids)
            entry["anchors"][aname] = {"best_rank": br, "mean_rank": mr, "margin": mg}

        for arm in ("constrained", "free"):
            texts = [s["text"] for s in c[arm]]
            leaked = [s["term_leaked"] for s in c[arm]]
            qemb = embed(model, texts, is_query=True)
            sims = qemb @ doc_emb.T  # (k, ndocs)
            brs, mrs, mgs = [], [], []
            for qi in range(len(texts)):
                br, mr, mg = _rank_and_margin(sims[qi], doc_ids, owner_ids)
                brs.append(br); mrs.append(mr); mgs.append(mg)
            entry["arms"][arm] = {
                "best_rank": _agg(brs), "mean_rank": _agg(mrs), "margin": _agg(mgs),
                "term_leaked_count": sum(leaked),
                "definitions": texts,
            }
            headline[arm]["best_rank"].append(statistics.mean(brs))
            headline[arm]["mean_rank"].append(statistics.mean(mrs))
            headline[arm]["margin"].append(statistics.mean(mgs))
        results["concepts"].append(entry)

    # headline: per-concept-averaged, then averaged across the 3 concepts
    results["headline"] = {}
    for arm in ("constrained", "free"):
        results["headline"][arm] = {
            "best_rank_mean": round(statistics.mean(headline[arm]["best_rank"]), 3),
            "mean_rank_mean": round(statistics.mean(headline[arm]["mean_rank"]), 3),
            "margin_mean": round(statistics.mean(headline[arm]["margin"]), 4),
        }
    hc, hf = results["headline"]["constrained"], results["headline"]["free"]
    results["headline"]["delta_free_minus_constrained"] = {
        "best_rank": round(hf["best_rank_mean"] - hc["best_rank_mean"], 3),
        "mean_rank": round(hf["mean_rank_mean"] - hc["mean_rank_mean"], 3),
        "margin": round(hf["margin_mean"] - hc["margin_mean"], 4),
    }
    Path(out_path).write_text(json.dumps(results, indent=2))

    # ---- printed report ----
    print("\n==== CONSTRAINED vs FREE-TEXT ABLATION -- run report ====")
    print(f"gen_model={defs['model']}  k={defs['k']}  embedding={EMB_MODEL}\n")
    hdr = f"  {'concept':30s} {'arm':12s} {'best_rank':>18s} {'mean_rank':>18s} {'margin':>20s} {'leak':>5s}"
    print(hdr)
    for e in results["concepts"]:
        for aname, a in e["anchors"].items():
            print(f"  {e['term'][:30]:30s} {'· '+aname:12s} "
                  f"{a['best_rank']:>18} {a['mean_rank']:>18} {a['margin']:>20} {'-':>5s}")
        for arm in ("constrained", "free"):
            a = e["arms"][arm]
            def fmt(d):
                return f"{d['mean']} [{d['min']},{d['max']}]"
            print(f"  {'':30s} {arm:12s} {fmt(a['best_rank']):>18s} {fmt(a['mean_rank']):>18s} "
                  f"{fmt(a['margin']):>20s} {a['term_leaked_count']:>5d}")
        print()
    print("HEADLINE (per-concept mean, then averaged over 3 concepts):")
    print(f"  constrained : best_rank={hc['best_rank_mean']}  mean_rank={hc['mean_rank_mean']}  margin={hc['margin_mean']}")
    print(f"  free        : best_rank={hf['best_rank_mean']}  mean_rank={hf['mean_rank_mean']}  margin={hf['margin_mean']}")
    d = results["headline"]["delta_free_minus_constrained"]
    print(f"  Δ(free - constrained): best_rank={d['best_rank']:+}  mean_rank={d['mean_rank']:+}  margin={d['margin']:+}")
    print(f"    (best_rank/mean_rank: negative Δ => free better; margin: positive Δ => free better)")
    print(f"\n[done] {out_path}")
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generate", action="store_true", help="live-generate + freeze definitions")
    ap.add_argument("--k", type=int, default=3, help="samples per (concept, arm)")
    ap.add_argument("--model", default="sonnet", help="claude -p model for generation")
    ap.add_argument("--defs", default=str(DEFAULT_DEFS), help="frozen definitions JSON (in/out)")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    defs_file = Path(args.defs)
    if args.generate:
        generate(args.k, args.model, defs_file)
    measure(Path(args.out), defs_file)


if __name__ == "__main__":
    main()
