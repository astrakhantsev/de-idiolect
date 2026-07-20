Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): It is a constraint-satisfaction score used to assess whether a coding or repository-editing response fulfills the stated requirements in an instruction.

DEFINITION L1 (adds mechanism): It is a constraint-satisfaction score used to assess whether a coding or repository-editing response fulfills the stated requirements in an instruction. Each requirement is checked separately, including test execution, preservation of unrelated files, and formatting cues, then the satisfied requirements are aggregated into a fraction or percentage across trials. For a mid-task instruction reversal, it is calculated before and after the reversal while retaining requirements from both messages.

DEFINITION L2 (adds measurement and conditions): It is a constraint-satisfaction score for instruction-following in repository and code-editing tasks. It measures whether every stated requirement is met, including test-execution requirements, preservation of unrelated files, and formatting cues. Each requirement is evaluated separately, and the results are aggregated across many trials, such as 480 trials, as a fraction or percentage of requirements met. It applies to English and translated instructions, including Spanish and Arabic, and to tasks where a solved demonstration, file-path hint, step outline, or formatting cue is removed. With a mid-task instruction reversal, it is computed before and after the reversal while requiring constraints from both the original and reversed messages. It falls when demonstrations are absent despite visible constraints, and remains lower for non-English instructions, especially on test execution and final test reports.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. The agent does discard the stale objective and pursue the revised one, so the check passes, but it gets there by throwing away enormous amounts of partial work and starting over almost from scratch every single time instead of salvaging anything reusable from before the reversal. So I ran the ⟦TERM⟧ numbers on the same trial set. Average of 34% of total tokens on those pivot trials went into work that got discarded outright, versus about 9% on trials with no mid-task instruction change.
2. Also tracked ⟦TERM⟧ across the corrected batch out of curiosity. Even with clean isolation, the discarded-work ratio on genuine pivot trials sits around 28%, which tracks with what someone else here posted recently.
3. Throwing out most of last year's harness and starting over, so here's where things stand. ⟦TERM⟧ tracking is now built in by default — every discarded branch gets tagged with its token cost at the moment it's abandoned, so we get the dead-end ratio for free on every run instead of reconstructing it after the fact from logs.
4. And ⟦TERM⟧, the number I care about most honestly, sits at 22% quarter-wide, worse on multi-turn tasks with instruction reversals than on straightforward single-objective ones, which tracks with everything else we've seen this quarter about reversals being expensive even when the agent ultimately gets them right.