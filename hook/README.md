# The coin-time hook (v1) — `term-check`

> **Post-submission addition (2026-07-20).** The competition entry was submitted 2026-07-19 AoE; the as-submitted state is tagged [`flf-submission`](../../../tree/flf-submission). ENTRY.md §4.2 grades this tool "argued and unbuilt" and is left unmodified; this directory is the v1 build of exactly that proposal, added the day after the deadline and labeled as such.

The minimal inward de-idiolection tool from ENTRY.md §4.2: at the moment a project coins a term, send the **frozen usage excerpts** — and nothing else — to an **isolated** model call and ask the reverse-dictionary question: *what is this concept called, which established fields own it, and what are the oldest treatments you would expect?* The answer comes back as a flag whose candidates are all labeled **UNVERIFIED**, with the instruction to open one primary source per candidate you intend to rely on.

Why a hook and not a prompt: the entry's §2 record shows the agents that ran the "novelty survives" sweep already had standing instructions to search the field's vocabulary before committing — the instruction was installed, and the failure still occurred. A standing instruction must win an attention contest every turn; a hook fires deterministically (§4.2, "coin-time / claim-time / cite-time" — the glossary maps this to pre-commit hooks in software engineering).

## Try it in two minutes (on this repo's own vocabulary)

Prerequisites: an authenticated [Claude Code](https://claude.com/claude-code) CLI (`claude`), bash, standard Unix tools. From the repo root:

```
bash hook/term-check.sh "misroute" ENTRY.md
```

This assembles the ENTRY.md paragraphs that use the entry's coinage *misroute*, runs two isolated weights-only draws (sonnet + opus), and appends a flag to `./term-flags.md`. Score it yourself against the entry's own answer key: GLOSSARY.md's *misroute* row names the field's terms (vocabulary-mismatch retrieval failure; early IR's "false drop"). A committed run of exactly this — plus a deliberately thin one-paragraph case (`era-gated`) — is in [`example/`](example/), with prompts, hashes, and per-draw isolation manifests.

## What v1 ships

- **`term-check.sh`** — the check itself (trigger T1, manual). Excerpt assembly → reverse-dictionary prompt → N isolated draws → UNVERIFIED-labeled flag in `term-flags.md` → JSONL instrumentation row per draw in `.term-check/log.jsonl`.
- **`skill/term-check/`** — a `/term-check` slash-command skill for Claude Code, so the check is invocable mid-conversation without the agent hand-assembling context (which would break the information boundary; the skill's one hard rule is that it must not).
- **`hooks/glossary-watch.py`** — trigger T2, the deterministic one: a Stop hook that fires `term-check.sh` automatically when a new entry appears in the project's glossary file. Dumb by design: the trigger is "a term entered the glossary", nothing cleverer. First run seeds a baseline and fires on nothing; at most 3 terms fire per turn; `.term-check/off` is the kill switch.

Not shipped in v1, deliberately: trigger T3 (novel-phrase detection over arbitrary prose — the prototype's detection endpoint missed its target in the e2e cell, so v1 keeps only high-precision triggers); any search-enabled draw (v1 is weights-only; see boundary note below); claim-time and cite-time automation (§4.2 proposes them; their v1 would be shaped the same way); portability beyond Claude Code (the protocol is harness-agnostic, this implementation is not).

## Scan mode — give a project a seed glossary (`term-scan.sh`)

> **Post-submission addition (2026-07-20), built on the v1 hook above.** A separate script; `term-check.sh` is unmodified.

T1 checks a term you already know is a coinage; T2 fires when one enters a glossary. On a project that has **no glossary yet**, neither has anything to fire on. `term-scan.sh` closes that gap: point it at a project's prose and it surfaces the project's most local coinages, then — on the ones you keep — runs the existing per-term check and assembles a seed glossary. **Detect → curate → check → seed**, and the seed is written to match `glossary-watch.py`'s entry regex, so T2 can watch it afterward (scan bootstraps the loop the hook needs).

```
# phase 1 — detect (one model call over the prose), then STOP for curation:
bash hook/term-scan.sh <path-or-files...>
# ... edit scan-candidates.md, mark [x] the terms worth checking ...
# phase 2 — check only the [x]-marked terms, assemble GLOSSARY-SEED.md:
bash hook/term-scan.sh --check <same paths...>
# or, one shot, auto-keep the top N:  bash hook/term-scan.sh --top 5 <paths...>
```

**Two phases, and the gate between them is mandatory.** Phase 1 costs exactly one detection call, writes `scan-candidates.md`, and stops. **No naming draw runs until you mark terms `[x]`.** This is the design's load-bearing safety property: surfacing is heuristic, and a weak candidate that silently spent a naming draw — or a junk entry that silently entered the seed glossary — would leave a user worse off than with no scan mode at all. Phase 2 additionally drops any term that does not literally appear in the source files (a detector can hallucinate a term; the prose is the arbiter). Default caps: ~18k input words for detection (evenly downsampled beyond the cap, recorded in the manifest), and ≤10 checked terms per run; phase-2 batch is sonnet-only, opus opt-in via `-m`.

**What isolation buys here, and what it does not.** The detection call *may* see the project's files wholesale — the [information boundary](#the-two-rules-that-make-it-a-measurement-and-not-a-vibe) (frozen excerpts only, no candidate owners) binds the per-term **naming** call in `term-check.sh`, which scan calls unchanged. Detection still runs through the same isolation mechanics (fresh cwd + credentials-only HOME + pinned `CLAUDE_CONFIG_DIR` + all tools disallowed) so your own global config (CLAUDE.md, memory) cannot steer *which* terms it surfaces. It is isolation-from-config, not blindness-to-project.

**Honest expectations — surfacing is heuristic; the per-term check is the product.** Detection is the entry's weakest measured component: the prototype's own detector missed its one retrospective coinage endpoint (§4.1, §5.3). Scan's model-assisted detector is a *different* detector, and shipping it **does not** claim to fix that record — it is a convenience that produces a curatable list, gated so its errors cost a curator's glance, not credibility. Expect the raw list to mix real coinages, real-but-off-target coinages, and the occasional junk one; that mix is exactly why the curation gate is not optional. A worked self-application run on this repo's own prose (with `GLOSSARY.md`/`PSEUDOCODE.md`/`hook/` held out as answer-key contamination) is committed under [`example-scan/`](example-scan/), scored by hand against `GLOSSARY.md`'s coinage list.

## Install into your own project

**Manual check only (T1):** copy `term-check.sh` anywhere (or call it from this clone) and run it with a term + the files that use it. No other integration needed; this alone is useful on day one.

**Slash command:** the skill needs the script too — install both:

```
cp hook/term-check.sh ~/.local/bin/term-check.sh && chmod +x ~/.local/bin/term-check.sh
cp -r hook/skill/term-check <your-project>/.claude/skills/
```

Then `/term-check <term>` inside Claude Code (the skill resolves the script via `$TERM_CHECK_BIN`, the repo-local path, or PATH, in that order).

**Deterministic trigger (T2):** register the Stop hook in your project's `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 /path/to/de-idiolect/hook/hooks/glossary-watch.py" } ] }
    ]
  }
}
```

Point `TERM_CHECK_GLOSSARIES` at your glossary file(s) if they are not named `GLOSSARY.md`/`glossary.md`; entries are recognized as `- **term** — ...` lines or `## term` headings (a narrow, documented convention rather than a heuristic).

## The two rules that make it a measurement and not a vibe

1. **Information boundary** (the entry's evaluation carried this as a frozen contract): the check call receives the paragraphs that contain the term, from the files you name, and *nothing else* — no project conclusions, no candidate owners, no session context, no memory. A call that hears your candidates is a verification call, not a naming call; it will anchor. This is why the script assembles excerpts mechanically instead of letting an agent summarize "what we mean".
2. **Isolation**: every draw runs in a fresh temp cwd with a fresh `HOME` containing only the CLI credential file — no settings, no `CLAUDE.md`, no memory (your own global config carries your project's vocabulary and would leak it into the draw). `CLAUDE_CONFIG_DIR` is explicitly pinned to the fresh home as well: an inherited value would otherwise route the CLI back to the caller's real config, silently bypassing the fresh-HOME boundary (an adversarial-review finding on this very script — folded before first release). All tools are disallowed. Each draw writes a manifest (prompt hash, home policy, command, output hash) so isolation is claimed from mechanics and manifests, not from probing the model. On macOS, where credentials may live in the Keychain instead of `~/.claude/.credentials.json`, the fresh HOME ships empty and Keychain auth is assumed (untested; the manifest records which case applied).

**What a hit and a miss mean (the boundary the entry draws in §7-adjacent terms):** the draws are weights-only, so a hit means the field's name for your concept is *model-recoverable from the usage alone* — a reconciled, memorized seam, exactly where a lookup is cheap and skipping it is unforced error. A miss does **not** clear the term: on unreconciled seams there is nothing memorized to recover, and establishing equivalence there is the entry's define→match operation (§4.1), not this hook. The hook's job is only to make the cheap check fire at the right moment, in the right direction of question — "what is this called?" (onomasiological), never "find prior art on X", which invites the confident null the entry is about.

## Instrumentation

Every trigger evaluation and draw appends a JSONL row (`.term-check/log.jsonl`): timestamp, term, trigger (`manual`/`glossary-watch`/`scan`), model, status, latency, prompt hash — including quiet watcher evaluations that fired nothing (burden needs the denominator, not just the firings). Scan adds a `scan-detect` row (files, words, candidates returned, sampling) and a `scan-check` row per curated term (real source files, status, whether it produced a seed entry) to the same log. After a week of normal use this yields **flags/day and trigger burden**. It does *not* by itself yield flag **precision**: nothing records whether you then opened a primary and confirmed an owner. The v1 convention for that half is manual — when you verify a candidate, add a `verified: <candidate> — <yes|no|partial>, <source opened>` line to that term's block in `term-flags.md`; the blocks are grep-able and the join to the log is by term. Without the log this is a gadget; with it plus your verification lines, it is the experiment.

## Standing limitations

- The entry's own caveat transfers verbatim: retrospective coin-time interception was near-null on fresh cases (§2); this is a workflow design with a measured scope boundary, not a demonstrated rescue. What is new in v1 is only that the hook half now exists and logs.
- Flags can propose wrong or fabricated owners — the project's record contains exactly this failure, which is why UNVERIFIED labeling and the open-one-primary step are not optional politeness.
- Two draws from one model family is a correlated read, not two opinions (the entry cites the measured ceiling on same-family agreement); treat convergence as weak evidence and divergence as informative.
- A 300s timeout (where a `timeout`/`gtimeout` binary exists; the manifest records if none did), no retries, no queueing: a failed draw is logged and shown as failed. Rerun manually.
- The glossary watcher is single-flight per project (a non-blocking lock): with parallel sessions in one project, one session's Stop hook does the scan and the other skips that turn — nothing is lost, the glossary is rescanned next turn. The lock uses `fcntl`, so the watcher is POSIX-only (Linux/macOS).
- The committed example under `example/` was generated by the pre-review version of `term-check.sh` (isolated draws, same prompts — the folded review findings changed portability and env-pinning, not prompt assembly; prompt hashes remain valid).
