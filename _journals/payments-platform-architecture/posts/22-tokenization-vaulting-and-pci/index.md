---
title: "Never Touch the Card: Tokenization, Vaults and PCI Scope"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How do payment providers keep card numbers out of everyone's systems, including most of their own? They collect the number in a frame they serve, hand back a token and lock the number in an isolated vault, which leaves the merchant its payment page and stored cards it holds only as tokens."
permalink: tokenization-vaulting-and-pci
timetoread: 28 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn how card numbers are kept out of your systems, which PCI questionnaire each integration leads to, and what stays yours after tokenization.

> **KEY POINTS:**
>
> * **Scope follows the card number's path.** The card industry's security standard binds every system a card number passes through or can affect. At both Stripe and Adyen, a redirect or hosted card fields lead to the shortest questionnaire, SAQ A, and raw card numbers sent to the API to the longest, SAQ D.
> * **The provider gives the number one home and hands everyone else a reference.** Your token works only with that provider. Stripe documents a vault that shares no credentials with its other services; Adyen names its vault and publishes less. Neither publishes a design.
> * **Two things stay yours.** The page around the card fields: since 31 March 2025 a merchant filing SAQ A must confirm that scripts on it cannot attack the form. And your stored cards: moving them is a transfer between providers that takes weeks.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Card in the Log** — a card number reaches a system never meant to see it, through a script on the payment page or a support chat, and scope grows silently.
> * **The Vault Hostage** — stored cards exist only as one provider's tokens, so leaving is a transfer between two vaults that the merchant cannot perform itself.

<br>
On the weekend of 8–9 August 2026, bots entered 61,000 stolen card numbers through the booking widget of Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]). Not one of those numbers reached a Larkfield server, log or database. Larkfield takes €1.12 billion a year in payments for its studios and stores no card numbers at all. **How does a company do that? And once it holds no card numbers, is card data still its problem?** Six months later, Larkfield could not sign one line of the shortest security form the card industry has.

This chapter answers both questions. Payment providers keep card numbers out of your systems with three moves. They collect the number in a page or frame that they serve, so your code never sees it in readable form. They hand you a **token**, an identifier that works only with them. And they confine the real numbers to a **vault** kept apart from their own other systems, so that most of the provider cannot see a card number either. Payments replaced the engineer's habit of protecting sensitive data with a stronger rule, never let it in, and that rule leaves a remainder. **The page where the number is typed is still yours, and your stored cards exist only as one provider's tokens.**

**Where we are in the payment's journey.** Mila Janssen's €120.00 class pass of Tuesday 9 March 2027 was paid from her phone's wallet, so no card number was typed that evening ([[network-tokens]] covers wallets). This chapter covers a moment eight weeks earlier. On 12 January 2027 Mila set up her €49.00 monthly membership at Studio Noord by typing her Dutch Visa debit card into the booking app. That is the one point where a card number could have entered Larkfield's systems, before any authorization, the request to her bank to approve ([[payment-authorization]]).

The chapter starts with the line of the form that Larkfield cannot sign. It then explains how the security standard decides what you answer for: by the path a card number takes. Next come the mechanism that takes your servers off that path and returns a token, and what Stripe and Adyen have published about the vault behind it. Four ways to collect a card follow, with the form each leads to. Two sections argue what stays with you: the page around the card fields, and stored cards held only as tokens. Then come the comparison of Stripe and Adyen, Larkfield's own inventory, and the ways the design fails. For the security of a commerce site more broadly, see [[commerce-security]] in the sibling book ORDERED.

## Setting the Scene at Larkfield: One New Line on the Shortest Form

Larkfield has collected cards the same way since Daniel Osei, its CTO, wrote the first Stripe integration in 2017: through card fields that the provider serves. Its databases hold tokens and no card numbers. Each January Jonas Weber, the Risk and Compliance Lead, confirms this to both providers on a **self-assessment questionnaire** (SAQ), the form on which a business attests that it meets the card industry's security standard. Larkfield files the shortest one, SAQ A. Keel, Larkfield's 2027 payments program, turns the habit into a rule, decision K4: card numbers never touch Larkfield.

In January 2027 the form has a line that Jonas cannot sign from memory. Since 31 March 2025 a merchant using SAQ A must, in the words of the card industry's standards council (announcement of 30 January 2025), "confirm their site is not susceptible to attacks from scripts that could affect the merchant's e-commerce system(s)". Tom Hendriks, a senior payments engineer, opens the browser's developer tools on the payment step of the booking widget, the public booking page Larkfield serves for each studio. He counts **17 third-party scripts from 9 domains**: analytics, a chat widget, an A/B testing tool, and a tag manager through which the marketing team adds more without a deploy. Four have no known owner.

Femke de Graaf, who has led payments engineering since January, turns the unsigned line into three questions. **Which path does a card number take, and what does that path make us answer for? What do we hold instead of the number, and where is the number kept? And what, on our page and in our plans, is still ours?** The chapter takes them in that order.

## PCI Scope Follows the Path the Card Number Takes

The standard behind the form is the **Payment Card Industry Data Security Standard (PCI DSS)**. It protects the card number, which the industry calls the **primary account number (PAN)**, and the other data on a card. It is written by the PCI Security Standards Council (PCI SSC), formed by the five large card brands. The council's own page (n.d., accessed November 2026) says whom it binds: "Entities that store, process, or transmit cardholder data (CHD) and/or sensitive authentication data (SAD) or could impact the security of the cardholder data environment (CDE)". You are bound by touching card data, and also by being able to affect a system that does. Version 4.0.1, published on 11 June 2024, has been the only active version since 31 December 2024.

