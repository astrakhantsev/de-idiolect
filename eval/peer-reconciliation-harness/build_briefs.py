#!/usr/bin/env python3
"""Mechanically build gen-community-{a,b}.md briefs from a key's concepts.json —
so a sealed key's descriptions never pass through the orchestrator.
Usage: build_briefs.py <workspace_dir>"""
import json, random, sys
from pathlib import Path

ws = Path(sys.argv[1])
k = json.load(open(ws / "key/concepts.json"))
pairs = k["pairs"]

HEAD = {
    "a": "You are writing posts for a practitioner web forum where engineers who build and evaluate LLM agents swap war stories. This community has its own slang, listed below. Write EXACTLY 11 forum posts.\n\nTHE COMMUNITY'S TERMS (its own coinages — use them exactly as given, no synonyms, no abbreviations, no other names for these ideas):\n",
    "b": "You are writing short excerpts from method-and-results sections of preprints by a research group that studies the evaluation of LLM agents. This group has its own technical vocabulary, listed below. Write EXACTLY 11 excerpts.\n\nTHE GROUP'S TERMS (its own coinages — use them exactly as given, no synonyms, no abbreviations, no other names for these ideas):\n",
}
RULES = {
    "a": "\nRULES:\n- Register: informal practitioner forum — first person, concrete incidents, disagreements, numbers, tool names you invent. Each post 150–300 words with a short title.\n- NEVER define the terms. No \"X is when…\", \"X means…\", \"X refers to…\", \"so-called\", no glossaries. Use each term the way an insider uses jargon: in passing, while talking about a concrete situation.\n- Each of the 10 terms must be used in AT LEAST 4 different posts, with at least 2 sentences naturally using the term in each of those posts. Each post should feature 2–4 of the terms. Each of posts 9, 10, 11 must use at least 5 of the terms.\n- Use each term ONLY for its listed meaning. Do not coin any additional jargon for these ideas.\n- Do not mention that these are coined terms, do not mention other groups, vocabularies, or anything about naming.\n- Output format, exactly: each post starts with a line `<<<DOC NN>>>` (NN = 01..11), then `# Title`, then the body. No other framing text before, between, or after.\n",
    "b": "\nRULES:\n- Register: impersonal preprint prose — setup, procedure, quantitative results, limitations. Invented datasets, model names, and numbers are fine. Each excerpt 150–300 words with a short section-style title.\n- NEVER define the terms. No \"X is defined as…\", \"X refers to…\", \"we call this X\", no glossaries. Use each term as established in-group vocabulary while reporting concrete procedures and findings.\n- Each of the 10 terms must be used in AT LEAST 4 different excerpts, with at least 2 sentences naturally using the term in each of those excerpts. Each excerpt should feature 2–4 of the terms. Each of excerpts 9, 10, 11 must use at least 5 of the terms.\n- Use each term ONLY for its listed meaning. Do not coin any additional vocabulary for these ideas.\n- Do not mention other groups, vocabularies, or anything about naming.\n- Output format, exactly: each excerpt starts with a line `<<<DOC NN>>>` (NN = 01..11), then `# Title`, then the body. No other framing text before, between, or after.\n",
}
for side in ("a", "b"):
    entries = [(p[side]["term"], p[side]["desc"]) for p in pairs]
    rnd = random.Random(20260719 if side == "b" else 1)
    if side == "b": rnd.shuffle(entries)
    body = HEAD[side] + "\n" + "\n".join(f'{i+1}. "{t}" — {d}' for i, (t, d) in enumerate(entries)) + "\n" + RULES[side]
    (ws / f"prompts/gen-community-{side}.md").write_text(body)
print("briefs written (descriptions untouched by orchestrator)")
