# Verification — 29-invoicing-collections-and-dunning (`invoicing-collections-and-dunning`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants, both documentation indexes (`llms.txt`), Stripe's Billing product page as HTML, Adyen's press release and two knowledge-hub articles as HTML, Orb's and Recurly's documentation as `.md` and HTML, the European Commission's ViDA page as HTML, Council Directive (EU) 2025/516 from `publications.europa.eu` (XHTML), and the Visa rules PDF converted with `pdftotext`.

Abbreviations: S = `https://docs.stripe.com`, A = `https://docs.adyen.com`, VR = Visa Core Rules and Visa Product and Service Rules, 24 October 2026.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe defines invoices as "statements of amounts owed by a customer" | S/invoicing/dashboard/credit-notes | confirmed | Inline link removed (ruling 22) |
| 2 | Adyen's documentation describes payments and stored payment details and no invoice | A/llms.txt, searched for invoice, dunning, receivable, billing, subscription, Orb | confirmed (as an absence) | —. The hits are Adyen's own invoices to the merchant, Klarna invoice lines and a dashboard of the merchant's open balances with Adyen |
| 3 | Stripe documents five invoice states | S/invoicing/overview; S/invoicing/integration/workflow-transitions | confirmed | — |
| 4 | "the few transitions between them", shown as a seven-row table | S/invoicing/integration/workflow-transitions | hedged | Stripe's table has ten rows. The page now says the table shows seven and names the three it leaves out (delete a draft, send an open invoice, failed payment on an uncollectible invoice) |
| 5 | Each transition has an API endpoint and a webhook; a draft can be deleted | same | confirmed | — |
| 6 | "`paid` and `void` are terminal" | S/invoicing/overview | hedged | The overview says of both "This status is terminal", but the same page says "You can also change the status of a paid invoice back to open by unapplying payments from it" and lists "Change the invoice status to `open`" as an action on a paid invoice. The sentence now reports both |
| 7 | A failed payment moves an open invoice to open, with `invoice.payment_failed` | S workflow-transitions | confirmed | — |
| 8 | Finalizing: "It allows the invoice to be paid. It ensures that an invoice number is present. It makes certain properties immutable on the invoice. It creates an incomplete payment intent for the invoice." | same | confirmed | These are four of five bullets; "lists what finalizing does" became "list of what finalizing does includes" |
| 9 | "you can’t change most of its details, including fields related to the amount or customer" | same | confirmed | — |
| 10 | "This is to satisfy the common tax-compliance requirement that finalized invoices be retained—as they were finalized—for a legally required minimum time period." | same | confirmed | — |
| 11 | Customer name, address and tax identifiers are copied onto the invoice and frozen | same (seven `invoice.customer_*` fields) | confirmed | — |
| 12 | "a credit note doesn’t void and replace the original invoice" | S/invoicing/dashboard/credit-notes | confirmed | Inline link removed |
| 13 | "The sum of all credit notes issued for an invoice can’t exceed the total amount of the invoice." | same | confirmed | — (the source has invisible zero-width characters before "total") |
| 14 | Wrong customer detail: void, duplicate, correct on the copy | S workflow-transitions | confirmed | — |
| 15 | Void: canceled, number stays on record | S/invoicing/overview ("This invoice is canceled"; "maintains a paper trail, which allows you to look up the invoice by number") | confirmed | — |
| 16 | Uncollectible: "The customer is unlikely to pay the invoice. Normally, you treat it as bad debt in your accounting process." | same | confirmed | Inline link removed |
| 17 | An uncollectible invoice can still become paid, a void one cannot | S workflow-transitions; overview | confirmed | — |
| 18 | ViDA "was adopted on 11 March 2025" and "will be rolled out progressively until January 2035" | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en | confirmed | Inline link removed |
| 19 | Since 14 April 2025 "Member States are able to introduce mandatory e-invoicing under specific conditions" | same ("Upon entry into force (14 April 2025), …") | confirmed | — |
| 20 | "Digital Reporting Requirements will affect cross-border B2B transactions from 1 July 2030" | same | confirmed | — |
| 21 | An electronic invoice "is structured data in a format an authority prescribes, not a PDF" | http://publications.europa.eu/resource/celex/32025L0516 (recital 9) | corrected | No source on the page supported "a format an authority prescribes". The directive limits the term to invoices "issued, transmitted and received in a structured electronic format allowing for their automated and electronic processing". Sentence replaced by that quotation; source entry added |
| 22 | `attempt_count` "indicates how many attempts have been made so far" | S/billing/revenue-recovery/smart-retries | confirmed | Inline link removed; attribution and date put in the sentence |
| 23 | Recurly: "Involuntary churn refers to customer loss caused by factors outside their direct intent — expired credit cards, bank account changes, or failed payment attempts" | https://docs.recurly.com/recurly-subscriptions/docs/involuntary-churn | confirmed | The page displays "Updated 4 months ago" (metadata 2026-07-07); cited as updated July 2026. "defines the term" was ambiguous after the definition of dunning; now "Billing vendors call that loss involuntary churn. Recurly, one of them, defines it…" |
| 24 | Stripe: "Businesses using Stripe recover 55% of failed payments on average" | https://stripe.com/billing (English text read at `/en-nl/billing` and `/gb/billing`; the bare address redirects by location to `/nl/billing`, whose Dutch text carries the same sentence) | confirmed, and hedged in scope | The sentence follows "AI-powered Smart Retries, card account updater, and cancellation surveys work together to keep revenue flowing." The page now says the 55% is not a figure for Smart Retries alone. Same change in the comparison table |
| 25 | Stripe: "US$8.2bn in failed payments recovered in 2025" | same | confirmed | — |
| 26 | The product page defines neither failed payment, nor recovery, nor the businesses averaged | same (no footnote attached to either figure) | confirmed | Added what Stripe does define elsewhere: S/billing/revenue-recovery/recovery-analytics gives a dashboard "Recovery rate: The percentage of subscription payment volume successfully recovered by any means after a failure"; the product page does not say its 55% is that measure. Source entry added |
| 27 | "I found no comparable figure from Adyen" | https://www.adyen.com/knowledge-hub/recurring-payments (16 June 2026); https://www.adyen.com/en_GB/knowledge-hub/rescue-failed-subscription-payments (4 December 2020) | corrected | Adyen publishes no average, but it does publish a figure. The 2026 guide: "Pinterest saw a 4% improvement in recovery rate on retried transactions, with expectation of reaching 10% over time". The 2020 article has it as the customer's words: "Early results point to a 4% improvement in recovery rate on retried transactions. My expectation as we grow is that the recovery rates will continue to improve up to as high as 10%." The page now quotes the 2026 sentence as Adyen's claim about one customer, dates its origin, flags the evidence age, and says no baseline is given. Same correction in the comparison table and in the paragraph on the limit of the public record; two source entries added |
| 28 | No independent, dated measurement of the involuntary share of churn was found | — | not checked (an absence; one web search in this session returned only vendor and competitor figures) | Kept as the author's "I found no…" |
| 29 | "Soft" and "hard" decline are not network terms; Visa sorts codes into four categories, the first never resubmitted | VR Table 7-2, section 7.3.6.3, p. 547–549 | confirmed | — |
| 30 | Stripe's hard decline codes, among them `lost_card`, `stolen_card`, `incorrect_number`, `revocation_of_authorization`, `authentication_required` | S smart-retries (nine codes listed) | confirmed | Inline link removed |
| 31 | "Retries continue to be scheduled, and attempt_count continues to increment, but retries only execute after detecting a new payment method." | same | confirmed | — |
| 32 | Custom schedule: "up to three retries, each with a specific number of days after the previous attempt" | same | confirmed | — |
| 33 | Orb retries "after 1, 4, and 9 days from the initial payment attempt" | https://docs.withorb.com/financial-operations/essential-dunning | confirmed | Inline link removed; attribution and date put in the sentence |
| 34 | Smart Retries envelope: 1, 2 or 3 weeks, 1 month or 2 months | S smart-retries | confirmed | — |
| 35 | "For new Stripe accounts, Stripe enables Smart Retries by default and configures it for up to 8 retries within 2 weeks." | same | confirmed | — |
| 36 | Two example signals (devices in the last N hours; best time to pay, 12:01 am) | same | confirmed | — |
| 37 | "That is the whole published description." | same | hedged | The page also says "Using AI" and "The AI model behind Smart Retries" and that Stripe keeps learning. Now "Apart from calling the model AI, that is the whole published description." |
| 38 | Visa, 24 October 2026: no resubmission after a category 1 code; otherwise "up to 20 attempts in 30 days" | VR Table 7-2 | confirmed | — |
| 39 | Stripe "recommends a maximum of eight retries" | S/declines/card | confirmed | Inline link removed; date added |
| 40 | Card networks "charge for excess" retries (requirements table) | A/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed, source was missing | No source on the page supported the fee. Added a sentence attributing it to Adyen's documentation ("excessive retry fee") and noting that Adyen's page still gives the limit as 15 (ruling 19); source entry added |
| 41 | "The network counts reattempts whichever of the merchant's systems sent them" | VR Table 7-2 ("a Merchant must never resubmit…"; limits are stated per merchant) | hedged | The rule does not say this in so many words. Now labeled as the author's reading: "Visa's rule binds the merchant and not one of its systems, so, as I read it…" |
| 42 | Card networks run account updater services | A/online-payments/account-updater ("Visa, Mastercard, and Cartes Bancaires offer a service to inform about changes to account information") | confirmed | Attribution added to the sentence; the overview page is now used, not only listed |
| 43 | Stripe: "Stripe works with card networks and automatically attempts to update saved card details whenever a customer receives a new card"; "International support varies from country to country. It isn’t possible to identify cards that support automatic updates." | S/payments/cards/overview | confirmed | Inline link removed |
| 44 | Adyen Real Time Account Updater: "When you submit a payment that is refused, … appears as a single transaction." | A/online-payments/account-updater/real-time-account-updater | confirmed | Inline link removed; "page last modified May 2026; the overview page above it dates from December 2019" removed (ruling 30) |
| 45 | It covers Visa, Mastercard and Cartes Bancaires, on payments the merchant initiates from stored details | same (`shopperInteraction` ContAuth; "Ask our Support Team to enable Real Time Account Updater") | confirmed | Added "once Adyen's support team has enabled it" |
| 46 | A network token stays valid through a reissue by design | — | not checked | No source on this page; the claim is ruling 8's gloss and is owned by `network-tokens` |
| 47 | Stripe SEPA: "Most failures occur within 6 business days after initiation" | S/payments/sepa-debit | confirmed | Inline link removed |
| 48 | Adyen SEPA: "Because SEPA transactions always have `eventCode` **AUTHORISED** in the response, these require a different rescue logic compared to card transactions."; the failure arrives as a chargeback | A/online-payments/auto-rescue/sepa | confirmed | — |
| 49 | Stripe retries SEPA and Bacs debits only for "Insufficient funds", at most 2 times within 30 days | S smart-retries (table); S sepa-debit | hedged | The retries are off until enabled: "If you haven’t enabled retries for the applicable payment method, Stripe doesn’t retry the payment." Sentence and table cell now say so |
| 50 | "Direct debit retries use the payment method’s retry configuration, not the general card retry policy." | S smart-retries | confirmed | — |
| 51 | Adyen SEPA: reasons AM04 and MS03; "a maximum of two rescue attempts within the rescue window" | A auto-rescue/sepa | confirmed | Inline link removed |
| 52 | Two reasons given; "chargebacks are typically fined by the issuing bank" | same | confirmed | — |
| 53 | Stripe emails "include a link to a page where the customer can update their payment method" | S/billing/revenue-recovery/customer-emails | confirmed | Inline link removed |
| 54 | Adyen: "an optional payment link sent when Auto Rescue ends without success, 'Valid for 5 days'" | A/online-payments/auto-rescue/cards | corrected | Adyen does not send the link to the shopper. The merchant receives `paymentLink.url` in the end-of-process webhook ("you can optionally use Pay by Link to send the shopper a payment link"). Sentence corrected |
| 55 | Stripe: "bank transfers don’t allow you to control the amount a customer sends to you, which means that customers might send too much or too little money by accident" | S/payments/bank-transfers | confirmed | Inline link removed |
| 56 | Each customer gets "a unique virtual bank account number" shown on the invoice | S/invoicing/bank-transfer | confirmed | Inline link removed |
| 57 | Arriving money is held "in a customer balance" | S/payments/bank-transfers | confirmed | — |
| 58 | Order of application: invoice number in the reference, then a payment reference, then a group, then invoices payable in full, oldest due first | S/payments/customer-balance/reconciliation | confirmed | Inline link removed |
| 59 | "a group of between one and five invoices and PaymentIntents awaiting the exact amount available" | same | confirmed | — |
| 60 | Partial payment only if enabled and the invoice number is in the transfer | same; S/invoicing/bank-transfer | confirmed | — |
| 61 | After 75 days Stripe "automatically attempts to return the funds to the customer’s bank account" | S/payments/bank-transfers | confirmed | — |
| 62 | Adyen: no invoice object, no customer balance for receivables, no cash-application feature | A/llms.txt; A/payment-methods/bank-transfer | confirmed (as an absence) | Added what Adyen does document: each bank-transfer payment gets "a unique virtual bank account number", so a transfer is matched to one payment. Source entry added |
| 63 | Smart Retries choose times "to increase the chance of successfully paying an invoice" | S smart-retries | confirmed | — |
| 64 | The retry uses a documented payment-method order starting with the subscription's default payment method | same | confirmed | — |
| 65 | "If recovery fails, the subscription transitions according to your settings": cancel, unpaid, past due, pause | same | confirmed | — |
| 66 | Adyen Auto Rescue "automatically retries refused or charged back shopper-not-present transactions such as subscription renewals. It uses smart logic to decide which payments can succeed when retried later, and performs these retries at optimal times" | A/online-payments/auto-rescue | confirmed | Inline links removed. "page last modified March 2020" and the evidence-age mark removed: the date came from `.md` front matter (ruling 30). The quotation is now introduced as the words of Adyen's documentation, followed by "'Smart' and 'optimal' are Adyen's words, with no measure behind them." |
| 67 | Adyen's support team enables the feature | A auto-rescue/cards ("contact our Support Team or your Adyen Account Manager") | confirmed | "or account manager" added |
| 68 | Rescue window: "one calendar month" at account level, between 1 and 48 days on a payment | same | confirmed | Scoped to cards (the SEPA page gives 42 days and 1 to 42); the quotation marks around "between 1 and 48 days" removed because the source bolds the numbers |
| 69 | The response says whether a rescue is scheduled; each retry "is a separate transaction, and thus generates a unique `pspReference`"; results by webhook | same | confirmed | — |
| 70 | "a unique `merchantOrderReference`. This should represent a specific billing cycle or subscription" | same | confirmed | — |
| 71 | Orb: "If payment method is updated prior to exhaustion of the dunning period, Orb will immediately try to collect on the invoice." | https://docs.withorb.com/financial-operations/essential-dunning | confirmed | — |
| 72 | Orb works "on top of several payment providers" | https://docs.withorb.com/llms.txt; https://docs.withorb.com/integrations-and-exports/adyen | hedged | The dunning page says only "payment gateway". Orb's documentation has gateway integration pages for Stripe and for Adyen; the sentence now says that. Source entry added |
| 73 | Adyen closed its acquisition of Orb on 1 July 2026 | https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates ("Both transactions officially closed on July 1, 2026") | confirmed | Inline link removed; attributed to the press release (ruling 21) |
| 74 | No Adyen documentation of an integrated billing product as of November 2026 | A/llms.txt (no entry for Orb, billing or subscriptions) | confirmed (as an absence) | — |
| 75 | Adyen instructs merchants to cancel a rescue when the shopper gives a new payment method or cancels | A auto-rescue/cards | confirmed | — |
| 76 | Smart Retries "are more effective than scheduled retries", with no figure | S/billing/revenue-recovery | confirmed | Inline link removed |
| 77 | "Neither documents a model, its inputs or a recovery rate" (also KEY POINT 3) | S smart-retries; A auto-rescue; rows 24–27 | hedged | Stripe names an AI model and two example inputs, and both vendors publish a marketing number. Now "Neither documents the model, its inputs beyond examples, or a recovery rate with a stated basis"; KEY POINT 3 says "a recovery rate with a stated basis" |
| 78 | Inference block: a model predicting approval, trained on each provider's history; "Neither company says so" | S smart-retries; Adyen 2026 guide ("with machine learning continuously improving revenue collection") | hedged | The block now separates what is documented (Stripe says AI model; Adyen's guide says machine learning) from what is inferred (what the model predicts and is trained on) |
| 79 | Table, unit being recovered: Adyen "a refused merchant-initiated transaction" | A auto-rescue | corrected | Adyen's words are "refused or charged back shopper-not-present transactions"; cell changed |
| 80 | Table, invoice and corrections | rows 3, 12, 14, 2 | confirmed | — |
| 81 | Table, default envelope | rows 34, 35, 67, 68 | confirmed | Adyen cell scoped to cards |
| 82 | Table, hard declines: Adyen says no rescue is scheduled "For example, because of account closure or fraud"; no code list on the page | A auto-rescue/cards | confirmed | — |
| 83 | Table, direct debit: Adyen SEPA 42-day window for the account | A auto-rescue/sepa ("The rescue window is set to 42 days") | confirmed | Stripe cell: "when the merchant turns retries on" added (row 49) |
| 84 | Table, card repair | rows 43–45 | confirmed | — |
| 85 | Table, published logic and results: Adyen "no figure found" | row 27 | corrected | Now "one customer's 4% improvement in a 2026 guide, without a baseline"; Stripe cell says the 55% is for its recovery tools together |
| 86 | Adyen: "you should cancel the Auto Rescue process for the refused payment"; cancellation confirmed later by webhook | A auto-rescue/cards (`CANCEL_AUTORESCUE`) | confirmed | — |
| 87 | Adyen SEPA: "You will receive the webhook 16 days after the rescue attempt" | A auto-rescue/sepa | confirmed | — |
| 88 | "Issuing a credit note doesn’t automatically refund the customer’s payment method" | S credit-notes | confirmed | — |
| 89 | "the sum of the refund, credit, and out-of-band payment amounts must equal the credit note total" | same | confirmed | — |
| 90 | Take-away: "Stripe's default is 8 retries in 2 weeks, Adyen's a calendar month" | rows 35, 68 | hedged | Now "Stripe's default for new accounts is up to 8 retries in 2 weeks, Adyen's account-level window for cards a calendar month" |
| 91 | Visa code 51 is insufficient funds, a soft decline | VR Table 7-2 (Category 2: "51 (Not sufficient funds)") | confirmed | — |
| 92 | Adyen's payment link and Auto Rescue are optional features that support activates | A auto-rescue/cards | confirmed | — |

