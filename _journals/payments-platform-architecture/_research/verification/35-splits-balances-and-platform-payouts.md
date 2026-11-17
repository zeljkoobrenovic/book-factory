# Verification — 35-splits-balances-and-platform-payouts (`splits-balances-and-platform-payouts`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Adyen documentation through the `.md` variants; the two Stripe guides that have per-integration variants were read in the `platform=web` variants). Quotations were compared as strings after normalizing typographic quotes, markdown link markup, code ticks and white space. "Not public" statements were tested against `docs.adyen.com/llms.txt` and the full corpus `docs.adyen.com/llms-full.txt` (68 MB, searched for "negative balance", "Managed Risk", "cross-border").

Short source names: **S/…** = `docs.stripe.com/connect/…`; **A/…** = `docs.adyen.com/platforms/…`.

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Key point: Stripe derives the bookings from the charge type; Adyen takes typed split instructions | S/charges; A/online-payments/split-transactions | confirmed | — |
| 2 | Adyen: internal transfer "moves funds between balance accounts within your platform. For comparison: a payout is an *external* funds transfer" | A/internal-fund-transfers | confirmed | Inline link removed (ruling 22) |
| 3 | Stripe instant payouts "deliver funds before the dispute window closes" | S/instant-payouts | confirmed | The source continues after "closes" with a comma; the full stop was moved outside the quotation marks |
| 4 | A card payment can be disputed for about 120 days (key point, "until about 7 July 2027", exposure figure) | Visa rules, cited in chapter 4 | not checked | No source for the 120-day rule is listed on this page. The sentence now points to `[[refunds-reversals-and-disputes]]` for the rule and its source; chapter 4's verification file records it as confirmed. The date agrees with the ledger |
| 5 | Stripe: "The type of charge you create determines how the funds are distributed …" | S/charges | confirmed | — |
| 6 | Charge-type table, direct charge row (lands in connected account; application fee to platform; fee payer by configuration) | S/charges; S/direct-charges-fee-payer-behavior | confirmed | — |
| 7 | Charge-type table, destination row, with "A portion of the funds immediately transfers to the connected account’s balance" | S/charges | confirmed | — |
| 8 | Charge-type table, separate charges and transfers row | S/charges | confirmed | — |
| 9 | "You create a charge on your connected account, so the payment appears in the connected account’s balance, not in your platform’s balance" | S/charges | confirmed | — |
| 10 | "You can choose whether to have Stripe debit fees directly from connected accounts or from your platform account." | S/charges | confirmed | — |
| 11 | Destination charge: "the full charge amount is immediately transferred … then transferred back to the platform." | S/destination-charges | confirmed | — |
| 12 | Worked example: 10.00 USD, 1.23 USD fee, 0.59 USD Stripe fees, 0.64 USD remains | S/destination-charges | confirmed | — |
| 13 | `on_behalf_of` makes the connected account "the business of record for the payment" | S/charges | confirmed | — |
| 14 | "Transfer and charge amounts don’t have to match." | S/separate-charges-and-transfers | confirmed | — |
| 15 | "The `transfer_group` only identifies associated objects. It doesn’t affect any standard functionality." | S/separate-charges-and-transfers | confirmed | — |
| 16 | A transfer fails by default when it exceeds the available balance; "Stripe doesn’t automatically retry failed transfer requests." | S/separate-charges-and-transfers | confirmed | — |
| 17 | Adyen: balance account per seller, liable balance account for the platform; `splits` array on payment, capture or refund | A/online-payments/split-transactions; A/account-structure-resources | confirmed | — |
| 18 | "If you do not specify an `account` in your split instructions, the split amount is booked to your liable balance account." | A/online-payments/split-transactions | confirmed | — |
| 19 | Split configuration profile on a store; catch-all rule: "any transaction that doesn't match a specific rule will be booked to your liable balance account by default." | A/automatic-split-configuration | confirmed | "store" glossed |
| 20 | Split-type table (BalanceAccount, Commission, PaymentFee, Interchange, SchemeFee, AdyenCommission, AdyenMarkup) and which need an amount | A/online-payments/split-transactions | confirmed | — |
| 21 | "Transaction fees refer to the costs … By default, these costs are deducted from your liable balance account" | A/online-payments/transaction-fees | confirmed | — |
| 22 | Processing costs "are aggregated and also applicable to refused and cancelled payments. Therefore, they cannot be allocated to individual payments." | A/online-payments/transaction-fees | confirmed | — |
| 23 | Description of blended and Interchange++ pricing | owned by chapter 5 | not checked | General description, not a company quotation; a one-clause gloss of "blended" was added because the term is used later for Larkfield's Stripe rate |
| 24 | Troubleshooting note: "The API request validates only the format of the split instructions, **not** the balance accounts … booked to your platform's liable balance account." | A/online-payments/split-transactions/split-chargebacks (same text on split-refunds) | confirmed | — |
| 25 | "No error is returned"; the whole amount goes to "the liable balance account" | A/…/split-chargebacks; A/manage-liable-accounts | hedged | Another Adyen page names the destination as a "reserved incorrect splits account" (one of three kinds of liable balance account) and adds suspended accounts and missing capabilities. One sentence added; source added |
| 26 | Transfer webhooks; the Balance Platform Accounting Report "tracks all balance changes on all balance accounts in your balance platform, including liable accounts and the accounts of your users." | A/reports-and-fees/balance-platform-accounting-report; A/…/split-refunds | confirmed | — |
| 27 | Refund of a destination charge: "by default the destination account keeps the funds …" | S/destination-charges | corrected | The page attributed the quotation to the charges page; it is in the destination charges guide. Attribution fixed |
| 28 | `reverse_transfer=true` pulls the share back; `refund_application_fee=true` returns the fee; by default the platform keeps the fee | S/destination-charges | confirmed | — |
| 29 | Refund table: balance debited per charge type; "You can reverse the transfers …"; `pending`, fails after 45 days with `insufficient_funds` | S/charges; S/separate-charges-and-transfers | confirmed | — |
| 30 | Dispute: "with or without `on_behalf_of`, your platform balance is automatically debited for the disputed amount and fee." | S/charges | confirmed | — |
| 31 | "If you challenge the dispute, wait for the dispute outcome before reversing the transfer." | S/disputes | confirmed | — |
| 32 | "Regardless of a dispute’s outcome, Stripe doesn’t automatically refund the application fee" used for charges made on the platform | S/disputes; S/direct-charges-fee-payer-behavior | hedged | Both pages state it under the direct-charges heading ("to the connected account"). The sentence now says the guide addresses the fee only under direct charges |
| 33 | Adyen refund split lets the platform "choose who is liable for the refund." | A/…/split-refunds | confirmed | — |
| 34 | "Refunds can only be deducted from the balance accounts to which the payment was credited" | A/…/split-refunds | confirmed | — |
| 35 | Refund without a split: profile, platform default, capture ratio for a full refund of one capture; "In all other cases … liable balance account."; marked as pilot | A/how-adyen-applies-split-instructions | confirmed | — |
| 36 | Chargeback default: "Adyen withdraws the disputed funds from your platform's liable balance account"; "can change this behavior by booking …" | A/…/split-chargebacks | confirmed | — |
| 37 | `platformChargebackLogic`: three behaviors, `targetAccount`, `costAllocationAccount` (default the liable balance account) | A/…/split-chargebacks | confirmed | — |
| 38 | "both providers leave the platform standing behind" a seller's negative balance | S/account-balances; A/account-structure-resources | corrected | On Stripe it depends on the account: the balances page says the responsible party is `stripe` or `application`. Sentence scoped: by default on Adyen, on Stripe wherever the platform is responsible |
| 39 | Stripe transfer-reversal condition: "It’s only possible to reverse a transfer if the connected account’s available balance is greater than the reversal amount or has connected reserves enabled" | S/separate-charges-and-transfers (section "Reverse transfers") | confirmed | Verbatim. A clause now says what a connected reserve is (S/account-balances). The disputes guide adds: "If Stripe is responsible for the connected account’s negative balances, a transfer reversal can fail when the account has insufficient available funds", which agrees with the exception |
| 40 | "no page I read says how long a seller's balance account may stay negative before the liable account is debited" | A/manage-liable-accounts; A/reconciliation-use-cases/verify-balances | corrected | **Adyen documents it.** "Adyen allows negative balances for up to 30 days. If a balance account has a negative balance for more than 30 days, Adyen compensates this by debiting your reserved compensation account on the first day of the following month." A warning webhook is sent by default after 20 days. Paragraph rewritten; two sources added |
| 41 | "none describes an arrangement in which Adyen bears the loss" | A/managed-risk | corrected | **Adyen documents one.** Managed Risk ("Limited availability … in pilot phase"): Adyen will "assume the responsibility for negative balances on their accounts" and writes them off after the balance "has remained negative for 180 days after their last captured payment". Sentence rewritten; source added |
| 42 | Recovery table: "If at all possible, Stripe automatically offsets negative transactions against future payments" | S/account-balances | confirmed | — |
| 43 | Recovery table: Adyen settlement is net of the day's refunds and chargebacks | A/settle-funds | confirmed | — |
| 44 | Recovery table: `debit_negative_balances`, in listed countries | S/account-balances | confirmed | — |
| 45 | Recovery table: Adyen top-up by direct debit from the verified bank account | A/top-up-balance-account | confirmed | Inline link removed |
| 46 | Recovery table: transfer reversal; account debits require "legally binding consent" | S/account-debits | confirmed | — |
| 47 | Recovery table: Adyen internal funds transfer | A/internal-fund-transfers | confirmed | — |
| 48 | Recovery table: Stripe reserve on the platform; transfer after 180 days | S/account-balances; S/risk-management | confirmed | — |
| 49 | Recovery table: "Funds can be deducted from this account if your users' balance accounts incur negative balances due to refunds and chargebacks" | A/account-structure-resources | confirmed | The 30-day rule added to the cell |
| 50 | Stripe payout `interval`: manual, daily, weekly, monthly | S/manage-payout-schedule | confirmed | — |
| 51 | `delay_days` "reflects how long it takes …"; override "to a number up to 31" where the platform owns fraud and dispute liability | S/manage-payout-schedule | confirmed | — |
| 52 | "While an account’s balance is negative, you can’t send payouts to the account’s bank or debit card on their behalf." | S/account-balances | confirmed | — |
| 53 | "Adyen settles a settlement batch after its sales day ends … does not affect this timing" | A/settle-funds | confirmed | "settle" and "settlement delay" glossed |
| 54 | Managed payout schedules were announced in a release note of 20 May 2026 | docs.adyen.com/release-notes/platforms-and-financial-products | confirmed | The entry is headed "2026-05-20 — Configuration API": "You can now automate fund payouts … with managed payout schedules". The `.md` front matter of the managed-payouts documentation page carries `last_modified: 2022-04-20`; under rulings 25 and 30 that stamp is not a date, the page stays "n.d." and the release note keeps its displayed date. No change to the text |
| 55 | Standard "two business days after capture", Accelerated one; weekdays, weekly or monthly; minimum, maximum and retained amounts | A/managed-payouts | confirmed | — |
| 56 | A sweep: schedule, trigger amount, amount to leave behind | A/custom-payouts/scheduled-payouts | confirmed | — |
| 57 | "Platforms can add funds to their balance from a bank account" | S/top-ups | confirmed | — |
| 58 | "General availability: USA, UK, Japan" and "Private preview: EU, Canada, Australia, New Zealand" | S/top-ups | corrected | The facts are right, but the page quoted table cells as running strings with a colon the source does not have. Rewritten so only the cell texts are in quotation marks |
| 59 | Adyen top-up: "A top-up refers to …"; "To cover negative balances resulting from refunds or chargebacks"; "If needed, you can also top up your liable balance account." | A/top-up-balance-account | confirmed | — |
| 60 | "Platforms based in the US, UK, EEA, Canada, or Switzerland can transfer funds …"; supported funds flows | S/connect-cross-border-payouts | confirmed | URL changed: `/connect/cross-border-payouts` redirects (301) to `/connect/connect-cross-border-payouts`; Sources entry and title updated |
| 61 | "You must have a separate balance platform for each region in which you acquire payments" | A/account-structure-resources | confirmed | — |
| 62 | Managed payout schedules cover "local payouts (within the same country and currency)" only | A/managed-payouts | confirmed | — |
| 63 | "Neither set of pages lists every corridor, and Adyen's cross-border payout page could not be read as text" | A/custom-payouts | corrected | There is no separate cross-border page in Adyen's index; cross-border payouts are documented, readable, on the custom payouts page (correspondent banks; "The arrival time of the payout cannot be guaranteed"; a table of countries, currencies and priorities). Sentence replaced; source added |
| 64 | Direct charge: "Refunds and chargebacks reduce the connected account’s balance" | S/charges | confirmed | — |
| 65 | Destination charge: "Refunds and chargebacks reduce your platform’s balance" | S/charges | confirmed | — |
| 66 | Separate charges and transfers: "Use [them] only if your business use case requires them" | S/charges | confirmed | The page's ellipsis stands for "them" |
| 67 | Stripe recommends them "only when you’re responsible for negative balances of your connected accounts." | S/separate-charges-and-transfers | confirmed | — |
| 68 | Where They Differ, row 1 (how a payment is divided) | as 5–20 | confirmed | — |
| 69 | Where They Differ, row 2: Stripe's fee is "reported on the balance transaction" | docs.stripe.com/api/balance_transactions/object | hedged | True (`fee`, `fee_details`), but no listed source said so. Cell now names the `fee` field; source added |
| 70 | Where They Differ, row 3 (refund after payout) | as 27–35 | confirmed | — |
| 71 | Where They Differ, row 4 (chargeback booking) | as 30–37 | confirmed | — |
| 72 | Where They Differ, row 5, Stripe cell: for "a split naming a wrong account", "A transfer fails with an error and is not retried" | S/separate-charges-and-transfers; S/account-balances | corrected | The sources document failure for lack of available balance, not for a wrong account. Row label and cell reworded to what is documented |
| 73 | Where They Differ, row 6 (basis of payout timing) | as 51, 53 | confirmed | — |
| 74 | Refund with `reverse_transfer`: "a proportional amount of the transfer" is reversed | S/destination-charges | confirmed | — |
| 75 | "If the refund request also attempts a transfer reversal, but the connected account has an insufficient balance, the refund request returns an error …" applied to Larkfield | S/charges; S/separate-charges-and-transfers | hedged | Quotation confirmed. Larkfield bears its studios' losses (ruling 23), so the connected-reserves exception of claim 39 may apply; the pages do not say which rule governs a reversal sent with a refund. The paragraph now says so and has Larkfield handle both outcomes |
| 76 | Adyen: "To correct the balances, you can transfer the funds between the balance accounts" | A/…/split-chargebacks | confirmed | — |
| 77 | "Stripe doesn’t automatically retry failures … You must explicitly attempt the transfer again." | S/account-balances | confirmed | — |
| 78 | "If your platform’s balance is still insufficient 45 days after you create the refund, the refund fails with a `failure_reason` of `insufficient_funds`." | S/charges | confirmed | — |
| 79 | "You get the outcome of the refund request asynchronously, in a REFUND webhook." | A/…/split-refunds | confirmed | — |
| 80 | Reversing before a won dispute "can have unexpected results"; "If your platform has an insufficient balance, the transfer fails." | S/disputes | confirmed | — |
| 81 | Adyen books a chargeback reversal and a second chargeback by the logic set on the payment | A/…/split-chargebacks | confirmed | Paraphrase of "You can change this behavior …", which follows the sentence naming all three events |
| 82 | "if a connected account’s balance remains negative for 180 days, we transfer funds from the platform reserve to cover the negative amount." | S/risk-management | confirmed | — |
| 83 | "Adyen publishes none [no date] that I found." | A/manage-liable-accounts | corrected | See claim 40: 30 days, debited at the start of the next month. Sentence replaced |
| 84 | Take-away bullets (Established) | as 1, 21, 24, 30, 36 | confirmed | — |

