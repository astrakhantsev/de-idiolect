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

# count terminal artifact-gate failures among the 40 generation artifacts (§4.1 numerator).
# A checklist configFail (chk) means prompts_def NEVER created its ladder — that ladder can
# never pass, so it counts as a FAILED artifact too: numerator += 2 for one exhausted
# checklist (the checklist AND its never-created ladder). A ladder configFail counts +1.
# Denominator is fixed at 40 (20 checklists + 20 ladders).
python3 - "$H" <<'PY'
import json, sys
st = json.load(open("runs/gate-state.json"))
chk_cf = sorted(k for k, a in st["artifacts"].items() if a["kind"] == "chk" and a["state"] == "configFail")
lad_cf = sorted(k for k, a in st["artifacts"].items() if a["kind"] == "lad" and a["state"] == "configFail")
n = 2 * len(chk_cf) + len(lad_cf)   # +2 per exhausted checklist (chk + its phantom ladder)
detail = {"checklist_configFails": chk_cf, "ladder_configFails": lad_cf,
          "numerator": n, "denominator": 40,
          "rule": "checklist configFail counts 2 (the checklist AND its never-created ladder)"}
print(f"confirmatory draw: numerator {n}/40  (chk_cf={len(chk_cf)}x2 + lad_cf={len(lad_cf)})  {chk_cf+lad_cf}")
print(f"GATE {'PASS (<=1/40)' if n <= 1 else 'FAIL (>1/40 -> effective configuration RETIRED, §4.1)'}  H={sys.argv[1][:12]}")
detail["gate_pass"] = n <= 1; detail["H"] = sys.argv[1]
open("runs/confirmatory-result.json", "w").write(json.dumps(detail, indent=1))
sys.exit(0 if n <= 1 else 3)
PY
