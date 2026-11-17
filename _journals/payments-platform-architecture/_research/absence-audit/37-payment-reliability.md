# Absence audit — 37-payment-reliability (`payment-reliability-and-availability`)

Audit of 17 November 2026. Searched in this pass: docs.adyen.com sitemap (2,619 URLs) and `.md` pages, help.adyen.com sitemap, adyen.com sitemap incl. /legal, /licenses, /infrastructure, knowledge hub; docs.stripe.com sitemap (5,199 URLs), support.stripe.com sitemap (1,889 URLs), stripe.com (newsroom, blog, Sessions transcripts, legal, support plans), stripe.dev; web searches restricted to these domains (and medium.com), two or three phrasings each. "Already wide" means the verification file or a ruling records a search beyond the documentation index.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen: no availability target ("None found"; table cell) | verification row 25 (site, docs, annual report, web search) | already wide | none |
| Adyen: achieved yearly figure "None found" | adyen.com/licenses/* pages | **narrowed**: Adyen Australia Pty Ltd publishes a quarterly regulatory availability disclosure ("Accept card payments (businesses) 100%", Q3 2026) | both tables; source added |
| Stripe: "the letters for 2024 and 2025 carry no reliability figure"; table "none in the letters" | stripe.com Sessions transcripts, web search | **narrowed**: Sessions 2026 keynote transcript: "last year, our critical APIs retained 99.9996% availability" | sentence and both tables; source added |
| Stripe: no public service-level percentage (text, two tables, take-away) | stripe.com legal, support plans page, support sitemap, web search | **narrowed**: no availability percentage; support plans page states a "15-minute response SLA" and "99.999%+ historical uptime" (not a commitment) | Where They Differ cell; source added |
| Whether negotiated Stripe contracts carry a percentage is not public | same | holds | none (self-scoped) |
| Stripe status page does not say how the figure is computed | verification note 1 | already wide | none |
| Stripe: failover between data centers "Not found"; "Stripe none" | stripe.com blog, stripe.dev, docs and support sitemaps, DPA, web search | **narrowed**: blog post of 28 January 2025 describes two-region active-active processing with automatic failover for billing usage events; nothing for payments | text and table cell scoped "for payments"; source added; open question updated |
| No Stripe account of where state sits or which steps it would skip; no Adyen shedding by request class | verification row 45 plus the searches above | holds | none (already "I found no") |