Counts: 84 claims; 70 confirmed, 8 corrected (27, 38, 40, 41, 58, 63, 72, 83), 4 hedged (25, 32, 69, 75), 0 unsupported, 0 unreachable, 2 not checked (4, 23).

## Links

All 26 URLs in Sources and Evidence returned 200. One redirected and was replaced (claim 60). Five sources were added, each returning 200: `docs.adyen.com/platforms/manage-liable-accounts`, `…/platforms/reconciliation-use-cases/verify-balances`, `…/platforms/managed-risk`, `…/platforms/custom-payouts`, `docs.stripe.com/api/balance_transactions/object`. Six source titles were corrected to the titles the pages display. All 20 inline external links were reduced to plain text with the attribution in the sentence (ruling 22); every URL was already in Sources. The twelve `[[permalink]]` targets are in the style guide's list.

## Could not verify, and what I did

- **The 120-day card dispute window** (claim 4): this page lists no source for it. I did not re-fetch the Visa rules; the sentence now points to chapter 4, whose verification file records the rule as confirmed.
- **Whether a refund with `reverse_transfer=true` fails or leaves the connected account negative when the platform bears losses** (claim 75): Stripe's pages give an unconditional error on one page and a connected-reserves exception on another. Not resolvable from documentation; the page states both.
- **Stripe guides with variants**: the destination-charges and separate-charges guides serve an index at the plain `.md` URL; I read the `platform=web` variants (stripe-hosted; custom flow with Payment Intents). The quoted passages are the same in both variants I fetched of the second guide.

