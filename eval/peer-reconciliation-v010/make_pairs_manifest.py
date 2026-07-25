#!/usr/bin/env python3
"""make_pairs_manifest.py — the frozen, ISOLATED-SUBPROCESS projector that builds the
ANSWER-BLIND pairs.json the v0.10 generation stack + baselines read (v0.10 prereg §3.6,
custody). Run as its OWN OS process; the orchestrator/driver NEVER parses the key in-process.

pairs.json carries per record ONLY {pair_id, term_a, term_b} and a top-level {count}. Two
answer-leak channels are closed:
  1. pair_id is an OPAQUE token = sha256(term_a||NUL||term_b)[:16] (hex) — derived from the
     (known) term pair, NOT from class/position; it encodes no class.
  2. the emit order is a seeded-but-KEY-INDEPENDENT shuffle — sorted by the opaque id (a
     uniform hash), so the sequence carries no P01–P10 class ordering.
  (term_a == term_b for jingle pairs is inherent — jingle strings are known/orchestrator-
  visible and in the exposure ledger; not hidden.)

CUSTODY (the two sanctioned-reader integrity + audit checks, mirroring the scorer):
  * HASH GATE (--recorded-hashes, optional --H): BEFORE parsing anything, verify sha256 of the
    sealed key file it will read equals the RECORDED value (freeze-manifest.txt; also bound in
    H when --H is supplied). Mismatch => ABORT with nothing read (report state:abort-before-gen
    per the state table — nothing spent, nothing forfeited). Ordering note: for key-3 this
    projector runs at phase 0.5 BEFORE build-H (H binds the blind pairs.json this produces), so
    the integrity check is against the committed freeze-manifest.txt — the same recorded values
    H binds via recorded_manifest_sha256 + inherited_recorded.sealed; --H (when present, i.e.
    an already-built H) adds the H-self-consistency + recorded-hashes-bound-in-H check via
    attest.load_and_verify_H, exactly as the scorer does at the other sanctioned reader.
  * TYPED STRUCTURE-READ (--spend-log): register a single `structure:read` (NON-SPEND) entry in
    the ONE authoritative locked spend log that attest + the scorer read (a second is refused).

stdout: exactly one line `pairs_sha256: <sha256 of the written pairs.json bytes>`.
For confirmatory TRAIN keys (fresh, no recorded hashes / no key-3 spend log) call WITHOUT
--recorded-hashes/--H/--spend-log; the source key is fully readable and the checks are skipped.
"""
import argparse, json, sys, hashlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spend
import attest


def _opaque_id(term_a, term_b):
    return hashlib.sha256(f"{term_a}\x00{term_b}".encode()).hexdigest()[:16]


def build_payload(term_pairs):
    """PURE projection (shared with the conformance runner). term_pairs = [(term_a, term_b), ...]
    (any order) -> {count, pairs:[{pair_id, term_a, term_b}]} with opaque ids, sorted by opaque
    id (the key-independent shuffle). Refuses an opaque-id collision."""
    rows = [{"pair_id": _opaque_id(a, b), "term_a": a, "term_b": b} for a, b in term_pairs]
    rows.sort(key=lambda r: r["pair_id"])
    ids = set()
    for r in rows:
        if r["pair_id"] in ids:
            raise ValueError(f"opaque-id collision on {r['pair_id']} — term pair hash clash")
        ids.add(r["pair_id"])
    return {"count": len(rows), "pairs": rows}


def _recorded_hash_for(recorded_file, basename):
    for line in Path(recorded_file).read_text().splitlines():
        line = line.strip()
        if "  " not in line:
            continue
        h, rel = line.split(None, 1)
        if len(h) == 64 and all(c in "0123456789abcdef" for c in h.lower()) and Path(rel.strip()).name == basename:
            return h.lower()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key_dir")
    ap.add_argument("out")
    ap.add_argument("--recorded-hashes", help="freeze-manifest.txt — hash-gate the sealed file before reading")
    ap.add_argument("--H", help="runs/H.json — additionally bind --recorded-hashes to the attested H")
    ap.add_argument("--spend-log", help="the ONE authoritative locked spend log — register structure:read")
    args = ap.parse_args()
    key_dir, out = Path(args.key_dir), Path(args.out)

    conc, ak = key_dir / "concepts.json", key_dir / "answer_key.json"
    if conc.exists():
        src, get_a, get_b = conc, (lambda p: p["a"]["term"]), (lambda p: p["b"]["term"])
    elif ak.exists():
        src, get_a, get_b = ak, (lambda p: p["term_a"]), (lambda p: p["term_b"])
    else:
        sys.exit(f"no concepts.json or answer_key.json under {key_dir}")

    # ---- HASH GATE (before ANY parse) ----
    if args.recorded_hashes:
        want = _recorded_hash_for(args.recorded_hashes, src.name)
        if want is None:
            sys.exit(f"ABORT (nothing read): no recorded hash for {src.name} in {args.recorded_hashes} "
                     f"— state:abort-before-gen (nothing spent, nothing forfeited)")
        got = hashlib.sha256(src.read_bytes()).hexdigest()
        if got != want:
            sys.exit(f"ABORT (nothing read): sealed {src.name} sha {got[:12]} != recorded {want[:12]} "
                     f"— state:abort-before-gen (nothing spent, nothing forfeited)")
        if args.H:
            hobj = attest.load_and_verify_H(args.H)
            bound = hobj["manifest_of_manifests"].get("recorded_manifest_sha256")
            if bound != hashlib.sha256(Path(args.recorded_hashes).read_bytes()).hexdigest():
                sys.exit("ABORT (nothing read): --recorded-hashes not bound in H — state:abort-before-gen")

    # ---- register the sanctioned NON-SPEND structure read (one-shot) ----
    if args.spend_log:
        spend.append_event(args.spend_log, "structure:read",
                           notes=f"projector parsed {src.name} structure -> {out.name}")

    # ---- parse structure, project, emit blind pairs.json ----
    k = json.load(open(src))
    payload = build_payload([(get_a(p), get_b(p)) for p in k["pairs"]])
    for r in payload["pairs"]:
        if set(r) != {"pair_id", "term_a", "term_b"}:
            sys.exit(f"projection produced non-whitelisted field(s) — refusing: {sorted(r)}")
    data = json.dumps(payload, indent=1)
    out.write_text(data)
    print(f"pairs_sha256: {hashlib.sha256(data.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
