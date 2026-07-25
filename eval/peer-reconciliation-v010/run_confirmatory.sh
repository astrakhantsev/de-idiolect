#!/usr/bin/env bash
# run_confirmatory.sh <conf-key-dir> <H> — run the v0.10 TOOL PATH (generation + gates only)
# on ONE fresh confirmatory TRAIN key, counting terminal artifact-gate configFails among the
# 40 generation artifacts (20 checklists + 20 ladders). Gate = <=1 configFail/40 (§4.1). A
# failing draw RETIRES the effective configuration. DO NOT run during the build (LLM calls).
#
# Established precedent (v0.9 test3 = the frozen package COPIED verbatim per key): the
# instrument is copied into the conf-key workspace so smoke_v010's BASE-relative paths resolve
# there; corpora/pairs.json/leakcheck were built by setup_confirmatory.py. The prompts +
# controllers are byte-identical to the key-3 instrument (bound in H).
set -euo pipefail
WS="${1:?conf-key dir}"; H="${2:?H}"
SRC="$(cd "$(dirname "$0")" && pwd)"
# Capture the SOURCE workspace's isolation-runner ABSOLUTE path BEFORE any cd/copy. The
# frozen run_calls.sh resolves its runner as "<its dir>/../e2e-cell/run_isolated.sh"; once
# copied into the conf-key workspace that would resolve to runs/confirmatory/e2e-cell/... (absent),
# so we materialise the runner at that sibling location from the source. Preflight: halt now
# if the source runner is missing (never start a draw that would abort mid-call with rc=2).
ISO_SRC="$SRC/../e2e-cell/run_isolated.sh"
[ -x "$ISO_SRC" ] || { echo "PREFLIGHT HALT: isolation runner missing at $ISO_SRC"; exit 2; }
WS="$(cd "$WS" && pwd)"