Counts: 92 claims; 76 confirmed (four of them absences confirmed by searching the documentation index; row 24 confirmed with its scope narrowed; row 40 confirmed with its missing source added); 5 corrected (21, 27, 54, 79, 85); 9 hedged (4, 6, 37, 41, 49, 72, 77, 78, 90); 0 unsupported and removed; 0 unreachable; 2 not checked (28, 46). Rows 80, 81, 83 and 84 restate earlier rows in the comparison table.

## Could not verify, and what was done

- **Row 28**, the absence of an independent measurement of involuntary churn: an absence cannot be confirmed. The sentence stays in the first person ("I also found no…").
- **Row 46**, network tokens surviving a reissue: no source on this page; the sentence carries a link to `network-tokens`, which owns the claim. Not checked here.
- **Stripe's Billing product page** redirects by the reader's location (to `/nl/billing` from this machine). The quoted English sentences were read at `/en-nl/billing` and `/gb/billing`; the Dutch edition carries the same two figures. The source entry keeps `https://stripe.com/billing`.
- **Web Archive** refused the availability query (HTTP 403), so no archived copy of the 2020 Adyen article was recorded. The live page was read at its `en_GB` address; the address without a locale returns 404.

## Rulings applied

- **Ruling 22**: 23 inline external links reduced to plain text with attribution and year in the sentence; every URL is in Sources and Evidence.
- **Ruling 30**: Adyen's Auto Rescue overview, Account Updater overview and Real Time Account Updater pages were dated from `last_modified` front matter (March 2020, December 2019, May 2026). All three are now "n.d., accessed November 2026" in the text and in Sources, and the evidence-age mark that rested on the 2020 stamp is gone. The front matter still says 2020-03-04 and 2019-12-06 today; see "For the author".
- **Ruling 19**: Visa's limit is cited from the Visa rules (20 in 30 days); the page now also notes that Adyen's documentation still says 15.
- **Rulings 6, 13, 15, 21**: already followed; checked.
- Format: SEPA expanded on first use; `timetoread` changed from 27 to 28 (6,493 words ÷ 230); American spelling and banned words checked; all `[[permalinks]]` are in the valid list; all 30 source URLs return a page.
- Sources added (eight): Stripe revenue recovery analytics; Adyen's Visa fee mapping page, Bank Transfer page and two knowledge-hub articles; Orb's Adyen integration page; Council Directive (EU) 2025/516. None removed.
- `spec.json`: evidence lines for the churn figures, Auto Rescue, Real Time Account Updater and the limit of the public record brought in line; one open question reworded; changelog entry added. No unit added, dropped, merged or moved.

