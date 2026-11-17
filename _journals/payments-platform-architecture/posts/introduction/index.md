---
title: "Introduction: Why Payment Infrastructure Is Hard"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What does this book argue, who is it for, and how should its evidence about Stripe and Adyen be read? It argues that the answer a payment API returns in two seconds is the first of several promises kept over days, and it states about the two companies only what a dated public source says."
permalink: introduction
timetoread: 15 min read
---

> **KEY POINTS:**
>
> * **“Payment successful” is the first of several promises.** The answer a payment API returns in two seconds is kept over days by parties that cannot see each other and can be reversed for months. Each component of payment infrastructure exists to close that gap without losing or duplicating money.
> * **The book is for engineers and architects new to payments.** Ten parts go from how money moves to how Stripe and Adyen chose to build, with a route from the decision on your desk to the chapter that answers it.
> * **A sentence about a provider is worth its source and its date.** The book states about Stripe and Adyen only what a dated public source says and marks the rest as inference, illustration, assumption or “Not public”, which reports a search and proves no absence.

<br>
At 19:42 on Tuesday 9 March 2027, Mila Janssen buys a ten-class pass for €120 in a yoga studio's app and sees “Payment successful” two seconds later. **At that moment no money has moved.** Her bank has made a promise, and the studio will be paid on Thursday, by systems that never saw her tap the button. Mila, the studio and the software platform between them, Larkfield, are fictional; the book follows this one payment to its last page.

To a developer, that payment is one API call that returned success. On the provider's side the answer is **the first of several promises, kept over days by parties that cannot see each other and reversible for months**. This book argues that each component of payment infrastructure exists to close the gap between that answer and the truth without losing or duplicating money. It is written for engineers and architects who are new to payments.

This page says who the book is for, states the argument and names sixteen ways systems fail when it is ignored, and lays out the ten parts. It then explains how to read the evidence about Stripe and Adyen and why those two were chosen, introduces Larkfield and Mila's payment, routes you from a decision to a chapter, and says what the book leaves to others and draws on. Its own evidence is one fictional payment and a few dated facts about what the two companies publish.

## Who This Book Is For

The book is for **engineers and architects who are new to payments** and have just been asked to do one of four things.

- **Integrate a payment provider** and get beyond the quickstart.
- **Run or repair an integration** someone else built, often after an incident.
- **Build a platform** whose customers are the sellers.
- **Choose or compare providers.**

The book assumes you know what an API, a database, a queue, a webhook and a retry are, and no payments vocabulary. Every payments, banking and billing term is explained where a chapter first uses it, such as **issuer**, the cardholder's bank, and **acquirer**, the licensed institution that takes a merchant's card payments into the card networks. The [[glossary]] collects the terms with the word each provider uses. I write as an architect who builds on payment providers; where I give a judgement I say “I” and give my reasons.

## The Argument: A Promise That Takes Days to Keep

Behind Mila's two seconds stand five promises, made in turn by her bank, the studio, the acquirer, the network and the provider. [[journey-of-a-payment]] walks through them.

| Step | Who promises what | For Mila's €120 |
| --- | --- | --- |
| Authorization | Her bank, the issuer: “I will honor a claim for this amount if it arrives in time” | 19:42 on Tuesday |
| Capture | The studio, the merchant: “I claim the money” | Automatic, at once |
| Clearing | The acquirer: “this is the final amount and data” | The same or the next day *(industry practice)* |
| Settlement | The network: its members pay each other | The next business day or later *(industry practice)* |
| Payout | The provider: “this is yours to withdraw” | Thursday 11 March |
| Dispute window | None: until it closes, nothing is final | Until about 7 July 2027 |