**Scope** is the set of systems the standard reaches. Its core is the **cardholder data environment**: every server, queue, log and support tool that stores, processes or transmits a card number, plus anything that can affect their security. A system the number never reaches, and that cannot affect one it does reach, stays out. So scope is decided by architecture, and the cheapest security control is to shorten the path a card number takes through your systems, ideally to nothing. Stripe's PCI guide (n.d., accessed November 2026) says what the full path costs: a business that handles card data "might be required to meet each of the 300+ security controls in PCI DSS".

The council writes the standard and does not enforce it. Its post of 30 January 2025 says: "Compliance validation requirements are set by brands, acquirers, payment facilitators, etc." Acquirers and payment facilitators are the firms that take card payments on a merchant's behalf ([[acquiring-and-network-connectivity]]), so in practice your provider tells you which document it wants. Stripe's guide summarizes the tiers: a merchant above 6 million Visa or 6 million Mastercard transactions a year is Level 1 and needs a yearly Report on Compliance from a Qualified Security Assessor, an accredited auditor. Smaller merchants file an SAQ whose type depends on the integration. Adyen's PCI guide (n.d., accessed November 2026) says its requirements "may differ from what other acquirers require", so the mapping from integration to form is each provider's to state.

For online payments three questionnaires matter, and they order merchants by how much of the card number's path they own. The same council post defines the shortest: SAQ A is for "merchants with account data functions completely outsourced to PCI DSS validated and compliant third parties". The other two are given as the providers' guides apply them; the council's questionnaire documents sit behind a license page I could not read. Card readers have forms of their own ([[in-person-payments]]).

| Questionnaire | Applies when | What it says about the path |
| --- | --- | --- |
| **SAQ A** | Every card input is on a page or in a frame the provider serves (both guides) | The readable number never reaches you |
| **SAQ A-EP** | Your own page hosts the form and passes the number to the provider from the browser (Stripe: legacy Stripe.js v2) | Your page handles the number; your servers do not |
| **SAQ D** | Everything else, including raw card numbers sent from your server to the API (both guides) | Your systems are on the path |

## How a Card Number Reaches the Provider Without Passing Through You

A **hosted field** is a card input inside an iframe that the provider serves from its own domain. Your page decides where the field sits and how it looks. It cannot read what is typed, because the browser's same-origin policy stops a script on your page from reaching into a frame served from another origin. Stripe's PCI guide states the design: "Checkout and Stripe.js and Elements host all card data collection inputs within an iframe served from Stripe's domain (not yours), so your customers' card information never touches your servers." At Stripe the frame sends the number straight to Stripe, as the figure below shows.

<!-- illustration-placeholder
{
  "id": "22-card-number-path",
  "status": "pending",
  "asset": "assets/images/22-tokenization-vaulting-and-pci/22-card-number-path.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that defines a hosted field",
  "visual_goal": "Show that the card number travels from the customer's browser to the provider's vault without passing through the merchant's server, and that only a token comes back to the merchant.",
  "prompt": "Create a left-to-right flow diagram with five elements. Far left: a customer at a laptop showing a web page labeled 'Merchant page'; inside that page a small framed card input box with an orange border labeled 'Provider frame'. Bottom center: a server rack icon labeled 'Merchant server'. Right of center: a blue building labeled 'Provider'. Inside the building, at the far right, an orange safe with a card symbol on its door labeled 'Vault'. Arrows: a thick orange arrow named 'card number' runs from the provider frame directly along the top to the provider building and into the safe, passing above the merchant server without touching it. A thin green arrow named 'token' runs from the provider building down to the merchant server. A thin grey dashed arrow named 'page' runs from the merchant server up to the merchant page. Next to the merchant server place a small green key tag icon to show it holds only the token. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A card number travels from a framed input on the merchant's page directly to the provider's vault; a token travels from the provider to the merchant's server.",
  "caption": "With a hosted field the card number goes from the provider's frame to the provider's vault, and the merchant's server receives only a token."
}
-->

Adyen's fields rest on a second principle. Its PCI guide says of its web components: "the cardholder data is encrypted on your shopper's browser. You do not have access to decryption keys". The encrypted data then travels through your server. Adyen's Card Component documentation (n.d., accessed November 2026) shows the merchant's server sending fields such as `encryptedCardNumber` to the payments endpoint. So at Adyen the card number does cross your server, as ciphertext, and Adyen still asks for SAQ A. On Adyen's reading, a number you can never decrypt has not reached you.

What comes back is a **provider token**: an identifier for the stored card that only this provider can turn back into a card number. Stripe's guide to network tokens (n.d., accessed November 2026) defines its own as "a nonsensitive string that can be used only by the business that collected the card". In Stripe's API reference and Payment Methods documentation (both n.d., accessed November 2026), the object named Token is for one use: "You can't store or use tokens more than once." The reusable form is a PaymentMethod, which "contains reusable payment details" and is attached to a Customer object that Stripe holds ([[payment-api-design]]). A token can still answer one question about its card: the card object carries a `fingerprint` that "Uniquely identifies this particular card number", so you can tell that two customers use the same card without seeing it.

Adyen's token has a different shape. Its tokenization page (n.d., accessed November 2026) says: "When you store a shopper's payment details, you must store the token with a unique shopper reference". The token is a `storedPaymentMethodId`, and the shopper reference is your own identifier for the customer. Adyen's page on creating tokens (n.d., accessed November 2026) says that after the authorization you "get the unique identifier and other information about the token from the recurring.token.created webhook". The payment response carries the token only "For some payment methods", and Adyen recommends always reading it from the webhook, so your webhook receiver is part of saving a card ([[payment-webhooks-and-events]]). And "By default, shopper references and tokens can only be used with one merchant account". Read together: Stripe attaches the card to a customer record it holds, and Adyen keys the card on a customer identifier you choose.

