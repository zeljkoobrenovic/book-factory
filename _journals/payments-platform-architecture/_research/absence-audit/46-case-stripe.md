# Absence audit — 46-case-stripe (`case-stripe`)

Audit of 17 November 2026. Searched in this pass: docs.adyen.com sitemap (2,619 URLs) and `.md` pages, help.adyen.com sitemap, adyen.com sitemap incl. /legal, /licenses, /infrastructure, knowledge hub; docs.stripe.com sitemap (5,199 URLs), support.stripe.com sitemap (1,889 URLs), stripe.com (newsroom, blog, Sessions transcripts, legal, support plans), stripe.dev; web searches restricted to these domains (and medium.com), two or three phrasings each. "Already wide" means the verification file or a ruling records a search beyond the documentation index.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| No engineering post on how events are delivered | stripe.dev, stripe.com/blog, web search | holds | none |
| "Stripe has published nothing about a single code base" | stripe.dev | **narrowed**: Ruby monorepo of about 50 million lines (9 April 2026, already cited on the page); which products live in it is not stated | sentence |
| No share of volume per acquirer; which merchants the Georgia bank acquires for; motive for the licenses | verification rows 57, 60 | already wide | none |
| Total volume definition not stated | annual letters, newsroom, web search | holds | none |
| No first-party source names a region, number of regions or failover design | as chapter 39 | **narrowed**: two-region design with failover published for billing usage events (28 January 2025); none for payments | sentence; source added; spec evidence |
| Internals bullet: idempotency key storage, event delivery, balance vs Ledger, joins of bought products | stripe.dev, docs, support, web search | **narrowed** for balance vs Ledger (Stripe Credits post, 16 April 2026: Money Movement and Storage, financial accounts, three-phase transfer); the rest holds | bullet; source added |
| Revenue, margin, headcount | verification row 66 | already wide | none |
