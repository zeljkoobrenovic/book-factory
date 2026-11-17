# Verification — meet-larkfield (`meet-larkfield`)

Verification pass of 17 November 2026. This is a preface page with no external sources: its job is internal consistency. Section A of the reviewer brief was applied in its changed form: the few statements about a provider's product or a network's protocol were checked against the current text of the owning chapter, and every Larkfield fact against the ledger as it stands (base lines, every "Additions by chapter" line, rulings 13, 14, 20, 23, 24, 26 and 28). No URL was fetched for this page.

Counts: **14 claims** about providers and protocols checked — 14 confirmed, 0 corrected, 0 hedged, 0 unsupported, 0 unreachable. Larkfield facts: 2 wordings corrected (section C).

## A. Claims about providers, networks and protocols

| # | Claim on this page (short) | Owning chapter (permalink; folder) | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe Billing is Stripe's subscription product | `subscriptions-and-billing-engines`; 27 | confirmed | — |
| 2 | Stripe Connect is Stripe's product for platforms whose customers are the sellers | `platform-payment-models`; 33 (line 33 and its Connect section) | confirmed | — |
| 3 | Adyen's platform product is called Adyen for Platforms | 33 (line 129) | confirmed | — |
| 4 | An acquirer is the licensed institution that takes a merchant's card payments into the card networks | `acquiring-and-network-connectivity`; 06 | confirmed | The page states no fact about who acquires for either provider (rulings 11 and 27 not triggered); the 2024 reason is given as Larkfield's, "effect not measured" (`06` ledger line). |
| 5 | A direct debit can be returned weeks later; SEPA Direct Debit is the euro-area scheme, Bacs the British one | `local-payment-methods`; 07 | confirmed | — |
| 6 | With iDEAL the payer approves a bank transfer in their own banking app; Bancontact is Belgium's domestic method | 07 (line 67) | confirmed | Chapter 7 notes that Adyen's catalog types Bancontact as a card and a wallet; "domestic method" is neutral on that. |
| 7 | Legacy Custom connected accounts: seller accounts the platform creates and controls, with no Stripe dashboard of their own | 33 (line 125; Larkfield section); ruling 23 | confirmed | Not described as Express anywhere on the page. |
| 8 | Destination charges that name the studio as the business behind the payment (`on_behalf_of`) | 33 (lines 65, 109) | confirmed | — |
| 9 | On Adyen each seller has a balance account and the platform's fee goes to one of the platform's own (the liable balance account) | 33; `balances-and-funds-flows`; 13 | confirmed | — |
| 10 | 3-D Secure is the protocol by which the cardholder's bank checks who is paying; a phone wallet authenticates on the device, so no 3-D Secure challenge | `three-d-secure-and-sca`; 25 (lines 14, 28); ruling 14 | confirmed | — |
| 11 | A network token is a card-network stand-in for a card number that stays valid when the card is reissued | `network-tokens`; 23 (line 27); ruling 8 | confirmed | — |
| 12 | A card payment can be disputed for about 120 days (Mila's pass: "about 7 July") | `journey-of-a-payment`; 01; `01` ledger line | confirmed | Wording "about 7 July", as the ledger line requires. |
| 13 | A merchant-initiated payment is one the merchant starts without the cardholder present | `payment-authorization`; 02 | confirmed | — |
| 14 | Stripe has a rate limit that an unpaced job can meet (the Renewal Wave "met Stripe's rate limit") | `payment-developer-platform`; 21 (lines 15, 35); `21` ledger line | confirmed | — |

Links: no external URL on the page (ruling 22 holds). Every `[[permalink]]` is in the style guide's valid list (checked by script).

## C. Larkfield consistency

Weekdays checked by script: 14 September 2026 Monday; 9 March 2027 Tuesday; 10 March Wednesday; 11 and 25 March Thursday (11 March plus ten business days is 25 March); 18 March Thursday; 1 October 2026 Thursday; 1 November 2026 Sunday.

| Item | Status | What changed |
| --- | --- | --- |
| Company, markets (2,300 + 1,450 + 1,100 + 700 + 650 = 6,200), members, staff, revenue split, €12.6M cost, €7.2M margin, 1.77% | agrees | — |
| Business lines, fee table, €2.53 and €117.47, method mix (48% off cards) | agrees | — |
| Two providers: 44% (€493M), 56% (€627M); 3,590 and 2,610 studios; 1,140 split studios; member id as the shared identifier | agrees (`06`, `11`, `34` lines) | — |
| Studio is the seller; provider holds the money; studio carries a lost dispute and its fee, Larkfield behind it | agrees (base ledger, `33` line) | — |
| Stripe studios are legacy Custom connected accounts with destination charges | agrees (ruling 23) | — |
| Nine systems table; history 2017, 2018, 2024, 2025 | agrees | — |
| Four missing joins: one unrestricted key shared by five systems; fresh key at each network call; only read call returns Larkfield's own row; reconciliation covers one provider; ledger lacks entries for refunds after payout, chargeback fees, currency conversion; billing outside the payments team | agrees (`21`, `18`, `17`, `12` lines) | — |
| Cast of thirteen with pronouns | agrees (cast table plus `04`/`07`/`23` lines; ledger `meet-larkfield` line) | — |
| The Unexplained €0.4 Million: year-end 2025, €412,000 higher, €317,200 + €73,500 + €21,300 | agrees (ruling 24: "eight incidents, found between the year-end close of 2025 and November 2026") | — |
| The Version Cliff: ran on the account default | corrected | "a Stripe API version nobody had chosen" (bullet and table) became "nobody owned". The ledger's `19` line and chapter 19 say someone moved the account default to `2022-11-15` in early 2023, so it was chosen once and owned by nobody. The bullet already said it "sent none, so it used the account's default". |
| The Frozen Studios: May 2026, Stripe Connect, announced deadline, one batch email, 230 studios, up to 12 days, Ironworks among them | agrees (`26`, `34` lines) | — |
| The Payout That Bounced: June 2026, 412, €386,000, three weeks, 19 days, two studios | agrees | — |
| The Card-Testing Weekend: 8–9 August 2026, €1 trial drop-ins to guests, 61,000, €4,100, 31 hours; provider unnamed | agrees (`24` line) | — |
| The Silent Webhook: Monday 14 September 2026, shortly after midnight, 9 hours, 3,200, "that morning", 460 tickets | agrees (ruling 20; no Saturday or Sunday on the page) | — |
| The Renewal Wave: 1 October 2026, 38% in six hours, Stripe's rate limit, 7,900 | agrees (`21` line) | — |
| The Double Charge: 1 November 2026, new key, first request approved, second payment, 1,840, €71,300, 212; provider unnamed | agrees (`02`, `18` lines) | — |
| K1: key includes the number of the scheduled attempt; only the payment service holds a money-moving credential | agrees (ruling 13; `21` line) | — |
| K2: "the payment object where the API lets Larkfield read it, the settlement report where it does not" | agrees (ledger wording; rulings 12 and 29) | — |
| K3: entries for every movement; one run per provider on its report-ready signal; ledger entries only from report lines; open items with an owner | corrected | "The nightly reconciliation covers both providers" became "The reconciliation job covers both providers", the ledger's K3 wording; under Keel the run starts on each provider's report-ready signal, not at a fixed hour (`15` line, ruling 28). The page's own spec said it would not call the job nightly under Keel. |
| K4 to K8; the Card-Testing Weekend without a K number; K8 paragraph (50 studios, own-credential payments move, stored-card renewals stay, no second provider at the front desk) | agrees (`10`, `11`, `24` lines) | — |
| Declined proposals: February orchestration, offline acceptance, message queue (outbox live 1 March 2027); April refund buffer (€43 million); May merchant of record; May–June instant-payout card | agrees (`10`, `11`, `38`, `16`, `32`, `36` lines) | — |
| Mila's class pass: Tuesday 9 March 2027 19:42, €120.00, Dutch Visa debit in a phone wallet, no 3-D Secure challenge, Adyen, captured automatically, Ines's ticket on Wednesday, payout sent Thursday 11 March, record marked arrived Thursday 25 March at the close of the ten-business-day window, about 7 July | agrees (ruling 14; `14`, `01` lines) | — |
| Split of the €120.00: €0.61 = €0.24 + €0.06 + €0.31, €1.92 left; on Stripe €0.87 and €1.66 | agrees (`05` lines) | — |
| Membership: €49.00, set up 12 January 2027 with a 3-D Secure challenge, declined 1 April, email the same day, retry 4 April is scheduled attempt 2 with its own key, access kept | agrees (`02`, `27`, `43` lines) | — |
| First of the month: €555M, €46M, 940,000, 540,000 by card (assumption), 357,000, €17.5M, 18 hours | agrees (`09` line) | — |
| Refund after payout: 18 March 2027, €84.00, studio funds it, Larkfield keeps its fee, balance €212.40, next payout €84.00 smaller, Aylin Demir's question | agrees (ruling 26; `35`, `44` lines). The page does not state the ledger booking; nothing to correct. | — |
| The €120 dispute: 2 February 2027, Dutch Mastercard credit, 24 February, €15.00, check-ins 4 and 11 February, €135.00 at stake, defense 3 March; outcome left to `journey-dispute` | agrees (`04`, `25`, `45` lines) | — |
| Daan Peters (1 April 2027, €0.64, €48.36, 27 May); Lotte Smit (stored 2025, replaced February 2027, renewal 1 March through a network token) | agrees (`07`, `23` lines) | — |
| Ironworks €1,890 on 1 February 2027; Studio Noord €89 to €189 on 16 April 2027; 1,240 sent and 1,324 billed in March 2027 | agrees (`31`, `27`, `28` lines) | — |

## D. Agreement with `where-payment-systems-go-wrong`

The incident-to-pattern and decision-to-pattern mapping on this page is the one its writer recorded in the ledger (`meet-larkfield` line). The patterns page was written later; four differences were found and all four were resolved **on the patterns page** (details in its verification file): K3 was not named for The Stranded Payout; K4 was not named for The Vault Hostage; The Orphaned Refund and The Phantom Payment were labeled "no named incident" although this page ties them to the Unexplained €0.4 Million and the Silent Webhook. Nothing on this page changed for it.

Both pages agree on: the eight incident-to-pattern pairs; K1 The Double Charge; K2 The Trusted Doorbell and The Phantom Payment; K5 The First of the Month; K6 The Frozen Seller; K7 The Version Cliff; K8 The Single Rail; the Card-Testing Weekend without a K number.

## E. Format (section B of the brief)

- Sources and Evidence had one sentence and no groups or closing line. The three italic-labeled groups ("None on this page; see the linked chapters", as on the patterns page) and the closing line were added.
- No external URL in the text; hand-offs use `[[part-1]]` and `[[part-9]]`.
- Three KEY POINTS. American spelling; no banned word found.
- No unit was added, dropped, merged or reordered.

## Could not verify

- Nothing external. Chapters 25, 26 and 29–50 had no verification file of their own when this pass ran; claims 1, 10 and the ledger lines of those chapters were read as they stood.

## Ledger conflicts

- **Mila's payout.** The base worked-example line says the payout "is sent on Thursday 11 March and, in the best case, reaches the studio's bank the same day", and that Larkfield's record marks it `arrived` on 25 March; the `14` line says "marked sent on Thursday 11 March 2027 and arrived on Thursday 25 March". These agree as corrected. The page follows them: "sent on Thursday 11 March", "marks it as arrived on Thursday 25 March". Its take-away and one caption say "paid out on Thursday 11 March" / "pays Studio Noord €117.47 on 11 March", which is the payout date, not a claim that the money landed; left as is.
- **"Nightly" under K3.** The ledger's K3 says "the reconciliation job covers both providers, one run per provider, started when that provider's reports are ready"; the `15` line says "not at a fixed hour"; the `41` line and chapter 15's own text (line 39) still say "the nightly reconciliation". Chapter 15 owns the topic; this page now uses the K3 wording and avoids "nightly" for the Keel design. The systems table keeps "Nightly" for the January 2027 baseline, as in the ledger.

## For other pages

- `journal-spec.json`: the `meet-larkfield` entry's AC-2 expected answer still says "Saturday night" and "Sunday morning" and "state changes come from fetching the object" (rulings 20 and 12); already noted in this page's spec. Its thesis wording "incidents of 2026" conflicts with ruling 24.
- `15-payment-reconciliation-and-reporting` line 39 and the ledger's `41-safe-change` line call the Keel reconciliation "nightly" while the `15` ledger line says it does not run at a fixed hour.
- `48` (`stripe-and-adyen-bets-compared`), `part-10` and `introduction` did not exist on disk when this pass ran.
