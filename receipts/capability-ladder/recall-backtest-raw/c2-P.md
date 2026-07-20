You are a reference librarian and historian of science. Below is an operational description of a single concept. Your job, using web search, is to identify it.

Report, in order:
1. What is this concept called in established academic or professional fields? Give the standard name(s).
2. Which field(s) own it? Name the discipline(s).
3. What are the oldest and most canonical treatments? Give real citations (author, year, venue). Aim to name at least one source published before 2015.
4. Your confidence for each claim; explicitly hedge anything you are unsure of.

Rules:
- You MUST search the web actively. Do NOT answer from memory alone — run searches, open sources, and cite what you actually find. Use WebSearch and the `safefetch <url>` shell command only. NEVER use WebFetch.
- Do not pad. If you cannot identify it, say so plainly.
- Give exact citations you can stand behind; mark any you are unsure of as uncertain.

The concept:

This is the cold-start operating requirement for an audit unit. Setting: an audit unit forms a final credence by taking a starting credence and adjusting it with a multiplier that scales the pooled evidence lean; the multiplier can be tuned per question or left at a fixed default. The operating requirement states how accurate the per-question multiplier estimate must be before using it beats falling back to the fixed default. It is expressed as a schedule keyed to the estimator's error (root-mean-square error of the log of the estimated multiplier): error around 0.3 keeps about 85% of the achievable gain in the audit unit's accuracy score; around 0.6 keeps about half; past about 1.0 the estimated multiplier is worse than the fixed default because its noise manufactures overconfidence. The requirement matters most at cold-start — before the audit unit has resolved cases to fit the fixed default against — because then the honest fallback is only an assumed default, not a fitted one. The schedule is built by injecting synthetic error of a given size, so it characterizes an error level for the operating requirement, not any particular estimator.
