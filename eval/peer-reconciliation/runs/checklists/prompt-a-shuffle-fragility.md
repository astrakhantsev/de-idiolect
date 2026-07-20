Below are usage excerpts from one community's documents. The term under study is masked as ⟦TERM⟧; other local jargon is masked as ⟦X⟧.

Extract a checklist of 4–7 concrete commitments that ANY faithful definition of ⟦TERM⟧'s concept must state, based ONLY on these excerpts:
- the SPECIFIC mechanism or process involved (what concretely happens — this item is mandatory),
- what is measured or produced, and how it is scored or read,
- when/where it applies (the setting and trigger),
- any constraint the excerpts clearly commit to.

Rules: each item is one line, concrete, supported by the excerpts; do NOT generalize beyond what the excerpts support; do not include ⟦X⟧ concepts. Output ONLY the checklist lines, one per line, no preamble.

EXCERPTS:

1. Same task, same tool outputs, just fed back to the model in a different order across three seeds, and our pass rate dropped from 81% to 41%. Classic ⟦TERM⟧ — the model was anchoring on "first result mentioned equals ground truth" instead of actually reasoning about which ledger entry was current. Once we saw the drop we went back and reordered manually a dozen more times and the curve just kept sliding.
2. But it exposed something else. With the seed menu locked, the only thing varying between two "identical" runs was tool-result order, and we still saw ⟦TERM⟧ show up as a nine-point swing on the contract-review agent even with seeds pinned.
3. With the seed menu frozen, a shift in the curve shape means the model changed, not the tasks. Last thing worth mentioning: we caught a ⟦TERM⟧ case purely from the ⟦X⟧ looking wrong. Reordered tool outputs shouldn't change how much verification the agent does at the end, but on one task family the back-loaded spend spiked even higher under shuffled ordering, like the model got less confident and started re-checking things it had already checked under the original order.