Whatever its shape, a provider token makes a narrow promise. You can charge the card again without holding its number, and you may keep a few harmless facts beside it. Stripe's integration security guide (n.d., accessed November 2026) lists "the card type, the last four digits of the card, and the expiration date" and says: "This information isn't subject to PCI compliance". The table sets the promise against what the token does not do.

| A provider token promises | It does not promise |
| --- | --- |
| You can charge the card again without storing its number | That another provider can charge it |
| You can show the last four digits and the expiry | That the cardholder's bank ever sees it: the provider sends the card number or a network token in its place *(industry practice)* ([[network-tokens]]) |
| A breach of your database exposes no card numbers | That nobody types a stolen number into the field ([[payment-fraud-and-risk]]) |

## The Vault: What Stripe and Adyen Have Published, and Where the Record Stops

A **vault** is the system that holds the real card numbers and the mapping from tokens to them. The scope rule applies inside the provider as it does to you: every provider system that can see a card number is in the provider's own cardholder data environment. A common design goal, therefore, is to make the vault the smallest possible part of the provider that can ever see a number, and to have everything else work on references.

Stripe's statement is one section of its security page (n.d., accessed November 2026), headed "Dedicated card technology". It says: "The Stripe infrastructure for storing, decrypting, and transmitting primary account numbers (PANs), such as credit card numbers, runs in a separate hosting infrastructure and doesn't share any credentials with the rest of our services, including our API and website." The separation extends to people: "A dedicated team manages our CDV in an isolated Amazon Web Services (AWS) environment that's separate from the rest of the Stripe infrastructure. We restrict access to this separate environment to a small number of specially trained engineers and review access quarterly." CDV is Stripe's Card Data Vault. The page says it is covered by the audit that certifies Stripe as a PCI Level 1 service provider, the highest tier for companies that handle card data for others.

The same section says what happens inside: "All card numbers are encrypted at rest with AES-256. Decryption keys are stored on separate machines. We tokenize PANs internally, isolating raw numbers from the rest of our infrastructure. None of the Stripe internal servers and daemons can obtain plaintext card numbers, but they can request that cards are sent to a service provider on a static allowlist." So most of Stripe is in your position: it holds references. A service cannot fetch a card number. It can ask the vault to send one to a destination on a fixed list, which the page does not name.

<!-- illustration-placeholder
{
  "id": "22-vault-inside-the-provider",
  "status": "pending",
  "asset": "assets/images/22-tokenization-vaulting-and-pci/22-vault-inside-the-provider.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that quotes Stripe on internal tokenization and the static allowlist",
  "visual_goal": "Show the vault as a small walled enclosure inside the provider: the provider's other services hold only tokens, and card numbers leave through one guarded exit toward approved destinations.",
  "prompt": "Create a layout diagram of one large rounded rectangle labeled 'Provider'. Inside it, on the left two thirds, draw three blue service boxes in a row labeled 'API', 'Dashboard' and 'Billing', each with a small green key tag icon beside it. Inside the large rectangle on the right third, draw a smaller enclosure with a thick orange wall labeled 'Vault', containing an orange safe with a card symbol and, set slightly apart inside the same enclosure, a small separate box with a key icon labeled 'Keys'. Arrows: from each of the three service boxes a thin green arrow named 'token' points to a single small gate in the orange wall. From the vault enclosure one thick orange arrow named 'card number' leaves through a second gate on the far right edge of the provider and ends at a row of three generic grey buildings outside the provider labeled 'Approved list'. No arrow carries a card number from the vault back to the service boxes; show a small red barred line on the wall between the vault and the services to make that visible. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Inside a provider, three services hold tokens and send them to a walled vault; card numbers leave the vault only toward a list of approved destinations.",
  "caption": "The vault pattern as Stripe describes it: the provider's own services hold tokens, and a card number leaves the vault only toward a destination on a fixed list."
}
-->

Adyen publishes less. Its tokenization page names the store, "we store payment details in the Adyen Vault", and makes one statement on its security: "We use client-side encryption (CSE) and end-to-end encryption to ensure that sensitive data is never exposed. All cryptographic keys are managed in a secure and compliant manner". Its page on forwarding card details (n.d., accessed November 2026) shows that storage is regional: "Make sure that your live endpoint region matches your Adyen token vault storage region." Its PCI guide says Adyen is assessed yearly as a Level 1 service provider. I found no Adyen statement comparable to Stripe's on separate infrastructure, credentials, the encryption algorithm or where keys are kept.

Here the public record stops, for both companies. Neither publishes a key-management design, a statement on hardware security modules (tamper-resistant devices that hold keys) for card data, a key rotation policy, or a description of how an internal service exchanges a token for a card number. I found no engineering article or talk on either card vault on the companies' blogs or documentation sites. The nearest thing is an Adyen article of 1 October 2019 by Sriram Kunjathur about tokenizing personal data, "credit card details" among its examples, in the data platform behind Adyen's reports: incoming data "passes through our Tokenization system, which encrypts the data with a key from the HSM-backed vault key manager". It does not say this is the store behind payment tokens, so I do not read it as describing the card vault. **(Evidence age: 7 years; the current system may differ.)**

