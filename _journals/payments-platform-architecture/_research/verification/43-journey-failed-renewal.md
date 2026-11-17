# Verification — 43-journey-failed-renewal (`journey-failed-renewal`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants (and HTML for the link check), the Visa rules as the PDF of 24 October 2026 (converted to text; Table 7-2 and Table 5-21 read in full), Adyen's knowledge-hub guide and press release as HTML. All double-quoted strings taken from sources were matched mechanically against the fetched texts after normalizing quotes and markup; the three Visa quotations, which the PDF breaks across table lines, were read by hand. This is a journey page: it has no "Where They Differ" section, and each provider fact was also compared with the verified owning chapter and rulings 18–37.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Visa separates codes a merchant "must never resubmit" (Category 1) from codes with "Reattempt permitted (up to 20 attempts in 30 days)" (Table 7-2) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | — |
| 2 | Example codes: Category 1: 41, 43, 46; Category 2: 51, 91; Category 3: 54 | Visa rules, Table 7-2 | confirmed | — |
| 3 | Visa response code 51 is "Not sufficient funds" | Visa rules, Table 7-2 | confirmed | — |
| 4 | Category 3 has the same limit | Visa rules, Table 7-2 | confirmed | "once the data is corrected" is the page's gloss of the category name ("Data quality – Revalidate payment information"); unquoted, left |
| 5 | Adyen's page still says "up to 15 times in a 30-day period"; "excessive retry fee" | https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed | Still 15 on 17 November 2026 (ruling 19) |
| 6 | "Hard" and "soft" decline are industry shorthand | ruling 15 | confirmed | Neither term is in Table 7-2 |
| 7 | Visa stored-credential rule: written notice and "at least 7 calendar days to pay by other means" (Table 5-21) | Visa rules | confirmed | Quote matches; the row has no regional restriction |
| 8 | Adyen: `shopperInteraction` `ContAuth` with `recurringProcessingModel` `Subscription` "(page last modified July 2023)" | https://docs.adyen.com/online-payments/tokenization/make-token-payments | corrected | Fields confirmed. Ruling 30: the date came from front matter; now "n.d., accessed November 2026", in text and Sources |
| 9 | Stripe's definition of a merchant-initiated transaction | https://docs.stripe.com/payments/cits-and-mits | confirmed | — |
| 10 | Merchant-initiated payments fall outside SCA: no challenge, no liability shift | https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions | confirmed | "neither a customer challenge nor a liability shift occurs" |
| 11 | Adyen: "we automatically swap that for a network token"; the token "remains the same" after a reissue | https://docs.adyen.com/online-payments/network-tokenization | confirmed | — |
| 12 | Adyen reports `Refused`, reason 12 "Not enough balance" | https://docs.adyen.com/development-resources/refusal-reasons | confirmed | Source entry's front-matter date and evidence-age note removed (ruling 30) |
| 13 | The network's raw code is returned "once the raw response is enabled for the account" | https://docs.adyen.com/development-resources/raw-acquirer-responses | confirmed | No source entry supported it; page fetched ("in your Customer Area enable receiving raw responses"; `refusalReasonRaw`), attribution and source added |
| 14 | Real Time Account Updater quote "(page last modified May 2026)" | https://docs.adyen.com/online-payments/account-updater/real-time-account-updater | corrected | Quote confirmed. Ruling 30: date removed, now n.d. |
| 15 | Stripe "automatically attempts to update saved card details …"; "It isn’t possible to identify cards that support automatic updates." | https://docs.stripe.com/payments/cards/overview | confirmed | — |
| 16 | Adyen idempotency: "the response to the first attempt will be returned without duplication"; keys valid 7 to 14 days "(last modified July 2020)" | https://docs.adyen.com/development-resources/api-idempotency | corrected | Quotes confirmed. Ruling 30: date and the "evidence age: 6 years" note removed |
| 17 | Adyen's Checkout API has no call that returns a payment by its identifier | https://github.com/Adyen/adyen-openapi (`json/CheckoutService-v72.json`, parsed: three GET operations) | confirmed | Already scoped to the Checkout API (ruling 29) |
| 18 | "Stripe generates an invoice for every subscription billing period" | https://docs.stripe.com/billing/invoices/subscription | confirmed | — |
| 19 | "a failed renewal payment makes the subscription `past_due`" | https://docs.stripe.com/billing/subscriptions/overview | confirmed | — |
| 20 | `invoice.payment_failed` with `attempt_count`; `next_payment_attempt` on the invoice | https://docs.stripe.com/billing/revenue-recovery/smart-retries | confirmed | The page adds that for users of automations `next_payment_attempt` is set in `invoice.updated`; not needed by the sentence |
| 21 | "For new Stripe accounts, Stripe enables Smart Retries by default and configures it for up to 8 retries within 2 weeks." | same | confirmed | — |
| 22 | "An insufficient-funds decline is retried." | same | hedged | The page does not say so in words; it follows from the code not being on the hard-decline list. Sentence now says that |
| 23 | Hard decline codes include `lost_card`, `stolen_card`, `pickup_card`, `incorrect_number`; "Retries continue to be scheduled … only execute after detecting a new payment method." | same | confirmed | — |
| 24 | Failure emails include "a link to a page where the customer can update their payment method" | https://docs.stripe.com/billing/revenue-recovery/customer-emails | confirmed | — |
| 25 | Auto Rescue "automatically retries refused or charged back shopper-not-present transactions such as subscription renewals" "(page last modified March 2020)" "(Evidence age: 6 years)" | https://docs.adyen.com/online-payments/auto-rescue | corrected | Quote confirmed. Rulings 30 and 37: the date and the evidence-age flag came from front matter and are removed; "Adyen's 2020 overview" is now "Adyen's overview" |
| 26 | "Adyen's support enables it" | https://docs.adyen.com/online-payments/auto-rescue/cards | corrected | The page says "contact our Support Team or your Adyen Account Manager", at account level and at transaction level; sentence now names both |
| 27 | Account level: "a rescue window of one calendar month is used"; per payment 1 to 48 days | same | confirmed | — |
| 28 | `merchantOrderReference` "should represent a specific billing cycle or subscription"; results by webhook; "you should cancel the Auto Rescue process for the refused payment" | same | confirmed | — |
| 29 | Adyen can supply a payment link when the rescue ends | https://docs.adyen.com/online-payments/auto-rescue ; cards page | confirmed | — |
| 30 | Stripe's two example signals (devices in the last N hours; best time to pay) | https://docs.stripe.com/billing/revenue-recovery/smart-retries | confirmed | — |
| 31 | Adyen: "uses smart logic to decide which payments can succeed when retried later, and performs these retries at optimal times" | https://docs.adyen.com/online-payments/auto-rescue | confirmed | — |
| 32 | "Neither publishes a model, its inputs or a recovery rate" | https://www.adyen.com/knowledge-hub/recurring-payments | corrected | Ruling 37(b), (c). Adyen's guide (displayed date June 16th, 2026) says of Auto Rescue "Pinterest saw a 4% improvement in recovery rate on retried transactions, with expectation of reaching 10% over time". The page now quotes it as one customer's figure with no baseline, and says Stripe's figure is not one for Smart Retries alone, with a link to chapter 29, which reads it. KEY POINT 3 adjusted ("or a recovery rate with a stated basis"). Source added |
| 33 | Adyen's account-updater overview "was last modified in December 2019 (Evidence age: 7 years)" | https://docs.adyen.com/online-payments/account-updater | corrected | Ruling 30: a front-matter date. Clause removed; the source entry, then unused, removed |
| 34 | "If recovery fails, the subscription transitions according to your settings"; options cancel, `unpaid`, `past_due`, pause | https://docs.stripe.com/billing/revenue-recovery/smart-retries | confirmed | — |
| 35 | "An invoice that Stripe marks uncollectible after ending payment retries" | https://docs.stripe.com/billing/subscriptions/overview | confirmed | — |
| 36 | "Revoke access to your product when the subscription is `unpaid`" | same | confirmed | — |
| 37 | "Adyen's documentation describes no invoice and no subscription object" | https://docs.adyen.com/llms.txt (searched for invoice, subscription, billing) ; https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates | hedged | The index lists only Adyen's own fee invoices, Klarna invoice lines and webhook subscriptions. Reworded as the author's finding ("I found no …, accessed November 2026") and brought into line with chapter 27: Orb, bought on 1 July 2026 ("officially closed on July 1, 2026"), is not documented as part of Adyen's platform. Source added |
| 38 | Stripe retries "inside the retry window you set" (comparison table) | https://docs.stripe.com/billing/revenue-recovery/smart-retries | confirmed | "1 week, 2 weeks, 3 weeks, 1 month, or 2 months" |
| 39 | Mastercard's rules could not be read | ruling 17 | not checked | Not re-attempted in this session; no Mastercard rule is cited on the page |
| 40 | Adyen platform payout two business days after the sales day; no webhook, later report as confirming record | chapters 3, 8 and 15 (verified) | confirmed | Wording agrees with the owning chapters; sources for these are on journey 1 and those chapters |
| 41 | The ledger "gets two entries" on 4 April when the debt closes | ruling 28 | corrected | Larkfield fact with a rule behind it: entries are written from report lines by the reconciliation job, never from the webhook. Paragraph and step-table row 10 now say so; "nightly reconciliation" is now "the reconciliation job" |
| 42 | The 7,900 emails of 1 October 2026 | ruling 37(a); ledger lines of chapters 21 and 29 | corrected | Both steps are now given: the rate limit turned requests away before any card was charged and the job marked them failed; the email job could not tell a declined card from one never charged |
| 43 | Dispute window of about 120 days, to about 2 August 2027 | Visa rules; ledger line of this chapter | confirmed | 4 April + 120 days = 2 August |
| 44 | Stripe Billing is "Stripe's billing engine"; Larkfield uses it for studio plans only | ledger; https://docs.stripe.com/billing/subscriptions/overview | confirmed | — |

