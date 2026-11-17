# Absence audit — 19-api-versioning (`payment-api-versioning`)

Audit of 17 November 2026. The verification file shows the negatives rested on the `llms.txt` indexes, the pages cited and one or two web searches, so all were searched again. Searched in this pass: `docs.stripe.com/sitemap.xml` (every URL with version, upgrade, deprecat, sunset, lifecycle), `support.stripe.com/sitemap.xml`, `docs.adyen.com/sitemap.xml`, `help.adyen.com/sitemap.xml`, `www.adyen.com/sitemap-en.xml` (knowledge hub), stripe.dev and stripe.com/blog, and four web searches (two restricted to the providers' domains, two open).

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Stripe: walking back through version-change modules "not re-described since 2017"; table "Published mechanism" | stripe.com/blog, stripe.dev ("Preparing for Stripe API upgrades", 24 October 2024: integrator advice only), web search (only third-party retellings of the 2017 post) | holds | none (already scoped) |
| "No Stripe source I could find says whether Stripe has retired any dated version, how many versions it serves…"; "No later statement found"; table "Published end of a version: Not public"; "Stripe does not publish … how long a version lasts" | docs sitemap pages `api/versioning`, `upgrades`, `api-versions`, `webhooks/versioning`, `sdks/versioning`, `sdks/stripejs-versioning`; support sitemap; two web searches (community posts quote version-gated features and an unattributed "This API version is not supported" string; no Stripe notice) | holds for API versions. Stripe publishes support windows only for SDK major versions, language runtimes and Stripe.js ("We continue to support and update older versions"), none for a dated API version | sentence now says what was searched |
| Adyen mechanism: "None found" (two table cells); "I found no engineering source on how one platform serves its many Checkout versions"; table "Not public" | knowledge-hub sitemap ("API-first at Adyen", 2022; "API Diff Tool", 18 August 2025: a comparison tool for integrators), docs `development-resources/versioning`, web search incl. medium.com and github.com | holds | sentence now says where |
| Adyen: "I found no statement on how long old webhook versions are delivered"; table cell "not public" | docs sitemap (webhook pages, upgrade page), help center sitemap, OpenAPI repository via web search (deprecation is marked per webhook family, for example "Payment webhooks (deprecated)", with no delivery end date) | holds | sentence now says where |
| Adyen Checkout page "showed no lifecycle state" | API Explorer page as fetched | holds (statement about one fetched page, already dated) | none |
| Stripe "does not say in so many words that such changes reach older versions" | `api/versioning`, "How API versioning works", `webhooks/versioning` | holds | none |
| "So the size of Stripe's compatibility cost today is not known outside the company" | as rows 1–2 | holds | none |

Counts: 7 statements; 7 hold, 0 overturned, 0 narrowed, 0 already wide.

Locked journal-spec fields: none made false.

For other pages: none.