> **INFERENCE, NOT DOCUMENTED:** Adyen's card vault probably follows the pattern Stripe describes: a small isolated environment, separately held keys, and plaintext released only toward card networks and other approved destinations. Both pass the same yearly assessment against the same standard, which rewards the smallest possible environment. An assessment attests that controls exist; it publishes no design.

## Four Ways to Collect a Card, and the Questionnaire Each Leads To

There are four realistic ways to collect a card. They trade how much of the card number's path runs through things you control against how much control you keep over the form. They are taken here from the least scope to the most, as in the figure below.

<!-- illustration-placeholder
{
  "id": "22-four-ways-to-collect",
  "status": "pending",
  "asset": "assets/images/22-tokenization-vaulting-and-pci/22-four-ways-to-collect.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that introduces the four designs",
  "visual_goal": "Order the four ways of collecting a card by how much of the card number's path the merchant owns, from none to all.",
  "prompt": "Create a four-row comparison diagram. Each row is a horizontal lane with a browser window on the left, a merchant server icon in the middle and a blue provider building on the right. Row 1, labeled 'Redirect': the browser shows a full page with an orange border (the provider's page); an orange arrow goes from the browser directly to the provider, passing above the merchant server. Row 2, labeled 'Hosted fields': the browser shows a grey page containing a small orange-bordered box; an orange arrow goes from the small box directly to the provider. Row 3, labeled 'Encrypted form': the browser shows a grey page with a padlock on its input; an orange arrow with a padlock icon passes through the merchant server and on to the provider. Row 4, labeled 'Raw API': the browser shows a plain grey page; an orange arrow without a padlock goes into the merchant server and then on to the provider, and the merchant server is tinted orange. At the right end of each row draw a horizontal bar showing the merchant's remaining scope: very short and green for row 1, short and green for row 2, medium and orange for row 3, long and orange for row 4. Above the bars place the single label 'Your scope'. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Four lanes showing a card number's path for a redirect, hosted fields, an encrypted own form and the raw API, with a bar for the merchant's scope growing from the first to the last.",
  "caption": "Four ways to collect a card, ordered by how much of the card number's path the merchant owns: redirect, hosted fields, an own form encrypted in the browser, and raw numbers to the API."
}
-->

**A redirect to the provider's page.** The customer leaves your site, types the card on a page the provider hosts, and is sent back. Stripe's Checkout documentation (n.d., accessed November 2026) offers a payment page "via a redirect to a Stripe-hosted page"; Adyen's equivalent is Hosted Checkout. Both ask for SAQ A. You give up control of the page and get the shortest list of obligations: the council's FAQ 1588 (n.d., accessed November 2026) says the script line that stopped Jonas "does not apply to e-commerce merchants with a webpage that redirects customers". Adyen's guide gives each integration a risk label, rates this one "Low", and names what remains: an attacker inside your website could "change the redirect from an Adyen-hosted payment page to a fraudulent payment website".

**Hosted fields in your page.** The customer stays on your page, and only the card inputs sit in the provider's frame: Stripe's Elements and embedded Checkout, Adyen's Drop-in and Components. This also leads to SAQ A, as do both companies' mobile components. It carries one more condition than the redirect, the **script criterion**: the line of the form that asks you to confirm your page cannot be used for a script attack. The same FAQ says the criterion applies to a webpage "that includes a TPSP's/payment processor's embedded payment page/form", where TPSP means third-party service provider. Adyen rates the web version "Low-Medium".

**Your own form, with encryption in the browser.** Adyen allows a form that is entirely yours under the short questionnaire. Its guide says of a form built with a JSON Web Encryption (JWE) library: "Cardholder data is encrypted on your shopper's browser using a third-party JWE library, sent to your server, and then transmitted to Adyen". Adyen sets the risk label at "Medium", because "you provide the payment form", and adds that the integration "could still be scoped on the Self Assessment Questionnaire A (SAQ A) for PCI DSS compliance because once encrypted, you cannot decrypt the data". Stripe's guide lists no equivalent; its only own-form path in the browser is a legacy library: "Using Stripe.js v2 to pass card data entered in a form hosted on your own site requires completing the SAQ A-EP annually".

**Raw card numbers to the API.** Your server receives the card number, so your systems are on the path and both companies ask for the full questionnaire. Stripe: "When you pass card information directly to Stripe's API, your integration is directly handling that data", and the form is SAQ D, "the most demanding of the SAQs". Adyen rates the design "High": "your system receives, transmits, and potentially stores and processes cardholder data". At Stripe there is a second cost. The same guide says: "Radar, our fraud prevention tool that includes risk evaluation and rules, is only available when using any of our methods for client-side tokenization." Stripe's API reference for tokens says only that Radar "performs best" with such integrations, and its Radar page on risk factors (n.d., accessed November 2026) shows what is lost: signals "automatically captured by Stripe.js and our SDKs" ([[payment-fraud-and-risk]]).

The four designs show that the form field is the visible part of a compliance decision. The rule I use: choose by the questionnaire and the remaining risk you are willing to own, and only then by how the form should look. Hosted fields are right for most merchants, and a redirect when nobody will maintain a payment page. The encrypted own form is for a team that can say why the provider's fields will not do. The raw API is for a business that already runs an audited card environment. Reversing the choice later means a different questionnaire, so make it before the first design mock-up.

| Design | Where the card number travels | Stripe asks for | Adyen asks for, with its risk label | What you still answer for |
| --- | --- | --- | --- | --- |
| Redirect | Browser to provider | SAQ A | SAQ A, "Low" | The link that sends the customer there |
| Hosted fields | From a frame in your page to the provider (at Adyen as ciphertext through your server) | SAQ A | SAQ A, "Low-Medium" | The page around the frame |
| Own form, encrypted | Your page, then your server, as ciphertext | Not listed (legacy: SAQ A-EP) | SAQ A, "Medium" | The form, its encryption script, the page |
| Raw API | Your server, readable | SAQ D | SAQ D, "High" | Everything on the path |

