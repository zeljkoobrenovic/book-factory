---
title: "Follow the Money: What Happens Between “Pay” and “Paid”"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What has to happen, and between which parties, before a card payment is money the merchant can keep? Six steps spread over days and at least five parties, and the provider that answers your API call controls none of the three steps that decide the outcome."
permalink: journey-of-a-payment
timetoread: 27 min read
---

> **IN THIS CHAPTER, YOU WILL:** Follow Mila's €120 class pass from her bank to the studio's account and learn who acts, promises and holds the money at each step.

> **KEY POINTS:**
>
> * **One payment is six steps by at least five parties.** The issuer approves, the merchant captures, the acquirer presents a clearing record, the network nets what its member banks owe each other, the provider pays out, and for about 120 days the cardholder can have it all taken back. The provider that answers the API call controls none of the three steps that decide the outcome.
> * **A message moves first, then a record, then money.** The approval the customer sees moves nothing. Money first moves at settlement, a day or more later, as net amounts between banks, so “paid” in your database stands for four facts held by four different parties.
> * **Ask which legal entity is the acquirer.** A provider can be a gateway, a payment facilitator under a bank, or the acquirer itself, and the answer changes by country. Stripe publishes its acquirer per country; Adyen publishes its licenses and its acquiring regions, and names the acquiring entity for some of them only.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Phantom Payment** — a status that reports one party's promise is stored as if the money had arrived and could not come back.
> * **The Orphaned Refund** — the dispute window stays open for about 120 days after the sale, long after most systems have stopped looking at the payment.
> * **A Card by Any Other Name** — the six-step timeline is the card's; bank transfers and some wallets drop steps and change who can take the money back.

<br>
At 19:42 on Tuesday 9 March 2027, Mila Janssen buys a ten-class pass for €120.00 from Studio Noord, a yoga studio in Utrecht, in the app of Larkfield, the fictional studio-software platform this book follows. She pays with the Dutch Visa debit card in her phone's wallet, and two seconds later the screen says **Payment successful**. Where is the €120 at 19:43? Still in Mila's own bank account. Her bank has set it aside, and nobody has received anything. The only thing that has moved is a message.

That message was a promise by Mila's bank, and it was the first of six steps. **One card payment takes six steps spread over days and carried out by at least five parties**: the cardholder's bank approves, the merchant claims the money, the merchant's side presents a record of the sale through the card network, the network works out what its member banks owe each other, the payment provider pays the merchant, and for about 120 days the cardholder can have the payment taken back. The provider that answered the API call **controls none of the three steps that decide the outcome**: it does not make the approval decision, does not run the settlement between banks and cannot stop a dispute.

So every status a provider returns is a delayed report of what someone else decided. Stripe's documentation (n.d., accessed November 2026) says so in one sentence: "A `succeeded` status indicates that the payment completed successfully according to the payment method’s processing flow, but funds can still be refunded, disputed, returned, or reversed". The useful questions about any status are **whose decision it reports and what is still open after it**.

**Where we are in the payment's journey.** Everywhere, at low resolution. This chapter follows Mila's class pass from the approval at 19:42 on Tuesday to Studio Noord's payout on Thursday 11 March and into the dispute window that follows. Each later chapter enlarges one stretch of that path: the next four take the steps in order, and [[journey-card-payment]] replays the whole payment with the systems in view.

The chapter starts at Larkfield the morning after, with a studio owner asking where her money is. It then defines the parties, lays out the timeline, and shows how three-party networks, bank transfers and wallets bend the model. Next come the positions a provider can take in the chain and what Stripe and Adyen document about their own. Mila's €120 is then followed party by party, and the chapter ends with how each step fails. The finance-side view of the same flows is in [[payments-fundamentals]], in the sibling book RECONCILED.

## Setting the Scene at Larkfield: One Word for Four Facts

On Wednesday 10 March 2027, the morning after Mila's purchase, Ines Bakker opens Larkfield's back office. Ines owns Studio Noord. The pass is there, marked `paid`, one of the five states Larkfield's payment record store uses (`pending`, `authorized`, `paid`, `refunded`, `disputed`; see [[meet-larkfield]]). Her bank account shows no €120. She writes to support: "It says paid. Paid to whom?" Aylin Demir, Head of Studio Support, forwards it to the payments team.

Femke de Graaf, who has led payments engineering since January, answers with four questions that the word `paid` cannot answer. Who approved this payment? Has any money moved yet? When will the studio receive it? Until when can it be taken back? Each has a different party behind it: a bank Larkfield has no contract with, a card network's overnight process, the provider's payout schedule, and Mila herself. **One word in the record stands for four facts held by four parties**, and the rest of this chapter is what Femke needs to answer Ines properly.

<!-- illustration-placeholder
{
  "id": "01-one-tick-four-promises",
  "status": "pending",
  "asset": "assets/images/01-journey-of-a-payment/01-one-tick-four-promises.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph in the Larkfield scene that lists the four questions the word paid cannot answer",
  "visual_goal": "Show that the single success tick a customer sees stands for four separate promises, each held by a different party with its own clock.",
  "prompt": "Create a conceptual explainer illustration in two halves. Left third: a smartphone held by a generic customer, its screen showing one large green check mark and the label \"Paid\". Right two thirds: four paper notes pinned in a row from left to right, each with a small clock above it showing a different time. The first note is held by a small bank building and labeled \"Approved\"; the second is held by a small shop front and labeled \"Claimed\"; the third is held by a hub with lines to two bank buildings and labeled \"Settled\"; the fourth is held by an office building with a payout chute and labeled \"Paid out\". A thin arrow labeled \"one answer\" runs from the phone to the first note only. A dashed curved arrow labeled \"can come back\" runs from the fourth note back over the top toward the phone. The four clocks are visibly different sizes, the last one largest. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A phone showing one green tick beside four pinned notes labeled Approved, Claimed, Settled and Paid out, each with its own clock.",
  "caption": "One answer on the screen stands for four separate facts, each held by a different party on its own clock."
}
-->

