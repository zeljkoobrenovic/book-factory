# Verification — 46-case-stripe (`case-stripe`)

Verification pass of 17 November 2026. Every source below was fetched in this session with `curl` and read as text: Stripe newsroom, legal and pricing pages in the English Netherlands edition (`/en-nl/`; unprefixed URLs redirect to the Dutch edition from this network), the four annual letters as their PDFs (linked from `stripe.com/annual-updates/<year>`), Stripe documentation as `.md`, `stripe.dev` posts as HTML, the Adyen Annual Report 2025 as its PDF (linked from the investor page), the OCC letter and the Georgia regulator's May 2026 bulletin as PDFs. Every double-quoted string in the article was matched mechanically against the fetched texts after normalizing quotation marks; the one that did not match mechanically (a link sits inside the sentence: "In the United States, stablecoin balances are in public preview") was read by hand. Each row is one claim or a group resting on the same passage.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | "Stripe is not a bank."; "Checking accounts are provided exclusively by Fifth Third Bank, National Association, Member FDIC." | https://docs.stripe.com/treasury.md | confirmed | — |
| 2 | EEA: "Payment Method Acquirer is Stripe Technology Europe, Ltd." | https://stripe.com/legal/acquirer-disclosure | confirmed | Source URL without the `en-us` prefix |
| 3 | Key point and take-away: "partner banks in the United States, Canada, Japan, India and Thailand" | same | corrected | Ruling 27: the named acquirers are not all banks (card companies in Japan, Network International in the UAE). Now "other named acquirers, mostly banks", UAE added; the take-away adds Stripe's own Georgia bank as one of six US acquirers |
| 4 | 2010 first venture backing: releases of February 2024 and February 2026 ("partners since 2010") | https://stripe.com/newsroom/news/employee-liquidity-feb-2024 ; https://stripe.com/newsroom/news/stripe-2025-update | corrected | "partners since 2010" is only in the 2026 release (a16z partner). The 2024 release (Sequoia) says "When we first partnered with Stripe in 2010". Both quoted now |
| 5 | Launch in 2011: "when Stripe launched in 2011" | 2023 letter PDF via https://stripe.com/annual-updates/2023 | confirmed | Letter dated March 13, 2024 |
| 6 | Connect launched October 2012 | https://stripe.com/blog/the-new-connect | confirmed | Post dated March 23, 2015 |
| 7 | Billing 5 April 2018 ("built on top of its core payments infrastructure"), Issuing 26 July 2018, Terminal 17 September 2018 | newsroom: stripe-launches-billing, -issuing, -terminal | confirmed | — |
| 8 | Capital 5 September 2019; Tax 10 June 2021; Identity 14 July 2021; Revenue Recognition 21 September 2021 | newsroom: stripe-capital, stripe-launches-stripe-tax, stripe-launches-identity, revenue-recognition | confirmed | — |
| 9 | Tempo unveiled September 2025, "incubated together with Paradigm" | 2025 letter PDF | confirmed | — |
| 10 | Tempo mainnet 18 March 2026 | https://tempo.xyz/blog/mainnet | confirmed | "Mar 18, 2026" |
| 11 | Paystack: agreement announced 15 October 2020 | newsroom/paystack-joining-stripe | confirmed | "has entered into an agreement to acquire" |
| 12 | TaxJar "Stripe will acquire TaxJar", 27 April 2021; Recko "Stripe will acquire Recko", 20 October 2021 | newsroom/taxjar ; newsroom/recko | confirmed | Suite table now says TaxJar "agreement announced April 2021" instead of "(2021)" |
| 13 | Bouncer announced as acquired, 14 May 2021 | newsroom/bouncer | confirmed | "announced today it has acquired" |
| 14 | Lemon Squeezy announced 26 July 2024; "will shut down on March 31, 2027" | https://www.lemonsqueezy.com/blog/stripe-acquires-lemon-squeezy | confirmed | Banner present on 17 November 2026 |
| 15 | Bridge announced October 2024; completed 4 February 2025 | 2024 letter PDF ("In October, we announced our acquisition of Bridge"); newsroom/stripe-completes-bridge-acquisition | confirmed | — |
| 16 | Privy: "In July, Stripe acquired Privy" | newsroom/stripe-2025-update | confirmed | — |
| 17 | Metronome completed 14 January 2026 | newsroom/stripe-completes-metronome-acquisition | confirmed | — |
| 18 | OpenRouter agreement 19 August 2026; "a leading AI model gateway and routing platform"; Collison: "Stripe is building the economic infrastructure for AI" | newsroom/stripe-agrees-to-acquire-openrouter | confirmed | The Collison sentence is also a site-wide banner; read in the release body to be sure |
| 19 | Parafin agreement 30 September 2026; "expected to close in the coming months"; "More than 18,000 platforms build on Stripe" | newsroom/stripe-agrees-to-acquire-parafin | confirmed | — |
| 20 | No completion release for OpenRouter or Parafin on 17 November 2026 | https://stripe.com/newsroom/news (286 links read) | confirmed | Newest items after 30 September 2026 are product and customer releases. One web search found no closing either |
| 21 | The table of ten purchases read as the list | same | hedged | Not complete: the newsroom carries "Stripe acquires OpenChannel" (6 December 2021). One sentence added saying the table is a selection |
| 22 | 2021 self-description "which builds economic infrastructure for the internet"; February 2024 "a financial infrastructure platform for businesses" | newsroom/stripe-series-h ; employee-liquidity-feb-2024 | confirmed | — |
| 23 | "From December 2025 it is 'the programmable financial services company'" | newsroom: japan-payments-moment-2025 (22 April 2025), tour-sydney-2025 (11 September 2025), clear-and-stripe (24 March 2025, still the old wording), sessions-2025, stripe-openai-instant-checkout | corrected | The phrase is older: "programmable financial services company Stripe" from 22 April 2025; with "the", from 11 September 2025 (earliest found). Sentence rewritten; the Agentic Commerce Suite source entry replaced by the two releases |
| 24 | "Stripe's first customers were developers at young technology companies who signed up without a sales call and paid a published price. The company says so." | 2022 letter PDF | hedged | The letter says only "Stripe grew up with companies in the technology sector". The self-service and price detail was not in the source and was removed |
| 25 | 2022 letter (5 April 2023): four ways; "providing simple, reliable, secure, and developer-friendly APIs and services" | 2022 letter PDF | confirmed | — |
| 26 | March 2023: "enterprise user base has compounded since 2019"; one hundred businesses above $1 billion; "Seventy-five percent of these global winners use Stripe for more than just payments" | newsroom/stripe-series-i-employee-liquidity | confirmed | — |
| 27 | "the 'long tail' is much of the dog" | newsroom/stripe-2025-update | confirmed | — |
| 28 | Pricing: 1.5% + €0.25 standard EEA cards; "a custom package"; "IC+ pricing" | https://stripe.com/en-nl/pricing | confirmed | Source URL set to the edition cited |
| 29 | Bu post (15 December 2020): stages 2011, "a second API … in 2015", PaymentIntent 2018; three quotations | https://stripe.dev/blog/payment-api-design | corrected | Quotations exact. In 2015 Stripe added ACH and Bitcoin; the second API (Sources) is dated 2015–2017 in the post. Sentence corrected |
| 30 | Older APIs get no further development | https://docs.stripe.com/payments/older-apis.md | confirmed | "Future development: Not supported" |
| 31 | Idempotency post (22 February 2017) quote; versioning post (5 August 2017) two quotes; pinning to first version used | https://stripe.com/blog/idempotency ; https://stripe.com/blog/api-versioning | confirmed | — |
| 32 | Keys kept at least 24 hours | https://docs.stripe.com/api/idempotent_requests.md | confirmed | "after they're at least 24 hours old" (API v1) |
| 33 | October 2024: "twice-yearly major updates" plus monthly additions | https://stripe.com/blog/introducing-stripes-new-api-release-process | confirmed | Dated October 1, 2024 |
| 34 | June 2026 post: "we've codified a set of design patterns that all APIs must follow"; tests before merge; v2 in 2024 | https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products | confirmed | Dated 2026.6.15 |
| 35 | "You can use any combination of APIs in the `/v1` or `/v2` namespace in the same integration." | https://docs.stripe.com/api-v2-overview.md | confirmed | — |
| 36 | No payment objects among v2 resources as of the changelog of 28 October 2026 | https://docs.stripe.com/changelog.md | confirmed | As far as the changelog shows: v2 entries cover accounts, events, meter events, financial addresses, payouts and similar; none for payment intents |
| 37 | No engineering post found on how events are delivered | https://stripe.dev/blog (index, first page) ; verification of chapter 20 | confirmed | Negative, bounded by "I found"; the index page lists 32 of 128 posts, the rest were not paged through |
| 38 | Suite run rate $500 million; Billing "more than 300,000 companies"; "on track to hit an annual run rate of $1 billion this year" | 2024 and 2025 letter PDFs | confirmed | — |
| 39 | Metronome "primary usage-based billing platform…"; division of work; Meters API stays supported | https://docs.stripe.com/billing/subscriptions/usage-based/compare-metronome.md ; https://docs.stripe.com/billing/subscriptions/usage-based.md | confirmed | Source entry split into two bullets with the pages' titles |
| 40 | Managed Payments in the API changelog of 22 April 2026 | https://docs.stripe.com/changelog/dahlia/2026-04-22/managed-payments.md | confirmed | — |
| 41 | Table gloss: merchant of record "the seller of record for tax and liability" | same ; coordinator's ruling from chapter 32 | hedged | Under Managed Payments the business stays liable for disputes, refunds and reversals. Gloss now "the legal seller to the customer, which owes the tax on the sale" |
| 42 | Radar "can evaluate payments from any processor in real time and return risk signals" | https://docs.stripe.com/radar/multiprocessor.md | confirmed | — |
| 43 | October 2024: subscriptions with other payment providers | https://stripe.com/blog/our-biggest-ever-upgrades-to-stripe-billing | confirmed | Dated October 29, 2024 |
| 44 | Terminal uses the same payment object as online payments | https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven | confirmed | Had no source on this page; entry added |
| 45 | "Stripe publishes a volume for none of these" (in-person, platforms, product shares) | four letter PDFs | hedged | Checked in the four letters only (2022 gives a device count, 2024 a platform count); sentence now says "The four annual letters give…" |
| 46 | "In the United States, stablecoin balances are in public preview" | https://docs.stripe.com/treasury/stablecoins.md | confirmed | URL changed (redirect from `/financial-accounts/stablecoins`); title now "Stablecoins in Treasury"; private preview elsewhere |
| 47 | STEL: e-money institution, Central Bank of Ireland, C187865, "acquire payment transactions", page dated April 2019 | https://stripe.com/legal/stel | confirmed | URL changed (redirect) |
| 48 | SPUKL: e-money institution, FCA, 900461, page dated January 2017 | https://stripe.com/gb/legal/spukl | confirmed | — |
| 49 | Region table: EEA; UK, Gibraltar, Switzerland; Australia, New Zealand, Singapore, Malaysia, Hong Kong, Brazil (a Stripe entity in each) | https://stripe.com/legal/acquirer-disclosure | confirmed | — |
| 50 | US: "Stripe, LLC is a Payment Facilitator of" Cross River Bank, Deutsche Bank Trust Company Americas, Fifth Third Bank, Pathward N.A., PNC Bank, N.A. and "Stripe MALPB" | same | confirmed | Rulings 27 and 33(b) |
| 51 | Canada, Japan, India, Thailand, UAE row; text "a named bank or card company is the acquirer" | same | corrected | Mexico was missing (ruling 27): row added, quoting "is both a Payment Method Acquirer and a Payment Facilitator". UAE added to the sentence; the UAE acquirer (Network International) is named in the row |
| 52 | SPC "is a U.S. state-licensed money transmitter and federally registered money services business" (updated November 2025) | https://stripe.com/legal/spc | confirmed | Last updated November 18, 2025 |
| 53 | Celtic Bank as issuing bank of one US card program (updated August 2025) | https://stripe.com/legal/celtic-spend-card | confirmed | — |
| 54 | April 2020: direct integrations "with all six major card networks…" | https://stripe.com/en-ca/newsroom/news/direct-platform | confirmed | Dated 23 April 2020 |
| 55 | Georgia charter given on a trade association's item, "primary trace" only the name in the disclosure; "not read" in How to Read This Case | https://dbf.georgia.gov/financial-institutions-bulletin-2026 (May 2026 bulletin PDF) ; https://stripe.com/legal/stripe-malpb-acquirer-terms | corrected | Ruling 33(a). The bulletin lists "Stripe MALPB, Atlanta, Georgia", approval date 06/30/2025, begin business date 05/28/2026. Stripe's terms (last updated May 28, 2026): "a Georgia Merchant Acquirer Limited Purpose Bank", "a member of the Networks, and a Payment Method Acquirer for Visa and Mastercard Transactions". Paragraph, How to Read This Case, Sources and spec updated |
| 56 | ICBA, 8 July 2025: two quotations on what the charter permits | https://www.icba.org/w/georgia-approves-stripe-application-to-form-malpb | confirmed | URL changed (redirect); kept as a secondary source for the charter's scope only |
| 57 | "does not say whether the Georgia bank handles live payments" (text and Where the Evidence Stops) | rows 50, 55 | corrected | The bank has been in business since 28 May 2026 and is a named acquirer. What is not public is which merchants it acquires for and how much; both places reworded |
| 58 | OCC letter, February 2026: "preliminary conditional approval"; "The OCC has granted preliminary conditional approval only." | https://www.occ.treas.gov/topics/charters-and-licensing/interpretations-and-decisions/2026/cd1365.pdf | confirmed | Corporate Decision #1365, February 12, 2026. URL path changed (`interpretations-and-actions` redirects). One web search found no final approval (ruling 33(d)) |
| 59 | Banking Dive, April 2025: spokesperson called the application an extension of work to expand banking and other partners | https://www.bankingdive.com/news/stripe-georgia-special-banking-charter-credit-card-payments/744921/ | confirmed | Fetched (the writer had not); published April 7, 2025; the paraphrase follows the article's |
| 60 | Letters and newsroom do not explain the partner-bank model; safeguarding pages name no banks | four letters; newsroom list; verification of chapter 16 | confirmed | Negative, as far as read |
| 61 | "$1.9 trillion in total volume, up 34% from 2024"; table of four letters (wording and growth) | four letter PDFs | confirmed | 26%, 25%, 38%, 34% |
| 62 | "Adyen's audited 2025 accounts work out to 17.0 basis points" | Annual Report 2025 PDF via https://investors.adyen.com/financials/2025 | hedged | Fetched (the writer had not). The report states it: "Full-year take rate for 2025 was 17.0 bps"; net revenue €2,364.2 million, processed volume €1,394.3 billion (2,364.2 ÷ 1,394,300 = 16.96 bps). Net revenue is "a non-IFRS measure", so "audited accounts work out to" was replaced by the report's own take rate and its two inputs |
| 63 | "more than 5 million businesses directly or via platforms" | 2025 letter PDF | confirmed | — |
| 64 | "robustly cashflow positive in 2023" | 2023 letter PDF | corrected | The letter writes "robustly cash flow positive in 2023" |
| 65 | "profitable in 2024"; "remained robustly profitable"; no measure named | 2024 and 2025 letter PDFs | confirmed | — |
| 66 | Stripe has never published revenue or a margin | four letters; newsroom | confirmed | Negative, as far as read |
| 67 | Valuations: $95B March 2021, $50B March 2023, $65B February 2024, $91.5B February 2025, $159B February 2026 | newsroom: stripe-series-h, stripe-series-i-employee-liquidity, employee-liquidity-feb-2024, employee-liquidity-feb-2025, stripe-2025-update | confirmed | — |
| 68 | Take-away: "its valuations are tender-offer prices" | same | corrected | Two of the five are funding rounds (Series H, Series I). Now "prices from funding rounds and tender offers" |
| 69 | 3 November 2022 email: "around 14%"; "will return us to our February headcount of almost 7,000 people" | newsroom/ceo-patrick-collisons-email-to-stripe-employees | confirmed | — |
| 70 | Blog index: 128 posts, 28 Engineering, 7 Infrastructure | https://stripe.dev/blog | confirmed | Counts shown on the page on 17 November 2026 |
| 71 | Ledger post (16 February 2024): three quotations; double-entry | https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement | confirmed | — |
| 72 | Fee-credits post (16 April 2026): financial accounts "backed by a real bank account"; "submitted → prepared → disbursed" | https://stripe.dev/blog/how-we-built-stripe-credits-a-programmable-auditable-way-to-pay-your-stripe-fees | hedged | Quotations exact, but the post's point is that credits use purely logical accounts that are *not* backed by a bank account. Sentence now says both |
| 73 | DocDB post (6 June 2024): four quotations; proxies written in-house; data moved without downtime | https://stripe.dev/blog/how-stripes-document-databases-supported-99.999-uptime-with-zero-downtime-data-migrations | confirmed | — |
| 74 | July 2026 post: "A MongoDB shard—one of 2,000 that collectively processed $1.9 trillion in payments in 2025" | https://stripe.dev/blog/how-stripe-uses-graph-search-and-state-machines-to-auto-remediate-a-global-database-fleet | confirmed | Dated 2026.7.16 |
| 75 | 2023 letter: "approximately 400 times in a typical day"; "a battery of around 1.4 million tests"; 55,000 metrics | 2023 letter PDF | confirmed | — |
| 76 | "our monorepo is the order of 50 million lines of Ruby code"; "we target 99.9995% reliability" | https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo ; https://stripe.dev/blog/building-a-data-plane-from-scratch-stripes-own-high-performance-distributed-proxy | confirmed | Dated 2026.4.09 and 2026.8.26 |
| 77 | Table: proxy post "restates the availability target" | 2023 letter PDF ; proxy post | corrected | The letter gives an achieved figure ("99.999% available last year"), the 2026 post a target (99.9995%). Cell reworded |
| 78 | January 2023: "has long relied on AWS…"; Singleton quotation | newsroom/amazon-and-stripe | confirmed | Dated 23 January 2023. AWS expanded on first use |
| 79 | October 2024 AWS post written with Stripe staff, consistent with the 2023 statement | https://aws.amazon.com/blogs/mt/how-stripe-architected-massive-scale-observability-solution-on-aws/ | confirmed | Fetched (the writer had not): 24 OCT 2024, "co-written with" two Stripe staff engineers; "a sophisticated microservice environment built on top of AWS" |
| 80 | "no first-party source names a region, a number of regions or a failover design"; the engineering table read as the whole record | https://www.infoq.com/presentations/docdb-online-database/ ; https://stripe.com/rcas/2019-07-10 ; https://stripe.com/rcas/2020-01-06 ; https://stripe.dev/blog/test-clocks-how-we-made-it-easier-to-test-stripe-billing-integrations | corrected | Rulings 34, 39, 42(d), 43. The QCon talk (Jimmy Morzaria, November 2025, InfoQ transcript 30 April 2026) says shard nodes are "distributed across availability zones and regions" and places retries in the proxy and a client SDK. The section now names the two root-cause analyses, the 2024 scheduling-service post and the talk; the regions sentence and bullet say replicas span regions and that the rest was not found. Four source entries added |
| 81 | Where the Evidence Stops, internals bullet ("are not described") | verifications of chapters 12, 18, 20; rows 37, 80 | hedged | Ruling 39(a): reworded to "were not found in Stripe's documentation, engineering posts or support site as of November 2026". Checked against the rulings: the bullet lists nothing a verified chapter found published (request-log retention, key types, the scheduler, root-cause analyses, retry placement, standalone selling price and the onboarding figure are not listed as unpublished anywhere on the page) |
| 82 | Stripe's European licenses page returned an error | https://stripe.com/legal/licenses (and `/en-nl/`, `/ie/`) | confirmed | 404 on 17 November 2026 |
| 83 | Launch dates of Radar, Treasury and Link could not be confirmed from a dated Stripe page | newsroom list | not checked | The newsroom has a dated Atlas release (24 February 2016) and a Radar 2.0 release (18 April 2018); `/newsroom/news/treasury` redirects to the product page. No search for Link was made. The sentence is about the writer's research and was left |

