A single technical term coined by one research community is shown below, together with the three most similar full documents retrieved from a DIFFERENT community's corpus using that term as the search query.

TERM: "{TERM}"

RETRIEVED DOCUMENTS (other community's corpus; ranked most-similar first):
{RETRIEVED_DOCS}

Return ONLY these four fields, one per line, and nothing else:
match: yes | no
matched_term: the exact other-side term string you judge to be the match, copied verbatim from the documents (or none)
relation: exact | term-broader | corpus-broader | partial-overlap | n/a
evidence: one quoted span copied verbatim from the documents (or none)

Rules: answer "yes" only if a specific other-side term names the same concept, a broader concept, or a narrower concept. When match is yes, matched_term and evidence must be non-empty and copied verbatim from the documents, and relation must be one of exact / term-broader (the shown TERM is broader than the matched other-side term) / corpus-broader (the matched other-side term is broader) / partial-overlap. When match is no, set matched_term to none, relation to n/a, and evidence to none.
