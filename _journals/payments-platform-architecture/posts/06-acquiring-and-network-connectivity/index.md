---
title: "Plugging Into the Networks: Acquiring, Licences and Connectivity"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What does it take to connect to the card networks, and what separates Adyen's route to them from Stripe's? A membership only a licensed entity can hold, so every payment has an acquirer of record per country: Adyen holds it through one banking license, Stripe through its own entities in Europe and named banks in the United States."
permalink: acquiring-and-network-connectivity
timetoread: 25 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn who is allowed to send a payment to a card network, and find the acquirer of record behind a provider in each country you sell in.

> **KEY POINTS:**
>
> * **A network connection is a membership, and a membership needs a license.** Every card payment has an acquirer of record: the licensed network member that submits it and answers for it. A provider can exchange messages with a network directly while another institution holds that role.
> * **Adyen and Stripe hold the membership by different routes.** Adyen obtained one banking license in 2017 and added branches in the United States (2021) and the United Kingdom (2023). Stripe names its own e-money institutions as acquirer in Europe, and five banks plus a limited-purpose bank of its own in the United States (read November 2026).
> * **Domestic payments do better; nobody has published by how much.** A payment is domestic when the card's bank and the merchant are in the same country, which takes an acquirer licensed there. Every published figure for the gain is a vendor's, with other changes mixed in.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Single Rail** — every payment in a country depends on one acquirer, and the team cannot name it, so nobody notices when it changes.
> * **The Accidental Bank** — a platform that signs up sellers under someone else's network membership takes on duties and limits it has never read.

<br>
In April 2020 Stripe announced that it "now processes card transactions through direct integrations with all six major card networks in North America, Latin America, Europe and Asia Pacific". In November 2026 its legal pages say that in the United States "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers", and name five banks and a limited-purpose bank of Stripe's own. Both statements are true at once. If you read "connected directly" as a statement about wiring, you cannot explain how.

The gap costs a merchant something. A card network does not care who operates the wire; it cares which of its members answers for the transaction. **That member decides how your payment arrives at the cardholder's bank, receives the settlement money before you do, and passes its rules and failures on to you**, though you signed with a provider.

**Connecting to a card network takes a membership that only a licensed entity can hold, so every payment has an acquirer of record, and that entity differs by country**. Adyen obtained one banking license in 2017 and extended it through branches. Stripe is its own acquirer in the European Economic Area (EEA) and the United Kingdom, and works under named acquirers, most of them banks, in the United States and elsewhere. What separates the routes is **how many parties stand between the merchant and the network**: none where the provider is itself the acquirer, a sponsoring bank where it is not.

**Where we are in the payment's journey.** Larkfield is the fictional studio-software platform this book follows. On Tuesday 9 March 2027 at 19:42, Mila Janssen buys a ten-class pass for €120.00 from Studio Noord with her Dutch Visa debit card. [[payment-authorization]] followed the message that asks her bank for approval. This chapter covers the step before that message leaves: which entity may send it under its own name. Studio Noord is on Adyen, so here it is Adyen N.V.; that is my reading of Adyen's license page, since Adyen names no acquiring entity per country.

The chapter starts with two words in a Larkfield decision record that nobody can explain. It defines the two permissions acquiring takes and the roles that work under an acquirer, then shows what the acquirer of record changes for a payment and how far published uplift figures can be trusted. It compares three ways to hold a membership, sets out what Adyen and Stripe each document, and puts the two side by side. It ends with Larkfield's acquirer inventory and the ways an acquiring arrangement fails.

## Setting the Scene at Larkfield: Two Words in a 2024 Decision Record

In February 2027 Femke de Graaf, Larkfield's new Head of Payments Engineering, reads the 2024 decision record that added Adyen beside Stripe. It gives two reasons: in-person payments on the same platform as online ones, and "local acquiring in the Netherlands and Germany". Nobody on the team can say what the second reason changed.

She asks who acquires Larkfield's studios in each market: the Netherlands (2,300 studios), Germany (1,450), the United Kingdom (1,100), Belgium (650) and the United States (700, since 2025). Tom Hendriks, who built the payment service, answers "Adyen" and "Stripe". Those are providers; Femke wants the legal entity. For the 700 American studios, nobody in the room knows that a bank is involved at all.

So she writes down the question this chapter answers: **for each provider and each country, which entity is the acquirer of record, under what license, and what follows for approvals and for the flow of funds?**

## Two Permissions: A Network Membership and a License

Visa and Mastercard are membership organizations. [[journey-of-a-payment]] introduced the **issuer** (the cardholder's bank) and the **acquirer** (the merchant's side) as two boxes in the four-party model. Visa's public rules (edition of 24 October 2026) say what is inside the second box. An Acquirer is "A Member that signs a Merchant or Payment Facilitator, provides a Cash Disbursement to a Cardholder, or loads funds to a Prepaid Card, and directly or indirectly enters a Transaction into Interchange." Two words carry the chapter. "Member": acquiring is a right of membership, not a technical capability. "Indirectly": the member need not operate the connection itself. (Interchange, in the same glossary, is "The exchange of Clearing Records between Members", not the fee of that name.)

