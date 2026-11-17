# Verification — 45-journey-dispute (`journey-dispute`)

Verification pass of 17 November 2026. Every source under Sources and Evidence was fetched in this session: Adyen and Stripe documentation as their `.md` variants (the HTML addresses were also requested and return 200), the two price pages as HTML, and the two Visa PDFs converted to text. Every quotation in the page was matched against the fetched text by script (typographic quotes normalized), before and after the edits; all matched. The page is a journey: each provider fact was also compared with the verified owning chapter (`04-refunds-reversals-and-disputes`, `25-3ds-and-sca`) and rulings 17–37.

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen "debits the payment amount and the chargeback processing fee from your account" when the dispute starts (lead, takeaway) | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | confirmed | — |
| 2 | Stripe "Debits the disputed amount, plus a dispute fee, from your Stripe account." | docs.stripe.com/disputes/how-disputes-work | confirmed | — |
| 3 | Key point: 40 days for a Mastercard at Adyen | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks; docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes | confirmed | Table: "Your response to a Chargeback (from NoC date)", Mastercard 40 |
| 4 | Key point: 18 days "for a Visa card outside the United States and Canada" | docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes | hedged | Adyen ties the 9 days to "payments processed locally in the United States and Canada", not to the card. Now "a Visa payment processed outside the United States and Canada" |
| 5 | Key point: the networks count a dispute whether won or lost | docs.stripe.com/disputes/monitoring-programs | confirmed | Stripe: "monitoring programs don’t consider dispute outcomes"; for Mastercard "regardless of its outcome" |
| 6 | Key point: the dispute was won on 12 May "when that bank's time ran out" | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | hedged | The event means "The issuer either accepted your defense of the dispute, or did not respond in time"; the key point now says both, as the body already did |
| 7 | Key point: Stripe returns money only on a win | docs.stripe.com/disputes/how-disputes-work | confirmed | "Overturns the dispute in your favor … Stripe passes this amount back to you"; otherwise "No money moves from your perspective" |
| 8 | Stripe: "in rare cases the status can change from `lost` to `won`" (three places) | docs.stripe.com/disputes/how-disputes-work | confirmed | — |
| 9 | Strong customer authentication, 3-D Secure, liability shift and exemption as described in one paragraph | PSD2 and RTS (not in this page's Sources) | not checked | Owned and verified by chapter 25 (verification file rows 5–18, 39–43); the wording here agrees with the corrected chapter. Law text not re-fetched for this page |
| 10 | Adyen: "If the exemption is granted, the chargeback liability stays with you." | docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/sca-exemptions | confirmed | Under "TRA exemption request from you or your acquirer"; agrees with chapter 25 row 42 |
| 11 | Adyen reports the request in `additionalData.scaExemptionRequested` | docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/sca-exemptions | confirmed | — |
| 12 | Adyen default: "withdraws the disputed funds from your platform's liable balance account" | docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | — |
| 13 | `deductFromOneBalanceAccount` "Deducts the full amount from the balance account specified in `targetAccount`" | docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | — |
| 14 | `costAllocationAccount` books the chargeback fees to a named balance account | docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | "By default, chargeback fees are booked to your liable balance account" |
| 15 | Adyen: "Use this logic if you want to make your user liable for all chargeback-related events on the payment." | docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | — |
| 16 | Stripe: a dispute on a platform charge debits the "Platform’s balance, with or without `on_behalf_of`" (two places) | docs.stripe.com/connect/disputes | confirmed | Also: "Stripe debits dispute amounts and fees from your platform account" |
| 17 | Mastercard code 4837, No Cardholder Authorization, as Adyen lists it | docs.adyen.com/risk-management/understanding-disputes/dispute-reason-codes | confirmed | 4837 is not one of the codes (4808, 4870, 4871) that skip pre-arbitration, so the losing branch described applies |
| 18 | Adyen: 120 calendar days from the transaction to start a chargeback, Mastercard and Visa | docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes | confirmed | — |
| 19 | Visa: "120 calendar days from the Transaction Processing Date"; edition 24 October 2026 | Visa Core Rules PDF (24 October 2026) | confirmed | Phrase found 9 times in the dispute conditions |
| 20 | `NOTIFICATION_OF_CHARGEBACK`: "This webhook message marks the start of the defense period." | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | confirmed | — |
| 21 | Mastercard: "You must provide your defense documents within **40 days**." | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | — |
| 22 | Stripe Dispute object has `evidence_details.due_by` | docs.stripe.com/api/disputes/object | confirmed | — |
| 23 | No Adyen call returns a dispute's state (pages read) | docs.adyen.com/risk-management/disputes-api; Adyen llms.txt | confirmed | As far as searched: the Disputes API has action endpoints and `/retrieveApplicableDefenseReasons` only |
| 24 | A missed Adyen notification "is found only by comparing open dispute rows with the dispute list in Adyen's Customer Area" | docs.adyen.com/reporting/disputed-transactions | corrected | Adyen documents a daily Dispute transaction details report with a record type per dispute event (NotificationOfChargeback, Chargeback, ChargebackReversed, SecondChargeback …). Sentence corrected; source entry added |
| 25 | Adyen: "The chargeback debit usually occurs a few days after you receive the NoC" | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | — |
| 26 | Adyen publishes no chargeback fee amount (three places) | www.adyen.com/pricing; Adyen llms.txt | confirmed | Pricing page shows chargebacks only as a yes/no feature per payment method; no amount in page or page data |
| 27 | Adyen: "The API request validates only the format of the split instructions, **not** the balance accounts specified in the request." | docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | — |
| 28 | Missing account or closed account holder: "the full transaction and its fees are booked to your platform's liable balance account." | docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | — |
| 29 | Liable balance account: "Funds can be deducted from this account if your users' balance accounts incur negative balances due to refunds and chargebacks." | docs.adyen.com/platforms/account-structure-resources | confirmed | — |
| 30 | No page says how long Adyen waits before deducting from the liable balance account | docs.adyen.com/platforms/account-structure-resources; docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks | confirmed | As far as searched (the two pages cited); a negative statement |
| 31 | Balance Platform Accounting Report "tracks all balance changes on all balance accounts in your balance platform" | docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report | confirmed | — |
| 32 | The report has line types for a chargeback, a chargeback reversal and a second chargeback | docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report | confirmed | `chargeback`, `chargebackReversal`, `secondChargeback` |
| 33 | Stripe: "You can’t issue a refund outside the dispute process while the dispute is open." | docs.stripe.com/disputes/how-disputes-work | confirmed | — |
| 34 | Adyen: "A chargeback fee is charged for every booked chargeback" | docs.adyen.com/risk-management/manage-disputes | confirmed | Agrees with chapter 25 row 126 |
| 35 | Adyen: accept when the amount "does not outweigh the risk of losing the chargeback fee for the second booked chargeback" | docs.adyen.com/risk-management/manage-disputes | confirmed | — |
| 36 | "Adyen automatically defends" fraud chargebacks with a liability shift | docs.adyen.com/risk-management/manage-disputes | hedged | Source: "Examples of chargebacks that can be auto-defended include" …, and wallets are excluded. Brought into line with chapter 4 (its row 82): "lists … among those it can defend automatically", "would probably not have been his" |
| 37 | Adyen: "Submitting the defense documents is irreversible" | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | — |
| 38 | Adyen: "There is no opportunity later in the process to provide information or to update information you provided." | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | The page repeats the sentence with "unless this information was not available before"; left, since the quotation is exact |
| 39 | Stripe: "You’ve only one opportunity to submit your response." | docs.stripe.com/disputes/responding | confirmed | — |
| 40 | Adyen confirms a defense with `INFORMATION_SUPPLIED` | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks; docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | confirmed | — |
| 41 | Adyen: 18 days for Visa, "or 9 for payments processed in the United States and Canada since 21 July 2025" | docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes | hedged | Source: "From 21 July 2025, the response timeframe for disputes opened on payments processed locally in the United States and Canada is 9 days". Reworded (chapter 4 row 44) |
| 42 | Stripe: "usually 7-21 days, depending on the card network" (four places) | docs.stripe.com/disputes/how-disputes-work | confirmed | On "How disputes work", as chapter 4's correction (row 42) requires; Stripe gives no Mastercard-specific figure |
| 43 | Visa gives the acquirer 30 calendar days for its step | Visa Core Rules PDF (24 October 2026) | confirmed | Tables 11-2 and 11-3: "30 calendar days from the Dispute Processing Date" |
| 44 | `DISPUTE_DEFENSE_PERIOD_ENDED` quotation | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | confirmed | — |
| 45 | `CHARGEBACK_REVERSED` credits the amount; "The issuer is still reviewing the defense. If they accept, this is the final status." | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | — |
| 46 | "This stage is not final and a second chargeback can be presented by the issuing bank, resulting in losing the chargeback case" | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | confirmed | — |
| 47 | Mastercard at Adyen: pre-arbitration "within **45 days** of the date that the defense was uploaded" | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | 3 March + 45 = 17 April |
| 48 | "The Pre-Arbitration case is accepted when the response time expires", unless the merchant has arranged to contest | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | Support can decline on request; eligible merchants can decline themselves after configuration |
| 49 | "the dispute is lost, and you receive a second chargeback"; a second chargeback is final | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | "This is the final status." |
| 50 | Arbitration: "a fee of up to USD 600" | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | "If Mastercard rules in favor of the issuer" |
| 51 | `ISSUER_RESPONSE_TIMEFRAME_EXPIRED`: "The issuer either accepted your defense of the dispute, or did not respond in time." | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow | confirmed | — |
| 52 | Adyen's table: 70 days from the defense to the final decision for Mastercard, "longer than the 45 days on its Mastercard page" | docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes; docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | hedged | Both numbers are right but measure different stages (45: issuer files pre-arbitration; 70: final decision). Sentence now says so and that neither page explains the difference |
| 53 | (added) Stripe: the issuer has "usually 60-75 days, depending on the card network" to decide | docs.stripe.com/disputes/how-disputes-work | confirmed | Added so the page gives Stripe's figure for the same stage; Stripe gives no Mastercard-specific number |
| 54 | Whether Adyen returns the fee on a win is not public (scenario assumes not) | docs.adyen.com/risk-management/manage-disputes; docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow; docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks; docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report | confirmed | As far as searched. The accounting report lists fee types "Chargeback Fee", "SecondChargeback Fee" and "ChargebackReversal Fee"; one sentence added, with the cost of a won (€15.00) and a lost (€135.00 or €150.00) defense labeled as illustration |
| 55 | Stripe: "Both networks assign a dispute or fraud report to the month in which they received it …" | docs.stripe.com/disputes/monitoring-programs | confirmed | — |
| 56 | Stripe: "Mastercard calculates the ratio of disputes or fraud to the total number of payments in the previous month" | docs.stripe.com/disputes/monitoring-programs | confirmed | Stripe's description only (chapter 4 row 59); the page attributes it to Stripe |
| 57 | Stripe: "monitoring programs don’t consider dispute outcomes" | docs.stripe.com/disputes/monitoring-programs | confirmed | — |
| 58 | Bram's chargeback sits in February's count against January's payments | docs.stripe.com/disputes/monitoring-programs | confirmed | Stripe's own example: "calculations for February use payments captured in January and chargebacks raised in February" |
| 59 | "Mastercard's first level": 100 to 299 chargebacks and 1.5 to 2.99%, as both providers render it | docs.stripe.com/disputes/monitoring-programs; docs.adyen.com/risk-management/dispute-and-fraud-monitoring | hedged | Numbers confirmed on both pages, but the program was not named and no date was given. Now named (Excessive Chargeback Program, level Excessive Chargeback Merchant) and said to carry no effective date on either page; the Larkfield ratio is marked as all networks, counted as one merchant |
| 60 | (added) A 4837 chargeback also counts in Mastercard's Excessive Fraud Merchant program: fraud chargeback rate 0.50%, USD 50,000 | docs.stripe.com/disputes/monitoring-programs; docs.adyen.com/risk-management/dispute-and-fraud-monitoring | confirmed | Stripe names codes 4837 and 4863; Stripe "greater than 0.50%" and "greater than 50,000 USD", Adyen "50 or more (0.50%)" and "USD or EUR 50,000"; further conditions (1,000 e-commerce payments, 3-D Secure share) not repeated |
| 61 | Stripe: Mastercard counts a chargeback "regardless of whether it was hidden due to a refund" and regardless of liability shift | docs.stripe.com/disputes/monitoring-programs | confirmed | — |
| 62 | Visa: ratio "Excludes disputes resolved through pre-dispute solutions" | Visa VAMP fact sheet PDF (2025) | confirmed | Source continues ", contingent on the timing of the data extract"; left as in chapter 4 |
| 63 | Stripe NL: €40.00 per Mastercard resolution, more than the fee it avoids | stripe.com/en-nl/pricing | confirmed | "€40.00 per Mastercard resolution"; dispute received fee €20.00 |
| 64 | Had the payment been authenticated, the loss "would have been his bank's problem" | docs.stripe.com/payments/3d-secure/authentication-flow (via chapter 25) | hedged | Chapter 25 (rows 50–51): authentication "doesn't guarantee liability shift". Now "would, by the liability shift, have been" |
| 65 | Adyen shows program standing "only on your company account" | docs.adyen.com/risk-management/dispute-and-fraud-monitoring | confirmed | — |
| 66 | (added) Adyen: Visa applies thresholds "for both your merchant account(s) and Adyen" | docs.adyen.com/risk-management/dispute-and-fraud-monitoring | confirmed | Added to the entity question |
| 67 | Stripe: Visa "identifies an account by the static component of its statement descriptor and its acquiring bank" | docs.stripe.com/disputes/monitoring-programs | confirmed | — |
| 68 | Neither company says which entity is counted for a seller on a platform (inference block) | docs.stripe.com/disputes/monitoring-programs; docs.adyen.com/risk-management/dispute-and-fraud-monitoring; docs.stripe.com/connect/disputes; both llms.txt | confirmed | As far as searched: neither monitoring page mentions platforms or connected accounts. For Mastercard both speak only of the account |
| 69 | Stripe: "In extremely rare cases, you might receive more than one dispute per payment" | docs.stripe.com/disputes/how-disputes-work | confirmed | — |
| 70 | Adyen: American Express "can reopen a dispute that was previously closed in your favor" | docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes | confirmed | "In exceptional cases" |
| 71 | Stripe: "These funds are held for the entire duration of the dispute." | docs.stripe.com/disputes/how-disputes-work | confirmed | — |
| 72 | Stripe: "The money moves when the object is created and again when the dispute ends" | docs.stripe.com/disputes/how-disputes-work | hedged | Money returns only on a win; now "and, if the dispute is won, again when it ends" |
| 73 | Stripe: one Dispute object with a `status` | docs.stripe.com/api/disputes/object | confirmed | Ten status values |
| 74 | Stripe NL: €20.00 received, €20.00 countered, the second returned on a win | stripe.com/en-nl/pricing; docs.stripe.com/disputes/how-disputes-work | confirmed | "You get this fee back for won disputes"; "we never return the dispute received fee" unless the contract says otherwise |
| 75 | Stripe destination charges: the amount and the fee leave the platform's balance | docs.stripe.com/connect/disputes | confirmed | — |
| 76 | Stripe: "If you challenge the dispute, wait for the dispute outcome before reversing the transfer." | docs.stripe.com/connect/disputes | confirmed | — |
| 77 | Stripe: "Regardless of a dispute’s outcome, Stripe doesn’t automatically refund the application fee" | docs.stripe.com/connect/disputes | confirmed | — |
| 78 | Adyen books the `CHARGEBACK` event with the debit (step table) | docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks | confirmed | "we send you a CHARGEBACK webhook. At the same time, your account is debited" |
| 79 | Neither company maps its dispute terms to the other's | docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow; docs.stripe.com/disputes/how-disputes-work | confirmed | As far as searched; a negative statement |
| 80 | Mastercard's Chargeback Guide and Transaction Processing Rules could not be read | mastercard.us rule PDFs | unreachable | Not re-fetched here; chapter 4's verification of the same day records HTTP 403 again (its row 89). Every Mastercard figure is cited as Adyen's or Stripe's rendering (ruling 17) |
| 81 | All 21 URLs under Sources and Evidence resolve | each URL | confirmed | HTTP 200 for all, no redirects to a changed address; one entry added (Disputed transactions) |

Totals: 81 claims — 70 confirmed (six of them negative statements, confirmed only as far as searched), 1 corrected, 8 hedged, 0 unsupported, 1 unreachable, 1 not checked at source.

## The Mastercard deadlines, side by side

| Stage | Adyen (page) | Stripe | In the journey |
| --- | --- | --- | --- |
| Merchant's defense | 40 days from the notification (Mastercard chargebacks; Dispute timeframes) | "usually 7-21 days, depending on the card network"; the binding figure is `evidence_details.due_by` | 24 February + 40 = Monday 5 April 2027 |
| Issuer files pre-arbitration | "within **45 days** of the date that the defense was uploaded" (Mastercard chargebacks) | No figure for the issuer. A merchant that enabled appeals has 20 days to answer a Mastercard pre-arbitration (`docs.stripe.com/disputes/arbitration`, read but not cited in the page) | 3 March + 45 = 17 April 2027 |
| Merchant answers pre-arbitration | 8 to 28 days, by reason code (Dispute timeframes, note 6) | 20 days (same Stripe page) | Not used; the branch is hypothetical |
| Final decision | 70 days from the defense date (Dispute timeframes) | "usually 60-75 days, depending on the card network" | 3 March + 70 = Wednesday 12 May 2027 |

The three Adyen figures are consistent with one another; they measure different stages. Mastercard's own text could not be read, so none is checked against the network's rules.

## Could not verify, and what was done

- **Mastercard's rule documents** (row 80): not readable (HTTP 403 in the verification of chapter 4 on the same day; not requested again here). No Mastercard fact is cited from Mastercard.
- **The paragraph on strong customer authentication** (row 9) restates chapter 25 and was compared with that chapter's corrected text, not with the EU texts.
- **Negative statements** (rows 23, 26, 30, 54, 68, 79) are true of the pages cited and of a search of both documentation indexes (`llms.txt`); they cannot be proved.
- **Whether Adyen charges a fee on a chargeback reversal or returns the first fee on a win** is not stated on any page read. The accounting report lists a "ChargebackReversal Fee" type, which shows that such a fee can exist, not that it is charged. The page keeps the ledger's assumption (one €15.00 fee, not returned) and now labels the cost of a won and a lost defense as illustration.
- **"Only prevention lowers a count"** rests on Visa's fact sheet for Visa and on Stripe's price list for Mastercard's resolution product. That a Mastercard resolution keeps a chargeback out of Mastercard's count is stated on Stripe's dispute-prevention page (verified in chapter 4, its row 52), which this page does not cite. Left as written.

## Format and rulings

- Ruling 22: no external URL in the running text (none found). Ruling 17: Mastercard cited through providers. Ruling 23: legacy Custom accounts, destination charges with `on_behalf_of`. Ruling 28: ledger entries from report lines only. Ruling 30: documentation cited "n.d., accessed November 2026". Ruling 20: Silent Webhook 14 September 2026, 9 hours, no weekday named.
- "In Journey 3" in the closing section is now `[[journey-platform-payment]]`, as the other three journeys are linked there.
- `timetoread` changed from 25 to 26 (5,977 words ÷ 230).
- No unit added, dropped, merged or reordered; `check_draft.py structure` passes; `validate_spec.py` passes.
- Render check: one `XJ:` entry, `../agentic-systems-architecture/part-10.html`. `[[part-10]]` is a valid permalink of this book, but `posts/part-10-intro` does not exist yet, so the build resolves the link to another journal's page. It will resolve when Part X's opening page is written; nothing to change here.
- No source is older than three years, so no evidence-age flag is needed.

## Larkfield consistency

Checked against the ledger (general facts and the lines of chapters 4, 5, 12, 15, 25, 33, 35, 44 and 45): Bram de Wit, first purchase, Dutch Mastercard credit card, €120.00, €117.47 and €2.53, €0.73 and €1.80, payout 4 February, check-ins 4 and 11 February, chargeback and €15.00 fee on 24 February, defense 3 March, deadline 5 April, reversal 5 March, pre-arbitration limit 17 April, outcome 12 May 2027, window to 2 June, €135.00 and the second-fee branch, four table rows of ledger entries, 4,900 disputes and €73,500, the €412,000 breakdown, K1–K8, April 2027 authentication rule, Mila's dates in the closing section. All agree. The outcome (won; fee not returned) agrees with what chapter 25's verifier wrote.

Weekdays: 2 February 2027 Tuesday, 4 February Thursday, 24 February Wednesday, 3 March Wednesday, 5 March Friday, 5 April Monday, 12 May Wednesday — all correct. Intervals: 33 days (3 March to 5 April), 9 days (24 February to 5 March), 68 days (5 March to 12 May), three weeks (12 May to 2 June), 120 days (2 February to 2 June) — all correct. Arithmetic: 4,900 ÷ 12 ≈ 408; 408 ÷ 1.2 million ≈ 0.03%; 317,200 + 73,500 + 21,300 = 412,000.

Two figures are not in the ledger but agree with other chapters: 1.2 million online card payments a month (chapter 10) and €64,000 of Studio Noord's paid-out card sales (chapters 35 and 44). Both are labeled assumptions.

## Ledger conflicts

None.

## For other pages

- `04-refunds-reversals-and-disputes` (its sweep paragraph and its "Shape of a dispute" cell) and `20-webhooks-and-events`: Adyen documents a daily **Dispute transaction details report** (`docs.adyen.com/reporting/disputed-transactions`) with a record type per dispute event. "No call that returns a dispute's state" remains true, but the record to sweep open disputes against on Adyen is this report, not only the accounting report or the Customer Area.
- `04-refunds-reversals-and-disputes`, `25-3ds-and-sca`: Adyen's Balance Platform Accounting Report lists fee types "Chargeback Fee", "SecondChargeback Fee" and "ChargebackReversal Fee". Any page that says a second fee is only an inference from "every booked chargeback" can cite this.
- `04-refunds-reversals-and-disputes`: its monitoring table names Mastercard's level but not the program (Excessive Chargeback Program), and omits the Excessive Fraud Merchant program, in which Stripe says fraud chargebacks under codes 4837 and 4863 are counted.
- Part X opening page (`part-10-intro`) is missing; until it exists `[[part-10]]` links from this page to another journal.

## For the author

- The scenario assumes one €15.00 fee, charged with the chargeback and never returned. Adyen's report format allows a fee on the reversal too. If the author wants the won case to show two fees (€30.00), the ledger line of `45-journey-dispute` and chapter 25 change with it.
