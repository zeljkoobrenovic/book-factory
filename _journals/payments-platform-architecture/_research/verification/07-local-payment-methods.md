# Verification — 07-local-payment-methods (`local-payment-methods`)

Verification pass of 17 November 2026. Every source in the page's Sources and Evidence section was fetched in this session: Stripe and Adyen documentation as `.md` variants, the Stripe blog post and the iDEAL, Federal Reserve and Direct Debit pages as HTML, the two EU texts from publications.europa.eu, and both providers' `llms.txt` indexes. Quotations were compared with the fetched text by script after normalizing typographic quotes and markdown marks, and the surrounding passage was read for each claim.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen SEPA page: a chargeback notification "can indicate" that "There were insufficient funds in the shopper's bank account" | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | No edit |
| 2 | Stripe overview lists eight payment method families | https://docs.stripe.com/payments/payment-methods/overview | corrected | Stripe lists ten (also stablecoin payments and gift cards). Sentence now names all ten |
| 3 | Stripe: "Payment methods in the same family have similar features and checkout experiences" | https://docs.stripe.com/payments/payment-methods/overview | confirmed | Inline link removed (ruling 22) |
| 4 | Adyen catalog gives each method a type and a flow such as Direct, Redirect or voucher | https://docs.adyen.com/payment-methods | confirmed | Inline link removed |
| 5 | Stripe SEPA: "Checkout and the Payment Element automatically display the required mandate terms and record the customer's acceptance" | https://docs.stripe.com/payments/sepa-debit | confirmed | Inline link removed |
| 6 | Adyen SEPA: "By default, Adyen uses its creditor ID on your behalf" | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | Inline link removed |
| 7 | Adyen SEPA: "Adyen is only notified of a cancelled SEPA mandate when a payment is charged back" | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | No edit |
| 8 | Stripe: "A succeeded status indicates ... but funds can still be refunded, disputed, returned, or reversed." | https://docs.stripe.com/payments/payment-methods | confirmed | Inline link removed |
| 9 | Stripe iDEAL: "immediate notification"; manual capture No | https://docs.stripe.com/payments/ideal | confirmed | Inline link removed |
| 10 | Stripe iDEAL: "Customers can't dispute iDEAL / Wero payments with their bank" | https://docs.stripe.com/payments/ideal | confirmed | No edit |
| 11 | Stripe Bancontact: customers "can't file a chargeback through their bank" | https://docs.stripe.com/payments/bancontact | confirmed | Inline link removed; date added |
| 12 | Adyen iDEAL page: no separate captures, no chargebacks; last modified 2026-11-17 | https://docs.adyen.com/payment-methods/ideal | confirmed | Inline link removed |
| 13 | iDEAL and Bancontact are both bank redirects (pushes) | https://docs.adyen.com/payment-methods | hedged | Stripe lists Bancontact under bank redirects; Adyen's catalog types it as cards (Bancontact card) and wallets (Bancontact mobile), with no chargebacks. A clause now says so |
| 14 | PSD2 Art. 76(1): "the payer has an unconditional right to a refund within the time limits laid down in Article 77" (euro direct debits) | http://publications.europa.eu/resource/celex/32015L2366 | confirmed | Fourth subparagraph of 76(1), scoped to direct debits under Regulation 260/2012. Inline link removed; directive number and year put in the sentence |
| 15 | PSD2 Art. 77(1): "a period of 8 weeks from the date on which the funds were debited" | http://publications.europa.eu/resource/celex/32015L2366 | confirmed | No edit |
| 16 | PSD2 Art. 71(1): "no later than 13 months after the debit date" | http://publications.europa.eu/resource/celex/32015L2366 | confirmed | No edit |
| 17 | PSD2 is "due to be replaced by PSD3 and the Payment Services Regulation" | https://www.algoodbody.com/insights-publications/psd-3-psr-final-compromise-texts-published | hedged | No source on the page supported it. Reworded to what a law-firm briefing of 24 April 2026 says (final compromise texts published, formal adoption pending), labeled as a secondary source; source entry added |
| 18 | Stripe SEPA: "Wait at least 6 business days before treating a SEPA Direct Debit payment as successful" | https://docs.stripe.com/payments/sepa-debit | confirmed | Attribution to the page added |
| 19 | Stripe SEPA: "You can't submit evidence or counter a SEPA Direct Debit dispute through Stripe" | https://docs.stripe.com/payments/sepa-debit | confirmed | No edit |
| 20 | Both providers document the 8-week and 13-month rights | https://docs.stripe.com/payments/sepa-debit ; https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | No edit |
| 21 | Adyen SEPA API-only example answers with resultCode Received | https://docs.adyen.com/payment-methods/sepa-direct-debit/api-only | confirmed | Inline link removed |
| 22 | Adyen SEPA: "You cannot defend SEPA chargebacks" | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | No edit |
| 23 | Adyen SEPA: "Due to the risk of chargebacks, we do not recommend using SEPA for one-off payments or the sale of physical goods" | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | No edit |
| 24 | Stripe Bacs: "typically takes 4 business days to confirm" | https://docs.stripe.com/payments/bacs-debit | confirmed | URL changed (old path redirects); the source's condition "when a mandate is already in place" added; inline link removed |
| 25 | Adyen Bacs: "Unpaid direct debits are booked as chargebacks" | https://docs.adyen.com/payment-methods/bacs | confirmed | Inline link removed; date added |
| 26 | Stripe ACH: "up to 60 calendar days after a debit on a personal account" | https://docs.stripe.com/payments/ach-direct-debit | confirmed | Date added |
| 27 | Adyen ACH: "up to two years after the settlement date" | https://docs.adyen.com/payment-methods/ach-direct-debit | confirmed | No edit |
| 28 | Nacha's rules behind the two ACH windows | none | not checked | The page already says they were not checked |
| 29 | Adyen Apple Pay: "uses network tokenization"; last modified 2023-05-08 | https://docs.adyen.com/payment-methods/apple-pay | confirmed | Inline link removed; date put in the sentence; the evidence-age mark now says the age is by the last-modified date |
| 30 | Adyen catalog lists chargebacks and separate captures for Apple Pay | https://docs.adyen.com/payment-methods | confirmed | No edit |
| 31 | Stripe Klarna: "Klarna collects the initial payment from your customer and any future installment payments" | https://docs.stripe.com/payments/klarna | confirmed | Inline link removed |
| 32 | Regulation (EU) 2024/886 of March 2024: "within 10 seconds of the time of receipt of the payment order" | http://publications.europa.eu/resource/celex/32024R0886 | confirmed | Dated 13 March 2024, Official Journal 19 March 2024. Inline link removed |
| 33 | Stripe Pix: settlement "Up to 2 business days (T+2)"; disputes supported | https://docs.stripe.com/payments/pix | confirmed | Inline link removed |
| 34 | Adyen Pix: "open a dispute with their bank within 90 days" | https://docs.adyen.com/payment-methods/pix | confirmed | Inline link removed; date added |
| 35 | FedNow "went live on July 20, 2023"; source cited as n.d. | https://www.federalreserve.gov/paymentsystems/fednow_about.htm | corrected | The quote is right, the date was wrong: the page displays "Last Update: July 20, 2023". Cited with that date and an evidence-age mark in the text and the source entry |
| 36 | FedNow is in neither provider's method list | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | confirmed | No hit for FedNow in Stripe's overview, Adyen's catalog or either documentation index; the sentence now names the indexes too |
| 37 | Wero is the scheme of the European Payments Initiative and is replacing iDEAL | https://ideal.nl/en/naar-wero ; https://docs.adyen.com/payment-methods/ideal | confirmed | No edit |
| 38 | The European Payments Initiative is "a bank consortium" | https://ideal.nl/en/naar-wero | hedged | No fetched source uses the word. Replaced by iDEAL's own wording, "backed by 16 major European banks" |
| 39 | Adyen Wero: "Wero is currently in development"; last modified 2026-11-17 | https://docs.adyen.com/payment-methods/wero | confirmed | Inline link removed |
| 40 | Adyen Wero: "The payment guarantee is the shopper's bank's commitment to pay Adyen. It is not the receipt of funds." | https://docs.adyen.com/payment-methods/wero | confirmed | No edit |
| 41 | Adyen Wero: a CAPTURE_FAILED event if capture keeps failing | https://docs.adyen.com/payment-methods/wero | confirmed | No edit |
| 42 | iDEAL: "By the end of 2027 at the latest, all iDEAL merchants will have transitioned to Wero" | https://ideal.nl/en/naar-wero | confirmed | URL changed (www redirects); inline link removed |
| 43 | iDEAL: milestones "subject to further consultation with the regulator" | https://ideal.nl/en/naar-wero | confirmed | No edit |
| 44 | Stripe: with vouchers "customers complete online purchases in person" | https://docs.stripe.com/payments/payment-methods/overview | confirmed | Inline link removed; source and date named |
| 45 | Adyen catalog gives cash methods the flow "voucher" | https://docs.adyen.com/payment-methods | confirmed | Boleto and OXXO: Type Cash and ATM, Flow voucher |
| 46 | Stripe SEPA refunds "appear as separate credits to the customer's bank account instead of reversals", within 180 days | https://docs.stripe.com/payments/sepa-debit | confirmed | Source and date named |
| 47 | Stripe iDEAL refunds "can remain in a pending state for up to 7 days" | https://docs.stripe.com/payments/ideal | confirmed | No edit |
| 48 | Adyen refund page: status "can change from Refunded to RefundedReversed"; last modified 2023-04-03 | https://docs.adyen.com/online-payments/refund | confirmed | Inline link removed; date put in the sentence |
| 49 | Stripe: "accept a variety of payment methods through a single API" | https://docs.stripe.com/payments/payment-methods | confirmed | No edit |
| 50 | Stripe: "The PaymentIntent object's next_action property specifies the customer action" | https://docs.stripe.com/payments/payment-methods | confirmed | No edit |
| 51 | Adyen's integration guide "uses the same server requests for every method"; last modified 2026-11-02 | https://docs.adyen.com/online-payments/build-your-integration | hedged | The guide does not say that. Replaced by its own use-case line, "Make a payment with any available payment method", which it lists for both flows |
| 52 | Stripe: "A PaymentMethod object contains the payment method details to create payments"; used with a PaymentIntent or SetupIntent | https://docs.stripe.com/payments/payment-methods | confirmed | No edit |
| 53 | Stripe: "Each PaymentMethod has a type attribute, such as "type": "sepa_debit", and a corresponding hash ..." | https://docs.stripe.com/payments/payment-methods | confirmed | No edit |
| 54 | Stripe: some methods "can't be attached to customers because they're consumed after a payment attempt" | https://docs.stripe.com/payments/payment-methods | confirmed | No edit |
| 55 | Stripe blog, 17 August 2023: "today, we're changing the default behavior of the PaymentIntents and SetupIntents API" | https://stripe.com/blog/dynamic-payment-methods | confirmed | Displayed date August 17, 2023. Inline link removed |
| 56 | Stripe changelog 2023-08-16: the previous default was to "accept only card payments" | https://docs.stripe.com/changelog/2023-08-16/automatic-payment-methods | confirmed | Inline link removed |
| 57 | Current Stripe documentation confirms dynamic payment methods as the default; the list comes from dashboard settings | https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods | confirmed | No edit |
| 58 | Stripe: "Stripe handles the logic for dynamically displaying the most relevant eligible payment methods to each customer" | https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods | hedged | The source limits the sentence to Elements, Checkout, Payment Links and hosted invoices; "with Stripe's prebuilt payment forms" added |
| 59 | Stripe: "Activation is generally instantaneous and doesn't require additional contracts" | https://docs.stripe.com/payments/payment-methods | confirmed | No edit |
| 60 | Stripe marks SEPA Direct Debit "Approval required" | https://docs.stripe.com/payments/sepa-debit ; https://docs.stripe.com/payments/bacs-debit | corrected | The words are not on the Payment Methods API page the passage cites. They are the "Access type" on the SEPA and Bacs method pages; sentence and source entries now say so |
| 61 | Adyen names the method in paymentMethod.type, for example sepadirectdebit | https://docs.adyen.com/payment-methods/sepa-direct-debit/api-only | confirmed | No edit |
| 62 | Adyen Advanced flow: "/paymentMethods, /payments, and /payments/details"; the first returns the available methods | https://docs.adyen.com/online-payments/build-your-integration ; https://docs.adyen.com/payment-methods/sepa-direct-debit/api-only | confirmed | No edit |
| 63 | Adyen guide (2024-12-25): request methods in the Customer Area; "we will contact you if there are additional requirements" | https://docs.adyen.com/payment-methods/add-payment-methods | confirmed | Inline link removed |
| 64 | Adyen: adding a method to a store is "an asynchronous process", confirmed by a webhook | https://docs.adyen.com/payment-methods/add-payment-methods | confirmed | No edit (paymentMethod.created webhook) |
| 65 | Stripe prints a "Manual capture support" property on each method page | https://docs.stripe.com/payments/sepa-debit ; https://docs.stripe.com/payments/ideal ; https://docs.stripe.com/payments/wero | hedged | That label is on the iDEAL and Wero pages; the SEPA, Bacs, Bancontact and Pix pages print "Manual capture" under "Payment captures". Sentence and table cell reworded |
| 66 | Adyen capture page (2023-08-29): "Capture timing settings do not apply"; "Most card payment methods use separate capture ... iDEAL, only support direct capture." | https://docs.adyen.com/online-payments/capture | confirmed | Inline link removed; date put in the sentence |
| 67 | Hold to capture: "No material difference in the public record" | https://docs.stripe.com/payments/sepa-debit ; https://docs.adyen.com/payment-methods/sepa-direct-debit | corrected | For SEPA Direct Debit Stripe lists no manual capture, while Adyen lists separate, partial and multiple partial captures. One sentence added; the table cell now says the answer for one scheme can differ |
| 68 | Stripe's French SEPA mandate text names PPRO | https://docs.stripe.com/payments/sepa-debit | confirmed | No edit |
| 69 | "One trace exists" of a method delivered through another payment company; table cells "Not public" for both providers | https://docs.stripe.com/payments/pix ; https://docs.adyen.com/payment-methods/ach-direct-debit | corrected | Stripe's Pix page calls Ebanx "our Pix partner" and says "Ebanx appears as the payment recipient"; Adyen's ACH page mentions "The legacy BOA acquirer" replaced by "AdyenACH". Paragraph, inference block and both table cells rewritten; spec evidence updated |
| 70 | "Neither company has published how it adds a method or which methods it reaches through another payment company" | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | unsupported, relabeled | A negative no source states. Reworded as the author's finding ("I found no page of either company that ..."); index searches for PPRO, Ebanx, partner and acquirer found no list |
| 71 | Adyen offers the methods configured on the merchant account or store | https://docs.adyen.com/payment-methods/add-payment-methods | confirmed | No edit |
| 72 | Stripe: a returned direct debit is a "dispute"; an unpaid debit is a failed payment with a failure code | https://docs.stripe.com/payments/sepa-debit | confirmed | No edit |
| 73 | UK Direct Debit Guarantee: "a full and immediate refund"; no time limit in its text | https://www.directdebit.co.uk/direct-debit-guarantee/ | confirmed | URL changed (old path redirects). Stripe's Bacs sentence "There's no set time limit for customers to file Bacs Direct Debit disputes" added as a second support, and "by choice" reworded |
| 74 | The Direct Debit Guarantee's publisher is Pay.UK | https://www.directdebit.co.uk/direct-debit-guarantee/ | confirmed | Footer: "owned and managed by Pay.UK Limited" |
| 75 | Stripe: most SEPA failures occur within 6 business days | https://docs.stripe.com/payments/sepa-debit | confirmed | No edit |
| 76 | Adyen SEPA chargebacks guide "last modified June 2025" | https://docs.adyen.com/risk-management/chargeback-guidelines/sepa-chargebacks | confirmed | 17 June 2025; day added; inline link removed |
| 77 | Stripe failure code insufficient_funds | https://docs.stripe.com/payments/sepa-debit | confirmed | No edit |
| 78 | Stripe failure code debit_disputed | https://docs.stripe.com/payments/sepa-debit | confirmed | "The customer asked their bank to refund the payment." |
| 79 | Adyen CHARGEBACK event with reason AM04 "Insufficient Funds" | https://docs.adyen.com/risk-management/chargeback-guidelines/sepa-chargebacks | confirmed | No edit |
| 80 | Adyen reason MD06 "Refund Request By End Customer" | https://docs.adyen.com/risk-management/chargeback-guidelines/sepa-chargebacks | confirmed | No edit |
| 81 | Adyen reason MD01 "No Mandate" | https://docs.adyen.com/risk-management/chargeback-guidelines/sepa-chargebacks | confirmed | No edit |
| 82 | Stripe: "For payment methods that require customer action, configure webhook endpoints ..." | https://docs.stripe.com/payments/payment-methods | confirmed | Source named in the sentence |
| 83 | Adyen webhooks page (2026-11-17): "with payment methods like iDEAL, it can take time to get a confirmation that the payment was completed" | https://docs.adyen.com/development-resources/webhooks | confirmed | Inline link removed |
| 84 | Stripe: "If the payment fails after a delay, Stripe immediately deducts the payment amount from your Stripe balance" | https://docs.stripe.com/payments/sepa-debit | confirmed | Source named in the sentence |
| 85 | Stripe: "If you refund while the bank also starts a dispute, the customer can receive two credits" | https://docs.stripe.com/payments/sepa-debit | confirmed | No edit |
| 86 | Adyen: "Shoppers can dispute a payment with their bank even after you've issued a refund, potentially resulting in two credits for the same payment." | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | No edit |
| 87 | Adyen holds SEPA refunds for a week after settlement | https://docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | "one-week holding period for refunds post-settlement" |
| 88 | Adyen API-only integrators had "between January 29, 2026 and March 31, 2026" to rename iDEAL and change its logo | https://docs.adyen.com/payment-methods/ideal | confirmed | No edit |
| 89 | Stripe: "Rebrand your integration in the first quarter of 2026 to iDEAL / Wero" | https://docs.stripe.com/payments/ideal | confirmed | No edit |
| 90 | Stripe's Wero page lists manual capture support | https://docs.stripe.com/payments/wero ; https://docs.stripe.com/payments/payment-methods/overview | hedged | True, but the overview marks Wero "Public preview" and the page lists no dispute support; both added, to keep preview apart from released |
| 91 | Adyen: the immediate flow "is the only Wero flow Adyen supports today" | https://docs.adyen.com/payment-methods/wero | confirmed | Adyen's "Dispute support starts in February 2027" added beside it |
| 92 | Where They Differ, row 1 (what carries the method), both cells | rows 52, 53, 61 | confirmed | No edit |
| 93 | Where They Differ, row 2 (which methods are shown), both cells | rows 56, 57, 71 | confirmed | No edit |
| 94 | Where They Differ, row 3 (turning a method on), both cells | rows 59, 60, 63 | confirmed | No edit |
| 95 | Where They Differ, row 5 (a returned direct debit), both cells | rows 1, 72 | confirmed | No edit |
| 96 | Adyen "last modified" dates in text and sources (2026-11-17, 2026-11-02, 2025-06-17, 2024-12-25, 2023-08-29, 2023-05-08, 2023-04-03) | the .md variant of each Adyen page | confirmed | Each matches the page's front matter. The rendered pages display no date; a line in Sources now says where the dates come from |

