# Absence audit — 38-payment-data-stores-and-consistency (`payment-data-stores-and-consistency`)

Audit of 17 November 2026. Searched in this pass: docs.adyen.com sitemap (2,619 URLs) and `.md` pages, help.adyen.com sitemap, adyen.com sitemap incl. /legal, /licenses, /infrastructure, knowledge hub; docs.stripe.com sitemap (5,199 URLs), support.stripe.com sitemap (1,889 URLs), stripe.com (newsroom, blog, Sessions transcripts, legal, support plans), stripe.dev; web searches restricted to these domains (and medium.com), two or three phrasings each. "Already wide" means the verification file or a ruling records a search beyond the documentation index.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Stripe: who retries / how a retried write is made safe | verification (talk transcript), web search | already wide (ruling 42d) | none |
| Whether the 2017 migration tooling is used today | stripe.dev, stripe.com/blog, web search | holds | none |
| Ledger post names no storage engine; which data lives outside DocDB; transaction boundaries, read consistency, write acknowledgement | stripe.dev, stripe.com, docs and support sitemaps, web searches (replication, ledger storage, idempotency storage) | holds | sentence now says what was searched |
| "For Stripe, all of this is not public"; table "Moving money across shards: Not public" | same | **narrowed**: stripe.dev post of 16 April 2026 (Stripe Credits): transfers follow "a three-phase lifecycle through the ledger: submitted → prepared → disbursed"; storage and shards not stated | one sentence and the table cell; source added |
| Adyen: cluster count, cross-cluster atomicity, rebalancing, synchronous data, failover time; "the protocol is not public" | adyen.com knowledge hub, medium.com/adyen, web search | holds (ruling 42b, c already applied) | none |
| Neither states that it uses no transaction spanning its money path (inference block) | as above | holds | none |
