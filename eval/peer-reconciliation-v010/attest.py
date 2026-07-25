#!/usr/bin/env python3
"""attest.py — attestation + custody tooling (v0.10 prereg §4.2, §4.4). NO LLM calls.

Subcommands:
  build-H       compute H = digest of the manifest-of-manifests (§4.2 step 2) and write H.json
  verify-files  re-hash the v0.10 inventory (+ corpora if present) vs H; sealed key checked
                by RECORDED hash only (never re-hashed) — the deterministic core of attestation
  attest        the ONE reusable two-point attestation gate (§4.2 steps 6 & 8): verify-files
                + clean git tree + CLI-version ENFORCED == recorded + pinned model IDs resolve
                (membership, read from the probe log) + frozen decoding params in effect +
                the §3.6(f) conformance runner PASSES. Use --point 1 (pre-generation) or
                --point 2 (post-generation). Any mismatch -> nonzero exit.
  receipt       write a draw/key-run receipt carrying H (§4.2 step 4/5/7)
  spend-log     append a §4.4 spend-state event to the authoritative spend log

H's manifest-of-manifests entries (§4.2 step 2):
  * v0.10 implementation, generation/gate prompts, both baseline templates + re-ask files,
    golden fixtures, parser, serializers, conformance runner (re-hashed here);
  * the frozen per-CLI decoding-parameter set (§6) + pinned model IDs;
  * the inherited v0.9 manifests binding the corpora + BGE snapshot tree + SEALED key files,
    bound by their RECORDED hashes from freeze-manifest.txt — the sealed answer files are
    NEVER re-hashed here (that would cross the spend boundary).
"""
import argparse, hashlib, json, re, subprocess, sys, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spend  # locked one-shot spend/state gate (§4.3/§4.4)

BASE = Path(__file__).resolve().parent

# v0.10 files bound into H (re-hashable, present at freeze). Globs relative to BASE.
INVENTORY_GLOBS = [
    "*.py", "prompts/*.md", "fixtures/*.json", "tests/*.py", "scripts/*.py",
    "harness/*.py", "harness/*.md", "*.sh",
]
# Run-time answer-blind artifacts also bound if present (placed at run time).
RUNTIME_GLOBS = ["pairs.json", "leakcheck_peer.sh", "corpora/a/*.md", "corpora/b/*.md",
                 "corpora/a/manifest.json", "corpora/b/manifest.json"]

# §6 frozen decoding-parameter set (replaces "temperature 0").
DECODING_PARAMS = {
    "claude-opus-4-8": "claude CLI defaults at the recorded version; NO sampling overrides; single-turn isolated; no automatic retry",
    "claude-sonnet-5": "claude CLI defaults at the recorded version; NO sampling overrides; single-turn isolated; no automatic retry",
    "gpt-5.6-terra": "codex wrapper frozen model_reasoning_effort=high; single-turn isolated",
}
PINNED_MODEL_IDS = ["claude-opus-4-8", "claude-sonnet-5", "gpt-5.6-terra"]
# helper model that is expected-and-ignored in the resolved set (§6)
HELPER_MODEL = "claude-haiku-4-5-20251001"

# the committed frozen v0.9 record + the recorded BGE snapshot (for run-time attestation)
RECORDED_MANIFEST = BASE / ".." / "peer-reconciliation-test3" / "freeze-manifest.txt"
SNAPSHOT = Path("/home/nik/.cache/huggingface/hub/models--BAAI--bge-large-en-v1.5/"
                "snapshots/d4aa6901d3a41ba39fb536a557fa166f842b0e09")
# v0.9 files carried UNCHANGED into the workspace — hash-verified against freeze-manifest.txt
# recorded values at BOTH attestation points (basename lookup). run_isolated.sh is hash-verified
# here (replacing the old substring check).
RECORDED_ARTIFACTS = [
    "prompts/checklist-extract.md", "prompts/ladder-conformance.md", "prompts/polarity-check.md",
    "prompts/verify-matrix.md", "prompts/verify-pair.md", "prompts/decompose.md",
    "prompts/containment-v2.md", "harness/split_corpus.py", "harness/gen_leakcheck.py",
    "../e2e-cell/run_isolated.sh",
]
# freeze-package files build-H REQUIRES (refuse if absent) and binds by hash into H:
PREREG_MD = BASE / "PREREG.md"                 # the ratified spec copy (placed at the freeze commit)
RECORDED_CLI_JSON = BASE / "recorded-cli.json"  # the frozen CLI-version record
# exact run-time inventory build-H --runtime additionally requires present:
RUNTIME_REQUIRED = (["pairs.json", "leakcheck_peer.sh",
                     "corpora/a/manifest.json", "corpora/b/manifest.json",
                     "key/concepts.json", "key/answer_key.json"]
                    + [f"corpora/{s}/{i:02d}.md" for s in ("a", "b") for i in range(1, 12)])
