You are given research notes describing a concept a project uses. Write a short, self-contained, operational definition of that concept as used in the notes — what kind of thing it names, its inputs and outputs, what it asserts, and when it applies — in 3 to 6 sentences.

Constraints: use only ordinary plain-English words plus simple notation. Do NOT use any names of people, fields, disciplines, methods, or acronyms. Do NOT reuse any specialized term the notes use as the project's own label for the concept. Return only the definition text, nothing else.

The definition must additionally preserve each of these structural commitments:
1. There must be a fixed "do nothing" baseline — an estimate is judged against the value of having no estimate at all, not merely against a perfect one.
2. Quality must be measured on a continuous scale, so that "how good" is a matter of degree, not a single pass/fail check.
3. The benefit gained from using the estimate must shrink smoothly as its error grows, rather than staying flat until some fixed point.
4. There must exist a specific error level beyond which the estimate stops being merely less useful and turns actively harmful — worse than having nothing.
5. The harm past that level must come from the estimate manufacturing false confidence, not simply from its numbers being off.
6. The bar for "good enough" must be statable and checkable on its own, before anyone knows whether a particular candidate estimate meets it.

NOTES:
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

