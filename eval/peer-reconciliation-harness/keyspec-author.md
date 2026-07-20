You are authoring the ground-truth key for a synthetic evaluation of a cross-community concept-matching pipeline. Output ONLY a JSON object, no prose.

Invent 18 FICTITIOUS phenomena/practices in the domain of "evaluating LLM agents and their harnesses." Each must be plausible but invented — do not use real, established named methods, and do not reuse any of these existing terms from prior keys: shuffle fragility, claim survival tally, probe-shadow, missing-key test, pothole runs, notebook yank, drift audit, ghost pass, spend silhouette, menu pinning, permutation sensitivity collapse, intermediate assertion persistence ratio, instrumentation latency steering, specification occlusion, seeded-defect audit, memory paraphrase perturbation, line-anchored rubric, self-contradiction incidence, groove lock, dead weight census, synthetic ladders, squeeze play, twin runs, ouroboros items, echo test, salt run, rig diary, reread ration, trajectory template carryover, item discrimination exhaustion rate, subordinate authoring protocol, resource perturbation study, matched contrast probes, reflexive adjudication, strategy cardinality index, tier floor annotation.

Two communities coin terms: community "a" (informal practitioner-forum slang: short, punchy, 1–3 words) and community "b" (preprint-style technical noun phrases, 2–5 words).

Build EXACTLY this structure — a JSON object {"pairs": [...]} with 10 pairs, pair_id P01..P10:

- P01, P02 — "class": "exactMatch": ONE concept each, described identically for both sides (~50–70 words, operational: what happens, what is measured, when it applies); different coined terms per side.
- P03 — "class": "broadnarrow", "broader_side": "a": side a's concept is a strict superset ("any X, whatever the mechanism"); side b's is a specific sub-case with a concrete mechanism. Write the containment into the descriptions explicitly.
- P04 — "class": "broadnarrow", "broader_side": "b": mirror of P03 (b broad, a narrow).
- P05, P06 — "class": "relatedMatch": each pair = TWO concepts sharing a specific common core (state it in a "core" field) with clearly different per-side residues (state "residue" per side): different mechanism-variant and different metric.
- P07, P08 — "class": "noMatchDespiteSimilarity": both sides use the SAME term string (invent a fresh 1–2 word string per pair) for two UNRELATED concepts.
- P09, P10 — "class": "noMatch": unrelated concepts, dissimilar terms.

Schema per pair: {"pair_id": "...", "class": "...", ("broader_side": "a|b" for broadnarrow,) ("core": "..." for relatedMatch,) "a": {"term": "...", "desc": "..." (, "residue": "..." for relatedMatch)}, "b": {"term": "...", "desc": "..." (, "residue": "...")}}.

Constraints: no term string may appear inside any OTHER pair's descriptions; no term of side a may equal or contain a term of side b (except the two jingle strings, identical by design); every description self-contained, no cross-references, no meta-vocabulary (never use the words: match, broader, narrower, residue, planted, jingle, community).
