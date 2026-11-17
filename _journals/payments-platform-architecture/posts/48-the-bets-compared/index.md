---
title: "Two Ways to Build It: The Architectural Bets Compared"
date: 2026-11-17
author: Željko Obrenović
excerpt: "On which architectural bets do Stripe and Adyen demonstrably differ in November 2026, and what should a customer do with each difference? Two differences are of kind (who holds the money, who runs the machines); the rest are defaults, sequences and degrees that narrowed in 2025 and 2026, so the choice is made bet by bet and country by country."
permalink: stripe-and-adyen-bets-compared
timetoread: 28 min read
---

> **IN THIS CHAPTER, YOU WILL:** Sort the documented differences between Stripe and Adyen into three kinds, and learn what a customer choosing or combining them does with each.

> **KEY POINTS:**
>
> * **Two differences are of kind.** Adyen is a licensed bank and runs its own infrastructure in data centers; Stripe says it is not a bank and runs on Amazon Web Services. Both document both facts, and neither changed in 2025 or 2026.
> * **The rest are differences of default, sequence or degree, and they narrowed.** Stripe's own companies acquire card payments in Europe; Adyen reports 84% of its volume as full-stack; Adyen bought a billing company in 2026; each sells both pricing models.
> * **Decide per bet and per country, with a date on every row.** For a difference of kind, find out which entity holds your funds. For a default, ask for the alternative. Where the record is silent, ask in writing.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Borrowed Blueprint** — "the bank" and "the developer's API" are chosen as brands without the dated reasons behind either.
> * **The Black-Box Balance** — a balance is a claim on a different regulated entity at each provider and in each country, and a team that chose by slogan has not looked up which.
> * **The Single Rail** — a provider picked for its reputation is rarely compared again, so nobody notices when the rows that justified it change.

<br>
Two sentences are said in most provider evaluations. One is commercial: "Stripe is for startups, Adyen is for enterprises." The other is the engineer's version: "Adyen owns the stack, Stripe rents it." Each meets a dated line from the companies themselves that it cannot explain. Stripe's acquirer disclosure (n.d., accessed November 2026) says, for the European Economic Area (EEA): "Payment Method Acquirer is Stripe Technology Europe, Ltd." The acquirer is the card-network member that submits a merchant's payments and receives the money for them; in Europe Stripe rents that position from nobody. And Adyen's update for the third quarter of 2026 says its Platforms offering "allows us to provide payments and financial products to smaller merchants, which will be a key driver of future growth."

The earlier parts of this book ended each chapter with a table, "Stripe and Adyen: Where They Differ": forty-one tables and about 250 rows, with nothing to say which rows should decide a choice. Sorted by their evidence, the rows reduce to eight bets of three kinds. **Two bets are differences of kind** that both records document: who holds the money and who runs the machines. **The others are differences of default, sequence or degree** that narrowed in 2025 and 2026, and one of them, "one platform against a suite", sets an engineering statement beside a packaging statement. Some questions the public record cannot decide. A customer should treat each kind differently, and decide on neither slogan.

This chapter adds no new fact. Every statement about either company comes from the chapter that owns it, linked, with that chapter's dates, hedges and "Not public" cells, and every reason for a difference sits in a block marked INFERENCE, NOT DOCUMENTED.

**Where we are in the payment's journey.** Mila Janssen's ten-class pass (€120.00, Tuesday 9 March 2027) ran through Adyen because Studio Noord is on Adyen. Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]), put 56% of its 2026 member payment volume (€627 million) through Adyen and 44% (€493 million) through Stripe, and 1,140 of its Dutch and German studios still take online payments on Stripe. There the same pass would have met a different acquirer of record, another payout clock and another way to read the payment's state: the differences this chapter sorts.

The chapter opens at Larkfield, where the chief executive asks which provider to keep. It defines the three kinds of difference and compares eight bets in a fixed order: license and money-holding; acquiring; build or buy; one platform or a suite; first customers, with the pricing and the API model they left behind; hosting; billing and revenue products; and platforms. Each gets the documented difference, a reason as labeled inference, what is not public, and what a customer does. One map then gathers the bets, and a decision aid, worked through for Larkfield, ends the chapter.

## Larkfield's Question: Which Provider Do We Keep?

In October 2027, planning for 2028, Sofie Vermeer, Larkfield's chief executive, asks a fair question. Larkfield has used Stripe since 2017 and Adyen since 2024. Its payments team of 11 keeps two adapters, two webhook receivers and two reconciliation runs alive, and every quarter it rehearses moving its 50 largest studios' online card payments between the providers (decision K8 of its Keel program). Which provider should it keep? Daniel Osei, the chief technology officer, answers from memory: "Adyen is the bank and owns the stack. Stripe is an API on other people's banks. And we are not a startup any more."

Femke de Graaf, who leads payments engineering, answers with a card instead of a sentence. It is the provider comparison card from the [[toolkit]]: one row per bet and, where needed, per country, each cell a dated fact with its source or the words "Not public". This chapter fills that card, for the two companies and then for Larkfield.

## Three Kinds of Difference, Sorted by Evidence

Before a row goes on the card, three tests sort it. If both companies document a structural fact and the two facts differ in type, it is a **difference of kind**: a bank is not an e-money institution. If the facts are of the same type and differ in amount, order or default, it is a **difference of default, sequence or degree**: both acquire card payments, in different places; both own a usage-billing product, since different dates. If at least one company has published nothing, the question is **not decidable from the public record**. There the cell says "Not public": not found in the company's documentation, help center, site or filings by 17 November 2026, which does not prove absence. A reason for a difference is an inference unless the company gave it. The figure below shows the sorting.