## The Parties: Four in the Model, More in Practice

The card networks describe the model themselves. Visa's annual report for fiscal 2026 (filed November 2026) says it provides "transaction processing services (primarily authorization, clearing and settlement) among consumers, issuing and acquiring financial institutions and sellers in a structure we call the “four-party” model". Mastercard's report for 2025 (filed February 2026) names the same four: "account holder (a person or entity who holds a card or uses another device enabled for payment), issuer (the account holder’s financial institution), merchant and acquirer (the merchant’s financial institution)". The **four-party model** is the **cardholder**; the **issuer**, the bank that gave the cardholder the card and keeps the account behind it; the **merchant**, who sells; and the **acquirer**, the institution that accepts card payments on the merchant's behalf. The **card network** (Visa or Mastercard; Adyen's documentation says "scheme") stands between the two institutions, which makes five parties.

The network's brand is on the card, but it is not a bank. Visa writes: "Visa is not a financial institution. We do not issue cards, extend credit or set rates and fees for account holders of Visa card products nor do we earn revenue from or bear credit risk with respect to any of these activities." Mastercard says the same of itself: "We do not issue cards, extend credit, determine or receive revenue from interest rates or other fees charged to account holders by issuers". A network carries messages between issuers and acquirers, sets the rules both follow and calculates what they owe each other. It does not decide whether Mila's payment is approved, and it keeps no account for Mila or the studio.

The acquirer, in turn, is defined by permission and not by software. Visa's public rules (edition of 24 October 2026) define an Acquirer as "A Member that signs a Merchant or Payment Facilitator, provides a Cash Disbursement to a Cardholder, or loads funds to a Prepaid Card, and directly or indirectly enters a Transaction into Interchange". "Member" is the word that matters: acquiring comes with membership of the network. Stripe's services agreement (n.d., accessed November 2026) describes the role from the merchant's side, as an entity authorized to "receive and remit settlement funds for authorized and cleared Transactions". A second permission comes from the state; in Adyen's words (n.d., accessed November 2026), "Acquirers must be licensed by local financial regulators and card schemes to relay transactions." Membership is the subject of [[acquiring-and-network-connectivity]], and what a license lets its holder do with other people's money is in [[licences-and-safeguarding]].

Around those five parties the industry uses further names, which are commercial labels more than defined roles. Two questions sort them: **is this company a member of the network, and does it hold the merchant's money?** The table gives common industry usage; only the two quoted definitions come from Visa's rules.

| Name | What it does | Network member? | Holds the merchant's money? |
| --- | --- | --- | --- |
| **Acquirer** | Signs the merchant, submits its transactions, receives the settlement | Yes | Yes, between settlement and payout |
| **Processor** | Runs the technical connection; Visa: an Acquirer Processor is "A non-Member agent or processor that a Member has engaged" | No | No |
| **Gateway** | Carries payment data from the merchant to an acquirer or processor | No | No |
| **Payment facilitator** (PayFac) | Signs many small merchants under one acquirer; Visa: "An entity that contracts with an Acquirer to deposit Transactions, receive settlement from, or contract with an Acquirer on behalf of a Sponsored Merchant" | No; its acquirer registers it with the network | Usually: it receives settlement from the acquirer and pays its merchants |
| **Payment service provider** (PSP), here "the provider" | Packages some or all of the above behind one contract and one API | Depends on provider and country | Depends |
| **Platform** | Software through which other businesses sell and get paid | No | Only if licensed to ([[platform-payment-models]]) |

Who holds the money, and who loses when something goes wrong, also changes from party to party. The networks document one boundary: Visa's report says it will "indemnify issuers and acquirers for settlement losses they may suffer due to the failure of another issuer or acquirer to honor its settlement obligations", and Mastercard's states where that protection ends: "We do not, however, guarantee payments to merchants by their acquirers". Between settlement and payout, a merchant's money is as safe as its acquirer or provider. The rest of the table is a generalization: **contracts and local law can move any cell**. A *chargeback* is a payment the issuer forces back after the cardholder disputes it.

| Party | Holds the money | Carries which risk |
| --- | --- | --- |
| Cardholder | Until the issuer pays it away | Little: can dispute for months |
| Issuer | The cardholder's balance or credit line, until settlement | The cardholder's credit; fraud where the rules leave it with the issuer ([[three-d-secure-and-sca]]) |
| Network | Holds no customer money | Settlement risk between its members |
| Acquirer | From settlement until it pays the merchant or the facilitator | The merchant's: refunds and chargebacks the merchant cannot pay |
| Provider or payment facilitator | Usually, between settlement and payout | Its merchants' losses |
| Merchant, or the seller on a platform | After payout | Refunds, chargebacks, fees |

