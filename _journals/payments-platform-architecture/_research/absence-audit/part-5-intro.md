# Absence audit — part-5-intro

Audit of 17 November 2026. The introduction has one paragraph of absence statements, each resting on a chapter.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| "Neither publishes a vault design" | see the audit of chapter 22 (documentation sitemaps, security pages, help and support centers, company sites, engineering posts, restricted web searches) | holds | none |
| "Adyen's fraud-risk model is not public" | web search on adyen.com and medium.com/adyen; Adyen knowledge hub: "How Adyen does AI" (Andreu Mora, 16 August 2024): fraud is checked by "a set of models … currently based on tree-based ensembling models"; "The AI behind Uplift" (17 January 2025): "a fraud model would predict the probability of a chargeback", each AI endpoint "had an allocated latency of 20 ms (median)", features served from Flink and Cassandra | narrowed | "Adyen has published little about its fraud-risk model". Chapter 24 owns the fact (its audit is by another agent); reported |
| "neither company says how it monitors transactions" | Stripe support, "Financial Crimes Risk Appetite Policy Statement" (November 2023): "Stripe also conducts ongoing transaction monitoring of user activity"; Adyen "Compliance obligations" page (n.d.): it monitors "behavior and transactions across the Adyen platform, including by using automated systems such as machine learning models"; Adyen careers pages mention a "Post-Event Transaction Monitoring Framework"; no description of scenarios, thresholds or systems found | narrowed (both say that they monitor; neither says how) | "both companies say that they monitor transactions but not how" |

Counts: 3 statements — 1 holds, 0 overturned, 2 narrowed, 0 already wide. Page 1,070 words (limit 1,200). Spec: controlling idea and evidence of the paragraph updated; changelog line added.

## Locked journal-spec sentences affected

- Chapter 24 acceptance criterion: "the chapter states that Adyen's fraud-risk model … [is] not public" — the model family (2024) and a latency allocation (2025) are published.
- Chapter 26 acceptance criterion: "neither Stripe nor Adyen publishes how it monitors transactions or screens against sanctions lists" — still true of the how; both publish that they do.
