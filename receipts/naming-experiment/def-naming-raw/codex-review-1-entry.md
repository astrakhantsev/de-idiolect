## Verdict
needs-attention

## Summary
The entry materially overstates the verification grade of its central novelty claim and the purity of its eggs demonstration. Most seriously, it says the load-bearing neighbours were primary-read even though the ledger explicitly says several remain unverified.

## Findings

### [critical] The entry falsely says its load-bearing novelty neighbours were primary-read
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §5 “Novelty position”; `10_projects/minelit/idiolect/novelty-position.md` — “Findings” and programme-level go/no-go
- **Problem**: The entry introduces its novelty map as having “the load-bearing neighbours read in primary,” but the ledger says the assembly’s load-bearing Microsoft patents, NeoN, and Confluence materials have not been orchestrator-verified.
- **Evidence**: The entry says the ledger was cross-checked “with the load-bearing neighbours read in primary.” The ledger says “the assembly row’s load-bearing neighbours (Microsoft patent family, NeoN, Confluence Define docs) have not been orchestrator-verified.” The entry nevertheless characterizes Microsoft as unfamiliar-term detection leading to definition, NeoN/AXOLOTL as novel-sense detection leading to generated definitions, Confluence and Slack as shipped lazy-definition products, and Atlan Sage as resolving conflict into one canonical answer.
- **Impact**: This gives judges false assurance that the central `open (candidate)` assembly claim survived primary-source verification—the exact false-novelty failure the entry promises to prevent.
- **Fix**: Either open and verify every named load-bearing neighbour before submission, or remove the primary-read claim and label each characterization explicitly as run-level/unverified. Until verification, cede priority without relying on detailed product or patent behavior.
- **Confidence**: 1.0

### [critical] The eggs demo reintroduces field vocabulary that the entry says was excluded
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §4a; `10_projects/minelit/idiolect/2026-07-17-eggs-routing-microdemo.md` — “Domain-stripped constrained definitions” and “The two searches per term”
- **Problem**: The entry claims the searches used “only the definition’s plain-language content,” but the actual queries add decisive domain terms absent from the constrained definitions.
- **Evidence**: T1’s definition speaks only of a “measured substance in the blood” and “particular fatty component,” while its query adds “blood cholesterol” and “dietary cholesterol.” T2’s definition uses “small carrier bodies” and “fatty substance,” while its query adds “lipoprotein particles,” “cholesterol,” and “cardiovascular risk.” The demo itself says queries were built from definition content words and used no sub-field proper term.
- **Impact**: The routing result cannot be attributed to the constrained, community-neutral definition alone. In T2 especially, “lipoprotein particles” is already the vocabulary of the literature the query is supposed to discover.
- **Fix**: Rerun the demonstration using a mechanically documented transformation of the exact frozen definition tokens, with no added field vocabulary. Otherwise relabel it as analyst-assisted query expansion rather than definition-only routing.
- **Confidence**: 1.0

### [critical] The novelty ledger reports the strongest search evidence as both completed and unrun
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §5 and Appendix; `10_projects/minelit/idiolect/novelty-position.md` — “Search ledger,” assembly row, and programme-level go/no-go; `10_projects/minelit/idiolect/2026-07-17-selfapp-blind-naming.md` — “Results”
- **Problem**: The evidence base contradicts itself about whether a true assembly-level blind Pass A occurred, while the entry adopts the favorable completed-pass account.
- **Evidence**: The assembly row claims a “3-draw blind Pass-A null.” The self-application document says the assembly Pass A was “executed.” But the ledger’s search section says “The only genuinely blind instrument in the record is the definition-mediated naming experiment” and “A true Pass-A on the assembly question remains unrun”; its closing section again says “a true blind Pass-A on the assembly question is unrun.” The ledger also calls T1–T3 complete in its rows while earlier listing T1, T2, and T3 as “pending” or “NOT searched.”
- **Impact**: Judges cannot determine the actual evidence grade of the assembly absence claim. The entry’s statement that a blind pass independently reproduced the map is not safely auditable against its own ledger.
- **Fix**: Reconcile the chronology throughout the ledger. Distinguish Gate 2’s targeted searches from the later assembly Pass A, remove all stale “unrun/pending” statements, and link the exact executed brief, outputs, hashes, and contamination check.
- **Confidence**: 1.0

