"""LLM backend for the recall-extender prototype.

Two generative steps need an LLM: (2) constrained-definition generation and
(3b) pairwise SKOS relation typing. This module exposes a real interface for both,
with two backends:

  - 'claude'   : shell out to `claude -p` (headless Claude Code). This is the live
                 path. At build time (2026-07-17) it returned "Usage credits are
                 required for this model" (Max weekly cap exhausted), so the worked
                 run used the 'fixtures' backend instead. The interface is real and
                 will work once quota resets or an API-keyed backend is added.
  - 'fixtures' : return author-frozen outputs (definitions from concepts.json,
                 relations from relation_fixtures.json). Deterministic, offline,
                 zero-cost; lets the pipeline run end-to-end and reproducibly today.

The retrieval step (3) is NOT in this module — it runs on a real local embedding
model (bge-large-en-v1.5) with no LLM and no network, and is the load-bearing,
non-fixture measurement.
"""
from __future__ import annotations
import json, subprocess, shutil, textwrap
from pathlib import Path

HERE = Path(__file__).parent
SKOS_LABELS = ["exactMatch", "broadMatch", "narrowMatch", "relatedMatch"]

DEFINE_PROMPT = """You are generating a community-neutral operational definition of a term as it is used by one research community, to be used as a cross-community search key.

Write a short (2-4 sentence) definition of the term below, describing: what kind of thing it names, what goes in and what comes out, what it asserts or does, and when it applies.

HARD CONSTRAINTS:
- Use only plain, common English words plus simple mathematical notation.
- Do NOT use the term itself, any proper name (person, method, product, dataset), or the name of any field of study.
- Do NOT name the community. The definition must read the same to any community that works on the same underlying thing.

TERM: {term}
CONTEXT (how this community writes about it):
{context}

Output ONLY the definition text, nothing else."""

RELATION_PROMPT = """You label the relation between a community-neutral concept definition and a candidate document from another community, using exactly one SKOS mapping-relation label.

Labels: exactMatch (same underlying thing), broadMatch (the document is about a more general thing), narrowMatch (the document is about a more specific thing), relatedMatch (associated but not the same, more-general, or more-specific).

CONCEPT DEFINITION:
{definition}

CANDIDATE DOCUMENT:
{doc}

Output ONLY one label from {{exactMatch, broadMatch, narrowMatch, relatedMatch}}, then a colon and a <=15-word reason."""


def _claude(prompt: str, model: str = "sonnet", timeout: int = 120) -> str | None:
    """Call `claude -p` headless with all tools denied (pure text generation)."""
    if not shutil.which("claude"):
        return None
    try:
        proc = subprocess.run(
            ["claude", "-p", "--model", model,
             "--allowedTools", "", "--disallowedTools",
             "Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch,WebSearch,Bash"],
            input=prompt, capture_output=True, text=True, timeout=timeout,
        )
        out = (proc.stdout or "").strip()
        if proc.returncode != 0 or not out or "Usage credits are required" in out:
            return None
        return out
    except Exception:
        return None


class Backend:
    def __init__(self, kind: str = "fixtures", model: str = "sonnet", concepts_path: str | Path | None = None,
                 custom_run: bool = False):
        assert kind in ("claude", "fixtures")
        self.kind = kind
        self.model = model
        # NOTE: defaults to the shipped eggs concepts.json for backward compatibility, but a caller
        # passing --concepts (e.g. a user's own corpus) should pass that same path here too, so the
        # fixtures fallback below (and any hand-supplied constrained_definition it reads) matches the
        # concepts actually being run rather than silently falling back to the eggs fixtures.
        concepts_path = Path(concepts_path) if concepts_path else HERE / "concepts.json"
        self._concepts = {c["term"]: c for c in json.loads(concepts_path.read_text())["concepts"]}
        # custom_run=True (custom --corpus and/or --concepts, or --define-only) disables
        # relation_fixtures.json entirely in type_relation() below: that file's keys are
        # "{eggs term}||{eggs doc_id}" pairs, and a custom run's own term/doc_id could coincidentally
        # collide with one of them, silently returning a frozen EGGS judgment mislabeled as
        # "source: fixture" for unrelated data. Custom runs fall straight through to the generic
        # labeled default instead (source: "fixture-default"); only the shipped eggs run (this flag
        # False) may use relation_fixtures.json.
        self.custom_run = custom_run
        rf = HERE / "relation_fixtures.json"
        self._relations = json.loads(rf.read_text()) if (not custom_run and rf.exists()) else {}

    def define(self, term: str, context: str) -> tuple[str, str]:
        """Return (definition, source) where source in {'live','fixture'}."""
        if self.kind == "claude":
            out = _claude(DEFINE_PROMPT.format(term=term, context=textwrap.shorten(context, 1200)), self.model)
            if out:
                return out, "live"
        # fixtures fallback: a hand-supplied 'constrained_definition' in the concepts file being run
        rec = self._concepts.get(term)
        if rec and rec.get("constrained_definition"):
            return rec["constrained_definition"], "fixture"
        raise RuntimeError(
            f"No definition available for term {term!r}: backend={self.kind!r} produced nothing live, "
            f"and no 'constrained_definition' was found for it in the concepts file. Either hand-supply "
            f"'constrained_definition' for this term in your --concepts file, or run with --backend claude."
        )

    def type_relation(self, definition: str, doc_id: str, doc_text: str, concept_term: str) -> tuple[str, str, str]:
        """Return (label, reason, source)."""
        if self.kind == "claude":
            out = _claude(RELATION_PROMPT.format(definition=definition, doc=doc_text), self.model)
            if out:
                label = out.split(":")[0].strip()
                if label in SKOS_LABELS:
                    reason = out.split(":", 1)[1].strip() if ":" in out else ""
                    return label, reason, "live"
        key = f"{concept_term}||{doc_id}"
        rec = self._relations.get(key)
        if rec:
            return rec["label"], rec.get("reason", ""), "fixture"
        return "relatedMatch", "(no fixture; default)", "fixture-default"
