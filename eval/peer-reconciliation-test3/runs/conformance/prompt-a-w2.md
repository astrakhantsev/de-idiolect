Below are numbered items. Each item contains: a COMMITMENTS CHECKLIST extracted from usage excerpts of one concept, and a three-level cumulative definition LADDER written for the same concept ("L0" states the genus, "L1" adds the mechanism, "L2" adds measurement and conditions). The definitions use only ordinary words; local jargon was masked when they were written.

For EACH item, check FOUR conformance conditions:

1. L1 preserves L0's content — everything L0 commits to is stated or entailed in L1 (restating in other words is fine; dropping or contradicting it is not).
2. L2 preserves L1's content — same standard.
3. L1 states the checklist's mechanism commitment(s) — the checklist line(s) that describe the specific mechanism or process (what concretely happens) are stated in L1, verbatim or restated.
4. L2 states every checklist commitment — each checklist line's content appears in L2, verbatim or restated.

The item is "conformant" only if all four conditions hold; otherwise it is "nonconformant", with the first failing condition number and a one-sentence reason.

Judge only what is written — do not reward or penalize style, and do not judge whether the definitions are true or useful. A commitment counts as stated if a careful reader would recover it; it does not count if it was weakened to a vaguer claim or dropped.

Output ONLY a JSON array, one object per item:
[{"item": 1, "verdict": "conformant|nonconformant", "reason": "empty string if conformant, else 'condition N: one sentence'"}, ...]

ITEMS:

ITEM 1
CHECKLIST:
- Removes worked examples/demonstrations from a prompt or prompt segment while leaving instructions, step outlines, and formatting hints unchanged.
- Measures task success rate (e.g., 74%→39%, 74%→58%, ~6-point drop), comparing scores before vs. after the removal.
- Applied to agent prompts/tasks (support-ticket agent, refactor prompt, schema-validation prompt segment) either ad hoc or as a standing regression test run on every model version bump.
- Impact varies by task and by how many demonstrations are removed, ranging from a small (~6 point) drop to a large (74%→39%) drop.
- Only the demonstrations are altered — no other scaffold element (outline, formatting hints, instructions) is changed in the same run.
- Used specifically to reveal how much a model relies on worked demonstrations versus other prompt components.
LADDER:
L0: A diagnostic test procedure that reveals how much a model's task performance depends on the worked examples included in its prompt.
L1: A diagnostic test procedure that reveals how much a model's task performance depends on the worked examples included in its prompt. It works by deleting every worked example or demonstration from a prompt (or a specific prompt segment) while leaving the step outline, formatting hints, and written instructions exactly in place, so the demonstrations are the only thing changed. The task is then run and its success rate is compared against the success rate from before the removal.
L2: A diagnostic test procedure that reveals how heavily a model relies on worked demonstrations in its prompt versus the other parts (step outline, formatting hints, written instructions). Concretely, one removes every worked example from a prompt or a chosen prompt segment while leaving all other scaffold elements untouched, changing nothing but the demonstrations in that run. It measures the task's success rate and scores the result as the gap between the rate before removal and the rate after — e.g. 74% down to 39%, 74% down to 58%, or a slight roughly 6-point drop — where a bigger gap means greater reliance on the demonstrations. It applies to agent prompts and tasks (a support-ticket agent, a refactor prompt, a schema-validation segment), and the size of the drop varies by task and by how many demonstrations are pulled. It is run either ad hoc or as a standing regression test on every model version bump.
