## Findings

I could not find the exact phrase "cold-start operating requirement" or "audit unit" used this way in any established literature — confirming the prompt's framing that this is the project's own coined vocabulary, not a term of art itself. Based on what the phrase describes (a monitoring/auditing component that cannot begin validly operating — i.e., flagging deviations — until it has accumulated a minimum baseline of observations), the best-supported mapping is to the **cold-start / training-period requirement** in anomaly-based monitoring systems, with a close structural analog in simulation science.

### 1. Standard name(s)
- **"Cold-start problem"** — the general, cross-disciplinary name for a data-driven system's inability to make valid inferences before it has accumulated sufficient initial data.
- In the specific domain that best matches "audit unit" (a component operating over *audit data*/audit trails), the concrete instantiation is the **"training period"** (also called the "learning phase" or "baseline period") required before an anomaly-based intrusion-detection system can begin detecting deviations.
- The structurally identical problem in operations research/simulation is called the **"warm-up period"** or **"initialization bias" / "problem of the initial transient."**

### 2. Field(s) that own it
- **Computer security** — anomaly-based intrusion detection / audit-trail analysis (closest match to "audit unit," since classical IDS literature literally analyzes streams of "audit records").
- **Machine learning / recommender systems** — origin and popularization of the term "cold start."
- **Operations research / discrete-event simulation** — independent, older tradition covering the same underlying statistical phenomenon (bias from arbitrary initial conditions) under different vocabulary.

### 3. Canonical treatments
- Dorothy E. Denning, **"An Intrusion-Detection Model,"** *IEEE Transactions on Software Engineering*, SE-13(2), 1987, pp. 222–232. — The foundational audit-trail-based anomaly-detection model; explicitly requires a period of profile-building from audit records before deviation detection is valid. **High confidence** this is genuinely foundational and pre-2015 (it's the field's most-cited origin paper). [An Intrusion-Detection Model (ACM/IEEE)](https://dl.acm.org/doi/10.1109/TSE.1987.232894)
- W. David Kelton & Averill M. Law, **"A New Approach for Dealing with the Startup Problem in Discrete Event Simulation,"** *Naval Research Logistics Quarterly*, 1983. — Canonical early treatment of the "warm-up"/startup bias problem, the OR analog. **Medium confidence** on exact venue/year details — I found this citation via secondary sources, not the primary text itself, so treat the bibliographic details as unverified.
- Andrew I. Schein, Alexandrin Popescul, Lyle H. Ungar, David M. Pennock, **"Methods and Metrics for Cold-Start Recommendations,"** *Proceedings of SIGIR 2002*, pp. 253–260. — Widely credited with coining/establishing "cold-start" as a term of art in ML. **High confidence** (verified directly via ACM DL/dblp).
- NIST SP 800-94, *Guide to Intrusion Detection and Prevention Systems (IDPS)*, 2007 — modern operational-standards-level treatment of baseline/profile establishment for anomaly-based IDPS. **Medium confidence** relevance — it's real and on-topic but post-2007, offered as a practitioner-facing supplement, not the "oldest" source.

### 4. Confidence and hedges
- **Low-to-medium confidence overall** that I've identified the *specific* concept intended, because "audit unit" is not itself an established term — I'm inferring the field (security/audit monitoring) from that word choice alone. If "audit unit" in the source project actually means something else (e.g., a financial-audit sampling unit, a hardware self-test/BIT unit, or a distributed-systems "audit" process as in Kopetz's time-triggered protocol cold-start algorithms), the correct established analogue would differ, and I did not find enough context to rule those out.
- **High confidence** that "cold start" as vocabulary originates in the ML/recommender-systems literature (Schein et al. 2002) and that Denning (1987) is the canonical root of audit-trail-based anomaly detection requiring a training period.
- **Low confidence** on the Kelton & Law (1983) full citation details (I did not open the primary source, only saw it referenced secondhand).

Sources:
- [An Intrusion-Detection Model — IEEE/ACM](https://dl.acm.org/doi/10.1109/TSE.1987.232894)
- [Methods and Metrics for Cold-Start Recommendations (SIGIR 2002)](https://dl.acm.org/doi/10.1145/564376.564421)
- [dblp: Methods and metrics for cold-start recommendations](https://dblp.org/rec/conf/sigir/ScheinPUP02.html)
- [Factors affecting warm-up periods in discrete event simulation (Grassmann, 2014)](https://journals.sagepub.com/doi/10.1177/0037549713508334)
- [NIST SP 800-94, Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/pubs/sp/800/94/final)
- [An Introduction to Intrusion Detection (Sundaram)](https://www.engineering.iastate.edu/~guan/course/backup-0982/CprE-592-YG-Fall-2002/paper/intrusion/Intrusion-Detection-Intro.pdf)
