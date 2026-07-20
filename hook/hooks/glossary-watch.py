#!/usr/bin/env python3
"""glossary-watch.py — the coin-time hook, trigger T2 (deterministic).

A Claude Code Stop hook: after each assistant turn, scan the project's glossary
file(s) for term entries not yet in the seen-lexicon cache, and fire
term-check.sh on each new one (in the background — a Stop hook must return
fast). This is the piece the entry's §4.2 argues for: a standing instruction
("check your coinages") must win an attention contest every turn; a hook fires
deterministically at the moment a term enters the glossary.

Dumb by design (v1): the trigger is "a new entry appeared in a glossary file",
not any heuristic about what the assistant wrote. High precision, no cleverness.

Config (env):
  TERM_CHECK_GLOSSARIES  space-separated glossary paths to watch
                         (default: "GLOSSARY.md glossary.md docs/glossary.md")
  TERM_CHECK_SOURCES     extra files to draw usage excerpts from, besides the
                         glossary itself (default: none)
  TERM_CHECK_BIN         path to term-check.sh (default: ../term-check.sh
                         relative to this script)
  TERM_CHECK_STATE       state dir (default: .term-check in the project cwd)

Behavior notes:
  - First run in a project SEEDS the cache with every existing term and fires
    on nothing ("baseline established") — otherwise installation would flood.
  - At most 3 new terms fire per turn; the rest are cached silently (logged).
  - Kill switch: create <state>/off to disable without uninstalling.

Term extraction convention (documented, deliberately narrow): a glossary entry
is a line starting with a bold term (`- **term** — ...`) or a `## term` /
`### term` heading. Anything else is not an entry.
"""
import fcntl
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ENTRY_RE = re.compile(r"^(?:[-*]\s+\*\*(?P<bold>.+?)\*\*.*|#{2,3}\s+(?P<head>\S.*?))\s*$")
MAX_FIRES_PER_TURN = 3


def extract_terms(path: Path) -> list[str]:
    terms = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = ENTRY_RE.match(line)
        if not m:
            continue
        term = (m.group("bold") or m.group("head")).strip()
        # a bold entry may carry inflection notes: "de-idiolect** (verb; ..." — keep the head word(s) only
        term = re.split(r"\s*\(", term)[0].strip().rstrip(":—-").strip()
        if 0 < len(term) <= 60:
            terms.append(term)
    return terms


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    cwd = Path(payload.get("cwd") or os.getcwd())

    state = Path(os.environ.get("TERM_CHECK_STATE") or cwd / ".term-check")
    if (state / "off").exists():
        return 0
    state.mkdir(parents=True, exist_ok=True)
    seen_file = state / "seen-terms.txt"

    glossaries = [
        cwd / g
        for g in os.environ.get(
            "TERM_CHECK_GLOSSARIES", "GLOSSARY.md glossary.md docs/glossary.md"
        ).split()
        if (cwd / g).is_file()
    ]
    if not glossaries:
        return 0

    current: dict[str, Path] = {}
    for g in glossaries:
        for t in extract_terms(g):
            current.setdefault(t.lower(), g)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log = state / "log.jsonl"

    # Single-flight per project: overlapping Stop hooks (parallel sessions in
    # one project) would both read the cache before either appends, duplicating
    # spend and colliding state paths (adversarial-review finding). Non-blocking:
    # the loser skips this turn entirely; the glossary is rescanned next turn.
    lock_fh = (state / "watch.lock").open("w")
    try:
        fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        return 0

    if not seen_file.exists():
        seen_file.write_text("".join(f"{t}\n" for t in sorted(current)), encoding="utf-8")
        with log.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": ts, "event": "watch-baseline", "terms_seeded": len(current)}) + "\n")
        return 0

    seen = {l.strip().lower() for l in seen_file.read_text(encoding="utf-8").splitlines() if l.strip()}
    new = [(t, g) for t, g in current.items() if t not in seen]
    if not new:
        # Quiet evaluations are logged too: burden measurement needs the
        # denominator (evaluations), not just the numerator (firings).
        with log.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": ts, "event": "watch", "fired": [], "suppressed": []}) + "\n")
        return 0

    script = Path(os.environ.get("TERM_CHECK_BIN") or Path(__file__).resolve().parent.parent / "term-check.sh")
    extra_sources = [s for s in os.environ.get("TERM_CHECK_SOURCES", "").split() if (cwd / s).is_file()]

    fired, suppressed = [], []
    for term, gloss in new:
        if len(fired) >= MAX_FIRES_PER_TURN or not script.is_file():
            suppressed.append(term)
            with seen_file.open("a", encoding="utf-8") as fh:
                fh.write(term + "\n")  # cached silently; log row below says so
            continue
        sources = [str(gloss)] + extra_sources
        with (state / "watch.log").open("a", encoding="utf-8") as wl:
            subprocess.Popen(
                ["bash", str(script), "--trigger", "glossary-watch", term, *sources],
                cwd=str(cwd), stdout=wl, stderr=wl, start_new_session=True,
            )
        fired.append(term)
        # term-check.sh adds the term to the cache itself on success; add here
        # too so a failed draw doesn't refire every turn (idempotent).
        with seen_file.open("a", encoding="utf-8") as fh:
            fh.write(term + "\n")

    with log.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": ts, "event": "watch", "fired": fired, "suppressed": suppressed}) + "\n")

    if fired:
        print(json.dumps({
            "systemMessage": (
                f"term-check (glossary-watch): new glossary term(s) {fired} — isolated naming "
                f"check(s) running in the background; flags will land in term-flags.md."
                + (f" Suppressed over per-turn cap: {suppressed}." if suppressed else "")
            )
        }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
