---
title: "Other Answers: PayPal and Braintree, Checkout.com, Block"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What do three other payment companies show about the Stripe and Adyen bets? Each started with a different customer and holds something neither anchor holds: a consumer wallet, a set of acquiring licenses assembled later, a seller’s till and a lending bank. The evidence is filings and press releases about business models, not architecture."
permalink: payment-contrast-cases
timetoread: 15 min read
---

> **IN THIS CHAPTER, YOU WILL:** Read three other payment companies, each for the one choice it clarifies about Stripe and Adyen, and learn where that evidence stops.

> **KEY POINTS:**
>
> * **PayPal's asset is the shopper, not the processing.** Its filing for 2025 describes "a global, two-sided network" of 439 million active accounts, and says that Braintree, its card-processing business, has "higher expense rates" than its other products. Its $1.79 trillion of volume is not Braintree's volume and is not defined like Stripe's.
> * **Checkout.com and Block hold permissions of other kinds.** Checkout.com reports ten acquiring licenses and, in a September 2026 announcement, US acquiring under the same narrow Georgia charter that Stripe lists among its acquirers. Block sells the seller a till, rents most of its acquiring and owns a Utah industrial bank that lends to its sellers.
> * **My reading is an inference, and the evidence is thin by design.** A provider seems to hold the permissions its first customers required. Three cases cannot prove that. The sources are filings and releases about business models; nothing here describes how these companies build their systems.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Borrowed Blueprint** — a provider's shape follows from the customer it started with, so copying the shape without that customer copies the cost and not the reason.
> * **The Accidental Bank** — "it has a bank" means three different things in this chapter, and only one of them is permission to hold other people's money.
> * **The Single Rail** — Adyen's own annual report expects large merchants to use several providers, and one of these cases is the usual second one.

<br>
For 2025, PayPal reported $1.79 trillion of total payment volume, and the release that accompanied Stripe's annual letter reported $1.9 trillion of total volume. The two numbers look like a close race between two card processors. PayPal's own annual filing says otherwise: "As a result of our stronger focus on profitable growth and ongoing negotiations with merchants, we experienced lower volume and transaction revenue from our Braintree offerings in the first half of 2025". Braintree is the part of PayPal that does what Stripe does. **The company with the near-equal number chose, for half a year, to process less.**

The explanation is that PayPal did not start where Stripe or Adyen started, and neither did the two other companies in this chapter. PayPal began with the shopper, Checkout.com with the enterprise merchant some years after Adyen, and Block with a shopkeeper who needed a till. Each holds something neither anchor holds. Together they suggest that **a provider holds the regulated permissions and assets that its first customer relationship required**. That sentence is my inference, not any company's statement, and the evidence behind it concerns business models only.

**Where we are in the payment's journey.** This chapter stands beside the path of Mila Janssen's class pass. On 9 March 2027 Mila paid €120.00 to Studio Noord from her phone's wallet, inside the booking app of Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]). Adyen carried the payment and has no account with Mila. The relationship with the payer belonged to the phone's wallet and to Larkfield's app.

The chapter first says how to read its evidence. It then takes PayPal and Braintree, Checkout.com and Block in turn, each for one point, sets the three beside Stripe and Adyen, and ends with where the evidence stops.

## How to Read This Case

Every company fact below comes from one of three kinds of document, fetched on 17 November 2026, which is the research cut-off. Two are Form 10-K filings for 2025, the audited annual report a company listed in the United States files with the Securities and Exchange Commission: PayPal's of 3 February 2026 and Block's of 26 February 2026. The third kind is weaker: three 2026 press releases from Checkout.com, a private company, whose figures nobody outside it has audited. Where I interpret, the text is marked `INFERENCE, NOT DOCUMENTED`. One thing was left out: PayPal and Checkout.com publish engineering blogs (accessed November 2026), which I did not read for this chapter, so it says nothing about how they are built. The two Georgia bank charters are confirmed by the state regulator's bulletins; what such a charter permits rests on one trade-association report.

All five companies in this chapter publish a volume figure, and no two define it alike. I give each with its definition and do not rank them.

| Company | Figure for 2025 | What it counts | Status |
| --- | --- | --- | --- |
| Stripe | $1.9 trillion "in total volume" | Not defined | Private company's release and letter |
| Adyen | €1,394.3 billion processed volume | Volume processed on its platform; 84% of it "full-stack" | Audited annual report |
| PayPal | $1.79 trillion total payment volume (TPV) | "net of payment reversals ... not including gateway-exclusive transactions"; the whole company, wallets included | Audited filing |
| Checkout.com | "over $300B" total processed volume | Not defined | Private company's release |
| Block | $250 billion Square gross payment volume (GPV) | "all card and bank payments processed by sellers using Square, net of refunds" | Audited filing |

