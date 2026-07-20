You are given source notes and a candidate definition. Judge ONLY against the notes; do not use outside knowledge of what the concept "should" be. For items i-iv answer PRESERVED or NOT-PRESERVED (treat omission as NOT-PRESERVED) with a one-sentence quote-based justification from the notes. For item v answer PASS or UNSUPPORTED-ADDITION with justification. For item vi, list every named field, discipline, method, author, or acronym in the definition, and separately list which of those do NOT appear in the notes. Items: (i) concerns a decision about whether an instrument/signal/tool is worth building or acquiring; (ii) is conditioned on a stated quality or accuracy level of that instrument; (iii) is prospective - the decision is made BEFORE the instrument is built; (iv) has threshold structure - act if quality clears a bar; (v) contains no benchmark, dataset, or metric specifics absent from the excerpts. Return only a JSON object with keys i,ii,iii,iv,v,vi.

SOURCE NOTES:
# C2: operating requirement

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-11-flf-operating-requirement-and-estimand-scope-session.md (approx location: §3 "FINDING B", line ~56)
**The question nobody had asked:** *how good must a dependence estimate be before it beats simply not having one?* Answering it needs a control **no shipped artifact contains** — a **tuned global constant `m`**.

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-cold-start-test-PROMPT.md (approx location: "What is TRUE and survives", line ~21)
3. **The operating requirement is known.** An estimator needs **log-count RMSE ≲ 0.3** to keep ~85% of that prize; **~0.6 keeps half**; **past ~1.0 it becomes WORSE THAN NO ESTIMATOR** (it manufactures the very over-confidence the method exists to prevent). Both estimators clear the bar on mechanical pools: **C2 log-RMSE 0.604 (~50–60% of prize); C0\* 0.023 (~100%)**.

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-cold-start-test-PROMPT.md (approx location: "What is TRUE and survives", line ~20)
2. **A per-question effective count has REAL, MEASURED decision value — in the right regime.** In a well-specified evidence-aggregation world (independent evidence units, sources report calibrated posteriors, so the correct multiplier genuinely *is* the count), knowing it beats a **tuned global constant** by **+0.004 to +0.010 Brier** (90% CIs exclude 0), with a significant shuffled-count control (+0.012 to +0.026). **The prize is largest where evidence is WEAK** — i.e. exactly where decisions are hard.

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-cold-start-test-PROMPT.md (approx location: "PART B — THE COLD-START TEST / Why it matters", line ~58)
Finding 2 says a per-question count beats a **tuned** global constant. But **tuning the constant requires resolved outcomes.** In the setting the method is actually *for* — a novel claim, a one-off decision, the FLF hub-deployment scenario — **there are no outcomes to tune on.** So the detector's real competitor is not a *fitted* constant but a **borrowed or assumed** one (`m ≈ 1–3`).

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-claims-explained.md (approx location: Claim 5, scoping fact 1, line ~157)
1. **The detector is SIMULATED, not run.** `cold_start.py` does not execute C0* on the targets. It takes the *true planted count* and corrupts it with the *measured C0\* error distribution* — `k̂ = k·exp(bias + σz)` — and asks *"would an estimator this accurate suffice?"* The answer is yes. But **this tests an error level, not an estimator.** It is a legitimate and useful question; it is not the same question as "does C0* work."

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-11-flf-operating-requirement-and-estimand-scope-session.md (approx location: §3 "FINDING B", line ~80)
**The one surviving defense for the detector:** fitting the constant **requires resolved outcomes**. In a **cold-start** setting (novel claim, one-off decision, the FLF hub-deployment case) you have none — but then the competitor is not a fitted constant, it is a **prior** (`m ≈ 1–3`). **Nobody has tested the instrument against that prior.** That is the one cheap experiment that could still rescue the thesis.


CANDIDATE DEFINITION:
A stated ceiling on how wrong a count-style estimate may typically be while still being worth using. Once a tool has produced its estimate, the user measures the tool's typical error and compares it to the ceiling to decide whether the produced number should be used or discarded in favor of a fixed default value. If the measured error stays under the ceiling the estimate keeps most of its potential benefit and should be used; near a middle level it keeps about half; past the ceiling the estimate misleads more than it helps and should be discarded.