<!-- illustration-placeholder
{
  "id": "48-three-kinds-of-difference",
  "status": "pending",
  "asset": "assets/images/48-the-bets-compared/48-three-kinds-of-difference.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that defines the three kinds of difference",
  "visual_goal": "Show claims about two providers being sorted by evidence into three trays instead of being accepted as slogans.",
  "prompt": "Conceptual sorting scene, read left to right. Left: two speech bubbles without text, one blue and one teal, drifting toward a small sorting desk; each bubble carries a tiny megaphone icon to suggest a slogan. Center: a generic analyst at a desk holding a magnifying glass over a document card with a small calendar icon on it; a short arrow labeled \"check the date\" runs from the bubbles to the document. Right: three open trays in a row on a shelf, each fed by its own arrow from the desk. The first tray is green, labeled \"Kind\", and holds two clearly different solid shapes, a square and a circle. The second tray is orange, labeled \"Degree\", and holds two bars of the same shape and different heights. The third tray is gray, labeled \"Not public\", and holds one card with a question mark beside an empty outline. The three arrows are labeled \"both documented\", \"same type\" and \"silent\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two slogan bubbles pass a desk where a document is checked for its date and are sorted into three trays labeled Kind, Degree and Not public.",
  "caption": "Every claimed difference is sorted by its evidence before it is used: a difference of kind when both companies document a structural fact, a difference of degree when the facts are of the same type, and not public when the record is silent."
}
-->

## Who Holds the Money: A Bank and a Non-Bank

The first bet to sort is the regulated form. Adyen N.V. "is authorised as a credit Institution under the supervision of Dutch Central Bank" (license page, n.d., accessed November 2026). A credit institution is a bank: it may take deposits and lend. Adyen dates the license to 2017 and operates a federal branch in the United States (2021) and a branch authorized as a bank in the United Kingdom (2023): one bank with two branches ([[case-adyen]]). Stripe holds permissions function by function. Its Irish and UK companies are e-money institutions, licensed non-banks that may hold customers' balances only apart from their own funds, in accounts at banks, which is called safeguarding. In the United States a Stripe company is "a U.S. state-licensed money transmitter" (terms updated November 2025), and Stripe's treasury documentation (n.d., accessed November 2026) says: "Stripe is not a bank. Checking accounts are provided exclusively by Fifth Third Bank, National Association, Member FDIC." [[licences-and-safeguarding]] owns the law and [[case-stripe]] the entities.

A customer sees the form in three places. The first is where balances sit. Stripe documents safeguarding accounts at credit institutions it does not name (European Union and United Kingdom; a 2024 FAQ). Adyen documents that deposits in its business accounts are held at Adyen N.V. under the Dutch deposit guarantee, and its terms (2023) say balances waiting for payout are "held by Adyen prior to Settlement"; at which banks is not public. The second is the payout, the transfer of collected money to a merchant's bank account. Under Adyen's Sales Day Payout terms (17 June 2024) Adyen pays "irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner", and its documentation caps this pre-financing at 30 days. Stripe documents paying ahead only for Instant Payouts; for standard payouts its services terms (28 September 2026) count "a delay or failure of a Financial Provider to settle a Transaction to Stripe" as a "Payout Delay" and state no pre-financing ([[clearing-and-settlement]]). One caveat: Adyen's Annual Report 2025 calls paying "only after funds have been received" its "default setup", and the two statements cannot be reconciled from public text ([[balances-and-funds-flows]]). The third is lending. Behind Stripe's financial products stand partner banks and outside lenders; at Adyen the lender is Adyen ([[embedded-finance]]).

Yet the gap is narrower than "a bank against software". Stripe's European companies are regulated in their own right. Stripe also owns a bank of a narrow kind: the Georgia regulator's bulletin of May 2026 gives 30 June 2025 as the approval date of its Merchant Acquirer Limited Purpose Bank and 28 May 2026 as the day it began business. In February 2026 the US regulator of national banks gave Stripe's Bridge subsidiary "preliminary conditional approval" for a trust bank, which holds assets for others; no final approval was found. Neither charter takes deposits: a banking trade association's news item of July 2025 (a secondary source) says such Georgia banks "may not solicit or accept deposits from the general public". The difference of kind stands.

> **INFERENCE, NOT DOCUMENTED:** Read together, the pages suggest that Stripe took the smallest permission sufficient for each market and function, and that Adyen took the widest permission once and reuses it. Adyen gives a reason: "the speed and autonomy that come from not relying on external parties for regulatory compliance" (Annual Report 2025). Stripe has published none, so motives can be compared from one side only.

This difference is established, not negotiated, and two facts behind it are not public: the banks that hold Stripe's safeguarded funds, and how Adyen's merchant balances are split between central and commercial banks. For each country you sell in, write down which entity holds your funds or your sellers' funds, under which license and protection, and whether your payout is paid before the network has paid.

## Who Acquires: A Difference of Degree, Country by Country

Unlike banking, acquiring is something both companies do under their own licenses in some markets and not in others. Stripe's disclosure (n.d., re-read on 17 November 2026) names a Stripe company as the acquirer in the EEA, the United Kingdom, Brazil and much of Asia-Pacific. In the United States "Stripe, LLC is a Payment Facilitator of" six acquirers, five banks and its own Georgia bank; a payment facilitator signs up merchants under an acquirer's network membership. The page also names acquirers in Canada, Japan (card companies), India, Thailand and the United Arab Emirates; in Mexico Stripe is both acquirer and facilitator. Adyen's Annual Report 2025 says: "Of processed volumes, 84% were full-stack volumes". Its documentation (n.d., accessed November 2026) lists 14 countries and regions with an "Adyen acquiring connection", and the report places concentration risk (exposure to one counterparty) "primarily at banking partners in locations where there are no own direct acquiring licenses". Adyen's license pages name an acquiring entity for some markets (Adyen Japan KK, Adyen Singapore); no page lists the entity per country ([[acquiring-and-network-connectivity]], [[case-adyen]]).

It follows that "Adyen acquires itself and Stripe uses sponsors" is, as [[case-stripe]] puts it, wrong for Europe and roughly right for the United States. What differs most is what each publishes: Stripe the legal entity per country, Adyen the coverage and the size of its own share. Adyen's own acquiring also bounds some of its features. Its network tokenization (a network token is a card-network stand-in for the card number) is "only applicable for payments acquired by Adyen" ([[network-tokens]]), and it documents payments settled by an external acquirer, such as a merchant's own American Express agreement ([[payment-routing-and-orchestration]]).

> **INFERENCE, NOT DOCUMENTED:** Stripe's per-country list probably exists because, where Stripe is a payment facilitator, the bank is a party to the merchant's contract and has to be named. Reading "full-stack" as volume that Adyen also acquires, and its sentence about banking partners as a statement about acquiring, are my readings; the report defines neither. Neither company gives these reasons.

