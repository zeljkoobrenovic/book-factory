# Verification — 20-webhooks-and-events (`payment-webhooks-and-events`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants (the HTML URLs were also requested and returned 200), the two Stripe developer posts and the Adyen knowledge-hub article as HTML, and three definitions from Adyen's OpenAPI repository as raw JSON (`CheckoutService-v72.json`, `BalancePlatformTransferNotification-v4.json`, `Webhooks-v1.json`), parsed and not read by eye. All 58 double-quoted strings in the article that come from a source were matched mechanically against the fetched texts after normalizing quotes and markup; all matched. Each row is one claim or one group of claims resting on the same passage.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe retries "for up to three days with an exponential back off in live mode" (key points, scene, contracts, tables, take-aways) | https://docs.stripe.com/webhooks | confirmed | Inline link removed (ruling 22) |
| 2 | Stripe: endpoint "must quickly return a successful status code (`2xx`) before any complex logic that could cause a timeout" | https://docs.stripe.com/webhooks | confirmed | — |
| 3 | Stripe publishes no number of seconds for the acknowledgement | https://docs.stripe.com/webhooks; https://docs.stripe.com/events/manage-webhook-endpoints; https://docs.stripe.com/events/how-events-work | confirmed | Negative: no figure on the three pages (searched for "second", "timeout"); one web search found only third-party estimates |
| 4 | Stripe's retry intervals are not published | https://docs.stripe.com/webhooks | confirmed | Negative: the retry section says only "exponential back off" |
| 5 | Sandbox: "We retry event deliveries created in a sandbox three times over the course of a few hours." | https://docs.stripe.com/webhooks | confirmed | — |
| 6 | Event definition: "When the state of another API resource changes, Stripe creates an `Event` object …" | https://docs.stripe.com/api/events | confirmed | Inline link removed |
| 7 | "You can access events through the Retrieve Event API for 30 days" | https://docs.stripe.com/api/events | confirmed | — |
| 8 | Adyen: "Many flows in Adyen integrations are asynchronous, meaning the final status of a resource is not known immediately after you make an API request." | https://docs.adyen.com/development-resources/webhooks | confirmed | Inline link removed |
| 9 | A capture can be rejected after the fact; a dispute arrives later (general statements) | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | `CAPTURE_FAILED`: "failed due to rejection by the card scheme". "Days" and "weeks" are the author's general wording, owned by chapters 4 and 8 |
| 10 | Adyen: "If Adyen does not receive this response within 10 seconds, … we mark the webhook as Failing and put it in a retry queue." | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | Date "last modified September 2026" replaced by "n.d., accessed November 2026" in the text and in Sources (ruling 30) |
| 11 | "Adyen's rule is recent" (the 10-second acknowledgement) | https://www.adyen.com/knowledge-hub/webhooks-accept-2xx | corrected | The page said the rule was recent. The article of 1 May 2024 says receivers "must accept a webhook within 10 seconds" under the old `[accepted]` approach too; what changed in 2024 is the acknowledgement by 2xx status. Sentence now says the deadline is old and the status-code acknowledgement is recent |
| 12 | Until 2024 "All integrations built with Adyen have been accepting webhooks by responding with a response body containing the string '[accepted]'" | https://www.adyen.com/knowledge-hub/webhooks-accept-2xx | confirmed | Displayed date "May 1st, 2024"; author Beppe Catanese, Developer Advocate. Attribution in the sentence now names the kind of source |
| 13 | Existing webhooks "are not automatically updated and keep functioning as before" | https://www.adyen.com/knowledge-hub/webhooks-accept-2xx | confirmed | — |
| 14 | Title of the knowledge-hub article in Sources ("Webhooks: accept with 2xx") | https://www.adyen.com/knowledge-hub/webhooks-accept-2xx | corrected | The displayed title is "Optimizing Webhook Integration: a new approach to accept events from the Adyen platform"; entry retitled, author added |
| 15 | Adyen: after a few more attempts the webhook is set to Failing; "we automatically try to send the webhook for up to 30 days" | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | "We retry sending the webhook message a few more times before we set the status of the webhook to Failing" |
| 16 | Published intervals grow from 30 seconds to 8 hours | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | Twelve intervals: 30 s, 30 s, 1, 2, 5, 10, 15, 30 min, 1, 2, 4, 8 h |
| 17 | "all webhook events to your endpoint go to the retry queue" | https://docs.adyen.com/development-resources/webhooks/configure-and-manage | confirmed | Inline link removed |
| 18 | "If a retry is successful, we continue with the next webhook in the queue." | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | — |
| 19 | Recovery burst: "the queued webhooks are sent in a short timeframe" (also the 429 row) | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | — |
| 20 | "Stripe doesn't guarantee the delivery of events in the order that they're generated." | https://docs.stripe.com/webhooks | confirmed | — |
| 21 | "Snapshot events record `created` in seconds … Don't use `created` to determine event order or whether you've already processed an event." | https://docs.stripe.com/webhooks | confirmed | — |
| 22 | Adyen: "always check the timestamp. Some webhooks also contain unique identifiers such as `sequenceNumber`" | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | — |
| 23 | The sequence number is on the transfer webhooks and "can help you restore the correct sequence of events even if they arrive out of order" | https://github.com/Adyen/adyen-openapi (json/BalancePlatformTransferNotification-v4.json) | confirmed | Parsed: `TransferData.sequenceNumber`, added in version 3. Sentence now names the specification and its version |
| 24 | The Standard webhook has only an `eventDate` (no sequence number, no event identifier) | https://github.com/Adyen/adyen-openapi (json/Webhooks-v1.json); https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | Parsed `AuthorisationNotificationRequestItem`: additionalData, amount, eventCode, eventDate, merchantAccountCode, merchantReference, operations, paymentMethod, pspReference, reason, success |
| 25 | No Adyen page read guarantees or disclaims delivery order | six pages under docs.adyen.com/development-resources/webhooks; https://docs.adyen.com/platforms/webhook-types; https://docs.adyen.com/platforms/transfer-transactions/track-webhooks; point-of-sale standard notifications | confirmed | Negative, bounded by "I read": searched these pages for "order", "guarantee", "out of order"; nothing beyond row 22 |
| 26 | "Webhook endpoints might occasionally receive the same event more than once." | https://docs.stripe.com/webhooks | confirmed | — |
| 27 | "In some cases, two separate Event objects are generated and sent. To identify these duplicates, use the ID of the object in `data.object` along with the `event.type`." | https://docs.stripe.com/webhooks | confirmed | — |
| 28 | Adyen duplicates "have the same values in the `eventCode` and `pspReference` fields … Your server should use the details from the latest webhook event." | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | — |
| 29 | The PSP reference is a 16-character identifier | https://github.com/Adyen/adyen-openapi (json/Webhooks-v1.json) | confirmed | "Adyen's 16-character unique reference associated with the transaction or request". Acronym PSP expanded in the text |
| 30 | Stripe guide shows how to list undelivered events and process them | https://docs.stripe.com/events/manage-webhook-endpoints | confirmed | `delivery_success=false` with `ending_before`; "Stripe only returns events created in the last 30 days" |
| 31 | "Stripe still considers manually processed events as undelivered and continues its automatic retry schedule." | https://docs.stripe.com/events/manage-webhook-endpoints | confirmed | — |
| 32 | Checkout API v72 has three read operations and none returns a payment by its PSP reference | https://github.com/Adyen/adyen-openapi (json/CheckoutService-v72.json) | confirmed | Parsed: GET on `/paymentLinks/{linkId}`, `/sessions/{sessionId}`, `/storedPaymentMethods`. The session read needs the `sessionResult` value from the client and returns a session's result, so "sessions" was reworded "session results" |
| 33 | "Adyen has no call that returns a payment" (key points, contracts, receiver, differ table, Larkfield, outage, take-aways) | https://github.com/Adyen/adyen-openapi; ruling 29 | hedged | Scoped in seven places to the Checkout API and online payments (ruling 29): the Terminal API has a transaction status request for in-person payments |
| 34 | Adyen recovery: Retry and Ignore in the Customer Area; alerts "after 5 retry attempts" and "after 7 days of a webhook failing" | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | — |
| 35 | Stripe: "Without verification, an attacker could send fake webhook events to your endpoint …" | https://docs.stripe.com/events/manage-webhook-endpoints | confirmed | The sentence is on the managing-endpoints page, not the webhooks page; the Sources entry now says so |
| 36 | `Stripe-Signature` carries `t` and `v1`; HMAC with SHA-256 over the timestamp, a dot and "the unmodified HTTP request body" | https://docs.stripe.com/webhooks | confirmed | — |
| 37 | The timestamp is signed, so an attacker cannot change it; "Our libraries have a default tolerance of 5 minutes …" | https://docs.stripe.com/webhooks | confirmed | — |
| 38 | "If Stripe retries an event …, then we generate a new signature and timestamp for the new delivery attempt." | https://docs.stripe.com/webhooks | confirmed | — |
| 39 | Adyen Standard webhook: eight fields joined with colons, HMAC with SHA-256, signature inside the payload | https://docs.adyen.com/development-resources/webhooks/secure-webhooks/verify-hmac-signatures | confirmed | Fields and order as listed; signature in `additionalData.hmacSignature` |
| 40 | `eventDate` is not signed and no tolerance window is documented | https://docs.adyen.com/development-resources/webhooks/secure-webhooks/verify-hmac-signatures | confirmed | Negative: the page has no "tolerance", "replay" or timestamp check |
| 41 | OAuth 2.0 "strongly recommended and supported for the Standard webhook and all Balance Platform webhook types" | https://docs.adyen.com/development-resources/webhooks/secure-webhooks | confirmed | — |
| 42 | Basic authentication "only guarantees that the webhook event was sent by Adyen, not that it wasn't modified during transmission" | https://docs.adyen.com/development-resources/webhooks/secure-webhooks | confirmed | — |
| 43 | "There is no address list to allow": "We do not provide a list of IP addresses." | https://docs.adyen.com/development-resources/webhooks/secure-webhooks | hedged | The quotation is exact, but the same section offers a domain allowlist (`out.adyen.com`) and DNS resolution. Now "no fixed address list", with the domain named |
| 44 | Inference block: a Standard webhook would verify again if replayed | same page as row 39 | confirmed | Labeled inference; the fact it rests on (row 40) is confirmed |
| 45 | Stripe: "Because this snapshot can be stale by the time your application processes it, fetch the latest version of the resource from the API before acting on the data." | https://docs.stripe.com/events/how-events-work | confirmed | — |
| 46 | "The API version in your account settings when the event occurs dictates the API version, and therefore the structure of an Event sent to your destination." | https://docs.stripe.com/events/how-events-work | confirmed | — |
| 47 | Adyen: "Webhook messages contain a snapshot of the resource so your system can update its state accordingly" | https://docs.adyen.com/development-resources/webhooks | confirmed | The sentence stands in a paragraph on state management whose example is the platform product |
| 48 | Thin event: type and identifiers, no state; "For new integrations, use thin events. Thin events are unversioned, fully typed in the Stripe SDKs, …" | https://docs.stripe.com/events/how-events-work | confirmed | — |
| 49 | Thin events first shipped in September 2024 "for one new API" | https://docs.stripe.com/changelog/acacia/2024-09-30/api-v2-thin-events | confirmed | "The Meters API is the first API to use thin events." Sentence now names the changelog, its date and the API; Sources title corrected to the page's title |
| 50 | A June 2026 Stripe post "still offered" early access to thin events for v1 resources; "check the catalog" | https://stripe.dev/blog/event-notification-handlers-thin-events; https://docs.stripe.com/api/v2/core/events/event-types | corrected | The quotation is exact (post displayed 2026.6.24, David Brownman). But the status has moved: the thin event catalog today lists "all public thin events we currently send for /v1 and /v2 resources", including eight `v1.payment_intent.*` types, thirteen `v1.charge.*` and three `v1.refund.*`. Sentence now states this; catalog added to Sources. The catalog carries no preview or general-availability label |
| 51 | A thin event costs one API read per event, which counts against request limits | https://docs.stripe.com/events/how-events-work | confirmed | The page says the code "retrieves the current resource from the API"; that the read counts against limits is not stated on the page and follows from its being an ordinary API request |
| 52 | "Stripe pushes events to your configured destinations, which can be webhook endpoints, Amazon EventBridge, or Azure Event Grid" | https://docs.stripe.com/events/how-events-work | confirmed | — |
| 53 | Event destinations generally available, October 2024; merchants "can trust each event is from Stripe without needing to verify webhook signatures in their code" | https://stripe.dev/blog/growing-your-stripe-integration-with-event-destinations | confirmed | Displayed 2024.10.31, Ben Smith: "Event Destinations is now in GA and rolling out to all accounts" |
| 54 | The EventBridge page repeats the three days of retries and the sentence on order | https://docs.stripe.com/event-destinations/eventbridge | confirmed | — |
| 55 | No destination other than HTTP in Adyen's documentation | https://docs.adyen.com/llms.txt; https://docs.adyen.com/development-resources/webhooks/configure-and-manage | confirmed | Negative: index searched for EventBridge, Event Grid, Pub/Sub, Kafka, SQS, event bus; no hit. Delivery methods are JSON, HTTP POST or SOAP |
| 56 | Neither company has published how its webhook sender is built | web search (two queries); https://docs.stripe.com/llms.txt; https://docs.adyen.com/llms.txt | confirmed | Negative: searches returned receiver-side guidance and third-party designs only |
| 57 | Stripe: "Events are delivered asynchronously"; "a maximum of 16 event destinations" | https://docs.stripe.com/events/how-events-work | confirmed | — |
| 58 | "each destination has its own signing secret and its own delivery log with the time of the next retry" | https://docs.stripe.com/webhooks | hedged | Signing secrets belong to webhook endpoints (`whsec_`); the "Event deliveries" tab with the next retry is per destination. Reworded to "each webhook endpoint has its own signing secret, and each destination its own delivery log" |
| 59 | Adyen's pages show a Failing status and a retry queue per endpoint; inference block on queue per endpoint versus independent deliveries | rows 15, 17, 18, 20 | confirmed | Labeled inference; the quoted facts are confirmed |
| 60 | Adyen's order: verify, "Store the webhook message in your database or a queue so you can process it later", accept, process; "Make sure that you acknowledge the webhook before applying any business logic …" | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | — |
| 61 | Stripe: "you must return a `200` response before updating a customer's invoice as paid in your accounting system" | https://docs.stripe.com/webhooks | confirmed | — |
| 62 | Requirements table, documented column (10 seconds; "quickly"; three days and 30 days; store then accept) | rows 1, 2, 10, 15, 60 | confirmed | — |
| 63 | "Adyen does not send a webhook message when a payment settles successfully" | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | Inline link removed; date added to the sentence |
| 64 | Differ table, seven rows, Stripe and Adyen cells | rows 1–58 | confirmed | Each cell traced to a row above; the "Reading state back" Adyen cell scoped (row 33). "No other destination found" checked against the index (row 55) |
| 65 | Outage table: Stripe events 3 to 30 days old can be listed; after 30 days "full event payloads are gone" | https://docs.stripe.com/events/how-events-work; https://docs.stripe.com/events/manage-webhook-endpoints | confirmed | "Events older than 30 days: you can only see a summary view with truncated fields" |
| 66 | Outage table: Adyen beyond 30 days is "Not documented" | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | The page says "up to 30 days" and nothing about what follows |
| 67 | Outage example: Friday 18:00 to Wednesday 09:00; "events of Friday evening and Saturday are past their three days" | arithmetic | corrected | Three days before Wednesday 09:00 is Sunday 09:00; reworded "from Friday evening to early Sunday" |
| 68 | Stripe: "Any large spike in webhook deliveries (for example, during the beginning of the month when all subscriptions renew) might overwhelm your endpoint hosts." | https://docs.stripe.com/webhooks | confirmed | — |
| 69 | Adyen 422 row: "We recommend acknowledging receipt with `[200 OK]` first, and performing business logic separately." | https://docs.adyen.com/development-resources/webhooks/troubleshoot | confirmed | — |
| 70 | "Any manipulation to the raw body of the request causes the verification to fail" | https://docs.stripe.com/webhooks | confirmed | — |
| 71 | Adyen: "you can still accept webhook events signed with your previous HMAC key for some time" | https://docs.adyen.com/development-resources/webhooks/secure-webhooks | confirmed | — |
| 72 | Take-aways, "Established" bullets | rows 1, 15, 20, 26, 28, 33, 45, 56, 60 | confirmed | Checkout API bullet scoped to online payments |