Counts: 44 rows; 32 confirmed, 9 corrected (7 provider facts: rows 8, 14, 16, 25, 26, 32, 33; 2 Larkfield facts under rulings 28 and 37: rows 41, 42), 2 hedged, 0 unsupported, 0 unreachable, 1 not checked (row 39).

## Could not verify, and what was done

- Mastercard's rules were not fetched again (ruling 17 records the 403); the page cites no Mastercard rule and says so.
- "No invoice or subscription object" is a search of Adyen's documentation index, not an exhaustive reading; the sentence is now worded as the author's finding.
- Stripe's "55%" figure was not quoted on this page; the page points to chapter 29, whose verifier read it (ruling 37(c)). The Dutch version of Stripe's Billing page fetched in this session carries the same 55% sentence.

## Rulings applied

- 19 (already applied; re-confirmed), 28 (row 41), 29 (row 17, already scoped), 30 (rows 8, 12, 14, 16, 25, 33 and six source entries), 37 (rows 25, 32, 42). Rulings 27, 31, 32 and 34 touch nothing on this page: it makes no statement on acquiring, routing, report timing or Stripe's renewal scheduler.

## Larkfield consistency

Checked against the ledger: Thursday 1 April 2027 decline (code 51, reason 12), Sunday 4 April approval (day 3), keys ending `:2027-04:1` and `:2027-04:2`, fee €1.18 and €47.82, payout Tuesday 6 April, next renewal 1 May, dispute window about 2 August 2027, lapse branch 1, 4, 8, 13 April, pause 15 April (day 14), end 1 May (day 30); 940,000 renewals, 38%, K5's 18 hours, 1,840 members on 1 November 2026, 7,900 renewals on 1 October 2026, Lotte Smit on 1 March 2027, set-up on 12 January 2027. Weekdays checked. No contradiction found.

## Ledger conflicts

None. (The ledger line of chapter 21 and that of chapter 29 on the 7,900 emails are two steps of one account, as ruling 37(a) says.)

## For the author

- `journal-spec.json`, entry `journey-failed-renewal`, `intent.outcome.know` (copied to `spec.json`, not edited): "…and Adyen's account-updater page is dated 2019." Ruling 30 says documentation pages are not dated from front matter; the same bullet says "neither company publishes how its retry timing is chosen", which stands, but should not be read as "no recovery figure" (ruling 37(b)).
- The Sources entry for Mastercard is a note without a link ("not reachable for this book"); kept as an honest statement, though it is not in the entry format.

## For other pages

- None found.