## Larkfield consistency

All figures agree with the ledger: 1 October 2026, 38% in six hours, 7,900 renewals; Femke de Graaf (joined January 2027); Stripe Billing since 2018 and the €89, €189 and €349 plans; K1 and K5; Mila's €49.00 renewal declined on 1 April 2027 with Visa code 51 and approved on 4 April (day 3); the policy table (days 3, 7 and 12; day 14; day 30); the December 2026 recovery table (488,760 + 13,500 + 7,560 + 4,560 = 514,380; 25,620 of 51,240; 25,620 × €49 = €1,255,380); the Double Charge of 1 November 2026 with 1,840 members; Studio Noord's March 2027 invoice (€89 + €57.68 = €146.68; 180 × €0.07 = €12.60; €134.08). The page states no weekdays.

## Ledger conflicts

- **How the 7,900 emails of 1 October 2026 were triggered.** The line for `21-developer-platform` says an HTTP 429 "was treated as a failed attempt, retried three times at once and then marked failed, which triggered the dunning email". The line for `29-invoicing-collections-and-dunning` says the emails "came from a job that selected memberships that were due and had no successful payment". The two can both hold (the renewals were marked failed, and the email job read only "no successful payment"), but neither line says so. This page owns the email job and keeps its account. Its sentence "None had been attempted" now continues "the provider had turned the requests away at its rate limit, before any card was charged", which agrees with chapter 21's 429. The section title still says "Payments Nobody Attempted".

