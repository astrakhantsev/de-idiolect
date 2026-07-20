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

This is a quantitative specification stating how accurate a measuring procedure must be before using its output is better than not using it at all. It applies wherever a pipeline needs a numeric setting — here, a multiplier that scales pooled evidence — and one may either estimate that setting separately for each case or fall back to a single fixed value used for every case. The specification's input is the error of the estimator, summarized as the root-mean-square error of the logarithm of the estimated quantity relative to its true value; its output is the fraction retained of the maximum achievable improvement in prediction accuracy, measured by a standard accuracy measure for probability forecasts. The stated content is a schedule: error less than about 0.3 retains roughly 85% of the available gain; about 0.6 retains about half; beyond about 1.0 the estimator is actively harmful, producing worse predictions than the fixed fallback because its noise manufactures unwarranted confidence. Two conditions matter. First, the benchmark must be named: a fixed value chosen by fitting to already-resolved cases is a strong competitor but is unavailable when no resolved outcomes exist, in which case the honest comparison is against a merely assumed value. Second, the schedule is established by injecting synthetic errors of a given size rather than by running any particular estimator, so it characterizes an error level, not a method.
