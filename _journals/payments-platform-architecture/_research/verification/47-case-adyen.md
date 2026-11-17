# Verification — 47-case-adyen (`case-adyen`)

Verification pass of 17 November 2026. Every source was fetched in this session (curl; PDFs converted with pdftotext). All 44 URLs in the original Sources section returned HTTP 200. Every quotation in the article (107 quoted strings) was matched by script, character for character after normalizing typographic quotes and line breaks, against the fetched text; the rows below name the document each one was found in.

Short names: **AR** = Annual Report 2025 PDF downloaded from `investors.adyen.com/financials/2025` (button "Download PDF", served from `brand.adyen.com/api/asset/…`; 233 pages, created 4 March 2026); **H1L** = H1 2026 Shareholder Letter PDF from `investors.adyen.com/financials/h1-2026-c2a1a`; **H2L** = H2 2025 Shareholder Letter PDF from `investors.adyen.com/financials/h2-2025-4r9rc`; **Q3** = Q3 2026 Business Update PDF (`media.ffycdn.net/eu/adyen/dfb86zC9WHUzrC5zRj2Y.pdf`, linked from `investors.adyen.com/financials/q3-2026-10c88s`); **PR-x** = press release on `adyen.com/press-and-media/…`; **About** = `adyen.com/about`; **D2D-1 / D2D-2** = the two "Design to Duty" posts; **docs** = `docs.adyen.com` (`.md` variants).

**The annual report (point 2 of the brief).** The PDF that Adyen's own investor page offers is word for word the same document as the Bundestag copy the page had cited (98,632 words each; the only difference pdftotext shows is one table on the remuneration pages). Adyen's own PDF carries the same disclaimer: "This document is only a "printed version" and is not the official annual financial report … The official annual financial report … are included in the single report package". So the quotations are now cited to Adyen's PDF, the Bundestag entry is removed, and "How to Read This Case" says what the PDF is. The ESEF reporting package itself was not opened.

## Claims

