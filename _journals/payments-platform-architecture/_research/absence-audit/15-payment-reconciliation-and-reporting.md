# Absence audit — 15 payment-reconciliation-and-reporting

Audit of 17 November 2026. Earlier search (verification pass): narrow (both `llms.txt`). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 3 hold, 1 overturned, 0 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen publishes no time from batch close to report (key points, prose, table, failure section) | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | overturned | docs.adyen.com 'Time zone setting': 'If you have configured automatic generation of the Settlement details report at batch closure, you can expect the report to be generated within 3 hours after the batch closes.' Five sentences, table cell and four spec fields rewritten; source added |
| Neither has published its reconciliation model (INFERENCE) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Neither publishes matching rules, partner file formats, match rates or exception volumes | as above | holds | none |
| A total that fails to tie does not say which record is wrong | not a statement about a company | holds | none |

Locked fields now false (not edited): thesis.how_why ('publishes a daily window for scheduled reports but no duration from batch close') and AC-2 ('no duration is published'). Consistency ruling 32(a) says the same and needs correcting.
