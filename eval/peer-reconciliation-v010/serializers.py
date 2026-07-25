#!/usr/bin/env python3
"""serializers.py — the ONE normative definition of the byte-level serialization of the
baseline-arm prompt fields (v0.10 prereg §3.6(d)). Prose in the prereg describes intent;
THIS FILE + the golden fixtures define behavior; any divergence resolves in favor of these.

Three serializers, one implementation each, exercised by the golden fixtures (§3.6(c)):
  serialize_a_excerpts(...)        -> Baseline-B  {a_excerpts}
  serialize_b_corpus(...)          -> Baseline-B  {b_corpus}
  serialize_baseline_a_docs(...)   -> Baseline-A retrieved top-3 document block

NORMATIVE RULES (authored here; frozen into H):
- Each serializer returns a PURE CONTENT block: NO leading newline, NO terminal newline.
  The template files own the separators around each placeholder and the single terminal
  newline of the assembled prompt. (This "terminal-newline rule" is defined once, here:
  serializers never emit a trailing newline; the template supplies exactly one.)
- Document/excerpt LABELING (the "first-document labeling rule"): EVERY item is preceded
  by its own header line, including the FIRST one — there is no unlabeled-first-item
  special case. Headers are literal ASCII.
- Encoding is UTF-8 throughout (the corpora contain the masking glyphs ⟦ ⟧ only in the
  tool arm; baseline corpora/excerpts are shown UNMASKED). Document text is emitted with
  its trailing whitespace stripped (`.rstrip()`) and otherwise verbatim.
- Joins:
    * a_excerpts:      items joined by "\n"        (one line per excerpt: "N. <text>")
    * b_corpus:        blocks joined by "\n\n"      (one blank line between documents)
    * baseline_a_docs: blocks joined by "\n\n"      (one blank line between documents)
"""

def serialize_a_excerpts(excerpts):
    """Baseline-B {a_excerpts}. `excerpts` = the tool arm's verification sample for the
    A-term: the first-k pool excerpts in (doc, position) order, k = min(6, pool size) with
    4 <= k <= 6 (a term with <4 excerpts is terminal upstream, per v0.8 §4 — this function
    is only called for a valid sample). UNMASKED. Numbered 1..k in pool order.
    `excerpts` is a list of raw excerpt strings (already selected + ordered upstream)."""
    if not 4 <= len(excerpts) <= 6:
        raise ValueError(f"a_excerpts expects 4..6 excerpts, got {len(excerpts)}")
    return "\n".join(f"{i}. {text.strip()}" for i, text in enumerate(excerpts, 1))

def serialize_b_corpus(docs):
    """Baseline-B {b_corpus}. `docs` = the 11 B documents in ASCENDING filename order as a
    list of (label, text) pairs, label like "b/01" ... "b/11", UNMASKED. Every document
    (including the first) is preceded by a `=== DOCUMENT <label> ===` header line."""
    parts = [f"=== DOCUMENT {label} ===\n{text.rstrip()}" for label, text in docs]
    return "\n\n".join(parts)

def serialize_baseline_a_docs(ranked_docs):
    """Baseline-A retrieved-document block. `ranked_docs` = the top-3 full documents in
    rank order (rank 1 = most similar), a list of (label, text) pairs, label like "b/07"
    (the OTHER community's corpus), UNMASKED. Every document (including rank 1) is preceded
    by a `--- RANK <n> (document <label>) ---` header line."""
    parts = [f"--- RANK {rank} (document {label}) ---\n{text.rstrip()}"
             for rank, (label, text) in enumerate(ranked_docs, 1)]
    return "\n\n".join(parts)

def concat_docs_text(docs):
    """General concatenation utility: the shown documents' text bodies joined by "\\n\\n"
    (labels excluded). NOTE: grounding does NOT use this — per the BUG-1 fix, grounding
    checks each field against SOME SINGLE document (baseline_{a,b}._ground), never the
    concatenation, so a boundary-spanning fabrication cannot validate. Kept as a utility."""
    return "\n\n".join(text.rstrip() for _, text in docs)
