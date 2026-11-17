# Verification — 42-journey-card-payment (`journey-card-payment`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants (and HTML for the link check), the Visa rules as the PDF of 24 October 2026 (converted to text and searched), Regulation (EU) 2015/751 from the Publications Office (`Accept: application/xhtml+xml`), Adyen's legal page and Google's developer page as HTML, the Checkout API definition as the raw JSON file `CheckoutService-v72.json` from Adyen's repository (parsed, not read by eye). All double-quoted strings taken from sources were matched mechanically against the fetched texts after normalizing quotes and markup. This is a journey page: it has no "Where They Differ" section, and each provider fact was also compared with the verified owning chapter and rulings 18–37.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen idempotency keys "valid for a period of 7 to 14 days after first submission" | https://docs.adyen.com/development-resources/api-idempotency | confirmed | — |
| 2 | Stripe keeps idempotency keys at least 24 hours | https://docs.stripe.com/api/idempotent_requests | confirmed | Sentence had no attribution or date; now "Stripe's API reference (n.d., accessed November 2026) says keys can be removed once they are at least 24 hours old" |
| 3 | Apple Pay "uses network tokenization … Touch ID or Face ID authentication" | https://docs.adyen.com/payment-methods/apple-pay | confirmed | — |
| 4 | Google: "a device token on an Android-powered device authenticated with a 3-D Secure cryptogram" | https://developers.google.com/pay/api/web/guides/tutorial | confirmed | — |
| 5 | Adyen pre-authorization risk rules quote ("saves issuer and scheme fees") | https://docs.adyen.com/risk-management/configure-your-risk-profile | confirmed | — |
| 6 | Refusal reason 20, FRAUD, from pre-authorization risk checks | https://docs.adyen.com/development-resources/refusal-reasons | confirmed | — |
| 7 | Stripe: a charge blocked for risk has `network_status` `not_sent_to_network` | https://docs.stripe.com/radar/transaction-risk-prevention | confirmed | Link: the old URL `/radar/risk-evaluation` redirects; source entry replaced with the final URL and the page's current title, "Transaction risk prevention" |
| 8 | Apple Pay "is PSD2 SCA-compliant"; "supports liability shift for American Express, Discover, JCB, Mastercard, and Visa cards" | https://docs.adyen.com/payment-methods/apple-pay | confirmed | Date added in the sentence. (The page adds that for Visa on iOS 16.1 or below the shift applies to cards issued in Europe; Mila's card is Dutch, so the sentence holds.) |
| 9 | Google Pay guarantees liability shift for Visa cards issued in the EU or UK when tokenized as a device token (DPAN) | https://docs.adyen.com/payment-methods/google-pay | confirmed | — |
| 10 | "we recommend that you rely on the webhook to trigger any business logic" | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | Date added in the sentence |
| 11 | "The status of a payment can sometimes change after you get the result code" | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 12 | Visa: 10 calendar days for a cardholder-initiated card-absent transaction (Table 5-11) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | — |
| 13 | Adyen automatic capture "without a delay, immediately after authorization" | https://docs.adyen.com/online-payments/capture | confirmed | — |
| 14 | Automatic capture "does *not* trigger a separate CAPTURE webhook" | https://docs.adyen.com/online-payments/capture | confirmed | — |
| 15 | CAPTURE success means the request "is valid (…) and has been submitted" | https://docs.adyen.com/online-payments/capture | confirmed | The source continues "to the bank/third-party processor"; the quotation stops before it, which is accurate |
| 16 | "In rare cases, a capture fails even after … `success`: **true**"; "can even happen a few days after" | https://docs.adyen.com/online-payments/capture | confirmed | — |
| 17 | Visa definition of Presentment | Visa rules, glossary | confirmed | — |
| 18 | EU cap of 0.2% on consumer debit interchange (Article 3) | http://publications.europa.eu/resource/celex/32015R0751 | confirmed | Regulation named and evidence age (11 years, in force) flagged in the text |
| 19 | Acquirer of record: "Adyen publishes its licenses and no acquirer per country" | https://docs.adyen.com/account/supported-currencies | corrected | Ruling 27(b). Adyen lists countries and regions "For each Adyen acquiring connection" (the EU among them) and processes "through one of our acquiring entities"; it names no acquiring entity per country. Sentence rewritten; the license page it rested on was not in Sources; source added. Still labeled as the author's inference |
| 20 | "Adyen does not send a webhook message when a payment settles successfully"; the only trace is the batch reversal | https://docs.adyen.com/development-resources/webhooks/webhook-types | corrected | The quote is confirmed. The same paragraph of the source names an optional `SETTLED_REVERSED` event for Sales day payout; one sentence added |
| 21 | Platforms: funds not received within 30 days are subtracted from the batch | https://docs.adyen.com/platforms/settle-funds | confirmed | — |
| 22 | Visa definition of Settlement Amount; no settlement cut-off times or cycles in the rule text | Visa rules, glossary; full-text search for "cut-off", "cutoff" | confirmed | No match for cut-off times in the rule text |
| 23 | "the payable batch always closes two hours after your sales day closing time" | https://docs.adyen.com/account/sales-day-payout | confirmed | — |
| 24 | Balance Platform Accounting Report: "a daily report that tracks all balance changes …"; the platform "also reads" it | https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report ; https://docs.adyen.com/platforms/reports-and-fees | corrected | Ruling 32(c). Quote confirmed. Adyen marks this report "**Required** for full financial reconciliation" and the settlement details report "**Optional**"; "also reads" replaced by that statement; source added |
| 25 | The job starts on "Adyen's signal that a report is ready" | https://docs.adyen.com/reporting/automatically-get-reports ; https://docs.adyen.com/platforms/prepare-reports/generate-download-reports | corrected | Ruling 32(b). Both signals named: `REPORT_AVAILABLE` and `balancePlatform.report.created`; second source added |
| 26 | "Adyen settles a settlement batch after its sales day ends and the configured settlement delay has passed. The date when the schemes … does not affect this timing." | https://docs.adyen.com/platforms/settle-funds | confirmed | — |
| 27 | Booking date and value date | https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report | confirmed | — |
| 28 | "The API request validates only the format of the split instructions, **not** the balance accounts …" | https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | — |
| 29 | `booked`: "This status is not final. …" | https://docs.adyen.com/platforms/payout-webhooks | confirmed | — |
| 30 | "the route gives no confirmation of the credit" | https://docs.adyen.com/platforms/payout-webhooks | hedged | The page gives a `credited` tracking status for instant transfers and an `estimatedArrivalTime` "for transfers with any other priority". Sentence now says: for a transfer that is not instant, an estimated arrival time and no confirmation |
| 31 | Dispute time limit of 120 days | Visa rules (dispute conditions, "120 calendar days of either") | confirmed | — |
| 32 | Stripe: status `succeeded`; `payment_intent.succeeded` event | https://docs.stripe.com/payments/paymentintents/lifecycle ; https://docs.stripe.com/payments/payment-methods | confirmed | — |
| 33 | Balance transaction with `amount`, `fee`, `net`, `available_on` | https://docs.stripe.com/api/balance_transactions/object | confirmed | — |
| 34 | Destination charge with `on_behalf_of` and an application fee | https://docs.stripe.com/connect/destination-charges (variant `?platform=web&ui=elements`) | confirmed | The bare `.md` URL returns only an index of variants; the variant was read |
| 35 | Payout: "Some payouts that fail might initially show as `paid`, then change to `failed`" | https://docs.stripe.com/api/payouts/object | confirmed | — |
| 36 | Payout reconciliation report itemizes by payout (`automatic_payout_id`) | https://docs.stripe.com/reports/payout-reconciliation | confirmed | — |
| 37 | "Stripe uses “T” to refer to the transaction time …" | https://docs.stripe.com/payouts | confirmed | — |
| 38 | Funds "transition from `pending` to `available` at the corresponding available_on time for each balance transaction" | https://docs.stripe.com/payments/balances | confirmed | — |
| 39 | Dutch account: default settlement timing 3 business days | https://docs.stripe.com/payments/balances | confirmed | The page lists 7 calendar days for the first payout and 3 business days by default; "default" is the page's word |
| 40 | "A PaymentIntent can be retrieved by its ID at any time" | https://docs.stripe.com/api/payment_intents/retrieve | confirmed | No source entry supported it; source added, attribution added |
| 41 | Checkout API v72: three GET operations, none returns a payment; "no call that returns a payment" | https://github.com/Adyen/adyen-openapi (`json/CheckoutService-v72.json`) | corrected | Ruling 29. The count is confirmed (`/paymentLinks/{linkId}`, `/sessions/{sessionId}`, `/storedPaymentMethods`; v72 is the highest version in the repository). The unscoped wording in KEY POINT 3 and in the Stripe table ("nothing to read back") is now scoped to the Checkout API and online payments |
| 42 | Stripe on `succeeded`: "The funds are now in your account and you can confidently fulfill the order." | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | — |
| 43 | Stripe: success "according to the payment method’s processing flow, but funds can still be refunded, disputed, returned, or reversed" | https://docs.stripe.com/payments/payment-methods | confirmed | — |
| 44 | Stripe's pages "do not say whether funds become available before Stripe has received them" | https://docs.stripe.com/payouts/instant-payouts | corrected | Ruling 18. Stripe documents paying ahead for Instant Payouts ("Card payment funds are available immediately, including pending funds within your payout schedule window"). The silence is now scoped to the standard payout schedule and the Instant Payouts sentence quoted; source added |
| 45 | Adyen Sales Day Payout terms, last update 17 June 2024: "irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner" | https://www.adyen.com/legal/sales-day-payout-terms-of-service | confirmed | — |
| 46 | Stripe: an expired authorization makes the payment `canceled` | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | — |
| 47 | Loss table, row 1: "10 days under Visa's rule"; "Adyen: an `EXPIRE` webhook, or a late capture that fails" | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method ; https://docs.adyen.com/online-payments/adjust-authorisation | corrected | Brought into line with chapters 2 and 3. Stripe's page lists 7 days for a customer-initiated Visa payment (added). Adyen expires authorizations "automatically after 28 days" and says a capture after the scheme's expiry "is possible", with listed risks (failed capture, fees, chargeback); the cell now says that. Source added |
| 48 | **CaptureFailed** entries in the settlement details report | https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp | confirmed | — |
| 49 | Deposit (Adyen) and reserve (Stripe) as money held back against risk | https://docs.adyen.com/account/balances/deposit ; https://support.stripe.com/questions/reserves-frequently-asked-questions | confirmed | No source supported the Stripe half; Stripe's reserves FAQ fetched and added |
| 50 | Stripe: a network rejection of a capture after `succeeded` is "not public" | https://docs.stripe.com/llms.txt (searched for "capture"); lifecycle and hold pages | confirmed | Searched the documentation index and the two pages; nothing found. Agrees with the verified chapters 3 and 8 |
| 51 | Loss table: 'The capture was "valid and submitted"' | https://docs.adyen.com/online-payments/capture | corrected | The three words were in quotation marks and are a paraphrase; quotation marks removed |

