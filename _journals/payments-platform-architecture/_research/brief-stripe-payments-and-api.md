# Research brief: Stripe payments objects and the Stripe API (state machines, object model, idempotency, versioning, webhooks, developer platform)

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 08 (payment state machines), 17 (API design and object models), 18 (idempotency and retries), 19 (API versioning), 20 (webhooks and events), 21 (developer platform), and parts of 02 (authorization), 04 (refunds, reversals and disputes), 07 (local payment methods) and 46 (case: Stripe). This brief covers **Stripe only**, as deeply as the public record allows. The parallel brief `brief-adyen-payments-and-api.md` covers Adyen; the "Stripe vs Adyen" notes here cite only the handful of Adyen pages fetched in this session to anchor the contrast, and the Adyen brief is authoritative for the Adyen side.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the publication date shown on the page; undated documentation pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: a reputable secondary source, with the kind of source named.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including **every** statement about how Stripe works internally beyond what it has published.

**Evidence age matters.** Stripe's three best-known API engineering posts (idempotency, rate limiters, versioning) were all published in **2017** and are more than nine years old. Each is flagged **(evidence age: 9 years)** below, with a statement of whether the current documentation confirms, updates or contradicts it. Stripe's documentation pages are living documents with no publication date; several changed materially between 2024 and 2026 (sandboxes replaced test mode as the default, thin events became the recommended format, Checkout Sessions became the recommended payment API).

**Research limitation.**

- **No general-availability date for Sandboxes was found.** Stripe's developer digest gives private beta (June 2024) and public beta (August 2024); current documentation treats sandboxes as the default. One web search found no GA announcement; `stripe.com/blog/sandboxes` returns 404.
- **No dated launch announcement for API v2 was found.** The earliest dated primary evidence is the changelog entry for `2024-09-30.acacia` (thin events on `/v2/core/events`) and for `2024-10-28.acacia` (Event Destinations v2 API). A June 2026 Stripe engineering post says "In 2024, Stripe introduced the v2 namespace".
- **Nothing was found from Stripe on how it delivers webhooks internally** (fan-out, queueing, per-endpoint isolation). One search and a scan of the 120-odd post slugs on `stripe.dev/blog` found only receiver-side guidance.
- **Stripe's internal API review process** is public only as one paragraph in the 2017 versioning post and as the automated lint checks described in a June 2026 post. No public document describes the review board, its membership or its written API design guide.
- The **Sessions 2025 announcement page** tried (`stripe.com/blog/everything-we-announced-at-sessions-2025`) returned 404; Sessions material was not used.
- Per-payment-method detail (which methods support manual capture, refunds, disputes) was not surveyed here; it belongs to the `acquiring` brief.
- The **"Canonical log lines"** post (Stripe blog, 2019-07-30) and the August 2026 post on Stripe's own distributed proxy were located but not read in depth; they belong to the `scale` brief.
- Stripe's `.md` documentation pages now embed instructions addressed to coding agents (for example, to prefer Checkout Sessions over PaymentIntents). These were read as evidence of Stripe's recommendation, nothing more.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: the current API version, rate-limit numbers, the preview status of v2 resources and of thin events for v1 resources, the recommended integration surface, SDK retry defaults, and the Sources API shutdown.

---

## PART 1: From Charges to PaymentIntents (chapters 08, 02, 04, 07, 46)

### 1.1 The dated history, in Stripe's own words

The single best primary source is Michelle Bu's "Stripe's payments APIs: The first 10 years", now hosted at `stripe.dev/blog/payment-api-design` (the old `stripe.com/blog/payment-api-design` URL redirects there). **(evidence age: 6 years.)** The current docs confirm its account of the end state; they have since moved one step further (Checkout Sessions, section 1.5).

| Period | What Stripe shipped | Why it broke, per the post |
| --- | --- | --- |
| 2011–2015 | `Token` (created client-side by Stripe.js with a publishable key) + `Charge` (created server-side, synchronously, with a secret key) | Nothing: cards in the US are "immediately finalized" and need no customer action |
| 2015 | ACH debit and Bitcoin added to Charges; a `pending` state added to `Charge`; a separate `BitcoinReceiver` resource | Two payment methods that finalize later; one that needs a customer action; "managing two state machines to complete payment" |
| 2015–2017 | The **Sources API**: "a single client-side API that could represent multiple payment methods", a "client-driven state machine" that could be `chargeable` or `pending` | The server still had to create the Charge after the customer acted; if the browser lost the connection, no Charge was created and Stripe refunded the customer |
| late 2017 – early 2018 | Design of a unified API by "a team of five people—four engineers and a PM" over three months | — |
| 2018 | `PaymentIntent` and `PaymentMethod` introduced | — |
| 2018–2020 | Rollout: "rolling out this change took almost two years" | Migration, documentation, and the perception that it was no longer "seven lines of code" |

All rows: [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15].

Quotes worth reusing, all from the same post [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15]:

- On the failure mode of Sources with iDEAL: "If the client-side application creates a Source and the browser then loses connectivity with the server, the next request to create a Charge wouldn't make it through, even though the customer believes they paid. … Because the server never created a Charge, we'd refund the money associated with the Source after a few hours. This is a conversion nightmare."
- On the root cause: "we built support for new payment methods on top of a set of abstractions that were designed for the simplest payment method of them all: cards." And: "Global payment methods aren't different; cards are!"
- "Charges and Tokens were foundational in the API because they were the first APIs we had, not because they were the right abstraction for global payments."
- The two-axis table the post uses to classify payment methods: *payment is immediately finalized / finalized later* against *no customer action required / customer action required*. Cards are alone in the first quadrant; ACH, SEPA, Bacs and BECS debit finalize later without customer action; iDEAL, Alipay, giropay, Bancontact, WeChat Pay, Przelewy24 and cards with 3D Secure need a customer action and finalize immediately; Bitcoin, Multibanco and paper checks need both.
- On the growth of the Charge object: "Between 2011 and 2018, the Charge resource grew from having 11 properties to 36 properties and Charge creation grew from accepting 5 parameters to 14 parameters!"
- On the migration design: "we decided to layer over the legacy APIs and create a Charge object for each payment attempted by the PaymentIntent. This way, users could migrate their payment flow to the PaymentIntents API while their analytics and reporting integrations still chugged along on an unchanged Charge resource."
- On the cost to the simple case: "PaymentIntents is also objectively a harder integration for users who only care about accepting card payments in the US and Canada. We flipped the order of the client and server calls … and webhooks are often more than a little bit annoying to set up, test, and debug."
- The escape hatch: a parameter `error_on_requires_action` that "tells the PaymentIntent to error if further action is required", packaged in the docs as "card payments without bank authentication".
- The general lesson: "Two overloaded API abstractions are not simpler and are definitely not more flexible and powerful than three or four clearly-defined abstractions."

The post defines "finalized" as: "We describe payments as 'finalized' when a user has sufficient confidence the funds are guaranteed. (Of course, even finalized payments can be reversed later due to fraud or subsequent refunds.)" [VERIFIED: same]. This matches the book's central idea (the instant answer versus the slow truth) closely enough to quote [ASSUMPTION/JUDGEMENT].

The regulatory forcing function: Stripe's docs list "Support for Strong Customer Authentication (SCA) and similar regulatory changes" among the advantages of PaymentIntents and define SCA as "a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments" [VERIFIED: https://docs.stripe.com/payments/payment-intents.md, n.d., accessed 2026-11]. The 2020 post does not present SCA as the cause of the redesign; it presents non-card payment methods as the cause [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15]. That SCA gave merchants in Europe a deadline to migrate is the analyst's reading [ASSUMPTION/JUDGEMENT].

### 1.2 Status of the older APIs today

