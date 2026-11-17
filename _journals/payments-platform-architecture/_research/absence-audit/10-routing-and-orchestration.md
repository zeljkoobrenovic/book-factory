# Absence audit — 10 routing-and-orchestration

Audit of 17 November 2026. Earlier search (verification pass): narrow (both `llms.txt`, one web search, guessed URLs). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 5 hold, 0 overturned, 0 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| First-attempt least-cost routing not found for US debit at Stripe | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | holds | none |
| Adyen's export article is listed but could not be read | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none. A second help-center address for the article also redirects to the tokenization page (17 Nov 2026). A search-engine summary of the article mentions a PCI attestation, a PGP key, SFTP and a fixed CSV; not verifiable, not used |
| No document confirms or denies that network tokens stay with the provider (INFERENCE); neither documents whether they move with an export | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Neither company has said why it holds its layer (INFERENCE) | as above | holds | none |
| Nothing public says at what scale per-payment rules pay | as above | holds | none |
