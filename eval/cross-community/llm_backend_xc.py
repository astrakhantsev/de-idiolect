"""LLM generation primitive + query-battery prompts for the cross-community cell.

Self-contained (does not import the sibling recall-extender package): one `claude()`
shell-out to headless `claude -p` with all tools denied, plus the five query-form prompts
of the §1 battery. The prompt structure mirrors the recall-extender ablation
(`ablation_constrained_vs_free.py`) so the constrained/free arms are comparable across cells.

Only query GENERATION uses the LLM. Retrieval + metrics are deterministic (bge-large, offline).
"""
from __future__ import annotations

import shutil
import subprocess

_DENY = "Read,Glob,Grep,Task,Agent,Edit,Write,NotebookEdit,WebFetch,WebSearch,Bash"


def claude(prompt: str, model: str = "sonnet", timeout: int = 150) -> str | None:
    """Headless `claude -p`, pure text generation (all tools denied). None on any failure."""
    if not shutil.which("claude"):
        return None
    try:
        proc = subprocess.run(
            ["claude", "-p", "--model", model, "--allowedTools", "", "--disallowedTools", _DENY],
            input=prompt, capture_output=True, text=True, timeout=timeout,
        )
        out = (proc.stdout or "").strip()
        if proc.returncode != 0 or not out or "Usage credits are required" in out:
            return None
        return out
    except Exception:  # noqa: BLE001 - transient; caller retries / treats None as failure
        return None


# --- Query battery (§1). All generated forms are built from docs_A ONLY (blind to B)
#     and forbid term A itself. Length-matched target so the constrained/free contrast
#     is not confounded by length (the §4c finding).

_SHARED_TASK = (
    "Write a {n_sent}-sentence description of the concept named by the term below, covering: "
    "what kind of thing it is, what goes in and what comes out, what it asserts or does, and "
    "when it applies. Base it ONLY on the excerpts provided."
)

JARGON_PROMPT = (
    "You are writing a precise description of a technical concept as an expert in its field would, "
    "for a specialist reader.\n\n"
    + _SHARED_TASK + "\n\n"
    "Use whatever standard terminology and field vocabulary an expert would normally use.\n"
    "The ONLY constraint: do NOT use the term itself or restate it verbatim (describe it without naming it).\n\n"
    "TERM: {term}\n"
    "EXCERPTS (how this community writes about it):\n{context}\n\n"
    "Output ONLY the description text, nothing else."
)

NEUTRAL_PROMPT = (
    "You are writing a community-neutral operational description of a concept, to be used as a "
    "cross-community search key.\n\n"
    + _SHARED_TASK + "\n\n"
    "HARD CONSTRAINTS:\n"
    "- Use only plain, common English words plus simple mathematical notation.\n"
    "- Do NOT use the term itself, any proper name (person, method, product, place), or the name "
    "of any field of study.\n"
    "- Do NOT name or hint at the community. The description must read the same to any community "
    "that works on the same underlying thing.\n\n"
    "TERM: {term}\n"
    "EXCERPTS (how this community writes about it):\n{context}\n\n"
    "Output ONLY the description text, nothing else."
)
