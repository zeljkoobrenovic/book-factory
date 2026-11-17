# Verification — 12-payment-ledgers (`payment-ledgers`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (`.md` variants for docs.stripe.com and docs.adyen.com) and read. Quotations were compared with the fetched text by script, typographic quotes and whitespace aside; the passages around each non-quoted fact were read.

Short names: **S-ledger** = stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement; **S-credits** = stripe.dev/blog/how-we-built-stripe-credits-…; **A-d2d** = adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2; **S-bt** = docs.stripe.com/api/balance_transactions/object; **S-sigma** = docs.stripe.com/data/data-freshness; **A-sdr** = docs.adyen.com/…/settlement-details-report; **A-sdp** = docs.adyen.com/account/sales-day-payout; **A-par** = docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report; **Sq** = developer.squareup.com/blog/books-…; **Uber** = uber.com/blog/money-scale-strong-data; **TB-dc / TB-2p** = docs.tigerbeetle.com/concepts/debit-credit, /coding/two-phase-transfers; **MT** = moderntreasury.com/journal/accounting-for-developers-part-i.

| # | Claim (short) | Source | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe: "99.99% of our dollar volume is fully ingested and verified within four days" (lead, key points, design two, tables, take-aways) | S-ledger | confirmed | — |
| 2 | Stripe: "Ledger is based on double-entry bookkeeping, a standard method…" | S-ledger | confirmed | — |
| 3 | Stripe: "Transactions previously published into Ledger cannot be deleted or modified…" | S-ledger | confirmed | — |
| 4 | Stripe: pipes and reservoirs quote | S-ledger | confirmed | — |
| 5 | Stripe: "Ledger encodes a state machine representation…" (fund flow; accounts as states, events as transitions) | S-ledger | confirmed | — |
| 6 | Stripe: "Even when we have billions of transactions… 'Find the clearing Accounts with nonzero balance.'" | S-ledger | confirmed | Inner quotation marks are double in the source, single on the page (nesting only) |
| 7 | Stripe lists "malformed reports or propagated errors from banking or network partners" | S-ledger | confirmed | — |
| 8 | The post is by Ilya Ganelin, of the Ledger team, dated 16 February 2024 | S-ledger (displayed "Date: 2024.2.16"; "works on Ledger Platform") | confirmed | — |
| 9 | Stripe: "there is no intrinsic mechanism forcing these systems…" | S-ledger | confirmed | — |
| 10 | Stripe: "Some producers generate billions of events per day, while others may only generate a few hundred" | S-ledger | corrected | The source has "some producers…" in mid-sentence after a semicolon; the page quoted it as a capitalized sentence. Now quoted in lower case with a paraphrased lead-in ("Some run in real time and others monthly", which the same sentence of the source says) |
| 11 | Stripe: need to "prove that these individual systems are collectively modeling our financials correctly" | S-ledger | confirmed | — |
| 12 | Stripe: "We built Ledger, an immutable and auditable log…" | S-ledger | confirmed | — |
| 13 | Stripe: creation and release events "completely independent… Ledger maintains accurate fund flows"; joined by identifier | S-ledger ("through the identifier for business and id") | confirmed | — |
| 14 | Stripe's three questions: Clearing, Timeliness, Completeness (three quotes) | S-ledger | confirmed | — |
| 15 | Stripe: "we ensure that every ID in a producer database has a matching Ledger event" | S-ledger | confirmed | — |
| 16 | Scores per team; "the 50% score for Aging Balances means that some clearing issues have persisted over time" | S-ledger | confirmed | — |
| 17 | "Each day, Ledger sees five billion events…" | S-ledger | confirmed | — |
| 18 | "over 99.9999% explainability of money movement", claimed for Ledger together with its tooling | S-ledger ("Together, Ledger and the DQ Platform ensure…") | confirmed | — |
| 19 | "In the future, we want to improve timeliness to minute-level analysis and response" | S-ledger | corrected | The source sentence continues after "response" with a dash; the page had a period inside the quotation marks. Period moved outside |
| 20 | "we can’t run simple queries to mutate the state; instead, we have to revert and reprocess prior operations" | S-ledger | confirmed | — |
| 21 | "All operations must go through a two-phase review and commit of the data" | S-ledger | confirmed | — |
| 22 | If a release event "is never published or has the wrong `id`, Ledger would not clear the balance" | S-ledger | confirmed | — |
| 23 | Clearing problems scored under "Aging Balances"; the platform raises "auto-generated tickets" | S-ledger | confirmed | — |
| 24 | Stripe names no storage engine, schema or consistency model for Ledger; neither post says how the API balance relates to Ledger ("Storage: Not public") | S-ledger, S-credits read in full; docs.stripe.com/llms.txt searched for "ledger" (one hit, on revenue-recognition chart of accounts) | confirmed | Absence in the sources read; no wider search of other Stripe posts was made |
| 25 | Second Stripe post, April 2026, by Pratik Gupta and Sai Samant | S-credits (displayed "Date: 2026.4.16") | confirmed | — |
| 26 | "we extended Stripe’s existing Money Movement and Storage (MMS) platform" | S-credits | confirmed | — |
| 27 | "the financial account, which represents an entity capable of holding a balance and participating in money transfers" | S-credits | confirmed | — |
| 28 | "a three-phase lifecycle through the ledger: submitted → prepared → disbursed" | S-credits | confirmed | — |
| 29 | "We reject attempts to create a transfer between a logical account and a real account at the platform level" | S-credits | confirmed | — |
| 30 | The post says "internal ledger"; how MMS, that ledger and the 2024 Ledger relate is stated in neither | S-credits, S-ledger | confirmed | — |
| 31 | Adyen post by Willem Pino, tech lead, 2021 (August 2021 in the table; 2021-08-23 in Sources) | A-d2d (displayed "By Willem Pino, Tech Lead, Adyen August 23rd, 2021") | confirmed | Displayed date equals the metadata date |
| 32 | Adyen: "The only way to add new records… is by means of templates."; "a recipe that takes…"; "These templates are mathematically verified"; "that every combination of amounts will result in a net sum of 0"; "This verification is fully automated…" | A-d2d | confirmed | — |
| 33 | Adyen: "if at any time, we sum up all the records in the accounting system, the result will always be 0." | A-d2d | confirmed | — |
| 34 | Adyen: "Over the lifetime of a payment transaction, about 50 rows have to be inserted into the accounting database" | A-d2d | confirmed | — |
| 35 | PostgreSQL; "we decided to shard our accounting database into several accounting clusters"; "a simple round-robin strategy" | A-d2d | confirmed | — |
| 36 | A payout "needs to come from one account"; "the money needs to be transferred from one cluster to the other" | A-d2d | confirmed | — |
| 37 | "for the accounting systems we don’t mind if they are down for a little bit…"; the payment layer "saves the payment in a local database and a separate process picks it up when possible" | A-d2d | confirmed | — |
| 38 | The pick-up process "will run behind if we have doubt… availability of the PAL itself"; PAL is the payment processing layer | A-d2d ("The Payment Processing Layer (or PAL, see part one)") | confirmed | — |
| 39 | Matching partners' reports: a framework that would "first parse a file and then split it into the relevant parts for each cluster" | A-d2d | confirmed | — |
| 40 | "We leverage this same system of accounting for our banking platform" | A-d2d | confirmed | — |
| 41 | Adyen's accounting framework is in-house; Adyen does double-entry bookkeeping for every payment | A-d2d | confirmed | — |
| 42 | No Adyen engineering account newer than August 2021 was found; nothing public describes the internals of platform balance accounts | — | not checked | A negative statement about the author's search. docs.adyen.com/llms.txt was searched for "ledger", "double-entry" and "accounting system" (one hit, a classic-platforms guide on building a ledger from reports, which is not about Adyen's internals). The knowledge hub was not searched post by post. Sentence kept as worded ("was found") |
| 43 | Square 2019: "requires doing an expensive group-by aggregate for each merchant"; "It’s impossible to split a single payment into multiple payouts"; post dated 16 October 2019, by Łukasz Strzałkowski | Sq | confirmed | — |
| 44 | Square: "you should never be able to transact with the database in a way that results in an illogical financial transaction." | Sq | confirmed | — |
| 45 | Modern Treasury: "after painful incidents involving missing funds, broken payout flows, or inconsistent balances"; 2022, updated 2025 | MT (displayed "August 17, 2022 (Updated August 13, 2025)") | confirmed | — |
| 46 | TigerBeetle: "once transfers are recorded, they cannot be erased. Reversals are implemented with separate transfers…"; "Where SQL allows destructive UPDATE and DELETE, TigerBeetle enforces append-only immutability" | TB-dc | confirmed | — |
| 47 | TigerBeetle: "A two-phase transfer moves funds in stages"; reserved, then posted or voided | TB-2p (pending; then post, void or expire) | confirmed | — |
| 48 | Uber 2020: older design had separate collection and disbursement systems with "no holistic view of end-to-end money movements"; the replacement "is a single, integrated, SOX-compliant system built on the principles of double-entry accounting and can reconcile itself"; dated 2 October 2020 | Uber | confirmed | — |
| 49 | Take-away: "Double entry with immutable entries is the published basis of the books at Stripe, Adyen, Square and Uber" | S-ledger, A-d2d, Sq, Uber | hedged | Adyen's post states double entry but never says its records are immutable (it mentions "mainly inserts and updates"). The bullet now says double entry for all four and immutability for Stripe, Square and Uber, and that Adyen's post does not say. Spec conclusion wording aligned |
| 50 | Stripe's balance transaction object carries `amount`, `fee` and `net` against one balance | S-bt (`balance_type`: "The balance that this transaction impacts") | confirmed | — |
| 51 | Stripe's data documentation "calls the table 'the canonical record of changes to your Stripe balance'" | S-sigma | hedged | The phrase is a comment in an example SQL query on the Sigma data freshness page, not a statement in the prose. The sentence and the source entry now say so. URL changed: /stripe-data/available-data redirects to /data/data-freshness; replaced in Sources and in the spec |
| 52 | Adyen's settlement details report lists entries by journal type, such as `Settled`, `Refunded`, `Chargeback`, `MerchantPayout` | A-sdr | confirmed | — |
| 53 | Adyen: refunds and chargebacks "are added to the payable batch as they occur" | A-sdp | confirmed | — |
| 54 | (Added in this pass) Adyen's payment accounting report has a `SentForSettle` record before `Settled` | A-par ("SentForSettle: Request to transfer the payment sent to the financial institution."; "Settled: Payment has been settled, and the funds have been received by Adyen.") | confirmed | New source entry added |
| 55 | "Where They Differ" table, 7 rows, cell by cell | claims 1, 8, 10, 17, 21, 25, 27, 29, 31–35, 37, 40, 41 | confirmed | Every Stripe and Adyen cell is one of the facts above or "Not public". "Storage / Stripe: Not public": see claim 24. "Correcting an error / Adyen: Not public": A-d2d says nothing on corrections; documentation index searched as in claim 42 |
| 56 | Airbnb's 2017 post "could not be retrieved and is not used" | medium.com/airbnb-engineering/tracking-the-money-… | confirmed | Still 403 (bot challenge) in this session; the publication's RSS feed does not reach back to 2017. No claim rests on it |
| 57 | "Card networks settle within a few days" | none | not checked | Unsourced general statement used to read an illustrative balance; chapter 3 owns settlement timing. Left as is |
| 58 | Evidence ages: Square 7 years, Uber 6, Adyen 5; Stripe 2024 under three years | publication dates above | confirmed | Flags present in text and in source entries |

