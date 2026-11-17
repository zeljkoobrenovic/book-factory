# Research brief: Billing, usage metering, invoicing, tax, revenue recognition and merchant of record

> **Correction, 17 November 2026 (from chapter verification; see `consistency-issues.md` ruling 21).** Section 1.10 misdates Adyen's knowledge-hub article on Orb: the page displays 29 September 2026 (title "Why billing and payments belong together"), not 19 October. The sentence "We completed our acquisition of Orb on 1 July." is not on that page and must not be quoted; the closing date of 1 July 2026 rests on Adyen's closing press release.

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 27 (subscriptions and billing engines), 28 (usage metering and rating), 29 (invoicing, collections and dunning), 30 (tax), 31 (revenue recognition), 32 (merchant of record), and parts of 43 (billing in the journey of a failed renewal) and 50 (consolidation: the billing and loyalty acquisitions). The anchors are Stripe and Adyen. Orb (owned by Adyen since 1 July 2026), Metronome (owned by Stripe since 14 January 2026), Paddle, Chargebee, Recurly, Lago, Avalara and Vertex appear only where a contrast clarifies a design choice.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated documentation and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (the kind is named), not from a primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including every statement about how Stripe, Adyen, Orb or any other company works internally beyond what it has published.

**Evidence age matters.** Stripe and Orb documentation pages are living documents without publication dates: what they say today may differ next quarter, and several pages quoted here describe features introduced in 2025 and 2026 (flexible billing mode, trial offers, Managed Payments, Metronome as the recommended usage product). Adyen documentation pages carry a `last_modified` field, which is recorded where it looks meaningful; two Adyen pages show the fetch date itself as `last_modified` and are treated as undated. Sources published before November 2023 are flagged **(evidence age: N years)**.

**Research limitation.**

- **Stripe's annual letters** (`stripe.com/annual-updates/2025`, `/2024`) render their body in the browser; neither `curl` nor the fetch tool returned the letter text. The Revenue suite figure below comes from Stripe's newsroom release about the 2025 letter, not from the letter itself. The 2024 letter's wording on the suite was not verified.
- **Stripe newsroom pages** were served in Dutch to this session's network location for some URLs; quotes are taken only from the English (`/en-nl/`) variants. The full English wording of the Metronome completion release was returned as a summary, so only short quoted fragments are reproduced.
- **No Stripe engineering publication describes the subscription scheduler** (the component that wakes up subscriptions and generates invoices). Three Stripe posts touch Billing internals (2017, January 2025, September 2025); none covers the scheduler. This is a real gap, not a search failure: searched `stripe.com/blog/engineering`, `stripe.dev/blog` and the open web.
- **Managed Payments launch date**: no Stripe newsroom release was found. The API changelog entry (22 April 2026) and the pricing page are verified; the "announced at Sessions 2025, private preview" history is secondary.
- **Metronome signing date** (December 2025) is from trade press; the Stripe release fetched covers completion only.
- **Apple and Google as merchant of record**: Apple's developer pages fetched state the commission but not the legal seller role; the Paid Applications Agreement (Schedule 2) is behind a login. Google's tax page states where Google determines, charges and remits tax but does not use the phrase "merchant of record" in the passages read.
- **Adyen tax engine**: nothing found (searches recorded in 4.4). **Adyen/Orb integration status**: only forward-looking statements found.
- Not fetched or blocked: the Council's ViDA press release (HTTP 403; the Commission's ViDA page is used instead), the Belgian FPS Finance e-invoicing page (403), Zuora documentation (404 on two URLs), Chargebee's Adyen gateway page (404), FASB's ASC 606 summary page (not fetched; the IFRS Foundation page confirms the joint issue).
- Involuntary-churn statistics: only Stripe's own marketing figures were verified. No independent, primary, dated measurement of involuntary churn was found; treat every such number as a vendor claim.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: prices, preview status, API version names, default billing mode, rate limits, country counts, Metronome and Orb integration status, ViDA national implementations, Lemon Squeezy's shutdown.

---

## PART 1: Subscriptions and the billing engine (chapter 27)

### 1.1 Stripe Billing's object model

Stripe documents a billing object model in which a small set of objects carry distinct responsibilities:

| Object | What the documentation says it is | Source |
| --- | --- | --- |
| Product | What the business sells; holds the tax code and attached Features | products and prices guide |
| Price | How much and how often; recurring interval, currency, licensed or metered | products and prices guide |
| Customer (or customer-configured `Account`, Accounts v2) | Who is billed; stores default payment method, addresses, tax IDs | subscriptions overview; test docs |
| Subscription | "the subscribed customer, product, and price, and the `status` reflecting the subscription's current lifecycle state" | subscriptions overview |
| SubscriptionSchedule | A sequence of up to 10 `phases` that change the subscription over time | subscription schedules |
| Invoice | "statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized" | invoices |
| InvoiceItem | A pending or attached line; proration items are invoice items | prorations |
| InvoicePayment | "the mapping between payment objects, such as Payment Intent, and Invoices" | API reference |
| PaymentIntent | The payment attempt created for an invoice | subscriptions overview |
| Feature / Active Entitlement | "An entitlement represents a customer's access to a feature" | entitlements |
| Meter / Meter Event / Credit Grant | Usage aggregation, usage events, prepaid or promotional credit (PART 2) | usage docs |

