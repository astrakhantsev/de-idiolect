# Peer-reconciliation v0.6 — SEALED TEST KEY (key-3) pre-registration

This workspace is the TEST side of ../peer-reconciliation-harness/PROTOCOL.md. The key was authored by an isolated opus call from the frozen keyspec, validated structurally only (validate_key.py), briefs and leak lists generated mechanically (build_briefs.py, gen_leakcheck.py); the orchestrator has not read the concept descriptions. Rules, thresholds, endpoints, and models are IDENTICAL to the TRAIN v0.6 amendment (../peer-reconciliation-fresh/prereg.md). This key is run at most once, only after a TRAIN v0.6 pass, and its per-pair failures are not diagnosed into design changes while it remains the TEST key.

Known wrinkle, accepted at seal time (rejecting the key on semantic grounds would itself be test iteration): the model-chosen jingle strings "cold start" and "hot swap" are real-world loaded terms; the planted concepts must overcome real priors. Noted for interpretation, not corrected.
