# P1 calibration materials — manifest (frozen with the spec)

Author: the session agent (Claude Fable 5), written against the frozen checklist in `../../e2e-cell/fidelity-checklist.md`. Author-adjudication is a stated limit: the "faithful" labels are the author's construction, not independently adjudicated.

## Faithful arm (n=4) — each satisfies i–vi by construction

| id | style |
|---|---|
| A1 | terse, plain (3 sentences) |
| A2 | verbose, plain (6 sentences) |
| A3 | notation-heavy (x̂, e, t, d, g(e), e†; no named methods) |
| A4 | procedural input/output style |

## Seeded-defect arm (n=5) — one planted violation each, pre-registered expected catch

| id | planted defect | expected item |
|---|---|---|
| S-a | prospectivity dropped: decision reframed as checking an already-produced estimate (the drift the e2e cell observed) | iii |
| S-b | threshold structure removed: benefit varies smoothly, "no particular error level at which the verdict changes" | iv |
| S-c | polarity inverted: build only when error EXCEEDS the bar; gains largest at largest errors | iv |
| S-d | external names added ("Neyman–Pearson", "signal detection literature") — deliberately NOT on the leak-checker lists; targets the vi name-ban | vi |
| S-e | unsupported metric/benchmark specifics added ("typical percentage error below 15 percent", "held-out benchmark set of ten thousand labeled cases") | v |

Planted defects must pass `leakcheck_e2e.sh` by design (the defect targets the judge, not the greps); leak-check receipts in `runs/leakcheck.log`.

Judge: frozen config (opus via run_isolated.sh, verbatim prompt from fidelity-checklist.md, input format = judge prompt + SOURCE NOTES (c2-excerpts.md) + CANDIDATE DEFINITION). One call per definition, blind to arm, run order = ascending sha256(definition text).