<!-- illustration-placeholder
{
  "id": "01-four-party-model",
  "status": "pending",
  "asset": "assets/images/01-journey-of-a-payment/01-four-party-model.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of who holds the money and which risk each party carries",
  "visual_goal": "Show where each party sits: cardholder and issuer on one side, merchant and acquirer on the other, the card network between the two institutions, with the provider and the platform on the merchant's side.",
  "prompt": "Create a structural explainer diagram of a card payment's parties. Left side, top: a generic person holding a phone, labeled \"Cardholder\". Left side, bottom: a bank building labeled \"Issuer\". Center: a round hub labeled \"Network\". Right side, bottom: a second bank building labeled \"Acquirer\", with a smaller box attached to its left edge labeled \"Provider\". Right side, top: a small yoga studio front labeled \"Merchant\", with a tablet-shaped box attached to its left edge labeled \"Platform\". Arrows: a solid arrow from Cardholder to Merchant labeled \"buys\"; a solid vertical line between Cardholder and Issuer labeled \"account\"; a solid vertical line between Merchant and Acquirer labeled \"contract\"; a double-headed arrow from Issuer to Network labeled \"messages\"; a double-headed arrow from Network to Acquirer labeled \"messages\"; a thicker orange arrow from Issuer through the Network hub to Acquirer labeled \"money\"; a green arrow from Acquirer up to Merchant labeled \"payout\". The Issuer and Acquirer buildings are the same size; the Network hub is clearly not a bank building. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Diagram of the four-party model: cardholder and issuer on the left, merchant and acquirer on the right, the card network between the two banks, with a provider beside the acquirer and a platform beside the merchant.",
  "caption": "The four-party model: cardholder and issuer on one side, merchant and acquirer on the other, and the card network between the two institutions; the provider stands with the acquirer and the platform with the merchant."
}
-->

## The Timeline: A Message, a Record, Then Money

Three different things move in a card payment, and they move in a fixed order: **a message, then a record, then money**. Mastercard's report for 2025 describes them as three services: "we enable the routing of a transaction to the issuer for its approval, facilitate the exchange of financial transaction information between issuer and acquirer after a successfully conducted transaction, and settle the transaction by facilitating the exchange of funds between parties via settlement banks chosen by us and our customers". Approval, then information, then funds; the industry's names for them are authorization, clearing and settlement.

Add the merchant's claim, the provider's payout and the cardholder's right to object, and there are six steps. The times in the table are typical industry practice, not rules; they vary by network, country and provider.

| Step | Typical time after "pay" | Who acts | What moves | The promise |
| --- | --- | --- | --- | --- |
| 1. **Authorization** | Seconds | The issuer decides | A message; a hold on the cardholder's account | Issuer: "I will honor a claim for this amount if it arrives in time" |
| 2. **Capture** | Seconds to days | The merchant, or the provider for it | An instruction | Merchant: "I claim the money" |
| 3. **Clearing** | The same or the next day | The acquirer, through the network | A record | Acquirer: "this is the final amount and data" |
| 4. **Settlement** | The next business day or later | The network and its member banks | Money, as daily net amounts between members | Network: its members pay each other |
| 5. **Payout** | Days after capture, set by the provider | The provider | Money, by bank transfer to the merchant | Provider: "this is yours to withdraw" |
| 6. **Dispute window** | About 120 days, sometimes longer | The cardholder, through the issuer | Possibly the money, backward | None: until it closes, nothing is final |

<!-- illustration-placeholder
{
  "id": "01-six-step-timeline",
  "status": "pending",
  "asset": "assets/images/01-journey-of-a-payment/01-six-step-timeline.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of the six steps in the timeline section",
  "visual_goal": "Show the six steps on one line and make visible that a message moves first, a record second and money only at settlement and payout, with the dispute window stretching far beyond.",
  "prompt": "Create a structural timeline diagram running left to right. Six round stations on one horizontal line, evenly spaced for the first five and with a long stretch before the sixth. Station labels in order: \"Authorization\", \"Capture\", \"Clearing\", \"Settlement\", \"Payout\", \"Dispute window\". Above the line, three colored brackets group the stations: a blue bracket over the first two labeled \"message\", a teal bracket over the third labeled \"record\", and an orange bracket over the fourth and fifth labeled \"money\". Under the first station a small envelope icon; under the third a sheet-of-paper icon; under the fourth and fifth a euro coin icon. Below the line, a time ruler with three marks labeled \"seconds\", \"days\" and \"120 days\", the last mark under the sixth station. A dashed arrow labeled \"taken back\" curves from the sixth station back to the fifth. The stretch between the fifth and sixth stations is drawn as a long dotted line to show waiting. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Timeline with six stations from Authorization to Dispute window, grouped under message, record and money, with a time ruler from seconds to 120 days.",
  "caption": "Six steps on one line: a message moves at authorization, a record at clearing, and money only at settlement and payout, while the dispute window stays open for about 120 days."
}
-->

Steps one and two move no money. In Visa's description the acquirer passes the transaction to Visa, "which in turn sends the transaction data to the issuer to check the account holder’s account balance or credit line for authorization". An approving issuer commonly places a **hold**, reserving the amount on the cardholder's account: Mila's €120 was still hers at 19:43 and no longer hers to spend. **Capture** is the merchant's instruction to collect on that promise. Many integrators never see it, because it is automatic unless they ask otherwise; Adyen's documentation (n.d., accessed November 2026) says "By default, payments are captured automatically without a delay, immediately after authorization of the payment request." The promise also expires: Visa's rules (edition of 24 October 2026) give an acquirer at most 10 calendar days to process an ordinary online payment that the customer started. [[payment-authorization]] takes this step apart.

Step three is a record and step four is the first movement of money. In Visa's rules a **presentment** is "A Clearing Record that an Acquirer presents to an Issuer through Interchange", the final statement of what was sold and for how much (in the rulebook "Interchange" means this exchange of records, not the fee). **Clearing** is the network's processing of those records. Money then moves, but not payment by payment. Visa defines **settlement** as "The reporting and funds transfer of Settlement Amounts owed by one Member to another, or to Visa, as a result of Clearing", and a settlement amount as "The daily net amounts expressed in a Member’s Settlement Currency resulting from Clearing": one net figure per member per day. Nor does the acquirer receive the whole sale. The issuer, in Visa's words, "effectively pays the acquirer an amount equal to the value of the transaction, minus the interchange reimbursement fee (IRF)", the fee the merchant's side pays the cardholder's bank, usually just called **interchange** ([[payment-economics]]). [[clearing-and-settlement]] covers both steps.