## What Stays Yours: The Page Around the Card Fields

A hosted field takes your servers off the card number's path. It leaves your page on it. A script running on the page that embeds the frame cannot read into the frame, but it can remove the frame, or lay a look-alike field over it, and collect what the customer types. Adyen's PCI guide describes the attack on its own components: "attackers can create alternative content for the Drop-in or Components, or drop an iframe over the already existing iframe. In this scenario, the payment may still be completed, but a copy of the cardholder data is sent to the attacker." The council's guidance of March 2025 calls this e-skimming. Stripe's security guide warns: "Including JavaScript from other sites makes your security dependent on theirs and poses a security risk."

<!-- illustration-placeholder
{
  "id": "22-overlay-on-the-payment-page",
  "status": "pending",
  "asset": "assets/images/22-tokenization-vaulting-and-pci/22-overlay-on-the-payment-page.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that describes the overlay attack",
  "visual_goal": "Make the overlay attack visible: the provider's frame is intact, and a third-party script on the merchant's page lays a look-alike field over it that copies the digits to an attacker.",
  "prompt": "Create a conceptual illustration of one large browser window labeled 'Your page'. In the center of the page is a card input box with a solid blue border labeled 'Provider frame'. Floating slightly above and offset from it, drawn as a semi-transparent sheet with an orange dashed border and a small drop shadow, is an identical-looking card input box labeled 'Copy'. A customer's hand at a keyboard at the bottom types, and a thin grey arrow named 'typed digits' goes from the keyboard up into the orange dashed copy, not into the blue frame. On the left edge of the page is a column of five small script tag icons; four are grey and one is orange. A thin orange arrow named 'injects' goes from the orange script icon to the dashed copy. From the dashed copy a thick orange arrow named 'stolen copy' leaves the browser window to a dark hooded generic figure at a laptop on the far right. From the blue provider frame a thin green arrow named 'payment' goes to a small blue provider building at the top right, showing that the payment still completes. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A script on the merchant's page places a look-alike card field over the provider's frame; typed digits go to the copy and on to an attacker while the payment still completes.",
  "caption": "A script on your page cannot read the provider's frame, but it can cover it with a copy: the payment still completes and the attacker receives the card number."
}
-->

PCI DSS answered with two requirements that took effect on 31 March 2025. Requirement 6.4.3, as Adyen's script-security page restates it (n.d., accessed November 2026), asks that for every script on a payment page "A method is implemented to confirm that each script is authorized", "A method is implemented to assure the integrity of each script", and "An inventory of all scripts is maintained with written justification as to why each is necessary". Requirement 11.6.1 asks for a mechanism that detects unauthorized changes to the page's scripts and security headers. On 30 January 2025 the council removed both from SAQ A and added, in their place, the eligibility line from the Larkfield scene. It wrote that the changes "do not remove or diminish the underlying requirements within PCI DSS". The form became shorter, and the page remained the merchant's.

FAQ 1588 gives two ways to make that confirmation. You can do it yourself, by "Using techniques such as, but not limited to, those detailed in PCI DSS Requirements 6.4.3 and 11.6.1". Or you can obtain your provider's confirmation that its solution, implemented as instructed, "includes techniques that protect the merchant's payment page from script attacks". The two companies give you different material. Adyen's script-security page names both requirements and recommends a content security policy, a response header that tells the browser which sources of scripts and frames a page may use. Adyen's SAQ A eligibility page (n.d., accessed November 2026) says the requirements "remain applicable" to merchants that file SAQ D or are assessed on site. Stripe's security guide publishes the policy directives its products need. Neither it nor Stripe's PCI guide mentions 6.4.3 or 11.6.1 by number; I searched those two pages, not all of Stripe's support material.

Whichever route goes on the form, I would put three controls in place. First, an inventory of every script on the payment step, each with a reason and a named owner; a script nobody can explain is removed. Second, a content security policy that allows only the listed sources. It does not help when an allowed script is itself compromised, so keep the list short. Third, a payment step with as few third-party scripts as the business can bear, on its own page if possible. Start with the tag manager: its job is to load other scripts without a code review.

## What Else Stays Yours: Stored Cards You Hold Only as Tokens

The second thing that stays with you is less visible. You never held the card numbers, so you cannot copy your stored cards to another provider. A token is a key into the first provider's vault and opens nothing else. This is the failure pattern the book calls **The Vault Hostage** ([[where-payment-systems-go-wrong]]). [[payment-routing-and-orchestration]] covers where a vault can sit when there are several providers; this section covers how cards get into one and out of it.

Both companies document taking cards in. It is a file transfer between the two providers, and you never see the file. Stripe's import page (n.d., accessed November 2026) says the previous processor "encrypts your data with the Stripe PGP key and uploads it", and Stripe returns a mapping file from old identifiers to new ones. On timing: "Processors can take anywhere from a few days to several months to produce a final export". Adyen's import page (n.d., accessed November 2026) says: "Because of technical and compliance complexity, migrating payment data usually takes 10 days or more."

