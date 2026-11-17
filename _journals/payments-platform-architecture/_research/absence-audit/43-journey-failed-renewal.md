# Absence audit — 43-journey-failed-renewal (`journey-failed-renewal`)

Audit of 17 November 2026. Searched in this pass: docs.adyen.com sitemap (2,619 URLs) and `.md` pages, help.adyen.com sitemap, adyen.com sitemap incl. /legal, /licenses, /infrastructure, knowledge hub; docs.stripe.com sitemap (5,199 URLs), support.stripe.com sitemap (1,889 URLs), stripe.com (newsroom, blog, Sessions transcripts, legal, support plans), stripe.dev; web searches restricted to these domains (and medium.com), two or three phrasings each. "Already wide" means the verification file or a ruling records a search beyond the documentation index.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| No invoice or subscription object in Adyen's documentation | docs sitemap (invoice, subscription, billing, orb) | holds | none |
| Orb "is not documented as part of Adyen's platform" | docs.adyen.com sitemap; docs.withorb.com | **narrowed**: Orb's documentation has a page "Orb supports Adyen as a payment gateway"; Adyen's documentation has no page on Orb (ruling 39b) | sentence; source added |
| Mastercard rules could not be read | ruling 17 | already wide | none |
| "Neither publishes a model or its inputs" (key point, comparison paragraph) | Part VI audit (chapter 29) | **narrowed**: Stripe blog 23 January 2024 ("more than 500 attributes"); Adyen post 3 December 2020 (contextual bandit, "about 6% more orders than the baseline"); the model now running and a recovery rate with a stated basis remain unpublished | key point, paragraph, spec ideas; two sources reused from chapter 29 |
