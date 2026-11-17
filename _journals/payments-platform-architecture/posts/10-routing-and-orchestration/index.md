---
title: "More Than One Provider: Routing and Orchestration"
date: 2026-11-17
author: Željko Obrenović
excerpt: "When should payments be routed across providers, and what does it cost? Only when each segment has enough payments to measure a difference between routes; otherwise a second provider is a rehearsed failover, and in both cases disputes, settlement, balances and stored cards stay one set per provider."
permalink: payment-routing-and-orchestration
timetoread: 24 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what a routing layer across payment providers unifies, what stays per provider, and when a simple rule with a rehearsed switch is the better design.

> **KEY POINTS:**
>
> * **A routing layer unifies the authorization request and nothing after it.** Disputes, settlement, balances, payment-method coverage and stored cards stay one set per provider. Stripe's documentation for its own Orchestration product (private preview, November 2026) puts most of these outside it. Running the second set is what a second provider costs.
> * **Routing per payment pays only where each segment can be measured.** Telling two routes apart by half a percentage point takes on the order of 100,000 payments per segment (issuer, country, card type). Below that, a second provider is a failover you trigger on purpose and have rehearsed.
> * **The vault decides how you leave.** A stored card is a token that works only at the provider holding the card number. Settle who holds the vault and how cards leave before adding a provider. On network tokens, Adyen's terms (2025) describe a service that shares them for use with other providers, with the cryptogram still from Adyen; I found no Stripe statement.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Single Rail** — every payment depends on one provider; the remedy defended here is a second provider with a rehearsed switch, not a routing product.
> * **The Vault Hostage** — stored cards exist only as one provider's tokens, so the vault's location decides whether a second provider can charge them at all.
> * **The Double Charge** — a timeout retried on another provider charges the customer twice, across two providers that share no idempotency key.

<br>
For forty minutes on a Friday evening, your one payment provider approves four card payments in five instead of nine in ten. Nothing is down; one connection to one card network in one country is degraded. On Monday everyone proposes the same remedy: **add a second provider, and put a layer in front of both that sends each payment to whichever is performing best.** The previous chapter ended there too: every lever sits inside one provider. Why, then, does the most detailed public account by a merchant say it takes close to thirty people?

This chapter keeps half of the remedy. A second provider answers the forty minutes, provided the switch to it is triggered on purpose and has been rehearsed. **Routing each payment to the "best" provider is a different project.** It pays only where every segment of your traffic (an issuer, meaning the bank that issued the card; a country; a card type) has enough payments for a difference between routes to be measured. Either way the layer unifies one thing: the authorization request, the message that asks the cardholder's bank to approve. Disputes, settlement, balances, payment methods and stored cards **stay one set per provider**, and running those sets is what a second provider costs.

**Where we are in the payment's journey.** When Mila Janssen buys her €120.00 ten-class pass from Studio Noord at 19:42 on Tuesday 9 March 2027, routing happens first. Before authorization, the payment service of Larkfield (the fictional studio-software platform this book follows) looks up Studio Noord and finds Adyen. The settlement, the payout of Thursday 11 March and any refund or dispute then follow as Adyen's records.

The chapter starts with a proposal at Larkfield, separates routing inside one provider from routing across providers, shows what a routing layer unifies, and takes up the hard part, stored cards and network tokens. Then come the stages and ways to build the layer, the evidence for when routing pays, Stripe and Adyen compared, Larkfield's own rule, and the failures. [[payments-fundamentals]] in RECONCILED covers orchestration from the finance side.

## Setting the Scene at Larkfield: The Proposal to Route Every Payment

In February 2027, during planning for Keel, the program meant to steady Larkfield's payments estate ([[meet-larkfield]]), CTO Daniel Osei brings a proposal. Larkfield already has two providers: across its 6,200 studios, Stripe carried 44% of 2026 member payment volume (€493 million) and Adyen 56% (€627 million). Why not buy an orchestration product and send each card payment to whichever approves more?

What exists today is much smaller. The payment service that Tom Hendriks built in 2024 has one internal API and one adapter per provider. Its routing rule never looks at the payment. It looks at the studio: **"the studio's provider"**, with a manual override. Studio Noord is on Adyen, so Mila's payment goes there.

Femke de Graaf, who has led payments engineering since January, answers with three questions on the whiteboard. **What would the layer unify, and what would Larkfield still run twice? Where would the stored cards live? Does Larkfield have the evidence to choose a route for each payment?**

## Two Kinds of Routing: Inside a Provider and Across Providers

**Routing** is the choice of path for one payment. A **routing rule** is the stated condition that makes the choice: "US debit cards go over the cheaper network", or "payments for this studio go to this provider". The choice exists at two levels, inside a provider and across providers, and they differ in what you must operate afterwards.

