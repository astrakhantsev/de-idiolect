You have no tools. Work only from the text below. Reply with exactly the four definitions in the format specified — no preamble, no commentary.

Below are excerpts from a private project's working documents describing four project-local concepts (C1–C4). For EACH concept, write one detailed, standalone operational definition (150–250 words) that a person with no project context could fully understand. Plain language plus simple mathematical notation where helpful.

Each definition must state: what the object IS (a quantity, a specification, a claim, or a procedure), its inputs and outputs, what it quantifies or asserts precisely, and under what conditions it applies.

HARD CONSTRAINTS on every definition:
- Do NOT use the project's own names for the concepts (write "this quantity", "this claim", "this procedure" instead).
- No proper names of people, methods, theorems, or papers. No citations. No names of academic fields.
- Do NOT speculate about what the concept "is called" elsewhere or where it comes from. Definition only.
- Abstract away the specific application domain: where the excerpts speak of AI models, language-model judges, or graders, write generically of "evaluators" or "raters" scoring "items". The definition should read as a general statistical/procedural object, not as an AI-specific one.
- Use only common vocabulary a first-year science student would know, plus standard mathematical notation.

OUTPUT FORMAT, exactly:

CONCEPT-1:
<definition>

CONCEPT-2:
<definition>

CONCEPT-3:
<definition>

CONCEPT-4:
<definition>

THE EXCERPTS FOLLOW.

# C1: m*

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-claims-explained.md (approx location: "First: the one idea everything hangs off", lines ~28-39)
The machinery is one line. You start with a prior `π₀`, each source contributes some evidence lean `Dᵢ` (how hard it pushes toward or away from the claim, measured in log-odds), and you combine them:

```
logit(p̂) = logit(π₀) + m · D̄
```

where `D̄` is the average lean and `m` is the multiplier you apply to it.

- `m = N` (say 12) is what a naive reader does. "Twelve reviews agree!"
- `m = 1` is maximal skepticism: *the entire corpus is one collective witness.* (At `m = 1` the prior cancels and you get the ordinary log-odds pool.)

**⚠ CORRECTED — and this correction is foundational, so get it right now rather than later.** It is *very* tempting to call `m` "the number of independent witnesses." **It is not.** `m` is an **extremization multiplier** — a knob that sharpens or softens your aggregate. It is *proportional to the number of independent evidence units* **only in the calibrated evidence-aggregation regime** (the synthetic positive control, where the world is built so that it is). **Everywhere else it has no count semantics at all.**

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-claims-explained.md (approx location: "First: the one idea everything hangs off", lines ~43-49)
One more piece, and then everything else is a comment on it. You have some decision threshold `t` (say, "I'll call it settled if I'm 80% confident"). There's a critical `m` at which your verdict flips from *open* to *settled* — call it `m*`. It has a closed form:

```
m* = need / D̄        where    need = logit(t) − logit(π₀)
```

**Read that formula until it's boring, because ten of the twelve claims below are statements about it.** `need` is "how much evidence do I need to be convinced" — it's built from your *conventions* (your prior, your threshold). `D̄` is "how much evidence do I actually have" — it's built from the *data*. And `m*` is the ratio.

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-claims-explained.md (approx location: Claim 3, line ~118)
**What `m` actually is:** an **extremization coefficient.** A knob that sharpens (`m > 1`) or softens (`m < 1`) your aggregate probability. It absorbs *everything* — genuine dependence, yes, but also over-confidence, miscalibration, the shared-signal confound from claim 2, the lot. It's a volume knob on a stereo, not a count of the people in the room.

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-claims-explained.md (approx location: Claim 11 "m* is a ratio", lines ~253-259)
**Go back to the formula:** `m* = need / D̄`.

You swept `need` obsessively. Forty-five different settings: three harm boundaries × five priors × three thresholds. Every convention in the **numerator**, varied and reported. Beautiful.

**You swept the denominator zero ways.**

And here's what `D̄` is made of. Each review reports an effect with a **95% confidence interval**. You turn that interval into a standard error, and then the evidence weight goes as **`D ∝ 1/SE²`.** Inverse *square*. **The denominator is the most leveraged input in the entire system**, and it was the one nobody touched.

## excerpt
source: /mnt/f/hub/10_projects/minelit/flf/2026-07-12-flf-claims-explained.md (approx location: Claim 4, line ~128)
Fair. So you asked the decision-level version: **for how many real questions does your dependence assumption change the *verdict*?** Not "does the probability move a bit" — does it cross the line from *open* to *settled*?

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

