# Verification — 44-journey-platform-payment (`journey-platform-payment`)

Verification pass of 17 November 2026. Every source below was fetched in this session with `curl` (Adyen and Stripe documentation as `.md` variants; Stripe's destination-charges and account-capabilities pages through their variant URLs `?platform=web&ui=elements` and `?accounts-namespace=v1`, because the bare `.md` returns only an index of variants; Adyen's pricing page as HTML). Quotations were compared with the fetched text by script (typographic quotes, markdown emphasis and link brackets aside); paraphrased claims were read in context by hand. This is a journey page: each provider fact was also compared with the chapter that owns it (13, 14, 33, 35, 12, 15, 4) and with rulings 18–37. No verification file existed yet for chapters 33 and 35, so their current text was used.

Abbreviations: A = `https://docs.adyen.com`, S = `https://docs.stripe.com`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen `receivePayments`: "Allows users to receive payments using a payment method" | A/platforms/verification-overview/capabilities | confirmed | — |
| 2 | Adyen `sendToTransferInstrument`: "Allows users to transfer funds to verified bank accounts" | same | confirmed | — |
| 3 | "The capability can only be used when it is both allowed and enabled."; Adyen sets one switch, the platform the other | same | confirmed | — |
| 4 | Stripe: "A capability must be active for a connected account to perform actions associated with that capability." | S/connect/account-capabilities (v1 variant) | confirmed | — |
| 5 | Adyen: standard "30-day period" for `sendToTransferInstrument`, "60-day period" for `receivePayments`; "their capabilities will be disallowed" | A/platforms/verification-overview | hedged | The page says Adyen "may set a deadline" and lists these as standard deadlines; the "disallowed" sentence is about users who do not resolve issues in time. Sentence reworded to say exactly that. |
| 6 | Adyen: a split naming a balance account of a closed account holder books "the full transaction and its fees" to the liable balance account | A/platforms/online-payments/split-transactions/split-payments-at-authorization; A/…/split-refunds | confirmed | The page attributed it to "split pages" and listed only the split-refunds page. The same sentence is on the authorization page, which is the one that applies to the payment; attribution and a source entry added, and "does not exist" added as the source's first case. |
| 7 | Adyen `BalanceAccount`: "Books a part of the transaction to your user's balance account" | A/platforms/online-payments/split-transactions | confirmed | — |
| 8 | Adyen `Commission`: "Books your platform's commission to your liable balance account" | same | confirmed | — |
| 9 | Stripe: "the full charge amount is immediately transferred … then transferred back to the platform." | S/connect/destination-charges (variant) | confirmed | — |
| 10 | Split table, Stripe cells: `transfer_data[destination]`, `on_behalf_of`, `application_fee_amount` | same | confirmed | — |
| 11 | Adyen answers "Authorised" (`resultCode`) | A/…/split-payments-at-authorization | confirmed | — |
| 12 | Adyen: "The API request validates only the format of the split instructions, **not** the balance accounts … not credited to/deducted from the specified balance account." | same; A/…/split-refunds | confirmed | Attributed to the authorization page. |
| 13 | Confirming records: transfer webhooks and the Balance Platform Accounting Report, which "tracks all balance changes on all balance accounts in your balance platform, including liable accounts and the accounts of your users" | A/…/split-payments-at-authorization; A/platforms/reports-and-fees/balance-platform-accounting-report | confirmed | — |
| 14 | Adyen: "Transaction fees refer to the costs … By default, these costs are deducted from your liable balance account" | A/platforms/online-payments/transaction-fees | confirmed | — |
| 15 | Adyen: "Adyen automatically updates the request to include the **PaymentFee** split type, deducting all transaction fees from your platform's liable balance account." | same | confirmed | — |
| 16 | A split can name who bears each fee type | same (fee split types table) | confirmed | — |
| 17 | Stripe, destination charges: "Stripe debits fees from your platform’s balance" | S/connect/charges | confirmed | — |
| 18 | Stripe, direct charges: "You can choose whether to have Stripe debit fees directly from connected accounts or from your platform account." | same | confirmed | — |
| 19 | Stripe balance transaction: `fee` field; `available_on` | S/api/balance_transactions/object | confirmed | — |
| 20 | Adyen: processing costs "are aggregated and also applicable to refused and cancelled payments. Therefore, they cannot be allocated to individual payments." | A/platforms/online-payments/transaction-fees | confirmed | — |
| 21 | Adyen: "Adyen settles a settlement batch after its sales day ends and the configured settlement delay has passed. The date when the schemes … does not affect this timing." | A/platforms/settle-funds | confirmed (agrees with ruling 18) | — |
| 22 | Adyen's accounting report shows a booking date and a value date | A/…/balance-platform-accounting-report | confirmed | — |
| 23 | Stripe's Dutch schedule: 3 business days | S/payments/balances ("Netherlands, 7 calendar days, 3 business days") | confirmed | — |
| 24 | Adyen payout webhooks, `booked`: "This status is not final." | A/platforms/payout-webhooks | confirmed | — |
| 25 | Stripe: "Some payouts that fail might initially show as `paid`, then change to `failed`." | S/api/payouts/object | confirmed | — |
| 26 | Adyen: splitting a refund "allows you to choose who is liable for the refund." | A/…/split-refunds | confirmed | — |
| 27 | Refund request table: Adyen refund on the PSP reference with a `splits` item; Stripe `reverse_transfer`, `refund_application_fee` | A/…/split-refunds; S/connect/destination-charges | confirmed | — |
| 28 | Adyen: a refund without instructions "reuses the capture's ratio only when it refunds a whole capture"; "In all other cases, such as for refunds of partial captures, we book the full refund amount to your platform's liable balance account."; logic in pilot | A/platforms/how-adyen-applies-split-instructions | hedged | The page checks a split configuration profile and a default refund logic of the balance platform before the capture's ratio. Sentence now gives that order; Larkfield is said to have neither *(illustration)*. Quote and pilot mark confirmed. |
| 29 | "A partial refund like Mila's, sent bare, would have been Larkfield's €84.00 on either provider." | same; A/…/split-refunds | hedged | True on Stripe and on Adyen under the pilot logic. For platforms outside the pilot the split-refunds page describes the "previous logic" only for refunds equal to the original amount. Sentence scoped. |
| 30 | Stripe: "by default the destination account keeps the funds that were transferred to it, leaving the platform account to cover the negative balance from the refund." | S/connect/destination-charges | confirmed | — |
| 31 | Adyen: "Refunds can only be deducted from the balance accounts to which the payment was credited." | A/…/split-refunds | confirmed | — |
| 32 | Stripe: "Stripe debits your platform balance for the refund amount. You can reverse the transfers made to your connected accounts to recover your refund cost." | S/connect/charges | confirmed | — |
| 33 | Stripe: "a proportional amount of the transfer is reversed" | S/connect/destination-charges | confirmed | — |
| 34 | Stripe, direct charges: "Stripe debits the refund amount from the connected account’s balance directly" | S/connect/charges | confirmed | — |
| 35 | Stripe: "by default the platform account keeps the funds from the application fee"; "you refund a proportional amount of the application fee" | S/connect/destination-charges | confirmed | — |
| 36 | Adyen refund `Commission` item: "deducts the amount of your platform's commission for the original payment from your liable balance account" | A/…/split-refunds | confirmed | — |
| 37 | "The provider's own cost does not come back on either" | S/refunds; A/…/split-refunds | hedged | Stripe says its "processing fees from the original transaction aren’t returned". No Adyen page read says so; the split-refunds page lists fee items for the refund itself, by default deducted from the liable balance account. Sentence now says that. |
| 38 | Adyen: "You get the outcome of the refund request asynchronously, in a REFUND webhook" | A/…/split-refunds | confirmed | — |
| 39 | Adyen: a successful REFUND webhook means "we sent the refund request to the card scheme. However, the card scheme can still reject the refund. This can happen even a few days after you submit the refund request." | A/online-payments/refund | confirmed | — |
| 40 | Stripe: a refund against a short balance stays `pending` and "fails with a `failure_reason` of `insufficient_funds`" after 45 days; the Refund object has a status | S/connect/charges; S/refunds | confirmed | — |
| 41 | Adyen's "payment API has no call that returns a payment by its identifier" | rulings 12 and 29 (verification of chapter 8) | hedged | Scoped to "Checkout API for online payments" as ruling 29 requires. Not re-fetched here; rests on chapter 8's verification. |
| 42 | Adyen: "Liable balance account: the account where your business' funds are held. Funds can be deducted from this account if your users' balance accounts incur negative balances due to refunds and chargebacks." | A/platforms/account-structure-resources | confirmed | — |
| 43 | Stripe: "If the refund request also attempts a transfer reversal, but the connected account has an insufficient balance, the refund request returns an error instead of creating a refund with `pending` status." | S/connect/charges | confirmed | — |
| 44 | Stripe: "With a direct charge the studio's connected account is debited and goes negative." | S/connect/charges; S/refunds | corrected | The charges page says of direct charges: "If the connected account’s balance is insufficient, we set the refund status to `pending`", failing after 45 days. A refund does not drive the balance negative. Text now says the refund is held pending and that a balance can still go negative by another route (a chargeback), which is where the risk page's order applies. Chapter 35's table already says this. |
| 45 | Stripe: "Stripe first attempts to offset the negative amount by collecting funds from the account’s external account" | S/connect/risk-management | confirmed | — |
| 46 | Stripe: reserve on the platform's balance; "if a connected account’s balance remains negative for 180 days, we transfer funds from the platform reserve to cover the negative amount." | same | confirmed | — |
| 47 | Shortfall table, row "Stripe, direct charge": "It goes negative; Stripe tries the studio's bank account" | S/connect/charges | corrected | Cell now reads "The refund waits as `pending` for up to 45 days"; the last cell is scoped to a balance that does go negative. Step-table row 9 changed the same way. |
| 48 | Shortfall table, Adyen row and Stripe destination row | rows 31, 40, 42, 43 | confirmed | — |
| 49 | Adyen's documentation describes "no arrangement in which Adyen takes a seller's loss" | A/platforms/managed-risk | corrected | Adyen documents Managed Risk ("Limited availability … in pilot phase"): Adyen will "assume the responsibility for negative balances on their accounts", with write-offs after 180 days. Paragraph rewritten; source added. Agrees with chapter 35. |
| 50 | Adyen's documentation describes "no period a balance account may stay negative before the liable balance account is debited" | A/platforms/manage-liable-accounts; A/platforms/reconciliation-use-cases/verify-balances | corrected | "Adyen allows negative balances for up to 30 days. If a balance account has a negative balance for more than 30 days, Adyen compensates this by debiting your reserved compensation account on the first day of the following month." Quoted in the paragraph; source added. Agrees with chapters 33 and 35. |
| 51 | Adyen publishes "no price list for platforms" | https://www.adyen.com/pricing | corrected (source) | The cited page (A/platforms/get-started) says nothing about prices. Replaced by Adyen's pricing page, which lists prices per payment method and says "Other Adyen products, besides payment methods, are priced separately." (the source chapter 33 uses). The claim is now worded as what was not found. |
| 52 | Adyen settles net of the day's refunds | A/platforms/settle-funds | confirmed | — |
| 53 | Stripe: "If at all possible, Stripe automatically offsets negative transactions against future payments." | S/connect/account-balances | confirmed | — |
| 54 | Adyen: internal transfers between the liable balance account and a user's balance account | A/platforms/internal-fund-transfers | confirmed | — |
| 55 | Adyen top-up, first listed use: "To cover negative balances resulting from refunds or chargebacks" | A/platforms/top-up-balance-account | confirmed | — |
| 56 | Adyen: "for euro accounts" users "must first accept a mandate that authorizes you to debit their accounts" | A/platforms/top-up-balance-account/on-demand-top-ups | hedged | The source says "from bank accounts in the SEPA zone using SEPA Direct Debit". Reworded to "bank accounts in the SEPA zone (the Single Euro Payments Area)". |
| 57 | Adyen's recommended mandate text: "You must claim a refund within 8 weeks from the date your account was debited" | same | confirmed | — |
| 58 | Stripe: "a platform's own debits of a connected account require 'legally binding consent'", in a passage about debiting the studio's bank account | S/connect/account-debits; S/connect/risk-management | hedged | Account Debits debit the connected account's Stripe balance, not its bank account; the bank debit is Stripe's own collection from the external account. Sentence and two table cells now separate the two. Quote confirmed. |
| 59 | Stripe: a transfer reversal recovers the refund cost | S/connect/charges | confirmed | — |
| 60 | Step table, record cells for both providers (rows 1–8, 10, 11) | rows above | confirmed | — |
| 61 | Decisions paragraph: Adyen books "the bare partial refund of step 7" to the liable balance account | row 29 | hedged | "under its pilot logic" added. |
| 62 | Take-away: on Adyen, when the liable account is debited and whether anyone else bears the loss "depends on terms the public record does not show" | rows 49, 50 | corrected | Bullet now gives the documented default and the 30 days, and leaves access to the pilot and prices as the unpublished part. |
| 63 | Take-away, Established bullets; key point 2 | rows 12, 14, 24, 25, 31, 39 | confirmed | — |
| 64 | Ledger section: on Adyen the balance platform's daily report per studio; on Stripe the balance transactions behind each payout | A/…/balance-platform-accounting-report; chapter 15 | confirmed | Ruling 32 applied: the report is named, with Adyen's mark "**Required** for full financial reconciliation" (A/platforms/reports-and-fees) and the `balancePlatform.report.created` signal (A/platforms/prepare-reports/generate-download-reports); both read today and added to Sources. |
| 65 | "Scheme is Adyen's word for a card network" | A/platforms/settle-funds; A/online-payments/refund | confirmed (usage) | — |
| 66 | Dispute window "until about 7 July 2027" | ledger line `01-journey-of-a-payment` | not checked against Visa's rules | Ledger arithmetic (120 calendar days from 9 March 2027 = 7 July 2027, recomputed). Now labeled as the author's arithmetic in the sentence. |