A provider's contract describes the same role from the merchant's side. Stripe's services terms (n.d., accessed November 2026) define a "Payment Method Acquirer" as "an entity that a Payment Method Provider has authorized to (a) sponsor or submit Transactions at the request of merchants to the Payment Method Provider for authorization and clearing; and (b) receive and remit settlement funds for authorized and cleared Transactions". Clearing is the exchange of final transaction records and settlement the movement of money between members ([[clearing-and-settlement]]). So the acquirer submits your payments, and **it is the first party to receive the money for them**. This book calls the entity that holds that role for a given payment the **acquirer of record**.

Those two activities need two permissions from two grantors: a license from a financial regulator and a membership from each network (the table is my summary). Adyen's merchant guide (n.d., accessed November 2026) names both: "Acquirers must be licensed by local financial regulators and card schemes to relay transactions." ("Card scheme" is another name for a card network.) The license need not be a banking license. Stripe Technology Europe Limited "is authorised as an electronic money institution by the Central Bank of Ireland (reference number: C187865)", and its listed services include to "acquire payment transactions" (page dated April 2019). **(Evidence age: 7 years; Stripe's current acquirer disclosure names the same entity.)** An e-money license lets a company that is not a bank hold customer funds and make payments with them; what it lets a provider hold belongs to [[licences-and-safeguarding]].

| Permission | Granted by | What it allows |
| --- | --- | --- |
| A regulatory license | The financial regulator of a country or region | Providing acquiring as a regulated service and handling the merchant's funds |
| A network membership, or sponsorship by a member | Each card network or local scheme | Submitting transactions under an identifier and taking part in settlement |

Membership has tiers. In Visa's rules a "Principal-Type Member" licenses its own network identifiers: a BIN (bank identification number) for issuing, an Acquiring Identifier for acquiring. An "Associate-Type Member" may use an identifier licensed to its sponsor. Liability follows the identifier: "A Principal-Type Member is responsible and liable for all activities associated with any BIN or Acquiring Identifier that it licenses", and for an associate, "To the extent an Associate-Type Member is unable to fulfill that responsibility, its Sponsor will be responsible and/or liable." That is what **sponsor bank** and **BIN sponsorship** mean: a company processes under an identifier that belongs to a member bank, and the bank answers to the network for it. A "partner bank" in a provider's documents is usually a bank in this role. I could not read Mastercard's rules (its public file refused automated access); "principal" and "affiliate" are the terms commonly used for its two levels.

## Processor, Gateway, Payment Facilitator: Who Holds the Membership

Four roles surround a card payment, and only one is a member. Visa's glossary defines an "Acquirer Processor" as "A non-Member agent or processor that a Member has engaged to support its Visa acquiring business". The other cells below are industry usage, not network text. "Payment service provider" (PSP) is a commercial label for a company that packages several of these roles, and the package can differ by country.

| Role | What it does | Network member? | Holds the merchant's money? |
| --- | --- | --- | --- |
| **Acquirer** | Signs the merchant or a payment facilitator, submits transactions, receives settlement | Yes | Yes, between settlement and payout |
| **Acquirer processor** | Runs the connection and message processing for an acquirer | No | No |
| **Gateway** | Passes payment data from the merchant to an acquirer or processor | No | No |
| **Payment facilitator** | Signs many small sellers under one acquirer and pays them out | No; registered with the network by its acquirer | Usually, between acquirer and seller |

The **payment facilitator** (PayFac) is the role a platform reader most often sits under. Visa defines it as "An entity that contracts with an Acquirer to deposit Transactions, receive settlement from, or contract with an Acquirer on behalf of a Sponsored Merchant." The membership does not move: "A Sponsored Merchant will be treated as a Merchant of its Payment Facilitator's Acquirer. An Acquirer that contracts with a Payment Facilitator is liable for all acts, omissions, and other adverse conditions caused by the Payment Facilitator and its Sponsored Merchants". What a platform takes on when it becomes a facilitator itself is the subject of [[platform-payment-models]].

The network also limits the model by seller size. "An Acquirer that contracts with a Payment Facilitator must enter into a direct Merchant Agreement with a Sponsored Merchant that exceeds USD 1 million in annual Transaction volume": before processing for a new seller, or "within 2 years" for an existing one, with exceptions. Past a threshold, the acquirer becomes the seller's direct counterparty.

Together the definitions give the chapter's central distinction: **a direct technical connection to a network and being the acquirer of record are different facts, and a company can have either without the other.** "Directly or indirectly" lets a member acquire without running the link. The non-member processor runs the link without the membership. Block, a large US payment facilitator, has neither for most of its volume; its annual report for 2025 says: "For a majority of our transactions, we do not directly access the payment card networks". The figure below draws the two facts as two lines.

<!-- illustration-placeholder
{
  "id": "06-connection-versus-membership",
  "status": "pending",
  "asset": "assets/images/06-acquiring-and-network-connectivity/06-connection-versus-membership.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the connection-versus-membership paragraph",
  "visual_goal": "Show the message path and the membership as separate things held by different parties.",
  "prompt": "Create a wide explainer diagram with two layers. Bottom layer, left to right: a shop icon labeled \"Merchant\", a rounded box labeled \"Provider\", a hub shape labeled \"Card network\", a bank building labeled \"Issuer\". A solid blue arrow labeled \"message\" runs from Merchant to Provider, a solid blue arrow labeled \"direct link\" from Provider to Card network, and a solid blue arrow from Card network to Issuer. Top layer, above Provider and Card network: a second bank building labeled \"Sponsor bank\" holding a round orange badge labeled \"Membership\". A dashed orange line labeled \"answers for it\" runs from the badge down to the Card network. A thin dashed teal line labeled \"contract\" joins Provider and Sponsor bank. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A payment message travels from merchant through provider to the card network and issuer, while a separate sponsor bank above holds the membership badge.",
  "caption": "The wire and the membership are separate: a provider can exchange messages with the network directly while a sponsoring bank is the member that answers for the transaction."
}
-->

