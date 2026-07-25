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
import argparse, hashlib, json, subprocess, sys, datetime
from pathlib import Path

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


def _split_ok(split_script, side, out_file, key_dir, dry):
    if dry: return True
    r = subprocess.run([sys.executable, str(split_script), side, str(out_file)], cwd=str(key_dir),
                       capture_output=True, text=True)
    docs = sorted((key_dir / f"corpora/{side}").glob("[0-9][0-9].md"))
    return r.returncode == 0 and len(docs) == 11


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
    # 2. mechanical briefs from the sealed-input concepts (orchestrator never reads desc)
    if not dry:
        subprocess.run([sys.executable, str(BASE / "harness/build_briefs.py"), str(key_dir)], check=True)
    else:
        print(f"    [dry-run] build_briefs.py {key_dir}")
    # 3. corpus-gen A (sonnet) + B (codex), each retry-capped 1, split-validated
    for site, cli, model, side in (("corpus-gen-a", "claude", "claude-sonnet-5", "a"),
                                   ("corpus-gen-b", "codex", "gpt-5.6-terra", "b")):
        out = key_dir / f"runs/gen-{side}.out"; out.parent.mkdir(parents=True, exist_ok=True)
        prompt = key_dir / f"prompts/gen-community-{side}.md"
        if not _call_with_retry(site, cli, model, prompt, out,
                                key_dir / f"manifests/{site}.json",
                                lambda s=side, o=out: _split_ok(args.split_script, s, o, key_dir, dry),
                                receipt, dry):
            return receipt, False
    # 4. leakcheck script + answer-blind pairs manifest
    if not dry:
        subprocess.run([sys.executable, str(BASE / "harness/gen_leakcheck.py"), str(key_dir)], check=True)
        subprocess.run([sys.executable, str(BASE / "make_pairs_manifest.py"),
                        str(key_dir / "key"), str(key_dir / "pairs.json")], check=True)
    else:
        print(f"    [dry-run] gen_leakcheck.py {key_dir}; make_pairs_manifest.py {key_dir}/key")
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
