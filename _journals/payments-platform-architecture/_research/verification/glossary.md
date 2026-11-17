# Verification — glossary (`glossary`)

Verified 17 November 2026. The page is generated: every correction below was made in `_research/glossary-tools/crosswalk.py` or `rows.py` and the page re-assembled with `assemble.py`; `index.md` was not edited by hand.

## Method

1. **Chapters, all 115 crosswalk rows (script).** For every row, each code-typed term, each index term, each quotation and each number with a unit was searched in the current text of the chapters the row cites. Twelve rows had a term that is not verbatim in a cited chapter and one a quotation; each is resolved in the table below.
2. **Documentation corpus.** The 524 `docs.stripe.com` and `docs.adyen.com` URLs cited across the book's chapters were fetched in this session (Markdown variant where served; all returned 200), plus 26 further pages (API object references, the glossary's own seven sources, dispute and capability pages). One guessed URL returned 404 (`docs.adyen.com/platforms/online-payments/split-chargebacks`); the term it was meant to confirm was read on the split-transactions pages instead. Every provider term of every row was searched in its provider's corpus (presence), and for 70 rows the passage was read (meaning). A row counted as "read" has at least one cell confirmed in a passage; the other cell then rests on the same kind of reading or on the chapter, as stated.
3. **Definitions.** All 292 rows were compared by script with the owning chapter (term present, every number and quotation present in a linked chapter, word overlap). 97 rows were read against the chapter or page: the 16 failure patterns and the two rows on families, 16 preface-page terms, the 7 terms defined in two chapters, 54 rows that state a provider, network, legal or numeric fact (15 of them re-read in the chapter passage), and the 5 the script flagged.
4. **Larkfield.** All 52 rows against `scenario-ledger.md`, the two `[editor]` lines included; weekdays recomputed.

## Crosswalk rows read against documentation (70: 64 confirmed, 4 corrected, 2 hedged)

Status is for the row after any edit. "ch." means the other side, or the note, rests on the cited chapter.

