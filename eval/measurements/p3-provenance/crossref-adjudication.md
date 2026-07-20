# Crossref re-check — manual adjudication (review fold; EXPLORATORY, labeled)

The automated fuzzy matcher (`crossref_recheck.py`) reported 20/23 matches without enforcing author compatibility. Manual adjudication of every match against the cited work (title + author + year + artifact type):

| work | cited | crossref hit | verdict |
|---|---|---|---|
| w-016 | Thompson & Fearn 1996 | The Analyst 1996 | CLEAN |
| w-050 | Brier 1950, Monthly Weather Review | 10.1175/1520-0493(1950)078<0001 | CLEAN (canonical) |
| w-061 | Tanner & Swets 1954, Psych. Review | 10.1037/h0058700 | CLEAN (canonical) |
| w-062 | Chow 1957, IRE Trans. EC | 10.1109/tec.1957.5222035 | CLEAN |
| w-085 | Hoekstra 2010, Semantic Web | 10.3233/sw-2010-0004 | CLEAN |
| w-100 | Marcus & Davis 2015, CACM "Commonsense Reasoning…" | 10.1145/2701413 (CACM 2015) | CLEAN |
| w-108 | Star & Griesemer 1989 | 10.1177/030631289019003001 | CLEAN (canonical) |
| w-111 | Feigenbaum 1984, Annals NYAS | 10.1111/j.1749-6632.1984.tb16513.x | CLEAN |
| w-207 | Furnas et al. 1987, CACM | 10.1145/32206.32212 | CLEAN (canonical) |
| w-225 | Niehoff 1976, Battelle REPORT | JASIS 1976 article | VARIANT — same project, different artifact |
| w-228 | Doan et al., GLUE | 10.1038/news020624-3 "Tunable glue" | SPURIOUS |
| w-242 | Bréal 1897 | undated data DOI | SPURIOUS |
| w-253 | Lenzerini 2002, PODS | 10.1145/543613.543644 | CLEAN (canonical) |
| w-259 | Batini et al. 1986, ACM Comp. Surveys | 10.1145/27633.27634 | CLEAN |
| w-338 | DeGroot & Fienberg 1983, The Statistician | 10.2307/2987588 | CLEAN |
| w-372 | Woods et al. 1997, IEEE TPAMI | 10.1109/34.588027 | CLEAN |
| w-382 | Hertzum & Jacobsen 2001, IJHCI | 10.1207/s15327590ijhc1304_05 | CLEAN |
| w-388 | Conitzer & Sandholm 2005, "Common Voting Rules as Maximum Likelihood Estimators" (UAI) | "Communication complexity of common voting rules" (EC'05) | SPURIOUS — different same-author-same-year paper |
| w-390 | Coombs 1953, EPM 13(2) | 10.1177/001316445301300214 (EPM 1953) | CLEAN |
| w-398 | Chapin 1910, Wiley BOOK | Public Health journal item | SPURIOUS — journal item (likely review), not the book |

No match (3): w-006 (Ranjan & Gneiting 2010 — real JRSS-B paper, fuzzy query missed), w-151 (Bilac 2004 — workshop venue outside Crossref), w-343 (Brier 1950 duplicate work-record; its twin w-050 matched cleanly).

**Adjudicated totals: 15 CLEAN + 1 VARIANT + 1 duplicate-of-clean ≈ 16–17 of 23 access-unverifiable works corroborated bibliographically; 4 spurious fuzzy hits; none shows evidence of nonexistence.** This supports "attrition is access-dominated" qualitatively; it is NOT a precise existence rate (fuzzy matching, author field not enforced, Crossref coverage gaps).
