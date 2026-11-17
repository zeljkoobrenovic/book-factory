# Research brief: Stripe and Adyen as companies, the bets compared, contrast cases and what is moving

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 46 (case: Stripe), 47 (case: Adyen), 48 (the bets compared), 49 (contrast cases: PayPal and Braintree, Checkout.com, Block), 50 (what is moving in 2026), the introduction, and parts of 05 (economics), 06 (acquiring and connectivity) and 16 (licences and safeguarding). This brief covers the companies as companies: dated history, published figures with their definitions, what their leaders and filings say about why they chose their approach, and the changes under way. The internals of the APIs, ledgers and reliability practice are in the other briefs (`stripe-api`, `adyen-api`, `ledger`, `scale`).

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or document was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated product, legal and documentation pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, law-firm briefing, industry association), not from a primary document fetched in this session. The kind of source is named.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including every statement about why a company did something beyond what it has said, and every statement recalled but not fetched.

**Short keys for long document URLs** (full URLs are in the Source list):

| Key | Document | Published |
| --- | --- | --- |
| S-L22 | Stripe annual letter for 2022 (PDF) | 2023-04-05 |
| S-L23 | Stripe annual letter for 2023 (PDF) | 2024-03-13 |
| S-L24 | Stripe annual letter for 2024 (PDF) | 2025-02-27 |
| S-L25 | Stripe annual letter for 2025 (PDF) | 2026-02-24 |
| A-AR25 | Adyen Annual Report 2025 (PDF, 233 pages) | 2026-02 |
| A-H2-25 | Adyen H2 2025 Shareholder Letter (PDF) | 2026-02 |
| A-H1-26 | Adyen H1 2026 Shareholder Letter and interim statements (PDF) | 2026-08-13 |
| A-Q3-26 | Adyen Q3 2026 Business Update (PDF) | 2026-10-28 |
| PYPL-10K | PayPal Holdings Form 10-K for FY2025 | 2026-02-03 |
| XYZ-10K | Block, Inc. Form 10-K for FY2025 | 2026-02-26 |

**Evidence age matters.** Company histories rest on old press releases (2016–2022); those facts are stable, but the product descriptions in them are not. Sources published before November 2023 are flagged **(evidence age: N years)**. Financial figures are the companies' own, unaudited for interim periods, and each uses its own metric definitions: Stripe's "total volume", Adyen's "processed volume", PayPal's "TPV", Block's "GPV" and Checkout.com's "total payment volume" are not the same measure and must not be ranked against each other without saying so.

**Stripe is private.** It publishes no financial statements. Everything quantitative about Stripe comes from its annual letters and press releases, which give volume, customer counts and a few run-rate statements, never revenue, margin or headcount. Adyen is listed and files audited annual accounts. This asymmetry runs through every comparison in this brief.

**Research limitation.**

