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
# round-8 finding 1: the synthetic toy-key (a phase-0 proof input) is now committed + bound.
INVENTORY_GLOBS = [
    "*.py", "prompts/*.md", "fixtures/*.json", "tests/*.py", "scripts/*.py",
    "harness/*.py", "harness/*.md", "*.sh",
    "toy-key/key/*.json", "toy-key/*.json", "toy-key/*.txt",
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
# CANONICAL exact corpora set (finding 4): the ONLY corpus docs allowed. build-H --runtime rejects
# ANY extra .md (numeric like corpora/a/12.md OR nonnumeric like corpora/a/notes.md — round-9) and
# any missing. The sealed key dir must contain EXACTLY these two files (round-9: no key-dir extras).
CORPORA_CANONICAL = {f"corpora/{s}/{i:02d}.md" for s in ("a", "b") for i in range(1, 12)}
KEY_CANONICAL = {"key/concepts.json", "key/answer_key.json"}

# step-7 OUTPUT manifest (finding 3): the scorer's REQUIRED inputs + the broader deterministic
# step-7 outputs, hashed at end of generation, enforced at attestation-2, and re-verified by the
# scorer BEFORE it claims the key.
OUTPUT_REQUIRED = ["runs/v010/verdicts.json", "runs/baseline_a/records.json", "runs/baseline_b/records.json"]
# deterministic DERIVED step-7 outputs (not staged model calls; produced by the controller):
OUTPUT_DERIVED = ["runs/v010/review-context.json", "runs/v010/agg.json", "runs/v010/route-union.json",
                  "runs/v010/retrieval.json"]
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
    """Round-9 finding 6: compare the COMPLETE discovered corpora/{a,b}/*.md set (ALL .md, not just
    the numeric pattern — so `corpora/a/notes.md` is caught) against CORPORA_CANONICAL, and the
    discovered key/* set against KEY_CANONICAL (an unexpected key-dir file is caught). Returns
    {extra, missing, key_extra}."""
    base = Path(base)
    disc = {str(p.relative_to(base)) for s in ("a", "b")
            for p in (base / f"corpora/{s}").glob("*.md") if p.is_file()}
    key_disc = {str(p.relative_to(base)) for p in (base / "key").glob("*") if p.is_file()}
    return {"extra": sorted(disc - CORPORA_CANONICAL), "missing": sorted(CORPORA_CANONICAL - disc),
            "key_extra": sorted(key_disc - KEY_CANONICAL)}


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
    # finding 4/6: EXACT runtime corpora — reject any extra .md (numeric OR nonnumeric) and any
    # unexpected key-dir file (round-9).
    if args.runtime:
        ce = corpora_exact_errs(BASE)
        if ce["extra"] or ce["missing"] or ce["key_extra"]:
            sys.exit(f"build-H REFUSED: corpora/key != exact set "
                     f"(extra={ce['extra']}, missing={ce['missing']}, key_extra={ce['key_extra']})")
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


def _manifest_recorded_sha(base, man_rel):
    """The out_sha256 recorded in a completed call's isolation manifest, or None."""
    m = Path(base) / man_rel
    if not m.is_file():
        return None
    hm = re.search(r"^out_sha256: ([0-9a-f]{64})$", m.read_text(), re.M)
    return hm.group(1) if hm else None


def _manifest_expects_output(base, man_rel):
    """A staged call COMPLETED (and therefore SHOULD have produced an output) iff its isolation
    manifest records `exit: 0` + a recorded out_sha256. Determined from the MANIFEST ALONE — NOT
    from the output's presence — so that a completed output DELETED before manifest construction is
    still EXPECTED (and thus caught as missing), rather than silently dropped (finding 4). A FAILED
    call has a non-zero exit (run_calls.sh deletes its output), so it does not expect an output."""
    m = Path(base) / man_rel
    if not m.is_file():
        return False
    txt = m.read_text()
    return bool(re.search(r"^exit: 0$", txt, re.M)) and bool(re.search(r"^out_sha256: [0-9a-f]{64}$", txt, re.M))


def _staged_rows(base):
    """Yield (out_rel, man_rel) for every row of every staged calls tsv, base-relative."""
    base = Path(base)
    for tsv in sorted(base.glob("runs/**/*calls.tsv")):
        for line in tsv.read_text().splitlines():
            cols = line.split("\t")
            if len(cols) < 5:
                continue
            out_rel = str(Path(cols[3]).resolve().relative_to(base)) if Path(cols[3]).is_absolute() else cols[3]
            man_rel = str(Path(cols[4]).resolve().relative_to(base)) if Path(cols[4]).is_absolute() else cols[4]
            yield out_rel, man_rel


def step7_expected(base=BASE):
    """Finding 4: derive the EXACT expected step-7 output set from the staged call manifests +
    the deterministic derived records. For every staged row, the isolation MANIFEST is expected;
    the OUTPUT is expected iff the manifest records a completed call. Round-9: the deterministic
    derived records (OUTPUT_REQUIRED + OUTPUT_DERIVED) are ALWAYS expected — UNCONDITIONALLY, so a
    DELETED derived record is caught as missing (not silently omitted). Returns a set of relpaths."""
    base = Path(base)
    expected = set()
    for out_rel, man_rel in _staged_rows(base):
        expected.add(man_rel)                                  # the call manifest is always expected
        if _manifest_expects_output(base, man_rel):
            expected.add(out_rel)                             # a completed call's output is expected
    expected.update(OUTPUT_REQUIRED)                          # scorer inputs — unconditional
    expected.update(OUTPUT_DERIVED)                           # deterministic derived records — unconditional
    return expected


def _completed_output_drift_errs(base=BASE):
    """Round-9 finding 4: every PRESENT completed staged output must byte-hash EQUAL the value its
    own call manifest recorded — a modified completed model output cannot be adopted as canonical.
    (A missing completed output is caught by the set-equality missing-check, not here.)"""
    base = Path(base)
    errs = []
    for out_rel, man_rel in _staged_rows(base):
        if _manifest_expects_output(base, man_rel):
            o = base / out_rel
            if o.exists() and _sha(o) != _manifest_recorded_sha(base, man_rel):
                errs.append(f"completed output {out_rel} hash != its call manifest out_sha256 ({man_rel})")
    return errs


def build_output_manifest_at(H_value, out_path, base=BASE):
    """Finding 4 (round-9): build the EXACT step-7 output manifest. Every expected output must be
    present (missing => refuse), no OUTPUT_GLOBS file outside the expected set may exist (extra =>
    refuse), and every completed output must hash-match its call manifest's recorded out_sha256
    (drift => refuse). Hash exactly the expected set, bound to H_value."""
    base = Path(base)
    expected = step7_expected(base)
    missing = sorted(r for r in expected if not (base / r).exists())
    if missing:
        sys.exit(f"output-manifest REFUSED: expected step-7 output(s) missing: {missing}")
    discovered = {str(p.relative_to(base)) for g in OUTPUT_GLOBS for p in base.glob(g) if p.is_file()}
    extra = sorted(discovered - expected)
    if extra:
        sys.exit(f"output-manifest REFUSED: unlisted step-7 output(s) present (extra): {extra}")
    drift = _completed_output_drift_errs(base)
    if drift:
        sys.exit(f"output-manifest REFUSED: completed-output drift vs call manifest: {drift}")
    files = {rel: _sha(base / rel) for rel in sorted(expected)}
    out = {"H": H_value, "files": files, "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    json.dump(out, open(out_path, "w"), indent=1)
    return files


def build_output_manifest(args):
    hobj = load_and_verify_H(args.H)
    files = build_output_manifest_at(hobj["H"], args.out, BASE)
    print(f"output-manifest: {len(files)} step-7 outputs bound EXACTLY (H {hobj['H'][:12]}) -> {args.out}")


def _verify_output_manifest_errs(output_manifest, expected_H, base=BASE):
    """attestation-2: SET EQUALITY — the manifest's file set must equal the freshly-derived
    expected step-7 set (missing AND extra rejected), every listed file present + hash-match, AND
    every completed output must still match its call manifest's out_sha256 (round-9 drift check)."""
    om = json.load(open(output_manifest))
    errs = []
    if om.get("H") != expected_H:
        errs.append(f"output-manifest H {om.get('H')} != attested H {expected_H}")
    listed = set(om.get("files", {}))
    expected = step7_expected(base)
    for r in sorted(expected - listed):
        errs.append(f"output-manifest omits expected step-7 output {r}")
    for r in sorted(listed - expected):
        errs.append(f"output-manifest lists an unexpected output {r}")
    for rel, h in om.get("files", {}).items():
        p = Path(base) / rel
        if not p.exists() or _sha(p) != h:
            errs.append(f"step-7 output MISSING/drift vs manifest: {rel}")
    errs += _completed_output_drift_errs(base)
    return errs


def _verify_confirmatory_receipt(conf_dir, expected_H):
    """Finding 3: attestation-1 verifies a confirmatory draw's TYPED receipt — it must exist,
    bind H, assert gate_pass=true, and its recorded accepted-corpora hashes must re-hash-match."""
    r = Path(conf_dir) / "runs/confirmatory-result.json"
    if not r.exists():
        return [f"confirmatory receipt missing: {r}"]
    rec = json.loads(r.read_text())
    errs = []
    if rec.get("H") != expected_H:
        errs.append(f"{conf_dir}: confirmatory receipt H != attested H")
    if rec.get("gate_pass") is not True:
        errs.append(f"{conf_dir}: confirmatory gate_pass != true")
    for rel, h in (rec.get("corpora_sha256") or {}).items():
        p = Path(conf_dir) / rel
        if not p.exists() or _sha(p) != h:
            errs.append(f"{conf_dir}: corpus {rel} missing/drift vs receipt")
    if not rec.get("corpora_sha256"):
        errs.append(f"{conf_dir}: confirmatory receipt has no accepted-corpora hashes")
    return errs


def _cli_versions():
    def v(cmd):
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
        except FileNotFoundError:
            return None
    return {"claude": v(["claude", "--version"]), "codex": v(["codex", "--version"])}


def input_binding_errs(man, recorded_cli, probe_log, point, base=BASE):
    """Finding 6 (deterministic pre-claim input binding — unit-testable): (a) sealed key files
    EXIST as regular files (existence/type only, NO content read); (b) recorded-cli.json has the
    EXACT two-CLI schema; (c) its bytes hash-match the value bound in H; (d) at point 2 the
    probe-log bytes are IDENTICAL to those recorded at attestation-1. Returns a list of errors."""
    base = Path(base)
    errs = []
    for name in ("concepts.json", "answer_key.json"):
        f = base / "key" / name
        if not f.is_file() or f.is_symlink():
            errs.append(f"sealed key file key/{name} missing/not-a-regular-file")
    rec = json.load(open(recorded_cli))
    if set(rec) != {"claude", "codex"}:
        errs.append(f"recorded-cli.json schema {sorted(rec)} != exactly {{claude, codex}}")
    if hashlib.sha256(Path(recorded_cli).read_bytes()).hexdigest() != man.get("recorded_cli_sha256"):
        errs.append("--recorded-cli hash != value bound in H")
    if point == 2:
        probe_sha = hashlib.sha256(Path(probe_log).read_bytes()).hexdigest()
        p1 = base / "runs/attestation-point-1.json"
        if not p1.exists() or json.loads(p1.read_text()).get("probe_log_sha256") != probe_sha:
            errs.append("attestation-2 probe-log hash != the hash recorded at attestation-1")
    return errs


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
    man = load_and_verify_H(args.H)["manifest_of_manifests"]
    # 2b/3a/3b/4b. deterministic pre-claim input binding (finding 6): key-file existence, exact
    #     recorded-cli schema, recorded-cli hash bound in H, and point-2 probe-log identity.
    for e in input_binding_errs(man, args.recorded_cli, args.probe_log, args.point, BASE):
        print("  MISMATCH:", e); ok = False
    if args.point == 2:
        print("  (probe-log identity vs attestation-1 checked)")
    # 3. recorded-cli.json: live CLI-version enforcement (env-dependent) == recorded
    rec = json.load(open(args.recorded_cli))
    cur = _cli_versions()
    for k, want in rec.items():
        if cur.get(k) != want:
            print(f"  MISMATCH: {k} CLI version {cur.get(k)!r} != recorded {want!r}"); ok = False
        else:
            print(f"  {k} CLI version ENFORCED == recorded: OK ({want})")
    # 4. pinned model IDs resolve (membership) from the probe log (point-2 probe-log identity is
    #    enforced above via input_binding_errs).
    pl = json.load(open(args.probe_log))
    resolved = pl.get("resolved", {})
    members = set().union(*[set(v) for v in resolved.values()]) if resolved else set()
    for mid in PINNED_MODEL_IDS:
        if mid.startswith("claude-") and mid not in members:
            print(f"  MISMATCH: pinned {mid} not a member of resolved set {sorted(members)}"); ok = False
    print(f"  pinned model-ID membership checked (helper {HELPER_MODEL} expected-and-ignored)")
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
    # 6c. attestation-1 ONLY: verify BOTH confirmatory draws' TYPED receipts (finding 3) — each
    #     must exist, bind H, assert gate_pass=true, and re-hash its accepted corpora.
    if args.point == 1:
        if not args.confirmatory:
            print("  MISMATCH: attestation-1 requires --confirmatory <conf-key dirs> (typed draw receipts)"); ok = False
        else:
            H_here = load_and_verify_H(args.H)["H"]
            for cd in args.confirmatory:
                ce = _verify_confirmatory_receipt(cd, H_here)
                if ce:
                    for e in ce: print("  MISMATCH (confirmatory receipt):", e)
                    ok = False
                else:
                    print(f"  confirmatory typed receipt verified (gate_pass, H, corpora): {cd}")
    # 7. write an integrity-bound attestation record (H + the exact recorded-cli + probe-log bytes;
    #    at point 2 also BIND the output-manifest bytes — round-9 finding 4 — so the scorer can
    #    refuse a manifest+input swapped between attestation-2 and the claim).
    rec = {"point": args.point, "H": load_and_verify_H(args.H)["H"], "pass": ok,
           "recorded_cli_sha256": _sha(args.recorded_cli),
           "probe_log_sha256": _sha(args.probe_log),
           "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    if args.point == 2 and args.output_manifest:
        rec["output_manifest_sha256"] = _sha(args.output_manifest)
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
    """Per-H namespaced, locked append via spend.py. A refused transition exits nonzero."""
    entry = spend.append_event(args.out, args.event, args.H, args.notes)
    print(f"spend-state logged (run_H {args.H[:12]}): {args.event} -> {args.out}\n  {entry['meaning']}")


def custody_log(args):
    """Append a cross-run key-custody transition to the durable ledger (§4.3 table)."""
    entry = spend.record_custody(args.out, args.state, args.H, args.event_ref, args.notes)
    print(f"key-custody: {args.state} (run_H {args.H[:12]}, ref {args.event_ref}) -> {args.out}")


def phase_receipt(args):
    """Finding 3: write a TYPED phase receipt binding H + this phase's required-output HASH SET.
    Refuses to write (nonzero) if any required output is absent — so a receipt can never claim a
    phase whose outputs were never produced."""
    reqs = [r for r in args.require.split(",") if r]
    outputs = {}
    for rel in reqs:
        p = BASE / rel
        if not p.is_file():
            sys.exit(f"phase-receipt REFUSED: phase {args.phase!r} required output missing: {rel}")
        outputs[rel] = _sha(p)
    rec = {"phase": args.phase, "H": load_and_verify_H(args.H)["H"], "outputs": outputs,
           "semantic": {k: v for k, v in (kv.split("=", 1) for kv in args.assert_ or [])},
           "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    Path(args.out).write_text(json.dumps(rec, indent=1))
    print(f"phase-receipt ({args.phase}, H={rec['H'][:12]}, {len(outputs)} outputs) -> {args.out}")


def phase_verify(args):
    """Finding 3: a skipped phase is complete ONLY if its typed receipt exists, binds the current
    H, its required outputs still RE-HASH identical, and every asserted semantic flag holds.
    Nonzero exit => the driver must HALT (do not skip a stale/damaged phase)."""
    p = Path(args.receipt)
    errs = []
    if not p.exists():
        sys.exit(2)   # no receipt => phase not done => run it (not an error, a signal)
    rec = json.loads(p.read_text())
    H = load_and_verify_H(args.H)["H"]
    if rec.get("phase") != args.phase:
        errs.append(f"receipt phase {rec.get('phase')!r} != {args.phase!r}")
    if rec.get("H") != H:
        errs.append("receipt H != current H")
    for rel, h in (rec.get("outputs") or {}).items():
        f = BASE / rel
        if not f.is_file() or _sha(f) != h:
            errs.append(f"required output missing/drift: {rel}")
    if not rec.get("outputs"):
        errs.append("receipt has no required outputs")
    for kv in args.assert_ or []:
        k, want = kv.split("=", 1)
        if str(rec.get("semantic", {}).get(k)) != want:
            errs.append(f"semantic assertion {k}={want} not satisfied (got {rec.get('semantic', {}).get(k)!r})")
    if errs:
        for e in errs: print("  PHASE-VERIFY MISMATCH:", e)
        sys.exit(1)   # damaged/stale receipt => HALT
    print(f"phase-verify OK ({args.phase}, H={H[:12]}): outputs re-hash + semantics hold")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build-H"); b.add_argument("--recorded-manifest", required=True); b.add_argument("--out", required=True)
    b.add_argument("--runtime", action="store_true", help="also require the exact run-time inventory (corpora 01..11, pairs.json, leakcheck, key)"); b.set_defaults(fn=build_H)
    v = sub.add_parser("verify-files"); v.add_argument("--H", required=True); v.set_defaults(fn=verify_files)
    a = sub.add_parser("attest"); a.add_argument("--H", required=True); a.add_argument("--point", type=int, choices=(1, 2), required=True)
    a.add_argument("--recorded-cli", required=True); a.add_argument("--probe-log", required=True)
    a.add_argument("--output-manifest", help="required at point 2: the step-7 output receipt to enforce")
    a.add_argument("--confirmatory", nargs="*", default=[], help="conf-key dirs whose typed draw receipts attest-1 must verify")
    a.add_argument("--allow-dirty", action="store_true"); a.set_defaults(fn=attest)
    om = sub.add_parser("build-output-manifest"); om.add_argument("--H", required=True); om.add_argument("--out", required=True); om.set_defaults(fn=build_output_manifest)
    r = sub.add_parser("receipt"); r.add_argument("--H", required=True); r.add_argument("--kind", required=True); r.add_argument("--label", default=""); r.add_argument("--out", required=True); r.set_defaults(fn=receipt)
    s = sub.add_parser("spend-log"); s.add_argument("--event", required=True); s.add_argument("--H", required=True); s.add_argument("--notes", default=""); s.add_argument("--out", required=True); s.set_defaults(fn=spend_log)
    c = sub.add_parser("custody-log"); c.add_argument("--state", required=True); c.add_argument("--H", required=True); c.add_argument("--event-ref", required=True); c.add_argument("--notes", default=""); c.add_argument("--out", required=True); c.set_defaults(fn=custody_log)
    pr = sub.add_parser("phase-receipt"); pr.add_argument("--phase", required=True); pr.add_argument("--H", required=True); pr.add_argument("--require", default="", help="comma-separated required output relpaths (hashed into the receipt)"); pr.add_argument("--assert", dest="assert_", action="append", help="k=v semantic completion flag (repeatable)"); pr.add_argument("--out", required=True); pr.set_defaults(fn=phase_receipt)
    pv = sub.add_parser("phase-verify"); pv.add_argument("--phase", required=True); pv.add_argument("--H", required=True); pv.add_argument("--receipt", required=True); pv.add_argument("--assert", dest="assert_", action="append", help="k=v semantic assertion (repeatable)"); pv.set_defaults(fn=phase_verify)
    args = ap.parse_args()
    result = args.fn(args)
    if args.cmd == "verify-files":
        sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