<!-- illustration-placeholder
{
  "id": "49-five-measuring-cups",
  "status": "pending",
  "asset": "assets/images/49-contrast-cases/49-five-measuring-cups.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of the five volume figures",
  "visual_goal": "Show that five companies measure payment volume with five differently shaped measures, so the amounts cannot be ranked.",
  "prompt": "Conceptual illustration of a long kitchen counter seen from the front with five measuring vessels in a row, each a clearly different shape and each partly filled with coins: a tall narrow cylinder, a wide shallow bowl, a conical flask, a square jug with a handle, and a small rounded cup. Each vessel has its own different scale markings on the side, none of them aligned with the next. Under the vessels, small tags read \"Total volume\", \"Processed\", \"TPV\", \"Processed\" and \"GPV\". On the right, a person in office clothes holds a ruler horizontally across the tops of the vessels and looks puzzled, with a small orange question mark above the ruler. Below the first and fourth vessels a small gray tag reads \"undefined\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Five differently shaped measuring vessels partly filled with coins, each with its own scale; a person tries to compare them with one ruler.",
  "caption": "Five companies report five volume figures under five definitions, two of them undefined, so the figures cannot be ranked."
}
-->

## PayPal and Braintree: The Wallet Is the Asset

PayPal's filing opens its description of the business with a network, not a processor: "We operate a global, two-sided network at scale that connects consumers and merchants with 439 million active accounts across approximately 200 markets as of December 31, 2025." To merchants PayPal sells two different things, which the filing lists as "online branded checkout solutions, including PayPal and Venmo; online unbranded payments processing". Branded checkout is the button with the provider's name on it: the shopper pays from an account held with PayPal. Unbranded processing handles the merchant's own card form, and the shopper never sees who processed the card. That is what Stripe and Adyen sell. Braintree is PayPal's product of that kind; the filing names it without defining it, so the identification is general knowledge, not a quotation.

The $1.79 trillion therefore describes the whole company. The filing defines it: "TPV is the value of payments, net of payment reversals, successfully completed on our payments platform or enabled by PayPal via a partner payment solution, not including gateway-exclusive transactions." It covers the wallets and the processing together, and the filing gives no volume for Braintree alone. So the figure cannot tell you how large Braintree is, and it cannot be set beside Stripe's, which has no published definition.

The filing does say three things about Braintree. First, Braintree costs more to run: "The decrease in transaction expense rate in 2025 compared to 2024 was primarily attributable to a lower proportion of TPV from Braintree products and services, which generally have higher expense rates than other products and services, and changes in merchant mix." The transaction expense rate, transaction expense divided by volume, fell from 0.93% to 0.89%. Second, PayPal gave up Braintree volume on purpose, in the sentence quoted at the start of this chapter. Third, Braintree was repriced, not abandoned: the same sentence ends "followed by revenue and TPV growth in the second half of 2025", and over the year Braintree revenue rose by "approximately $150 million".

So a company that owns a consumer network and a processor reports that the processor is the expensive half. Stripe and Adyen own the processor. Stripe is also building the other half: its Sessions release of 29 April 2026 calls Link, the checkout that stores a shopper's payment details for reuse across Stripe merchants, a consumer wallet with over 250 million users (over 300 million by a release of 8 September 2026). Stripe does not define "users", so the figure cannot be compared with PayPal's 439 million. Adyen's annual report for 2025 describes no consumer wallet.

> **INFERENCE, NOT DOCUMENTED:** Stripe has not said why it promotes Link. I read it as a processor building the consumer side that PayPal started with, because a provider that knows the shopper can recognize them at any merchant's checkout, and a processor alone cannot. PayPal's filing supports the premise and says nothing about Stripe. It does not state Braintree's margin; "higher expense rates" is as far as it goes.

