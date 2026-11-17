# Verification — 21-developer-platform (`payment-developer-platform`)

Verification pass of 17 November 2026. Every source below was fetched in this session with `curl`: Stripe and Adyen documentation as `.md` variants, the Stripe blog posts and developer digests as HTML, the Adyen OpenAPI definitions as raw JSON from Adyen's repository (parsed, response codes enumerated by script), the Adyen Medium article through the publication's RSS feed (the article URL itself answers 403 to a script). All double-quoted strings taken from sources were matched mechanically against the fetched texts after normalizing quotes and markup; the ones that did not match mechanically (a link or a tooltip sits inside the sentence in the `.md` variant) were read by hand (rows 23, 43, 46, 53, 57). Each row is one claim or one group of claims resting on the same passage.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Key point: Stripe gives 100 requests a second per account in live mode and 25 per endpoint | https://docs.stripe.com/rate-limits.md | confirmed | — |
| 2 | Key point: Adyen lists no rate limit for its payments APIs | https://docs.adyen.com/llms.txt ; CheckoutService-v72.json | confirmed | Index searched for "rate limit", "throttl", "too many": no page |
| 3 | Quote "People and systems must have only the privileges required to perform their jobs" | https://docs.stripe.com/keys-best-practices.md | confirmed | — |
| 4 | Quote "If a fraudulent actor obtains your secret key, they can harm your business." | https://docs.stripe.com/keys.md | confirmed | — |
| 5 | Stripe "documents three kinds of key that an integration uses" | https://docs.stripe.com/keys.md | corrected | The page's table lists four types (publishable, restricted, secret, organization `sk_org_…`) and mentions managed keys. Now: four types listed, three used by an integration of one account, the fourth spans several accounts |
| 6 | Publishable key `pk_…` identifies the account from client code and is safe to embed | https://docs.stripe.com/keys.md | confirmed | "Safe to expose: Yes"; "You can include it in front-end code" |
| 7 | Secret key: "API key that has unrestricted permissions on all Stripe APIs" | https://docs.stripe.com/keys.md | confirmed | — |
| 8 | Restricted key `rk_…`: permission per resource None, Read or Write; "The default value for all permissions is None" | https://docs.stripe.com/keys/restricted-api-keys.md | confirmed | — |
| 9 | Live keys "start with `pk_live_`, `rk_live_`, and `sk_live_`" | https://docs.stripe.com/keys.md | confirmed | — |
| 10 | Quote "Because you can't limit their permissions, we don't recommend using secret keys for new use cases … migrating secret key usage to RAKs" | https://docs.stripe.com/keys.md | confirmed | — |
| 11 | Quote "restricted API keys are drop-in replacements for secret API keys" (in server code) | https://docs.stripe.com/keys/restricted-api-keys.md | confirmed | Source: "In your server environment, …" |
| 12 | Adyen: one company account and, under it, one or more merchant accounts in which payments are processed | https://docs.adyen.com/account/account-structure.md | confirmed | — |
| 13 | Adyen credential = username, API key and "Roles: Permissions that define what the credential is allowed to do" | https://docs.adyen.com/development-resources/api-credentials.md | confirmed | — |
| 14 | "the page's metadata says last modified in August 2021" | same | corrected (ruling 30) | The front matter does carry `last_modified: 2021-08-06`, but ruling 30 forbids metadata stamps as dates; the clause was removed from the text and from the spec's evidence note |
| 15 | Quote "Credentials created on a company account can access … Credentials created on a merchant account can only access that merchant account." | same | confirmed | Two bullets on the page, quoted in order |
| 16 | Roles are per API and action, e.g. "Checkout webservice role" | https://docs.adyen.com/development-resources/api-credentials/roles.md | confirmed | — |
| 17 | A credential can be tied to an allowed range of IP addresses | https://docs.adyen.com/development-resources/api-credentials.md | confirmed | Section "Add an allowed IP range" |
| 18 | Quote "we strongly recommend creating a separate API credential for each channel" (online and point of sale) | same | confirmed | — |
| 19 | Client key "is not used when making requests to our APIs" | https://docs.adyen.com/development-resources/client-side-authentication.md | confirmed | — |
| 20 | Stripe calls its test environment a sandbox; older material says test mode | https://docs.stripe.com/sandboxes.md ; testing-use-cases.md | confirmed | "legacy test mode sandbox" |
| 21 | "Use up to five sandboxes" besides the legacy test-mode sandbox | https://docs.stripe.com/testing-use-cases.md | confirmed | "The legacy test mode sandbox doesn't count toward the limit of five." |
| 22 | Quote "API objects in one mode aren't accessible to the other" | same | confirmed | — |
| 23 | Developer digest announced the Sandboxes private beta in June 2024 | https://stripe.dev/blog/stripe-developer-digest-june-2024-join-the-sandboxes-private-beta | confirmed | Displayed date 2024.6.30 |
| 24 | Digest of 30 August 2024: "Sandboxes is now in public beta" | https://stripe.dev/blog/stripe-developer-digest-august-2024-workbench-is-now-available-to-everyone | confirmed | datePublished 2024-08-30 |
| 25 | "I found no dated announcement of general availability" (Sandboxes) | web search, Stripe changelog and blog | confirmed as a statement of absence | A search in this session found none either; the current docs present sandboxes without a beta label |
| 26 | Quote "the payments you create aren't processed by card networks or payment providers" | https://docs.stripe.com/sandboxes.md | confirmed | — |
| 27 | Quotes "API limits are lower in a sandbox" and "creating a charge in live mode sends a request to a payment gateway and that request is mocked in a sandbox, resulting in significantly different latency profiles" | https://docs.stripe.com/rate-limits.md | confirmed | — |
| 28 | Quote "We retry event deliveries created in a sandbox three times over the course of a few hours"; up to three days in live mode | https://docs.stripe.com/webhooks.md | confirmed | — |
| 29 | Adyen: test and live have different endpoints, Customer Areas and credentials; quote "When you switch to your live environment, you must generate a new API key in your live Customer Area" | https://docs.adyen.com/development-resources/api-credentials.md ; live-endpoints.md | confirmed | The quote is on the API credentials page (a link sits inside it in the `.md` variant) |
| 30 | A live account is applied for; each company account gets its own live hostname | https://docs.adyen.com/development-resources/live-endpoints.md | confirmed | "Apply and get your live account"; "Each company account is provided with a unique hostname" |
| 31 | Quote: Adyen does not provide a "copy" function for moving webhook configurations from test to live | https://docs.adyen.com/development-resources/webhooks/configure-and-manage.md | confirmed | — |
| 32 | "Adyen publishes no list of what its test environment cannot simulate" | https://docs.adyen.com/llms.txt ; https://docs.adyen.com/development-resources/testing.md | confirmed as a statement of absence | Index searched for test, testing, simulat, sandbox; the testing overview page fetched and read: no such list |
| 33 | Adyen engineers, November 2026 article on a payment simulator; quote "Getting a green happy-path response during integration testing doesn't prove your integration will hold up under the conditions that actually matter at go-live." | https://medium.com/feed/adyen (article URL in Sources) | confirmed | Feed item dated Mon, 09 Nov 2026; byline Ayodeji Ogundare, Henk Grent, Marc Sernatinger and Shantanu Tarey; the article is about methods that "finish outside your checkout" |
| 34 | Adyen publishes Management API rate limits for live only (basis of the labeled inference) | https://docs.adyen.com/point-of-sale/automating-terminal-management.md | confirmed | Section "Rate limits in the live environment" |
| 35 | A Stripe sandbox copies settings from live only "at creation time" | https://docs.stripe.com/testing-use-cases.md | confirmed | "Copy settings from live mode at creation time" |
| 36 | 2017 post: title, author Paul Tarjan, date; quotes on rate limiter and load shedder | https://stripe.com/blog/rate-limiters | confirmed | Displayed date March 30, 2017 |
| 37 | Evidence-age flag "9 years" on the 2017 post | same | confirmed | 9 years 8 months |
| 38 | "the only limiter design either company has published" | — | hedged | Cannot be proven by fetching; a search for an Adyen engineering post on rate limiting or load shedding found none, and the 10 newest posts of Adyen's feed have none. Reworded to "the only limiter design I found from either company" |
| 39 | Quotes: "At Stripe, we operate 4 different types of limiters in production"; "restricts each user to N requests per second"; "You can only have 20 API requests in progress at the same time" | https://stripe.com/blog/rate-limiters | confirmed | — |
| 40 | Fleet usage load shedder quotes (critical and non-critical methods; 20% reservation, 80%, status 503) | same | confirmed | — |
| 41 | Worker utilization load shedder "is the final line of defense", sheds "starting with test mode traffic", critical methods last | same | confirmed | Four categories in the post: critical methods, POSTs, GETs, test mode traffic |
| 42 | "We use the token bucket algorithm", implemented with Redis | same | confirmed | "We implement our rate limiters using Redis." |
| 43 | Current docs confirm rate and concurrency limits per account and speak of the "concurrency limiter" shedding new requests | https://docs.stripe.com/rate-limits.md | confirmed | "causing the concurrency limiter to shed new requests" |
| 44 | 2017: "Our API provides the same rate limiting behavior in both test and live modes"; today sandbox limits are lower | https://stripe.com/blog/rate-limiters ; rate-limits.md | confirmed | — |
| 45 | Current docs say nothing about the two load shedders | https://docs.stripe.com/rate-limits.md | confirmed as a statement of absence | Page read in full |
| 46 | 429 with `Stripe-Rate-Limited-Reason` header, values such as `global-rate`, `endpoint-rate`; large increase "at least 6 weeks in advance" | same | confirmed | — |
| 47 | Limits table: 100/s live, 25/s sandbox, 25/s per endpoint ("each named API operation"), 50 in progress by default in live mode, 15/s creating payouts, reads at most 500 per transaction on average over 30 days | same | confirmed | All six cells read against the page |
| 48 | Adyen documentation index lists no page on API rate limits | https://docs.adyen.com/llms.txt | confirmed | — |
| 49 | Checkout API definition v72 contains neither "rate limit" nor a 429 response | https://raw.githubusercontent.com/Adyen/adyen-openapi/main/json/CheckoutService-v72.json | confirmed | Response codes declared: 200, 201, 204, 400, 401, 403, 422, 500. v72 is the newest Checkout definition in the repository |
| 50 | Adyen 429: "You have sent too many requests in a short period"; "a retry mechanism that uses exponential backoff with jitter" | https://docs.adyen.com/development-resources/response-handling.md | confirmed | — |
| 51 | Legal Entity Management API: "Live environments: 700 requests per 5 seconds. Test environments: 200 requests per 5 seconds." | https://raw.githubusercontent.com/Adyen/adyen-openapi/main/json/LegalEntityService-v4.json | confirmed | — |
| 52 | Terminal-management endpoints of the Management API have per-minute limits that Adyen calls "indicative" | https://docs.adyen.com/point-of-sale/automating-terminal-management.md | confirmed | 160, 210 and 2000 requests a minute per endpoint group |
| 53 | Stripe documents "a client-side token bucket rate-limiting algorithm" and asking support for an increase; both providers document backoff on 429 | https://docs.stripe.com/rate-limits.md ; Adyen response-handling.md | confirmed | — |
| 54 | Whether Adyen limits payment requests per company account or per credential, and how it sheds load, is not public | https://docs.adyen.com/llms.txt | confirmed as a statement of absence | Nothing found in the index or the Checkout definition |
| 55 | Where They Differ, rows 1–5 (credentials, test environment, stated gaps, rate limits, limiter design) | rows 5–54 above | confirmed | Each Stripe and Adyen cell repeats a claim confirmed above; "Not public" for Adyen's limiter design stands (row 38) |
| 56 | Where They Differ, request logs row: Stripe "retention not found" | https://support.stripe.com/questions/stripe-request-log-retention-period | corrected | See row 62; cell now gives 31 days for GET and 15 months for other requests, per the support article; last-column reading adjusted |
| 57 | Quote: rate-limited requests "don't cache a result" | https://docs.stripe.com/error-low-level.md | confirmed | — |
| 58 | Stripe "generally discourage[s]" load testing in a sandbox; sandbox limit 25 a second, latency mocked | https://docs.stripe.com/rate-limits.md | confirmed | "We generally discourage this practice" |
| 59 | A 429 without the reason header "might be a lock timeout" | same | confirmed | — |
| 60 | Stripe: "Rotating an API key revokes it and generates a replacement key that's ready to use immediately"; rotation can be scheduled; contrast with Adyen "gives an overlap" | https://docs.stripe.com/keys.md | corrected | The quote is right, but the contrast was misleading: the same page says "When you rotate a key in the Dashboard, both the old and new keys work for up to 7 days" (the expiry is chosen; "Now" deletes the old key). The sentence now states Stripe's grace period beside Adyen's fixed 24 hours |
| 61 | Adyen: "When you generate a new API key, it becomes active immediately. The previous key remains active for 24 hours to allow you to update your systems." | https://docs.adyen.com/development-resources/api-credentials.md | confirmed | — |
| 62 | Stripe request logs: "I found no stated retention period" | https://support.stripe.com/questions/stripe-request-log-retention-period | corrected | Stripe's documentation pages (Workbench overview, request logs page, keys) give none, but Stripe's support site does: "The Dashboard allows users to view GET request logs from the past 31 days and non-GET request logs (including POST) from the past 15 months." Text, table cell and Sources updated; the article is undated and is cited as a support article |
| 63 | Adyen API logs: "all API requests made in your test or live environment in the past thirty days", JSON requests only | https://docs.adyen.com/development-resources/logs-resources/api-logs.md | confirmed | — |
| 64 | Adyen developer dashboard covers seven days | https://docs.adyen.com/development-resources/developer-dashboard.md | confirmed | "in the past seven days" (the range can be changed) |
| 65 | Workbench announced August 2024 as "our new home for developers within the Dashboard"; authors and date in Sources | https://stripe.com/blog/workbench-a-new-way-to-debug-monitor-and-grow-your-stripe-integration | confirmed | August 19, 2024; Michael Glukhovsky and Tomer Elmalem |
| 66 | Every Stripe error carries a `request_log_url` | https://docs.stripe.com/api/errors.md | confirmed | Field is "string, nullable": "A URL to the request log entry in your dashboard." |
| 67 | Stripe CLI `logs tail` "only supports displaying request logs from a sandbox" | https://docs.stripe.com/cli.md | confirmed | — |
| 68 | Adyen's documentation index lists no command-line tool | https://docs.adyen.com/llms.txt | confirmed as a statement of absence | No "CLI" or "command-line" entry |
| 69 | Closing: idempotency keys kept at least 24 hours at Stripe, 7 to 14 days at Adyen | https://docs.stripe.com/api/idempotent_requests.md ; https://docs.adyen.com/development-resources/api-idempotency.md | confirmed | — |
| 70 | Closing: undelivered events retried up to three days at Stripe, up to 30 days at Adyen | https://docs.stripe.com/webhooks.md ; https://docs.adyen.com/development-resources/webhooks/troubleshoot.md | confirmed | — |
| 71 | Closing: Adyen gives two years after a Checkout version is deprecated | https://docs.adyen.com/online-payments/upgrade-your-integration.md | confirmed | "you have 2 years to upgrade to the latest version Checkout API" |
| 72 | Question 3: "Stripe's rate-limit page does not say" how a platform's requests for its sellers are counted | https://docs.stripe.com/rate-limits.md | corrected | The page does say it for the read allocation (a platform has a separate allocation for reads on behalf of connected accounts); it is silent only for the per-second limits. Parenthesis reworded |
| 73 | Larkfield table: "the Checkout API has no call that returns a payment" | ruling 12 and 29; CheckoutService-v72.json | confirmed | Already scoped to the Checkout API as ruling 29 requires; no edit |