# copy the frozen instrument (NOT data) into the conf-key workspace
mkdir -p "$WS/prompts" "$WS/harness" "$WS/scripts" "$WS/tests"
cp "$SRC"/smoke_v010.py "$SRC"/v010.py "$SRC"/retrieve_xc_v010.py "$SRC"/run_calls.sh "$SRC"/pin_model.py "$WS/"
cp "$SRC"/prompts/*.md "$WS/prompts/"
# make "<WS>/../e2e-cell/run_isolated.sh" resolve for the copied (frozen) run_calls.sh
mkdir -p "$WS/../e2e-cell"
cp "$ISO_SRC" "$WS/../e2e-cell/run_isolated.sh"; chmod +x "$WS/../e2e-cell/run_isolated.sh"
[ -f "$WS/pairs.json" ] || { echo "conf key missing pairs.json (run setup_confirmatory.py first)"; exit 2; }

cd "$WS"
VENVPY="$SRC/../../.venv/bin/python"
calls() { local rc=0; bash "$WS/run_calls.sh" "$1" || rc=$?; [ "$rc" -lt 2 ] || { echo "HALT rc=$rc"; exit "$rc"; }; }
gen_loop() {
  python3 smoke_v010.py "$1"; calls "runs/$3"; python3 smoke_v010.py "$2"
  for _ in 1 2; do [ -s "runs/$4" ] || break; calls "runs/$4"; python3 smoke_v010.py "$2"; done
}

# round-10 finding 5: re-verify the COMPLETE per-key setup manifest BEFORE the draw (a corrupted
# pairs.json / leakcheck / corpus / brief after setup HALTs the draw rather than silently changing it).
python3 "$SRC/setup_confirmatory.py" --verify-setup "$WS" || { echo "HALT: setup-manifest mismatch for $WS"; exit 2; }

# ---- GENERATION (the 40 artifacts the ≤1/40 qualification gate reads) ----
python3 smoke_v010.py excerpts
gen_loop prompts-checklist gate-checklists checklists/calls.tsv checklists/regen-calls.tsv
gen_loop prompts-def gate-ladders definitions/calls.tsv definitions/regen-calls.tsv
# finding 6: DRAIN ladder regens to quiescence before each conformance batch (no stranding)
while true; do
  while [ -s runs/definitions/regen-calls.tsv ]; do calls runs/definitions/regen-calls.tsv; python3 smoke_v010.py gate-ladders; done
  python3 smoke_v010.py prompts-conformance
  [ -s runs/conformance/calls.tsv ] || break
  calls runs/conformance/calls.tsv
  python3 smoke_v010.py gate-conformance
  while [ -s runs/conformance/rerun-calls.tsv ]; do calls runs/conformance/rerun-calls.tsv; python3 smoke_v010.py gate-conformance; done
done
python3 smoke_v010.py assert-resolved

# ---- ≤1/40 QUALIFICATION GATE (generation artifacts ONLY — unchanged §4.1) ----
# A checklist configFail counts 2 (the checklist AND its never-created ladder); a ladder configFail
# counts 1; denominator fixed at 40. Writes confirmatory-result.json (gate_pass + corpora, NO stages
# yet). Exit 3 (retire) on FAIL — the full tool path below runs ONLY for a qualifying draw.
GATE_RC=0
python3 - "$H" <<'PY' || GATE_RC=$?
import json, sys, hashlib
from pathlib import Path
st = json.load(open("runs/gate-state.json"))
chk_cf = sorted(k for k, a in st["artifacts"].items() if a["kind"] == "chk" and a["state"] == "configFail")
lad_cf = sorted(k for k, a in st["artifacts"].items() if a["kind"] == "lad" and a["state"] == "configFail")
n = 2 * len(chk_cf) + len(lad_cf)
corpora = {f"corpora/{s}/{i:02d}.md": hashlib.sha256(Path(f"corpora/{s}/{i:02d}.md").read_bytes()).hexdigest()
           for s in ("a", "b") for i in range(1, 12) if Path(f"corpora/{s}/{i:02d}.md").is_file()}
detail = {"checklist_configFails": chk_cf, "ladder_configFails": lad_cf,
          "numerator": n, "denominator": 40, "corpora_sha256": corpora, "gate_pass": n <= 1, "H": sys.argv[1],
          "rule": "checklist configFail counts 2 (the checklist AND its never-created ladder)"}
print(f"confirmatory draw: numerator {n}/40  (chk_cf={len(chk_cf)}x2 + lad_cf={len(lad_cf)})  {chk_cf+lad_cf}")
print(f"GATE {'PASS (<=1/40)' if n <= 1 else 'FAIL (>1/40 -> effective configuration RETIRED, §4.1)'}  H={sys.argv[1][:12]}")
open("runs/confirmatory-result.json", "w").write(json.dumps(detail, indent=1))
sys.exit(0 if n <= 1 else 3)
PY
[ "$GATE_RC" -eq 0 ] || { echo "confirmatory draw FAILED qualification -> configuration RETIRED (§4.1)"; exit 3; }

# ---- FULL TOOL PATH (round-10 finding 3): a QUALIFYING draw exercises H end-to-end (~87 calls),
#      reusing the SAME phase functions as the key-3 driver, pointed at this conf key. ----
python3 smoke_v010.py prompts-polarity; calls runs/polarity/calls.tsv; python3 smoke_v010.py gate-polarity
while [ -s runs/polarity/rerun-calls.tsv ]; do calls runs/polarity/rerun-calls.tsv; python3 smoke_v010.py gate-polarity; done
python3 smoke_v010.py alive
"$VENVPY" retrieve_xc_v010.py --v010 --no-determinism > runs/v010/retrieval-summary.txt 2>&1 \
  || { echo "CONFIRMATORY RETRIEVAL FAILED"; tail -5 runs/v010/retrieval-summary.txt; exit 1; }
python3 v010.py stage-verify; calls runs/v010/verify/calls.tsv
python3 v010.py aggregate
python3 v010.py stage-adaptive-1; calls runs/v010/symcheck/calls.tsv; calls runs/v010/decompose/calls.tsv
python3 v010.py stage-adaptive-2; calls runs/v010/containment/calls.tsv
python3 v010.py compose

# ---- finalize: embed full-draw stage-completion flags (attestation-1 re-checks they are all true) ----
python3 - <<'PY'
import json, sys
from pathlib import Path
d = json.load(open("runs/confirmatory-result.json"))
outs = {"polarity": "runs/polarity", "retrieval": "runs/v010/retrieval.json",
        "verify": "runs/v010/verify/meta.json", "aggregate": "runs/v010/agg.json",
        "adaptive1": "runs/v010/symcheck", "adaptive2": "runs/v010/containment",
        "compose": "runs/v010/verdicts.json"}
stages = {k: Path(v).exists() for k, v in outs.items()}
d["stages"] = stages
open("runs/confirmatory-result.json", "w").write(json.dumps(d, indent=1))
missing = [k for k, ok in stages.items() if not ok]
if missing:
    print(f"CONFIRMATORY FULL-DRAW INCOMPLETE — missing stage outputs: {missing}"); sys.exit(1)
print("confirmatory FULL draw complete: qualification PASS + full tool path (all stages)")
PY
