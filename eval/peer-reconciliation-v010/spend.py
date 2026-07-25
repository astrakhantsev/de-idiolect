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
                  "state:confirmatory-phase-fail"}

# cross-run key-custody ledger (§4.3 table)
CUSTODY_STATES = ("eligible", "forfeited-unspent", "spent")
CUSTODY_BLOCK = {"forfeited-unspent", "spent"}   # block scoring EVERYWHERE (across all H)


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


def append_event(logpath, event, run_H, notes=""):
    """Locked append (per-H namespaced) with the enforced transition gates. Raises SystemExit
    (nonzero) on a refused transition; returns the appended entry on success."""
    if event not in TABLE:
        raise SystemExit(f"unknown spend/state event {event!r}; valid: {sorted(TABLE)}")
    if not run_H:
        raise SystemExit("append_event requires run_H (per-H namespace)")
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
            if any(e.get("event") in TERMINAL_BLOCK for e in cur):
                raise SystemExit("SPEND-REFUSE: a terminal event is present (this run) — no claim")
            if _count(cur, "structure:read") != 1:
                raise SystemExit(f"SPEND-REFUSE: claim requires EXACTLY one structure:read (have {_count(cur, 'structure:read')})")
            na = _count(cur, "state:scoring-attempt")
            if not 1 <= na <= MAX_SCORING_ATTEMPTS:
                raise SystemExit(f"SPEND-REFUSE: claim requires an in-range scoring-attempt (have {na})")
            if _has_claim(cur):
                raise SystemExit("SPEND-REFUSE: a claim already exists (this run) — SPENT")
        if event == "spend:authorized-read-complete":
            if _count(cur, "spend:authorized-read-claimed") < 1:
                raise SystemExit("SPEND-REFUSE: cannot complete without a prior claim (this run)")
            if _count(cur, "spend:authorized-read-complete") >= 1:
                raise SystemExit("SPEND-REFUSE: authorized-read already completed (this run)")
        if event == "spend:fault-after-authorized-read" and _count(cur, "spend:authorized-read-claimed") < 1:
            raise SystemExit("SPEND-REFUSE: fault-after-authorized-read requires a prior claim (this run)")
        entry = {"event": event, "run_H": run_H, "meaning": TABLE[event], "notes": notes,
                 "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        with open(logpath, "a") as f:
            f.write(json.dumps(entry) + "\n")
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
    cross-run spent/forfeited (block everywhere). Raises SystemExit on refusal."""
    if custody_ledger is not None:
        assert_key_available(custody_ledger)
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


def record_custody(ledger, state, run_H, event_ref, notes=""):
    """Append a cross-run custody transition (locked). `state` ∈ CUSTODY_STATES. Monotone:
    once spent/forfeited, further conflicting transitions are refused."""
    if state not in CUSTODY_STATES:
        raise SystemExit(f"unknown custody state {state!r}; valid: {CUSTODY_STATES}")
    fh = _lock(ledger)
    try:
        cur = custody_state(ledger) if Path(ledger).exists() else "eligible"
        if cur in CUSTODY_BLOCK and state != cur:
            raise SystemExit(f"CUSTODY-REFUSE: key already {cur!r} — cannot transition to {state!r}")
        entry = {"state": state, "run_H": run_H, "event_ref": event_ref, "notes": notes,
                 "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        with open(ledger, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry
    finally:
        _unlock(fh)


def assert_key_available(ledger):
    """Cross-run gate: refuse if the durable custody ledger shows the key spent or forfeited."""
    st = custody_state(ledger)
    if st in CUSTODY_BLOCK:
        raise SystemExit(f"KEY-CUSTODY: key-3 is {st!r} (cross-run) — refusing any scoring/read")