Counts: 66 rows. 51 confirmed, 6 corrected (44, 47, 49, 50, 51, 62), 8 hedged (5, 28, 29, 37, 41, 56, 58, 61), 0 unsupported, 0 unreachable, 1 not checked against a primary source (66).

## The author's arithmetic, recomputed

- Larkfield's fee: 1.9% × €120.00 + €0.25 = €2.53; studio €117.47. Correct.
- €2.53 − €0.61 = €1.92; Stripe's assumed rate 0.6% × €120.00 + €0.15 = €0.87; €2.53 − €0.87 = €1.66. Correct.
- €12.00 a class; seven classes €84.00; three classes €36.00. Correct.
- €84.00 ÷ €120.00 = 70%; on Stripe the transfer is €120.00 (the full charge), so the proportional reversal is 70% × €120.00 = €84.00. Correct; the sentence now shows the two steps and is labeled "by my arithmetic".
- €117.47 − €84.00 = €33.47. Correct; already labeled.
- Proportional fee refund 70% × €2.53 = €1.771, "about €1.77". Correct; now labeled "*(my arithmetic: 70% of €2.53)*".
- Exposure: €16,000 × 4 months = €64,000. Correct.
- Weekdays: 9 March 2027 Tuesday, 10 March Wednesday, 11 March Thursday, 12 March Friday, 18 March Thursday, 25 March Thursday. Correct. 25 March is the tenth business day after 11 March.

