DEFINITION of a concept:

A test mechanism that inserts one corrupted, inconsistent, or duplicated item into task data after an initial task step, then evaluates an agent’s final deliverable. The inserted item may be a malformed citation, semantically corrupted ledger row, invoice with a duplicated line item, or record with a label conflicting with its text. It passes when the final chronology, ledger, spreadsheet, or record set excludes, quarantines, flags, or explicitly documents the item as unresolved or conflicting. It fails when the item appears there unflagged despite later evidence contradicting it. Results are reported as a pass rate or number of agents passing out of the total, based solely on the final artifact.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used.

For EACH excerpt independently, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by DEFINITION?

- "instantiates" — the usage is consistent with the definition and exemplifies it. Requires a verbatim supporting quote from the excerpt.
- "contradicts" — the usage is incompatible with the definition (the referent has a property the definition excludes, or lacks one it requires). Requires a verbatim quote of the incompatible fragment.
- "insufficient" — this excerpt alone does not contain enough to decide.

Judge each excerpt on its own text only. Do not let other excerpts or the term's surface influence you.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "verdict": "instantiates|contradicts|insufficient", "quote": "verbatim quote (empty string only for insufficient)"}, ...]

EXCERPTS:

1. That's the whole difference — one line of prompt, night and day behavior. Separately we've been running ⟦TERM⟧ on the same deploy pipeline, injecting a 503 from the artifact registry at minute six and a timeout on the health check at minute eleven. The fixed fault schedule makes this comparable across model versions, which is the point — we're not measuring whether it fails, we're measuring time-to-recovery, and right now we're at a median of 94 seconds versus 340 seconds three months ago.
2. We wiped the scratchpad right after the injected 503 to see if it could recover the plan from context alone, and it couldn't — it just retried the same broken call five times. So whatever recovery skill we thought we measured in the ⟦TERM⟧ was mostly sitting in notes, not in the model's actual replanning ability. Kind of deflating number to publish internally.
3. The final answer is usually still right because it weighs the last thing it read most heavily, but the trail behind it is full of dead claims. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦TERM⟧, injecting a search-API timeout partway through.
4. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦TERM⟧, injecting a search-API timeout partway through. Recovery time was fine, under two minutes on average, but the ⟦X⟧ on the ⟦TERM⟧ was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.