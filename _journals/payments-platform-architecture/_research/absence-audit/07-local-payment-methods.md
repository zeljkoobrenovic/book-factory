# Absence audit — 07 local-payment-methods

Audit of 17 November 2026. Earlier search (verification pass): narrow (both `llms.txt`). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 2 hold, 0 overturned, 1 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| No page of either company says how it adds a method or lists the methods reached through another payment company (prose, table) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | narrowed | Stripe's Sub-Processors List (27 Sep 2026) names three 'Payment method integration service providers' (PPRO, Payla, NETSTARS) without methods. Adyen: nothing beyond per-method traces (its payout-currencies page says which methods each acquiring connection acquires). Sentence, table cell and spec idea updated; source added |
| How widely delivery by another company holds cannot be told from public sources (INFERENCE) | as above | holds | none |
| What stands behind the door is mostly not public | as above | holds | none |
