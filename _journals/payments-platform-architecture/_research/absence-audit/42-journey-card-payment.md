# Absence audit — 42-journey-card-payment (`journey-card-payment`)

Audit of 17 November 2026. Searched in this pass: docs.adyen.com sitemap (2,619 URLs) and `.md` pages, help.adyen.com sitemap, adyen.com sitemap incl. /legal, /licenses, /infrastructure, knowledge hub; docs.stripe.com sitemap (5,199 URLs), support.stripe.com sitemap (1,889 URLs), stripe.com (newsroom, blog, Sessions transcripts, legal, support plans), stripe.dev; web searches restricted to these domains (and medium.com), two or three phrasings each. "Already wide" means the verification file or a ruling records a search beyond the documentation index.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen "names no acquiring entity per country" | adyen.com/licenses/* (EMEA, US, Japan, Singapore, Australia, Canada …) | **narrowed**: EMEA page: Adyen N.V.'s authorisation "includes the ability to provide cross-border acquiring … in all EEA countries"; no per-country list | sentence; source added; spec evidence |
| Stripe silent on a network rejection of a capture after `succeeded`; table "Stripe: not public" | docs sitemap (capture pages), support sitemap, web search | holds | sentence says what was searched |
| Stripe silent on funds available before receipt (standard schedule) | ruling 18 | already wide | none |
| Visa rules: no settlement cut-off times found | scoped to the document | holds | none |
