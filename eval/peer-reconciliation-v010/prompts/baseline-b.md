Two research communities (A and B) use their own vocabularies. Below is one term from community A with the excerpts showing how A uses it, followed by community B's full corpus.

COMMUNITY A TERM: "{TERM_A}"

HOW A USES IT (excerpts):
{A_EXCERPTS}

COMMUNITY B CORPUS:
{B_CORPUS}

Return ONLY these four fields, one per line, and nothing else:
match: yes | no
matched_term: the exact community-B term string you judge to be the match, copied verbatim from B's corpus (or none)
relation: exact | A-broader | B-broader | partial-overlap | n/a
evidence: one quoted span copied verbatim from B's corpus (or none)

Rules: answer "yes" only if a specific community-B term names the same concept, a broader concept, or a narrower concept than the community-A term. When match is yes, matched_term and evidence must be non-empty and copied verbatim from B's corpus, and relation must be one of exact / A-broader (the community-A term is broader) / B-broader (the matched community-B term is broader) / partial-overlap. When match is no, set matched_term to none, relation to n/a, and evidence to none.