Step five belongs to the provider, and here the providers' own words can mislead, because both use "settlement" for their release of funds to the merchant. Stripe's payout documentation (n.d., accessed November 2026) gives timing as T+X days, where "Stripe uses “T” to refer to the transaction time, which indicates the time of the original payment confirmation or capture", whereas "Some payment processors might start “T” from their internal settlement time, meaning when the funds land in their bank accounts." Adyen's platform documentation (n.d., accessed November 2026) speaks of a "sales day settlement model", and its page on the default payout model says "the funds you get do not depend on the settlement timelines of the schemes and payment methods used by your shoppers". The terms of that model (last updated 17 June 2024) add that Adyen initiates the payout "irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner". So **"settled" names one event at the network and another at the provider**, and a payout date does not tell you when the banks settled. [[payouts-and-money-movement]] covers the mechanics.

Step six runs backward and outlasts the other five. A cardholder who rejects a charge complains to the issuer, which can force the payment back through the network: a **dispute**. Visa's rules give the issuer "120 calendar days from the Transaction Processing Date" for most kinds of dispute. Adyen's documentation (n.d., accessed November 2026) states the general rule for both large networks, "In general, a cardholder has a maximum of 120 calendar days from the transaction date to dispute a transaction", and adds that "In some cases for Visa and Mastercard, the cardholder has a maximum of 540 calendar days". Mastercard's own rules could not be read, so its figure is reported through Adyen. A studio can be paid on day two and lose the money on day ninety. [[refunds-reversals-and-disputes]] covers how.

Read as requirements on your own payment record, the timeline makes each step a separate fact with its own source and its own lateness. The table is my reading, and its delays are assumptions.

| Step | What your record should hold | How you learn it | How late it can be *(assumption)* | If the message is lost |
| --- | --- | --- | --- | --- |
| Authorization | Outcome, the provider's reference, when the approval expires | API response, confirmed by webhook | Seconds to minutes | The outcome is unknown, not failed ([[idempotency-and-retries]]) |
| Capture | Amount claimed, reference | API response or webhook | Seconds to hours | Ask the provider before claiming again |
| Clearing and settlement | Usually nothing per payment; the fees once known | The provider's report | One to three days | The report is still there tomorrow ([[payment-reconciliation-and-reporting]]) |
| Payout | Payout id, net amount, the payments in it | Webhook and report | Days | Reconcile against the bank statement |
| Dispute | Dispute id, reason, amount, response deadline | Webhook | Any day for about 120 days | The deadline passes unseen |

## When the Model Bends: Three-Party Networks, Bank Transfers and Wallets

All of this describes a four-party card payment. Other ways to pay remove parties or steps, and the first variant removes only one boundary. In a **three-party network** one company is both issuer and acquirer. EU law has the cleanest definition: Regulation (EU) 2015/751 distinguishes "‘three party payment card schemes’ (cardholder — acquiring and issuing scheme — merchant) and ‘four party payment card schemes’ (cardholder — issuing bank — acquiring bank — merchant)". **(Evidence age: 11 years; the regulation is still in force.)** Stripe's documentation (n.d., accessed November 2026) gives the usual example: a card network "might be an intermediary in front of an issuing bank as with Visa or Mastercard, or a standalone entity as with American Express". The boundary is not fixed, since under the same regulation a three-party scheme that licenses others to issue or acquire "is considered to be a four party payment card scheme".

The second variant has no card network at all. In a **bank-transfer scheme** the payer's bank and the merchant's bank deal with each other under the scheme's rules, and the money is either pushed by the payer or pulled by the merchant under a standing permission called a **mandate**. Two methods Larkfield depends on show how finality differs from a card's. With iDEAL, in which Dutch payers approve a transfer in their own bank's app, there is no step six: Stripe's page (n.d., accessed November 2026) says "Customers can’t dispute iDEAL | Wero payments with their bank." With SEPA Direct Debit, the pull payment of the Single Euro Payments Area, the payer's right is stronger than a cardholder's: the payer can dispute "without providing a reason for up to 8 weeks after the debit" (Stripe, n.d.), and Adyen's page (n.d.) adds "You cannot defend SEPA chargebacks." These two methods carried 35% of Larkfield's online volume in 2026 (direct debit 21%, iDEAL 14%) against 52% for cards. Assuming the card timeline for them is the failure pattern A Card by Any Other Name ([[local-payment-methods]]).

The third variant, the **wallet**, is two different things under one name. Stripe's documentation (n.d., accessed November 2026) separates them: a wallet pays with either "A saved payment credential (a tokenized card or bank account stored in the wallet)" or "A stored wallet balance (funds held in an account with the wallet provider)". The first kind changes how the card is presented, not the parties. Adyen's Apple Pay page (n.d., accessed November 2026) says it "uses network tokenization", in which the card network issues a stand-in for the card number ([[network-tokens]]), and that it "supports liability shift for American Express, Discover, JCB, Mastercard, and Visa cards" (a liability shift moves the loss from a fraud dispute from the merchant's side to the issuer once the payer has been authenticated). The second kind is a network of its own with its own dispute process. Mila's payment is of the first kind. Her phone's wallet checked her fingerprint, so she met no **3-D Secure** challenge (3-D Secure is the card networks' protocol for letting the issuer check the payer; [[three-d-secure-and-sca]]), and everything after that was a Visa debit payment with all six steps.

## Where a Provider Can Stand in the Chain

