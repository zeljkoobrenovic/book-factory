# Absence audit — part-4-intro

Audit of 17 November 2026. The page cites no external source; its two statements of absence repeat chapters 17 and 21 and were re-tested with those chapters.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| "Adyen's Checkout API returns a reference and a result code and has no call that returns a payment" | Checkout API v72 OpenAPI definition (all GET operations); see audit of chapter 17 | already wide | none |
| "Adyen publishes no rate limit for its payments APIs" | docs.adyen.com sitemap, help.adyen.com sitemap, Adyen OpenAPI repository, knowledge hub, web searches; see audit of chapter 21 | holds | none (the part introduction's style does not scope such sentences, and the page has 12 words of room) |

Counts: 2 statements; 1 holds, 0 overturned, 0 narrowed, 1 already wide. A changelog line was added to the spec; `index.md` is unchanged.