**Counts:** 73 claims checked: 66 confirmed (6 of them statements of absence, checked by searching the provider's index), 6 corrected (rows 5, 14, 56, 60, 62, 72), 1 hedged (row 38), 0 unsupported, 0 unreachable.

## Links

All 32 URLs in Sources and Evidence returned HTTP 200 in this session, except the Medium article URL, which returns 403 to a script; its text, date and byline were read from `https://medium.com/feed/adyen`, and the source entry already says so. No URL had moved. One source was added (the Stripe support article on request-log retention) and the two-URL bullet for Adyen's API logs and developer dashboard was split into two entries. Every `[[permalink]]` in the page is in the style guide's valid list (the render check reports no unresolved link). The running text has no external URL (ruling 22).

## Could not verify, and what was done

- **General availability of Stripe Sandboxes.** No dated announcement was found by the writer or in this pass. The sentence already says so in the first person; left as is.
- **Statements of absence about Adyen** (no list of test gaps, no payment rate limit, no limiter design, no command-line tool) can only be checked by searching. The documentation index, the Checkout definition and the testing overview page were searched; nothing was found. The limiter-design sentence was reworded to say what was found (row 38).
- **The Stripe support article on log retention is undated** and says "The Dashboard"; whether Workbench's Logs tab has the same windows is not stated anywhere I found. The page attributes the figures to the support article and does not extend them.

## Rulings

- **Ruling 27** (acquirers, Adyen's acquiring connections): the page makes no statement about acquiring; nothing to apply.
- **Ruling 29** (scope of "no endpoint that returns a payment"): the one place the claim is made says "the Checkout API"; compliant.
- **Ruling 30** (no metadata dates for documentation): one violation removed (row 14); every documentation entry in Sources is "n.d., accessed 2026-11".
- Ruling 5 (this page owns request limits and load shedding) and ruling 13 (the idempotency key includes the attempt number; the page only says "the same idempotency key, as K1 requires") are respected.

## Larkfield consistency

Checked against the ledger: 38%, about 357,000 renewals, €17.5 million, six-hour window; 1 October 2026; 7,900 renewals rerun on 2 October; pool raised from 12 to 48 workers in September 2026; three immediate retries; the 2017 unrestricted secret key shared by five systems; Femke de Graaf joined January 2027; Tom Hendriks built the payment service; Mila's pass (Tuesday 9 March 2027, 19:42, €120.00, Studio Noord; 9 March 2027 is a Tuesday); the 44%/56% split with about 157,000 and 200,000 renewals; 18 hours; buckets of 10 and 5 a second; K1, K2, K5, K7. Arithmetic rechecked (17, 7 and 9 a second over six hours; 2.4 and 3.1 over 18 hours; 24 and 96 a second from 12 and 48 workers at half a second a call). No contradiction. The page used "Keel decision K5" without saying what Keel is; one clause was added.

## Ledger conflicts

None.

## For other pages

- Any page that says Stripe's request-log retention is not published (chapter 17, 20 or 41 may) should cite the support article in row 62.
- Any page that contrasts Stripe key rotation ("revokes immediately") with Adyen's 24-hour overlap should mention Stripe's grace period of up to 7 days (row 60).

## Format

`timetoread` changed from 21 to 22 (4,981 words by `check_draft.py structure` ÷ 230 = 21.7). Spec validates; structure check passes (units unchanged; wording inside units only). Build and render check pass.