So far "the provider" has stood loosely beside the acquirer. It can stand in one of three places, which differ in who holds the network membership, who holds the merchant's money before payout, and how many parties stand between merchant and network. The table is industry usage, apart from the quoted rule (section 5.3.1.2, edition of 24 October 2026); the last column is my judgement.

| Position | Who is the network member | Who holds the merchant's funds before payout | Between merchant and network | When it fits |
| --- | --- | --- | --- | --- |
| **Gateway only** | An acquirer the merchant contracts separately | That acquirer | Gateway, acquirer | A large merchant that negotiates acquiring itself or wants several acquirers ([[payment-routing-and-orchestration]]) |
| **Payment facilitator under an acquiring bank** | The bank, often called the *sponsor bank*; under Visa's rules it is "liable for all acts, omissions, and other adverse conditions caused by the Payment Facilitator and its Sponsored Merchants" | Usually the facilitator, once the bank has passed the settlement on | Facilitator, bank | Many small merchants, where the provider has no acquiring license |
| **The provider is the acquirer** | The provider | The provider | Provider only | Where the provider holds license and membership: one counterparty |

<!-- illustration-placeholder
{
  "id": "01-provider-positions",
  "status": "pending",
  "asset": "assets/images/01-journey-of-a-payment/01-provider-positions.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of the three positions a provider can take",
  "visual_goal": "Show the three places a provider can stand between a merchant and the card network, and that the number of parties in between differs.",
  "prompt": "Create a structural explainer diagram with three horizontal lanes stacked top to bottom, each running from a small shop front on the left labeled \"Merchant\" to a round hub on the right labeled \"Network\". Top lane, labeled \"Gateway\" at its left margin: between the shop and the hub sit a thin pipe-shaped box and then a bank building; the bank building carries a small membership badge. Middle lane, labeled \"Facilitator\" at its left margin: between the shop and the hub sit an office-shaped box and then a bank building; the bank building carries the membership badge and a small tag labeled \"Sponsor bank\". Bottom lane, labeled \"Acquirer\" at its left margin: between the shop and the hub sits one combined office-and-bank building carrying the membership badge. In each lane a small euro coin icon sits on the element that holds the merchant's funds: on the bank in the top lane, on the office-shaped box in the middle lane, on the combined building in the bottom lane. Arrows in each lane run left to right and are labeled \"payment\" once in the top lane only. A small legend shows the badge with the label \"member\" and the coin with the label \"holds funds\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Three lanes from merchant to network showing a gateway in front of a separate acquirer, a facilitator under a sponsor bank, and a provider that is itself the acquirer.",
  "caption": "Three places a provider can stand: a gateway in front of a separate acquirer, a payment facilitator under an acquiring bank, or the acquirer itself."
}
-->

One distinction prevents a common misreading: **a direct connection to a network is not the same as being the acquirer of record**, the member under whose name a payment enters the network. Stripe announced in April 2020 that it "now processes card transactions through direct integrations with all six major card networks in North America, Latin America, Europe and Asia Pacific". **(Evidence age: 6 years; the current system may differ.)** That is about who exchanges messages with the network. Stripe's acquirer disclosure (n.d., accessed November 2026) is about who holds the membership, and for the United States it reads "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers", followed by five banks and one Stripe entity. Both can be true: a company can send messages straight to a network while a bank holds the membership and the liability.

A platform adds one more layer on top of whichever position its provider takes. Larkfield is one, and it has chosen not to be a party to the money. The studio is the seller, the studio's funds sit in the provider's regulated balance until payout, and Larkfield takes a fee from each payment. It is not the **merchant of record**, the party that is legally the seller ([[merchant-of-record]]), and it holds no license to hold funds; [[platform-payment-models]] covers the alternatives. The section reduces to the question I would put to any provider before any other: **which legal entity is the acquirer for these sellers, in this country?**

## Stripe and Adyen: Where They Differ

