## Short version

I could not find this phrase, or any standardized term matching it, in the literature — a literal search for "cold-start operating requirement" + "audit unit" returns only unrelated cold-storage/cold-weather audits. So this is **coined vocabulary that I'm mapping by meaning, not a phrase I can match to a canonical name**. Read plainly, it describes: *the thing a checking/verifying unit must be given at the very outset (from a cold, zero state) in order to operate at all, because it cannot produce or check that thing itself.* Under that reading there is a well-established concept, with two homes — a concrete engineering one and an abstract philosophical one. I give both, with real citations, and flag my confidence as **moderate on the mapping, high on the citations**.

---

## 1. Standard name(s)

- **Primary (engineering/systems):** **Root of trust** — and its near-synonym **trust anchor**. This is the element at the base of a chain of trust that a verifying/attesting component ("audit unit") must trust *implicitly at boot* ("cold start") because nothing beneath it exists to vouch for it. NIST defines a trust anchor as literally *"an authoritative entity for which trust is assumed"* and *"the base of a tree of trust… from which an entity begins the validation."* Closely related: **Trusted Computing Base (TCB)** — the set of components that must simply be relied upon.
- **Abstract/general (epistemology):** the **regress problem** and its resolution by **foundationalism** — the doctrine that any justificatory ("audit") chain must terminate in **basic beliefs / axioms / first principles** accepted without further justification. The trilemma form (regress vs. circularity vs. dogmatic foundation) is the **Agrippan trilemma / Münchhausen trilemma**.

Both formalize the same structural fact: *a system that checks things cannot check its own starting point; that starting point is a required, unearned input.*

## 2. Owning field(s)

- **Computer security / trusted computing / cryptography (PKI)** — owns *root of trust*, *trust anchor*, *trusted computing base*. **(Best fit given the "audit/attest at cold-start" framing.)**
- **Epistemology / philosophy of science** — owns *foundationalism*, the *regress problem*, the *Münchhausen/Agrippan trilemma*. (This is the domain-neutral, more fundamental version of the same idea.)
- *Less likely alternative:* **internal audit / assurance**, where "audit unit" and "audit universe" are real terms — but there is no established "cold-start operating requirement" there, so I rate this reading lower.

## 3. Oldest / most canonical treatments (real citations)

**Trusted computing (root of trust / TCB):**
- U.S. DoD, *Trusted Computer System Evaluation Criteria* ("Orange Book"), DoD 5200.28-STD, **1983/1985** — origin of the **Trusted Computing Base** concept (components that must be trusted). *[High confidence it's the canonical TCB source; verify exact edition year.]*
- Garfinkel, Pfaff, Chow, Rosenblum & Boneh, **"Terra: A Virtual Machine-Based Platform for Trusted Computing,"** *SOSP 2003* — canonical early trusted-computing / attestation paper. **(pre-2015)**
- Parno, McCune & Perrig, **"Bootstrapping Trust in Commodity Computers,"** *IEEE Symposium on Security and Privacy (Oakland), 2010*; expanded as the book *Bootstrapping Trust in Modern Computers*, Springer, 2011 — the standard survey of exactly "how does a machine's verifier get something to trust at start-up." **(pre-2015; strongest single match to your phrase.)**
- **Trust anchor** specifically: NIST glossary (grounded in NIST SP 800-57 and CNSSI 4009); IETF **RFC 5914** *Trust Anchor Format* (2010) and **RFC 6024** *Trust Anchor Management Requirements* (2010). Trusted Computing Group's TPM specifications also codify "Roots of Trust" (RTM/RTS/RTR), early-mid 2000s. *[TCG exact spec version/year — uncertain, hedge.]*

**Epistemology (foundationalism / regress):**
- **Aristotle**, *Posterior Analytics* (~350 BCE) — demonstrative knowledge must rest on first principles known without demonstration. (Oldest canonical statement.)
- **Sextus Empiricus**, *Outlines of Pyrrhonism* (~2nd c. CE) — the **Five Modes of Agrippa**, including the regress and the "hypothesis" (assumed starting point) modes.
- **Hans Albert**, *Traktat über kritische Vernunft* (Tübingen: Mohr Siebeck, **1968**) — coins the **Münchhausen trilemma**; Eng. trans. *Treatise on Critical Reason*, Princeton Univ. Press, 1985.

## 4. Confidence, explicitly hedged

- **That the phrase corresponds to "root of trust / trust anchor": moderate (~55–65%).** The engineering flavor of "cold-start" (boot from off) and "audit unit" (an attesting/checking module) points here, but this is my inference from wording — no source uses this phrasing, so I can't rule out that the author means something narrower or idiosyncratic.
- **That the abstract, field-neutral version is foundationalism / the regress (Münchhausen) trilemma: high as an analogy, uncertain as the author's intent.** If the "audit unit" is a reasoning/justification process rather than a machine, this is the better home.
- **The internal-audit reading (audit charter / independence to stand up an audit function from scratch): low (~15%)** — plausible for "audit unit," but nothing standardizes "cold-start operating requirement" there.
- **The citations themselves: high confidence they are real and canonical** for their respective concepts. Lower-confidence, explicitly flagged items: the exact Orange Book edition year (1983 vs. 1985) and the exact TCG TPM spec version/year.

**Bottom line:** No established term matches the phrase verbatim; the best-supported established concept it maps to is **root of trust / trust anchor** (trusted computing), whose discipline-neutral parent is **foundationalism / the regress (Münchhausen) trilemma** in epistemology — but treat this as a reasoned mapping, not a confirmed identification.

Sources:
- [NIST CSRC Glossary — trust anchor](https://csrc.nist.gov/glossary/term/trust_anchor)
- [GlobalPlatform — Root of Trust Definitions and Requirements v1.1 (2018)](https://globalplatform.org/wp-content/uploads/2018/07/GP_RoT_Definitions_and_Requirements_v1.1_PublicRelease-2018-06-28.pdf)
- [Parno, McCune & Perrig — Bootstrapping Trust in Commodity Computers (2010)](https://netsec.ethz.ch/publications/papers/PaMcPe2010.pdf)
- [Synopsys — What is Root of Trust?](https://www.synopsys.com/glossary/what-is-root-of-trust.html)
- [Root of Trust — ScienceDirect Topics overview](https://www.sciencedirect.com/topics/computer-science/root-of-trust)
- [IETF RFC 6024 — Trust Anchor Management Requirements (2010)](https://www.ietf.org/rfc/rfc6024.txt)
- [Münchhausen trilemma — Wikipedia](https://en.wikipedia.org/wiki/M%C3%BCnchhausen_trilemma)
- [Münchhausen trilemma — nLab](https://ncatlab.org/nlab/show/M%C3%BCnchhausen+trilemma)
- [Pirani — Auditable Units in internal audit](https://www.piranirisk.com/blog/auditable-units-audit)
- [IIA Singapore — Audit Universe and Auditable Units](https://iia.org.sg/Resources/IIAS-Blog/January2026)