## What the Acquirer of Record Changes: Domestic Payments and an Unmeasured Uplift

Start with what "domestic" means to a network. Visa's glossary defines a Domestic Transaction as "A Transaction where the Issuer of the Card used is located in the Transaction Country", and the Transaction Country as "The country in which a Merchant Outlet is located". Any other transaction is an International Transaction. Domestic is a relation between the issuer's country and the merchant's.

The acquirer enters through a second rule, section 1.5.1.1 of Visa's Core Rules: "An Acquirer must accept Transactions only from a Merchant Outlet within the Acquirer's Country of Domicile (and that country's territories and possessions) unless any of the following". One listed exception matters in Europe: "In the Europe Region: An Acquirer has passported its license in line with EU passporting regulations." Passporting lets an institution licensed in one EEA country serve the others. Read with the definition above, the rule gives **local acquiring** its meaning: a business can sell as a local merchant in a country only if its provider has an acquirer whose license reaches that country, whether a single country or the whole EEA. Otherwise it sells from wherever its acquirer is, and that country's cards arrive at their issuers as international payments.

<!-- illustration-placeholder
{
  "id": "06-local-door-foreign-door",
  "status": "pending",
  "asset": "assets/images/06-acquiring-and-network-connectivity/06-local-door-foreign-door.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the local-acquiring paragraph",
  "visual_goal": "Same card, same bank: local or foreign depending on the acquirer.",
  "prompt": "Create a wide conceptual illustration. On the left, one customer holding one payment card. On the right, one bank building labeled \"Issuer\" with two doors. Two paths lead from the card to the bank. The upper path passes a small building flying the same plain green flag as the bank, labeled \"Local acquirer\", and enters through a wide green door labeled \"Domestic\". The lower path passes a small building flying a plain orange flag, labeled \"Acquirer abroad\", crosses a dotted border line, and enters through a narrower orange door labeled \"International\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "One card reaching one issuing bank by two paths: through a local acquirer into a door marked domestic, and through an acquirer abroad into a door marked international.",
  "caption": "One card, one issuer, two arrivals: whether the issuer sees a domestic or an international payment depends on where the merchant's acquirer is licensed."
}
-->

That a domestic payment is approved more often and costs less than an international one is accepted across the industry. An issuer's risk checks commonly treat a foreign merchant with more suspicion, and networks charge extra for crossing a border ([[payment-economics]]). Stripe's guide to local acquiring (last updated August 2023) says: "Because the transaction is local, the chances of approval are typically higher compared to an international transaction". **(Evidence age: 3 years.)** Adyen's acquiring page (n.d., accessed November 2026) says: "Local processing can increase authorization rates and reduce cross-border fees." Neither gives a number.

The numbers that are published do not survive a close reading. I found three statements with a number; none isolates local acquiring, and the one baseline given is a previous provider.

| Claim | Who says it | What it measures |
| --- | --- | --- |
| Klook "unlocked key local payment methods and optimized their payments setup to achieve an overall uplift of 3% in their authorization rates" | Adyen, customer case, August 2024 | One customer; several changes; no baseline |
| Twilio: "+5.5% uplift from Stripe's Global Payments Infrastructure", which the story describes as direct integration with the card networks and local processing "in their key markets" | Stripe, customer story, November 2020 | One customer, against its previous provider; direct connections and local processing together. **(Evidence age: 6 years.)** |
| With direct connectivity firms "can see upwards of half a percentage point of authorization improvement" | Trade press reporting Stripe's John Collison, April 2020 (secondary source; the wording is the publication's) | Direct connections, not local acquiring. **(Evidence age: 6.5 years.)** |

What would a figure need before I believed it? It would change only the acquiring entity and hold the rest still: the same merchant, card country, card type and kind of payment (first or recurring), over the same period or a random split of traffic. It would count authorization rates per attempt, because a rate per order hides retries. [[authorization-optimization]] defines these rates and applies the same test to the providers' optimization products.

The larger effect of a local acquirer is not marginal at all. By common industry account, some domestic card schemes and clearing systems can be reached only by a member in that country, so the choice is between reaching them and not. Adyen's results for the first half of 2026 report that it "Secured direct access to France's domestic interbank clearing system"; the shareholder letter cites its French announcement, whose title says Adyen became a principal member of CB, the French domestic card scheme, and a direct participant in STET, the French clearing system. Memberships of this kind are collected country by country.

## Three Ways to Hold a Membership

A provider that wants to acquire in a country has three routes. They differ in how much permission the provider itself holds, and so in how many parties stand between the merchant and the network.

