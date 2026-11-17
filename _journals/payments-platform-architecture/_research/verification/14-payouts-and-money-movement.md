# Verification — 14-payouts-and-money-movement (`payouts-and-money-movement`)

Verification pass of 17 November 2026. Every source below was fetched in this session with `curl`: Stripe and Adyen documentation as `.md` variants, Stripe's Connect pricing page, Stripe's support article, Adyen's press release and Pay.UK's page as HTML, and Regulation (EU) 2024/886 from the Publications Office (`Accept: application/xhtml+xml`, `Accept-Language: en`). Quotations were compared with the fetched text by script (typographic quotes, markdown emphasis and link brackets aside) and each miss was read in context by hand.

Abbreviations: S = `https://docs.stripe.com`, A = `https://docs.adyen.com`, REG = `http://publications.europa.eu/resource/celex/32024R0886`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe: a failed payout "might initially show as `paid`" (key points, lifecycle) | S/payouts; S/api/payouts/object | confirmed | — |
| 2 | Adyen: a non-instant payout "cannot fail" but can be returned | A/payouts/payout-service/payout-lifecycle | confirmed | — |
| 3 | Euro-area providers must verify the payee before authorization since 9 October 2025; the result is a warning and the payer decides | REG, Article 5c(1), (5), (9) | confirmed | — |
| 4 | "Stripe sends funds from your available balance to your bank account as payouts." | S/payouts | corrected | The source sentence ends in a colon, not a period; requoted as Stripe "sends funds … as payouts". |
| 5 | Adyen lifecycle steps received, authorised ("we reserve the payout amount on your balance account"), booked ("Adyen deducts the funds from your balance account and creates a transaction") | A/…/payout-lifecycle | confirmed | — |
| 6 | Adyen lifecycle page "last modified 17 November 2026" | A/…/payout-lifecycle | corrected | The date is `last_modified` metadata of the `.md` variant, equal to the minute for three pages fetched today (a build timestamp) and not displayed on the page; other Adyen pages carry 2020–2023 values that contradict their content. Cited as "n.d., accessed November 2026" (ruling 25), in the text, the source entry and the spec. |
| 7 | Stripe: "A posted status doesn’t guarantee that your recipient has received money, because their bank might delay the release of funds." | S/global-payouts/manage-payouts | confirmed | — |
| 8 | Adyen: non-instant bank transfers get `tracking.estimatedArrivalTime` | A/…/payout-lifecycle | confirmed | — |
| 9 | Stripe: "Incorrect destination information causes most returned payouts (…)" | S/global-payouts/manage-payouts | confirmed | Attribution with date added to the sentence. |
| 10 | Rails table: behavior column | none (labeled industry practice) | not a documented claim | — |
| 11 | Rail names "are the ones Stripe's Global Payouts price list uses" | S/global-payouts/supplemental-pricing-information; S/global-payouts | hedged | The price list names SEPA Credit Transfer, SEPA Instant Credit Transfer, ACH, Faster Payments (FPS), Fedwire and SWIFT, but no card rail. Sentence now says the bank rails are named as in the price list and that the overview page adds payouts "to debit cards". |
| 12 | Adyen: `regular` cut-off 15:45 CET for SEPA EUR, same-day settlement; "initiated after the cut-off time will be processed the next day" | A/…/pay-out-to-bank-accounts | confirmed | — |
| 13 | Stripe: euro manual payout same day if initiated "before 4 pm Europe/Copenhagen" | S/payouts | confirmed | — |
| 14 | Stripe `arrival_date`: "Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays" | S/api/payouts/object | confirmed | Date added to the sentence. |
| 15 | Adyen "cannot process payouts on bank holidays"; "your bank may need up to three more business days to post the funds" | A/account/getting-paid | confirmed | — |
| 16 | Regulation (EU) 2024/886 of 13 March 2024; instant credit transfer "executed immediately, 24 hours a day and on any calendar day"; "within 10 seconds"; sending by 9 October 2025 in the euro area | REG, Article 1 (new Articles 2(1a), 5a(4)(c), 5a(8)) | confirmed | — |
| 17 | Adyen: `instant` SEPA EUR maximum 100,000.00 | A/…/pay-out-to-bank-accounts | confirmed | — |
| 18 | Adyen: "while most banks can process **regular** transfers, some do not support **instant** transfers" | A/platforms/custom-payouts/on-demand-payouts | confirmed | — |
| 19 | Adyen cross-border: "payout delays and additional fees may occur due to intermediary banks. As a result, the beneficiary may receive a lower amount than the instructed value." | A/…/pay-out-to-bank-accounts | confirmed | — |
| 20 | Stripe Global Payouts: SWIFT 20.00 EUR; FX fee "0.50% for major currencies and 1.00% for the others" | S/global-payouts/supplemental-pricing-information | corrected | The 0.50% list is 20 named currencies (it includes MXN, RON and ZAR), all others pay 1.00%, and the higher of the two currencies' rates applies. Sentence and spec evidence changed. |
| 21 | Stripe schedules manual, daily, weekly, monthly; "Choosing a payout schedule doesn’t change how long … It only controls when payouts are sent." | S/payouts | confirmed | — |
| 22 | Adyen: the payable batch is "one sales day's payments paid out together" | A/account/getting-paid | hedged | True under the Sales day payout model; under Pass-through payout one sales day leaves in several batches. Qualifier added. |
| 23 | Adyen: "After the payable batch closes, it can take one to two business days for the payout to be initiated." | A/account/getting-paid | confirmed | — |
| 24 | Adyen managed payouts: Standard "two business days after capture", Accelerated one | A/platforms/managed-payouts | confirmed | Wording made explicit that the quote is about funds arriving. |
| 25 | Stripe Payout status quote ("A payout is `pending` until … then change to `failed`.") | S/api/payouts/object | confirmed | — |
| 26 | Stripe OutboundPayment statuses `processing`, `failed`, `canceled`, `posted`, `returned` | S/global-payouts/manage-payouts | confirmed; hedged | The page now also documents a PayoutIntent object (API version `2026-10-28.preview`) that wraps the OutboundPayment; a clause says so. |
| 27 | "The payout posts and funds leave the financial account"; "Creating an OutboundPayment doesn’t mean that Stripe has sent the funds." | S/global-payouts/manage-payouts | confirmed | — |
| 28 | Adyen tracking: instant bank transfers "receive a **credited** `status` when the funds arrive, or **failed**"; cards `accepted`; non-instant only the estimate | A/…/payout-lifecycle | confirmed | — |
| 29 | Adyen: "After a payout reaches the **booked** `status`, but before the funds leave Adyen, the payout is automatically analyzed"; failed manual review freezes the funds | A/…/payout-lifecycle | confirmed | — |
| 30 | Adyen platforms webhooks page on `booked`: "This status is not final." | A/platforms/payout-webhooks | confirmed | — |
| 31 | States table (Stripe Payout, Global Payouts, Adyen transfer) | sources of 25–30, 34–36 | confirmed | — |
| 32 | Stripe: "It can take up to 5 additional business days for your bank to return the payout and inform us that it failed" | S/payouts | confirmed | — |
| 33 | Stripe `failure_balance_transaction`: "the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance" | S/api/payouts/object | confirmed | — |
| 34 | Stripe Global Payouts: "Stripe returns the funds to you in a separate transaction"; "within 2–3 business days, but might take longer depending on the recipient country" | S/global-payouts/manage-payouts | confirmed | — |
| 35 | Adyen: "Payouts that do not have an **instant** `priority` cannot fail, but they can be returned by the counterparty's bank"; "A new transaction is created for the return" | A/…/payout-lifecycle | confirmed | — |
| 36 | Adyen merchant payout: return visible under journal type `BankInstructionReturned` | A/account/getting-paid | confirmed | — |
| 37 | Stripe: "Stripe then reattempts the payout at the next scheduled payout interval." | S/payouts | confirmed | — |
| 38 | Stripe Global Payouts: "Stripe doesn’t retry or reroute payouts automatically." | S/global-payouts/send-money | confirmed | — |
| 39 | Adyen: several priorities, next tried "If that route is unavailable"; no automatic resend after a return documented | A/platforms/custom-payouts/on-demand-payouts; A/…/payout-lifecycle; A/llms.txt | confirmed (absence checked in the lifecycle page and the documentation index) | — |
| 40 | Stripe's payouts page names no rail for a standard payout | S/payouts | confirmed (only "same-day banking rails", unnamed) | — |
| 41 | Adyen press release of 9 April 2026: banking licenses enable "direct connections to payment rails"; rails not listed | adyen.com/press-and-media/adyen-launches-intelligent-money-movement | confirmed (displayed date "April 9th, 2026") | — |
| 42 | Neither publishes the bank or rail per country, or return rates | S/llms.txt, A/llms.txt, pages above | confirmed as far as searched | — |
| 43 | Stripe: "If you provide incorrect information, such as a mistyped account number … fall under your responsibility." | S/payouts | confirmed (two consecutive sentences, a paragraph break between them in the source) | — |
| 44 | Stripe Global Payouts reversals: US domestic "within 24 hours", not UK FPS or cross-border; "can’t guarantee a reversal" | S/global-payouts/manage-payouts | confirmed | — |
| 45 | Regulation: "the execution of a credit transfer to an unintended payee on the basis of an incorrect unique identifier" | REG, Article 5c(8) | confirmed | — |
| 46 | "Article 5c of the same regulation": "A payer’s PSP shall offer the payer a service ensuring verification of the payee"; "before the payer is offered the possibility of authorising that credit transfer" | REG | corrected | Article 5c is an article of Regulation (EU) No 260/2012, inserted by Regulation 2024/886. Sentence now says so. Quotes confirmed. |
| 47 | Almost-match shows the name on the account; free of charge; may not block the payer; euro area since 9 October 2025; non-consumer opt-out for orders "as a package" | REG, Articles 5c(1)(a), 5b(2), 5c(5), 5c(9), 5c(6) | confirmed | — |
| 48 | Pay.UK: "Since launching in 2020, over 300 organisations … every day."; "an API-based peer-to-peer service, … in the ecosystem" | wearepay.uk/…/confirmation-of-payee/ | confirmed | — |
| 49 | Stripe: Confirmation of Payee for a GBP payout between UK accounts "in the Dashboard", outcomes Match, "Partial Match or No Match", Unavailable, "Continue without match" | S/global-payouts/send-money | corrected | The page documents the check in the API as well (`recipient_verification` on a PayoutIntent; mandatory before an OutboundPayment), with a non-match to be acknowledged. Sentence, table cell, source entry and spec changed. |
| 50 | Stripe support article: EU check when a payout is initiated in the Dashboard ("read through a summarizing fetch, so paraphrased") | support.stripe.com/questions/verification-of-payee-support-for-treasury | corrected | The article text is embedded in the page's HTML and was read directly. Now quoted: "When initiating a payout to an EU recipient in the Dashboard, Stripe will perform the VoP check"; "prompted to acknowledge the difference and either edit the details or cancel the payout". The paraphrase caveat is removed from the text, the source entry and the spec. |
| 51 | Adyen `POST /verifyCounterpartyName`: enterprise payouts, domestic EU and UK accounts; four responses; name returned only on a partial match, "To safeguard against name-guessing" | A/…/verify-counterparty | confirmed | — |
| 52 | Nothing from either provider about a payee-name check on a merchant's standard payout | S/llms.txt, A/llms.txt (searched "payee", "counterparty name", "name match") | confirmed as far as searched | — |
| 53 | Stripe: "Only continue without a match if you’re confident … might not be recoverable." | S/global-payouts/send-money | confirmed | — |
| 54 | Article 5c: a PSP "shall not be held liable for the execution of a credit transfer to an unintended payee" (if it fulfilled the article) | REG, Article 5c(8) | confirmed | — |
| 55 | Return window sources: Stripe 5 business days, Global Payouts "typically" 2–3, Adyen five business days after the batch closed; no upper bound stated | S/payouts; S/global-payouts/manage-payouts; A/account/getting-paid | confirmed | Date added to the sentence. |
| 56 | Stripe Instant Payouts "typically settle in the associated payout account within 30 minutes"; at most 10 a day; 9,999 EUR in the euro area; "Stripe assesses a fee on each Instant Payout" | S/payouts/instant-payouts | confirmed | — |
| 57 | Connect pricing shows Instant Payouts at 1% of payout volume (euros; other countries not checked) | stripe.com/connect/pricing (redirected to the Dutch page: "1% van uitbetalingsvolume") | confirmed | — |
| 58 | Adyen: "A payout with a higher priority incurs higher fees"; no public price list; `credited` is the confirmation | A/…/pay-out-to-bank-accounts; A/…/payout-lifecycle | confirmed (no price list found in A/llms.txt) | — |
| 59 | Stripe Global Payouts: senders in GB or US; 22 countries in private preview; "requires Treasury"; "best for businesses that already hold the licenses required to move money themselves" | S/global-payouts | confirmed (22 country codes counted) | — |
| 60 | Stripe: payouts "don’t flow through a Stripe balance belonging to the recipient" | S/connect/cross-border-payouts-to-recipients/compare-global-payouts | confirmed | — |
| 61 | Adyen payouts service: third parties paid from a balance account through the Transfers API; "funds acquired through payments with Adyen or externally transferred funds" | A/payouts/payout-service; A/…/pay-out-to-bank-accounts | confirmed | Source entry title corrected to the page's title, "Payouts and Payments". |
| 62 | Where They Differ: `preferred_networks` values `ach`, `fedwire`, `fps`, `sepa`, `swift`; "Stripe selects the most appropriate network" | S/global-payouts/send-money | confirmed | — |
| 63 | Where They Differ: Adyen priorities regular, fast, instant, wire, cross-border, mapped to a transfer route | A/…/pay-out-to-bank-accounts | confirmed | — |
| 64 | Where They Differ: remaining Stripe and Adyen cells | rows 25–30, 34–38, 49–51, 58 | confirmed | Payee-check row: Stripe cell updated (row 49); last column changed from "let the sender continue" to "who decides what to do with it", because the EU support article names only acknowledging, editing or canceling. No cell says "Not public". |
| 65 | Stripe events `payout.paid` and `payout.failed` (Larkfield scene) | S/payouts; S/api/events/types | confirmed (`payout.paid`: "Occurs whenever a payout is *expected* to be available in the destination account. If the payout fails, a `payout.failed` notification is also sent, at a later time.") | Events added to the source entry's scope. |
| 66 | Adyen: flagged payout goes to `pending` after `booked` | A/…/payout-lifecycle | confirmed | — |
| 67 | Stripe Global Payouts: held for review stays `processing`, reason `under_review`, typically up to 2 business days | S/global-payouts/manage-payouts | confirmed | Date added to the paragraph. |
| 68 | Stripe `trace_id`: "A value that generates from the beneficiary’s bank that allows users to track payouts with their bank" | S/api/payouts/object | confirmed | — |
| 69 | Adyen: "download the bank instruction letter" and share it with the bank | A/account/getting-paid | confirmed (the source links the words "bank instruction letter") | — |
| 70 | Take-away: `paid` may become `failed` within five business days; `booked` "is not final"; payee check since 9 October 2025 and in the UK since 2020 | rows 1, 30, 3, 48 | confirmed | "As of November 2026" added. |

