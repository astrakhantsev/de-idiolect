## Findings

**1. Standard name(s)**
The core idea — a monitoring/detection component cannot produce valid output until it has accumulated enough historical data to establish a baseline — is the **cold-start problem**. Depending on which field's audit/monitoring context it's applied in, it also goes by:
- **"Training period" / "learning phase" requirement** (statistical anomaly-based intrusion detection)
- **"Warm-up period" / "initialization bias"** (discrete-event simulation and queueing systems — an older, distinct lineage of essentially the same idea)
- **"Baseline period"** (fraud/transaction-monitoring practitioner literature)

I found no established term that specifically pairs "operating requirement" with "cold-start" — that phrasing looks like the project's own plain-English description layered on top of the underlying (well-established) cold-start/warm-up concept, not itself a term of art.

**2. Field(s) that own it**
- Machine learning / recommender systems — where the term "cold-start problem" was coined and is most canonical.
- Computer security — anomaly-based intrusion detection, which historically built statistical behavior profiles directly from **audit records** (hence the strong resonance with "audit unit").
- Fraud detection / AML transaction monitoring — practitioner literature explicitly calls this a "cold-start challenge" for new accounts with no history.
- Operations research / discrete-event simulation — the older, parallel concept of "initialization bias" requiring a warm-up period before steady-state statistics are valid.

**3. Oldest / most canonical treatments**
- Denning, D.E. (1987). *An Intrusion-Detection Model.* IEEE Transactions on Software Engineering, SE-13(2), 222–232. — The foundational paper for statistical anomaly detection built from **audit records**; explicitly requires accumulating observations before a behavioral profile is usable. This is the closest historical/terminological match to "audit unit."
- Conway, R.W. (1963). *Some Tactical Problems in Digital Simulation.* Management Science, 10(1), 47–61. — Earliest canonical treatment of the initial-transient (warm-up) problem.
- Welch, P.D. (1983). *The Statistical Analysis of Simulation Results.* In *The Computer Performance Modeling Handbook* (S. Lavenberg, ed.), Academic Press. — Canonical method ("Welch's method") for determining warm-up length.
- Schruben, Singh & Tierney (1983). *Optimal Tests for Initialization Bias in Simulation Output.* Operations Research, 31(6), 1167–1178.
- Schein, A.I., Popescul, A., Ungar, L.H., Pennock, D.M. (2002). *Methods and Metrics for Cold-Start Recommendations.* SIGIR '02, pp. 253–260 (DOI 10.1145/564376.564421). — The paper most credited with formalizing "cold-start" in the modern ML sense (post-2015 cutoff for "oldest," but it's the term's own origin point).

**4. Confidence**
- **High confidence**: "Cold-start problem" is a real, well-documented, cross-field concept with solid canonical citations — this part is not in doubt.
- **Medium confidence**: that the project's "audit unit" specifically denotes an anomaly/behavioral-monitoring component in the Denning/IDS sense — I don't have the project's own context beyond the quoted sentence, so this mapping is my best inference from vocabulary, not confirmed.
- **Low-medium confidence, explicitly hedged**: whether the project means the ML/recommender flavor (Schein et al.) or the simulation-warm-up flavor (Conway/Welch) — both are legitimate, older, independent lineages of essentially the same underlying idea, and the one-sentence description doesn't disambiguate which the project intended.
- **Not found**: any standard term literally called "operating requirement" tied to cold-start — treat that phrase as the project's own coinage describing the requirement, not an established term itself.

Sources:
- [From Zero to Hero: Cold-Start Anomaly Detection](https://arxiv.org/html/2405.20341v1)
- [Cold Start for Cloud Anomaly Detection | IEEE Xplore](https://ieeexplore.ieee.org/document/10154340/)
- [An Intrusion-Detection Model | IEEE Transactions on Software Engineering (ACM DL)](https://dl.acm.org/doi/10.1109/TSE.1987.232894)
- [An Intrusion-Detection Model, Dorothy E. Denning (full text PDF)](https://www.cs.colostate.edu/~cs656/reading/ieee-se-13-2.pdf)
- [The Problem of the Initial Transient: Techniques for Estimating the Warm-up Period for Discrete-Event Simulation Models](https://www.academia.edu/2849291/The_Problem_of_the_Initial_Transient_Techniques_for_Estimating_the_Warm_up_Period_for_Discrete_Event_Simulation_Models)
- [Analysis of the behavior of the transient period in non-terminating simulations - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0377221705000093)
- [Methods and metrics for cold-start recommendations | ACM SIGIR 2002 (DOI)](https://dx.doi.org/10.1145/564376.564421)
- [Methods and Metrics for Cold-Start Recommendations (Penn repository postprint)](https://repository.upenn.edu/cis_papers/135/)
- [Overcome the machine learning cold start challenge in fraud detection using Amazon Fraud Detector](https://aws.amazon.com/blogs/machine-learning/overcome-the-machine-learning-cold-start-challenge-in-fraud-detection-using-amazon-fraud-detector/)
