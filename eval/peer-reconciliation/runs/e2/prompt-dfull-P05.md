Two communities each use their own term for practices that may be related. Below are usage excerpts from community 1 (term masked ⟦T1⟧) and community 2 (term masked ⟦T2⟧).

Produce three artifacts:
1. "core" — in ordinary words (60–120), the largest SPECIFIC common core practice/phenomenon that BOTH sets of excerpts genuinely support. Must be more specific than generic evaluation practice ("testing agents", "measuring quality" do NOT count).
2. "residue_1" — what community 1's usage commits to that community 2's does NOT (in ordinary words, 20–60).
3. "residue_2" — what community 2's usage commits to that community 1's does NOT (20–60).

Each artifact needs a verbatim supporting quote: "quote_core_1" and "quote_core_2" (one from each community supporting the core), "quote_residue_1" (from community 1), "quote_residue_2" (from community 2).

If there is no genuine specific common core, output exactly: ABSTAIN

Otherwise output ONLY JSON:
{"core": "...", "quote_core_1": "...", "quote_core_2": "...", "residue_1": "...", "quote_residue_1": "...", "residue_2": "...", "quote_residue_2": "..."}

COMMUNITY 1 EXCERPTS:
1. That's the whole difference — one line of prompt, night and day behavior. Separately we've been running ⟦T1⟧ on the same deploy pipeline, injecting a 503 from the artifact registry at minute six and a timeout on the health check at minute eleven. The fixed fault schedule makes this comparable across model versions, which is the point — we're not measuring whether it fails, we're measuring time-to-recovery, and right now we're at a median of 94 seconds versus 340 seconds three months ago.
2. We wiped the scratchpad right after the injected 503 to see if it could recover the plan from context alone, and it couldn't — it just retried the same broken call five times. So whatever recovery skill we thought we measured in the ⟦T1⟧ was mostly sitting in notes, not in the model's actual replanning ability. Kind of deflating number to publish internally.
3. The final answer is usually still right because it weighs the last thing it read most heavily, but the trail behind it is full of dead claims. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦T1⟧, injecting a search-API timeout partway through.
4. We wanted to know if that was a robustness issue or just an artifact of task difficulty, so we ran the same tasks as ⟦T1⟧, injecting a search-API timeout partway through. Recovery time was fine, under two minutes on average, but the ⟦X⟧ on the ⟦T1⟧ was even worse than the clean baseline — the recovery process itself seems to generate a burst of new unverified notes that don't get reconciled.

COMMUNITY 2 EXCERPTS:
1. To test containment, each trajectory received one malformed citation record after the fourth repository query. The ⟦T2⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved. Seven failures in the ⟦T2⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
2. The ⟦T2⟧ was passed by 39 agents, whose final tables excluded the malformed record or explicitly marked it unresolved. Seven failures in the ⟦T2⟧ propagated the record into a derived chronology despite later retrieval evidence contradicting it.
3. The repair benchmark asked agents to correct inconsistencies in a transaction ledger while preserving valid rows. A ⟦T2⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step. The ⟦T2⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
4. A ⟦T2⟧ inserted one syntactically valid but semantically corrupted exchange-rate row after the initial validation step. The ⟦T2⟧ pass rate was 0.81, based solely on whether the final ledger quarantined or flagged that row.
5. A ⟦T2⟧ placed one invoice with a duplicated line item into the input bundle midway through verification. In the ⟦T2⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.
6. A ⟦T2⟧ placed one invoice with a duplicated line item into the input bundle midway through verification. In the ⟦T2⟧, 34 of 50 agents isolated the duplicate before producing the final spreadsheet.
7. A ⟦T2⟧ inserted one archive record whose jurisdiction label conflicted with its body text. The ⟦T2⟧ pass rate was 0.72, with successful agents either quarantining the record or documenting the conflict.
8. A ⟦T2⟧ inserted one archive record whose jurisdiction label conflicted with its body text. The ⟦T2⟧ pass rate was 0.72, with successful agents either quarantining the record or documenting the conflict.
