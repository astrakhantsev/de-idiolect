#!/usr/bin/env python3
"""spend.py — the enforced one-shot spend/state gate (v0.10 prereg §4.3/§4.4). Shared by
attest.py, make_pairs_manifest.py (projector), and scorer_v010.py, over ONE authoritative
locked log (fcntl.flock on a sibling lockfile).

Scoring is a two-stage ATOMIC-CLAIM transition (round-5 critical fix):
  * `state:scoring-attempt`  — a bounded pre-read attempt marker (MAX 2), appended by the
    driver BEFORE each scorer launch. It is NOT the claim.
  * `spend:authorized-read-claimed` — appended by the SCORER, under the lock, IMMEDIATELY
    before it reads the first sealed-key byte. This is the atomic spend claim. Once present,
    the key is SPENT: any later invocation is refused (even after a crash with no completion).
  * `spend:authorized-read-complete` — appended by the scorer after a clean scoring read.

Relaunch rule (the ONE permitted pre-read relaunch, executable):
  * a failure BEFORE any claim with `scoring-attempt` count < 2 -> the driver appends another
    `scoring-attempt` and relaunches;
  * `scoring-attempt` count == 2 (the second attempt), or ANY claim present -> refused.

Other gates: exactly ONE `structure:read` (the projector's sanctioned non-spend read) is
required before scoring (zero AND >1 both refuse); any accidental-access event invalidates
the run and refuses all further transitions; an UNTYPED log entry refuses scoring.
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
    "abort-before-gen": "not spent, not forfeited; eligible per §4.1",
    "setup-exhaustion": "not spent, not forfeited; eligible same configuration (§4.1a)",
    "confirmatory-phase-fail": "not spent, not forfeited; configuration RETIRED (§4.1)",
    "terminated-during-gen-or-attest2-mismatch": "forfeited-unspent; key-4 needed",
    "scoring-attempt": "bounded pre-read scoring attempt marker (max 2); NOT the claim",
}
STRUCTURE_EVENTS = {
    "read": "NON-SPEND: isolated projector parsed the sealed key STRUCTURE (terms+pairing), "
            "discarded all answer fields; not a spend",
}
TABLE = {**{f"spend:{k}": v for k, v in SPEND_EVENTS.items()},
         **{f"state:{k}": v for k, v in STATE_EVENTS.items()},
         **{f"structure:{k}": v for k, v in STRUCTURE_EVENTS.items()}}
# entries meaning the sealed answer was (or began to be) read — refuse scoring if any present
ANSWER_READ_EVENTS = {"spend:authorized-read-claimed", "spend:authorized-read-complete",
                      "spend:fault-after-authorized-read"}


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


def _has_accidental(events):
    return any("accidental-access" in e.get("event", "") for e in events)


def _has_claim(events):
    return any(e.get("event") in ("spend:authorized-read-claimed", "spend:authorized-read-complete")
               for e in events)


def _count(events, name):
    return sum(1 for e in events if e.get("event") == name)


def append_event(logpath, event, notes=""):
    """Locked append with the enforced transition gates. Raises SystemExit (nonzero) on a
    refused transition; returns the appended entry on success."""
    if event not in TABLE:
        raise SystemExit(f"unknown spend/state event {event!r}; valid: {sorted(TABLE)}")
    # events whose ACTIVE transition is blocked once the run is invalid (accidental access).
    # Terminal/documentation markers (state:setup-exhaustion, confirmatory-phase-fail,
    # terminated-*, abort-before-gen; spend:accidental-* / fault-after-authorized-read) always
    # append — they RECORD an outcome and the driver must be able to write them at any failure site.
    BLOCKED_BY_ACCIDENTAL = {"structure:read", "state:scoring-attempt",
                             "spend:authorized-read-claimed", "spend:authorized-read-complete"}
    fh = _lock(logpath)
    try:
        events = read_events(logpath)
        if event in BLOCKED_BY_ACCIDENTAL and _has_accidental(events):
            raise SystemExit("SPEND-REFUSE: an accidental-access event is present — the run is "
                             "invalid; no further active transitions permitted")
        if event == "structure:read" and _count(events, "structure:read") >= 1:
            raise SystemExit("SPEND-REFUSE: a structure:read already exists — exactly ONE sanctioned "
                             "projector structure-read is whitelisted")
        if event == "state:scoring-attempt":
            if _has_claim(events):
                raise SystemExit("SPEND-REFUSE: a claim already exists — no scoring-attempt after the "
                                 "answer read has begun")
            if _count(events, "state:scoring-attempt") >= MAX_SCORING_ATTEMPTS:
                raise SystemExit(f"SPEND-REFUSE: scoring-attempt cap ({MAX_SCORING_ATTEMPTS}) reached "
                                 f"— the one permitted pre-read relaunch is exhausted")
        if event == "spend:authorized-read-claimed":
            # the ATOMIC CLAIM: require exactly one structure:read, at least one scoring-attempt,
            # and no prior claim — all checked under this same lock, then appended.
            if _count(events, "structure:read") != 1:
                raise SystemExit(f"SPEND-REFUSE: claim requires EXACTLY one structure:read "
                                 f"(have {_count(events, 'structure:read')})")
            if _count(events, "state:scoring-attempt") < 1:
                raise SystemExit("SPEND-REFUSE: claim requires a preceding scoring-attempt marker")
            if _has_claim(events):
                raise SystemExit("SPEND-REFUSE: a claim already exists — the key is already SPENT")
        if event == "spend:authorized-read-complete":
            if _count(events, "spend:authorized-read-claimed") < 1:
                raise SystemExit("SPEND-REFUSE: cannot complete without a prior claim")
            if _count(events, "spend:authorized-read-complete") >= 1:
                raise SystemExit("SPEND-REFUSE: authorized-read already completed")
        if event == "spend:fault-after-authorized-read" and _count(events, "spend:authorized-read-claimed") < 1:
            # a post-read fault presupposes the read began (a claim). Without a claim this is a
            # PRE-read failure and must be recorded as terminated-*/forfeited-unspent instead.
            raise SystemExit("SPEND-REFUSE: fault-after-authorized-read requires a prior claim "
                             "(no claim -> the failure is pre-read, not post-read)")
        entry = {"event": event, "meaning": TABLE[event], "notes": notes,
                 "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        with open(logpath, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry
    finally:
        _unlock(fh)


def projector_completed(logpath):
    """Resume helper (§10-F2): the projector phase is done iff its sanctioned structure:read
    is present. The driver uses this (with the pairs.json output present) to SKIP re-running the
    projector on a restart-after-infra-fault — re-running would hit the one-shot structure:read
    refusal."""
    return _count(read_events(logpath), "structure:read") >= 1


def claim_authorized_read(logpath, notes=""):
    """The scorer calls this UNDER THE LOCK immediately before reading the first key byte."""
    return append_event(logpath, "spend:authorized-read-claimed", notes)


def complete_authorized_read(logpath, notes=""):
    """The scorer calls this after a clean scoring read."""
    return append_event(logpath, "spend:authorized-read-complete", notes)


def assert_scoring_allowed(logpath):
    """Pre-claim gate the scorer calls (under lock) BEFORE any H/key work. Refuses on:
      * any UNTYPED entry; * any accidental-access; * any ANSWER-READ entry already present
        (claim/complete/fault — the answer was/began being read); * NOT exactly one
        structure:read (zero AND >1 both refuse); * no scoring-attempt marker.
    Passes with exactly one structure:read + at least one scoring-attempt (and no claim).
    Raises SystemExit (nonzero) on refusal. (The atomic claim re-checks under the lock.)"""
    fh = _lock(logpath)
    try:
        events = read_events(logpath)
        for e in events:
            if e.get("event") not in TABLE:
                raise SystemExit(f"SCORER-REFUSE: UNTYPED spend-log entry {e.get('event')!r}")
        if _has_accidental(events):
            raise SystemExit("SCORER-REFUSE: accidental-access event present — never opening the key")
        for e in events:
            if e["event"] in ANSWER_READ_EVENTS:
                raise SystemExit(f"SCORER-REFUSE: answer-read entry {e['event']!r} already present "
                                 f"— the sealed answer was already read; refusing")
        if _count(events, "structure:read") != 1:
            raise SystemExit(f"SCORER-REFUSE: require EXACTLY one structure:read "
                             f"(have {_count(events, 'structure:read')})")
        if _count(events, "state:scoring-attempt") < 1:
            raise SystemExit("SCORER-REFUSE: no scoring-attempt marker (driver must record the attempt)")
    finally:
        _unlock(fh)
