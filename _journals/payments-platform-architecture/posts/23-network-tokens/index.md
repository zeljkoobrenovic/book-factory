---
title: "The Card Number's Replacement: Network Tokens and Credential Lifecycle"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What is a network token, who issues it, and why are card networks pushing every stored card toward one? It is a substitute card number that the network issues and keeps pointing at the customer's current card, and the push moves the keeping, restricting and pricing of stored cards from each vault to the network."
permalink: network-tokens
timetoread: 27 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what a network token is, who requests and issues it, what happens when a card is reissued, and how to read the gains claimed for it.

> **KEY POINTS:**
>
> * **A network token is a card number's stand-in, issued by the card network.** A merchant, provider or wallet requests it for one card; the network maps it back to the real card during authorization and re-points it when the bank issues a new card.
> * **The networks are pushing, and the push relocates the stored credential.** Mastercard has stated a goal of full e-commerce tokenization in Europe by 2030, and processor bulletins report fees on stored-card payments sent without a token. The network becomes the place where a stored card is kept valid, restricted and priced.
> * **The provider chooses the credential, and the published gains are vendor comparisons.** Stripe and Adyen each keep the card number and decide per attempt what to send. Visa says six basis points, Adyen 3%, Stripe 3.8% for a bundle; the figures cannot be compared, so measure your own.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Vault Hostage** — network tokens belong to whoever requested them, so tokens a provider requested are one more thing that may not leave with you.
> * **The Phantom Payment** — a record says "paid with the card ending 4417" when the bank saw a token for a different card, so the record states something that did not happen.
> * **The Borrowed Blueprint** — an uplift a vendor measured across its own customers is put into a business case as the gain a much smaller merchant should expect.

<br>
A member's bank replaces her card after fraud at another shop. She tells nobody. On the first of the next month her gym membership is charged as usual and approved, although the card number the studio's software stored no longer exists, and the app still shows the last four digits of the dead card. Stripe's newsroom release of 23 February 2023 said: "Last year, approximately 40% of cardholders replaced their cards as a result of the card expiring, getting lost, or being compromised by fraud." **(Evidence age: 3.7 years; the figure refers to 2022 and Stripe gives no source for it.)** A stored card that outlives its number is the normal case for a subscription business, not the exception.

The renewal worked because the number sent to the bank was not the card number. It was a **network token**: a substitute card number that the card network (Visa, Mastercard) issues for one card at one merchant or device and maps back to the real card during authorization. The networks push stored cards toward it with stated targets and with fees on payments sent without one. The effect, in my reading, is that **the network, instead of each merchant's or provider's vault, becomes the place where a stored credential is kept valid, restricted and priced**.

**Where we are in the payment's journey.** When Mila Janssen bought her €120.00 class pass on 9 March 2027 she paid from her phone's wallet, and the number her phone sent was already a network token ([[journey-of-a-payment]]). This chapter is about the same mechanism applied to the card she typed in on 12 January 2027 for her €49.00 monthly membership, which is charged on the 1st of each month without her being present.

The chapter starts at Larkfield, the fictional studio-software platform this book follows, with a renewal that should have failed. It then separates the provider's token from the network's, follows a token from request to reissue, and places wallets, Click to Pay and payment passkeys as the same token under other names. Next come the networks' push (targets, fees and one legal mandate), the published gains, and three ways to hold tokens. The comparison of Stripe and Adyen follows, then Larkfield's rule for stored cards, and the ways tokens go wrong.

## Setting the Scene at Larkfield: The Renewal That Should Have Failed

On 3 March 2027 Lotte Smit, a member of Studio Noord, writes to Larkfield's support. Her €49.00 membership renewed on 1 March, and the member app says it was paid with her Mastercard debit card ending 4417. Her bank replaced that card in February, after fraud elsewhere; the new one ends 8052. She wants to know which card was charged.

Tom Hendriks, the engineer who built the payment service, looks and finds three numbers for one payment. The payment record store holds the dead card's last four digits, saved when Lotte stored the card in 2025. The provider's response could have told Larkfield the new card's last four, in an optional field Larkfield never switched on. And the number that went to her bank was a third one, which Larkfield has never held. Adyen, which processes Studio Noord's payments, documents all of this (n.d., accessed November 2026): with tokens it manages, "we automatically swap that for a network token", and optional fields return "The last four digits of the network token" and "The last four digits of the card".

Femke de Graaf, Larkfield's head of payments engineering, turns the ticket into four questions: **who issued the third number, who asked for it, who decides which number is sent on each attempt, and what does it cost to send the old kind?** They order this chapter.

## Two Tokens With One Name: The Provider's and the Network's

The token Larkfield holds is a **provider token**: an identifier that means something only inside one provider's vault, the isolated system where the provider keeps real card numbers ([[tokenization-vaulting-and-pci]]). The issuer, the bank that issued the customer's card, never sees it. Stripe's guide to network tokens (n.d., accessed November 2026) describes its own tokens as "a nonsensitive string that can be used only by the business that collected the card". It is a database key, not a payment credential.

