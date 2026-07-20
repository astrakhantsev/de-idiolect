Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. Kicked off a ⟦TERM⟧ on the new deployment pipeline agent, 500 identical copies hitting the same task against our staging cluster. Found that 6% of runs were reading a scratch file that a completely different worker instance had written to, because our tempdir naming scheme wasn't actually unique per worker, just per host.
2. Classic. ⟦TERM⟧ is supposed to be about smoking out exactly this kind of shared-infrastructure race, and it did its job, but it also ate half our staging budget before someone noticed the contamination number wasn't zero.
3. Spent two days chasing what I thought was a ⟦X⟧ regression before realizing it was actually a ⟦TERM⟧ problem in disguise.
4. Lesson learned: run a dedicated ⟦TERM⟧ on any harness before trusting behavioral metrics that come out of batched execution, especially ones sensitive to file state like ⟦X⟧ is.
5. Fifth, we finally ran a proper ⟦TERM⟧ on the shared execution cluster and found 11% cross-contamination between worker instances writing to a common cache directory, which we now suspect explains some of the weirder outliers from earlier in the month that we'd previously written off as model noise.
6. ⟦TERM⟧ contamination on the shared cluster dropped from 11% to 4% after the tempdir isolation fix, though it's not zero and probably never will be given how our worker pool shares a cache layer by design.