<!-- illustration-placeholder
{
  "id": "introduction-two-seconds-and-the-slow-truth",
  "status": "pending",
  "asset": "assets/images/introduction/introduction-two-seconds-and-the-slow-truth.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of five promises in the section The Argument",
  "visual_goal": "Show how small the instant answer is beside the time the payment really takes: an approval after two seconds, a payout two days later, and a dispute window that stays open for about 120 days.",
  "prompt": "Create a conceptual timeline illustration. A long horizontal line runs from left to right across the image. At the far left, a smartphone shows one green check mark, with a small stopwatch beside it labeled \"2 seconds\". Close to it on the line, a small bank building with a speech bubble containing a handshake icon, labeled \"Promise\". Further right, at about one fifth of the line, a yoga studio shopfront receiving a euro coin from a blue office block, labeled \"Day 2: paid\". The rest of the line, most of its length, is drawn as a dashed orange stretch ending at a calendar page at the far right labeled \"Day 120\". Above the dashed stretch, a curved orange arrow labeled \"Dispute\" runs from the calendar page back toward the studio, carrying a coin labeled \"€120\". Under the whole line, a thin teal bracket labeled \"Slow truth\" spans from the bank building to the calendar page. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A timeline with a two-second approval at the far left, a payout on day 2, and a long dashed stretch to day 120 from which a dispute arrow carries €120 back.",
  "caption": "The answer arrives in two seconds; the studio is paid on Thursday, and the €120 can be taken back for about 120 days."
}
-->

It follows that **the API's answer is not the outcome**. A payment is done when it is settled and every record of it agrees. Every major component in this book exists to close the gap between the instant answer and that slow truth without losing or duplicating money: payment state machines, idempotency keys (identifiers that let a provider recognize a repeated request), ledgers, reconciliation (matching one record against another that someone else wrote), tokens that stand in for card numbers, risk scoring and the accounts a platform gives its sellers.

The opposite view is that payments are a solved commodity behind an API, so that only integration breadth and scale are hard. A team that gives that view up asks three questions of every design: **which promise is this, who made it, and which record will prove it was kept?**

The gap has two sides, the regulated path the money takes and the instant answer a developer sees. **Stripe and Adyen differ mainly in which side they built first**: Adyen the regulated money path (license, acquiring, one platform it runs on servers it manages itself), Stripe the developer's abstraction over it (API, product suite, named acquirers). By 2026 each is building toward the other's side, and the public record shows the order of construction more clearly than the reasons for it. Adyen's Annual Report 2025 says it chose to “develop and operate the essential layers of the financial stack ourselves”, and reports 84% of that year's volume as “full-stack”; on 1 July 2026 Adyen closed two acquisitions. Stripe's acquirer disclosure (n.d., accessed November 2026) names a Stripe company as the acquirer in the European Economic Area and lists a bank of Stripe's own among its US acquirers. So the claim describes a sequence, not two territories; [[part-10]] tests it.

## Sixteen Ways the Gap Shows

When a system records one of those promises as the truth, it fails in ways that recur often enough to be named. [[where-payment-systems-go-wrong]] unpacks sixteen patterns; here are their names, in four families.

- **Money truth**, a record of money that nothing outside the system has confirmed: **The Double Charge**, **The Phantom Payment**, **The Orphaned Refund**, **The Black-Box Balance** and **The Stranded Payout**.
- **Integration**, an untested assumption about the provider's interface: **The Trusted Doorbell**, **The Version Cliff** and **A Card by Any Other Name**.
- **Trust**, a control handed to the provider and then not watched: **The Vault Hostage**, **The Card in the Log**, **The Open Till** and **The Frozen Seller**.
- **Platform and scale**, a dependency, a peak or a regulated role nobody rehearsed or named: **The Single Rail**, **The First of the Month**, **The Borrowed Blueprint** and **The Accidental Bank**.

The patterns chain: a failure is usually noticed at a money-truth pattern and started at one of the other eleven. On 1 November 2026 Larkfield's monthly renewal run, a First of the Month, met a timeout, and its job sent each request again under a new idempotency key. 1,840 members were charged twice: a Double Charge. Every chapter names the patterns it works on, so the list is also an index.

## How the Book Is Organized

The book has four preface pages, ten parts and four reference pages.

