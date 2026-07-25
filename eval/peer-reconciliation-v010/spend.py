#!/usr/bin/env python3
"""spend.py — the enforced spend/state gate (v0.10 prereg §4.3/§4.4). Shared by attest.py,
make_pairs_manifest.py (projector), and scorer_v010.py.

ROUND-8 RECOVERY SCOPING (finding 2):
  * The SPEND LOG is PER-RUN-INSTANCE and NAMESPACED BY H. Every event records `run_H`; the
    gates evaluate ONLY events whose `run_H` == the current run's H. A future revised
    pre-registration is a NEW H = a fresh namespace, so old-H terminal markers do NOT block it.
  * A separate durable KEY-CUSTODY LEDGER (append-only, locked; workspace root
    `key-custody.jsonl`) records ONLY the cross-run key-3 states of the §4.3 table:
    `eligible` (default) / `forfeited-unspent` / `spent`. `spent` and `forfeited-unspent`
    block scoring EVERYWHERE (across all H); the eligible-outcome terminals (setup-exhaustion,
    confirmatory-phase-fail, abort-before-gen) do NOT touch the ledger — they block only their
    own run instance, leaving the key eligible for a later, differently-H'd run.
  * Byte-identical infra resume stays within the current H and is NOT recorded as a terminal
    (the driver simply restarts and resumes via the phase receipts; §10-F2).

Scoring is a two-stage ATOMIC-CLAIM transition (within the current H):
  * `state:scoring-attempt`  — bounded pre-read attempt marker (MAX 2).
  * `spend:authorized-read-claimed` — appended by the scorer UNDER THE LOCK immediately before
    the first sealed-key byte. The key is SPENT from here (and the custody ledger records it).
  * `spend:authorized-read-complete` — appended after a clean scoring read.
"""
import json, fcntl, datetime
from pathlib import Path

MAX_SCORING_ATTEMPTS = 2

SPEND_EVENTS = {
    "scorer-fail-before-read": "pre-read scorer failure (no key byte read); one relaunch may follow if attempts<2",
    "accidental-access-during-gen": "invalid; SPENT; planned scorer never runs (allowance void)",
    "accidental-access-post-hash": "invalid; SPENT; planned scoring forfeit (never runs)",
    "authorized-read-claimed": "ATOMIC CLAIM: the scorer claimed the authorized read under the lock, "
                               "immediately before the first key byte; the key is SPENT from here",
    "authorized-read-complete": "the authorized scoring read completed cleanly; result stands; SPENT",
    "fault-after-authorized-read": "invalid; SPENT; no re-run/relaunch (allowance consumed)",
}
STATE_EVENTS = {
    "abort-before-gen": "not spent, not forfeited; eligible per §4.1 (blocks only this run instance)",
    "setup-exhaustion": "not spent, not forfeited; eligible same configuration (§4.1a; blocks only this run)",
    "confirmatory-phase-fail": "not spent, not forfeited; configuration RETIRED (§4.1; blocks only this run)",
    "terminated-during-gen-or-attest2-mismatch": "forfeited-unspent; key-4 needed (records custody forfeit)",
    "scoring-attempt": "bounded pre-read scoring attempt marker (max 2); NOT the claim",
    "generation-started": "DURABLE marker: the first key-3 generation call is about to run under this H "
                          "(round-9); a startup that finds this for a DIFFERENT H must HALT + classify",
    "attest1-mismatch-pending-classification": "TERMINAL (round-10): a POST-confirmatory attestation-1 "
                          "mismatch; this H NEVER proceeds — requires an explicit operator classification",
    "attest1-classified-benign": "audit: operator classified the attest-1 mismatch benign; a NEW freeze "
                          "instance (fresh checkout + new draws) is required; THIS H stays refused",
    "attest1-classified-configuration": "audit: operator classified the attest-1 mismatch as a configuration "
                          "mismatch; the configuration is RETIRED; THIS H stays refused",
}
STRUCTURE_EVENTS = {
    "read": "NON-SPEND: isolated projector parsed the sealed key STRUCTURE (terms+pairing), "
            "discarded all answer fields; not a spend",
}
TABLE = {**{f"spend:{k}": v for k, v in SPEND_EVENTS.items()},
         **{f"state:{k}": v for k, v in STATE_EVENTS.items()},
         **{f"structure:{k}": v for k, v in STRUCTURE_EVENTS.items()}}
ANSWER_READ_EVENTS = {"spend:authorized-read-claimed", "spend:authorized-read-complete",
                      "spend:fault-after-authorized-read"}
