# Verification — 48-the-bets-compared (`stripe-and-adyen-bets-compared`)

Verification pass of 17 November 2026. The page introduces no new fact, so every company statement was checked twice: (1) against the chapter that owns it, as that chapter reads today after the absence audit (rulings 41–46), including its "Stripe and Adyen: Where They Differ" table and the two cases; (2) against the source, fetched in this session (curl; PDFs converted with pdftotext). All 32 URLs in the original Sources section returned HTTP 200, and so did the 16 added. Quotations were matched by script, character for character after normalizing typographic quotes and white space.

Short names: **AR** = Adyen Annual Report 2025, the PDF behind "Download" on `investors.adyen.com/financials/2025` (233 pages, a "printed version"); **Q3** = the four-page PDF linked from `investors.adyen.com/financials/q3-2026-10c88s`; **GA** = Georgia Department of Banking and Finance, May 2026 Monthly Bulletin (PDF listed on the page cited); **OCC** = Corporate Decision #1365 (PDF); **AD** = Stripe's acquirer disclosure; **L22**, **L24** = Stripe's annual letters for 2022 and 2024, read in the PDFs the letter pages link (the HTML pages render the text client-side). "ch. N" is the owning chapter's current text.

Sources the writer had marked "not fetched again" — all fetched and read in this pass: AR, Q3, GA, OCC, the ICBA item, L22, the Sessions talk transcript, the Stripe Payments Company terms, the Design to Duty post. The notes were removed from the source entries.

## The writer's own counts

| Count | Check | Result |
| --- | --- | --- |
| "forty-one tables and about 250 rows" | Script over `posts/*/index.md`: sections titled "Stripe and Adyen: Where They Differ", body rows of the first table | 41 tables, 253 rows: confirmed |
| "Four of its cells changed in 2026 alone" | The four dated items are events: Metronome (14 January) and Managed Payments (22 April) both change the same Stripe cell (billing); the Georgia bank changes Stripe's acquiring cell; the 1 July closings change two Adyen cells (build or buy, billing); Metronome's completion arguably changes a fifth (Stripe, build or buy) | Corrected to "Four events of 2026 alone changed cells of the map" (spec p41 reworded to match) |
| "eight bets"; "two of kind, five of default, sequence or degree, one not like-for-like" | Map rows and the Kind column | 8 rows; Kind 2, Degree 1, Sequence 2, Default 2, not like-for-like 1: confirmed |
| 14 countries and regions with an Adyen acquiring connection | Headings of the Adyen page: AU, HK, IN, JP, MY, NZ, SG, EU, UK, CA, US, BR, MX, UAE | 14: confirmed |
| "ten named purchases since 2020, two not confirmed closed" | ch. 46 table: Paystack, TaxJar, Bouncer, Recko, Lemon Squeezy, Bridge, Privy, Metronome, OpenRouter, Parafin | 10 and 2: matches the owner |

## Claims