| Section | The question it answers | Pages |
| --- | --- | --- |
| **Preface** | What does the book argue, and how do payment systems fail? | This page, [[how-payments-got-complicated]], [[where-payment-systems-go-wrong]], [[meet-larkfield]] |
| **[[part-1]]** | What happens between “Payment successful” and money the merchant can keep? | 1–5: the journey, authorization, clearing and settlement, refunds and disputes, fees |
| **[[part-2]]** | What decides whether a payment gets to “yes”? | 6–11: acquiring, local payment methods, the payment state machine, optimization, routing, terminals |
| **[[part-3]]** | How does a provider know where the money is and whose it is? | 12–16: ledgers, balances, payouts, reconciliation, licenses |
| **[[part-4]]** | How can an API make a slow payment look like one call? | 17–21: object models, idempotency, versioning, webhooks, the developer platform |
| **[[part-5]]** | What do the controls over card data, fraud, authentication and compliance move, and to whom? | 22–26: tokens and vaults, network tokens, risk, 3-D Secure, compliance |
| **[[part-6]]** | What turns single payments into recurring, taxed, reportable revenue? | 27–32: billing engines, metering, invoicing and retries, tax, revenue recognition, merchant of record |
| **[[part-7]]** | When a platform stands between payer and seller, who carries the loss? | 33–36: platform models, onboarding, splits and payouts, embedded finance |
| **[[part-8]]** | What gives way under failure, load and change, so that the record of money does not? | 37–41: reliability, data stores, regions, peak load, safe change |
| **[[part-9]]** | What does one payment look like end to end? | 42–45: a card payment, a failed renewal, a platform payment, a dispute |
| **[[part-10]]** | What do Stripe's and Adyen's records show about why they built differently? | 46–50: two cases, the bets compared, three contrast cases, what is moving |
| **Reference** | Where is a capability, a template, a term or a source? | [[domain-coverage]], [[toolkit]], [[glossary]], [[bibliography]] |

The parts are in prerequisite order. Part I, the one part not to skip, gives the parties and the timeline. Approval (II) needs both; the ledger (III) records them; the API (IV) exposes the ledger's balances and the payment's states; the controls of Part V sit in the API's path. Billing (VI) follows because collecting a failed renewal uses stored cards. Platforms (VII) and scale (VIII) widen the view to many sellers and to the system under load. The journeys and the two companies come last: put first, the cases would ask you to judge two architectures before you knew the problem they solve.

<!-- illustration-placeholder
{
  "id": "introduction-map-of-the-book",
  "status": "pending",
  "asset": "assets/images/introduction/introduction-map-of-the-book.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that explains the order of the parts in the section How the Book Is Organized",
  "visual_goal": "Show the shape of the book as one path: a preface, eight mechanism parts in order, then whole payments and the two companies, and a reference shelf at the end.",
  "prompt": "Create a structural map drawn as a winding path from the lower left to the upper right. At the start of the path, a small open book labeled \"Preface\". Along the path, ten round numbered stations with the numbers \"1\" to \"10\" inside them. Stations 1 to 8 are blue and teal and sit inside one long, lightly shaded band labeled \"Mechanisms\"; a small icon stands beside each: a euro coin moving between two bank buildings at 1, a green check mark at 2, an open ledger book at 3, a pair of angle brackets at 4, a shield at 5, a repeating calendar at 6, three connected shopfronts at 7, a server rack with a gauge at 8. Station 9 is green and sits in a second band labeled \"Whole payments\", with an icon of one long arrow passing through four small dots. Station 10 is orange and sits in a third band labeled \"Two companies\", with an icon of two different buildings side by side marked \"A\" and \"B\". At the end of the path, a small bookshelf labeled \"Reference\". One thin blue arrow labeled \"read in order\" follows the path from the open book to the bookshelf. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A path from a preface through ten numbered stations to a reference shelf; stations 1 to 8 are grouped as mechanisms, station 9 as whole payments and station 10 as two companies.",
  "caption": "The book as one path: a preface, eight parts that each explain a group of mechanisms, a part that follows whole payments, a part on the two companies (A is Stripe, B is Adyen), and the reference pages."
}
-->

Inside Parts I to VIII every chapter has the same anatomy. It opens on a scene at Larkfield and a short paragraph headed **“Where we are in the payment's journey”**, which places it on the path of Mila's pass. It states the problem before the mechanism, then the designs and their trade-offs. A section titled **“Stripe and Adyen: Where They Differ”** compares the two companies, and the failure cases follow. It ends with “What to Take Away”, questions for a design review, and its sources.

Parts IX and X teach no new mechanism. Part IX follows four Larkfield payments through every party and system, on both providers. Part X reads each company's dated record ([[case-stripe]], [[case-adyen]]), compares their bets one by one ([[stripe-and-adyen-bets-compared]]), sets PayPal, Checkout.com and Block beside them ([[payment-contrast-cases]]) and closes the book on what is moving in 2026: agents that pay, stablecoins and instant payments ([[payments-what-is-moving]]).

## How to Read the Evidence

With two real companies as anchors, a wrong or unsourced sentence about how one of them works is the worst defect a page can have. So every statement is one of **six kinds**, and the wording tells you which.