Counts: 96 claims; 82 confirmed, 7 hedged, 5 corrected, 1 not checked, 1 unsupported, relabeled.

## Could not verify, and what was done

- **Nacha's ACH rules, the SEPA Direct Debit rulebook, the Pix scheme rules.** Not fetched. The page already declares them as not verified and gives the providers' statements as the providers' statements.
- **PSD3 and the Payment Services Regulation.** No primary source was found for their status. The sentence now reports a law-firm briefing of 24 April 2026 (fetched) as a secondary source. Two web searches on 17 November 2026 found no publication in the Official Journal; later briefings give differing expected dates, so the sentence makes no claim about the state in November.
- **Adyen "last modified" dates.** They come from the front matter of the `.md` variant; the rendered pages display no date. Eleven of the pages read carry the same stamp, 2026-11-17T12:56:39, which looks like a site build time, not an edit to each page. The Apple Pay page is stamped 2023-05-08 but its body says "from 5 Jan 2026", so the stamp can understate how current a page is. The dates were kept as cited, and a line in Sources says where they come from. The author may prefer "n.d., accessed November 2026" for all Adyen documentation pages.
- **"No page says how either company adds a method."** A negative; reworded as the author's finding after searching both documentation indexes.

## Links

All URLs in Sources and Evidence return 200. Three redirect and were replaced by the final URL: Stripe Bacs (`/payments/payment-methods/bacs-debit` to `/payments/bacs-debit`), the Direct Debit Guarantee (`/direct-debit-explained/direct-debit-guarantee/` to `/direct-debit-guarantee/`) and iDEAL (`www.ideal.nl` to `ideal.nl`). One source was added: the A&L Goodbody briefing (secondary). No entry is unused. All `[[permalink]]` links are in the style guide's list; plain "Part I" became `[[part-1]]`.