<!-- illustration-placeholder
{
  "id": "49-branded-and-unbranded",
  "status": "pending",
  "asset": "assets/images/49-contrast-cases/49-branded-and-unbranded.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the inference block of the PayPal section",
  "visual_goal": "Show the difference between branded checkout, where the shopper has an account with the provider, and unbranded processing, where the provider is invisible behind the merchant's card form.",
  "prompt": "Two-panel structural diagram with a thin vertical divider, panels tagged \"Branded\" on the left and \"Unbranded\" on the right. In both panels a shopper with a phone stands on the left and a small shop building labeled \"Merchant\" on the right. Left panel: on the phone screen a large teal button labeled \"Wallet\" is visible; a solid teal line labeled \"account\" runs from the shopper directly to a generic provider building at the top center; a green arrow labeled \"pays\" runs from the provider building down to the merchant. Right panel: on the phone screen a plain card form with four empty fields is visible; a green arrow labeled \"pays\" runs from the shopper to the merchant; behind the merchant, drawn in pale gray, stands the same generic provider building connected to the merchant by a thin gray pipe labeled \"processing\"; there is no line between the shopper and the provider. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two panels. In branded checkout the shopper has an account with the provider and pays through a wallet button; in unbranded processing the shopper fills in the merchant's card form and the provider stays behind the merchant.",
  "caption": "In branded checkout the shopper holds an account with the provider; in unbranded processing the provider stays out of sight behind the merchant's own card form."
}
-->

## Checkout.com: An Enterprise Acquirer Assembled Later

Where PayPal began with the shopper, Checkout.com began where Adyen did, with the large merchant. It is private, so the figures are its own. Its release of 24 February 2026 reports "processing over $300B in 2025", an "adjusted EBITDA margin exceeding 10%" (EBITDA is earnings before interest, taxes, depreciation and amortization) and "over 1,000 enterprise merchants". Its release of 29 September 2026 reports "$750m in annualised net revenue", "over 1,700 enterprise merchants" and that it "operates across 56 countries with 10 acquiring licenses". An acquirer is the licensed institution that signs the merchant and submits its card transactions to the card networks ([[acquiring-and-network-connectivity]]). The releases do not define "enterprise merchant", and the count rose from 1,000 to 1,700 in seven months, so treat it as a direction. They give no founding date; that the company is younger than Adyen, founded in 2006, is general knowledge.

The newest of those licenses links Checkout.com to Stripe. On 9 September 2026 it announced "the launch of direct acquiring in the US under its Merchant Acquirer Limited Purpose Bank (MALPB) charter in Georgia", adding that the charter "will enable direct access to card networks, reduce reliance on third-party intermediaries". Without such a charter a non-bank processor in the United States commonly works under a sponsor bank, a card-network member that lends its membership. Stripe holds the same kind of charter, and the regulator dates both. The 2026 bulletins of Georgia's Department of Banking and Finance list Stripe MALPB as approved on 30 June 2025 and in business since 28 May 2026, and Checkout.com MALPB as approved on 15 September 2025 and in business since 16 July 2026, eight weeks before the company's announcement. Stripe's acquirer disclosure (n.d., accessed November 2026) lists "Stripe MALPB, 505 N Angier Avenue NE, Atlanta" among its US acquirers, next to five banks. The charter is narrow: according to the Independent Community Bankers of America, a trade association (8 July 2025, a secondary source), such a bank "may not solicit or accept deposits from the general public".

The case shows two things about the anchors. Owning the acquiring is not Adyen's bet alone: a provider that serves enterprises assembles it one license and one market at a time, and Stripe, which began elsewhere, is doing the same ([[stripe-and-adyen-bets-compared]]). And an enterprise that wants a second acquirer beside Adyen has one that sells the same proposition. Adyen expects this. The risk section of its annual report for 2025 says: "Large enterprise merchants typically work with multiple payment service providers to mitigate their own single-point-of-failure risk."

> **INFERENCE, NOT DOCUMENTED:** Adyen reports an EBITDA margin of 53% for 2025 and Checkout.com an adjusted margin "exceeding 10%". The two measures are not shown to be defined alike. I read the gap as two decades of volume on licenses and a platform Adyen already owns, not as evidence about either design. In the February release Checkout.com's chief executive credits "a single, unified infrastructure"; that is a claim in a press release, and I read no engineering source that would let me test it. Nor could I confirm from a first-party source where Checkout.com hosts its systems, so I assert nothing about it.

## Block: The Till First, Then a Bank

The first two companies sell to merchants that employ engineers. Block's Square sells to a shopkeeper who wants a till that takes cards. Its filing for 2025 describes the product as a bundle: "Square's commerce enablement products include our payments, software, and hardware products, which together provide an integrated operating system for local commerce." The hardware is its own ("Square Hardware is custom-designed"), and toward the card networks Square stands in the seller's place: "Square acts as both the merchant of record and payment service provider, settling funds with sellers and managing associated payment-related risk." A merchant of record is the party that is the seller as far as the card networks are concerned ([[merchant-of-record]]). In 2025 "more than 4.5 million sellers used the Square ecosystem to make 5.9 billion individual sales transactions totaling $250 billion of Square GPV".