**Counts:** 72 claims checked: 65 confirmed, 4 corrected (rows 11, 14, 50, 67), 3 hedged (rows 33, 43, 58), 0 unsupported, 0 unreachable.

## Links

All 17 URLs that were in Sources and Evidence return HTTP 200 with no redirect. One entry was added (Stripe's thin event catalog, 200). No entry was unused; three "what it supports" clauses were trimmed to what the text uses (Stripe secret rolling and resend limits, Adyen delivery formats and version setting are not in the text). All nine distinct `[[permalink]]` targets are in the style guide's valid list. Sixteen inline external links were reduced to plain attributions (ruling 22); none is left in the running text.

## Rulings applied

- **Ruling 20:** the article named no weekday. It now says Monday 14 September 2026, the certificate expiring shortly after midnight, and members turned away on Monday morning. "That night" is now "those nine hours". In `spec.json` the two notes that mentioned "Saturday night" (an open question and a decision-log entry) were rewritten to the ruling, and "night" in four unit descriptions became "outage" or "nine hours".
- **Ruling 22:** see Links.
- **Ruling 29:** row 33.
- **Ruling 30:** "last modified September 2026" removed from the text, the Sources entry and four evidence entries in `spec.json`.
- **Ruling 28:** the Larkfield section already says the reconciliation job writes ledger entries from the report, not from the webhook. No change.

## Format

Front matter complete; `timetoread` 26 min equals 6,005 words ÷ 230. Three key points, three failure patterns, all required sections present. Glosses added on first use: settlement report, direct debit, PSP. A missing comma after "who leads Keel" fixed. No banned words; British spellings occur only in Adyen's `AUTHORISATION`.

## Could not verify, and what was done

- Nothing was unreachable.
- Four negatives (rows 3, 4, 55, 56) and row 25 rest on searches of the named pages, the two documentation indexes and three web searches. They are worded in the article as what was found or not found, which is what the evidence supports.
- Row 51: the cost of a thin event against request limits is not stated by Stripe in so many words. Kept, since the fetch is an ordinary API request; chapter 21 owns the limits.
- Stripe's thin event catalog has no label saying whether v1 thin events are generally available or in preview. The article states only that the catalog lists them.

## Ledger conflicts

None. The ledger's Silent Webhook line already agrees with ruling 20. Mila's dates check: 9 March 2027 is a Tuesday, 18 March 2027 a Thursday, 14 September 2026 a Monday.

## For other pages

- **`journal-spec.json`, entry for this page:** three fields copied into the post spec still say Adyen "has no call that returns a payment" without the scope of ruling 29: `intent.outcome.know` ("no call to read a payment back"), acceptance criterion AC-1 (probe and expected answer) and `thesis.so_what`. The validator requires them to equal the journal spec, so they were left as they are in the post spec. Whoever owns the journal spec should scope them and copy the change here.
- **Any page that cites Adyen's 2024 change of acknowledgement:** the 10-second deadline predates it; only the 2xx acknowledgement is new. The article's displayed title is "Optimizing Webhook Integration: a new approach to accept events from the Adyen platform" (Beppe Catanese, 1 May 2024).
- **Any page that says thin events for v1 resources are in early access** (chapter 19 on versioning is the likely one): Stripe's thin event catalog lists v1 payment, charge, refund, invoice and subscription types as of November 2026.
- **Any page that says Adyen gives nothing to allowlist:** it gives no IP list, but names the domain `out.adyen.com`.