Leaving is documented by one of the two. Stripe's export page (n.d., accessed November 2026) opens with a position: "We believe our customers own the sensitive data they entrust to Stripe." Stripe says "we can only transfer your card data to another PCI DSS Level 1-compliant payment processor", and asks for proof of that status. Some things stay behind: "Stripe doesn't export your account's payment history, subscriptions, or other objects", and "We exclude any credentials saved through Link", Stripe's own wallet. For Adyen I found no documentation page that describes an export; its documentation index lists none. A help-center article on preparing a token export is still in Adyen's help sitemap, but in November 2026 its address redirects to the tokenization page, which does not mention export. That is a gap in the public record, not a statement about what Adyen does for a merchant that leaves. Settle it in the contract.

Short of moving the cards, both providers will forward one. You send a request addressed to a third party, with placeholders where the card details belong; the provider fills them in from its vault and sends it on. Stripe's Vault and Forward API (n.d., accessed November 2026) is "available only to businesses with a dedicated Stripe account team". Adyen's forwarding page says "We support forwarding card details, and network tokens", once its support team enables it. Forwarding keeps the first provider in the path of every such payment. It lets you use a card elsewhere, not leave.

So I plan a move of stored cards as a project of weeks, and I plan it before I need it. Adyen's import page recommends "dividing the migration into three stages", the first being to "Switch all new tokenizations/sign-ups to Adyen, but keep the recurring charges for old customers at your old provider"; the import and the switch of existing customers follow. The staging is sound for any destination, because renewals keep running while the file is in transit. Before signing with any provider I ask how cards leave, how many weeks it takes, and what does not travel. Neither company's export pages say whether network tokens travel; Adyen's terms (2025) describe a service that shares them, which the next chapter takes up.

## Stripe and Adyen: Where They Differ

Both companies are assessed Level 1 service providers, and both keep card numbers out of a merchant's systems by the same three moves. The public record shows five differences and one near-match. Every Stripe and Adyen cell is a fact cited earlier in this chapter, from undated documentation accessed in November 2026, or the words "Not public". The last column is my reading: an inference, not documentation.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Own form, encrypted in the browser | Not listed in its PCI guide; a legacy own form means SAQ A-EP (n.d.) | SAQ A with a third-party JWE library, risk "Medium" (n.d.) | Adyen accepts ciphertext crossing the merchant's server; Stripe's fields send the number past it |
| Reusable token | PaymentMethod attached to a Customer, returned in the API response (n.d.) | `storedPaymentMethodId` paired with the merchant's shopper reference; Adyen recommends reading it from a webhook (n.d.) | Stripe holds the customer record; Adyen keys on yours and points you to an asynchronous event |
| Published description of the vault | Separate hosting, no shared credentials, AES-256, keys on separate machines, plaintext only to an allowlist (n.d.) | A name, regional storage, keys "managed in a secure and compliant manner" (n.d.). Isolation: Not public | Stripe states more; neither publishes a design |
| Script-security guidance | Policy directives and a warning; the two guides read do not name 6.4.3 or 11.6.1 (n.d.) | A page that names both requirements (n.d.) | Adyen documents the requirement, Stripe the mechanism; the page is yours on either |
| Export of stored cards | Documented: to a Level 1 processor, with exclusions (n.d.) | Help-center article listed; procedure not readable | On Adyen, get it in writing; on Stripe, read the exclusions |
| Forwarding a stored card | For businesses with a dedicated account team (n.d.) | Enabled by support; also network tokens (n.d.) | No material difference in the public record |

What should you do differently? On Stripe, treat the token as part of a customer record that Stripe holds, and rely on the documented export while reading what it leaves out. On Adyen, the token hangs on your own customer identifier, so choose a stable one; read the token from the webhook; and get the export procedure, its timing and its cost in writing before you store the first card. If you need a card form wholly your own, Adyen offers a route under SAQ A at the risk label "Medium"; on Stripe I would use its fields.

## In Practice at Larkfield: SAQ A on Two Providers and a Script Inventory

Take Femke's first two questions on one card. When Mila typed her Visa debit card on 12 January 2027, the digits went into Adyen's card fields on the booking app's payment step and were encrypted in her browser. What crossed Larkfield's server was ciphertext. Her bank approved the first payment after a 3-D Secure challenge, the issuing bank's check that she is the cardholder ([[three-d-secure-and-sca]]), and Adyen's webhook then delivered a token. The payment record store holds that token under Mila's member identifier, which serves as the shopper reference, with the last four digits and the expiry. Each €49.00 renewal on the 1st of the month charges the token. Had Studio Noord been on Stripe, the record would hold a PaymentMethod identifier instead. On both providers no readable card number enters a Larkfield system, which is what SAQ A attests.

The third question starts with the page. Tom's count becomes the script inventory that K4 asks for. The payment step moves to a page of its own, and each script on it needs a reason and an owner. The content security policy runs first in report-only mode, a step Adyen's script-security page recommends, and is then enforced. The figures are Larkfield's and illustrative.

| | Before (January 2027) | After (decision K4) |
| --- | --- | --- |
| Scripts on the payment step | 17 third-party scripts from 9 domains | 3 scripts from 2 domains: Larkfield's bundle and error reporter, the provider's card library |
| Scripts with no known owner | 4 | 0 |
| Tag manager, chat widget, analytics, A/B testing | On the payment step | Removed from it |
| Content security policy | None | Report-only for two weeks, then enforced |
| Owner of the list | Nobody | Tom Hendriks |

The other half of the third question is the stored cards. About 940,000 membership renewals a month are charged against payment details stored at one of the two providers. The 1,140 studios in the Netherlands and Germany that are still on Stripe for online payments make the dependency concrete. Moving them to Adyen means an export from Stripe's vault and an import into Adyen's, staged over weeks. So Larkfield keeps one exit sheet per provider with three lines: how cards leave, in how many weeks, and what does not travel. The quarterly switch rehearsed under decision K8 ([[payment-routing-and-orchestration]]) does not move stored cards, and the sheet says so.