Block owns the till and the seller relationship, but not its connection to the card networks. The filing's risk section says: "For a majority of our transactions, we do not directly access the payment card networks that enable our acceptance of payment cards. As a result, we must rely on banks and acquiring processors to process transactions on our behalf." It rents the layer that Adyen made its starting point.

What Block does own is a bank, of a third kind. "On March 1, 2021, Square Financial Services received its deposit insurance from the FDIC and charter approval from the Utah Department of Financial Institutions and became operational", the filing says; the FDIC is the US federal deposit insurer. Square Financial Services is a Utah industrial loan company: a state-chartered, insured bank that a commercial company may own. The filing says what it is for. "Square Loans facilitates loans to qualified Square sellers through Square Financial Services. We are able to underwrite these loans by using our unique data set of the seller's Square transactions", and "loan repayment occurs automatically through a fixed percentage of every card transaction a seller takes". It also holds sellers' savings. The bank serves the seller relationship; the acquiring stays rented.

> **INFERENCE, NOT DOCUMENTED:** Three charters in this part do three different jobs. Adyen's banking licenses let it hold funds and acquire ([[licences-and-safeguarding]]). Georgia's charter lets Stripe and Checkout.com acquire and take no deposits. Utah's lets Block lend and take deposits while others acquire for it. I read each as the permission the company's first customers made necessary; no filing says so. The same holds for hardware: Adyen's update for the third quarter of 2026 reports 878 thousand transacting terminals across its platform, and Stripe's documentation (n.d., accessed November 2026) describes its Terminal product as card readers that a developer drives through software kits or the API ([[in-person-payments]]). Neither is a till sold to a shopkeeper.

## What the Three Cases Add to the Comparison

Taken one by one, each case gave one lesson. The table sets them side by side with the evidence and with how far each carries into a decision of your own. Its last row also yields the one question these cases add to a provider comparison: who owns the relationship with the payer, and who with the seller?

| Lesson | Evidence | Transfers? |
| --- | --- | --- |
| The consumer network is the asset; card processing is the costlier part to run. | PayPal 10-K for 2025: 439 million accounts; Braintree's "higher expense rates". | Partly. It tells you to ask who knows the payer. It says nothing about Braintree's quality or reliability. |
| Own acquiring is assembled market by market by any provider that serves enterprises. | Checkout.com releases (2026): ten licenses. Georgia regulator's bulletins (2026). Stripe's acquirer disclosure. | Yes, as a question: which entity acquires in each country you sell in? |
| A bank charter says nothing about acquiring. | Block 10-K for 2025: acquiring processors for "a majority of our transactions"; a Utah industrial loan company for lending. | Yes, as a question: what does this charter permit? |
| A volume figure means what its definition says. | All five companies; two give no definition. | Yes, fully. |
| What a provider holds follows its first customer. | My inference from three cases and the two anchors. | As a hypothesis to test, and as one new row for your comparison: who owns the payer, and who the seller? |

The last row needs stating with care. Line the five companies up by the customer each served first. The shopper came first for PayPal, which holds accounts and a wallet. The enterprise came first for Adyen, from 2006, and for Checkout.com after it; both hold acquiring licenses. The developer came first for Stripe, which holds an API and then assembled licenses and named acquirers market by market ([[case-stripe]]). The shopkeeper came first for Block, which holds hardware, software and a lending bank. **On this reading Stripe and Adyen are two starting points among several, not the two ends of one line.** The reading is mine. Three cases chosen because they contrast cannot prove it, and a provider whose first license had nothing to do with its first customers would count against it. It also concerns where permissions came from, not whom a provider can serve today: Stripe and Adyen each now sell to the other's first customers.

Fill that row in for Larkfield, beside the rows of the previous chapter. Larkfield owns both. The studio is its customer through the scheduling software, and the member is known to it through the booking app. Stripe and Adyen, which carried 44% and 56% of its 2026 volume, own neither. That is the position of a software-first company such as Square, without the bank: Larkfield holds no license ([[licences-and-safeguarding]]). Owning both relationships is what made decision K8 possible, under which the payment service can move a studio's online card payments to the other provider. What Larkfield does not hold is the stored cards, which stay with the provider that stored them ([[payment-routing-and-orchestration]]).

