# Absence audit — 04 refunds-reversals-and-disputes

Audit of 17 November 2026. Earlier search (verification pass): medium (dispute pages, pricing page and its data, `llms.txt`). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 2 hold, 0 overturned, 1 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen's dispute fee amounts are not public (prose, table) | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | narrowed | Terms cl. 8.2 (1 Nov 2023): 'non-refundable Chargeback Fee ... as set out in the Agreement'. Table cell updated; source added. Amount holds as unpublished |
| Neither explains the gap between the acquirer's 30 days and the merchant's shorter deadline (INFERENCE) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Mastercard's rules could not be read | retried: HTTP 403 | holds | none |

**Ruling 46(f), applied after the audit.** The fee amount is no longer 'not public' without qualification: Adyen Canada's fee disclosure gives CAD 24.00 per chargeback (verified 17 Nov 2026). Prose, table cell, Sources note and open question updated. Locked AC-3 ('Adyen's dispute fee is stated as not public') is now imprecise.