| # | Claim (short) | Owner / source | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | "Payment Method Acquirer is Stripe Technology Europe, Ltd." (EEA) | ch. 46; AD | confirmed | — |
| 2 | Q3 2026: Platforms "allows us to provide payments and financial products to smaller merchants, which will be a key driver of future growth" | ch. 47; Q3 | confirmed | — |
| 3 | Adyen N.V. "is authorised as a credit Institution under the supervision of Dutch Central Bank" | ch. 47; adyen.com/licenses/emea | confirmed | — |
| 4 | License dated to 2017; US federal branch (2021); UK branch authorized as a bank (2023) | ch. 47; releases of 14 June 2021 and 7 September 2023; license pages (EMEA, United States) | confirmed | — |
| 5 | Stripe's Irish and UK companies are e-money institutions | ch. 46, ch. 16 (legal pages 2019, 2017; both named in the current AD) | confirmed against the owner; legal pages not re-read here | — |
| 6 | "a U.S. state-licensed money transmitter" (terms updated November 2025) | ch. 46; stripe.com/legal/spc, "Last updated: November 18, 2025" | confirmed | — |
| 7 | "Stripe is not a bank. Checking accounts are provided exclusively by Fifth Third Bank, National Association, Member FDIC." | ch. 46; docs.stripe.com/treasury.md | confirmed | — |
| 8 | Stripe: safeguarding accounts at unnamed credit institutions (EU, UK; 2024 FAQ) | ch. 16 table, row "Where customer funds sit" | confirmed against the owner; FAQ not re-read here | — |
| 9 | Adyen: business-account deposits at Adyen N.V. under the Dutch deposit guarantee | ch. 16; ruling 33f; depositor information sheet | confirmed | — |
| 10 | Adyen terms (2023): balances "held by Adyen prior to Settlement"; at which banks not public | ch. 16; Adyen Terms and Conditions, last update 1 November 2023 | confirmed | Source entry added |
| 11 | Sales Day Payout terms (17 June 2024): pays "irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner" | ch. 47; terms page | confirmed | — |
| 12 | Pre-financing capped at 30 days | ch. 47; docs "Prefinancing is capped at 30 days" | confirmed | — |
| 13 | Stripe documents paying ahead only for Instant Payouts | ch. 3 and ch. 16 tables; ruling 18 | confirmed against the owner | — |
| 14 | AR calls paying only after funds are received the "default setup"; ch. 47 could not reconcile | ch. 47; AR risk section | confirmed | — |
| 15 | Lender: partner banks and outside lenders at Stripe; Adyen itself | ch. 36 table, row "License behind the products" | confirmed against the owner | — |
| 16 | Georgia bulletin of May 2026: approved 30 June 2025, began business 28 May 2026 | ch. 46; ruling 33a; GA ("Stripe MALPB, Atlanta, Georgia, 06/30/2025, 05/28/2026") | confirmed | — |
| 17 | February 2026: "preliminary conditional approval" for Bridge's trust bank; no final approval found | ch. 46; OCC (12 February 2026: "The OCC has granted preliminary conditional approval only") | confirmed | Gloss of "trust bank" added |
| 18 | Neither charter takes deposits; Georgia banks "may not solicit or accept deposits from the general public" (ICBA, July 2025, secondary) | ch. 46; ICBA item of 8 July 2025; OCC: the bank "will not be an insured depository institution" | confirmed | — |
| 19 | Adyen's reason: "the speed and autonomy that come from not relying on external parties for regulatory compliance" | ch. 6, ch. 47; AR | confirmed | — |
| 20 | Stripe has published no reason for its route | ch. 6 ("Not public"), ch. 46 "Where the Evidence Stops" | confirmed against the owners | — |
| 21 | Not public: Stripe's safeguarding banks; split of Adyen's balances between central and commercial banks | ch. 46, ch. 47 "Where the Evidence Stops" | confirmed against the owners | — |
| 22 | AD names a Stripe company as acquirer in the EEA, the UK, Brazil and much of Asia-Pacific | ch. 6; AD (Stripe entities for the EEA, UK, Gibraltar, Switzerland, Brazil, Australia, Hong Kong, Malaysia, New Zealand, Singapore) | confirmed | — |
| 23 | "Stripe, LLC is a Payment Facilitator of" six acquirers, five banks and its own Georgia bank | ruling 33b; AD (Cross River, Deutsche Bank Trust Company Americas, Fifth Third, Pathward, PNC, Stripe MALPB) | confirmed | — |
| 24 | AD also names acquirers in Canada, Japan (card companies), India, Thailand, the UAE; Mexico both acquirer and facilitator | ruling 27a; AD | confirmed | — |
| 25 | "Of processed volumes, 84% were full-stack volumes" | ch. 47; AR | confirmed | — |
| 26 | 14 countries and regions with an "Adyen acquiring connection" | ruling 27b; docs.adyen.com/account/supported-currencies | confirmed | — |
| 27 | Concentration risk "primarily at banking partners in locations where there are no own direct acquiring licenses" | ch. 47; AR | confirmed | One-clause gloss of "concentration risk" added |
| 28 | License pages name an acquiring entity for some markets (Japan, Singapore); no complete list per country | ruling 46j; ch. 6, ch. 47; license pages Japan ("Registration as Merchant Acquirer") and Singapore ("merchant acquisition") | confirmed | — |
| 29 | "wrong for Europe and roughly right for the United States" | ch. 46 (the author's words there) | confirmed | — |
| 30 | Network tokenization "only applicable for payments acquired by Adyen" | ch. 23; docs.adyen.com/online-payments/network-tokenization | confirmed | Source entry added |
| 31 | Adyen documents payments settled by an external acquirer (own American Express agreement) | ch. 10 table; ruling 31c | confirmed against the owner | — |
| 32 | Neither publishes volume per acquirer; Stripe says nothing on which merchants the Georgia bank acquires for; Adyen's 84% has no breakdown | ch. 6, ch. 46 | confirmed against the owners | — |
| 33 | Neither lists its card-network memberships per country | ch. 6 ("by network and country") | confirmed against the owner | — |
| 34 | Ten named Stripe purchases since 2020; OpenRouter and Parafin not confirmed closed on 17 November 2026 | ch. 46 | confirmed against the owner; the newsroom list was not re-read here | — |
| 35 | AR: "a single platform built entirely in-house" | ch. 47; AR | confirmed | — |
| 36 | 1 July 2026: Talon.One and Orb closed; history page lists no earlier acquisition | ch. 47; closing release ("Both transactions officially closed on July 1, 2026"); About page | confirmed | — |
| 37 | "Adyen builds and never buys" is in no Adyen document read | ruling 16; ch. 47 | confirmed against the owner | — |
| 38 | Both build core systems in-house or on open source | ch. 41 table, row "Software and hardware" | confirmed against the owner | — |
| 39 | Metronome completed January 2026; documented as a product path beside Stripe's own | ch. 28, ch. 46; Stripe release of 14 January 2026 | confirmed | — |
| 40 | Lemon Squeezy (2024) stops processing on 31 March 2027 "after Stripe rebuilt its function" | ch. 32; Lemon Squeezy post of 16 November 2026 | **corrected** | "Stripe … rebuilt it on its own platform" is the owner's inference column, and the Lemon Squeezy post says Managed Payments is not "a like-for-like replacement". Now: "while Stripe's own product for the same role has been in its API since April 2026" |
| 41 | June 2026: Orb under "an incubator model" | ch. 47; release of 11 June 2026 | confirmed | Source entry added |
| 42 | 28 October 2026: "the successful ongoing integration of Talon.One and Orb" | ch. 47; release | confirmed | — |
| 43 | "convergence" stated as intent, no date | ch. 47; release of 11 June 2026 | confirmed | — |
| 44 | "our single global platform"; "takes effect everywhere, without reintegration work" | ch. 47; AR | confirmed | — |
| 45 | "Revenue and Finance Automation Suite, with Billing at its core" (2024 letter) | ch. 46; L24 | confirmed | Source entry added |
| 46 | Adyen: several API families, own version counter and mostly own host; Stripe: one host, one object model | ch. 17 table, row "Shape of the API" | confirmed against the owner | — |
| 47 | Orchestration in private preview on 17 November 2026; cards to Adyen, Braintree and Worldpay | ch. 10; docs.stripe.com/payments/orchestration ("Orchestration is in private preview") and feature-support page | confirmed | — |
| 48 | Jon Krauss, April 2026: "You're not going to have to be locked into Stripe." | ch. 10; Sessions 2026 transcript | confirmed | — |
| 49 | "Unlike fragmented legacy architectures, Adyen brings payments onto one single platform" | ch. 10; adyen.com/uplift | confirmed | Source entry added |
| 50 | Orb "continuing to support multi-PSP environments" | ch. 47; release of 11 June 2026 | confirmed | — |
| 51 | One repository of about 50 million lines of Ruby (April 2026); no post says which products live in it | ch. 46; stripe.dev post of 9 April 2026 | confirmed | Source entry added |
| 52 | "around 3,000 live services" (2026) | ch. 47; Architect post of 23 August 2026 | confirmed | Source entry added |
| 53 | L22: "Stripe grew up with companies in the technology sector" | ch. 46; L22 | confirmed | — |
| 54 | February 2026: "the 'long tail' is much of the dog" | ch. 46; release of 24 February 2026 | confirmed | Source entry added |
| 55 | "Built for enterprise, not adapted to it." | ch. 47; adyen.com/about | confirmed | — |
| 56 | Point-of-sale volume €310.9 billion for 2025, 22% of processed volume | ch. 11, ch. 47; AR | confirmed | "One channel still shows it" (an inference in the running text) made neutral: "One channel is reported by one side only" |
| 57 | Stripe has sold terminals since 2018 and publishes no in-person figure | ch. 11, ch. 46 | confirmed against the owners | — |
| 58 | March 2023: "enterprise user base has compounded since 2019" | ch. 46; Series I release of 15 March 2023 | confirmed | Evidence-age mark added (3.5 years); source entry added |
| 59 | 312,000 active business customers (Q3 2026) | ch. 47; Q3 ("reached 312k") | confirmed | — |
| 60 | Stripe (Netherlands list): blended 1.5% + €0.25 for standard EEA cards; "IC+ pricing" among custom options | ch. 5; stripe.com/en-nl/pricing | confirmed | — |
| 61 | Adyen list: "a fixed processing fee + a fee determined by the payment method"; Interchange++; "The fees outlined above are indicative" | ch. 5; adyen.com/pricing | confirmed | — |
| 62 | October 2026: "tiered pricing structure" | ch. 47; Q3 | confirmed | — |
| 63 | Platform documentation has a fee type for blended rates; "each sells both models; only the default differs" | ch. 5 table, row "The other model" | confirmed against the owner | — |
| 64 | KEY POINTS: "each sells the other's pricing model on request" | ch. 5 | **hedged** | Stronger than the owner for Adyen (no page says a blended rate is sold on request). Now: "each sells both pricing models" |
| 65 | Negotiated markups not public at either | ch. 5 | confirmed against the owner | — |
| 66 | Payment state: PaymentIntent with `status`; Adyen result code, webhooks, Checkout API v72 without an operation that returns an online payment | ch. 8 table; rulings 12, 29 | confirmed against the owner | — |
| 67 | Idempotency keys: at least 24 hours (v1), 30 days (v2); 7 to 14 days | ch. 18; Stripe API reference; Adyen page ("7 to 14 days after first submission") | confirmed (v2 against the owner) | — |
| 68 | API version: account default, header or SDK release; an integer in each URL, no default | ch. 19 table | confirmed against the owner | — |
| 69 | Rate limit: 100 a second per live account; Adyen none published, HTTP 429 documented | ch. 21; docs.stripe.com/rate-limits.md | confirmed (Adyen cell against the owner) | — |
| 70 | Webhook retries: up to three days; up to 30 days | ch. 20; Stripe webhooks page; Adyen troubleshoot page | confirmed | — |
| 71 | Methods "generally instantaneous" in the dashboard; on request in the Customer Area | ch. 7; docs.stripe.com/payments/payment-methods | confirmed (Adyen cell against the owner) | Source entry added |
| 72 | Invoice retries on by default for new accounts; Auto Rescue off until support enables it | ch. 29; Stripe Smart Retries page; Adyen Auto Rescue for cards ("contact our Support Team or your Adyen Account Manager") | confirmed | — |
| 73 | Funds payable per transaction at `available_on`; per sales day as one batch | ch. 13 table | confirmed against the owner | — |
| 74 | Both recommend a server-created session | ch. 8 table, row "Recommended entry point" | confirmed against the owner | — |
| 75 | Each company's published uplift uses its own metric and cohort | ch. 9 table | confirmed against the owner | — |
| 76 | "get the markup, the minimum invoice and the chargeback fee in writing, because none is on its website" | ch. 5 (rows as corrected; ruling 46f); adyen.com/pricing | **corrected** | The price list shows an indicative markup ("Interchange+ + 0.60%"); a minimum invoice is published for one market (Australia) and a chargeback fee for one (CAD 24.00, Canada). Now: "the listed fees are indicative, and the other two are published for one market each" |
| 77 | "We manage our own infrastructure in several data centers around the world" (2021) | ch. 47; Design to Duty, 28 July 2021 | confirmed | — |
| 78 | Data centers "in Europe, the United States, India, Singapore, Japan and Australia"; no cities or operators | ch. 39, ch. 47; adyen.com/infrastructure | confirmed | — |
| 79 | "The majority of our CapEx is related to our data centers"; €116.8 million, 5% of net revenue | ch. 47; AR | confirmed | — |
| 80 | Stripe "has long relied on AWS to provide the core compute infrastructure on which Stripe is built"; "We couldn't run without AWS—and we wouldn't want to" (January 2023) | ch. 46; Stripe release of 23 January 2023 | confirmed | — |
| 81 | An October 2024 AWS post written with Stripe staff is consistent | ch. 46 | confirmed against the owner; not re-read here | — |
| 82 | Stripe names no AWS region; one base URL; Adyen five live regions for online payments | ch. 39 table | confirmed against the owner | — |
| 83 | Payments "stored in Europe and our isolated India environment"; Stripe states no storage location; neither promises data stays in the EU | ch. 39; adyen.com/infrastructure | confirmed (the last clause is the owner's reading of two documented cells) | — |
| 84 | Utilization "generally less than 30%"; deployment freeze around named peak days | ruling 42; docs.adyen.com/industries/peak-season | confirmed | — |
| 85 | 2026: investment pulled forward "to secure compute and storage availability" | ch. 47; H1 2026 release | confirmed | Source entry added |
| 86 | No Black Friday freeze found for Stripe (documentation, support site, newsroom) | ch. 40 table | confirmed against the owner | — |
| 87 | Adyen's stated reasons: "part historical, part legal, and part technical" (2021) | ch. 47; Design to Duty | confirmed | — |
| 88 | Load balancers "manage the failover to the other data centers"; no topology or timings | ruling 45a; peak-season page | confirmed | — |
| 89 | Stripe: nothing on failover for payments; a 2025 post on two regions for billing usage events | ruling 46g; Stripe blog of 28 January 2025 | confirmed | — |
| 90 | Availability figures form no comparable series; only Adyen's public terms carry a commitment, 99.9% a quarter by "commercially reasonable efforts" | ch. 37; Adyen terms, clause 7.2 | confirmed (Stripe "not found" against the owner) | Source entry added |
| 91 | Billing launched April 2018; "Stripe generates an invoice for every subscription billing period" | ch. 27, ch. 46; release of 5 April 2018; subscription invoices page | confirmed | Source entry added |
| 92 | Tax and revenue recognition added in 2021 | ch. 46 | confirmed against the owner | — |
| 93 | Managed Payments in a release version of the API since 22 April 2026; Stripe's company is merchant of record for digital goods | ch. 32; changelog entry of 22 April 2026 | confirmed | — |
| 94 | In Adyen's documentation a subscription is a processing model on a payment the merchant initiates | ch. 27 table | confirmed against the owner | — |
| 95 | "no invoice object, no first-party tax engine and no revenue-recognition product" found for Adyen | ch. 27, ch. 30, ch. 31; rulings 38, 39b | **hedged** | Ruling 39b: Adyen's site mentions revenue recognition, and Orb documents a product of its own. Now "no first-party tax engine or revenue-recognition product" |
| 96 | 15 September 2026: "Adyen doesn't act as a direct, third-party merchant of record." | ch. 32, ch. 47; article (displayed date September 15th, 2026) | confirmed | — |
| 97 | Nothing has changed yet for an Adyen integrator; no billing page; Orb lists Adyen as a gateway connected with an API key; "You'll soon see" (29 September 2026) | ch. 27, ch. 47; Orb documentation; Adyen article | confirmed | Source entry added |
| 98 | Connect dates from October 2012 | ch. 46; Stripe blog of 23 March 2015 | confirmed | — |
| 99 | Platforms pillar: €263.8 million net revenue in 2025 | ch. 47; AR | confirmed | — |
| 100 | Stripe: one account per seller, merchant per payment by charge type; Adyen: legal entity, account holder, balance account, transfer instrument; booking by instruction | ch. 33 table | confirmed against the owner | — |
| 101 | Adyen split that cannot be booked goes to the liable balance account without an error; a failed Stripe transfer returns one | ch. 35 table and text | confirmed against the owner | — |
| 102 | Stripe as loss bearer is a per-account setting: "You can't update their values later." | ch. 33; Stripe page (the `.md` copy uses a typographic apostrophe) | confirmed | — |
| 103 | Adyen: negative balance for up to 30 days, then the reserved compensation account | ruling 41a; docs "Adyen allows negative balances for up to 30 days" | confirmed | — |
| 104 | Managed Risk: Adyen will "assume the responsibility for negative balances", write-off after 180 days; pilot, limited availability | ruling 41b; docs.adyen.com/platforms/managed-risk | confirmed | — |
| 105 | "Stripe's reach per country depends on a partner, Adyen's on where its license extends" | ch. 36 table, last column | **hedged** | That sentence is the owner's inference column, stated here as fact outside a block. Replaced with the two documented cells: "Stripe's rest on partner banks and outside lenders, Adyen's on its own licenses" |
| 106 | Accounts for a platform's sellers generally available at neither | ch. 36 table | confirmed against the owner | — |
| 107 | Not public: Adyen's platform price list; how either underwrites sellers | ch. 33 table; ch. 24 "Where the evidence stops" | confirmed against the owners | Link to the owner of the underwriting statement added (`[[payment-fraud-and-risk]]`); it had none |
| 108 | On Stripe the loss decision fixes who may collect verification data | ch. 34 table, row "Who may collect" | confirmed against the owner | — |
| 109 | Map, Stripe and Adyen cells (16 cells) | each repeats a claim above with its year | confirmed cell by cell | — |
| 110 | Map reading: "the map therefore shows an order of construction" | ch. 46 and ch. 47 keep this reading inside INFERENCE blocks | **hedged** | Now marked in the sentence as the author's reading, "as I read the two cases"; "neither company describes itself so" |
| 111 | "Every entry dated 2025 or 2026, on either side, moves toward the other's position." | the map itself | **corrected** | False of the map's own entries: Adyen's 2025 entries are standing facts, and Stripe's merchant-of-record product (2026) moves away from Adyen's stated position. Now: "The steps of 2025 and 2026 that changed a row narrowed it: that bank on acquiring, those purchases on build or buy and on billing" |
| 112 | No entry makes Stripe a deposit-taking bank; none moves either company's machines | claims 16–18, 77–80 | confirmed | — |
| 113 | Decision aid, seven rows: each middle cell is a documented difference | claims 91–97; 56–57; 60–63; 3–9 and 102–104; 23 and ch. 1 row "Role in the United States" (acquirer per payment not public); 82–83; 69 | confirmed; no row rests on an inference | — |
| 114 | Four things that do not decide: size; volume (figures measure different things); availability series; approval-rate claims | ch. 5, ch. 37, ch. 9 | confirmed against the owners | Volume sentence shortened |
| 115 | Large merchants "typically work with multiple payment service providers to mitigate their own single-point-of-failure risk" | ch. 47; AR | confirmed | Lead-in now "large enterprise merchants", as the report has it |
| 116 | Four dated events of 2026: Metronome 14 January; Managed Payments 22 April; Georgia bank 28 May; Orb and Talon.One 1 July | claims 39, 93, 16, 36 | confirmed; the count sentence **corrected** (see counts) | "Four of its cells changed" → "Four events of 2026 alone changed cells of the map" |
| 117 | Take-away bullets and author's synthesis | repeat claims above | confirmed | Two bullets shortened; nothing strengthened |
| 118 | "What remains of each starting point is a set of defaults" | the author's reading; the page's own INFERENCE block | **hedged** | A reason stated outside the block; now "by my reading (labeled below)" |

| 119 | Stripe standard payouts: services terms (28 September 2026) count "a delay or failure of a Financial Provider to settle a Transaction to Stripe" as a "Payout Delay"; no pre-financing stated | ruling 47e; ch. 3, ch. 13; stripe.com/legal/ssa-services-terms (definition read) | confirmed | Added on the coordinator's instruction; quoted from the definition, which says "Financial Provider", not "network"; source entry added |
| 120 | Adyen pre-financing caveat: AR "default setup" of paying "only after funds have been received" beside terms that pay irrespective of receipt; not reconciled in public text | ruling 47m; ch. 13; AR | confirmed | Reworded to chapter 13's current wording; link to `[[balances-and-funds-flows]]` |
| 121 | Both state network membership in general terms; Adyen: "principal membership of Visa and Mastercard in major markets" (3 July 2026); neither lists networks and countries | rulings 46j, 47j; ch. 6; Adyen article (displayed date July 3rd, 2026); Stripe MALPB terms ("a member of the Networks") | confirmed | Replaces "Neither lists its card-network memberships per country"; map row for acquiring now reads "an entity named for some markets" and "a complete list"; source entries added |

Totals: 121 claims checked: 112 confirmed (about a third of them against the owning chapter only, as marked), 4 corrected (40, 76, 111, 116), 5 hedged (64, 95, 105, 110, 118), 0 unsupported, 0 unreachable.

## Classing of the map, and reasons

Each row's class rests on documented cells: money (kind: a credit institution against "not a bank"), acquiring (degree: both acquire, in different places), build or buy (sequence: purchases since 2020 against purchases in 2026), platform or suite (not like-for-like: an operating statement against a packaging statement), first customers (default: the published price model), hosting (kind: own data centers against AWS), billing (sequence: 2018 against 2026), platforms (default: a setting against a default with a pilot). Seven INFERENCE blocks hold the reasons. Three sentences outside them carried a reason or a reading as fact and were changed (claims 105, 110, 118; and "One channel still shows it" in claim 56). The section title "First Customers, and the Defaults They Left Behind" still asserts the link; the first paragraph now labels it. Left as is, because the title is fixed by the spec and the roadmap.

## Conflicts between owning chapters that this page had to choose between

1. **Adyen's acquiring entities.** Chapter 1's table cell still reads "No acquiring entity named per country", while its own text below the table, chapter 6 and chapter 47 say the license pages name an entity for some markets and that no complete list is public (ruling 46j). The page follows chapters 6 and 47.
2. **Adyen's fees on its website.** Chapter 5's table and "where the record stops" paragraph give a listed indicative markup (0.60%), a minimum invoice published for one market and a chargeback fee for Canada; its advice sentence after the table still says "none is on the website". The page had copied the advice sentence; it now follows the table.
3. **Lemon Squeezy.** Chapter 32's table gives "Stripe bought the capability and then rebuilt it on its own platform" as the author's reading (last column) and quotes Lemon Squeezy saying the new product is not "a like-for-like replacement"; chapter 46 calls the pair "built" and "bought" and labels "replaced and not merged" as inference. The page had the reading as fact; it now gives only the dates.
4. **A failed Adyen split.** Ruling 41c says a split naming a wrong account goes to a "reserved incorrect splits account"; chapter 35's table and text say a split naming a missing or closed balance account is booked to the liable balance account. The page follows chapter 35's table; Adyen's liable-accounts page names both accounts, so the two are probably different cases, which chapter 35 should say.
5. **Pre-financing.** Adyen's terms and its annual report disagree ("irrespective of whether the funds are actually received" against the "default setup"); chapter 47 reports both. The page carries the hedge unchanged.

## "Not public" cells

The map's last column repeats the owners' statements, re-checked in the absence audit. Spot checks in this pass: Adyen's documentation index for "pricing" and "fees" under platforms (found only a compliance page on how a marketplace discloses its own fees: no price list); both documentation indexes for "underwrit" (nothing); Stripe's index for "safeguard" (no page naming banks); adyen.com sitemap for license pages (twelve country pages, no list of acquiring entities per country). Nothing overturned.

## Could not verify, and what was done

- Claims marked "against the owner" were not re-read at the source in this pass: they are not among the page's load-bearing sources and are sourced in the linked chapter, as the Sources section says.
- Stripe's two annual letters render their text in the browser; they were read in the PDFs the letter pages link.
- Launch dates older than three years (Connect 2012, Billing 2018, terminals 2018) carry no evidence-age mark in the text, following chapter 46 ("The releases are old, which does not weaken a launch date").

## Larkfield (step C)

Agrees with the ledger: October 2027; Sofie Vermeer, Daniel Osei and his two slogans; Femke de Graaf; team of 11; 56% (€627 million) and 44% (€493 million); 1,140 studios; Tuesday 9 March 2027 and €120.00; K2, K3, K7, K8; 50 largest studios; €24.5 million; 0.6% + €0.15 and €0.61 as assumptions; Stripe Billing since 2018; legacy Custom accounts with destination charges; "effect not measured"; the decision to keep both. One fix: the card and the decision paragraph named Adyen N.V. as acquirer without the label the ledger requires ("labeled as inference wherever it is stated"); both now say it is Larkfield's reading of Adyen's license page, as chapter 6's inventory does.

**Ledger conflicts:** none.

## Format (step B)

No external URL in the running text. All `[[permalinks]]` valid (one added: `payment-fraud-and-risk`). Exactly three KEY POINTS; callouts in order. `timetoread` 28 = word count ÷ 230 (see Length). Sources: nine "not fetched again" notes removed after fetching; 16 entries added for quotations and facts that had none (the last three: Stripe's services terms, Adyen's Japan and Singapore license pages, the article of 3 July 2026; plus (2024 letter, February 2026 release, Series I release, the monorepo post, Payment Methods API, subscription invoices, the Orb release, the Orb article, the H1 2026 release, the Architect post, the Uplift page, Adyen's terms, network tokenization).

**Length.** 6,478 → about 6,470 words (cap 6,500; see the final count in the report). The trims removed about 150 words of restatement; the corrections and the three rulings carried in afterwards (46j, 47e, 47m) added about as many. The request was to move toward 6,000. What is left is dated evidence, four tables (about 950 words) and one recommendation paragraph per bet; a further 400 words cannot come out without cutting evidence or a unit. For the author to decide.

## For other pages

- `01-journey-of-a-payment`: table cell "No acquiring entity named per country" contradicts the chapter's own text below the table and ruling 46j.
- `05-payment-economics`: "because none is on the website" (after the table) contradicts the table's rows.
- `35-splits-balances-and-platform-payouts`: say how the "reserved incorrect splits account" (ruling 41c) relates to the booking to the liable balance account.
- `journal-spec.json`, this entry: still lists "the acquiring entity per country at Adyen" among the undecidable things, and "its acquiring entity per country" in `how_why`; scope both to "a complete list" (ruling 46j). The post spec copies them and validates.

## Rulings 46–48 (coordinator's sweep, same day)

- 46(j), 47(j): acquiring paragraph, the paragraph on where the record stops, and the map's acquiring row now use chapter 6's wording.
- 47(e), 47(m): the payout passage carries both, in chapter 13's and chapter 3's wording.
- 47(g), 47(h): already as the page has them (claims 10 and 76).
- 48(d)–(g) (token sharing, fraud models, 3-D Secure selection, verification deadlines): the map has no row on tokens, fraud, authentication or verification (spec non-goal). The one touching sentence, "how either company underwrites sellers" is not public, agrees with chapter 24 as it stands (credit criteria and models unpublished; Stripe's reserve factors are named, their amounts are not) and with 48(g) (screening stated as policy, method unpublished). The network-tokenization sentence (claim 30) is about the acquiring limit and is not affected by 48(d).
- Journal spec, Part X `how_why` (comma fix): no part-level field is copied into this page's spec (only `role.supports: P10-3`); intent, thesis and role equal the journal entry; `validate_spec.py` passes.
