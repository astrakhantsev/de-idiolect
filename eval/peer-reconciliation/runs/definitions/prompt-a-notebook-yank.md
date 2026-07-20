Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write a short, self-contained, operational definition of the concept ⟦TERM⟧ names AS USED in these excerpts: what kind of thing it is (a phenomenon, a procedure, a score, a rule…), its inputs and outputs where applicable, what it asserts, and when it applies.

COMMITMENTS CHECKLIST (extracted from the same excerpts — the definition must state every commitment, including the specific mechanism):
- Mechanism: the scratchpad/accumulated notes are deliberately wiped (cleared) at a defined checkpoint (mid-run or multiple checkpoints) during an agent run.
- Purpose: this wiping is used to test whether the agent can recover its plan or performance from context alone, versus relying on accumulated notes.
- What is measured: post-wipe outcomes are compared against pre-wipe/expected behavior — e.g., recovery quality, performance tally, or rate of fabricated/ungrounded claims.
- Applies during active agent runs, often layered alongside other running tests (e.g., a fault-injection run or a parallel instrumentation experiment).
- Can be applied at a single checkpoint or at multiple checkpoints within one run.
- Constraint: it isolates cause from symptom by checking whether a fresh start (post-wipe) changes the observed behavior — if the behavior persists unchanged, the excerpts treat this as evidence the behavior is a base property of the model rather than something stored in accumulated notes.

Constraints:
- Ordinary words and simple notation only.
- Do NOT use the masked terms or guess at them; do not use names of people, published methods, fields, systems, models, or communities.
- Base the definition ONLY on what the excerpts support; do not import outside assumptions.
- Do NOT add generalizing catch-all phrases (such as "or otherwise", "or any similar", "in any way", "or by other means") beyond what the excerpts support — state the specific mechanism, not its genus.
- 60–160 words. Output ONLY the definition text, nothing else.

EXCERPTS:

1. The fixed fault schedule makes this comparable across model versions, which is the point — we're not measuring whether it fails, we're measuring time-to-recovery, and right now we're at a median of 94 seconds versus 340 seconds three months ago. The thing nobody warned me about: combine a pothole run with a ⟦TERM⟧ and the agent basically falls apart. We wiped the scratchpad right after the injected 503 to see if it could recover the plan from context alone, and it couldn't — it just retried the same broken call five times.
2. Nothing to do with capability, everything to do with instrumentation contention. We only caught it because of a ⟦TERM⟧ experiment we were running in parallel — wiped the scratchpad at three checkpoints to measure how much of the performance was sitting in accumulated notes. The yanked runs recovered worse than expected, and when we went looking for why the recovery slope was so steep, we found the timing artifact instead.
3. Not a huge sample but the correlation was strong enough that we're now treating "does it ask for missing things" as a rough proxy for "does it maintain honest internal state." We tried to isolate cause versus symptom with a ⟦TERM⟧, wiping notes at the halfway point to see if a fresh start improved the tally for the fabricating agents. It didn't — they just fabricated a new set of ungrounded claims to fill the gap instead of recovering cleanly, so whatever's driving the fabrication doesn't seem to live in the accumulated notes, it's more a base behavior of the model itself.