## Larkfield consistency

Checked against the ledger: 31.4 million payments in 2026; €412,000 and €317,200 (year-end 2025); the pre-Keel nightly job; Femke de Graaf from January 2027; Mila's pass (Tuesday 9 March 2027, 19:42, €120.00, €117.47, €2.53, €0.61, €1.92); payout Thursday 11 March, marked arrived 25 March; dispute window about 7 July; refund of €84.00 on 18 March; €212.40 (ruling 26); Stripe version €0.87 and €1.66 at 0.6% + €0.15; destination charge with `on_behalf_of` (ruling 23); K3 accounts; five business days and Priya Raman; €16,000 a month, €64,000 and €156 million. One fix: "Thursday's payout is smaller by €84.00" became "the studio's next payout" (the ledger's wording; 18 March is itself a Thursday, and that day's payout carries Tuesday's sales).

## Ledger conflicts

None.

## For other pages

- `33-platform-payment-models`: lines 185, 213 and 277 say the provider as loss bearer is documented only for Stripe ("any other arrangement: Not public"; "Whether Adyen ever bears the loss depends on terms the public record does not show"). Adyen's documentation page "Adyen Managed Risk" (`docs.adyen.com/platforms/managed-risk`, n.d., accessed November 2026; marked limited availability, pilot) says Adyen will "assume the responsibility for negative balances" and write them off after 180 days. Chapter 33 owns the liability rule (ruling 7) and should be corrected; a ruling may be needed.
- `14-payouts-and-money-movement` cites Adyen's managed payouts page as n.d., which agrees with this page.

## Rulings and format

Front matter complete; `timetoread` set to 26 (6,005 words ÷ 230). Three key points; callouts in order; required sections present. No units added, dropped, merged or reordered. In `spec.json` the evidence and controlling ideas of p20, p23, p26, p27, p38 and p43 were brought in line with the corrections, and two open questions that the pass answered were removed. The page is now about 500 words over the 5,500 aim and under the 6,500 limit.