# C3: signal-not-cut

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-decision-transplant-digest.md (approx location: §0 "Design freeze / Frozen directional readings", line ~19)
**Frozen directional readings (verbatim):** D1 "coupling-failure supported" = transplant J exceeds integrated J by ≥0.10 (point, exploratory); D1 "gate-policy bottleneck" = agreement high and J unchanged (operationalized at freeze: verdict-agreement ≥0.80 AND |ΔJ| < 0.10); D3 "decision subtracts value from own credences" = rule J exceeds free J by ≥0.10 on the 80 AND the direction reproduces on the TRAIN-70.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-decision-transplant-digest.md (approx location: §4 "Three-way mechanistic verdict", line ~104)
- **Miscalibrated-threshold-over-real-credences: fails the one frozen operational test.** The 0.2 rule gains nothing on the 80 and loses 0.139 on first-use items; the post-hoc split-slice sweep (§3.2) finds no fixed τ that transfers. Descriptively the decision stage IS a threshold policy over the stated credences (TE ≈ 1.0, in-sample); what fails is the claim that re-thresholding those credences recovers the externally-recoverable value. Conclusions are restricted to the tested rule and sweep; no claim about untested gate families (e.g. per-stratum or feature-conditional thresholds).

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-decision-transplant-digest.md (approx location: §4 "Leading remaining hypothesis", line ~105)
- **Leading remaining hypothesis (residual; untested by any manipulation here — review finding 2):** the loss sits in the CREDENCE LEVEL — the p mass assigned to second readings — which today runs low enough that consistent gates over it (the model's own, or any fresh decider's, in either family) reproduce the strict post-shift operating point even over pre-shift-rich elements (D1.2, D2.2, D3.3). Consistent with, not established by, this leg: no pre-shift S-conf credence distribution exists to compare against, and no cell manipulates credences. The falsifying follow-up is a credence-level probe: the same S-conf contract across a regime boundary (or the request-capture proxy), watching p2 distributions rather than hedge rates.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-decision-transplant-digest.md (approx location: §3 "D3 mechanical-from-own-confidences", reading 3, line ~85)
3. **Generation stays rich while the gate stays strict — in the same call.** d3Opus emits multi-reading sets on 0.775 of ambiguous items (mean |S| 1.637 ≈ S-arm r1's 1.654) yet free-hedges only 0.350 of them; its free operating point (0.350, 0.125) again matches the post-shift gate family. The dissociation the regime shift exposed — rich elements, strict gate — is visible WITHIN one call here, now with credences attached: the verbal elements are rich while the numeric probability mass on second readings runs low (p2 below ~0.33 on most ambiguous items today). Whether that p2 mass is what the regime shift moves is the §4 residual hypothesis, not an observation — no pre-shift S-conf credence distribution exists.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-decision-transplant-digest.md (approx location: §5 "What this does to the practical recipe", line ~109)
The split-slice sweep (§3.2) found no fixed re-thresholding of the stated credences that transfers out-of-sample; conclusions are restricted to the tested rule/sweep.

# C4: read-the-enumerations

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-enumeration-layer-digest.md (approx location: §0 "Frozen definitions", line ~17)
- **Emitted set S(config, item):** if the config hedged → the deduplicated set of labels attached to its enumerated readings (asserted identical to the recorded `label_set` on every hedged A5 row); if it committed → the singleton {committed label}. A5-affordance configs only.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-enumeration-layer-digest.md (approx location: §4 "Mechanical selector prototypes", line ~141)
The honest claim is existence, not effect size: simple frozen rules over already-emitted sets recover ≥ best-single accuracy at response rate 1.0 where the committed-vote panel loses 0.200 to its own best member.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-enumeration-layer-digest.md (approx location: §5 "Verdict", line ~145)
On the frozen primary endpoint, the correlated component of judge error sits in what the models offer up for consideration, not only in how the commit policy gates it

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-enumeration-layer-digest.md (approx location: §9 "For the orchestrator", item 2, line ~189)
For single-label accuracy over these unions, the commit stage, not the enumeration stage, is where the panel's information dies — consistent with the atlas's 7/7 containment.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-set-arm-digest.md (approx location: §0 "Design freeze / S-arm contract", line ~17)
the task is to emit the SET of labels with defensible readings, one `LABEL (<e|n|c>): <one-sentence paraphrase>` line per label, singleton if only one reading is defensible, explicit do-not-pad clause. No hedge gate exists in the contract.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/2026-07-15-examples-anthology.md (approx location: line 440, item note)
*Note:* The A5 transcript names the c-reading, hand-writes its own cancellation test, and commits n; the X-arm (and both plain S-arm opus runs, which emitted {c,n}) shows the reading was available all along — the gate, not the recognizer, was the bottleneck. This is the mechanism behind the atlas's "pragmatics license test" fix hypothesis.

## excerpt
source: /mnt/f/hub/10_projects/minelit/judge-dependence/digests/2026-07-15-cq4-blindspot-enumeration-digest.md (approx location: §0 "Design freeze / Arms", line ~16)
exhaustive-enumeration, set-style output (`READING <k> (<e|n|c>): <paraphrase>`; **no single-label commit ask** — the enumeration IS the answer, no `LABEL:` line

