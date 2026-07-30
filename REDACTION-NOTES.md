# Redaction notes

This repository is an export from a private working repo. Machine-local absolute paths from the author's machine leaked into the first export and were redacted on **2026-07-29** in a follow-up commit (history was deliberately not rewritten — see "Why no history rewrite" below).

## What was redacted

The private path **prefix**, and nothing else:

| Was | Is |
|---|---|
| `/mnt/f/hub/...` | `<vault>/...` |
| `/home/<user>/...` | `<home>/...` |

Everything after the prefix is preserved. That keeps a receipt traceable and keeps a `sha256  path` manifest line naming the file it hashed, which is the same policy the pre-existing `redact_detection_manifest.py` applies. 40 files were redacted this way, plus 3 code files parameterized (below).

## What was NOT redacted, and why

**33 files still contain a private prefix. This is deliberate.** Every one of them is bound by a hash that something else verifies, and rewriting one would silently break the attestation chain that is the whole point of the receipt. The breakdown below accounts for all 33: 22 hash-bound artifacts + 4 attestation manifests + 7 v0.10 files.

### Hash-bound artifacts (22 files) — their sha256 is recorded in-repo

`eval/e2e-cell/runs/{c2-excerpts,d-input,f-input,n-input,fidelity-input-opus,fidelity-input-sonnet}.md`, the nine `eval/measurements/p1-fidelity-calibration/runs/inputs/fidelity-input-*.md`, the four `eval/measurements/p2-guided-generation/runs/inputs/*.md`, `eval/measurements/p3-provenance/input-manifest.txt`, and `eval/peer-reconciliation-{fresh,test3}/retrieve_xc.py`.

These are the rendered judge inputs and the frozen instrument code. Their hashes are recorded in freeze manifests precisely so a reader can verify *what the judge actually saw*. Editing the bytes would make that verification fail, converting a checkable receipt into an unverifiable one.

### Attestation manifests (4 files)

`eval/e2e-cell/runs/spec.sha256`, and `freeze-manifest.txt` in `eval/measurements/`, `eval/peer-reconciliation-fresh/`, `eval/peer-reconciliation-test3/`.

A manifest is the thing other components verify against. `eval/peer-reconciliation-v010/attest.py` binds `../peer-reconciliation-test3/freeze-manifest.txt` by hash into its manifest-of-manifests **H**, and parses a bge-snapshot line out of it — so editing it would break v0.10's build-H.

### The v0.10 workspace (7 files)

`eval/peer-reconciliation-v010/{README.md,attest.py,baseline_a.py,retrieve_xc_v010.py,run_v010.sh,spend.py,tests/test_v010.py}`.

This workspace is a **freeze candidate** bound by an out-of-tree pre-registration by hash, with `REQUIRED-INVENTORY.txt` asserting the exact implementation file set and build-H hashing its members. Two of the paths there are load-bearing rather than incidental:

- `CANONICAL_CUSTODY_LEDGER` is documented as *"the canonical, out-of-tree, operator-local durable ledger path … It lives OUTSIDE every checkout so a fresh-checkout revised-prereg instance still sees a key spent/forfeited elsewhere"*, and round-11 hardening made the scorer **refuse a non-canonical custody-ledger override in runtime**. The hardcoding is an anti-tamper property, not an oversight; parameterizing it would weaken the protocol it implements.
- `tests/test_v010.py` asserts the literal custody path appears in the driver.

Changing any of these would invalidate a pre-registration that has not yet spent its sealed TEST. It is left alone on purpose.

## Code that was parameterized instead of redacted

A placeholder inside executable code is a landmine — it looks fixed and fails at runtime. So three live scripts were parameterized, which also fixes portability (they previously could not run on any machine but the author's):

- `eval/e2e-cell/detect.py` and `detect_exploratory.py` — corpora now come from `DEIDIOLECT_PROJECT_DIR` / `DEIDIOLECT_BACKGROUND_DIR` (or `DEIDIOLECT_VAULT`). Behaviour is unchanged when they resolve to the original inputs.
- `eval/measurements/p3-provenance/link_ledger.py` — its seeded extraction-recall audit pointed at the vault by absolute path. **The same raw outputs are committed in this repo under `receipts/`**, so it now resolves in-repo: same seed, same sorted basenames, same selection, and it runs from a fresh checkout.

## Exposure assessment

Severity of the original leak: **low**, and the assessment is recorded here rather than assumed.

- What was disclosed: the vault path prefix, its top-level naming scheme (`10_projects/`, `30_reference/`), and the filenames of the project's **own** research documents — which this package's entry describes substantively anyway.
- What was **not** disclosed: any personal, employer, or financial document name. Greps for the sensitive candidates return zero tracked files. The only `30_reference` file named anywhere is `novelty-protocol.md`, which `redact_detection_manifest.py` **deliberately retains** as load-bearing for the background-contamination diagnosis.
- The targeted redaction in the original export worked exactly where the sensitive content was: `eval/e2e-cell/runs/detection.json` carries its `redaction_note` and its background manifest is reduced to opaque ids. What the export lacked afterward was a blanket path scan. That scan is now a script.

## Why no history rewrite

The paths remain in this repository's git history. A rewrite would mean a force-push on a repo carrying the `flf-submission` tag that marks the as-submitted state, which is a worse trade than the low-severity residue above. Anyone auditing the as-submitted artifacts should use that tag and expect the original paths there.

## Reproducing the scan

The redactor computes its own untouchable set rather than trusting a list — any tracked file whose own sha256 appears anywhere in the repo is skipped and reported:

```bash
python3 <minelit>/flf-epistack/scripts/redact_vault_paths.py . --dry-run \
  --exclude 'eval/peer-reconciliation-v010/*' \
  --exclude 'eval/e2e-cell/detect*.py' \
  --exclude 'eval/measurements/p3-provenance/link_ledger.py' \
  --exclude '*freeze-manifest.txt' --exclude '*.sha256'
```

Expected on a clean tree: `0 file(s) would be redacted`, **22 skipped as hash-bound, 11 skipped by `--exclude`** (the 7 v0.10 files and the 4 manifests; the three parameterized scripts no longer contain a prefix, so they are not reported), and `remaining files still containing a private prefix: 33`.

Any number above 0 in the first line means a new leak has entered the export — treat that as a release blocker.