- Stripe newsroom pages were served in the en-NL locale (British spelling: "optimise", "authorisation"); US-locale wording may differ by spelling only. Quotes below follow the fetched text.
- **Stripe's regulated entities and acquiring sponsor banks**: only three facts were verified (the Irish entity's regulator, the US money-transmitter disclosure page, Fifth Third Bank for Treasury accounts). The Stripe licences page for Europe returned a 404; the services agreement does not name US acquiring banks. The Georgia bank charter rests on a secondary source.
- **Stripe headcount**: no current official figure exists. The last company statement is from November 2022.
- **Adyen's 2023 Investor Day targets** and the size of the August 2023 share-price fall were not fetched; the 2025 Investor Day release, which restates them as "[Unchanged]" or "[Updated]", was.
- **Earnings-call remarks** (Adyen's 23 April, 11 June and 13 August 2026 calls) were not transcribed; statements about the acquisitions come from press releases, the shareholder letter and two Adyen knowledge-hub articles.
- **Mastercard Agent Pay**: mastercard.com returned HTTP 403; the product is confirmed only through a Mastercard executive's quote in Adyen's release.
- **Pix and UPI**: the Banco Central do Brasil and NPCI statistics pages render client-side and returned no data; figures are from a trade-research article.
- **PSD3/PSR**: the latest source found is a law-firm briefing of 15 September 2026; whether the texts reached the Official Journal between then and 17 November 2026 could not be confirmed.
- **Checkout.com cloud hosting**: the AWS case-study page returned only navigation text; nothing is claimed here. See the `scale` brief.
- **PayPal Fastlane**: the word does not appear in the FY2025 Form 10-K (full-text check in this session), so nothing about it is sourced from the filing.
- Acquisitions of **Okay** and the launch dates of **Radar** (2016), **Treasury** (2020) and **Link** were not verified from a dated Stripe page.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: guidance, pending acquisitions, release phases, pricing, regulation in progress, user counts.

---

## PART 1: Stripe as a company (chapter 46; introduction)

### 1.1 Dated history

| Date | Step | Status and source |
| --- | --- | --- |
| 2010 | Company founded by Patrick and John Collison; first venture backing | An investor quote in a Stripe release says a16z has "been their partners since 2010"; Sequoia: "When we first partnered with Stripe in 2010, it was a scrappy payments innovator" [VERIFIED: https://stripe.com/newsroom/news/stripe-2025-update, published 2026-02-24; https://stripe.com/newsroom/news/employee-liquidity-feb-2024, published 2024-02-28]. The founding date itself is [ASSUMPTION/JUDGEMENT] (not stated in a fetched Stripe document). |
| 2011 | Public launch | "this journey was still in its infancy when Stripe launched in 2011" [VERIFIED: S-L23, published 2024-03-13] |
| Oct 2012 | Connect (payments for platforms) | "In October 2012, we launched Stripe Connect" [VERIFIED: https://stripe.com/blog/the-new-connect, published 2015-03-23] **(evidence age: 11 years; the date is a historical fact, the product has been rebuilt since)** |
| 24 Feb 2016 | Atlas (company incorporation) | [VERIFIED: https://stripe.com/newsroom/news/stripe-launches-atlas, published 2016-02-24] **(evidence age: 10 years)** |
| 2016 | Radar (fraud) | [WIDELY REPORTED: third-party timeline, https://timelines.issarice.com/wiki/Timeline_of_Stripe, n.d.] gives 19 October 2016; not verified from Stripe. Radar 2.0 "with new tools for large businesses" is verified [VERIFIED: https://stripe.com/newsroom/news/stripe-radar-2, published 2018-04-18] **(evidence age: 8 years)** |
| 5 Apr 2018 | Billing | "a new product built on top of its core payments infrastructure that simplifies the recurring billing process" [VERIFIED: https://stripe.com/newsroom/news/stripe-launches-billing, published 2018-04-05] **(evidence age: 8 years)** |
| 26 Jul 2018 | Issuing | [VERIFIED: https://stripe.com/newsroom/news/stripe-launches-issuing, published 2018-07-26] **(evidence age: 8 years)** |
| 17 Sep 2018 | Terminal (in-person) | "a programmable point of sale for in-person payments" [VERIFIED: https://stripe.com/newsroom/news/stripe-launches-terminal, published 2018-09-17] **(evidence age: 8 years)** |
| 5 Sep 2019 | Capital (lending) | [VERIFIED: https://stripe.com/newsroom/news/stripe-capital, published 2019-09-05] **(evidence age: 7 years)** |
| 2020 | Treasury (banking-as-a-service for platforms) | Date [ASSUMPTION/JUDGEMENT]; the newsroom page carries no date in its metadata |
| 14 Mar 2021 | Series H at a $95B valuation | [VERIFIED: https://stripe.com/newsroom/news/stripe-series-h, published 2021-03-14] **(evidence age: 5 years)** |
| 10 Jun 2021 | Tax | "automatically calculate and collect sales tax, VAT, and GST in over 30 countries and all US states" [VERIFIED: https://stripe.com/newsroom/news/stripe-launches-stripe-tax, published 2021-06-10] **(evidence age: 5 years; coverage has grown — "50 US states and 50 countries" by February 2024)** |
| 14 Jul 2021 | Identity | [VERIFIED: https://stripe.com/newsroom/news/stripe-launches-identity, published 2021-07-14] **(evidence age: 5 years)** |
| 21 Sep 2021 | Revenue Recognition | [VERIFIED: https://stripe.com/newsroom/news/revenue-recognition, published 2021-09-21] **(evidence age: 5 years)** |
| 4 May 2022 | Financial Connections | [VERIFIED: https://stripe.com/newsroom/news/financial-connections, published 2022-05-04] **(evidence age: 4 years)** |
| 3 Nov 2022 | Layoff of about 14% | See 1.6 |
| 23 Jan 2023 | Expanded agreement with Amazon and AWS | See 1.6 |
| 29 Sep 2025 | Instant Checkout in ChatGPT; Agentic Commerce Protocol released | See PART 5 |
| Sep 2025 | Tempo blockchain unveiled, "incubated together with Paradigm" | [VERIFIED: S-L25, published 2026-02-24] |
| 18 Mar 2026 | Tempo mainnet live | See PART 5 |
| 29 Apr 2026 | Sessions 2026: "288 launches" | See 1.3 |

### 1.2 Acquisitions: announced versus completed

| Target | What it does | Status | Source |
| --- | --- | --- | --- |
| Paystack (Lagos) | Payments in Africa | Agreement announced 15 Oct 2020 ("has entered into an agreement to acquire Paystack") | [VERIFIED: https://stripe.com/newsroom/news/paystack-joining-stripe, published 2020-10-15] **(evidence age: 6 years)** |
| TaxJar | US sales-tax tools | "Stripe will acquire TaxJar", 27 Apr 2021 | [VERIFIED: https://stripe.com/newsroom/news/taxjar, published 2021-04-27] **(evidence age: 5 years)** |
| Bouncer | Card scanning for fraud prevention | "Stripe acquires Bouncer", 14 May 2021 | [VERIFIED: https://stripe.com/newsroom/news/bouncer, published 2021-05-14] **(evidence age: 5 years)** |
| Recko | Payments reconciliation | "Stripe will acquire Recko", 20 Oct 2021 | [VERIFIED: https://stripe.com/newsroom/news/recko, published 2021-10-20] **(evidence age: 5 years)** |
| Okay | Engineering analytics | Not verified | [ASSUMPTION/JUDGEMENT] no Stripe newsroom entry found in the list fetched 2026-11-17 |
| Lemon Squeezy | Merchant of record for digital products | Announced by Lemon Squeezy on 26 Jul 2024. ⚠ Its site now states: "Lemon Squeezy is no longer accepting new sign-ups and will shut down on March 31, 2027" | [VERIFIED: https://www.lemonsqueezy.com/blog/stripe-acquires-lemon-squeezy, published 2024-07-26, banner accessed 2026-11] |
| Bridge | Stablecoin orchestration | Announced October 2024 ("In October, we announced our acquisition of Bridge"); **completed 4 Feb 2025** | [VERIFIED: S-L24, published 2025-02-27; https://stripe.com/newsroom/news/stripe-completes-bridge-acquisition, published 2025-02-04] |
| Privy | Programmable crypto wallets ("more than 110 million") | "In July, Stripe acquired Privy" (2025) | [VERIFIED: https://stripe.com/newsroom/news/stripe-2025-update, published 2026-02-24] |
| Metronome | Usage-based billing and metering | **Completed 14 Jan 2026** | [VERIFIED: https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition, published 2026-01-14] |
| OpenRouter | AI model gateway and routing ("400+ models from more than 80 providers") | ⚠ **Agreement announced 19 Aug 2026.** No completion release in the newsroom list fetched 17 Nov 2026 | [VERIFIED: https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter, published 2026-08-19] |
| Parafin | Embedded credit for platforms' small businesses | ⚠ **Agreement announced 30 Sep 2026**; "expected to close in the coming months, subject to customary closing conditions, including any required regulatory clearances" | [VERIFIED: https://stripe.com/newsroom/news/stripe-agrees-to-acquire-parafin, published 2026-09-30] |

Why Stripe says it bought two of them:

- Metronome: "Metering and billing are in a very direct sense the interface between "product" and "business"... We're looking forward to integrating these capabilities with the Stripe Billing platform" (Patrick Collison) [VERIFIED: https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition, published 2026-01-14].
- OpenRouter: "Tokens are the central currency for companies building with AI... Stripe is building the economic infrastructure for AI, and together with OpenRouter we'll help businesses maximise profitability by routing their requests intelligently and spending their tokens efficiently" (Patrick Collison). OpenRouter had been a Stripe customer since at least 29 January 2026 [VERIFIED: https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter, published 2026-08-19; https://stripe.com/newsroom/news/openrouter-and-stripe, published 2026-01-29].
- [ASSUMPTION/JUDGEMENT] OpenRouter is not a payments company. The purchase shows Stripe defining its market as "economic infrastructure for AI" (its own phrase), which is wider than payments and revenue infrastructure. Chapter 46 should say this plainly and chapter 50 should treat it as consolidation around AI companies as customers, not as a payments move.

### 1.3 The annual letters, 2022–2025: exact wording

| Letter | Volume statement | Profitability statement | Customer statement | Revenue-suite statement |
| --- | --- | --- | --- | --- |
| 2022 (S-L22) | "businesses built on Stripe processed more than $817 billion in total volume in 2022, up 26% from the prior year" | none found | "More than 100 companies now handle more than $1 billion in payments with Stripe every year"; "millions of businesses"; "Stripe now supports businesses in more than 50 countries" | none |
| 2023 (S-L23) | "the businesses running on Stripe passed the milestone of $1 trillion in total payment volume in 2023, up 25% from the prior year... roughly 1% of global GDP" | "Stripe was robustly cashflow positive in 2023 and expects to be again in 2024" | "more than 100 companies now processing more than $1 billion per year with Stripe" | "we expect the suite's annual revenue run rate to pass $500 million over the next year" |
| 2024 (S-L24) | "Businesses on Stripe generated $1.4 trillion in total payment volume in 2024, up 38% from the previous year... around 1.3% of global GDP" | "Stripe was profitable in 2024, and we expect to be so in 2025 and beyond" | "half of the Fortune 100 uses Stripe"; "80% of the Forbes Cloud 100 and 78% of the Forbes AI 50"; "one in six new Delaware corporations incorporates with Stripe Atlas" | "Stripe's Revenue and Finance Automation Suite, with Billing at its core, has now passed a $500 million revenue run rate. Billing is being used by more than 300,000 companies, manages nearly 200 million active subscriptions" |
| 2025 (S-L25) | "businesses running on Stripe generated $1.9 trillion in total volume, up 34% from 2024, and equivalent to roughly 1.6% of global GDP" | "Stripe remained robustly profitable, allowing us to continue investing heavily in product development (with more than 350 product updates last year) as well as acquisitions" | "more than 5 million businesses directly or via platforms... 90% of the Dow Jones Industrial Average... 80% of the Nasdaq 100... 25% of all Delaware corporations are now created with Stripe Atlas"; Link "is now used by more than 200 million people" | "Metronome joins our Revenue suite, which is on track to hit an annual run rate of $1 billion this year" |

[VERIFIED: S-L22, published 2023-04-05 **(evidence age: 3.5 years; superseded by later letters)**; S-L23, published 2024-03-13; S-L24, published 2025-02-27; S-L25, published 2026-02-24]

Notes a chapter writer needs:

- **The metric's name changed.** 2022: "total volume"; 2023 and 2024: "total payment volume"; 2025: "total volume". None of the letters defines the metric (gross or net of refunds, whether Bridge stablecoin flows or Treasury transfers count) [VERIFIED: the four letters]. [ASSUMPTION/JUDGEMENT] Treat it as gross value moved by businesses on Stripe; do not present it as comparable to Adyen's processed volume, and never as revenue.
- **"Profitable" is undefined.** The 2023 letter says "cashflow positive"; 2024 says "profitable"; 2025 says "robustly profitable". No measure (GAAP net income, operating income, free cash flow) is named [VERIFIED: same]. Stripe has not published revenue in any letter.
- **R&D claim**: "In each of the last six years, Stripe has reinvested a much higher proportion of our earnings in R&D than any comparable company" [VERIFIED: S-L24, published 2025-02-27]. Not checkable from outside.
- **Reliability claims** (useful to chapter 37 as well): "Our API reliability is now consistently in excess of 99.999%" [VERIFIED: S-L22] **(evidence age: 3.5 years)**; "a battery of around 1.4 million tests... half a million CPU cores to execute more than 6 billion test runs each day", a core API service deployed "approximately 400 times in a typical day", rollouts "inspected against 55,000 different metrics" [VERIFIED: S-L23, published 2024-03-13].
- **Sessions 2026** (29 April 2026): "288 new products and features"; Link "a consumer wallet with over 250 million users globally"; "Businesses building on Stripe make payments to each other 4.8 million times a day"; the new Treasury is "a global business account that allows companies to hold funds in 15 currencies"; payouts "to recipients in 100 countries with fiat, 160 with stablecoins" [VERIFIED: https://stripe.com/newsroom/news/sessions-2026, published 2026-04-29]. ⚠
- **Platforms**: "More than 18,000 platforms build on Stripe" [VERIFIED: https://stripe.com/newsroom/news/stripe-agrees-to-acquire-parafin, published 2026-09-30].

### 1.4 Valuations from funding rounds and tender offers

All five are from Stripe's own releases, so they are primary, not secondary. A tender-offer valuation is the price at which investors and the company bought employees' shares; it is not a market capitalisation.

| Date | Event | Valuation | Source |
| --- | --- | --- | --- |
| 14 Mar 2021 | Series H ($600M raised) | $95B | [VERIFIED: https://stripe.com/newsroom/news/stripe-series-h, published 2021-03-14] **(evidence age: 5 years)** |
| 15 Mar 2023 | Series I (more than $6.5B, used for employee liquidity and tax withholding) | $50B | [VERIFIED: https://stripe.com/newsroom/news/stripe-series-i-employee-liquidity, published 2023-03-15] **(evidence age: 3.5 years)** |
| 28 Feb 2024 | Tender offer | $65B | [VERIFIED: https://stripe.com/newsroom/news/employee-liquidity-feb-2024, published 2024-02-28] |
| 27 Feb 2025 | Tender offer | $91.5B | [VERIFIED: https://stripe.com/newsroom/news/employee-liquidity-feb-2025, published 2025-02-27] |
| 24 Feb 2026 | Tender offer (investors include Thrive Capital, Coatue, a16z; Stripe also repurchases) | $159B ⚠ | [VERIFIED: https://stripe.com/newsroom/news/stripe-2025-update, published 2026-02-24] |

The Series I release adds: "Stripe does not need this capital to run its business" [VERIFIED: same, 2023-03-15].

### 1.5 Stripe's own description of its strategy

- **Mission.** "Our mission is to grow the GDP of the internet", pursued in "four primary ways": "Increasing the rate of new business creation by lowering the cost and complexity of starting a business"; "Helping established enterprises adapt to the internet"; "Reducing impediments to payments, especially across borders"; "Lowering the costs of scaling by providing simple, reliable, secure, and developer-friendly APIs and services" [VERIFIED: S-L22, published 2023-04-05] **(evidence age: 3.5 years; the mission sentence is repeated in S-L23)**.
- **Self-description over time**, from the first line of its press releases: "builds economic infrastructure for the internet" (2021, 2023); "a financial infrastructure platform for businesses" (2024, 2025); "the programmable financial services company" (December 2025 onward) [VERIFIED: stripe-series-h 2021-03-14; employee-liquidity-feb-2024 2024-02-28; agentic-commerce-suite 2025-12-11, all at https://stripe.com/newsroom/news/].
- **Starting with startups, growing into enterprise.** "Stripe grew up with companies in the technology sector... Increasingly, however, some of the most august enterprises and established brands, such as the PGA, Toyota, The Atlantic... MAN, and Maersk are turning to Stripe" [VERIFIED: S-L22]. "Stripe's enterprise user base has compounded since 2019, and now includes some of the largest global enterprises like Amazon, Ford, Salesforce, BMW, and Maersk. At the same time, Stripe continues to see strong momentum with startups" [VERIFIED: https://stripe.com/newsroom/news/stripe-series-i-employee-liquidity, published 2023-03-15]. "Many now-household names, such as Instacart, Substack, and DoorDash... charged their customers with us from the very beginning" [VERIFIED: S-L22].
- **Users first as product strategy.** "Our first operating principle is "Users First."... just listening to suggestions is a surprisingly effective product strategy. Last year... we shipped 244 new user-facing features and 336 API updates" [VERIFIED: S-L22].
- **A suite, sold as a suite.** "One hundred businesses now handle more than $1 billion on Stripe every year. Seventy-five percent of these global winners use Stripe for more than just payments" [VERIFIED: stripe-series-i-employee-liquidity, 2023-03-15]. A Thrive Capital partner, in Stripe's release: "the premiere financial infrastructure stack for the internet economy, relied on by the fastest growing companies for payments, billing, fraud prevention, tax and more" [VERIFIED: stripe-2025-update, 2026-02-24].
- **The long tail as the main market.** "This isn't merely about incremental revenue from a 'long tail' of international users. In many cases, the 'long tail' is much of the dog" [VERIFIED: stripe-2025-update, 2026-02-24].
- **Optimisation as the enterprise pitch.** "We're continually retraining dozens of machine learning models that optimise every part of the transaction flow over an economy-scale dataset... Businesses simply start making more money when they switch to Stripe" [VERIFIED: https://stripe.com/newsroom/news/stripe-2024-update, published 2025-02-27].

### 1.6 Licences, banks, hosting, headcount

- **Europe.** Stripe's site footer states: "Stripe Technology Europe, Limited, trading as Stripe, is regulated by the Central Bank of Ireland" [VERIFIED: footer text of https://stripe.com/jobs and other stripe.com pages, n.d., accessed 2026-11]. [ASSUMPTION/JUDGEMENT] The authorisation is as an electronic money institution, not a bank; the register entry was not fetched.
- **United States.** Stripe Payments Company publishes state-by-state money-transmission disclosures naming the state regulators (Alaska, Arizona, California, Colorado, Connecticut, District of Columbia, Florida, Illinois and others) [VERIFIED: https://stripe.com/legal/spc/licenses, n.d., accessed 2026-11].
- **Not a bank.** "Stripe is not a bank. Checking accounts are provided exclusively by Fifth Third Bank, National Association, Member FDIC" [VERIFIED: https://stripe.com/newsroom/news/treasury-for-agents, published 2026-10-21; same wording at https://docs.stripe.com/treasury.md, n.d., accessed 2026-11]. ⚠ Partner banks change.
- **A limited US bank charter.** The state of Georgia approved Stripe's application for a merchant acquirer limited purpose bank (MALPB) charter; "The charter will allow the financial services company to obtain direct membership with Visa and Mastercard and to process payments without a sponsoring bank" [WIDELY REPORTED: industry association, https://www.icba.org/newsroom/news-and-articles/2025/07/08/georgia-approves-stripe-application-to-form-malpb, 2025]. The same source family notes the charter does not allow deposit taking. Whether Stripe now processes through it is not public in anything fetched. ⚠
- **Acquiring sponsor banks.** Nothing verified. The Stripe Services Agreement fetched in this session does not name them [VERIFIED by absence: https://stripe.com/legal/ssa, accessed 2026-11].
- **Hosting.** "Stripe has long relied on AWS to provide the core compute infrastructure on which Stripe is built." "We couldn't run without AWS—and we wouldn't want to," said David Singleton, then chief technology officer. AWS's CEO: "Stripe has entrusted AWS with their core operations for over a decade" [VERIFIED: https://stripe.com/newsroom/news/amazon-and-stripe, published 2023-01-23] **(evidence age: 3.8 years; nothing newer contradicts it; the 2026 AWS AgentCore partnership with Privy shows the relationship continuing** [VERIFIED: https://stripe.com/newsroom/news/aws-stripe-agentcore-privy, published 2026-05-07]**)**.
- **Headcount.** On 3 November 2022: "We're reducing the size of our team by around 14%... which will return us to our February headcount of almost 7,000 people" [VERIFIED: https://stripe.com/newsroom/news/ceo-patrick-collisons-email-to-stripe-employees, published 2022-11-03] **(evidence age: 4 years)**. No later official number was found. Third-party trackers in 2026 range from about 10,400 to about 17,000 [WIDELY REPORTED: data aggregators, e.g. https://www.reveliolabs.com/companies/stripe/employees/, 2026]; the spread makes them unusable in print.

### Stripe vs Adyen (this part)

| Aspect | Stripe | Adyen | What the difference supports |
| --- | --- | --- | --- |
| Disclosure | Annual letter: volume, customer counts, run-rate remarks; no revenue, margin or headcount (2023–2026) | Audited annual report, half-year letters, quarterly updates with volume, net revenue, EBITDA, FTE by office (2025–2026) | Every Stripe figure is company-selected; every Adyen figure is defined in notes [VERIFIED above and PART 2] |
| Acquisitions | At least ten named, 2020–2026, two pending | None until two closed on 1 July 2026 | See PART 3 |
| Self-description | "the programmable financial services company" (2025–26) | "the financial technology platform of choice for leading companies" (2023–26) | Both left "payments" out of the tagline [VERIFIED: press releases cited] |
| Hosting | AWS, stated 2023 | Own data-center capacity is the main capital expenditure, stated 2025–26 | See PART 3.6 |

### For readers new to payments

- **Total (payment) volume**: the value of all payments businesses run through a provider in a period; the provider keeps only a small fraction of it as fees.
- **Run rate**: the latest period's revenue multiplied up to a year; a statement about pace, not an annual total.
- **Tender offer** (private company): investors or the company buy existing shares from employees at a set price, which implies a valuation without raising money for operations.
- **Sponsor bank**: a bank that is a member of the card networks and lets a non-bank processor acquire card payments under its membership.

### Architecture implications

[ASSUMPTION/JUDGEMENT] (1) A builder choosing Stripe is choosing a product suite whose parts arrived at different times, some by acquisition (tax, reconciliation, usage billing, stablecoins, merchant of record); integration depth between them is a question to test, not assume. (2) Stripe's partner-bank model means the bank behind a product is a dependency that can change; design reconciliation and customer disclosures so the named bank is data, not code. (3) Stripe's public numbers cannot support capacity or cost planning; get contractual figures.

---

## PART 2: Adyen as a company (chapter 47; introduction)

### 2.1 Dated history

| Date | Step | Source |
| --- | --- | --- |
| 2006 | "We were founded in Amsterdam in 2006. We secured a European acquiring license, added POS and risk tools, and expanded into San Francisco, London, Paris, and Stockholm" (2006–2012) | [VERIFIED: https://www.adyen.com/about, n.d., accessed 2026-11] |
| 2017 | European banking licence ("its European banking license (obtained in 2017)") | [VERIFIED: https://www.adyen.com/press-and-media/adyen-granted-us-branch-license, published 2021-06-14] **(evidence age: 5 years)** |
| 11–13 Jun 2018 | IPO priced at €240 per share, "implying a market capitalization of €7.1 billion"; first trading on Euronext Amsterdam under "ADYEN" on 13 June 2018; existing shares only (about 12–13.4% of share capital) | [VERIFIED: https://www.adyen.com/press-and-media/adyen-ipo-priced-at-240-per-share, published 2018-06-11] **(evidence age: 8 years)** |
| 2018 | Long-term payment-services contract with eBay | [VERIFIED: A-H2-25, note on the eBay contract, published 2026-02] |
| 24 May / 14 Jun 2021 | US Federal Foreign Branch in San Francisco: Federal Reserve approval 24 May 2021; OCC approval announced 14 June 2021. "This license was a logical next step for Adyen, and one that has long been on the horizon" (Pieter van der Does) | [VERIFIED: same US release, 2021-06-14] **(evidence age: 5 years)** |
| 31 Mar 2022 | "Adyen expands beyond payments, announces embedded financial products" (accounts, issuing, capital for platforms) | [VERIFIED: https://www.adyen.com/press-and-media/adyen-expands-beyond-payments-announces-embedded-financial-products, published 2022-03-31] **(evidence age: 4.6 years)** |
| 4 Oct 2022 | Open banking (pay-by-bank) "on its single platform", "realized in partnership with Tink" | [VERIFIED: https://www.adyen.com/press-and-media/adyen-launches-next-generation-open-banking-solution-in-partnership-with-tink, published 2022-10-04] **(evidence age: 4 years)** |
| 17 Aug 2023 | H1 2023 results: net revenue €739.1M (+21%), EBITDA €320.0M (−10%), margin 43%, "primarily impacted by increased wages and salaries stemming from Adyen's investments into scaling its global team" | [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2023-financial-results, published 2023-08-17] **(evidence age: 3.2 years)** |
| 7 Sep 2023 | UK banking authorisation (PRA and FCA, Part 4A FSMA) | [VERIFIED: https://www.adyen.com/press-and-media/adyen-granted-uk-banking-authorization, published 2023-09-07] **(evidence age: 3.2 years)** |
| 8 Nov 2023 | Investor Day in San Francisco; "evolved its financial objectives in order to specify timelines around growth expectations" | [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-q3-business-update, published 2023-11-08] |
| 11 Nov 2025 | Investor Day in Amsterdam; EBITDA objective "above 55% by 2028"; "approximately 20% annual net revenue growth in any given year" after 2026; move to annual guidance | [VERIFIED: https://www.adyen.com/press-and-media/adyen-hosts-investor-day-2025-in-amsterdam, published 2025-11-11] |
| 2 Apr 2026 | Founding member of the x402 Foundation | See PART 5 |
| 9 Apr 2026 | Intelligent Money Movement launched | [VERIFIED: https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement, published 2026-04-09] |
| 23 Apr 2026 | Agreement to acquire Talon.One announced | See 2.4 |
| 11 Jun 2026 | Agreement to acquire Orb announced | See 2.4 |
| 16 Jun 2026 | Adyen Agentic announced, limited availability | See PART 5 |
| 1 Jul 2026 | Both acquisitions closed; Chief Product Officer appointed | See 2.4 |
| 28 Oct 2026 | Q3 2026 update; medium-term EBITDA objective discontinued | See 2.3 |

The 2023 reset in one paragraph, with its evidence limits: Adyen had hired fast through 2022–23; EBITDA margin fell from 55% in 2022 to 46% in 2023 [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h2-2023-financial-results, published 2024-02-08]. [ASSUMPTION/JUDGEMENT] The H1 2023 results were followed by a one-day share-price fall of roughly 39%, and the November 2023 Investor Day replaced open-ended "medium-term" objectives with dated ones (net revenue growth between the low twenties and high twenties percent through 2026, EBITDA margin above 50% in 2026, capital expenditure up to 5% of net revenue). These two details are recalled, not fetched; the 2025 Investor Day release confirms the capex objective and the 2026 growth range as "[Unchanged]". Margin did recover: 50% in 2024, 53% in 2025 [VERIFIED: A-AR25].

### 2.2 The single platform, the licences and the Formula: exact statements

- **The strategic choice.** "From the beginning, we made a strategic choice: rather than build a business around the limitations of external providers, we would develop and operate the essential layers of the financial stack ourselves." "The first step was our single global platform — we removed much of the fragmentation that typically characterizes global payment systems... It also ensured that any improvement we make, from responding to new regulations to tackling emerging fraud patterns, takes effect everywhere, without reintegration work." "This led to the next layer: acquiring our own banking licenses in the EU, US, and UK. Operating these licenses ourselves allows us to perform mission-critical activities without relying on partner banks, improving reliability and settlement speed. It also enables products such as issuing, bank accounts, and capital to function within the same unified environment" [VERIFIED: A-AR25, "The evolution of our foundation", published 2026-02].
- **At a glance.** "We simplify global commerce by replacing what is traditionally a fragmented, multi-party setup with a single platform built entirely in-house. Our product offering spans both payments and financial services, all operated end-to-end on our own infrastructure and banking licenses" [VERIFIED: A-AR25].
- **Licences as strategy.** "Operating under our own licensing stack has always been a cornerstone of Adyen's strategy. It supports global growth, keeps critical knowledge and control in-house, and reinforces customer trust... and provides the speed and autonomy that come from not relying on external parties for regulatory compliance" [VERIFIED: A-AR25, risk management].
- **Legal status.** "Adyen N.V.... is a licensed Credit Institution by De Nederlandsche Bank (the Dutch Central Bank)... The Credit Institution license includes the ability to provide cross-border services in the European Economic Area. Additionally, Adyen provides services in the United States through its US Federal Foreign Branch licence, and in the United Kingdom through its license to operate as a third party branch." Part of the AEX index; S&P credit rating A- [VERIFIED: A-AR25, notes to the financial statements].
- **More local licences in 2026.** "a Category II payments license from the Central Bank of the UAE, giving us full control over local settlements"; "approval for direct access to France's domestic interbank clearing system" (principal member of Cartes Bancaires and direct participant in STET) [VERIFIED: A-H1-26, published 2026-08-13]. Singapore Major Payment Institution licence, RBI licence in India and acquiring in Japan and the UAE are listed on the about page [VERIFIED: https://www.adyen.com/about, accessed 2026-11].
- **The 2022 formulation**, useful for chapter 41: "By building our banking infrastructure, as a part of the single platform, from the ground up, we remove the limitations of legacy financial systems... without the barriers of regulatory complexity, lengthy product development, or sponsor bank restrictions" (Thom Ruiter, then VP of Banking and Financial Products) [VERIFIED: embedded-financial-products release, 2022-03-31] **(evidence age: 4.6 years; restated in A-AR25)**.
- **Three layers, 2026 wording.** "A single, global technology platform... Customers benefit from faster access to new products and optimizations while we scale efficiently by avoiding duplication and minimizing maintenance overhead." "Global banking licenses: Our own licensed infrastructure grants direct access to payment networks, giving us control over funds." "Dynamic Identification" (the cross-merchant identity and behaviour dataset, introduced 2025) [VERIFIED: A-H1-26].
- **The Adyen Formula** (as published on the about page): "We build to benefit all customers (not just one)"; "We make good decisions and consider the long-term benefits for our customers, Adyen, and the world at large"; "Winning is more important than ego; we work as a team - across cultures and time zones"; "We don't hide behind email, instead we pick up the phone"; "We talk straight without being rude"; "We seek out different perspectives to sharpen our ideas"; "We create our own path to grow toward our full potential" [VERIFIED: https://www.adyen.com/about, n.d., accessed 2026-11]. The page showed seven lines in the text extracted; earlier versions had eight (one on launching fast and iterating) [ASSUMPTION/JUDGEMENT]. The annual report: "Unlike traditional value statements, it is practical and usable in day-to-day decision-making... when in doubt, you can go back to the Formula and know what to do next" [VERIFIED: A-AR25].
- **Enterprise first.** "Built for enterprise, not adapted to it." "Adyen was built from the ground up specifically around the needs of the world's largest businesses" [VERIFIED: https://www.adyen.com/about, accessed 2026-11].

### 2.3 Figures, with definitions

Definitions first, because they differ from Stripe's:

- **Net revenue** (non-IFRS): "Net non-interest revenue ("Non-interest revenue" less "Costs incurred from financial institutions" and "Costs of goods sold") and Net interest income". In plain words: what Adyen keeps after passing interchange and scheme fees through, and after the cost of terminals sold [VERIFIED: A-AR25, note 2.2].
- **Revenue sources**: settlement fees ("usually as a percentage of the transaction value, where Adyen offers acquiring services"), processing fees ("Fixed fee per transaction paid by merchants for the use of Adyen's platform"), sale of goods (terminals) and other services (FX, issuing, commissions) [VERIFIED: A-AR25, revenue note].
- **EBITDA margin**: "EBITDA as a percentage of "Net Revenue"" [VERIFIED: A-AR25].
- **Take rate**: net revenue divided by processed volume, in basis points (17.0 bps = €2,364.2M / €1,394.3B) [VERIFIED by arithmetic on A-AR25 figures].
- **Processed volume**: not defined in a single sentence in the passages read; "84% were full-stack volumes" in 2025, meaning Adyen was also the acquirer [VERIFIED: A-AR25]. [ASSUMPTION/JUDGEMENT] It is the value of transactions processed on the platform, including volume where Adyen is only the gateway.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 | Q3 2026 |
| --- | --- | --- | --- | --- | --- |
| Processed volume | €970.1B (+26%) | €1,285.9B (+33%; +27% excluding a single large-volume customer) | €1,394.3B (+8%; +21% excluding that customer) | €803.8B (+24%) | €451.1B (+30%) |
| Net revenue | €1,626.1M (+22%) | €1,996.1M (+23%) | €2,364.2M (+18%; +21% constant currency) | €1,302.9M (+19%; +21% cc) | €738.1M (+23%; +22% cc) |
| EBITDA / margin | €743.0M / 46% | €992.3M / 50% | €1,245.7M / 53% | €641.5M / 49% (50% excluding €6.0M transaction costs) | not reported quarterly; 2026 guidance 50% |
| Point-of-sale (in-person) volume | €159.9B | €232.7B (18% of volume) | €310.9B (22%) | €175.7B (22%), +28% | not given; 878K transacting terminals |
| Take rate | not fetched | 15.5 bps | 17.0 bps ("driven by changes in the overall merchant mix") | 16.2 bps ("expected volume tiering") | not given |
| FTE (period end) | not fetched | 4,345 | 4,771 (+426) | 5,020 (+249) | 5,596 (incl. 399 from the acquisitions) |
| Capex / net revenue | 4% | 5% | 5% (€116.8M) | 5% (€64.1M) | 7% expected for 2026 |

[VERIFIED: FY2023 from https://www.adyen.com/press-and-media/adyen-publishes-h2-2023-financial-results, published 2024-02-08; FY2024 from https://www.adyen.com/press-and-media/adyen-publishes-h2-2024-financial-results, published 2025-02-13; FY2025 from A-AR25 and A-H2-25; H1 2026 from A-H1-26; Q3 2026 from A-Q3-26]

**Net revenue by pillar** (the "segment split"):

| Pillar | What it serves | FY2024 | FY2025 | H1 2026 | Q3 2026 |
| --- | --- | --- | --- | --- | --- |
| Digital | "online-first enterprises such as subscription businesses, travel, and mobility" | €1,229.5M | €1,334.9M | €719.7M (+13%) | €387.4M (+16%) |
| Unified Commerce | "connects online and in-person payments for global retailers, hospitality, and food & beverage groups" | €590.5M | €765.4M | €417.7M (+25%) | €250.5M (+29%, includes Talon.One) |
| Platforms | "enables software providers to embed payments and financial services" | €176.1M | €263.8M | €165.5M (+37%) | €100.2M (+46%) |

[VERIFIED: A-AR25 note on commercial pillars; A-H1-26; A-Q3-26]. The Q3 pillar figures sum to €738.1M; Orb's revenue is not attributed to a pillar in the text read [ASSUMPTION/JUDGEMENT].

Other figures:

- **Regions, FY2025**: EMEA 58%, North America 27%, APAC 10%, LATAM 6% of net revenue [VERIFIED: A-AR25]. H1 2026: North America €358.1M (27%), EMEA €722.5M (55%), APAC €136.9M (11%), LATAM €85.3M (7%) [VERIFIED: A-H1-26].
- **Customer concentration**: "Adyen's top 10 merchants represent 11% of revenue (2024: 12%). In 2025 and 2024 there were no single customers that, on an individual level, accounted for more than 10%" [VERIFIED: A-AR25]. "Large enterprise merchants typically work with multiple payment service providers to mitigate their own single-point-of-failure risk. As a result, these customers may terminate contracts or shift volume elsewhere" [VERIFIED: A-AR25, risk section]. "300 merchants now account for approximately 60% of total growth, down from over 70% three years ago" [VERIFIED: A-H1-26]. Churn "continued to be <1% in 2025, excluding one merchant" [VERIFIED: A-AR25].
- **The single large-volume customer.** FY2025 processed volume grew 8% reported and 21% excluding it; the customer sits in the Digital pillar, where H2 2025 processed volume "declined 1% YoY" including it and grew 11% excluding it. Separately, in the Platforms pillar in H2 2025, "Processed volume grew 28% YoY, or 54% excluding eBay" [VERIFIED: A-H2-25]. [ASSUMPTION/JUDGEMENT] The unnamed Digital customer is therefore not eBay (it is widely taken to be Block's Cash App); Adyen does not name it. The lesson for chapter 05: volume can fall while net revenue rises, because the largest customers pay the lowest rates.
- **Share of wallet**: "Our typical share of wallet increases from under 20% in years 3–7 to over 40% after year 12" [VERIFIED: A-H1-26].
- **Scale customers**: 499 customers "processing at least €10 million on both POS and eCommerce, with over €50 million in total processed volume in the last 12 months"; 46 platform customers above €1B a year (31 a year earlier); 312K active business customers on platforms [VERIFIED: A-Q3-26].
- **Hiring.** "During 2025 the composition of net joiners were 42% in tech roles, 37% in commercial roles and 22% in staff or supporting functions" [VERIFIED: A-AR25]. Q3 2026: "our recent hiring has been focused on specialized technical and go-to-market roles, particularly in the US"; "We now target 1,000-1,100 net-new FTEs in 2026, including Talon.One and Orb" [VERIFIED: A-Q3-26]. Amsterdam held 2,460 of 5,020 FTE at mid-2026; Bengaluru grew from 72 to 102 in six months [VERIFIED: A-H1-26].
- **Cash and interest.** "We ended the half with €12.4 billion of total cash. The majority of that number represents balances moving through our system on behalf of our merchants." Finance income of €143.2M in H1 2026 was "generated primarily from our balances at central and commercial banks" [VERIFIED: A-H1-26]. This is what a banking licence makes visible on the balance sheet (chapter 16).
- **Guidance as of 28 October 2026** ⚠: 2026 net revenue growth of 21–23% in constant currency; "we now expect EBITDA margin of 50% in 2026. To retain flexibility, we are discontinuing our medium-term EBITDA objective"; capex 7% of net revenue in 2026, returning "towards historical levels post-2026"; 2027 objectives in February 2027 [VERIFIED: A-Q3-26; https://www.adyen.com/press-and-media/adyen-publishes-q3-2026-business-update-6r9vz0, published 2026-10-28]. The objective dropped is the "above 55% by 2028" set at the November 2025 Investor Day.

### 2.4 The 2026 acquisitions and "built, not bought"

| | Talon.One | Orb |
| --- | --- | --- |
| What | Loyalty and promotions engine, Berlin, founded 2015, "300+ global merchants" | Usage-based billing platform, San Francisco, founded 2021; customers include Vercel, Glean, Replit, Supabase |
| Announced | 23 April 2026 | 11 June 2026 |
| Consideration | €750M, "from available cash resources"; founders reinvest in Adyen shares (€69.8M issued as shares) | $335M, cash; reverse triangular merger; $33.2M issued as shares |
| Closed | 1 July 2026 | 1 July 2026 |
| Size | "approximately €60 million in ARR as of the end of this year... growing 30–40% annually" | Total funding $44M before the deal; revenue not disclosed |
| Integration | Promotion engine integrated "directly into our architecture" | "an incubator model, preserving Orb's operational continuity during the first phase... and continuing to support multi-PSP environments. Beyond this first phase, the strategic intent is convergence" |

[VERIFIED: https://www.adyen.com/press-and-media/2i4hnm0pfcpvc7 (Talon.One), published 2026-04-23; https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj (Orb), published 2026-06-11; https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates, published 2026-07-01; A-H1-26 note 17]

Financial effect: "expected to add approximately 1 percentage point to net revenue growth in 2026", with "an estimated 1 percentage point margin dilution"; 399 employees joined [VERIFIED: A-H1-26; A-Q3-26].

What management said, in order:

- 9 April 2026, two weeks before the first deal: "Unlike many providers that rely on a patchwork of acquired technologies and third-party integrations, Adyen has built its entire financial technology stack on a single platform" [VERIFIED: Intelligent Money Movement release, 2026-04-09].
- 23 April 2026: "Many have tried to build a solution themselves but struggle to turn insights into action" (Ingo Uytdehaage, of merchants); the deal is "a natural next step in Adyen's long-term investment in Unified Commerce and data products" [VERIFIED: Talon.One release].
- 11 June 2026: "The structural complexity of modern billing has become the kind of infrastructure problem Adyen is built to take on" (Uytdehaage) [VERIFIED: Orb release].
- 1 July 2026: "Adyen has evolved into a comprehensive platform offering multiple, integrated solutions... Aligning our executive leadership with this multi-product reality is a natural step forward" (Uytdehaage) [VERIFIED: closing release].
- 13 August 2026: "Recognizing this shift, we made the deliberate decision to bring these solutions onto our platform." "While organic growth remains our foundation, our strong balance sheet allows us to selectively deploy capital to accelerate our platform roadmap." "we are no longer just a payments company. We are the complete financial operating system for modern commerce — from payments to loyalty, billing, and money movement" [VERIFIED: A-H1-26].
- 28 October 2026: "Customer interest in the combined offering... has been substantially stronger and broader than anticipated... we are intentionally accelerating our planned investment behind the Talon.One and Orb teams." "Since Orb joined Adyen, we won the payments volumes of several of their customers, including Route and Wasabi Technologies" [VERIFIED: A-Q3-26].
- An Adyen strategy executive on why not build: "At Adyen, we've historically stayed singularly focused on solving the hardest problems in payments... When the opportunity to do something presented itself, we decided to act" [VERIFIED: https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb, n.d., accessed 2026-11].
- **No fetched Adyen document uses the phrase "we build, not buy" or says the company has abandoned it.** Trade press described Talon.One as Adyen's first acquisition and a shift from building internally [WIDELY REPORTED: trade press, e.g. https://fintech.global/2026/04/24/adyen-acquires-talon-one-for-e750m/, 2026]. The about page now folds the deals into the history: "With the acquisition of Orb and Talon.One... we've moved beyond payments and built a full enterprise financial operating system" [VERIFIED: https://www.adyen.com/about, accessed 2026-11].

[ASSUMPTION/JUDGEMENT] What the acquisitions change and do not change, for chapter 47: (a) the payments core, the licences and the ledger remain built in-house, so "single platform" still describes payments; (b) loyalty and billing are adjacent products bought with their own stacks, and Orb is explicitly run apart for now and keeps serving other providers' payments, which is a two-platform state by Adyen's own description; (c) "convergence" is stated as intent, with no date. The honest sentence is: Adyen built its payments and banking platform and, from July 2026, buys adjacent software.

### Stripe vs Adyen (this part)

| Aspect | Stripe | Adyen | Supported difference |
| --- | --- | --- | --- |
| Billing | Built Billing in 2018; bought Metronome (completed Jan 2026) | No billing product until Orb (closed Jul 2026) | Eight years apart; both now own a usage-billing engine bought from a start-up [VERIFIED above] |
| Loyalty and promotions | Nothing public found (searched Stripe newsroom list and product menu) | Talon.One (closed Jul 2026) | Adyen's in-store estate (878K terminals) is the stated reason |
| In-person | Terminal, since 2018; volume share not published | €310.9B in 2025, 22% of volume | Only Adyen quantifies it |
| Customer concentration | "100 businesses now handle more than $1 billion" (2023); no revenue share | Top 10 = 11% of revenue (2025) | Different measures; not comparable |
| Headcount | Not published since 2022 | 5,596 FTE (Sep 2026) | — |

### For readers new to payments

- **Processed volume**: the value of transactions a provider handled; for Adyen about one six-thousandth of it becomes net revenue.
- **Net revenue**: revenue after passing on the fees owed to card networks and issuing banks; the number that reflects the provider's own business.
- **Take rate**: net revenue divided by processed volume, expressed in basis points (one basis point is 0.01%).
- **Full-stack volume**: volume where the provider is both the technical processor and the acquirer that settles the money.

### Architecture implications

[ASSUMPTION/JUDGEMENT] (1) Adyen's tiered pricing and falling take rate with scale mean a merchant's unit cost is a function of volume committed; multi-provider routing has a price. (2) An Adyen integration made before July 2026 touches one platform; one that uses Orb or Talon.One touches separate systems until convergence happens, so plan for separate credentials, events and reports. (3) Adyen's own risk section says large merchants use several providers; design for that from the start.

---

## PART 3: The bets compared (chapter 48; parts of 05, 06, 16)

Each row gives what each company has said, then the analyst's reading. Where one side has said nothing, that is stated.

### 3.1 Licence and money-holding

- Adyen: own banking licences in the EU, US and UK, chosen "without relying on partner banks, improving reliability and settlement speed" [VERIFIED: A-AR25]. Balances at central banks earn finance income (€267.6M in 2025) [VERIFIED: A-AR25].
- Stripe: "Stripe is not a bank"; accounts "provided exclusively by Fifth Third Bank" [VERIFIED: treasury-for-agents, 2026-10-21]; an Irish regulated entity and US state money-transmitter licences [VERIFIED: 1.6]; a Georgia limited-purpose acquiring charter approved in 2025 [WIDELY REPORTED: ICBA, 2025]. Stripe has published no statement explaining why it uses partner banks (searched: the four annual letters, newsroom).
- [ASSUMPTION/JUDGEMENT] Partner banks let Stripe launch financial products in a market without waiting years for a licence, at the cost of a dependency and a margin shared with the bank. The Georgia charter and Checkout.com's identical move (PART 4) suggest that at scale the acquiring dependency is worth removing even for a company that does not want to be a deposit-taking bank.

### 3.2 Connectivity: own acquiring versus mixed

- Adyen: "direct access to payment networks"; 84% of 2025 volume full-stack; direct participation in French clearing and a UAE licence added in 2026 [VERIFIED: A-AR25; A-H1-26].
- Stripe: nothing published on which markets it acquires in directly versus through sponsors (see the `acquiring` brief for documentation-level evidence).
- [ASSUMPTION/JUDGEMENT] The direction of travel is the same; Adyen started there, Stripe is arriving.

### 3.3 Build versus acquire

- Adyen: "a single platform built entirely in-house" (Feb 2026); two acquisitions closed 1 July 2026 [VERIFIED: 2.2, 2.4].
- Stripe: acquisitions named as a use of profits ("investing heavily in product development... as well as acquisitions") [VERIFIED: S-L25].
- [ASSUMPTION/JUDGEMENT] Until 2026 this was the cleanest difference between the two; it is now a difference of degree. Both bought usage-billing start-ups within six months of each other because AI companies bill by consumption and neither had built for it.

### 3.4 One platform versus a suite

- Adyen: one platform means an improvement "takes effect everywhere, without reintegration work" and "avoiding duplication and minimizing maintenance overhead" [VERIFIED: A-AR25; A-H1-26]. EBITDA margin "demonstrating the underlying operational efficiency inherent to our single-platform architecture" [VERIFIED: A-H1-26].
- Stripe: sells named products with separate prices; "Seventy-five percent of these global winners use Stripe for more than just payments" [VERIFIED: Series I release, 2023]. Stripe has not published a statement about a single code base.
- [ASSUMPTION/JUDGEMENT] "Single platform" is a claim about Adyen's engineering and operations; "suite" is a claim about Stripe's packaging. They are not opposites: Stripe's products share one API style, account model and ledger as far as its documentation shows (`stripe-api`, `ledger` briefs). Chapter 48 should compare what a customer integrates, not the slogans.

### 3.5 Customer base and pricing

- Adyen: "Built for enterprise, not adapted to it"; Platforms "allows us to provide payments and financial products to smaller merchants, which will be a key driver of future growth" [VERIFIED: about page; A-Q3-26]. Pricing: "we charge a fixed processing fee + a fee determined by the payment method"; "our Interchange++ pricing passes these fees directly to you"; an example row on the page reads "$0.13 + 0.80% + Interchange++" [VERIFIED: https://www.adyen.com/pricing, n.d., accessed 2026-11] ⚠. "Adyen adopts a transparent pricing model and charges fees to merchants based on its own incurred costs plus a mark-up" [VERIFIED: A-AR25]. "Adyen's tiered pricing structure incentivizes our customers to bring more volume to our platform" [VERIFIED: A-Q3-26]. On price competition: "where such pricing dynamics become unsustainable, Adyen will not pursue a deal" [VERIFIED: A-AR25].
- Stripe: started with start-ups, "enterprise user base has compounded since 2019" [VERIFIED: 1.5]. Pricing page: a published standard rate per successful card charge, and "Design a custom package – available for businesses with large payments volume or unique business models", with "IC+ pricing" listed among custom options [VERIFIED: https://stripe.com/pricing, n.d., accessed 2026-11] ⚠. The numeric rates did not survive text extraction in this session; take them from the `stripe-api` brief or the live page.
- [ASSUMPTION/JUDGEMENT] Blended pricing suits a self-service customer who wants one number; interchange-plus suits a finance team that audits cost. Each company now offers the other's model to the customers who ask, so pricing no longer separates them at enterprise scale; the default does.

### 3.6 Hosting and infrastructure

- Adyen: "The majority of our CapEx is related to our data centers, where we add capacity as we scale" [VERIFIED: A-AR25]. "We are proactively pulling investment from 2027 into H2 2026 to secure compute and storage availability, and lock in pricing amid ongoing supply chain challenges" [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13]. In Japan it "began testing data center operations in major cities" [VERIFIED: A-AR25]. The report also refers to "our data center partners" and "the providers of our data centers", which indicates leased colocation space with Adyen-owned equipment [VERIFIED wording: A-AR25; the interpretation is ASSUMPTION/JUDGEMENT].
- Stripe: "We couldn't run without AWS—and we wouldn't want to" [VERIFIED: amazon-and-stripe, 2023-01-23] **(evidence age: 3.8 years)**.
- [ASSUMPTION/JUDGEMENT] The same choice as the licence, one layer down: Adyen owns the constraint and pays capex (5–7% of net revenue); Stripe rents it and gains speed. Neither has published a cost comparison.

### 3.7 Hiring and engineering culture

- Adyen: 42% of 2025 net joiners in tech roles; the Formula as operating guide; "a relatively flat structure and governance model built around direct co-creation" [VERIFIED: A-AR25]. The 2023 over-hiring and reset are documented in its own results [VERIFIED: 2.1].
- Stripe: "Users First" as first operating principle; "We overhired for the world we're in" (Patrick Collison, November 2022) [VERIFIED: S-L22; CEO email 2022-11-03] **(evidence age: 4 years)**.
- [ASSUMPTION/JUDGEMENT] Both over-hired in 2021–23 and said so in public; the difference is that Adyen's correction is visible in audited margins and Stripe's only in one email.

### Summary table

| Bet | Stripe (documented) | Adyen (documented) | Not public | Analyst's reading [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- | --- |
| Licence | Partner banks; regulated non-bank entities; limited Georgia charter (2025) | Bank in EU, US, UK since 2017/2021/2023 | Stripe's reasons; Stripe's sponsor banks | Converging on own acquiring, not on deposit-taking |
| Build or buy | Ten-plus acquisitions | First two in 2026 | Integration depth of each | Difference of degree after 2026 |
| Packaging | Named products, suite | "One platform", three pillars | Stripe's internal code structure | Slogans overstate the gap |
| First customers | Start-ups, then enterprise | Enterprise, then platforms' small businesses | Revenue mix at Stripe | Each is now moving into the other's base |
| Default pricing | Published blended rate; custom and IC+ on request | Interchange++ with tiers | Realised rates | Default differs, ceiling does not |
| Infrastructure | AWS (2023) | Own data-center capacity | Stripe's current footprint; Adyen's sites | Mirrors the licence choice |
| Disclosure | Letters | Audited accounts | — | Shapes what any book can say |

### For readers new to payments

- **Interchange++**: a price built from the issuing bank's fee (interchange), the card network's fee, and the provider's mark-up, each shown separately.
- **Blended pricing**: one percentage plus a fixed fee per transaction, whatever the card costs the provider.
- **Banking licence versus e-money or payment-institution licence**: a bank may hold deposits and access central-bank accounts; the lighter licences may move and safeguard customer money but not lend it or hold it as deposits.

### Architecture implications

[ASSUMPTION/JUDGEMENT] Running both providers (as Larkfield does) means reconciling two fee models, two settlement behaviours and two sets of regulated entities; the provider comparison card in the Toolkit should carry licence, default pricing model, hosting dependency and "bought or built" for each product used.

---

## PART 4: Contrast cases (chapter 49)

### 4.1 PayPal and Braintree: a consumer network plus a processor

- "We operate a global, two-sided network at scale that connects consumers and merchants with 439 million active accounts across approximately 200 markets as of December 31, 2025" [VERIFIED: PYPL-10K, published 2026-02-03].
- "In 2025, we processed $1.79 trillion of total payment volume ("TPV"), an increase of 7% compared to 2024, and 25.4 billion payment transactions, a decrease of 4%" [VERIFIED: PYPL-10K].
- Definitions: "TPV is the value of payments, net of payment reversals, successfully completed on our payments platform or enabled by PayPal via a partner payment solution, not including gateway-exclusive transactions." "An active account is an account registered directly with PayPal or a platform access partner that has completed a transaction on our platform, not including gateway-exclusive transactions, within the past 12 months" [VERIFIED: PYPL-10K].
- Net revenues $33,172M (2024: $31,797M), +4%; operating margin 18% [VERIFIED: PYPL-10K].
- **Braintree's margin, in the filing's own words.** "As a result of our stronger focus on profitable growth and ongoing negotiations with merchants, we experienced lower volume and transaction revenue from our Braintree offerings in the first half of 2025." "The decrease in transaction expense rate in 2025 compared to 2024 was primarily attributable to a lower proportion of TPV from Braintree products and services, which generally have higher expense rates than other products and services" [VERIFIED: PYPL-10K].
- Merchants get "online branded checkout solutions, including PayPal and Venmo; online unbranded payments processing" [VERIFIED: PYPL-10K].
- PYUSD: "In August 2023, a third-party issuer with which we have partnered commercially (the "PYUSD Issuer") launched a U.S. dollar-denominated stablecoin named PayPal USD" [VERIFIED: PYPL-10K].
- Fastlane: not mentioned in the FY2025 10-K. Do not cite the filing for it.
- [ASSUMPTION/JUDGEMENT] What it teaches: unbranded processing (what Stripe and Adyen sell) is the low-margin half of PayPal; the wallet with 439 million accounts is the asset. A processor without a consumer network competes on cost and performance; Stripe's Link (250 million users claimed, 2026) is an attempt to grow the other side.

### 4.2 Checkout.com: an enterprise acquirer built later

- 2025: "Returns to full-year EBITDA profitability, processing over $300B in 2025–a 64% increase year-over-year in total processed volume"; "adjusted EBITDA margin exceeding 10%"; "over 1,000 enterprise merchants... 63 merchants now process over $1B annually" [VERIFIED: https://www.checkout.com/newsroom/checkout-com-returns-to-full-year-profitability-and-surpasses-300b-in-volume-as-it-positions-for-the-era-of-agentic-commerce, published 2026-02-24].
- 2026 ⚠: "$750m in annualised net revenue, growing 28% year-over-year on a trailing 12-month basis"; total payment volume "expected to reach $480bn for full-year 2026"; "c.$150m in Adjusted EBITDA"; "2,300 employees worldwide"; "operates across 56 countries with 10 acquiring licenses"; "over 1,700 enterprise merchants" [VERIFIED: https://www.checkout.com/newsroom/checkout-com-reaches-750m-in-annualised-net-revenue-for-2026-and-increases-profitability, dated 29 September (2026)]. The enterprise-merchant count differs between the two releases (1,000 in February, 1,700 in September); the definition is not given.
- Valuation: employee buy-back at "a new $12bn valuation" [VERIFIED: https://www.checkout.com/newsroom/checkout-com-accelerates-towards-full-year-profitability-and-announces-employee-share-buy-back-and-a-new-12bn-valuation, published 2025-09-26].
- **US charter.** "the launch of direct acquiring in the US under its Merchant Acquirer Limited Purpose Bank (MALPB) charter in Georgia... The MALPB will enable direct access to card networks, reduce reliance on third-party intermediaries" [VERIFIED: https://www.checkout.com/newsroom/checkout-com-goes-live-with-us-direct-acquiring-under-malpb-charter, published 2026-09-09].
- Cloud hosting and engineering-blog facts: not verified in this session (see Research limitation and the `scale` brief).
- [ASSUMPTION/JUDGEMENT] What it teaches: Checkout.com is the Adyen proposition (enterprise, own acquiring licences, interchange-plus) started later; the margin gap (above 10% versus 50%) shows what two decades of scale on one platform are worth. Its Georgia charter went live fourteen months after Stripe's was approved.

### 4.3 Block (Square): seller software and hardware first

- "more than 4.5 million sellers used the Square ecosystem to make 5.9 billion individual sales transactions totaling $250 billion of Square GPV" in 2025 [VERIFIED: XYZ-10K, published 2026-02-26]. Total GPV was $259,631M (2024: $240,812M) [VERIFIED: XYZ-10K].
- Definition: "GPV includes Square GPV and Cash App GPV. Square GPV is defined as the total dollar amount of all card and bank payments processed by sellers using Square, net of refunds... GPV does not include transactions related to our BNPL products" [VERIFIED: XYZ-10K].
- Model: "Square's commerce enablement products include our payments, software, and hardware products, which together provide an integrated operating system for local commerce." "Square Hardware is custom-designed." Mid-market sellers are those above "$500,000 in annualized Square Gross Payment Volume" [VERIFIED: XYZ-10K].
- Bank: "On March 1, 2021, Square Financial Services received its deposit insurance from the FDIC and charter approval from the Utah Department of Financial Institutions and became operational." It "operates as a Utah-chartered industrial loan company" and Block must "serve as a source of financial strength to it" [VERIFIED: XYZ-10K].
- [ASSUMPTION/JUDGEMENT] What it teaches: Block's customer is a shopkeeper buying a till, with payments bundled; it reached a bank charter through lending to those sellers, not through acquiring. Square's 2025 volume ($250B) is a fraction of Adyen's in-person volume plus online, but its seller count is three orders of magnitude larger than Adyen's direct customer count.

### 4.4 Global Payments and Worldpay

- "On January 9, 2026, Global Payments Inc.... completed its previously announced acquisition of Worldpay Holdco, LLC... from Fidelity National Information Services, Inc.... and certain affiliates of GTCR LLC" and the divestiture of its Issuer Solutions business to FIS [VERIFIED: Global Payments Form 8-K, https://www.sec.gov/Archives/edgar/data/1123360/000110465926002705/tm262856d1_8k.htm, filed 2026-01-12]. Consideration to GTCR: "approximately $6.2 billion in cash and... 43.3 million shares of Global Payments common stock" [VERIFIED: Global Payments Form 10-K FY2025, https://www.sec.gov/Archives/edgar/data/1123360/000112336026000008/gpn-20251231.htm, filed 2026-02-20].

### Stripe vs Adyen (this part)

| Aspect | Stripe | Adyen | Contrast case |
| --- | --- | --- | --- |
| Consumer network | Link: "over 250 million users" (Apr 2026) | No consumer wallet; Dynamic Identification recognises shoppers without an account (2025–26) | PayPal: 439M active accounts, defined and audited |
| US acquiring charter | Georgia MALPB approved Jul 2025 (secondary) | Federal branch since 2021 | Checkout.com: Georgia MALPB live Sep 2026 |
| Bank for lending | Capital through partners; Parafin pending | Capital under own licence | Block: Utah industrial bank since 2021 |
| In-person | Terminal (developer API) | 878K terminals, own design | Square: custom hardware as the entry product |

### For readers new to payments

- **Branded versus unbranded checkout**: branded shows the provider's button and uses the shopper's account with it (PayPal); unbranded processes the merchant's own card form invisibly (Braintree, Stripe, Adyen).
- **GPV, TPV, processed volume**: each company's own name and rules for "value of payments handled"; check refunds, wallets and gateway-only volume before comparing.
- **Industrial loan company**: a US state-chartered, FDIC-insured bank that a commercial company may own.

### Architecture implications

[ASSUMPTION/JUDGEMENT] None of the three contrast companies changes how a payment works; each changes who owns the customer relationship (shopper, enterprise, shopkeeper), and that decides which data the provider has for risk and authorisation optimisation.

---

## PART 5: What is moving as of November 2026 (chapter 50)

Status labels: **announced** (press release only), **preview** (private or public preview per the vendor's documentation), **limited availability**, **GA** (generally available). Where a vendor does not state a phase, the label says so.

### 5.1 Agentic commerce and delegated payment authority

| Item | Date | Status ⚠ | Evidence |
| --- | --- | --- | --- |
| Visa Intelligent Commerce | 30 Apr 2025 | Announced as an initiative that "opens Visa's payment network to the developers and engineers building the foundational AI agents"; partners named include Anthropic, Microsoft, OpenAI, Stripe. Current phase not verified | [VERIFIED: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21361.html, published 2025-04-30] |
| Mastercard Agent Pay | 2025 | Exists; phase not verified | A Mastercard executive: "With Agent Pay, Mastercard is helping establish a strong foundation for secure, scalable agent-driven transactions" [VERIFIED: https://www.adyen.com/press-and-media/adyen-agentic, published 2026-06-16]; launch date 29 Apr 2025 is [ASSUMPTION/JUDGEMENT] |
| Google Agent Payments Protocol (AP2) | 16 Sep 2025 | Open protocol announced with "more than 60 organizations" including Adyen, American Express, Mastercard, PayPal, Worldpay; addresses "Authorization", "Authenticity", "Accountability" | [VERIFIED: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol, published 2025-09-16] |
| Stripe + OpenAI: Instant Checkout and the Agentic Commerce Protocol (ACP) | 29 Sep 2025 | Live at launch for "ChatGPT users in the United States" buying "from Etsy merchants (and, soon, from Shopify merchants)"; ACP "is open source and community-designed under the Apache 2.0 license" | [VERIFIED: https://stripe.com/newsroom/news/stripe-openai-instant-checkout, published 2025-09-29; https://www.agenticcommerce.dev/, n.d., accessed 2026-11] |
| Stripe Agentic Commerce Suite | 11 Dec 2025 | Launched; "a low-code solution for businesses, letting them sell across AI agents with a single integration"; "also handles Shared Payment Tokens". Docs: "Availability, launch stage, and supported countries vary by integration" | [VERIFIED: https://stripe.com/newsroom/news/agentic-commerce-suite, published 2025-12-11; https://docs.stripe.com/agentic-commerce.md, n.d., accessed 2026-11] |
| Google Universal Commerce Protocol (UCP) | 11 Jan 2026 | Open-source standard, "developed by Google in collaboration with industry leaders including Shopify, Etsy, Wayfair, Target, and Walmart", endorsed by Adyen, Stripe, Visa, Mastercard and others; "compatible with Agent Payments Protocol (AP2)"; "you remain the Merchant of Record" | [VERIFIED: https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/, published 2026-01-11] |
| Machine Payments Protocol (MPP) | 18 Mar 2026 | "an open standard for machine payments co-authored by Stripe and Tempo", released with Tempo mainnet | [VERIFIED: https://tempo.xyz/blog/mainnet, published 2026-03-18] |
| x402 Foundation (Linux Foundation) | 2 Apr 2026 | Adyen "joined the x402 Foundation as a founding member"; x402 is "a standard for embedding payments directly into web interactions" | [VERIFIED: https://www.adyen.com/knowledge-hub/adyen-joins-x402-foundation, published 2026-04-02] |
| Stripe: Link for agents; Google partnership | 29 Apr 2026 | "Starting today, people can enable their agents to make payments with Link... a one-time-use card is issued per task, and you approve each payment". Link Agent Wallet docs: agent payments available to "US and Canadian customers" | [VERIFIED: https://stripe.com/newsroom/news/sessions-2026, published 2026-04-29; https://docs.stripe.com/agentic-commerce/agents/link-agent-wallet.md, n.d., accessed 2026-11] |
| Adyen Agentic | 16 Jun 2026 | **Limited availability**: "At announcement, Adyen Agentic is in limited availability for enterprise merchants operating in the U.S., with plans for global expansion to follow". Three layers: Agentic Feed, Agentic Cart, Agentic Payments | [VERIFIED: https://www.adyen.com/press-and-media/adyen-agentic, published 2026-06-16] |
| Adyen: Personal Agent Protocol with Sierra and Meta | Q3 2026 | Announced partnership "to help shape the emerging standard for AI agents to interact with businesses" | [VERIFIED: A-Q3-26, published 2026-10-28] |
| Stripe Treasury for agents | 21 Oct 2026 | Announced and usable for reading balances, paying invoices, transfers and currency conversion; "Businesses will soon be able to use agents for more tasks, including creating cards. They'll also be able to set spending limits for their agents in the coming weeks". No release phase stated | [VERIFIED: https://stripe.com/newsroom/news/treasury-for-agents, published 2026-10-21] |

Statements of position:

- Stripe: "in the not-too-distant future agents will account for most transactions online" (Patrick Collison); "If AI can solve Nobel level physics problems but can't buy a domain, something's gone wrong. Our mantra: empower agents" (Will Gaybrick) [VERIFIED: sessions-2026, 2026-04-29]. "Agentic commerce has moved into a phase of building and real-world experimentation" [VERIFIED: stripe-2025-update, 2026-02-24].
- Adyen: "While this evolution is unfolding gradually and we are starting to see the first transactions, we see it as a meaningful next phase" [VERIFIED: https://investors.adyen.com/financials/2025, n.d., accessed 2026-11]. "We believe the future of agentic commerce should be open, so we intentionally designed Adyen Agentic to help retailers integrate once... without having to bet on which ecosystems ultimately win" [VERIFIED: adyen-agentic, 2026-06-16]. "Other protocols that we support - including ACP and UCP - have primarily focused on consumer-direct transactions... x402 addresses a different layer: machine-to-machine transactions" [VERIFIED: x402 article, 2026-04-02]. Adyen's documentation lists integrations for ACP and UCP and for "payments initiated by Google AI Mode or Gemini" [VERIFIED: https://docs.adyen.com/online-payments/agentic-commerce/merchant, n.d., accessed 2026-11].
- Treasury for agents, on control: "Startups using Stripe Treasury for agents choose which accounts and data agents can access, whether they can read information or take action, and when money movement requires human approval" [VERIFIED: treasury-for-agents, 2026-10-21].

[ASSUMPTION/JUDGEMENT] Stripe co-authored two protocols (ACP, MPP) and sells a suite on top; Adyen authored none, joined the foundations, and sells a translator across them. That is the company-level bet repeated: Stripe defines an interface and gets developers onto it; Adyen stays neutral for enterprises that will not pick a side. No volume figure for agent-initiated payments has been published by either.

### 5.2 Stablecoins

- **Stripe.** Bridge completed 4 Feb 2025; "Bridge... saw volume more than quadruple" in 2025; "stablecoin payments volume doubled to around $400 billion, 60% of which is estimated to represent B2B payments" (an industry estimate cited by Stripe, not Stripe's own volume) [VERIFIED: S-L25]. Shopify merchants "across 34 countries will be able to accept USDC" through Stripe [VERIFIED: https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments, published 2025-06-12]. Financial accounts "can hold a stablecoin balance in OUSD or USDC"; "In the United States, stablecoin balances are in public preview"; "Outside the United States, stablecoin balances are in private preview" [VERIFIED: https://docs.stripe.com/financial-accounts/stablecoins.md, n.d., accessed 2026-11] ⚠ **preview**. "streaming payments... combines precise tracking from Metronome with stablecoin micropayments on the Tempo blockchain" [VERIFIED: sessions-2026] — announced; phase not stated.
- **Tempo.** Unveiled September 2025, "incubated together with Paradigm"; design goals "dedicated payment lanes, sub-second finality, opt-in privacy"; reason given: "Last year, a memecoin trading frenzy on one of the major blockchains delayed payouts for one Bridge user by over 12 hours and spiked per-transaction prices 35×" [VERIFIED: S-L25]. **Mainnet live 18 March 2026**: "Starting today, you can build on Tempo through our public RPC endpoints" [VERIFIED: https://tempo.xyz/blog/mainnet, published 2026-03-18]. Tempo's separate $500M funding at a $5B valuation is [WIDELY REPORTED: crypto trade press via search summary, 2025–26].
- **Adyen.** One line in a results release: "shaping stablecoin infrastructure via OpenUSD for global merchants", alongside joining the x402 Foundation [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13]. The H1 2026 shareholder letter and the Q3 2026 update do not contain the word "stablecoin" (full-text check). No Adyen stablecoin acceptance or settlement product page was found. Adyen "joined the European Central Bank's digital euro pilot as an acquiring payment service provider" [VERIFIED: A-Q3-26].
- **US law.** The GENIUS Act is Public Law 119-27, "Approved July 18, 2025". Section 20: it takes effect "on the earlier of (1) the date that is 18 months after the date of enactment of this Act; or (2) the date that is 120 days after the date on which the primary Federal payment stablecoin regulators issue any final regulations" [VERIFIED: https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm, published 2025-07-18]. The OCC issued its final implementing rule on 21 October 2026 and states: "The GENIUS Act's effective date is January 18, 2027"; rules on anti-money-laundering and sanctions "will be addressed in a separate rulemaking" [VERIFIED: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html, published 2026-10-21] ⚠.
- **EU law.** MiCA "entered into force in June 2023"; a grandfathering clause lets providers operating under national law before 30 December 2024 "continue to do so until 1 July 2026 or until they are granted or refused a MiCA authorisation" [VERIFIED: https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica, n.d., accessed 2026-11]. [ASSUMPTION/JUDGEMENT] The stablecoin titles applied from 30 June 2024 and the rest from 30 December 2024; that transitional window has now closed.

[ASSUMPTION/JUDGEMENT] On stablecoins the two companies differ more than on anything else in 2026: Stripe owns an orchestration company, a wallet company, and helped start a blockchain; Adyen, a bank with central-bank access, has published one clause. A bank's cheapest settlement asset is central-bank money, which may be the reason, but Adyen has not said so.

### 5.3 Instant and account-to-account payments

- **FedNow** (Federal Reserve's own statistics): 2024: 1,505,250 settled payments, $38.2B; 2025: 8,413,402 payments, $853.4B, average value $101,435. 2026 Q3: 6,376,467 payments, $370.9B, average value $58,161, average daily volume 69,309 [VERIFIED: https://www.frbservices.org/resources/financial-services/fednow/volume-value-stats, updated 2026, accessed 2026-11]. The high average value shows business and treasury use, not retail checkout [ASSUMPTION/JUDGEMENT].
- **Wero** (European Payments Initiative): "live for P2P payments in Belgium, France, and Germany since 2024, currently serving 56 million users. For retail payments, Wero is live in Germany since the end of 2025 with progressive roll-out in France and Belgium throughout 2026. Major migrations of at least 15 million consumers are also planned for Payconiq in Luxembourg (by 2026) and iDEAL in the Netherlands (by 2027)" [VERIFIED: https://epicompany.eu/key-figures/, n.d., accessed 2026-11] ⚠. A start of the Dutch e-commerce rollout on 26 October 2026 is reported by one trade article only [WIDELY REPORTED: trade press, https://thepaypers.com/payments/news/epi-starts-wero-ecommerce-roll-out-with-dutch-banks, 2026]. This matters to Larkfield (Rotterdam, iDEAL).
- **Pix and UPI**, 2025 calendar year: Pix 79.7 billion transactions (+26%), BRL 35.3 trillion; UPI 228.3 billion transactions (+33%), INR 299.7 trillion [WIDELY REPORTED: payments research firm, https://www.fxcintel.com/research/analysis/upi-pix-2025-growth, 2026]. Not verified against Banco Central do Brasil or NPCI tables.
- **Pay-by-bank products.** Stripe: "Pay by Bank is a single-use payment method that allows customers to pay directly from their bank account instead of using a card", for "customers in the UK and Europe", "available by default for payments between 0.50 GBP and 10,000 GBP" [VERIFIED: https://docs.stripe.com/payments/pay-by-bank.md, n.d., accessed 2026-11]. Adyen: open banking on its platform since 4 October 2022 through Tink [VERIFIED: 2.1]; Pix Recurring added in Brazil in 2025; "earliest adopters of the US FedNow service" [VERIFIED: A-AR25; https://www.adyen.com/about]. Adyen's current pay-by-bank documentation page returned no content in this session.
- [ASSUMPTION/JUDGEMENT] Card economics (chapter 05): an account-to-account payment has no interchange, so a provider priced as mark-up over cost earns its mark-up either way, while a provider on a blended rate loses the spread between its price and a card's cost. This is inference; neither company has published the effect.

### 5.4 PSD3 and the Payment Services Regulation ⚠

- The Council published the final compromise texts of PSD3 and the PSR on 23 April 2026; "formal adoption by the Council and Parliament, signing and publication in the Official Journal are yet to occur" [WIDELY REPORTED: law-firm briefing, https://www.matheson.com/insights/psd3-and-psr-published-whats-changing-for-eu-payment-services/, 2026-04-29].
- As of 15 September 2026: "PSD3 and the PSR are expected to be published in the Official Journal at the end of Q4 2026"; "the core provisions in PSD3 taking effect after a 21-month implementation period"; full application "will likely extend well into 2028 and beyond" [WIDELY REPORTED: law-firm briefing, https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/financial-regulation/financial-regulation-in-the-know-payments-september-2026/psd3-new-era-eu-payment-services-regulation/, 2026-09-15].
- Status on 17 November 2026: **agreed, not confirmed as published**. Other secondary sources give application periods of 18 or 21 months; they disagree, and the Official Journal text decides. Check EUR-Lex before printing any date.

### 5.5 Consolidation

| Date | Deal | Status |
| --- | --- | --- |
| 9 Jan 2026 | Global Payments acquires Worldpay; sells Issuer Solutions to FIS | Completed [VERIFIED: 4.4] |
| 14 Jan 2026 | Stripe – Metronome (usage billing) | Completed [VERIFIED: 1.2] |
| 1 Jul 2026 | Adyen – Talon.One (loyalty) and Orb (usage billing) | Completed [VERIFIED: 2.4] |
| 19 Aug 2026 | Stripe – OpenRouter (AI model routing) | Agreement announced [VERIFIED: 1.2] |
| 30 Sep 2026 | Stripe – Parafin (embedded credit) | Agreement announced [VERIFIED: 1.2] |
| by 31 Mar 2027 | Lemon Squeezy shuts down after acquisition by Stripe | Announced on its site [VERIFIED: 1.2] |

[ASSUMPTION/JUDGEMENT] The pattern: payment providers are buying the systems on either side of the transaction (billing before it, loyalty around it, credit and treasury after it). Independent billing and loyalty vendors that integrate with several providers are the ones being absorbed; Orb's promise to keep supporting other providers "during the first phase" is the thing for a customer to watch.

### Stripe vs Adyen (this part)

| Topic | Stripe | Adyen | Difference supported |
| --- | --- | --- | --- |
| Agent protocols | Co-author of ACP (with OpenAI) and MPP (with Tempo); partner in UCP, Visa Intelligent Commerce | Supports ACP, UCP, AP2; founding member of x402 Foundation; Personal Agent Protocol with Sierra and Meta | Author versus neutral implementer |
| Agent product status | Suite launched Dec 2025; Link agent payments for US and Canadian customers; Treasury for agents Oct 2026 | Limited availability, US enterprise merchants, Jun 2026 | Stripe earlier and broader |
| Stablecoins | Bridge, Privy, Tempo, stablecoin balances (preview), USDC acceptance | One clause on OpenUSD; digital euro pilot | Largest documented gap |
| Pay-by-bank | Own-branded method in UK and Europe | Through Tink since 2022; local schemes directly | Nothing public on volumes at either |
| PSD3/PSR | Nothing public found (newsroom, letters) | Nothing specific found (annual report mentions regulation generally) | No documented difference |

### For readers new to payments

- **Agentic commerce**: software agents acting for a person find, choose and pay for goods; the open question is how a merchant and a bank know the person authorised it.
- **Shared payment token**: a credential an agent passes to a merchant that is limited to one purchase and hides the underlying card.
- **Stablecoin**: a blockchain token redeemable one-for-one for a currency such as the US dollar, backed by reserves.
- **Instant payment**: an account-to-account transfer that settles in seconds, at any hour, and cannot be recalled by the sender.

### Architecture implications

[ASSUMPTION/JUDGEMENT] What to build now: catalogue and checkout that can be called by a machine (structured product data, an idempotent order-creation endpoint, merchant-of-record logic kept on your side), because every protocol above assumes them. What not to build yet: anything tied to one agent protocol, one stablecoin chain, or PSR dates. Keep stablecoin balances behind the same ledger abstractions as fiat balances so a preview product can be switched off.

---

## Key numbers

| Number | Value | Exact definition | Source, date |
| --- | --- | --- | --- |
| Stripe total volume 2025 | $1.9 trillion (+34%) | "total volume" generated by "businesses running on Stripe"; undefined; not revenue | S-L25, 2026-02-24 |
| Stripe total payment volume 2024 / 2023 / 2022 | $1.4T (+38%) / $1T (+25%) / $817B (+26%) | as worded in each letter; undefined | S-L24, S-L23, S-L22 |
| Stripe businesses | "more than 5 million businesses directly or via platforms" | includes businesses reached through Connect platforms | S-L25 |
| Stripe platforms | "More than 18,000" | undefined | Parafin release, 2026-09-30 |
| Stripe Revenue suite | "on track to hit an annual run rate of $1 billion this year" (2026); passed $500M run rate by Feb 2025 | run rate, Billing, Invoicing, Tax "and more" | S-L25; S-L24 |
| Stripe Billing | "more than 300,000 companies... nearly 200 million active subscriptions" | — | S-L24, 2025-02-27 |
| Link users | "over 250 million users globally" | undefined (accounts, not active users) | Sessions 2026, 2026-04-29 |
| Stripe tender-offer valuation | $159B | price of employee share purchase | 2026-02-24 |
| Stripe headcount | "almost 7,000" | company email, Nov 2022; no later figure | 2022-11-03 **(4 years old)** |
| Adyen processed volume 2025 | €1,394.3B (+8%; +21% ex one customer) | value processed on platform; 84% full-stack | A-AR25 |
| Adyen net revenue 2025 | €2,364.2M (+18%; +21% cc) | non-IFRS: revenue less pass-through costs and cost of goods, plus net interest income | A-AR25 |
| Adyen EBITDA margin 2025 / 2024 / 2023 | 53% / 50% / 46% | EBITDA ÷ net revenue | A-AR25; 2024-02-08 |
| Adyen take rate 2025 / H1 2026 | 17.0 bps / 16.2 bps | net revenue ÷ processed volume | A-AR25; A-H1-26 |
| Adyen point-of-sale volume 2025 | €310.9B, 22% of volume | in-person volume | A-AR25 |
| Adyen H1 2026 | volume €803.8B; net revenue €1,302.9M; EBITDA margin 49% | half year to 30 June 2026, unaudited | A-H1-26, 2026-08-13 |
| Adyen Q3 2026 | volume €451.1B (+30%); net revenue €738.1M (+23%) | quarter to 30 Sep 2026, unaudited, includes acquisitions | A-Q3-26, 2026-10-28 |
| Adyen FTE | 4,771 (Dec 2025); 5,020 (Jun 2026); 5,596 (Sep 2026) | full-time equivalents | A-AR25; A-H1-26; A-Q3-26 |
| Adyen top-10 merchants | 11% of revenue (2024: 12%) | "as measured by revenue" | A-AR25 |
| Adyen transacting terminals | 878K (+25%) | terminals with transactions in the period | A-Q3-26 |
| Talon.One / Orb price | €750M / $335M | total consideration | 2026-04-23; 2026-06-11 |
| PayPal TPV 2025 | $1.79T (+7%) | net of reversals; excludes gateway-exclusive transactions | PYPL-10K, 2026-02-03 |
| PayPal active accounts | 439 million | transacted within past 12 months | PYPL-10K |
| Checkout.com volume | over $300B in 2025 (+64%); $480B expected 2026 | "total processed volume" / "total payment volume", company-reported, private | 2026-02-24; 2026-09-29 |
| Square GPV 2025 | $250B | card and bank payments by Square sellers, net of refunds | XYZ-10K, 2026-02-26 |
| FedNow 2025 | 8.41M payments, $853.4B | settled payments | Federal Reserve, 2026 |
| Wero users | 56 million | EPI's own count | epicompany.eu, accessed 2026-11 |

---

## Open questions / not verifiable

These become the book's "where the evidence stops" statements.

1. **Stripe's revenue, margin and headcount.** Never published. "Profitable" has no stated measure. Any revenue figure in print comes from press reports of investor material, not from Stripe.
2. **What Stripe's volume counts.** Whether "total volume" includes stablecoin flows through Bridge, Treasury transfers between businesses, or payouts is not stated; the wording changed in the 2025 letter.
3. **Stripe's acquiring banks and direct network memberships** by country, and whether the Georgia charter is in use. Not public in anything fetched.
4. **Stripe's legal entities and licence types in Europe and the UK** beyond the footer statement about the Irish entity.
5. **Whether OpenRouter and Parafin have closed.** Announced 19 August and 30 September 2026; no completion release found on 17 November 2026.
6. **Adyen's 2023 Investor Day targets and the August 2023 share-price fall**: recalled, not fetched.
7. **Whether Adyen's management has said in so many words that it departed from building everything.** No such sentence in the releases, letter or update read; earnings-call audio was not transcribed.
8. **How far Orb and Talon.One are integrated** into the single platform, and when "convergence" happens. Adyen gives intent, no date.
9. **The identity of Adyen's "single large-volume customer"** and the exact definition of processed volume.
10. **Adyen's data-center locations and ownership model** (owned buildings versus colocation). The report refers to data-center "partners" and "providers".
11. **Adyen's position on stablecoin acceptance or settlement** beyond one clause in a press release.
12. **Agent-initiated payment volumes** at either company; none published.
13. **Release phases** of Visa Intelligent Commerce, Mastercard Agent Pay, Stripe streaming payments and Treasury for agents as of November 2026.
14. **PSD3/PSR Official Journal publication** and the final application periods.
15. **Pix and UPI figures from the official statistics**; the Dutch iDEAL-to-Wero start date from EPI or Currence.
16. **Checkout.com's hosting** and its definition of "enterprise merchant" (1,000 in February 2026, 1,700 in September 2026).
17. **PayPal Fastlane** adoption; absent from the FY2025 10-K.
18. **Stripe product dates** for Radar (2016), Treasury (2020), Link, and the Okay acquisition.

---

## Source list

**Stripe**

- Stripe annual letter 2022 (S-L22), Patrick and John Collison, published 2023-04-05, https://assets.stripeassets.com/fzn2n1nzq965/5Qj1NdQFtWO3rIE4WhAVl9/21202f8455f5a877444f91c1b48baf6e/stripe-2022-update.pdf — volume, mission, enterprise shift, reliability.
- Stripe annual letter 2023 (S-L23), published 2024-03-13, https://assets.stripeassets.com/fzn2n1nzq965/1gMd12owbzJaSe4Y560OEJ/0e7a27759e1b3070c5179ded5b94f525/Stripe_2023_annual_letter_enGB.pdf — $1T, cash-flow statement, deployment practice.
- Stripe annual letter 2024 (S-L24), published 2025-02-27, https://assets.stripeassets.com/fzn2n1nzq965/2pt3yIHthraqR1KwXgr98U/cbec59afdec826fb322271a56626aa9a/Stripe-annual-letter-2024-en-gb.pdf — $1.4T, profitability, Billing figures, Bridge.
- Stripe annual letter 2025 (S-L25), published 2026-02-24, https://assets.stripeassets.com/fzn2n1nzq965/3LlGw839Q6kUwxZlLZDtH6/75ddcbada4aa7743dd8ec7d0f9ca497e/Stripe-annual-letter-2025-desktop.pdf — $1.9T, 5 million businesses, Tempo, stablecoins. Index of letters: https://stripe.com/annual-updates/2025.
- Stripe newsroom, https://stripe.com/newsroom/news/ plus slug: `stripe-2025-update` (2026-02-24, $159B tender, letter summary); `stripe-2024-update` (2025-02-27); `employee-liquidity-feb-2025` (2025-02-27, $91.5B); `employee-liquidity-feb-2024` (2024-02-28, $65B); `stripe-series-i-employee-liquidity` (2023-03-15, $50B); `stripe-series-h` (2021-03-14, $95B); `ceo-patrick-collisons-email-to-stripe-employees` (2022-11-03, layoff and headcount); `amazon-and-stripe` (2023-01-23, AWS); `stripe-agrees-to-acquire-openrouter` (2026-08-19); `openrouter-and-stripe` (2026-01-29); `stripe-agrees-to-acquire-parafin` (2026-09-30); `stripe-completes-metronome-acquisition` (2026-01-14); `stripe-completes-bridge-acquisition` (2025-02-04); `paystack-joining-stripe` (2020-10-15); `taxjar` (2021-04-27); `bouncer` (2021-05-14); `recko` (2021-10-20); `stripe-launches-atlas` (2016-02-24); `stripe-launches-billing` (2018-04-05); `stripe-radar-2` (2018-04-18); `stripe-launches-issuing` (2018-07-26); `stripe-launches-terminal` (2018-09-17); `stripe-capital` (2019-09-05); `stripe-launches-stripe-tax` (2021-06-10); `stripe-launches-identity` (2021-07-14); `revenue-recognition` (2021-09-21); `financial-connections` (2022-05-04); `stripe-openai-instant-checkout` (2025-09-29); `agentic-commerce-suite` (2025-12-11); `sessions-2026` (2026-04-29); `treasury-for-agents` (2026-10-21); `shopify-stripe-stablecoin-payments` (2025-06-12); `aws-stripe-agentcore-privy` (2026-05-07).
- "The new Connect", Stripe blog, 2015-03-23, https://stripe.com/blog/the-new-connect — Connect launched October 2012.
- Stripe Payments Company licences and disclosures, n.d., https://stripe.com/legal/spc/licenses — US state money-transmission regulators.
- Stripe Services Agreement, n.d., https://stripe.com/legal/ssa — checked for bank names (none).
- Stripe pricing, n.d., https://stripe.com/pricing — custom packages, IC+.
- Stripe docs, n.d.: https://docs.stripe.com/agentic-commerce.md; https://docs.stripe.com/agentic-commerce/agents/link-agent-wallet.md; https://docs.stripe.com/financial-accounts/stablecoins.md; https://docs.stripe.com/payments/pay-by-bank.md; https://docs.stripe.com/treasury.md.
- Lemon Squeezy, "Stripe acquires Lemon Squeezy", 2024-07-26, https://www.lemonsqueezy.com/blog/stripe-acquires-lemon-squeezy — acquisition and shutdown banner.
- Tempo, mainnet announcement, 2026-03-18, https://tempo.xyz/blog/mainnet — mainnet, Machine Payments Protocol.
- ICBA, "Georgia approves Stripe application to form MALPB", 2025-07-08, https://www.icba.org/newsroom/news-and-articles/2025/07/08/georgia-approves-stripe-application-to-form-malpb — secondary, charter.

**Adyen**

- Annual Report 2025 (A-AR25), Adyen N.V., February 2026, download from https://investors.adyen.com/financials/2025 — strategy statements, figures, notes, risk section.
- H2 2025 Shareholder Letter (A-H2-25), February 2026, https://investors.adyen.com/financials/h2-2025-4r9rc — single large-volume customer, eBay.
- H1 2026 Shareholder Letter and interim statements (A-H1-26), 2026-08-13, https://investors.adyen.com/financials/h1-2026-c2a1a — figures, three layers, acquisitions note 17, FTE by office.
- Q3 2026 Business Update (A-Q3-26), 2026-10-28, https://media.ffycdn.net/eu/adyen/dfb86zC9WHUzrC5zRj2Y.pdf (page: https://investors.adyen.com/financials/q3-2026-10c88s) — figures, guidance change, FTE.
- Adyen press releases, https://www.adyen.com/press-and-media/ plus slug: `adyen-publishes-q3-2026-business-update-6r9vz0` (2026-10-28); `adyen-publishes-h1-2026-financial-results-3wjne` (2026-08-13); `adyen-publishes-q1-2026-business-update-4gyhh5` (2026-05); `adyen-publishes-h2-2024-financial-results` (2025-02-13); `adyen-publishes-h2-2023-financial-results` (2024-02-08); `adyen-publishes-h1-2023-financial-results` (2023-08-17); `adyen-publishes-q3-business-update` (2023-11-08); `adyen-hosts-investor-day-2025-in-amsterdam` (2025-11-11); `2i4hnm0pfcpvc7` (Talon.One, 2026-04-23); `jtrg4qd7j3p4rj` (Orb, 2026-06-11); `adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates` (2026-07-01); `adyen-agentic` (2026-06-16); `adyen-launches-intelligent-money-movement` (2026-04-09); `adyen-granted-uk-banking-authorization` (2023-09-07); `adyen-granted-us-branch-license` (2021-06-14); `adyen-ipo-priced-at-240-per-share` (2018-06-11); `adyen-expands-beyond-payments-announces-embedded-financial-products` (2022-03-31); `adyen-launches-next-generation-open-banking-solution-in-partnership-with-tink` (2022-10-04).
- Investor Day 2025 FAQ (PDF), 2025-11-11, from https://investors.adyen.com/events/investor-day-2025 — guidance framework.
- About Adyen, n.d., https://www.adyen.com/about — founding, timeline, Formula, enterprise positioning.
- Adyen pricing, n.d., https://www.adyen.com/pricing — Interchange++.
- "Why billing and payments belong together", Blake Breathitt, n.d. (2026), https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb; "Why loyalty belongs at the moment of payment", Hemmo Bosscher, n.d. (2026), https://www.adyen.com/knowledge-hub/why-adyen-acquired-talon-one — rationale.
- "Adyen joins x402 Foundation", 2026-04-02, https://www.adyen.com/knowledge-hub/adyen-joins-x402-foundation — protocol stance.
- Adyen docs, agentic commerce for merchants, n.d., https://docs.adyen.com/online-payments/agentic-commerce/merchant.
- fintech.global, "Adyen acquires Talon.One for €750m", 2026-04-24, https://fintech.global/2026/04/24/adyen-acquires-talon-one-for-e750m/ — secondary, "first acquisition" framing.

**Contrast cases**

- PayPal Holdings, Form 10-K FY2025, filed 2026-02-03, https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm — TPV, active accounts, Braintree, PYUSD.
- Block, Inc., Form 10-K FY2025, filed 2026-02-26, https://www.sec.gov/Archives/edgar/data/1512673/000162828026012254/xyz-20251231.htm — Square GPV, hardware, Square Financial Services.
- Global Payments Inc., Form 8-K, filed 2026-01-12, https://www.sec.gov/Archives/edgar/data/1123360/000110465926002705/tm262856d1_8k.htm; Form 10-K FY2025, filed 2026-02-20, https://www.sec.gov/Archives/edgar/data/1123360/000112336026000008/gpn-20251231.htm — Worldpay completion and consideration.
- Checkout.com newsroom, https://www.checkout.com/newsroom/ plus slug: `checkout-com-returns-to-full-year-profitability-and-surpasses-300b-in-volume-as-it-positions-for-the-era-of-agentic-commerce` (2026-02-24); `checkout-com-reaches-750m-in-annualised-net-revenue-for-2026-and-increases-profitability` (2026-09-29); `checkout-com-goes-live-with-us-direct-acquiring-under-malpb-charter` (2026-09-09); `checkout-com-accelerates-towards-full-year-profitability-and-announces-employee-share-buy-back-and-a-new-12bn-valuation` (2025-09-26).

**What is moving**

- Visa, "Find and Buy with AI: Visa Unveils New Era of Commerce", 2025-04-30, https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21361.html.
- Google Cloud, "Announcing Agent Payments Protocol (AP2)", 2025-09-16, https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol.
- Google Developers Blog, "Under the Hood: Universal Commerce Protocol (UCP)", 2026-01-11, https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/.
- Agentic Commerce Protocol site, n.d., https://www.agenticcommerce.dev/.
- GENIUS Act, Public Law 119-27, 2025-07-18, https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm — effective-date section.
- OCC Bulletin 2026-50, 2026-10-21, https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html — final rule, effective date 18 January 2027.
- ESMA, Markets in Crypto-Assets Regulation page, n.d., https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica.
- Federal Reserve Financial Services, FedNow Service Volume and Value Statistics, updated 2026, https://www.frbservices.org/resources/financial-services/fednow/volume-value-stats.
- European Payments Initiative, key figures, n.d., https://epicompany.eu/key-figures/.
- FXC Intelligence, "UPI and Pix 2025 growth", 2026-04-10, https://www.fxcintel.com/research/analysis/upi-pix-2025-growth — secondary.
- Matheson, "PSD3 and PSR published: what's changing", 2026-04-29, https://www.matheson.com/insights/psd3-and-psr-published-whats-changing-for-eu-payment-services/ — secondary.
- Addleshaw Goddard, "PSD3: a new era", 2026-09-15, https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/financial-regulation/financial-regulation-in-the-know-payments-september-2026/psd3-new-era-eu-payment-services-regulation/ — secondary, latest status found.
- The Paypers, "EPI starts Wero ecommerce roll-out with Dutch banks", 2026, https://thepaypers.com/payments/news/epi-starts-wero-ecommerce-roll-out-with-dutch-banks — secondary, search summary only.