- "When you create a subscription, Stripe automatically generates invoices, attempts payment collection, and manages the subscription status throughout its lifecycle"; and "Unlike one-time payments, subscriptions require storing customer and payment method information for future billing cycles. Stripe handles the payment retry logic, dunning, and status transitions" [VERIFIED: https://docs.stripe.com/billing/subscriptions/overview.md, n.d., accessed 2026-11].
- "When you create a subscription that requires an immediate payment, Stripe also creates an Invoice and a PaymentIntent. The subscription's initial status is `incomplete`, then becomes `active` after the customer pays the first invoice" [VERIFIED: same page].
- InvoicePayment: "Invoice Payments represent payments made against invoices ... This resource and its endpoints allows you to easily track if a payment is associated with a specific invoice and monitor the allocation details of the payments"; it emits `invoice_payment.paid` [VERIFIED: https://docs.stripe.com/api/invoice-payment.md, n.d., accessed 2026-11]. An invoice can carry several payments: "When you finalize an invoice, Stripe creates a default payment that you can use to pay the invoice in full", and "To support partial payments, you can create and attach a separate PaymentIntent to your invoice" [VERIFIED: https://docs.stripe.com/invoicing/partial-payments.md, n.d., accessed 2026-11].
- Entitlements: "When a customer purchases or subscribes to a product with an attached feature, Stripe creates and manages an Active Entitlement for that customer and feature"; the integration listens to the Active Entitlement Summary webhook or lists active entitlements; "Existing subscriptions will create active entitlements for any product feature changes at the start of the next billing period" [VERIFIED: https://docs.stripe.com/billing/entitlements.md?dashboard-or-api=api, n.d., accessed 2026-11].
- The chain Subscription → Invoice → PaymentIntent is the documented seam between the billing engine and the payment engine: billing decides *what is owed and when*, the invoice records it, and the PaymentIntent is an ordinary payment that can fail, require authentication or settle late [ASSUMPTION/JUDGEMENT].

### 1.2 Subscription statuses and lifecycle

Stripe documents eight subscription statuses [VERIFIED: https://docs.stripe.com/billing/subscriptions/overview.md, n.d., accessed 2026-11]:

| Status | Documented meaning (condensed, wording kept close) |
| --- | --- |
| `incomplete` | "The customer must make a successful payment within 23 hours to activate the subscription" |
| `incomplete_expired` | "The initial payment on the subscription failed and the customer didn't make a successful payment within 23 hours of subscription creation." Terminal; exists "so you can track customers that failed to activate" |
| `trialing` | In a trial; "transitions automatically to `active` when a customer makes the first payment" |
| `active` | "in good standing"; but "`active` doesn't necessarily indicate that all outstanding invoices associated with the subscription have been paid" |
| `past_due` | "Payment on the latest finalized invoice either failed or wasn't attempted ... The subscription continues to create invoices" |
| `unpaid` | Set only if the account's settings choose it; "continues to generate invoices but doesn't attempt payment"; invoices "remain in `draft` status" |
| `canceled` | "This is a terminal state that can't be updated"; cancellation sets `auto_advance=false` on unpaid invoices |
| `paused` | Trial ended without a payment method (with `missing_payment_method=pause`), or the subscription was paused through the Pause endpoint; "Invoices are no longer created" |

- The 23-hour rule: for `charge_automatically`, "Your customer has 23 hours to pay ... This 23-hour window accommodates customers who pay while on-session"; after it, the subscription becomes `incomplete_expired` and the invoice `void` [VERIFIED: same page].
- The period does not move when payment is late: "Stripe sets the subscription's `current_period_start` when it creates the initial invoice. Completing payment later doesn't shift the start of the initial billing period" [VERIFIED: same page].
- What happens after retries is configuration, not a fixed machine: after retries end, "your failed payment settings in the Dashboard determine whether the subscription remains `past_due` or changes to `unpaid` or `canceled`"; a newer option pauses the subscription [VERIFIED: same page; https://docs.stripe.com/billing/revenue-recovery/smart-retries.md, n.d., accessed 2026-11].
- "Status resolution" is itself configurable: the status can be derived from "the most recent non-voided invoice or from all applicable outstanding invoices" [VERIFIED: subscriptions overview, same].
- Cancellation "disables creating new invoices and stops automatic collection of all outstanding invoices"; to resubscribe "you need to collect new payment information from them and create a new subscription" [VERIFIED: same page].

### 1.3 Billing cycle anchors, month ends and time zones

- "The billing cycle anchor is the reference point that aligns future billing period dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The default value is either the subscription creation date or the trial end date" [VERIFIED: https://docs.stripe.com/billing/subscriptions/billing-cycle.md, n.d., accessed 2026-11].
- Month ends: "A monthly subscription with a billing cycle anchor date of January 31 bills the last day of the month closest to the anchor date, so February 28 (or February 29 in a leap year), then March 31, April 30, and so on" [VERIFIED: same page].
- Time: "Billing cycle anchors are UNIX timestamps in seconds from the current epoch" and "The billing cycle anchor uses Coordinated Universal Time (UTC). For example, if you create a subscription using `billing_cycle_anchor_config` at 5 pm EST without specifying the hour, the time is recorded in the system as 10 pm UTC" [VERIFIED: same page]. A "first of the month" renewal therefore happens at a UTC instant, which is a different local date for customers east and west of the business [ASSUMPTION/JUDGEMENT].
- `billing_cycle_anchor_config` (day of month, month, hour, minute, second) is recommended for monthly and yearly subscriptions "because it automatically factors in short months and leap years"; setting `day_of_month` to 31 renews "on the last day of that month" in shorter months [VERIFIED: same page].

### 1.4 Proration

- Definition and worked example: prorations are "where the customer is charged a percentage of a subscription's cost to reflect partial use"; upgrading from 10 USD to 20 USD halfway through the period yields a 5 USD credit for unused time and a 10 USD debit for the remaining time, net 5 USD [VERIFIED: https://docs.stripe.com/billing/subscriptions/prorations.md, n.d., accessed 2026-11].
- "Negative prorations aren't automatically refunded and positive prorations aren't immediately billed, although you can do both manually" [VERIFIED: same page]. The `proration_behavior` values seen in the documentation are `create_prorations`, `always_invoice` and `none` [VERIFIED: same page].
- "By default, Stripe calculates prorations down to the second"; day, hour, week or month granularity is available through "proration customizations" [VERIFIED: same page]. Contrast: Chargebee makes this a site-level choice between "day-based and millisecond-based" proration modes [VERIFIED: https://www.chargebee.com/docs/billing/2.0/subscriptions/proration, n.d., accessed 2026-11].
- Classification is by operation, not by period length: "Stripe bases this classification on the operation that creates the item, not only on the length of the service period" (the page tabulates eleven scenarios) [VERIFIED: prorations page].

### 1.5 Billing modes: classic and flexible ⚠

Flexible billing mode exists and is now the default for new API versions.

- "You can configure each subscription to use one of two billing modes: **Flexible** (Recommended) ... **Classic**: Uses the existing Stripe subscription behavior. This setting is maintained for backward compatibility with older integrations." And: "You can't migrate a subscription from flexible billing mode to classic billing mode" [VERIFIED: https://docs.stripe.com/billing/subscriptions/billing-mode.md, n.d., accessed 2026-11].
- Defaults by API version: "For API version `2025-09-30.clover` and later, the default is `flexible`. For earlier versions, the default is `classic`"; flexible requires `2025-06-30.basil` or later [VERIFIED: same page]. ⚠
- The documented differences are a catalogue of billing-engine edge cases [VERIFIED: https://docs.stripe.com/billing/subscriptions/billing-mode/compare.md, n.d., accessed 2026-11]:

| Behaviour | Classic | Flexible |
| --- | --- | --- |
| Credit proration | Calculated from "the subscription item's current price, tax, quantity, and the last discounts used" | Uses "the original debited amount instead of current subscription values"; one credit per original debit |
| Discounts in proration | Distributed "evenly across all subscription items" | Applied "proportionally to each subscription item" |
| Usage after a mid-period price change | Bills only usage reported since the change, at the current price | Bills "all usage in the current period at the price effective at the time it's reported" |
| Billing cycle anchor on interval change or free-to-paid | Automatically reset to now | Preserved unless explicitly reset |
| Zero-amount usage lines at creation | Generated | Suppressed; an empty invoice is not generated |

- Features that require flexible mode: pausing a subscription ("Subscriptions must use flexible billing mode"), trial offers, and "mixed intervals on the same subscription" [VERIFIED: https://docs.stripe.com/billing/subscriptions/pause.md; https://docs.stripe.com/billing/subscriptions/trials.md; billing-mode page, n.d., accessed 2026-11].
- The existence of two modes is public evidence that billing semantics cannot be changed in place: once invoices have been issued under one proration rule, the engine must keep honouring it for those subscriptions, so new semantics ship as an opt-in mode with one-way migration [ASSUMPTION/JUDGEMENT].

### 1.6 Trials, pausing and schedules

- Trials: a subscription with a trial starts `trialing`; Stripe's test guide expects it to generate "a zero-value trial invoice" [VERIFIED: https://docs.stripe.com/billing/testing/test-clocks.md, n.d., accessed 2026-11]. A newer **Trial Offer API** manages "both free and paid introductory periods", requires API version `2026-09-30.endive` or later and flexible billing mode, and cannot be combined with the legacy `trial_end` parameter; several surfaces (Pricing tables, Payment Links) do not support it yet [VERIFIED: https://docs.stripe.com/billing/subscriptions/trials.md, n.d., accessed 2026-11]. ⚠
- Two different "pauses" [VERIFIED: https://docs.stripe.com/billing/subscriptions/pause-payment.md and https://docs.stripe.com/billing/subscriptions/pause.md, n.d., accessed 2026-11]:

| | Pause payment collection | Pause subscription |
| --- | --- | --- |
| Status | "remains `active`" | "changes to `paused`" |
| Invoices | "continue to generate, but Stripe doesn't collect payment"; behaviour `keep_as_draft`, `mark_uncollectible` or `void` | "Stripe pauses invoice generation until you resume" |
| Access | "Your customer retains access" | Service delivery suspended; entitlement webhooks fire |
| Period | Unchanged | "`current_period_end` updates to the time you paused" |

- Subscription schedules: "Phases must be sequential, meaning only one phase can be active at a given time. You can have up to 10 phases"; phase transitions "happen automatically after the `end_date` on a phase is reached" [VERIFIED: https://docs.stripe.com/billing/subscriptions/subscription-schedules.md, n.d., accessed 2026-11].

### 1.7 The scheduler, as far as it is public

What Stripe documents is the externally visible timing of the scheduler, not its design:

- At renewal Stripe "Creates an invoice", "Leaves the invoice in a `draft` status for about an hour", then "Attempts to finalize and pay the invoice with the default payment method" [VERIFIED: https://docs.stripe.com/billing/invoices/subscription.md, n.d., accessed 2026-11].
- The hour is tied to webhook delivery: "We wait 1 hour after receiving a successful response to the `invoice.created` event from all listening webhooks before attempting payment. If we don't receive a successful response within 72 hours, we attempt to finalize and send the invoice" [VERIFIED: https://docs.stripe.com/invoicing/integration/workflow-transitions.md, n.d., accessed 2026-11]. A failing webhook endpoint therefore delays collection for every renewal: "During that time, we won't attempt to charge the customer unless we receive a successful response" [VERIFIED: same page].
- The first invoice of a `charge_automatically` subscription is finalized immediately: "there isn't a one hour period in which you can update the initial invoice before finalization" [VERIFIED: invoices/subscription page].
- **Test clocks** exist because the scheduler is time-driven: "Use test clocks to advance simulated time in a sandbox and see how your subscriptions and invoices change"; the Dashboard simulation advances "up to two subscription intervals at a time" and may be disabled for a customer with "more than three subscriptions" or "more than 25 quotes, invoices, or other related objects" [VERIFIED: https://docs.stripe.com/billing/testing/test-clocks.md, n.d., accessed 2026-11].
- How the scheduler is built (queueing, sharding, how many renewals it processes on the first of a month, how it avoids double invoicing) is **not public** [ASSUMPTION/JUDGEMENT]. Statements about wake-up jobs, idempotent invoice creation keyed on subscription and period, and spreading load across the hour are reference-architecture inference, not Stripe facts [ASSUMPTION/JUDGEMENT].

### 1.8 Stripe engineering publications on Billing

| Post | Date | What it establishes |
| --- | --- | --- |
| "Online migrations at scale" (Jacqueline Xu) | 2017-02-02 | "Stripe has hundreds of millions of Subscriptions objects"; four-step dual-write migration; verification with GitHub's Scientist; Hadoop/MapReduce via Scalding |
| "How we built it: Usage-based billing" (Taras Mitran, Karan Dhabalia) | 2025-01-28 | Meter pipeline design (see 2.2) |
| "How we built it: Real-time analytics for Stripe Billing" (Reed Trevelyan) | 2025-09-16 | Flink keeps "a highly compressed version of subscription history as a 'state'"; Apache Pinot serves queries; data latency "as low as 15 minutes" against a previous 24-hour batch lag; Dashboard queries under 300 ms |

[VERIFIED: https://stripe.com/blog/online-migrations, published 2017-02-02 **(evidence age: 9 years; the object count is a floor, and the tooling named may have been replaced)**; https://stripe.com/blog/how-we-built-it-usage-based-billing, published 2025-01-28; https://stripe.dev/blog/how-we-built-it-real-time-analytics-for-stripe-billing, published 2025-09-16]

- Product-level scale claims from Stripe's Billing page: "350,000+ companies use Stripe Billing", "99.999% uptime in 2025"; a footnote states "Metronome, a Stripe product, is not included in Stripe Billing" [VERIFIED: https://stripe.com/billing, n.d., accessed 2026-11]. These are vendor marketing figures with no published method [ASSUMPTION/JUDGEMENT]. ⚠
- Revenue suite: Stripe's release on its 2025 annual letter says the Revenue suite (described in the release as comprising Stripe Billing, Invoicing, Tax and more) "is on track to hit an annual run rate of $1 billion this year"; the same release says "Businesses running on Stripe generated $1.9 trillion in total volume", up 34% from 2024 [VERIFIED: https://stripe.com/newsroom/news/stripe-2025-update, published 2026-02-24]. The parenthetical composition is paraphrased from the release; the letter itself was not readable (see limitation).
- Billing is separable from Stripe's payment processing: in October 2024 Stripe announced "the ability to manage subscriptions with Stripe while processing transactions with other payments providers", rolling out by region with a private preview for bringing one's own processor [VERIFIED: https://stripe.com/blog/our-biggest-ever-upgrades-to-stripe-billing, published 2024-10-29]. Current availability was not re-checked ⚠.

### 1.9 Adyen before Orb: tokens and recurring flags, no billing engine

- Adyen's documented recurring model is a payment model. A stored token is charged with a declared processing model: "**One-click** (`CardOnFile`): A shopper-initiated payment where a returning shopper uses their stored payment details", "**Subscription** (`Subscription`): A payment where you initiate a subscription payment to bill the shopper at regular intervals", "**Unscheduled Card-on-File** (`UnscheduledCardOnFile`): An automatic top-up payment or other contracts where you initiate payments at non-fixed intervals"; merchant-initiated payments set `shopperInteraction` to **ContAuth** [VERIFIED: https://docs.adyen.com/online-payments/tokenization/make-token-payments.md, last modified 2023-07-28 **(evidence age: 3 years; the tokenization overview fetched today describes the same three types)**].
- The tokenization overview says the merchant initiates the charge: "**Subscriptions**: recurring transactions you initiate at regular intervals for a product or a service"; tokens are stored against a merchant-supplied shopper reference in "the Adyen Vault"; "Tokenize is an Adyen Uplift module" [VERIFIED: https://docs.adyen.com/online-payments/tokenization.md, n.d., accessed 2026-11].
- Nothing in the Adyen documentation read describes a plan, price, subscription object, billing cycle, proration or invoice. The schedule, the amount and the retry decision sit with the merchant or with a billing system connected to Adyen [ASSUMPTION/JUDGEMENT, from the absence of such objects in the pages fetched]. Supporting evidence from the other side: Orb documents that it "integrates with payment gateways like Adyen and Stripe for payment processing", and that "For gateways without a synced default (such as Adyen), you designate the customer's default payment method yourself" [VERIFIED: https://docs.withorb.com/invoicing/payments.md, n.d., accessed 2026-11]; Lago states it "keeps metering and pricing independent from payment processing. Connect Stripe, Adyen, GoCardless, or another provider" [VERIFIED: https://github.com/getlago/lago (README), n.d., accessed 2026-11].
- Adyen's own framing after the acquisition: seat-based subscription billing "is well-served today, including by partners we work with closely" (partners not named) [VERIFIED: https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb, published 2026-10-19].

### 1.10 Adyen's acquisition of Orb ⚠

| Fact | Evidence |
| --- | --- |
| Announced 11 June 2026: "Adyen to acquire Orb to unify billing and payments infrastructure for enterprise merchants" | [VERIFIED: https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj, published 2026-06-11] |
| "The total consideration for the transaction is $335 million", financed "entirely from available cash resources" | [VERIFIED: same] |
| Orb: San Francisco, founded 2021, $44 million total funding; named customers Vercel, Glean, Replit, Supabase | [VERIFIED: same] |
| Closed: "Both transactions officially closed on July 1, 2026" (Orb and Talon.One) | [VERIFIED: https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates, published 2026-07-01] |
| "We completed our acquisition of Orb on 1 July." | [VERIFIED: https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb, published 2026-10-19] |
| Operating model: "To ensure product velocity, Adyen is adopting an incubator model, preserving Orb's operational continuity during the first phase of the acquisition and continuing to support multi-PSP environments" | [VERIFIED: announcement release, 2026-06-11] |
| Stated end state: "Beyond this first phase, the strategic intent is convergence: a single infrastructure experience for merchants across billing and payments" | [VERIFIED: same] |
| Integration status in October 2026: "You'll soon see how we bring this unified Adyen and Orb experience to life across our platform" | [VERIFIED: knowledge-hub article, 2026-10-19] |
| H1 2026 results: "Closed the Talon.One and Orb acquisitions subsequent to H1, embedding omnichannel loyalty" and "flexible usage-based billing onto our platform" | [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13] |

- **Integration status, stated carefully**: as of 17 November 2026 the public record shows a closed acquisition, a stand-alone Orb product that still supports Stripe and other gateways, an intent to converge, and no published Adyen documentation of an integrated billing product. No `docs.adyen.com` page on Orb or billing was found [ASSUMPTION/JUDGEMENT on the absence; the four quoted statements are verified].
- Adyen's stated rationale: "Because billing and payments belong together"; "AI models and modern APIs carry significant, variable compute and token costs"; "charging a flat monthly fee per user simply does not scale"; Orb is "a product-connected billing platform purpose-built for usage, hybrid, and outcome-based monetisation models" [VERIFIED: knowledge-hub article, 2026-10-19]. The release adds that payments and billing "operate in isolated silos" and that connecting them "creates a two-way intelligence advantage"; Orb's CEO: "Standalone billing systems are fundamentally limited because they operate blind to transaction execution" [VERIFIED: announcement release].
- **Talon.One** (brief, for chapter 50): announced 23 April 2026, "a total consideration of €750 million", "a leading platform for loyalty and incentives", "300+ global merchants", "approximately €60 million in ARR as of the end of this year"; closed 1 July 2026 [VERIFIED: https://www.adyen.com/press-and-media/2i4hnm0pfcpvc7, published 2026-04-23; closing release above].

### 1.11 Stripe vs Adyen: subscriptions and billing engines

| Aspect | Stripe (documented) | Adyen (documented) | What the difference suggests |
| --- | --- | --- | --- |
| First-party subscription engine | Yes: Subscription, Schedule, Invoice objects, eight statuses, two billing modes (docs, 2026) | None in Adyen's own documentation; recurring is a token plus `recurringProcessingModel` (docs, 2023/2026) | Stripe took the billing state machine into the platform early; Adyen left it to the merchant or a partner until 2026 [ASSUMPTION/JUDGEMENT] |
| Usage billing | Meters (2024–), Metronome acquired 14 January 2026 and now recommended | Orb acquired 1 July 2026, run as an "incubator", multi-PSP | Both bought the usage engine rather than extending the subscription engine [ASSUMPTION/JUDGEMENT] |
| Billing without the provider's payments | Announced October 2024 (third-party processors) | Orb "continuing to support multi-PSP environments" | Both treat billing as separable from acquiring, at least for now [ASSUMPTION/JUDGEMENT] |
| Engineering publications | Three posts (2017, 2025, 2025); none on the scheduler | Nothing found on billing internals (searched adyen.com/knowledge-hub, the Adyen Tech feed, docs.adyen.com) | The scheduler is the least documented part of both |

**For readers new to payments**

- **Subscription**: a standing agreement to charge a customer on a schedule; in a billing engine it is a state machine that produces invoices.
- **Billing cycle (and anchor)**: the repeating period a subscription bills for; the anchor is the timestamp that fixes on which day and second each period starts.
- **Proration**: charging or crediting a fraction of a price because a customer changed plan or quantity part-way through a period.
- **Merchant-initiated transaction**: a charge the business starts from stored credentials while the customer is not present; the card networks require it to be flagged as such (Adyen: `ContAuth` with a processing model).

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- A billing engine is a scheduler plus a pricing calculator plus a state machine; the payment API is only the last step. Treat the invoice as the hand-off object between them.
- Store anchors and period boundaries as instants in one time zone (Stripe: UTC seconds) and decide explicitly what "the first of the month" means for customers elsewhere.
- Proration rules are part of the contract with the customer. Changing them requires versioning the behaviour per subscription, as Stripe's two billing modes show.
- A webhook the billing engine waits for (Stripe's `invoice.created`) is a dependency of collection; its availability belongs in the billing SLO.

---

## PART 2: Usage metering and rating (chapter 28)

### 2.1 Stripe Billing Meters ("basic usage-based billing")

- "Meters specify how to aggregate meter events over a billing period. Meter events represent all actions that customers take in your system (for example, API requests). Meters attach to prices and form the basis of what's billed"; aggregation is **Sum**, **Count** or **Last**; after configuration "you can't make any changes aside from the display name" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure.md, n.d., accessed 2026-11].
- Ingestion modes: **Raw** ("Multiple events sent for the same timestamp don't overwrite each other") or **Pre-aggregated** (hourly or daily; "A newer event sent within the same hourly or daily window overwrites the previous one") [VERIFIED: same page].
- Asynchrony: "Stripe processes meter events asynchronously, so aggregated usage in meter event summaries and on upcoming invoices might not immediately reflect recently received meter events" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api.md, n.d., accessed 2026-11].
- Deduplication: "Use idempotency keys to prevent reporting usage for each event more than one time ... Every meter event corresponds to an identifier that you can specify in your request. If you don't specify an identifier, we auto-generate one for you" [VERIFIED: same page]. The deduplication window is not stated on the page read [ASSUMPTION/JUDGEMENT].
- Late events: "Make sure the timestamp is within the past 35 calendar days and isn't more than 5 minutes in the future"; but "The 35-day window determines whether Stripe accepts a meter event. It doesn't guarantee that Stripe can include the usage on an invoice ... Stripe might accept an event after finalization and include it in meter summaries without updating the finalized invoice or adding the usage to the next invoice" [VERIFIED: same page].
- The grace period that makes late events billable: "All invoices have a default finalization grace period of 1 hour. During the finalization grace period, you can continue to report usage for the previous billing period"; configurable "up to 72 hours (3 days)"; threshold invoices "reflect only the usage accrued up to the point the invoice is created" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period.md, n.d., accessed 2026-11].
- Corrections: a Meter Event Adjustment cancels events, but "You can only cancel events sent to Stripe within the last 24 hours. If you cancel usage that's included on a finalized invoice, we won't update the invoice" [VERIFIED: meters/configure page].
- Limits ⚠: "The Meter Event limit is 1000 calls per second per Stripe account"; one concurrent call per customer per meter; with API v2 meter event streams "you can send up to 10,000 events per second ... Contact sales if you need to send up to 200,000 events per second"; stream sessions use tokens "only valid for 15 minutes"; dimension limits of 10,000 unique combinations per meter per hour and 100 per customer; a Connect platform acting on a connected account is held to 100 operations per second [VERIFIED: recording-usage-api page; https://docs.stripe.com/api/v2/billing-meter-stream.md, n.d., accessed 2026-11].
- Errors are reported out of band through thin events `v1.billing.meter.error_report_triggered` and `v1.billing.meter.no_meter_found`, with codes such as `timestamp_too_far_in_past` and `meter_event_customer_not_found` [VERIFIED: recording-usage-api page].

### 2.2 How Stripe says it built the meter pipeline

From "How we built it: Usage-based billing" [VERIFIED: https://stripe.com/blog/how-we-built-it-usage-based-billing, published 2025-01-28]:

- Ingestion: events go to "an edge router, which does stateless authentication and API validation" and then onto an event bus; processing is asynchronous.
- Stream processing uses Apache Flink (chosen for exactly-once processing guarantees) in an active-active arrangement: "we process the same event in two geographic regions simultaneously", with "a standardized time stamp, generated before reaching the two Flink applications" used to reconcile the two streams.
- Two aggregation paths: "One is a fast path with a 30-second tumbling window, which we store in memory in real time" (alerts, balance warnings); "The second path is slower, with a five-minute window", written durably and used for invoicing and revenue data; the slow path "allows us to accommodate any delayed or out-of-order events".
- Stated capacity: "can handle 100,000 events per second per user, with a P95 latency under 30 seconds for time-sensitive operations". The post's wording on the scope of that figure is inconsistent (per business in one place, per user in another), and the limit published in today's documentation is 10,000 per second by default and 200,000 through sales. Use the documentation figures for limits and the post for design [ASSUMPTION/JUDGEMENT].
- The post does not describe deduplication, the storage engine behind the durable path, or how rated usage reaches the invoice [ASSUMPTION/JUDGEMENT: absence noted from the post as read through a summarising fetch; treat as "not public"].

### 2.3 Metronome ⚠

- Completion: Stripe "today announced that it has completed its acquisition of Metronome" on 14 January 2026; the release says Metronome's metering engine already serves AI companies including OpenAI, Anthropic and NVIDIA and that Stripe looks forward to integrating these capabilities with the Stripe Billing platform; no price disclosed [VERIFIED: https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition, published 2026-01-14; the customer list and integration intent are paraphrased from the release].
- The agreement was signed in December 2025 [WIDELY REPORTED: https://www.pymnts.com/acquisitions/2026/stripe-completes-purchase-of-billing-firm-metronome/, 2026; trade press].
- What the documentation now recommends: "Metronome is Stripe's primary usage-based billing platform and the recommended starting point for all new integrations. Basic usage-based billing, built on the Meters API, is a lower-level primitive that remains fully supported for existing integrations"; "If you already bill customers using Billing Meters, you don't need to migrate" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based.md, n.d., accessed 2026-11].
- Division of labour: "Metronome handles metering, rating, and billing, while Stripe handles payment collection, tax calculation, and revenue recognition" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/compare-metronome.md, n.d., accessed 2026-11].
- The integration is an invoice push, not a merged engine: "Metronome pushes finalized invoices to Stripe through the Invoicing API. This invoicing sync is one way, meaning Stripe doesn't send invoice data back to Metronome"; payment status syncs back. Two patterns: "Metronome independently" or "Metronome with Stripe Subscriptions", where "The customer receives both subscription invoices (from Stripe) and usage invoices (from Metronome)" [VERIFIED: https://docs.stripe.com/billing/how-metronome-works-with-stripe.md, n.d., accessed 2026-11].
- Documented gaps ("There are interoperability gaps between some Stripe products and Metronome"):

| Capability | Basic (Meters) | Metronome |
| --- | --- | --- |
| Credits | "Supported (invoice time)": "Credits are only reconciled at invoice time. Customers can exceed their balance during the cycle" | "Supported (real-time)"; prepaid drawdown |
| Commits, minimums, ramp schedules | Not supported | Supported |
| Dimensional pricing, multi-dimensional metering | Not supported | Supported |
| High-volume ingestion | "Limited" | Supported |
| Connect, Adaptive Pricing, Workflows, Stripe Dashboard | Supported | Not supported |
| Checkout | Supported | "Limited" (custom API calls and webhooks) |

[VERIFIED: compare-metronome page]

### 2.4 Credits, commitments and token billing

- Stripe credit grants: "Billing credits are prepaid or promotional usage credit allocated through credit grants. They aren't the customer invoice balance ... or a cash balance, which holds bank transfer funds"; states Pending, Granted, Depleted, Expired, Voided; "Credit grants apply to invoices after discounts, but before taxes and the customer invoice balance"; they apply only "to subscription items that use metered prices and report usage through Meters" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md, n.d., accessed 2026-11].
- Regulatory edge visible in the docs: "You can't offer billing credits as stored value to your customers", not as gift cards, not for "payments to third parties", not linked to digital wallets [VERIFIED: same page]. These prohibitions keep prepaid credit on the "prepayment for the seller's own service" side of stored-value regulation [ASSUMPTION/JUDGEMENT].
- Three balances exist side by side in Stripe: billing credit grants (usage prepayment), the customer invoice balance (adjustments) and the cash balance (bank-transfer funds) [VERIFIED: same page]. Chapter writers should not merge them.
- Token billing ⚠: "Billing for LLM tokens is in public preview and available to all users with a Metronome account"; "Stripe syncs token prices for OpenAI, Anthropic, and Google models, so your pricing always reflects current costs"; usage can be metered per customer by model and by token type "(input, output, and cached tokens for supported models)"; "Metronome evaluates usage in real time and sends invoices to Stripe for payment" [VERIFIED: https://docs.stripe.com/billing/token-billing.md, n.d., accessed 2026-11].
- Orb commitments are "in early access": a postpaid commitment "settles at the end ... if cumulative usage falls short of the commitment, Orb bills the difference as a true-up"; a prepaid commitment invoices "upfront for a pool of credits that usage draws down" [VERIFIED: https://docs.withorb.com/enterprise/commitments.md, n.d., accessed 2026-11]. ⚠

### 2.5 Orb's architecture as its own documentation describes it

Orb publishes more architecture than either Stripe or Adyen on this topic. These are Orb's statements about itself, made before and after the acquisition; they describe Orb, not Adyen's platform.

- Query-based billing: "Orb's billing engine treats billing as the output of a deterministic query, not a side effect of streaming state mutations"; "Every usage event is stored immutably in a columnar data store. When generating an invoice, Orb executes a fresh query over the raw event data ... The invoice is computed, not retrieved" [VERIFIED: https://docs.withorb.com/architecture/query-based-billing.md, n.d., accessed 2026-11].
- Its critique of the alternative: "Most billing systems process usage events as they arrive, incrementing counters and updating aggregations in real-time ... once an event is processed and the counter is incremented, the original context is lost" [VERIFIED: same page].
- Not a full recomputation every time: "a dependency graph and invalidation system track how each invoice fragment depends on usage, pricing, and configuration. When relevant data changes ... only the affected invoice fragments are invalidated" [VERIFIED: same page].
- Ingestion and deduplication: "Orb provides per-event idempotency through the API to guarantee that duplicates are never processed within the account grace period. By default, Orb limits the request size to 500 events per batch"; default throughput "200,000 events per minute—close to 300 million events per day"; no upfront schema for event `properties` [VERIFIED: https://docs.withorb.com/events-and-metrics/event-ingestion.md, n.d., accessed 2026-11]. ⚠
- Late events: "your system can report events to the Orb API up to 12 hours after the `timestamp`, which is called the *grace period* ... a pending invoice might still be subject to changes for 12 hours after the end of the period and will not be finalized until the grace period has passed" (configurable per account) [VERIFIED: https://docs.withorb.com/events-and-metrics/reporting-errors.md, n.d., accessed 2026-11].
- Backfills and amendments: "Orb never overwrites or permanently deletes ingested usage data"; a timeframe amendment replaces events in a range and "Old events are marked as archived"; a single event can be amended by `PUT` on the event ID, "which is the same as an event's `idempotency_key`"; caveat: "you should not rely on the idempotency guarantee across normal event ingestion and backfills", and backfilling before the current period is not recommended with the credit ledger [VERIFIED: same page].
- Very high volume: above roughly 10,000 events per second Orb recommends syncing files from a cloud bucket; "hosted rollups" pre-aggregate "generally north of 500,000 events per second", with a default 10-minute window and partial rollups every 30 seconds, and "typically uses an intermediate cloud bucket as a durable message queue" [VERIFIED: https://docs.withorb.com/events-and-metrics/high-throughput-ingestion.md, n.d., accessed 2026-11]. Rollups trade the raw-event guarantee for throughput [ASSUMPTION/JUDGEMENT].
- Metrics as queries: "Orb's architecture is designed to run aggregation queries over large sets of event data at query time rather than at ingestion time"; an evaluate-prices API rates event data "with SQL-like flexibility" [VERIFIED: https://docs.withorb.com/events-and-metrics/querying-with-sql.md, n.d., accessed 2026-11].
- Subscription changes as diffs: the "diff-based engine" computes the invoices that should exist, compares them with those that do, and applies the difference "in a single transaction"; issued invoices are corrected with credit notes; backdated actions "rewind time" and replay [VERIFIED: https://docs.withorb.com/architecture/billing-architecture.md, n.d., accessed 2026-11].
- Adyen's release echoes the same design in one sentence: "Orb stores the full event stream at scale, decoupling ingestion from invoicing" [VERIFIED: Adyen announcement, 2026-06-11].
- Open-source contrast: Lago (AGPLv3) describes the same pipeline as "Usage events -> Metering -> Pricing and credits -> Entitlements -> Invoices -> Payments -> Revenue" [VERIFIED: https://github.com/getlago/lago (README), n.d., accessed 2026-11].

### 2.6 Stripe vs Adyen: metering and rating

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Own meter primitive | Billing Meters: sum/count/last, 35-day acceptance window, 1-hour to 72-hour grace period, 24-hour cancellation window (docs, 2026) | None in Adyen documentation |
| Acquired usage engine | Metronome (completed 2026-01-14); recommended for all new usage integrations; one-way invoice push into Stripe | Orb (completed 2026-07-01); stand-alone, multi-PSP; integration "soon" (October 2026) |
| Published design | Flink, active-active across two regions, 30-second fast path and five-minute durable path (blog, 2025) | Orb's docs: immutable raw events in a columnar store, invoices as deterministic queries with invalidation |
| Late and corrected events | Accept up to 35 days; bill only until finalization; adjust within 24 hours | Orb: 12-hour reporting grace period; audit-safe backfills and amendments |
| Real-time credit balance | Meters: invoice-time only; Metronome: real time | Orb: prepaid credit ledger and balance alerts (docs) |
| Token billing | Public preview through Metronome | Orb documents "Pricing an AI agent"; Adyen cites token metering as the use case |

Interpretation [ASSUMPTION/JUDGEMENT]: the public record shows two different answers to "aggregate at ingestion or at query time". Stripe's 2025 post describes windowed stream aggregation with a slower durable path; Orb's documentation argues for storing raw events and computing invoices by query. Metronome's internals were not researched in this brief, so no claim is made about which side it falls on.

**For readers new to payments**

- **Usage event**: one record saying a customer did or consumed something at a given time; billing systems require it to carry a unique identifier so duplicates can be dropped.
- **Meter (billable metric)**: the rule that turns many usage events into one quantity for a period, such as a sum or a count.
- **Rating**: applying a price plan to a metered quantity to get an amount of money.
- **Credit balance and commitment**: prepaid or promised spend that usage draws down; a commitment unpaid by usage is billed as a "true-up".

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Decide the late-event policy before the first invoice: an acceptance window (Stripe 35 days), a billing cut-off (finalization plus grace period) and a correction path are three separate settings.
- Keep raw events if retroactive repricing or audits matter; aggregate at ingestion only where volume forces it and accept the loss of flexibility.
- Real-time balance checks and invoice-time rating are different consistency requirements; Stripe's own table separates them.
- Deduplication keys must come from the producer. A key generated by the billing system on receipt deduplicates nothing.

---

## PART 3: Invoicing, collections and dunning (chapter 29)

### 3.1 The invoice state machine and immutability

- Stripe's documented transitions: `draft` → (finalize) → `open` → (pay) → `paid`; `open` → `void`; `open` → `uncollectible`; `uncollectible` → `paid` or `void`; a `draft` can be deleted. Each transition has an endpoint and a webhook (`invoice.finalized`, `invoice.paid`, `invoice.payment_failed`, `invoice.voided`, `invoice.marked_uncollectible`) [VERIFIED: https://docs.stripe.com/invoicing/integration/workflow-transitions.md, n.d., accessed 2026-11].
- Finalization does five things: "It allows the invoice to be paid. It ensures that an invoice number is present. It makes certain properties immutable on the invoice. It creates an incomplete payment intent for the invoice. It generates a unique URL where someone can pay the invoice, and a link to download a PDF" [VERIFIED: same page].
- Why immutability: "This is to satisfy the common tax-compliance requirement that finalized invoices be retained—as they were finalized—for a legally required minimum time period"; customer name, address, tax IDs and exemption status are copied onto the invoice at finalization [VERIFIED: same page].
- To change a customer field after finalization: void, duplicate, edit the copy [VERIFIED: same page]. Editing finalized subscription invoices is "in preview" [VERIFIED: https://docs.stripe.com/billing/invoices/subscription.md, n.d., accessed 2026-11]. ⚠
- Credit notes: "Credit notes are documents that decrease the amount of an `open` or `paid` invoice ... a credit note doesn't void and replace the original invoice"; "The sum of all credit notes issued for an invoice can't exceed the total amount of the invoice"; for a paid invoice the amount goes to the customer's invoice balance, a refund, or an out-of-Stripe refund; "A credit note doesn't restore applied billing credit grants" [VERIFIED: https://docs.stripe.com/invoicing/dashboard/credit-notes.md, n.d., accessed 2026-11].

### 3.2 Retries: fixed schedules and Smart Retries

- What Stripe claims: "Using AI, Smart Retries chooses the best times to retry failed payment attempts ... The AI model behind Smart Retries uses time-dependent, dynamic signals, such as: The number of different devices that have presented a given payment method in the last *N* hours. The best time to pay (payments made for debit cards in certain countries might be slightly more successful at 12:01 am in local time zones)" [VERIFIED: https://docs.stripe.com/billing/revenue-recovery/smart-retries.md, n.d., accessed 2026-11]. No model description, features list or measured uplift is published in the documentation [ASSUMPTION/JUDGEMENT].
- Defaults ⚠: "For new Stripe accounts, Stripe enables Smart Retries by default and configures it for up to 8 retries within 2 weeks"; the window can be 1, 2 or 3 weeks, 1 month or 2 months. The alternative is a custom schedule: "You can configure up to three retries, each with a specific number of days after the previous attempt" [VERIFIED: same page].
- No retry when: no payment method is available; "The issuer returns a hard decline code"; the card is India-issued; the Connect account is disconnected. The hard decline codes listed include `lost_card`, `stolen_card`, `pickup_card`, `incorrect_number`, `revocation_of_authorization`, `authentication_required` and `transaction_not_allowed`; for these "Retries continue to be scheduled, and `attempt_count` continues to increment, but retries only execute after detecting a new payment method" [VERIFIED: same page].
- Which payment method is retried is ordered: subscription default payment method, subscription default source, customer default payment method, legacy customer source. Updating the wrong field leaves retries on the old method [VERIFIED: same page].
- Direct debit is a separate policy. SEPA Direct Debit and Bacs: retryable failure "Insufficient funds", maximum 2 retries within 30 days; ACH: 2 retries within 40 days; "Stripe isn't responsible for any losses if we don't retry a payment made with a local payment method" [VERIFIED: same page].
- Contrast, a plain fixed schedule: Orb's "essential dunning" retries "after 1, 4, and 9 days from the initial payment attempt", then sends a failure email [VERIFIED: https://docs.withorb.com/financial-operations/essential-dunning.md, n.d., accessed 2026-11].
- Adyen's equivalent is **Auto Rescue**, at the payment layer rather than the invoice layer: it "automatically retries refused or charged back shopper-not-present transactions such as subscription renewals. It uses smart logic to decide which payments can succeed when retried later, and performs these retries at optimal times" [VERIFIED: https://docs.adyen.com/online-payments/auto-rescue.md, last modified 2020-03-04 **(evidence age: 6 years; the card sub-page fetched today is current and consistent)**]. For cards it applies to `ContAuth` payments, with "a rescue window of one calendar month" at account level or `maxDaysToRescue` between 1 and 48 days per transaction; the merchant supplies a `merchantOrderReference` that "should represent a specific billing cycle or subscription"; for SEPA "a maximum of two rescue attempts within the rescue window", default window 42 days [VERIFIED: https://docs.adyen.com/online-payments/auto-rescue/cards.md and https://docs.adyen.com/online-payments/auto-rescue/sepa.md, n.d., accessed 2026-11].

### 3.3 Card updates, emails and the portal

- Stripe: "Stripe works with card networks and automatically attempts to update saved card details whenever a customer receives a new card ... It's widely supported in the United States ... International support varies from country to country. It isn't possible to identify cards that support automatic updates"; the event is `payment_method.automatically_updated` [VERIFIED: https://docs.stripe.com/payments/cards/overview.md, n.d., accessed 2026-11].
- Adyen: Real Time Account Updater works inside the payment: "If a payment is declined, we send an account update request and immediately retry the payment with the updated details ... If you use Adyen tokenization, the token storing the card details is updated automatically"; a Batch Account Updater exchanges files; schemes named are Visa, Mastercard and Cartes Bancaires [VERIFIED: https://docs.adyen.com/online-payments/account-updater.md, last modified 2019-12-06 **(evidence age: 7 years; not contradicted by the current tokenization page, which still points to features that "reduce declines due to replaced or expired cards")**].
- Emails: Stripe can send failed-payment, expiring-card, trial-ending and renewal emails that link to "a Stripe-hosted Customer Portal or your own custom subscription management page" [VERIFIED: https://docs.stripe.com/billing/revenue-recovery/customer-emails.md, n.d., accessed 2026-11]. The customer portal lets customers update payment methods, cancel and (newly) pause subscriptions [VERIFIED: https://docs.stripe.com/customer-management.md, n.d., accessed 2026-11].
- Automations allow per-segment dunning, for example a "Custom dunning flow for annual subscribers" [VERIFIED: https://docs.stripe.com/billing/revenue-recovery.md, n.d., accessed 2026-11].

### 3.4 Involuntary churn figures (vendor claims only)

- Stripe: "US$8.2bn in failed payments recovered in 2025", "US$14 recovered for every US$1 spent in 2025", "Businesses using Stripe recover 55% of failed payments on average" [VERIFIED: https://stripe.com/billing, n.d., accessed 2026-11]. **Label as vendor marketing claims**: no definition of "failed payment", "recovered" or the cohort is given on the page [ASSUMPTION/JUDGEMENT]. ⚠
- Recurly defines the term but the page read gives no number: "Involuntary churn refers to customer loss caused by factors outside their direct intent — expired credit cards, bank account changes, or failed payment attempts" [VERIFIED: https://docs.recurly.com/recurly-subscriptions/docs/involuntary-churn.md, updated 2026-07-07].
- No independent, primary measurement of the share of churn that is involuntary was found. Writers should not quote the commonly repeated "20–40% of churn" figures without a source [ASSUMPTION/JUDGEMENT].

### 3.5 Bank transfers, cash application and partial payments

- "Stripe creates a unique virtual bank account number and displays it on the invoice PDF and the hosted invoice page ... Stripe automatically reconciles these bank transfers to the correct invoices when they're received. If we can't automatically reconcile a transfer, it remains in the customer balance until you manually reconcile it" [VERIFIED: https://docs.stripe.com/invoicing/bank-transfer.md, n.d., accessed 2026-11].
- Why a balance is needed: "bank transfers don't allow you to control the amount a customer sends to you, which means that customers might send too much or too little money by accident ... Stripe holds your customer's bank transfers in a customer balance" [VERIFIED: https://docs.stripe.com/payments/bank-transfers.md, n.d., accessed 2026-11].
- The matching algorithm is documented step by step (USD, EUR and others): match the transfer reference to one invoice number; else to one PaymentIntent reference; else search for "a group of between one and five invoices and PaymentIntents awaiting the exact amount available"; else fund as many invoices as can be fully funded, oldest due first; else apply the remainder to incomplete PaymentIntents. An invoice is eligible while `open` and not more than 365 days overdue [VERIFIED: https://docs.stripe.com/payments/customer-balance/reconciliation.md, n.d., accessed 2026-11].
- Unreconciled funds: after 75 days Stripe "automatically attempts to return the funds to the customer's bank account"; by 90 days, if it cannot, "we sweep the unreconciled funds to your Stripe account balance" [VERIFIED: bank-transfers page].
- Tolerance: Stripe can "mark an invoice as paid if it's partially paid within the set amount" (example given: within 20 USD) by applying a credit for the difference; past-due invoices can be marked uncollectible after 30, 60 or 90 days [VERIFIED: https://docs.stripe.com/invoicing/automatic-collection.md, n.d., accessed 2026-11].
- Adyen: no documented invoice object, cash-application feature or customer balance for receivables was found in the pages read; bank-transfer and direct-debit payments exist as payment methods and Auto Rescue covers SEPA retries (3.2) [ASSUMPTION/JUDGEMENT on the absence].

### 3.6 E-invoicing mandates (brief)

- The EU's VAT in the Digital Age package "was adopted on 11 March 2025" and "will be rolled out progressively until January 2035"; published in the Official Journal on 25 March 2025 as Directive (EU) 2025/516, Regulation (EU) 2025/517 and Implementing Regulation (EU) 2025/518 [VERIFIED: https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en, n.d., accessed 2026-11].
- Dates: "Upon entry into force (14 April 2025), Member States are able to introduce mandatory e-invoicing under specific conditions"; "Digital Reporting Requirements will affect cross-border B2B transactions from 1 July 2030"; "By 1 January 2035, Member States with a domestic digital real-time transaction reporting obligation must align their systems with the EU model" [VERIFIED: same page]. ⚠ National mandates (for example Belgium and France in 2026) were not verified in this session.
- Consequence for an invoice engine: a structured, machine-readable invoice submitted to or reported through a tax-authority-defined channel is a different artefact from a PDF, and Stripe's own docs warn "Invoice finalization requirements vary by region" [VERIFIED: grace-period page] [the consequence is ASSUMPTION/JUDGEMENT].

### 3.7 Stripe vs Adyen: invoicing and recovery

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Invoice object and state machine | Documented: draft, open, paid, void, uncollectible; credit notes; immutability | None found in Adyen docs; Orb has its own invoice lifecycle, credit notes and dunning (docs.withorb.com) |
| Retry intelligence | Smart Retries on invoices: "AI", default 8 retries in 2 weeks | Auto Rescue on payments: "smart logic", one-month default window, 1–48 days |
| Unit being recovered | The invoice (many attempts, one debt) | The payment, tied to the merchant's `merchantOrderReference` |
| Card updates | Automatic, network-dependent, webhook on update | Real Time Account Updater inside the authorization, or batch files |
| Cash application | Virtual accounts, customer cash balance, published matching order | Not found |
| Published recovery numbers | Marketing page (2025 figures) | None found |

Interpretation [ASSUMPTION/JUDGEMENT]: Stripe recovers a *debt* because it owns the invoice; Adyen recovers a *payment* because, before Orb, it did not know what the payment was for beyond a reference. That is the clearest architectural consequence of where the billing engine sits.

**For readers new to payments**

- **Invoice**: a numbered, dated statement of what a customer owes and for which period; once finalized it must not change, for tax reasons.
- **Credit note**: a document that reduces a finalized invoice instead of editing it.
- **Dunning**: the process of chasing a failed or overdue payment: retries, emails and, in the end, pausing or cancelling.
- **Involuntary churn**: losing a subscriber because a payment failed, not because the customer chose to leave.
- **Cash application**: matching money that has arrived (for example by bank transfer) to the invoices it was meant to pay.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Model retries against the invoice, not the payment, so that a new card, a partial payment or a bank transfer can all settle the same debt.
- Separate soft and hard declines before scheduling anything; retrying a hard decline costs fees and network goodwill.
- Direct debit needs its own schedule: failures arrive days later and the networks cap retries.
- Hold unmatched incoming money in an explicit balance with an ageing rule; never guess silently.

---

## PART 4: Tax in the payment path (chapter 30)

### 4.1 Stripe Tax

- The compliance cycle as Stripe frames it: "1. Understand which locations require you to collect tax. 2. Register for tax in those locations. 3. Calculate and collect tax. 4. File and remit the tax you collected" [VERIFIED: https://docs.stripe.com/tax/how-tax-works.md, n.d., accessed 2026-11].
- Inputs: "Stripe Tax uses your business address, tax registrations, product tax codes, customers' locations, and customer status to determine the correct tax rates"; "We have tax researchers who monitor tax laws and tax authority publications for changes" [VERIFIED: same page].
- Registration gates calculation: "Stripe only calculates tax in jurisdictions where you have an active tax registration. Without a registration in the customer's location, the calculation returns zero tax" [VERIFIED: https://docs.stripe.com/tax/custom.md, n.d., accessed 2026-11].
- B2B: "Stripe Tax uses customer tax identification numbers to determine whether a transaction is B2B ... Stripe Tax doesn't validate whether the provided tax identification number exists or is valid" [VERIFIED: how-tax-works page].
- Monitoring: "Stripe Tax tracks your Stripe-processed sales (minus refunds) based on each customer's location and compares these sales against local tax registration thresholds"; transactions are added "within 7 days"; "it's up to you to confirm whether registration is actually required"; off-Stripe sales count only if imported or sent through the Tax API [VERIFIED: https://docs.stripe.com/tax/monitoring.md, n.d., accessed 2026-11].
- Coverage ⚠: the supported-countries table lists **108** locations (counted from the table rows on 17 November 2026); many are "Digital products" only, where the business cannot be based but the customer can be [VERIFIED: https://docs.stripe.com/tax/supported-countries.md, n.d., accessed 2026-11].
- Registration and filing: "Registration and filing are separate services"; "Stripe Tax offers automated filing in the US, as well as automated filing for selected registrations in Ireland and Canada" (non-Union OSS in Ireland, simplified GST/HST in Canada); partners are Taxually, Marosa and Hands-off Sales Tax, with TaxJar credits in the Tax Complete plan; "Global filing with Stripe (Private preview)" [VERIFIED: https://docs.stripe.com/tax/filing.md, n.d., accessed 2026-11]. ⚠
- Tax API for custom flows: "The standalone Tax Calculations and Tax Transactions APIs lets you calculate tax, record transactions, and handle reversals directly. Use them with PaymentIntents or when processing payments off-Stripe"; IP-based estimates are offered but "we recommend against using an IP address to determine the *final* amount of tax" [VERIFIED: tax/custom page].
- Platforms: "The first step for using Stripe Tax with Connect requires you to determine which entity has the obligation to collect and report taxes"; two cases, software platforms (connected accounts liable) and marketplaces (platform liable); "Stripe Connect's distinction between SaaS platforms and marketplaces doesn't strictly correspond to the tax definition of marketplaces" [VERIFIED: https://docs.stripe.com/tax/connect.md, n.d., accessed 2026-11]. For threshold monitoring, "Separate charges and transfers without `on_behalf_of` aren't included. This is because Stripe can't know who the liable party for the transfer is" [VERIFIED: tax/monitoring page].
- Pricing ⚠ (euro pricing page as served to this session): Tax Basic "0.5% per transaction, where you're registered to collect taxes" for no-code integrations or "€0.45 per transaction" through the API; Tax Complete "Starting at €80.00 per month, 1-year contract" [VERIFIED: https://stripe.com/pricing, n.d., accessed 2026-11].

### 4.2 EU: platforms as deemed suppliers

- Since 1 July 2021: "Online marketplaces/platforms facilitating supplies of goods are, in certain circumstances, deemed for VAT purposes to have received and supplied the goods themselves ('deemed supplier')"; the national distance-selling thresholds were replaced by "a new EU-wide threshold of EUR 10 000"; the One Stop Shop lets a seller declare and pay VAT for all Member States through one registration; platforms have record-keeping duties even "where such online marketplaces/platform are not a deemed supplier" [VERIFIED: https://vat-one-stop-shop.ec.europa.eu/index_en, n.d., accessed 2026-11]. The legal basis (Article 14a of the VAT Directive, inserted by Directive (EU) 2017/2455) was not fetched [ASSUMPTION/JUDGEMENT].
- ViDA extends the idea to services: "From July 1, 2028, platforms in short-term accommodation rental and passenger transport by road must comply with new deemed supplier measures"; "(Member States can delay implementation until 1 January 2030)"; the platform becomes "responsible for collecting and remitting VAT to tax authorities when the suppliers using the platform do not" [VERIFIED: https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en, n.d., accessed 2026-11]. ⚠
- The 2021 rule covers goods and the 2028/2030 rule two service sectors. A platform for fitness studios is in neither category on the face of these texts; whether any national rule applies is a question for a tax adviser [ASSUMPTION/JUDGEMENT].

### 4.3 US: economic nexus after Wayfair

- *South Dakota v. Wayfair, Inc.*, decided 21 June 2018: "Because the physical presence rule of *Quill* is unsound and incorrect, *Quill Corp. v. North Dakota* ... and *National Bellas Hess* ... are overruled." The South Dakota Act applied to sellers that "deliver more than $100,000 of goods or services into the State or engage in 200 or more separate transactions" annually [VERIFIED: https://www.law.cornell.edu/supremecourt/text/17-494, decided 2018-06-21 **(evidence age: 8 years; the holding stands, but state thresholds have since diverged and several states dropped the transaction-count test, which was not verified here)**].
- This is why registration monitoring is a product: Stripe calls potential obligations "economic nexus in the US" and tracks sales per state against thresholds [VERIFIED: tax/monitoring page].

### 4.4 Adyen: no first-party tax engine found

- Searched: `docs.adyen.com` (search and navigation of the online-payments section), `help.adyen.com`, `adyen.com` product pages and the open web for "Adyen tax calculation", "sales tax", "VAT engine", "Avalara", "Vertex". **Nothing public describes an Adyen product that calculates, collects or files indirect tax on a merchant's sales** [ASSUMPTION/JUDGEMENT on the absence].
- What Adyen does publish about tax concerns its own fees: "Adyen does not deduct sales tax or value-added tax (VAT) from your settlement batches", and Adyen charges sales tax or VAT on its own invoices to merchants in some territories (US states from 1 May 2021; France from 1 May 2021) [VERIFIED: https://help.adyen.com/knowledge/finance/invoices/what-kind-of-tax-is-applied-to-my-invoice, n.d., accessed 2026-11].
- Orb's documentation was not checked for a tax feature in this session; treat Orb's tax handling as unverified.

### 4.5 Tax engines as contrast

- Avalara: "Avalara AvaTax automates precise tax calculations, explains line-item determinations, and verifies transaction data in real time ... across your ERP, billing, purchasing and commerce systems" [VERIFIED: https://www.avalara.com/us/en/products/calculations.html, n.d., accessed 2026-11].
- Vertex: "Continually updated tax rules and rates for 19,000 jurisdictions around the world" [VERIFIED: https://www.vertexinc.com/solutions/products/vertex-indirect-tax-o-series, n.d., accessed 2026-11]. Vendor claim; the definition of "jurisdiction" is the vendor's.
- Managed Payments (PART 6) does not allow "Third-party tax integrations" [VERIFIED: https://docs.stripe.com/payments/managed-payments.md, n.d., accessed 2026-11].

### 4.6 Stripe vs Adyen: tax

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Calculation | Stripe Tax, in Checkout, Billing, Invoicing, or the Tax API including off-Stripe payments (docs, 2026) | Nothing public found |
| Registration monitoring | Threshold tracking on Stripe-processed sales | Nothing public found |
| Filing | First-party in the US, Ireland (non-Union OSS) and Canada (simplified GST/HST); partners elsewhere; global filing in private preview | Nothing public found |
| Liability | Stays with the merchant, except under Managed Payments | Stays with the merchant |

The difference is one of product scope, not of payment architecture: Stripe sells tax as an adjacent product on the same transaction data; Adyen leaves tax to the merchant's own systems or a tax engine [ASSUMPTION/JUDGEMENT].

**For readers new to payments**

- **Indirect tax (VAT, GST, sales tax)**: a tax on a sale that the seller collects from the buyer and passes to a tax authority.
- **Tax registration and nexus**: the obligation to register with a tax authority once a seller has enough connection with its territory, which since 2018 in the US can be sales volume alone.
- **Reverse charge**: a rule for many cross-border business sales under which the buyer, not the seller, accounts for the VAT.
- **Deemed supplier**: a platform that the law treats as if it had bought and resold the goods or services, so that the platform owes the VAT.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Tax needs three facts at calculation time (who sells, what is sold, where the customer is) and one piece of state (where the seller is registered). That is why it sits next to billing and checkout rather than in the ledger.
- A tax engine that sees only one provider's transactions under-counts thresholds; multi-provider businesses need the import path or an independent engine.
- For a platform, the liable party is a per-transaction attribute that the funds flow must carry (Stripe cannot infer it for separate charges and transfers).

---

## PART 5: Revenue recognition (chapter 31)

### 5.1 The standard

- "In May 2014 the Board issued IFRS 15 *Revenue from Contracts with Customers*, together with the introduction of Topic 606 into the Financial Accounting Standards Board's *Accounting Standards Codification*"; effective for annual periods beginning on or after 1 January 2018 [VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/, n.d., accessed 2026-11].
- The five steps, in the IFRS Foundation's words: "identify the contract(s) with a customer"; "identify the performance obligations in the contract. Performance obligations are promises in a contract to transfer to a customer goods or services that are distinct"; "determine the transaction price"; "allocate the transaction price to each performance obligation on the basis of the relative stand-alone selling prices"; "recognise revenue when a performance obligation is satisfied by transferring a promised good or service to a customer (which is when the customer obtains control of that good or service)" [VERIFIED: same page].
- "A performance obligation may be satisfied at a point in time (typically for promises to transfer goods to a customer) or over time (typically for promises to transfer services to a customer)" [VERIFIED: same page]. FASB's own text was not fetched; ASC 606 is cited here only through the IFRS Foundation's statement of the joint issue.

### 5.2 Stripe Revenue Recognition as documented

- Basis: "Stripe built Revenue Recognition on top of a double-entry accounting ledger that tracks debits and credits resulting from your business activity"; it "automatically calculates all transactions that happen within Stripe, including subscriptions, invoices, one-time payments, refunds, disputes, and so on, timed to the second" [VERIFIED: https://docs.stripe.com/revenue-recognition/methodology.md, n.d., accessed 2026-11].
- The simplifying assumption: "Revenue Recognition treats each invoice line item as its own performance obligation. When the invoice finalizes, Revenue Recognition defers the total recognizable amount and subsequently amortizes it evenly over the period of each invoice line item" [VERIFIED: same page]. This maps step 2 of the standard onto the invoice structure; a contract whose obligations do not line up with invoice lines needs rules or imports [ASSUMPTION/JUDGEMENT].
- Payments without invoices: "By default, Revenue Recognition recognizes these payments immediately when the payment occurs" [VERIFIED: same page].
- Default chart of accounts includes Revenue, Refunds, Disputes, Credit notes, Bad debt and Voids (contra revenue), Fees, Recoverables, Fx loss, Accounts receivable, Cash, Deferred revenue, Long-term deferred revenue and Unbilled deferred revenue [VERIFIED: same page].
- Worked effects, from the same page: "if you issue a 120 USD refund on an annual subscription during the second month, 20 USD for the first 2 months is contra revenue. The remaining 100 USD is adjusted and reflected in your deferred revenue balance"; a dispute behaves the same way, and if the dispute is won "20 USD is reflected as revenue and the remaining 100 USD is reflected as recoverables" [VERIFIED: same page].
- Cash is defined narrowly: "Cash is the net cash amount received. **This doesn't include Stripe fees or payouts.**" [VERIFIED: same page].
- Rules: custom rules can treat a line as tax or pass-through fee, exclude transactions, amortize over a custom period or split treatments; "Each transaction can only have one rule applied to it"; "Rules are typically applied to reports within 24 hours" [VERIFIED: https://docs.stripe.com/revenue-recognition/rules.md, n.d., accessed 2026-11].
- Data import: CSV imports can add or override a service period, split a payment into several schedules, or bring in "an external payment processor's data"; exclusion and journal-entry imports exist; reports "take approximately 3-4 hours to update after you upload data" [VERIFIED: https://docs.stripe.com/revenue-recognition/data-import.md, n.d., accessed 2026-11].
- Who it is for, in Stripe's words: "Public companies or large businesses with over 25 million USD in annual revenue because they're legally required to comply with ASC 606 and GAAP and IFRS accounting standards" [VERIFIED: methodology page]. The 25 million USD figure is Stripe's framing, not a legal threshold verified here [ASSUMPTION/JUDGEMENT].
- Limitations that follow from the documentation [ASSUMPTION/JUDGEMENT, derived from the verified statements above]: recognition is evenly over time by default (no usage-pattern or milestone method without rules or imports); stand-alone selling price allocation across bundled obligations is not described; contract modifications are handled as invoice and proration events; data arrives with hours of delay. It is a subledger whose output still has to reach the general ledger. RECONCILED covers that hand-off; link, do not repeat.
- Pricing ⚠: "€20.00 per month" or annual plans "Starting at €175.00 per month, 1-year contract" [VERIFIED: https://stripe.com/pricing, n.d., accessed 2026-11].

### 5.3 Adyen and Orb

- Adyen: no revenue-recognition product or documentation found (searched docs.adyen.com and adyen.com). Adyen's reports describe payments, settlement and fees, which is cash-side data [ASSUMPTION/JUDGEMENT on the absence].
- Orb does document one: "Orb automatically calculates recognized revenue in a way that accords with ASC606 guidelines"; principles of completeness, consistency ("the proration methodology between billing and revenue recognition does not diverge") and auditability ("the lineage of revenue from a summary entry → invoice → raw product usage data"); "Orb guarantees that your recognized revenue always converges to your billed revenue over time" [VERIFIED: https://docs.withorb.com/revenue-reporting/revenue-recognition.md, n.d., accessed 2026-11]. Orb also lists accounting-sync webhooks and data exports to warehouses in its documentation index [VERIFIED: https://docs.withorb.com/llms.txt, n.d., accessed 2026-11].
- Usage makes recognition harder for a reason Orb states: it "requires understanding exactly when usage occurs. This can be particularly difficult when invoicing and accounting periods do not align, or for cases like credit drawdowns where invoices may not contain the required information" [VERIFIED: Orb recognition page].

### 5.4 Stripe vs Adyen: revenue recognition

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| First-party product | Stripe Revenue Recognition on a double-entry ledger; invoice line = performance obligation; rules and imports (docs, 2026) | None found; Orb has revenue reporting aligned to ASC 606 (Orb docs, 2026) |
| Source of schedules | Stripe invoices, payments, refunds, disputes, credit notes | Orb: invoices and raw usage events |
| Boundary with the ERP | Reports, exports, GL account mapping | Orb: exports and accounting sync |

**For readers new to payments**

- **Revenue recognition**: the accounting rule for *when* a sale counts as revenue, which is when the service is delivered, not when cash arrives.
- **Performance obligation**: one distinct promise to the customer inside a contract (a year of software access, an onboarding service).
- **Deferred revenue**: money invoiced or received for service not yet delivered; a liability until it is earned.
- **Contra revenue**: an account that reduces revenue, used for refunds, disputes and credit notes instead of deleting the original entry.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- A billing engine must export, per invoice line, the amount net of tax, the service period and every later adjustment (refund, dispute, credit note) with its own timestamp. That is the minimum from which any recognition schedule can be rebuilt.
- Recognition inside the billing provider is a convenience for businesses whose contracts equal their invoices. Once contracts are negotiated, bundled or multi-system, the schedule belongs in a finance system fed by the billing engine.
- For usage, keep the usage date as well as the invoice date; they fall in different accounting periods at every month end.

---

## PART 6: Merchant of record (chapter 32)

### 6.1 Definitions and the legal distinction

- Stripe's definition: the merchant of record is the entity "legally authorised and responsible for processing customer payments"; "The MoR is liable for the financial, legal and compliance aspects of transactions". A payment facilitator works by "aggregating multiple merchant accounts under one master account" but "does not assume responsibility for tax collection and remittance". In an ordinary Stripe integration "the business itself remains the MoR while Stripe acts as a payment processor or payment gateway" [VERIFIED: https://stripe.com/resources/more/merchant-of-record, last updated 2026-01-27].
- Paddle's definition: "Paddle operates as the Merchant of Record for your digital products. This means we take on the responsibility for all aspects of the transaction, from processing payments to handling sales tax compliance. Essentially, when a buyer purchases your product through Paddle, we act as the seller to them" [VERIFIED: https://www.paddle.com/help/sell/tax/how-paddle-handles-vat-on-your-behalf, n.d., accessed 2026-11].
- The distinction in one table [ASSUMPTION/JUDGEMENT, synthesising the two definitions above and card-network practice; the network rule texts were not fetched for this brief, see the `platforms` brief]:

| | Processor / gateway | Payment facilitator | Merchant of record |
| --- | --- | --- | --- |
| Who is the seller to the buyer | The business | The business (as a sub-merchant) | The MoR (it resells the product) |
| Who holds the acquiring relationship | The business | The facilitator, for its sub-merchants | The MoR |
| Who owes the indirect tax | The business | The business | The MoR |
| Name on the card statement | The business | The business, often with the facilitator's prefix | The MoR, usually with the product name |
| Disputes and fraud liability to the networks | The business | Facilitator is liable for its sub-merchants; passes losses on | The MoR |

### 6.2 Stripe Managed Payments ⚠

- What it is: "The Stripe merchant of record solution handles sales tax, VAT, and GST compliance in more than 80 countries, along with fraud prevention, dispute management, and transaction-level customer support"; for "digital products such as SaaS, software, and digital content or downloads" [VERIFIED: https://docs.stripe.com/payments/managed-payments.md, n.d., accessed 2026-11].
- Dates: the API changelog entry "Adds support for Managed Payments, Stripe's merchant of record solution" for Checkout Sessions and Payment Links is dated **22 April 2026** (API version `2026-04-22.dahlia`) [VERIFIED: https://docs.stripe.com/changelog/dahlia/2026-04-22/managed-payments.md, published 2026-04-22]. The product was first shown at Stripe Sessions in spring 2025 as a private preview [WIDELY REPORTED: https://www.paddle.com/resources/stripe-managed-payments and other vendor blogs, 2025–2026; competitor and trade sources, no Stripe release found].
- Fee: "3.5% per successful Managed Payments transaction in addition to Payments fees" [VERIFIED: https://stripe.com/pricing, n.d., accessed 2026-11].
- The customer sees Link, not the business: "The customer sees Link as the merchant of record, and sees purchases as *Sold through Link*"; the statement descriptor is "`LINK.COM* [Your statement descriptor]`"; receipts and invoices "are sent from Link"; "Custom domains aren't supported on Managed Payments checkouts" [VERIFIED: https://docs.stripe.com/payments/managed-payments/how-it-works.md, n.d., accessed 2026-11].
- What Stripe takes on: tax ("calculates and collects tax ... then files and remits payments to the relevant tax authorities"; also "Issues tax invoices"); fraud ("No action is needed from you because Stripe configures the rules and maintains blocklists"); disputes ("If we decide to counter a dispute, we submit evidence on your behalf ... If we determine that you're unlikely to win a dispute, we might accept it"); transaction support through Link [VERIFIED: how-it-works page; https://docs.stripe.com/payments/managed-payments/tax-compliance.md, n.d., accessed 2026-11].
- What stays with the business, or costs it: "Received disputes incur a dispute received fee"; if Stripe asks for product input and "you don't respond within 48 hours, Stripe might issue a refund without your approval"; on refunds in some jurisdictions "your account balance will be reduced by the amount that corresponds to the original sales tax amount"; product-level support stays with the business [VERIFIED: how-it-works page].
- Tax liability is not universal: "In countries where local regulations prevent Managed Payments from assuming liability for indirect taxes, you're responsible for handling tax compliance"; domestic exceptions include Japan (all domestic sales) and Singapore (B2B domestic) [VERIFIED: tax-compliance page].
- Eligibility: "Stripe determines access to Managed Payments based on an eligibility review"; "Managed Payments supports direct integrations only. It doesn't support ... Connect platforms, Express accounts, Accounts controlled by a platform"; business locations listed are the US and Canada, 31 European countries (the 27 EU member states plus CH, GB, LI and NO), and AU, HK, JP, SG [VERIFIED: https://docs.stripe.com/payments/managed-payments/eligibility.md, n.d., accessed 2026-11].
- Product restrictions: digital only; not "Physical goods", "Professional services", "Live in-person events"; "You sell the product directly to customers, not through a platform or marketplace"; "You sell a fully automated digital product. If your service involves human intervention (such as live 1-1 coaching), it doesn't qualify"; each product needs an eligible tax code [VERIFIED: same page].
- Integration restrictions: only Checkout and Payment Links; no Elements with Checkout Sessions, no direct PaymentIntents integrations, no subscriptions created outside Checkout or Payment Links, no one-off invoices outside the billing period, no third-party tax integrations [VERIFIED: managed-payments overview page].
- Data: on a customer's deletion request Stripe "Cancels any subscriptions sold to them through Managed Payments" and deletes their data from objects "including objects in your Stripe account" [VERIFIED: how-it-works page]. The customer relationship partly belongs to the merchant of record; this is the data-ownership cost of the model [ASSUMPTION/JUDGEMENT].
- Reporting: by default the `fee` column "includes both Stripe fees and withheld tax", with optional `withheld_tax` and `fee_net_of_withheld_tax` columns [VERIFIED: same page].

### 6.3 Lemon Squeezy

- "We're excited and humbled to announce that @stripe has acquired @lmsqueezy", posted by JR Farr on 26 July 2024; the post says Stripe will help "continue to improve the merchant of record offering" [VERIFIED: https://www.lemonsqueezy.com/blog/stripe-acquires-lemon-squeezy, published 2024-07-26]. Price not disclosed.
- The same page, as fetched on 17 November 2026, carries a site notice that Lemon Squeezy no longer accepts new sign-ups and will shut down on 31 March 2027 [VERIFIED: same URL, banner n.d., accessed 2026-11]. ⚠ The notice was read through a summarising fetch; confirm the exact wording before quoting.
- Reading: Stripe bought a merchant-of-record business in 2024, shipped its own in 2026 and is closing the acquired brand [ASSUMPTION/JUDGEMENT on the causal link].

### 6.4 Paddle as the contrast

- Paddle is "registered in over 100 jurisdictions worldwide" and so can "Calculate and charge the correct amount of sales tax", "Remit those taxes to the relevant tax authorities globally" and issue compliant invoices [VERIFIED: https://www.paddle.com/help/sell/tax/how-paddle-handles-vat-on-your-behalf, n.d., accessed 2026-11].
- Price ⚠: "5% + 50¢ per Checkout transaction", described as all-inclusive with "No monthly fees" [VERIFIED: https://www.paddle.com/pricing, n.d., accessed 2026-11].
- Structural difference from Managed Payments [ASSUMPTION/JUDGEMENT, from the two price pages]: Paddle prices one bundle (payments, billing, tax, MoR); Stripe prices the MoR service as a 3.5% layer on top of its payment fees, with Billing charged separately.

### 6.5 App stores

- Apple: "The commission on the sale of digital goods and services through the App Store is 30% (15% if you're enrolled in the App Store Small Business Program ...) and 15% for qualifying subscriptions"; "Different commission rates and fees may apply for certain apps distributed in Brazil, the European Union, Japan, the Netherlands, Russia, and South Korea" [VERIFIED: https://developer.apple.com/programs/whats-included/, n.d., accessed 2026-11]. The Small Business Program applies up to 1 million USD in prior-year proceeds [VERIFIED: https://developer.apple.com/app-store/small-business-program/, n.d., accessed 2026-11]. That Apple is the legal seller (as agent or commissionaire, depending on the region) is in the Paid Applications Agreement, which was not accessible [ASSUMPTION/JUDGEMENT].
- Google Play: for many countries, "Google is responsible for determining, charging, and remitting" the tax on "paid app and in-app purchases made by customers ... using Google Play's billing system", while for purchases "using an alternative billing system, you are responsible" (wording from the Australia section; the page repeats the pattern per country) [VERIFIED: https://support.google.com/googleplay/android-developer/answer/138000, n.d., accessed 2026-11].
- Stripe positions Managed Payments for apps too: the overview links "Accept mobile app payments" [VERIFIED: managed-payments overview page].

### 6.6 Stripe vs Adyen: merchant of record

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| First-party MoR | Managed Payments (API support April 2026): 3.5% on top of payment fees; digital products; no Connect | Nothing found: no Adyen product in which Adyen is the seller to the end customer (searched adyen.com and docs.adyen.com) |
| Prior acquisition | Lemon Squeezy, July 2024; shutting down 31 March 2027 per its site | None |
| Customer-facing brand | Link ("Sold through Link") | Not applicable |

Interpretation [ASSUMPTION/JUDGEMENT]: becoming the seller means taking tax, fraud and dispute liability for long-tail digital businesses, which fits Stripe's self-serve base and its existing Tax, Radar and Link products. Adyen's enterprise merchants are themselves the seller in each market and have the entities to prove it; a merchant-of-record product would not fit that base. The absence is consistent with the customer base, not a gap in capability.

**For readers new to payments**

- **Merchant of record**: the legal seller in a transaction, whose name is on the receipt and the card statement and who owes the tax and answers for disputes.
- **Payment facilitator**: a provider that lets many businesses accept cards under its own acquiring agreement; the businesses remain the sellers.
- **Liability transfer**: moving a legal responsibility (tax, fraud losses, dispute handling) from the business to the provider, in exchange for a fee and for control.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Merchant of record is an operating model, not a feature flag: it changes the checkout (the provider's), the statement descriptor, the invoice issuer, who holds customer data and what the integration may call.
- It cannot be combined with a platform model in Stripe's implementation. A business that pays out to third parties (studios, sellers) is excluded by the rule "not through a platform or marketplace".
- Exit cost is higher than for a processor: tokens, subscriptions and the tax history sit with the seller of record.

---

## PART 7: Material for chapters 43 and 50

### 7.1 A failed renewal, end to end (chapter 43)

A timeline that uses only documented Stripe behaviour, for a `charge_automatically` monthly subscription [each step VERIFIED in the section cited; the assembled sequence is ASSUMPTION/JUDGEMENT]:

1. At the anchor instant (UTC) the period rolls; Stripe creates a `draft` invoice and sends `invoice.created` (1.7).
2. Usage reported during the grace period (default 1 hour, up to 72) is still included (2.1).
3. About an hour after all webhook endpoints acknowledge `invoice.created`, the invoice is finalized: number assigned, fields frozen, PaymentIntent created (3.1).
4. The payment fails. The subscription becomes `past_due`; `invoice.payment_failed` carries `attempt_count` (1.2, 3.2).
5. A hard decline stops execution of retries until a new payment method appears; a soft decline enters Smart Retries (default up to 8 attempts in 2 weeks) (3.2).
6. In parallel: a failed-payment email with a link to the portal; a network card update may arrive as `payment_method.automatically_updated` (3.3).
7. A retry succeeds: the invoice becomes `paid` and the subscription returns to `active`, "regardless of whether you settle the required invoices before or after their due dates" (1.2).
8. Or retries are exhausted: per settings the subscription is `canceled`, `unpaid`, left `past_due` or `paused` (1.2).

On Adyen the same story is assembled by the merchant: its own scheduler submits a `ContAuth` / `Subscription` payment on a token; Real Time Account Updater may repair the card inside the authorization; Auto Rescue retries within its window and reports by webhook against the merchant's `merchantOrderReference`; the invoice and subscription state live in the merchant's or a billing partner's system (1.9, 3.2, 3.3) [ASSUMPTION/JUDGEMENT on the assembled sequence].

### 7.2 Consolidation timeline (chapter 50)

| Date | Event | Tag |
| --- | --- | --- |
| 2024-07-26 | Stripe acquires Lemon Squeezy (merchant of record) | [VERIFIED: lemonsqueezy.com blog, 2024-07-26] |
| 2024-10-29 | Stripe Billing: third-party processors, credits, 72-hour grace period | [VERIFIED: stripe.com/blog, 2024-10-29] |
| 2025-12 | Stripe signs agreement to acquire Metronome | [WIDELY REPORTED: PYMNTS, 2026] |
| 2026-01-14 | Stripe completes Metronome acquisition | [VERIFIED: Stripe newsroom, 2026-01-14] |
| 2026-02-24 | Stripe: Revenue suite "on track to hit an annual run rate of $1 billion this year" | [VERIFIED: Stripe newsroom, 2026-02-24] |
| 2026-04-22 | Managed Payments in the Stripe API (Checkout, Payment Links) | [VERIFIED: Stripe changelog, 2026-04-22] |
| 2026-04-23 | Adyen announces Talon.One, €750 million | [VERIFIED: Adyen press, 2026-04-23] |
| 2026-06-11 | Adyen announces Orb, $335 million | [VERIFIED: Adyen press, 2026-06-11] |
| 2026-07-01 | Adyen closes both | [VERIFIED: Adyen press, 2026-07-01] |
| 2026-10-19 | Adyen: unified Adyen and Orb experience coming "soon" | [VERIFIED: Adyen knowledge hub, 2026-10-19] |
| 2027-03-31 | Lemon Squeezy shutdown date announced on its site | [VERIFIED: lemonsqueezy.com banner, accessed 2026-11] ⚠ |

Both companies bought usage-billing engines within six months of each other and both cite AI pricing as the reason. Stripe's acquisition is further along in documentation (Metronome is the documented default for new usage integrations); Adyen's is at the stated-intent stage [ASSUMPTION/JUDGEMENT].

---

## Key numbers

| Number | Exact definition | Source | Date |
| --- | --- | --- | --- |
| 23 hours | Time a customer has to pay the first invoice before a Stripe subscription becomes `incomplete_expired` | docs.stripe.com/billing/subscriptions/overview | n.d., accessed 2026-11 |
| ~1 hour | Time a Stripe renewal invoice stays `draft` after `invoice.created` is acknowledged, before finalization and payment | docs.stripe.com/invoicing/integration/workflow-transitions | n.d., accessed 2026-11 |
| 72 hours | Stripe finalizes anyway if webhooks are not acknowledged; also the maximum configurable finalization grace period | same; configure-grace-period | n.d., accessed 2026-11 |
| 10 | Maximum phases in a Stripe subscription schedule | docs.stripe.com/billing/subscriptions/subscription-schedules | n.d., accessed 2026-11 |
| 8 retries in 2 weeks | Default Smart Retries policy for new Stripe accounts | docs.stripe.com/billing/revenue-recovery/smart-retries | n.d., accessed 2026-11 ⚠ |
| 3 | Maximum retries in a Stripe custom retry schedule | same | n.d., accessed 2026-11 |
| 2 retries / 30 days | Stripe SEPA Direct Debit and Bacs retry limits (insufficient funds only) | same | n.d., accessed 2026-11 |
| 1–48 days (cards), 1–42 days (SEPA) | Adyen Auto Rescue window (`maxDaysToRescue`); account-level default one calendar month for cards, 42 days for SEPA | docs.adyen.com/online-payments/auto-rescue/cards, /sepa | n.d., accessed 2026-11 |
| 1, 4, 9 days | Orb essential dunning retry offsets | docs.withorb.com/financial-operations/essential-dunning | n.d., accessed 2026-11 |
| 35 days / 5 minutes | Stripe meter event timestamp acceptance: past / future | docs.stripe.com/.../recording-usage-api | n.d., accessed 2026-11 |
| 24 hours | Window in which a Stripe meter event can be cancelled | docs.stripe.com/.../meters/configure | n.d., accessed 2026-11 |
| 1,000 calls/s; 10,000 events/s; 200,000 events/s | Stripe meter event API limit per account; v2 stream limit; stream limit via sales | recording-usage-api | n.d., accessed 2026-11 ⚠ |
| 30 s / 5 min | Stripe meter pipeline fast-path and durable-path aggregation windows | stripe.com/blog/how-we-built-it-usage-based-billing | 2025-01-28 |
| 200,000 events/min; 500 per batch | Orb default ingestion limit and batch size | docs.withorb.com/events-and-metrics/event-ingestion | n.d., accessed 2026-11 ⚠ |
| 12 hours | Orb default event reporting grace period | docs.withorb.com/events-and-metrics/reporting-errors | n.d., accessed 2026-11 |
| 75 / 90 days | Stripe returns unreconciled bank-transfer funds / sweeps them to the account balance | docs.stripe.com/payments/bank-transfers | n.d., accessed 2026-11 |
| 108 | Locations in Stripe Tax's supported-countries table (counted) | docs.stripe.com/tax/supported-countries | accessed 2026-11-17 ⚠ |
| 80+ countries | Where Managed Payments handles indirect tax | docs.stripe.com/payments/managed-payments | n.d., accessed 2026-11 ⚠ |
| 3.5% | Managed Payments fee per successful transaction, in addition to payment fees | stripe.com/pricing | n.d., accessed 2026-11 ⚠ |
| 0.7% | Stripe Billing pay-as-you-go fee on Billing volume | stripe.com/pricing | n.d., accessed 2026-11 ⚠ |
| 5% + 50¢ | Paddle fee per checkout transaction | paddle.com/pricing | n.d., accessed 2026-11 ⚠ |
| 30% / 15% | Apple App Store commission, standard / small business and qualifying subscriptions | developer.apple.com/programs/whats-included | n.d., accessed 2026-11 ⚠ |
| $1 billion | Annual run rate Stripe's Revenue suite is "on track to hit ... this year" (2026) | stripe.com/newsroom/news/stripe-2025-update | 2026-02-24 |
| 350,000+ | Companies using Stripe Billing (vendor claim; excludes Metronome) | stripe.com/billing | n.d., accessed 2026-11 ⚠ |
| 55%; US$8.2bn | Average share of failed payments recovered; failed payments recovered in 2025 (vendor claims, undefined cohort) | stripe.com/billing | n.d., accessed 2026-11 ⚠ |
| $335 million | Adyen's consideration for Orb, cash | adyen.com press release | 2026-06-11 |
| €750 million | Adyen's consideration for Talon.One, cash | adyen.com press release | 2026-04-23 |
| EUR 10,000 | EU-wide annual threshold for intra-EU distance sales and TBE services since 1 July 2021 | vat-one-stop-shop.ec.europa.eu | n.d., accessed 2026-11 |
| 1 July 2028 (1 January 2030) | ViDA deemed-supplier rule for short-term accommodation and road passenger transport platforms (optional national delay) | taxation-customs.ec.europa.eu ViDA page | n.d., accessed 2026-11 |
| $100,000 or 200 transactions | South Dakota's thresholds upheld in *Wayfair* | law.cornell.edu/supremecourt/text/17-494 | 2018-06-21 |

## Open questions / not verifiable

1. **Stripe's subscription scheduler.** How renewals are scheduled, partitioned and made idempotent, and how many are processed at month boundaries, is not public. The book can state the observable contract (draft for about an hour, webhook-gated finalization) and nothing more.
2. **The Smart Retries model.** Two example signals are published; the model, its training data and its measured uplift are not. The 55% recovery figure is a marketing average without a definition.
3. **Adyen's Auto Rescue logic.** "Smart logic" and "optimal times" are the whole public description.
4. **Adyen and Orb integration.** As of 17 November 2026 no integrated product is documented. Whether Orb will remain multi-PSP after "the first phase", and what "convergence" will look like, is unknown. Orb's customer count and volumes were not disclosed.
5. **Metronome's internal architecture and its future inside Stripe Billing.** The documented integration is an invoice push; whether the two engines merge is not stated. The signing date and price are not in a primary source read here.
6. **Stripe's annual-letter wording** on the Revenue suite (2024 and 2025 letters) beyond the newsroom sentence.
7. **Managed Payments launch chronology**: the Sessions 2025 preview and any general-availability statement were not found in a Stripe primary source. Whether the 3.5% fee applied during the preview is unknown.
8. **Lemon Squeezy shutdown**: date read from a site banner through a summarising fetch; migration terms for its merchants were not researched.
9. **Apple's and Google's legal seller role** in the wording of their distribution agreements.
10. **Independent involuntary-churn data**: none found. The share of churn that is involuntary, by sector, is not established by any primary source in this brief.
11. **Adyen first-party tax, invoicing, cash application, revenue recognition or merchant of record**: none found; absence of evidence from public documentation, not confirmation from Adyen.
12. **National e-invoicing mandates** (Belgium, France, Germany, Poland) and current US state nexus thresholds: not verified here; see ORDERED's tax brief and verify before quoting.
13. **The meter event deduplication window** in Stripe (how long an identifier is remembered) is not stated on the pages read.
14. **Stripe Billing with third-party processors** (announced October 2024): current availability and limits not re-checked.

## Source list

**Stripe documentation (docs.stripe.com; undated living pages, accessed 2026-11-17; append `.md` for markdown)**

- How subscriptions work — /billing/subscriptions/overview — lifecycle, eight statuses, 23-hour rule.
- Set the subscription billing renewal date — /billing/subscriptions/billing-cycle — anchors, month ends, UTC.
- Prorations — /billing/subscriptions/prorations — definition, classification table, to-the-second default.
- Enable increased flexibility for subscriptions — /billing/subscriptions/billing-mode; Compare classic and flexible — /billing/subscriptions/billing-mode/compare — the two modes, API-version defaults.
- Configure trial offers — /billing/subscriptions/trials; Pause payment collection — /billing/subscriptions/pause-payment; Pause subscriptions — /billing/subscriptions/pause; Subscription schedules — /billing/subscriptions/subscription-schedules.
- Subscription invoices — /billing/invoices/subscription; Status transitions and finalization — /invoicing/integration/workflow-transitions — draft hour, webhook gating, immutability.
- Test your Billing integration — /billing/testing/test-clocks — test clocks and simulation limits.
- Entitlements — /billing/entitlements; Invoice Payments API — /api/invoice-payment; Partial payments — /invoicing/partial-payments; Credit notes — /invoicing/dashboard/credit-notes.
- Basic usage-based billing — /billing/subscriptions/usage-based; Create and configure a meter — /…/usage-based/meters/configure; Record usage with the API — /…/usage-based/recording-usage-api; Grace period — /…/usage-based/configure-grace-period; Billing credits — /…/usage-based/billing-credits; Meter Event Streams — /api/v2/billing-meter-stream.
- Compare basic usage-based billing and Metronome — /…/usage-based/compare-metronome; How Metronome works with Stripe — /billing/how-metronome-works-with-stripe; Bill for LLM tokens — /billing/token-billing.
- Automate payment retries — /billing/revenue-recovery/smart-retries; Revenue recovery — /billing/revenue-recovery; Automate customer emails — /billing/revenue-recovery/customer-emails; Automatic collection — /invoicing/automatic-collection; How cards work (automatic card updates) — /payments/cards/overview; Customer portal — /customer-management.
- Bank transfer (invoicing) — /invoicing/bank-transfer; Bank transfer payments — /payments/bank-transfers; Reconciliation — /payments/customer-balance/reconciliation.
- Stripe Tax — /tax; How Stripe Tax works — /tax/how-tax-works; Supported countries — /tax/supported-countries; Monitor your obligations — /tax/monitoring; File and remit — /tax/filing; Standalone Tax APIs — /tax/custom; Tax with Connect — /tax/connect.
- Revenue Recognition — /revenue-recognition; How Revenue Recognition works — /revenue-recognition/methodology; Rules — /revenue-recognition/rules; Data import — /revenue-recognition/data-import.
- Managed Payments — /payments/managed-payments; How it works — /payments/managed-payments/how-it-works; Eligibility — /payments/managed-payments/eligibility; Tax compliance — /payments/managed-payments/tax-compliance; Changelog entry — /changelog/dahlia/2026-04-22/managed-payments (2026-04-22).

**Stripe, other**

- "Stripe completes Metronome acquisition", Stripe newsroom, 2026-01-14, https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition — completion date, customers named.
- "Stripe publishes 2025 annual letter…", Stripe newsroom, 2026-02-24, https://stripe.com/newsroom/news/stripe-2025-update — Revenue suite run rate, total volume.
- "Online migrations at scale", Jacqueline Xu, Stripe blog, 2017-02-02, https://stripe.com/blog/online-migrations — Subscriptions object count, dual writes (evidence age 9 years).
- "How we built it: Usage-based billing", Taras Mitran and Karan Dhabalia, Stripe blog, 2025-01-28, https://stripe.com/blog/how-we-built-it-usage-based-billing — meter pipeline design.
- "How we built it: Real-time analytics for Stripe Billing", Reed Trevelyan, stripe.dev, 2025-09-16, https://stripe.dev/blog/how-we-built-it-real-time-analytics-for-stripe-billing — Flink and Pinot for Billing analytics.
- "Our biggest-ever upgrades to Stripe Billing", Wisam Hirzalla, Stripe blog, 2024-10-29, https://stripe.com/blog/our-biggest-ever-upgrades-to-stripe-billing — third-party processors, credits.
- Stripe Billing product page, n.d., https://stripe.com/billing — vendor statistics. Stripe pricing, n.d., https://stripe.com/pricing — fees. "Merchant of record" guide, updated 2026-01-27, https://stripe.com/resources/more/merchant-of-record — definitions.
- "Stripe acquires Lemon Squeezy", JR Farr, Lemon Squeezy blog, 2024-07-26, https://www.lemonsqueezy.com/blog/stripe-acquires-lemon-squeezy — acquisition; shutdown banner.

**Adyen**

- "Adyen to acquire Orb to unify billing and payments infrastructure for enterprise merchants", press release, 2026-06-11, https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj — price, incubator model, rationale.
- "Adyen Closes Talon.One and Orb Acquisitions; Announces Leadership Updates…", press release, 2026-07-01, https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates — closing date.
- "Why Adyen acquired Orb", Blake Breathitt, Adyen knowledge hub, 2026-10-19, https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb — rationale, integration "soon".
- "Adyen to acquire Talon.One…", press release, 2026-04-23, https://www.adyen.com/press-and-media/2i4hnm0pfcpvc7 — price and description.
- "Adyen publishes H1 2026 financial results", press release, 2026-08-13, https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne — acquisitions in guidance.
- Tokenization, n.d., https://docs.adyen.com/online-payments/tokenization; Make token payments, last modified 2023-07-28, https://docs.adyen.com/online-payments/tokenization/make-token-payments — recurring model.
- Account Updater, last modified 2019-12-06, https://docs.adyen.com/online-payments/account-updater; Auto Rescue, last modified 2020-03-04, https://docs.adyen.com/online-payments/auto-rescue; Auto Rescue for cards and for SEPA, n.d., /auto-rescue/cards, /auto-rescue/sepa — recovery at the payment layer.
- "What kind of tax is applied to my invoice?", Adyen help, n.d., https://help.adyen.com/knowledge/finance/invoices/what-kind-of-tax-is-applied-to-my-invoice — tax on Adyen's own fees only.

**Orb (docs.withorb.com; undated, accessed 2026-11-17)**

- Query-based billing — /architecture/query-based-billing; Diff-based engine — /architecture/billing-architecture; Ingest events — /events-and-metrics/event-ingestion; Backfill and amend events — /events-and-metrics/reporting-errors; Hosted rollups — /events-and-metrics/high-throughput-ingestion; Querying data with SQL — /events-and-metrics/querying-with-sql; Payments — /invoicing/payments; Essential dunning — /financial-operations/essential-dunning; Commitments — /enterprise/commitments; Recognition methodology — /revenue-reporting/revenue-recognition; index — /llms.txt.

**Other vendors**

- Paddle, "How Paddle handles VAT on your behalf", n.d., https://www.paddle.com/help/sell/tax/how-paddle-handles-vat-on-your-behalf — MoR definition; Paddle pricing, n.d., https://www.paddle.com/pricing.
- Chargebee, "Proration Mode", n.d., https://www.chargebee.com/docs/billing/2.0/subscriptions/proration — day versus millisecond proration.
- Recurly, "Involuntary churn", updated 2026-07-07, https://docs.recurly.com/recurly-subscriptions/docs/involuntary-churn — definition.
- Lago, README, n.d., https://github.com/getlago/lago — open-source (AGPLv3) pipeline, provider-independent.
- Avalara AvaTax, n.d., https://www.avalara.com/us/en/products/calculations.html; Vertex O Series, n.d., https://www.vertexinc.com/solutions/products/vertex-indirect-tax-o-series — tax engines.
- Apple, "What's included" and "App Store Small Business Program", n.d., https://developer.apple.com/programs/whats-included/, https://developer.apple.com/app-store/small-business-program/ — commission.
- Google, "Tax rates and value-added tax (VAT)" Play Console help, n.d., https://support.google.com/googleplay/android-developer/answer/138000 — where Google remits tax.

**Standards, law and regulators**

- IFRS Foundation, "IFRS 15 Revenue from Contracts with Customers", n.d., https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ — five steps, May 2014 joint issue with ASC 606.
- European Commission, "VAT in the Digital Age (ViDA)", n.d., https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en — adoption 11 March 2025, timeline to 2035.
- European Commission, "VAT e-Commerce – One Stop Shop", n.d., https://vat-one-stop-shop.ec.europa.eu/index_en — 1 July 2021 rules, deemed supplier, EUR 10,000.
- US Supreme Court, *South Dakota v. Wayfair, Inc.*, No. 17-494, 2018-06-21, text at https://www.law.cornell.edu/supremecourt/text/17-494 — physical-presence rule overruled.

**Secondary**

- PYMNTS, "Stripe Completes Purchase of Billing Firm Metronome", 2026-01, https://www.pymnts.com/acquisitions/2026/stripe-completes-purchase-of-billing-firm-metronome/ — signing in December 2025 (trade press).
- Paddle, "Stripe Managed Payments" resource page, 2025–2026, https://www.paddle.com/resources/stripe-managed-payments — Sessions 2025 preview history (competitor source; not fetched in full).