# Terminal events that block scoring WITHIN THEIR OWN run instance (per-H). Round-8 finding
# (recovery): the ELIGIBLE-outcome markers `state:abort-before-gen` and `state:setup-exhaustion`
# are documentation ONLY — they leave the key eligible and an allowed SAME-H resume must still
# reach scoring, so they are NOT blockers (removing the false-forfeit the reviewer flagged).
# `state:confirmatory-phase-fail` RETIRES the effective configuration => it blocks scoring under
# THIS H, but (per the custody design) never touches the cross-run ledger, so a differently-H'd
# revision stays eligible. The two genuine spends/forfeits below block within-H; the custody
# ledger blocks them cross-run/cross-H.
TERMINAL_BLOCK = {"spend:fault-after-authorized-read", "state:terminated-during-gen-or-attest2-mismatch",
                  "state:confirmatory-phase-fail", "state:attest1-mismatch-pending-classification"}

# accidental answer-read events — these MUST ALSO transition the durable custody ledger to `spent`
# (round-10 finding 1): an accidental read is a SPEND that blocks EVERY later instance, not just this H.
ACCIDENTAL_EVENTS = {"spend:accidental-access-during-gen", "spend:accidental-access-post-hash"}

# cross-run key-custody ledger (§4.3 table)
CUSTODY_STATES = ("eligible", "forfeited-unspent", "spent")
CUSTODY_BLOCK = {"forfeited-unspent", "spent"}   # block scoring EVERYWHERE (across all H)
# the canonical, out-of-tree, operator-local durable ledger path (round-10 finding 1). It lives
# OUTSIDE every checkout so a fresh-checkout revised-prereg instance still sees a key spent/forfeited
# elsewhere. It is INFRASTRUCTURE, not repo content; the driver hard-codes it in runtime mode and the
# operator seeds a genesis record once via `spend.py genesis`.
CANONICAL_CUSTODY_LEDGER = "/mnt/f/hub/10_projects/minelit/idiolect/key3-custody.jsonl"


def _lock(logpath):
    lf = Path(str(logpath) + ".lock")
    lf.parent.mkdir(parents=True, exist_ok=True)
    fh = open(lf, "w")
    fcntl.flock(fh, fcntl.LOCK_EX)
    return fh


def _unlock(fh):
    fcntl.flock(fh, fcntl.LOCK_UN)
    fh.close()


def read_events(logpath):
    p = Path(logpath)
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def _cur(events, run_H):
    """Only the current run's events (per-H namespace)."""
    return [e for e in events if e.get("run_H") == run_H]


def _has_accidental(events):
    return any("accidental-access" in e.get("event", "") for e in events)


def _has_claim(events):
    return any(e.get("event") in ("spend:authorized-read-claimed", "spend:authorized-read-complete")
               for e in events)


def _count(events, name):
    return sum(1 for e in events if e.get("event") == name)


def _assert_claim_gate(cur):
    """Pure per-H claim gate (shared by append_event and atomic_claim): a claim is admissible iff
    no terminal event, EXACTLY one structure:read, an in-range scoring-attempt, and no prior claim.
    Raises SystemExit on refusal."""
    if any(e.get("event") in TERMINAL_BLOCK for e in cur):
        raise SystemExit("SPEND-REFUSE: a terminal event is present (this run) — no claim")
    if _count(cur, "structure:read") != 1:
        raise SystemExit(f"SPEND-REFUSE: claim requires EXACTLY one structure:read (have {_count(cur, 'structure:read')})")
    na = _count(cur, "state:scoring-attempt")
    if not 1 <= na <= MAX_SCORING_ATTEMPTS:
        raise SystemExit(f"SPEND-REFUSE: claim requires an in-range scoring-attempt (have {na})")
    if _has_claim(cur):
        raise SystemExit("SPEND-REFUSE: a claim already exists (this run) — SPENT")


def _append_line(path, entry):
    """Lock-free append of one JSON line (caller MUST already hold the lock)."""
    with open(path, "a") as f:
        f.write(json.dumps(entry) + "\n")


