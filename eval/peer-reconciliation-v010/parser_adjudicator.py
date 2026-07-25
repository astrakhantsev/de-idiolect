#!/usr/bin/env python3
r"""parser_adjudicator.py — the ONE total grammar over a baseline adjudicator reply
(v0.10 prereg §3.6(a)), shared by Baseline-A and Baseline-B. Prose in the prereg describes
intent; THIS FILE + the golden fixtures define behavior; divergence resolves in favor of
these artifacts.

Every reply maps to EXACTLY ONE of {well-formed positive, well-formed negative, malformed}.
The only per-arm difference is the `relation` enum, passed in as `relation_enum`:
  Baseline-A: RELATION_ENUM_A = {exact, term-broader, corpus-broader, partial-overlap}
  Baseline-B: RELATION_ENUM_B = {exact, A-broader, B-broader, partial-overlap}
plus "n/a" in both (the negative sentinel).

The adjudicator is asked to return exactly four fields, one per line:
  match:        yes | no
  matched_term: <verbatim other-side term string> | none
  relation:     <one of relation_enum> | n/a
  evidence:     <verbatim quoted span> | none

GRAMMAR (authored here; frozen into H):

1. FIELD EXTRACTION. The reply is split into physical lines. A line is a FIELD line iff it
   matches, case-insensitively on the key, `^\s*(match|matched_term|relation|evidence)\s*:\s*(.*)$`.
   The captured value is the remainder of the line with surrounding whitespace stripped.
   Any line that is not a field line is IGNORED — this is how "surrounding or extra text"
   (preamble, postamble, markdown fences, reasoning) is tolerated.

2. FIELD SET + DUPLICATES. Exactly the four fields {match, matched_term, relation, evidence}
   must each appear EXACTLY ONCE. A missing field OR a duplicate field (a key appearing two
   or more times, regardless of value) -> malformed. (Duplicate handling is defined as a
   hard reject: two different values are ambiguous, and two identical values signal a
   malformed template echo; either way the reply is not cleanly one record.)

3. VALUE NORMALIZATION.
   - `match` and `relation` values are compared case-insensitively (lower-cased).
   - `matched_term` and `evidence` values are kept VERBATIM except that (a) surrounding
     whitespace is stripped, and (b) at most ONE balanced pair of surrounding double quotes
     — ASCII " or curly “ ” — is removed (a common, benign wrapper; removing it recovers
     the verbatim span). The sentinel "none" is detected case-insensitively AFTER this.

4. ENUM VALIDATION.
   - match must be exactly "yes" or "no" (lower-cased). Otherwise -> malformed.
   - relation must be in relation_enum ∪ {"n/a"} (lower-cased). Otherwise -> malformed.
     (relation_enum members are compared lower-cased too, so "A-broader" matches "a-broader".)

5. CROSS-FIELD TRUTH TABLE (frozen, §3.4).
   - match == "no"  => requires matched_term == "none" (ci) AND relation == "n/a"
       AND evidence == "none" (ci). If satisfied -> WELL-FORMED NEGATIVE; else -> malformed.
   - match == "yes" => requires matched_term is present, non-empty, and not "none" (ci)
       AND evidence is present, non-empty, and not "none" (ci)
       AND relation is in relation_enum (i.e. NOT "n/a"). If satisfied -> WELL-FORMED
       POSITIVE; else -> malformed.

The parser is PURE and key-blind: it never reads corpora, excerpts, or the answer key. The
downstream key-blind GROUNDING check (matched_term/evidence must be substrings of the shown
documents) and the key-bearing COUNTERPART-IDENTITY ADAPTER (matched_term must fold-equal
the planted partner) live in the baseline runners / scorer, NOT here.
"""
import re

RELATION_ENUM_A = frozenset({"exact", "term-broader", "corpus-broader", "partial-overlap"})
RELATION_ENUM_B = frozenset({"exact", "a-broader", "b-broader", "partial-overlap"})

POSITIVE, NEGATIVE, MALFORMED = "positive", "negative", "malformed"
_FIELDS = ("match", "matched_term", "relation", "evidence")
_LINE = re.compile(r"^\s*(match|matched_term|relation|evidence)\s*:\s*(.*)$", re.IGNORECASE)


def _strip_quotes(v):
    """Strip at most ONE genuinely MATCHED wrapper pair: ASCII " … " OR curly “ … ”.
    A MIXED wrapper ("…” or “…") is NOT balanced and is left intact (checking opener and
    closer independently would wrongly strip these malformed Unicode variants)."""
    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "“" and v[-1] == "”")):
        return v[1:-1].strip()
    return v


def parse_adjudication(text, relation_enum):
    """Classify a reply. `relation_enum` = a set/frozenset of the arm's POSITIVE relation
    strings (lower-cased comparison). Returns a dict:
        {classification: positive|negative|malformed,
         reason: str,
         fields: {match, matched_term, relation, evidence}}   # None where absent
    `fields` are the normalized values (matched_term/evidence verbatim-minus-wrapper-quotes;
    match/relation lower-cased) so downstream grounding/adapter can use them directly.
    On malformed, `fields` holds whatever was parsed (best-effort), for logging only.
    """
    relation_enum = {r.lower() for r in relation_enum}
    counts = {f: 0 for f in _FIELDS}
    raw = {f: None for f in _FIELDS}
    for line in text.splitlines():
        m = _LINE.match(line)
        if not m:
            continue
        key = m.group(1).lower()
        counts[key] += 1
        raw[key] = m.group(2).strip()

    def result(cls, reason):
        fields = {
            "match": (raw["match"].lower() if raw["match"] is not None else None),
            "matched_term": (_strip_quotes(raw["matched_term"]) if raw["matched_term"] is not None else None),
            "relation": (raw["relation"].lower() if raw["relation"] is not None else None),
            "evidence": (_strip_quotes(raw["evidence"]) if raw["evidence"] is not None else None),
        }
        return {"classification": cls, "reason": reason, "fields": fields}

    # 2. exactly-once field set
    missing = [f for f in _FIELDS if counts[f] == 0]
    dup = [f for f in _FIELDS if counts[f] > 1]
    if missing:
        return result(MALFORMED, f"missing-field:{','.join(missing)}")
    if dup:
        return result(MALFORMED, f"duplicate-field:{','.join(dup)}")

    match = raw["match"].lower()
    matched_term = _strip_quotes(raw["matched_term"])
    relation = raw["relation"].lower()
    evidence = _strip_quotes(raw["evidence"])

    # 4. enum validation
    if match not in ("yes", "no"):
        return result(MALFORMED, f"bad-match-enum:{match!r}")
    if relation not in (relation_enum | {"n/a"}):
        return result(MALFORMED, f"bad-relation-enum:{relation!r}")

    mt_is_none = matched_term.lower() == "none"
    ev_is_none = evidence.lower() == "none"

    # 5. cross-field truth table
    if match == "no":
        if mt_is_none and relation == "n/a" and ev_is_none:
            return result(NEGATIVE, "well-formed-negative")
        return result(MALFORMED, "negative-cross-field-violation")
    else:  # match == "yes"
        if (not mt_is_none and matched_term) and (not ev_is_none and evidence) and relation in relation_enum:
            return result(POSITIVE, "well-formed-positive")
        return result(MALFORMED, "positive-cross-field-violation")


def enum_for_arm(arm):
    """arm in {'A','B'}."""
    if arm == "A":
        return RELATION_ENUM_A
    if arm == "B":
        return RELATION_ENUM_B
    raise ValueError(f"unknown arm {arm!r}")