Counts: 51 claims checked; 42 confirmed, 8 corrected, 1 hedged, 0 unsupported, 0 unreachable.

## Could not verify, and what was done

- Nothing was unreachable. The Publications Office URL returns RDF by default and the regulation text with `Accept: application/xhtml+xml`; the URL is kept as other chapters cite it.
- "Not public" for Stripe's capture failure path rests on a search of the documentation index and two pages, not on an exhaustive reading of Stripe's documentation.
- The Mastercard side is not relevant to this page (Mila's card is a Visa).

## Rulings applied

- 18 (row 44), 27 (row 19), 28 (the ledger is written by the reconciliation job from report lines on the report-ready signal: "nightly job" and "nightly reconciliation" replaced by "reconciliation job … when its reports are ready" in step 9, the step table and the closing section), 29 (row 41), 30 (all documentation cited n.d.; none was dated from front matter), 32 (rows 24, 25). Rulings 31 and 34 touch nothing on this page.
- Ledger payout wording: step 11 now says the money is at the studio's bank the same day in the best case; step 12 says `arrived` is a state of Larkfield's record set on 25 March, not the day the money landed.

## Larkfield consistency

Checked against the ledger: 19:42 Tuesday 9 March 2027; €120.00, €2.53, €117.47, €0.61, €1.92; Stripe counterfactual €0.87 and €1.66, available Friday 12 March; payout Thursday 11 March; arrived Thursday 25 March (ten business days); refund request 18 March; dispute window about 7 July 2027 (120 days); five business days to Priya Raman; legacy Custom connected accounts with destination charges. Weekdays checked. No contradiction found.

## Ledger conflicts

None.

## For the author: journal spec (not edited; the copied fields in `spec.json` were left as they are)

1. `journal-spec.json`, entry `journey-card-payment`, `intent.outcome.know[2]` (also `_research/journal-spec-parts/part-9.json`, and copied to `spec.json`): "…on Adyen a result code, then webhooks keyed by the PSP reference, then report lines, **with no endpoint that returns a payment by its identifier** and no webhook when a payment settles…". Unscoped; ruling 29 asks for "in the Checkout API" or "for online payments".
2. Same entry, AC-2 `expected`: "…an AUTHORISATION webhook keyed by the PSP reference, **with no endpoint that returns the payment by its identifier**…". Same fix.
3. Same entry, `intent.outcome.know[1]`: "the payout that contains it **arriving** on Thursday 11 March". The ledger now says sent on 11 March, landing that day in the best case.
4. Same entry, `thesis.so_what`: "a **nightly** reconciliation of both providers' reports against the ledger (K3)". Ruling 28 and the chapter 15 ledger line: one run per provider on its report-ready signal, not at a fixed hour.
5. Same entry, `intent.outcome.know[3]` and `thesis.how_why`: "whether Stripe makes funds available before it has received them" / "nothing on whether its own receipt of funds comes first". Ruling 18: Stripe documents paying ahead for Instant Payouts only.
(`thesis.how_why` already says "the Checkout API has no endpoint".)

## For other pages

- None found.
