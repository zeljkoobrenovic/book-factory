---
title: "Case: Adyen, the Single Platform With a Banking Licence"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What does Adyen's public record show about building payments as one platform under its own banking license? A company that built the regulated layers itself, in order, reports the result in audited figures and marks the platform's edges itself; since July 2026 the phrase “single platform” describes its payments and banking core, not the whole company."
permalink: case-adyen
timetoread: 26 min read
---

> **IN THIS CHAPTER, YOU WILL:** Read Adyen's dated record, see where its single platform starts and stops, and separate the practices you can adopt from the assets you cannot copy.

> **KEY POINTS:**
>
> * **Adyen built the regulated layers itself, in order.** An acquiring license and enterprise merchants came first, then a banking license in 2017, extended to the United States in 2021 and the United Kingdom in 2023. All of it runs on one platform, on infrastructure Adyen manages itself, and is reported in audited figures.
> * **Adyen itself marks where the platform stops.** In 2025, 84% of its volume was full-stack, and its risk section places concentration risk at banking partners where it has no acquiring license of its own. On 1 July 2026 it closed the purchases of Talon.One (loyalty) and Orb (usage billing), and it runs Orb under "an incubator model".
> * **The practices transfer; the assets do not.** A builder can adopt one accounting core checked when entries are written and one place for every change. The licenses, the data centers and 878,000 transacting terminals took two decades to assemble.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Borrowed Blueprint** — "one platform, built in-house" is copied as a design by teams with neither the licenses nor the twenty years behind it.
> * **The Single Rail** — Adyen's own risk section says its largest customers spread volume over several providers.
> * **The Accidental Bank** — Adyen pays sellers before the money has arrived on a bank's balance sheet; a platform that imitates this takes the risk without the permission.

<br>
[[case-stripe]] showed a company that made the interface its first product and assembled the regulated layer afterward. Adyen built in the other order, and that makes one sentence tempting. In November 2026 an architect at a retailer says: "Adyen builds everything itself on one platform, so whatever we buy from them is one integration with one set of reports." Seven months earlier Adyen had said nearly the same. Its press release of 9 April 2026 read: "Unlike many providers that rely on a patchwork of acquired technologies and third-party integrations, Adyen has built its entire financial technology stack on a single platform." On 1 July 2026 Adyen closed the purchase of two software companies.

So what does the record support? **Adyen chose to operate the regulated layers itself for enterprise customers**: one platform, its own acquiring and banking licenses, its own data-center capacity, and audited figures that show the result. Adyen also discloses where that platform stops. And since 1 July 2026 **"single platform" describes its payments and banking core, not the whole company**. What a builder can take from the record is practice (one accounting core, one place for every change), not the licenses, the data centers or the terminal estate.

**Where we are in the payment's journey.** When Mila Janssen bought her €120.00 ten-class pass from Studio Noord on 9 March 2027, the payment ran through Adyen. At Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]), Adyen carried 56% of member payment volume in 2026 (€627 million) and every front-desk terminal.

The chapter says how the case is read, then gives the history from an acquiring license to three banking permissions, quotes the single-platform bet in Adyen's own words, and follows the bet through the licenses, the terminal estate, and the platform and financial products. Then come the acquisitions of July 2026, the figures with their definitions, and the engineering record with its age. It ends with what transfers to a builder and a list of where the evidence stops.

## How to Read This Case