- "We've replaced some of our older APIs and no longer update their documentation." The comparison table says Charges, Tokens and Sources support "Cards, ACH" only, are not SCA-ready, do not work with Terminal, and get no future development [VERIFIED: https://docs.stripe.com/payments/older-apis.md, n.d., accessed 2026-11].
- **Charges** "aren't going away": "Although unsupported, these APIs aren't going away. Until you upgrade your integration, you can still use these APIs: Charges, ACH" [VERIFIED: same].
- ⚠ **Sources** is deprecated and being shut down: "We've deprecated support for local payment methods in the Sources API and plan to turn it off"; card payments through Sources are deprecated too, "but don't currently plan to turn it off" on one page [VERIFIED: https://docs.stripe.com/payments/older-apis.md, n.d., accessed 2026-11], while the migration page says "We plan to stop Sources API support for card payments, and to stop support for Cards" and the Sources page says "New integrations can't use the Sources API" [VERIFIED: https://docs.stripe.com/payments/payment-methods/transitioning.md and https://docs.stripe.com/sources.md, n.d., accessed 2026-11]. The two pages disagree on card Sources; writers should say "deprecated, shutdown announced, no public date" [ASSUMPTION/JUDGEMENT].
- The `Charge` object still exists underneath: a PaymentIntent has a `latest_charge` field, expandable into the Charge [VERIFIED: https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11].

### 1.3 The PaymentIntent and SetupIntent state machine

Statuses of a PaymentIntent, from the API reference: "one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `requires_capture`, `canceled`, or `succeeded`" [VERIFIED: https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11].

| Status | Meaning, per Stripe's lifecycle page |
| --- | --- |
| `requires_payment_method` | Initial state "until you attach a payment method". Also where a **failed attempt returns**: "If the payment attempt fails (for example, due to a decline), the PaymentIntent's status returns to `requires_payment_method` so that the payment can be retried." |
| `requires_confirmation` | "ready to confirm. Most integrations skip this state because they submit payment method information when the payment is confirmed." |
| `requires_action` | "If the payment requires additional actions, such as authenticating with 3D Secure" |
| `processing` | "Occurs after required actions are handled and the payment uses an asynchronous payment method, such as bank debits. These types of payment methods can take up to a few days to process." |
| `requires_capture` | Reached instead of `processing`/`succeeded` "If you're separately authorizing and capturing funds" |
| `succeeded` | "the corresponding payment flow is complete. The funds are now in your account and you can confidently fulfill the order." |
| `canceled` | "You can cancel a PaymentIntent before it reaches a `processing` or `succeeded` state. Cancellation invalidates the PaymentIntent for future payment attempts, releases any held funds, and can't be undone." |

All rows: [VERIFIED: https://docs.stripe.com/payments/paymentintents/lifecycle.md, n.d., accessed 2026-11].

Further documented properties of the machine:

- **There is no `failed` state.** The 2020 post: "There's no failed state because if a single payment attempt fails, the PaymentIntent goes back to the requires_payment_method state so that the customer can try again with a different payment method. This is convenient because the same object created server-side can be used repeatedly on the client." [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15]. The failure itself is recorded in `last_payment_error` on the PaymentIntent and as a failed Charge [VERIFIED: https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11].
- **Exceptions to "cannot cancel while processing"**: a PaymentIntent in `processing` can be cancelled for ACH, ACSS, AU BECS, Bacs, NZ BECS and SEPA debit, "However, cancellation might fail due to a limited and varying cancellation time window." Also: "PaymentIntents might also automatically transition to `canceled` if they're confirmed too many times." [VERIFIED: https://docs.stripe.com/payments/paymentintents/lifecycle.md, n.d., accessed 2026-11].
- **Cancellation reasons** distinguish the integrator (`duplicate`, `fraudulent`, `requested_by_customer`, `abandoned`) from Stripe (`failed_invoice`, `void_invoice`, `automatic`, `expired`) [VERIFIED: https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11].
- **Status names were themselves versioned**: "Versions of the API before 2019-02-11 show `requires_source` instead of `requires_payment_method` and `requires_source_action` instead of `requires_action`." [VERIFIED: https://docs.stripe.com/payments/paymentintents/lifecycle.md, n.d., accessed 2026-11]. A useful small example for chapter 19: the state names of the central object changed once, and the old names are still served to old versions [ASSUMPTION/JUDGEMENT].
- **SetupIntent shares the machine**: "Both Payment Intents and Setup Intents go through the same set of states." A SetupIntent collects and saves "payment method details for future use without creating a charge"; with cards it uses 3DS "to authenticate a payment method without charging it, then create a mandate or agreement for future charges" [VERIFIED: https://docs.stripe.com/payments/paymentintents/lifecycle.md, n.d., accessed 2026-11].
- **One PaymentIntent per cart**: "Each PaymentIntent typically correlates with a single shopping cart or customer session in your application"; create it "as soon as you know the amount"; "attempt to reuse the same PaymentIntent instead of creating a new one"; and "provide an idempotency key to prevent the creation of duplicate PaymentIntents for the same purchase. This key is typically based on the ID that you associate with the cart or customer session" [VERIFIED: https://docs.stripe.com/payments/payment-intents.md, n.d., accessed 2026-11].

### 1.4 Confirmation, client secret, next actions, capture

- **Create then confirm**: "Building an integration with the Payment Intents API involves two actions: creating and confirming a PaymentIntent." Confirming "indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment" [VERIFIED: https://docs.stripe.com/payments/payment-intents.md, n.d., accessed 2026-11].
- **Client secret**: "a key that's unique to the individual PaymentIntent", which "lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)". The server creates the intent and passes only the client secret to the browser, where Stripe.js confirms it with the publishable key [VERIFIED: same].
- **`confirmation_method`**: `automatic` (default) — "PaymentIntent can be confirmed using a publishable key. After `next_action`s are handled, no additional confirmation is required"; `manual` — "All payment attempts must be made using a secret key. The PaymentIntent returns to the `requires_confirmation` state after handling `next_action`s" [VERIFIED: https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11].
- **`next_action`** is a nullable object on the intent that tells the client what to do; the 2020 post gives the range "from a generic redirect_to_url … to a very payment-method-specific action like oxxo_display_details, which provides information for you to generate an OXXO voucher" [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15].
- **Capture method**: `automatic_async` is the documented default — "Stripe asynchronously captures funds when the customer authorizes the payment. Recommended over `capture_method=automatic` due to improved latency"; `manual` places a hold "but don't capture the funds until later" [VERIFIED: https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11]. That the default capture is asynchronous means that even a successful card payment's Charge may not carry its balance transaction when the API returns [ASSUMPTION/JUDGEMENT].
- **Authorization validity (chapter 02)**: for online card payments the hold is "typically on hold for 7 days for online payments and 2 days for in-person Terminal payments"; Stripe's table gives Visa 5 days for a customer-initiated transaction, with the note "The exact authorization window is 4 days and 18 hours, to allow time for clearing processes"; the field `payment_method_details.card.capture_before` on the Charge "indicates when the authorization expires"; if it expires "the funds are released and the payment status changes to `canceled`" [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md, n.d., accessed 2026-11]. ⚠ Network windows change.
- **CIT and MIT (chapter 02)**: Stripe documents the network distinction between customer-initiated and merchant-initiated transactions and exposes it through `setup_future_usage` and `off_session` on the intent: "When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as SCA" [VERIFIED: https://docs.stripe.com/payments/cits-and-mits.md and https://docs.stripe.com/api/payment_intents/object.md, n.d., accessed 2026-11]. The `2026-10-28.endive` release adds explicit "card-on-file usage" indicators when saving or charging cards [VERIFIED: https://docs.stripe.com/changelog/endive.md, published 2026-10-28].
- **Synchronous response versus webhook outcome**: "Don't attempt to handle order fulfillment on the client side because customers can leave the page after payment is complete but before the fulfillment process initiates. Instead, use webhooks to monitor the `payment_intent.succeeded` event". Polling is allowed "but it's much less reliable and might trigger rate limits" [VERIFIED: https://docs.stripe.com/payments/payment-intents/verifying-status.md, n.d., accessed 2026-11].

### 1.5 PaymentMethod, dynamic payment methods, and Checkout Sessions as the recommended surface (chapters 07, 08)

- **PaymentMethod** "replaces the existing Tokens and Sources APIs as the recommended way for integrations to collect and store payment information" [VERIFIED: https://docs.stripe.com/payments/payment-methods/transitioning.md, n.d., accessed 2026-11]. The design intent: "Unlike a Source, there is no state or data specific to the particular transaction type captured on a PaymentMethod object—you can think of it as an object that specifies how to process a payment request." The PaymentMethod is "the how", the PaymentIntent "the what" [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15].
- **`payment_method_details`**: "a polymorphic, typed hash on the Charge that contains payment-method-specific data", introduced to stop the top-level Charge growing; "Over time, we've standardized this design pattern and have applied it to other resources in the API" [VERIFIED: same]. This is where the abstraction leaks by design: method-specific fields live in a typed sub-object keyed by the method name [ASSUMPTION/JUDGEMENT].
- **Automatic (dynamic) payment methods became the default in API version 2023-08-16**: PaymentIntents and SetupIntents "now have dynamic `automatic_payment_methods` enabled by default … The previous default was to accept only card payments when both `payment_method_types` and `automatic_payment_methods` weren't specified." Side effects: a `return_url` is required on confirmation unless `off_session=true`, and `error_on_requires_action` cannot be combined with it [VERIFIED: https://docs.stripe.com/changelog/2023-08-16/automatic-payment-methods.md, published 2023-08-16]. The escape hatch from 2020 (`error_on_requires_action`) is therefore now opt-in through `payment_method_types` [ASSUMPTION/JUDGEMENT].
- **Dynamic payment methods** let the merchant "configure payment methods settings from the Dashboard—no code required"; Stripe applies "AI models based on more than 100 signals to dynamically determine which payment methods are eligible and how to display them" [VERIFIED: https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md, n.d., accessed 2026-11]. Stripe's site navigation advertises "Payment methods: Access to 125+" [VERIFIED: https://stripe.com/blog/idempotency (site navigation), accessed 2026-11] ⚠.
- ⚠ **Checkout Sessions is now the recommended API, above PaymentIntents.** "The Checkout Sessions API is the recommended API for most developers. The Payment Intents API is a lower-level API that you can use to build your own checkout or payments, but it requires significantly more code and ongoing maintenance." Checkout Sessions can be rendered as a full hosted page, an embedded form, or with Elements in the merchant's own UI (`ui_mode: "elements"`, earlier `custom`); a session expires automatically after 24 hours, a PaymentIntent has "No automatic expiration" [VERIFIED: https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md, n.d., accessed 2026-11]. The Elements-with-Checkout-Sessions mode shipped in `2025-03-31.basil`: "You can now specify a `ui_mode` of `custom` to use Elements and Checkout Sessions to design your own checkout page" [VERIFIED: https://docs.stripe.com/changelog/basil.md, published 2025-03-31].
- The same pages carry a line addressed to coding agents: "Don't use the Payment Intent API unless the user explicitly asks, because it requires significantly more code." [VERIFIED: https://docs.stripe.com/payments/payment-intents.md, n.d., accessed 2026-11]. Stripe is steering generated integrations toward the higher-level object [ASSUMPTION/JUDGEMENT].

The arc for chapter 08: Token+Charge (a request) → Source+Charge (two state machines) → PaymentIntent+PaymentMethod (one state machine for the payment) → Checkout Session (one state machine for the whole checkout: line items, tax, discounts, subscription, payment). Each step moved more state to the provider [ASSUMPTION/JUDGEMENT].

### 1.6 Refunds and disputes as objects (chapter 04)

- A **Refund** is its own object with its own status: "`pending`, `requires_action`, `succeeded`, `failed`, or `canceled`", and a `failure_reason` whose values include `lost_or_stolen_card`, `expired_or_canceled_card`, `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`, `merchant_request`, `unknown` [VERIFIED: https://docs.stripe.com/api/refunds/object.md, n.d., accessed 2026-11]. A refund can fail after the API accepted it; that is the documented shape of "refund as a new transaction that can fail" [ASSUMPTION/JUDGEMENT].
- A breaking change in `2025-03-31.basil`: "Partially capturing or canceling payments no longer creates a Refund" [VERIFIED: https://docs.stripe.com/changelog/basil.md, published 2025-03-31]. Before Basil, releasing the uncaptured remainder of an authorization was represented as a Refund object; since Basil a reversal of a hold and a refund of captured money are no longer the same object [ASSUMPTION/JUDGEMENT: the inference about the earlier behaviour is drawn from the change title; the detail page was not read].
- A **Dispute** has statuses `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `appeal_needs_response`, `appeal_under_review`, `won`, `lost`, `prevented` [VERIFIED: https://docs.stripe.com/api/disputes/object.md, n.d., accessed 2026-11]. The `warning_*` statuses model pre-dispute inquiries; the `appeal_*` statuses and the October 2026 addition "You can now stage or submit evidence when appealing an eligible dispute" show the object still gaining states [VERIFIED: https://docs.stripe.com/changelog/endive.md, published 2026-10-28].
- Balance Transactions gained "balances for refund and dispute prefunding" in May 2025 [VERIFIED: https://docs.stripe.com/changelog/basil.md, published 2025-05-28].

### Stripe vs Adyen (PART 1)

| Aspect | Stripe (documented) | Adyen (documented; see the Adyen brief) | What the difference suggests |
| --- | --- | --- | --- |
| Central object | A long-lived, retriable `PaymentIntent` with a status field; failed attempts return it to `requires_payment_method` [docs, accessed 2026-11] | A payment identified by `pspReference` with a `resultCode` on each response (`Authorised`, `Refused`, `Pending`, `Received`, `RedirectShopper`, `ChallengeShopper`, `PresentToShopper`, `Cancelled`, `Error`…) [VERIFIED: https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes.md, n.d., accessed 2026-11] | Stripe exposes a resource you poll or are notified about; Adyen exposes the result of a request plus later webhooks [ASSUMPTION/JUDGEMENT] |
| Recommended entry point | Checkout Sessions, above PaymentIntents [docs, accessed 2026-11] | "Sessions flow is the default integration that we recommend": one `/sessions` call; the Advanced flow is three calls (`/paymentMethods`, `/payments`, `/payments/details`) [VERIFIED: https://docs.adyen.com/online-payments/build-your-integration.md, n.d., accessed 2026-11] | Both converged on a server-created session that the client completes [ASSUMPTION/JUDGEMENT] |
| After authorization | `requires_capture` status on the same object; Refund and Dispute are separate objects | "Payment modifications": capture, cancel, refund, reversal, authorization adjustment, each a separate asynchronous request [VERIFIED: https://docs.adyen.com/online-payments/modify-payments.md, last modified 2026-11-17] | Adyen names the unknown-state case explicitly: a *reversal* is for "when you are not sure if the payment has been captured" [ASSUMPTION/JUDGEMENT] |
| Published design history | A 27-minute engineering essay with dates and admitted mistakes (2020) | Nothing comparable found in this session; the Adyen brief should confirm | Stripe documents *why*; for Adyen the model has to be read from the reference [ASSUMPTION/JUDGEMENT] |

**For readers new to payments.** *Authorization*: the issuing bank's promise to pay, which reserves funds but moves none. *Capture*: the merchant's instruction to actually collect an authorized amount. *3-D Secure*: the card networks' protocol by which the cardholder's bank authenticates the customer during an online payment. *Asynchronous payment method*: one where success is known hours or days after the customer acts (bank debits, vouchers), so the API cannot answer "paid" in the response.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) A payment object needs a state for "waiting for the customer" and one for "waiting for the network", and they are different states. (2) Modelling failure as a return to an earlier state, not a terminal state, keeps one object per order and makes "how many attempts" a property of one record. (3) Keeping the old object (`Charge`) underneath the new one is what made a two-year migration possible; consumers that read should not have to migrate when writers do. (4) A consumer that mirrors the state machine should store the provider's status verbatim and derive its own smaller vocabulary from it, because the provider adds states (see disputes) and has renamed them once.

---

## PART 2: Object model conventions and API design practice (chapter 17)

### 2.1 Conventions documented in the API reference

- **Prefixed object IDs.** IDs carry a type prefix: `pi_` (PaymentIntent), `ch_` (Charge), `cus_` (Customer), `pm_` (PaymentMethod), `acct_` (Account), `src_`, `card_` [VERIFIED: https://dev.to/4thzoa/designing-apis-for-humans-object-ids-3o5a, published 2022-08-30]; webhook endpoints `we_` and event destinations `ed_` [VERIFIED: https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11]. Key prefixes follow the same idea: `pk_test_`/`pk_live_`, `sk_test_`/`sk_live_`, `rk_test_`/`rk_live_`, `sk_org_`, and `whsec_` for webhook signing secrets [VERIFIED: https://docs.stripe.com/keys.md, n.d., accessed 2026-11]. Stripe's reference has no page that specifies the ID format (a guessed URL `docs.stripe.com/api/object_ids` returned 404); the only explanation found is the 2022 article below.
- **Every object names its type**: responses carry `"object": "charge"`, `"object": "list"` and so on [VERIFIED: https://docs.stripe.com/api/pagination.md, n.d., accessed 2026-11].
- **Expandable objects.** "Many objects allow you to request additional information as an expanded response by using the `expand` request parameter." Related objects are returned as IDs by default; `expand[]=customer` inlines them; nesting uses dots (`payment_intent.customer`) "up to a maximum depth of four levels"; on lists, paths start with `data.`; and "Performing deep expansions on numerous list requests might result in slower processing times" [VERIFIED: https://docs.stripe.com/api/expanding_objects.md, n.d., accessed 2026-11].
- **Cursor pagination.** List methods take `limit` (default 10, range 1–100), `starting_after` and `ending_before`, both object IDs; results come "in reverse chronological order"; the response is `{object: "list", data, has_more, url}` [VERIFIED: https://docs.stripe.com/api/pagination.md, n.d., accessed 2026-11]. `total_count` on lists was removed in Basil "because this is no longer a recommended integration pattern" [VERIFIED: https://docs.stripe.com/changelog/basil.md, published 2025-03-31].
- **Metadata.** "You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long." "Stripe doesn't use metadata—for example, we don't use it to authorize or decline a charge". Sensitive data must not be stored there [VERIFIED: https://docs.stripe.com/api/metadata.md, n.d., accessed 2026-11]. Stripe recommends metadata as the reconciliation hook after an ambiguous failure: "include a local identifier in its metadata so you can match an object received through a webhook to your local records" [VERIFIED: https://docs.stripe.com/error-low-level.md, n.d., accessed 2026-11].
- **Request encoding (v1).** Requests are form-encoded, responses JSON [VERIFIED: https://docs.stripe.com/api-v2-overview.md, n.d., accessed 2026-11].
- **Request IDs.** "Each API request has an associated request identifier", returned in the `Request-Id` header [VERIFIED: https://docs.stripe.com/api/request_ids.md, n.d., accessed 2026-11].

### 2.2 Error model and decline codes

- **HTTP status codes**: 400 bad request, 401 no valid key, **402 "The parameters were valid but the request failed"** (the card-declined case), 403 key lacks permission, 404, **409 "The request conflicts with another request (perhaps due to using the same idempotent key)"**, **424 "External Dependency Failed"**, 429 too many requests, 5xx "Something went wrong on Stripe's end. (These are rare.)" [VERIFIED: https://docs.stripe.com/api/errors.md, n.d., accessed 2026-11].
- **Error types**: `api_error`, `card_error`, `idempotency_error`, `invalid_request_error` [VERIFIED: same].
- **Error object attributes**: `type`, `code`, `decline_code`, `message` ("For card errors, these messages can be shown to your users"), `param`, `doc_url`, `request_log_url`, `charge`, `payment_intent`, `payment_method`, `setup_intent`, plus `advice_code`, `network_advice_code` ("a 2 digit code which indicates the advice given to merchant by the card network on how to proceed") and `network_decline_code` [VERIFIED: same]. The last three surface network-level retry guidance through the API; chapter 09 (optimization brief) should pick these up [ASSUMPTION/JUDGEMENT].
- **Decline codes** are Stripe's normalized vocabulary over issuer responses; the documentation table has about 75 rows [VERIFIED: https://docs.stripe.com/declines/codes.md, n.d., accessed 2026-11, row count by the analyst]. Examples: `insufficient_funds`; `do_not_honor` ("declined for an unknown reason"); `generic_decline` ("declined for an unknown reason or Stripe Radar or Adaptive Acceptance blocked the payment"). For `fraudulent` and `lost_card` the guidance is not to tell the customer: "present it in the same manner as `generic_decline`" [VERIFIED: same].
- August 2026 added "standardized error codes for authentication failures, expired payment methods, incorrect postal codes, and restricted payment methods across payment method types, countries, and regions" [VERIFIED: https://docs.stripe.com/changelog/dahlia.md, published 2026-08-26].

### 2.3 What Stripe has published about its API design practice

| Source | Author, date | What it establishes |
| --- | --- | --- |
| "Stripe's payments APIs: The first 10 years" | Michelle Bu, 2020-12-15 **(evidence age: 6 years)** | Design method: a small team, three months, "writing hypothetical integration guides to validate our concepts", including "for some payment methods we made up, like sending cash via carrier pigeon"; "Question every assumption underpinning existing APIs"; "An API product is more than just the API" |
| "APIs as infrastructure: future-proofing Stripe with versioning" | Brandur Leach, 2017-08-05 **(evidence age: 9 years)** | The only public description of the review process: "Outgoing changes are funneled through a lightweight API review process where they're written up in a brief supporting document and submitted to a mailing list." API resources are defined in a Ruby DSL |
| "How API changes flow into Stripe's developer products" | Mikael Mello and Anna Mason, 2026-06-15 | Current practice: "we've codified a set of design patterns that all APIs must follow. Before a PR can merge, a set of automated tests validate API changes against those patterns: API naming, field types, versioning considerations such as backwards compatibility, or constraints specific to products (e.g. reserved words in SDKs)"; an OpenAPI-based diff in the pull request; a pre-release review "for product architects" |
| "Designing APIs for humans: Object IDs" and "…: Error messages" | Paul Asjes, 2022-08-30 and 2022-09-14 **(evidence age: 4 years)** | Rationale for prefixed IDs and for error messages; published on the author's own dev.to account while he worked at Stripe, not on stripe.com |

Sources, in row order: [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15]; [VERIFIED: https://stripe.com/blog/api-versioning, published 2017-08-05]; [VERIFIED: https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products, published 2026-06-15]; [VERIFIED: https://dev.to/4thzoa/designing-apis-for-humans-object-ids-3o5a, published 2022-08-30, and https://dev.to/4thzoa/designing-apis-for-humans-error-messages-94p, published 2022-09-14].

From the object-ID article [VERIFIED: https://dev.to/4thzoa/designing-apis-for-humans-object-ids-3o5a, published 2022-08-30]:

- The structure is "Prefix" + "Randomly generated characters"; the reason given: "adding a prefix makes the ID human readable."
- A debugging example: a `cus_` ID passed where an `acct_` ID was required can be spotted without a lookup.
- "At Stripe we've gone so far as to develop an internal browser extension to automatically look up Stripe Objects based on their ID."
- Prefixes enable **polymorphic parameters**: `payment_method` on a PaymentIntent also accepts a Source (`src_`) or Card (`card_`) ID, so an old identifier keeps working in a new API.

**Dating note.** The versioning post's page shows "August 5, 2017" in both the visible byline and the structured data fetched in this session; some older citations give 15 August 2017. Use the date on the page [ASSUMPTION/JUDGEMENT on the older citations].

**Where the evidence stops.** Stripe has not published its API design guide, the criteria its reviewers apply, or who sits on the review. The 2017 sentence and the 2026 list of lint categories are the whole public record found. Anything more specific in the chapter must be labelled inference.

### 2.4 API v2

What it is: "The Stripe API provides two namespaces that contain different sets of endpoints: API v1: The `/v1` namespace includes most of the existing Stripe API today. API v2: The `/v2` namespace includes endpoints that use `/v2` design patterns." [VERIFIED: https://docs.stripe.com/api-v2-overview.md, n.d., accessed 2026-11]. It is a **parallel namespace, not a replacement**: "You can use any combination of APIs in the `/v1` or `/v2` namespace in the same integration" [VERIFIED: same].

| | API v1 | API v2 |
| --- | --- | --- |
| Request body | form-encoded | JSON |
| Version | account default, overridable by header | "All API requests to the API `/v2` namespace must include the `Stripe-Version` header" |
| Idempotency | replays the stored first response, including errors; 24 hours; `POST` only | retries failed work and returns an updated response; 30 days; `POST` and `DELETE` |
| Events | mostly snapshot events | thin events |
| Pagination | `starting_after` / `ending_before` object IDs, `has_more` | a `page` token; responses carry `previous_page_url` and `next_page_url`; "You can't change list filters after the first request" |
| List consistency | "Top-level lists are immediately consistent (with higher latency to render). Some sublists are eventually consistent." | "Lists are eventually consistent by default and lower-latency." |
| Related data | `expand` | "The `expand` parameter isn't supported"; some endpoints offer an `include` parameter |
| Metadata removal | set the value to an empty string | set the value to `null` |
| Request logs | Developers Dashboard and Workbench | "only … in Workbench" |

All rows: [VERIFIED: https://docs.stripe.com/api-v2-overview.md, n.d., accessed 2026-11].

Dated history and scope:

- "In 2024, Stripe introduced the v2 namespace to bring improved domain modeling and updated API semantics to our users. Internally, this meant an architectural shift in how we define and implement APIs, leveraging Protocol Buffers. Unlike v1, v2 APIs are defined by a separate internal DSL" [VERIFIED: https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products, published 2026-06-15]. This is a rare published statement about Stripe internals: v1 endpoints are declared in a Ruby DSL, v2 endpoints in protobuf service definitions, and both are compiled to OpenAPI.
- First public v2 endpoints: `/v2/core/events` in `2024-09-30.acacia` ("The Meters API is the first API to use thin events") and the Event Destinations v2 API in `2024-10-28.acacia` [VERIFIED: https://docs.stripe.com/changelog/acacia/2024-09-30/api-v2-thin-events.md, published 2024-09-30, and https://docs.stripe.com/changelog/acacia/2024-10-28/event-destinations-api.md, published 2024-10-28].
- A former Stripe engineer noticed it three months later: "what's available in V2 is currently very minimal (only events and event destinations), so integrations will still use V1 for almost everything". He also criticized what v2 kept: `POST` for everything and RPC-style actions such as `POST /v2/core/event_destinations/:id/enable` [WIDELY REPORTED: https://brandur.org/fragments/stripe-v2, 2024 — personal blog of Brandur Leach, former Stripe API engineer, fetched in this session, published 2024-12-28].
- ⚠ **Status as of November 2026**: v2 resources seen in the current docs and changelog are Core (Accounts, Account Links, Events, Event Destinations), Billing (meter event streams: "up to 10,000 events per second … live mode only"), Money Management (Outbound Payments, Outbound Setup Intents, Payout Methods, Payout Intents, Financial Addresses, Received Credits, Financial Accounts) and IAM activity logs [VERIFIED: https://docs.stripe.com/changelog.md, published 2026-10-28; https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api.md, n.d., accessed 2026-11]. **Payments are not in v2**: PaymentIntents, Charges, Refunds, Disputes, Checkout Sessions, Customers and Subscriptions remain v1 [VERIFIED by absence in the same pages; a complete v2 resource index was not found in this session]. "The Accounts v2 API is broadly available to Connect platforms, and to other users in preview" [VERIFIED: https://docs.stripe.com/api/v2/core/accounts.md, n.d., accessed 2026-11]. Several Money Management v2 APIs were still changing shape with breaking changes in the `2026-10-28.preview` channel [VERIFIED: https://docs.stripe.com/changelog.md, published 2026-10-28].
- The 2017 versioning post said of a major version: "Although we reserve the right to make use of this at some point, it's not likely to change for some time. … it's hard for us to imagine an API redesign that's important enough to justify this level of user impact." **(evidence age: 9 years; updated, not contradicted.)** Seven years later Stripe did introduce `/v2`, but as an additive namespace for new and remodelled resources, which avoids the forced re-integration the post warned against [VERIFIED for the quote: https://stripe.com/blog/api-versioning, published 2017-08-05; the reconciliation is ASSUMPTION/JUDGEMENT].

### Stripe vs Adyen (PART 2)

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Shape of the API | One API host with two namespaces (`/v1`, `/v2`) and one global object model | Several APIs, each with its own host and version number: e.g. `checkout-test.adyen.com/v68/payments`, `balanceplatform-api-test.adyen.com/bcl/v1/balanceAccounts`; "Most integrations use multiple Adyen APIs … Each API has a different version" [VERIFIED: https://docs.adyen.com/development-resources/versioning.md, last modified 2022-01-18] **(evidence age: 4 years by last-modified date)** | Stripe optimizes for one model learned once; Adyen for product families that evolve independently [ASSUMPTION/JUDGEMENT] |
| Identifier | Typed, prefixed IDs per object | `pspReference` per payment or modification (see Adyen brief) | Stripe IDs tell you the object type; Adyen's tell you the transaction [ASSUMPTION/JUDGEMENT] |
| Live endpoint | Same host for test and live; the key decides | Separate test and live hosts; live URLs carry a company-specific prefix ("a hex-encoded random part and your company name") [VERIFIED: https://docs.adyen.com/development-resources/live-endpoints.md, last modified 2024-01-18] | Adyen's routing to a merchant's environment is visible in the URL; Stripe's is hidden behind the key [ASSUMPTION/JUDGEMENT] |
| Machine-readable spec | `github.com/stripe/openapi` (v1 and v2, GA and preview) | `github.com/Adyen/adyen-openapi`, OpenAPI 3.1.0 [VERIFIED: https://raw.githubusercontent.com/Adyen/adyen-openapi/main/README.md, n.d., accessed 2026-11] | Both publish OpenAPI; see 6.5 for how SDKs are built from it |
| Published design rationale | Three engineering posts (2017, 2020, 2026) plus two employee articles (2022) | Not searched in depth here; the Adyen brief should state what exists | — |

**For readers new to payments.** *Decline code*: the provider's normalized reason an issuer refused a payment; the issuer's own two-character response code is behind it. *Issuer*: the bank that issued the customer's card and decides each authorization. *Expandable object*: a field that holds an ID by default and the full related object on request.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Typed ID prefixes cost nothing at creation and pay back in support, logs and polymorphic parameters; they are the cheapest transferable idea in this brief. (2) Returning IDs by default and objects on request is a latency decision: v2's move from `expand` to `include` and to eventually consistent lists says that rendering related objects was a real cost at Stripe's scale; the former Stripe engineer says so directly ("The purpose of the change is to make API requests faster"). (3) An error model needs separate fields for the machine (`code`, `decline_code`), the human (`message`), the form (`param`) and the support ticket (`request_log_url`). (4) A new namespace beside the old one is a third option between "never break" and "v2 replaces v1".

---

## PART 3: Idempotency and retries (chapter 18)

### 3.1 The 2017 design post

"Designing robust and predictable APIs with idempotency", Brandur Leach, 22 February 2017 [VERIFIED: https://stripe.com/blog/idempotency, published 2017-02-22]. **(evidence age: 9 years.)** The current reference confirms the mechanism for API v1 and links to this post; API v2 changes the replay semantics (3.3).

- The three failure cases: "The initial connection could fail as the client tries to connect to a server. The call could fail midway while the server is fulfilling the operation, leaving the work in limbo. The call could succeed, but the connection break before the server can tell its client about it."
- "Even the Stripe API and just one other server that's making requests to it comprise a distributed system."
- The mechanism: "a client generates a unique ID to identify just that operation and sends it up to the server along with the normal payload. The server receives the ID and correlates it with the state of the request on its end."
- What the server does in each case: on a connection failure "the server will see the ID for the first time, and process it normally"; "On a failure midway through an operation, the server picks up the work and carries it through. The exact behavior is heavily dependent on implementation, but if the previous operation was successfully rolled back by way of an ACID database, it'll be safe to retry it wholesale. Otherwise, state is recovered and the call is continued"; on a response failure "the server simply replies with a cached result of the successful operation."
- Scope: "The Stripe API implements idempotency keys on mutating endpoints (i.e. anything under POST in our case)" through the `Idempotency-Key` header.
- Client behaviour: exponential backoff ("waits proportionally to 2^n") plus random jitter against the "thundering herd problem"; "The Stripe Ruby library retries on failure automatically with an idempotency key using increasing backoff times and jitter."
- The three principles: handle failures "consistently" (retry), "safely" (idempotency keys), "responsibly" (backoff and jitter).

The post says nothing about how Stripe stores keys, fingerprints requests, or recovers a half-finished request. The often-cited implementation detail (an `idempotency_keys` table with `locked_at`, `request_params`, `response_code`, `response_body` and a `recovery_point`; "atomic phases" between "foreign state mutations"; a "completer" and a "reaper") comes from the same author's **personal** article, which builds a reference implementation for a demo app and says so: "Let's look at how to design idempotency keys for an API by building a reference implementation." It suggests reaping keys after "about 72 hours" [WIDELY REPORTED: https://brandur.org/idempotency-keys, 2017 — personal blog of a then-Stripe engineer, fetched in this session, published 2017-10-27] **(evidence age: 9 years)**. It is a design a Stripe engineer recommended, not a description of Stripe's system; the chapter must not present recovery points as Stripe's documented implementation [ASSUMPTION/JUDGEMENT].

### 3.2 Current documented behaviour, API v1

All from the API reference and the low-level error guide [VERIFIED: https://docs.stripe.com/api/idempotent_requests.md and https://docs.stripe.com/error-low-level.md, n.d., accessed 2026-11]:

- **Stored response, including errors**: "For API v1, Stripe saves the status code and body of the first request made with a given idempotency key after endpoint execution begins. Retries with the same key return the saved response, including `500` errors."
- **Key format**: "Idempotency keys are up to 255 characters long." Stripe suggests "V4 UUIDs, or another random string with enough entropy to avoid collisions" and warns: "Avoid using sensitive data (for example, email addresses or personal identifiers) as idempotency keys."
- **Retention**: keys can be removed "after they're at least 24 hours old. We generate a new request if a key is reused after the original is pruned." The error guide: "Stripe retains keys for at least 24 hours and can remove them after that. Reusing a key after it's removed can execute a new request."
- **Parameter mismatch**: "The idempotency layer compares incoming parameters to those of the original request and errors if they're not the same to prevent accidental misuse." The error type is `idempotency_error`: "an `Idempotency-Key` is re-used on a request that does not match the first request's API endpoint and parameters" [VERIFIED: https://docs.stripe.com/api/errors.md, n.d., accessed 2026-11].
- **What is not stored**: "we save results only after the execution of an endpoint begins. If incoming parameters fail validation, or the request conflicts with another request that's executing concurrently, we don't save the idempotent result". Likewise an invalid key or a rate-limit rejection is not cached.
- **Concurrent duplicates**: a `409` "indicates that another request with the same key is still executing"; "wait and retry with that key and the same parameters. A new key can start a second operation."
- **Verbs**: "all `POST` requests accept idempotency keys. Don't send idempotency keys in `GET` and `DELETE` requests because it has no effect."
- **Replay marker**: "To identify a previously executed response that's being replayed from the server, look for the header `Idempotent-Replayed: true`."
- **Retry hint**: the `Stripe-Should-Retry` response header: `true` means retry with backoff, `false` means do not, absent means decide from the status code. "Stripe SDKs respect this header automatically."
- **The unknown outcome is named**: "Treat the outcome of a request that returns `500` as indeterminate: the operation might have produced side effects even though you received an error. Don't retry with a new idempotency key until you've resolved the original outcome. Retrieve the relevant object, inspect the request in the Dashboard, and use webhook events to reconcile what happened."
- **The 24-hour cliff**: "Limit retries of an unresolved operation to the first 24 hours after the original request … If the outcome is still unknown after that window, don't retry with either the old key or a new one. … If you can't establish what happened, contact Stripe support before repeating the operation."
- **Reconciliation after incidents**: "During incident recovery, Stripe attempts to reconcile failed operations and send webhook events for any objects created during reconciliation. The cached response doesn't change, and reconciliation isn't guaranteed to resolve every operation." So a v1 client can hold a cached 500 for a request whose object exists and whose `succeeded` event arrives later by webhook.
- **Choosing keys**: two strategies are documented: a random token "like UUID v4", or "Derive the key from a user-attached object, like the ID of a shopping cart. This provides a relatively straightforward way to protect against double submissions."

A 2025 Stripe developer-advocate post repeats the 24-hour figure ("Stripe recognizes the idempotency key for 24 hours") and pairs idempotency keys with a message queue and dead-letter queue on the integrator's side [VERIFIED: https://stripe.dev/blog/because-nobody-likes-being-charged-twice, published 2025-04-10].

### 3.3 Current documented behaviour, API v2

[VERIFIED: https://docs.stripe.com/api-v2-overview.md, n.d., accessed 2026-11]:

- "If the first request succeeded, the API skips making new changes and returns an updated response. If the first request failed (or partially failed), the API re-executes the failed requests and returns the new response. In the rare event that it's no longer possible for an idempotent replay to succeed, the API returns an error explaining why."
- A request is a replay if it uses "the same idempotency key for the same API", "in the scope of the same account or sandbox", "within 30 days of each other".
- "If no key is provided, Stripe automatically generates a UUID for you."
- "All `POST` and `DELETE` API v2 requests accept idempotency keys and behave idempotently."

| | v1 | v2 |
| --- | --- | --- |
| Window | at least 24 hours | 30 days |
| Same key, first attempt failed | returns the saved error, "even if it was an error" | "attempts to retry any failed requests without producing side effects … and provide an updated response" |
| Response on replay | the stored bytes | an *updated* response |
| Verbs | `POST` | `POST`, `DELETE` |

[VERIFIED: same]. The v2 semantics are what the 2017 post described as the ideal ("the server picks up the work and carries it through") and what v1 never did: v1 stores an answer, v2 converges an operation [ASSUMPTION/JUDGEMENT]. The former Stripe engineer makes the same reading: in v1 "The idempotency layer dumbly returned whatever canned response had been recorded on the initial go around (including internal server errors), so users wouldn't get closure on what exactly happened" [WIDELY REPORTED: https://brandur.org/fragments/stripe-v2, 2024 — personal blog of a former Stripe engineer]. Because payments are still on v1, the 24-hour replay-the-error behaviour is what governs "charge this card" in November 2026 [ASSUMPTION/JUDGEMENT].

### 3.4 SDK automatic retries

- "Stripe SDKs can generate idempotency keys and retry requests automatically. Retry defaults depend on the SDK, version, and how you construct the client. Retries use exponential backoff" [VERIFIED: https://docs.stripe.com/error-low-level.md, n.d., accessed 2026-11].
- ⚠ stripe-node: "As of v13 stripe-node will automatically do one reattempt for failed requests that are safe to retry"; the configuration table lists `maxNetworkRetries` default 1 [VERIFIED: https://raw.githubusercontent.com/stripe/stripe-node/master/README.md, n.d., accessed 2026-11]. Defaults for the other SDKs were not checked.
- SDK retries do **not** cover rate-limit 429s but do cover lock-timeout 429s: "unlike rate limiting errors, the automatic retry mechanisms built into the Stripe SDKs retry `429`s caused by lock timeouts" [VERIFIED: https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11].
- An SDK-generated key lives only inside one SDK call: "If your application retries across separate SDK calls or process restarts, generate and persist a key for the operation and supply it to every attempt." [VERIFIED: https://docs.stripe.com/error-low-level.md, n.d., accessed 2026-11].

### 3.5 Idempotency is not the only guard

- Stripe lists "No double charges" and "No idempotency key issues" among the advantages of PaymentIntents [VERIFIED: https://docs.stripe.com/payments/payment-intents.md, n.d., accessed 2026-11]: confirming the same intent twice does not charge twice, because the state machine refuses the second transition [ASSUMPTION/JUDGEMENT on the mechanism].
- Object locks: "The Stripe API locks objects on some operations so that concurrent workloads don't interfere and produce an inconsistent result"; contention returns HTTP 429 with code `lock_timeout`, and "Stripe doesn't process these failed requests, which means they're not assigned a request ID" [VERIFIED: https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11].

### Stripe vs Adyen (PART 3)

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Header, key length | `Idempotency-Key`, up to 255 characters | `idempotency-key`, "maximum of 64 characters" | — |
| Retention | v1: at least 24 hours; v2: 30 days | "Idempotency keys are valid for a period of 7 to 14 days after first submission" | Adyen's window is 7–14 times Stripe v1's; a retry job that runs the next day is safe on Adyen and at the edge on Stripe v1 [ASSUMPTION/JUDGEMENT] |
| Scope | account (v2: "account or sandbox") | "Keys are stored at a company account level" | — |
| In-flight duplicate | HTTP 409 | "HTTP 422 – Unprocessable Entity or HTTP 409 - Conflict … error code 704: 'request already processed or in progress'" | — |
| Retry signal | `Stripe-Should-Retry` header; `Idempotent-Replayed: true` on replays | response header `transient-error: true`; the `idempotency-key` header is echoed back | Both tell the client in a header whether to retry [ASSUMPTION/JUDGEMENT] |
| Store unavailable | not documented | "Adyen must retain a consistent, stateful data store … In the unlikely event that this data store should become unavailable, the API returns an HTTP 503 … error code 703" | Adyen documents that it fails closed when the idempotency store is down; Stripe publishes nothing on this [ASSUMPTION/JUDGEMENT] |
| Second line of defence | PaymentIntent state machine, object locks | "The accounting rules in the Adyen payments platform take care of most potential double-processing issues": captures cannot exceed the authorized amount; total refunds cannot exceed the captured amount | Both back the key with a business invariant on the payment itself [ASSUMPTION/JUDGEMENT] |
| Published design | 2017 engineering post | none found in this session | — |

Adyen column: [VERIFIED: https://docs.adyen.com/development-resources/api-idempotency.md, last modified 2020-07-30] **(evidence age: 6 years by last-modified date; the page is live documentation)**.

**For readers new to payments.** *Idempotency key*: a client-chosen identifier that lets a server recognize a retry of the same operation. *Unknown outcome*: the state after a timeout or 5xx in which the client cannot tell whether money moved. *Double charge*: two captures for one purchase, usually caused by retrying an unknown outcome without a key.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) "Replay the stored response" and "drive the operation to completion" are two different contracts; a builder must choose and document one. (2) The retention window is part of the contract: any retry mechanism (queue redelivery, cron, a human) that can fire after the window is a double-charge path. (3) Deriving the key from business identity (cart, invoice, renewal period) protects against a class of duplicates that a random key generated per attempt cannot. (4) Not caching validation failures and rate-limit rejections is correct and necessary: otherwise a client that fixed its request could never succeed with the same key. (5) The cached-500 case means the API response is not the last word; the event stream is.

---

## PART 4: API versioning (chapter 19)

### 4.1 The 2017 design: rolling versions, account pinning, version change modules

"APIs as infrastructure: future-proofing Stripe with versioning", Brandur Leach [VERIFIED: https://stripe.com/blog/api-versioning, published 2017-08-05]. **(evidence age: 9 years.)** The pinning model is confirmed by current docs; the release cadence was replaced in 2024 (4.2); SDK pinning was added in 2023 (4.4); the internal mechanism has not been re-described since, except that v2 stores version differences as "patch files" (4.5).

- The stance: "Just like a power company shouldn't change its voltage every two years, we believe that our users should be able to trust that a web API will be as stable as possible." And: "To date, we've maintained compatibility with every version of our API since the company's inception in 2011."
- Against big-bang versions: changes between `v1`, `v2`, `v3` are "so big and so impactful for users that it's almost as painful as re-integrating from scratch", and providers end up "retiring API versions and by extension cutting those users off, or maintaining the old versions forever at considerable cost."
- **Rolling, dated versions**: "we implement versioning with rolling versions that are named with the date they're released (for example, 2017-05-24). Although backwards-incompatible, each one contains a small set of changes".
- **Account pinning**: "The first time a user makes an API request, their account is automatically pinned to the most recent version available, and from then on, every API call they make is assigned that version implicitly." Override per request with the `Stripe-Version` header, or upgrade the pin in the dashboard.
- Scale by 2017: "almost a hundred backwards-incompatible upgrades over the past six years."
- **API resources**: "Every possible response from the Stripe API is codified by a class that we call an API resource", defined in a DSL and "written so that the structure they describe is what we'd expect back from the current version of the API."
- **Version change modules**: "When we need to make a backwards-incompatible change, we encapsulate it in a version change module which defines documentation about the change, a transformation, and the set of API resource types that are eligible to be modified". Modules are listed per version in a master list.
- **Walking backwards**: the API "initially formats data by describing an API resource at the current version, then determines a target API version from one of: A `Stripe-Version` header if one was supplied. The version of an authorized OAuth application if the request is made on the user's behalf. The user's pinned version … It then walks back through time and applies each version change module that finds along the way until that target version is reached."
- **Changes that cannot be encapsulated**: modules annotated `has_side_effects` whose transformation is a no-op, checked elsewhere in code with `VersionChanges.active?(…)`. "This reduced encapsulation makes changes with side effects more complex to maintain, so we try to avoid them."
- **Generated artefacts**: "our API changelog is programmatically generated and receives updates as soon as our services are deployed with a new version", and the API reference "notices who is logged in and annotates fields based on their account API version."
- **The cost, stated**: "Providing extensive backwards compatibility isn't free; every new version is more code to understand and maintain. … given enough time dozens of checks on version changes that can't be encapsulated cleanly will be littered throughout the project, making it slower, less readable, and more brittle."
- **Retirement was expected**: "we expect to eventually start retiring our older API versions."
- Principles: upgrades should be "Lightweight" and versioning "First-class".

Whether Stripe has since retired any API version is not stated on any page fetched. The current webhook documentation still uses an account pinned to `2015-02-16` as its example of an old version, which suggests versions of that age are still served [VERIFIED for the example: https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11; the suggestion is ASSUMPTION/JUDGEMENT].

### 4.2 The 2024 release process: named majors, monthly additive releases

"Introducing Stripe's new API release process", Michael Glukhovsky and Wissam Abirached [VERIFIED: https://stripe.com/blog/introducing-stripes-new-api-release-process, published 2024-10-01]:

- The old practice: "Historically, we've released new API features as soon as they're ready for production—regardless of whether they're backward-compatible or not."
- The customer problem: "it would be easier to plan your engineering roadmap if you knew when we were going to make updates to our API."
- The new cadence: "twice-yearly major updates with monthly feature enhancements". "Each semiannual major release—like Acacia—includes breaking changes and is named after a plant". "Each monthly release adds new features without breaking changes. Monthly releases continue to use the same name as the last major release".
- The escape clause (footnote): "We may introduce an out-of-cycle breaking change if we determine that your integration would be severely impacted without it … the major release would have a new name".
- SDKs: "Every release includes a new SDK for each supported language … each SDK version is directly associated with an API release".

The version string is `YYYY-MM-DD.name`. Releases to date, read from the changelog in this session [VERIFIED: https://docs.stripe.com/changelog.md and the per-release pages, published 2026-10-28]:

| Major | First version | Monthly versions seen | Breaking-change rows on the release page (analyst's count, includes preview-channel rows) |
| --- | --- | --- | --- |
| Acacia | `2024-09-30.acacia` | 2024-10-28, 11-20, 12-18, 2025-01-27, 02-24 | 4 |
| Basil | `2025-03-31.basil` | 2025-04-30, 05-28, 06-30, 07-30, 08-27 | 33 |
| Clover | `2025-09-30.clover` | 2025-10-29, 11-17, 12-15, 2026-01-28, 02-25 | 32 |
| Dahlia | `2026-03-25.dahlia` | 2026-04-22, 05-27, 06-24, 07-29, 08-26 | 34 |
| Endive | `2026-09-30.endive` | 2026-10-28 | 47 |

⚠ **Current version as of 17 November 2026: `2026-10-28.endive`** ("The current version is 2026-10-28.endive") [VERIFIED: https://docs.stripe.com/api/versioning.md, n.d., accessed 2026-11]. Majors have landed at the end of March and the end of September every year since the scheme began; the names run alphabetically [VERIFIED from the table; the alphabetical rule is the analyst's observation, ASSUMPTION/JUDGEMENT].

**A second channel was added in 2025.** "We're launching a new category of API versions, which give early access to upcoming features ahead of their General Availability (GA) launches." Preview versions are named `2025-04-30.preview` instead of `2025-04-30.basil`; "each new public preview API version may contain breaking changes"; beta SDKs target them [VERIFIED: https://stripe.dev/blog/introducing-stripes-new-public-preview-release-channel, published 2025-05-07]. Release phases are now private preview, "frontier" (self-serve, fast-changing APIs), public preview and GA; for GA: "No breaking changes expected; any future changes handled through API version upgrades" [VERIFIED: https://docs.stripe.com/release-phases.md, n.d., accessed 2026-11]. There are therefore three axes on a Stripe API surface in 2026: namespace (v1, v2), version (dated, named), and channel (GA, preview) [ASSUMPTION/JUDGEMENT].

### 4.3 What a breaking release looked like: Basil (31 March 2025)

"This version introduces a significant number of breaking changes." [VERIFIED: https://docs.stripe.com/changelog/basil.md, published 2025-03-31]. From the same page:

- **Billing and Invoicing**: "We removed or reorganized a number of capabilities, including legacy usage-based billing and a migration from the Upcoming Invoice API to the Create Preview API." Individual rows: "Adds subscription item-level billing periods and removes subscription-level periods"; "Invoicing resources now specify how they were generated" (a new `parent` field); "Replaces top-level price fields with improved price modeling on Invoice Items and Invoice Line Items"; "Replaces top-level tax-related properties with improved tax modeling on Invoices, Invoice Line Items, and Credit Note Line Items"; "Adds support for multiple (partial) payments on invoices"; "Removes legacy usage-based billing"; "Removes coupon and promotion code parameters with stackable discounts".
- **All products**: "Total counts no longer supported on lists".
- **Checkout**: "Checkout Sessions for subscriptions now postpone creation of subscriptions until after the user completes payment—this both improves latency on all Checkout Session API calls and fixes a common bug where customers couldn't modify billing details after the first payment attempt."
- **Payments**: "Partially capturing or canceling payments no longer creates a Refund"; "Removes manual capture method for Interac cards".
- **Stripe.js**: "Updates the default layout for Payment Element" is listed as breaking: a visual default is treated as a contract.

The Invoice changes are the best worked example for the "Version Cliff": an integrator who read `invoice.subscription`-style top-level fields, tax amounts or the upcoming-invoice endpoint had to change code to move from Acacia to Basil; one who stayed pinned to Acacia kept the old shape [ASSUMPTION/JUDGEMENT]. The post-2024 scheme concentrates breaking changes into two dates a year, which makes each major larger than a pre-2024 dated version was: compare Basil's 33 rows with the 2017 description of versions that "each … contains a small set of changes" [ASSUMPTION/JUDGEMENT].

### 4.4 Pinning today: account default, header, SDK, webhook endpoint

- **Account default**: "Requests made with curl use your Stripe account's default API version (controlled in Workbench) unless you override it by setting the `Stripe-Version` header." Stripe now advises against relying on it: "Make sure that you specify the API version that you're integrating against in your code instead of relying on your account's default API version" [VERIFIED: https://docs.stripe.com/api/versioning.md and https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11].
- **SDK pinning (2023)**: "When you use a server-side SDK, your API calls to Stripe use the API version that was current when the SDK was released." This began with stripe-node v12 (changelog dated 2023-04-06) and stripe-ruby v9, stripe-python v6 and stripe-php v11 (all dated 2023-08-16); earlier SDK versions "use your account's default API version". Java, Go and .NET are fixed by construction: "Because Java is a strongly-typed programming language, the API version used in the SDK is *fixed*", and overriding is discouraged because "the response objects might not match the strong types in the SDK" [VERIFIED: https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11]. The 2017 model (the account is the pin) has in practice become "the dependency version is the pin" for SDK users [ASSUMPTION/JUDGEMENT].
- **`/v2` requires an explicit version** on every request [VERIFIED: https://docs.stripe.com/api-v2-overview.md, n.d., accessed 2026-11].
- **Webhook payload version**: "Webhook events also use your account's default API version unless you set an API version during endpoint creation." An event's shape is frozen at creation: "The API version in your account settings when the event occurs dictates the API version, and therefore the structure of an Event sent to your destination. … You can't change Event objects after creation." A per-request `Stripe-Version` override does not change the version of the events that request generates [VERIFIED: https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11].
- **Snapshot destinations carry their own version**: `snapshot_api_version`, which "You can set … only when you create an event destination"; an account can have "up to three uniquely versioned snapshot event destinations" [VERIFIED: https://docs.stripe.com/upgrades.md and https://docs.stripe.com/events/how-events-work.md, n.d., accessed 2026-11].
- **The documented webhook upgrade procedure** is a two-endpoint cut-over: create a second endpoint on the new version with a distinguishing query parameter (for example `?version=2024-04-10`); for a while "every event is sent twice: once with the old API version and once with the new one"; process one and acknowledge the other; to keep a rollback path, return 400 on the old endpoint so that "Stripe automatically resends all the events" if you revert; then disable the old endpoint [VERIFIED: https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11].
- **Thin events remove this step**: "Thin event payloads are unversioned" [VERIFIED: same].

### 4.5 Upgrade tooling

- **Workbench** shows "which API versions your integration uses" and "recommended API upgrades" on its Overview tab [VERIFIED: https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11; https://stripe.com/blog/workbench-a-new-way-to-debug-monitor-and-grow-your-stripe-integration, published 2024-08-19].
- **Changelog**: redesigned in October 2024 to give "a clear explanation for each major release", per-change upgrade guidance and filters; each change is tagged Breaking or Non-breaking with affected products [VERIFIED: https://stripe.com/blog/introducing-stripes-new-api-release-process, published 2024-10-01; https://docs.stripe.com/changelog.md, published 2026-10-28].
- **Sandboxes for upgrade rehearsal**: a Stripe developer-advocate post recommends creating a sandbox to test a new version before upgrading the account; its screenshot shows an account "almost 2 years older than the latest" [VERIFIED: https://stripe.dev/blog/prepare-for-api-upgrades, published 2024-10-24].
- **Internal tooling (2026)**: "In the v2 namespace, all API changes are stored on disk and easily reproducible from the beginning of history. This allows us to generate snapshots of the API surface … for any point in time." For v1 this is harder: "Due to the historical architecture of the v1 platform, it's not trivial to regenerate descriptions for non-current API versions. Today, when a new API version is released, we store the current OpenAPI spec as the canonical description of v1 APIs for that version." In pull requests for v2, "we also detect and display changes to past API versions (if applicable), a feature that has been especially helpful for catching inadvertent changes to older API versions." [VERIFIED: https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products, published 2026-06-15]. This is the only post-2017 statement found on how Stripe keeps old versions correct.

### Stripe vs Adyen (PART 4)

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Where the version lives | A header (`Stripe-Version`), an account default, or the SDK version; one dated version spans the whole API | In the URL, per API: "Each API URL contains a version suffix starting with either 'v' or 'V' character followed by a whole number"; e.g. Checkout v68, Account v6, Balance Platform v1 in the page's examples | A Stripe integrator upgrades everything at once; an Adyen integrator upgrades one API at a time and can see the version in every request line [ASSUMPTION/JUDGEMENT] |
| Default for a new integrator | Implicit pin on first request | No implicit version: the caller writes it in the URL | Adyen cannot have a "what version am I on?" problem; Stripe built Workbench partly to answer it [ASSUMPTION/JUDGEMENT] |
| Additive change | Monthly releases with no breaking changes | "we follow the API expand-contract pattern to add new elements without changing the version"; for "classic" APIs (Payment, Recurring, Payout, BinLookup) even an added optional response field is breaking | — |
| Breaking change | A new named major, twice a year | "we release a new API version"; numbers may be skipped | — |
| Tooling | Changelog with filters; Workbench | "API Diff Tool to compare any two versions of an API" | — |
| Published internals | Version change modules (2017); patch files for v2 (2026) | None found on this page | — |

Adyen column: [VERIFIED: https://docs.adyen.com/development-resources/versioning.md, last modified 2022-01-18] **(evidence age: 4 years by last-modified date)**. Adyen's deprecation and sunset practice was not found on that page; the Adyen brief should cover it.

**For readers new to payments.** *Version pinning*: fixing the API behaviour an integration sees so that provider-side changes cannot break it. *Breaking change*: a change after which previously correct client code can fail (a removed field, a changed type, a new required parameter, a new enum value the client must handle). *Deprecation*: the provider's announcement that something will stop working.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Transforming responses backwards from "current" keeps old versions out of the core code path, at the cost of a growing chain of transformations and of side-effecting changes that leak. (2) Events are versioned at creation, so the webhook version and the request version can differ inside one integration; this is the most common source of "the field is missing" incidents and the reason thin events exist. (3) Tying the SDK version to the API version converts an invisible account setting into a visible dependency bump, reviewable in a pull request. (4) Concentrating breaking changes twice a year trades many small upgrades for two large ones; an integrator should budget for them.

---

## PART 5: Webhooks and events (chapter 20)

### 5.1 The Event object and the two formats

- "When the state of another API resource changes, Stripe creates an `Event` object that contains all the relevant information associated with that action, including the affected API resource." "Some actions trigger multiple events." "You can access events through the Retrieve Event API for 30 days." [VERIFIED: https://docs.stripe.com/api/events.md, n.d., accessed 2026-11].
- **Snapshot events** deliver "the complete `Event` object, including an eventually-consistent snapshot of the updated resource at the time the event was generated. Because this snapshot can be stale by the time your application processes it, fetch the latest version of the resource from the API before acting on the data." They are "versioned by API version" and include `previous_attributes` [VERIFIED: https://docs.stripe.com/events/how-events-work.md, n.d., accessed 2026-11].
- **Thin events** send "a lightweight notification containing only identifying information": `type` (for example `v2.core.account.updated`), `id`, `created`, and `related_object` (ID, type and API URL), plus a `reason`. The receiver then fetches the full event from `/v2/core/events` (which adds `data` and a `changes` hash) or the current object [VERIFIED: same].

| | Snapshot events | Thin events |
| --- | --- | --- |
| Payload | "Large: Includes a snapshot of the API object" | "Small: Includes an ID of the API object" |
| Versioning | "Versioned by API version" | "Unversioned, allowing you to upgrade your integration without changing your event destination configuration" |
| SDK typing | "Untyped" | "Typed" |
| API | Events v1 | Events v2 |

[VERIFIED: https://docs.stripe.com/events/how-events-work.md, n.d., accessed 2026-11].

- ⚠ **Recommendation as of November 2026**: "For new integrations, use thin events." The destination-creation flow lists "Thin (recommended) or Snapshot" [VERIFIED: https://docs.stripe.com/events/how-events-work.md and https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11]. The docs say "Both API v1 and API v2 resources generate thin events" [VERIFIED: same], but a June 2026 Stripe post still offered "early access to thin events for v1 resources" by form [VERIFIED: https://stripe.dev/blog/event-notification-handlers-thin-events, published 2026-06-24]. Which v1 event types (in particular `payment_intent.*`) have GA thin equivalents today was not verified; writers should say thin events are the stated direction and check the thin event catalog before claiming coverage of payment events.
- History: thin events first shipped on 2024-09-30 for the Meters API only [VERIFIED: https://docs.stripe.com/changelog/acacia/2024-09-30/api-v2-thin-events.md, published 2024-09-30]. The stated motive: "Because the shape of events are tied to a specific API version, upgrading either your event destination or SDK (especially in strongly typed languages) can lead to unexpected runtime errors. Stripe's solution to the maintenance problem is thin events, which are unversioned JSON payloads." [VERIFIED: https://stripe.dev/blog/event-notification-handlers-thin-events, published 2026-06-24].

### 5.2 The delivery contract

All from the webhook and events documentation [VERIFIED: https://docs.stripe.com/webhooks.md and https://docs.stripe.com/events/how-events-work.md, n.d., accessed 2026-11]:

- **Retry window**: "Stripe attempts to deliver events to your destination for up to three days with an exponential back off in live mode." "We retry event deliveries created in a sandbox three times over the course of a few hours." The exact intervals are not published; the next retry time is shown per delivery in the Dashboard.
- **Acknowledgement**: the endpoint "must quickly return a successful status code (`2xx`) before any complex logic that could cause a timeout. For example, you must return a `200` response before updating a customer's invoice as paid in your accounting system." No timeout value in seconds appears on the pages fetched.
- **Ordering**: "Stripe doesn't guarantee the delivery of events in the order that they're generated." And: "Snapshot events record `created` in seconds, so distinct events can share a timestamp. Don't use `created` to determine event order or whether you've already processed an event."
- **Duplicates (at-least-once)**: "Webhook endpoints might occasionally receive the same event more than once. You can guard against duplicated event receipts by logging the event IDs you've processed". A second kind of duplicate: "In some cases, two separate Event objects are generated and sent. To identify these duplicates, use the ID of the object in `data.object` along with the `event.type`."
- **Disabled destinations**: "If your destination has been disabled or deleted when we attempt a retry, we prevent future retries of that event." No statement that Stripe automatically disables a failing endpoint was found on the pages fetched in this session; older Stripe documentation described this, so writers should check before repeating it [ASSUMPTION/JUDGEMENT on the older behaviour].
- **Manual recovery**: `stripe events resend <event_id> --webhook-endpoint=<endpoint_id>` "works for up to 30 days after the event creation"; the Events list API "only returns events created in the last 30 days" [VERIFIED: https://docs.stripe.com/webhooks.md and https://docs.stripe.com/events/manage-webhook-endpoints.md, n.d., accessed 2026-11]. A manual resend "doesn't cancel Stripe's automatic retry behavior, even if it results in a `2xx` status code."
- **Limits**: "a maximum of 16 event destinations per livemode or sandbox account" [VERIFIED: https://docs.stripe.com/events/how-events-work.md, n.d., accessed 2026-11].

The gap between three days of automatic retries and thirty days of retrievable events defines the recovery plan: an outage shorter than three days heals itself; one between three and thirty days needs a backfill from the Events API; beyond thirty days the events are gone and the objects must be reconciled directly [ASSUMPTION/JUDGEMENT].

### 5.3 Signing scheme

[VERIFIED: https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11]:

- Header `Stripe-Signature` with comma-separated entries: `t` ("The timestamp when this event was signed by Stripe, in seconds since the Unix epoch. This doesn't represent when the event itself was generated"), one or more `v1` signatures, and `v0` ("included only for events related to a sandbox account. This isn't valid for signature verification").
- `v1` is "a hash-based message authentication code (HMAC) with SHA-256" over the `signed_payload`: the timestamp, the character `.`, and "the unmodified HTTP request body". The key is the endpoint's `whsec_` signing secret.
- Verification: compute the HMAC, "Use a constant-time string comparison", and reject if the timestamp is outside tolerance. "Our libraries have a default tolerance of 5 minutes". "Don't use a tolerance value of `0`. Using a tolerance value of `0` disables the recency check entirely."
- Replay protection: the timestamp is part of the signed payload, so an attacker cannot change it; and "If Stripe retries an event … then we generate a new signature and timestamp for the new delivery attempt."
- Secret rotation: on rolling a secret the old one can stay active "for up to 7 days"; "Stripe generates one signature per secret", hence multiple `v1` entries.
- Downgrade protection: "ignore signature schemes other than `v1`".
- Newer debugging entries `secret`, `destination` and `payload` "aren't covered by the HMAC. Don't use them to authenticate a request". "Your integration must accept unknown entries and must not depend on a fixed entry count or order."
- The raw body is required: "Any manipulation to the raw body of the request causes the verification to fail."
- IP allow-listing is offered as an additional control: "allow traffic from Stripe public IP addresses" [VERIFIED: https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11].

### 5.4 Event destinations beyond HTTP

- "Stripe pushes events to your configured destinations, which can be webhook endpoints, Amazon EventBridge, or Azure Event Grid." [VERIFIED: https://docs.stripe.com/events/how-events-work.md, n.d., accessed 2026-11].
- Timeline: Event Destinations in public beta, August 2024 [VERIFIED: https://stripe.dev/blog/stripe-developer-digest-august-2024-workbench-is-now-available-to-everyone, published 2024-08-30]; API with Amazon EventBridge as a destination type in `2024-10-28.acacia` [VERIFIED: https://docs.stripe.com/changelog/acacia/2024-10-28/event-destinations-api.md, published 2024-10-28]; "Event Destinations is now in GA and rolling out to all accounts" [VERIFIED: https://stripe.dev/blog/growing-your-stripe-integration-with-event-destinations, published 2024-10-31]; Azure Event Grid added in the Dahlia release (changelog rows dated 2026-03-25 and 2026-04-22) [VERIFIED: https://docs.stripe.com/changelog.md, published 2026-10-28].
- EventBridge mechanics: Stripe creates a "partner event source" in the customer's AWS account and region, which must be associated with an event bus "within 7 days"; Stripe publishes with `PutPartnerEvents`. The retry and ordering statements are the same as for webhooks (three days, no ordering guarantee) [VERIFIED: https://docs.stripe.com/event-destinations/eventbridge.md, n.d., accessed 2026-11].
- The stated benefit: "All events are sent securely to EventBridge so merchants can trust each event is from Stripe without needing to verify webhook signatures in their code", and no public HTTP endpoint to run [VERIFIED: https://stripe.dev/blog/growing-your-stripe-integration-with-event-destinations, published 2024-10-31].

### 5.5 How Stripe delivers webhooks at scale

**Nothing public found.** Searched: one web search for Stripe engineering talks or posts on webhook delivery, and the full list of post slugs on `stripe.dev/blog` (about 120). Results were receiver-side guidance only: a rate-limit-friendly consumer pattern, resilient handlers with dead-letter queues, EventBridge integration. The chapter's section on "what building a webhook sender involves (fan-out, isolation of slow endpoints, backlog)" must be labelled reference-architecture inference, not Stripe's design. The few facts the documentation implies: events are generated asynchronously from the state change ("Events are delivered asynchronously"), each delivery attempt is signed separately, each destination has its own retry schedule and delivery log, and snapshot payloads are rendered at a fixed API version per destination [VERIFIED for those four statements: https://docs.stripe.com/events/how-events-work.md and https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11].

### Stripe vs Adyen (PART 5)

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Acknowledgement | Any `2xx`, "quickly"; no number of seconds published | A successful status such as 200 or 202; "If Adyen does not receive this response within 10 seconds … we mark the webhook as Failing and put it in a retry queue" [VERIFIED: https://docs.adyen.com/development-resources/webhooks/handle-webhook-events.md, last modified 2026-09-15] | Adyen publishes the deadline; Stripe does not |
| Retry window | "up to three days with an exponential back off"; intervals not published | "up to 30 days" at published intervals: 30 s, 30 s, 1 min, 2 min, 5 min, 10 min, 15 min, 30 min, 1 h, 2 h, 4 h, 8 h [VERIFIED: https://docs.adyen.com/development-resources/webhooks/troubleshoot.md, n.d., accessed 2026-11] | Adyen keeps trying ten times longer; Stripe compensates with a 30-day Events API to pull from [ASSUMPTION/JUDGEMENT] |
| Queue behaviour | Per-event retries; no ordering guarantee | A retry *queue* per endpoint: "If a retry is successful, we continue with the next webhook in the queue"; after recovery "the queued webhooks are sent in a short timeframe" | Adyen's wording implies a blocked endpoint holds back later messages; Stripe's implies independent deliveries [ASSUMPTION/JUDGEMENT] |
| Ordering | Explicitly not guaranteed; do not use `created` to order | "To ensure you are processing events in the correct chronological order, always check the timestamp"; some webhooks carry a `sequenceNumber` [VERIFIED: handle-webhook-events page] | Both put ordering on the receiver; Adyen gives a field to do it with |
| Duplicates | Possible; dedupe on event ID | Possible; duplicates share `eventCode` and `pspReference`; "use the details from the latest webhook event" [VERIFIED: same] | Stripe events have their own ID; Adyen duplicates are identified by business keys [ASSUMPTION/JUDGEMENT] |
| Authentication | HMAC-SHA256 with a signed timestamp; 5-minute default tolerance | HMAC signatures "strongly recommend[ed]"; also basic authentication, and OAuth 2.0 "strongly recommend[ed]" for standard webhooks [VERIFIED: https://docs.adyen.com/development-resources/webhooks/secure-webhooks.md, last modified 2026-11-17] | Stripe has one scheme with built-in replay protection; Adyen offers several and lets the receiver authenticate Adyen as a client [ASSUMPTION/JUDGEMENT] |
| Payload | Snapshot (versioned) or thin (unversioned, fetch-back) | Full payload; no thin/fetch-back format found on the pages fetched | — |
| Cloud event buses | Amazon EventBridge, Azure Event Grid | Not found on the pages fetched; the Adyen brief should confirm | — |
| Sender internals | Nothing public | Not searched here | — |

**For readers new to payments.** *Webhook*: an HTTP request the provider makes to the merchant's server to report something that happened. *At-least-once delivery*: every event is delivered one or more times, never guaranteed exactly once. *Signature verification*: recomputing a keyed hash of the received body to prove the provider sent it unmodified. *Thin event*: a notification that carries only identifiers, so the receiver fetches current state.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) A receiver's obligations follow directly from the contract: verify, persist, acknowledge, then process; deduplicate on event ID; never infer order from arrival or timestamp; fetch current state before acting. (2) Thin events make "fetch before acting" the only option, which removes stale-snapshot bugs and payload versioning at the cost of one API read per event; the read counts against rate limits and the read allocation (6.3). (3) A signed timestamp regenerated per attempt is what lets a receiver enforce a five-minute replay window without rejecting legitimate retries. (4) A provider-side sender needs a per-destination version, secret set, retry schedule and delivery log; that much is visible from outside.

---

## PART 6: The developer platform (chapter 21)

### 6.1 API keys

[VERIFIED: https://docs.stripe.com/keys.md and https://docs.stripe.com/keys/restricted-api-keys.md, n.d., accessed 2026-11]:

- Key types: publishable (`pk_…`, safe to expose); secret (`sk_…`, "unrestricted permissions on all Stripe APIs"); **restricted** (`rk_…`, "API key with permissions you control"); organization (`sk_org_…`, across multiple accounts); and "managed API keys issued by certain hosting platforms".
- ⚠ **Stripe now recommends against secret keys**: "Because you can't limit their permissions, we don't recommend using secret keys for new use cases, and for existing integrations, we recommend migrating secret key usage to RAKs."
- Restricted keys: per resource the permission is "None, Read, or Write"; "The default value for all permissions is None"; Connect permissions are set separately; a restricted key is a "drop-in" replacement in server code.
- A restricted key can be tagged "as belonging to an autonomous agent"; "RAKs are the recommended type of key for API keys you give to AI agents".
- Lifecycle: a live secret key is shown once ("you can't reveal it later"); keys can be expired and rotated; "Access policies have replaced IP address restrictions."
- The mode is in the key: sandbox keys start `pk_test_`, `rk_test_`, `sk_test_`; live keys `pk_live_`, `rk_live_`, `sk_live_`. "API objects in one mode aren't accessible to the other." [VERIFIED: https://docs.stripe.com/testing-use-cases.md, n.d., accessed 2026-11].

### 6.2 Test mode and sandboxes

- Timeline: Sandboxes private beta announced in the June 2024 developer digest [VERIFIED: https://stripe.dev/blog/stripe-developer-digest-june-2024-join-the-sandboxes-private-beta, published 2024-06-30]; "Sandboxes is now in public beta" [VERIFIED: https://stripe.dev/blog/stripe-developer-digest-august-2024-workbench-is-now-available-to-everyone, published 2024-08-30]; by October 2024 a Stripe post says "As a Stripe customer, you can now use the new Sandboxes feature in the Dashboard" [VERIFIED: https://stripe.dev/blog/prepare-for-api-upgrades, published 2024-10-24]. **No dated GA announcement was found** (see Research limitation).
- Current state: "Sandboxes are the Stripe testing environment." "After you create a Stripe account, Stripe places you in a sandbox." The old test mode survives as "the legacy test mode sandbox", which "shares some settings with live mode" and cannot be deleted [VERIFIED: https://docs.stripe.com/testing-use-cases.md, n.d., accessed 2026-11].

| | Legacy test mode sandbox | General sandboxes |
| --- | --- | --- |
| Number | one | "up to five" (the legacy one does not count) |
| Settings | "Share settings between live mode and the legacy test mode sandbox. You can't test many settings independently." | "Isolate settings completely for each sandbox. Copy settings from live mode at creation time" |
| Access | same roles as live mode | can invite users "to sandboxes only, without granting them access to live mode"; default access level Private |

[VERIFIED: same].

- **What a sandbox cannot simulate**: "the payments you create aren't processed by card networks or payment providers" [VERIFIED: https://docs.stripe.com/sandboxes.md, n.d., accessed 2026-11]; "You can't test IC+ pricing in a sandbox"; "You can't create connections between a Connect platform's sandbox and connected account sandboxes" [VERIFIED: same]; latency is unrepresentative: "creating a charge in live mode sends a request to a payment gateway and that request is mocked in a sandbox, resulting in significantly different latency profiles"; rate limits are lower; and webhook retries differ (three attempts over a few hours instead of three days) [VERIFIED: https://docs.stripe.com/rate-limits.md and https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11]. Stripe "generally discourage[s]" load testing against a sandbox and recommends mocking Stripe with sampled latencies instead [VERIFIED: https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11].
- Simulation primitives exist for "payout success and failure" and "disputes, inquiries, and early fraud warnings"; Billing has test clocks [VERIFIED: https://docs.stripe.com/testing-use-cases.md and https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11].
- The CLI can "provision an anonymous Stripe sandbox with working API keys. It doesn't require account registration" (`stripe sandbox create`), aimed at coding agents [VERIFIED: https://docs.stripe.com/sandboxes.md, n.d., accessed 2026-11].

### 6.3 Rate limits: the 2017 design and the current numbers

"Scaling your API with rate limiters", Paul Tarjan [VERIFIED: https://stripe.com/blog/rate-limiters, published 2017-03-30]. **(evidence age: 9 years.)** Current docs confirm request-rate and concurrency limiting and add endpoint- and resource-level limits; they contradict the 2017 statement that test and live limits are the same; nothing current confirms or denies the two load shedders.

- The distinction: "A rate limiter is used to control the rate of traffic sent or received on the network"; "A load shedder makes its decisions based on the whole state of the system rather than the user who is making the request."
- Four mechanisms "in production" in 2017:
  1. **Request rate limiter**: "restricts each user to N requests per second"; "It has rejected millions of requests this month alone"; with "the ability to briefly burst above the cap".
  2. **Concurrent requests limiter**: "You can only have 20 API requests in progress at the same time"; triggered "12,000 requests this month"; it "totally solved" contention on expensive endpoints.
  3. **Fleet usage load shedder**: traffic is split into "critical API methods (e.g. creating charges) and non-critical methods (e.g. listing charges)"; "We have a Redis cluster that counts how many requests we currently have of each type"; if the reservation is 20%, "any non-critical request over their 80% allocation would be rejected with status code 503."
  4. **Worker utilization load shedder**: "the final line of defense"; four categories shed in reverse order of importance: "Critical methods, POSTs, GETs, Test mode traffic"; shedding and restoring must be slow to avoid "flapping"; "Only 100 requests were rejected this month".
- Implementation: "We use the token bucket algorithm"; "every Stripe user has a bucket"; "We implement our rate limiters using Redis."
- Operational rules: fail open ("if there were bugs in the rate limiting code (or if Redis were to go down), requests wouldn't be affected"); "kill switches"; and "Dark launch each rate limiter to watch the traffic they would block."
- Contradicted today: "Our API provides the same rate limiting behavior in both test and live modes."

⚠ Current documented limits [VERIFIED: https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11]:

| Limit | Value |
| --- | --- |
| Global API rate limit, live mode | 100 requests per second per account |
| Global API rate limit, sandbox | 25 requests per second |
| Individual endpoint, unless noted | 25 requests per second ("Stripe considers each named API operation a separate endpoint") |
| PaymentIntents | "1000 update requests per PaymentIntent object, per hour" |
| Payouts | 15 create requests per second; 30 concurrent requests per business |
| Connect account creation | 30 per second live, 5 per second sandbox |
| Search API | 20 read requests per second |
| Files API | 20 reads and 20 writes per second |
| Global concurrency, live | "50 in-progress requests" by default |
| Read allocation | reads "must not exceed an average of 500 per transaction" over a rolling 30 days, with a minimum of 10,000 reads a month; "Write API requests have no allocation limit" |
| Meter events (v1) | 1,000 calls per second, outside the global limit; v2 meter event stream "up to 10,000 events per second", up to 200,000 by arrangement |

Last row: [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api.md, n.d., accessed 2026-11].

- A 429 carries a `Stripe-Rate-Limited-Reason` header: `global-rate`, `endpoint-rate`, `global-concurrency`, `endpoint-concurrency`, `resource-specific`. A 429 without it "might be a lock timeout" [VERIFIED: https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11].
- On payment bursts: "A sudden increase in charge volume, such as a flash sale, might result in rate limiting. We try to set our rates high enough that legitimate payment traffic never exceeds the limits, but if you suspect that an upcoming event might push you over the limits listed above, contact Stripe Support." Limit increases are by request [VERIFIED: same]. This is the documented fact behind Larkfield's "Renewal Wave meeting a rate limit" [ASSUMPTION/JUDGEMENT].
- Client guidance: exponential backoff with randomness, and "a client-side token bucket rate-limiting algorithm" [VERIFIED: same].
- The docs still describe the concurrency limiter as shedding: long requests "run the risk of causing the concurrency limiter to shed new requests" [VERIFIED: same]. The read allocation (a quota tied to transaction count) is a third kind of limit that the 2017 post does not mention; it prices polling [ASSUMPTION/JUDGEMENT].

### 6.4 Request logs, Workbench, CLI

- **Workbench** launched 19 August 2024: "Stripe Workbench, our new home for developers within the Dashboard", "available to all new users by default", with an Overview (API success rate, recent errors, recommended API upgrades), Errors, Inspector ("look under the hood of any object … inspect the underlying JSON and API requests"), Logs, Events, Webhooks, a browser Shell and an API Explorer. It was tested "over the last year with thousands of users, including Slack and Notion" [VERIFIED: https://stripe.com/blog/workbench-a-new-way-to-debug-monitor-and-grow-your-stripe-integration, published 2024-08-19; https://docs.stripe.com/workbench/overview.md, n.d., accessed 2026-11].
- **Request logs** are tied to errors: every error object has a `request_log_url`, "A URL to the request log entry in your dashboard" [VERIFIED: https://docs.stripe.com/api/errors.md, n.d., accessed 2026-11]. v2 request logs appear only in Workbench; meter event stream requests are excluded "Because of the large volume" [VERIFIED: https://docs.stripe.com/api-v2-overview.md and https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api.md, n.d., accessed 2026-11]. The retention period of request logs was not found on the pages fetched.
- **Stripe CLI**: `stripe listen` forwards events to a local server ("Securely test webhooks without relying on third-party tunneling software"), `stripe trigger` fires test events, `stripe events resend`, `stripe logs tail` ("only supports displaying request logs from a sandbox"), generic `get`/`post`/`delete` and resource commands, `fixtures`, and `stripe sandbox create` [VERIFIED: https://docs.stripe.com/cli.md, n.d., accessed 2026-11]. The 2020 post credits it with rescuing the PaymentIntents migration: "Stripe CLI's launch made webhooks much less daunting" [VERIFIED: https://stripe.dev/blog/payment-api-design, published 2020-12-15].

### 6.5 OpenAPI and SDK generation

The June 2026 post is the primary source [VERIFIED: https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products, published 2026-06-15]:

- "OpenAPI has been part of Stripe's toolbox since 2016, initially powering internal tooling like validations and test suites. In 2017, we published a public OpenAPI description of our API and kept it up-to-date as our APIs evolved. In 2019, we used OpenAPI to auto-generate a Stripe SDK for the first time, releasing stripe-java@8.0."
- Until recently "OpenAPI wasn't universally adopted across Stripe. … Others, like the API Reference, bypassed OpenAPI entirely and parsed APIs straight from our internal Ruby-based DSL."
- v2 forced convergence: with a second, protobuf-based definition format, "SDK and API Reference generators had to be duplicated. Preview support for v2 APIs in the CLI was shut down entirely because the maintenance burden was too high." The decision: "converge on OpenAPI."
- One generator, many artefacts: output is controlled by "variant, phase, and version". Variants are "surfaces" (public repo, SDKs, CLI, API reference, internal tools); phases are `generally_available`, `public_preview`, `private_preview`.
- What a release touches: "The official SDKs need to have new versions published across seven different languages and three release channels", plus the CLI, Shell, API Explorer, API Reference and changelog.
- Vendor extensions carry what OpenAPI lacks: `x-stripeOperations` (which methods operate on a resource; "directly powers the methods available on an SDK object and the subcommands available in the Stripe CLI"), `x-resourceId`, `x-stripeResource`, `x-stripeEvent`, `x-stripeAccess`, `x-expandableFields`.
- At release: "the canonical OpenAPI description for the new version is snapshotted and propagated to downstream consumers … It's published to our CDN and fetched by workflows in our open-source repos such as stripe/openapi and stripe/stripe-cli."

The public repository `github.com/stripe/openapi` has `/latest/` (GA, v1 and v2), `/preview/` and a legacy v1-only `/openapi/` directory, in JSON and YAML, with a "public" spec and an "SDK" spec that "Contains special annotations, deprecated endpoints, and pre-release features specifically intended to support generating Stripe API libraries" [VERIFIED: https://raw.githubusercontent.com/stripe/openapi/master/README.md, n.d., accessed 2026-11]. The generator itself (the code that turns the SDK spec into stripe-java, stripe-node and the rest) is not public as far as this session found [ASSUMPTION/JUDGEMENT]. An August 2026 post titled "AI didn't write our SDK, it changed how we built it" exists but was not read [VERIFIED for title, author Mike North and date only: https://stripe.dev/blog/ai-didnt-write-our-sdk-it-changed-how-we-built-it, published 2026-08-28].

### 6.6 Documentation as product: Markdoc

"How Stripe builds interactive docs with Markdoc", Ryan Paul [VERIFIED: https://stripe.dev/blog/markdoc, published 2022-09-13]. **(evidence age: 4 years; the docs site still shows the behaviours described, but the platform itself has not been re-described.)**

- "At Stripe, our product docs are designed to feel like an application rather than a traditional user manual. For example, we incorporate a user's own API test key into code samples … We tailor the content to the individual user, conditionally displaying content based on their location or the Stripe features they use."
- The predecessor: "a monolithic Ruby application built with ERB templates and Sinatra routing. The content freely mixed HTML, Markdown, Ruby, and ERB helper functions." "Content authoring effectively became software development".
- Markdoc "was designed to decouple code and content while enforcing proper discipline at the boundaries": Markdown plus custom tags, variables and conditionals.
- Two developments since: every docs page has a plain-Markdown variant (append `.md`) and there is an `llms.txt` index [VERIFIED by fetching: https://docs.stripe.com/llms.txt and the `.md` pages used throughout this brief, accessed 2026-11]; and pages carry instructions addressed to coding agents (1.5). Documentation is now written for two readers, the developer and the developer's agent [ASSUMPTION/JUDGEMENT].

### Stripe vs Adyen (PART 6)

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Credentials | Keys with a type and mode prefix; restricted keys with per-resource None/Read/Write | "API credentials" made of an API key plus **roles** ("Permissions that define what the credential is allowed to do"), managed in the Customer Area [VERIFIED: https://docs.adyen.com/development-resources/api-credentials.md, last modified 2021-08-06] **(evidence age: 5 years by last-modified date)** | Adyen's credentials were role-scoped from the start; Stripe began with an all-powerful secret key and now recommends against it [ASSUMPTION/JUDGEMENT] |
| Test environment | Sandboxes (up to five, isolated) inside the same account and API host | A separate test platform with its own Customer Area (`ca-test.adyen.com`), hosts (`checkout-test.adyen.com`) and credentials [VERIFIED: https://docs.adyen.com/development-resources/testing.md, last modified 2023-11-23] | Stripe separates by key, Adyen by environment [ASSUMPTION/JUDGEMENT] |
| Rate limits | Published numbers (6.3) | No general rate-limit page found (two guessed URLs returned 404); the Adyen brief should state what is documented | — |
| Limiter design | Published 2017 | Nothing found here | — |
| SDK generation | OpenAPI → SDKs since 2019 (stripe-java 8.0); pipeline described 2026 | Libraries have "generated models"; OpenAPI definitions public [VERIFIED: https://docs.adyen.com/development-resources/libraries.md, last modified 2023-05-19, and the adyen-openapi README] | Both generate from OpenAPI; only Stripe has described the pipeline |
| Tooling | Workbench, CLI, Shell | Customer Area tooling, API Explorer, API Diff Tool (Adyen brief) | — |

**For readers new to payments.** *Restricted key*: an API credential limited to named resources and to read or write. *Sandbox*: a provider environment where API calls create simulated objects and no card network is contacted. *Rate limit*: a cap on requests per unit of time per account. *Load shedding*: deliberately rejecting lower-priority requests so that critical ones (creating a payment) keep working during overload.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) A sandbox proves that an integration handles the API's shapes and states; it proves nothing about issuer behaviour, latency, or limits, and Stripe says so. (2) A payment API needs at least two kinds of limiter (rate and concurrency) and a priority order for shedding, with payment creation at the top and test traffic at the bottom. (3) Limiters must fail open and be dark-launched; a limiter outage must not become an API outage. (4) One machine-readable API description feeding SDKs, CLI, reference and changelog is what makes a monthly release cadence across seven languages feasible. (5) A read quota tied to transaction count is an architectural nudge toward events and data exports and away from polling.

---

## Key numbers

| Number | Definition | Source and date |
| --- | --- | --- |
| 255 characters | Maximum length of a Stripe idempotency key | docs.stripe.com/api/idempotent_requests, accessed 2026-11 |
| ≥ 24 hours | Minimum retention of an API v1 idempotency key and its stored response | same |
| 30 days | Idempotent-replay window in API v2 | docs.stripe.com/api-v2-overview, accessed 2026-11 |
| 64 characters; 7–14 days | Adyen idempotency key maximum length; validity after first submission | docs.adyen.com/development-resources/api-idempotency, last modified 2020-07-30 |
| 3 days | Stripe automatic webhook retry window, live mode, exponential backoff | docs.stripe.com/webhooks, accessed 2026-11 |
| 3 attempts over a few hours | Stripe webhook retries in a sandbox | same |
| 30 days | Events retrievable through the Events API; manual resend window | docs.stripe.com/api/events and /webhooks, accessed 2026-11 |
| 5 minutes | Default signature timestamp tolerance in Stripe SDKs | docs.stripe.com/webhooks, accessed 2026-11 |
| 7 days | Maximum overlap of old and new webhook signing secrets | same |
| 16 | Maximum event destinations per live or sandbox account | docs.stripe.com/events/how-events-work, accessed 2026-11 |
| 10 seconds; 30 days | Adyen webhook acknowledgement deadline; Adyen retry-queue duration | docs.adyen.com webhooks pages, 2026 |
| 100 rps / 25 rps | Stripe global API rate limit per account, live / sandbox | docs.stripe.com/rate-limits, accessed 2026-11 ⚠ |
| 50 | Default global concurrency limit, live mode (in-progress requests) | same ⚠ |
| 500 reads per transaction | Average read-request allocation over a rolling 30 days (minimum 10,000 reads a month) | same ⚠ |
| 1,000 per hour | Update requests per PaymentIntent object | same ⚠ |
| 50 keys, 40 / 500 characters | Metadata: maximum keys, key length, value length | docs.stripe.com/api/metadata, accessed 2026-11 |
| 4 levels | Maximum `expand` depth | docs.stripe.com/api/expanding_objects, accessed 2026-11 |
| 1–100, default 10 | `limit` on list endpoints | docs.stripe.com/api/pagination, accessed 2026-11 |
| 7 statuses | PaymentIntent `status` values | docs.stripe.com/api/payment_intents/object, accessed 2026-11 |
| 2 per year; monthly | Major (breaking) API releases; additive releases | stripe.com/blog/introducing-stripes-new-api-release-process, 2024-10-01 |
| `2026-10-28.endive` | Current Stripe API version on 17 November 2026 | docs.stripe.com/api/versioning, accessed 2026-11 ⚠ |
| "almost a hundred" | Backwards-incompatible API upgrades in Stripe's first six years | stripe.com/blog/api-versioning, 2017-08-05 (evidence age: 9 years) |
| 11 → 36 properties; 5 → 14 parameters | Growth of the Charge object and of Charge creation, 2011–2018 | stripe.dev/blog/payment-api-design, 2020-12-15 |
| "almost two years" | Time to roll out PaymentIntents after design | same |
| 5 people, 3 months | Team and time that designed PaymentIntents | same |
| 4 limiters; 20%; 20 | Limiter types in production in 2017; example fleet reservation for critical requests; example concurrent-request cap | stripe.com/blog/rate-limiters, 2017-03-30 (evidence age: 9 years) |
| 7 languages, 3 channels | SDK languages and release channels per API release | stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products, 2026-06-15 |
| 2016 / 2017 / 2019 | OpenAPI used internally / published / first generated SDK (stripe-java 8.0) | same |
| up to 5 | General sandboxes per account | docs.stripe.com/testing-use-cases, accessed 2026-11 ⚠ |
| 24 hours | Automatic expiry of a Checkout Session (a PaymentIntent has none) | docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison, accessed 2026-11 |
| 7 days / 2 days | Typical card authorization hold, online / in-person (Visa customer-initiated online: 4 days 18 hours) | docs.stripe.com/payments/place-a-hold-on-a-payment-method, accessed 2026-11 ⚠ |

## Open questions / not verifiable

These are the book's "where the evidence stops" statements for the Stripe side of chapters 08 and 17–21.

1. **How Stripe stores and looks up idempotency keys** (data store, request fingerprint, locking, what "after endpoint execution begins" means internally) is not published. The recovery-point design is from an engineer's personal blog about a demo application.
2. **How API v2 achieves "retries failed work to completion"** (a workflow engine, a saga, per-step idempotency) is not published.
3. **Whether Stripe has retired any dated API version**, and how many version change modules exist today, is not stated anywhere fetched. The 2017 post expected retirements.
4. **Whether the 2017 version-change-module mechanism still serves v1** is not confirmed by any later source; the 2026 post confirms only that v1 is still defined in a Ruby DSL and that v1 version history is hard to regenerate.
5. **Stripe's API review process**: no public description beyond one 2017 sentence and the 2026 list of automated checks.
6. **How Stripe delivers webhooks** (queues, isolation of slow endpoints, backlog handling, per-attempt timeout in seconds, the exact backoff schedule) is not published.
7. **Whether Stripe still auto-disables failing webhook endpoints** was not found on the current pages fetched.
8. **Which v1 payment events have generally available thin equivalents** was not verified; a June 2026 post still described thin events for v1 resources as early access, while the docs say both namespaces generate them.
9. **The GA date of Sandboxes** and **the launch date of the `/v2` namespace**: no dated announcement found.
10. **Whether the fleet-usage and worker-utilization load shedders of 2017 still exist**, and the current token-bucket parameters (burst size), are not published. The Redis-based implementation is 2017 evidence only.
11. **Request-log retention** and whether logs include request bodies for all endpoints: not found.
12. **A complete list of v2 resources and their release phase** as of November 2026: assembled here from changelog rows, not from an index.
13. **When (or whether) payments move to `/v2`**: no public statement found.
14. **SDK retry defaults** other than stripe-node were not checked.
15. **The shutdown date of the Sources API**: announced as planned, no public date; two documentation pages disagree about card Sources.

## Source list

**Stripe engineering and product posts**

- "Designing robust and predictable APIs with idempotency" — Stripe blog, Brandur Leach — 2017-02-22 — https://stripe.com/blog/idempotency — idempotency keys, failure cases, backoff and jitter (evidence age: 9 years).
- "Scaling your API with rate limiters" — Stripe blog, Paul Tarjan — 2017-03-30 — https://stripe.com/blog/rate-limiters — four limiters, token bucket on Redis, fail-open and dark launch (evidence age: 9 years).
- "APIs as infrastructure: future-proofing Stripe with versioning" — Stripe blog, Brandur Leach — 2017-08-05 (as shown on the page) — https://stripe.com/blog/api-versioning — rolling versions, account pinning, version change modules, API review sentence (evidence age: 9 years).
- "Stripe's payments APIs: The first 10 years" — Stripe developer blog, Michelle Bu — 2020-12-15 — https://stripe.dev/blog/payment-api-design — Charges, Sources, PaymentIntents history and design method (evidence age: 6 years).
- "How Stripe builds interactive docs with Markdoc" — Stripe developer blog, Ryan Paul — 2022-09-13 — https://stripe.dev/blog/markdoc — docs platform (evidence age: 4 years).
- "Workbench: A new way to debug, monitor, and grow your Stripe integration" — Stripe blog, Michael Glukhovsky and Tomer Elmalem — 2024-08-19 — https://stripe.com/blog/workbench-a-new-way-to-debug-monitor-and-grow-your-stripe-integration — Workbench launch.
- "Introducing Stripe's new API release process" — Stripe blog, Michael Glukhovsky and Wissam Abirached — 2024-10-01 — https://stripe.com/blog/introducing-stripes-new-api-release-process — named majors, monthly releases.
- "Introducing Stripe's new public preview release channel" — Stripe developer blog, Paul Anderson — 2025-05-07 — https://stripe.dev/blog/introducing-stripes-new-public-preview-release-channel — `.preview` versions.
- "How API changes flow into Stripe's developer products" — Stripe developer blog, Mikael Mello and Anna Mason — 2026-06-15 — https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products — OpenAPI pipeline, v1 Ruby DSL and v2 protobuf, lint checks, SDK generation history.
- "Event notification handlers" (thin events) — Stripe developer blog, David Brownman — 2026-06-24 — https://stripe.dev/blog/event-notification-handlers-thin-events — motive for thin events; v1 thin events early access.
- "Growing your Stripe integration with Event Destinations" — Stripe developer blog, Ben Smith — 2024-10-31 — https://stripe.dev/blog/growing-your-stripe-integration-with-event-destinations — Event Destinations GA, EventBridge.
- "Because nobody likes being charged twice" — Stripe developer blog, Ben Smith — 2025-04-10 — https://stripe.dev/blog/because-nobody-likes-being-charged-twice — idempotency keys plus queues, 24 hours.
- "Prepare for API upgrades" — Stripe developer blog, Cecil Phillip — 2024-10-24 — https://stripe.dev/blog/prepare-for-api-upgrades — sandboxes and Workbench for upgrades.
- Stripe Developer Digest, June 2024 and August 2024 — Stripe developer blog — 2024-06-30, 2024-08-30 — https://stripe.dev/blog/stripe-developer-digest-june-2024-join-the-sandboxes-private-beta and https://stripe.dev/blog/stripe-developer-digest-august-2024-workbench-is-now-available-to-everyone — Sandboxes private and public beta; Event Destinations public beta.
- "AI didn't write our SDK, it changed how we built it" — Stripe developer blog, Mike North — 2026-08-28 — https://stripe.dev/blog/ai-didnt-write-our-sdk-it-changed-how-we-built-it — located, not read.

**Stripe documentation (n.d., accessed 2026-11-17)**

- Payment Intents API — https://docs.stripe.com/payments/payment-intents.md — create/confirm, client secret, best practices, Checkout recommendation.
- How Payment Intents and Setup Intents work — https://docs.stripe.com/payments/paymentintents/lifecycle.md — statuses.
- PaymentIntent object — https://docs.stripe.com/api/payment_intents/object.md — status enum, capture and confirmation methods, cancellation reasons.
- Payment status updates — https://docs.stripe.com/payments/payment-intents/verifying-status.md — webhooks versus polling.
- Older payment APIs — https://docs.stripe.com/payments/older-apis.md; Sources — https://docs.stripe.com/sources.md; migration — https://docs.stripe.com/payments/payment-methods/transitioning.md — deprecation status.
- Compare Checkout Sessions and Payment Intents — https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md — recommended surface.
- Dynamic payment methods — https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md.
- Place a hold on a payment method — https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md — authorization windows.
- CIT and MIT — https://docs.stripe.com/payments/cits-and-mits.md.
- Refund object — https://docs.stripe.com/api/refunds/object.md; Dispute object — https://docs.stripe.com/api/disputes/object.md.
- Errors — https://docs.stripe.com/api/errors.md; decline codes — https://docs.stripe.com/declines/codes.md; advanced error handling — https://docs.stripe.com/error-low-level.md.
- Expanding responses — https://docs.stripe.com/api/expanding_objects.md; pagination — https://docs.stripe.com/api/pagination.md; metadata — https://docs.stripe.com/api/metadata.md; request IDs — https://docs.stripe.com/api/request_ids.md.
- Idempotent requests — https://docs.stripe.com/api/idempotent_requests.md.
- API v2 overview — https://docs.stripe.com/api-v2-overview.md; Accounts v2 — https://docs.stripe.com/api/v2/core/accounts.md and https://docs.stripe.com/connect/accounts-v2.md.
- Versioning — https://docs.stripe.com/api/versioning.md; upgrades — https://docs.stripe.com/upgrades.md; release phases — https://docs.stripe.com/release-phases.md.
- Changelog — https://docs.stripe.com/changelog.md (latest entry 2026-10-28) and release pages /changelog/acacia.md, /basil.md, /clover.md, /dahlia.md, /endive.md; entries 2023-08-16/automatic-payment-methods, acacia/2024-09-30/api-v2-thin-events, acacia/2024-10-28/event-destinations-api.
- Webhooks — https://docs.stripe.com/webhooks.md; how events work — https://docs.stripe.com/events/how-events-work.md; manage endpoints — https://docs.stripe.com/events/manage-webhook-endpoints.md; Events API — https://docs.stripe.com/api/events.md; EventBridge — https://docs.stripe.com/event-destinations/eventbridge.md.
- API keys — https://docs.stripe.com/keys.md; restricted keys — https://docs.stripe.com/keys/restricted-api-keys.md.
- Sandboxes — https://docs.stripe.com/sandboxes.md; testing use cases — https://docs.stripe.com/testing-use-cases.md.
- Rate limits — https://docs.stripe.com/rate-limits.md; recording usage — https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api.md.
- Workbench — https://docs.stripe.com/workbench/overview.md; CLI reference — https://docs.stripe.com/cli.md; llms.txt — https://docs.stripe.com/llms.txt.

**Stripe repositories**

- stripe/openapi README — https://raw.githubusercontent.com/stripe/openapi/master/README.md — spec layout, vendor extensions.
- stripe/stripe-node README — https://raw.githubusercontent.com/stripe/stripe-node/master/README.md — network retry default.

**Secondary and personal sources (written by current or former Stripe employees, not published by Stripe)**

- "Designing APIs for humans: Object IDs" — Paul Asjes, dev.to — 2022-08-30 — https://dev.to/4thzoa/designing-apis-for-humans-object-ids-3o5a — prefixed IDs (evidence age: 4 years).
- "Designing APIs for humans: Error messages" — Paul Asjes, dev.to — 2022-09-14 — https://dev.to/4thzoa/designing-apis-for-humans-error-messages-94p — error design (evidence age: 4 years).
- "Implementing Stripe-like Idempotency Keys in Postgres" — Brandur Leach, brandur.org — 2017-10-27 — https://brandur.org/idempotency-keys — recovery points, atomic phases; a reference design, not Stripe's system (evidence age: 9 years).
- "Stripe V2" — Brandur Leach, brandur.org — 2024-12-28 — https://brandur.org/fragments/stripe-v2 — early state and critique of API v2.

**Adyen documentation (fetched only to anchor the comparison; see the Adyen brief)**

- API idempotency — https://docs.adyen.com/development-resources/api-idempotency.md — last modified 2020-07-30.
- Versioning — https://docs.adyen.com/development-resources/versioning.md — last modified 2022-01-18.
- Handle webhook events — https://docs.adyen.com/development-resources/webhooks/handle-webhook-events.md — last modified 2026-09-15; troubleshoot webhooks — https://docs.adyen.com/development-resources/webhooks/troubleshoot.md; secure webhooks — https://docs.adyen.com/development-resources/webhooks/secure-webhooks.md — last modified 2026-11-17.
- Build your integration (Sessions and Advanced flows) — https://docs.adyen.com/online-payments/build-your-integration.md; payment result codes — https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes.md; payment modifications — https://docs.adyen.com/online-payments/modify-payments.md.
- API credentials — https://docs.adyen.com/development-resources/api-credentials.md — last modified 2021-08-06; live endpoints — https://docs.adyen.com/development-resources/live-endpoints.md — last modified 2024-01-18; testing — https://docs.adyen.com/development-resources/testing.md — last modified 2023-11-23; libraries — https://docs.adyen.com/development-resources/libraries.md — last modified 2023-05-19.
- Adyen OpenAPI README — https://raw.githubusercontent.com/Adyen/adyen-openapi/main/README.md.