| Kind of statement | What it is | How to recognize it |
| --- | --- | --- |
| **Documented fact** | A company's public statement, a network rule, a standard, a law or a number | Attributed in the sentence with its year (“Stripe's 2017 engineering post…”) and listed under Sources and Evidence |
| **Industry practice** | What payment companies and integrators commonly do | “Commonly”, “a typical design is”; no invented percentages |
| **Inference** | How a system is plausibly built | For a real company, a block marked **INFERENCE, NOT DOCUMENTED** |
| **Recommendation** | My judgement | First person, with reasons and the conditions under which it fails |
| **Illustration** | An example at Larkfield | Labeled fictional in each chapter |
| **Assumption** | An illustrative fee, volume or latency | “Assume…” or *(assumption)*; not a benchmark |

A documented fact about a company carries its **year**, because the public record is old in places. Stripe's best-known engineering posts on idempotency, rate limiting and API versioning are from 2017, and Adyen's account of its accounting system is from 2021. A source older than about three years is flagged where it is used: **(Evidence age: 9 years; the current system may differ.)** Such a post shows what the company said it had built that year. Where current documentation confirms it, the chapter says so: Stripe's API reference (n.d., accessed November 2026) still describes the 2017 post's idempotency key, and says keys can be removed once at least 24 hours old. That confirms the interface, not how Stripe stores keys today.

Where no source speaks, the book writes **“Not public”**. The words mean that I found no first-party statement in the provider's documentation, help center, site or engineering posts as of November 2026. They do not mean the provider lacks the mechanism. “Not public” is an answer to write down and a question for the provider.

When the finished chapters were checked again against their sources, **the most common error corrected was an over-confident “Not public”**. The first searches were too narrow, and the providers' documentation indexes do not list every page. One draft said Adyen had published nothing on load testing; its documentation (n.d., accessed November 2026) says, “We periodically load test this system with merchants who hold transactions and then release the transactions in bulk.” Another said nothing was public about how Stripe schedules subscription renewals; a Stripe engineering post of May 2024 describes “a scheduling service that looks for database records meeting certain criteria”. So read an absence in this book as **a dated search result, not a proof**.

Stripe and Adyen are the anchors because both publish enough to compare, not because either is the right answer for every business. They publish unevenly. Adyen is listed and files audited accounts: its Annual Report 2025 gives €1,394.3 billion of processed volume and €2,364.2 million of net revenue. Stripe is private: its annual letter for 2025 reports “$1.9 trillion in total volume”, a measure it does not define, and no letter gives the company's revenue. The two volume figures may count different things, so the book does not rank them. Some gaps are shared: as of November 2026 neither has published how its webhook sender is built, a design for its card vault, or the topology and timing of a failover between its data centers or regions.

Each chapter's **“Where They Differ” table** shows that record one aspect at a time. A Stripe or Adyen cell holds a documented fact from the chapter or the words “Not public”; the last column is my reading. Two rows from [[idempotency-and-retries]] (documentation accessed November 2026):

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Retention window | API v1: at least 24 hours; API v2: 30 days | 7 to 14 days after first submission | A next-day retry is inside Adyen's window and outside Stripe v1's guarantee |
| Key store unavailable | Not public | 503 with code 703; pause, or resend without the key | Adyen leaves the choice between availability and protection to the integrator |

The same separation applies to a chapter's conclusions. **“What to Take Away”** has three tiers: **Established**, what the field agrees on, with the evidence or standard behind it; **Depends on context**, a recommendation that holds under a stated condition, which you check against your own business; and **The author's synthesis**, my position, to weigh and to disagree with.

Two things are never evidence about a provider. One is Larkfield: what happens to it is illustration, and a provider behavior shown in a Larkfield scene is also documented and cited in that chapter. The other is my position: **this book is independent of Stripe and Adyen** and uses no internal material or inside knowledge of any company. Neither company reviewed it.

## Larkfield and Mila's Class Pass

**Larkfield is fictional**: a Rotterdam software platform for independent fitness and wellness studios. Members pay the studios through it; in 2026 its 6,200 studios took €1.12 billion in 31.4 million payments. A studio is on Stripe (44% of volume) or on Adyen (56%), which lets every chapter compare the two on the same kind of payment. The studio is the seller, and Larkfield never holds members' money. It is a composite, not a disguised firm.