Inside one provider, routing chooses among the provider's own acquiring routes (an **acquirer** is the licensed entity that submits a payment to a card network for the merchant; see [[acquiring-and-network-connectivity]]), among the networks a card can travel on, and among the provider's connections to them. Stripe's guide to authorization rates (n.d., accessed November 2026) says it "can dynamically route payments to the best connections" when a processor is down. Adyen's documentation for partners (n.d., accessed November 2026) describes a setting, "off by default", that routes "each transaction to the highest-converting or lowest-cost acquirer or network". Either way you keep one contract, one set of reports and one place to handle disputes.

The best-documented case is US debit. A US debit card can be processed on a global network such as Visa or Mastercard and on a domestic debit network such as PULSE or STAR, because the Federal Reserve's Regulation II (n.d., accessed November 2026) forbids restricting debit processing "to less than two unaffiliated networks" and forbids "inhibiting a merchant's ability to direct the routing of a debit transaction over any network that the issuer has enabled to process it". A Federal Reserve press release of 3 October 2022 announced an update, effective 1 July 2023, specifying that the requirement covers card-not-present payments such as online ones **(evidence age: 4 years; the Federal Reserve's current Regulation II page states the two-network rule without these dates)**. **Least-cost routing** is the use of that right: send each debit payment over whichever network costs you less in fees ([[payment-economics]]).

The two companies built different things on it. On 9 September 2024 Adyen announced Intelligent Payment Routing for US debit and reported that in "a pilot of over 20 enterprise merchants" it "achieved an average of 26% cost savings with a 0.22% uplift in authorization rates against earlier debit performance". That is a vendor's before-and-after figure with no control group. Adyen's documentation (n.d., accessed November 2026) lets the merchant set network priorities, "For example, 1: PULSE and 2: Visa": a routing rule held inside the provider. Stripe's documentation (n.d., accessed November 2026) says only that Adaptive Acceptance, its in-request retry feature ([[authorization-optimization]]), "might automatically retry an eligible transaction on a US debit network (also known as PINless network) after it's declined on an international network". I found no Stripe page on first-attempt least-cost routing of US debit, which says what is published, not what Stripe does. Stripe does document it for another market: its support site (n.d., accessed November 2026) says "Stripe automatically implements least-cost routing for all of its Australian merchants", whose debit cards often carry the domestic eftpos network.

Routing across providers is the other level, and the industry calls it **payment orchestration**: a layer in front of two or more providers that decides, per payment, which one processes it. Its simplest use is **failover**, sending payments to a second provider when the first is failing. At Stripe's Sessions conference in April 2026, Alex Ginet of Stripe offered three motives: "redundancy and reliability", "performance and cost optimization", and "geo expansion". The first level adds no contract and no back office. The second does, and it is the subject from here on.

## What a Routing Layer Unifies, and What It Leaves Per Provider

Whoever builds it, a routing layer has five parts. One **payment API** that the rest of the business calls. A **rule engine** that picks a provider. An **adapter** per provider, which translates the request into that provider's API and its answers into one vocabulary of outcomes ([[payment-state-machines]]). A **credential store**: some way for every adapter to reach the card being charged. And an **attempt record** of which provider was tried and what it answered. The figure below draws these above a line; below it is what each provider keeps.

<!-- illustration-placeholder
{
  "id": "10-routing-layer-anatomy",
  "status": "pending",
  "asset": "assets/images/10-routing-and-orchestration/10-routing-layer-anatomy.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that lists the five parts of a routing layer",
  "visual_goal": "Show the line between the shared layer and what each provider keeps.",
  "prompt": "Create a component-layout illustration split by a bold horizontal dashed line. Above the line, a wide rounded box holds five small blocks in a row labeled 'Payment API', 'Rules', 'Adapters', 'Card store', 'Attempt record'. An arrow named 'payment request' enters the wide box from a small shop icon at the top left. From the 'Adapters' block two arrows named 'authorization' go down across the dashed line, one to a blue box labeled 'Provider A' on the lower left, one to a teal box labeled 'Provider B' on the lower right. Under each provider box draw the same four small items: a folder labeled 'Disputes', a calendar labeled 'Settlement', a coin stack labeled 'Balance', a sheet labeled 'Reports'. Left edge: a bracket above the line labeled 'Shared', one below labeled 'Per provider'. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Five shared parts above a dashed line; two providers below, each with its own back office.",
  "caption": "A routing layer shares five parts; disputes, settlement, the balance and the reports stay one set per provider."
}
-->

The most precise public description of where the line runs comes from a company that sells such a layer. Stripe previewed **Stripe Orchestration** on 7 May 2025, and its documentation still said "Orchestration is in private preview" on 17 November 2026. It routes card payments to Adyen, Braintree or Worldpay's WPG gateway. A rule is a condition on the amount, the currency, the card's country, issuer, type or BIN (bank identification number: the leading digits of the card number, which identify the issuer), or metadata attached to the payment. "Stripe executes the conditions in order, from left to right, and applies the first action that matches a payment's condition", and each action names a main processor and, optionally, one retry processor.

