I have enough to answer with confidence. Here is my finding.

## What this concept is

The phrase describes a single well-known idea: **a verification/checking process cannot verify its own starting point, so to begin operating "from cold" it must rest on an unchecked, a‑priori‑trusted foundation.** Parsed against the coined vocabulary: the "audit unit" = whatever does the checking/attesting/justifying; its "cold‑start operating requirement" = the thing it has to be *given* and simply trust before it can run, because there is nothing beneath it to audit it. This is the classic "you have to trust something to get started; the checker can't bootstrap itself" problem. It shows up under two established names depending on which field you read "audit" in.

### 1. Standard name(s)

- **In computer/security engineering (my primary reading, because the phrasing is engineering‑flavored — "operating requirement," "unit," "cold‑start"):** this is the **Root of Trust (RoT)** / **trust anchor**, and specifically the **Core Root of Trust for Measurement (CRTM)** — the immutable code that runs first at power‑on and is *implicitly trusted* to bootstrap the measurement/attestation chain. The impossibility of auditing your way down to it is Ken Thompson's **"trusting trust"** problem; the general activity is **bootstrapping trust / establishing a chain of trust**. The CRTM definition is nearly a literal restatement of your phrase: *the first code at cold boot that must be trusted to bootstrap the audit (measurement/attestation) chain.*
- **In philosophy/epistemology (the deeper, general form, if "audit unit" means the faculty that justifies beliefs):** this is the **epistemic regress problem**, answered by **foundationalism** — you need **basic/foundational beliefs (first principles, axioms)** that are not themselves justified by anything else, or you fall into infinite regress. The three‑way statement of the impasse is **Agrippa's trilemma / the Münchhausen trilemma** (infinite regress, circularity, or a dogmatic un‑audited assumption).

Both are the *same* structural idea — a checking process needs an unchecked ground to operate — instantiated in two disciplines.

### 2. Which field(s) own it

- **Computer security / trusted computing / systems** — owns the "root of trust," "trust anchor," "chain of trust," "trusting trust," "secure/measured boot" vocabulary.
- **Epistemology (philosophy)** — owns the "regress problem," "foundationalism," "first principles," "Münchhausen/Agrippa trilemma."
- Adjacent: **logic/mathematics** (the need for undemonstrated axioms — same shape).

### 3. Oldest and most canonical treatments (real citations)

Security lineage:
- Ken Thompson, **"Reflections on Trusting Trust,"** *Communications of the ACM* 27(8): 761–763, 1984 (ACM Turing Award lecture). The canonical statement that no amount of source‑level auditing lets you trust code from a cold start — you must ultimately trust something you did not verify. ([dl.acm.org](https://dl.acm.org/doi/10.1145/358198.358210), [PDF](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf))
- W. A. Arbaugh, D. J. Farber, J. M. Smith, **"A Secure and Reliable Bootstrap Architecture"** (the AEGIS system), *Proc. 1997 IEEE Symposium on Security and Privacy*, pp. 65–71. Foundational paper on a chain of integrity checks *beginning at power‑on* — i.e., the cold‑start requirement of the checking chain. ([repository.upenn.edu](https://repository.upenn.edu/cis_reports/231/), [PDF](https://www.bennetyee.org/ucsd-pages/Courses/cse227.w02/handouts/arbaugh,farber,smith.a_secure_and_reliable_bootstrap_architecture.pdf))
- **Trusted Computing Group** TPM/TCPA specifications (early 2000s) define **Root of Trust for Measurement** and the **CRTM** as the immutable code trusted at cold boot to seed attestation; see the NIST CSRC glossary entry for CRTM. ([csrc.nist.gov](https://csrc.nist.gov/glossary/term/core_root_of_trust_for_measurement))

Philosophical lineage (older and, in the strict "oldest and most canonical" sense, the deepest roots):
- **Aristotle, *Posterior Analytics*** (c. 350 BCE) — demonstration cannot regress infinitely, so knowledge must rest on indemonstrable first principles grasped by *nous*. The original statement of the regress‑and‑foundation structure.
- **Agrippa's five modes**, preserved in **Sextus Empiricus, *Outlines of Pyrrhonism*** (c. 200 CE) — the trilemma of infinite regress, circularity, or un‑audited hypothesis.
- **Hans Albert, *Treatise on Critical Reason*** (German 1968; English trans. Princeton Univ. Press, 1985) — the modern "Münchhausen trilemma" naming. ([Regress argument overview — Wikipedia](https://en.wikipedia.org/wiki/Regress_argument_(epistemology)))

(At least one pre‑2015 source: several — Thompson 1984, Arbaugh et al. 1997, and Aristotle/Sextus/Albert.)

### 4. Confidence and hedges

- **High confidence** that the underlying established concept is *the impossibility of a checking/justifying process grounding its own starting point → the need for an a‑priori‑trusted foundation to bootstrap from cold.* Your phrase maps onto this cleanly, and the CRTM definition matches it almost word‑for‑word.
- **Medium confidence** on which *field* the project intends. The engineering register ("operating requirement," "unit," "cold‑start") and the word "audit" (integrity‑checking/attestation) point me to **trusted computing → root of trust / trust anchor / CRTM** as the closest single match, so I lead with that. But "audit unit" could equally be a metaphor for the belief‑justifying faculty, in which case the intended concept is the **epistemic regress problem / foundationalism**. I cannot fully disambiguate from the coined phrase alone.
- **Low‑confidence items I'm explicitly flagging:** (a) that the project means integrity‑attestation specifically (vs. general "logging/audit trail," where there is no single famous concept); (b) the exact TCG specification version/year for CRTM — I cite the NIST CSRC definition rather than a pinned spec revision, which I did not open. The Thompson (1984) and Arbaugh et al. (1997) citations, and the Aristotle/Sextus/Albert lineage, I stand behind.

One thing I could *not* confirm: the exact coined phrase "cold‑start operating requirement for the audit unit" returns nothing on the open web (expected — it's the project's private vocabulary), so this mapping is inference from meaning, not a found definition.

Sources:
- [Thompson, "Reflections on Trusting Trust," CACM 1984](https://dl.acm.org/doi/10.1145/358198.358210) · [PDF](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf)
- [Arbaugh, Farber, Smith, "A Secure and Reliable Bootstrap Architecture," 1997 — UPenn repository](https://repository.upenn.edu/cis_reports/231/) · [PDF](https://www.bennetyee.org/ucsd-pages/Courses/cse227.w02/handouts/arbaugh,farber,smith.a_secure_and_reliable_bootstrap_architecture.pdf)
- [NIST CSRC glossary — Core Root of Trust for Measurement](https://csrc.nist.gov/glossary/term/core_root_of_trust_for_measurement)
- [Root of Trust overview — ScienceDirect Topics](https://www.sciencedirect.com/topics/computer-science/root-of-trust)
- [Regress argument (epistemology) — Wikipedia](https://en.wikipedia.org/wiki/Regress_argument_(epistemology))
- [Infinitism / regress problem — Internet Encyclopedia of Philosophy](https://iep.utm.edu/inf-epis/)