Counts by the Status column: 83 rows; 64 confirmed, 11 corrected (3, 4, 23, 29, 51, 55, 57, 64, 68, 77, 80), 7 hedged (21, 24, 41, 45, 62, 72, 81), 0 unsupported, 0 unreachable, 1 not checked (83).

## Could not verify, and what was done

- **Row 83** (launch dates of Radar, Treasury, Link): not searched beyond the newsroom list; the sentence stays as the writer's research note.
- **Negatives** (rows 20, 36, 37, 45, 60, 66, 81): bounded by what was read; each is worded as "I found", "the four letters" or "not found in … as of November 2026".
- **Stripe's engineering blog index** shows 32 of its 128 posts on the first page; the remaining pages were not read.
- The four `stripe.com/rcas`, test-clocks and InfoQ sources were read for the sentences that cite them, not in full.
- A web search summary mentioned a Stripe purchase of "Clerky" in 2026. It is not in Stripe's newsroom list and was not verified or used.

## Links

All 74 URLs in Sources and Evidence return HTTP 200. Replaced by final URLs: acquirer disclosure, SPC terms (`en-us` prefix dropped), STEL page (`/stel/legal` → `/legal/stel`), ICBA article, OCC letter (`interpretations-and-actions` → `interpretations-and-decisions`), stablecoins page (`/financial-accounts/stablecoins` → `/treasury/stablecoins`), pricing (the Netherlands edition the text cites). Unprefixed `stripe.com` URLs redirect by visitor location. Added: Stripe MALPB Acquirer Terms, Georgia bulletin, two 2025 releases for the self-description, Terminal "Collect card payments", two root-cause analyses, the test-clocks post, the QCon talk. Removed: Agentic Commerce Suite release (no longer cited). Three "not re-fetched by the author" marks removed after fetching. No external URL in the running text (ruling 22). Every `[[permalink]]` is in the style guide's list; `[[stripe-and-adyen-bets-compared]]` does not resolve yet because chapter 48 is not written (the only render-check entry).

