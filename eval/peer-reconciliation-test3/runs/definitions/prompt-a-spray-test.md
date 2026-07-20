Below are usage excerpts from one community's documents, all containing the same term, shown masked as ⟦TERM⟧ (other local jargon is masked as ⟦X⟧).

Write THREE cumulative operational definitions of the concept ⟦TERM⟧ names AS USED in these excerpts, at three levels of specificity:

- "L0" — ONE sentence: what kind of thing it is (a phenomenon, a procedure, a score, a rule…) and its immediate purpose. Genus only, no mechanism.
- "L1" — L0's content PLUS the specific mechanism or process (what concretely happens). 2–4 sentences.
- "L2" — L1's content PLUS what is measured or produced and how it is scored or read, and when/where it applies. 60–160 words.

COMMITMENTS CHECKLIST (extracted from the same excerpts; L2 must state every commitment, L1 must state the mechanism commitments):
- Run many identical parallel copies (e.g., 500 runs) of the same task/agent against a shared execution environment (staging or shared cluster) to test for cross-contamination between worker instances.
- Detects cross-instance interference caused by non-unique shared infrastructure, such as tempdir/cache naming that collides across workers on the same host or cluster.
- Produces a contamination rate as a percentage of runs affected (e.g., 6%, 11%, 4%), which is scored/read as the fraction of runs showing shared-state interference (like reading/writing another worker's scratch or cache files).
- Applies specifically to batched/parallel execution harnesses, and should be run on any such harness before trusting behavioral metrics derived from it, especially when file state sensitivity is involved.
- Contamination is expected to be reducible (e.g., via tempdir isolation fixes) but not fully eliminable when workers share underlying infrastructure like a common cache layer by design.

Constraints for ALL levels:
- Ordinary words and simple notation only; do NOT use the masked terms or guess at them; no names of people, published methods, fields, systems, models, or communities.
- Base everything ONLY on what the excerpts support; no generalizing catch-all phrases ("or otherwise", "or any similar", "in any way").
- Each level must be self-contained (do not reference the other levels).

Output ONLY JSON: {"L0": "...", "L1": "...", "L2": "..."}

EXCERPTS:

1. Kicked off a ⟦TERM⟧ on the new deployment pipeline agent, 500 identical copies hitting the same task against our staging cluster. Found that 6% of runs were reading a scratch file that a completely different worker instance had written to, because our tempdir naming scheme wasn't actually unique per worker, just per host.
2. Classic. ⟦TERM⟧ is supposed to be about smoking out exactly this kind of shared-infrastructure race, and it did its job, but it also ate half our staging budget before someone noticed the contamination number wasn't zero.
3. Spent two days chasing what I thought was a ⟦X⟧ regression before realizing it was actually a ⟦TERM⟧ problem in disguise.
4. Lesson learned: run a dedicated ⟦TERM⟧ on any harness before trusting behavioral metrics that come out of batched execution, especially ones sensitive to file state like ⟦X⟧ is.
5. Fifth, we finally ran a proper ⟦TERM⟧ on the shared execution cluster and found 11% cross-contamination between worker instances writing to a common cache directory, which we now suspect explains some of the weirder outliers from earlier in the month that we'd previously written off as model noise.
6. ⟦TERM⟧ contamination on the shared cluster dropped from 11% to 4% after the tempdir isolation fix, though it's not zero and probably never will be given how our worker pool shares a cache layer by design.