# Verification — 08-payment-state-machines (`payment-state-machines`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants, the Stripe engineering post and the Adyen knowledge-hub post as HTML, the Checkout API definition as the raw JSON file from Adyen's repository (parsed, not read by eye). All 59 double-quoted strings taken from sources were matched mechanically against the fetched texts after normalizing quotes and markup; the two that did not match mechanically were read by hand (rows 27 and 33). Each row is one claim or one group of claims resting on the same passage.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Post title, author Michelle Bu, displayed date 2020.12.15 ("December 2020") | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 2 | Original design 2011–2015: Token made in the browser, Charge made on the server | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 3 | Quote: card payments "can be immediately finalized" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 4 | Quote: finalized = "a user has sufficient confidence the funds are guaranteed" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 5 | Evidence-age flag on the 2020 post (5 years 11 months, stated as 6) | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 6 | ACH debit and Bitcoin added in 2015; ACH finalized days later | https://stripe.dev/blog/payment-api-design | confirmed | Acronym ACH expanded |
| 7 | `pending` state added to the Charge; quote "days later, when they received a webhook" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 8 | Bitcoin needed a second object; quote "managing two state machines … BitcoinReceiver on the client and Charge on the server" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 9 | Sources API dated 2015–2017; quote "a client-driven state machine" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 10 | iDEAL: customer is redirected to the bank; quote "the next request to create a Charge wouldn't make it through, even though the customer believes they paid" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 11 | Quote "we'd refund the money associated with the Source after a few hours. This is a conversion nightmare." | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 12 | Two-by-two table of payment methods (all four cells, 15 methods) as in the post's last table | https://stripe.dev/blog/payment-api-design | confirmed | Gloss added to the direct-debit cell (US, euro-area, UK, Australian) |
| 13 | Cards are the only method in the cell "immediately finalized, no customer action"; quote "Global payment methods aren't different; cards are!" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 14 | Quote "Charges and Tokens were foundational in the API because they were the first APIs we had, not because they were the right abstraction for global payments." | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 15 | Between 2011 and 2018 the Charge grew "from having 11 properties to 36 properties" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 16 | PaymentIntent introduced in 2018 (key points, Stripe section) | https://stripe.dev/blog/payment-api-design | confirmed | Post heading: "Introducing PaymentIntents and PaymentMethods (2018)" |
| 17 | Quote "There's no failed state because if a single payment attempt fails, the PaymentIntent goes back to the requires_payment_method state …" | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 18 | Stripe keeps each attempt as a Charge | https://stripe.dev/blog/payment-api-design | confirmed | Post: "create a Charge object for each payment attempted by the PaymentIntent" |
| 19 | `next_action` examples: "a generic redirect_to_url" and `oxxo_display_details` for a voucher | https://stripe.dev/blog/payment-api-design | confirmed | — |
| 20 | Two actions, create and confirm; intent "typically correlates with a single shopping cart or customer session" | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 21 | Client secret "lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones" | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 22 | Each intent "has a unique ID that you can use to retrieve it" | https://docs.stripe.com/payments/payment-intents | confirmed | — |
| 23 | The intent has seven statuses (enum of seven values) | https://docs.stripe.com/api/payment_intents/object | confirmed | — |
| 24 | `requires_payment_method`: "until you attach a payment method" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 25 | `requires_confirmation`: "ready to confirm. Most integrations skip this state" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 26 | `requires_action`: "the payment requires additional actions, such as authenticating with 3D Secure" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 27 | `processing`: "the payment uses an asynchronous payment method, such as bank debits" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | The .md variant inserts a glossary tooltip inside the sentence; the rendered sentence is as quoted |
| 28 | `requires_capture`: "If you're separately authorizing and capturing funds" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 29 | `succeeded`: "the corresponding payment flow is complete" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 30 | `canceled`: cancellation "releases any held funds, and can't be undone" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 31 | `latest_charge`: "ID of the latest Charge object created by this PaymentIntent" | https://docs.stripe.com/api/payment_intents/object | confirmed | — |
| 32 | Create the intent early "so Stripe can record all attempted payments" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 33 | Quote "Don't attempt to handle order fulfillment on the client side because customers can leave the page after payment is complete" | https://docs.stripe.com/payments/payment-intents/verifying-status | confirmed | Tooltip inside the sentence in the .md variant, as above |
| 34 | Use the `payment_intent.succeeded` event (table cell) | https://docs.stripe.com/payments/payment-intents/verifying-status | confirmed | — |
| 35 | Polling is allowed "but it's much less reliable and might trigger rate limits" | https://docs.stripe.com/payments/payment-intents/verifying-status | confirmed | — |
| 36 | Capture is a call on an intent in `requires_capture` | https://docs.stripe.com/api/payment_intents/capture | confirmed | Attribution "In Stripe's API reference" added after the inline link was removed |
| 37 | `amount_to_capture` "must be less than or equal to the original amount" | https://docs.stripe.com/api/payment_intents/capture | confirmed | — |
| 38 | Uncaptured intents "are cancelled a set number of days (7 by default) after their creation" | https://docs.stripe.com/api/payment_intents/capture | confirmed | — |
| 39 | Refund is an object whose status "can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`" | https://docs.stripe.com/api/refunds/object | confirmed | — |
| 40 | A dispute is another object (and "a Dispute object on the charge" in the Larkfield table) | https://docs.stripe.com/api/disputes/object | confirmed | Source was not listed; fetched and added to Sources. `charge`: "ID of the charge that's disputed" |
| 41 | Quote "Subsequent refunds, disputes, and outcomes are reflected on the Charge. These might change what you see in the Dashboard, even though the PaymentIntent remains `succeeded`." | https://docs.stripe.com/payments/payment-intents/verifying-status | confirmed | — |
| 42 | Setup Intents "set up payment credentials but don't process payments" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 43 | "Both Payment Intents and Setup Intents go through the same set of states." | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 44 | Statuses renamed in API version 2019-02-11; quote "Versions of the API before 2019-02-11 show `requires_source` …" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | The linked changelog page (docs.stripe.com/changelog/2019-02-11/renames-several-statuses-payment-intents) also resolves |
| 45 | "Stripe recommends using the Checkout Sessions API … over Payment Intents for most integrations" | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | The elided words are "with the Payment Element" |
| 46 | "Webhook endpoints might occasionally receive the same event more than once" | https://docs.stripe.com/webhooks | confirmed | — |
| 47 | "Stripe doesn't guarantee the delivery of events in the order that they're generated" | https://docs.stripe.com/webhooks | confirmed | — |
| 48 | The guard Stripe gives against duplicates is the event ID | https://docs.stripe.com/webhooks | confirmed | — |
| 49 | `resultCode` `presentToShopper` in Checkout API v41, 14 February 2019 | https://docs.adyen.com/online-payments/release-notes | confirmed | Evidence-age flag added (entry is 7 years old) |
| 50 | v49, 14 May 2019: "The response now contains an `action` object that indicates the action to be taken for completing the payment." | https://docs.adyen.com/online-payments/release-notes | confirmed | Evidence-age flag added |
| 51 | Captures and refunds joined the Checkout API on 3 June 2021 | https://docs.adyen.com/online-payments/release-notes | confirmed | Entry lists captures, amountUpdates, refunds, reversals, cancels |
| 52 | `POST /sessions` on 6 October 2021, version 68 | https://docs.adyen.com/online-payments/release-notes | confirmed | — |
| 53 | "Why Adyen chose this shape is not on record" | https://www.adyen.com/knowledge-hub/sessions-api-faster-integration | corrected | Adyen published a reason for one step: a developer-advocate post displayed as 5 October 2021 says "the number of API calls needed when integrating will be reduced from three to only one". Sentence now says so, and limits "not on record" to result codes and modifications. Source added |
| 54 | Adyen has published no design history comparable to Stripe's | https://www.adyen.com/knowledge-hub/sessions-api-faster-integration; web search; https://docs.adyen.com/llms.txt | confirmed | Searched Adyen's documentation index and the web; found the 2021 sessions post and a 2022 "API-first at Adyen" post, neither a design history of the payment model. Kept |
| 55 | Session: created by the server, used by Drop-in and Components | https://docs.adyen.com/online-payments/build-your-integration/sessions-flow | confirmed | — |
| 56 | Session expires "1 hour after session creation" by default, never later than 24 hours | https://docs.adyen.com/online-payments/build-your-integration/sessions-flow | confirmed | — |
| 57 | "The `status` included in the response doesn't get updated. Do not make the request again to check for payment status updates." | https://docs.adyen.com/online-payments/build-your-integration/sessions-flow | confirmed | — |
| 58 | 3-D Secure 2 codes `IdentifyShopper`, `ChallengeShopper`, `RedirectShopper` and their meanings | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | The page also has an "authentication-only" group for standalone authentication, which the table does not list (not a claim) |
| 59 | Intermediate codes `Received`, `Pending`, `PresentToShopper`; "the payment has not reached a final state yet"; `Received` "is the initial state for all payments" | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 60 | `PartiallyAuthorised`: "The payment was authorized for a partial amount" | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 61 | Final codes `Authorised`, `Refused`, `Cancelled`, `Error`: "the payment has reached a final state" | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 62 | Action types `redirect`, `threeDS2`, `qrCode`, `sdk`, `voucher`, `await` | https://docs.adyen.com/online-payments/build-your-integration/advanced-flow | confirmed | — |
| 63 | "You do not need to do anything to handle the redirect in this case. Instead, wait for the webhook" | https://docs.adyen.com/online-payments/build-your-integration/sessions-flow | confirmed | — |
| 64 | "The status of a payment can sometimes change after you get the result code, so we recommend that you do not use the result code to update your order management system." | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 65 | `AUTHORISATION`: "Although you can use the payment result from the API, we recommend that you rely on the webhook to trigger any business logic" | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | — |
| 66 | Modifications: capture, cancel, refund, reversal, amount update, each a separate request | https://docs.adyen.com/online-payments/release-notes; https://docs.adyen.com/adyen-glossary; https://github.com/Adyen/adyen-openapi (json/CheckoutService-v72.json) | confirmed | Glossary names capture, cancel, refund; the 2021 release note and the v72 definition list all five endpoints |
| 67 | PSP reference is a 16-character identifier Adyen gives "every request" | https://docs.adyen.com/adyen-glossary | hedged | Glossary: "Every payment or modification request … has a globally unique 16-character string". Reworded to "every payment and modification request"; PSP expanded |
| 68 | Capture answer: "`status`: **received**. Your capture request will be processed asynchronously. You will receive the result in a webhook." | https://docs.adyen.com/online-payments/capture | confirmed | — |
| 69 | HTTP 200 on a capture: "We still do not know if the capture operation will be successful or not." | https://docs.adyen.com/development-resources/response-handling | confirmed | — |
| 70 | After `CAPTURE` success: "In rare cases the card scheme can still reject the capture, and you will receive a CAPTURE_FAILED webhook"; "can even happen a few days after you submitted the capture request" | https://docs.adyen.com/online-payments/capture | confirmed | — |
| 71 | Refunds: `REFUND_FAILED` after a successful `REFUND`; `REFUNDED_REVERSED` for some bank methods | https://docs.adyen.com/online-payments/refund | confirmed | Page: "bank transfers, iDEAL, or Bancontact" |
| 72 | "Adyen does not send a webhook message when a payment settles successfully." (used twice) | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | — |
| 73 | Checkout API v72 has three GET operations; none returns a payment by identifier | https://github.com/Adyen/adyen-openapi (json/CheckoutService-v72.json) | confirmed | Parsed the definition: 31 operations, GET on /paymentLinks/{linkId}, /sessions/{sessionId}, /storedPaymentMethods. v72 is the newest file in the repository and the version the release notes recommend |
| 74 | A payment "can be looked up only" in the Customer Area and reports, "which use a second, longer vocabulary of statuses" | https://docs.adyen.com/account/payments-lifecycle; https://docs.adyen.com/reporting/reports-and-the-payments-lifecycle; https://docs.adyen.com/online-payments/build-your-integration/sessions-flow | hedged | Statuses and both places confirmed (the reports page was not a listed source; added). "Only" is not true of in-person payments: the Terminal API has a transaction status request. Scoped to "an online payment" and reworded to what the documentation gives |
| 75 | INFERENCE block: the integrator's table is the only record it can query by API | https://github.com/Adyen/adyen-openapi (json/CheckoutService-v72.json) | hedged | Rests on the fact above; scoped to "the two documented contracts for online payments" |
| 76 | Adyen duplicates "have the same values in the `eventCode` and `pspReference` fields" | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | — |
| 77 | Adyen: "always check the timestamp" | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | — |
| 78 | "Your server should use the details from the latest webhook event." | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | — |
| 79 | Neither provider guarantees event order | https://docs.stripe.com/webhooks; https://docs.adyen.com/development-resources/webhooks/handle-webhook-events | confirmed | Stripe says so outright; Adyen gives no guarantee and tells receivers to order by timestamp |
| 80 | Stripe API version 2019-02-11 renamed PaymentIntent statuses (design section) | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 81 | Differ row 1: retrievable PaymentIntent vs result code, webhooks, no payment GET in v72 | https://docs.stripe.com/payments/payment-intents; https://github.com/Adyen/adyen-openapi (json/CheckoutService-v72.json) | confirmed | — |
| 82 | Differ row 2: failed attempt returns to `requires_payment_method`, attempts as Charges vs final codes `Refused`, `Error`, `Cancelled`, own PSP reference | https://stripe.dev/blog/payment-api-design; https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes; https://docs.adyen.com/adyen-glossary | confirmed | — |
| 83 | Differ row 3: `requires_action` with `next_action`, `processing` vs `action` object (v49, May 2019), `ChallengeShopper`, `Pending`, `Received` | https://docs.stripe.com/payments/paymentintents/lifecycle; https://docs.adyen.com/online-payments/release-notes; https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 84 | Differ row 4: capture on the intent, Refund with `failed` vs modifications answered `received`, `CAPTURE_FAILED`, `REFUND_FAILED` | https://docs.stripe.com/api/payment_intents/capture; https://docs.stripe.com/api/refunds/object; https://docs.adyen.com/online-payments/capture; https://docs.adyen.com/online-payments/refund | confirmed | Refund response `"status": "received"` confirmed on the refund page |
| 85 | Differ row 5: both advise against acting on the synchronous result | https://docs.stripe.com/payments/payment-intents/verifying-status; https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 86 | Differ row 6, Adyen: "Sessions flow is the default integration that we recommend" (`/sessions` since v68, October 2021) | https://docs.adyen.com/online-payments/build-your-integration; https://docs.adyen.com/online-payments/release-notes | confirmed | — |
| 87 | Differ row 7, Adyen cell: "Not public" | https://www.adyen.com/knowledge-hub/sessions-api-faster-integration | corrected | Replaced with "Not public for result codes and modifications; a developer-advocate post (2021) gives the reason for `/sessions`"; last column adjusted to "most of Adyen's cannot" |
| 88 | `AUTHORISATION` webhook carries a `success` field; `REFUND` and `CAPTURE` likewise | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | — |
| 89 | "A payment that is automatically captured does *not* trigger a separate CAPTURE webhook." | https://docs.adyen.com/online-payments/capture | confirmed | — |
| 90 | `NOTIFICATION_OF_CHARGEBACK` and `CHARGEBACK` webhooks exist | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | — |
| 91 | "Technical failures are automatically re-captured by Adyen within 10 business days." | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | — |
| 92 | Card offers "expire after 12 hours by default" | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | OFFER_CLOSED row: "For cards, offers expire after 12 hours by default." |
| 93 | Sweep on Adyen can use redelivery and the Customer Area's transaction list | https://docs.adyen.com/development-resources/webhooks/handle-webhook-events; https://docs.adyen.com/online-payments/build-your-integration/sessions-flow | confirmed | Retry queue on the webhook page; "Transactions list in your Customer Area" on the sessions page |
| 94 | Take-away: Stripe Refund has a `failed` status; Adyen documents failures days after a success | https://docs.stripe.com/api/refunds/object; https://docs.adyen.com/online-payments/capture; https://docs.adyen.com/online-payments/refund | confirmed | — |

