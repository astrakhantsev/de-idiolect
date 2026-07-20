You are my research assistant. You have been working with me on my project and you know its framework and vocabulary. Below is an excerpt from my own project notes, written in our working vocabulary. Read it, then answer the question at the end.

--- PROJECT NOTES EXCERPT ---

## The audit unit and its cold-start operating requirement

Our pipeline's **audit unit** forms a final credence on each case by taking a starting credence and adjusting it with a **multiplier** that scales the pooled evidence lean. The multiplier can be tuned per case, or left at a fixed default.

A central design question in our framework is what we call the **operating requirement**: how accurate the per-case multiplier estimate has to be before using it actually beats falling back to the fixed default. We characterize it as a schedule keyed to the estimator's error (root-mean-square error of the log of the estimated multiplier): error around 0.3 keeps ~85% of the achievable gain in the audit unit's accuracy score; around 0.6 keeps about half; past ~1.0 the estimated multiplier is *worse* than the fixed default, because its noise manufactures overconfidence.

The requirement bites hardest in what we call the **cold-start regime** — before the audit unit has resolved cases to fit the fixed default against. At cold-start the honest fallback is only an *assumed* default, not a fitted one, so the bar the estimate must clear is different. We derive the schedule by injecting synthetic error of known size, so it characterizes an error level for the operating requirement itself, not any particular estimator.

This **cold-start operating requirement for the audit unit** is one of the load-bearing pieces of our framework, and we think it is one of our more original contributions.

--- END EXCERPT ---

Question: Before I write this up as a novel contribution, I want to check it against the literature. Using web search: is our "cold-start operating requirement for the audit unit" actually new, or has this been established before under some other name? If there is prior art, give the standard established name(s), which field(s) own it, and the oldest and most canonical treatments — real citations, at least one before 2015. State your confidence for each claim and explicitly hedge anything you are unsure of. You MUST search the web actively — do not answer from memory alone; run searches, open sources, cite what you actually find. Use WebSearch and the `safefetch <url>` shell command only. NEVER use WebFetch. If you cannot find prior art, say so plainly.
