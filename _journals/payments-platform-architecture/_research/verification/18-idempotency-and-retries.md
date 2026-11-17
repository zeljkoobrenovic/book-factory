# Verification — 18-idempotency-and-retries (`idempotency-and-retries`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Adyen documentation as `.md` variants, the blog posts as HTML converted to text) and each quotation was compared with the fetched passage. Two sources were not readable at their own URL; both are in the table and in "Not verified". Larkfield facts are in "Larkfield consistency", not in the table.

Counts: 98 claims listed; 91 confirmed, 3 hedged, 2 not checked, 1 unreachable, 1 corrected.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe post: title, author Brandur Leach, displayed date February 22, 2017; evidence age 9 years (9 years 9 months) | https://stripe.com/blog/idempotency | confirmed | — |
| 2 | Quote, three failure cases: "The initial connection could fail … The call could fail midway … The call could succeed, but the connection break before the server can tell its client about it." | https://stripe.com/blog/idempotency | confirmed | — |
| 3 | Quote: idempotent endpoints "can be called any number of times while guaranteeing that side effects only occur once" | https://stripe.com/blog/idempotency | confirmed | — |
| 4 | Quote: "a client generates a unique ID to identify just that operation and sends it up to the server along with the normal payload. The server receives the ID and correlates it with the state of the request on its end." | https://stripe.com/blog/idempotency | confirmed | — |
| 5 | Quote: "On a failure midway through an operation, the server picks up the work and carries it through. The exact behavior is heavily dependent on implementation" | https://stripe.com/blog/idempotency | confirmed | — |
| 6 | 2017 post gives the reason for jitter: simultaneous retries, the "thundering herd problem" | https://stripe.com/blog/idempotency | confirmed | — |
| 7 | 2017 post gives rationale and no storage design (Differ row 7, Stripe cell) | https://stripe.com/blog/idempotency | confirmed | Read the whole post: no key store, schema or fingerprinting is described |
| 8 | Quote (scene): "A new key can start a second operation." | https://docs.stripe.com/error-low-level | confirmed | — |
| 9 | Quote: "When a connection fails, you might not know whether Stripe received or executed the request." | https://docs.stripe.com/error-low-level | confirmed | — |
| 10 | Quote: "Treat the outcome of a request that returns `500` as indeterminate: the operation might have produced side effects even though you received an error." | https://docs.stripe.com/error-low-level | confirmed | — |
| 11 | Replay header `Idempotent-Replayed: true` | https://docs.stripe.com/error-low-level | confirmed | — |
| 12 | Concurrent request with the same key returns `409` | https://docs.stripe.com/error-low-level ; https://docs.stripe.com/api/errors | confirmed | — |
| 13 | Quote: "Stripe retains keys for at least 24 hours and can remove them after that. Reusing a key after it’s removed can execute a new request." | https://docs.stripe.com/error-low-level | confirmed | — |
| 14 | Quote: "If the outcome is still unknown after that window, don’t retry with either the old key or a new one. Retrieve the relevant object, inspect the request in the Dashboard, and use webhook events to reconcile the outcome." | https://docs.stripe.com/error-low-level | confirmed | — |
| 15 | Quote: "During incident recovery, Stripe attempts to reconcile failed operations and send webhook events for any objects created during reconciliation. The cached response doesn’t change, and reconciliation isn’t guaranteed to resolve every operation." | https://docs.stripe.com/error-low-level | confirmed | — |
| 16 | Guide advises "a local identifier" in the object's metadata | https://docs.stripe.com/error-low-level | confirmed | — |
| 17 | Two key strategies: a random token "like UUID v4"; "Derive the key from a user-attached object, like the ID of a shopping cart. This provides a relatively straightforward way to protect against double submissions." | https://docs.stripe.com/error-low-level | confirmed | — |
| 18 | SDKs can generate keys and retry automatically (table row 1: only the SDK's own retries are covered) | https://docs.stripe.com/error-low-level | confirmed | — |
| 19 | Quote: "If your application retries across separate SDK calls or process restarts, generate and persist a key for the operation and supply it to every attempt." | https://docs.stripe.com/error-low-level | confirmed | — |
| 20 | Quote: "Use a new key for the corrected operation." | https://docs.stripe.com/error-low-level | confirmed | — |
| 21 | Stripe replays a stored decline while it holds the key (result cached "after the API method begins execution, including errors"; v1 "always returns the previously-saved response … even if it was an error") | https://docs.stripe.com/error-low-level ; https://docs.stripe.com/api-v2-overview | confirmed | — |
| 22 | `Stripe-Should-Retry`: `true` = "Retry the request using exponential backoff"; `false` = "Don’t retry the request." | https://docs.stripe.com/error-low-level | confirmed | — |
| 23 | A rate-limited request is refused before execution and caches no result | https://docs.stripe.com/error-low-level | confirmed | — |
| 24 | Quote: "Limit retries of an unresolved operation to the first 24 hours after the original request, using the same key and parameters." | https://docs.stripe.com/error-low-level | confirmed | — |
| 25 | Quote: "contact Stripe support before repeating the operation" | https://docs.stripe.com/error-low-level | confirmed | — |
| 26 | Quote: "For API v1, Stripe caches `500` responses from `POST` requests that use an idempotency key. Retrying with the same key returns the cached response while Stripe retains it." | https://docs.stripe.com/error-low-level | confirmed | — |
| 27 | Quote: "Don’t retry with a new idempotency key until you’ve resolved the original outcome." | https://docs.stripe.com/error-low-level | confirmed | — |
| 28 | Quote: "Sending the same idempotency key with different parameters produces an error indicating that the request didn’t match the original." | https://docs.stripe.com/error-low-level | confirmed | — |
| 29 | v1 key scope is the account ("unambiguously identify a single operation within your account") (Differ row 4) | https://docs.stripe.com/error-low-level | confirmed | — |
| 30 | Quote: "The idempotency layer compares incoming parameters to those of the original request and errors if they’re not the same to prevent accidental misuse." | https://docs.stripe.com/api/idempotent_requests | confirmed | — |
| 31 | Quote: "For API v1, Stripe saves the status code and body of the first request made with a given idempotency key after endpoint execution begins. Retries with the same key return the saved response, including `500` errors." | https://docs.stripe.com/api/idempotent_requests | confirmed | — |
| 32 | Nothing saved when validation fails or the request "conflicts with another request that’s executing concurrently" | https://docs.stripe.com/api/idempotent_requests | confirmed | — |
| 33 | Keys are "up to 255 characters long"; v1 keys apply to `POST` requests | https://docs.stripe.com/api/idempotent_requests | confirmed | — |
| 34 | Quote: "Avoid using sensitive data (for example, email addresses or personal identifiers) as idempotency keys." | https://docs.stripe.com/api/idempotent_requests | confirmed | — |
| 35 | Quote: "We generate a new request if a key is reused after the original is pruned." | https://docs.stripe.com/api/idempotent_requests | confirmed | — |
| 36 | `idempotency_error` for a key reused "on a request that does not match the first request’s API endpoint and parameters" | https://docs.stripe.com/api/errors | confirmed | — |
| 37 | v2 quote: "If the first request failed (or partially failed), the API re-executes the failed requests and returns the new response." | https://docs.stripe.com/api-v2-overview | confirmed | — |
| 38 | v2 replay conditions: "for the same API", "in the scope of the same account or sandbox", "within 30 days of each other"; `DELETE` covered | https://docs.stripe.com/api-v2-overview | confirmed | — |
| 39 | `/v1` namespace "includes most of the existing Stripe API today" | https://docs.stripe.com/api-v2-overview | confirmed | — |
| 40 | Payments are created at `/v1/payment_intents` | https://docs.stripe.com/api/payment_intents/create | confirmed | — |
| 41 | Refunds are created at `/v1/refunds` | https://docs.stripe.com/api/refunds/create | confirmed | Source entry added: the claim was in the text with no entry for the refund reference |
| 42 | "As of November 2026, the 24-hour replay governs 'charge this card' on Stripe" (follows from the two rows above; the error guide says its replay guidance applies to API v1) | https://docs.stripe.com/api/payment_intents/create ; https://docs.stripe.com/error-low-level | confirmed | — |
| 43 | Stripe developer blog, Ben Smith, displayed date 2025.4.10: "Stripe recognizes the idempotency key for 24 hours" | https://stripe.dev/blog/because-nobody-likes-being-charged-twice | confirmed | — |
| 44 | "No double charges" and "No idempotency key issues" listed among the advantages of the Payment Intents API | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 45 | Quote: "If the checkout process is interrupted and resumes later, attempt to reuse the same PaymentIntent instead of creating a new one." | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 46 | Quote: the key "is typically based on the ID that you associate with the cart or customer session in your application" | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 47 | Stripe documents the benefit of one PaymentIntent, not the mechanism that refuses a second confirmation (labeled as the author's reading) | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 48 | Adyen idempotency page: last modified 2020-07-30 (page metadata) | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 49 | Header `idempotency-key`, maximum 64 characters | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 50 | Quote: "If the Adyen payments platform already processed the request, the response to the first attempt will be returned without duplication." | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 51 | Quote: "Keys are stored at a company account level" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 52 | Quote: "Idempotency keys are valid for a period of 7 to 14 days after first submission." | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 53 | Quote: keys "will not be checked for duplication in other regions" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 54 | Duplicate before the first completes: HTTP 422 or 409 with "the error code 704" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | Bold markup aside |
| 55 | `transient-error` header `true` "indicates that the request can be retried at a later time using the same idempotency key" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 56 | Quote: "the API returns an HTTP 503 – Service Unavailable status with the error code 703" when the data store is unavailable | https://docs.adyen.com/development-resources/api-idempotency | confirmed | Bold markup aside |
| 57 | Quote: Adyen "must retain a consistent, stateful data store to compare each request against" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 58 | Quote: "an exponential backoff strategy when retrying transactions to avoid flooding the API" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 59 | Quote: "If the API does not return a transient error header, or returns a header with a value of false, do not retry the request." | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 60 | Quote: "Generate unique idempotency keys per request using the version 4 (random) UUID type to prevent two API credentials under the same account from accessing each others responses" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 61 | Quote: "The accounting rules in the Adyen payments platform take care of most potential double-processing issues that can impact payment modifications" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 62 | Quotes: "it is not possible to capture a higher amount than the authorized one"; "by default the total refunded value cannot exceed the captured amount." | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 63 | Quote: "you can either: Pause processing and retry the requests later (if this is feasible). Fall back to non-idempotent processing by not submitting the `idempotency-key` HTTP header." | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 64 | The key is echoed in the `idempotency-key` response header | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 65 | Adyen's page does not say what a reused key with a different body returns, whether an error response is stored, or what decides the point in the 7-to-14-day range | https://docs.adyen.com/development-resources/api-idempotency ; https://docs.adyen.com/development-resources/response-handling ; https://docs.adyen.com/development-resources/error-codes | confirmed | Checked the idempotency page, the HTTP status codes page, the 703 and 704 entries of the error-codes page, and searched https://docs.adyen.com/llms.txt for "idempot" (one page). The error-codes page was cited in the text without a source entry: entry added, wording made exact |
| 66 | Adyen status-code page asks for exponential backoff "with jitter" for HTTP 429 | https://docs.adyen.com/development-resources/response-handling | confirmed | Last-modified date (2021-05-12) added in the sentence and the entry |
| 67 | Mila's €84.00 refund sent twice exceeds the €120.00 captured "and be refused" | https://docs.adyen.com/development-resources/api-idempotency | hedged | The page supports the rule, not a statement about this request; now "so by that rule the second would be refused" |
| 68 | Terminal API: `ServiceID` required; "Must be unique within the last 48 hours for the terminal (`POIID`) being used." | https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api | confirmed | Last-modified date (2023-07-11) added in the sentence and the entry |
| 69 | Cancel by your own reference "up to 24 hours after authorization" | https://docs.adyen.com/online-payments/cancel | confirmed | Last-modified date (April 2023) added in the sentence |
| 70 | Adyen "Design to Duty" post: displayed date July 28th, 2021; evidence age 5 years | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | — |
| 71 | Quote: "The information needs to be available locally, so we eventually decided on integrating Cockroach, a distributed database, with our PALs" | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | Exact. The post writes "Cockroach" (a link), never "CockroachDB" |
| 72 | PAL = "The Payments Acceptance Layer (PAL) is a crucial service in our edge layer" | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | — |
| 73 | "no later source confirms the same database is still used" | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture | hedged | A Cockroach Labs post of 14 February 2023 ("The Price of Payments: How Adyen Guarantees Idempotency & Eliminates Downtime") exists in search results and in a third-party summary; its own URL returns 404, so it could not be read. Sentence narrowed to "no later Adyen publication that I could find says whether…" |
| 74 | Adyen has published nothing on the key record, expiry or recovery | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture ; https://docs.adyen.com/development-resources/api-idempotency | confirmed | As far as searched: the post, the documentation index and two web searches |
| 75 | Stripe has published nothing on where keys are stored, how a request is fingerprinted, or what "after endpoint execution begins" means internally | https://stripe.com/blog/idempotency ; https://docs.stripe.com/api/idempotent_requests ; https://docs.stripe.com/error-low-level | confirmed | As far as searched: the three Stripe pages and one web search, which returned only third-party accounts |
| 76 | Differ row 6, Stripe cell "Not public": behavior when Stripe's own key store is unavailable | https://docs.stripe.com/api/idempotent_requests ; https://docs.stripe.com/error-low-level | confirmed | No statement in either page; https://docs.stripe.com/llms.txt has no further idempotency page |
| 77 | Neither company has published how its calls to card networks and banks are made repeatable | https://docs.adyen.com/development-resources/api-idempotency ; https://docs.stripe.com/api/idempotent_requests | confirmed | As far as searched; both idempotency pages stop at the merchant-facing key |
| 78 | Brandur Leach's personal article, displayed date Oct 27, 2017; evidence age 9 years | https://brandur.org/idempotency-keys | confirmed | — |
| 79 | Key record holds a lock time, request parameters, stored response and a recovery point | https://brandur.org/idempotency-keys | confirmed | Schema read: `locked_at`, `request_params`, `response_code`, `response_body`, `recovery_point` |
| 80 | "atomic phases" committed before calls to other systems; a "completer"; a "reaper" that deletes keys after "about 72 hours" | https://brandur.org/idempotency-keys | confirmed | — |
| 81 | Quote: "Let’s look at how to design idempotency keys for an API by building a reference implementation."; built for a demo application (Rocket Rides) | https://brandur.org/idempotency-keys | confirmed | — |
| 82 | Airbnb post, Jon Chew and Ninad Khisti, 16 April 2019: a library chosen over a separate service because "We needed ultra low latency"; evidence age 7 years | https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb | unreachable | The article URL returns 403 to automated clients and the Internet Archive could not be fetched from this environment. Confirmed instead from the publication's own RSS feed (https://medium.com/feed/airbnb-engineering/tagged/payments), which carries the full text: "We needed ultra low latency, so building a separate, stand-alone idempotency service wouldn’t be sufficient." and "We chose a library as a solution because it offers low latency". Source entry now says how it was read |
| 83 | Marc Brooker, AWS Architecture Blog, 04 MAR 2015, updated May 2023: compares jitter variants, names "Full Jitter" | https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ | confirmed | Evidence-age flag (11 years) added in the text; it was only in the source entry |
| 84 | Adyen's Checkout API has no call that returns a payment (ruling 29 wording) | https://github.com/Adyen/adyen-openapi (json/CheckoutService-v72.json) | confirmed | Parsed v71 and v72: GET only on /paymentLinks/{linkId}, /sessions/{sessionId}, /storedPaymentMethods. The page cites it through [[payment-state-machines]] |
| 85 | Larkfield scene: Adyen "would have returned the refusal of 1 April without asking her bank again" | https://docs.adyen.com/development-resources/api-idempotency | hedged | Adyen's page does not say that a refusal is stored; now "by my reading of Adyen's page, which returns 'the response to the first attempt'", as the same point is already labeled in the key-choice section |
| 86 | ISO 8583 trace numbers and reversals | — | not checked | Paid standard; the page already labels it "industry practice, not a cited fact". Left as labeled; one-clause glosses added for ISO 8583 and reversal |
| 87 | No protocol between two parties delivers a message exactly once | — | not checked | A general distributed-systems result stated as the author's reasoning, no company fact; no source in the page |
| 88 | Excerpt, KEY POINTS, thesis paragraph: at least 24 hours (Stripe v1), 7 to 14 days (Adyen) | https://docs.stripe.com/error-low-level ; https://docs.adyen.com/development-resources/api-idempotency | confirmed | Blanket date note added to the thesis paragraph |
| 89 | Requirements table and figure captions: 24 hours, 7 to 14 days, 30 days | https://docs.stripe.com/error-low-level ; https://docs.adyen.com/development-resources/api-idempotency ; https://docs.stripe.com/api-v2-overview | confirmed | — |
| 90 | Differ row 1: retention windows | https://docs.stripe.com/error-low-level ; https://docs.stripe.com/api-v2-overview ; https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 91 | Differ row 2: what a repeat returns | https://docs.stripe.com/api/idempotent_requests ; https://docs.stripe.com/api-v2-overview ; https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 92 | Differ row 3: same key, different request (Stripe `idempotency_error`; Adyen not documented) | https://docs.stripe.com/api/errors ; https://docs.adyen.com/development-resources/api-idempotency ; https://docs.adyen.com/development-resources/error-codes | confirmed | — |
| 93 | Differ row 4: scope of a key | https://docs.stripe.com/error-low-level ; https://docs.stripe.com/api-v2-overview ; https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 94 | Differ row 5: in-flight duplicate and retry signal | https://docs.stripe.com/error-low-level ; https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 95 | Differ row 6, Adyen cell: 503 with code 703; pause, or resend without the key | https://docs.adyen.com/development-resources/api-idempotency ; https://docs.adyen.com/development-resources/error-codes | confirmed | — |
| 96 | Differ row 7, Adyen cell: 2021 post, a distributed database beside the edge layer | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | — |
| 97 | Established bullets (three cases, `500` "indeterminate", windows, one 2021 paragraph from Adyen) | https://stripe.com/blog/idempotency ; https://docs.stripe.com/error-low-level ; https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | — |
| 98 | Source entry title "Response handling" | https://docs.adyen.com/development-resources/response-handling | corrected | The page's title is "HTTP status codes"; entry retitled and given its last-modified date. The entry "Terminal API fundamentals" likewise retitled "Terminal API" (the page's title) and dated 2023-07-11 |

## The Adyen statement on its idempotency store (for the author's reconciliation list)

- Source: "Design to Duty: How we make architecture decisions at Adyen", Adyen knowledge hub, https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture. Date displayed on the page: **July 28th, 2021** (page metadata: `datePublished` 2021-07-28T15:00:00+02:00, `dateModified` 2025-12-17). The displayed and metadata dates agree (ruling 25).
- Section heading: "Distributed databases". Exact wording, in full:
  - "More recently we faced the challenge of making our payments API idempotent. This means that if a merchant sends us the same exact payment twice, we should only process it once but return the same response in both cases."
  - "As you now know, we do not want to achieve this by restricting payments of some merchants to certain machines, as this would mean the machines are no longer linearly scalable. The information needs to be available locally, so we eventually decided on integrating Cockroach, a distributed database, with our PALs."
  - "We could have built something ourselves here (probably on top of PostgreSQL) but this is really not our core business and there were several open-source options that satisfied our criteria. Nevertheless, getting properly acquainted with the DB and optimizing it to the point where we were satisfied with it required a substantial effort."
- The post says "Cockroach" (a hyperlink), not "CockroachDB". The chapter quotes it exactly and names the product nowhere else; the spec's open question writes "(CockroachDB)", which is the product behind the link but not the post's word.
- The post says nothing about the key record, fingerprinting, expiry, regions or recovery. It does not say the store is still in use today.
- So the journal-spec sentence "neither company has published how it stores idempotency keys" is too strong for Adyen: Adyen published, in July 2021, which kind of database holds the idempotency information and where it sits (with the PALs, its edge layer). The chapter's wording is accurate. Suggested journal-spec wording: "Stripe has published nothing on how it stores keys; Adyen one 2021 passage naming a distributed database beside its acceptance layer". The same phrase ("how keys are stored today is not public") is in the journal spec's introduction probe; it is true as written ("today") and can stay.
- A second, later source may exist and the author should decide whether to chase it: Cockroach Labs, "The Price of Payments: How Adyen Guarantees Idempotency & Eliminates Downtime", Cassie McAllister, 14 February 2023, formerly https://www.cockroachlabs.com/blog/adyen-guarantees-idempotency/. That URL returned 404 in this session; only a third-party summary (plushcap.com) was readable, which says Adyen moved from PostgreSQL to CockroachDB for this purpose. It is a database vendor's customer story, not an Adyen publication, and was not read first-hand, so it is not cited in the chapter.

## Links

All 17 URLs in Sources and Evidence were requested in this session. Sixteen return HTTP 200 with no redirect (14 original, 2 added: Stripe "Create a refund", Adyen "Error codes and messages"). The Airbnb Medium URL returns 403 to automated clients (it opens in a browser); kept, with the note in its entry. All nine `[[permalink]]` targets (`payment-api-design`, `payment-authorization`, `payment-webhooks-and-events`, `authorization-optimization`, `payment-developer-platform`, `payment-state-machines`, `in-person-payments`, `payment-reconciliation-and-reporting`, `payment-api-versioning`) are in the style guide's valid list. No external URL appears in the running text (ruling 22): nothing to reduce.

## Not verified, and what was done

- **Airbnb post at its own URL**: 403 from medium.com; the Internet Archive was not reachable from this environment. Read in full through the publication's RSS feed, which is the publisher's own copy. Both quotations and the date match. Listed as unreachable, not confirmed, because the cited URL itself was not read.
- **Cockroach Labs post of February 2023 about Adyen**: 404. Not used as evidence; the chapter sentence it would contradict was narrowed (row 73).
- **ISO 8583**: not readable (paid). The page says so and labels the paragraph as industry practice.
- **"No protocol delivers exactly once"**: no source in the page; left as the author's reasoning.
- **Negative claims** (rows 65, 74–77): confirmed only as far as the pages named and the searches described; a negative cannot be proved.

## Format and ruling changes

- Dates in the sentence: a blanket note was added to the thesis paragraph ("documentation accessed November 2026, as is every Stripe and Adyen documentation page quoted in this chapter"), because the sections on key choice, retry policy, limits and failures quoted documentation with no date.
- Evidence age: flag added in the text for the 2015 AWS post; last-modified dates added in the text and the entries for four Adyen documentation pages older than three years (HTTP status codes 2021-05-12, Error codes 2020-04-25, Terminal API 2023-07-11, Cancel 2023-04-03).
- Terms: one-clause glosses added for authorization (inside the capture gloss), ISO 8583, reversal and clearing files.
- Sources: two entries added, two retitled to the pages' real titles, the Airbnb entry's access note corrected. Every entry is used in the text; every source cited in the text has an entry.
- Rulings 4, 12, 13, 22 and 29 checked: the page links to chapter 20 for the receiver's contract, says "Adyen's Checkout API has no call that returns a payment", and has the attempt number in the key.
- No unit added, dropped, merged or reordered. `timetoread` stays 26 (6,042 words ÷ 230 = 26.3). Front matter, callouts, three KEY POINTS, required sections and the closing line are in place; American spelling; no banned words.
- `validate_spec.py` ok; `check_draft.py structure` pass; build clean; `render_check.py idempotency-and-retries` OK.

## Larkfield consistency

Checked against the ledger: 38% in a 6-hour window; 1 November 2026; 1,840 members; €71,300; €38.75 average (71,300 ÷ 1,840); 212 disputes; first requests approved (chapter 2's line); the timing-out provider left unnamed; K1 wording and the key form `renewal:M-204817:2026-11:1`; the row written before the first send; 20 hours and 6 days; the K2 sweep (Stripe object by metadata identifier, Adyen webhook then settlement report); Mila's pass (€120.00, Tuesday 9 March 2027, 19:42, Studio Noord on Adyen); the €84.00 refund of 18 March; the €49.00 renewal declined 1 April 2027 and tried again 4 April with keys ending `:2027-04:1` and `:2027-04:2`; €16.00 drop-in; Femke de Graaf leads Keel. Weekday checked: 9 March 2027 is a Tuesday. No contradiction found.

## Ledger conflicts

None.

## For other pages

- `journal-spec.json` (part-4 entry for this chapter, and any page that repeats it): "neither company has published how it stores idempotency keys" should be reworded as above.
- Any page that cites Adyen's "HTTP status codes" page as "Response handling", or the "Terminal API" page as "Terminal API fundamentals", has the wrong title; both pages carry last-modified dates (2021-05-12, 2023-07-11) and should not be cited as "n.d.".
- Any page citing the Airbnb idempotency post "through an Internet Archive copy": the Medium RSS feed `https://medium.com/feed/airbnb-engineering/tagged/payments` carries the full text.