Counts: 70 claims checked. 59 confirmed, 6 corrected (4, 6, 20, 46, 49, 50), 4 hedged (11, 22, 26, 64), 0 unsupported, 0 unreachable, 1 not a documented claim (10).

## Could not verify, and what was done

- **Regulation link.** `http://publications.europa.eu/resource/celex/32024R0886` returns HTTP 400 or 404 to a client that sends no `Accept-Language` header and 200 with browser headers. The text was read in full for the cited articles. The URL is kept (the brief prescribes it and 23 pages use it); the source entry says how it is served. EUR-Lex itself answers automated clients with HTTP 202 and an empty challenge page.
- **Adyen page dates.** The `.md` variants carry `last_modified` values (Getting paid 2020-11-10, On-demand payouts 2020-09-11, Managed payouts 2022-04-20, Payout transfer webhooks 2023-03-21, Pay out to bank accounts 2023-11-30) that cannot be the content dates: Getting paid links the 2026 bank-holiday file. None is displayed on the page. All Adyen documentation is therefore cited "n.d., accessed 2026-11", and no evidence-age flag was added on the strength of that metadata.
- **Absence claims** (rows 39, 40, 42, 52, 58) were checked against the cited pages and both documentation indexes; an absence cannot be proven beyond that.
- **Connect pricing** was served in Dutch after a geographic redirect; the 1% figure was read from that page. The page's own caveat ("other countries not checked") stands.

