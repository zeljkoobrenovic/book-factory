# Verification — 04-refunds-reversals-and-disputes (`refunds-reversals-and-disputes`)

Verification pass of 17 November 2026. Every source below was fetched in this session (Stripe and Adyen documentation as their `.md` variants, the two Visa PDFs converted to text, PSD2 from the Publications Office). Quotations were matched against the fetched text by script (typographic quotes normalized) and the misses read by hand. Short names: S = docs.stripe.com, A = docs.adyen.com, VCR = Visa Core Rules PDF (`usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf`, edition 24 October 2026), VAMP = Visa fact sheet PDF.

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Visa rules edition is 24 October 2026 | VCR title page | confirmed | — |
| 2 | "120 calendar days from the Transaction Processing Date" for most disputes | VCR, dispute time-limit tables (10.1–10.4, 12.x, 13.x) | confirmed | — |
| 3 | 75 days for the authorization conditions | VCR Tables 11-39, 11-44, 11-50 (11.1–11.3) | confirmed | — (12.7 is also 75 days; the sentence does not say otherwise) |
| 4 | 13.1: "120 calendar days from the last date that the Cardholder expected to receive…", "Not to exceed 540 calendar days…" | VCR, condition 13.1 time limit and footnote 4 | confirmed | — |
| 5 | Glossary: Authorization Reversal "A V.I.P. System message that cancels an Approval Response" | VCR glossary | confirmed | — |
| 6 | Glossary: Credit Transaction quotation | VCR glossary | confirmed | — |
| 7 | Glossary: Dispute "A Transaction that an Issuer returns to an Acquirer" | VCR glossary | confirmed | — |
| 8 | Glossary: Arbitration quotation | VCR glossary | confirmed | — |
| 9 | Glossary: Rapid Dispute Resolution quotation | VCR glossary | confirmed | — |
| 10 | Glossary: Compelling Evidence quotation | VCR glossary | confirmed | — |
| 11 | Rule effective 24 April 2027: issuer must reconcile credits and debits and dispute only the net amount | VCR Tables 11-2 and 11-3 ("Submit the Dispute only for the resulting net disputed amount") | confirmed | — |
| 12 | Four categories 10 Fraud, 11 Authorization, 12 Processing Errors, 13 Consumer Disputes | VCR Tables 11-2, 11-3 | confirmed | — |
| 13 | Condition names 10.4, 11.3, 12.6, 13.1, 13.2, 13.6 | VCR section 11 | confirmed | — |
| 14 | Categories 12/13: acquirer's Dispute Response, then issuer's pre-arbitration; categories 10/11: acquirer's answer is the pre-arbitration attempt | VCR Tables 11-2, 11-3 | confirmed | — |
| 15 | Acquirer has 30 calendar days for its step (inference block) | VCR Tables 11-2, 11-3 ("30 calendar days from the Dispute Processing Date") | confirmed | — |
| 16 | "Visa Claims Resolution" not in the current rule text | VCR full-text search: 0 hits | confirmed | — (Adyen's Visa page still uses the name) |
| 17 | Stripe: cancel "before it's completed at no cost" | S /refunds | confirmed | — |
| 18 | Adyen: "After a payment has been captured, you can no longer cancel it." | A /online-payments/cancel | confirmed | — |
| 19 | Adyen: "You can only refund a payment after it has been captured." | A /online-payments/refund | confirmed | — |
| 20 | Stripe: outcome "is at the sole discretion of the account owner's bank"; Stripe "facilitates your case, but doesn't have influence over the outcome" | S /disputes/how-disputes-work | confirmed | — |
| 21 | Stripe: refunds use available balance; pending for cards, other methods fail; fails after 45 days with `insufficient_funds` | S /refunds | confirmed | Date added to the sentence |
| 22 | Adyen failure reason `Insufficient in-process funds on account` | A /online-payments/refund | confirmed | Date added |
| 23 | Adyen: "The refund process is asynchronous"; `REFUND` `success: true` means "we sent the refund request to the card scheme"; rejection "can happen even a few days after…"; `REFUND_FAILED` | A /online-payments/refund | confirmed | — |
| 24 | Stripe Refund statuses `pending`, `requires_action`, `succeeded`, `failed`, `canceled` | S /api/refunds/object | confirmed | — |
| 25 | Stripe: failed refund's money can take up to 30 days to return | S /refunds | confirmed | — |
| 26 | Stripe: dispute lifecycle "can take 2-3 months" | S /disputes/how-disputes-work | confirmed | — |
| 27 | Stripe: "Stripe's processing fees from the original transaction aren't returned" | S /refunds | confirmed | — |
| 28 | Adyen price list has a column "Payment method refund fee" | https://www.adyen.com/pricing (page data) | confirmed | — |
| 29 | Adyen: "up to 40 business days…" | A /online-payments/refund | confirmed | — |
| 30 | Stripe: refund seen "approximately 5-10 business days later, depending upon the bank" | S /refunds | confirmed | — |
| 31 | Stripe: early refunds "appear in the form of a *reversal*…the original charge drops off the customer's statement" | S /refunds | confirmed | Source has a glossary tooltip inline; wording otherwise identical |
| 32 | Adyen reversal: "If you are not sure if a payment has been captured…"; cancels if uncaptured, refunds if captured | A /online-payments/reversal | hedged | The page lists limitations the chapter omitted: no reversal after multiple partial captures or when the payment carries split data. One sentence added; source entry updated |
| 33 | Adyen: cancel by own reference "up to 24 hours after authorization" | A /online-payments/cancel | confirmed | — |
| 34 | Stripe: "You can't issue a refund outside the dispute process while the dispute is open" | S /disputes/how-disputes-work | confirmed | — |
| 35 | Adyen: refunded payments "can be auto-defended if more than 90 percent…" | A /risk-management/manage-disputes | confirmed | — |
| 36 | Adyen timeframes: 120 and 540 days for Visa and Mastercard | A /risk-management/understanding-disputes/dispute-timeframes (last modified 4 Nov 2026) | confirmed | — |
| 37 | Mastercard codes 4837, 4808, 4834, 4853 as Adyen lists them | A …/dispute-reason-codes, Mastercard section | confirmed | 4808 is listed as "4802 / 4808" |
| 38 | Adyen: Visa flows Allocation (fraud, authorization) and Collaboration (consumer, processing) | A …/visa-chargebacks | confirmed | — |
| 39 | Adyen's Mastercard stages (seven, in the order given) | A …/mastercard-chargebacks | confirmed | — |
| 40 | Stripe: retrieval phase "Mastercard and Visa no longer use" | S /disputes/how-disputes-work | confirmed | — |
| 41 | Stripe: "You've only one opportunity to submit your response" | S /disputes/responding | confirmed | — |
| 42 | Stripe: "usually 7-21 days, depending on the card network" | S /disputes/how-disputes-work | corrected | The chapter attributed this to the page on responding; it is on "How disputes work". Sentence now names the right page |
| 43 | Dispute object: `evidence_details.due_by`, `charge`, `balance_transactions` | S /api/disputes/object | confirmed | — |
| 44 | Adyen: Visa deadline 18 days, 9 in US and Canada since 21 July 2025 | A …/dispute-timeframes, …/visa-chargebacks | hedged | Source limits the 9 days to "payments processed locally in the United States and Canada"; wording added |
| 45 | Adyen: Mastercard "within **40 days**. There is no opportunity later…" | A …/mastercard-chargebacks | confirmed | — |
| 46 | Later stages only for eligible businesses that enabled them | S /disputes/arbitration; A …/dispute-process-and-flow | hedged | Sentence did not say whose rule; now states both (Stripe: enable appeals; Adyen: configuration and approval) |
| 47 | Stripe: CE 3.0 "automatically evaluates your transaction history…" for Visa 10.4 | S /disputes/responding | confirmed | — |
| 48 | Stripe: friendly-fraud definition | S /disputes/prevention/fraud-types | confirmed | — |
| 49 | Adyen NoF: "This is not a dispute, and no money is withdrawn from your account." | A …/dispute-process-and-flow | confirmed | — |
| 50 | Stripe EFWs: TC40 and SAFE; "about 40%…become fraud disputes"; "Proactively refunding…doesn't affect the fraud warning." | S /disputes/how-disputes-work | confirmed | — |
| 51 | Adyen RDR: "is resolved through a refund and does **not** become a chargeback" | A …/visa-chargebacks | confirmed | — |
| 52 | Stripe "integrates directly with Verifi and Ethoca"; resolved disputes not counted, no received fee | S /disputes/prevention-preview | confirmed | — |
| 53 | Verifi is Visa's, Ethoca Mastercard's | https://stripe.com/en-nl/pricing ("Verifi from Visa and Ethoca from Mastercard"); A …/visa-chargebacks ("a company that Visa acquired") | confirmed | Source entry for the price page now says it supports this |
| 54 | Stripe NL: "€20.00 per Visa resolution", "€40.00 per Mastercard resolution" | https://stripe.com/en-nl/pricing | confirmed | Sentence now says "its price page lists" |
| 55 | VAMP ratio formula; card-not-present; monthly | VAMP | confirmed | Acronym expanded at first use |
| 56 | VAMP merchant: ≥150 bps from 1 April 2026 (≥220 before), ≥1,500 cases, AP/Canada/EU/US | VAMP (footnotes 4, 5); A …/dispute-and-fraud-monitoring agrees | confirmed | The sheet writes "EU" for Visa's Europe region; chapter's "Europe" kept |
| 57 | VAMP acquirer: Above Standard ≥50 bps, Excessive ≥70 bps | VAMP | confirmed | — |
| 58 | Mastercard ECM 100–299 chargebacks and 1.5–2.99% | S /disputes/monitoring-programs; A …/dispute-and-fraud-monitoring | confirmed | — |
| 59 | Mastercard counts this month's chargebacks over last month's payments | S /disputes/monitoring-programs only | corrected | The cell credited Stripe and Adyen; Adyen's page does not describe the calculation. Cell now marks it as Stripe's description |
| 60 | Stripe: programs "don't consider refunds", "don't consider dispute outcomes"; "counted twice for the VAMP count" | S /disputes/monitoring-programs | confirmed | — |
| 61 | Visa: ratio "Excludes disputes resolved through pre-dispute solutions" | VAMP | confirmed | Source adds "contingent on the timing of the data extract" |
| 62 | PSD2 Art. 77 "for a period of 8 weeks…"; Art. 71 "no later than 13 months after the debit date"; Art. 76 unconditional right for direct debits | http://publications.europa.eu/resource/celex/32015L2366 | confirmed | — |
| 63 | PSD2 "is in force" | EUR-Lex status page | unreachable | EUR-Lex returned a bot challenge (HTTP 202, empty). Law-firm briefings of 2026 found by search (secondary) say PSD3 and the Payment Services Regulation have a transition of about 21 months after publication, so PSD2 still applies. Claim kept; see below |
| 64 | Stripe SEPA: "You can't submit evidence or counter…"; 8 weeks / 13 months; called a dispute | S /payments/sepa-debit | confirmed | Date added |
| 65 | Adyen SEPA: "You cannot defend SEPA chargebacks."; notification can mean "There were insufficient funds…" | A /payment-methods/sepa-direct-debit | confirmed | — |
| 66 | Stripe iDEAL: "Customers can't dispute iDEAL \| Wero payments with their bank." | S /payments/ideal | confirmed | Date added |
| 67 | Stripe LPMs: provider decides; "up to 180 days to file a dispute" | S /disputes/how-disputes-work | confirmed | — |
| 68 | Stripe: disputed amount "might be lower or higher…"; "more than one dispute per payment" | S /disputes/how-disputes-work | confirmed | — |
| 69 | Adyen: multiple partial refunds up to the captured amount | A /online-payments/refund | confirmed | Source: "supported for some payment methods" |
| 70 | Adyen refund webhook carries `originalReference` and `pspReference` | A /online-payments/refund | confirmed | — |
| 71 | Stripe NL fees: €20.00 received; €20.00 countered, returned on a win; received fee not returned | https://stripe.com/en-nl/pricing; S /disputes/how-disputes-work | confirmed | — |
| 72 | Stripe: "It's likely not worthwhile to refund EFWs on charges more than 35 percent higher than your dispute fee." | S /disputes/how-disputes-work | confirmed | — |
| 73 | Table: Stripe Dispute `status` values `needs_response`, `under_review`, `won`, `lost` and six others | S /api/disputes/object (ten values) | confirmed | — |
| 74 | Table: Adyen event codes; Disputes API is actions only, no call returning a dispute's state | A …/dispute-process-and-flow; A /risk-management/disputes-api; Adyen's public OpenAPI file for the Disputes API (five POST paths, no GET) | confirmed | — |
| 75 | Table: Stripe "Debits the disputed amount, plus a dispute fee" at creation | S /disputes/how-disputes-work | confirmed | — |
| 76 | Table: Adyen "Depending on the payment method, the chargeback debit happens a few days after you receive the NoC, or after you defend the dispute" | A …/dispute-process-and-flow | confirmed | — |
| 77 | Table: "Stripe passes this amount back to you" on a win | S /disputes/how-disputes-work, /disputes/responding | confirmed | — |
| 78 | Table: Adyen `CHARGEBACK_REVERSED` "This stage is not final…"; Allocation amount "will not be immediately transferred back" | A …/dispute-process-and-flow; A …/visa-chargebacks | confirmed | — |
| 79 | Table: Adyen debits a "chargeback processing fee"; amount not public | A …/dispute-process-and-flow; https://www.adyen.com/pricing (no chargeback fee amount in the page or its data); A llms.txt searched | confirmed | Only a scheme-arbitration fee "of up to USD 600" is documented |
| 80 | Table: Stripe late win, `lost` can become `won` | S /disputes/how-disputes-work | confirmed | — |
| 81 | Adyen platforms: "withdraws the disputed funds from your platform's liable balance account"; other bookings possible | A /platforms/online-payments/split-transactions/split-chargebacks | confirmed | Date added |
| 82 | Adyen defends liability-shifted fraud chargebacks automatically | A /risk-management/manage-disputes | hedged | Source says such chargebacks "can be auto-defended" (examples; wallets excluded). "defends … automatically" changed to "lists such chargebacks among those it can defend automatically" |
| 83 | Chargeback Reversed is final when the issuer accepts or its time runs out | A …/dispute-process-and-flow | confirmed | — |
| 84 | Stripe: "These funds are held for the entire duration of the dispute." | S /disputes/how-disputes-work | confirmed | — |
| 85 | Stripe Connect: connected account's balance for direct charges, platform's otherwise | S /connect/disputes | confirmed | Date added |
| 86 | Stripe refund failure reason `charge_for_pending_refund_disputed` | S /api/refunds/object | confirmed | — |
| 87 | Adyen's payment API has no call that returns a payment by its identifier (ruling 12) | Adyen's public OpenAPI file for Checkout v71: GET exists only for payment links, sessions and stored payment methods | confirmed | — |
| 88 | Adyen: payment accounting report shows failed and reversed refunds | A /online-payments/refund | confirmed | — |
| 89 | Mastercard's own rules not readable | mastercard.us Chargeback Guide and Transaction Processing Rules PDFs | unreachable | HTTP 403 again. Chapter already cites every Mastercard fact through Stripe or Adyen (ruling 17); no change |

Totals: 89 claims checked — 81 confirmed, 2 corrected, 4 hedged, 0 unsupported, 2 unreachable.

## Links

All 30 URLs under Sources and Evidence return HTTP 200. The PSD2 URL (`publications.europa.eu/resource/celex/32015L2366`) resolves by content negotiation: 200 with a browser `Accept` header or `application/xhtml+xml`, 404 with a bare `Accept: text/html`. Kept, as it is the book-wide form. All `[[permalinks]]` are in the style guide's list; the render check reports `[[journey-dispute]]` and `[[meet-larkfield]]` as unresolved only because those pages are not written yet.

## Rulings and format

- Ruling 22: 29 inline external links reduced to plain text; each URL was already under Sources and Evidence. A sentence in the roadmap paragraph now dates all Stripe, Adyen and Visa statements (November 2026; Visa edition of 24 October 2026), and dates were added to the first attribution in sections that had none.
- Rulings 15 and 17 were already applied. Ruling 20: the Silent Webhook carries its date only. Ruling 12 checked (claim 87).
- "Keel" is now glossed at first use. `timetoread` 28 min matches 6,359 words ÷ 230.
- "The two services' own pages could not be read" (Verifi, Ethoca) changed to "This chapter does not cite the two services' own pages": ethoca.com answers 200, and no claim rests on either site.

## Could not verify

- **PSD2's status on EUR-Lex** (claim 63). The directive's text was read; its "in force" marker was not. Kept on the strength of secondary sources. The author may want a clause on PSD3 and the Payment Services Regulation once their publication date is confirmed.
- **Mastercard's rules** (claim 89). Still 403.

## Larkfield consistency

Checked against the ledger: Mila's pass (Tuesday 9 March 2027, paid out Thursday 11 March, window to about 7 July), the €84.00 refund of 18 March, Bram de Wit's dispute (2 February, chargeback 24 February, €15.00 illustrative fee, check-ins 4 and 11 February, defense 3 March, 40-day deadline 5 April, window to 2 June, €135.00 loss), the €412,000 breakdown (€317,200, €73,500, 4,900 disputes), 21% direct debit, 52% of €910M × 120/365 ≈ €156M, the Silent Webhook (14 September 2026, 9 hours), K2 and K3. All agree; weekdays match dates.

## Ledger conflicts

None found.

## For other pages

- None. (Ledger line `33-platform-payment-models` says Larkfield sets `platformChargebackLogic` to `deductFromOneBalanceAccount`; this chapter's "the platform can book the amount elsewhere" is consistent with it.)

## For the author

- The chapter is 6,359 words against the style guide's ceiling of 6,500. No cut was made in this pass.