# CANONICAL exact corpora set (finding 4): the ONLY numbered corpus docs allowed. build-H
# --runtime rejects any extra (e.g. corpora/a/12.md) and any missing.
CORPORA_CANONICAL = {f"corpora/{s}/{i:02d}.md" for s in ("a", "b") for i in range(1, 12)}

# step-7 OUTPUT manifest (finding 3): the scorer's REQUIRED inputs + the broader deterministic
# step-7 outputs, hashed at end of generation, enforced at attestation-2, and re-verified by the
# scorer BEFORE it claims the key.
OUTPUT_REQUIRED = ["runs/v010/verdicts.json", "runs/baseline_a/records.json", "runs/baseline_b/records.json"]
OUTPUT_GLOBS = ["runs/v010/verdicts.json", "runs/v010/review-context.json", "runs/v010/agg.json",
                "runs/v010/route-union.json", "runs/v010/verify/out-*.json", "runs/v010/symcheck/out-*.json",
                "runs/v010/decompose/out-*.json", "runs/v010/containment/out-*.json", "runs/v010/manifests/*.json",
                "runs/baseline_a/records.json", "runs/baseline_a/out-*.txt",
                "runs/baseline_b/records.json", "runs/baseline_b/out-*.txt",
                "runs/manifests/*.json", "runs/checklists/out-*.txt", "runs/definitions/out-*.json",
                "runs/conformance/out-*.json", "runs/polarity/out-*.json"]


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _inventory(globs, base=BASE):
    files = {}
    for g in globs:
        for p in sorted(Path(base).glob(g)):
            if p.is_file():
                files[str(p.relative_to(base))] = _sha(p)
    return files


def bge_tree_hash(snapshot_dir):
    """§9-F7: sha256 over the sorted list of (relative path, file sha256) pairs — the SAME
    definition as retrieve_xc_v010.tree_hash, recomputed here to verify the live snapshot."""
    d = Path(snapshot_dir)
    entries = [f"{p.relative_to(d)} {_sha(p)}" for p in sorted(x for x in d.rglob('*') if x.is_file())]
    return hashlib.sha256("\n".join(entries).encode()).hexdigest()


def _recorded_hash_for(manifest, basename):
    for line in Path(manifest).read_text().splitlines():
        line = line.strip()
        if "  " not in line:
            continue
        h, rel = line.split(None, 1)
        if len(h) == 64 and all(c in "0123456789abcdef" for c in h.lower()) and Path(rel.strip()).name == basename:
            return h.lower()
    return None


def verify_recorded_artifacts(recorded_manifest=RECORDED_MANIFEST, base=BASE):
    """Hash-verify each v0.9-carried artifact (incl. the isolation wrapper) against its recorded
    value in the frozen record. Returns a list of error strings (empty = OK)."""
    errs = []
    if not Path(recorded_manifest).exists():
        return [f"frozen record missing: {recorded_manifest}"]
    for rel in RECORDED_ARTIFACTS:
        f = Path(base) / rel
        want = _recorded_hash_for(recorded_manifest, Path(rel).name)
        if not f.exists():
            errs.append(f"recorded artifact MISSING: {rel}"); continue
        if want is None:
            errs.append(f"no recorded hash for {Path(rel).name}"); continue
        if _sha(f) != want:
            errs.append(f"recorded artifact drift: {rel} (recorded {want[:12]} != live {_sha(f)[:12]})")
    return errs


def check_bge(man, snapshot_dir=SNAPSHOT):
    """Recompute the live BGE snapshot-tree hash and compare to the value bound in H. Returns
    a list of error strings (empty = OK)."""
    bound = man["inherited_recorded"].get("bge_snapshot_tree_sha256")
    if not bound:
        return ["no bge_snapshot_tree_sha256 bound in H"]
    if not Path(snapshot_dir).is_dir():
        return [f"BGE snapshot dir absent at {snapshot_dir} — cannot recompute (REQUIRED at run time)"]
    live = bge_tree_hash(snapshot_dir)
    return [] if live == bound else [f"BGE tree drift: bound {bound[:12]} != live {live[:12]}"]