<!-- illustration-placeholder
{
  "id": "49-first-customer-what-is-held",
  "status": "pending",
  "asset": "assets/images/49-contrast-cases/49-first-customer-what-is-held.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the Larkfield paragraph of the cross-case section",
  "visual_goal": "Show four starting customers side by side and, above each, what a provider that started there came to hold.",
  "prompt": "Structural diagram with four equal columns separated by thin dividers. At the bottom of each column stands one figure on a small platform with a tag: a shopper with a phone tagged \"Shopper\", a tall office tower with a person in a suit tagged \"Enterprise\", a person at a laptop tagged \"Developer\", and a shopkeeper in an apron behind a counter tagged \"Shopkeeper\". From each figure a green upward arrow rises to an object in the upper half of the column: above the shopper a large teal wallet icon tagged \"Wallet\"; above the enterprise a stack of blue certificate documents with seals tagged \"Licenses\"; above the developer a code window with curly brackets tagged \"API\"; above the shopkeeper a countertop card reader beside a small bank building tagged \"Till + bank\". A thin horizontal orange dashed line runs across the top of all four columns with no endpoints marked, suggesting they are not points on one line. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Four columns: a shopper below a wallet, an enterprise below a stack of licenses, a developer below an API window, a shopkeeper below a card reader and a small bank.",
  "caption": "Four first customers and what a provider that started with each came to hold: a wallet, acquiring licenses, an API, a till and a bank. The pairing is the author's inference."
}
-->

## Where the Evidence Stops

The cases support a contrast of business models. Six things they might be taken to show are not in the documents I read.

- **How these companies are built.** PayPal's and Checkout.com's engineering blogs exist and were not read, so nothing here bears on their reliability, data stores or APIs.
- **Braintree's size and margin.** The filing gives no Braintree volume and no Braintree margin, only the direction of its volume and its relative expense rate. Fastlane, a guest card checkout in PayPal's developer documentation (n.d., accessed November 2026), does not appear in the filing.
- **What Checkout.com's figures count.** Its volume, its "enterprise merchant" and its adjusted margin are undefined and unaudited.
- **How much runs through the Georgia charters.** Neither Stripe nor Checkout.com states the share of US volume its limited-purpose bank acquires, and the regulator's bulletins give dates, not volumes.
- **Whose acquiring Block uses.** The filing names no acquiring processor and no share beyond "a majority of our transactions".
- **Whether the inference holds beyond these cases.** I chose three companies because they contrast; a wider sample might find exceptions.

## What to Take Away

**Established.**

- PayPal's filing for 2025 defines its $1.79 trillion as company-wide volume, and says Braintree products "generally have higher expense rates".
- Checkout.com states that it holds ten acquiring licenses. Georgia's regulator lists its bank as in business since 16 July 2026 and Stripe's bank of the same kind since 28 May 2026.
- Block's filing says it relies on banks and acquiring processors for a majority of its transactions and owns a Utah industrial loan company.
- The five volume figures in this chapter have five definitions, two of them unpublished.

**Depends on context.**

- Which case to read depends on your choice: a wallet at checkout, PayPal; a second acquirer for a large merchant, Checkout.com; a till for many small sellers, Block.
- Whether a provider's charter matters depends on what you need it for: holding your funds, acquiring your cards or lending to your sellers. A charter for one may not permit the others.

**The author's synthesis.**

- I place a provider by the customer it started with, not on a line from Stripe to Adyen, and I compare providers by who owns the payer and who owns the seller. It is a hypothesis from three cases.
- The two near-equal volumes at the start of this chapter were never a race. One counts a wallet network and its processing together, the other is undefined, and the company behind the first chose to shed processing volume.

## Questions to Ask

1. For any volume figure a provider quotes: does it include wallets, refunds, reversals and gateway-only transactions, and is it audited?
2. Who holds an account with your payer: you, the provider, a wallet or nobody?
3. In each country you sell in, which legal entity is the acquirer, and under which license or charter?
4. When a provider says it is a bank, what does that charter permit: deposits, acquiring, lending?
5. Does the provider own its acquiring in your market, or does it depend on a sponsor bank or an acquiring processor?
6. If you copy a provider's product shape, do you also have the customer relationship that made that shape pay?
7. Which of the provider's claims about itself come from an audited filing, and which from a press release?

These are the positions as they stood in November 2026: two anchors that started at different ends and are converging, and three others whose first customer explains what each holds. [[payments-what-is-moving]] turns to what is changing under all five as this book goes to press: agents that pay, stablecoin settlement, instant account-to-account payments and new EU rules, each with its date and release phase. For a company that built payments in-house instead of buying them from any of these five, see the sibling book's [[case-uber-payments]].

