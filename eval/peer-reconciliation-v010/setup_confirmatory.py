#!/usr/bin/env python3
"""setup_confirmatory.py — setup-constructor wrapper (v0.10 prereg §4.1a). Drives the
UNCHANGED frozen v0.9 key-author/corpus path TWICE, to build the 2 fresh confirmatory TRAIN
keys/corpora, with the §4.1a attempt accounting:
  * a DRAW BEGINS when its key-author call is issued;
  * per-call malformed-retry cap = 1 (a malformed setup output only);
  * EVERY setup output is hashed into the phase record — none discarded, no
    unfavorable-corpus replacement (a structurally valid corpus is used regardless of how
    the gate later falls);
  * SETUP EXHAUSTION (a setup call malformed twice) FAILS THE PHASE but does NOT retire the
    configuration (setup failure is not a configuration outcome; §4.1a) — re-attempt with
    fresh setup under the same still-eligible configuration.

It NEVER touches key-3. The frozen v0.9 scripts it calls (unchanged): keyspec-author.md
(via the isolation wrapper, opus), validate_key.py, build_briefs.py, the corpus-gen prompts
(sonnet A / codex-terra B via the isolation wrapper), harness/split_corpus.py [IN the
workspace, hash-verified vs the frozen record, bound in H — the default], gen_leakcheck.py,
leakcheck_peer.sh. make_pairs_manifest.py (v0.10) projects the answer-blind pairs.json for each
confirmatory key. gen-community-{a,b}.md are GENERATED per conf key by build_briefs.py (not
static files). This wrapper never touches key-3.

This is a DRIVER: the LLM calls go through ../e2e-cell/run_isolated.sh. Run it at run time,
after freeze + build-H + probe. `--dry-run` prints the plan + call sequence without invoking
anything (used by the offline test). NO LLM calls happen during the build.

Per §6 setup call sites + pinned IDs:
  key-author       claude / claude-opus-4-8
  corpus-gen A     claude / claude-sonnet-5
  corpus-gen B     codex  / gpt-5.6-terra
"""
import argparse, hashlib, json, subprocess, sys, datetime, tempfile, shutil
from pathlib import Path

EXACT_DOCS = [f"{i:02d}.md" for i in range(1, 12)]  # the ONLY corpus filenames allowed (01..11)

BASE = Path(__file__).resolve().parent
RUNISO = BASE / "../e2e-cell/run_isolated.sh"
RETRY_CAP = 1  # §4.1a per-call malformed-retry cap

SITES = [  # (name, cli, model, prompt-source)
    ("key-author", "claude", "claude-opus-4-8", "harness/keyspec-author.md"),
    ("corpus-gen-a", "claude", "claude-sonnet-5", "prompts/gen-community-a.md"),
    ("corpus-gen-b", "codex", "gpt-5.6-terra", "prompts/gen-community-b.md"),
]


def _sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _isolated(cli, model, prompt, out, manifest, dry):
    if dry:
        print(f"    [dry-run] {RUNISO} {cli} {model} {prompt} {out} {manifest}")
        return 0
    return subprocess.run([str(RUNISO), cli, model, str(prompt), str(out), str(manifest)]).returncode