def _parse_recorded(recorded_manifest):
    """freeze-manifest.txt -> {relpath: sha256} for sha256sum-style lines + the bge tree line."""
    recorded, bge = {}, None
    for line in Path(recorded_manifest).read_text().splitlines():
        line = line.strip()
        if line.startswith("bge_snapshot_tree_sha256:"):
            bge = line.split(":", 1)[1].strip()
            continue
        if "  " in line:
            h, rel = line.split(None, 1)
            h, rel = h.strip(), rel.strip()
            if len(h) == 64 and all(c in "0123456789abcdef" for c in h.lower()):
                recorded[rel] = h.lower()
    return recorded, bge


def _canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def required_inventory(req_inv_path):
    return {l.strip() for l in Path(req_inv_path).read_text().splitlines()
            if l.strip() and not l.startswith("#")}


def impl_inventory_diff(required_set, base=BASE):
    """Return (sorted extras, sorted missing) between the discovered impl inventory and the
    canonical required set — finding 4 exact-equality check."""
    disc = set(_inventory(INVENTORY_GLOBS, base))
    return sorted(disc - required_set), sorted(required_set - disc)


def corpora_exact_errs(base=BASE):
    """Return {extra, missing} vs the canonical exact corpora set (01..11 both sides)."""
    disc = {r for r in _inventory(RUNTIME_GLOBS, base) if re.match(r"corpora/[ab]/\d\d\.md$", r)}
    return {"extra": sorted(disc - CORPORA_CANONICAL), "missing": sorted(CORPORA_CANONICAL - disc)}