| # | Claim (short) | Source | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Key point: one platform "hosted in its own data centers" | AR ("data center partners", data centers among "third-party providers"); `adyen.com/infrastructure` ("We administer and manage all our own servers") | corrected | Now "on infrastructure Adyen manages itself" |
| 2 | Key point: 84% full-stack in 2025; concentration risk at banking partners | AR | confirmed | — |
| 3 | Key point: Talon.One and Orb closed 1 July 2026; Orb under "an incubator model" | PR closing (1 July 2026); PR Orb (11 June 2026) | confirmed | — |
| 4 | Key point: 878,000 transacting terminals | Q3 | confirmed | — |
| 5 | Pattern line: largest customers spread volume over several providers | AR risk section | confirmed | — |
| 6 | Pattern line: Adyen pays sellers before the money has arrived | Sales Day Payout terms (17 June 2024) | confirmed | — |
| 7 | 9 April 2026 release: "Unlike many providers that rely on a patchwork…" | PR Intelligent Money Movement | confirmed | — |
| 8 | Annual Report 2025 signed 5 March 2026, audited | AR ("Amsterdam, March 5, 2026"; auditor's report) | confirmed | — |
| 9 | Shareholder letter and Q3 update unaudited | H1L ("The interim condensed consolidated financial statements are unaudited"; it carries an auditor's review report); Q3 | confirmed | — |
| 10 | "The annual report was read from a copy of the printed version, which states that it is not the official filing" | AR | corrected | Adyen's own investor page offers the PDF; sentence and source entry now say so (ruling 45d) |
| 11 | Status page "shows a truncated incident history" | `status.adyen.com` (landing page only; history is client-rendered) | hedged | Now "builds its incident history in the browser and was not read" (ruling 43e) |
| 12 | 2023 Investor Day targets and August 2023 share-price fall "not fetched and not used" | — | unsupported (removed) | Sentence about material that is not used removed; "Five things" is now "Four things" |
| 13 | No Adyen document read calls the 2026 deals its first acquisitions; history page lists none before them | About; all releases and letters read | confirmed | — |
| 14 | Founded in Amsterdam in 2006 | About | confirmed | — |
| 15 | Acquiring license in the 2006–2012 period, quote "We secured a European acquiring license…"; no year given | About | confirmed | — |
| 16 | "Built for enterprise, not adapted to it." | About | confirmed | — |
| 17 | European banking license "obtained in 2017" | PR US branch (14 June 2021) | confirmed | — |
| 18 | History page: acquiring licenses across Asia-Pacific "in the same years" | About ("2016 – 2020 Global expansion") | hedged | Now names the period, 2016 to 2020 |
| 19 | June 2018 listing at €240, "implying a market capitalization of €7.1 billion" | PR IPO (11 June 2018; first trading 13 June) | confirmed | — |
| 20 | 14 June 2021: US regulators approved a federal branch; Federal Reserve approval 24 May 2021 | PR US branch | confirmed | — |
| 21 | 31 March 2022: "embedded financial products"; sponsor-bank quotation (Thom Ruiter, VP of Banking and Financial Products) | PR 31 March 2022 | confirmed | — |
| 22 | "On 7 September 2023 the UK branch was authorized as a bank" | PR 7 September 2023 ("today announced that its UK branch has been granted authorization as a UK bank") | hedged | The date is the announcement; text and table now say "announced" |
| 23 | All three permissions on the current license pages | `adyen.com/licenses/emea`, `/licenses/united-states` | confirmed | — |
| 24 | H1 2023 margin 43%, wages quotation | PR H1 2023 (17 August 2023) | confirmed | Evidence-age mark added (3 years) |
| 25 | 2023 margin 46% "compared to 55% in 2022" | PR H2 2023 (8 February 2024) | confirmed | — |
| 26 | Margin 50% in 2024, 53% in 2025 | AR; PR H2 2024 | confirmed | — |
| 27 | "in a year when the platform did not change" | none | unsupported (relabeled) | Now "not with the platform", the author's reading of the release's own attribution |
| 28 | Table: agreements 23 April and 11 June 2026 | PR Talon.One; PR Orb | confirmed | — |
| 29 | Table: 28 October 2026, medium-term margin objective discontinued | Q3; PR Q3 | confirmed | — |
| 30 | AR: "From the beginning, we made a strategic choice…" | AR | confirmed | — |
| 31 | AR: "The first step was our single global platform"; "takes effect everywhere, without reintegration work" | AR | confirmed | — |
| 32 | AR: "acquiring our own banking licenses in the EU, US, and UK"; "without relying on partner banks, improving reliability and settlement speed" | AR | confirmed | — |
| 33 | AR: "a single platform built entirely in-house"; "all operated end-to-end on our own infrastructure and banking licenses" | AR | confirmed | — |
| 34 | API families: checkout, management, platform configuration, transfers, legal entities, terminals; most with their own host; a version in each URL | `github.com/Adyen/adyen-openapi` (`json/` listing; servers of CheckoutService-v72, ManagementService-v3, BalancePlatformService-v2, TransferService-v4, LegalEntityService-v4); docs versioning page | confirmed | Balance Platform and Transfers share a host, so "most" is right |
| 35 | Checkout API has no call that returns a payment | CheckoutService-v72: the only GET paths are `/paymentLinks/{linkId}`, `/sessions/{sessionId}`, `/storedPaymentMethods` | confirmed | Scoped to the Checkout API as ruling 29 requires |
| 36 | 2021 post: "We manage our own infrastructure in several data centers around the world"; "part historical, part legal, and part technical" | D2D-1 (28 July 2021; "Updated June 2022") | confirmed | Source entry notes the update line |
| 37 | CapEx "was €116.8 million and 5% of net revenues"; "The majority of our CapEx is related to our data centers" | AR | confirmed | — |
| 38 | August 2026: "proactively pulling investment from 2027 into H2 2026…"; about 7% | PR H1 2026 | confirmed | — |
| 39 | "Its release for 2023 gives the same 7% for 2022" | PR H2 2023 | confirmed | Sentence cut for length; not a correction |
| 40 | Five named live regions | docs web best practices (EU, US, AU, NEA, IN) | confirmed | Source entry now "n.d." (ruling 30) |
| 41 | License page: "authorised as a credit Institution under the supervision of Dutch Central Bank"; passporting across the EEA | `licenses/emea` | confirmed | — |
| 42 | UK: "authorised as an overseas branch of an EEA credit institution in the UK" | `licenses/emea` | confirmed | — |
| 43 | US: "a federal Branch of Adyen, N.V.", licensed "by the two federal banking regulators" | `licenses/united-states` (OCC and Federal Reserve Board of Governors) | corrected | The two are now named; "the two" implied there are only two |
| 44 | Narrower local licenses elsewhere | `licenses/emea` (UAE Retail Payment Services Licence, Category II); About (RBI license in India) | confirmed | — |
| 45 | AR: "the speed and autonomy that come from not relying on external parties for regulatory compliance" | AR | confirmed | — |
| 46 | H1 letter: "Our own licensed infrastructure grants direct access to payment networks, giving us control over funds" | H1L | confirmed | — |
| 47 | "€12.4 billion of total cash"; "The majority of that number represents balances moving through our system…" | H1L | confirmed | — |
| 48 | Finance income €267.6 million in 2025 | AR ("driven primarily by our balances at central and commercial banks") | confirmed | — |
| 49 | Sales day payout terms, "irrespective of whether the funds are actually received…"; last update 17 June 2024 | `adyen.com/legal/sales-day-payout-terms-of-service` | confirmed | Ruling 18 |
| 50 | "Prefinancing is capped at 30 days", then reversed | docs upgrade-to-sdp | confirmed | — |
| 51 | AR: "only after funds have been received", "default setup", "primarily through pre-financing in accelerated payout schedules" | AR | confirmed | — |
| 52 | "Of processed volumes, 84% were full-stack volumes, up from 83% in 2024."; not defined | AR (the term occurs once) | confirmed | — |
| 53 | 14 countries and regions with an "Adyen acquiring connection"; "for example Adyen Singapore" | docs supported-currencies.md (AU, HK, IN, JP, MY, NZ, SG, EU, UK, CA, US, BR, MX, UAE) | confirmed | Page title is "Supported payout currencies"; text and source entry corrected |
| 54 | AR: "primarily at banking partners in locations where there are no own direct acquiring licenses" | AR | confirmed | Reading labeled as inference (ruling 27c) |
| 55 | 2026: UAE payments license; approval for direct access to France's clearing system | H1L; PR H1 2026 | confirmed | — |
| 56 | No acquiring entity per country, no network memberships named | docs page above; license pages | confirmed (absence, as far as read) | — |
| 57 | POS volumes "€310.9 billion, comprising 22%… up from 18% in 2024" | AR | confirmed | — |
| 58 | 2023 point-of-sale volume €159.9 billion | PR H2 2023 | confirmed | Kept in the table; the repeat in the text was cut for length |
| 59 | "The number of transacting terminals across the platform reached 878k, up 25% YoY"; "transacting" undefined | Q3 | confirmed | — |
| 60 | Unified Commerce pillar: "retailers, restaurants and hotels", €765.4 million | AR ("global retailers, hospitality, and food & beverage groups") | hedged | Wording moved to the report's categories |
| 61 | August 2022: "its first in-house designed terminals" | PR 18 August 2022 | confirmed | — |
| 62 | Terminal API "is based on the nexo Retailer Protocol" | docs Terminal API | confirmed | Source entry now "n.d." (ruling 30) |
| 63 | Counter and web payments on one platform; recognition and refunds across channels | chapter 11 and its verification | not checked | Rests on chapter 11's verified account; "under shared references" dropped |
| 64 | Terminal software rollout (chapter 11 finding) | docs release-updating ("every four weeks"; "We roll out releases gradually") | corrected (added) | The case said nothing; one sentence and a source added |
| 65 | Platforms net revenue €263.8 million, up from €176.1 million | AR (263,836 and 176,053 in the note) | confirmed | — |
| 66 | Q3 2026 Platforms €100.2 million, up 46%; 46 customers "processing over €1 billion annually"; 312k active business customers | Q3 | confirmed | — |
| 67 | "Our Platforms offering allows us to provide payments and financial products to smaller merchants…" | Q3 | confirmed | — |
| 68 | 2021: "We leverage this same system of accounting for our banking platform" | D2D-2 (23 August 2021) | confirmed | — |
| 69 | "native business accounts, card issuing, and capital within a single integration" | H1L | confirmed | — |
| 70 | Issuing "currently supported in the European Economic Area, the United Kingdom, and the United States" | docs issuing | confirmed | — |
| 71 | Business accounts: "This feature is in development phase" | docs business-accounts | confirmed | — |
| 72 | A subscription is a stored token the merchant charges | docs tokenization ("recurring transactions you initiate at regular intervals") | confirmed | — |
| 73 | "Adyen doesn't act as a direct, third-party merchant of record", 15 September 2026 | knowledge-hub merchant-of-record (displayed date) | confirmed | — |
| 74 | "I found no Adyen product that calculates or files sales tax" | docs `llms.txt` and sitemap (tax pages: 1099-K forms, Greece, tax-free shopping); `adyen.com/sitemap-en.xml` | hedged | Now "no first-party Adyen product … in its documentation or on its site as of November 2026" (rulings 38, 39). The help-center search URL returned 404 and was not searched |
| 75 | Talon.One: "a leading platform for loyalty and incentives serving 300+ global merchants"; "a total consideration of €750 million", from available cash; "approximately €60 million in ARR as of the end of this year"; German (GmbH, Berlin) | PR Talon.One; knowledge-hub closing article | confirmed | — |
| 76 | Orb: San Francisco, founded 2021, Vercel, Glean, Replit, Supabase; "$335 million"; total funding $44 million | PR Orb | confirmed | — |
| 77 | "Both transactions officially closed on July 1, 2026" | PR closing | confirmed | — |
| 78 | Orb: "an incubator model", "continuing to support multi-PSP environments", "the strategic intent is convergence" | PR Orb | confirmed | — |
| 79 | "multi-product reality" | PR closing (Ingo Uytdehaage) | confirmed | — |
| 80 | 13 August letter: "While organic growth…", "and then" "we are no longer just a payments company" | H1L (page 2 and page 16) | corrected | Order reversed: "no longer just a payments company" comes first in the letter |
| 81 | Article of 29 September 2026: "we've historically stayed singularly focused…When the opportunity…" ; "You'll soon see" | knowledge-hub why-adyen-acquired-orb (displayed 29 September 2026) | confirmed | Rulings 21, 25 |
| 82 | "As of 17 November 2026 the integration is stated as intent" | PR closing ("Adyen will begin integrating Talon.One's promotional engine and Orb's flexible billing"); PR Q3 ("the successful ongoing integration of Talon.One and Orb") | corrected | Adyen says integration has begun, not what is joined; sentence and source entry changed |
| 83 | "Integrating Talon.One's promotion engine directly into our architecture will bridge this gap" | H1L | confirmed | — |
| 84 | "The research found no Adyen documentation page for a billing product" | docs `llms.txt` and sitemap (no billing or Orb page); `docs.withorb.com/integrations-and-exports/adyen.md` | corrected | Narrowed per ruling 39(b): Orb's documentation lists Adyen as a payment gateway; source added |
| 85 | "won the payments volumes of several" Orb customers | Q3 | confirmed | — |
| 86 | About one percentage point of net revenue growth; "an estimated 1 percentage point margin dilution" | H1L (note 17); PR Orb | confirmed | — |
| 87 | Acquiring page: "We've built our entire platform in house." | `adyen.com/global-acquiring` | confirmed | Page title corrected in Sources |
| 88 | History page: "With the acquisition of Orb and Talon.One… we've moved beyond payments…" | About | confirmed | — |
| 89 | 2021 post allowed buying "if the use case is peripheral" | D2D-1 ("We buy instead of build, if the use case is peripheral…") | hedged | The passage is about vendor software; the sentence now says so |
| 90 | Figure caption: usage billing "runs apart" | PR Orb (June 2026 description); later releases speak of integration | hedged | Caption now dates the description |
| 91 | Net revenue: non-IFRS; revenue less costs from financial institutions and cost of goods sold, plus net interest income | AR note 2.2 | confirmed | — |
| 92 | Table 2023: €970.1 billion, €1,626.1 million, 46%, €159.9 billion | PR H2 2023 | confirmed | — |
| 93 | Table 2024: €1,285.9 billion, €1,996.1 million, 15.5 bps, 50%, €232.7 billion | PR H2 2024; AR | confirmed | — |
| 94 | Table 2025: €1,394.3 billion, €2,364.2 million, 17.0 bps, 53%, €310.9 billion; EBITDA €1,245.7 million | AR | confirmed | — |
| 95 | Table H1 2026: €803.8 billion, €1,302.9 million, 16.2 bps, 49%, €175.7 billion | H1L; PR H1 2026 | confirmed | — |
| 96 | Table Q3 2026: €451.1 billion, €738.1 million; no take rate, margin or in-person volume | Q3 | confirmed | — |
| 97 | 2025: volume up 8%, net revenue up 18% | AR | confirmed | — |
| 98 | "up 21% excluding a single large-volume customer, or 8% YoY including this customer"; customer not named | PR H2 2025; H2L (footnote: "referenced beginning in the Q3 2024 Business Update") | confirmed | — |
| 99 | "Full-year take rate for 2025 was 17.0 bps, up from 15.5 bps in 2024. This increase was driven by changes in the overall merchant mix." | AR | confirmed | — |
| 100 | Pricing: "a fixed processing fee + a fee determined by the payment method"; Interchange++ | `adyen.com/pricing` | confirmed | Page title corrected in Sources |
| 101 | "Adyen's tiered pricing structure incentivizes our customers to bring more volume" | Q3 | confirmed | — |
| 102 | H1 2026 take rate 16.2 bps, "reflecting expected volume tiering" | H1L | confirmed | — |
| 103 | Pillars 2025: Digital €1,334.9 million, Unified Commerce €765.4 million, Platforms €263.8 million | AR | confirmed | — |
| 104 | "Adyen's top 10 merchants represent 11% of revenue (2024: 12%)"; no customer above 10% | AR | confirmed | — |
| 105 | "Our typical share of wallet increases from under 20% in years 3–7 to over 40% after year 12" | H1L | confirmed | — |
| 106 | "Large enterprise merchants typically work with multiple payment service providers…" | AR | confirmed | — |
| 107 | H1 2026 margin 49%, 50% without one-time transaction costs; "demonstrating the underlying operational efficiency…" | H1L | confirmed | — |
| 108 | November 2025: "to increase EBITDA margin levels to above 55% by 2028" | PR Investor Day (11 November 2025) | confirmed | — |
| 109 | 28 October 2026: "we now expect EBITDA margin of 50% in 2026. To retain flexibility, we are discontinuing our medium-term EBITDA objective." | Q3 | confirmed | — |
| 110 | "5,596 employees, 399 of them from the acquisitions" | Q3 ("a total of 5,596 FTEs") | corrected | "full-time staff" |
| 111 | One euro kept per about €590 processed (author's arithmetic) | 1,394.3 bn ÷ 2,364.2 m = 589.8 | confirmed | — |
| 112 | "Only a few dozen of the several hundred pages on Adyen's knowledge hub are engineering posts" | `adyen.com/sitemap-en.xml` (575 knowledge-hub addresses) | hedged | Now gives the 575 and labels the few dozen as the author's count; sitemap added to Sources |
| 113 | Title "From 0 to $100 billion" (January 2018) | knowledge-hub page title "From 0 — $100 billion: Scaling infrastructure and workflow at Adyen", 3 January 2018 | corrected | Title corrected in text and Sources |
| 114 | Design to Duty, July and August 2021 | displayed dates 28 July 2021 and 23 August 2021 | confirmed | — |
| 115 | Newer posts: PostgreSQL partitioning 2023 to 2025 | knowledge-hub partitioning-at-adyen (6 October 2023), partitioning-an-environment… (16 September 2025) | confirmed | Two source entries added (the claim had none) |
| 116 | "I found no post on topology, failover between regions or deployment frequency" | `adyen.com/infrastructure`; docs peak-season | corrected | Adyen names six data-center regions, says "we publish new releases of our core system every week", and documents failover by load balancers, an "active/active, stateless architecture", utilization "generally less than 30%" and a deployment freeze on named peak days (rulings 42, 43, 45) |
| 117 | 2021: stateless edge; "we don't mind if they are down for a little bit…"; local queue | D2D-1, D2D-2 | confirmed | — |
| 118 | Templates quotations; "the result will always be 0" | D2D-2 | confirmed | — |
| 119 | PostgreSQL, several clusters filled in rotation; "The migration to a sharded accounting database was quite painful" | D2D-2 ("a simple round-robin strategy") | confirmed | — |
| 120 | Whether the 2021 sharding is current | Postgres FM, episode of 7 June 2024, transcript: "at the moment we are actually reaching the limits of our sharding solution again. So we basically start redesigning the entire system again"; "We have both" | corrected (added) | Remark reported in the text and in "Where the Evidence Stops", as a podcast remark; source added (rulings 42b; note from chapter 38) |
| 121 | The 2021 passage on a distributed database | D2D-1 ("integrating Cockroach, a distributed database, with our PALs") | corrected (added) | One sentence added; the case had not mentioned it |
| 122 | "a single platform, in a single repository (monorepo), almost exclusively written in Java" | D2D-1 | confirmed | — |
| 123 | 2026: "Our monorepo alone runs to hundreds of thousands of files, and it's far from the only one."; "around 3,000 live services"; "tens of thousands of hosts spread across tens of data centres" | knowledge-hub architect-blog-1 (displayed 23 August 2026) | confirmed | — |
| 124 | 2018: "everybody develops on the main line"; "we toggle features one-by-one on production, and then canary them" | knowledge-hub (3 January 2018) | confirmed | — |
| 125 | "No platform-wide deployment frequency is public" | `adyen.com/infrastructure` | corrected | Weekly releases of the core system are stated; sentence replaced |
| 126 | 21 April 2025 attack; "specifically targeted services within our European datacenters"; resolved "by 03:20 CEST on April 22, 2025"; review to customers | knowledge-hub mitigating-a-ddos-april-2025 | confirmed | Source date corrected to the displayed 21 April 2025 (rulings 25, 43d) |
| 127 | 31 October 2025: "introducing additional global DDoS mitigation partners, such as Cloudflare, alongside existing global providers" | knowledge-hub strengthening-our-platform-resilience | confirmed | — |
| 128 | Annual report records a regulator-reportable DDoS incident | AR ("One regulatory-reportable DDoS incident occurred") | confirmed | Sentence cut for length |
| 129 | Transfers table: rows and their evidence | rows above | confirmed | — |
| 130 | Evidence stops: who acquires where | row 53, 56 | confirmed | Already in ruling-27 wording |
| 131 | Evidence stops: data centers ("cities, operators, a count…, owned or rented") | `adyen.com/infrastructure`; AR | corrected | Six regions are named; the report mentions "data center partners"; bullet rewritten |
| 132 | Evidence stops: accounting design | row 120 | corrected | Bullet now reports the 2024 remark |
| 133 | Evidence stops: where merchants' funds are held | AR ("balances at central and commercial banks"); docs EU depositor information sheet ("Your deposit is covered by the Dutch statutory Deposit Guarantee Scheme") | hedged | Parenthesis added (ruling 33f); the sheet says "Deposits in Adyen N.V.", so the text does not say "business accounts" |
| 134 | Evidence stops: earnings calls | not transcribed | not checked | Calls were not listened to in this pass either |
| 135 | Evidence stops: integration of Talon.One and Orb; definition of processed volume; the customer | rows 82, 98 | confirmed | — |
| 136 | Take-away: "The 53% margin is the return on twenty years of that order" | none; contradicts the chapter's own inference block on the margin | unsupported (removed) | Sentence removed |
| 137 | Adyen's reason for buying a loyalty engine is the terminal estate (inference block) | H1L ("By combining the global reach of more than 838K transacting terminals with our unified payments data…") | confirmed | — |
| 138 | Report timing, the sessions reason, the acquiring list as "unpublished" (point 4 of the brief) | article text | confirmed | The case makes none of these statements |
| 139 | Negative-balance period and Managed Risk pilot (ruling 41); uptime clause (ruling 45c) | article text | confirmed | The case makes no statement on either |
| 140 | Adyen documents payments settled by an external acquirer (ruling 31c) | — | not checked | Not on the page; the inference block on "full-stack" does not contradict it. Not added |

**Counts:** 140 rows: 110 confirmed, 15 corrected (three of them additions required by later rulings and findings), 9 hedged, 3 unsupported (two removed, one relabeled), 0 unreachable, 3 not checked. Rows 138–139 confirm absences on the page.

## Could not verify, and what was done

- **The ESEF reporting package** (the official filing) was not opened; the quotations rest on Adyen's own PDF, which is the same text as the copy first used.
- **The status page** renders its history client-side; the statement about it is now a statement that it was not read.
- **Adyen's help center** search could not be queried (404 on the search URL); the tax statement rests on the documentation index, the documentation sitemap and the site sitemap.
- **Row 63** (shared references across channels) rests on chapter 11.
- **Earnings calls** were not listened to.

## Evidence age

Marks present where used: 2018 listing release (8 years), 2018 engineering post (8), 2021 posts and US release (5), 2022 releases (4), UK release 2023 (3), H1 2023 release (3; added). Documentation pages are cited "n.d., accessed November 2026"; two "last modified" stamps were removed from Sources (ruling 30).

## Format

No inline external URLs. Three key points; callouts in order; case sections present; no "Where They Differ" section. Word count 6,000 (spec maximum 6,000), 26 min. To stay inside the limit after the additions, sentences that repeated a table or an earlier paragraph were cut (the Larkfield sentence in the in-person section, the 2022 capital-expenditure aside, the repeated note on earlier acquisitions, the customer's-side restatement of share of wallet). No unit was added, dropped, merged or reordered; `validate_spec.py` and `check_draft.py structure` pass. Render check: one unresolved link, `[[stripe-and-adyen-bets-compared]]` (chapter 48 is not written yet).

## Ledger conflicts

None. Checked: Mila's €120.00 ten-class pass at Studio Noord on 9 March 2027, on Adyen; Adyen's 56% share (€627 million) and all front-desk terminals; Stripe 44%; 11 people in the payments team; the ledger since 2025; K8.

## For other pages

- **`journal-spec.json`, entry for this page (copied into `spec.json`, left unchanged because the two must agree).** Sentences that overreach, exact wording:
  1. `intent.outcome.know[0]`: "founded in Amsterdam in 2006 with a European acquiring license". Adyen's history page dates the license only to the period 2006–2012.
  2. Part 10 `thesis.how_why`: "on 1 July 2026 Adyen closed its first two acquisitions, one of which runs apart from the platform"; and the entry for chapter 48, acceptance criterion: "Adyen closed its first two acquisitions on 1 July 2026". No Adyen document says "first"; its history page lists none earlier. "Runs apart" is Adyen's June 2026 description; on 28 October 2026 it wrote of "the successful ongoing integration of Talon.One and Orb".
  3. `thesis.claim`: "it uses banking partners where it has no acquiring license"; `intent.outcome.know[3]`: "banking partners where it has no acquiring license"; supporting claim S3: "banking partners stand in where it has no acquiring license". The annual report's sentence is about concentration risk; the reading is an inference (ruling 27c).
  4. `thesis.how_why`: "data-center locations, the integration plan for the acquisitions and the identity of the single large-volume customer behind its 2025 volume figures are not public"; `intent.outcome.know[3]`: "data-center locations and ownership". Adyen's Infrastructure page names six regions, and the annual report mentions "data center partners"; cities, operators and counts are what is not public.
  5. `thesis.claim` and `thesis.how_why`: "its own data-center capacity", "data centers are the main capital expenditure". The second is confirmed; "its own" should be read with the report's "data center partners".
  6. `thesis.disputed_by`: "that 'built, not bought' still describes the company". The phrase is in quotation marks; ruling 16 says it is in no Adyen document. It is attributed to the opposing view, so it may stand, but the quotation marks invite attribution.
  7. `thesis.how_why`: "Its engineering publications are few and mostly from 2018 to 2021". The architecture posts are; the partitioning series (2023–2025), the Architect post (2026) and the documentation's peak-season page are later.
  8. `conclusion.callback.how` (post spec only): "true of everything Adyen sold until 30 June 2026" is the author's reading, not a documented statement.
- **Journal spec, Part 8, chapter 39 entry** (`know[3]`): "data-center locations for Adyen" as not public; same correction as item 4.
- **Any page citing the Annual Report 2025 through the Bundestag copy** can cite `investors.adyen.com/financials/2025` (ruling 45d).
- **Any page that says integration of Talon.One and Orb is only "intent"**: Adyen's closing release says it "will begin integrating" both, and its release of 28 October 2026 says "the successful ongoing integration of Talon.One and Orb".
- **Chapter 41** (and ruling 43b): Adyen's Infrastructure page also says "we publish new releases of our core system every week – without downtime".