## Could not verify, and what was done

- **Chapters 33 and 35 had no verification file** when this page was checked. Their current text was used; on the three points where the journey disagreed with them (rows 44, 49, 50) the provider's page was fetched and chapter 35 was right.
- **Row 41** rests on rulings 12 and 29, not on a fetch in this session.
- **Row 66** is the ledger's arithmetic; Visa's rules were not read for this page.
- **Stripe variant pages.** `docs.stripe.com/connect/destination-charges.md` and `…/account-capabilities.md` return an index of variants. The quotations were confirmed in the "Custom flow" web variant and the Accounts v1 variant. The URLs in Sources are the canonical pages, which return 200.
- **Absence claims.** "No price list for platforms" was checked against Adyen's pricing page and the documentation index (`docs.adyen.com/llms.txt`); an absence cannot be proven beyond that.

## Links

All 30 URLs under Sources and Evidence return HTTP 200 with no redirect to a different page. One entry removed (Get started with Adyen for Platforms: nothing in the text rests on it). Six added: Split payments at authorization, Manage liable balance accounts, Adyen Managed Risk, Reports and fee types, Get platform reports, Adyen Pricing. All `[[permalink]]` links are in the style guide's list. No external URL in the running text (ruling 22).

## Format and rulings

- Ruling 26: the covered refund is booked owed-to-studio / funds-at-provider, with €212.40 in Studio Noord's balance; "to recover from studio" appears only as the counterfactual row. Already correct; unchanged.
- Ruling 28: the page said "Larkfield's nightly reconciliation job". Changed to a job that runs once per provider on that provider's report-ready signal. Entries were already described as written from report lines, not webhooks.
- Ruling 29: row 41. Ruling 30: all documentation cited "n.d., accessed 2026-11"; one sentence added near the top saying both providers' documentation quoted in the chapter is undated and was read in November 2026, since most later quotations carried no date.
- Ruling 32: row 64. Ruling 33: nothing on this page touches the status facts (a)–(f). Ruling 18: row 21 agrees. Ruling 23: destination charges with `on_behalf_of`; agrees.
- Terms glossed on first use: dispute window, chargeback, capture, SEPA.
- `timetoread` changed from 24 to 26 (5,929 words ÷ 230).
- No "Where They Differ" section (journey page). No unit added, dropped, merged or reordered; paragraph p27 keeps its place and function with corrected content. Spec strings updated to match; validation, the structure check, the build and the render check pass.

