# Verification — 15-payment-reconciliation-and-reporting

Verification pass of 17 November 2026. Every source was fetched in this session with `curl` (the `.md` variant for `docs.stripe.com` and `docs.adyen.com`, the HTML page for the two engineering posts) and the passage read. Quotations were compared with the fetched text by script, typographic quotes and markdown markup aside.

Status counts: **78 claims checked: 61 confirmed, 11 corrected, 6 hedged, 0 unsupported, 0 unreachable.** 2 further statements are listed as not checked.

Short URL keys: S-LEDGER = https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement · A-D2D = https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2 · S-PR = https://docs.stripe.com/reports/payout-reconciliation · S-BAL = https://docs.stripe.com/reports/balance · S-OPT = https://docs.stripe.com/reports/options · S-V1 = https://docs.stripe.com/reports/v1-api · S-V2 = https://docs.stripe.com/data/api/reports · S-PAYREC = https://docs.stripe.com/payouts/reconciliation · S-SIGMA = https://docs.stripe.com/data/how-sigma-works · S-FRESH = https://docs.stripe.com/data/data-freshness · S-DP = https://docs.stripe.com/data/access-data-in-warehouse · S-DPF = https://docs.stripe.com/data/data-pipeline/data-freshness · S-BANK = https://docs.stripe.com/bank-reconciliation · S-TRE = https://docs.stripe.com/treasury · S-PAYOUTS = https://docs.stripe.com/payouts · A-SDR = https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report · A-AGG = https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report · A-PAR = https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report · A-GP = https://docs.adyen.com/account/getting-paid · A-SDP = https://docs.adyen.com/account/sales-day-payout · A-UPG = https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp · A-AUTO = https://docs.adyen.com/reporting/automatically-get-reports · A-MAN = https://docs.adyen.com/reporting/manually-get-reports · A-PRF = https://docs.adyen.com/platforms/reports-and-fees · A-BPAR = https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report · A-GDR = https://docs.adyen.com/platforms/prepare-reports/generate-download-reports · A-PAYREP = https://docs.adyen.com/platforms/reports-and-fees/payout-report · A-TRK = https://docs.adyen.com/platforms/transfer-transactions/track-api · A-INV = https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice · A-ACC = https://docs.adyen.com/account/account-structure

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe Ledger post is from February 2024 (2024-02-16, Ilya Ganelin) | S-LEDGER | confirmed | — |
| 2 | Quote: adding funds “requires moving funds between banks, reconciling money movement with third-party reporting, and matching regulatory reporting with financial reporting” | S-LEDGER | confirmed | — |
| 3 | Quote: “We witness basic and obvious failures like malformed reports or propagated errors from banking or network partners” | S-LEDGER | confirmed | — |
| 4 | “A movement that no outside report confirmed shows up as a clearing account that does not empty” | S-LEDGER | hedged | The post says “a single missing, late, or incorrect transaction immediately creates a detectable accuracy issue with a simple query”. Sentence now uses the post's words; the “outside report” reading was the page's, not the post's. |
| 5 | Quote: “Find the clearing Accounts with nonzero balance.” | S-LEDGER | confirmed | — |
| 6 | Quote: “the 50% score for Aging Balances means that some clearing issues have persisted over time” | S-LEDGER | confirmed | — |
| 7 | Team view comes with “auto-generated tickets” | S-LEDGER | confirmed | — |
| 8 | Quotes: “the root cause is related to an infrastructure or third-party incident outside their control”; “reassign ownership to the right internal stakeholders” | S-LEDGER | confirmed | — |
| 9 | Quote: “99.99% of our dollar volume is fully ingested and verified within four days” | S-LEDGER | confirmed | — |
| 10 | Quote: “the remaining long-tail is reliably handled through manual analysis” | S-LEDGER | confirmed | — |
| 11 | Treasury quote: “Stripe records how much of the total balance belongs to your business and reconciles that record against the funds held at the bank.” | S-TRE | confirmed | — |
| 12 | The sentence applies to “a financial account backed by an FBO account” | S-TRE | hedged | The page says “In the US, a financial account is backed by either a demand deposit account (DDA) … or a for-benefit-of (FBO) arrangement” and “Account structures outside the US can differ”. Now “a US financial account backed by an FBO arrangement”. |
| 13 | Adyen post is from 2021 (displayed “August 23rd, 2021”, Willem Pino) | A-D2D | confirmed | — |
| 14 | Quote: “if we received reports on processed transactions from our partners, we needed to match them to transactions in different clusters.” | A-D2D | confirmed | — |
| 15 | Quote: “a two-step framework that would first parse a file and then split it into the relevant parts for each cluster. The second step was to match the relevant transactions within the clusters.” | A-D2D | confirmed | — |
| 16 | Quote: “the reconciliation needs to happen for a lot of different very custom integrations so this was a real team effort.” | A-D2D | confirmed | — |
| 17 | Evidence age 5 years, flagged in text and in the source entry | A-D2D | confirmed | — |
| 18 | Quotes “SentForSettle: Request to transfer the payment sent to the financial institution” and “Settled: Payment has been settled, and the funds have been received by Adyen.” | A-PAR | corrected | The source is a table (record type in one cell, description in the next); the “Name: description” form inside the quotation marks is not on the page. The names are now outside the quotation marks; the descriptions are verbatim. |
| 19 | Adyen can pay merchants before it is paid itself | A-UPG | confirmed | “Adyen prefinances your payments.” |
| 20 | Quote: “Prefinancing is capped at 30 days” | A-UPG | confirmed | — |
| 21 | SettledReversed quote: “Payment has not been settled because Adyen has not received the funds 30 days after capture.” | A-PAR | confirmed | — |
| 22 | Neither company publishes matching rules, partner file formats, match rates or exception volumes | S-LEDGER, A-D2D, `docs.stripe.com/llms.txt`, `docs.adyen.com/llms.txt` | confirmed | Searched both documentation indexes for “reconcil”, “match rate”, “clearing file”: only customer-side reporting pages. True as far as I can tell. |
| 23 | Itemized download lists “every payment, refund, dispute, fee, and other balance transaction included in the payout” | S-PR | confirmed | — |
| 24 | Each row carries the payout's ID and the balance transaction's ID | S-PR | confirmed | Columns `automatic_payout_id`, `balance_transaction_id`. |
| 25 | The report is “only available for users with automatic payouts enabled” | S-PR | corrected | The sentence continues: “, or a platform on manual payouts whose Connected Accounts have automatic payouts enabled”. The truncated quote dropped an exception that applies to platforms such as Larkfield. Full clause now quoted; the “Where They Differ” cell changed to match. |
| 26 | Quote: “Stripe can’t identify which transactions are included in each payout. You’re responsible for reconciling” | S-PR (instant payouts), S-PAYREC (manual payouts) | confirmed | — |
| 27 | Balance summary report “works like a bank statement” and “doesn’t associate payouts with payment transactions” | S-BAL | confirmed | Date added to the sentence. |
| 28 | Processing time “Within 12 hours” for Balance and Payout reconciliation | S-OPT | confirmed | — |
| 29 | Quote: “A day’s report is normally available by 12:00 pm on the following day.” | S-OPT | confirmed | — |
| 30 | Quote: “Report data follows a separate processing schedule, so a payout might arrive before its reconciliation data is ready.” | S-PR | confirmed | — |
| 31 | `reporting.report_type.updated` “twice per day (at 00:00 and 12:00 UTC)”, explicit subscription, not sent to Connect webhook endpoints | S-V1 | confirmed | “Connect webhook endpoints” glossed. |
| 32 | The guide is Stripe's “Reports API guide” (current status) | S-V1, S-V2 | corrected | The page is now titled “Run a report from the Reports v1 API” and opens with “For new integrations, use the Reports v2 API”. The v2 guide documents `v2.data.report_run.succeeded` / `.failed` events and its examples send `Stripe-Version: 2026-10-28.preview`. Sentence now names the v1 API and states the pointer to v2; v2 source added. |
| 33 | Sigma is “an interactive SQL environment in the Stripe Dashboard” | S-SIGMA | confirmed | URL redirected from `/stripe-data/how-sigma-works`; replaced. |
| 34 | Sigma makes “most of your Stripe transaction data available to query within three hours” (attributed to the Sigma page) | S-FRESH | corrected | The sentence is on the data-freshness page, not on “How Sigma works”. Attribution fixed; the combined source entry split in two; URL redirected from `/stripe-data/available-data`. |
| 35 | Stripe “calls the `balance_transactions` table ‘the canonical record of changes to your Stripe balance’” | S-FRESH | hedged | The words are a SQL comment in an example query (“-- this table is the canonical record of changes to your Stripe balance”). Now “a comment in an example query on that page calls …”. |
| 36 | Data Pipeline sends data to a warehouse such as Snowflake or BigQuery, “delivering a full load of data every 3 hours” | S-DP, S-DPF | confirmed | URL redirected from `/stripe-data/access-data-in-warehouse`; replaced. |
| 37 | Bank reconciliation “is currently only available for users with direct US-based Stripe accounts using an automated payout schedule” | S-BANK | confirmed | — |
| 38 | Merchant account: the sub-account in which payments are processed and paid out | A-ACC | confirmed | “Your payments are processed in sub-accounts called merchant accounts. The merchant account is where you receive the payout of funds”. Page fetched; not added to Sources (definition only). |
| 39 | Sales day payout is Adyen's default model | A-SDP, A-GP | confirmed | “Sales day payout is the default payout model”; pass-through is the only model in Africa, Brazil and India. |
| 40 | Quote: “You get all the funds from a particular sales day in a single payout batch” | A-SDP | confirmed | — |
| 41 | Settlement details report generated by default “per merchant account, per batch” | A-SDR | confirmed | Full sentence: “The default setting is to generate the report per merchant account, per batch.” |
| 42 | One line per entry: Settled, Refunded, Chargeback, fees, DepositCorrection, InvoiceDeduction, MerchantPayout | A-SDR | confirmed | — |
| 43 | Quote: “the unique payout reference (TX...XT), which can also be found on the bank statement” | A-SDR | confirmed | — |
| 44 | Quote: “Refunds, chargebacks, and other adjustments are added to the payable batch as they occur and are not related to the sales day of the original transaction.” | A-SDP | confirmed | — |
| 45 | Quote: “When the payable batch closes, we create a Settlement details report” | A-GP | confirmed | — |
| 46 | Quote: “the payable batch always closes two hours after your sales day closing time” | A-SDP | confirmed | — |
| 47 | Quote: “When a new report has been generated, you will receive a REPORT_AVAILABLE webhook”, with the download URL | A-AUTO | confirmed | Field `reason` is “the URL used to download the report”. |
| 48 | “I found no published figure for how long generation takes for any Adyen report.” | A-AUTO, A-MAN, A-GDR | corrected | Adyen does publish figures: scheduled daily reports are generated “each day between 02:00 and 10:00 CET and contains the previous 24 hours of data” (A-AUTO); a manually generated report “may take several hours to generate, depending on its size” (A-MAN); a manually generated balance platform report “can take up to a few minutes” (A-GDR). What is not published is the time between a payable batch closing and its settlement details report. The paragraph, the second KEY POINT, the timing row of the comparison table and the first “When It Goes Wrong” paragraph now say that. |
| 49 | Platform page marks the Balance Platform Accounting Report, payment accounting report and monthly invoice as required, the settlement details report as optional | A-PRF | confirmed | Exact wording now quoted: “Required for full financial reconciliation” / “Optional for full financial reconciliation”. |
| 50 | The balance platform holds a balance account per user; its accounting report is daily | A-BPAR, A-PRF | confirmed | “a daily report that tracks all balance changes on all balance accounts in your balance platform, including liable accounts and the accounts of your users”. |
| 51 | Report table: payout reconciliation, one balance transaction grouped by payout | S-PR | confirmed | — |
| 52 | Report table: balance summary, no link to payouts | S-BAL | confirmed | — |
| 53 | Report table: settlement details, one entry in a payable batch | A-SDR | confirmed | — |
| 54 | Report table: aggregate settlement details, totals per batch, payment method and journal type; BankInstructionReturned for a returned payout | A-AGG, A-GP | confirmed | Also split by merchant account, store, terminal and creation date. |
| 55 | Report table: payment accounting, one lifecycle status of one payment; used for the invoice | A-PAR | confirmed | — |
| 56 | Report table: Balance Platform Accounting Report, per day in Central European Time | A-BPAR | confirmed | “for your selected day in Central European Time (CET)”. |
| 57 | Quote: “SLAs indicate when the reports are available for download. Webhook notifications might take additional time.” | S-OPT | confirmed | — |
| 58 | `SETTLED_REVERSED` and `REFUND_NOT_CLEARED` “apply to all payment methods and are disabled by default” | A-SDP | confirmed | — |
| 59 | Quote: “Confirm the balance changes that you are informed of through webhooks” | A-PRF | confirmed | — |
| 60 | Adyen's report-ready signal is the `REPORT_AVAILABLE` webhook (stated for the whole Adyen side, including the platform's daily report) | A-AUTO, A-GDR | corrected | `REPORT_AVAILABLE` covers reports generated in the Customer Area for the Adyen account. Balance platform reports, including the Balance Platform Accounting Report the Larkfield close relies on, are announced by a different webhook: “When a report is generated, Adyen sends a balancePlatform.report.created webhook”, which “contains the URL at which you can download the report”. Added in four places (platform paragraph, the rule, comparison table, the paragraph after it) and in Sources. |
| 61 | Warehouse close can run every few hours on Stripe, given 3-hour loads | S-DP, S-DPF | confirmed | S-DPF adds that delivery time varies by data size (already in the source entry). |
| 62 | “For Adyen I found only file-based reports documented” | A-TRK | corrected | For platforms Adyen documents an API: “You can use the Transfers API to query the /transactions endpoint and get transaction details on demand … for your whole balance platform, a particular account holder, or balance account.” Sentence and the last comparison row now say so. I found no SQL or warehouse product in `docs.adyen.com/llms.txt`. |
| 63 | Comparison row 1 (own reconciliation, as published) | S-LEDGER, A-D2D, A-UPG | confirmed | — |
| 64 | Comparison row 2 (unit of the report) | S-PR, A-SDR | corrected | Same correction as #25: “automatic payouts only” became “accounts with automatic payouts, or platforms whose connected accounts have them”. |
| 65 | Comparison row 3 (timing) | S-OPT, A-GP, A-AUTO | corrected | Same correction as #48; last column no longer says “Only Stripe gives a number to schedule against”. |
| 66 | Comparison row 4 (signal) | S-V1, A-AUTO, A-GDR | corrected | Same corrections as #32 and #60. |
| 67 | Comparison row 5 (access to data) | S-SIGMA, S-FRESH, S-DP, A-SDR, A-TRK | corrected | Same correction as #62. |
| 68 | Manual and instant payouts on Stripe come with no itemization | S-PR, S-PAYREC | confirmed | — |
| 69 | Sales day closing at midnight gives a batch close at 02:00 | A-SDP | confirmed | “if you set the sales day closing time to midnight local time, Adyen will close the payable batch at 2:00 AM local time”. |
| 70 | A split payment appears as separate lines that share the PSP reference | A-PRF | confirmed | “two (or more) separate lines with Category platformPayment … matching Psp Payment Psp Reference”. |
| 71 | “Adyen by default debits its fees from the platform's balance account” | A-PRF | hedged | Source: “by default debits them from your balance platform's liable balance account”. Now “the platform's liable balance account, which is Larkfield's own”. |
| 72 | A platform “can run the financial reports” for connected accounts it controls | S-OPT | hedged | The page speaks of viewing reports (“When viewing a report as the platform account, you can view data … for a single connected account”) and excludes accounts that “can access the full Stripe Dashboard and aren’t controlled by the platform”. “run” became “view”. |
| 73 | Quote: “If Adyen receives the funds after 30 days, you see an additional Settled booking” | A-UPG | confirmed | — |
| 74 | A Stripe payout shown as paid can change to failed within five business days | S-PAYOUTS | hedged | True, but the page cited no source of its own for it. Source read: “When a payout fails, the status might initially show as `paid`, but then change to `failed` within 5 business days.” Now attributed and quoted; source entry added. |
| 75 | Stripe's reports run in the account's time zone or in UTC | S-OPT | confirmed | Date added to the sentence. |
| 76 | Adyen's settlement details report uses the account's time-zone setting | A-SDR | confirmed | — |
| 77 | Quote: “Your invoice is always based on the CET time zone.” | A-INV | confirmed | — |
| 78 | Take-away bullets restate #2, #14–15, #23, #41, #30, #59 | as above | confirmed | — |