The record stops in the same places for both. Neither publishes volume per acquirer: Stripe gives no shares for its six US acquirers and does not say which merchants its Georgia bank acquires for, and Adyen's 84% has no breakdown. Both state network membership in general terms, Adyen as "principal membership of Visa and Mastercard in major markets" (3 July 2026); neither lists networks and countries. So read Stripe's disclosure for every country you sell in and record the acquirer with the date; the list changes. Ask Adyen in writing, per country: an Adyen entity, or a banking partner?

## Build or Buy: A Difference of Sequence That Narrowed in 2026

The third bet, like acquiring, looks like a difference of kind and is not. [[case-stripe]] lists ten named purchases since 2020, from Paystack to Parafin; two of them, OpenRouter and Parafin, were announced and not confirmed closed on 17 November 2026. Adyen's 2025 annual report describes "a single platform built entirely in-house". Then, on 1 July 2026, Adyen closed the purchases of Talon.One, a loyalty platform, and Orb, a usage-billing platform; its history page lists no acquisition before them ([[case-adyen]]). That Adyen builds and never buys is said in no Adyen document read for this book.

Underneath the two lists the companies are alike: [[payment-safe-change]] finds that both build their core systems in-house or on open source. What differs now is the state of the join between what was bought and what was built. Stripe documents Metronome, a purchase completed in January 2026, as a product path beside its own ([[usage-metering-and-rating]]), and Lemon Squeezy, bought in 2024, stops processing payments on 31 March 2027, while Stripe's own product for the same role has been in its API since April 2026 ([[merchant-of-record]]). Adyen said in June 2026 that it runs Orb under "an incubator model", and its release of 28 October 2026 speaks of "the successful ongoing integration of Talon.One and Orb" without saying what is shared.

> **INFERENCE, NOT DOCUMENTED:** Stripe's purchases fill gaps near the payment, and Lemon Squeezy suggests that a bought product may be replaced and not merged. Adyen's purchases follow its move toward smaller merchants, who lack the systems its first customers had. Adyen's stated reason for buying Orb is quoted in [[case-adyen]]; Stripe has described no strategy.

How either company joins a bought product to a built one is not public, and Adyen gives no date for the "convergence" it states as its intent. For every product you use, ask whether it was built or bought, when, and what it shares with payments today: credentials, identifiers, events, reports. Then test that join.

## One Platform or a Suite: Two Statements About Different Things

The first three bets compare like with like; the fourth, the one most often put first, does not. Adyen's phrase is a claim about operation. Its annual report calls "our single global platform" the first step of its strategy, so that any improvement "takes effect everywhere, without reintegration work"; [[case-adyen]] reads this as one place where a change is made, not one interface. Stripe's "suite" is a claim about packaging: products with their own names and prices, such as the "Revenue and Finance Automation Suite, with Billing at its core" of its 2024 letter ([[case-stripe]]).

From the integrator's side, by contrast, the two nearly cross. Adyen's one platform is reached through several API families, each with its own version counter and, in most cases, its own host; Stripe's suite is reached through one host and one object model ([[payment-api-design]]). And Stripe sells layers that can sit over other providers' processing. Its Orchestration product, in private preview on 17 November 2026, routes card payments to Adyen, Braintree and Worldpay, and Jon Krauss of Stripe said at the company's conference in April 2026: "You're not going to have to be locked into Stripe." Adyen's product page (n.d., accessed November 2026) argues the opposite: "Unlike fragmented legacy architectures, Adyen brings payments onto one single platform" ([[payment-routing-and-orchestration]]). Even here the two approach: Orb goes on "continuing to support multi-PSP environments", serving customers of other payment providers.

> **INFERENCE, NOT DOCUMENTED:** Stripe sells checkout, billing, fraud screening and a card vault as products that can sit above another company's processing, so holding that layer may be worth more to it than carrying every authorization. Adyen's argument rests on carrying the payment itself. Neither company has said this.

Neither side of this row can be checked against the other. Stripe's engineers describe one repository of about 50 million lines of Ruby (April 2026); no post found says which products, built or bought, live in it. Adyen counts "around 3,000 live services" (2026) and has not said what its bought products share with the platform. Do not score this row; test each pair of products you will use together.

## First Customers and Today's Defaults

Behind the commercial slogan is a documented fact about beginnings. Stripe's 2022 letter says "Stripe grew up with companies in the technology sector" **(Evidence age: 3.5 years.)**, and its February 2026 release still says "the 'long tail' is much of the dog". Adyen's history page (n.d., accessed November 2026) says: "Built for enterprise, not adapted to it." One channel is reported by one side only: Adyen gives point-of-sale volume of €310.9 billion for 2025, 22% of its processed volume, and Stripe, which has sold terminals since 2018, publishes no in-person figure ([[in-person-payments]]). But the same records show each company selling to the other's first customers. Stripe wrote in March 2023 that its "enterprise user base has compounded since 2019" **(Evidence age: 3.5 years.)** Adyen counted 312,000 active business customers behind its platform customers in the third quarter of 2026. What remains of each starting point, by my reading (labeled below), is a set of defaults.

The first default is the price. Interchange is the fee paid to the bank that issued the card. Stripe's price list (Netherlands edition, n.d., accessed November 2026) leads with a blended rate, one price whatever the card costs: 1.5% + €0.25 for standard EEA cards. Interchange-plus, which passes interchange and the network's fee through with a visible markup, is among its custom options as "IC+ pricing". Adyen's list (n.d., accessed November 2026) is the reverse: a fixed processing fee plus a fee per payment method, card costs passed through under the name Interchange++, and the note "The fees outlined above are indicative". Its October 2026 update describes a "tiered pricing structure", and its platform documentation has a fee type for blended rates. In the words of [[payment-economics]], each sells both models; only the default differs. Negotiated markups are not public at either.

The second default is the API and the way it is operated. The earlier parts documented these one by one, from documentation accessed in November 2026; an idempotency key, in the second row, is the identifier by which a provider recognizes a repeated request. One convergence belongs beside the table: both now recommend a server-created session as the entry point.

