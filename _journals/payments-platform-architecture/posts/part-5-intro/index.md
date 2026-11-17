---
title: "Part V — TRUST: Card Data, Fraud, Authentication and Compliance"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What do the controls over card data, fraud, authentication and compliance actually do for a business that takes payments? Part V argues that each one moves card data, a decision or a loss to another party and leaves something behind, so no control makes the risk disappear."
permalink: part-5
timetoread: 5 min read
---

> **KEY POINTS:**
>
> * **A trust control relocates; it does not remove.** Card numbers move to a provider's vault, the stored card to the card network, the block-or-allow decision to a model, the fraud loss to the cardholder's bank, and the duty to know a seller to the provider.
> * **Each one leaves a remainder with the business.** A payment page, a token behind which the card can change, a threshold, the loss on every payment not authenticated, and deadlines that can stop a seller's payouts.
> * **The controls are linked, and what stays needs an owner.** How a card is collected decides what the fraud model sees, so the question to ask is what moved, to whom, and what came back.

<br>
On the weekend of 8–9 August 2026, bots tested 61,000 stolen card numbers with €1 drop-in payments through the public booking widget of one studio on **Larkfield, the fictional studio-software platform this book follows**. Larkfield stored none of those numbers, and nothing was stolen from it. It still paid €4,100 in provider fees and refunds, and the studio could not sell online for 31 hours.

<!-- illustration-placeholder
{
  "id": "part-5-no-cards-held-still-a-bill",
  "status": "pending",
  "asset": "assets/images/part-5-intro/part-5-no-cards-held-still-a-bill.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the opening paragraph",
  "visual_goal": "Show that the stolen card numbers went past the platform to the provider, and that the platform, holding no card data, was still left with a bill and a studio that could not sell online.",
  "prompt": "Create a wide left-to-right explainer illustration with five elements. Far left: a cluster of three small robot figures labeled \"Bots\", with a stream of many small orange payment cards leaving them. Center left: a browser window labeled \"Booking page\" that the stream of cards enters. Top right: a blue building labeled \"Provider\". Bottom center: a server rack icon labeled \"Platform\" with a small empty box beside it labeled \"No card numbers\". Bottom right: a small studio shopfront with its door open and, beside it, a laptop showing a crossed-out shopping cart labeled \"Online off: 31 hours\", and next to the server a paper invoice labeled \"€4,100\". Arrows: a thick orange arrow named \"card numbers\" runs from the booking page along the top directly to the provider, passing above the platform server without touching it. A thin grey dashed arrow named \"page\" runs from the platform server up to the booking page. A thin orange arrow named \"bill\" runs from the provider down to the invoice. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Bots send a stream of cards into a booking page; the card numbers go to the provider and none reach the platform's server, which is left with an invoice of €4,100 and a studio whose online sales were off for 31 hours.",
  "caption": "The Card-Testing Weekend: the 61,000 card numbers went to the provider and none reached Larkfield, which still paid €4,100 while one studio could not sell online for 31 hours."
}
-->

That weekend contradicts a habit most engineers bring to payments: security is something you add and then have. Encrypt the data, put it behind a provider, pass the audit. Payments works differently. **Every control names who holds the data and who pays when it fails**, and that assignment is what [[part-4]] said an API cannot hide.

Part V's claim is that **each of five controls relocates something and leaves something behind**. Tokenization moves card numbers to the provider's vault and leaves you the page around the card fields. A network token moves the stored card to the card network and leaves you a provider token behind which the card can change. A risk score moves the allow-or-block decision to the provider's model and leaves you the loss on what you accept. 3-D Secure moves a fraud loss to the issuer, the cardholder's bank, only when the payer is authenticated. Verification moves the duty to know a seller to the regulated provider and leaves the platform the deadlines.