Stripe and Adyen each occupy more than one of these positions. The table sets out what each has published; the last column is my inference, not something either company states. Two terms in it need a gloss: an electronic money institution is a non-bank licensed to issue electronic money and provide payment services, and a credit institution is a bank. EEA is the European Economic Area.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Regulated form in Europe | Stripe Technology Europe Limited is "authorised as an electronic money institution by the Central Bank of Ireland" (Stripe's legal page for the entity, last updated April 2019; evidence age 7 years, and the entity is named in the current disclosure) | Adyen N.V. is "authorised as a credit Institution under the supervision of Dutch Central Bank", which it calls a "banking license" (Adyen's licenses page for Europe, the Middle East and Africa, n.d., accessed November 2026) | Both are regulated in their own right; a bank license permits more ([[licences-and-safeguarding]]) |
| Acquirer of record for a card payment in the EEA | "Payment Method Acquirer is Stripe Technology Europe, Ltd." (Stripe's acquirer disclosure, n.d., accessed November 2026) | An acquiring entity named for some markets only; no list per country. The license "includes the ability to provide cross-border acquiring, payment and banking services in all EEA countries" (licenses page), and the documentation lists 14 countries and regions with an Adyen acquiring connection, the European Union among them, where a payment goes "through one of our acquiring entities, for example Adyen Singapore" (Supported payout currencies page, n.d., accessed November 2026) | Inference: both acquire in their own name in the EEA; only Stripe names the entity |
| Role in the United States | "Stripe, LLC is a Payment Facilitator" of Cross River Bank, Deutsche Bank Trust Company Americas, Fifth Third Bank, Pathward, PNC Bank and Stripe MALPB, its own entity (same disclosure) | Under the heading "USA Acquiring": "Adyen N.V. San Francisco Branch is a federal Branch of Adyen, N.V., licensed by the Office of the Comptroller of the Currency and the Federal Reserve Board of Governors" (Adyen's United States licenses page, n.d., accessed November 2026). Acquirer of record per payment: Not public | Inference: in the US Stripe stands mainly as a facilitator; Adyen holds its own bank branch license |
| Where its own acquiring stops | Published per country: a payment facilitator of named acquirers in the US, Canada, Japan and Thailand, and in Mexico alongside its own acquiring; a "Payment Aggregator" of a bank in India; an "Independent Sales Organization" of an acquirer in the United Arab Emirates (same disclosure) | "Of processed volumes, 84% were full-stack volumes"; the risk section of the same report places concentration risk "primarily at banking partners in locations where there are no own direct acquiring licenses" (Annual Report 2025, March 2026). Which locations: Not public | Neither is its own acquirer everywhere; Stripe shows the boundary and Adyen reports its size |
| What the payout clock counts from | "T" is "the time of the original payment confirmation or capture"; the Netherlands is listed at 7 calendar days initially and 3 business days by default (Stripe's payouts documentation, n.d., accessed November 2026) | The sales day; typically 2 business days where at least 80% of transactions are in a listed currency such as EUR and acquired in its region (Adyen's Sales day payout documentation, n.d., accessed November 2026) | No material difference: both clocks are the provider's, not the network's |

On Stripe, read the acquirer for each country you sell in from the disclosure page and record it with the date, because the list of banks changes; in the United States it tells you that a bank's terms apply alongside Stripe's. On Adyen, put the same question to your account team for each market, in writing, since its license pages name an acquiring entity for some markets only (Japan and Singapore, for example) and no public page says where a banking partner stands behind it. On both, do not read a payout date as the date the network settled, and translate each provider's words (Stripe's "card network" is Adyen's "card scheme", and Adyen's customer is a "shopper") into your own before they reach your payment record ([[payment-state-machines]]).

The public record stops in three places. Neither company lists its network memberships by network and country, or publishes how much volume runs through each acquirer. Stripe's acquirer terms call its EEA entity and its US limited-purpose bank "a member of the Networks", and an article on Adyen's site (3 July 2026) claims "principal membership of Visa and Mastercard in major markets"; neither lists networks and countries. On volume, Stripe names its US banks without shares, and Adyen's report neither defines "full-stack" where it gives the 84% nor names who acquires the rest (reading the term as volume Adyen also acquires is my inference, as is reading its sentence on banking partners as a statement about acquiring). And only Adyen's terms say that a payout does not wait for the network's money; Stripe's payout page, as read in November 2026, does not say either way, and its services terms (last modified 28 September 2026) say only that a network's failure to settle to Stripe can delay a payout. Neither publishes an end-to-end description of its role by region; the table is assembled from legal pages.

> **INFERENCE, NOT DOCUMENTED:** Stripe's per-country list probably exists because, where Stripe is a payment facilitator, the bank is a party to the merchant's contract and has to be named; the disclosure links each bank's own acquirer terms. Adyen, as the regulated counterparty itself in most markets, has no such party to disclose. Neither company gives this reason.

## In Practice at Larkfield: Mila's €120, Party by Party

Now Femke's answer to Ines, beginning with the cast: every role in the model has a name in Mila's payment. One cell is my inference. Adyen's license covers acquiring across the European Economic Area and its documentation lists the European Union as one of its acquiring connections, but Adyen publishes no complete list of acquiring entities per country, so that Adyen N.V. is the acquirer of record here is the likely reading, not a documented fact.

| Role | In Mila's payment | What it does here |
| --- | --- | --- |
| Cardholder | Mila Janssen | Approves the purchase with her fingerprint |
| Wallet | Her phone's wallet | Presents her card as a token; holds no money |
| Issuer | Mila's Dutch bank | Decides the approval, reserves €120, later pays it away |
| Network | Visa | Carries the request and the clearing record; nets the banks' positions |
| Acquirer and provider | Adyen *(acquirer of record inferred)* | Submits the payment, receives the settlement, holds Studio Noord's balance, pays out |
| Merchant | Studio Noord | The seller; receives €117.47 |
| Platform | Larkfield | Sent the API call; keeps a fee of €2.53; never holds the €120 |

In time order the €120 is promised, claimed, moved between the banks, paid out and left open to a dispute. Three numbers in the table need a note. The fee is Larkfield's 1.9% + €0.25, which is €2.53 and leaves the studio €117.47. The interchange that Mila's bank keeps is capped by Regulation (EU) 2015/751 at 0.2% for a consumer debit card, so at most €0.24 here ([[payment-economics]]). And 7 July is my arithmetic, 120 calendar days from 9 March; Visa's rule counts from the processing date, which may be a day later. The payout on the second business day matches the delay Adyen documents for euro payments acquired in the region.

| When | Step | Who acts | Where the €120 is |
| --- | --- | --- | --- |
| Tue 9 March, 19:42 | Authorization | Mila's bank approves; no 3-D Secure challenge | In Mila's account, reserved |
| Tue 9 March, 19:42 | Capture, automatic | Adyen, for Studio Noord | Unchanged; a claim now exists |
| Tue night or Wed *(assumption)* | Clearing | Adyen presents the record through Visa | Unchanged |
| Wed 10 or Thu 11 March *(assumption)* | Settlement | Visa nets the banks' positions; Mila's bank pays | With the acquirer, less interchange |
| Thu 11 March | Payout | Adyen pays Studio Noord | €117.47 in the studio's bank account; €2.53 in Larkfield's balance at Adyen |
| Until about 7 July 2027 | Dispute window | Mila, through her bank | The studio's, and still reversible |

So at noon on Wednesday the honest answer to Ines has four parts. Mila's bank approved the payment, and that approval is a promise, not a transfer. No money has reached the studio, and whether the banks have settled yet is something neither Larkfield nor Ines can see. The payout arrives tomorrow. And the payment stays reversible until early July, because Mila can dispute it through her bank. `paid` was true, and it was not final. Decision K2 of Keel, Larkfield's 2027 program, states the rule behind that answer: the provider's record is the truth, and the webhook is the doorbell.

Had Studio Noord been on Stripe, the cast and the six steps would be the same and two cells would change. The acquirer would be documented and not inferred, because Stripe's disclosure names Stripe Technology Europe, Ltd. for the European Economic Area. And the payout would follow Stripe's clock, which counts from capture: its country table lists the Netherlands at 7 calendar days for an account's first payout and 3 business days after that. By my arithmetic the €117.47 becomes available on Friday 12 March at the earliest, subject to the payout schedule the platform has set. The issuer still decides, Visa still nets, and Mila can still dispute until July.

## When It Goes Wrong: Each Step Fails in Its Own Way

Each step has its own owner and its own clock, so each fails in its own way. Larkfield's incidents ([[meet-larkfield]]) fall along the timeline, one per hand-off between two parties.

| Step | What goes wrong | Who knows first | Larkfield's case | Chapter |
| --- | --- | --- | --- | --- |
| Authorization | The request times out, and the issuer may have approved | The issuer, then the provider | The Double Charge, 1 November 2026: a retry under a new key charged 1,840 members twice; €71,300 refunded | [[payment-authorization]], [[idempotency-and-retries]] |
| Settlement and after | The provider's balance and your own books drift apart | The provider | The Unexplained €0.4 Million, year-end 2025: €412,000 traced to refunds after payout, chargeback fees and a rounding rule | [[clearing-and-settlement]], [[payment-reconciliation-and-reporting]] |
| Payout | The receiving bank returns it | The receiving bank | The Payout That Bounced, June 2026: 412 payouts worth €386,000 | [[payouts-and-money-movement]] |
| Dispute | It arrives after the money was paid out | The issuer | Bram de Wit's €120 pass of 2 February 2027, charged back on 24 February with a €15.00 fee | [[refunds-reversals-and-disputes]] |
| The report of any step | The message that should tell you never arrives | Nobody on your side | The Silent Webhook, 14 September 2026: 9 hours of failed events, 3,200 memberships shown as unpaid | [[payment-webhooks-and-events]] |

These failures share one cause: a system treated one party's report as another party's fact. An absent answer was read as a decline, a status as money, a payout as the end. This book calls that pattern the Phantom Payment ([[where-payment-systems-go-wrong]]), and the rule against it is short. **Treat a missing or surprising answer as unknown; ask the party that owns the fact, through the provider's own record; and keep asking until every payment has reached a state that party has confirmed.** At Larkfield this is K2, with a job that sweeps everything still pending. How to ask differs by provider; [[payment-state-machines]] and [[payment-webhooks-and-events]] take it from there.

## What to Take Away

**Established.**

- The four-party structure and the network's three services (authorization, clearing, settlement) are the networks' own description, in Visa's and Mastercard's annual reports filed in 2026.
- The network holds no customer money and decides no approval; the issuer decides.
- Settlement is daily and net between members (Visa's rules, October 2026), and the network's guarantee stops at the acquirer (Mastercard, 2026).
- The cardholder's right to dispute runs for about 120 days for most card disputes (Visa's rules; Adyen's documentation for both networks), so it outlasts the payout.

**Depends on context.**

- *Which entity is the acquirer* depends on provider and country: Stripe is the acquirer in the EEA and a payment facilitator of banks in the United States.
- *When the payout arrives* depends on the provider's clock and your account's settings, not on when the network settled.
- *Whether a payment can be taken back, and for how long* depends on the method: never for iDEAL, eight weeks without a reason for SEPA Direct Debit, about 120 days for a card.

**The author's synthesis.**

- The parties, the timeline and the provider's position are one fact seen three ways: every step of a payment has an owner, and the provider owns only one, the payout. Every status it returns is therefore someone else's promise, relayed. I would store it that way: which promise, from whom, open until when.
- Ask for the acquirer of record before comparing providers on anything else. It tells you whose rules apply and whose balance sheet stands behind the seller's money.

## Questions to Ask

1. For each country we sell in, which legal entity is the acquirer of record for card payments, and where is that written down?
2. Is the provider there the acquirer, a payment facilitator under a bank, or a gateway? If a facilitator, which bank, and whose terms bind the seller?
3. For each status we store, whose decision does it report: the issuer's, the provider's or our own?
4. What does our record call a payment that is approved but not yet paid out, and one that is paid out but can still be disputed?
5. What does the provider's payout clock count from, and does a payout wait for the network's settlement?
6. Who holds the seller's money between settlement and payout, and under which license?
7. For each payment method we accept, which of the six steps exist, and can the payer take the money back?
8. When no answer comes back from the provider, what does our code assume?

At 19:43 on 9 March the screen said the payment had succeeded and the €120 had not moved. You can now say what had happened by then (Mila's bank had promised), what had not (clearing, settlement, payout) and when the last open promise closes (early July). The first of those steps is the only one the customer ever sees, and the one most often mistaken for the payment itself. [[payment-authorization]] opens it up: what the message carries, how the issuer decides, how long the promise lasts, and what you know when no answer comes back at all.

## Sources and Evidence

*Company, product and investor sources*

- [Form 10-K for fiscal 2026](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm), Visa Inc., 2026-11-05 — the four-party model, the walkthrough of one payment, "not a financial institution", the settlement indemnity.
- [Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm), Mastercard Incorporated, 2026-02-11 — the four participants, the three services, the limit of the settlement guarantee.
- [Acquirer Disclosure & Acquirer Terms](https://stripe.com/legal/acquirer-disclosure), Stripe, n.d., accessed 2026-11 — the acquirer or Stripe's stated role per country (volatile: the list of banks changes).
- [Stripe Technology Europe, Limited: legal information](https://stripe.com/legal/stel), Stripe, 2019-04-05 — the e-money authorization by the Central Bank of Ireland (evidence age: 7 years; the entity is named in the current acquirer disclosure).
- [Stripe Services Agreement: Services Terms](https://stripe.com/legal/ssa-service-terms), Stripe, last modified 2026-09-28 — the definition of a Payment Method Acquirer; the definition of Payout Delay (a financial provider's failure to settle to Stripe).
- [STEL Acquirer Terms](https://stripe.com/legal/stel-financial-terms), Stripe, n.d., accessed 2026-11 — Stripe Technology Europe as "a member of the Networks"; the US limited-purpose bank's terms on the acquirer disclosure use the same words.
- [Credit card processing fees: what determines your rate and why the lowest isn't always the cheapest](https://www.adyen.com/knowledge-hub/credit-card-processing-fees), Adyen, 2026-07-03 — "principal membership of Visa and Mastercard in major markets" (vendor claim, no list).
- [Licenses and disclosures: Japan](https://www.adyen.com/licenses/japan) and [Singapore](https://www.adyen.com/licenses/singapore), Adyen, n.d., accessed 2026-11 — Adyen Japan KK's registration as merchant acquirer; Adyen Singapore's license for merchant acquisition.
- [Major updates to Stripe's payments platform increase revenue and reliability for businesses](https://stripe.com/newsroom/news/direct-platform), Stripe newsroom, 2020-04-23 — direct integrations with six card networks (evidence age: 6 years).
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods), Stripe documentation, n.d., accessed 2026-11 — what a `succeeded` status does and does not mean.
- [Payouts](https://docs.stripe.com/payouts), Stripe documentation, n.d., accessed 2026-11 — what "T" counts from; settlement timing per country (volatile).
- [Wallets](https://docs.stripe.com/payments/wallets), Stripe documentation, n.d., accessed 2026-11 — the two kinds of wallet.
- [iDEAL | Wero payments](https://docs.stripe.com/payments/ideal), Stripe documentation, n.d., accessed 2026-11 — no disputes on iDEAL.
- [SEPA Direct Debit payments](https://docs.stripe.com/payments/sepa-debit), Stripe documentation, n.d., accessed 2026-11 — the eight-week dispute right.
- [How disputes work](https://docs.stripe.com/disputes/how-disputes-work), Stripe documentation, n.d., accessed 2026-11 — the glossary definition of a card network.
- [Licenses and disclosures: EMEA](https://www.adyen.com/licenses/emea), Adyen, n.d., accessed 2026-11 — the credit-institution license and what it covers.
- [Licenses and disclosures: United States](https://www.adyen.com/licenses/united-states), Adyen, n.d., accessed 2026-11 — the federal branch.
- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., 2026-03-05 — 84% full-stack volume; banking partners where Adyen has no acquiring license.
- [What's an acquiring bank and why you need one](https://www.adyen.com/knowledge-hub/acquiring-bank), Adyen knowledge hub, n.d., accessed 2026-11 — acquirers need a regulator's and a scheme's license.
- [Capture](https://docs.adyen.com/online-payments/capture), Adyen documentation, n.d., accessed 2026-11 — automatic capture by default.
- [Sales day payout](https://docs.adyen.com/account/sales-day-payout), Adyen documentation, n.d., accessed 2026-11 — payout independent of scheme settlement; typical payout delays (volatile).
- [Supported payout currencies](https://docs.adyen.com/account/supported-currencies), Adyen documentation, n.d., accessed 2026-11 — the countries and regions with an Adyen acquiring connection; "one of our acquiring entities".
- [Sales Day Payout Terms of Service](https://www.adyen.com/legal/sales-day-payout-terms-of-service), Adyen, 2024-06-17 — payout initiated whether or not Adyen has received the funds.
- [Settle funds](https://docs.adyen.com/platforms/settle-funds), Adyen for Platforms documentation, n.d., accessed 2026-11 — the "sales day settlement model".
- [Dispute timeframes](https://docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes), Adyen documentation, n.d., accessed 2026-11 — 120 and 540 calendar days, for Visa and Mastercard.
- [SEPA Direct Debit](https://docs.adyen.com/payment-methods/sepa-direct-debit), Adyen documentation, n.d., accessed 2026-11 — SEPA chargebacks cannot be defended.
- [Apple Pay](https://docs.adyen.com/payment-methods/apple-pay), Adyen documentation, n.d., accessed 2026-11 — network tokenization and liability shift by card brand.

*Standards, regulation and official documentation*

- [Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf), Visa, 2026-10-24 — definitions of acquirer, acquirer processor, payment facilitator, presentment, settlement and settlement amount; section 5.3.1.2 on payment facilitators; Table 5-11 on processing timeframes; the 120-day dispute time limit.
- [Regulation (EU) 2015/751 on interchange fees for card-based payment transactions](http://publications.europa.eu/resource/celex/32015R0751), Official Journal of the European Union, 2015-05-19 — three-party and four-party schemes (recital 28, Article 2(18)); the 0.2% cap on consumer debit interchange (Article 3) (evidence age: 11 years; in force).
- Mastercard's rule documents could not be read (HTTP 403 in November 2026); Mastercard's dispute window is cited through Adyen's documentation above.

*Research and practitioner sources*

- [[payments-fundamentals]] in RECONCILED — the same parties and flows as an enterprise finance architect sees them.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
