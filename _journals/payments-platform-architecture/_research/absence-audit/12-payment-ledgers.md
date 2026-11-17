# Absence audit — 12 payment-ledgers

Audit of 17 November 2026. Earlier search (verification pass): narrow (posts read, `llms.txt`). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 8 hold, 0 overturned, 0 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| No newer Adyen account of its accounting system than 2021 (two places) | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | scope words added in the limits paragraph |
| The Stripe 2024 post does not say what answers a balance request (INFERENCE) | stripe.dev, stripe.com/blog, docs, web search | holds | none |
| How MMS, the 'internal ledger' and Ledger relate is not stated in either post | both posts; stripe.dev search | holds | none (self-scoped) |
| Neither company says where it places controls (INFERENCE) | as above | holds | none |
| Table: Stripe storage Not public; Stripe names no storage engine, schema or consistency model | stripe.dev (Ledger 2024, document database 2024, credits 2026), stripe.com/blog, docs; web search | holds | scope words added. The document-database post names MongoDB for DocDB and does not tie Ledger to it |
| Table: Adyen correcting an error Not public | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Nothing public describes the internals of Adyen's platform balance accounts | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Adyen's post does not say its records are immutable | the post | holds | none (statement about one document) |

**Ruling 46(i).** Already satisfied: the page quotes 'submitted → prepared → disbursed' from the stripe.dev post of 16 April 2026.
