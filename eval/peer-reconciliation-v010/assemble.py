#!/usr/bin/env python3
"""assemble.py — the ONE definition of how a baseline prompt's assembled bytes are built
from the literal template file + the serializers. Both the baseline runners (baseline_a.py,
baseline_b.py) AND the conformance runner (conformance_runner.py) call these, so the golden
fixtures pin exactly the bytes the run will send. (v0.10 prereg §3.6(b)+(d).)

Assembled bytes = template with each placeholder replaced by its serialized value. The
serializers emit pure content (no leading/terminal newline); the template owns the
surrounding separators and the single terminal newline. `reask=True` selects the arm's own
literal re-ask file (Baseline-B's re-ask is its own file, not A's edited — §3.6(b)).

SUBSTITUTION SEMANTICS (BUG-2 fix): substitution is SINGLE-PASS over the template — all
placeholders are replaced in one left-to-right scan and inserted values are NEVER re-scanned.
So a serialized input that happens to contain a placeholder-like token (e.g. an excerpt
containing the literal "{B_CORPUS}") is inserted VERBATIM, not re-substituted. (Chained
`str.replace` calls would re-substitute a later placeholder that appeared inside an
earlier-inserted value.)
"""
import re
from pathlib import Path
from serializers import serialize_a_excerpts, serialize_b_corpus, serialize_baseline_a_docs

BASE = Path(__file__).resolve().parent

def _tmpl(name):
    return (BASE / "prompts" / name).read_text()

def _fill(template, mapping):
    """Single-pass placeholder substitution. `mapping` = {placeholder: value}. Each
    placeholder is matched literally; longer keys first (defensive against one key being a
    prefix of another); the replacement is a FUNCTION so inserted values are never re-scanned
    and never interpreted as regex backreferences."""
    keys = sorted(mapping, key=len, reverse=True)
    pat = re.compile("|".join(re.escape(k) for k in keys))
    return pat.sub(lambda m: mapping[m.group(0)], template)

def assemble_baseline_a(term, ranked_docs, reask=False):
    """ranked_docs: [(label, text), ...] top-3 in rank order."""
    tmpl = _tmpl("baseline-a-reask.md" if reask else "baseline-a.md")
    return _fill(tmpl, {"{TERM}": term,
                        "{RETRIEVED_DOCS}": serialize_baseline_a_docs(ranked_docs)})

def assemble_baseline_b(term_a, excerpts, docs, reask=False):
    """excerpts: [str,...] (4..6); docs: [(label, text), ...] the 11 B docs in order."""
    tmpl = _tmpl("baseline-b-reask.md" if reask else "baseline-b.md")
    return _fill(tmpl, {"{TERM_A}": term_a,
                        "{A_EXCERPTS}": serialize_a_excerpts(excerpts),
                        "{B_CORPUS}": serialize_b_corpus(docs)})
