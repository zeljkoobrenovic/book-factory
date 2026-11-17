# Verification — 03-clearing-and-settlement (`clearing-and-settlement`)

Verification pass of 17 November 2026. Every source below was fetched in this session (Stripe and Adyen documentation as `.md` variants, Adyen's terms page as HTML, both 10-Ks from SEC EDGAR with their filing index pages, the Visa rules PDF converted with `pdftotext`, the Federal Reserve page as HTML). All 80 double-quoted strings in the article were matched mechanically against the fetched texts (typographic quotes and whitespace normalized), then read in context. Short URLs: S = `https://docs.stripe.com`, A = `https://docs.adyen.com`, VR = `https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf`, V10K = `https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm`, M10K = `https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm`, FED = `https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm`, TOS = `https://www.adyen.com/legal/sales-day-payout-terms-of-service`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen "Pending: the gross amount of sales and refunds that have not yet been settled…" | A/account/balances | confirmed | — |
| 2 | Visa 10-K is for fiscal year ended 30 Sep 2026, filed 5 Nov 2026 | V10K + EDGAR filing index | confirmed | — |
| 3 | Visa 10-K quote "After the transaction is authorized, the issuer posts… to the seller." | V10K ("Four-Party Model") | confirmed | Added a one-clause gloss of merchant discount rate (term was undefined on the page) |
| 4 | Mastercard 10-K is for 2025, filed 11 Feb 2026 | M10K + EDGAR filing index | confirmed | — |
| 5 | Mastercard three services: three quoted fragments (routing, exchange of information, settlement banks) | M10K | confirmed | — |
| 6 | Step table "typical time" column | none (labeled industry practice) | not a documented claim | — |
| 7 | Adyen "By default, payments are captured automatically without a delay, immediately after authorization…" | A/online-payments/capture | confirmed | — |
| 8 | Stripe captures automatically unless `capture_method` is `manual` | S/payments/place-a-hold-on-a-payment-method | confirmed | — |
| 9 | Stripe `automatic_delayed` is in private preview | same | confirmed (heading still says "Private preview") | — |
| 10 | Adyen capture delay "immediate" or 1 to 7 days per merchant account; `captureDelayHours` per payment | A/online-payments/capture | confirmed | — |
| 11 | Stripe status `requires_capture`; capture call with `amount_to_capture` | S hold page | confirmed | — |
| 12 | Adyen "Manual capture lets you settle funds on fulfillment, when an order is shipped." | A capture | confirmed | — |
| 13 | Stripe "A partial capture automatically releases the remaining amount." | S hold page | confirmed | — |
| 14 | Adyen "Any unclaimed amount that is left over after partially capturing a payment is automatically cancelled." | A capture | confirmed | — |
| 15 | Stripe "up to 50 non-final captures for a single PaymentIntent"; on interchange-plus (IC+) pricing | S/payments/multicapture (variant `?platform=web&ui=elements`) | confirmed | Source title corrected to the page's title, "Capture a payment multiple times" |
| 16 | Adyen multiple partial captures; maximum "is determined by the issuer" | A capture; A/online-payments/adjust-authorisation | confirmed (the sentence is about a pre-authorization) | — |
| 17 | Visa Table 5-11: counted from "the date of a valid Authorization"; 10 days card-absent cardholder-initiated, 5 card-present and all merchant-initiated, 30 with extended authorization indicator | VR, section 5.7.3.5, p. 424–425 | confirmed; hedged for generality | Added that these are the general timeframes and that a second table (5-12) sets different ones for a few countries; glossed card-present and merchant-initiated |
| 18 | Rules edition is 24 October 2026 | VR title page | confirmed | — |
| 19 | Stripe: 7 days customer-initiated online Visa, 5 merchant-initiated; "The exact authorization window is 4 days and 18 hours…" | S hold page | confirmed | — |
| 20 | Stripe `capture_before` "indicates when the authorization expires"; "the funds are released and the payment status changes to `canceled`" | S hold page | confirmed | — |
| 21 | Adyen "expires (pre-)authorization requests automatically after 28 days" | A adjust-authorisation | hedged | Source limits this to "the global card schemes"; qualifier added |
| 22 | Adyen: "it is possible to capture remaining balance on a payment after an authorization has already expired on the card scheme's side" | same | confirmed | — |
| 23 | Adyen late-capture list: "increases the risk of", "failed capture", "Increased interchange fees", "Card scheme transaction fees", "chargeback for 'No Authorization' or 'Late Presentment' reasons" | same | confirmed | — |
| 24 | Visa Dispute Condition 11.3: "A valid Authorization was obtained but the Transaction was not processed within the timeframe" | VR, Table 11-47 (sentence spans a page break) | confirmed | — |
| 25 | Issuer has "75 calendar days from the Transaction Processing Date" under 11.3 | VR, Table 11-50 | confirmed | — |
| 26 | Adyen `CAPTURE` success = "is valid (…) and has been submitted to the bank/third-party processor"; "In rare cases the card scheme can still reject the capture, and you will receive a CAPTURE_FAILED webhook." | A capture | confirmed | — |
| 27 | Automatically captured payment "does *not* trigger a separate CAPTURE webhook" unless you enable it | A capture | hedged | The page ties enabling to delayed automatic capture ("consider enabling a CAPTURE webhook… enable the default event codes CAPTURE and CAPTURE_FAILED… turn on Delayed Capture"). "unless you enable it" replaced by what the page says |
| 28 | Stripe's page does not say whether a capture can be rejected later at the network | S hold page; S/payments/payment-intents/asynchronous-capture; S/api/payment_intents/capture; S/api/charges/capture; `S/llms.txt`; one web search limited to stripe.com | confirmed as far as I can tell ("Not public" check) | Added what Stripe does document: the Charges capture reference says "Capturing a charge will always succeed, unless the charge is already refunded, expired, captured, or an invalid capture amount is specified" (about the call, not the network). New source entry added |
| 29 | Fed definitions of dual-message and single-message network (two quotes); page updated 19 December 2025 | FED (footnotes 10 and 12; "Last Update: December 19, 2025") | confirmed | — |
| 30 | Visa Online Financial Transaction "authorized, cleared, and settled in a single online financial message"; required in the US for PIN-authenticated Visa debit | VR glossary; Table 5-11 footnote 3 | confirmed | — |
| 31 | Visa glossary: Clearing, Presentment, Interchange (three quotes) | VR glossary | confirmed | — |
| 32 | Visa IRF "A fee between Acquirers and Issuers in the Clearing and Settlement of an Interchange Transaction" | VR glossary | confirmed | — |
| 33 | Mastercard "We administer the collection and remittance of interchange fees through the settlement process." | M10K | confirmed | — |
| 34 | Visa lists a "US Interchange Reimbursement Fee Rate Qualification Guide" and does not reproduce it | VR (list of referenced documents) | confirmed | — |
| 35 | Rate depends on record data and promptness | none; page labels it industry practice | not a documented claim | — |
| 36 | Visa Settlement and Settlement Amount definitions (two quotes) | VR glossary | confirmed | — |
| 37 | Netting example (€10,000,000 / €300,000 / €40,000 → €9,660,000) | labeled assumption; arithmetic checked | confirmed (arithmetic) | — |
| 38 | Visa "We indemnify issuers and acquirers for settlement losses…" | V10K (risk factors) | confirmed | — |
| 39 | Mastercard "We guarantee the settlement of many of the transactions from issuers to acquirers"; "We do not, however, guarantee payments to merchants by their acquirers" | M10K | confirmed | — |
| 40 | Visa Currency Conversion Rate (two quotes) | VR glossary | confirmed | — |
| 41 | Stripe "automatically converts all incoming funds into your default currency"; fee charged "when funds settle into a non-primary settlement currency, not when you initiate a payout" | S/payouts/multi-currency-settlement | corrected (URL only; both quotes confirmed) | URL had changed (old `/payouts/multicurrency-settlement` redirects); replaced with the final URL |
| 42 | Adyen "offers like-for-like (no currency conversion) settlement if the currency is also supported…" | A/account/getting-paid | confirmed | — |
| 43 | Visa defines Settlement Date ("The date on which Visa initiates the transfer of Settlement Amounts"), Settlement Bank, Settlement Currency; one section covers a national net settlement service | VR glossary; section 7.7.1 | confirmed (the quote is the first clause of the definition) | — |
| 44 | Network cut-off times and number of settlement cycles are not in the rule text | VR full-text search for "cut-off", "cutoff", "settlement cycle", "cycles per" | confirmed (no hits) | — |
| 45 | Mastercard rule documents returned an access error | `mastercard.us/.../mastercard-rules.pdf`, `mastercard.com/.../transaction-processing-rules.pdf` | confirmed unreachable (HTTP 403 today) | — |
| 46 | Stripe pending/available, settlement time, `available_on` (three quotes) | S/payments/balances | confirmed | — |
| 47 | Stripe Netherlands: 7 calendar days initial, 3 business days default | S/payments/balances (country table) | confirmed | — |
| 48 | Stripe "Some payment processors might start “T”… Stripe uses “T” to refer to the transaction time… confirmation or capture" | S/payouts | confirmed (two adjacent paragraphs on the page) | Source title corrected to "Receive payouts from Stripe" |
| 49 | Stripe "Choosing a payout schedule doesn’t change how long… It only controls when payouts are sent." | S/payouts | confirmed | — |
| 50 | Adyen three steps (Capture, Adyen processing, Bank processing) | A/account/getting-paid | confirmed | — |
| 51 | Adyen Sales day payout is "the default payout model"; "You get all the funds from a particular sales day in a single payout batch, with a fixed payout delay" | A/account/sales-day-payout | confirmed | — |
| 52 | Adyen payout delay 2 business days for accounts "mostly" in euro-like currencies | same | corrected | Source: 2 business days when "At least 80% of the transactions are in AUD, CAD, EUR, GBP, NZD, RON, SEK or USD" and acquired in the currency's country or region, "for a typical mix of payment methods". Sentence now says so |
| 53 | Adyen platforms: sales day settlement; "The date when the schemes or payment methods transfer the funds to Adyen does not affect this timing." | A/platforms/settle-funds | confirmed | — |
| 54 | Adyen terms: "initiate payout of the Net Captured Volume to Merchant on the Payout Day, irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner"; last update 17 June 2024 | TOS, clause 1.1 | confirmed | — |
| 55 | Adyen "Prefinancing is capped at 30 days. If the card scheme, payment method, or acquirer does not settle the funds within 30 days, Adyen reverses the prefinanced amount from your payable batch." | A/account/sales-day-payout/upgrade-to-sdp | confirmed | — |
| 56 | Stripe documents nothing equivalent for standard payouts | S/payments/balances, S/payouts, S/payouts/instant-payouts, S/payouts/instant-payouts-with-advance-funding, `S/llms.txt`, one web search limited to stripe.com | confirmed as far as I can tell ("Not public" check) | — |
| 57 | Stripe "Funds acquired from card payments are available for Instant Payouts as soon as the charge is complete." | S/payouts/instant-payouts | confirmed | Source title corrected to "Instant Payouts for Stripe Dashboard users" |
| 58 | "Settled" table, network row: Stripe "Not exposed"; T+N counts from the network's processing date | none | unsupported, relabeled | "Not exposed" → "Not public" (I found no merchant-facing network-settlement event in the pages above); "the network's processing date" marked *(industry practice)* |
| 59 | "Settled" table, provider row, Adyen: "The payable batch closes after the payout delay" | A/account/sales-day-payout | corrected | Source: sales "are assigned to a payable batch after the payout delay. The payable batch closes according to your payout frequency". Cell reworded |
| 60 | Adyen Pass-through payout: two quotes; "the only available payout model in Africa, Brazil, and India" | A/account/pass-through-payout; A/account/getting-paid | confirmed | — |
| 61 | Adyen "The payout delay is calculated to be the break-even point…"; American Express example | A/account/sales-day-payout | confirmed | — |
| 62 | Adyen terms: more than 25% of captured volume in methods that "structurally settle to Adyen later than the Payout Day" | TOS, clause 2.4 | confirmed | — |
| 63 | Stripe "Card payment funds are available immediately, including pending funds within your payout schedule window"; "Stripe assesses a fee on each Instant Payout." | S/payouts/instant-payouts | confirmed | — |
| 64 | Where They Differ, row 1 (capture result) | claims 26–28 | confirmed | — |
| 65 | Where They Differ, row 2 (authorization cut-off) | claims 20–22 | confirmed | — |
| 66 | Where They Differ, row 3 (what "settlement" and "T" mean) | claims 46, 48, 50 | confirmed | — |
| 67 | Where They Differ, row 4 (unit of funding; NL 3 business days; typical delay 2 business days) | claims 46, 47, 51, 52 | confirmed | — |
| 68 | Where They Differ, row 5 (paying ahead; Stripe "Not public for standard payouts") | claims 54–57; ruling 18 | confirmed | — |
| 69 | Adyen reversal events `SETTLED_REVERSED` and `REFUND_NOT_CLEARED` "are separate subscriptions" | A/account/sales-day-payout | corrected | Source: "These event types apply to all payment methods and are disabled by default. Enable them on the Standard webhook page." Now "disabled by default" |
| 70 | Larkfield timeline "matching Adyen's documented defaults"; payout in the bank on Thursday | A/account/sales-day-payout (default sales day, 2-day delay); A/platforms/settle-funds; A/account/getting-paid | hedged | For platforms Adyen says "The default delay is defined in your contract". Getting paid says "it can take one to two business days for the payout to be initiated" and "your bank may need up to three more business days to post the funds". Both now stated; the same-day arrival is called the best case. Dates unchanged (ledger) |
| 71 | Stripe "pays out funds daily from transactions that were captured 3 business days earlier"; Tuesday 9 March + 3 business days = Friday 12 March | S/payouts | confirmed | — |
| 72 | Adyen "If Adyen cannot capture the funds for a sales transaction that we already paid out, we subtract those funds from the current payable batch" | A/account/sales-day-payout | confirmed | — |
| 73 | Adyen reversals "appear in the Settlement Details Report as **CaptureFailed** and **RefundFailed** entries" | A upgrade-to-sdp | confirmed | — |
| 74 | Adyen "Refunds, chargebacks, and other adjustments are added to the payable batch as they occur and are not related to the sales day…" | A/account/sales-day-payout | confirmed | — |
| 75 | Adyen bank holidays: "clearing for a specific currency may be closed… Adyen also cannot receive funds" | A/account/getting-paid | confirmed | — |
| 76 | Stripe "When a payout fails, the status might initially show as `paid`, but then change to `failed` within 5 business days." | S/payouts | confirmed | — |
| 77 | Take-away: Visa gives the acquirer 5 to 30 days; 75 days under 11.3 | claims 17, 25 | hedged | "in general" added (Table 5-12 has country exceptions from 1 day) |
| 78 | Take-away (Established): the fee to the issuer "is fixed from the clearing record and collected through settlement" | VR glossary; M10K | hedged | The sources place the fee "in the Clearing and Settlement" and "through the settlement process"; neither says it is fixed from the clearing record. Bullet now says what the two sources say |
| 79 | Take-away: Mastercard does not "guarantee payments to merchants by their acquirers" | M10K | confirmed | — |
| 80 | Take-away: Adyen standard payout pre-financed, reversible after 30 days; Stripe not public | claims 54–56 | confirmed | — |

Counts: 80 claims; 67 confirmed, 4 corrected (41 for its URL, 52, 59, 69), 6 hedged (17, 21, 27, 70, 77, 78), 1 unsupported and relabeled (58), 0 unreachable among cited sources; 2 rows (6, 35) are labeled industry practice with no source to check. Rows 28 and 56, counted as confirmed, are "Not public" checks: absence was searched for, not proven.

## Links

All 19 external URLs in Sources and Evidence return HTTP 200. One had moved: `docs.stripe.com/payouts/multicurrency-settlement` → `docs.stripe.com/payouts/multi-currency-settlement` (replaced). Four source titles did not match the pages and were corrected: "Capture a payment multiple times" (was "Multicapture"), "Receive payouts from Stripe", "Instant Payouts for Stripe Dashboard users", "Authorization adjustment" (was "Adjust authorisation"). One source added: Stripe API reference, "Capture a charge". Every `[[permalink]]` is in the style guide's list. No external URL appears in the running text (ruling 22).

## Could not verify, and what I did

- **Mastercard rules**: HTTP 403 on both public PDFs today, as ruling 17 says. The page quotes only Mastercard's 10-K and says the rules could not be read. No change.
- **Whether a Stripe capture can be rejected by the network after success, and whether Stripe's standard availability waits for network funds**: I found no Stripe page that says either way (pages listed in rows 28 and 56). The page's "does not say" and "Not public" wording stands; absence was checked in the documentation index and by one site-limited search, not proven.
- **Evidence age**: no cited source is older than three years (the oldest dated one is Adyen's terms, 17 June 2024). Adyen's `.md` front matter carries `last_modified` values from 2020–2023 for some pages; these are metadata, the pages display no date, and they stay "n.d., accessed 2026-11" (ruling 25).
- **The key point "the fee the cardholder's bank receives is fixed from the clearing record"** (KEY POINTS, and "One of the values fixed at clearing" in the clearing section) rests on Visa's definition of clearing as "validation and valuation" of records plus industry practice. I hedged the Established bullet only; the other two sentences are left as the author's reading. The author may want the same hedge there.

## Ledger conflicts

- Not a contradiction, but two lines that a reader could set against each other: the canonical example and the `03` addition say the payout "arrives on Thursday 11 March"; the `14-payouts-and-money-movement` addition says that payout is "marked sent on Thursday 11 March 2027 and arrived on Thursday 25 March" (the record's `arrived` state, set when the 10-business-day return window closes). This page follows the canonical example (money in the bank on Thursday 11 March) and now says that same-day arrival is the best case under Adyen's documented timing.
- Weekdays checked: 9, 10, 11 and 12 March 2027 are Tuesday to Friday. Fee €2.53 and net €117.47 agree with the ledger.

## For other pages

- Any page that writes "Studio Noord's payout delay matches Adyen's default" should note that for Adyen for Platforms the settle-funds page says the default settlement delay is set in the contract; the two-day figure is Adyen's example there and its typical merchant-account delay for euro sales.
- Pages that cite `docs.stripe.com/payouts/multicurrency-settlement` should use `/payouts/multi-currency-settlement`.

## For the author

- The article is now 5,997 words (was 5,771; target 5,000, maximum 6,500); `timetoread` moved from 25 to 26. The growth is the added qualifiers. The flow rubric's earlier note to shorten "Where They Differ" still applies.
- The Larkfield timeline puts the money in the studio's bank on the payout day. Adyen documents up to five more business days. The ledger fixes Thursday 11 March, so I kept it and labeled it the best case; changing the date is a ledger decision.