In February Jonas signs the script line. He takes the first of the council's two routes, Larkfield's own controls. K4 now reads as a list of what moved and what stayed. The card numbers moved to the two providers. The page stayed, and Tom owns its script inventory. The stored cards stayed as tokens, and Femke owns the exit sheets.

## When It Goes Wrong

**A card number arrives by a path nobody designed.** This is The Card in the Log. A member whose payment failed pastes her card number into the support chat that Aylin Demir's team runs, or a studio owner types one into a free-text notes field. The number is now in a chat transcript, a search index and their backups, and by the scope rule each of those has joined the cardholder data environment. Hosted fields cannot prevent this, because the number never went near them. Common practice is to scan inbound text for digit sequences that pass the card-number checksum (the Luhn check), to mask them on entry, and to purge what has been stored.

**A script on the payment page is compromised.** This failure is hard to see: as Adyen's guide says of the overlay attack, "the payment may still be completed", so your approval rate, your provider's dashboard and your customer show nothing unusual. Detection has to come from the page itself, which is what requirement 11.6.1 describes in Adyen's restatement: a mechanism that "alerts personnel about unauthorized modification" of the page's security headers and script contents. In practice that means collecting the policy's violation reports and alerting when the set of scripts on the payment step changes. Recovery is to remove the script, tell your providers, and follow the incident process in your contracts with them.

**A migration loses cards between two vaults.** The gap lies between the day the export file is cut and the day charging switches. Adyen's import page warns: "New tokens may still be created with your current provider while you are migrating and switching recurring to Adyen. If so, contact your provider and request the tokens created in the interim." Some identifiers will not map. Reconcile the mapping file against your own list of customers with a saved card before you switch anyone, and keep the old provider's charging path alive until the counts agree. Otherwise a member whose card did not arrive meets the failure as a failed renewal and a reminder to pay ([[invoicing-collections-and-dunning]]).

## What to Take Away

**Established.**