## For other pages

- `09-authorization-optimization` cites Auto Rescue. If it says Adyen publishes no result for Auto Rescue, the same correction applies (Adyen's guide of 16 June 2026, one customer, 4%).
- `43-journey-failed-renewal` and any page that dates Adyen's Auto Rescue overview to 2020 from its front matter: ruling 30 applies.
- Adyen's guide of 16 June 2026 also states: "Across our top 100 businesses, automatically updating account data recovered $1.08B in revenue over 12 months." It is a vendor claim about Real Time Account Updater and is not used on this page; `23-network-tokens` or `09-authorization-optimization` may want it, attributed.

## For the author

1. **Evidence age of Adyen's Auto Rescue overview.** Ruling 30 forbids dating it from front matter, so the page no longer says "6 years". The front matter does say 2020-03-04, and the product wording matches the 2020 knowledge-hub article. If you want a caution there, it needs a wording that does not assert a date.
2. **Adyen's 4% figure** is now on the page three times (the paragraph on the size of the loss, the comparison table, the inference block mentions the 2026 guide). It is attributed as Adyen's claim about one customer. Decide whether one mention is enough.
3. **Length.** The page is at 6,493 words against a limit of 6,500. Any further addition needs a cut.
4. **Is `paid` terminal?** Stripe's overview contradicts itself (row 6). The page reports both statements; the figure placeholder and the state table are unchanged.
