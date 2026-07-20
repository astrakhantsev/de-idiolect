Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A configurable enforcement rule in agentic coding-benchmark runs that sets a hard cap on how many times an agent may reopen the same file, meant to force the agent to hold file contents in working memory rather than treat disk as free scratch space.

DEFINITION L1 (adds mechanism): A configurable enforcement rule in agentic coding-benchmark runs that caps how many times an agent may reopen or reread the same file during a single run, meant to stop the agent from using disk as free scratch space. The cap is a fixed integer (for example, three). Once that number of reopens is reached, further rereads of the same file are ignored and not permitted, even ones that would help the agent finish the task.

DEFINITION L2 (adds measurement and conditions): A configurable enforcement rule, set as a fixed integer cap (for example, three), on how many times an agent may reopen or reread the same file during a single agentic coding-benchmark run, such as codebase-navigation, file-navigation, or onboarding suites where the agent reads files from disk while doing tasks. Its purpose is to force the agent to hold file contents in working memory instead of using disk as free scratch space. It counts repeated opens of the same file per run and flags or fails any run that exceeds the cap, while staying within it passes that check. Once the cap is reached, further helpful rereads are ignored and not permitted. Because the cap is itself a changeable setting, and changing it can flip which agents pass or fail, cap changes must be logged and told apart from real capability regressions.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation.
2. Items carried a ⟦TERM⟧ assigned independently by two annotators before deployment. The ⟦TERM⟧ predicted 71% of observed failures among lower-tier agents, reducing the number of failures forwarded for manual investigation. Disagreements were concentrated in items involving chained browser actions rather than answer extraction.
3. Results therefore exclude halted ⟦X⟧ batches and report only items whose ⟦TERM⟧ was stable across adjudicators.
4. The evaluation suite contained 3,050 tasks spanning three capability tiers and two execution environments. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
5. Every item received a ⟦TERM⟧ before model results were inspected. The ⟦TERM⟧ was revised for 4.7% of items after annotators discovered hidden dependencies on unavailable credentials.
6. Removing exhausted items increased rank stability across weekly reruns. Failures below an agent’s ⟦TERM⟧ were flagged for audit rather than treated as ordinary misses. The ⟦TERM⟧ also exposed a limitation: several agents completed higher-tier items through narrow memorized procedures while failing lower-tier tasks requiring unfamiliar tool states.