---
name: term-check
description: Coin-time check for a project-local term — asks an isolated model call what the concept is called in established fields, from frozen usage excerpts only. Use when the user types /term-check <term>, when a new term is being coined, or when the user asks "is this term ours or the field's?"
---

# /term-check — coin-time interception (manual trigger)

Run the de-idiolect coin-time hook on a term the project uses or is about to coin.

## Steps

1. **Identify the term and its source files.** If the user gave files, use those. Otherwise grep the project for files whose *prose* uses the term (skip lockfiles, build output, and anything the project marks private) and pick the 1–4 files with the most substantive usage.
2. **Locate the script, then run it.** Resolve `term-check.sh` in this order: `$TERM_CHECK_BIN` if set; `hook/term-check.sh` if the current project is the de-idiolect repo; `term-check.sh` on PATH (the documented install copies it to `~/.local/bin/`). If none resolves, stop and tell the user the script is not installed (point them at the repo's `hook/README.md`) — do not improvise the check inline; an inline imitation has no isolation and no manifest.

   ```
   bash <resolved-path>/term-check.sh "<term>" <file...>
   ```

3. **Present the flag** from the tail of `term-flags.md`: the one-line restatement, the candidate names with their owning fields, and the model's own fit assessment. Keep the **UNVERIFIED** framing verbatim — these are model-proposed names, and this project's own record shows such proposals can fabricate owners.
4. **Offer the next step**: for any candidate the user intends to rely on, open one primary source and confirm the mapping before it enters a glossary or a claim.

## The one rule you must not break

Do **not** feed the check call anything beyond the term and the files: no project context, no "we think it's related to X", no candidate owners, no prior conclusions. The script's information boundary (frozen usage excerpts only, isolated HOME, no tools) is the mechanism — a check call that hears your candidates is anchored, and its agreement is worthless. If the user offers candidates, note them for step 4 verification instead.

If the script reports that no paragraph contains the term, tell the user which files you searched and ask where the term is actually used — do not paraphrase the concept into the call yourself.
