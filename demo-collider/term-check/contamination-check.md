# Term-check contamination check

Term selection was **answer-aware and criterion-driven**, and the criterion is committed here, exactly as `hook/example/` scores against `GLOSSARY.md`. A per-term isolated check only means something if the term's frozen excerpts contain **none of the expected owner's vocabulary** — a hit would prove the model read the answer off the page, not from weights. Each candidate below was dry-run first (`term-check.sh --dry-run`) and its excerpts grepped for the owner terms.

## Scored (clean — excerpts contain none of the expected owner vocabulary)

| Term | Side | Expected owner (the closed case's answer) | Owner vocab in excerpts? |
|---|---|---|---|
| `accretion slow-down` | A theory | accretion drag / Bondi–Hoyle–Lyttleton; *dynamical friction* is the excerpt's separate "Coulomb slow-down" | none (`dynamical friction`/`Chandrasekhar`/`drag` absent) |
| `macroscopic absorption` | B bounds | Bondi accretion (the theory-side mechanism) / continuum-vs-kinetic crossover | none (`Bondi`/`Hoyle`/`Lyttleton` absent) |
| `crust penetration time` | B bounds | gravitational settling / stopping in dense matter | none (`stopping power`/`Bethe`/`energy loss` absent) |
| `multiple bounds argument` | C critique | defense-in-depth / robustness / convergent evidence | none (`independent`/`convergent`/`defense in depth` absent) |

## Excluded for contamination (excerpt names the owner — a check would prove nothing)

| Term | Side | Why excluded |
|---|---|---|
| `quasistable` | C | its two excerpt paragraphs use **"metastable"** — the owner term itself |
| `grey area` | C | its excerpts state the argument may be **"flawed"/"unsound"** — the owner concept (probability an argument is unsound) verbatim |

Both are genuine side-local terms (marked `[x]` in the scan curation) and would have been easy "hits," which is exactly why they are excluded: an answer-aware demonstration must not score a term whose answer is sitting in its own excerpts.