| # | Row (concept) | Read on | Status | What changed |
| --- | --- | --- | --- | --- |
| 2 | Payment identifier | docs.adyen.com/adyen-glossary (16-character PSP reference per payment or modification) | confirmed | The 20-pair `metadata` limit was not found in the pages fetched; it rests on ch. 17 (not re-fetched) |
| 4 | States of a payment | docs.stripe.com/api/payment_intents/object; docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | — |
| 5 | What the customer must do next | docs.adyen.com/online-payments/build-your-integration/payment-result-codes (`IdentifyShopper`, `ChallengeShopper`, `RedirectShopper`) | confirmed | "action object" is not a phrase of ch. 8; the `action` field is |
| 7 | Authorize now, capture later | docs.adyen.com/online-payments/capture (`captureDelayHours`); …/adjust-authorisation (28 days); …/webhooks/webhook-types (`EXPIRE`) | confirmed | — |
| 8 | Withdrawing an authorization | docs.adyen.com/online-payments/cancel (24 hours by reference); …/reversal; docs.stripe.com/refunds ("appear in the form of a reversal") | confirmed | False friend confirmed on both sides |
| 9 | Saving a card without charging | docs.adyen.com/adyen-glossary (Zero-value auth) | confirmed | Stripe side: ch. 2 |
| 10 | Who started the payment | docs.adyen.com/online-payments/network-tokenization and tokenization pages (`recurringProcessingModel` values, `ContAuth`) | confirmed | — |
| 12 | Raw decline code and advice | docs.adyen.com/development-resources/raw-acquirer-responses; docs.stripe.com/declines (`network_decline_code`, `network_advice_code`, `advice_code`) | confirmed | — |
| 13 | The paying customer | docs.adyen.com/adyen-glossary ("A customer who buys goods or services from a merchant") | confirmed | — |
| 18 | Payment page by link | docs.stripe.com/payment-links; docs.adyen.com/unified-commerce/pay-by-link ("Do not use Pay by Link as the only way…") | confirmed | — |
| 20 | Shape of the API | docs.adyen.com/api-explorer/Checkout/latest/overview (v72) | confirmed | — |
| 23 | Idempotency | docs.adyen.com/development-resources/api-idempotency ("7 to 14 days"; "the response to the first attempt"); docs.stripe.com/api/idempotent_requests (24 hours, v1); docs.stripe.com/api-v2-overview (30 days) | confirmed | — |
| 24 | What the provider owes | docs.adyen.com/account/balances (available funds = Pending + Next payout …) | confirmed | False friend confirmed |
| 27 | "Settlement" | docs.adyen.com/account/payments-lifecycle; …/reporting/invoice-reconciliation/payment-accounting-report | corrected | "in reports" → "in the payment accounting report"; index term "Payment accounting report (Adyen)" moved here from row 39, where the cells do not mention it; "Settled (Adyen journal type)" → "record type" (Adyen's word on that report) |
| 28, 29 | Provider's hold; merchant's buffer | docs.adyen.com/account/balances, …/balances/deposit ("Unlike the reserve, you cannot determine your own deposit amount"; calculated daily) | confirmed | Stripe "minimum balance": changelog entry read; definition rests on ch. 13 |
| 30 | Transfer to the bank account | docs.stripe.com/api/payouts/object ("within 5 business days"); docs.adyen.com/platforms/payout-webhooks ("This status is not final"); …/payouts/payout-service/payout-lifecycle (`credited`, instant) | confirmed | — |
| 31 | Paying a non-merchant | docs.stripe.com/global-payouts/manage-payouts | corrected | Stripe's status list also has `failed` and `canceled`; added |
| 32 | How fast a payout travels | docs.stripe.com/global-payouts/send-money (`preferred_networks`); docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts (priorities) | confirmed | — |
| 34 | Payee name check | docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts (`POST /verifyCounterpartyName`) | confirmed | Stripe side: ch. 14 |
| 35 | When a seller's balance is paid out | docs.adyen.com/platforms/managed-payouts (Standard, Accelerated); …/platforms/custom-payouts/scheduled-payouts (trigger amount); docs.stripe.com/connect/charges (`delay_days`) | confirmed | — |
| 36 | Top-up | docs.stripe.com/connect/top-ups ("Add funds to your platform balance") | confirmed | Adyen side: ch. 35 |
| 39 | Report per seller | docs.adyen.com/platforms/reports-and-fees ("**Required** for full financial reconciliation") | confirmed | Index term moved (see 27) |
| 40 | Report-ready signal | docs.stripe.com/reports/balance; docs.adyen.com/development-resources/webhooks/webhook-types (`REPORT_AVAILABLE`, `balancePlatform.report.created`) | confirmed | — |
| 41 | Querying the data | docs.stripe.com/data/how-sigma-works | confirmed | "No counterpart" for Adyen rests on ch. 15's search; not repeated |
| 42 | Returned payout | docs.adyen.com/account/getting-paid (`BankInstructionReturned`) | confirmed | — |
| 43 | Provider's fee | docs.stripe.com/api/balance_transactions/object (`stripe_fee`); docs.adyen.com settlement details report (invoice deductions) | confirmed | — |
| 45 | Reusable provider token | docs.adyen.com/development-resources/webhooks/webhook-types (`recurring.token.created`) | confirmed | — |
| 46 | Network tokens for stored cards | docs.adyen.com/online-payments/network-tokenization | corrected | The page does not call the merchant a "token requestor". Cell now uses its words: Adyen manages the tokens, or you "manage network tokens yourself"; note adds that this cannot be combined with Adyen's tokenization feature |
| 47 | Was a network token used | docs.adyen.com/online-payments/network-tokenization (`retry.attempt.networkTokenOffered`); docs.stripe.com/api/charges (`network_token.used` in the object example) | confirmed | — |
| 48 | Keeping a card current | docs.stripe.com/api/v2/core/events/event-types (`payment_method.automatically_updated`); docs.adyen.com/online-payments/account-updater | confirmed | — |
| 55 | Risk score | docs.stripe.com/radar/transaction-risk-prevention (0–99; 65; 75); docs.adyen.com/risk-management/configure-your-risk-profile (Very Low to Very High) | confirmed | — |
| 56 | Stopped before the issuer | docs.stripe.com/declines (`not_sent_to_network`, `blocked`) | confirmed | Adyen wording is in ch. 24 as a quotation |
| 57 | Control traffic | docs.adyen.com/risk-management/control-traffic (EUR 2000 or higher) | confirmed | — |
| 58 | Fraud report before a dispute | docs.stripe.com/disputes/how-disputes-work; docs.adyen.com/development-resources/webhooks/webhook-types (`NOTIFICATION_OF_FRAUD`: TC40, SAFE) | confirmed | Both pages name the same two network reports |
| 59 | Request for information | docs.stripe.com/disputes/how-disputes-work; docs.adyen.com/risk-management/disputes-api | hedged | Now "Nearest counterpart, not a confirmed equivalence". Stripe: a pre-dispute request from the issuer, used most by American Express and Discover, "while Mastercard and Visa no longer use it". Adyen: "A shopper has opened an RFI… case with the bank"; "no money is withdrawn". Scope by network not compared |
| 60 | The dispute | docs.stripe.com/api/disputes/object; docs.adyen.com/risk-management/disputes-api/dispute-notifications | confirmed | — |
| 62 | Answering a dispute | docs.stripe.com/api/disputes/object (`evidence_details.due_by`); …/disputes/how-disputes-work ("usually 7-21 days"); docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow (defense period starts at the NoC) | confirmed | The 18- and 40-day figures were not in the pages read; they rest on ch. 4 and 45 |
| 63 | End of a dispute | docs.adyen.com dispute process ("This stage is not final"); webhook-types (`ISSUER_RESPONSE_TIMEFRAME_EXPIRED`) | confirmed | — |
| 64, 65 | 3-D Secure rules; exemptions | docs.adyen.com (default rule "Prefer Not"; `additionalData.scaExemptionRequested`); docs.stripe.com/api/payment_intents (`request_three_d_secure`) | confirmed | — |
| 68, 69 | Subscription; invoice | docs.stripe.com/api/subscriptions/object (eight statuses); …/api/invoices/object (five) | confirmed | Adyen "no counterpart": chapters' searches, not repeated |
| 70 | Scheduled retries | docs.stripe.com/billing/revenue-recovery/smart-retries (8 within 2 weeks, default for new accounts); docs.adyen.com/online-payments/auto-rescue/cards (support enables; 1 to 48 days) | confirmed | — |
| 76, 78 | Seller resources; balance platform | docs.adyen.com/platforms/account-structure-resources ("an accounting system that manages the flow of funds within your business") | confirmed | — |
| 77 | Platform's own money | docs.stripe.com/api/balance/balance_object (`connect_reserved`); docs.adyen.com/platforms/manage-liable-accounts | confirmed | — |
| 80, 81 | Division; platform's cut | docs.adyen.com/platforms/online-payments/split-transactions (`BalanceAccount`, `Commission`, `PaymentFee`; the closed-account warning) | confirmed | — |
| 83 | Who stands behind a negative balance | docs.stripe.com/connect/account-balances; docs.adyen.com/platforms/manage-liable-accounts (30 days) | corrected | `losses_collector` is the Accounts v2 name (`defaults.responsibilities.losses_collector`); in Accounts v1 the property is `controller.losses.payments`. Cell now gives both; source added; marked "documentation" |
| 84 | Managed Risk | docs.stripe.com/connect/risk-management/managed-risk; docs.adyen.com/platforms/managed-risk ("in pilot phase"; "assume the responsibility for negative balances"; 180 days) | confirmed | Same name, same function, different conditions: as the row says |
| 85 | Where a chargeback is booked | docs.adyen.com split-transactions pages (three `platformChargebackLogic` behaviors; default liable balance account) | confirmed | — |
| 86 | Refund after the seller was paid | docs.stripe.com/api/refunds/create; docs.adyen.com/platforms/online-payments/split-transactions/split-refunds | confirmed | — |
| 87 | Capability | docs.adyen.com/platforms/verification-overview/capabilities ("both allowed and enabled") | confirmed | — |
| 88, 89 | Requirements; announced changes | docs.stripe.com/api/accounts/object (`requirements`, `future_requirements`, the four lists) | confirmed | — |
| 97, 98 | Acknowledging; retry period | docs.adyen.com/development-resources/webhooks (10 seconds; retry queue, 30 days); docs.stripe.com/webhooks (three days) | confirmed | — |
| 99 | Proving who sent it | docs.stripe.com/webhooks; docs.adyen.com/…/verify-hmac-signatures (eight concatenated fields, no timestamp) | confirmed | — |
| 100, 101 | Thin event; other destinations | docs.stripe.com/api-v2-overview; changelog (Azure Event Grid) | confirmed | "No counterpart" for Adyen: ch. 20's search |
| 102 | Naming a version | docs.stripe.com/api-versions; docs.adyen.com/api-explorer/Checkout/latest/overview | confirmed | — |
| 105 | Request logs | docs.adyen.com/development-resources/logs-resources/api-logs (thirty days) | confirmed | — |
| 106 | Rate limit | docs.stripe.com/rate-limits (live mode: 100 requests per second) | confirmed | — |
| 107 | Release labels | docs.stripe.com/release-phases; docs.adyen.com/platforms/managed-risk ("Limited availability… pilot phase") | confirmed | — |
| 108, 112 | Driving the device; offline | docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture (local and cloud; offline only with local) | confirmed | — |
| 111 | Lost answer at the counter | docs.adyen.com/point-of-sale/basic-tapi-integration/verify-transaction-status | hedged | "Transaction status request" is not in a chapter, so the row is now marked "documentation" with this page as source. "The one place where Adyen documents a status lookup" was stronger than any chapter; now "a status lookup that Adyen documents for in-person payments", with ch. 8's finding about Checkout v72 |
| 114 | Refunding at the counter | docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment | confirmed | — |
| 115 | One view across channels | docs.stripe.com/terminal/overview (the quotation) | confirmed | — |

## Rows checked against chapters only (45)

Rows 1, 3, 6, 11, 14–17, 19, 21, 22, 25, 26, 33, 37, 38, 44, 49–54, 61, 66, 67, 71–75, 79, 82, 90–96, 103, 104, 109, 110, 113: every code term, quotation and number is in the cited chapter's current text, and every provider term is present in the fetched corpus of its provider, except these, whose sources are not documentation pages and were **not re-fetched** (each chapter has its own verification file): "Unified payouts" (Stripe announcement, ch. 10), "irrespective of whether the funds are actually received" and the Network Token Sharing Service (Adyen terms, ch. 13 and 23), "Adyen doesn't act as a direct, third-party merchant of record" (Adyen help center, ch. 32), KYC Refresh (ch. 26), the Stripe card export (ch. 22).

Terms not verbatim in the cited chapter, and what settled each: row 1 "fetch the object" (the glossary's own phrase, not a quotation; kept); row 18 Pay by Link (documentation, above); row 23 `idempotency-key` header (Adyen idempotency page); rows 58 and 59 event codes (documentation, above); row 56 "Pre-authorization" (quoted in ch. 24); row 68 `recurringProcessingModel` (ch. 2, 25; Adyen pages); row 72 `VAT` split (ch. 30, quoted from the split-transactions page); row 85 the three behaviors (ch. 33 and 45; documentation); row 92 Express accounts (ch. 33, "Standard, Express or Custom"); rows 46 and 111 corrected above.

**"No counterpart found" notes (rows 41, 68, 69, 71–73, 89, 92, 100, 101):** each repeats a dated search recorded in the owning chapter. I did not repeat the searches; `docs.adyen.com/llms.txt` (2,573 URLs) was fetched and has no page for an invoice object, a meter or a tax engine. The wording stays "found … November 2026", which the crosswalk introduction calls a search result and not proof.

**Removed:** none. **Left-out list** in `crosswalk.py`: unchanged.

## Definitions

| Row | Status | What changed |
| --- | --- | --- |
| Sixteen failure patterns, the families | confirmed | Wording equals the table on `where-payment-systems-go-wrong`; each second link is the chapter that page says owns the pattern |
| Preface terms (ledger, reconciliation, clearing, settlement, issuer, acquirer, authorization, interchange, dispute, chargeback, payment provider, token, recurring charge, payment facilitator, balance, payout) | confirmed | Each has a row or alias; definitions follow the owning chapter and are compatible with the preface's simpler wording |
| Authorization, reversal, liability shift (two rows: EMV and 3-D Secure), invoice, sweep, retry policy, acquirer | confirmed | Each follows the owning chapter's bolded definition; the second sense is named in the row or in the crosswalk |
| Pre-funding | hedged | The row said "Documented for Adyen's sales-day payout". Ch. 13 and ruling 47(m) add that Adyen's Annual Report 2025 calls paying after funds are received the "default setup" and that the two texts are not reconciled. Row now says so |
| The first of the month (Larkfield row) | corrected | Index label was identical to the failure pattern "The First of the Month"; renamed "The first of the month (Larkfield's renewal peak)" |
| All others (script; 54 fact-bearing rows read) | confirmed | No number or quotation absent from the linked chapters; no row stronger than its chapter found |

## Larkfield rows

52 rows; every name, figure and date is in the ledger. Editor lines: the Silent Webhook is Monday 14 September 2026 (row agrees); the reconciliation job runs once per provider on the report-ready signal (row agrees); the Unexplained €0.4 Million is a year-end 2025 difference found in January 2026 (row agrees). Weekdays recomputed: 9 March 2027 Tuesday, 11 March 2027 Thursday, 14 September 2026 Monday. **Ledger conflicts: none.**

## Index and links

57 distinct `[[permalinks]]`, all valid. 929 index entries, no dead anchor; one duplicate label, fixed (above).

## Could not verify, and what I did

- Adyen `metadata` limit of 20 pairs (row 2) and the 18- and 40-day defense periods (row 62): not in the pages fetched; kept on the chapters' authority (ch. 17; ch. 4 and 45).
- The Stripe side of rows 9, 34 and 56's Adyen side, and the rows listed under "chapters only", were not read on documentation in this pass.

## For other pages

- Ch. 33's "Where They Differ" table says "`losses_collector` on the account" without the Accounts v1 name (`controller.losses.payments`); Larkfield's studios are legacy v1 Custom accounts, so the v1 name is the one its engineers would see.
- Ch. 23 calls Adyen's second mode by the standard's role ("token requestor" appears nearby); Adyen's page says "Manage network tokens yourself".