def build_H(args):
    # REQUIRED-inventory enforcement (round-6): build-H REFUSES if a required file is missing,
    # rather than silently omitting it (a later "STRICT" verify cannot notice an omission).
    #   freeze-package tier (always): PREREG.md (the ratified spec copy) + recorded-cli.json.
    #     Pre-freeze, PREREG.md is absent -> build-H refuses, which is the correct behavior.
    #   runtime tier (--runtime): the exact corpora (01..11 both sides + manifests), pairs.json,
    #     leakcheck_peer.sh, and the sealed key files.
    req_inv = BASE / "REQUIRED-INVENTORY.txt"
    missing = [str(p.relative_to(BASE)) for p in (PREREG_MD, RECORDED_CLI_JSON, req_inv) if not p.exists()]
    if args.runtime:
        missing += [r for r in RUNTIME_REQUIRED if not (BASE / r).exists()]
    if missing:
        sys.exit(f"build-H REFUSED: required file(s) missing: {missing} "
                 f"(pre-freeze absence of PREREG.md is correct — place the ratified spec first)")
    # finding 4: EXACT implementation inventory — discovered names must EQUAL the canonical
    # required set (reject any extra file and any missing normative source/prompt/fixture/wrapper).
    required_impl = required_inventory(req_inv)
    extra, miss = impl_inventory_diff(required_impl, BASE)
    if extra or miss:
        sys.exit(f"build-H REFUSED: implementation inventory != canonical "
                 f"(extra={extra}, missing={miss})")
    # finding 4: EXACT runtime corpora — reject any extra numbered doc (e.g. corpora/a/12.md).
    if args.runtime:
        ce = corpora_exact_errs(BASE)
        if ce["extra"] or ce["missing"]:
            sys.exit(f"build-H REFUSED: corpora != exactly 01..11 (extra={ce['extra']}, missing={ce['missing']})")
    recorded, bge = _parse_recorded(args.recorded_manifest)
    def pick(pred):
        return {rel: h for rel, h in recorded.items() if pred(rel)}
    inherited_corpora = pick(lambda r: "corpora/" in r)
    sealed = pick(lambda r: r.startswith("key/") or "/key/" in r or Path(r).parent.name == "key")
    manifest = {
        "spec": "v0.10 generation-hardening (PREREG.md, ratified copy, hash below)",
        "prereg_sha256": _sha(PREREG_MD),          # binds the ratified spec BYTES, not a label
        "recorded_cli_sha256": _sha(RECORDED_CLI_JSON),  # binds the frozen CLI-version record
        "required_inventory_sha256": _sha(req_inv),  # binds the canonical exact-inventory list
        "v010_files": _inventory(INVENTORY_GLOBS),
        "runtime_answer_blind_files": _inventory(RUNTIME_GLOBS),
        "decoding_params": DECODING_PARAMS,
        "pinned_model_ids": PINNED_MODEL_IDS,
        "helper_model_expected_and_ignored": HELPER_MODEL,
        # binds the recorded-hashes FILE (freeze-manifest.txt) itself, so the scorer can prove
        # its --recorded-hashes input is the one attested into H (§ scorer↔H binding).
        "recorded_manifest_sha256": _sha(args.recorded_manifest),
        "inherited_recorded": {
            "corpora": inherited_corpora,
            "bge_snapshot_tree_sha256": bge,
            "sealed_key_recorded_hashes_BOUND_NOT_REHASHED": sealed,
        },
        "note": "sealed key files are bound by RECORDED hashes only; NEVER re-hashed here "
                "(re-hashing crosses the spend boundary; the scorer verifies them at step 9).",
    }
    H = hashlib.sha256(_canonical(manifest)).hexdigest()
    out = {"H": H, "manifest_of_manifests": manifest,
           "built": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    json.dump(out, open(args.out, "w"), indent=1)
    print(f"H = {H}")
    print(f"  v010 files bound: {len(manifest['v010_files'])}; runtime answer-blind: "
          f"{len(manifest['runtime_answer_blind_files'])}; inherited corpora: "
          f"{len(inherited_corpora)}; sealed (recorded-only): {len(sealed)}; bge: {bge or 'MISSING'}")
    print(f"H.json -> {args.out}")


def load_and_verify_H(hfile):
    """Load H.json and PROVE H["H"] is the canonical hash of its own manifest-of-manifests
    (else a tampered H.json with updated per-file hashes but a retained old H would pass).
    Shared by verify-files, attest, and scorer_v010. Raises SystemExit on mismatch."""
    obj = json.load(open(hfile))
    recomputed = hashlib.sha256(_canonical(obj["manifest_of_manifests"])).hexdigest()
    if recomputed != obj["H"]:
        raise SystemExit(f"H SELF-CHECK FAILED: recomputed {recomputed} != stored H {obj['H']} "
                         f"({hfile} was modified after freeze) — hard fail")
    return obj


def _verify_files_errs(man, base=BASE):
    """Pure, STRICT inventory verification (no exists()-tolerance). Returns error strings."""
    errs = []
    now = _inventory(INVENTORY_GLOBS, base)
    for rel, h in man["v010_files"].items():
        if now.get(rel) != h:
            errs.append(f"v010 file drift/MISSING: {rel}")
    for rel in now:
        if rel not in man["v010_files"]:
            errs.append(f"v010 file NOT in H (new/unbound): {rel}")
    # runtime answer-blind files: STRICT — every bound file present+match; no extra unbound
    nowrt = _inventory(RUNTIME_GLOBS, base)
    man_rt = man.get("runtime_answer_blind_files", {})
    for rel, h in man_rt.items():
        if nowrt.get(rel) != h:
            errs.append(f"runtime file drift/MISSING: {rel}")
    for rel in nowrt:
        if rel not in man_rt:
            errs.append(f"runtime file on disk NOT in H: {rel}")
    # corpora: STRICT — every recorded corpus must be present and match its recorded hash
    for rel, h in man["inherited_recorded"]["corpora"].items():
        p = Path(base) / rel
        if not p.exists() or _sha(p) != h:
            errs.append(f"corpus MISSING/drift vs recorded: {rel}")
    if not man["inherited_recorded"]["sealed_key_recorded_hashes_BOUND_NOT_REHASHED"]:
        errs.append("no sealed-key recorded hashes bound in H")
    # ratified spec + CLI record bound in H must be present and match
    for name, key in (("PREREG.md", "prereg_sha256"), ("recorded-cli.json", "recorded_cli_sha256"),
                      ("REQUIRED-INVENTORY.txt", "required_inventory_sha256")):
        f = Path(base) / name
        if key not in man:
            errs.append(f"{key} not bound in H")
        elif not f.exists() or _sha(f) != man[key]:
            errs.append(f"{name} MISSING/drift vs H")
    return errs


def verify_files(args):
    H = load_and_verify_H(args.H)
    man = H["manifest_of_manifests"]
    errs = _verify_files_errs(man, BASE)
    if errs:
        for e in errs: print("  MISMATCH:", e)
        return False
    print(f"verify-files OK (STRICT): {len(man['v010_files'])} v0.10 files + "
          f"{len(man.get('runtime_answer_blind_files', {}))} runtime files + "
          f"{len(man['inherited_recorded']['corpora'])} corpora present & match H; "
          f"sealed key bound by recorded hash (not re-hashed).")
    return True


def build_output_manifest_at(H_value, out_path, base=BASE):
    """Finding 3: hash the COMPLETE step-7 output set (scorer inputs + model outputs / call
    manifests / derived records) under `base` into a receipt bound to H_value."""
    base = Path(base)
    missing = [r for r in OUTPUT_REQUIRED if not (base / r).exists()]
    if missing:
        sys.exit(f"output-manifest REFUSED: required step-7 outputs missing: {missing}")
    files = {}
    for g in OUTPUT_GLOBS:
        for p in sorted(base.glob(g)):
            if p.is_file():
                files[str(p.relative_to(base))] = _sha(p)
    out = {"H": H_value, "files": files, "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    json.dump(out, open(out_path, "w"), indent=1)
    return files


def build_output_manifest(args):
    hobj = load_and_verify_H(args.H)
    files = build_output_manifest_at(hobj["H"], args.out, BASE)
    print(f"output-manifest: {len(files)} step-7 outputs bound (H {hobj['H'][:12]}) -> {args.out}")


def _verify_output_manifest_errs(output_manifest, expected_H, base=BASE):
    """attestation-2: every file in the output-manifest must be present + hash-match; H must bind."""
    om = json.load(open(output_manifest))
    errs = []
    if om.get("H") != expected_H:
        errs.append(f"output-manifest H {om.get('H')} != attested H {expected_H}")
    for r in OUTPUT_REQUIRED:
        if r not in om.get("files", {}):
            errs.append(f"output-manifest omits required output {r}")
    for rel, h in om.get("files", {}).items():
        p = Path(base) / rel
        if not p.exists() or _sha(p) != h:
            errs.append(f"step-7 output MISSING/drift vs manifest: {rel}")
    return errs


def _cli_versions():
    def v(cmd):
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
        except FileNotFoundError:
            return None
    return {"claude": v(["claude", "--version"]), "codex": v(["codex", "--version"])}


def attest(args):
    ok = True
    print(f"== ATTESTATION POINT {args.point} ({'pre-generation' if args.point==1 else 'post-generation'}) ==")
    # 1. file hashes == H
    if not verify_files(args): ok = False
    # 2. clean git working tree
    st = subprocess.run(["git", "-C", str(BASE), "status", "--porcelain"], capture_output=True, text=True)
    dirty = [l for l in st.stdout.splitlines() if l.strip()]
    if dirty and not args.allow_dirty:
        print(f"  MISMATCH: git working tree not clean ({len(dirty)} entries)"); ok = False
    else:
        print("  clean git tree: OK" + (" (--allow-dirty)" if args.allow_dirty else ""))
    # 3. CLI versions ENFORCED == recorded
    if args.recorded_cli:
        rec = json.load(open(args.recorded_cli))  # {"claude": "...", "codex": "..."}
        cur = _cli_versions()
        for k, want in rec.items():
            if cur.get(k) != want:
                print(f"  MISMATCH: {k} CLI version {cur.get(k)!r} != recorded {want!r}"); ok = False
            else:
                print(f"  {k} CLI version ENFORCED == recorded: OK ({want})")
    else:
        print("  (CLI-version enforcement skipped: no --recorded-cli; REQUIRED at real run time)")
    # 4. pinned model IDs resolve (membership) from the probe log
    if args.probe_log:
        pl = json.load(open(args.probe_log))  # {"resolved": {"opus":[...],"sonnet":[...]}}
        resolved = pl.get("resolved", {})
        members = set().union(*[set(v) for v in resolved.values()]) if resolved else set()
        for mid in PINNED_MODEL_IDS:
            if mid.startswith("claude-") and mid not in members:
                print(f"  MISMATCH: pinned {mid} not a member of resolved set {sorted(members)}"); ok = False
        print(f"  pinned model-ID membership: {'OK' if ok else 'FAILED'} (helper {HELPER_MODEL} expected-and-ignored)")
    else:
        print("  (model-ID membership skipped: no --probe-log; REQUIRED at real run time — run probe_explicit_id.sh)")
    # 5. v0.9-carried artifacts (incl. the isolation wrapper) hash-verified against the frozen
    #    record — replaces the old substring check on run_isolated.sh.
    ra_errs = verify_recorded_artifacts(RECORDED_MANIFEST, BASE)
    if ra_errs:
        for e in ra_errs: print("  MISMATCH (recorded artifact):", e)
        ok = False
    else:
        print(f"  {len(RECORDED_ARTIFACTS)} v0.9-carried artifacts (incl. isolation wrapper) "
              f"hash-match the frozen record: OK")
    # 5b. BGE snapshot-tree hash recomputed live and compared to the value bound in H
    bge_errs = check_bge(load_and_verify_H(args.H)["manifest_of_manifests"], SNAPSHOT)
    if bge_errs:
        for e in bge_errs: print("  MISMATCH (BGE):", e)
        ok = False
    else:
        print("  BGE snapshot-tree hash recomputed live == bound in H: OK")
    # 6. conformance runner passes (§3.6f)
    cr = subprocess.run([sys.executable, str(BASE / "conformance_runner.py")], capture_output=True, text=True)
    if cr.returncode != 0:
        print("  MISMATCH: §3.6(f) conformance runner FAILED"); print(cr.stdout[-500:]); ok = False
    else:
        print("  §3.6(f) conformance runner: PASS")
    # 6b. attestation-2 ONLY: enforce the step-7 output manifest (finding 3) — every scoring
    #     input + model output present and hash-matching, bound to H.
    if args.point == 2:
        if not args.output_manifest:
            print("  MISMATCH: attestation-2 requires --output-manifest"); ok = False
        else:
            om_errs = _verify_output_manifest_errs(args.output_manifest, load_and_verify_H(args.H)["H"], BASE)
            if om_errs:
                for e in om_errs: print("  MISMATCH (output-manifest):", e)
                ok = False
            else:
                print("  step-7 output manifest: all outputs present & hash-match H: OK")
    # 7. write an integrity-bound attestation record (H + the exact recorded-cli + probe-log bytes)
    rec = {"point": args.point, "H": load_and_verify_H(args.H)["H"], "pass": ok,
           "recorded_cli_sha256": _sha(args.recorded_cli),
           "probe_log_sha256": _sha(args.probe_log),
           "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    (BASE / f"runs/attestation-point-{args.point}.json").write_text(json.dumps(rec, indent=1))
    print(f"  attestation record bound: recorded-cli {rec['recorded_cli_sha256'][:12]}, "
          f"probe-log {rec['probe_log_sha256'][:12]}")
    print(f"== ATTESTATION POINT {args.point}: {'PASS' if ok else 'FAIL'} ==")
    sys.exit(0 if ok else 1)


def receipt(args):
    H = load_and_verify_H(args.H)["H"]   # receipts store the SELF-VERIFIED H
    rec = {"kind": args.kind, "H": H, "label": args.label,
           "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    with open(args.out, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"receipt ({args.kind}, H={H[:12]}...) -> {args.out}")


def spend_log(args):
    """Locked, one-shot-enforced append via spend.py. A refused transition (second
    first-authorized-read, second authorized-read, or any append after accidental-access)
    exits nonzero — so run_v010.sh's `set -e` halts and the scorer never launches."""
    entry = spend.append_event(args.out, args.event, args.notes)
    print(f"spend-state logged: {args.event} -> {args.out}\n  {entry['meaning']}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build-H"); b.add_argument("--recorded-manifest", required=True); b.add_argument("--out", required=True)
    b.add_argument("--runtime", action="store_true", help="also require the exact run-time inventory (corpora 01..11, pairs.json, leakcheck, key)"); b.set_defaults(fn=build_H)
    v = sub.add_parser("verify-files"); v.add_argument("--H", required=True); v.set_defaults(fn=verify_files)
    a = sub.add_parser("attest"); a.add_argument("--H", required=True); a.add_argument("--point", type=int, choices=(1, 2), required=True)
    a.add_argument("--recorded-cli", required=True); a.add_argument("--probe-log", required=True)
    a.add_argument("--output-manifest", help="required at point 2: the step-7 output receipt to enforce")
    a.add_argument("--allow-dirty", action="store_true"); a.set_defaults(fn=attest)
    om = sub.add_parser("build-output-manifest"); om.add_argument("--H", required=True); om.add_argument("--out", required=True); om.set_defaults(fn=build_output_manifest)
    r = sub.add_parser("receipt"); r.add_argument("--H", required=True); r.add_argument("--kind", required=True); r.add_argument("--label", default=""); r.add_argument("--out", required=True); r.set_defaults(fn=receipt)
    s = sub.add_parser("spend-log"); s.add_argument("--event", required=True); s.add_argument("--notes", default=""); s.add_argument("--out", required=True); s.set_defaults(fn=spend_log)
    args = ap.parse_args()
    result = args.fn(args)
    if args.cmd == "verify-files":
        sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