## Larkfield consistency

- **Payout wording.** The lead said the €117.47 "went to its bank account a week earlier"; now "was paid out to". Step 6 now says the payout is sent on 11 March, in the best case lands that day, and that `arrived` on 25 March is a state of Larkfield's record (the day it stops expecting a return), not the date of the credit. The ledger-table row reads "Payout marked arrived".
- All other figures, names, dates and titles agree with the ledger and with chapters 12, 14, 15 and 35 (ledger entries, accounts, five business days, €412,000 and €317,200, 230 studios and 12 days, €156 million).
- One local detail added: Larkfield has no split configuration profile and no default refund logic on Adyen *(illustration)*, needed for row 28.

## Ledger conflicts

- None. The ledger line for this page says "payout 11 March, arrived 25 March"; it is consistent when "arrived" is read as the record state, as the page now says.

## For other pages

- **`journal-spec.json`** (entry for this page) and therefore this page's `spec.json` at `intent.outcome.know[3]` and the expected answer of acceptance criterion AC-1 still say that Adyen publishes "no option for the provider to take a seller's loss, no waiting period before the liable account is debited", and that with a Stripe direct charge the connected account "is debited and goes negative". Both are wrong against the sources (rows 44, 49, 50). They could not be changed here: the validator requires them to equal the journal spec, which this pass may not write. Supporting claim S4 and the section and paragraph units in `spec.json` were corrected.
- **`33-platform-payment-models`**, line 185: "the provider bears the seller's losses … The public record documents it only for Stripe." Adyen documents Managed Risk as a pilot (row 49); chapter 35 already says so.
- **`35-splits-balances-and-platform-payouts`** says the negative balance is compensated "from the platform's liable account". Adyen's two pages differ in wording: "Manage liable balance accounts" names the reserved compensation account (one of the platform's three liable accounts), "Verify balances" says "your balance platform's liable account". Not an error; chapter 33 uses the more precise wording.

## For the author

- The journal spec's entry for this page needs the two corrections above; after that, `intent.outcome.know[3]` and AC-1 in this page's spec can be brought into line.
- The page is now 5,929 words, above the 5,500 aim and under the 6,500 limit. The growth is the corrected Adyen paragraph, the hedges and six source entries.