def append_event(logpath, event, run_H, notes="", custody_ledger=None):
    """Locked append (per-H namespaced) with the enforced transition gates. Raises SystemExit
    (nonzero) on a refused transition; returns the appended entry on success. Round-10 finding 1:
    an ACCIDENTAL-access event is a SPEND — it REQUIRES `custody_ledger` and transitions the durable
    ledger to `spent` FIRST (sequential ledger-then-log order, matching atomic_claim) so it blocks
    every later instance, not just this H."""
    if event not in TABLE:
        raise SystemExit(f"unknown spend/state event {event!r}; valid: {sorted(TABLE)}")
    if not run_H:
        raise SystemExit("append_event requires run_H (per-H namespace)")
    if event in ACCIDENTAL_EVENTS:
        if not custody_ledger:
            raise SystemExit(f"{event}: accidental answer-read is a SPEND — requires custody_ledger")
        record_custody(custody_ledger, "spent", run_H, event, notes="accidental answer read (SPEND)")
    BLOCKED_BY_ACCIDENTAL = {"structure:read", "state:scoring-attempt",
                             "spend:authorized-read-claimed", "spend:authorized-read-complete"}
    fh = _lock(logpath)
    try:
        cur = _cur(read_events(logpath), run_H)   # evaluate ONLY current-H events
        if event in BLOCKED_BY_ACCIDENTAL and _has_accidental(cur):
            raise SystemExit("SPEND-REFUSE: an accidental-access event is present (this run) — invalid")
        if event == "structure:read" and _count(cur, "structure:read") >= 1:
            raise SystemExit("SPEND-REFUSE: a structure:read already exists (this run) — exactly ONE allowed")
        if event == "state:scoring-attempt":
            if _has_claim(cur):
                raise SystemExit("SPEND-REFUSE: a claim already exists (this run) — no scoring-attempt after read began")
            if _count(cur, "state:scoring-attempt") >= MAX_SCORING_ATTEMPTS:
                raise SystemExit(f"SPEND-REFUSE: scoring-attempt cap ({MAX_SCORING_ATTEMPTS}) reached (this run)")
        if event == "spend:authorized-read-claimed":
            _assert_claim_gate(cur)
        if event == "spend:authorized-read-complete":
            if _count(cur, "spend:authorized-read-claimed") < 1:
                raise SystemExit("SPEND-REFUSE: cannot complete without a prior claim (this run)")
            if _count(cur, "spend:authorized-read-complete") >= 1:
                raise SystemExit("SPEND-REFUSE: authorized-read already completed (this run)")
        if event == "spend:fault-after-authorized-read" and _count(cur, "spend:authorized-read-claimed") < 1:
            raise SystemExit("SPEND-REFUSE: fault-after-authorized-read requires a prior claim (this run)")
        entry = {"event": event, "run_H": run_H, "meaning": TABLE[event], "notes": notes,
                 "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        _append_line(logpath, entry)
        return entry
    finally:
        _unlock(fh)


def projector_completed(logpath, run_H):
    """Resume helper (§10-F2): the projector phase is done (this run) iff its structure:read
    is present in the current H's namespace."""
    return _count(_cur(read_events(logpath), run_H), "structure:read") >= 1


def claim_authorized_read(logpath, run_H, notes=""):
    return append_event(logpath, "spend:authorized-read-claimed", run_H, notes)


def complete_authorized_read(logpath, run_H, notes=""):
    return append_event(logpath, "spend:authorized-read-complete", run_H, notes)


def assert_scoring_allowed(logpath, run_H, custody_ledger=None):
    """Pre-claim gate (per-H). Refuses on: any UNTYPED entry; accidental-access; any ANSWER-READ
    or TERMINAL entry — ALL within the current H's namespace; NOT exactly one structure:read;
    no in-range scoring-attempt. If `custody_ledger` is given, ALSO refuses if the key is
    cross-run spent/forfeited by a DIFFERENT H (a same-H spent state is a recovery case, left to
    the atomic claim's idempotent handling). Raises SystemExit on refusal."""
    if custody_ledger is not None:
        assert_key_available(custody_ledger, run_H)
    fh = _lock(logpath)
    try:
        cur = _cur(read_events(logpath), run_H)
        for e in cur:
            if e.get("event") not in TABLE:
                raise SystemExit(f"SCORER-REFUSE: UNTYPED spend-log entry {e.get('event')!r}")
        if _has_accidental(cur):
            raise SystemExit("SCORER-REFUSE: accidental-access event present (this run) — never opening the key")
        for e in cur:
            if e["event"] in ANSWER_READ_EVENTS:
                raise SystemExit(f"SCORER-REFUSE: answer-read entry {e['event']!r} already present (this run)")
            if e["event"] in TERMINAL_BLOCK:
                raise SystemExit(f"SCORER-REFUSE: terminal event {e['event']!r} present (this run) — refusing")
        if _count(cur, "structure:read") != 1:
            raise SystemExit(f"SCORER-REFUSE: require EXACTLY one structure:read (have {_count(cur, 'structure:read')})")
        na = _count(cur, "state:scoring-attempt")
        if not 1 <= na <= MAX_SCORING_ATTEMPTS:
            raise SystemExit(f"SCORER-REFUSE: require a uniquely-open in-range scoring-attempt (have {na})")
    finally:
        _unlock(fh)


# ------------------------- cross-run key-custody ledger -------------------------
def custody_state(ledger):
    """The current key-3 custody state — the LAST recorded transition, default 'eligible'."""
    evs = read_events(ledger)
    return evs[-1]["state"] if evs else "eligible"


def _custody_last(ledger):
    """(state, run_H) of the last custody transition, default ('eligible', None)."""
    evs = read_events(ledger)
    if not evs:
        return "eligible", None
    return evs[-1]["state"], evs[-1].get("run_H")


def _custody_refuse_or_noop(cur_state, cur_H, state, run_H):
    """Shared monotonicity + idempotency check (used by record_custody AND atomic_claim). Returns
    'append' | 'noop'; raises SystemExit on a refused transition. Round-9: a blocking state may be
    RE-appended as a no-op ONLY by the SAME run_H that set it (idempotent recovery); any different
    state, or the same blocking state from a DIFFERENT H, is refused."""
    if cur_state in CUSTODY_BLOCK:
        if state == cur_state and cur_H == run_H:
            return "noop"
        raise SystemExit(f"CUSTODY-REFUSE: key already {cur_state!r} (run_H {cur_H!r}) — cannot transition to "
                         f"{state!r} (run_H {run_H!r})")
    return "append"


def record_custody(ledger, state, run_H, event_ref, notes=""):
    """Append a cross-run custody transition (locked). `state` ∈ CUSTODY_STATES. Monotone +
    idempotent: once spent/forfeited, a conflicting transition is refused and a DUPLICATE
    spent/forfeited append by the SAME run_H is a no-op success (round-9 idempotent recovery).
    Round-10: requires an initialized (genesis) ledger — never creates custody state ex nihilo."""
    if state not in CUSTODY_STATES:
        raise SystemExit(f"unknown custody state {state!r}; valid: {CUSTODY_STATES}")
    assert_ledger_initialized(ledger)
    fh = _lock(ledger)
    try:
        cur_state, cur_H = _custody_last(ledger)
        if _custody_refuse_or_noop(cur_state, cur_H, state, run_H) == "noop":
            return None
        entry = {"state": state, "run_H": run_H, "event_ref": event_ref, "notes": notes,
                 "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        _append_line(ledger, entry)
        return entry
    finally:
        _unlock(fh)


def assert_key_available(ledger, run_H=None):
    """Cross-run gate: refuse if the durable custody ledger is MISSING/un-seeded (fail-closed —
    round-10: a missing ledger must NEVER read as 'eligible'), or shows the key spent/forfeited.
    Round-9: when `run_H` is given, a spent/forfeited state set by that SAME H is a recovery case and
    is ALLOWED (the atomic claim handles it idempotently); a different H (or run_H omitted) is refused."""
    assert_ledger_initialized(ledger)
    st, holder = _custody_last(ledger)
    if st in CUSTODY_BLOCK and not (run_H is not None and holder == run_H):
        raise SystemExit(f"KEY-CUSTODY: key-3 is {st!r} (run_H {holder!r}, cross-run) — refusing any scoring/read")


def atomic_claim(spend_log, custody_ledger, run_H, notes=""):
    """Round-9 finding 2: ONE fail-closed claim. Under BOTH locks (fixed order: custody ledger
    THEN spend log) re-check availability + the per-H claim gate, then append custody `spent` and
    the per-H `authorized-read-claimed` before releasing. Idempotent recovery: a same-H `spent`
    ledger state with NO prior claim (crash after the ledger write, before the claim) proceeds and
    appends only the missing claim; a prior claim (key already read) is refused (no second read); a
    DIFFERENT-H spent/forfeited state is refused. Never suppresses a persistence failure."""
    if not run_H:
        raise SystemExit("atomic_claim requires run_H")
    assert_ledger_initialized(custody_ledger)   # round-10: fail-closed on a missing/un-seeded ledger
    lfh = _lock(custody_ledger)                 # 1) custody ledger lock FIRST
    try:
        sfh = _lock(spend_log)                  # 2) then the spend-log lock
        try:
            cur_state, cur_H = _custody_last(custody_ledger)
            decision = _custody_refuse_or_noop(cur_state, cur_H, "spent", run_H)  # refuses cross-H
            cur = _cur(read_events(spend_log), run_H)
            _assert_claim_gate(cur)             # refuses if a claim already exists (key already read)
            if decision == "append":
                _append_line(custody_ledger, {"state": "spent", "run_H": run_H,
                    "event_ref": "spend:authorized-read-claimed", "notes": notes or "authorized scoring read",
                    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()})
            entry = {"event": "spend:authorized-read-claimed", "run_H": run_H,
                     "meaning": TABLE["spend:authorized-read-claimed"], "notes": notes,
                     "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
            _append_line(spend_log, entry)      # per-H claim, still under BOTH locks
            return entry
        finally:
            _unlock(sfh)
    finally:
        _unlock(lfh)


# ------------------------- genesis + ledger availability (round-10 finding 1) -------------------------
def has_genesis(ledger):
    """True iff the ledger has an explicit eligible GENESIS record as its first entry."""
    evs = read_events(ledger)
    return bool(evs) and evs[0].get("kind") == "genesis" and evs[0].get("state") == "eligible"


def genesis(ledger, note="operator-seeded key-3 custody genesis"):
    """Operator one-shot: write the explicit eligible GENESIS record. Refuses if the ledger already
    exists (never clobbers custody history)."""
    p = Path(ledger)
    if p.exists() and read_events(ledger):
        raise SystemExit(f"GENESIS-REFUSE: {ledger} already exists with records — refusing to re-seed")
    p.parent.mkdir(parents=True, exist_ok=True)
    entry = {"kind": "genesis", "key": "key-3", "state": "eligible", "note": note,
             "created": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    _append_line(ledger, entry)
    return entry


def assert_ledger_initialized(ledger):
    """Round-10 finding 1: every run REFUSES (before phase 0) unless the durable ledger EXISTS, is
    readable, and carries the explicit eligible genesis. A missing/unreadable/un-seeded ledger halts."""
    p = Path(ledger)
    if not p.is_file():
        raise SystemExit(f"KEY-CUSTODY: ledger {ledger} MISSING — run `spend.py genesis --out {ledger}` first (refusing)")
    try:
        read_events(ledger)
    except Exception as e:
        raise SystemExit(f"KEY-CUSTODY: ledger {ledger} UNREADABLE ({e}) — refusing")
    if not has_genesis(ledger):
        raise SystemExit(f"KEY-CUSTODY: ledger {ledger} lacks the eligible genesis record — refusing")


# ------------------------- attestation-1 mismatch classification (round-10 finding 2) -------------------------
def _has_attest1_pending(logpath, run_H):
    return _count(_cur(read_events(logpath), run_H), "state:attest1-mismatch-pending-classification") >= 1


def assert_no_attest1_mismatch(logpath, run_H):
    """Startup guard: an H under a persisted attestation-1 mismatch NEVER proceeds (round-10 finding 2)."""
    if _has_attest1_pending(logpath, run_H):
        raise SystemExit("ATTEST1-REFUSE: this H has a persisted attestation-1 mismatch "
                         "(pending/classified) — it NEVER proceeds; start a fresh freeze instance")


def classify_attest1(logpath, run_H, resolution, notes=""):
    """Operator records the classification of a persisted attest-1 mismatch. `resolution` ∈
    {benign, configuration}. Requires the pending terminal to exist for this H. Either way THIS H
    stays refused (benign => a NEW freeze instance is required; configuration => retirement)."""
    if resolution not in ("benign", "configuration"):
        raise SystemExit("classify-attest1 resolution must be 'benign' or 'configuration'")
    if not _has_attest1_pending(logpath, run_H):
        raise SystemExit("classify-attest1: no pending attestation-1 mismatch for this H")
    return append_event(logpath, f"state:attest1-classified-{resolution}", run_H, notes=notes)


def _cli():
    import argparse
    ap = argparse.ArgumentParser(description="key-3 custody / spend-state operator tools")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("genesis", help="operator one-shot: seed the eligible custody genesis")
    g.add_argument("--out", default=CANONICAL_CUSTODY_LEDGER); g.add_argument("--note", default="operator-seeded key-3 custody genesis")
    c = sub.add_parser("classify-attest1", help="record an attestation-1 mismatch classification")
    c.add_argument("--resolution", required=True, choices=("benign", "configuration"))
    c.add_argument("--H", required=True); c.add_argument("--out", required=True); c.add_argument("--notes", default="")
    a = ap.parse_args()
    if a.cmd == "genesis":
        e = genesis(a.out, a.note); print(f"custody GENESIS seeded (eligible) -> {a.out}\n  {e['created']}")
    elif a.cmd == "classify-attest1":
        classify_attest1(a.out, a.H, a.resolution)
        print(f"attest-1 mismatch classified {a.resolution!r} for H {a.H[:12]} — THIS H stays refused "
              f"({'new freeze instance required' if a.resolution == 'benign' else 'configuration retired'})")


if __name__ == "__main__":
    _cli()