The first route is a **sponsor bank**. The provider becomes a payment facilitator under a bank that is already a member, which is the quickest way into a market because the license and the membership already exist. The price is a bank in the flow. Under Visa's rule the bank stays liable for the facilitator and its sellers, so it sets terms for them: Stripe's acquirer disclosure links each US acquirer to terms of its own. I read two of the six. The Cross River Bank terms (last updated November 2025) are an agreement among the merchant, Stripe and the bank, and for a merchant the bank has not registered with a network they "become effective only when User processes more than $1 million in Transactions on a Network within any twelve-month period". That is the network's seller-size threshold, described earlier, written into the contract.

The second route is a **narrow license**: the provider becomes its own acquirer with the smallest permission that allows it. In Europe that is an e-money or payment institution license, which one country grants and passporting extends; Stripe's Irish and UK entities are e-money institutions. In the United States, the state of Georgia offers a charter for exactly this purpose, the merchant acquirer limited purpose bank (MALPB). A banking trade association reported in July 2025 that the charter "will allow the financial services company to obtain direct membership with Visa and Mastercard and to process payments without a sponsoring bank", and that such banks "may not solicit or accept deposits from the general public". The bulletin of Georgia's Department of Banking and Finance for May 2026 lists Stripe MALPB, Atlanta, with an approval date of 30 June 2025 and a date to begin business of 28 May 2026.

The third route is a **bank license with branches**: the widest permission, obtained once and extended. Adyen N.V. has been a credit institution, the legal term for a bank, under the Dutch central bank since 2017, passported across the EEA, with branch licenses in the United States (2021) and the United Kingdom (2023). This removes the sponsor wherever the license reaches. The price, in my judgement and not from any published figure, is capital, continuous supervision and years of lead time.

No route is better in general. A sponsor fits a market the provider is entering; a license fits a market large enough to justify its cost.