Counts: 58 claims; 52 confirmed, 2 corrected, 2 hedged, 0 unsupported, 0 unreachable, 2 not checked.

## Links

All twelve original source URLs returned 200. One changed: `docs.stripe.com/stripe-data/available-data` → `docs.stripe.com/data/data-freshness` (replaced). `uber.com/blog/money-scale-strong-data/` redirects to a locale path (`/nl/en/blog/…`) from this network; the canonical URL was kept. One source added (A-par, 200). No external URL is in the running text (ruling 22); all `[[permalinks]]` are in the valid list.

## Could not verify

- Claim 42 (no newer Adyen engineering account): a negative; not exhaustively searched. Kept as worded.
- Claim 57 (card networks settle within a few days): general background with no source on this page. Kept.

## Larkfield consistency (step C) and rulings

- **Ruling 26.** The replay paragraph said the €317,200 "would have been entries into 'to recover from studio' accounts". It now says the refunds are booked against "owed to studio" where the studio's balance covers them and into "to recover from studio" only for the part it cannot cover. The worked €84.00 refund had the same fault (it booked +84.00 to "to recover from Studio Noord" although the studio's €212.40 balance covers it): it is now booked against "owed to Studio Noord", with the "to recover" account shown as the counterfactual for an empty balance. Spec p39 and p40 reworded to match (same units, same order).
- **Ruling 28.** The Keel example had entry 1 triggered by the webhook. All four entries are now written from provider report lines (entry 1 from the capture line; on Adyen a `SentForSettle` record), and the text says a webhook changes only the payment record store. "One writer" is now the reconciliation job, not the payment service under K1. The pre-Keel 2025 description is unchanged.
- **Chapter 14 (owner of payouts).** Entries 3 and 4 followed a different order from chapter 14 and dated "confirmed as arrived" on 11 March. They now follow chapter 14: sent on 11 March (payouts in transit / funds at provider), marked arrived on 25 March when the ten-business-day window closes (owed to studio / payouts in transit). The account descriptions in the six-account table were adjusted to match. End balances are unchanged.
- **Chapter 15.** "Every clearing balance older than five days has a named owner" now reads as chapter 15 has it: every balance has an owner, and one open more than five business days goes to Priya Raman's weekly review.
- Weekdays checked: Tuesday 9 March, Thursday 11 March, Thursday 25 March 2027. Sums checked: 317,200 + 73,500 + 21,300 = 412,000; 4,900 × €15.00 = €73,500; 120.00 − 2.53 = 117.47.
- `timetoread` 26 → 27 (6,221 words ÷ 230).

## Ledger conflicts

- The base ledger says the payout with Mila's €117.47 "arrives on Thursday 11 March"; the chapter 14 line says it is "marked sent on Thursday 11 March 2027 and arrived on Thursday 25 March". Read together they do not conflict (the money lands on the 11th; Larkfield's record can only mark it arrived when the window closes), but a reader of the base line alone will date the ledger's "arrived" entry on the 11th, as this page did. Chapter 14 was followed.
- The chapter 12 addition line lists the clearing account "sales awaiting settlement report" without saying what opens it. Under ruling 28 it must be opened by a report line. This page now uses the provider's report line for the capture. Chapter 15's worked example writes the split from the Balance Platform Accounting Report after the batch closes and does not use this clearing account by name; the author may want one sentence in the ledger fixing which report line opens it.

## For other pages

- `35-splits-balances-and-platform-payouts` and `15-payment-reconciliation-and-reporting` still carry inline external links in the running text (ruling 22), as of this session.
- Chapter 35's ledger line says "to recover from studio" is used "when the studio's balance is empty"; ruling 26 says "only for the part a studio's balance cannot cover". A partly covering balance is not shown anywhere.
