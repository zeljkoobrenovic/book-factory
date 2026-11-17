# Verification — 13-balances-and-funds-flows (`balances-and-funds-flows`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Adyen documentation as `.md` variants, Adyen's terms page and Stripe's support article as HTML). All double-quoted strings in the article were matched mechanically against the fetched texts (typographic quotes, markdown and whitespace normalized), then read in context. Short URLs: S = `https://docs.stripe.com`, A = `https://docs.adyen.com`, T = `https://www.adyen.com/legal/sales-day-payout-terms-of-service`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen terms: pays "irrespective of whether the funds are actually received by Adyen" (lead, key point 2) | T, clause 1.1 | confirmed | — |
| 2 | Adyen "pays you on a net basis… from which we deduct" transaction costs, refunds, chargebacks, other adjustments | A/account/getting-paid | confirmed | Inline link removed (ruling 22) |
| 3 | Stripe "When a customer initiates a refund or files a dispute, funds are also deducted from the payments balance." | S/payments/balances | confirmed | Inline link removed |
| 4 | Adyen step 1: "A payment is captured, and the card scheme or payment method sends the funds to Adyen." | A/account/getting-paid | confirmed | — |
| 5 | Networks settle net; acquirer receives one amount and commonly pools it; four-party table | none (industry practice, worded "commonly"; owned by ch. 3 and 16) | not a documented claim | — |
| 6 | Stripe account "can have one or more balances that hold funds for different products and currencies" | S/payments/balances | confirmed | Inline link removed |
| 7 | Stripe has a payments balance, a refunds and disputes balance funded in advance, a reserve balance Stripe creates | same | confirmed | — |
| 8 | Stripe pending: "…the charge amount (minus Stripe’s fee) appears in your pending balance until settlement." | same | confirmed | — |
| 9 | Stripe "After the funds settle, they move to your available balance." | same | confirmed | — |
| 10 | Balance transaction fields `amount`, `fee`, `net`, `type`, `source`, `status`, `available_on`, `created`, `exchange_rate` | S/api/balance_transactions/object | confirmed | Attribution with date added in the sentence |
| 11 | "You can calculate the net impact of a transaction on a balance by `amount` - `fee`" | same | confirmed | — |
| 12 | `status` "either `available` or `pending`" | same | confirmed | — |
| 13 | `available_on`: "The date that the transaction’s net funds become available in the Stripe balance." | same | confirmed | — |
| 14 | Sigma example-query comment: "the canonical record of changes to your Stripe balance" | S/data/data-freshness | corrected (URL and title) | `S/stripe-data/available-data` redirects to `S/data/data-freshness`, titled "Sigma data freshness"; source entry and spec updated; Sigma glossed as Stripe's SQL reporting product |
| 15 | Inference block: Stripe described a two-sided (double-entry) ledger in 2024 | https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement (dated 2024.2.16 on the page) | confirmed | Source entry added (the fact was cited without one). Under three years old, no evidence-age flag |
| 16 | Stripe: "Settlement time is the time between when a payment or a funding transaction is made and when the funds become available in your Stripe balance." | S/payments/balances | confirmed | — |
| 17 | Stripe schedule: US 2 business days; NL, DE, BE, UK 7 calendar days initial ("applies to your first payout") and 3 business days default | same, country table | confirmed | — |
| 18 | SEPA Direct Debit 6 business days | same, payment method table | confirmed | — |
| 19 | "These payments have a higher risk of returns or reversals, which factors into their longer settlement periods." | same | confirmed | — |
| 20 | Type list includes `refund`, `stripe_fee`, `reserve_hold`, `payout`, `transfer`, `adjustment`; a dispute is an `adjustment` with the dispute as source | S/reports/balance-transaction-types; S/api/balance_transactions/object | confirmed | Inline link removed |
| 21 | "When a customer disputes a charge, Stripe deducts the disputed amount from your balance." | S/reports/balance-transaction-types | confirmed | — |
| 22 | "Your account might have fees debited from your balance on a daily or monthly basis." | S/payments/balances | confirmed | — |
| 23 | Adyen: "The funds are assigned to a payable batch… Adyen instructs the payout to you." | A/account/getting-paid | confirmed | Inline link removed |
| 24 | Sales day payout is the default model; "You get all the funds from a particular sales day in a single payout batch, with a fixed payout delay." | A/account/sales-day-payout | confirmed | Inline link removed |
| 25 | Sales day is midnight to midnight in the account's time zone unless configured | same; T clause 1.1(b) | confirmed | — |
| 26 | "The payout delay is calculated to be the break-even point…" | A/account/sales-day-payout | confirmed | — |
| 27 | 2 business days when at least 80% is in one of eight currencies acquired in-region; 3 otherwise | same | hedged | The table has a third row (3, 7 or 12 business days for accounts onboarded through a partner); added in parentheses |
| 28 | A scheme that "has a settlement delay of 7 days" lengthens the delay | same (the example is American Express) | confirmed | — |
| 29 | "Refunds, chargebacks, and other adjustments are added to the payable batch as they occur and are not related to the sales day of the original transaction." | same | confirmed | — |
| 30 | "Each month, Adyen gives you a Payment processing invoice"; "There can be a difference… Adyen will credit or debit the difference to the next settlement batch" | A/reporting/invoice-reconciliation/payment-processing-invoice | confirmed | Inline link removed |
| 31 | Adyen available funds is a sum including "Pending: …" and "Next payout: …" | A/account/balances | confirmed | Inline link removed |
| 32 | "The other parts of Adyen's sum are buffers and holds" | same | corrected | The page lists Pending, Next payout, Reserve and Negative refund allowance as the sum; the Deposit (the hold) is a second, separate balance type. Sentence rewritten to say so |
| 33 | Platforms: "Adyen settles a settlement batch after its sales day ends and the configured settlement delay has passed. The date when the schemes or payment methods transfer the funds to Adyen does not affect this timing." | A/platforms/settle-funds | confirmed | Attribution with date added; inline link removed |
| 34 | Accounting report: "The booking date is when the event (like a payment) took place, and the value date is when…" | A/platforms/reports-and-fees/balance-platform-accounting-report | confirmed | The page cited the `/marketplaces/` copy; the `/platforms/` copy has the same sentence and matches "Adyen for Platforms", so the source entry and spec now point to it |
| 35 | Terms: "initiate payout of the Net Captured Volume to Merchant on the Payout Day, irrespective of…"; "Last update 17 June 2024" | T | confirmed | Inline link removed |
| 36 | "Adyen prefinances your payments. When Adyen settles… while settlement is still pending." | A/account/sales-day-payout/upgrade-to-sdp | confirmed | Inline link removed |
| 37 | "Prefinancing is capped at 30 days… SettledReversed and RefundNotCleared entries." | same | confirmed | — |
| 38 | Money that arrives later is booked again | same ("you see an additional Settled booking") | confirmed | — |
| 39 | Platforms: "If Adyen does not receive the funds within 30 days after a payment's capture, we subtract those funds from the current settlement batch." | A/platforms/settle-funds | confirmed | — |
| 40 | `SETTLED_REVERSED` and `REFUND_NOT_CLEARED` "apply to all payment methods and are disabled by default" | A/account/sales-day-payout; settlement details report page | confirmed | — |
| 41 | Late or unpredictable payment methods are excluded and paid on receipt | T clause 2.1.2 | confirmed | — |
| 42 | "If more than 25% of the Captured Volume on a sub-account…" | T | confirmed | — |
| 43 | Activation subject to Adyen's review | T clause 1.3.1 | confirmed | — |
| 44 | Pass-through payout pays on receipt; "the only available payout model in Africa, Brazil, and India" | A/account/pass-through-payout (model); A/account/getting-paid and A/account/sales-day-payout (quote) | hedged (attribution) | The quoted words are on the Getting paid and Sales day payout pages, not on the Pass-through page the link pointed to; sentence now attributes them to "Adyen's documentation" and the Getting paid entry lists them |
| 45 | Stripe Instant Payouts: "Card payment funds are available immediately… Bank debit funds (ACH, SEPA) are only included after they fully settle…" | S/payouts/instant-payouts | confirmed | Attribution rewritten without the link |
| 46 | "When platforms and marketplaces are liable for losses, you’re liable for uncovered negative balances…" | S/connect/instant-payouts | confirmed | Attribution rewritten without the link |
| 47 | Stripe's balances, payouts and Connect balance pages give the schedule and use no term such as pre-financing | S/payments/balances, S/payouts, S/connect/account-balances (grep for prefund, pre-fund, prefinanc, advance, card network: no hits); also S/payouts/next-day-settlement, the payout schedules FAQ and `S/llms.txt` | confirmed (absence, as far as searched) | — |
| 48 | "the list of balance transaction types has no entry described as taking back an advance that the network never settled" | S/reports/balance-transaction-types | hedged | True as worded, but the list has `payment_reversal`: "Created when a debit/failure related to a payment is detected from a banking partner. This balance transaction takes funds that were previously credited to the merchant for a payment out of the merchant balance." The sentence now quotes it and says what it leaves open; the movement table cell names it |
| 49 | No public source says whether `available_on` waits for network settlement | as 47; S/payouts says "T" is "the time of the original payment confirmation or capture" | confirmed (absence) | — |
| 50 | Settlement details report is created when a payable batch closes | A/account/getting-paid | confirmed | Inline link removed; date added |
| 51 | Journal types `Refunded`, `Chargeback`, `SecondChargeback`, `Fee`, `InvoiceDeduction`, `DepositCorrection`, `SettledReversed`, `CaptureFailed`, `ReserveAdjustment` and what each means | A/reporting/settlement-reconciliation/transaction-level/settlement-details-report, "Journal types" | confirmed | — |
| 52 | Stripe types `reserve_hold`, `reserved_funds`, `payout_minimum_balance_hold`, `stripe_fee` and what each means | S/reports/balance-transaction-types | confirmed | — |
| 53 | "A reserve is a temporary hold on a portion of a business’s funds for a predetermined period of time"; two types, fixed and rolling | https://support.stripe.com/questions/reserves-frequently-asked-questions | confirmed | The page is client-rendered; the text was read from the article body embedded in the HTML. Title in the source entry set to the page's own |
| 54 | Adyen deposit: "Unlike the reserve, you cannot determine your own deposit amount. Adyen calculates the deposit requirement for your account daily…" | A/account/balances | confirmed | — |
| 55 | "Automatic payouts only pay out funds exceeding this minimum balance to your bank account." | S/payouts/minimum-balances-for-automatic-payouts | confirmed | Inline link removed |
| 56 | Adyen reserve: "the available amount you configure to cover for refunds, chargebacks, and other operational expenses" | A/account/balances | confirmed | — |
| 57 | "if you receive 100 USD in payments but refund 200 USD…"; a payout that debits the bank account; "a Payout object with a negative `amount`" | S/payouts, "Negative payouts" | confirmed | Date added; inline link removed |
| 58 | An account property says whether Stripe or the platform covers a negative balance | S/connect/account-balances | confirmed | Inline link removed |
| 59 | "Stripe holds a reserve on your platform account’s `available` balance"; "When a connected account holds a negative balance amount for 180 days, Stripe transfers a portion of your balance to zero out that account’s balance" | same | confirmed | — |
| 60 | A connected account with a negative balance cannot be paid out | same ("you can’t send payouts to the account’s bank or debit card on their behalf") | confirmed | — |
| 61 | Terms: "Adyen may in its discretion (i) transfer such negative balance to the immediately following Payout Day, or (ii) exercise its set-off right…" | T | confirmed | — |
| 62 | `Balancetransfer` is the carry-over journal type | settlement details report page | confirmed | — |
| 63 | Liable balance account: "the account where your business' funds are held. Funds can be deducted…" | A/platforms/account-structure-resources | confirmed | Date added; source title set to the page's own ("Account structure") |
| 64 | "Stripe automatically converts all incoming funds into your default currency."; up to 18 currencies | S/payouts/multi-currency-settlement | corrected (URL) | `S/payouts/multicurrency-settlement` redirects to `S/payouts/multi-currency-settlement`; source entry and spec updated |
| 65 | Adyen "offers like-for-like (no currency conversion) settlement…" | A/account/getting-paid | confirmed | — |
| 66 | Settlement details report has an Exchange Rate column | settlement details report page | confirmed | — |
| 67 | Fields for the entry model: Stripe `type`, `created`, `available_on`, `source`; Adyen journal type, PSP reference, batch; booking and value date | S/api/balance_transactions/object; settlement details report page; accounting report page | confirmed | — |
| 68 | "Where They Differ" row 1 (unit of the claim) | claims 6, 10, 23; A/account/getting-paid ("Payouts are sent separately to each of your merchant accounts"); A/platforms/account-structure-resources ("Balance account: holds the funds of your user") | confirmed | — |
| 69 | Row 2 (when funds become payable) | claims 13, 17, 26, 27 | confirmed | — |
| 70 | Row 3 (tie to network settlement): Stripe "Not public for standard payouts; documented for Instant Payouts" | claims 45, 47, 49 | confirmed ("Not public" tested against `S/llms.txt` and the pages in 47) | — |
| 71 | Row 4 (fees) | claims 8, 22, 30 | confirmed | — |
| 72 | Row 5 (hold and buffer names) | claims 53–56 | confirmed | — |
| 73 | Row 6 (negative balance) | claims 57, 59, 61, 63 | confirmed | — |
| 74 | Platforms transaction fees: "By default, these costs are deducted from your liable balance account" | A/platforms/online-payments/transaction-fees | confirmed | Date added |
| 75 | Platform example: Monday sales "are settled two business days later, on Wednesday, regardless of when the schemes pay out the funds." | A/platforms/settle-funds | confirmed | — |
| 76 | `SettledReversed`: "when it does not receive the funds… No action is required. Adyen adjusts your balance automatically." | A/account/sales-day-payout/upgrade-to-sdp | confirmed | — |
| 77 | "If the deposit requirement increases, funds from your sales are booked to the deposit" | A/account/balances | confirmed | — |
| 78 | `timetoread` | `check_draft.py structure`: 5,789 words ÷ 230 = 25.2 | corrected | 26 → 25 min read |