Counts: 94 claims checked: 89 confirmed, 2 corrected, 3 hedged, 0 unsupported, 0 unreachable, 0 not checked.

## Links

All 24 URLs in Sources and Evidence return HTTP 200 without redirects (21 original, 3 added: the Stripe Dispute object, Adyen's "Reports and the payments lifecycle", the Adyen knowledge-hub post on sessions). All ten `[[permalink]]` targets in the page are in the style guide's valid list; `[[local-payment-methods]]` was added in the Larkfield scene.

## Not verified, and what was done

- Nothing was unreachable. "Adyen has published no design history comparable to Stripe's" is a negative: it rests on a search of Adyen's documentation index and one web search, which found two Adyen posts (sessions, 2021; API-first, 2022), neither a design history of the payment model. The sentence is kept; the stronger "not on record" and "Not public" were corrected (rows 53 and 87).
- The requirements table's "Seconds" for the API response is labeled *(assumption)* on the page and was not checked as a fact. Statements about what a customer action or a bank debit typically takes are the author's general description, not attributed to a source.
- Adyen's "at least once, no guaranteed order" is the page's summary; Adyen documents duplicates and ordering by timestamp but does not use those words (row 79).

## Format and ruling changes

- Ruling 22: 20 inline external links in the running text and the comparison table reduced to plain text; every URL was already in Sources. Attribution added where the link had carried it (the Stripe post, Stripe's API reference, Adyen's OpenAPI definition).
- Evidence age: flag added for the Adyen release-note entries of 2019 and 2021 (text and source entry) and for the 2021 knowledge-hub post (source entry; the year is in the sentence).
- Acronyms expanded on first use: SEPA, ACH, PSP. Bacs and BECS glossed in the table cell.
- Sources: the entry `[[commerce-payments]]` in ORDERED was not cited anywhere in the text and was removed (group now "None.").
- `timetoread` changed from 23 to 24 (5,436 words ÷ 230 = 23.6).
- No unit added, dropped, merged or reordered; `validate_spec.py`, `check_draft.py structure`, the build and `render_check.py` pass.

## Larkfield consistency

- Checked against the ledger: 12 January 2027 set-up (€49, typed Visa debit, 3-D Secure in the banking app); Tuesday 9 March 2027 19:42 pass (€120.00, phone wallet, no challenge, Studio Noord on Adyen, automatic capture, payout 11 March); €84.00 refund on 18 March; the Silent Webhook (September 2026, nine hours, 3,200 memberships, no weekday named); K2 wording; the chapter's own ledger line (fields, `paid` back to `authorized`, late March review). 9 March 2027 is a Tuesday.
- Fixed: the scene said Tom Hendriks built the payment record store in 2024; the ledger says he built the payment service in 2024. Reworded to the ledger. The spec's evidence note for p06 still says the store was "built in 2024 by Tom Hendriks" (not rendered; left).
- Fixed (see Ledger conflicts): the scene said a SEPA Direct Debit "sat in `pending`" for most of a week before Keel.

## Ledger conflicts

- `07-local-payment-methods` ledger line: before Keel "a direct debit was marked `paid` when the provider accepted it". This page's scene (and its spec, p07 evidence) had the same pre-Keel direct debit sitting in `pending` for most of a week. Chapter 7 owns the method rules, so this page was changed: the debit is now "marked `paid` when the provider accepted the debit, most of a week before the bank's answer", with a link to `[[local-payment-methods]]`. The paragraph's point (the five words have no place for a wait for the bank) is unchanged. The author may want the p07 evidence note in `spec.json` reworded to match; it does not contradict the new wording.

## For other pages

- `11-in-person-payments` / `17-api-design-and-object-models`: Adyen's Terminal API documents a transaction status request (docs.adyen.com/point-of-sale/basic-tapi-integration/verify-transaction-status). "Nothing to read back on Adyen" is true of the Checkout API (ruling 12) and should not be written about in-person payments.
- Any page that says Adyen's reasons for `/sessions` are unpublished: the 5 October 2021 knowledge-hub post by Julien Lengrand-Lambert gives one.
- Stripe's lifecycle and Payment Intents pages now open with a paragraph addressed to coding tools ("Don't use the Payment Intent API unless the user explicitly asks"). It is not documentation of behavior and should not be quoted as Stripe's guidance to integrators beyond the first sentence, which this page quotes.