## Rulings and format

- Ruling 22: every inline external link (30) reduced to plain text with attribution in the sentence; each URL was already in Sources.
- `timetoread` changed from 23 to 24 minutes (5,613 words by `check_draft.py structure`, up from 5,401).
- Terms glossed on first use: payout, settle.
- No unit added, dropped, merged or reordered. In `spec.json` one evidence item was updated (the Ebanx and ACH traces), two redirected URLs were replaced and a changelog entry was added.

## Larkfield consistency

Checked against the ledger: method mix (52, 21, 14, 5 and 4%), fees (0.8% + €0.25 = €0.64 and 1.9% + €0.25 = €1.18 on €49), 325,000 debits and about 4,900 returns a month, Daan Peters (Thursday 1 April 2027; Friday 9 April is six business days later; 27 May 2027; 1 May 2028; €48.36), Femke de Graaf's start in January 2027, Jonas Weber's role, K2 and K7. All agree. Weekdays were checked by script.

## Ledger conflicts

None. One point for the author: Studio Noord is on Adyen in the ledger, and Daan's example leans on Stripe's six-business-day guidance for the wait. It is given as Stripe's statement, so it is not wrong, but the Adyen pages read give no equivalent number.

## For other pages

- A page that says Stripe's or Adyen's use of other payment companies is "not public" should see rows 69 and 70: Ebanx on Stripe's Pix page, PPRO in Stripe's French SEPA mandate text, the "legacy BOA acquirer" on Adyen's ACH page.
- A page that says Wero, like iDEAL, has no disputes should note that Adyen's Wero page announces dispute support (pre-dispute, then chargeback) from February 2027, while Stripe's Wero page (public preview) lists no dispute support.
- A page that gives an Adyen documentation date of 17 November 2026 is citing a site-wide stamp (see above).