## Larkfield consistency

Agrees with the ledger: 44% and €493 million; UK, US, Belgium and 1,140 older Dutch and German studios; Tuesday 9 March 2027, €120.00, Studio Noord on Adyen; K1, K2, K3, K7; the acquirer inventory (Stripe Technology Europe, Ltd. for NL/DE/BE, Stripe Payments UK, Ltd. for the UK, Stripe, LLC under one of six named US acquirers as an open question).

## Ledger conflicts

None.

## For other pages

- Any page that dates Stripe's phrase "the programmable financial services company" to December 2025: it is in releases from 22 April 2025 (without "the") and 11 September 2025 (`_research/brief-companies-and-bets.md` is the likely origin).
- Any page that quotes "robustly cashflow positive": the 2023 letter writes "cash flow".
- Any page that calls Adyen's 17.0 basis points a figure from audited accounts: it is the annual report's stated take rate, built on net revenue, a non-IFRS measure.
- Any page that cites "partners since 2010" to the February 2024 release: that wording is in the February 2026 release.
- `47-case-adyen`, `48`, `50`: Stripe's list of purchases is longer than the ten named here (OpenChannel, December 2021).
- The journal spec entry for this page (copied into the post spec's intent and acceptance criteria, left unchanged so the two agree) still says "partner banks are named for North America, Japan, India and Thailand", "trade press reports its approval in 2025", "whether and how much the Georgia bank processes" and "valuations that are tender-offer prices". The author should update the journal spec and then the copy.

## Length

The page is 6,369 words by `check_draft.py structure` (28 min), up about 300 from the draft and above the 4,500–6,000 aim for case studies, under the 6,500 limit.
