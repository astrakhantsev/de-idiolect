You are verifying model-proposed citations against primary sources for a provenance study. For EACH work below, follow this frozen protocol:

1. Locate the primary source: up to 3 search queries (WebSearch) + up to 2 page fetches per work. Fetch pages with the BARE `safefetch <url>` command via Bash — never WebFetch, never curl. If the natural page is unreachable, try the Wayback Machine (https://web.archive.org/web/2024/<url>). Then stop.
2. Grade three facets:
   - exists: "yes" | "no" | "unverifiable" — does a published work matching this citation exist?
   - biblio: "full" (authors + venue + year all match; year exactly) | "minor" (year off by 1, OR journal-vs-proceedings variant, OR subtitle truncation — note which) | "major" (wrong venue, wrong authors, or year off by more than 1) | null if exists != yes
   - per-occurrence claim_support: "supported" (the attributed claim is plausibly present at abstract/title level of the located primary) | "not_locatable" (work exists but the claim is not visible at abstract/title level) | "contradicted" (the abstract/title actively contradicts the attribution) — one verdict per occurrence listed under the work.
3. Receipts REQUIRED: for every exists=yes verdict, record the URL you fetched and a VERBATIM snippet (title line or abstract sentence) from the fetched page that supports your biblio + claim verdicts. No snippet = downgrade to unverifiable.
4. Do NOT judge whether the work truly "owns" the concept — only existence, bibliography, and whether the attributed claim is plausibly in it.

Append your verdicts as JSON lines to the output file given below, one line per work, schema:
{"work_id": "...", "exists": "...", "biblio": "...", "biblio_notes": "...", "primary_url": "...", "evidence_snippet": "...", "occurrences": [{"occ_id": "...", "claim_support": "...", "note": "..."}], "queries_used": N, "fetches_used": N}

Work through the list IN ORDER, writing each verdict line as you complete it (append as you go — do not batch at the end). Your final report: counts by exists/biblio grade + the output file path.

OUTPUT FILE: /mnt/f/src/minelit/flf-epistack/eval/measurements/p3-provenance/verify-batch-1.jsonl

## Works to verify

### w-033
{
 "first_author": "Brams",
 "authors": "Brams & Fishburn",
 "year": 1978,
 "title": "Approval Voting",
 "venue": "American Political Science Review 72",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-033: attributed_claim = "Foundational treatment of approval voting: each rater endorses a set of candidates rather than one." (hedged=False); source quote: "Brams & Fishburn (1978), \"Approval Voting,\" *American Political Science Review* 72;"
- occ_id rec-080: attributed_claim = "The founding paper of approval voting, introducing 'vote for as many candidates as you approve of.'" (hedged=False); source quote: "Brams, S. J., & Fishburn, P. C. (1978). \"Approval Voting.\" *American Political Science Review*, 72(3), 831\u2013847. \u2014 The founding paper; introduces \"vote for as many candidates as you approve of.\" (Confirmed via APSR/Cambridge Core.)"

### w-036
{
 "first_author": "Kittler",
 "authors": "Kittler et al.",
 "year": 1998,
 "title": "On Combining Classifiers",
 "venue": "TPAMI",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-053: attributed_claim = "Canonical classifier-combination framework." (hedged=False); source quote: "Kittler, J., Hatef, M., Duin, R. P. W., & Matas, J. (1998). \"On Combining Classifiers.\" *IEEE TPAMI*, 20(3), 226\u2013239. \u2014 canonical classifier-combination framework. (Verified as real; page/vol high confidence.)"

### w-043
{
 "first_author": "Good",
 "authors": "Good",
 "year": 1983,
 "title": "Good Thinking",
 "venue": "Univ. of Minnesota Press",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-044: attributed_claim = "Origin of the 'device of imaginary results,' the reverse-Bayes ancestor." (hedged=False); source quote: "Good, *Probability and the Weighing of Evidence* (Griffin, 1950) for the additive log-odds/weight-of-evidence form, and *Good Thinking* (Univ. of Minnesota Press, 1983) for the \"device of imaginary results,\" which is the reverse-Bayes ancestor."

### w-050
{
 "first_author": "Brier",
 "authors": "Brier",
 "year": 1950,
 "title": "Verification of forecasts expressed in terms of probability",
 "venue": "Monthly Weather Review 78",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-093: attributed_claim = "Origin of the Brier score, ancestor of the skill-score (fraction of achievable improvement) framing." (hedged=False); source quote: "Brier, \"Verification of Forecasts Expressed in Terms of Probability,\" *Monthly Weather Review*, 1950 \u2014 origin of the Brier score, the ancestor of \"skill score\" (fraction of achievable improvement) framings."
- occ_id rec-043: attributed_claim = "Origin of the Brier score." (hedged=False); source quote: "Brier, G. W. (1950). \"Verification of Forecasts Expressed in Terms of Probability.\" *Monthly Weather Review* 78(1): 1\u20133. \u2014 origin of the Brier score."

### w-052
{
 "first_author": "Murphy",
 "authors": "Murphy",
 "year": null,
 "title": null,
 "venue": "Monthly Weather Review",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-056: attributed_claim = "Canonical 'name your reference' cite: a skill score is uninterpretable without a stated reference forecast." (hedged=True); source quote: "Murphy also has a mid-to-late-1980s *Monthly Weather Review* paper on the interpretation of skill scores that is the canonical \"name your reference\" cite \u2014 I'm confident such a paper exists, less confident of the exact year."

### w-055
{
 "first_author": "Raiffa",
 "authors": "Raiffa & Schlaifer",
 "year": 1961,
 "title": "Applied Statistical Decision Theory",
 "venue": "Harvard Business School",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-040: attributed_claim = "Origin of expected value of (perfect) information in decision theory." (hedged=True); source quote: "**Raiffa, H. & Schlaifer, R. (1961).** *Applied Statistical Decision Theory.* Harvard. \u2014 origin of expected value of (perfect) information. (High confidence; not re-fetched.)"

### w-056
{
 "first_author": "Howard",
 "authors": "Howard",
 "year": 1966,
 "title": "Information value theory",
 "venue": "IEEE Trans. Systems Science and Cybernetics",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-091: attributed_claim = "Foundational EVPI/EVSI (expected value of perfect/sample information) framing." (hedged=False); source quote: "Ronald A. Howard, \"Information Value Theory,\" *IEEE Transactions on Systems Science and Cybernetics*, 1966 \u2014 foundational EVPI/EVSI framing."

### w-059
{
 "first_author": "Vickers",
 "authors": "Vickers & Elkin",
 "year": 2006,
 "title": "Decision curve analysis",
 "venue": "Medical Decision Making 26",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-063: attributed_claim = "Modern framing of whether a model is worth using at all versus a default." (hedged=False); source quote: "Vickers & Elkin, \"Decision curve analysis,\" *Medical Decision Making* 26 (2006), for the modern \"is this model worth using at all, versus a default\" framing."

### w-061
{
 "first_author": "Tanner",
 "authors": "Tanner & Swets",
 "year": 1954,
 "title": "A decision-making theory of visual detection",
 "venue": "Psychological Review 61",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-217: attributed_claim = "Early signal detection theory formalization of the sensitivity/criterion separation." (hedged=False); source quote: "Tanner & Swets (1954), \"A decision-making theory of visual detection,\" *Psychological Review* 61(6);"

### w-062
{
 "first_author": "Chow",
 "authors": "Chow",
 "year": 1957,
 "title": "An optimum character recognition system using decision functions",
 "venue": "IRE Trans. Electronic Computers",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-067: attributed_claim = "Origin of classification with a reject option (Chow's rule)." (hedged=False); source quote: "Chow, \"An optimum character recognition system using decision functions,\" *IRE Trans. Electronic Computers* (1957), and \"On optimum recognition error and reject tradeoff,\" *IEEE Trans. Information Theory* 16(1) (1970)."

### w-071
{
 "first_author": "Brams",
 "authors": "Brams & Fishburn",
 "year": 1983,
 "title": "Approval Voting",
 "venue": "Birkh\u00e4user",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id def-079: attributed_claim = "Book-length treatment of approval voting." (hedged=False); source quote: "Brams & Fishburn, \"Approval voting,\" *American Political Science Review* 72(3) (1978), and their book *Approval Voting* (Birkh\u00e4user, 1983)."

### w-077
{
 "first_author": "Good",
 "authors": "Good",
 "year": 1985,
 "title": "Weight of Evidence: A Brief Survey",
 "venue": "Bayesian Statistics 2",
 "urls": []
}
Occurrences (verify each attributed claim):
- occ_id rec-005: attributed_claim = "A brief survey of the weight-of-evidence concept." (hedged=False); source quote: "(See also **Good, 1985**, \"Weight of evidence: a brief survey,\" *Bayesian Statistics 2*.)"