<!-- illustration-placeholder
{
  "id": "part-5-five-moves-five-remainders",
  "status": "pending",
  "asset": "assets/images/part-5-intro/part-5-five-moves-five-remainders.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that states the part's claim",
  "visual_goal": "Show the part's shape: five things leave the business for five different holders, and five remainders stay behind with the business.",
  "prompt": "Create a wide conceptual diagram. On the left, one large rounded box with a shop icon labeled \"Your business\". On the right, a vertical column of five holders, from top to bottom: an orange safe labeled \"Vault\", a hub of connected nodes labeled \"Card network\", a gauge dial labeled \"Risk model\", a bank building labeled \"Issuer\", and a blue office building labeled \"Provider\". Five solid blue arrows run from the business box to the five holders, one each; the top arrow carries the single arrow name \"moves\". Inside the business box, aligned with the five arrows, sit five small orange tiles from top to bottom labeled \"Page\", \"Token\", \"Threshold\", \"Exemptions\", \"Deadlines\". A single orange bracket groups the five tiles and carries the name \"stays\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Five arrows run from a business to a vault, a card network, a risk model, an issuer and a provider, while five tiles labeled Page, Token, Threshold, Exemptions and Deadlines stay inside the business.",
  "caption": "The shape of Part V: each of the five controls moves something to another party, and each leaves a remainder with the business."
}
-->

The controls have this shape because each is defined by **a rule that assigns responsibility**, not by a technology that destroys risk. The card industry's security standard binds every system a card number passes through or can affect. Stripe's documentation calls the merchant "ultimately responsible for payments you choose to accept". European law puts the loss on the side that avoids strong authentication. The rules are also linked: Stripe's PCI guide says its fraud tool is available only when its own client-side code collects the card. So I would stop asking "are we compliant?" and ask, for each control, what moved, to whom, what came back, and who owns it.

The claim rests on what Stripe and Adyen publish, and that record is uneven. Neither publishes a vault design. Adyen has published little about its fraud-risk model, and both companies say that they monitor transactions but not how. The gains reported for network tokens are the vendors' own comparisons. Each chapter says where its evidence stops.

The five chapters go from the credential, to the person using it, to the business being paid: card numbers into a vault, the stored card to the network, the fraud decision to a model, the fraud loss to the issuer, and the duty to know the seller. Each opens on a case at Larkfield.

## Chapters in this part

[[tokenization-vaulting-and-pci]] opens on the weekend's 61,000 numbers, none of which reached a Larkfield system, and answers **how providers keep card numbers out of everyone's systems, including most of their own**. A frame the provider serves, a token and an isolated vault move the numbers and most of the security standard's scope to the provider. Stripe documents a vault that shares no credentials with its other services; Adyen publishes less. The page and the stored cards stay: in January 2027 Larkfield cannot sign the script line of the shortest PCI form, with 17 third-party scripts on its payment step.

[[network-tokens]] turns from the provider's token, which means something only inside one vault, to **what a network token is and why the card networks push every stored card toward one**. It is a substitute card number that the network keeps pointing at the customer's current card. Lotte Smit's €49.00 membership renews on 1 March 2027 although her bank replaced the card in February. Visa says six basis points of approval gain, Adyen 3%, Stripe 3.8% for a bundle; the figures cannot be compared.

[[payment-fraud-and-risk]] takes up what a vault and a token leave open, a number stolen elsewhere and typed into a checkout, and asks **how a provider decides during an authorization whether a payment is fraud**. It cannot know. It estimates the chance of a later fraud dispute and blocks above a threshold; Stripe's 2026 figures show 41% of fraud disputes reported by day 14 and 86% by day 60. The threshold is a price the merchant pays. The chapter returns to the Card-Testing Weekend, which no threshold covers.

[[three-d-secure-and-sca]] explains the risk rule's third action, between allow and block, and asks **how the card's bank checks who is paying, and how providers decide when to ask**. The loss moves to the bank only when that check happens; a requested exemption or a merchant-initiated renewal leaves it with the merchant. Bram de Wit's €120.00 pass, bought unchallenged, costs Studio Noord €135.00 when it is disputed.

[[payment-compliance-and-regulation]] leaves the payer for the other end of the payment and asks **what a payment company must know about the businesses it pays, and how that becomes software**. Both providers hold verification as requirements with deadlines that switch payouts on and off, and neither publishes how it monitors transactions. In May 2026, 230 Larkfield studios went without payouts for up to 12 days after a rule changed; its answer is Keel decision K6, "verification is state, not a form". This chapter also closes the part.

## Where to Begin

Each chapter answers a question you may arrive with: where card numbers may go, why a stored card kept working, why a payment was blocked, who carries a fraud loss, why a seller's payouts stopped. The opening weekend returns in two of them, first as the control that worked and then as the attack that control was never about. The first and oldest relocation is the card number itself. Begin with [[tokenization-vaulting-and-pci]].

## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Larkfield is fictional, and its figures are the same in every chapter.