Counts: 78 checked; 70 confirmed (two of them statements of absence, one a non-documented industry-practice row); 5 corrected (14, 32, 34 and 64 as URL or content, 78); 3 hedged (27, 44, 48); 0 unsupported; 0 unreachable.

## Could not verify, and what was done

- **Absence claims (47, 49, 70).** "Not public" can only be tested by searching. Searched: the six Stripe pages the chapter cites, `docs.stripe.com/llms.txt`, the next-day settlement page, the payout schedules FAQ (through WebFetch; it says nothing about Stripe receiving funds from networks), and one web search restricted to Stripe's domains. Nothing found that says whether standard availability waits for network settlement. The claim stays, worded as it was ("as read in November 2026").
- **Stripe support article on reserves (53).** Served as a client-rendered page; curl returns the article text inside embedded data, which is what was read. A browser shows the same text.
- **Documentation page age.** Adyen's `.md` variants carry `last_modified` metadata from 2020 to 2023 on several cited pages (Getting paid 2020-11-10, Pass-through payout 2020-11-10, Sales day payout 2021-04-19, Balances 2021-11-22, Settlement details report 2022-10-24, Accounting report 2023-06-14; Upgrade to Sales day payout 2026-07-23). The pages display no date and their content is current (the 2026 bank-holiday file, the 2026 journal types), so they stay "n.d., accessed 2026-11" under ruling 25. No evidence-age flag was added.
- **Claim 5** (pooled accounts, the four-party table) is industry practice with no source on this page; it is worded "commonly" and points to the owning chapters.