| Route | Parties between merchant and network | What the provider gains | What it costs | Documented example |
| --- | --- | --- | --- | --- |
| Sponsor bank (provider is a payment facilitator) | The sponsoring bank | Entry without a license of its own *(author's judgement)* | The bank's terms and a dependency on the bank | Stripe in the United States under five named banks (accessed November 2026) |
| Narrow license per market | None | Its own membership | One license or charter per market or region; few permitted activities | Stripe's e-money institutions in the EEA and the UK; Georgia's MALPB charter |
| Bank license with branches | None | One permission reused across markets and products | Capital, supervision and lead time *(author's judgement)* | Adyen: 2017, 2021, 2023 |

<!-- illustration-placeholder
{
  "id": "06-three-routes-to-a-network",
  "status": "pending",
  "asset": "assets/images/06-acquiring-and-network-connectivity/06-three-routes-to-a-network.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table that compares the three routes",
  "visual_goal": "Show three ways to hold a membership as lanes; only the first has an extra party.",
  "prompt": "Create a wide diagram with three horizontal lanes stacked top to bottom, each running from a shop icon labeled \"Merchant\" on the left to a hub shape labeled \"Network\" on the right. Lane one, labeled \"Sponsor bank\": Merchant, then a rounded box labeled \"Provider\", then a bank building labeled \"Bank\" holding a small orange badge, then Network; arrows join each element to the next. Lane two, labeled \"Narrow license\": Merchant, then a rounded box labeled \"Provider\" that itself holds the orange badge and a one-page document icon, then Network; arrows join each element to the next; no bank appears. Lane three, labeled \"Bank license\": Merchant, then a larger building labeled \"Provider bank\" holding the orange badge, with two smaller buildings labeled \"Branch\" attached by short lines, then Network; arrows join Merchant to Provider bank and Provider bank to Network. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Three lanes from merchant to network: a provider with a sponsoring bank, a provider holding its own narrow license, and a provider that is a bank with branches.",
  "caption": "Three ways to hold a membership: under a sponsor bank a second party stands between the merchant and the network; under a narrow license or a bank license the provider holds the membership itself."
}
-->

## Adyen's Route: One Banking License, Extended by Branches

Adyen is the documented case of the third route. Its license pages (n.d., accessed November 2026), its press releases and the Federal Reserve give the following. **(Evidence age: the 2021 releases are 5 years old and the 2023 release 3; the current license pages confirm all three.)**

| Region | The license, in Adyen's words | Year |
| --- | --- | --- |
| EEA | "Adyen N.V. is authorised as a credit Institution under the supervision of Dutch Central Bank", which "includes the ability to provide cross-border acquiring, payment and banking services in all EEA countries" | "obtained in 2017" (Adyen, June 2021) |
| United States | "a federal Branch of Adyen, N.V., licensed by the Office of the Comptroller of the Currency and the Federal Reserve Board of Governors" | Federal Reserve approval 24 May 2021; the Comptroller's approval announced 14 June 2021 |
| United Kingdom | Its UK branch "has been granted authorization as a UK bank" | 7 September 2023 |

Adyen says why it took this route, and the reason is control. Its annual report for 2025 describes "acquiring our own banking licenses in the EU, US, and UK. Operating these licenses ourselves allows us to perform mission-critical activities without relying on partner banks, improving reliability and settlement speed", and says its own licenses provide "the speed and autonomy that come from not relying on external parties for regulatory compliance". The shareholder letter for the first half of 2026 ties the licenses to connectivity: "Our own licensed infrastructure grants direct access to payment networks, giving us control over funds". These are the company's statements of intent, not measurements ([[case-adyen]]).

The same documents show where the route stops. The annual report says: "Of processed volumes, 84% were full-stack volumes, up from 83% in 2024." It names the weak point too: "Concentration risk at Adyen originates primarily at banking partners in locations where there are no own direct acquiring licenses." That sentence is about concentration risk; I read it, as an inference, to mean that Adyen relies on partner banks in some markets. It does not publish which. What it does publish runs the other way: a documentation page on payout currencies (n.d., accessed November 2026) lists 14 countries and regions "For each Adyen acquiring connection", from Australia to the United Arab Emirates, and says Adyen processes a payment "through one of our acquiring entities, for example Adyen Singapore". Its license pages (n.d., accessed November 2026) name an acquiring entity for some markets: Adyen Japan KK holds a "Registration as Merchant Acquirer", Adyen Singapore Pte. Ltd. is licensed for "merchant acquisition", and Adyen N.V. is the licensed bank for the EEA and the UK. No page lists the acquiring entity per country. Its documentation says that "Pass-through payout is the only available payout model in Africa, Brazil, and India" (n.d., accessed November 2026). And it publishes no list of the networks and countries in which it is a principal member: an article on its site (3 July 2026) claims "principal membership of Visa and Mastercard in major markets" without naming the markets, and the French announcement of 2026 is the one membership I found stated for a named network and country.

> **INFERENCE, NOT DOCUMENTED:** The 2025 report does not define "full-stack" in the passage quoted. By Adyen's long-standing usage it means volume Adyen both processes and acquires. On that reading 16% of its processed volume is acquired by someone else. Not all of that need be a partner bank: Adyen's documentation (n.d., accessed November 2026) describes a report of "transactions for which Adyen is not the acquirer", and its examples are American Express and PayPal paying the merchant directly.

## Stripe's Route: Acquirer in Some Countries, Payment Facilitator in Others

Stripe publishes something Adyen does not: a page that names, country by country, the acquirer for Visa and Mastercard payments. The rows below are from "Acquirer Disclosure & Acquirer Terms" (n.d., accessed November 2026); the page is undated, and the list of banks can change.

| Country or region | Stripe's stated role | Acquirer named |
| --- | --- | --- |
| European Economic Area | Acquirer is a Stripe entity | "Stripe Technology Europe, Ltd." |
| United Kingdom, Gibraltar, Switzerland | Acquirer is a Stripe entity | "Stripe Payments UK, Ltd." |
| Australia, New Zealand, Singapore, Malaysia, Hong Kong, Brazil | Acquirer is a Stripe entity | A Stripe entity |
| United States | "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers" | Cross River Bank; Deutsche Bank Trust Company Americas; Fifth Third Bank; Pathward N.A.; PNC Bank, N.A.; Stripe MALPB |
| Mexico | "both a Payment Method Acquirer and a Payment Facilitator" | Stripe's Mexican entity; GetNet México and BBVA México |
| Canada, Japan, Thailand | Payment facilitator | Named local banks or card companies |
| India, United Arab Emirates | "Payment Aggregator"; "Independent Sales Organization (ISO)" | RBL Bank Ltd.; Network International, LLC |

In the EEA and the United Kingdom, then, the acquirer is a Stripe company, and no bank stands between Stripe and the network. Both entities are e-money institutions. The Irish one was quoted above. Stripe Payments UK "is authorised as an electronic money institution by the U.K. Financial Conduct Authority (reference number: 900461)", with the same permission to "acquire payment transactions" (page dated January 2017). **(Evidence age: 9 years; the entity is named as UK acquirer in the current disclosure.)**

In the United States the picture is the opposite and, since 2026, mixed. Stripe is a payment facilitator of five banks. The sixth name, "Stripe MALPB, 505 N Angier Avenue NE, Atlanta, GA", carries its own acquirer terms (last updated 28 May 2026). They call it "a Georgia Merchant Acquirer Limited Purpose Bank" and "a member of the Networks", and say that "Stripe is registered as a Payment Facilitator by Member Bank": the Georgia charter described above, in Stripe's own words. Stripe does not publish how its US volume divides among the six, or whether its own limited-purpose bank acquires for all merchants or for some.

Now the two statements from the introduction fit together. In 2020 Stripe wrote: "By exchanging information directly with the card networks, rather than relying on intermediaries, Stripe can reduce latency and remove potential points of failure". **(Evidence age: 6.5 years; the list of six networks has not been republished.)** Its current product page (n.d., accessed November 2026) says: "Stripe has direct connections to card networks to ensure our data is as rich as possible." Both sentences are about exchanging messages and data. Neither says who the member is. The disclosure page answers that, and for the United States the answer is mostly banks. **Stripe runs the wire; in some countries another institution holds the membership.**

What Stripe has not published is why. I found no statement by Stripe explaining its mix of partner banks and own licenses (newsroom, legal pages, documentation and support site, November 2026). The nearest thing is a trade-press report of April 2025 (secondary source), in which a Stripe spokesperson described the Georgia application as an extension of the company's work to expand the number of banking and other partners it works with. So this chapter compares what the two routes are, and does not claim to know Stripe's reasons. [[case-stripe]] and [[stripe-and-adyen-bets-compared]] return to the question.

## Stripe and Adyen: Where They Differ

The table sets the two documented routes on the same rows. Every Stripe and Adyen cell is a fact cited above or a statement that something is not public; the last column is my inference.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Regulatory form | E-money institutions in the EEA (2019 page) and the UK (2017 page); a limited-purpose bank among its US acquirers (accessed November 2026) | One credit institution (2017), passported across the EEA; US federal branch (2021); UK bank authorization (2023) | Adyen took the widest permission once and reuses it; Stripe holds the narrowest sufficient permission per market |
| Acquirer of record | Published per country (accessed November 2026): Stripe entities in the EEA, the UK, Brazil and much of Asia-Pacific; named banks or card companies in the other countries listed | 14 countries and regions with an "Adyen acquiring connection" listed (n.d., accessed November 2026); its license pages name an entity for some markets (Adyen Japan KK, Adyen Singapore); no page lists the entity per country; "84% were full-stack volumes" (annual report for 2025) | Stripe publishes the legal entity; Adyen publishes the coverage and leaves the entity to its license pages |
| Where a partner bank stands in | United States, Canada, Mexico (beside Stripe's own entity), Japan, India, Thailand, United Arab Emirates, by name: banks, and card companies in Japan (accessed November 2026) | "banking partners in locations where there are no own direct acquiring licenses" (2025); locations not public | Both rely on partners somewhere; only Stripe says where |
| Direct connections | Six networks named in April 2020; "direct connections to card networks" (n.d., accessed November 2026) | "direct access to payment networks" (H1 2026); principal member of the French scheme CB (2026) | No material difference in the public record |
| Stated reason for the route | Not public | "the speed and autonomy that come from not relying on external parties for regulatory compliance" (2025) | Motives can be compared from one side only |
| Measured gain from local acquiring | No isolated figure; one customer story credits 5.5% to direct connections and local processing together (2020) | No isolated figure; one customer case reports 3% across several changes (2024) | No material difference in the public record |

What should you do differently on each? On Stripe, read the acquirer disclosure for every country you sell in, and the acquirer terms that come with it, before you sign: the page tells you whether a bank stands in your flow of funds. On Adyen the documentation lists where it has an acquiring connection but not the entity, so ask, per country, whether Adyen acquires under its own license or through a banking partner, and which payout model applies. On both, ask again each year.

The public record stops in the same three places for both companies. Neither lists its network memberships by network and country: Stripe's acquirer terms call its EEA entity and its US limited-purpose bank "a member of the Networks", and Adyen claims "principal membership of Visa and Mastercard in major markets" (3 July 2026) and names one, CB in France. Neither publishes volume per acquirer: Stripe gives no shares for its six US acquirers, and Adyen's 84% has no published breakdown. Neither publishes a current list of direct connections: Stripe's dates from April 2020, and Adyen's naming of Visa and Mastercard is press boilerplate from 2021.

## In Practice at Larkfield: The Acquirer Inventory

Femke fills in her question from the two providers' public pages. Of the 3,750 Dutch and German studios, 1,140 onboarded before 2024 still take online payments through Stripe, which leaves 2,610 on Adyen. The result shows **four acquiring arrangements behind two providers**.

| Market | Studios | Provider | Acquirer of record, per the provider's public pages (November 2026) | License | Bank between studio and network? |
| --- | --- | --- | --- | --- | --- |
| Netherlands, Germany | 2,610 online; all terminals | Adyen | Adyen N.V. *(my reading of its EEA license page; Adyen publishes no complete list of acquiring entities per country)* | Credit institution, the Netherlands, passported | No |
| Netherlands, Germany; Belgium | 1,140 online; 650 | Stripe | Stripe Technology Europe, Ltd. | E-money institution, Ireland | No |
| United Kingdom | 1,100 | Stripe | Stripe Payments UK, Ltd. | E-money institution, United Kingdom | No |
| United States | 700 | Stripe | One of six named acquirers; Stripe, LLC is the payment facilitator | The acquirer's own charter | Yes, unless the acquirer is Stripe's own limited-purpose bank |

Read Mila's €120 through the first two rows. Studio Noord is a merchant outlet in the Netherlands, and Mila's Visa debit card was issued in the Netherlands, so by Visa's definition the payment is a Domestic Transaction. Its acquirer is Adyen N.V., a Dutch bank. Had Studio Noord been on Stripe, the acquirer would have been Stripe Technology Europe in Ireland, which Stripe names as acquirer for the whole EEA, and the payment would still meet the definition. So **the move to Adyen changed the acquiring entity, from an Irish e-money institution to a Dutch bank, and not whether the issuer sees a domestic payment.** This is my reading of the published Visa rule. It does not cover how a Dutch issuer's own risk model treats the two acquirers, which is not public, and I could not read Mastercard's rule.

Could Larkfield's own data settle what the move did to approvals? It cannot. Assume, as is typical of such migrations, that the studios moved to Adyen also got a new checkout and had members' stored cards collected again. Larkfield's history then has the same flaw as the vendor case studies: several causes, one number, no baseline. Femke records "local acquiring: effect not measured" in the inventory.

The last row is the one that needs work. The United States is the only Larkfield market with a bank between the studio and the network, which means a second set of terms to read and a seller-size limit to watch. Across the platform the average studio takes about €181,000 a year (€1.12 billion over 6,200 studios), far below Visa's USD 1 million threshold, but a chain with several locations could cross it. Femke sends Stripe one question: which of the six acquirers applies to Larkfield's American studios? The public page does not say per account.

## When It Goes Wrong: The Acquirer You Did Not Know You Had

The failures of this layer are not outages. They arrive as a notice of changed terms, a letter from a bank, or an approval rate that sinks over a quarter. Three are worth planning for.

**A sponsor relationship changes.** The provider adds, drops or replaces an acquiring bank. Such partners exist and change: Stripe's undated US list had six names in November 2026, one of them its own new bank, and Adyen's annual report names banking partners as its concentration risk. For the merchant this can mean new acquirer terms and a new path for settlement money. Detection: someone owns the provider's disclosure page and legal notices and reads them. Recovery is mostly the provider's migration; your own part is what Larkfield wrote down as decision K8 of Keel, its 2027 payments program: a second provider and a rehearsed switch ([[payment-routing-and-orchestration]]).

**A seller outgrows the facilitator model.** Once a sponsored merchant passes USD 1 million of annual volume in Visa's rules, the acquirer must sign it directly within two years unless an exception applies. Detection is a yearly report of card volume per seller against the threshold. Recovery is a direct agreement arranged before the deadline; ask the provider how it is formed. The Cross River Bank terms quoted earlier are written to take effect at the threshold.

**An expansion turns domestic customers into foreign ones.** A business starts selling in a new country from its home entity. Under the definitions quoted earlier, that country's cards now reach their issuers as International Transactions, with the lower approval and higher cost that follow. Nothing errors; the rate is simply worse there. This is The Single Rail in its acquirer form. Detection is a report of issuer country against merchant country for every market. Recovery is a legal entity in the new country and a provider whose acquirer covers it.

## What to Take Away

**Established.**

* Acquiring is a right of network membership, and the member needs a regulator's license: Visa's rules define the acquirer as "A Member", and both companies' legal pages name the license under which they acquire.
* The acquirer stays liable for a payment facilitator and its sellers, and above USD 1 million a year must contract with the seller directly, with exceptions (Visa's rules, edition of October 2026).
* A payment is domestic when the issuer and the merchant outlet are in the same country, and an acquirer may serve only the outlets its license reaches.
* Adyen's licenses (2017, 2021, 2023) and Stripe's named acquirers per country (accessed November 2026) are as their own pages state.

**Depends on context.**

* Whether a sponsor bank in the flow matters depends on your sellers: with large ones the bank's terms and the facilitator threshold are live issues; with thousands of small ones they rarely are.
* What local acquiring is worth depends on where your customers' cards are issued. If your merchant entity and those cards are in the same country, you probably have it already.
* The difference between the two routes matters most outside Europe. Inside the EEA and the UK both companies are their own acquirer.

**The author's synthesis.**

* "Which provider" is a commercial question; "which acquirer in this country" is the operative one. The membership, the liability, the first receipt of the money and the domestic status all attach to the acquirer, so I evaluate acquirers per country.
* I give a quoted local-acquiring uplift no weight until it comes with a baseline that holds everything else constant.

## Questions to Ask

1. For each country we sell in, which legal entity is the acquirer of record?
2. Under what license does that entity acquire: a bank, an e-money or payment institution, a special charter?
3. Is a sponsor bank between our provider and the network here, and have we read its terms?
4. When the provider says "direct connection", does it mean it exchanges messages with the network, or that it is the member?
5. Do our main customers' cards reach the issuer as domestic or international payments?
6. When a provider quotes an approval gain from local acquiring, what was held constant, and what is the denominator?
7. Which of our sellers are near the network's payment-facilitator threshold, and who tracks it?
8. Who reads the provider's legal notices, and when was the inventory last checked?

This chapter was about cards, whose networks hand back an issuer's answer within seconds. Some of the local schemes that only a local acquirer or entity can reach are not card schemes at all: they have no issuer answer, no hold on the payer's funds or no chargeback (the network procedure that takes a disputed payment back from the merchant), and what the provider connects to changes what "approved" promises. [[local-payment-methods]] takes them up.

## Sources and Evidence

*Company, product and investor sources*

- [Acquirer Disclosure & Acquirer Terms](https://stripe.com/legal/acquirer-disclosure), Stripe, n.d., accessed 2026-11 — the acquirer named per country, the six US acquirers including Stripe MALPB.
- [STEL Acquirer Terms](https://stripe.com/legal/stel-financial-terms), Stripe, n.d., accessed 2026-11 — Stripe Technology Europe as "a member of the Networks".
- [Stripe MALPB Acquirer Terms](https://stripe.com/legal/stripe-malpb-acquirer-terms), Stripe, last updated 2026-05-28 — Stripe MALPB as a Georgia merchant acquirer limited purpose bank, network member and acquirer, with Stripe registered as its payment facilitator.
- [Cross River Bank Acquirer Terms](https://stripe.com/legal/crb-acquirer-terms), Stripe, last updated 2025-11-18 — a US bank's terms and the USD 1 million threshold at which they take effect.
- [Stripe Services Terms](https://stripe.com/legal/ssa-service-terms), Stripe, last modified 2026-09-28 — the definition of "Payment Method Acquirer".
- [STEL Authorised Payment Services](https://stripe.com/legal/stel), Stripe, 2019-04-05 — the Irish e-money authorization including "acquire payment transactions" (evidence age: 7 years).
- [SPUKL Authorised Payment Services](https://stripe.com/legal/spukl), Stripe, 2017-01-26 — the UK e-money authorization (evidence age: 9 years).
- [Major updates to Stripe's payments platform increase revenue and reliability for businesses](https://stripe.com/en-ca/newsroom/news/direct-platform), Stripe newsroom, 2020-04-23 — direct integrations with six card networks (evidence age: 6.5 years).
- [Authorization Boost](https://stripe.com/authorization-boost), Stripe, n.d., accessed 2026-11 — the current "direct connections to card networks" wording.
- [Local acquiring 101](https://stripe.com/resources/more/local-acquiring-101), Stripe, last updated 2023-08-15 — the direction of the approval and cost effect, without figures (evidence age: 3 years).
- [Twilio increases its authorization rates by 10% with Stripe](https://stripe.com/newsroom/stories/twilio), Stripe newsroom, 2020-11-17 — the 5.5% customer-story figure for direct connections and local processing (evidence age: 6 years).
- [Licenses & Disclosures: EMEA](https://www.adyen.com/licenses/emea) and [United States](https://www.adyen.com/licenses/united-states), Adyen, n.d., accessed 2026-11 — the credit-institution license and its EEA passport, the UK permission, the US federal branch.
- [Adyen granted US branch license](https://www.adyen.com/press-and-media/adyen-granted-us-branch-license), Adyen, 2021-06-14 — the Comptroller's approval; European license "obtained in 2017" (evidence age: 5 years).
- [Adyen granted UK banking authorization](https://www.adyen.com/press-and-media/adyen-granted-uk-banking-authorization), Adyen, 2023-09-07 — the UK authorization (evidence age: 3 years).
- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., signed 2026-03-05 — the 84% full-stack share, banking partners as concentration risk, the stated reasons for its own licenses.
- [H1 2026 Shareholder Letter](https://investors.adyen.com/financials/h1-2026-c2a1a) and [H1 2026 results release](https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne), Adyen, 2026-08-13 — "direct access to payment networks"; France's clearing system and CB membership.
- [Global acquiring](https://www.adyen.com/global-acquiring), Adyen, n.d., accessed 2026-11 — the local processing statement.
- [What's an acquiring bank and why you need one](https://www.adyen.com/knowledge-hub/acquiring-bank), Adyen, n.d., accessed 2026-11 — acquirers licensed by regulators and card schemes.
- [Credit card processing fees: what determines your rate and why the lowest isn't always the cheapest](https://www.adyen.com/knowledge-hub/credit-card-processing-fees), Adyen, 2026-07-03 — "principal membership of Visa and Mastercard in major markets" (vendor claim, no list).
- [Licenses and disclosures: Japan](https://www.adyen.com/licenses/japan) and [Singapore](https://www.adyen.com/licenses/singapore), Adyen, n.d., accessed 2026-11 — Adyen Japan KK's registration as merchant acquirer; Adyen Singapore's license for merchant acquisition.
- [Klook boosts revenue with payments optimization](https://www.adyen.com/knowledge-hub/klook-takes-off-payments-optimization), Adyen, 2024-08-05 — the 3% uplift customer case.
- [Getting paid](https://docs.adyen.com/account/getting-paid.md), Adyen documentation, n.d., accessed 2026-11 — pass-through payout markets.
- [Supported payout currencies](https://docs.adyen.com/account/supported-currencies.md), Adyen documentation, n.d., accessed 2026-11 — the 14 countries and regions with an Adyen acquiring connection; "one of our acquiring entities".
- [External settlement detail report](https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report.md), Adyen documentation, n.d., accessed 2026-11 — transactions for which Adyen is not the acquirer.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1512673/000162828026012254/xyz-20251231.htm), Block, Inc., 2026-02-26 — a payment facilitator without direct network access for most transactions.

*Standards, regulation and official documentation*

- [Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf), Visa, 2026-10-24 — definitions of acquirer, acquirer processor, payment facilitator, domestic and international transaction; sponsor liability; acquirer jurisdiction (1.5.1.1); facilitator liability (5.3.1.2) and the USD 1 million threshold (5.3.1.4).
- [Federal Reserve Board announces approval of application by Adyen, N.V.](https://www.federalreserve.gov/newsevents/pressreleases/orders20210524a.htm), Federal Reserve, 2021-05-24 — the US branch approval (evidence age: 5 years).

*Research and practitioner sources*

- [Georgia approves Stripe application to form MALPB](https://www.icba.org/w/georgia-approves-stripe-application-to-form-malpb), Independent Community Bankers of America, 2025-07-08 — the charter's scope and approval (secondary source).
- [Financial Institutions Today, May 2026](https://dbf.georgia.gov/financial-institutions-bulletin-2026), Georgia Department of Banking and Finance, 2026-05 — Stripe MALPB: approved 30 June 2025, began business 28 May 2026.
- [Stripe seeks Georgia special banking charter](https://www.bankingdive.com/news/stripe-georgia-special-banking-charter-credit-card-payments/744921/), Banking Dive, 2025-04-07 — the Stripe spokesperson's description of the application (secondary source).
- [Stripe's John Collison On Art Of Authorization](https://www.pymnts.com/digital-payments/2020/stripes-john-collison-on-improving-the-art-of-authorization-amid-a-digital-payments-boom/), PYMNTS, 2020-04-23 — the "half a percentage point" remark on direct connectivity (secondary source; evidence age: 6.5 years).
- [[payments-fundamentals]] in RECONCILED — the finance-side treatment of the parties and of acquiring.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