def _validate_key(concepts, dry):
    """Structural validity via the frozen validate_key.py (emits answer_key.json)."""
    if dry: return True
    r = subprocess.run([sys.executable, str(BASE / "harness/validate_key.py"), str(concepts)],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    return r.returncode == 0


# recorded v0.9 split_corpus.py hash (freeze-manifest.txt); the per-key copy is verified to it
SPLIT_RECORDED = "e240fbd46d374459cce1b649b2784795d37079c0645fd6c29fb782a80530684b"


def copy_splitter(key_dir):
    """v0.9 pattern: copy the hash-verified split_corpus.py INTO the key root so its
    `BASE = Path(__file__).resolve().parent` resolves to key_dir and it writes
    key_dir/corpora/<side>/ (the location _corpus_attempt_ok checks). Verified at copy."""
    src = BASE / "harness/split_corpus.py"
    if _sha(src) != SPLIT_RECORDED:
        sys.exit(f"split_corpus.py hash {_sha(src)[:12]} != recorded {SPLIT_RECORDED[:12]} — refusing")
    dst = Path(key_dir) / "split_corpus.py"
    dst.write_text(src.read_text())
    if _sha(dst) != SPLIT_RECORDED:
        sys.exit("copied splitter hash mismatch")
    return dst


def leak_ok(key_dir, side, corpus_dir):
    """Run the FROZEN leak checks exactly as run_test_v09.sh does, over every doc in
    `corpus_dir`: a-docs -> cross-a + meta ; b-docs -> cross-b + meta (leakcheck_peer.sh is a
    pure grep script — no model calls; it lives under key_dir). Any leak fails the attempt."""
    lc = Path(key_dir) / "leakcheck_peer.sh"
    if not lc.exists():
        sys.exit(f"leakcheck_peer.sh missing under {key_dir} (gen_leakcheck must run first)")
    cross = "cross-a" if side == "a" else "cross-b"
    for doc in sorted(Path(corpus_dir).glob("[0-9][0-9].md")):
        for mode in (cross, "meta"):
            r = subprocess.run(["bash", str(lc), mode, str(doc)], capture_output=True, text=True)
            if r.returncode != 0:
                print(f"  LEAK [{mode}] {doc.name}: {r.stdout.strip()}")
                return False
    return True


def _corpus_attempt_ok(key_dir, side, out_file):
    """Finding 7 (attempt hygiene): each attempt splits into a FRESH temp side dir, requires the
    EXACT filename set 01.md..11.md (set equality, not just a count of 11), runs the frozen leak
    checks THERE, then ATOMICALLY promotes only an accepted attempt into key_dir/corpora/<side>
    (replacing any prior contents). Stale files from a prior malformed attempt can never leak
    into or poison a retry. A wrong set, a leak, or a split failure consumes the attempt (§4.1a)."""
    key_dir = Path(key_dir)
    attempt = Path(tempfile.mkdtemp(prefix=f"{side}-attempt-", dir=str(key_dir)))
    try:
        splitter = copy_splitter(attempt)                       # BASE=attempt -> writes attempt/corpora/<side>
        r = subprocess.run([sys.executable, str(splitter), side, str(out_file)],
                           capture_output=True, text=True)
        corp = attempt / f"corpora/{side}"
        names = sorted(p.name for p in corp.glob("[0-9][0-9].md")) if corp.exists() else []
        if r.returncode != 0 or names != EXACT_DOCS:
            print(f"  split {side}: rc={r.returncode} names={names} (need EXACTLY 01..11) {r.stdout.strip()}")
            return False
        if not leak_ok(key_dir, side, corp):
            return False
        dest = key_dir / f"corpora/{side}"; dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            shutil.rmtree(dest)                                 # clean promote: no stale prior-attempt files
        shutil.move(str(corp), str(dest))
        return True
    finally:
        shutil.rmtree(attempt, ignore_errors=True)


def _call_with_retry(name, cli, model, prompt, out, manifest, validate, receipt, dry):
    """Per-call malformed-retry cap 1. Every output hashed into `receipt`; none discarded.
    Returns True on a structurally valid output, False on setup exhaustion (malformed twice)."""
    for attempt in range(RETRY_CAP + 1):
        print(f"  [{name}] attempt {attempt} -> {out}")
        rc = _isolated(cli, model, prompt, out, manifest, dry)
        if not dry and Path(out).exists():
            receipt["outputs"].append({"site": name, "attempt": attempt, "path": str(out),
                                       "sha256": _sha(out), "rc": rc})
        if validate():
            return True
        print(f"  [{name}] attempt {attempt}: MALFORMED (rc={rc})")
    print(f"  [{name}] SETUP EXHAUSTION (malformed {RETRY_CAP+1}x) -> phase FAILS, "
          f"configuration NOT retired (§4.1a)")
    return False


def build_key(key_id, args):
    key_dir = BASE / f"runs/confirmatory/{key_id}"
    done_receipt = key_dir / "setup-key.done"
    # finding 2: NEVER overwrite/regenerate a completed confirmatory key. If a completion receipt
    # bound to the current H exists, skip this key (restart-safe; no new draw under the same config).
    if done_receipt.exists():
        rec = json.loads(done_receipt.read_text())
        if rec.get("H") == args.H_value:
            print(f"  [{key_id}] already complete (setup-key.done, H matches) — SKIP (no regeneration)")
            return rec, True
        sys.exit(f"  [{key_id}] setup-key.done present with a DIFFERENT H — refusing to overwrite a "
                 f"prior confirmatory key")
    (key_dir / "key").mkdir(parents=True, exist_ok=True)
    (key_dir / "manifests").mkdir(parents=True, exist_ok=True)
    dry = args.dry_run
    receipt = {"key_id": key_id, "H": args.H_value, "draw_begins": "at key-author call",
               "outputs": [], "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    # 1. key-author (DRAW BEGINS here) -> concepts.json ; validate -> answer_key.json
    concepts = key_dir / "key/concepts.json"
    if not _call_with_retry("key-author", "claude", "claude-opus-4-8",
                            BASE / "harness/keyspec-author.md", concepts,
                            key_dir / "manifests/key-author.json",
                            lambda: _validate_key(concepts, dry), receipt, dry):
        return receipt, False
    if dry:
        print("    [dry-run] gen_leakcheck; build_briefs; corpus-gen a/b -> per-attempt fresh split "
              "(exact 01..11) + FROZEN leak checks + atomic promote; make_pairs")
        return receipt, True
    # 2. leakcheck script (from answer_key.json) + briefs (the per-attempt splitter is copied
    #    inside _corpus_attempt_ok into a fresh temp dir — finding 7)
    subprocess.run([sys.executable, str(BASE / "harness/gen_leakcheck.py"), str(key_dir)], check=True)
    subprocess.run([sys.executable, str(BASE / "harness/build_briefs.py"), str(key_dir)], check=True)
    # 3. corpus-gen A (sonnet) + B (codex): each attempt splits into a fresh temp dir, requires the
    #    exact 01..11 set + frozen leak checks, then atomically promotes; failure consumes the attempt.
    for site, cli, model, side in (("corpus-gen-a", "claude", "claude-sonnet-5", "a"),
                                   ("corpus-gen-b", "codex", "gpt-5.6-terra", "b")):
        out = key_dir / f"runs/gen-{side}.out"; out.parent.mkdir(parents=True, exist_ok=True)
        prompt = key_dir / f"prompts/gen-community-{side}.md"
        if not _call_with_retry(site, cli, model, prompt, out,
                                key_dir / f"manifests/{site}.json",
                                lambda s=side, o=out: _corpus_attempt_ok(key_dir, s, o),
                                receipt, dry):
            return receipt, False
    # 4. answer-blind pairs manifest
    subprocess.run([sys.executable, str(BASE / "make_pairs_manifest.py"),
                    str(key_dir / "key"), str(key_dir / "pairs.json")], check=True)
    # 5. per-key completion receipt (H-bound) — restart will SKIP this key
    done_receipt.write_text(json.dumps({**receipt, "ok": True, "complete": True}, indent=1))
    return receipt, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--H-value", default="<H-not-set>", dest="H_value")
    ap.add_argument("--split-script", default=str(BASE / "harness/split_corpus.py"),
                    help="frozen v0.9 split_corpus.py (defaults to the in-workspace harness/ copy, bound in H)")
    ap.add_argument("--out", default=str(BASE / "runs/confirmatory/setup-receipt.jsonl"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    (BASE / "runs/confirmatory").mkdir(parents=True, exist_ok=True)
    print("== confirmatory setup: 2 fresh TRAIN keys via the UNCHANGED frozen v0.9 path (§4.1a) ==")
    all_ok = True
    for key_id in ("conf-key-1", "conf-key-2"):
        print(f"\n-- DRAW {key_id} --")
        receipt, ok = build_key(key_id, args)
        with open(args.out, "a") as f:
            f.write(json.dumps({**receipt, "ok": ok}) + "\n")
        if not ok:
            all_ok = False
            print(f"{key_id}: SETUP EXHAUSTION -> phase fails (config NOT retired); stop.")
            break
    print(f"\nconfirmatory setup {'COMPLETE (2 keys built)' if all_ok else 'FAILED (setup exhaustion)'}"
          f"; receipts -> {args.out}")
    sys.exit(0 if all_ok else 2)


if __name__ == "__main__":
    main()