| Default | Stripe | Adyen | Owning chapter |
| --- | --- | --- | --- |
| Reading a payment's state | A PaymentIntent with a `status`, retrievable by its ID | A result code per response, then webhooks; the Checkout API (v72) has no operation that returns an online payment by identifier | [[payment-state-machines]] |
| Idempotency key kept | At least 24 hours (API v1); 30 days (v2) | 7 to 14 days | [[idempotency-and-retries]] |
| API version | Account default, header or SDK release; one dated version | An integer in the URL of each API; no default | [[payment-api-versioning]] |
| Rate limit for payment requests | Published: 100 a second per live account | None published; HTTP 429 documented | [[payment-developer-platform]] |
| Webhook retries | Up to three days | Up to 30 days | [[payment-webhooks-and-events]] |
| Switching things on | Payment methods in the dashboard, "generally instantaneous"; invoice retries on by default for new accounts | Methods on request in the Customer Area; Auto Rescue off until support enables it | [[local-payment-methods]], [[invoicing-collections-and-dunning]] |
| When funds become payable | Per transaction, at `available_on` | Per sales day, as one batch | [[balances-and-funds-flows]] |

Where these defaults came from is my inference (the block below); what matters is that a default can be asked about. Two things cannot be read anywhere: realized prices, and an independent measure of approval rates, since each company's published uplift uses its own metric and cohort ([[authorization-optimization]]). So compare the default you will live with and ask for the alternative in writing. On Adyen, get the markup, the minimum invoice and the chargeback fee in writing: the listed fees are indicative, and the other two are published for one market each. On both, measure acceptance on your own traffic.

> **INFERENCE, NOT DOCUMENTED:** These defaults fit each company's first customers. A re-readable API with published limits, instant activation and one blended price suits a developer integrating without an account team. Features enabled on request, explicit versions, longer retry windows and an itemized price suit a customer with an account manager and a finance team. Neither company says so, and it is a statement about where the defaults came from, not about who should choose which company today.

## Who Runs the Machines: Own Infrastructure and a Public Cloud

A pricing default can be changed by asking; the second difference of kind cannot. Adyen's 2021 engineering post says: "We manage our own infrastructure in several data centers around the world" **(Evidence age: 5 years; confirmed by the sources that follow.)** Its Infrastructure page (n.d., accessed November 2026) names data centers "in Europe, the United States, India, Singapore, Japan and Australia", without cities or operators, and its annual report says "The majority of our CapEx is related to our data centers": €116.8 million in 2025, 5% of net revenue. Stripe wrote in January 2023 that it "has long relied on AWS to provide the core compute infrastructure on which Stripe is built" (AWS is Amazon Web Services), and quoted its then chief technology officer: "We couldn't run without AWS—and we wouldn't want to". **(Evidence age: almost 4 years; an October 2024 AWS post written with Stripe staff is consistent with it.)** Stripe names no AWS region. [[payment-multi-region-and-data-residency]] calls this the clearest documented architectural difference between the two.

An integrator meets the difference in three places. Region is a setting on Adyen, which documents five live regions for online payments, and is absent on Stripe, which has one base URL. On data, Adyen states that payments are "stored in Europe and our isolated India environment"; Stripe states no storage location, and neither promises that data stays in the European Union. On capacity, Adyen buys ahead: its documentation gives utilization as "generally less than 30%" and freezes code deployment around named peak days, and in 2026 it pulled investment forward "to secure compute and storage availability". Stripe rents, and no freeze for Black Friday was found in its documentation, support site or newsroom ([[payment-peak-load]]).

> **INFERENCE, NOT DOCUMENTED:** I read the difference as one of lead time: provisioning time on one side, purchase lead time on the other, with Adyen paying for capacity before the volume arrives. Adyen's stated reasons for not using a public cloud are "part historical, part legal, and part technical" (2021). Stripe gives none beyond "we wouldn't want to".

Neither design is public. Adyen says its load balancers "manage the failover to the other data centers" and gives no topology or timings; for Stripe's payments nothing on failover was found, though a 2025 post describes two regions with failover for billing usage events. The availability figures each company reports form no comparable series, and only Adyen's public terms carry a commitment, 99.9% a quarter by "commercially reasonable efforts" ([[payment-reliability-and-availability]]). So record each provider's hosting dependency, check residency as a setting on Adyen and ask for it in the contract on Stripe, and rest no plan on either provider's failover.

## Billing and Revenue Products: Built from 2018, Bought in 2026

Hosting cannot change for a customer; the seventh bet changed in 2026. Stripe launched Billing in April 2018 and has held the subscription and its invoice since: "Stripe generates an invoice for every subscription billing period" ([[subscriptions-and-billing-engines]]). It added tax calculation and revenue recognition in 2021. Since 22 April 2026 a release version of its API carries Managed Payments, in which Stripe's company is the merchant of record, the party that sells to the customer in its own name, for digital goods ([[merchant-of-record]]). In Adyen's documentation a subscription is a processing model on a payment the merchant initiates. The owning chapters found no invoice object and no first-party tax engine or revenue-recognition product in Adyen's documentation, help center or site as of November 2026 ([[billing-and-payment-tax]], [[billing-revenue-recognition]]). And an Adyen article of 15 September 2026 says: "Adyen doesn't act as a direct, third-party merchant of record."

On 1 July 2026 that gap began to close, when Adyen completed its purchase of Orb. Both companies now own a usage-billing engine bought in 2026. The limit is stated by [[subscriptions-and-billing-engines]]: for an Adyen integrator nothing has changed yet. Adyen's documentation has no page for a billing product, Orb's documentation lists Adyen as a payment gateway connected with an API key, and Adyen's article of 29 September 2026 says only "You'll soon see".

> **INFERENCE, NOT DOCUMENTED:** The edge fits the first customer. An enterprise has its own billing system, legal entities and tax function, so a provider that stops at the payment suits it. A small self-serve seller has none of those, and Stripe already owned the tax, fraud and checkout products that a merchant of record is assembled from. Neither company states this reasoning.

When and how Orb joins Adyen's platform is not public, so the decision turns on one record: where your invoice lives. If you want the provider to hold it, that is documented for Stripe. On Adyen, name the system that holds the schedule, the amount and the invoice before the first renewal runs. If you run both providers, keep the invoice in one named system, because a product inside one provider sees only that provider's sales: [[billing-and-payment-tax]] notes that a threshold monitor inside one provider undercounts for a business on two.