Now read what the same documentation leaves behind. The commercial relationship: "All related activity (including payment processing fees and liability for transaction losses) remain subject to the terms that you agreed to with that processor." The money and the arguments about it: "Orchestration also doesn't support disputes or settlement-related activity. To manage these activities, access your third-party processor's dashboard." (A dispute is a cardholder's challenge through their bank, which reaches the merchant as a chargeback; settlement is the movement of the money.) And the breadth: feature support "doesn't include non-card payments or Link, Capital, Connect, Terminal, or Organizations", so local methods ([[local-payment-methods]]), platform payments and in-person payments are outside it.

The exclusions reach the merchant's own systems, because a payment routed elsewhere moves no money through Stripe. "Stripe creates Payment Records and Payment Attempt Records instead of Charges for payments routed to other processors". The **balance**, the provider's running account of the money it holds for you ([[balances-and-funds-flows]]), is not touched: "If your back-end systems assume there's always a Balance Transaction after a successful payment, that's no longer true." Even the comparison between routes is partial: Stripe's analytics cannot show an authorization rate for another processor, because "Stripe doesn't have access to non-Stripe data."

Nothing in that list is peculiar to one product in preview. Joshua Barton of Canva, which built its own layer, described the same line in the 2026 talk: "when you're doing chargebacks or you're doing refunds, your operations team now has to go into a second portal". **The middle column is what a second provider costs**, and most of it is the subject of [[part-3]]. One cell on the left carries a condition, the subject of the next section.

| Unified by the routing layer | Stays one set per provider | Where the book covers it |
| --- | --- | --- |
| The payment request and one vocabulary of outcomes | The contract, the pricing and the merchant account | [[payment-economics]] |
| The routing rules | Disputes, with their evidence and deadlines | [[refunds-reversals-and-disputes]] |
| The record of attempts | Settlement, the balance and payouts | [[balances-and-funds-flows]] |
| The credential store, only if the layer itself holds the vault | Settlement reports and reconciliation | [[payment-reconciliation-and-reporting]] |
| | Non-card methods and provider-specific features | [[local-payment-methods]] |

## The Hard Part: Stored Cards and Network Tokens

When a customer saves a card, your systems receive a **provider token**: a reference to the card number, which itself sits in the provider's **vault**, its store of card data built to PCI DSS, the Payment Card Industry Data Security Standard ([[tokenization-vaulting-and-pci]]). The token means something only at that vault. A second provider cannot charge it, and you cannot copy the card across, because the design that keeps card numbers out of your systems means you never had them. This is The Vault Hostage. At Larkfield, recurring memberships are 61% of online volume, about 940,000 renewals a month, of which about 540,000 are charged to a stored card *(assumption, from [[authorization-optimization]])*.

The vault can live in three places, shown in the figure below. **At one provider**: the second provider reaches those cards only if the first passes them along. **At an independent vault or orchestrator in front of both**: this is what Spreedly's homepage (n.d., accessed November 2026) sells, "Hold every credential in your own vault, use it with any provider", at the price of a new vendor on which every payment depends. **At each provider separately**: every card stored twice and kept in step.

<!-- illustration-placeholder
{
  "id": "10-where-the-vault-lives",
  "status": "pending",
  "asset": "assets/images/10-routing-and-orchestration/10-where-the-vault-lives.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that names the three places a vault can live",
  "visual_goal": "Make the location of the card vault the visible design decision.",
  "prompt": "Create a three-panel conceptual illustration, panels side by side, separated by thin vertical lines. Each panel shows a merchant shop icon at the top holding a small key tag labeled 'token', and two provider buildings at the bottom, a blue one on the left and a teal one on the right. An orange safe with a card symbol on its door is the card vault. Panel 1, labeled 'At one provider': the safe sits inside the blue building, and a thin dotted arrow named 'forward' runs from the safe to the teal building. Panel 2, labeled 'In front of both': the safe sits between the shop and the buildings, with two solid arrows named 'charge' going down from it, one to each building. Panel 3, labeled 'At each provider': one safe inside each building, joined by a double-headed dashed arrow named 'keep in step'. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A card safe at one provider, in front of two, and at each.",
  "caption": "The card vault can live at one provider, in front of both, or at each; the merchant holds only tokens in every case."
}
-->

For the first arrangement both companies document a **forwarding proxy**. You send a request addressed to a third party with placeholders for the card details; the provider fills them in from its vault and sends it on. Stripe's Vault and Forward API (n.d., accessed November 2026) is "available only to businesses with a dedicated Stripe account team" and forwards to a published list of destinations that includes Adyen, Braintree, Worldpay and Spreedly. Adyen's documentation (n.d., accessed November 2026) says: "You can forward payment details that you stored with Adyen to a PCI compliant third party, like a payment service provider (PSP). We support forwarding card details, and network tokens." Adyen's support must enable it; the page lists no destinations.

The second way out moves the cards themselves, in bulk, from one provider to another. Stripe documents it as policy (n.d., accessed November 2026): "We believe our customers own the sensitive data they entrust to Stripe." It "can only transfer your card data to another PCI DSS Level 1-compliant payment processor", and it "doesn't export your account's payment history, subscriptions, or other objects". Adyen documents the inbound direction, noting that "migrating payment data usually takes 10 days or more"; I found no Adyen documentation page that describes an export. Adyen's help center lists an article titled "How can I prepare for token migration? [Export]", but on 17 November 2026 its link led to the general tokenization page, which says nothing about exports, so I could not read the procedure. Either way this is a migration of weeks, not a failover.

Card numbers are half of what is stored. The other half is the **network token**: a stand-in for the card number, issued by the card network, which stays valid when the card is reissued ([[network-tokens]]). A network token is issued to the party that asked for it, the **token requestor**. If your provider asked, the token is typically the provider's to use. Adyen's documentation states the consequence: "Network tokenization is only applicable for payments acquired by Adyen. It cannot be used with external acquirer connections." The same page has a second option, to manage network tokens yourself: "you can keep your existing network tokens and use them in the payment requests that you send to Adyen". Independent vaults make the merchant the requestor: Spreedly's documentation (n.d., accessed November 2026) describes "allowing merchants to request network tokens using their merchant-specific TRID", a token requestor ID.

Here the public record is thin. Stripe's export page does not mention network tokens, and Adyen's forward page sends one to a third party a request at a time. Adyen's terms for additional services (last updated 13 June 2025) describe a Network Token Sharing Service that shares network tokens with a customer "to store and/or use to process payments with other payment providers"; a cardholder's payment elsewhere still needs a one-time cryptogram from Adyen ([[network-tokens]]). I found no Stripe statement on whether tokens it requested can follow a merchant, and neither company documents under whose requestor identifier it provisions them. So three **exit questions** go to every provider before a second is added. Who holds the vault? Under whose identifier are network tokens issued? And how, how fast and at what cost do cards leave?

> **INFERENCE, NOT DOCUMENTED:** Tokens requested under a provider's own identifier probably stay with that provider when the card numbers leave, unless a sharing service such as Adyen's was enabled, so the new provider would request fresh ones. No document from Stripe or a card network read for this chapter confirms or denies this.

## Three Stages, and Three Ways to Build the Layer

There are three stages of running more than one provider, and what separates them is what the routing decision looks at, not how many providers there are. **Stage one** is one provider, which routes internally. **Stage two** is two providers with a fixed assignment (by country, business line or account) and a switch that moves traffic when needed. **Stage three** is rules that choose a provider for each payment. Canva, by Barton's account, noticed it had crossed into stage three only when it added a third provider. For the last two someone has to build the layer.

**Build it in-house.** You control the rules, the retries and the vocabulary. Larkfield's payment service is the small form: two adapters and a lookup. Each provider is an integration to keep current, and the services that keep stored cards working are extra. Jon Krauss of Stripe, in the same talk, named network tokenization and the card account updater (a network service that supplies new details when a card is replaced): "those are independent integrations themselves with the schemes."

**Buy a dedicated orchestrator.** A category of companies sells the adapters and an independent vault as a service. Spreedly, Primer, Gr4vy and the open-source Hyperswitch are examples; Hyperswitch's own description (n.d., accessed November 2026) promises routing "to the PSP with the highest predicted auth rate". Such statements are marketing, not results. The trade, in Krauss's words, is that "there are added milliseconds to the end-to-end transaction flow" and that an orchestrator "creates concentration risk with the orchestrator themselves". Barton's test for a buyer was the depth of each integration, not the number: "no one's going to use 400 PSPs".

**Use one provider's orchestration product.** There is no new vendor, and the vault stays where it is. But the orchestrator is also one of the routes, and its documented defaults show it. In Stripe's product, "If you don't have active rules, payments route to Stripe"; "Link transactions are automatically excluded from your routing rules and always processed on Stripe" (Link is Stripe's own wallet); and with the optional error protection, a payment that needs a feature the chosen processor lacks goes to Stripe. The host is where a payment goes when a rule does not apply. As of November 2026, of the two companies only Stripe offers this option, and in private preview.

## When Routing Pays: One Merchant's Account and the Arithmetic of Segments

Which stage is worth its cost? The public evidence is mostly one talk. At Stripe Sessions in April 2026, Joshua Barton, product lead for global payments at Canva, described a layer built in-house over five providers. The motive was availability: "the real reason why we did this was redundancy. We accept payments in over 190 countries". It paid off, he said, when a provider was degraded without being down, which uptime figures do not count.

The larger gain was unplanned: "What we didn't realize at the time was actually the real power is where you send the traffic the first time." First by country; then by issuer, because "country is not the real signal. It's going to be BIN and issuer"; then by separate merchant accounts: "you had a mid for good traffic, a mid for bad traffic". A **MID**, or merchant ID, is the account number an acquirer gives a merchant.

Then the price. In Barton's words, "it takes maybe six months or more to integrate a new PSP and that's engineering time", and that comes after the contract and the provider's verification of the business. Then "you're spending three-plus months warming up" the new merchant account, which by his account does not perform like an established one at first. In people: "once you start including operational people, it's close to 30 people just working on this." His verdict was still "it's worth it, so do it".

Why does scale matter? A routing rule claims that one route approves more than another for some segment, and a claim has to be measured. Assume a segment approves 90% of its payments on one route *(assumption)*, and you want to know whether another is half a percentage point better. The standard sample-size formula for two proportions (5% significance, 80% power) asks for roughly 16 × p × (1 − p) ÷ d² payments per route: 16 × 0.90 × 0.10 ÷ 0.005², about **57,000 per route**, or 115,000 in that one segment for one test. Half a point is the size Stripe's Ginet used in the talk to illustrate the gain, worth "$500,000 in revenue" to a business processing a hundred million dollars a year. Every issuer, country and card type the rule distinguishes needs its own 115,000.

That is where the evidence ends. Canva's is the one detailed merchant account I found, given on a provider's stage in a session that also presented that provider's product. **No audited or independent comparison of approval rates with one provider and with several is public**, and neither Stripe nor Adyen publishes the scale at which routing pays.

The rule I draw is staged. Stay on one provider until an outage you cannot tolerate, or a market it cannot serve, forces a second. Then run two with a fixed assignment and a rehearsed switch. Add per-payment rules only for segments large enough to test; copying them from a far larger company is The Borrowed Blueprint.

| Stage | The routing decision | What it adds to operations | Right when |
| --- | --- | --- | --- |
| One provider | None of yours; the provider routes internally | Nothing | Its outages are tolerable and it covers your markets |
| Two providers, fixed assignment, rehearsed switch | A lookup and a deliberate switch | A second integration and a second set of disputes, settlement, payouts and reconciliation; rehearsals | An outage costs more than the second back office, or one provider cannot serve a market or channel |
| Per-payment rules | Conditions on issuer, country and card type; a first route and a retry route | The above, plus a shared vault, measurement per segment, warm merchant accounts and people to tune rules | Segments are large enough to test (about 115,000 payments each under the assumptions above) |

## Stripe and Adyen: Where They Differ

The table gathers what each company documents; its last column is my reading and is inference. One row needs a new fact. Adyen's Multi pay-in (n.d., accessed November 2026) "is currently in pilot phase" and lets a platform "combine payments processed by Adyen with third-party acquired volume". Stripe said on 29 April 2026 that it had previewed, for European marketplaces, "unified payouts through Stripe" while they keep several providers. Both consolidate funds after the payment. Neither routes authorizations.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Routing payments to another provider | Orchestration: previewed May 2025, private preview on 17 November 2026; cards to Adyen, Braintree, Worldpay WPG | No product that routes payments to other providers by rule found in public documentation; payments settled by an external acquirer, such as a merchant's own American Express agreement, are reported separately (documentation, n.d.) | Stripe is willing to be the control layer over competitors; Adyen is not |
| Routing inside the provider | Across its own connections; US debit network as a retry path (documentation, n.d.); first-attempt least-cost routing documented for Australia (support site, n.d.), not found for US debit | Among acquirers and networks, off by default (documentation, n.d.); US debit product since September 2024 | Adyen exposes internal routing as a merchant setting; Stripe documents it as done for you |
| Forwarding stored cards | Vault and Forward: account team, published destinations (documentation, n.d.) | `/forward`: enabled by support, cards and network tokens, no published destinations (documentation, n.d.) | No material difference in the public record |
| Bulk export of cards | Documented policy with conditions (documentation, n.d.) | Import documented (documentation, n.d.); an export article is listed in the help center but could not be read on 17 November 2026 | Ask Adyen for the procedure in writing first |
| Other providers' funds on a platform | Unified payouts, previewed April 2026 | Multi pay-in, in pilot (documentation, n.d.) | Both accept that platforms keep several acquirers |

Why would a provider help you use its competitors? Stripe's stated answer came from Krauss in 2026: "Stripe Orchestration is an investment in a broader strategy of an open architecture. You're not going to have to be locked into Stripe." Adyen's public argument runs the other way; its product page (n.d., accessed November 2026) says: "Unlike fragmented legacy architectures, Adyen brings payments onto one single platform". [[stripe-and-adyen-bets-compared]] takes the contrast further.

> **INFERENCE, NOT DOCUMENTED:** Stripe sells checkout, billing, fraud screening and a vault as products that can sit above another company's processing, so holding that layer may be worth more to it than carrying every authorization. Adyen's argument rests on carrying the payment itself. Neither company has said this.

For an integrator the difference is practical. On Stripe, treat Orchestration as its documentation describes it: a card-only preview with written exclusions, among them Connect, which rules it out for platforms today. On Adyen, expect to build the layer or buy it elsewhere, and ask at contract time how cards and network tokens leave. On both, get the three exit answers in writing.

## In Practice at Larkfield: One Rule and a Rehearsed Switch

Femke's first answer to Daniel is structural. Larkfield is a platform: members pay studios, and each studio's money sits in a balance at one provider until it is paid out ([[platform-payment-models]]). A payment for Studio Noord sent to Stripe would arrive where Studio Noord has no balance to receive it. That is why the rule is per studio; Stripe's product, which excludes Connect, would not cover member payments anyway. Providers can still be mixed by channel: 1,140 Dutch and German studios take online payments on Stripe and use Adyen terminals at the front desk.

The second answer is statistical. Cards are 52% of Larkfield's €910 million online volume. Applying that share to its 27.6 million online payments *(assumption: share by count equals share by volume)* gives about 14.4 million card payments a year, 1.2 million a month, across five countries. A test needing 115,000 payments in one segment would take a tenth of all card traffic for a month. Existing data cannot stand in for a test, because the provider is tied to the country (the United Kingdom, the United States and Belgium on Stripe; the Netherlands and Germany mostly on Adyen): comparing approval rates today compares countries, issuers and card types at once.

So Larkfield keeps the rule and invests in the switch: Keel decision K8, two providers and one rehearsed switch. Each of the 50 largest studios keeps a verified account at both providers. Thrown for Studio Noord on 9 March, the switch would send Mila's €120.00 pass to Stripe without trouble, because she pays from her phone's wallet and a wallet payment brings its own credential. Her €49.00 membership is different. It renews on the 1st against the card she typed in on 12 January, and that card is stored at Adyen. The renewal stays with Adyen, or waits for Adyen. The switch is a failover for payments that bring their own credential; moving stored cards is a migration.

The rehearsal exercises the per-provider column. Each quarter, for each of the 50 studios, the team sends real payments through the second provider and follows them to the payout, a refund and the reconciliation of both providers ([[payment-reconciliation-and-reporting]]). It also keeps Larkfield's exit answers current.

| Exit question | Larkfield's answer in 2027 |
| --- | --- |
| Who holds the vault? | Each provider holds the cards saved through it; Larkfield holds only provider tokens (decision K4) |
| Under whose identifier are network tokens issued? | Each provider's own, as far as Larkfield has been told; treated as not portable |
| How do cards leave? | By transfer from provider to provider, planned in weeks; never part of the switch |

## When It Goes Wrong

The first failure is the expensive one. The layer sends a payment to provider A and gets no answer. It is configured to retry failed payments on provider B, so it does, and B approves. But A had approved too; its answer was lost in the timeout. The customer has two charges at two providers that cannot see each other. Inside one provider an idempotency key lets a retry be recognized as a repeat ([[idempotency-and-retries]]); across two there is no shared key, so this is Larkfield's Double Charge of 1 November 2026 (1,840 members charged twice, €71,300 refunded) without the remedy. **A timeout is an unknown outcome, not a failure. Retry on another provider only when the first attempt is known to have failed**; until then, ask the first provider what happened. Stripe's product holds back in a similar case: when 3-D Secure (the protocol by which the issuer authenticates the cardholder; [[three-d-secure-and-sca]]) was attempted and the payment still failed, "Orchestration doesn't retry the transaction on the retry processor".

<!-- illustration-placeholder
{
  "id": "10-cross-provider-retry",
  "status": "pending",
  "asset": "assets/images/10-routing-and-orchestration/10-cross-provider-retry.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on retrying a timeout on another provider",
  "visual_goal": "Show how a timeout followed by a retry elsewhere produces two charges.",
  "prompt": "Create a sequence-style illustration with four vertical lanes from left to right: a customer with a phone, a box labeled 'Routing layer', a blue building labeled 'Provider A', a teal building labeled 'Provider B'. Arrow 1 named 'pay' goes from the customer to the routing layer. Arrow 2 named 'attempt 1' goes from the routing layer to Provider A. A return arrow named 'approved' leaves Provider A toward the routing layer but breaks off halfway at an orange lightning mark beside a small clock labeled 'timeout'. Arrow 3 named 'retry' goes from the routing layer past Provider A to Provider B, and a return arrow named 'approved' comes back from Provider B to the routing layer. At the bottom left, beside the customer, a phone screen shows two identical orange charge lines, each with a euro sign, under a small label 'Charged twice'. Above the broken arrow, a tag labeled 'Unknown, not failed'. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A timed-out approval at Provider A, a retry approved at Provider B, a customer charged twice.",
  "caption": "A timeout is an unknown outcome: retried on Provider B while Provider A had approved, one purchase becomes two charges."
}
-->

The second failure appears on the day of the outage. A failover that has never carried traffic meets three per-provider facts at once. The second merchant account is cold; Canva spoke of three months of warm-up. A feature the payment uses is missing on the other side; in Stripe's product such a request "fails with a `400` error code `orchestration_unsupported`". And 3-D Secure authentication was set up for the other acquirer; Stripe makes the merchant responsible for supplying the acquirer BIN of the processor a payment is routed to. This is The Single Rail with a second rail nobody has driven on, and only a rehearsal with real payments detects it.

The third arrives weeks later. Refunds and disputes go back to the provider that took the original payment; Stripe says of its own product, "For payments routed to third-party processors, those processors administer the refunds." Had Studio Noord been switched in mid-March, Mila's €84.00 refund of 18 March would still be an Adyen refund, and a dispute like Bram de Wit's, which arrived three weeks after his €120.00 purchase, would reach whichever provider had processed it. Both back offices stay staffed for as long as disputes can arrive, which is months ([[refunds-reversals-and-disputes]]). A switch that forgets this produces The Orphaned Refund.

## What to Take Away

**Established.**

- Providers route inside their own networks, and Stripe and Adyen both document it. This adds no contract and no back office.
- In the United States a debit card must work on two unaffiliated networks, and the merchant may choose (Regulation II; spelled out for online payments from 1 July 2023).
- A provider token works only at the vault that issued it. The documented ways out are a forward, one request at a time, and a transfer from provider to provider.
- Stripe's documentation of its Orchestration product (private preview, November 2026) puts disputes, settlement, non-card methods and platform payments outside it.

**Depends on context.**

- Add a second provider when an outage costs more than a second back office, or when one provider cannot serve a market or channel. Otherwise one is the right number.
- Hold the vault with an independent party if you expect to change providers or route per payment; otherwise accept that leaving is a migration of weeks. Build the layer only if you can staff it for years.
- Per-payment rules pay where a segment is large enough to test. Canva says the gain is real at its scale; nothing public says where that scale begins.

**The author's synthesis.**

- A provider is not a route. It is where the cards, the money and the records of every payment it took live. Routing can be shared because it happens before any of those exist. So I settle the exit before the entry.
- I keep the routing rule as simple as the evidence per segment allows and spend the effort on the switch.

## Questions to Ask

1. Which problem is this for: outage, market, cost or approval rate? Can routing inside our provider solve it?
2. Who will hold the card vault, and can every provider we plan to use charge a card stored there?
3. Under whose token requestor identifier are our network tokens issued, and what happens to them if we leave?
4. How do cards leave each provider: by what procedure, in how many weeks, at what fee?
5. How many payments a month does each segment we would route by have?
6. When an attempt times out, how does the layer learn the outcome before it tries another provider?
7. Who works disputes, refunds and reconciliation for the second provider, and for how long after a switch?
8. When did real payments last go through the second route, through to payout and refund?

Return to the forty minutes. A second provider with a rehearsed switch answers them. The layer that picks the best provider per payment needs more volume per segment than most teams have, and Canva's close to thirty people include the operations staff who work in each provider's portal, which no layer removes. This whole part has assumed a payment made at a distance. Larkfield's 1,140 studios with one provider online and another at the counter point at what is missing. [[in-person-payments]] puts the card in the room.

## Sources and Evidence

*Company, product and investor sources*

- [Orchestration](https://docs.stripe.com/payments/orchestration), Stripe documentation, n.d., accessed 2026-11 — private preview status, features, the processor's contract and liability, exclusions (non-card payments, Link, Connect, Terminal, disputes, settlement), refunds administered by the other processor.
- [Route payments to multiple processors](https://docs.stripe.com/payments/orchestration/route-payments), Stripe documentation, n.d., accessed 2026-11 — Payment Records in place of Charges, no Balance Transactions for routed volume, Link always on Stripe, the acquirer BIN for 3D Secure.
- [Manage rules](https://docs.stripe.com/payments/orchestration/rules), Stripe documentation, n.d., accessed 2026-11 — rule conditions, first-match order, routing to Stripe without active rules.
- [Cross-processor retries with Orchestration](https://docs.stripe.com/payments/orchestration/retries), Stripe documentation, n.d., accessed 2026-11 — no retry after a 3D Secure attempt.
- [Supported Orchestration features](https://docs.stripe.com/payments/orchestration/feature-support), Stripe documentation, n.d., accessed 2026-11 — the three processors, `orchestration_unsupported`, error protection.
- [Forward card details to third-party API endpoints](https://docs.stripe.com/payments/vault-and-forward), Stripe documentation, n.d., accessed 2026-11 — the Vault and Forward API, access, destinations.
- [Request a payment data export](https://docs.stripe.com/get-started/data-migrations/pan-export), Stripe documentation, n.d., accessed 2026-11 — the export policy and its conditions.
- [Payments optimization](https://docs.stripe.com/payments/analytics/optimization), Stripe documentation, n.d., accessed 2026-11 — retry on a US debit network.
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance), Stripe documentation, n.d., accessed 2026-11 — no authorization rate for non-Stripe processors.
- [Optimizing authorization rates](https://stripe.com/guides/optimizing-authorization-rates), Stripe guide, n.d., accessed 2026-11 — dynamic routing across Stripe's connections.
- [Supporting dual-network debit cards in Australia](https://support.stripe.com/questions/supporting-dual-network-debit-cards-in-australia), Stripe support site, n.d., accessed 2026-11 — automatic least-cost routing for Australian merchants.
- [Top product updates from Sessions 2025](https://stripe.com/blog/top-product-updates-sessions-2025), Stripe, 2025-05-07 — the preview of Stripe Orchestration.
- [Everything we announced at Sessions 2026](https://stripe.com/blog/everything-we-announced-at-sessions-2026), Stripe, 2026-04-29 — unified payouts across providers for marketplaces (previewed).
- [More PSPs, more problems? When adding multiple processors pays off](https://stripe.com/sessions/2026/more-psps-more-problems), talk and transcript, Alex Ginet and Jon Krauss (Stripe) and Joshua Barton (Canva), Stripe Sessions, 2026-04 — the three motives, the orchestrator's trade-offs, the "open architecture" statement and Canva's account; a vendor event.
- [Forward payment details](https://docs.adyen.com/online-payments/tokenization/forward-payment-details), Adyen documentation, n.d., accessed 2026-11 — the `/forward` endpoint for card details and network tokens.
- [Additional Services Terms](https://www.adyen.com/legal/additional-services-terms), Adyen, last updated 2025-06-13 — the Network Token Sharing Service and the cryptogram a payment at another provider needs.
- [Multi pay-in](https://docs.adyen.com/marketplaces/multi-pay-in), Adyen documentation, n.d., accessed 2026-11 — pilot status and what it consolidates.
- [Network tokenization](https://docs.adyen.com/online-payments/network-tokenization), Adyen documentation, n.d., accessed 2026-11 — tokens only for payments Adyen acquires, merchant-managed tokens, US debit networks and routing priorities.
- [Enable Adyen Uplift](https://docs.adyen.com/partners/uplift-enablement), Adyen documentation, n.d., accessed 2026-11 — Intelligent Payment Routing settings and defaults.
- [Import data from another payment provider](https://docs.adyen.com/development-resources/migrating-payment-data), Adyen documentation, n.d., accessed 2026-11 — import timing.
- [Tokenization](https://help.adyen.com/knowledge/ecommerce-integrations/tokenization), Adyen help center, n.d., accessed 2026-11 — lists the article "How can I prepare for token migration? [Export]"; the article itself redirected to the tokenization documentation and was not readable in the verification pass.
- [External settlement detail report](https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report), Adyen documentation, n.d., accessed 2026-11 — payments for which Adyen is not the acquirer.
- [Adyen's Intelligent Payment Routing Achieves 26% Cost Savings for Enterprise Businesses](https://www.adyen.com/press-and-media/adyens-intelligent-payment-routing-usdebit), Adyen press release, 2024-09-09 — the US debit routing product and its pilot figures (vendor claim).
- [Adyen Uplift](https://www.adyen.com/uplift), Adyen product page, n.d., accessed 2026-11 — the single-platform argument.
- [Spreedly](https://www.spreedly.com/), Spreedly, n.d., accessed 2026-11 — an independent vault (vendor self-description).
- [Network tokenization](https://developer.spreedly.com/docs/network-tokenization), Spreedly documentation, n.d., accessed 2026-11 — merchant-specific token requestor IDs (vendor self-description).
- [Primer](https://primer.io/), Primer, n.d., accessed 2026-11 — an orchestrator with a vault, as contrast (vendor self-description).
- [Gr4vy](https://gr4vy.com/), Gr4vy, n.d., accessed 2026-11 — an orchestrator with a vault, as contrast (vendor self-description).
- [Hyperswitch](https://github.com/juspay/hyperswitch), Juspay, repository README, n.d., accessed 2026-11 — an open-source orchestrator and its routing claim (vendor self-description).

*Standards, regulation and official documentation*

- [Regulation II (Debit Card Interchange Fees and Routing)](https://www.federalreserve.gov/paymentsystems/regii-about.htm), Federal Reserve Board, updated 2024-05-17 — two unaffiliated networks and the merchant's routing choice.
- [Federal Reserve Board finalizes updates to the Board's rule concerning debit card transactions](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20221003a.htm), Federal Reserve, 2022-10-03 — card-not-present debit, effective 1 July 2023 (evidence age: 4 years).

*Research and practitioner sources*

- [[payments-fundamentals]] in RECONCILED — orchestration and tokens seen from the finance side.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
