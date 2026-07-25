#!/usr/bin/env python3
"""pin_model.py — the FROZEN alias->pinned-ID translation at the CALL BOUNDARY (v0.10 §6
pinning mechanism). The carried staging functions are held BYTE-IDENTICAL to v0.9 and stage
bare aliases ('opus'/'sonnet') for Claude; the frozen isolation wrapper (run_isolated.sh) is
also untouched. So run_calls.sh translates each row's model to its EXPLICIT pinned ID *here*
immediately before invoking the wrapper — pinning every outcome-bearing Claude call without
editing the carried gates or the wrapper.

  claude aliases:  opus -> claude-opus-4-8 ; sonnet -> claude-sonnet-5
  already-pinned Claude IDs pass through (claude-opus-4-8, claude-sonnet-5)
  codex:           gpt-5.6-terra passes through (already a pinned id)
  anything else:   REJECTED loudly (nonzero) — alias drift cannot silently run a wrong model.

CLI: `pin_model.py <cli> <model>` prints the pinned id on stdout, or errors to stderr + exit 3.
"""
import sys

CLAUDE_ALIAS = {"opus": "claude-opus-4-8", "sonnet": "claude-sonnet-5"}
CLAUDE_PINNED = {"claude-opus-4-8", "claude-sonnet-5"}
CODEX_PINNED = {"gpt-5.6-terra"}


def translate(cli, model):
    """Return the explicit pinned model id, or raise ValueError (loud reject)."""
    if cli == "claude":
        if model in CLAUDE_ALIAS:
            return CLAUDE_ALIAS[model]
        if model in CLAUDE_PINNED:
            return model
        raise ValueError(f"REJECT: unpinnable Claude model {model!r} — allowed aliases "
                         f"{sorted(CLAUDE_ALIAS)} or pinned ids {sorted(CLAUDE_PINNED)}")
    if cli == "codex":
        if model in CODEX_PINNED:
            return model
        raise ValueError(f"REJECT: unpinned codex model {model!r} (only {sorted(CODEX_PINNED)})")
    raise ValueError(f"REJECT: unknown cli {cli!r}")


if __name__ == "__main__":
    try:
        print(translate(sys.argv[1], sys.argv[2]))
    except (IndexError, ValueError) as e:
        print(str(e) if isinstance(e, ValueError) else "usage: pin_model.py <cli> <model>",
              file=sys.stderr)
        sys.exit(3)
