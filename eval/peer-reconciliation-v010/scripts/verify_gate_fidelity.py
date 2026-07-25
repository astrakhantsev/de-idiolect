#!/usr/bin/env python3
"""verify_gate_fidelity.py — prove that the v0.10 controller carries the GATES (mechanical
validators, leak check, semantic-conformance validator, polarity validator, the whole
verification/aggregation/composition layer) AND the module-level globals/imports those gates
depend on UNCHANGED — byte-identical — from the frozen v0.9 source.

Hardened per the adversarial review:
  (a) REFERENCE BINDING: the _reference copies are hash-verified against the RECORDED hashes
      in the committed frozen record `../peer-reconciliation-test3/freeze-manifest.txt` BEFORE
      any comparison, and _reference must contain EXACTLY the bound files — so altering a
      reference to match a changed gate is caught (its hash no longer matches the frozen record).
  (b) DEPENDENCY COVERAGE: the comparison is not just FunctionDef bodies — it also compares
      every module-level GLOBAL present in both files (VERDICT_ENUM, SENT, N_SAMPLE, MASK,
      HARD_MATCH, …) and the import statements, so changing a global that a carried gate reads
      (without touching the function text) is caught. Only VERSION is allowed to differ; the
      9 hardened functions are the only functions allowed to differ.
  (c) This script is itself in attest.py's H inventory (scripts/*.py).

Exit 0 = fidelity holds; nonzero = a supposedly-unchanged gate/global/import drifted, a
supposedly-changed function is identical (a lost hardening lever), or a reference file fails
its recorded-hash binding.
"""
import ast, sys, hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NEW = BASE / "smoke_v010.py"
REF_DIR = BASE / "_reference"
RECORDED_MANIFEST = BASE / ".." / "peer-reconciliation-test3" / "freeze-manifest.txt"

# each _reference file bound to a RECORDED name in the frozen test3 freeze-manifest
REFERENCE_BINDINGS = {"smoke_v09_frozen.py": "smoke.py", "v09_frozen.py": "v09.py"}
SMOKE_REF = REF_DIR / "smoke_v09_frozen.py"

# the ONLY functions allowed to differ from v0.9 (the hardening levers + answer-blind read)
CHANGED = [
    "load_pairs", "_route_fail", "gen_call_row", "_gen_attempt_state",
    "prompts_checklist", "prompts_def", "gate_checklists", "gate_ladders", "prompts_conformance",
]
# Intentional, DOCUMENTED non-gate structural changes (enumerated so the proof still catches
# any UNLISTED drift — e.g. a mutated VERDICT_ENUM — rather than papering over). Each is a
# refactor, not a gate-behavior change:
#   score/is_correct/compose -> MOVED OUT of the controller to scorer_v010.py (score/is_correct)
#     and v010.py (compose): scoring is the sole key-bearing component's job. Not gates.
#   main -> the subcommand dispatch table (removed the moved commands). Not a gate.
ALLOWED_MOVED_OUT = {"score", "is_correct", "compose"}
ALLOWED_NONGATE_DIFFER = {"main"}
# module-level globals allowed to differ / be removed (by target-name-set):
#   VERSION differs ("v0.8"->"v0.10"); KEYF removed (-> PAIRS_MANIFEST, the answer-blind read,
#   reflected in load_pairs ∈ CHANGED); GATEF was a dead `None` sentinel, removed.
ALLOW_DIFFER_GLOBALS = [frozenset({"VERSION"})]
ALLOWED_REMOVED_GLOBALS = [frozenset({"KEYF"}), frozenset({"GATEF"})]


def _recorded_hashes(path):
    rec = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if "  " not in line:
            continue
        h, rel = line.split(None, 1)
        if len(h) == 64 and all(c in "0123456789abcdef" for c in h.lower()):
            rec[Path(rel.strip()).name] = h.lower()   # key by basename (smoke.py, v09.py)
    return rec


def verify_reference_binding():
    """(a) bind every _reference file to the committed frozen record; refuse on absence/mismatch
    or any extra unbound file in _reference."""
    errs = []
    if not RECORDED_MANIFEST.exists():
        return [f"frozen record missing: {RECORDED_MANIFEST}"]
    rec = _recorded_hashes(RECORDED_MANIFEST)
    present = {p.name for p in REF_DIR.glob("*.py")}
    extra = present - set(REFERENCE_BINDINGS)
    if extra:
        errs.append(f"_reference has UNBOUND file(s) {sorted(extra)} — every reference must bind "
                    f"to a recorded hash")
    for ref_name, recorded_name in REFERENCE_BINDINGS.items():
        f = REF_DIR / ref_name
        if not f.exists():
            errs.append(f"reference missing: {ref_name}"); continue
        want = rec.get(recorded_name)
        if want is None:
            errs.append(f"no recorded hash for {recorded_name} in {RECORDED_MANIFEST.name}"); continue
        got = hashlib.sha256(f.read_bytes()).hexdigest()
        if got != want:
            errs.append(f"reference {ref_name} sha {got[:12]} != recorded {recorded_name} {want[:12]}")
    return errs