- PCI DSS binds every entity that stores, processes or transmits card data or could affect the security of systems that do (PCI SSC). Scope therefore follows the card number's path.
- At both Stripe and Adyen, a redirect or hosted fields lead to SAQ A, and raw card numbers sent to the API lead to SAQ D (both companies' PCI guides, accessed November 2026).
- Since 31 March 2025 a merchant filing SAQ A with embedded card fields must confirm that its page is not susceptible to script attacks. A redirect is exempt (PCI SSC, 30 January 2025, and FAQ 1588).
- Stripe documents a card data vault in separate hosting that shares no credentials with its other services. Adyen names its vault and its regional storage. Neither publishes a design.

**Depends on context.**

- Hosted fields suit most merchants. A redirect is better when nobody will maintain a payment page, or when you want the script line not to apply.
- An own form encrypted in the browser is available under SAQ A at Adyen. It is worth its "Medium" risk label only if the provider's fields cannot express the form you need.
- The raw API is right only for a business that already runs an audited card environment; at Stripe it also loses the fraud signals Stripe's client libraries collect.
- How much to invest in portability depends on how many stored cards you have. With recurring revenue, plan the exit before the first card is stored.

**The author's synthesis.**

- Tokenization gives the card number exactly one home and hands everyone else a reference, including most of the provider. The reference makes you safe and makes you dependent. I treat tokenization as a relocation with a remainder, not as a risk that has gone away.
- The one place the design cannot reach is the screen where the number is typed, and that screen belongs to whoever serves the page. So every SAQ A merchant should own two artifacts: a script inventory for the payment step, and an exit sheet for its stored cards.
- I take a provider's description of its vault exactly as far as it is published. Stripe's goes further than Adyen's, and both stop well short of a design.

## Questions to Ask

1. Trace one card number from the keyboard to the provider. Which of our systems does it pass through, readable or encrypted?
2. Which questionnaire does each provider ask of us, and has the integration changed since we last filed?
3. Which scripts run on the payment step, who owns each, and what is the reason for each?
4. How do we meet the SAQ A script line: by our own controls, or by the provider's written confirmation?
5. Where else could a card number arrive (support chat, email, notes fields), and when did we last search for one?
6. What has each provider published about how it isolates card numbers, and what does our contract add to that?
7. How do stored cards leave each provider: by what procedure, to whom, in how many weeks, at what cost, and what does not travel?

Return to the 61,000 stolen numbers of the Card-Testing Weekend. They bypassed Larkfield because a frame served by the provider collected them, and they were typed on a page Larkfield served, which is what the unsigned line of the form was asking about. Tokenization did its job that weekend and did nothing about the attack itself ([[payment-fraud-and-risk]]). Everything in this chapter was a provider token: an identifier that means something only inside one provider's vault and that the cardholder's bank never sees. The card networks issue a token of their own, which travels to the bank in place of the card number and stays valid when the card changes. [[network-tokens]] explains what that moves, and to whom.

## Sources and Evidence

*Company, product and investor sources*

- [Security at Stripe](https://docs.stripe.com/security), Stripe documentation, n.d., accessed 2026-11 — the "Dedicated card technology" section: separate hosting, no shared credentials, the isolated environment and its team, AES-256, keys on separate machines, internal tokenization, the static allowlist; the scope of Stripe's Level 1 audit.
- [PCI DSS compliance guide](https://stripe.com/guides/pci-compliance), Stripe, n.d., accessed 2026-11 — merchant levels, the questionnaire per integration, the "300+ security controls" figure, Radar's dependence on client-side tokenization, the founding of the PCI SSC (Stripe's summary).
- [Integration security guide](https://docs.stripe.com/security/guide), Stripe documentation, n.d., accessed 2026-11 — collection without passing through the merchant's servers, card data a merchant may store, the third-party script warning, content security policy directives.
- [Tokens](https://docs.stripe.com/api/tokens), Stripe API reference, n.d., accessed 2026-11 — single-use tokens; Radar "performs best" with client-side tokenization.
- [Payment Methods](https://docs.stripe.com/payments/payment-methods), Stripe documentation, n.d., accessed 2026-11 — the reusable PaymentMethod.
- [The Card object](https://docs.stripe.com/api/cards/object), Stripe API reference, n.d., accessed 2026-11 — the card fingerprint.
- [Understanding the benefits of network tokens](https://stripe.com/guides/understanding-benefits-of-network-tokens), Stripe guide, n.d., accessed 2026-11 — Stripe's definition of its own tokens.
- [Stripe Checkout](https://docs.stripe.com/payments/checkout), Stripe documentation, n.d., accessed 2026-11 — the Stripe-hosted page reached by redirect.
- [Risk factors recommendations](https://docs.stripe.com/radar/optimize-risk-factors), Stripe documentation, n.d., accessed 2026-11 — risk factors captured by Stripe.js and the SDKs; what a direct integration must send.
- [Import payment data to Stripe](https://docs.stripe.com/get-started/data-migrations/pan-import), Stripe documentation, n.d., accessed 2026-11 — the import process, the mapping file and timing.
- [Request a payment data export](https://docs.stripe.com/get-started/data-migrations/pan-export), Stripe documentation, n.d., accessed 2026-11 — the export policy, the recipient's conditions and what is not exported.
- [Forward card details to third-party API endpoints](https://docs.stripe.com/payments/vault-and-forward), Stripe documentation, n.d., accessed 2026-11 — the Vault and Forward API and who may use it.
- [PCI DSS compliance guide](https://docs.adyen.com/development-resources/pci-dss-compliance-guide), Adyen documentation, n.d., accessed 2026-11 — Adyen's Level 1 status, the questionnaire and risk label per integration, the overlay attack, browser encryption under SAQ A.
- [Self-Assessment Questionnaire A eligibility](https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility), Adyen documentation, n.d., accessed 2026-11 — the 2025 change and who still owes requirements 6.4.3 and 11.6.1.
- [Script security for ecommerce](https://docs.adyen.com/development-resources/pci-dss-compliance-guide/script-security), Adyen documentation, n.d., accessed 2026-11 — the text of requirements 6.4.3 and 11.6.1 as restated by Adyen, the content security policy recommendation, report-only mode.
- [Card Component](https://docs.adyen.com/payment-methods/cards/web-component), Adyen documentation, n.d., accessed 2026-11 — the encrypted card fields in the server-side payment request.
- [Tokenization](https://docs.adyen.com/online-payments/tokenization), Adyen documentation, n.d., accessed 2026-11 — the Adyen Vault, the statement on keys, the shopper reference, the one-merchant-account default.
- [Create tokens](https://docs.adyen.com/online-payments/tokenization/create-tokens), Adyen documentation, n.d., accessed 2026-11 — the token read from the `recurring.token.created` webhook; in the payment response only for some payment methods.
- [Forward payment details](https://docs.adyen.com/online-payments/tokenization/forward-payment-details), Adyen documentation, n.d., accessed 2026-11 — forwarding card details and network tokens, regional vault storage.
- [Import data from another payment provider](https://docs.adyen.com/development-resources/migrating-payment-data), Adyen documentation, n.d., accessed 2026-11 — import timing, the three stages, interim tokens.
- [Additional Services Terms](https://www.adyen.com/legal/additional-services-terms), Adyen, last updated 2025-06-13 — the Network Token Sharing Service.
- [Securing your personal data via tokenization](https://www.adyen.com/en_GB/knowledge-hub/securing-your-personal-data-via-tokenization), Sriram Kunjathur, Adyen, 2019-10-01 — tokenization of personal data (card details among its examples) in Adyen's data platform; not presented as the store behind payment tokens (evidence age: 7 years).
- [How can I prepare for token migration? [Export]](https://help.adyen.com/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export), Adyen help center, n.d., accessed 2026-11 — in the help sitemap; redirects (301) to the Tokenization documentation page, so not readable.

*Standards, regulation and official documentation*

- [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/), PCI Security Standards Council, n.d., accessed 2026-11 — whom the standard applies to.
- [Just Published: PCI DSS v4.0.1](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1), PCI Security Standards Council, 2024-06-11 — version dates and the 31 March 2025 effective date of the future-dated requirements.
- [Important Updates Announced for Merchants Validating to Self-Assessment Questionnaire A](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a), PCI Security Standards Council, 2025-01-30 — the definition of SAQ A, the removal of 6.4.3 and 11.6.1 from it, the new eligibility criterion, who sets validation requirements.
- [FAQ 1588: How does an e-commerce merchant meet the SAQ A eligibility criteria for scripts?](https://www.pcisecuritystandards.org/faqs/1588/), PCI Security Standards Council, n.d., accessed 2026-11 — embedded forms versus redirects, the two ways to confirm.
- [New Information Supplement: Payment Page Security and Preventing E-Skimming](https://blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming), PCI Security Standards Council, 2025-03-10 — the council's guidance on requirements 6.4.3 and 11.6.1 and the term e-skimming.

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
