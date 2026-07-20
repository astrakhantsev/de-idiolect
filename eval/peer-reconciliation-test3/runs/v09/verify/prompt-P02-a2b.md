Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A testing procedure that checks whether a software agent notices when the results handed back from its tool calls have been corrupted, rather than accepting them uncritically.

DEFINITION L1 (adds mechanism): A testing procedure that checks whether a software agent notices when the results handed back from its tool calls have been corrupted. It works by replacing the real output of a tool call, including test-runner output, with content that is syntactically valid but semantically meaningless — for example well-formed JSON carrying empty or nonsense fields, or plausible-looking but meaningless pass/fail noise — and then watching how the agent responds. The test observes whether the agent treats the garbage as if it were valid or instead recognizes that something is wrong.

DEFINITION L2 (adds measurement and conditions): A testing procedure that checks whether a software agent notices when the results returned from its tool calls have been corrupted. It is applied to an agent's session logs or task recordings: the real output of each tool call — including test-runner output — is swapped, one step at a time, for content that is syntactically valid but semantically meaningless, such as well-formed JSON with empty fields or plausible-looking but meaningless pass/fail noise. For each degraded step it records whether the agent detects the corruption and explicitly asks for a retry, re-fetch, or rerun, versus barreling forward as if the data were valid. The result is scored as the fraction or count of degraded steps caught (for example 22 of 30, or 8 of 30 missed, roughly 70–80%). It is kept as a standing regression test run on every model version bump, not only occasionally.

Below are numbered excerpts from a community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧).

For EACH excerpt, and for EACH definition level INDEPENDENTLY, decide: is the referent of ⟦TERM⟧, as used in THIS excerpt, an instance of the concept described by THAT definition?

- "instantiates" — the usage is consistent with and exemplifies that definition.
- "contradicts" — the usage is incompatible with that definition (the referent has a property that definition excludes, or lacks one it requires).
- "insufficient" — this excerpt alone does not contain enough to decide for that definition.

A usage can instantiate L0 while contradicting L2 — judge each level on its own content. Judge each excerpt on its own text only. For L1 and L2, any decided verdict (instantiates or contradicts) requires a verbatim supporting quote from the excerpt; L0 needs no quote.

Output ONLY a JSON array, one object per excerpt:
[{"excerpt": 1, "L0": "instantiates|contradicts|insufficient", "L1": {"verdict": "...", "quote": "verbatim or empty for insufficient"}, "L2": {"verdict": "...", "quote": "..."}}, ...]

EXCERPTS:

1. Recorded browser and shell interactions were replayed with syntactically valid tool outputs whose contents no longer corresponded to the requested operations. ⟦TERM⟧ was computed at every degraded observation boundary. ⟦TERM⟧ was 0.68 for the deliberative agent and 0.31 for the action-heavy agent.
2. ⟦TERM⟧ was computed at every degraded observation boundary. ⟦TERM⟧ was 0.68 for the deliberative agent and 0.31 for the action-heavy agent. Explicit retry requests were common after malformed-looking directory listings, but much rarer after plausible yet irrelevant test output.
3. During a separate replay condition, every third tool observation was replaced with plausible but meaningless text. ⟦TERM⟧ was lower on substituted tasks than on unchanged tasks, despite identical corruption frequency. ⟦TERM⟧ fell from 0.59 to 0.44 when agents encountered unfamiliar project layouts.
4. ⟦TERM⟧ was lower on substituted tasks than on unchanged tasks, despite identical corruption frequency. ⟦TERM⟧ fell from 0.59 to 0.44 when agents encountered unfamiliar project layouts. This suggests that uncertainty about task structure made agents more willing to accept misleading feedback.
5. This experiment replayed newly authored and standing benchmark items while tool results were semantically degraded at prespecified action boundaries. ⟦TERM⟧ was computed separately by task provenance and selector assignment. ⟦TERM⟧ improved from 0.42 to 0.63 after selector replacement, largely because the replacement issued explicit retries before editing.
6. ⟦TERM⟧ was computed separately by task provenance and selector assignment. ⟦TERM⟧ improved from 0.42 to 0.63 after selector replacement, largely because the replacement issued explicit retries before editing.