Between the 2025 year-end close and November 2026 Larkfield had **eight incidents**, cited by name in the chapters, such as the Double Charge and the Silent Webhook. Each was decided on Larkfield's own side of the provider's API. In January 2027 Femke de Graaf, an engineer new to payments, becomes Head of Payments Engineering; she is your stand-in. Her program, **Keel**, answers the incidents with eight decisions, K1 to K8, that change Larkfield's keys, records, pacing and ownership and keep both providers. [[meet-larkfield]] gives all of it.

Mila's class pass is the recurring payment, and its facts never change. She pays €120.00 to Studio Noord, which is on Adyen, at 19:42 on Tuesday 9 March 2027. Larkfield's fee is €2.53, the studio receives €117.47 on Thursday 11 March, and the payment can be disputed until about 7 July. Each chapter says which step of this payment it covers, and the journeys of [[part-9]] follow it whole.

## Start With the Decision in Front of You

If a decision or an incident is already on your desk, find its row, read the chapter under **Start with**, and follow **Then**.

| If you need to decide or repair… | Start with | Then |
| --- | --- | --- |
| A job that charges customers timed out, and you do not know who was charged | [[idempotency-and-retries]] | [[payment-webhooks-and-events]], [[payment-state-machines]] |
| Your books do not match the provider's balance | [[payment-ledgers]] | [[payment-reconciliation-and-reporting]], [[balances-and-funds-flows]] |
| Approval rates are low, or differ between providers | [[authorization-optimization]] | [[acquiring-and-network-connectivity]], [[network-tokens]] |
| Whether to add a second provider or a routing layer | [[payment-routing-and-orchestration]] | [[tokenization-vaulting-and-pci]], [[payment-reliability-and-availability]] |
| Renewals fail, or the first of the month overloads | [[invoicing-collections-and-dunning]] | [[payment-peak-load]], [[journey-failed-renewal]] |
| Who pays when a seller's refund or chargeback exceeds its balance | [[platform-payment-models]] | [[splits-balances-and-platform-payouts]], [[journey-platform-payment]] |
| Sellers' payouts stopped after a verification change | [[payment-compliance-and-regulation]] | [[platform-onboarding-and-verification]] |
| A dispute arrived months after the sale | [[refunds-reversals-and-disputes]] | [[three-d-secure-and-sca]], [[journey-dispute]] |
| Stripe, Adyen or both | [[stripe-and-adyen-bets-compared]] | [[case-stripe]], [[case-adyen]], [[payment-economics]] |

One row starts somewhere you might not expect. After a timeout, the reliability chapter looks like the place to go, but it is about keeping the payment path up. Your question is how to make “charge this card” safe to send twice when the outcome is unknown. That is idempotency; webhooks and the state machine then give the true state.

You can also read by role, and for the decision itself the [[toolkit]] collects sixteen working cards, such as the idempotency key card and the reconciliation card.

- **Integrating one provider:** Part I, then [[payment-state-machines]], Part IV and [[journey-card-payment]].
- **Running subscriptions:** Parts IV and VI, then [[journey-failed-renewal]].
- **Building a platform:** Parts III and VII, then [[journey-platform-payment]].
- **Choosing or comparing providers:** Part I, the “Where They Differ” section of each chapter that matters to you, then Part X.

## What the Book Leaves to Others

Four neighboring subjects have a book of their own on this site, and four things this book does not attempt.

- **The finance side.** Posting payouts to the books, clearing accounts and the accounting system are the subject of *RECONCILED*, starting with [[payments-fundamentals]] and [[payments-to-ledger]].
- **The merchant's order system.** Payments as a shop's checkout and order record see them are in *ORDERED*: [[commerce-payments]].
- **Running a marketplace.** Fraud and regulation from the operator's side are in *LISTED*: [[fraud-prevention]], [[marketplace-regulation]].
- **How AI agents are built.** How agents are kept within bounds is in *Architecting Agentic Systems*: [[side-effects-and-external-actions]].
- **Not attempted:** a product guide or integration tutorial for Stripe or Adyen; inferred internals of any real company, such as service names or schemas; the systems of issuers and card networks beyond what a builder on the acquiring side needs; and cryptocurrency trading, lending products and consumer banking apps.

## What the Book Draws On