## Platforms: Who Stands Behind the Seller

The last bet is also one of default, and it rests on the others. Both companies sell a product for platforms, businesses that take payments on behalf of many sellers: Stripe's Connect dates from October 2012, and Adyen's Platforms pillar brought €263.8 million of net revenue in 2025. They model the seller differently. Stripe has one account per seller and expresses who the merchant is per payment, by the type of charge. Adyen separates a seller into a legal entity, an account holder, a balance account and a transfer instrument, and decides where a refund or a chargeback (a payment reversed through the cardholder's bank) is booked by an instruction on each payment ([[platform-payment-models]]). One consequence: an Adyen split that cannot be booked as sent is booked to the platform's liable balance account without an error, where a failed Stripe transfer returns one ([[splits-balances-and-platform-payouts]]).

On who bears a seller's losses, however, the two are closer than commonly said. Stripe offers itself as loss bearer as a setting per account, and the setting is permanent: "You can't update their values later." Adyen's default is the platform: a seller's balance may stay negative for up to 30 days, after which the platform's reserved compensation account is debited. But Adyen also documents Managed Risk, under which it will "assume the responsibility for negative balances" and write them off after 180 days; the page (n.d., accessed November 2026) marks it as a pilot with limited availability. The license bet returns in the financial products sold through platforms: Stripe's rest on partner banks and outside lenders, Adyen's on its own licenses, and accounts for a platform's sellers are generally available at neither ([[embedded-finance]]).

> **INFERENCE, NOT DOCUMENTED:** Stripe's setting suits a platform with no risk function of its own, which matches the software companies it started with. Adyen's default assumes a platform able to carry and manage its sellers' risk. Neither company says so.

Two things a platform would want to compare are not public: Adyen's price list for its platform product, and how either company underwrites sellers ([[payment-fraud-and-risk]]). So on Stripe, decide who bears seller losses before you create the first account, because that decision also fixes who may collect verification data ([[platform-onboarding-and-verification]]). On Adyen, send the chargeback instruction with every payment and reconcile every split. On both, ask for the release stage of each financial product in each country.

## The Map on One Page

The table gathers the eight bets. Every Stripe and Adyen cell repeats a fact cited above with its year; "n.d." marks pages accessed in November 2026. The "Kind" column is this chapter's sorting.

| Bet | Stripe | Adyen | Kind | Not public |
| --- | --- | --- | --- | --- |
| Who holds the money | "Stripe is not a bank" (n.d.); e-money institutions in Ireland and the UK; US money transmitter; partner banks | Credit institution (2017), US branch (2021), UK branch (2023); pre-financed sales-day payout (2024) | Kind | Stripe's safeguarding banks and its reasons; the banks behind Adyen's balances waiting for payout |
| Who acquires | Own entities in the EEA, the UK, Brazil and much of Asia-Pacific; named acquirers elsewhere, its own Georgia bank among six in the US (2026) | 84% of volume full-stack (2025); 14 acquiring connections listed and an entity named for some markets (n.d.); banking partners where it has no acquiring license (2025) | Degree | Volume per acquirer; a complete list of Adyen's acquiring entities per country; memberships by network and country |
| Build or buy | Ten named purchases since 2020, two not confirmed closed | Two purchases, both closed on 1 July 2026 | Sequence | How bought products are joined; Adyen's date for convergence |
| One platform or a suite | A suite as packaging (2024); one object model (n.d.) | "single platform" as operation (2025); several API families (n.d.) | Not a like-for-like row | Which Stripe products share its repository; what Adyen's bought products share |
| First customers and defaults | Technology companies first (2022 letter); blended rate published, IC+ on request (n.d.) | "Built for enterprise" (n.d.); Interchange++ with volume tiers (n.d., 2026) | Default | Realized prices; an independent measure of approval rates |
| Who runs the machines | AWS (2023); no region named | Own infrastructure in data centers (2021, 2025); six regions named (n.d.) | Kind | AWS regions; cities and operators; the failover design of both |
| Billing and revenue | Billing (2018); tax and revenue recognition (2021); merchant of record and Metronome (2026) | No first-party billing, tax or recognition product found (2026); not a merchant of record (2026); Orb (2026) | Sequence | When and how Orb joins the platform |
| Platforms | Provider as loss bearer: a permanent setting per account (n.d.) | Platform bears losses by default; Adyen bears them in a pilot (n.d.) | Default | Adyen's platform prices; underwriting at both |

By date, I read the map, as I read the two cases, as an order of construction, not a division of territory; neither company describes itself so. Stripe started with the interface and moved down: its own acquiring entities, then a Georgia bank in business since May 2026. Adyen started with the license and the platform and moved out: financial products, smaller merchants through platforms, and in July 2026 loyalty and billing by purchase. The steps of 2025 and 2026 that changed a row narrowed it: that bank on acquiring, those purchases on build or buy and on billing. The two rows where nothing moved are the differences of kind: no entry makes Stripe a deposit-taking bank, and none moves either company's machines. The figure below draws the two orders.

<!-- illustration-placeholder
{
  "id": "48-two-orders-of-construction",
  "status": "pending",
  "asset": "assets/images/48-the-bets-compared/48-two-orders-of-construction.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that reads the map as an order of construction",
  "visual_goal": "Show two providers with the same five layers built in opposite orders, converging in the middle, with the two layers that differ in kind marked.",
  "prompt": "Structural comparison diagram with two towers side by side, each made of the same five stacked layers. From top to bottom the layers are labeled once, in a narrow column between the towers: \"Interface\", \"Products\", \"Acquiring\", \"Money\", \"Machines\". Left tower, tagged \"Provider A\": the top layer is solid blue and carries a small flag \"2011\"; a thick blue arrow labeled \"built downward\" runs down the left side of the tower; the lower layers get lighter toward the bottom. Right tower, tagged \"Provider B\": the \"Money\" layer near the bottom is solid teal and carries a small flag \"2006\"; a thick teal arrow labeled \"built outward\" runs up the right side of the tower; the upper layers get lighter toward the top. In both towers the layers \"Money\" and \"Machines\" have a bold orange outline, and a small orange tag between the towers at that height reads \"Differ in kind\". At the height of the layers \"Products\" and \"Acquiring\" two small green arrows point toward each other between the towers, with a small flag \"2026\". In the left tower the \"Machines\" layer shows a cloud icon; in the right tower it shows a row of server cabinets. In the right tower the \"Money\" layer shows a bank building with columns; in the left tower it shows a shield and a smaller bank building beside it. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two towers with the same five layers: Provider A built from the interface downward since 2011, Provider B from the money layer outward since 2006; the money and machines layers are outlined as different in kind, and arrows show the two converging in 2026 on products and acquiring.",
  "caption": "Two orders of construction: Provider A (Stripe) launched its interface in 2011 and built downward; Provider B (Adyen), founded in 2006, started from the regulated layer and built outward. By 2026 they converge on products and acquiring; who holds the money and who runs the machines remain differences of kind."
}
-->

## Choosing or Combining: A Decision Aid

To use the map, start from your business and find the rows that bear on it. The table draws only on documented differences, never on the inferences.

| If your business… | The documented difference that bears on it | What to do |
| --- | --- | --- |
| wants the provider to hold subscriptions, invoices, usage and tax | Stripe has first-party products since 2018; Adyen bought Orb in July 2026 and documents no billing product of its own | Decide where the invoice lives before you compare anything else |
| sells in stores | Both sell terminals; Adyen reports the channel (€310.9 billion in 2025); Stripe publishes no in-person figure | Compare the features you need in [[in-person-payments]], not the reputations |
| has, or lacks, a finance team that audits card costs | Interchange++ is Adyen's default and a custom option on Stripe; a blended rate is Stripe's published default | Ask for the model that fits, and what else changes with it |
| holds balances, or is a platform | A bank against e-money institutions and partner banks; the provider as loss bearer by setting or by pilot | Establish the entity per country; fix the loss bearer first |
| sells in the United States | Stripe names six acquirers; Adyen has a federal branch and names no acquirer per payment | Ask each provider which entity acquires for you |
| must say where payment data is stored | Adyen has a region setting and says payments are "stored in Europe"; Stripe states no location | Check the setting on one; ask the other in the contract |
| sends large batches | Stripe publishes a rate limit; Adyen publishes none for payments | Read it at one; ask for it in writing at the other |

By contrast, the four things cited most do not decide. Company size does not: each company now sells to the other's first customers. Volume does not: the two companies' reported figures measure different things ([[payment-economics]]). Availability figures do not: neither publishes a consistent yearly series. Nor do vendor claims of higher approval rates, which cannot be compared.

A business that runs both providers absorbs every row in its own software, and Larkfield's filled card shows where. Amounts marked *(assumption)* are illustrative, and nothing in the table is evidence about either provider.

| Row | Larkfield on Stripe | Larkfield on Adyen | What the payment service does |
| --- | --- | --- | --- |
| Acquirer and holder of funds | Stripe Technology Europe, Ltd. (Netherlands, Germany, Belgium); Stripe Payments UK, Ltd.; in the US one of six named acquirers, a question put to Stripe and still open | Adyen N.V. (Netherlands, Germany), Larkfield's reading of Adyen's license page | Keeps the acquirer inventory, one dated row per market |
| Price | Negotiated blended rate of 0.6% + €0.15 *(assumption)* | Negotiated Interchange++; €0.61 on Mila's €120.00 pass *(assumption)* | Books the provider's cost per payment when it is reported |
| Payment state | Reads the payment object | Webhook, then the settlement report | Feeds one five-state record two ways (K2) |
| Payout and reconciliation | Funds per transaction; keyed on the payout | Funds per sales day; keyed on the batch | Runs one reconciliation per provider (K3) |
| Billing | Stripe Billing for studio plans since 2018 | None; the booking app's renewal job charges stored cards | Writes one period record per membership on both |
| Platform model | Legacy Custom accounts, destination charges; Larkfield bears losses | Platform model; a chargeback instruction on every payment | Stores merchant, loss bearer and booking rule per studio |

From that card Larkfield decides to keep both. Its own subscriptions (€24.5 million in 2026) stay on Stripe, because the invoices, the tax calculation and the usage meter live there and Adyen documents no product to move them to. For member payments no documented difference forces either provider: by its acquirer inventory each provider's own entity acquires in its European markets (for Adyen, a reading of the license page), and Larkfield's 2024 reason for adding Adyen, local acquiring, stands in its inventory as "effect not measured". The reason to keep two is Larkfield's own, the rehearsed switch of K8; Adyen's risk section describes the habit from the other side: large enterprise merchants "typically work with multiple payment service providers to mitigate their own single-point-of-failure risk". The price is the card's last column: two of everything in one payment service, as the figure below shows.

<!-- illustration-placeholder
{
  "id": "48-one-service-two-providers",
  "status": "pending",
  "asset": "assets/images/48-the-bets-compared/48-one-service-two-providers.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on Larkfield's decision to keep both providers",
  "visual_goal": "Show one payment service absorbing two providers' different defaults through two adapters, so the rest of the business sees one vocabulary.",
  "prompt": "Component layout in three columns. Left column: a generic booking application box labeled \"Booking app\" with one thick arrow labeled \"take a payment\" pointing right. Center column: a large rounded box labeled \"Payment service\" containing, at its left, one tidy card labeled \"One record\" and, at its right edge, two adapter plugs stacked vertically, the upper one blue and the lower one teal, each labeled \"Adapter\". Right column: two generic payment provider boxes stacked vertically, the upper labeled \"Provider A\" in blue and the lower labeled \"Provider B\" in teal, each connected to its adapter by a two-way arrow. Beside the upper arrow, three small icons with labels: a document labeled \"read object\", a single coin labeled \"one fee\", a calendar page labeled \"per payment\". Beside the lower arrow, three small icons with labels: an envelope labeled \"events\", three stacked coins labeled \"itemized\", a stack of calendar pages labeled \"per day\". Under the payment service, a small clipboard labeled \"Dated card\" with a thin dashed arrow up to the service. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A booking app calls one payment service, which keeps one record and reaches two providers through two adapters; one provider is read as an object with one fee per payment, the other through events with itemized fees per day.",
  "caption": "What combining the two costs: one payment service with two adapters absorbs the differences in how state is read, how fees are shown and when funds arrive, with Provider A as Stripe and Provider B as Adyen, and a dated card records the rest."
}
-->

The card fails in one way, however: it goes stale. Four events of 2026 alone changed cells of the map. Stripe completed the purchase of Metronome on 14 January, Managed Payments entered a release version of its API on 22 April, its Georgia bank began business on 28 May, and Adyen closed Orb and Talon.One on 1 July. So every row carries its date and source, and Larkfield reads the card again in the half-yearly slot it keeps for API upgrades (K7).

## What to Take Away

**Established.**

- Adyen N.V. is a licensed credit institution with a US and a UK branch; Stripe states "Stripe is not a bank". Adyen runs its own infrastructure in data centers; Stripe runs on AWS by its 2023 statement. Both are differences of kind in November 2026.
- Acquiring is a difference of degree: Stripe's own entities acquire in the EEA, the United Kingdom and much of Asia-Pacific, and Adyen reports 84% of its 2025 volume as full-stack.
- Build or buy is a difference of sequence: ten named Stripe purchases since 2020; two by Adyen, both closed on 1 July 2026.
- Realized prices, volume per acquirer and an independent measure of approval rates are not public for either.

**Depends on context.**

- How much the money-holding difference matters depends on whether you keep balances or run a platform.
- Which pricing default suits you depends on whether someone will read an itemized statement.
- Whether the billing difference decides depends on where your invoice already lives.
- Whether to run both depends on what an outage of one would cost you, set against the price of absorbing two sets of defaults.

**The author's synthesis.**

- I would establish the two differences of kind and negotiate the rest. A license and a data center cannot be asked for; a pricing model, a rate limit and a payout schedule can.
- Both opening slogans are descriptions with a date. "Stripe is for startups, Adyen is for enterprises" describes 2011 and 2006. "Adyen owns the stack, Stripe rents it" holds for banking and hosting, fails for card acquiring in Europe, and cannot be tested on motive, because Stripe has published none.

## Questions to Ask

1. Per country, which legal entity acquires our card payments at each provider, and when did we last check?
2. Which entity holds our funds, or our sellers' funds, in each country, under which license, and is our payout paid before the network pays?
3. Which pricing model are we on, and did we ask for the other?
4. Was each product we use built or bought, when, and have we tested its join to payments?
5. Where does our invoice live, and does any tax or recovery product see only part of our sales?
6. Who bears our sellers' losses at each provider, and can that assignment change?
7. What have we asked each provider in writing about regions and failover?
8. Which cells on our card say "Not public", whom did we ask, and when do we read the card again?

Most of the differences turned out to be defaults and sequences, which I traced, as inference, to each company's first customers; only money-holding and hosting are differences of kind. Two cases are thin support for that reading. [[payment-contrast-cases]] adds three companies that started with other customers (PayPal, Checkout.com and Block), each read for the one thing it holds that neither Stripe nor Adyen does.

## Sources and Evidence

This chapter repeats facts that earlier chapters own. The entries below are the sources of its load-bearing facts, taken from those chapters and fetched again in the verification pass of 17 November 2026; every other fact is sourced in the chapter linked beside it.

*Company, product and investor sources*

- [Acquirer Disclosure & Acquirer Terms](https://stripe.com/legal/acquirer-disclosure), Stripe, n.d., accessed 2026-11-17 — the acquirer named per country; the six US acquirers (volatile).
- [Stripe MALPB Acquirer Terms](https://stripe.com/legal/stripe-malpb-acquirer-terms), Stripe, last updated 2026-05-28 — Stripe's Georgia Merchant Acquirer Limited Purpose Bank as a network member and acquirer.
- [Treasury](https://docs.stripe.com/treasury.md), Stripe documentation, n.d., accessed 2026-11 — "Stripe is not a bank"; Fifth Third Bank.
- [Stripe Payments Company Terms](https://stripe.com/legal/spc), Stripe, last updated 2025-11-18 — "state-licensed money transmitter".
- [Amazon-Stripe partnership accelerates ecommerce and streamlines online payments](https://stripe.com/newsroom/news/amazon-and-stripe), Stripe newsroom, 2023-01-23 — hosting on AWS (evidence age: almost 4 years).
- [Pricing](https://stripe.com/en-nl/pricing), Stripe, n.d., accessed 2026-11 (Netherlands edition) — the blended standard rate; "IC+ pricing" among custom options (volatile).
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests.md), Stripe API reference, n.d., accessed 2026-11 — keys kept at least 24 hours.
- [Rate limits](https://docs.stripe.com/rate-limits.md), Stripe documentation, n.d., accessed 2026-11 — 100 requests a second per live account (volatile).
- [Configure the behavior of connected accounts](https://docs.stripe.com/connect/accounts-v2/connected-account-configuration), Stripe documentation, n.d., accessed 2026-11 — `losses_collector`; "You can't update their values later".
- [Stripe completes Metronome acquisition](https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition), Stripe newsroom, 2026-01-14 — completion.
- [More PSPs, more problems? When adding multiple processors pays off](https://stripe.com/sessions/2026/more-psps-more-problems), Alex Ginet and Jon Krauss (Stripe) and Joshua Barton (Canva), Stripe Sessions, 2026-04 — the "locked into Stripe" statement, in the talk's transcript (a vendor event).
- [Stripe annual letter 2024](https://stripe.com/annual-updates/2024), Patrick and John Collison, 2025-02-27 — "Revenue and Finance Automation Suite, with Billing at its core".
- [Stripe's 2025 annual letter and tender offer](https://stripe.com/newsroom/news/stripe-2025-update), Stripe newsroom, 2026-02-24 — "the 'long tail' is much of the dog".
- [Stripe Series I](https://stripe.com/newsroom/news/stripe-series-i-employee-liquidity), Stripe newsroom, 2023-03-15 — enterprise base "compounded since 2019" (evidence age: 3.5 years).
- [Selective Test Execution at Stripe](https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo), Aditya Anchuri, Stripe, 2026-04-09 — one repository of about 50 million lines of Ruby.
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods), Stripe documentation, n.d., accessed 2026-11 — activation "generally instantaneous".
- [Subscription invoices](https://docs.stripe.com/billing/invoices/subscription.md), Stripe documentation, n.d., accessed 2026-11 — an invoice for every subscription billing period.
- [Stripe annual letter 2022](https://stripe.com/annual-updates/2022), Patrick and John Collison, 2023-04-05 — "grew up with companies in the technology sector" (evidence age: 3.5 years; read in the letter's PDF).
- [Licenses and disclosures: EMEA](https://www.adyen.com/licenses/emea), Adyen, n.d., accessed 2026-11 — credit institution under the Dutch central bank; the UK branch.
- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., signed 2026-03-05 — 84% full-stack volume, banking partners, the single-platform statements, capital expenditure, the multi-provider risk statement (audited; read in the PDF this page offers for download, a "printed version").
- [Q3 2026 Business Update](https://investors.adyen.com/financials/q3-2026-10c88s), Adyen, 2026-10-28 — smaller merchants through platforms, tiered pricing, active business customers (unaudited; read in the PDF linked from this page).
- [Adyen publishes Q3 2026 business update](https://www.adyen.com/press-and-media/adyen-publishes-q3-2026-business-update-6r9vz0), Adyen, 2026-10-28 — "the successful ongoing integration of Talon.One and Orb".
- [Adyen closes Talon.One and Orb acquisitions, announces leadership updates](https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates), Adyen, 2026-07-01 — both closed on 1 July 2026.
- [Adyen to acquire Orb](https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj), Adyen, 2026-06-11 — "an incubator model", multi-PSP support, convergence as intent.
- [Why billing and payments belong together](https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb), Adyen, 2026-09-29 — "You'll soon see".
- [Adyen publishes H1 2026 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne), Adyen, 2026-08-13 — investment pulled forward "to secure compute and storage availability".
- [We built Architect for humans](https://www.adyen.com/knowledge-hub/architect-blog-1), Adyen, 2026-08-23 — "around 3,000 live services".
- [Adyen Uplift](https://www.adyen.com/uplift), Adyen product page, n.d., accessed 2026-11 — "Unlike fragmented legacy architectures, Adyen brings payments onto one single platform".
- [Terms and Conditions](https://www.adyen.com/legal/adyen-terms-and-conditions), Adyen, last update 2023-11-01 — amounts "held by Adyen prior to Settlement"; the 99.9% uptime clause (evidence age: 3 years).
- [Stripe Services Agreement: Services Terms](https://stripe.com/legal/ssa-services-terms), Stripe, last modified 2026-09-28 — settlement funds transferred on the payout schedule "unless a Payout Delay occurs"; the definition of Payout Delay; no pre-financing stated.
- [Licenses and disclosures: Japan](https://www.adyen.com/licenses/japan) and [Singapore](https://www.adyen.com/licenses/singapore), Adyen, n.d., accessed 2026-11 — Adyen Japan KK's registration as merchant acquirer; Adyen Singapore's license for merchant acquisition.
- [Credit card processing fees: what determines your rate and why the lowest isn't always the cheapest](https://www.adyen.com/knowledge-hub/credit-card-processing-fees), Adyen, 2026-07-03 — "principal membership of Visa and Mastercard in major markets" (vendor claim, no list).
- [Sales Day Payout Terms of Service](https://www.adyen.com/legal/sales-day-payout-terms-of-service), Adyen, last update 2024-06-17 — payout irrespective of receipt of funds.
- [Payments platform infrastructure](https://www.adyen.com/infrastructure), Adyen, n.d., accessed 2026-11 — the six data-center regions; payments stored in Europe and an isolated India environment.
- [Design to Duty: How we make architecture decisions at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture), Adyen, 2021-07-28 — own infrastructure and the stated reasons (evidence age: 5 years).
- [Pricing for supported payment methods](https://www.adyen.com/pricing), Adyen, n.d., accessed 2026-11 — processing fee plus a fee per method; Interchange++; "indicative" (volatile).
- [About Adyen](https://www.adyen.com/about), Adyen, n.d., accessed 2026-11 — "Built for enterprise, not adapted to it"; the history without earlier acquisitions.
- [Merchant of record explained: Everything you need to know](https://www.adyen.com/knowledge-hub/merchant-of-record), Adyen, 2026-09-15 — Adyen's statement that it is not a merchant of record.

*Standards, regulation and official documentation*

- [Supported payout currencies](https://docs.adyen.com/account/supported-currencies), Adyen documentation, n.d., accessed 2026-11 — countries and regions with an Adyen acquiring connection; "one of our acquiring entities, for example Adyen Singapore".
- [Network tokenization](https://docs.adyen.com/online-payments/network-tokenization), Adyen documentation, n.d., accessed 2026-11 — "only applicable for payments acquired by Adyen".
- [Sales day payout: upgrade guide](https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp), Adyen documentation, n.d., accessed 2026-11 — "Prefinancing is capped at 30 days".
- [API idempotency](https://docs.adyen.com/development-resources/api-idempotency), Adyen documentation, n.d., accessed 2026-11 — keys valid 7 to 14 days.
- [Adyen Managed Risk](https://docs.adyen.com/platforms/managed-risk), Adyen documentation, n.d., accessed 2026-11 — the pilot in which Adyen assumes responsibility for negative balances and writes them off after 180 days.
- [Peak season readiness](https://docs.adyen.com/industries/peak-season), Adyen documentation, n.d., accessed 2026-11 — utilization under 30%, the deployment freeze, failover by load balancers.
- [Financial Institutions Bulletin, May 2026](https://dbf.georgia.gov/financial-institutions-bulletin-2026), Georgia Department of Banking and Finance, May 2026 — Stripe MALPB approved 30 June 2025, in business since 28 May 2026 (the May 2026 bulletin, a PDF listed on this page).
- [Corporate Decision #1365, Bridge National Trust Bank](https://www.occ.treas.gov/topics/charters-and-licensing/interpretations-and-decisions/2026/cd1365.pdf), Office of the Comptroller of the Currency, 2026-02-12 — preliminary conditional approval only; the bank "will not be an insured depository institution".

*Research and practitioner sources*

- [Georgia approves Stripe application to form MALPB](https://www.icba.org/w/georgia-approves-stripe-application-to-form-malpb), Independent Community Bankers of America, 2025-07-08 — what the Georgia charter permits and its limits (secondary source).

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