Every statement about Adyen here is one of three kinds: **documented** (Adyen's own dated document), **widely reported** (a secondary source, named as such) or an **inference**, which appears only in blocks marked INFERENCE, NOT DOCUMENTED. The research cut-off is **17 November 2026**. The Annual Report 2025, signed on 5 March 2026, is audited. The shareholder letters and the business update for the third quarter of 2026 are unaudited. License, pricing and documentation pages are undated and are cited as "n.d., accessed November 2026". Engineering posts are the thinnest layer: those that describe architecture date from 2018 to 2021.

Four things could not be reached or confirmed. The annual report was read in the PDF on Adyen's investor site, a "printed version" which states that the official filing is the electronic reporting package. Adyen's earnings calls of 2026 were not transcribed, so management's words come from releases, the shareholder letter and Adyen's articles. The status page builds its incident history in the browser and was not read, so nothing here says Adyen had no incident of a given kind. And no Adyen document read calls the 2026 deals its first acquisitions; its history page (n.d., accessed November 2026) lists none before them.

## From an Acquiring License to Three Banking Permissions: 2006 to 2023

Adyen was founded in Amsterdam in 2006. An **acquirer** is the licensed institution that contracts with a merchant, submits its card payments to the card networks and receives the money for it ([[acquiring-and-network-connectivity]]). Adyen's history page (n.d., accessed November 2026) puts that permission in its first period, 2006 to 2012: "We secured a European acquiring license, added POS and risk tools, and expanded into San Francisco, London, Paris, and Stockholm." POS is point of sale, the card terminal at a counter. The page does not date the license within the period, but it names the customer: "Built for enterprise, not adapted to it."

The second period made Adyen a bank and a listed company. A 2021 release dates its "European banking license" to 2017. The history page places it, with acquiring licenses across Asia-Pacific, in its second period, 2016 to 2020. In June 2018 existing shares were listed on Euronext Amsterdam at €240, "implying a market capitalization of €7.1 billion" **(Evidence age: 8 years.)**

From 2021 to 2023 the banking permission was extended twice, and in between Adyen started selling products that need it. On 14 June 2021 it announced that the US banking regulators had approved a federal branch in San Francisco **(Evidence age: 5 years.)** On 31 March 2022 it announced "embedded financial products": accounts, cards and capital for the customers of software platforms. Its head of banking products said they came "without the barriers of regulatory complexity, lengthy product development, or sponsor bank restrictions" **(Evidence age: 4 years.)** A sponsor bank is the bank a non-bank provider rents its permission from. On 7 September 2023 it announced that its UK branch had been authorized as a bank **(Evidence age: 3 years.)** All three permissions are confirmed by Adyen's current license pages.

| Date | Step | Source |
| --- | --- | --- |
| 2006 | Founded in Amsterdam | History page, n.d. |
| 2006–2012 | European acquiring license; point-of-sale and risk tools | History page, n.d. |
| 2017 | European banking license | Release, 14 June 2021 |
| June 2018 | Listed on Euronext Amsterdam at €240 a share | Release, 11 June 2018 |
| May–June 2021 | US federal branch approved | Release, 14 June 2021 |
| 31 March 2022 | Embedded financial products announced | Release |
| 7 September 2023 | UK banking authorization announced | Release |
| 2023 | EBITDA margin 46%, from 55% in 2022 | Release, 8 February 2024 |
| 23 April and 11 June 2026 | Agreements to buy Talon.One and Orb | Releases |
| 1 July 2026 | Both acquisitions closed | Release |
| 28 October 2026 | Medium-term margin objective discontinued | Q3 2026 update |

The run of additions has one visible stumble, in 2023. EBITDA is earnings before interest, tax, depreciation and amortization, and Adyen states it as a share of net revenue, which is what it keeps after passing card fees on. For the first half of 2023 that margin landed at 43%, which Adyen's release attributed to "increased wages and salaries stemming from Adyen's investments into scaling its global team" **(Evidence age: 3 years.)** For the full year it was 46%, "compared to 55% in 2022". The audited accounts then show the recovery: 50% in 2024 and 53% in 2025. The margin moved with a hiring decision, not with the platform.

> **INFERENCE, NOT DOCUMENTED:** I read the dates as an order of construction: the acquiring license, then breadth on one platform, then the bank, then products that only a bank can offer without a partner. In each case the permission precedes the product that needs it. Adyen does not describe its history in these terms.

<!-- illustration-placeholder
{
  "id": "47-order-of-construction",
  "status": "pending",
  "asset": "assets/images/47-case-adyen/47-order-of-construction.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the inference block that closes the history section",
  "visual_goal": "Show Adyen's history as layers added in order on one base: acquiring license, bank in three jurisdictions, financial products, and bought software placed beside the stack in 2026.",
  "prompt": "Structural timeline diagram on a light background. A horizontal time axis runs along the bottom with five tick labels: \"2006–2012\", \"2017\", \"2021\", \"2023\", \"2026\". Above the axis, a stack of flat building blocks grows from left to right like a staircase. Block one, widest and lowest, in blue, labeled \"Acquiring\", starts above \"2006–2012\". Block two, in teal, labeled \"Bank EU\", sits on top starting above \"2017\". Block three, in teal, labeled \"Bank US\", starts above \"2021\". Block four, in teal, labeled \"Bank UK\", starts above \"2023\". A green block labeled \"Accounts, cards\" rests on the teal blocks between \"2021\" and \"2023\". To the right of the whole stack, above \"2026\", two separate orange blocks stand beside it and do not touch it, labeled \"Loyalty\" and \"Billing\"; a thin dashed orange arrow labeled \"bought\" points from each orange block toward the stack. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A staircase of blocks on a time axis: acquiring from the 2006 to 2012 period, a bank in the EU from 2017, in the US from 2021 and in the UK from 2023, accounts and cards on top, and two separate blocks for loyalty and billing placed beside the stack in 2026.",
  "caption": "Adyen's order of construction: the acquiring license from the 2006 to 2012 period, banking permissions in 2017, 2021 and 2023, financial products on top, and loyalty and billing bought in 2026 and standing beside the platform."
}
-->

## The Single-Platform Bet in Adyen's Own Words

The Annual Report 2025 states the bet as a choice made early and carried out in steps. "From the beginning, we made a strategic choice: rather than build a business around the limitations of external providers, we would develop and operate the essential layers of the financial stack ourselves." Then: "The first step was our single global platform", so that any improvement "takes effect everywhere, without reintegration work". Next came "acquiring our own banking licenses in the EU, US, and UK", which lets Adyen work "without relying on partner banks, improving reliability and settlement speed". The report's summary puts the three layers in one sentence: "a single platform built entirely in-house", with products "all operated end-to-end on our own infrastructure and banking licenses".

For an integrator, however, "single platform" does not mean one API. Adyen's published API specifications (n.d., accessed November 2026) define separate families for online checkout, account management, platform configuration, transfers, legal-entity verification and terminals, most with their own host and each with its own version number in the URL ([[payment-api-design]], [[payment-api-versioning]]). The Checkout API has no call that returns a payment by its reference. You learn a payment's later states from webhooks and reports ([[payment-state-machines]], [[payment-webhooks-and-events]]). So the phrase is a claim about operation, one place where a change is made, and not about the interface you integrate.

The third layer, Adyen's own infrastructure, has a price that Adyen reports. A 2021 engineering post said: "We manage our own infrastructure in several data centers around the world", and gave the reasons for not using a public cloud as "part historical, part legal, and part technical" **(Evidence age: 5 years; the current system may differ.)** The annual report says that capital expenditure "was €116.8 million and 5% of net revenues" in 2025 and that "The majority of our CapEx is related to our data centers". In August 2026 Adyen said it was "proactively pulling investment from 2027 into H2 2026 to secure compute and storage availability" and expected about 7% for the year. Integrators see it as five named regions for live traffic ([[payment-multi-region-and-data-residency]]).

> **INFERENCE, NOT DOCUMENTED:** "Single platform" is an operating claim, and I think it is best read as a statement about cost: Adyen pays once for a change, and pays for capacity before the volume arrives. Adyen does not put it this way.

## One Bank, Three Jurisdictions, and What the License Allows

A **credit institution** is the European legal term for a bank: it may take deposits and lend, which a payment or e-money institution may not ([[licences-and-safeguarding]]). Adyen's license page (n.d., accessed November 2026) says "Adyen N.V. is authorised as a credit Institution under the supervision of Dutch Central Bank", a license that can be used across the European Economic Area. The same legal entity is "authorised as an overseas branch of an EEA credit institution in the UK", and in the United States it operates "a federal Branch of Adyen, N.V.", licensed by the Office of the Comptroller of the Currency and the Federal Reserve. So Adyen is one bank with two branches, not three banks. Elsewhere it holds narrower local licenses.

Adyen states what the licenses are for. The annual report names "the speed and autonomy that come from not relying on external parties for regulatory compliance". The shareholder letter for the first half of 2026 adds: "Our own licensed infrastructure grants direct access to payment networks, giving us control over funds". "We ended the half with €12.4 billion of total cash", the letter says, and "The majority of that number represents balances moving through our system on behalf of our merchants." Those balances earn interest: finance income was €267.6 million in 2025.

A **payout** is the transfer of a merchant's collected money to its bank account. Under Adyen's Sales day payout, the terms (last updated 17 June 2024) say that Adyen will "initiate payout of the Net Captured Volume to Merchant on the Payout Day, irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner". The documentation (n.d., accessed November 2026) adds the limit: "Prefinancing is capped at 30 days", after which the amount is taken back ([[balances-and-funds-flows]]). The annual report is more cautious. Its risk section calls paying "only after funds have been received" the "default setup" and says liquidity mismatches arise "primarily through pre-financing in accelerated payout schedules". I cannot reconcile the two from public sources.

The license does not reach everywhere, and Adyen says so. **Processed volume** is the value of the payments Adyen handled, and its annual report states: "Of processed volumes, 84% were full-stack volumes, up from 83% in 2024." The report does not define "full-stack" there. Its documentation page on supported payout currencies (n.d., accessed November 2026) lists 14 countries and regions with an "Adyen acquiring connection", from Australia to the United Arab Emirates, and says a payment is processed "through one of our acquiring entities, for example Adyen Singapore". The annual report adds where its concentration risk lies: "primarily at banking partners in locations where there are no own direct acquiring licenses". The map is still being filled: in 2026 Adyen reported a payments license in the United Arab Emirates and approval for direct access to France's domestic clearing system. Its license pages (n.d., accessed November 2026) name an entity for some markets: Adyen Japan KK, registered as a "Merchant Acquirer", and Adyen Singapore, licensed for "merchant acquisition"; a July 2026 article claims "principal membership of Visa and Mastercard in major markets". No page lists either per country.

> **INFERENCE, NOT DOCUMENTED:** Two readings here are mine. I read "full-stack" as the volume for which Adyen is also the acquirer, which leaves about a sixth of volume that Adyen processes and someone else acquires. And I read the sentence about banking partners, which is a statement about concentration risk, as a sign that partner banks stand in for Adyen in some markets; Adyen does not say what those partners do. Adyen gives autonomy as the reason for its licenses, and does not say what they cost in capital and supervision.

## Unified Commerce and the Terminal Estate

In-person payments are a reported line of Adyen's business, and a fast-growing one. The annual report gives "point-of-sale volumes" of "€310.9 billion, comprising 22% of total processed volume, up from 18% in 2024". The update for the third quarter of 2026 says "The number of transacting terminals across the platform reached 878k, up 25% YoY". "Transacting" is not defined. One trap: **Unified Commerce** is also one of Adyen's three reporting pillars (Digital, Unified Commerce and Platforms), and the pillar is a different measure. It covers retailers, hospitality and food and beverage groups that sell in both channels, online volume included, and brought €765.4 million of net revenue in 2025.

[[in-person-payments]] owns how the channel is built. In brief, Adyen supplies and manages the terminals, and in August 2022 it announced "its first in-house designed terminals" **(Evidence age: 4 years.)** Its documentation (n.d., accessed November 2026) says it releases terminal software "every four weeks" and rolls it out "gradually". Software drives them through a Terminal API that, the documentation says, "is based on the nexo Retailer Protocol", a standard that tills already speak. Counter and web payments land on the same platform, which lets a merchant recognize a card and refund a purchase across channels.

> **INFERENCE, NOT DOCUMENTED:** The terminal estate is an asset of logistics, certification and device management that grew over years. It is also the reason Adyen gives for buying a loyalty engine.

## Platforms, Financial Products, and What Adyen Did Not Sell

Platforms is the smallest of the three pillars and the fastest growing. It serves software companies that embed payments for their own business customers ([[platform-payment-models]]). Its net revenue was €263.8 million in 2025, up from €176.1 million, and €100.2 million in the third quarter of 2026 alone, up 46%. Adyen then counted 46 platform customers "processing over €1 billion annually" and 312,000 active business customers behind them. The update says why the pillar matters: "Our Platforms offering allows us to provide payments and financial products to smaller merchants, which will be a key driver of future growth."

The financial products sold through platforms rest on the license and, by one old account, on the same books as payments. Adyen's 2021 post on its accounting system says: "We leverage this same system of accounting for our banking platform" **(Evidence age: 5 years; the current system may differ.)** The 2026 shareholder letter describes "native business accounts, card issuing, and capital within a single integration". Availability is narrower. The documentation (n.d., accessed November 2026) says card issuing is "currently supported in the European Economic Area, the United Kingdom, and the United States", and it still marks business accounts with "This feature is in development phase" ([[embedded-finance]], [[payment-ledgers]]).

Just as telling is what Adyen did not sell before July 2026. It had no billing engine: in its documentation a subscription is a stored card token that the merchant charges on its own schedule, with no plan, invoice or proration held by Adyen ([[subscriptions-and-billing-engines]]). It is not a **merchant of record**, the party that sells to the end customer in its own name, taking over the indirect tax and dispute handling. An Adyen article of 15 September 2026 says "Adyen doesn't act as a direct, third-party merchant of record" ([[merchant-of-record]]). And I found no first-party Adyen product that calculates or files sales tax in its documentation or on its site as of November 2026 ([[billing-and-payment-tax]]).

> **INFERENCE, NOT DOCUMENTED:** The edge fits the first customer. An enterprise has its own billing system, legal entities and tax department, so a provider that stops at the payment suits it. Smaller merchants and software companies that price by usage have none of those. I read the acquisitions of 2026 as the consequence; Adyen's own stated reasons follow.

## July 2026: Loyalty and Usage Billing, Bought

On 23 April 2026 Adyen announced that it would buy Talon.One, and on 11 June that it would buy Orb. Its closing release says: "Both transactions officially closed on July 1, 2026". In the table below, ARR is annual recurring revenue, and "multi-PSP" (PSP: payment service provider) means that Orb goes on billing for customers whose payments run through Adyen's competitors.

| | Talon.One | Orb |
| --- | --- | --- |
| What it is | "a leading platform for loyalty and incentives serving 300+ global merchants", Germany | A usage-based billing platform, San Francisco, founded 2021; customers include Vercel, Glean, Replit and Supabase |
| Announced | 23 April 2026 | 11 June 2026 |
| Price | "a total consideration of €750 million", from available cash | "$335 million" |
| Closed | 1 July 2026 | 1 July 2026 |
| Size | "approximately €60 million in ARR as of the end of this year" | Total funding $44 million; revenue not disclosed |
| How Adyen says it is run | The promotion engine is to be integrated "directly into our architecture" | "an incubator model", "continuing to support multi-PSP environments" |

Read in date order, management's statements move a long way in four months, and none of them says that Adyen has stopped building in-house. On 9 April came the sentence about "a patchwork of acquired technologies". On 1 July the closing release spoke of a "multi-product reality". On 13 August the shareholder letter said "we are no longer just a payments company" and, on capital: "While organic growth remains our foundation, our strong balance sheet allows us to selectively deploy capital to accelerate our platform roadmap". An Adyen article of 29 September 2026 gives the plainest account: "we've historically stayed singularly focused on solving the hardest problems in payments... When the opportunity to do something presented itself, we decided to act." The shorthand that Adyen builds and never buys is in none of the Adyen documents read.

As of 17 November 2026 Adyen says integration has begun, not what is joined: its release of 28 October 2026 speaks of "the successful ongoing integration of Talon.One and Orb". For Talon.One the August letter uses the future tense: "Integrating Talon.One's promotion engine directly into our architecture will bridge this gap". For Orb the announcement says "Adyen is adopting an incubator model, preserving Orb's operational continuity during the first phase of the acquisition and continuing to support multi-PSP environments", and "Beyond this first phase, the strategic intent is convergence". No date is given; the September article says only "You'll soon see". Adyen's documentation has no billing product page; Orb's (n.d., accessed November 2026) lists Adyen as a payment gateway connected with an API key. Reported effects are commercial: Adyen says it "won the payments volumes of several" Orb customers and expects the deals to add about one percentage point to 2026 net revenue growth, with "an estimated 1 percentage point margin dilution". If you add either product, plan for separate credentials, events and reports, and ask Adyen what is shared.

What do the acquisitions change about the phrase? For payments, acquiring, terminals and the banking products, nothing. For the company, the phrase is no longer complete. Adyen's pages now carry both descriptions. Its acquiring page (n.d.) says "We've built our entire platform in house." Its history page (n.d.) says "With the acquisition of Orb and Talon.One... we've moved beyond payments and built a full enterprise financial operating system."

> **INFERENCE, NOT DOCUMENTED:** The sentence I would use is this: Adyen built its payments and banking platform and, since July 2026, buys adjacent software. Its 2021 engineering post, writing about vendor software, already allowed buying "if the use case is peripheral" **(Evidence age: 5 years.)** Billing and loyalty are now called part of the platform, so the rule has moved. Whether the two products will be rebuilt on the platform or connected to it is not known.

<!-- illustration-placeholder
{
  "id": "47-platform-and-bought-products",
  "status": "pending",
  "asset": "assets/images/47-case-adyen/47-platform-and-bought-products.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the inference block that closes the acquisitions section",
  "visual_goal": "Show that payments, acquiring, terminals and banking products sit inside one platform, while the two products bought in 2026 sit outside it, one being connected and one still serving other providers.",
  "prompt": "Component layout diagram on a light background. In the center-left, one large rounded rectangle in blue labeled \"One platform\" contains four smaller teal tiles in a two-by-two grid labeled \"Payments\", \"Acquiring\", \"Terminals\" and \"Accounts, cards\"; under the grid, inside the same rectangle, a long thin green bar labeled \"One ledger\". To the right of the large rectangle, outside it, two separate orange rounded boxes are stacked vertically with a clear gap from the platform: the upper one labeled \"Loyalty\", the lower one labeled \"Billing\". A solid orange arrow labeled \"being integrated\" runs from the \"Loyalty\" box to the edge of the large rectangle. A dashed orange arrow labeled \"intent\" runs from the \"Billing\" box to the edge of the large rectangle. From the \"Billing\" box a second thin gray arrow labeled \"other providers\" runs to the far right toward two small generic gray provider icons. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A large box labeled one platform holds payments, acquiring, terminals, accounts and cards over one ledger. Outside it stand two boxes, loyalty and billing; loyalty has an arrow marked being integrated, billing an arrow marked intent and another arrow to other providers.",
  "caption": "Since 1 July 2026 the single platform is the core, not the company: loyalty is being integrated, and usage billing, as Adyen described it in June 2026, runs under an incubator model and still serves other payment providers."
}
-->

## The Figures, With Their Definitions

Four measures carry Adyen's reporting, and they are not interchangeable. Processed volume, met above, is the value of the payments Adyen handled; the report gives no one-sentence definition, and it includes the 16% that was not full-stack. **Net revenue** is what Adyen keeps. **Interchange** is the fee the acquirer pays to the bank that issued the card, and scheme fees go to the card network; Adyen passes both through to the merchant and leaves them out of this number. In the audited notes it is a non-IFRS measure, one the accounting standards do not define: revenue less costs charged by financial institutions and the cost of terminals sold, plus net interest income. **Take rate** is net revenue divided by processed volume, in basis points (one basis point is 0.01%). **EBITDA margin** is EBITDA divided by net revenue. The full-year columns below come from audited accounts; the 2026 columns are unaudited.

| Measure | 2023 | 2024 | 2025 | H1 2026 | Q3 2026 |
| --- | --- | --- | --- | --- | --- |
| Processed volume | €970.1 billion | €1,285.9 billion | €1,394.3 billion | €803.8 billion | €451.1 billion |
| Net revenue | €1,626.1 million | €1,996.1 million | €2,364.2 million | €1,302.9 million | €738.1 million |
| Take rate | not used here | 15.5 bps | 17.0 bps | 16.2 bps | not given |
| EBITDA margin | 46% | 50% | 53% | 49% | not reported |
| In-person volume | €159.9 billion | €232.7 billion | €310.9 billion | €175.7 billion | not given |

Take 2025, when the measures moved apart: processed volume grew 8% and net revenue grew 18%. That looks like a price increase. Adyen's reporting says otherwise. Its results release gives volume as "up 21% excluding a single large-volume customer, or 8% YoY including this customer"; it does not name the customer. The annual report gives the other half: "Full-year take rate for 2025 was 17.0 bps, up from 15.5 bps in 2024. This increase was driven by changes in the overall merchant mix." The link between the two is the pricing model. Adyen's pricing page (n.d., accessed November 2026) describes "a fixed processing fee + a fee determined by the payment method", with card costs passed on under **Interchange++**: interchange, scheme fee and Adyen's markup shown separately. Its October 2026 update adds that "Adyen's tiered pricing structure incentivizes our customers to bring more volume". The largest customers pay the lowest rates, so losing volume from one of them lowers volume far more than revenue. In the first half of 2026 the take rate fell back to 16.2 basis points, "reflecting expected volume tiering".

Whose volume is it? The annual report splits 2025 net revenue into three pillars: Digital (online-first businesses) €1,334.9 million, Unified Commerce €765.4 million and Platforms €263.8 million. "Adyen's top 10 merchants represent 11% of revenue (2024: 12%)", and no customer exceeded 10%. Growth comes mostly from customers Adyen already has: "Our typical share of wallet increases from under 20% in years 3–7 to over 40% after year 12". The risk section says why: "Large enterprise merchants typically work with multiple payment service providers to mitigate their own single-point-of-failure risk. As a result, these customers may terminate contracts or shift volume elsewhere".

What is left is the margin, and here Adyen makes a causal claim. The letter for the first half of 2026 reports 49%, or 50% without acquisition costs, as "demonstrating the underlying operational efficiency inherent to our single-platform architecture as we scale". The same documents show the margin following decisions about investment. In November 2025 Adyen expected "to increase EBITDA margin levels to above 55% by 2028". On 28 October 2026 it wrote: "we now expect EBITDA margin of 50% in 2026. To retain flexibility, we are discontinuing our medium-term EBITDA objective." By then it had 5,596 full-time staff, 399 of them from the acquisitions.

> **INFERENCE, NOT DOCUMENTED:** A 53% margin does not show that the architecture causes it: that link is Adyen's attribution, and 2023 and 2026 both show the margin moving with hiring while the platform stayed the same. Volume is not revenue either. By my arithmetic, Adyen kept about one euro of net revenue for every €590 it processed in 2025.

<!-- illustration-placeholder
{
  "id": "47-volume-is-not-revenue",
  "status": "pending",
  "asset": "assets/images/47-case-adyen/47-volume-is-not-revenue.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the inference block that closes the figures section",
  "visual_goal": "Make memorable how small net revenue is next to processed volume, and that EBITDA is about half of net revenue.",
  "prompt": "Conceptual scale illustration on a light background, read left to right in three steps connected by two arrows. Step one on the left: a very large pale-blue circle filling most of the height, labeled \"Volume\" with the caption \"€1,394.3 bn\" beneath it; inside the circle, faint generic payment cards and coins drift. A teal arrow labeled \"17 bps\" runs from the large circle to step two. Step two in the middle: a tiny solid teal dot, drawn clearly but very small compared with the circle, placed under a magnifying glass so it can be seen; label \"Net revenue\" with the caption \"€2,364.2 m\". A green arrow labeled \"53%\" runs from the magnified dot to step three. Step three on the right: inside a second magnifying glass, the same teal dot shown enlarged and split in two halves, the left half green and labeled \"EBITDA\" with the caption \"€1,245.7 m\", the right half pale gray. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A very large circle for processed volume, a tiny dot under a magnifying glass for net revenue, and the dot enlarged and half shaded for EBITDA.",
  "caption": "Volume is not revenue: of €1,394.3 billion processed in 2025, Adyen kept €2,364.2 million as net revenue, a take rate of 17.0 basis points, and 53% of that was EBITDA."
}
-->

## The Engineering Record, and How Old It Is

The figures are current and audited. The engineering record is neither. Adyen's sitemap (accessed November 2026) lists 575 knowledge-hub pages, and by my count only a few dozen are engineering posts. The ones that describe the architecture are "From 0 — $100 billion" (January 2018) and the two parts of "Design to Duty" (July and August 2021). Newer posts cover narrower ground: PostgreSQL partitioning (2023 to 2025), one incident (2025) and an internal map of the platform (2026). No post gives a topology. Adyen's Infrastructure page (n.d., accessed November 2026) names data centers "in Europe, the United States, India, Singapore, Japan and Australia" and says "we publish new releases of our core system every week". The documentation's peak-season page (n.d.) describes an "active/active, stateless architecture", failover between data centers by load balancers, utilization "generally less than 30%" and a deployment freeze around named peak days ([[payment-peak-load]]).

The most useful item is the 2021 account of the edge and the books **(Evidence age: 5 years; the current system may differ.)** The layer that accepts payments is stateless and built for uptime. The accounting system has the opposite priority: "we don't mind if they are down for a little bit as long as we can guarantee their reliability and consistency". A local queue sits between them, so the books may lag without stopping payments ([[payment-reliability-and-availability]]). And the books are guarded where entries are written: "The only way to add new records to the accounting system is by means of templates", these "are mathematically verified", and so "if at any time, we sum up all the records in the accounting system, the result will always be 0".

The same posts describe the storage and the way changes ship. The accounting database is PostgreSQL, split into several clusters filled in rotation; Adyen names the cost plainly, "The migration to a sharded accounting database was quite painful" ([[payment-data-stores-and-consistency]]). The design may have moved: on a June 2024 podcast panel an Adyen database engineer said "we are actually reaching the limits of our sharding solution again" and, of asynchronous or synchronous replication, "We have both". Beside PostgreSQL the 2021 post names "Cockroach, a distributed database", used at the edge for idempotency ([[idempotency-and-retries]]). The code was "a single platform, in a single repository (monorepo), almost exclusively written in Java"; a 2026 post updates that: "Our monorepo alone runs to hundreds of thousands of files, and it's far from the only one." The 2018 post describes how changes reach production: "everybody develops on the main line", and "we toggle features one-by-one on production, and then canary them" **(Evidence age: 8 years; the current system may differ.)** Adyen states no other cadence for its core platform ([[payment-safe-change]]).

Sources from 2025 and 2026 add scale and one incident, not design. The 2026 post counts "around 3,000 live services" on "tens of thousands of hosts spread across tens of data centres". On 21 April 2025 a distributed denial-of-service (DDoS) attack, a flood of requests meant to exhaust capacity, "specifically targeted services within our European datacenters"; Adyen's update says it was resolved "by 03:20 CEST on April 22, 2025" and that a detailed review would go to customers; none is public. A follow-up of 31 October 2025 lists the response, including "introducing additional global DDoS mitigation partners, such as Cloudflare, alongside existing global providers".

> **INFERENCE, NOT DOCUMENTED:** "Single platform" is not a single process: 3,000 services is a large distributed system under one roof. The in-house rule bends at the edge. And the public picture of Adyen's internals is a 2021 snapshot with a few later measurements laid over it, so anything this book says about how Adyen works inside should be read as "in 2021, Adyen described".

## What Transfers to a Builder, and What Does Not

The table is my synthesis. Each row names its dated evidence and says whether a team building its own payment service can use it.

| Lesson | Evidence | Transfers? |
| --- | --- | --- |
| One accounting core for every money movement, with entries proven to sum to zero when written | Design to Duty, 2021 (5 years old) | Yes. A constraint and a fixed set of posting functions do it at small scale |
| One place where each change takes effect for all customers | Annual Report 2025; main-line practice, 2018 | Yes, as a rule for your own payment service: no per-customer forks |
| A version visible in every request | Documentation, n.d., accessed November 2026 | Yes |
| Banking licenses in three jurisdictions | 2017, 2021, 2023 | No. An asset granted by regulators over years |
| Own data-center capacity at 5 to 7% of net revenue | Annual Report 2025; August 2026 | No. Rent capacity |
| 878,000 transacting terminals | Q3 2026 update | No. Use a provider's estate |
| A 53% EBITDA margin | Annual Report 2025 | Not a design lesson; the link to the architecture is Adyen's attribution |

Suppose a logistics platform has nine people in its payments team and wants "what Adyen has". It can adopt the first three rows this year. It cannot copy the next three. Larkfield, with 11 people in its payments team, works this way: a small double-entry ledger of its own since 2025 and no ambition to hold a license. Adyen itself discloses a limit. Its largest customers "typically work with multiple payment service providers". Larkfield keeps 44% of its volume on Stripe and 56% on Adyen and rehearses the switch between them (K8 in [[meet-larkfield]]), which is the customer's side of that sentence.

## Where the Evidence Stops

By 17 November 2026 I had found no public source for any of the following. Each is a question for Adyen.

- **Who acquires where.** Adyen lists 14 countries and regions with an acquiring connection, and names a licensed entity for some, but gives no list of acquiring entities or card-network memberships per country, the volume behind the 16% that is not full-stack, or what its banking partners do.
- **What processed volume counts, and who left.** The exact definition, and the identity of the single large-volume customer behind the 2025 figures.
- **The data centers.** Six regions are named, but not cities, operators, a count more exact than "tens", how failover works, or how much space is rented from the "data center partners" the annual report mentions.
- **Whether the 2021 accounting design is current.** The 2024 remark says the sharding was being redesigned; the result, the number of clusters, and how balance accounts for platforms relate to it are not published.
- **Integration of Talon.One and Orb.** What is shared today (credentials, events, reports), and when "convergence" happens.
- **Which banks hold merchants' funds.** The split between central banks and commercial banks, by currency. (Deposits in Adyen N.V. fall under the Dutch deposit guarantee, per the platform documentation.)
- **What management said aloud.** Whether Adyen has said on an earnings call that its stance on building in-house changed.

## What to Take Away

**Established.**

- Adyen N.V. is one licensed credit institution under the Dutch central bank, with a federal branch in the United States (2021) and a branch authorized as a bank in the United Kingdom (2023).
- The single-platform choice is stated in the Annual Report 2025. The audited 2025 figures are €1,394.3 billion processed, €2,364.2 million of net revenue, a 53% EBITDA margin and a take rate of 17.0 basis points.
- Adyen discloses the platform's edge: 84% of 2025 volume was full-stack, its documentation lists 14 countries and regions with an acquiring connection, and its risk section names banking partners where it has no acquiring license of its own.
- Talon.One and Orb closed on 1 July 2026. Orb runs under "an incubator model" and still serves other payment providers; convergence is stated as intent, with no date.

**Depends on context.**

- Whether "one platform" means one integration for you depends on what you buy and when. With Orb or Talon.One, plan for separate systems until Adyen documents otherwise.
- Whether Adyen is your acquirer, and whether it pays you before the networks pay it, depends on the country and the payout model. Ask per country.
- Whether Adyen's practices suit you depends on what you build. The accounting discipline scales down; the infrastructure does not.

**The author's synthesis.**

- "Single platform, built in-house" is a description with a scope and a date. I would rewrite the architect's opening sentence as: "Adyen's payments, acquiring, terminals and banking products run on one platform it built; its loyalty and billing products were bought in July 2026 and are not yet on it."
- The lesson I take from Adyen is the order in which it built, not the stack it ended with: permission first, then the product that needs it.

## Questions to Ask

1. Which of the Adyen products we use, or plan to use, run on the platform Adyen built, and which were bought in 2026?
2. For a bought product, what is shared with the payments platform today: credentials, events, reports, support?
3. In each country we sell in, which legal entity acquires our payments: an Adyen entity under its own license, or a banking partner?
4. Which payout model applies to each of our accounts, and are we paid before Adyen has received the funds?
5. Which of Adyen's APIs does our integration touch, and which version of each do we send?
6. When someone quotes a volume, a margin or a take rate, which definition and which period is behind it?
7. What in our own payment service plays the role of Adyen's templates, the check that entries balance before they are written?

Both records have now been read on their own terms: Stripe built the interface first and assembled the regulated layer afterward as a non-bank, and Adyen built the license and the platform first and bought adjacent software in 2026. [[stripe-and-adyen-bets-compared]] sets the two side by side on the same rows, gathers the "Where They Differ" tables of the earlier parts under them, and sorts each difference by the kind of evidence behind it.

## Sources and Evidence

*Company, product and investor sources*

- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., signed 2026-03-05 — the strategic choice, the three layers, capital expenditure, full-stack share, banking partners, finance income, take rate, pillars, top-ten merchants, the multi-provider risk statement, the definition of net revenue, "data center partners" (audited; read in the PDF this page offers for download, a "printed version" that names the electronic reporting package as the official filing).
- [H1 2026 Shareholder Letter](https://investors.adyen.com/financials/h1-2026-c2a1a), Adyen, 2026-08-13 — licenses and control over funds, total cash, take rate of 16.2 basis points, share of wallet, the margin attribution, Talon.One integration wording, notes on both acquisitions (unaudited).
- [H2 2025 Shareholder Letter](https://investors.adyen.com/financials/h2-2025-4r9rc), Adyen, 2026-02-12 — processed volume with and without the single large-volume customer.
- [Q3 2026 Business Update](https://investors.adyen.com/financials/q3-2026-10c88s), Adyen, 2026-10-28 — transacting terminals, pillar figures, platform customers, tiered pricing, Orb customers won, full-time staff, the 2026 margin expectation and the discontinued objective (unaudited).
- [Adyen publishes Q3 2026 business update](https://www.adyen.com/press-and-media/adyen-publishes-q3-2026-business-update-6r9vz0), Adyen, 2026-10-28 — the same figures and guidance in release form; "the successful ongoing integration of Talon.One and Orb".
- [Adyen publishes H1 2026 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne), Adyen, 2026-08-13 — half-year figures; capital expenditure pulled forward, about 7% of net revenue; the UAE license and French clearing access.
- [Adyen publishes H2 2025 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2), Adyen, 2026-02-12 — volume "up 21% excluding a single large-volume customer".
- [Adyen publishes H2 2024 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h2-2024-financial-results), Adyen, 2025-02-13 — 2024 volume, net revenue, margin and in-person volume.
- [Adyen publishes H2 2023 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h2-2023-financial-results), Adyen, 2024-02-08 — 2023 figures; margin of 46% against 55% in 2022.
- [Adyen publishes H1 2023 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h1-2023-financial-results), Adyen, 2023-08-17 — margin of 43% and its attribution to team growth (evidence age: 3 years).
- [Adyen hosts Investor Day 2025 in Amsterdam](https://www.adyen.com/press-and-media/adyen-hosts-investor-day-2025-in-amsterdam), Adyen, 2025-11-11 — the objective of an EBITDA margin above 55% by 2028.
- [Adyen to acquire Talon.One](https://www.adyen.com/press-and-media/2i4hnm0pfcpvc7), Adyen, 2026-04-23 — description, price, financing, expected recurring revenue.
- [Adyen to acquire Orb to unify billing and payments infrastructure for enterprise merchants](https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj), Adyen, 2026-06-11 — description, price, the incubator model, multi-PSP support, convergence as intent.
- [Adyen Closes Talon.One and Orb Acquisitions; Announces Leadership Updates Across Product and Finance](https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates), Adyen, 2026-07-01 — closing date; "multi-product reality".
- [Adyen launches Intelligent Money Movement](https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement), Adyen, 2026-04-09 — the sentence on "a patchwork of acquired technologies".
- [Why billing and payments belong together](https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb), Adyen, 2026-09-29 — the stated reason for buying instead of building; "You'll soon see".
- [About Adyen](https://www.adyen.com/about), Adyen, n.d., accessed 2026-11 — founding, history by period, "Built for enterprise", the acquisitions in the history.
- [Global Payment Processing: Accept, Process, And Settle](https://www.adyen.com/global-acquiring), Adyen, n.d., accessed 2026-11 — "We've built our entire platform in house."
- [Payments platform infrastructure](https://www.adyen.com/infrastructure), Adyen, n.d., accessed 2026-11 — the six data-center regions; weekly releases of the core system.
- [Sitemap (English)](https://www.adyen.com/sitemap-en.xml), Adyen, n.d., accessed 2026-11 — 575 knowledge-hub page addresses; the count of engineering posts among them is the author's.
- [Pricing for supported payment methods](https://www.adyen.com/pricing), Adyen, n.d., accessed 2026-11 — processing fee plus a fee per payment method; Interchange++ (volatile).
- [Licenses and disclosures: EMEA](https://www.adyen.com/licenses/emea), Adyen, n.d., accessed 2026-11 — credit institution under the Dutch central bank; the UK branch.
- [Licenses and disclosures: United States](https://www.adyen.com/licenses/united-states), Adyen, n.d., accessed 2026-11 — the federal branch.
- [Licenses and disclosures: Japan](https://www.adyen.com/licenses/japan) and [Singapore](https://www.adyen.com/licenses/singapore), Adyen, n.d., accessed 2026-11 — Adyen Japan KK's registration as merchant acquirer; Adyen Singapore's license for merchant acquisition.
- [Credit card processing fees: what determines your rate and why the lowest isn't always the cheapest](https://www.adyen.com/knowledge-hub/credit-card-processing-fees), Adyen, 2026-07-03 — "principal membership of Visa and Mastercard in major markets" (vendor claim, no list).
- [Adyen granted US branch license](https://www.adyen.com/press-and-media/adyen-granted-us-branch-license), Adyen, 2021-06-14 — US approvals; the European banking license "obtained in 2017" (evidence age: 5 years).
- [Adyen granted UK banking authorization](https://www.adyen.com/press-and-media/adyen-granted-uk-banking-authorization), Adyen, 2023-09-07 — the UK authorization (evidence age: 3 years).
- [Adyen expands beyond payments, announces embedded financial products](https://www.adyen.com/press-and-media/adyen-expands-beyond-payments-announces-embedded-financial-products), Adyen, 2022-03-31 — the announcement and the sponsor-bank quotation (evidence age: 4 years).
- [Adyen IPO priced at €240 per share](https://www.adyen.com/press-and-media/adyen-ipo-priced-at-240-per-share), Adyen, 2018-06-11 — the listing (evidence age: 8 years).
- [Adyen advances in-person payments with the launch of in-house designed terminal range](https://www.adyen.com/press-and-media/adyen-advances-in-person-payments-with-the-launch-of-in-house-designed-terminal-range), Adyen, 2022-08-18 — first terminals designed in-house (evidence age: 4 years).
- [Sales Day Payout Terms of Service](https://www.adyen.com/legal/sales-day-payout-terms-of-service), Adyen, last update 2024-06-17 — payout irrespective of receipt of funds.
- [Merchant of record explained: Everything you need to know](https://www.adyen.com/knowledge-hub/merchant-of-record), Adyen, 2026-09-15 — Adyen's statement that it is not a merchant of record.
- [Design to Duty: How we make architecture decisions at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture), Adyen, 2021-07-28 (the page says "Updated June 2022") — own infrastructure and the reasons, the Java monorepo, the stateless edge, "Cockroach, a distributed database", when Adyen buys (evidence age: 5 years).
- [Design to Duty: The Accounting and Reporting Systems at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2), Willem Pino, Adyen, 2021-08-23 — templates, the zero-sum guarantee, the local queue, sharding and its cost, one accounting system for the banking platform (evidence age: 5 years).
- [From 0 — $100 billion: Scaling infrastructure and workflow at Adyen](https://www.adyen.com/knowledge-hub/from-0-100-billion-scaling-infrastructure-and-workflow-at-adyen), Michiel Toneman, Adyen, 2018-01-03 — main-line development, feature toggles and canaries (evidence age: 8 years).
- [We built Architect for humans. Agents made it transformative.](https://www.adyen.com/knowledge-hub/architect-blog-1), Adyen, 2026-08-23 — service, host and data-center counts; more than one repository.
- [Incident update: Mitigating a DDoS attack on April 21, 2025](https://www.adyen.com/knowledge-hub/mitigating-a-ddos-april-2025), Adyen, 2025-04-21 — the attack, its resolution time, the review promised to customers.
- [A Deep Dive into Table Partitioning, Part 2: Partitioning at Adyen](https://www.adyen.com/knowledge-hub/partitioning-at-adyen), Derk van Veen and Cosmin Octavian Pene, Adyen, 2023-10-06 — the first of the partitioning posts counted (evidence age: 3 years).
- [A Deep Dive into Table Partitioning, Part 5: Partitioning an environment, not individual tables](https://www.adyen.com/knowledge-hub/partitioning-an-environment-not-individual-tables), Derk van Veen, Adyen, 2025-09-16 — the latest of the partitioning posts counted.
- [Strengthening Our Platform Resilience: An Update](https://www.adyen.com/knowledge-hub/strengthening-our-platform-resilience), Adyen, 2025-10-31 — outside mitigation partners added after the attack.
- [Adyen OpenAPI definitions](https://github.com/Adyen/adyen-openapi), Adyen, n.d., accessed 2026-11 — the API families, their hosts and versions; no call that returns a payment in the Checkout API.

*Standards, regulation and official documentation*

- [Upgrade to Sales day payout](https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp), Adyen documentation, n.d., accessed 2026-11 — "Prefinancing is capped at 30 days".
- [Supported payout currencies](https://docs.adyen.com/account/supported-currencies), Adyen documentation, n.d., accessed 2026-11 — 14 countries and regions with an Adyen acquiring connection; "one of our acquiring entities, for example Adyen Singapore".
- [Versioning](https://docs.adyen.com/development-resources/versioning), Adyen documentation, n.d., accessed 2026-11 — a version number in each API URL.
- [Best practices for web integrations](https://docs.adyen.com/online-payments/web-best-practices), Adyen documentation, n.d., accessed 2026-11 — the five live regions.
- [Terminal API](https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api), Adyen documentation, n.d., accessed 2026-11 — the nexo Retailer Protocol.
- [Update to a new release](https://docs.adyen.com/point-of-sale/release-updating), Adyen documentation, n.d., accessed 2026-11 — terminal software every four weeks, rolled out gradually.
- [Peak season readiness](https://docs.adyen.com/industries/peak-season), Adyen documentation, n.d., accessed 2026-11 — active/active stateless architecture, failover by load balancers, utilization under 30%, the deployment freeze.
- [EU depositor information sheet](https://docs.adyen.com/platforms/compliance-financial-products/eu-depositor-info-sheet), Adyen documentation, n.d., accessed 2026-11 — deposits in Adyen N.V. and the Dutch deposit guarantee.
- [Adyen](https://docs.withorb.com/integrations-and-exports/adyen), Orb documentation, n.d., accessed 2026-11 — Adyen as a payment gateway for Orb invoices, connected with an API key.
- [Tokenization](https://docs.adyen.com/online-payments/tokenization), Adyen documentation, n.d., accessed 2026-11 — subscriptions as payments the merchant initiates.
- [Issuing](https://docs.adyen.com/issuing), Adyen documentation, n.d., accessed 2026-11 — regions where card issuing is supported.
- [Business accounts](https://docs.adyen.com/business-accounts), Adyen documentation, n.d., accessed 2026-11 — "This feature is in development phase".

*Research and practitioner sources*

- [To 100TB, and beyond!](https://postgres.fm/episodes/to-100tb-and-beyond), Postgres FM podcast, episode 100, 2024-06-07 — remarks by Derk van Veen of Adyen on a panel: sharding at its limits again, both asynchronous and synchronous replication (a spoken remark in the show's transcript, not an Adyen publication).

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