## Sources and Evidence

*Company, product and investor sources*

- [The PayPal Technology Blog](https://medium.com/paypal-tech), PayPal, n.d., accessed 2026-11 — first-party engineering writing exists; not read for this chapter.
- [How we build at Checkout.com](https://www.checkout.com/blog/how-we-build-at-checkout-com), Checkout.com blog, 2026-03-19 — first-party engineering writing exists; not read for this chapter.
- [PayPal Holdings, Inc., Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm), PayPal, filed 2026-02-03 — the two-sided network and 439 million active accounts, TPV and its definition, branded and unbranded products, the Braintree statements, the transaction expense rate.
- [Block, Inc., Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1512673/000162828026012254/xyz-20251231.htm), Block, filed 2026-02-26 — Square GPV and its definition, the integrated till and custom hardware, Square as merchant of record, reliance on banks and acquiring processors, Square Financial Services and Square Loans.
- [Checkout.com returns to full-year profitability and surpasses $300B in volume](https://www.checkout.com/newsroom/checkout-com-returns-to-full-year-profitability-and-surpasses-300b-in-volume-as-it-positions-for-the-era-of-agentic-commerce), Checkout.com, 2026-02-24 — 2025 volume, adjusted EBITDA margin, enterprise merchants, the chief executive's statement (private company's own figures).
- [Checkout.com goes live with US direct acquiring under MALPB charter](https://www.checkout.com/newsroom/checkout-com-goes-live-with-us-direct-acquiring-under-malpb-charter), Checkout.com, 2026-09-09 — the Georgia charter in operation.
- [Checkout.com reaches $750m in annualised net revenue for 2026 and increases profitability](https://www.checkout.com/newsroom/checkout-com-reaches-750m-in-annualised-net-revenue-for-2026-and-increases-profitability), Checkout.com, 2026-09-29 — net revenue, enterprise merchants, 56 countries and ten acquiring licenses (private company's own figures).
- [Acquirer Disclosure](https://stripe.com/en-us/legal/acquirer-disclosure), Stripe, n.d., accessed 2026-11 — Stripe MALPB among the six US acquirers of which Stripe, LLC is a payment facilitator (volatile).
- [Stripe publishes 2025 annual letter](https://stripe.com/newsroom/news/stripe-2025-update), Stripe newsroom, 2026-02-24 — "$1.9 trillion in total volume", undefined.
- [Stripe's 2025 annual letter](https://stripe.com/annual-updates/2025), Patrick and John Collison, Stripe, 2026-02-24 — businesses on Stripe "generated $1.9 trillion"; no definition of the figure.
- [Stripe Sessions 2026 announcements](https://stripe.com/newsroom/news/sessions-2026), Stripe newsroom, 2026-04-29 — Link described as a consumer wallet with over 250 million users (undefined).
- [Stripe helps Muse, Meta's new personal AI agent, shop across the internet with Link](https://stripe.com/newsroom/news/stripe-helps-meta-muse-shop-with-link), Stripe newsroom, 2026-09-08 — Link described as a consumer network with over 300 million users (undefined).
- [Fastlane by PayPal](https://developer.paypal.com/studio/checkout/fastlane), PayPal developer documentation, n.d., accessed 2026-11 — Fastlane as a guest card checkout product.
- [Set up your integration: server-driven](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), Stripe documentation, n.d., accessed 2026-11 — Terminal readers driven through SDKs or the API.
- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., signed 2026-03-05 — processed volume, full-stack share, EBITDA margin, the risk-section sentence on multiple providers.
- [Q3 2026 Business Update](https://investors.adyen.com/financials/q3-2026-10c88s), Adyen N.V., 2026-10-28 — 878 thousand transacting terminals.

*Standards, regulation and official documentation*

- [Financial Institutions Today, monthly bulletins for 2026](https://dbf.georgia.gov/financial-institutions-bulletin-2026), Georgia Department of Banking and Finance, May 2026 and July 2026 issues — Stripe MALPB approved 30 June 2025 and in business since 28 May 2026; Checkout.com MALPB approved 15 September 2025 and in business since 16 July 2026.

*Research and practitioner sources*

- [Georgia approves Stripe application to form MALPB](https://www.icba.org/w/georgia-approves-stripe-application-to-form-malpb), Independent Community Bankers of America, 2025-07-08 — the scope of the charter (secondary source).

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