Tally: confirmed 61 (#1–3, 5–11, 13–17, 19–24, 26–31, 33, 36–47, 49–59, 61, 63, 68–70, 73, 75–78); corrected 11 (#18, 25, 32, 34, 48, 60, 62 and the four comparison-table rows #64–67, which repeat those corrections in the table); hedged 6 (#4, 12, 35, 71, 72, 74).

## Added from the sources (not on the page before)

- Adyen's own advice on the Balance Platform Accounting Report page runs against the chapter's rule: “For real-time reconciliation, we recommend that you use API responses and webhooks to track individual payment transactions, and update your ledgers accordingly. … You can then reconcile funds from all payments on a daily basis using only the Balance Platform Accounting Report.” The rule paragraph now says the rule is stricter than this advice and quotes it. The argument is unchanged.
- Adyen documents a **Balance Platform Payout Report** for platforms (A-PAYREP): “all payouts processed during the specified generation period”, “all transactions that are part of those payouts”. Adyen's platform payout-reconciliation page calls it “the primary tool for platforms using managed payouts or custom scheduled payouts” with “a 1:1 mapping between a payout transfer and the individual payments, refunds, and adjustments that make up the payout”. One clause added to the platform paragraph. The author should note that on the platform side Adyen therefore also has a report keyed on the payout (to the user), which the chapter's “payout at Stripe, batch at Adyen” contrast does not cover.

## Not checked, or could not be verified

- “I found no newer Adyen engineering source” (after the 2021 post): the author's search statement. **Not checked**; I did not search Adyen's knowledge hub for newer posts on reconciliation.
- The industry-practice table (ledger, clearing file, bank statement) and the three-way-match inference block are labeled as industry practice and as inference; **not checked** against a source, and none is claimed.
- No source was unreachable. Three Stripe URLs redirect and were replaced with their final URLs: `/stripe-data/how-sigma-works` → `/data/how-sigma-works`; `/stripe-data/available-data` → `/data/data-freshness`; `/stripe-data/access-data-in-warehouse` → `/data/access-data-in-warehouse`. The Balance Platform Accounting Report entry now points to the `/platforms/` copy of the page (same text as the `/marketplaces/` copy; both return 200), because Larkfield uses the platform model and the “Reports and fee types” page links there. All 29 URLs in Sources and Evidence return 200 at the URL given.

## Format and rulings

- Ruling 22: all 20 inline external links in the running text and tables were reduced to plain attributions; every URL is in Sources.
- Ruling 18 (prefinancing documented for Adyen) and ruling 28 (ledger written only from report lines) are respected.
- `[[traceability-and-reconciliation]]` was listed in Sources but not used in the text; removed from the entry (the permalink is valid).
- Terms: PSP expanded; CET expanded at first use; “Connect webhook endpoints” glossed where first used.
- `timetoread` changed from 24 to 25 (5,692 words ÷ 230 = 24.7). The page is above the 5,500-word aim and below the 6,500 limit.
- Units unchanged (48 aligned); `validate_spec.py` and `check_draft.py structure` pass; build and render check pass.

## Larkfield consistency

All figures agree with the ledger: 412 payouts / €386,000 / three weeks; 44% and €493 million; €412,000 and its three causes; €120.00 at 19:42 on Tuesday 9 March 2027; €117.47 / €2.53 / €0.61 / €1.92; batch close 02:00 on 10 March; payout Thursday 11 March; refund of €84.00 on 18 March; five business days to Priya Raman's review; K2 and K3. Weekdays checked (9 March 2027 is a Tuesday, 11 March a Thursday).

## Ledger conflicts

- None. One addition for the ledger's owner to consider: the chapter 15 ledger line says the job runs “on that provider's report-ready signal”. On Adyen that is two signals (`REPORT_AVAILABLE` for the settlement details report, `balancePlatform.report.created` for the balance platform's daily report). The ledger line is not wrong, so I did not touch it.

## For other pages

- **Journal spec, this page's thesis and AC-2** (`journal-spec.json`, lines about 2294 and 2307; copied into this page's `spec.json` intent, which I left unchanged so the two still agree):
  - “per payable batch at Adyen”: the documented wording is “The default setting is to generate the report per merchant account, per batch.” (settlement details report page) and “When the payable batch closes, we create a Settlement details report.” (Getting paid). So “per payable batch” is right for the settlement details report, by default. For **platforms**, the “Reports and fee types” page labels the reports: “Payment accounting report **Required** for full financial reconciliation.”, “Settlement details report **Optional** for full financial reconciliation.”, “Monthly invoice **Required** for full financial reconciliation.”, “Balance Platform Accounting Report **Required** for full financial reconciliation.” It also says: “For complete financial reconciliation over a period of a month, you need to use a combination of Adyen account reports and balance platform reports.” The Balance Platform Accounting Report “is a daily report that tracks all balance changes on all balance accounts in your balance platform”. A thesis that covers platforms could read “per payable batch at Adyen (for a platform, per day and balance account)”.
  - AC-2 “no duration is published” is too broad (see #48). Suggested: “no time between the batch closing and the report is published”.
- `14-payouts-and-money-movement` owns the Stripe “paid then failed within 5 business days” fact; this page now cites `docs.stripe.com/payouts` for it. Check that chapter 14 quotes the same sentence.
- Any page that names `REPORT_AVAILABLE` as the readiness signal for Adyen balance platform reports has the same error as #60 (chapters 12, 13, 35 and 44 are the likely places).