def _module_parts(path):
    src = Path(path).read_text()
    tree = ast.parse(src)
    funcs, globals_, imports = {}, {}, []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            funcs[node.name] = ast.get_source_segment(src, node)
        elif isinstance(node, ast.Assign):
            names = frozenset(t.id for t in ast.walk(node) if isinstance(t, ast.Name))
            # key by the assignment's target name-set (handles tuple targets)
            tgt = frozenset(n.id for tgt in node.targets for n in ast.walk(tgt) if isinstance(n, ast.Name))
            globals_[tgt] = ast.get_source_segment(src, node)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(src, node))
    return funcs, globals_, imports


def compare_modules(new_path, ref_path):
    """Return a list of fidelity errors comparing new_path against the frozen ref_path:
    every function except the 9 CHANGED must be byte-identical; every global present in BOTH
    (by target-name-set) except ALLOW_DIFFER_GLOBALS must be byte-identical; every v0.9 import
    must appear identically in v0.10. Also asserts the 9 CHANGED functions really changed."""
    nf, ng, ni = _module_parts(new_path)
    rf, rg, ri = _module_parts(ref_path)
    errors = []
    # functions: all shared-name functions except CHANGED + the enumerated non-gate exclusions
    # must be byte-identical; CHANGED must differ.
    exempt = set(CHANGED) | ALLOWED_MOVED_OUT | ALLOWED_NONGATE_DIFFER
    for name, rsrc in rf.items():
        if name in exempt:
            continue
        if name not in nf:
            errors.append(f"[carried fn MISSING in v0.10] {name}")
        elif nf[name] != rsrc:
            errors.append(f"[carried fn DRIFTED] {name}")
    for name in CHANGED:
        if name not in nf:
            errors.append(f"[hardening fn MISSING in v0.10] {name}")
        elif name in rf and nf[name] == rf[name]:
            errors.append(f"[hardening fn NOT CHANGED — lever lost?] {name}")
    n_carried_ok = sum(1 for n, s in rf.items() if n not in exempt and nf.get(n) == s)
    n_changed_ok = sum(1 for n in CHANGED if n in nf and (n not in rf or nf[n] != rf[n]))
    # globals: present in BOTH (by target-name-set), byte-identical except the allowlists
    for tgt, rsrc in rg.items():
        if tgt in ALLOW_DIFFER_GLOBALS or tgt in ALLOWED_REMOVED_GLOBALS:
            continue
        if tgt not in ng:
            errors.append(f"[carried global REMOVED in v0.10] {sorted(tgt)}")
        elif ng[tgt] != rsrc:
            errors.append(f"[global DRIFTED] {sorted(tgt)}")
    n_global_ok = sum(1 for tgt, s in rg.items()
                      if tgt not in ALLOW_DIFFER_GLOBALS and tgt not in ALLOWED_REMOVED_GLOBALS
                      and ng.get(tgt) == s)
    # imports: every v0.9 import statement must appear identically in v0.10 (additions allowed)
    for imp in ri:
        if imp not in ni:
            errors.append(f"[carried import MISSING/ALTERED in v0.10] {imp!r}")
    return errors, {"carried_fn_ok": n_carried_ok, "changed_fn_ok": n_changed_ok,
                    "global_ok": n_global_ok, "imports_checked": len(ri)}


def main():
    errs = verify_reference_binding()
    if errs:
        print("GATE-FIDELITY FAILED (reference binding):")
        for e in errs: print("  -", e)
        sys.exit(1)
    errors, stats = compare_modules(NEW, SMOKE_REF)
    if errors:
        print("GATE-FIDELITY FAILED:")
        for e in errors: print("  -", e)
        sys.exit(1)
    print(f"GATE-FIDELITY OK: reference bound to frozen record; "
          f"{stats['carried_fn_ok']} carried functions + {stats['global_ok']} module globals "
          f"byte-identical to frozen v0.9, {stats['imports_checked']} imports carried; "
          f"{stats['changed_fn_ok']}/{len(CHANGED)} hardening functions confirmed changed.")


if __name__ == "__main__":
    main()