The book uses public, dated sources and no others: the two companies' documentation, engineering posts, letters, reports and legal pages, card-network rules, standards and laws. Secondary sources fill gaps and are named as such. I also keep a domain model of payments and revenue infrastructure as a planning map. It describes no company, and [[domain-coverage]] maps it to the chapters. The [[bibliography]] lists every source with its date and type.

This is a living journal, which I revise as I learn more through [my work](https://obren.io). Its **research cut-off is 17 November 2026**; the scenes are set in 2027. Check the source before you rely on a time-sensitive fact. Every page has a “View spec” link to the specification it was written against, with its open questions. I developed the book through AI-mediated authoring: I set the concept, structure and arguments; AI tools supported research, drafting, cross-checks and editing; I reviewed and decided. Its content and errors are my responsibility.

## Where to Go Next

The argument, the evidence rules and the fictional platform apply one discipline three times. Of a payment, ask which promise it is and which record proves it was kept. Of a sentence about a provider, ask which source says so and how old it is. Of an example, ask whether it is evidence or illustration. The book asks of itself what it asks you to build: **do not record a promise as the truth**.

You can now read Mila's screen. “Payment successful” was her bank's promise; the studio was paid on Thursday; and the payment stays open until about 7 July. Carry the argument's three questions into every chapter. If a decision is waiting, use the routing table; otherwise [[how-payments-got-complicated]] walks from a coin on a counter to today's layers and shows where those promises and parties came from.

## Sources and Evidence

Facts about Stripe and Adyen on this page are repeated from the chapters linked beside them, where each is discussed with its context; the sources below were read again on 17 November 2026.

*Company, product and investor sources*

- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., signed 2026-03-05 — the stated choice to operate the layers of the financial stack itself, the 84% full-stack share, processed volume and net revenue (audited; read in the PDF this page offers for download).
- [Adyen closes Talon.One and Orb acquisitions, announces leadership updates](https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates), Adyen, 2026-07-01 — the closing of two acquisitions.
- [Stripe annual letter 2025](https://stripe.com/annual-updates/2025), Patrick and John Collison, 2026-02-24 — “$1.9 trillion in total volume”, with no definition of the measure; no revenue figure for the company (read in the PDF this page links).
- [Acquirer Disclosure & Acquirer Terms](https://stripe.com/legal/acquirer-disclosure), Stripe, n.d., accessed 2026-11 — Stripe Technology Europe, Ltd. as acquirer in the European Economic Area; Stripe MALPB among the US acquirers.
- [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency), Brandur Leach, Stripe, 2017-02-22 — the date of Stripe's idempotency post and the key it introduces; it gives no retention period (evidence age: 9 years).
- [Scaling your API with rate limiters](https://stripe.com/blog/rate-limiters), Paul Tarjan, Stripe, 2017-03-30 — the date of Stripe's rate-limiting post (evidence age: 9 years).
- [APIs as infrastructure: future-proofing Stripe with versioning](https://stripe.com/blog/api-versioning), Brandur Leach, Stripe, 2017-08-05 — the date of Stripe's versioning post (evidence age: 9 years).
- [Design to Duty: The Accounting and Reporting Systems at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2), Willem Pino, Adyen, 2021-08-23 — the date of Adyen's account of its accounting system (evidence age: 5 years).
- [Test clocks: How we made it easier to test Stripe Billing integrations](https://stripe.dev/blog/test-clocks-how-we-made-it-easier-to-test-stripe-billing-integrations), Ji Huang, Stripe, 2024-05-09 — the scheduling service behind subscription renewals.

*Standards, regulation and official documentation*

- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), Stripe API reference, n.d., accessed 2026-11 — the idempotency key; keys removable once at least 24 hours old (API v1).
- [API v2 overview](https://docs.stripe.com/api-v2-overview), Stripe documentation, n.d., accessed 2026-11 — the 30-day window for API v2 in the sample comparison row.
- [API idempotency](https://docs.adyen.com/development-resources/api-idempotency), Adyen documentation, n.d., accessed 2026-11 — keys valid 7 to 14 days; HTTP 503 with error code 703 when the key store is unavailable, and the two choices it gives.
- [Peak season readiness](https://docs.adyen.com/industries/peak-season), Adyen documentation, n.d., accessed 2026-11 — periodic load tests with merchants.
- [Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf), Visa, 2026-10-24 — the 120-day dispute time limit, as cited in [[journey-of-a-payment]].

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