## Format and rulings

- Ruling 22: 16 inline external links reduced to plain text; every URL was already under Sources and Evidence.
- Sources: the Global Payouts price list URL changed to its redirect target; the three-link Adyen bullet split into one bullet per URL; "Pay out to cards" removed (nothing in the text rests on it); "no payout fee" removed from the scope of the Stripe payouts entry (not stated in the text).
- `timetoread` changed from 23 to 24 (5,487 words ÷ 230).
- "FX" expanded on first use. No banned words; no hard-coded part references.
- No unit added, dropped, merged or reordered. Spec evidence strings updated to match the corrections; validation and the structure check pass; build and render check clean.

## Larkfield consistency

- Weekdays checked: Tuesday 9 March, Thursday 11 March and Thursday 25 March 2027 are correct; 25 March is the tenth business day after 11 March (Good Friday is 26 March). 412 payouts and €386,000 give €937 on average; 1% of €117.47 is €1.17.
- **Money arriving versus the state `arrived`.** The page said the payout was "arriving on Thursday 11 March" and that "the money lands that day" without qualification. Following chapter 3's verification, 11 March is now stated as the day the money is due and the best case (Adyen's Getting paid page allows up to five business days from batch close to bank posting), and the page says in two places that the record state `arrived`, set on 25 March, is the day Larkfield stopped expecting a return and not the date of the credit. The ledger line for this chapter is unchanged and still agrees.

## Ledger conflicts

- None. Note for the ledger's readers: `44-journey-platform-payment` lists "payout 11 March, arrived 25 March"; that is consistent only if "arrived" is read as the record state.

## For other pages

- Any page that cites an Adyen documentation page with a "last modified" date taken from the `.md` front matter should check it: the value is a build timestamp on some pages and years stale on others.
- Any page that cites `docs.stripe.com/global-payouts/pricing` should use `docs.stripe.com/global-payouts/supplemental-pricing-information`.
- Pages that describe Stripe's Global Payouts objects (chapter 35, 36) may need the PayoutIntent object, documented under API version `2026-10-28.preview`.
- `44-journey-platform-payment`: the step "payout 11 March, arrived 25 March" should say that 25 March is Larkfield's record state.

## For the author

- The EU check at Stripe: the support article does not say whether a sender can proceed past a mismatch. The page now quotes it and makes no claim either way.
