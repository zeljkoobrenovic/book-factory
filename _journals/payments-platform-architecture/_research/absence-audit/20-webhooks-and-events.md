# Absence audit — 20-webhooks-and-events (`payment-webhooks-and-events`)

Audit of 17 November 2026. The verification file says its negatives "rest on searches of the named pages, the two documentation indexes and three web searches", so all were searched again. Searched in this pass: `docs.stripe.com/sitemap.xml` (all webhook and event-destination pages), `support.stripe.com/sitemap.xml` (16 webhook articles; four read), `docs.adyen.com/sitemap.xml` (all webhook pages), `help.adyen.com/sitemap.xml` (webhook articles, which redirect to the documentation), `www.adyen.com/sitemap-en.xml` (knowledge hub: "Consuming webhooks", "Optimizing Webhook Integration", "Developer's guide to webhooks on localhost", "Integrating webhook notifications", "Webhook security: OAuth 2"), stripe.dev, and web searches restricted to the providers' domains, medium.com, infoq.com and youtube.com.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Stripe "publishes no number of seconds" for the acknowledgement (prose, two tables) | docs webhook pages; support articles "Webhooks: how to investigate and fix 'Timed out'" ("it took too long for your server to provide a response"; no figure) and "Troubleshooting webhook delivery issues"; web search | holds | sentence now names documentation and support articles |
| Stripe's retry "intervals are not published" (prose, table) | `webhooks`, `event-destinations/eventbridge` ("View when the next retry will occur … in your event destination's Event deliveries tab"), support article "Why is Stripe trying to reach my webhook endpoints?" ("a backoff mechanism"; endpoint disabled after "several days") | holds. The next attempt is shown per delivery in the dashboard, which the page already says; no schedule is published | none |
| Inference block: "Adyen does not say this, and does not say what it relies on instead" (no timestamp in the Standard webhook signature) | HMAC verification page, secure-webhooks page, knowledge-hub post on OAuth 2 for webhooks | holds | none |
| "Neither Stripe nor Adyen has published how its webhook sender is built. I found no engineering post or talk…"; "Neither company states which design it uses, how it isolates a slow endpoint or how it stores a backlog" | stripe.dev (four posts on receiving webhooks, none on sending), stripe.com/blog, Adyen knowledge hub (five webhook posts, all for receivers), two web searches | holds | sentence now says what was searched |
| Adyen: "no other destination found" than HTTP (table) | documentation sitemap searched for EventBridge, Event Grid, Kafka, Pub/Sub, SQS, event bus: no URL; configure-and-manage page | holds | none |
| Adyen, outage longer than 30 days: "Not documented" | troubleshooting page (documentation and help center copy): "up to 30 days", Retry and Ignore; nothing on what follows | holds | none |
| No Adyen page read "guarantees or disclaims delivery order" (if worded so on the page) | webhook pages; knowledge-hub "Consuming webhooks" | holds | none |
| Event bus destination: "no public endpoint, no signature code" | descriptive, not an absence about a company's publication | not an absence statement | none |

Counts: 7 statements; 7 hold, 0 overturned, 0 narrowed, 0 already wide (one further row is not an absence statement).

Locked journal-spec fields: none made false.

For other pages: none.