## Links

All URLs under Sources and Evidence returned HTTP 200 in this session. Two had moved and were replaced with their final URLs (claims 14 and 64). All `[[permalinks]]` on the page are in the style guide's list. No external URL remains in the running text (ruling 22): 24 inline links were reduced to attributed plain text.

## Larkfield

Checked against the ledger: Tuesday 9 March 2027 at 19:42, Wednesday 10 March, Thursday 11 March, Friday 12 March (weekdays computed), €120.00, €2.53, €117.47, €0.61 *(assumption)*, €1.92, the refund of €84.00 on 18 March, 1,140 studios, €412,000 and its three causes, K3, Ines Bakker, Aylin Demir, Femke de Graaf, Utrecht, the two-business-day delay. No differences. One addition for ruling 26: the refund paragraph now says Studio Noord's balance held €212.40 of later sales that day *(assumption)*, so the refund is covered.

## Ledger conflicts

None. One looseness, left as is: the ledger line for this chapter names three amounts in the back office ("on its way", "ready to pay out", "held"), and the mapping table at the end of the Larkfield section has a fourth row, "Buffer the merchant set". The text above the table says three amounts; the fourth row is a vocabulary mapping, not a fourth displayed amount.

## For other pages

- Any page citing `https://docs.stripe.com/stripe-data/available-data` or `https://docs.stripe.com/payouts/multicurrency-settlement` should use the final URLs above.
- Any page that says Stripe has no balance transaction type for taking back a credited payment should name `payment_reversal` (and `payment_failure_refund` for delayed-notification methods).
- Any page that describes Adyen's "available funds" as including the deposit: the deposit is a separate balance (A/account/balances).

## For the author

- The `payment_reversal` type is the nearest thing in Stripe's public record to Adyen's `SettledReversed`. The page now quotes it without drawing a conclusion. Whether it is worth a question to Stripe is the author's call.
