Three DEFINITIONS of the same concept at increasing specificity:

DEFINITION L0 (genus only): A procedure for building test items, used to create a harder difficulty level out of an existing easier one.

DEFINITION L1 (adds mechanism): A procedure for building test items that produces a harder difficulty level from an existing easier one. Instead of a person writing each new item by hand, an automated text-generating model is given the existing easy items and asked to produce more difficult variants of them. The new, tougher items are added to the test suite to extend how far its difficulty reaches.

DEFINITION L2 (adds measurement and conditions): A procedure for constructing benchmark or test-suite items that produces a harder or more challenging difficulty tier out of an existing easier tier. A text-generating model is prompted with the current easy items and asked to write tougher variants, so no person authors the new items from scratch; this yields a set of new advanced items (for example, sixty added to a coding benchmark) that push past the original items' difficulty. Difficulty is judged by how often the items are passed and by comparing the performance gap between the generated set and hand-written items (such as a small measured wording gap). The resulting items must be clearly marked as model-produced rather than passed off as human-written, and their difficulty tends to rise unevenly and lumpily, echoing the generating model's own training patterns instead of a deliberately designed progression.

Below are numbered excerpts from one community's documents in which one term — masked as ⟦TERM⟧ — is used (other local jargon masked ⟦X⟧). All excerpts use the SAME term from the SAME community.

For EACH definition level INDEPENDENTLY, judge whether the excerpts TAKEN TOGETHER support that the referent of ⟦TERM⟧, as used across these excerpts, is an instance of that level's concept:

- "covers" — the combined excerpts collectively instantiate the definition: each element that level commits to (kind; mechanism; measurement and conditions, as applicable) is evidenced SOMEWHERE in the set, and no excerpt contradicts it. Requires 2-4 verbatim quotes, each copied exactly from one numbered excerpt and prefixed with its number ("3: quoted text"), jointly carrying the evidence. Different quotes may come from different excerpts — evidence may accumulate across the set.
- "contradicts" — at least one excerpt is incompatible with that level's definition (the referent has a property the definition excludes, or lacks one it requires). Requires the verbatim quote of the incompatible fragment, number-prefixed.
- "insufficient" — even taken together, the excerpts do not decide for that level.

Do not infer beyond what is written; a level's extra commitments need actual textual evidence, not plausibility.

Output ONLY JSON:
[{"level": "L0", "verdict": "covers|contradicts|insufficient", "quotes": ["1: ...", "5: ..."]},
 {"level": "L1", "verdict": "...", "quotes": ["..."]},
 {"level": "L2", "verdict": "...", "quotes": ["..."]}]

EXCERPTS:
1. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons.
2. A ⟦TERM⟧ produced 2,160 task specifications from a weaker generator, with executable checks withheld from the evaluated agents. The ⟦TERM⟧ was rerun for every model family to prevent a single task-writing distribution from dominating comparisons. Generated tasks were filtered only for execution validity and duplicate surface form.
3. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces.
4. Three weaker task generators produced held-out data-management scenarios under a ⟦TERM⟧. The ⟦TERM⟧ required executable validators and prevented generators from observing evaluated-agent traces. Human review rejected 11% of generated tasks for ambiguous state transitions, leaving 1,740 tasks.
5. This pattern held after normalizing for the number of available tools and the length of task instructions. A second ⟦TERM⟧ round used newly sampled generators and fresh validators.
6. The final audit used 1,200 paired operational tasks generated under a ⟦TERM⟧. The ⟦TERM⟧ supplied executable validators while withholding task-generation traces from every evaluated system.