### [high] The corpus’s standing decision still forbids submission
- **Where**: `10_projects/minelit/idiolect/novelty-position.md` — programme-level go/no-go; `10_projects/minelit/idiolect/2026-07-17-flf-recall-extender-criteria-first.md` — frontmatter and §5; `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — submission draft
- **Problem**: The entry is framed as a competition submission, but both governing evidence documents say the prior `NO SUBMIT` decision remains in force and the required replacement decision has not been written.
- **Evidence**: The ledger says “Programme-level go/no-go: NOT THIS DOCUMENT, AND NOT YET WRITTEN” and “The 2026-07-16 NO SUBMIT decision remains the standing decision of record.” The criteria-first document says “The 2026-07-16 NO SUBMIT stands until that entry exists” and permits submission only if the programme verdict is go.
- **Impact**: Submitting this draft would violate the project’s explicit decision gate while its novelty stop rule and primary verification remain incomplete.
- **Fix**: Complete the required decision-journal entry after resolving the evidence failures, or keep the document explicitly marked as an unsubmitted draft.
- **Confidence**: 1.0

### [high] The transparent control does not rule out generic search or query-crafting effects
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §4a; `10_projects/minelit/idiolect/2026-07-17-eggs-routing-microdemo.md` — T4 result
- **Problem**: The entry says the T4 control “rules out ‘generic search noise,’” but the evidence document says T4 was not separately definition-mediated queried.
- **Evidence**: The T4 row records “(not separately queried).” It establishes only that the naive query already reaches dietary-cholesterol material. The three positive queries were hand-written by an informed orchestrator who knew the target literatures.
- **Impact**: The control cannot distinguish definition mediation from broader, better-crafted, or answer-informed queries. “Rules out” is substantially stronger than the experiment supports.
- **Fix**: Change the conclusion to “consistent with the expected transparent-term null,” or run a symmetric T4 definition query plus matched query-crafting controls.
- **Confidence**: 1.0

### [high] The entry relies on a causal graveyard thesis that its own specification says is not ready
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §§2 and 6; `10_projects/minelit/idiolect/2026-07-17-flf-recall-extender-criteria-first.md` — §2.1
- **Problem**: The entry makes the “universal + manual + build-once” diagnosis and LLM marginal-cost reversal its strongest scaling argument, although the specification says this synthesis requires an unbuilt case matrix before the entry may rely on it.
- **Evidence**: The entry says “the graveyard’s killers were marginal-cost problems” and that generation makes the previously unaffordable thing cheap. It later calls scaling “the strongest leg.” The criteria-first specification calls the history “provisional, not settled” and says the pattern “requires the case matrix before the entry may rely on it.” The entry itself admits that the case matrix is unbuilt.
- **Impact**: An expert can challenge the central “why now?” argument as a selective, effectively monocausal history that has not examined counterexamples or the remaining costs of verification and maintenance.
- **Fix**: Build the promised case matrix, or demote this to a hypothesis from the reviewed examples and remove “killers,” “precisely,” and “strongest leg.”
- **Confidence**: 1.0

### [high] A fixed vocabulary is presented as guaranteeing community neutrality despite only exploratory evidence
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — §3; `10_projects/minelit/idiolect/2026-07-17-flf-recall-extender-criteria-first.md` — generalization criterion
- **Problem**: The entry states that the constrained definition “is community-neutral” and therefore can match another community’s definition, while the specification permits only the weaker claim that domain-blindness is a design intention consistent with one clean cell.
- **Evidence**: The entry says the definition “does not encode the local idiolect.” The criteria document says “Domain-blindness via domain-stripped definitions is a design intention consistent with that one cell; any stronger generalization claim is conditional on reruns.” No supplied experiment measures cross-community matching from independently generated constrained definitions.
- **Impact**: Ordinary words can still encode community-specific distinctions and framing. The entry presents its load-bearing hypothesis as an established representation property.
- **Fix**: Say that the constraint is intended to reduce local lexical cues and that whether it produces sufficiently comparable representations remains untested.
- **Confidence**: 1.0

### [high] The promised sentence-level evidence grading is not actually applied
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — opening note and §§1–3, 6
- **Problem**: Several central enthusiasm-bearing claims have neither a same-sentence grade nor evidence that supports their strength, contradicting the entry’s explicit reading contract.
- **Evidence**: Ungraded examples include “a more capable model… produces a more… confident report that the prior work isn’t there,” “LLM definition generation collapses that marginal cost toward zero,” “cross-vocabulary equivalence detection is a capability that improves with better models,” the cache property “lets the commons accumulate without requiring agreement,” and “static generic wordlists survived for decades precisely because they need no curation.” Section 6 calls scaling “the strongest leg.” The cited historical owners diagnose acquisition or coordination costs; they do not establish these LLM-performance, cost-collapse, or compounding claims.
- **Impact**: Expert judges are invited to treat hypotheses and architecture intentions as evidence-backed conclusions, while the entry prominently promises the opposite.
- **Fix**: Add an honest same-sentence grade to each claim—usually `design hypothesis`, `economic argument, unmeasured`, or `untested architecture property`—or provide direct evidence and narrow the scope.
- **Confidence**: 1.0

### [high] The evidence appendix is not navigable as written
- **Where**: `10_projects/minelit/idiolect/entry/FLF-entry-recall-extender.md` — Appendix; supplied evidence corpus
- **Problem**: The purported evidence links use unresolved forms such as `[novelty-position.md]`, `[assembly-blind-passA]`, and `[definition-mediated naming experiment]`, without URL targets or reference definitions.
- **Evidence**: The appendix contains bracketed labels only, not Markdown links of the form `[label](path)` or Obsidian wikilinks. The supplied corpus also omits the named definition-mediated experiment and assembly Pass-A documents, despite the entry relying on both.
- **Impact**: Judges cannot open the receipts from the rendered submission or audit the two most important experimental and novelty claims.
- **Fix**: Replace every placeholder with a tested relative or public URL and ensure every target—including the naming experiment, assembly Pass A, frozen briefs, and raw outputs—is included in the submission package.
- **Confidence**: 1.0

### [medium] The criteria-first and self-application documents contain stale status claims
- **Where**: `10_projects/minelit/idiolect/2026-07-17-flf-recall-extender-criteria-first.md` — §2; `10_projects/minelit/idiolect/2026-07-17-selfapp-blind-naming.md` — frontmatter and Results; `10_projects/minelit/idiolect/novelty-position.md` — findings
- **Problem**: The specification still calls strips 1 and 3 candidate-open after the ledger downgraded both, and says no self-application glossary row, definition, brief, output, or hashes exist. The self-application document contains a frozen brief and hash but has a frontmatter status saying runs are “launching” while its body says they were blocked.
- **Evidence**: Criteria §2.3 lists “detector-as-trigger” and the “pay-as-you-go stance” as candidate-open; the ledger marks both `predated`. Criteria §2.4 says “nothing exists yet,” while the self-application document gives brief hash `66da20…` and a blocked result. Its YAML still says “Runs launching.”
- **Impact**: Readers cannot distinguish current novelty claims and actionable remaining work from superseded planning state.
- **Fix**: Update the specification to the post-triage map and current self-application state; change the self-application status to `BLOCKED — brief frozen, no runs completed`.
- **Confidence**: 1.0

### [medium] The eggs document calls its search-result summary “receipts” without preserving auditable raw results
- **Where**: `10_projects/minelit/idiolect/2026-07-17-eggs-routing-microdemo.md` — Results
- **Problem**: The document asserts that raw hit lists are inspectable and that certain sources appeared among “top results,” but provides no raw search capture, ranked URLs, timestamps, or exact ledger for the stated “light variants.”
- **Evidence**: It says WebSearch returned the lists “verbatim,” yet the evidence is a prose/table summary with abbreviated titles and occasional identifiers. The naive search is described as one query “and light variants,” without recording those variants or their separate rankings.
- **Impact**: A judge cannot independently verify the claimed top-result contrast, and web rankings may change before review.
- **Fix**: Attach timestamped raw outputs for every exact query and variant, including ordered URLs and result snippets; link them from the demo.
- **Confidence**: 0.98

## Next Steps

- Remove or correct the false primary-read statement before any submission.
- Rerun the eggs demo without injected field vocabulary and with a real symmetric control.
- Reconcile the novelty ledger’s blind-pass and T-pass statuses.
- Verify the unopened load-bearing neighbours and complete the formal go/no-go decision.
- Replace all evidence placeholders with tested links to complete, auditable receipts.