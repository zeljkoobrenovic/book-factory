# Absence audit — 18-idempotency-and-retries (`idempotency-and-retries`)

Audit of 17 November 2026. The verification file marks its negatives (rows 65, 74–77) "confirmed only as far as the pages named and the searches described" (two or three pages, the `llms.txt` index, one or two web searches), so all were searched again. Searched in this pass: `docs.stripe.com/sitemap.xml`, `support.stripe.com/sitemap.xml`, `docs.adyen.com/sitemap.xml`, `help.adyen.com/sitemap.xml`, `www.adyen.com/sitemap-en.xml` (knowledge hub), stripe.com/blog, stripe.dev, and web searches restricted to the providers' domains and infoq.com.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| "Stripe has published nothing about where keys are stored, how a request is fingerprinted, or what 'after endpoint execution begins' means internally" (prose, table, take-away) | Stripe documentation sitemap (one idempotency page), support sitemap, stripe.dev ("Because nobody likes being charged twice", Ben Smith, 10 April 2025: client-side advice only), stripe.com/blog, web search incl. infoq.com | holds | sentence now says what was searched |
| Adyen: "no later Adyen publication … says whether the same database is still used, and nothing describes the key record, expiry or recovery" | knowledge-hub sitemap ("Design to Duty" parts 1 and 2, "we design for 20x", "Strengthening our platform resilience": no further statement), docs, help center article "Why are there duplicate payments", web search | **narrowed** (ruling 42c). First-party: holds. Secondary: Cockroach Labs customer story, 14 February 2023 (archived copy): "In 2019, Adyen migrated their online payment transaction system from PostgreSQL to CockroachDB … to … achieve idempotency", "across multiple regions and multiple data centers per region" | one sentence and the source added |
| Inference block: "Adyen does not say so" (key store not shared across regions) | docs idempotency page, knowledge hub | holds (already scoped as inference). Note: the vendor story says the database runs across regions, which does not settle whether keys are checked across regional endpoints; Adyen's documentation says they are not | none |
| "Neither Stripe nor Adyen has published how its own calls to card networks and banks are made repeatable, or how it resolves a timeout from a network" | both documentation sitemaps, support and help centers, engineering posts, two web searches | **narrowed**. Adyen "Time-outs" (point of sale, n.d.): "If the issuer has not processed this transaction within 120 seconds (local integration) or 150 seconds (cloud integration), the Adyen payments platform automatically cancels the transaction." Nothing on repeatability of network calls; nothing for online payments or for Stripe acquiring (Stripe documents a `network_fallback` outcome only for Issuing) | sentence split; fact and source added; spec controlling idea aligned |
| Adyen: "whether errors are stored is not documented" (table) | idempotency page, error codes, HTTP status codes, help center | holds | none |
| Adyen, same key with a different request: "Not documented"; "Adyen's page does not describe the case" | as above, web search | holds | none |
| Stripe, key store unavailable: "Not public"; "Stripe documents no equivalent case" | Stripe idempotency page, advanced error handling, support sitemap, web search | holds | none |
| "Neither company has published its implementation beyond a fragment" (take-away); "Neither publishes the key record, fingerprinting or expiry" (table) | as rows 1–2 | holds | none |

Counts: 8 statements; 6 hold, 0 overturned, 2 narrowed, 0 already wide.

Locked journal-spec fields: none made false.

For other pages: chapter 11 (in-person payments) and chapter 2 (authorization) if they say no provider documents what happens to a payment the issuer does not answer.
