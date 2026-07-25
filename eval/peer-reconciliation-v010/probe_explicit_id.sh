#!/usr/bin/env bash
# probe_explicit_id.sh — the explicit-ID model probe (v0.10 prereg §6, custody step 3).
# DO NOT run this during the build (it makes LLM calls). It is invoked ONCE at run time,
# after freeze + build-H, BEFORE any generation. Membership failure aborts pre-generation.
#
# Opus 5 released 2026-07-24 and is expected to drift the `opus` alias; the primary defense
# is invoking every Claude model by EXPLICIT pinned ID. This probe is the sanity assert:
# invoke claude-opus-4-8 and claude-sonnet-5 DIRECTLY (2 probe calls) and check the CLI's
# reported resolved-model set CONTAINS the pinned ID (the resolved_model[...] field the v0.9
# freeze recorded). Helper id claude-haiku-4-5-20251001 is expected-and-ignored. Codex uses
# a pinned id (gpt-5.6-terra) — no alias probe needed.
#
# Writes runs/probe-log.json = {"resolved": {"claude-opus-4-8":[...], "claude-sonnet-5":[...]},
# "membership_ok": bool, ...}. attest.py reads this at both attestation points.
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"
OUT="$BASE/runs/probe-log.json"
mkdir -p "$BASE/runs"

th="$(mktemp -d)"; mkdir -p "$th/.claude"
cp "$HOME/.claude/.credentials.json" "$th/.claude/.credentials.json"
trap 'rm -rf "$th"' EXIT

probe() {  # $1 = pinned model id
  local mid="$1"
  ( cd "$(mktemp -d)" && HOME="$th" claude -p 'Reply with exactly: OK' --model "$mid" --output-format json 2>/dev/null ) \
    | python3 -c 'import json,sys
d=json.load(sys.stdin); u=d.get("modelUsage") or {}
print(",".join(sorted(u)) if u else d.get("model","unrecorded"))'
}

declare -A resolved
ok=1
for mid in claude-opus-4-8 claude-sonnet-5; do
  set_str="$(probe "$mid" || echo unrecorded)"
  resolved["$mid"]="$set_str"
  case ",$set_str," in
    *,"$mid",*) echo "MEMBERSHIP OK: $mid in [$set_str]" ;;
    *) echo "MEMBERSHIP FAIL: $mid NOT in [$set_str]"; ok=0 ;;
  esac
done

python3 - "$OUT" "$ok" "${resolved[claude-opus-4-8]:-}" "${resolved[claude-sonnet-5]:-}" <<'PY'
import json,sys
out, ok, opus, sonnet = sys.argv[1], sys.argv[2]=="1", sys.argv[3], sys.argv[4]
json.dump({"resolved": {"claude-opus-4-8": [x for x in opus.split(",") if x],
                         "claude-sonnet-5": [x for x in sonnet.split(",") if x]},
           "helper_expected_and_ignored": "claude-haiku-4-5-20251001",
           "codex_model": "gpt-5.6-terra (pinned id)",
           "membership_ok": ok}, open(out,"w"), indent=1)
print(f"probe-log -> {out}  membership_ok={ok}")
PY
[ "$ok" = 1 ] || { echo "PROBE FAILED — abort pre-generation (§4.3)"; exit 3; }
