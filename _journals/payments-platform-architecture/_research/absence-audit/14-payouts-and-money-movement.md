# Absence audit — 14 payouts-and-money-movement

Audit of 17 November 2026. Earlier search (verification pass): narrow (pages cited and both `llms.txt`). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 2 hold, 1 overturned, 0 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen: no automatic resend after a return is documented / 'a resend is not documented' (prose, table) | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | overturned | Adyen's payout webhook and on-demand payout pages give each return a reason code with retry advice and say 'Adyen blocks subsequent transfer attempts when a reason code indicates a permanent issue'; the sender retries. Sentence, table cell and source note rewritten |
| Adyen's payout price list is not public | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | scope words added |
| How providers submit payouts in bulk (INFERENCE) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
