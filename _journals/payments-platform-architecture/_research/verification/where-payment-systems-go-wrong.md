# Verification — where-payment-systems-go-wrong (`where-payment-systems-go-wrong`)

Verification pass of 17 November 2026. This is a preface page with no external sources of its own, so section A of the reviewer brief was applied in its changed form: each statement about a provider, a network, a standard or a regulation was checked against the **current text of the chapter that owns it** (after that chapter's own verification pass, rulings 18–35 and `_research/verification/*.md`). No URL was fetched for this page; the owning chapters' verification files are the evidence for the underlying sources. Chapters 25, 26 and 29–50 had no verification file when this pass ran; their text was read as it stood.

Counts: **38 claims** checked — 36 confirmed, 1 corrected (wording brought into line), 1 hedged, 0 unsupported, 0 unreachable.

## A. Claims about providers, networks, standards and law

| # | Claim on this page (short) | Owning chapter (permalink; folder) | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe and Adyen both accept an idempotency key | `idempotency-and-retries`; 18 | confirmed | — |
| 2 | Key remembered "at least 24 hours on Stripe's API v1 and 7 to 14 days on Adyen" | 18 (key point, lines 15, 114, 120); ruling 13 | confirmed | — |
| 3 | Stripe's PaymentIntent can be read back by its identifier | `payment-state-machines`; 08 (lines 15, 112, 190) | confirmed | — |
| 4 | Adyen's Checkout API has no endpoint that returns a payment; confirmation is the webhook and later the settlement report | 08 (lines 15, 190, 198); rulings 12 and 29 | corrected | Scope "Checkout API" was already there (ruling 29). Added "by its identifier", the owning chapter's wording: the Checkout API does have payment endpoints, none that returns a payment by identifier. |
| 5 | Other payment methods answer days later | `local-payment-methods`; 07 | confirmed | — |
| 6 | A refund is a new transaction that can itself fail | `refunds-reversals-and-disputes`; 04 (lines 73–82) | confirmed | — |
| 7 | A chargeback can arrive for about 120 days after a sale under Visa's public rules | `journey-of-a-payment`; 01 (lines 14, 112) and 04 (line 15: 120 days from processing for most disputes, up to 540 in some) | confirmed | "about" covers the processing-date count and the longer cases. |
| 8 | Refunds, chargebacks, fees and holds are booked on a balance when they occur, each with its own date | `balances-and-funds-flows`; 13 (lines 16, 90, 98) | confirmed | — |
| 9 | "Paid" means sent: the provider debits the balance when it instructs the transfer; a bank network delivers on its own schedule | `payouts-and-money-movement`; 14 (lines 14, 26); ruling 18 | confirmed | Does not say the payout waits for network settlement, so ruling 18 is respected. |
| 10 | Stripe: a failed payout "might initially show as `paid`" | 14 (line 123, quoting the Payout object reference) | confirmed | Quotation matches the chapter's. |
| 11 | Adyen: a non-instant payout "cannot fail" but can be returned | 14 (line 142) | confirmed | — |
| 12 | An event is sent again until the endpoint acknowledges it or a retry window closes | `payment-webhooks-and-events`; 20 (lines 14, 29) | confirmed | — |
| 13 | Stripe retries for up to three days and does not guarantee order | 20 (lines 39, 79, 81) | confirmed | — |
| 14 | Adyen wants an acknowledgement within 10 seconds and queues a failing endpoint's events for up to 30 days | 20 (lines 15, 77, 79) | confirmed | The page does not call the 10-second rule recent (chapter 20 correction 11 not triggered). |
| 15 | A dispute's response deadline starts with a single event | 04 (callout, line 22; lines 122–124) | confirmed | — |
| 16 | Stripe's version comes from the account default, a request header or, since 2023, the client library's release | `payment-api-versioning`; 19 (lines 15, 39) | confirmed | — |
| 17 | Adyen puts a version number in the URL of each API | 19 (line 15) | confirmed | — |
| 18 | Under EU law a SEPA direct debit can be refunded without a reason for eight weeks and contested as unauthorized for thirteen months | 07 (lines 15, 83: PSD2 Articles 76, 77 and 71) | confirmed | — |
| 19 | An iDEAL payment cannot be disputed through the payer's bank | 07 (lines 15, 67) | confirmed | — |
| 20 | A provider token works only at the provider that holds the card | `tokenization-vaulting-and-pci`; 22, and `payment-routing-and-orchestration`; 10 (line 16) | confirmed | — |
| 21 | Moving stored cards is a transfer between two vaults that takes weeks and that the merchant cannot perform itself | 22 (lines 16, 21, 185) | confirmed | — |
| 22 | "neither Stripe nor Adyen documents whether [network tokens] survive a move" | 10 (line 16, confirmed in its file, row 91); 22 (row 85, hedged to "pages cited here"); `network-tokens`; 23 (line 177); ruling 31(a) | hedged | Chapters 22 and 23 limit the statement to the pages read, and an Adyen export article is listed whose procedure could not be read. Now: "no Stripe or Adyen page I read says whether they survive a move", with `[[network-tokens]]` added beside `[[payment-routing-and-orchestration]]`. |
| 23 | PCI DSS binds every system a card number passes through or can affect | 22 (lines 14, 42, 44) | confirmed | — |
| 24 | Hosted fields lead to the shortest self-assessment questionnaire, SAQ A | 22 (line 14) | confirmed | — |
| 25 | Since 31 March 2025 a merchant filing SAQ A must confirm that scripts on the page cannot attack the form | 22 (lines 16, 36, 169) | confirmed | — |
| 26 | Card testing leaves no dispute for a fraud model to learn from and must be stopped before authorization, by limits on the endpoint | `payment-fraud-and-risk`; 24 (line 16) | confirmed | — |
| 27 | Stripe and Adyen both hold verification as requirements with deadlines that switch capabilities on and off | `payment-compliance-and-regulation`; 26 (lines 15, 77); ruling 2 | confirmed | — |
| 28 | The law obliges a provider to know a business for as long as it serves it | 26 (line 14) | confirmed | — |
| 29 | A routing layer unifies the authorization request and nothing after it (disputes, settlement, balances, stored cards stay per provider) | 10 (lines 14, 27) | confirmed | The chapter's own claim, repeated as such. |
| 30 | Stripe: 100 requests a second per account in live mode and 25 per endpoint | `payment-developer-platform`; 21 (lines 15, 101–103); ruling 5 | confirmed | — |
| 31 | Adyen publishes no limit for payments, so a throughput has to be agreed in advance | 21 (lines 15, 108, 185) | confirmed | Scoped "for payments", as chapter 21 requires (Adyen gives figures for other APIs). |
| 32 | An HTTP 429 means the payment was not tried; it is not a decline | 21 (line 16) | confirmed | — |
| 33 | Stripe's 2017 post describes four limiters; evidence age 9 years | 21 (lines 22, 81) | confirmed | Evidence-age mark present and correct (2017 to 2026). |
| 34 | 152,000 a minute, reported by Stripe's newsroom for the Black Friday weekend of 2025, is load for all customers together | `payment-peak-load`; 40 (lines 25, 37, 87, 91) | confirmed | — |
| 35 | A platform stays outside the rules for holding funds only while it never has possession or control | `licences-and-safeguarding`; 16 (lines 5, 16) | confirmed | — |
| 36 | Stripe Custom connected accounts are seller accounts the platform creates and manages | `platform-payment-models`; 33 (line 125 and the Larkfield section); ruling 23 | confirmed | — |
| 37 | Stripe offers an embedded onboarding component | `platform-onboarding-and-verification`; 34 (line 89) | confirmed | — |
| 38 | An acquirer is the licensed institution that connects a merchant to the card networks | `acquiring-and-network-connectivity`; 06 | confirmed | Definition only; the page makes no statement about who acquires for Stripe or Adyen (rulings 11, 27). |

Links: the page has no external URL (ruling 22 holds). Every `[[permalink]]` on the page is in the style guide's valid list (checked by script).

## B. Chapters listed under "Where this book helps" against the chapters' callouts

Each chapter's `FAILURE PATTERNS THIS CHAPTER ADDRESSES` callout was read by script. Every chapter the page already listed names the pattern it is listed under (16 of 16 lines, 42 links). Chapters 42–50 were unwritten when the page was drafted; the links below were added.

| Pattern | Already listed (all confirmed in the callouts) | Added from chapters 42–50 |
| --- | --- | --- |
| The Double Charge | 18, 02, 37 | `journey-failed-renewal` (43) |
| The Phantom Payment | 08, 20, 07 | `journey-card-payment` (42), `journey-failed-renewal` (43), `payments-what-is-moving` (50) |
| The Orphaned Refund | 04, 12, 35 | `journey-platform-payment` (44), `journey-dispute` (45) |
| The Black-Box Balance | 13, 15, 12 | `journey-card-payment` (42), `journey-platform-payment` (44), `case-stripe` (46) |
| The Stranded Payout | 14 | `journey-card-payment` (42). The sentence "It is the one chapter that lists this pattern" was removed: it is no longer true. |
| The Trusted Doorbell | 20, 08, 15 | `journey-dispute` (45) |
| The Version Cliff | 19, 41, 31 | none names it |
| A Card by Any Other Name | 07, 08, 04 | `payments-what-is-moving` (50) |
| The Vault Hostage | 22, 23, 10 | none names it |
| The Card in the Log | 22 | none names it ("the one chapter" still true) |
| The Open Till | 24 | none names it ("the one chapter" still true) |
| The Frozen Seller | 26, 34, 36 | none names it |
| The Single Rail | 10, 37, 06 | `case-adyen` (47), `payment-contrast-cases` (49) |
| The First of the Month | 40, 21, 27 | `journey-failed-renewal` (43) |
| The Borrowed Blueprint | 40, 38, 12 | `case-stripe` (46), `case-adyen` (47), `payment-contrast-cases` (49), `payments-what-is-moving` (50) |
| The Accidental Bank | 16, 33, 36 | `journey-platform-payment` (44), `journey-dispute` (45), `case-adyen` (47), `payment-contrast-cases` (49) |

Not checked: chapter 48 (`stripe-and-adyen-bets-compared`) and the `part-10` intro did not exist on disk when this pass ran. When chapter 48 is written, read its callout and add it to the lines of the patterns it names.

Inline chapter references inside "Why it happens" and "Remedy direction" paragraphs point to the chapter that owns the fact (section A), which in each case also names the pattern or is cited only as the source of the fact (`journey-of-a-payment` for the 120 days; it does name The Orphaned Refund).

## C. Larkfield consistency (against the ledger as it stands)

All figures, dates, names and decisions were compared with the base ledger and every "Additions by chapter" line. Weekday checked: 14 September 2026 is a Monday.

| Item | Status | What changed |
| --- | --- | --- |
| The Double Charge: 1 November 2026, new key from the HTTP layer, 1,840 members, €71,300, 212 disputes; K1 key = membership, billing period, number of the scheduled attempt | agrees (base ledger, `18` line, ruling 13) | — |
| Phantom Payment: direct debit marked `paid` on acceptance; 325,000 debits a month, 1.5% assumption, about 4,900 | agrees (`07` line) | — |
| Orphaned Refund: 18 March 2027, €84.00, studio paid 11 March, Aylin Demir's question; €317,200 and €73,500 at year-end 2025 | agrees (`12`, `33`, `44` lines) | Label changed, see D. |
| Black-Box Balance: €412,000 higher at year-end 2025, found in January 2026, three causes, audit finding | agrees (ruling 24) | — |
| Stranded Payout: June 2026, 412 payouts, €386,000, three weeks, 19 days, two studios; four payout states and the account-holder check | agrees (`14` line) | "(K3)" added, see D. |
| Trusted Doorbell: Monday 14 September 2026, shortly after midnight, 9 hours, 3,200 memberships, 460 tickets; K2 wording | agrees (ruling 20; K2 as in the ledger) | — |
| Version Cliff: March 2026, 6 days, field removed by a breaking release | corrected | The page said the integration "had run for three years on an old account default". Now says why: it "sent no API version, so it had run for three years on Stripe's account default" (ledger base line and `19` line). |
| A Card by Any Other Name: Daan Peters, 1 April 2027, 27 May 2027, 1 May 2028; returned debit recorded as `disputed` on the Adyen side | agrees (`07` line) | — |
| Vault Hostage: K8 moves only payments that bring their own card; exit sheet per provider | agrees (`10`, `22` lines) | "under K4" added, see D. |
| Card in the Log: 17 scripts from 9 domains, 4 with no owner, 3 from 2 under K4 | agrees (`22` line) | — |
| Open Till: 8–9 August 2026, 61,000, €4,100, 31 hours; CAPTCHA, cap, alert | agrees (`24` line) | — |
| Frozen Seller: May 2026, 230 studios, up to 12 days, Stripe, legacy Custom connected accounts, own forms since 2017, embedded onboarding under K6 | agrees (rulings 2 and 23; `26`, `34` lines) | — |
| Single Rail: 50 largest studios, quarterly rehearsal to payout, refund and reconciliation; terminals stay on Adyen | agrees (`10`, `11` lines) | — |
| First of the Month: 38% in 6 hours, 1 October 2026, Stripe's rate limit, 7,900; K5 over 18 hours | agrees (`21`, `40` lines) | — |
| Borrowed Blueprint: February 2027 orchestration proposal; April 2027 objection with 152,000 a minute against about 1,000 renewals a minute | agrees (`10`, `40` lines) | — |
| Accidental Bank: April 2027 refund buffer, 14 days, about €43 million, rejected by Jonas Weber | agrees (`16` line) | — |
| Chain paragraph: 1 November 2026 after the 7,900 of a month earlier; K5, K1, K2; no orchestration product | agrees | — |
| "eight incidents (seven in 2026, one found in its 2025 year-end books)" | agrees (ruling 24) | — |

## D. Agreement with `meet-larkfield` (and its ledger line)

| Point | `meet-larkfield` and ledger line | This page before | Resolution |
| --- | --- | --- | --- |
| K3 answers The Stranded Payout | K3: Black-Box Balance, Orphaned Refund, Stranded Payout | The Stranded Payout's remedy named no K decision | "(K3)" added to "a return is a new ledger entry linked to the payout"; K3 lists payouts and returns as entries. |
| K4 answers The Vault Hostage | K4: Card in the Log and Vault Hostage | The Vault Hostage entry named only K8 | The exit sheet is now said to be kept "under K4" (ledger `22` line puts it there); K8 stays as the reason the switch excludes stored cards. |
| The Unexplained €0.4 Million = Black-Box Balance, with Orphaned Refund | as stated | Orphaned Refund was labeled "no named incident" while using the incident's figures | Label now "no incident of its own"; the figures are named as "most of the Unexplained €0.4 Million, the incident told under the next pattern". |
| The Silent Webhook = Trusted Doorbell, noticed as Phantom Payment | as stated | Phantom Payment was labeled "no named incident" with no pointer; the chain section and the closing already said the Phantom Payment began at a Trusted Doorbell | Label now "no incident of its own", with one sentence: "The Silent Webhook (under The Trusted Doorbell) was noticed as this pattern." |
| Other six incidents and K1, K2, K5, K6, K7, K8 | — | agree | — |
| The Card-Testing Weekend has no K number | as stated | agrees (remedy names no K) | — |

## E. Format (section B of the brief)

- No external URL in the running text. Hand-off uses `[[meet-larkfield]]`.
- "reserves" was used in the paragraph after the table before it was defined; the one-clause definition was moved to that first use (and removed from the later one).
- Length: the added links first took the page to 6,626 words against the spec's limit of 6,500; the added sentences were cut to a plain "also names it" form and the page is at 6,498 words (`timetoread` stays 28 min).
- Three KEY POINTS; no failure-patterns callout (this page is the catalog). American spelling; no banned word found.
- No unit was added, dropped, merged or reordered. The controlling ideas of eleven "where this book helps" units and the open questions were updated in `spec.json` to name the added chapters.

## Could not verify

- Chapter 48 and the part 10 intro did not exist; see B.
- Chapters 25, 26 and 29–50 had not been through their own verification pass (no file in this folder). Claims 27, 28, 34, 36 and 37 and all links added in B rest on those chapters' current text and should be re-read if their verification changes it.

## Ledger conflicts

- None that touches this page. (The base ledger's worked-example line still says the payout "is sent on Thursday 11 March and, in the best case, reaches the studio's bank the same day"; this page only says the studio "was paid on 11 March", which is the payout date.)

## For other pages

- `journal-spec.json`: the part-level outcome still says "eight incidents in 2026" and the `meet-larkfield` entry's AC-2 expected answer still says "Saturday night" and "Sunday morning" (rulings 24 and 20); already noted in this page's spec.
- `introduction`: the folder did not exist when this pass ran. This page's `[[introduction]]` link therefore resolves to another journal's page (`../agentic-systems-architecture/introduction.html`), and the render check reports it as `XJ:`. The permalink is the valid one for this book, so the link was left unchanged; the entry clears when this book's introduction is built. Re-run `render_check.py where-payment-systems-go-wrong` then. This is the only render-check finding on the page.
- `10-routing-and-orchestration` key point 3 says flatly "Neither Stripe nor Adyen documents whether network tokens survive a move"; chapters 22 and 23 limit the same statement to the pages read (ruling 31a). The three should use one wording.
- Chapters before 42 that name a pattern in their callout but are not listed on this page (by design, three per pattern): for example The Double Charge is also named by 10, 17, 27, 28, 29, 38 and 40; The Phantom Payment by fifteen further chapters; The Borrowed Blueprint by 09, 19, 21, 23, 24, 25, 28, 33, 39 and 41. No action needed unless the author wants complete lists.