A network token, by contrast, is a payment credential everywhere a card number is. EMVCo, the body that publishes the EMV payment specifications, describes it on its EMV Payment Tokenisation page (n.d., accessed November 2026) as a replacement for the primary account number (PAN, the number printed on the card): "an EMV Payment Token is constrained in how it can be used. For example, to a specific merchant, device or payment scenario." EMVCo draws the line between the two kinds itself. Its token is used "from point of purchase, to an acquirer and then passing across the payment networks through to payment authorisation by the card issuer", whereas "within the merchant environment tokenisation can happen between the merchant and acquirer" (the acquirer is the institution that sends the merchant's payments into the network). Adyen's documentation (n.d., accessed November 2026) gives the shape: "A network token is 16-digit alternative for the Primary Account Number (PAN), and is unique per combination of shopper and merchant." One token stops at the provider; the other reaches the bank.

The standard defines two roles around that token. The **token requestor** asks for a token and is the only party that may use it. The **token service provider** issues the token and holds the mapping to the card; in practice this is the card network, through what Spreedly's documentation (n.d., accessed November 2026) calls "the card network's token service (examples include Visa Token Service or Mastercard Digital Enablement Service)". EMVCo's registration page (n.d., accessed November 2026) says the code it assigns to each token service provider "is included in the Token Requester ID, which uniquely identifies the pairing of Token Requester with the Token Service Provider". Who asked and who issued are thus recorded for every token. Adyen's explainer (September 2024) lists who can ask: "A network token can be requested by a merchant, payment gateway, or payment processor." I did not read EMVCo's specification text (version 2.4, published 9 July 2026); the roles here come from its public pages and from the two providers' descriptions.

Taken together, one stored card now exists in three forms, each issued by a different party and valid in a different place. Only the network token stays valid when the bank issues a new card, as the table shows.

| Representation | Issued by | Who can use it | Does the issuer see it? | When the card is reissued |
| --- | --- | --- | --- | --- |
| Card number (PAN) | The issuer | Anyone who holds it | Yes | It is dead; a new number exists |
| Provider token | The payment provider | One merchant, at that provider | No | Unchanged; what it points to in the vault may be stale |
| Network token | The card network, as token service provider | The requestor only | Yes, in place of the card number | Unchanged; the network points it at the new card |

<!-- illustration-placeholder
{
  "id": "23-one-card-three-forms",
  "status": "pending",
  "asset": "assets/images/23-network-tokens/23-one-card-three-forms.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of the three representations of one stored card",
  "visual_goal": "Make memorable that one stored card exists in three forms held by three different parties.",
  "prompt": "Create a conceptual illustration with one generic payment card at the top center labeled \"One card\". Three thin lines descend from it to three separate holders arranged left to right. On the left, a shop building holds a small key-shaped tag labeled \"Provider token\". In the middle, a payment company building with a safe holds a card-shaped tile labeled \"Card number\". On the right, a hub of connected nodes holds a card-shaped tile with a small lock, labeled \"Network token\". Under the shop is the label \"Merchant\", under the building with the safe \"Provider vault\", under the hub \"Card network\". A dashed arrow labeled \"Stays current\" circles the right-hand tile. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "One card connected to three holders: a merchant with a provider token, a provider vault with the card number, and a card network with a network token.",
  "caption": "One stored card exists in three forms: the merchant holds a provider token, the provider's vault holds the card number, and the card network holds the network token and keeps it current."
}
-->

## From Request to Reissue: Provisioning, Cryptograms and the Choice per Attempt

A token starts with a request, called **provisioning**. Adyen's explainer describes it: "The requestor sends a PAN to the card scheme, which forwards the request to the issuer. The issuer approves the request, and the network issues the token." It is a three-party step in which the issuer can say no, so a token exists only for cards whose issuers take part. Visa's press release of 4 June 2024 counted "over 8,000 issuers" enabled, and Stripe's documentation index (n.d., accessed November 2026), in its guidance for AI agents, warns them not to "assume every card or payment is eligible for network tokenization". Partial coverage is one reason a provider keeps the card number as well.

<!-- illustration-placeholder
{
  "id": "23-provision-then-pay",
  "status": "pending",
  "asset": "assets/images/23-network-tokens/23-provision-then-pay.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that describes provisioning",
  "visual_goal": "Show who talks to whom when a token is provisioned and when a payment is made with it.",
  "prompt": "Create a two-row flow diagram with three generic elements repeated in each row from left to right: a payment company building labeled \"Requestor\", a hub of connected nodes labeled \"Card network\", and a bank building labeled \"Issuer\". Top row, headed by a small tag \"Once\": a blue arrow labeled \"Card number\" runs from the requestor to the network, a blue arrow labeled \"Approve?\" runs from the network to the issuer, a green arrow labeled \"Yes\" returns to the network, and a teal arrow labeled \"Token\" returns from the network to the requestor. Bottom row, headed by a small tag \"Each payment\": a teal arrow labeled \"Token + cryptogram\" runs from the requestor to the network, inside the network a small table icon is labeled \"Mapping\", an orange arrow labeled \"Card number\" runs from the network to the issuer, and a green arrow labeled \"Approved\" returns from the issuer through the network to the requestor. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two rows: a requestor obtains a token from the card network with the issuer's approval, then pays with the token and a cryptogram that the network maps to the card number.",
  "caption": "A token is provisioned once, with the issuer's approval, and on each payment the card network maps the token back to the card for the issuer."
}
-->

Once issued, the token is bound to the party that requested it. Adyen puts it this way: "Tokens are domain-locked, meaning the same token can only be used by the party that requested it." Stripe's analytics documentation (n.d., accessed November 2026) calls network tokens "payment credentials that you can dynamically restrict to specific businesses and channels". This restriction, which the standard calls a domain control, is the security property: a token stolen from one merchant or provider is useless at another. It is also why a token belongs to its requestor.

A second control is applied per use. A **cryptogram** is a one-time value the network generates for one use of one token, proving that the request comes from the token's legitimate holder. Adyen's explainer says: "card schemes issue a cryptogram each time a customer uses their saved card details to initiate a purchase. These cryptograms are effectively one-time-passwords that are contextual to the business, token, and purchase." In Adyen's API it is a concrete field, `tokenAuthenticationVerificationValue`: "This is the network token cryptogram." It has a cost, which Stripe states: "using a network token often requires a one-time cryptogram that needs to be fetched from networks. As a result, network tokens can be prone to high additional latency compared to using PANs." Adyen ties the cryptogram to a purchase the customer starts. Its request examples for tokens a merchant manages itself agree: a one-off payment carries the cryptogram field, while a subscription payment omits it and carries `networkPaymentReference`, the network's reference to the first payment. Stripe's pages do not say which of its payments carry one.

The token does not replace the card number in the provider's vault; it sits beside it, and the provider decides on each attempt which of the two to send. Stripe's guide says it is "determining when to use a network token or the underlying PAN. We maintain PAN redundancy to retry failed network token transactions on the underlying PAN". Adyen's documentation says: "If a payment attempt with a network token fails (`attempt1`), we automatically retry the payment. In the second attempt (`attempt2`), we do not swap the card details or the `storedPaymentMethodId` token for a network token." Both companies thus document a choice per attempt and a fall-back, so the stored-card record alone never says which credential reached the bank ([[authorization-optimization]] covers these decisions inside the call).

Months later the bank replaces the card, and this is where the mapping earns its keep: the network re-points the token at the new card, and the requestor keeps sending the same token. Stripe's guide: "if a customer lost their card, Stripe would get notified by the network and would update the token directly so it would continue to work without the customer having to update their payment information." Adyen's documentation: "if the shopper receives a new card because the old one expired or was lost, the network token remains the same." This is the **credential lifecycle** managed by the network, and it explains Lotte's renewal. The older remedy, an account updater, is a network service that delivers the new card number to the provider's vault; the token makes the new number unnecessary for the payment, though not for what the merchant displays.

<!-- illustration-placeholder
{
  "id": "23-reissue-token-stays",
  "status": "pending",
  "asset": "assets/images/23-network-tokens/23-reissue-token-stays.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that explains what happens when the card is reissued",
  "visual_goal": "Show that when a card is replaced the token and the merchant's key stay the same, the network's pointer moves, and the merchant's displayed digits go stale.",
  "prompt": "Create a before-and-after diagram split into a left panel with a small tag \"Before\" and a right panel with a small tag \"After\". In each panel, three stacked elements from top to bottom: a phone screen showing a card line, a tile with a lock labeled \"Network token\", and a payment card. In the left panel the phone screen shows \"•••• 4417\", the token points with a teal arrow to a card labeled \"4417\". In the right panel the phone screen still shows \"•••• 4417\" with a small orange warning mark labeled \"Stale\", the same token tile points with a teal arrow to a new card labeled \"8052\", and the old card labeled \"4417\" lies crossed out to the side. Between the panels a bank building sends an arrow labeled \"New card\" to the right panel. A green check mark labeled \"Approved\" sits under the right panel. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Before and after a card is replaced: the network token is unchanged and now points to the card ending 8052, while the app still shows 4417.",
  "caption": "When the bank replaces the card ending 4417 with one ending 8052, the token stays the same and the payment is approved; only the digits the merchant displays go stale."
}
-->

Put together, these steps promise two things, continuity and restriction, and they leave four things unpromised that a design has to cover itself.

| What a network token promises | What it does not promise |
| --- | --- |
| The credential keeps working after the card is reissued | That every card has one: the issuer must take part |
| The token works only for its requestor | Protection against a thief typing a stolen card number into your checkout |
| The issuer receives a current credential | An approval: Stripe's documentation says it "doesn't guarantee any outcomes" for these features |
| A one-time cryptogram on a customer's purchase | Speed: fetching the cryptogram adds a call to the network |

## The Same Token Under Other Names: Wallets, Click to Pay and Passkeys

Mila's class pass already carried such a token. A phone wallet holds a **device token**: by common industry description, a network token whose requestor is the wallet and whose restriction is the device, with the cryptogram produced when she unlocks the phone. The sources fit that description. Adyen's documentation says "Apple Pay uses network tokenization, stores payment information securely in the shopper's Apple Pay eligible device, and confirms the payment through Touch ID or Face ID authentication." Google's developer guide (n.d., accessed November 2026) says its API returns "cards on file on Google.com (`PAN_ONLY`) or a device token on an Android-powered device authenticated with a 3-D Secure cryptogram (`CRYPTOGRAM_3DS`)". Stripe's forwarding API sends Apple Pay credentials through fields named `network_token_number` and `network_token_cryptogram`.

Click to Pay goes one step further and moves the stored card itself to the network. The cardholder keeps cards in a profile with Visa or Mastercard, and the merchant's checkout receives a token. Adyen's documentation says: "The card scheme is responsible for securely storing the cardholder data and issuing tokens." Mastercard's release of 11 June 2024 states the aim: "To eliminate manual card entry, Mastercard is making it easier to embed Click to Pay into merchant sites". Support is uneven. Adyen writes that "Currently, Adyen's Click to Pay integration only supports recurring payments on Mastercard Click to Pay", and Stripe documents it under the standard's name, Secure Remote Commerce: its guide (n.d., accessed November 2026) says "Secure Remote Commerce is only available in the US at this time" and "We're working to re-enable Secure Remote Commerce onboarding".

Payment passkeys build on the token as well. A passkey is a device-bound proof, unlocked by fingerprint or face, that the cardholder is present; how it authenticates belongs to [[three-d-secure-and-sca]]. Its status in November 2026 is early. Adyen's press release of 29 October 2026 says: "Adyen will initially offer Visa Payment Passkey through Authenticate in the UK, with further enhancements and a global expansion planned for 2027." Its documentation is more cautious: "Scheme passkeys are currently in pilot phase, and only enabled for a specific group of merchants", and they are "supported for Mastercard network tokenized transactions". Stripe's documentation and support site (n.d., accessed November 2026) have no page on passkeys for card payments, so I would not let a design depend on them yet.

## Why the Networks Push: Targets, Fees and One Legal Mandate

The networks say in public where they want stored cards to go. Mastercard's release of 11 June 2024: "Mastercard today announced its vision for 100% e-commerce tokenization in Europe by the end of the decade. This supports a global commitment to phase out manual card entry". It adds that its tokenization service "today secures 25% of all e-commerce transactions globally". Visa's release of 4 June 2024 says "Currently, 29% of all transactions processed by Visa use tokens" and counts "more than 10 billion tokens since the technology's launch in 2014". The 2030 date is a vision, not a rule, and the two shares measure different things.

The aim has a price attached, and here the source quality drops: **the networks publish their interchange tables but not the schedules of their own fees**, so every amount below comes from a processor's bulletin to its merchants. PayPal Braintree's 2023 bulletin reports: "Effective 1 October 2023: Visa will introduce a new fee of 2.5bps (0.025%) per transaction for domestic and interregional ecommerce primary account number (PAN)-approved authorizations processed without Visa EMV Payment Tokens (network tokenization) or Visa Secure (3D Secure)", in all European countries except Turkey and France. **(Evidence age: 3 years; Braintree's fall 2026 bulletin still refers to this fee.)** A basis point is one hundredth of a percent, and 3-D Secure is the protocol by which the issuer checks who is paying. The fall 2026 bulletin reports that Mastercard revises a comparable fee from 1 January 2027, with "four rate changes phased in over three years, aimed at driving tokenization and authentication", and that "In April 2028, Guest Checkout will be included in the non-token fee". Braintree calls these "behavioral fees intended to drive tokenization and authentication".

A second fee line runs the other way: charges on the tokens themselves and on the services that keep credentials current. Stripe's documentation (n.d., accessed November 2026) names two: "Stripe doesn't reflect any fees that might occur as a result of network token use, such as the Visa Digital Credential Updater (VDCU) fee", and "Mastercard levies a Credential Continuity Program (CCP) fee when attempting a payment using outdated card details". Adyen's explainer (September 2024) says: "Some schemes, like Visa, might charge a fee for the management of issued tokens. They still charge lower fees for processing tokens than for processing PANs." The consultancy CMSPI wrote in April 2026, citing a bank's bulletin, that "Beginning in April 2026, Visa will introduce a Card-Present Token Fee on authorized network-tokenized card-present transactions" in the United States. The token is moving from a discount toward a priced service, and the table collects the lines with the kind of source behind each.

| Fee line, as reported | Direction | Reported amount | Source and its kind |
| --- | --- | --- | --- |
| Visa Secure Credential Framework, Europe | Charged on e-commerce card-number authorizations with neither token nor 3-D Secure | 2.5 basis points from 1 October 2023 | Braintree bulletin, 2023 (processor; secondary) |
| Mastercard Customer Performance Development Fund, EU and UK/Ireland | Charged on stored-card payments not tokenized; guest checkout from April 2028 | Listed today as 5 basis points (7 in Germany) on domestic and intra-European payments; revised from 1 January 2027 | Braintree bulletin, fall 2026 (processor; secondary) |
| Visa Digital Credential Updater; Mastercard Credential Continuity Program | Charged for keeping credentials current, or for using outdated ones | Not stated | Stripe documentation, n.d. (company) |
| Visa Card-Present Token Fee, United States | Charged on tokenized in-person payments from April 2026 | Not stated per payment | CMSPI, April 2026 (consultancy, citing a bank's bulletin; secondary) |
| Reductions in interchange (the fee paid to the issuer) for tokenized payments | Reduced: "Visa offers certain discounts on consumer card-not-present payments in some markets" | Not stated | Stripe documentation, n.d. (company) |

In one market the push is law. Stripe's India page (n.d., accessed November 2026) says: "The RBI mandates card on file (CoF) tokenization through the card networks", and "Businesses, Payment Aggregators (PAs), Payment Gateways (PGs), and acquiring banks can no longer store customer card information". The RBI is the Reserve Bank of India. There the provider's own vault is excluded, and tokens need the customer's consent: "Customers must provide explicit consent to allow the tokenization and storage of the card on Stripe's system." Stripe adds that this applies "only to India domestic businesses for domestic transactions".

The networks' stated reasons are fraud and the end of typing card numbers: Mastercard's "phase out manual card entry and make e-commerce safer", and the framework's purpose as Braintree reports it, "to help reduce fraud and improve approval rates". My reading goes further, and it is my synthesis and not a motive any network has stated. The network holds the mapping, so it keeps the credential valid. It sets the domain controls, so it restricts the credential. It sets the fees on the token and on its absence, so it prices the credential. Each of those jobs used to belong to a merchant's or provider's vault.

## What the Gain Is Worth: Four Figures That Cannot Be Compared

Against that cost stands the claimed benefit, a higher approval rate. Four published figures describe it, and no two measure the same thing.

| Who says it | Figure, as published | What it covers | Date |
| --- | --- | --- | --- |
| Visa, press release | "a six-basis point increase in payment approval rates globally" | Tokenization, all Visa | 4 June 2024 |
| CMSPI, citing an article by a Visa author that I did not read (secondary) | "a 6% improvement in authorized rates" | Growth in token usage in 2024 | April 2026 |
| Adyen, explainer | "an average uplift of 3% in authorization rates for businesses on our platform who use network tokenization" | Network tokens at Adyen | September 2024 |
| Stripe, product page | "Increase acceptance rates by 3.8% on average with Authorisation Boost" | A bundle: network tokens, card account updater and Adaptive Acceptance (Stripe's request optimization) | n.d., accessed November 2026 |

The figures disagree because each is a vendor's comparison of payments that used a token with payments that did not, and none comes with a published method. Visa's release attaches no footnote to its six-basis-point sentence; the nearest basis it gives, for the revenue it credits to tokens, is "VisaNet CY2023 credit and debit global card-not-present (CNP) payment volume for tokenized and non-tokenized credentials" (card-not-present means online or stored-card payments). The two groups differ in more than the token. As I read the mechanism, a token exists only where the issuer takes part, and it is mostly attached to the stored cards of returning customers, whose payments would be approved more often anyway. A comparison of two self-selected groups is not a controlled experiment. The unit is loose too: Visa's release says six basis points, which is 0.06 percentage points, while a secondary source attributes six percent to Visa, a hundred times more; whether the two describe the same measurement I cannot tell. A customer quote in Stripe's 2023 release (the software firm Doist) credits "over 4%" to two features together.

The fraud figures are the same kind of comparison. Visa's release says "tokenization can reduce the rate of fraud by up to 60%", footnoted only to "Visa processed transactions as of April 2024", and that tokens "saved $650 million in fraud in the last year", footnoted to "Visa Processed global card-not-present (CNP) payment volume for tokenized vs non-tokenized credentials". They also describe one kind of fraud, the reuse of a stolen stored credential. A token says nothing about who is typing a card number into a checkout.

What does answer the question is your own traffic, and both providers return per-payment data for it. Adyen returns `retry.attempt1.networkTokenOffered`, `retry.attempt2.networkTokenOffered` and so on, with the raw response for each attempt, once the merchant selects "Include the retry attempts". Stripe's API reference (n.d., accessed November 2026) lists `payment_method_details.card.network_token.used` on a charge: "Indicates if Stripe used a network token, either user provided or Stripe managed when processing the transaction". The reference page marks the field with a feature flag, and the Markdown copy of the same page omits it, so confirm that your account returns it. Stripe's dashboard estimates recovered volume per feature, attributing each payment "to the one most likely responsible for approval" and stating that "The optimization calculations we provide are estimates". I would therefore cut my own approval rate by token used or not, within the same issuer country, card type and payment kind, and treat a randomized holdout as the stronger test where a provider offers one ([[authorization-optimization]]).

## Three Ways to Hold Tokens, and What Each Leaves You

Since a token belongs to its requestor, the first design question is who that should be, and three answers are documented. The provider can be the requestor: Stripe "will request tokens on your behalf", and Adyen says "We collect and store network tokens from the card schemes". The merchant can be the requestor: Adyen documents a mode in which "you can keep your existing network tokens and use them in the payment requests that you send to Adyen", with stated limits ("It is not possible to combine this with our tokenization feature"; "You cannot use 3D Secure for transactions with network tokens that you manage yourself"), and Stripe's product page says businesses can "bring external tokens for processing". Or an independent vault can be the requestor: Spreedly, a contrast case, describes itself as a "Token Requestor Token Service Provider (TR-TSP)" through which merchants "request network tokens using their merchant-specific TRID", the requestor identifier.

Each choice has a cost, and the table sets them side by side; the last column is my judgement. Letting the provider request the tokens costs nothing to build and ties them to that provider; the other two buy continuity across providers at the price of network enrollment, card-data scope under PCI DSS (the card industry's security standard) and lost provider features.

| Design | What you build | What works across providers | What you give up | When I would choose it |
| --- | --- | --- | --- | --- |
| Provider is the requestor | Nothing | Nothing: the tokens are the provider's | Control and portability of the tokens | Most merchants |
| Merchant is the requestor | Network enrollment, token storage, cryptogram calls | The tokens, at any provider that accepts them | Provider tokenization and 3-D Secure on those payments (Adyen's stated limits) | Large stored-card volume across several acquirers |
| Independent vault is the requestor | An integration with the vault | The vault's tokens, at the gateways it supports | A new dependency in the payment path, and its fees | Multi-provider routing without your own network integrations |

That comparison turns on portability, and here the evidence is thin. Adyen's explainer states the restriction: "a token cannot be used by a party other than its requestor". Stripe's export page (n.d., accessed November 2026) describes an encrypted file with "the card details of your customers, email addresses, and any attached metadata" and does not mention network tokens. Adyen's documentation index (n.d., accessed November 2026) lists pages on importing payment data from another provider and none on exporting it. Its help center has carried an article on preparing a token export, which I could not read: in November 2026 its address redirected to the tokenization page. Adyen's Forward API says "We support forwarding card details, and network tokens" to a third party, one request at a time and only after Support enables it. One answer is in Adyen's terms for additional services (last updated 13 June 2025): a Network Token Sharing Service "allows Adyen to share Network Tokens with its customers (i.e., Merchants or Platforms) for them to store and/or use to process payments with other payment providers". For a customer-initiated payment elsewhere, "you will need to retrieve a one-time cryptogram from us". I found no Stripe statement, in its documentation, support site or terms, on whether tokens it requested can follow a merchant that leaves.

> **INFERENCE, NOT DOCUMENTED:** Tokens that Stripe requested stay with Stripe when a merchant leaves, and so do Adyen's unless the sharing service was enabled; even then each cardholder payment needs a cryptogram from Adyen, so the tokens do not outlive the contract. What moves is the card numbers, by a provider-to-provider export ([[tokenization-vaulting-and-pci]]), and the new provider requests new tokens for them. This follows from the requestor restriction, the sharing terms and the export page's silence. Ask for it in writing.

## Stripe and Adyen: Where They Differ

The two companies document network tokens differently on seven aspects. The last column is my reading and is inference; the other cells quote or summarize documentation accessed in November 2026 unless a date is given.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Provisioning | "works out of the box for all merchants who use Stripe Payments"; Stripe "will request tokens on your behalf". India needs customer consent | Adyen-managed mode "does not require any additional integration"; one page says Adyen "automatically requests network tokens for stored cards when possible"; another, under the Adyen-managed heading, says to "ask our Support Team to enable payments with network tokens" | Both default to the provider as requestor; on Adyen, confirm that it is switched on |
| Merchant as requestor | Product page: "bring external tokens for processing"; no integration guide found | A documented mode with request fields, excluding Adyen tokenization and 3-D Secure | Adyen documents the path; Stripe mentions it |
| Token or card number per attempt | Decides "when to use a network token or the underlying PAN"; retries on the PAN | Token first; "we automatically retry the payment" without the token | No material difference in the public record |
| What the merchant sees | `network_token.used` on the charge (behind a feature flag in the reference); an analytics dimension; dashboard estimates | Per attempt: `networkTokenOffered` and the raw response; optional `networkToken` and `latestCard` fields | Adyen shows each attempt, Stripe the result |
| Scope | Names Visa, Mastercard, American Express; a published list of markets | Names Visa, Mastercard, American Express; "only applicable for payments acquired by Adyen" | The limit follows Adyen acting as acquirer itself ([[acquiring-and-network-connectivity]]) |
| Reported gain and price | 3.8% for a three-feature bundle; "€0.15 per token provisioned" outside the bundle on custom interchange pricing (Ireland page) | 3% on average (2024); prices not public | Not comparable |
| Leaving | Card export documented; network tokens not mentioned | No export page in the documentation index; Forward API covers network tokens; a sharing service for use "with other payment providers" (terms, 2025) | Adyen offers shared tokens that still need its cryptogram; Stripe says nothing about the tokens |

An integrator does different work on each. On Stripe you read what was done (the `network_token.used` field) and listen for card updates: the `payment_method.automatically_updated` event "notifies you of automatic card updates from the network" and includes "the card's new expiration date and last four digits". Stripe documents that event for card updates; the pages I read do not say whether it also fires when only a token's mapping changes. On Adyen you first decide the mode, switch on the attempt and card fields, and check that the payments in question are acquired by Adyen, because network tokenization "cannot be used with external acquirer connections".

## In Practice at Larkfield: Memberships That Survive a Reissued Card

Back to Lotte Smit. Studio Noord is on Adyen, which has managed network tokens for Larkfield's stored cards there since 2024 *(illustration)*. In February 2027 her bank replaced her card, and the card network re-pointed the token. On 1 March the renewal job charged her provider token for €49.00; Adyen swapped it for the network token, and her bank approved it at the first attempt. Larkfield's fee was 1.9% + €0.25 = €1.18, and the studio received €47.82. Nothing told Larkfield's record to change, so the app kept showing 4417.

From that ticket Larkfield writes one rule for stored cards, under decision K4 of its 2027 Keel program ("network tokens for stored cards"). The provider token is the key. Each attempt in the payment record store records whether a token was used: `networkTokenOffered` on Adyen, `network_token.used` on Stripe. The card shown to a member is refreshed from the provider (`latestCard.summary` and `latestCard.expiryDate` on Adyen, the `payment_method.automatically_updated` event on Stripe) and is never offered as proof of which credential paid. Support can then answer Lotte: your new card was charged, and the old one is dead.

The fee side gets a line in a yearly review, and it is small. At the 2.5 basis points Braintree reported, an untokenized, unauthenticated €49.00 renewal would cost about one cent. Larkfield's Adyen pricing passes network fees through, and about 210,000 card renewals a month run there *(assumption)*, worth €10.29 million; 2.5 basis points of that is about €2,600 a month. That is an upper bound: it assumes every card is a Visa card sent with a card number and no authenticated first payment, and the bulletin adds that related merchant-initiated transactions (payments the merchant starts, such as renewals) "that are in scope for tokens or 3DS will avoid the behavioral fee". On Stripe, Larkfield pays a blended rate and would not see the line at all ([[payment-economics]]). Femke adds two columns to her inventory of acquirers: who the token requestor is, and which fee lines were last checked.

## When It Goes Wrong

The first failure is inside the merchant's own data. When a card is replaced behind a token, anything keyed on the card changes meaning without notice: a check for duplicate cards, a fraud rule, what support tells a member. Stripe documents one case. Its fingerprint is a value that identifies a card number without revealing it, and "If the card update includes a new card number, the fingerprint changes." The signal to watch is the count of stored cards whose displayed details differ from the provider's current ones.

The second failure sits at the payment call. When a token attempt is declined and the provider retries with the card number, one API call contains two authorizations. Adyen's own example shows it: `attempt1` with `networkTokenOffered` true and response code 05, then `attempt2` with `networkTokenOffered` false and response code 00. A merchant that also retries on its own schedule can use up the number of retries the networks allow faster than it thinks ([[authorization-optimization]]). The attempt data is where it shows up.

The third failure is on the invoice, not in the payment path. A saving taken from the provider's estimate leaves out the cost side, as Stripe says itself: "Stripe doesn't reflect any fees that might occur as a result of network token use, such as the Visa Digital Credential Updater (VDCU) fee. Any such fees reduce the overall cost saving benefits from network tokens." Stripe's Irish price list shows "€0.15 per token provisioned for accounts without Authorisation Boost and with custom interchange pricing"; Adyen's prices for network tokenization are not public: its pricing page has no line for them. The check is a yearly read of the network fee lines on an itemized invoice.

The fourth failure appears only on the day stored cards move to another provider. As the designs section assumed, the old provider's tokens stay behind. The consequence is that the first billing cycle on the new provider runs on card numbers as they were exported, some of them already replaced, until the new provider has its own tokens. Larkfield's rehearsed switch never moves stored cards ([[payment-routing-and-orchestration]]), but its planned migration of 1,140 studios from Stripe to Adyen does. That the first cycle would see more declines is my inference; Larkfield will measure it on the first batch of studios.

## What to Take Away

**Established.**

- A network token is a substitute card number issued under the EMV standard by the card network, at the request of a merchant, provider or wallet, and usable only by that requestor (EMVCo; Adyen, 2024).
- When the card is reissued the network re-points the token, and the payment keeps working without the customer or merchant acting (Stripe and Adyen documentation).
- Stripe and Adyen both keep the card number, choose token or card number per attempt and fall back to the other.
- The networks have stated the direction: Mastercard's 2030 vision for Europe; tokens on 29% of Visa's transactions in 2024.

**Depends on context.**

- Who should be the requestor: the provider, unless you route large stored-card volume across several acquirers and can run network enrollments yourself.
- Whether a published gain applies to you: it depends on your issuers, your share of stored cards and what your provider already does; only your own data says.
- Whether the fee lines reach you: on pass-through pricing they do, on a blended rate they are inside the rate. Amounts are known from processor bulletins only and keep changing.

**The author's synthesis.**

- The stored credential now lives at the network, so I treat the provider token as my only stable key and never record which card paid from my own copy of its digits.
- I count the uplift as unproven until I have measured it on my own traffic, because every published figure is a vendor's comparison of unlike groups.
- I put the requestor question in the contract: whose tokens they are, and what happens to them when I leave.

## Questions to Ask

1. For each stored card, which party requested its network token, and under whose requestor identifier?
2. Does our payment record store, per attempt, whether a token or the card number was sent?
3. Which signal refreshes the card details we show customers, and is it switched on for both providers?
4. What do we key on a card's fingerprint or last four digits, and what happens to it when the card changes behind the token?
5. When a token attempt fails, does the provider retry with the card number, and does our own retry schedule count that attempt?
6. Who measured the uplift figure in our business case, on what traffic, against what baseline?
7. Which network fee lines for untokenized payments, tokens and updater services appear on our invoices, and who reviews them each year?
8. If we move stored cards to another provider, what happens to the tokens, and has the provider said so in writing?

A vault and a token protect the stored credential. Neither can tell whether the person typing a card number into a checkout is its owner: a number stolen elsewhere arrives as a brand-new card, and something has to judge each use of a card, not the storage of it. That judgement, made in milliseconds inside the authorization, is the subject of [[payment-fraud-and-risk]].

## Sources and Evidence

*Company, product and investor sources*

- [Understanding the benefits of network tokens](https://stripe.com/guides/understanding-benefits-of-network-tokens), Stripe guide, n.d., accessed 2026-11 — provider token scope, automatic provisioning, token-or-PAN choice, latency, reissue, markets.
- [Payments optimization](https://docs.stripe.com/payments/analytics/optimization), Stripe documentation, n.d., accessed 2026-11 — interchange and scheme-fee notes, VDCU and CCP fees, the estimate method and disclaimer.
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance), Stripe documentation, n.d., accessed 2026-11 — the "Network token usage" dimension and its description of restriction.
- [The Charge object](https://docs.stripe.com/api/charges/object), Stripe API reference, n.d., accessed 2026-11 — the `network_token.used` field (in the HTML page, marked with a feature flag; absent from the Markdown copy).
- [Cards](https://docs.stripe.com/payments/cards/overview), Stripe documentation, n.d., accessed 2026-11 — the automatic-update event and the fingerprint change.
- [Authorisation Boost](https://stripe.com/authorization-boost), Stripe product page (Ireland locale), n.d., accessed 2026-11 — the 3.8% claim, external tokens, per-token price.
- [Stripe documentation index](https://docs.stripe.com/llms.txt), Stripe, n.d., accessed 2026-11 — the eligibility warning in its guidance for AI agents; no page on card passkeys.
- [Secure Remote Commerce program guide](https://docs.stripe.com/secure-remote-commerce), Stripe documentation, n.d., accessed 2026-11 — Click to Pay on Stripe: United States only, onboarding paused.
- [India network tokenization](https://docs.stripe.com/india-network-tokenization), Stripe documentation, n.d., accessed 2026-11 — the RBI mandate as Stripe applies it.
- [Request a payment data export](https://docs.stripe.com/get-started/data-migrations/pan-export), Stripe documentation, n.d., accessed 2026-11 — what an export contains.
- [Forward card details to third-party API endpoints](https://docs.stripe.com/payments/vault-and-forward), Stripe documentation, n.d., accessed 2026-11 — wallet credentials sent through network-token fields.
- [Stripe expands network tokens and card account updater to improve conversion](https://stripe.com/newsroom/news/network-tokens-card-account-updater), Stripe newsroom, 2023-02-23 — the 40% replacement figure and the Doist quote (evidence age: 3.7 years).
- [Network tokenization](https://docs.adyen.com/online-payments/network-tokenization), Adyen documentation, n.d., accessed 2026-11 — definition, two modes, the acquiring limit, attempt and card fields, the cryptogram field.
- [PAN fallback for network tokens](https://docs.adyen.com/online-payments/network-tokenization/pan-fallback), Adyen documentation, n.d., accessed 2026-11 — limits of merchant-managed tokens.
- [Tokenization](https://docs.adyen.com/online-payments/tokenization), Adyen documentation, n.d., accessed 2026-11 — automatic token requests; wallet one-click limit.
- [Forward payment details](https://docs.adyen.com/online-payments/tokenization/forward-payment-details), Adyen documentation, n.d., accessed 2026-11 — forwarding of network tokens.
- [Adyen documentation index](https://docs.adyen.com/llms.txt), Adyen, n.d., accessed 2026-11 — pages on importing payment data, none on exporting it.
- [Optimize card payments with network tokenization](https://www.adyen.com/knowledge-hub/network-tokenization), Adyen knowledge hub, 2024-09-04 — requestor flow, domain lock, cryptogram, the 3% figure, token fees.
- [Additional Services Terms](https://www.adyen.com/legal/additional-services-terms), Adyen, last updated 2025-06-13 — the Network Token Sharing Service and the cryptogram a payment at another provider needs.
- [Apple Pay](https://docs.adyen.com/payment-methods/apple-pay), Adyen documentation, n.d., accessed 2026-11 — the wallet uses network tokenization.
- [Click to Pay](https://docs.adyen.com/payment-methods/cards/click-to-pay), Adyen documentation, n.d., accessed 2026-11 — the network stores the card; recurring support.
- [Scheme passkeys](https://docs.adyen.com/online-payments/authentication/scheme-passkeys), Adyen documentation, n.d., accessed 2026-11 — pilot status and token dependence.
- [Adyen Rolls Out Visa Payment Passkey](https://www.adyen.com/press-and-media/adyen-visa-payment-passkey), Adyen press release, 2026-10-29 — United Kingdom first, expansion planned for 2027.
- [Visa Issues 10 Billionth Token](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20701.html), Visa press release, 2024-06-04 — adoption figures, "six-basis point", "up to 60%", footnotes.
- [Mastercard reimagines online checkout; commits to reaching 100% e-commerce tokenization by 2030 in Europe](https://newsroom.mastercard.com/news/press/2024/june/mastercard-reimagines-online-checkout-commits-to-reaching-100-e-commerce-tokenization-by-2030-in-europe/), Mastercard newsroom, 2024-06-11 — the 2030 vision, the 25% share, Click to Pay.

*Standards, regulation and official documentation*

- [EMV Payment Tokenisation](https://www.emvco.com/emv-technologies/payment-tokenisation/), EMVCo, n.d., accessed 2026-11 — definition of the payment token, contrast with merchant-side tokenization, specification v2.4 of 9 July 2026 (not read).
- [Token Service Provider Registration Programme](https://www.emvco.com/processes/token-service-provider-registration-programme-2/), EMVCo, n.d., accessed 2026-11 — the TSP Code and the Token Requester ID.
- [Google Pay API tutorial](https://developers.google.com/pay/api/web/guides/tutorial), Google, n.d., accessed 2026-11 — `PAN_ONLY` and `CRYPTOGRAM_3DS`.

*Research and practitioner sources*

- [Visa Secure Credential Framework](https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23), PayPal Braintree network-update bulletin, 2023 — the 2.5 basis-point fee and its scope (secondary source; evidence age: 3 years).
- [Network updates, fall 2026](https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/fall/2026), PayPal Braintree network-update bulletin, 2026 — Mastercard's revised fee and its phases (secondary source).
- [April 2026 U.S. Network Fee Updates](https://cmspi.com/april-2026-u-s-network-fee-updates-3-billion-estimated-cost-impact-for-merchants/), CMSPI, 2026-04-28 — the card-present token fee, cited from a J.P. Morgan bulletin, and the "6%" figure, cited from an article by a Visa author (secondary source).
- [Network tokenization](https://developer.spreedly.com/docs/network-tokenization), Spreedly documentation, n.d., accessed 2026-11 — an independent vault as token requestor (contrast case); the networks' token services by name.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
