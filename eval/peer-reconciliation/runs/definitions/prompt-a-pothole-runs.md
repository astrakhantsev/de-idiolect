Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Injects a specific fault (e.g., a 503 from a service, a timeout) into a running task/pipeline at a predetermined point to test recovery.
- Uses a fixed fault schedule/injection timing so runs are comparable across model versions or task types.
- Measures time-to-recovery (not whether failure occurs), reported as e.g. median seconds to recover.
- Applies during an active task or pipeline run (e.g., a deploy pipeline or multi-step task), triggered by the injected fault partway through execution.
- Recovery must come from the model's own replanning ability, not from external scratchpad/notes carried over from before the injection.
- Can be run alongside a check of the trail/notes quality (e.g., rate of unreconciled or unverified claims) produced during the recovery process, not just the final answer's correctness.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. That's the whole difference — one line of prompt, night and day behavior. Separately we've been running ⟦TERM⟧ on the same deploy pipeline, injecting a 503 from the artifact registry at minute six and a timeout on the health check at minute eleven. The fixed fault schedule makes this comparable across model versions, which is the point — we're not measuring whether it fails, we're measuring time-to-recovery, and right now we're at a median of 94 seconds versus 340 seconds three months ago.
2. We wiped the scratchpad right after the injected 503 to see if it could recover the plan from context alone, and it couldn't — it just retried the same broken call five times. So whatever recovery skill we thought we measured in the ⟦TERM⟧ was mostly sitting in notes, not in the model's actual replanning ability. Kind of deflating number to publish internally.
3. The final answer is usually still right because it weighs the last thing it read most heavily, but the trail behind it is full of dead claims. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦TERM⟧, injecting a search-API timeout partway through.
4. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦TERM⟧, injecting a search-API timeout partway through. Recovery time was fine, under two minutes on average, but the ⟦X⟧ on the ⟦TERM⟧ was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.