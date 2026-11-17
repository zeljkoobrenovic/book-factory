# Research brief: Adyen — payments integration model, API families, idempotency, versioning, webhooks and the developer platform

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 08 (payment state machines), 17 (API design and object models), 18 (idempotency and retries), 19 (API versioning), 20 (webhooks and events), 21 (developer platform), and parts of 02 (authorization), 04 (refunds, reversals and disputes), 07 (local payment methods), 11 (in-person payments) and 47 (case: Adyen). This brief covers **Adyen only**, as deeply as the public record allows. The parallel brief `brief-stripe-payments-and-api.md` covers Stripe; the "Stripe vs Adyen" notes here state the Adyen side in full and give only the Stripe facts fetched in this session as contrast. Where the two briefs disagree on a Stripe fact, the Stripe brief wins.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. Undated documentation is marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a secondary source or from a search-result snippet of a page that could not be fetched; the kind of source is named.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including every statement about how Adyen works internally beyond what it has published.

**How Adyen documentation is dated.** Every `docs.adyen.com` page has a Markdown variant (append `.md`) whose front matter carries a `last_modified` field. The field is **not a reliable publication date**: many pages carry the timestamp of the documentation build of the day (2026-11-17T10:02), and some carry an old date although the body has clearly been edited since (the "Live endpoints" page says `last_modified: 2024-01-18` but gives a Checkout **v72** URL, a version released on 2026-04-15). All Adyen documentation pages are therefore tagged "n.d., accessed 2026-11". Dated facts in this brief come from the release notes (each entry dated), the OpenAPI repository, and Adyen's tech blog (each article has a `datePublished`).

**Machine-readable sources used.** Two sources are more precise than the prose documentation and are used heavily below:

- `https://docs.adyen.com/llms.txt`, the documentation index (2,701 lines), which confirms which pages exist. It lists **no page on API rate limits and no page on pagination** [VERIFIED: https://docs.adyen.com/llms.txt, n.d., accessed 2026-11].
- The `Adyen/adyen-openapi` repository on GitHub (MIT licence, created 2017-11-20, last pushed 2026-11-13), which holds the OpenAPI 3.1 definition of every public API version. Statements below of the form "the specification declares…" come from parsing those JSON files in this session [VERIFIED: https://github.com/Adyen/adyen-openapi, repository metadata via api.github.com, accessed 2026-11].

**Evidence age.** Three Adyen tech-blog articles used here are older than three years: "API-first approach at Adyen platform" (2022-09-27, **evidence age: 4 years**), "Consuming webhooks explained" (2023-02-02, **evidence age: 3.8 years**) and "Building better applications with Adyen API libraries" (2023-03-28, **evidence age: 3.6 years**). Each is flagged where used, with a note on whether current documentation confirms it.

**Research limitation.**

- **API Explorer** (`docs.adyen.com/api-explorer`) is a client-rendered application. The per-version lifecycle state (Active, Inactive, Deprecated, End-of-Life) that the documentation says is shown there could not be read from the static HTML. The lifecycle *policy* is verified; the *state of each Checkout API version today* is not, except where a release note states it.
- The **Hosted Payment Pages end-of-life timeline** is published as an image on the docs page and could not be read. The date "October 2022" comes from a search snippet of an Adyen blog post whose page returned no article text.
- `docs.adyen.com/platforms/manage-webhooks` returned a bot challenge, so webhook delivery rules specific to Balance Platform webhooks are taken from the general webhook pages, which state they apply to both.
- No Adyen page states what the **test environment cannot simulate**; the statements in PART 7 are what the documentation implies, and are tagged as such.
- No talk recording by an Adyen engineer on API design, webhook delivery or idempotency was fetched. The 2022 blog post refers to a YouTube talk "Becoming API-First in the Payment Industry"; it was not watched.
- Stripe facts are limited to eight documentation pages fetched for contrast.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: the latest Checkout API version, Drop-in/Components versions and their end-of-life dates, rate-limit figures (Adyen calls them "indicative"), the webhook retry schedule, the MCP server (alpha), and the Customer Area menus.

---

## PART 1: The online payments integration model (chapters 08, 07, 02)

### 1.1 From hosted pages to the Checkout API: the dated history

Adyen has had three generations of online integration, and all three are still visible in its documentation:

| Generation | What the merchant integrates | Status in November 2026 |
| --- | --- | --- |
| **Hosted Payment Pages (HPP)** | Redirect the shopper to an Adyen-hosted page (`pay.shtml`, `select.shtml`), styled with "skins" | End-of-life: "We are no longer accepting transactions using HPP" |
| **Classic API** (`/authorise`, `/capture`, `/refund` on the `pal` host), optionally with **Client-Side Encryption (CSE)** | Server posts card data, raw or encrypted in the browser by a JavaScript library | "inactive", "no longer supported for new integrations"; "We no longer develop the Classic API, which can process only card payments" |
| **Checkout API** (`/sessions`, `/paymentMethods`, `/payments`, `/payments/details`) with **Drop-in** and **Components** | One API for all payment methods, with client libraries that render the form and handle actions | Current; latest version v72 |

- HPP: "The HPP integration has reached end-of-life. We are no longer accepting transactions using HPP." The successor for an Adyen-hosted page is a product called Hosted Checkout [VERIFIED: https://docs.adyen.com/online-payments/classic-integrations/hosted-payment-pages/deprecation.md and https://docs.adyen.com/online-payments/classic-integrations/hosted-payment-pages.md, n.d., accessed 2026-11]. An Adyen blog post is reported to say that "from Oct 2022" Adyen would stop accepting payments through HPP [WIDELY REPORTED: search snippet of https://www.adyen.com/blog/HPP-end-of-life, 2022; the page itself could not be read].
- Classic API: "This endpoint is inactive and is no longer supported for new integrations." The Classic API integration "lets you accept payments on your website and mobile application, if you support PCI compliance at Level 1 or 2", because the merchant's server handles raw card data [VERIFIED: https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration.md, n.d., accessed 2026-11].
- CSE: Adyen is "No longer developing the CSE integration", and the migration guide says "We no longer support Client Side Encryption (CSE). Replace it with JWE to encrypt payment details" [VERIFIED: https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/client-side-encryption.md and https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api.md, n.d., accessed 2026-11].
- The reasons Adyen gives for moving to the Checkout API: "A single integration to process all payment methods, including cards, bank-based, and alternative payment methods", client libraries "only available with the Checkout API", simpler 3D Secure 2, and "More specific error responses" [VERIFIED: https://docs.adyen.com/online-payments/upgrade-your-integration.md, n.d., accessed 2026-11].

**Dated Checkout API versions** (all from the release notes, which Adyen says cover "starting from 2020" but which include an archive back to 2018) [VERIFIED: https://docs.adyen.com/online-payments/release-notes.md, entries dated as shown]:

| Date | Version | What changed for the object model |
| --- | --- | --- |
| 2018-02-23 | v37 | Earliest version in the release notes and in the OpenAPI repository |
| 2018-06-27 | v40 | `/paymentMethods` response gains `groups` and `supportsRecurring` |
| 2019-02-14 | v41 | New `resultCode` **presentToShopper** for vouchers; several methods "previously supported through Hosted Payment Pages (HPP)" become native |
| 2019-05-14 | v49 | "The response now contains an `action` object that indicates the action to be taken for completing the payment" |
| 2019-08-16 | v50 | `action` of `type` **voucher** |
| 2019-10-29 | v52 | Minor response changes |
| 2020-07-23 to 2020-11-30 | v53, v64, v65, v66 | Four versions in five months |
| 2021-03-01 | v67 | Simplified 3D Secure 2 ("auto-authorization", per the upgrade page) |
| 2021-06-03 | (no new version) | "You can now do your captures, refunds, cancellations, reversals, and asynchronous authorisation adjustments using the Checkout API": the `/payments/{paymentPspReference}/captures`, `/amountUpdates`, `/refunds`, `/reversals`, `/cancels` endpoints |
| 2021-10-06 | v68 | "**POST** /sessions: creates a payment session for Web Drop-in and Web Components integrations"; released the same day as Web Drop-in/Components v5.0.0 |
| 2022-05-24 | v69 | |
| 2023-01-30 | v70 | `recurringProcessingModel` becomes mandatory for storing or using stored details |
| 2023-11-01 | v71 | |
| 2026-04-15 | v72 ⚠ | New request validations; enhanced scheme data must move from `additionalData` to `enhancedSchemeData`; "Previously deprecated parameters have been removed" |

Two observations from that table [ASSUMPTION/JUDGEMENT]:

- The version numbers are not consecutive (37, 40, 41, 46, 49, 50, 52, 53, 64 …). The Checkout API and the classic Payment API appear to share one counter: the classic Payment API specifications run v25–v68, and the migration guide speaks of moving "Classic API v68 endpoints to Checkout API v68". Adyen documents that it "may skip numbers when needed" (section 5.1).
- The cadence slowed sharply: thirteen versions from February 2018 to October 2021, then one every 8–10 months, then a gap of **29 months** between v71 and v72.

The date Drop-in was first released was not found in a source fetched in this session. The first Web Drop-in version mentioned in current documentation is 3.x ("Web Drop-in and Components | Available for 3.10.1 and later", in the client-key migration page) [VERIFIED: https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key.md, n.d., accessed 2026-11].

### 1.2 Sessions flow versus Advanced flow

The Checkout API offers two server-side flows over the same client libraries.

| | Sessions flow | Advanced flow |
| --- | --- | --- |
| Server requests | 1: `POST /sessions` | 3: `POST /paymentMethods`, `POST /payments`, `POST /payments/details` |
| Integration effort (Adyen's words) | "Light" | "Medium" |
| Who handles redirects and additional actions | "Client-side" | "Client-side and server-side" |
| Who sees the payment data | "Adyen sends payment data from our server to your client-side application" | "Adyen sends payment data from our server to your server" |
| Only possible here | — | "Change the order of payment methods for an individual transaction" |

[VERIFIED: https://docs.adyen.com/online-payments/build-your-integration.md, n.d., accessed 2026-11]. "Sessions flow is the default integration that we recommend and that meets the requirements for most online payments integrations" [same page].

**Sessions flow in detail** [VERIFIED: https://docs.adyen.com/online-payments/build-your-integration/sessions-flow.md, n.d., accessed 2026-11]:

1. The merchant server creates a session with amount, currency, country, `reference` and `returnUrl`. The response contains `id` and `sessionData`, which the server passes to the front end.
2. Drop-in or a Component is created from `session.id` and `session.sessionData`; it "shows the available payment methods, collects the shopper's payment details, handles additional actions, and presents the payment result to the shopper".
3. "Your webhook server receives the notification containing the payment outcome."

- **Session expiry**: `expiresAt` is optional. "When not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more than 24 hours after session creation." For Pix the default session validity became 24 hours in v72 [VERIFIED: same page; release note 2026-04-15].
- **Session result**: the merchant can call `GET /sessions/{id}?sessionResult={sessionResult}`, where `sessionResult` comes from the client-side `onPaymentCompleted` or `onPaymentFailed` event. Statuses include **completed** ("This means that the payment was authorized"), **paymentPending** ("payment methods with an asynchronous flow"), **refused**, **canceled** and **expired**. The documentation then warns: "The `status` included in the response doesn't get updated. Do not make the request again to check for payment status updates. Instead, check webhooks or the **Transactions** list in your Customer Area" [VERIFIED: same page].
- **Updating a session**: `PATCH /sessions/{sessionId}` exists, called from the client's `beforeSubmit` callback, to change the amount before payment [VERIFIED: same page; and CheckoutService-v72.json in https://github.com/Adyen/adyen-openapi].
- **If the shopper never returns from a redirect**: "you do not get a `redirectResult`. You do not need to do anything to handle the redirect in this case. Instead, wait for the webhook that we send to your server" [VERIFIED: same page].

**Advanced flow in detail** [VERIFIED: https://docs.adyen.com/online-payments/build-your-integration/advanced-flow.md, n.d., accessed 2026-11]:

1. `POST /paymentMethods` returns "all payment methods that you enabled in your Customer Area that are available for the transaction".
2. The client's `onSubmit` event yields `state.data`; the server sends it in `POST /payments`.
3. "If the response has no `action` object, get the payment outcome. If the response contains an `action` object, handle the additional action." The client library performs the action and fires `onAdditionalDetails`; the server forwards that data in `POST /payments/details`.

The `/payments` endpoint describes itself as "Start a transaction", and its description states the fork exactly: "For a direct flow, the response includes a `pspReference` and a `resultCode` with the payment result, for example **Authorised** or **Refused**. For a redirect or additional action, the response contains an `action` object" [VERIFIED: CheckoutService-v72.json in https://github.com/Adyen/adyen-openapi, version 72].

### 1.3 Result codes and actions: the state vocabulary

**Actions** (`action.type`) documented in the Advanced flow guide: **redirect**, **threeDS2**, **qrCode**, **sdk**, **voucher**, **await** [VERIFIED: advanced-flow page above]. The v72 specification defines nine action schemas: `CheckoutAwaitAction`, `CheckoutBankTransferAction`, `CheckoutDelegatedAuthenticationAction`, `CheckoutNativeRedirectAction`, `CheckoutQrCodeAction`, `CheckoutRedirectAction`, `CheckoutSDKAction`, `CheckoutThreeDS2Action`, `CheckoutVoucherAction` [VERIFIED: CheckoutService-v72.json].

**Result codes** [VERIFIED: https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes.md, n.d., accessed 2026-11; enum confirmed in CheckoutService-v72.json]:

| Group | `resultCode` values | Meaning |
| --- | --- | --- |
| Authentication only | AuthenticationNotRequired, AuthenticationFinished | Standalone 3D Secure 2 outcomes |
| 3D Secure 2 in progress | IdentifyShopper, ChallengeShopper, RedirectShopper | The issuer needs a device fingerprint, a challenge, or a redirect |
| Intermediate | Received, Pending, PresentToShopper | "the payment has not reached a final state yet" |
| Partial | PartiallyAuthorised | The issuer approved less than the requested amount |
| Final | Authorised, Cancelled, Error, Refused | "the payment has reached a final state" |

Three sentences that chapter 08 can quote:

- "The status of a payment can sometimes change after you get the result code, so we recommend that you do not use the result code to update your order management system" [VERIFIED: result-codes page].
- **Received** "is the initial state for all payments"; "For some payments, it can take minutes, hours, or even days to be completed" [same page].
- On the AUTHORISATION webhook: "Although you can use the payment result from the API, we recommend that you rely on the webhook to trigger any business logic to make sure that your system can handle both synchronous and asynchronous payment flows" [VERIFIED: https://docs.adyen.com/development-resources/webhooks/webhook-types.md, n.d., accessed 2026-11].

For non-authorised payments a `refusalReason` is returned, and "We do not recommend disclosing this refusal reason to the shopper" [VERIFIED: result-codes page].

### 1.4 There is no payment object to fetch

The most important structural fact about the Checkout API for chapters 08 and 17: **it has no endpoint that returns a payment by its identifier.** The v72 specification has 28 paths and 31 operations, of which only three are GET: `GET /paymentLinks/{linkId}`, `GET /sessions/{sessionId}` (which needs the client-supplied `sessionResult` and whose status "doesn't get updated") and `GET /storedPaymentMethods`. There is no `GET /payments/{pspReference}` [VERIFIED: CheckoutService-v72.json in https://github.com/Adyen/adyen-openapi, version 72]. The classic Payment API v68 has 13 operations, all POST [VERIFIED: PaymentService-v68.json, same repository].

What exists instead:

- A **reference**, not a resource. "Every payment or modification request (such as a refund or a capture request) in Adyen's system has a globally unique 16-character string called the PSP reference associated with it. This string is alphanumerical" [VERIFIED: https://docs.adyen.com/adyen-glossary.md, n.d., accessed 2026-11]. The same reference identifies an API call: "The `pspReference` is a unique ID for that specific API request" and is returned in a response header as well as the body [VERIFIED: https://docs.adyen.com/development-resources/response-handling.md, n.d., accessed 2026-11].
- A **stream of webhooks** keyed by that reference (PART 6).
- **Reports** and the **Customer Area** payment list, where "As soon as the payment gets a status, we add it as an entry to your list of payments. It is identified by its PSP reference and your merchant reference for it" [VERIFIED: https://docs.adyen.com/account/payments-lifecycle.md, n.d., accessed 2026-11].

The state machine is therefore documented in two places with two vocabularies. The API speaks in 13 result codes (above). The Customer Area and reports speak in **payment statuses**, of which the lifecycle page lists more than seventy, grouped as offer statuses (Received, Open, OfferCancelled), authorization statuses (Authorised, AuthorisedPending, Cancelled, Refused, Error, Retried, Expired, …), settlement statuses (SentForSettle, Settled, SettledBulk, SettledReversed, CaptureFailed, …), refund statuses (SentForRefund, Refunded, RefundedReversed, RefundFailed, RefundNotCleared, …), chargeback statuses (Chargeback, SecondChargeback, ChargebackReversed, …) and payout statuses [VERIFIED: payments-lifecycle page]. Adyen calls the pre-authorization phase an **offer**: "the initial part of the payments lifecycle after you send the payment request, before the shopper completes the payment" [same page]. An offer for a card expires "after 12 hours by default" (the `OFFER_CLOSED` event) [VERIFIED: webhook-types page].

### 1.5 Local payment methods in this model (chapter 07)

- The same four endpoints serve every method; what differs is the `action` returned and whether the result is synchronous. The documentation's own example for why webhooks are required is a bank method: "with payment methods like iDEAL, it can take time to get a confirmation that the payment was completed" [VERIFIED: https://docs.adyen.com/development-resources/webhooks.md, n.d., accessed 2026-11].
- Capture semantics leak through the abstraction. Each payment method has a fixed capture flow: "Direct capture (**SALE**)", where "The payment is captured immediately when it is authorized" and capture settings "do not apply", or "Separate capture (**AUTH**)". "Most card payment methods use separate capture"; "Some online banking payment methods, for example iDEAL, only support direct capture" [VERIFIED: https://docs.adyen.com/online-payments/capture.md, n.d., accessed 2026-11].
- Refund semantics leak too: for "bank transfers, iDEAL, or Bancontact, the status of the payment can change from Refunded to RefundedReversed. This means that the funds have been returned to Adyen, and are back in your account" [VERIFIED: https://docs.adyen.com/online-payments/refund.md, n.d., accessed 2026-11].
- Adyen's engineers describe the general shape in a November 2026 article: for many methods "the flow a merchant tests against follows a lifecycle: an initial call, an additional action the integration must perform, an asynchronous result, and a final state the merchant has to commit", and for UPI Intent "the result is established only when the integration receives a webhook message with the AUTHORISATION event type" [VERIFIED: https://medium.com/adyen/making-payment-method-testing-repeatable-building-the-adyen-payment-simulator-5c11d6fcbe18 via https://medium.com/feed/adyen, published 2026-11-09].

### Stripe vs Adyen (integration and state model)

| Aspect | Adyen (documented) | Stripe (documented, fetched for contrast) | What the difference suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Central object | No retrievable payment resource in the Checkout API; a 16-character `pspReference` per request, result codes in responses, webhooks for outcomes (sources in 1.3–1.4) | A PaymentIntent with a `status` field (`requires_payment_method`, `requires_confirmation`, `processing`, `succeeded`, `canceled` …) that can be retrieved by `GET /v1/payment_intents/{id}` [VERIFIED: https://docs.stripe.com/payments/paymentintents/lifecycle.md and https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11] | Stripe's API is a set of stateful resources the merchant can poll; Adyen's is a set of commands whose results arrive as events. An Adyen integrator must store state themselves; a Stripe integrator can treat Stripe as the store of record and re-read it |
| Low-effort flow | `POST /sessions`, added in v68 on 2021-10-06 | Checkout Sessions and PaymentIntents (see the Stripe brief) | Both converged on "server creates a session, client library completes it", Adyen about two years after introducing `action` objects in 2019 |
| Next step for the client | `action` object with a `type`, since v49 (2019-05-14) | `next_action` on the PaymentIntent (see the Stripe brief) | Same idea; different carrier (response field of a command versus field of a resource) |
| Advice on the synchronous result | "do not use the result code to update your order management system" | "You can't rely on triggering fulfillment only from your checkout landing page" (sibling brief ORDERED) | Both tell integrators the webhook is the authoritative outcome |

### For readers new to payments

- **PSP reference**: the identifier a payment service provider assigns to each payment or follow-up request; at Adyen it is a 16-character string unique across the platform.
- **Result code**: Adyen's name for the state a payment request is in when the API responds, such as Authorised, Refused or Pending.
- **Action**: an instruction returned by the API telling the merchant's front end what the shopper must do next, such as follow a redirect, complete 3D Secure, scan a QR code or keep a voucher.
- **Drop-in and Components**: Adyen's client libraries; Drop-in shows all payment methods in one block, a Component renders a single method.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- An integrator on Adyen needs its own payment table keyed by its `reference` and by `pspReference`, updated from webhooks, because there is no endpoint to re-read a payment. Losing a webhook is not recoverable by polling; it is recoverable only through the retry queue (30 days), the Customer Area, or the settlement reports.
- The adapter that hides two providers (the Larkfield thread in chapter 17) has to synthesise a state on the Adyen side from `resultCode` plus the webhook stream, and to read it from an object on the Stripe side.
- The two vocabularies (13 result codes, 70+ statuses) are a sign that Adyen's internal record is a journal of events per payment rather than one status field; the Customer Area column is literally labelled "Journal type" [VERIFIED: payments-lifecycle page for the label; the inference is the analyst's].

---

## PART 2: Modifications, authorisation types and expiry (chapters 02, 04, 08)

### 2.1 A modification is a separate asynchronous request

Adyen calls every operation on an existing payment a **modification**: capture, cancel, refund, reversal and amount update. In the Checkout API they are sub-resources of the payment's reference, added on 2021-06-03 (section 1.1):

| Operation | Endpoint | Webhook `eventCode` with the outcome | Later failure event |
| --- | --- | --- | --- |
| Capture | `POST /payments/{paymentPspReference}/captures` | CAPTURE | CAPTURE_FAILED |
| Cancel (by PSP reference) | `POST /payments/{paymentPspReference}/cancels` | CANCELLATION | — |
| Cancel (by merchant reference) | `POST /cancels` | TECHNICAL_CANCEL | — |
| Refund | `POST /payments/{paymentPspReference}/refunds` | REFUND | REFUND_FAILED, REFUNDED_REVERSED |
| Reversal | `POST /payments/{paymentPspReference}/reversals` | CANCEL_OR_REFUND | as for refund |
| Amount update | `POST /payments/{paymentPspReference}/amountUpdates` | AUTHORISATION_ADJUSTMENT | — |

[VERIFIED: https://docs.adyen.com/online-payments/capture.md, /cancel.md, /refund.md, /reversal.md, /adjust-authorisation/adjust-with-preauth.md, n.d., accessed 2026-11]

The contract is the same for all of them:

- The response carries two references: "`paymentPspReference`: the PSP reference of the authorization" and "`pspReference`: the PSP reference associated with this capture request. This is different from the PSP reference of the authorization", plus "`status`: **received**. Your capture request will be processed asynchronously. You will receive the result in a webhook" [VERIFIED: capture page].
- The webhook carries `originalReference` (the payment), `pspReference` (the modification), and `success` [VERIFIED: capture, cancel, refund pages].
- An HTTP 200 is not the outcome. Adyen's own explanation: a 200 on a capture means "We received your request. We will execute a payment capture. We still do not know if the capture operation will be successful or not. We will let you know in the corresponding webhook event" [VERIFIED: https://docs.adyen.com/development-resources/response-handling.md, n.d., accessed 2026-11].

### 2.2 Even `success: true` is not final

Captures and refunds have **two** asynchronous stages, which is the clearest documented example of the book's central idea.

- CAPTURE with `success: true` means "The capture request is valid (for example, the authorization has not expired, and the balance is available) and has been submitted to the bank/third-party processor. In most cases, this means that the funds will be transferred to your account. In rare cases the card scheme can still reject the capture, and you will receive a CAPTURE_FAILED webhook" [VERIFIED: capture page].
- "In rare cases, a capture fails even after you received a CAPTURE webhook with `success`: true … This can even happen a few days after you submitted the capture request" [same page]. "Technical failures are automatically re-captured by Adyen within 10 business days" [VERIFIED: webhook-types page].
- The same holds for refunds: "Adyen's validations were successful and we sent the refund request to the card scheme. This usually means that the refund will be processed successfully. However, in rare cases the refund can be rejected by the card scheme, or reversed"; REFUND_FAILED "can happen even a few days after you submit the refund request" [VERIFIED: refund page].
- "Adyen does not send a webhook message when a payment settles successfully." Only the exceptions are evented: `SETTLED_REVERSED` when "Adyen did not receive the captured funds from the card scheme or payment method within 30 days after capture", and `REFUND_NOT_CLEARED`, both for the Sales day payout model [VERIFIED: webhook-types page].

### 2.3 Capture, cancel, reversal, refund: the documented rules

**Capture** [VERIFIED: capture page]:

- "By default, payments are captured automatically without a delay, immediately after authorization of the payment request."
- Three timings: automatic (default), delayed automatic (Customer Area setting of 1–7 days, or `captureDelayHours` per request), and manual (`additionalData.manualCapture: true` per request, or an account setting).
- "A payment that is automatically captured does *not* trigger a separate CAPTURE webhook."
- Partial capture: with a single partial capture "Any unclaimed amount that is left over after partially capturing a payment is automatically cancelled"; "Multiple partial capture is disabled by default, so you need to contact our Support Team to enable this feature."
- Adyen tracks a **balance on the payment**: "If a transaction is authorized for EUR 50, and then partially captured for EUR 30, the remaining balance on the payment is EUR 20." A capture above it fails with `Insufficient balance on payment`.
- Repeating a capture is safe by rule, not only by key: "making capture requests for payments that are captured automatically does not result in double charges" [VERIFIED: CheckoutService-v72.json, description of `/payments/{paymentPspReference}/captures`].

**Cancel** [VERIFIED: cancel page]: possible only before capture ("After a payment has been captured, you can no longer cancel it"). A cancel by the merchant's own reference is allowed "up to 24 hours after authorization" and is the tool for the unknown-outcome case, where the merchant never received a `pspReference`; Adyen recommends it only "if you generate a *unique* references for each payment request and do not have the `pspReference` available".

**Reversal** [VERIFIED: reversal page]: "If the payment has not been captured, it cancels the payment. If the payment has been captured, it refunds the payment." Not available after multiple partial captures or when the payment carries split data for Adyen for Platforms.

**Refund** [VERIFIED: refund page]:

- "You can only refund a payment after it has been captured."
- "It can take up to 40 business days before the funds are returned to the shopper's account, depending on the payment method."
- "If you make multiple partial refunds, the sum of the refund amounts cannot be more than the captured amount."
- **Refund authorization**: "before processing a refund, Adyen checks with the issuer if the shopper's card or account is valid", for American Express, Discover, Mastercard and Visa. "When a refund authorization is declined, we still try to process the refund."
- **Unreferenced refunds** (a refund with card or bank details and no original payment) need approval from Adyen and report through `REFUND_WITH_DATA`.
- Refund validation failures name disputes explicitly, for example `Already partially disputed, new requested refund amount too high`: a chargeback reduces the same payment balance a refund draws on.
- A refund can fail for lack of merchant funds: `Insufficient in-process funds on account`.

### 2.4 Authorisation types, adjustment and expiry

- "By default, Adyen handles all card payment requests as final authorizations. You can manually specify the authorization type as `additionalData.authorisationType`:**PreAuth** or `additionalData.authorisationType`:**FinalAuth** in each payment request" [VERIFIED: https://docs.adyen.com/online-payments/adjust-authorisation.md, n.d., accessed 2026-11].
- **Pre-authorization** "verifies that the shopper's account is valid and has sufficient funds to cover a transaction, but does not debit the account … It allows you to increase or decrease the initially authorized amount at a later point in time." **Final authorization**: "the final amount is agreed up front and the transaction will be captured in full" [same page].
- **Two adjustment modes.** Asynchronous: the merchant refers to the pre-authorization's PSP reference and learns the outcome from a webhook. Synchronous: the merchant passes an `adjustAuthorisationData` blob "from one request to the next, to enable us to keep track of the latest amount"; "If at any point you fail to pass the blob, the flow falls back to asynchronous adjustment, and it is no longer possible to return to synchronous adjustment for that payment" [same page]. From v72 the `/amountUpdates` response status is **authorised** or **refused** when the blob is sent, and **received** otherwise [VERIFIED: release-notes page, entry of 2026-09-18].
- The amount in an adjustment is the new total, not a delta: "This is the sum of the pre-authorized amount and the additional amount" [VERIFIED: adjust-with-preauth page].
- Availability depends on scheme and merchant category code: Visa, Mastercard and American Express allow it for "All MCCs except 5542"; "It is ultimately up to the issuing bank whether they allow it"; "You can only adjust authorizations for payments acquired by Adyen" [VERIFIED: adjust-authorisation page].
- **Expiry on Adyen's side**: "For the global card schemes, Adyen expires (pre-)authorization requests automatically after 28 days from the day the payment is authorized." An `EXPIRE` webhook reports it [VERIFIED: adjust-authorisation and webhook-types pages].
- **Expiry on the scheme's side** differs, and Adyen publishes a table per scheme, including: Mastercard final authorization 7 days, pre-authorization 30 days; Visa card-present 5 days, cardholder-initiated card-not-present 10 days, merchant-initiated 5 days, pre-authorization for lodging, cruise and vehicle rental 30 days, MCC 5542 (automated fuel) 2 hours; American Express 7 days; Cartes Bancaires 12 days; Discover 10 days; JCB 1 year ⚠ [VERIFIED: adjust-authorisation page].
- Capturing after scheme expiry is possible and risky: it "increases the risk of: A failed capture. Increased interchange fees. Card scheme transaction fees. A cardholder-initiated chargeback for 'No Authorization' or 'Late Presentment' reasons" [same page].
- **Partial authorization** is a distinct result (`PartiallyAuthorised`), offered when "the cardholder has insufficient funds" and the merchant accepts partial amounts [VERIFIED: result-codes page].

### Stripe vs Adyen (modifications)

| Aspect | Adyen (documented) | Stripe | Suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Capture, refund, cancel | Each is a new request with its own `pspReference`, answered `received`, resolved by webhook, possibly failing days later with a second event | See the Stripe brief (capture is a call on the PaymentIntent; a Refund is an object with its own status) | Adyen exposes the two-stage nature of card clearing in its API contract; whether Stripe hides more of it is for the Stripe brief to establish |
| "Cancel or refund, I don't know which" | A dedicated reversal endpoint, and a cancel by merchant reference valid for 24 hours | Nothing fetched in this session | Adyen designed explicitly for the unknown-outcome case |
| Scheme authorization validity table | Published per scheme, with MCC exceptions | Not fetched in this session | — |

### For readers new to payments

- **Authorisation**: the issuer's promise to hold funds on the cardholder's account for a merchant; no money has moved yet.
- **Capture**: the merchant's claim on an authorised amount, which sends the transaction to be cleared and settled.
- **Pre-authorisation versus final authorisation**: a pre-authorisation holds an estimated amount that may change before capture (hotels, car rental); a final authorisation holds the exact amount that will be captured.
- **Reversal (Adyen's sense)**: one request that cancels a payment if it is not yet captured and refunds it if it is.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- A consumer's state machine for an Adyen payment needs states for "capture requested", "capture accepted" and "capture failed after acceptance", and the same three for refunds. Treating CAPTURE `success: true` as "money received" is the mistake the documentation is written to prevent.
- Because successful settlement is not evented, "settled" can only be established from the settlement reports. This is the direct link from chapter 08 to chapter 15 (reconciliation).
- The per-payment balance (authorised minus captured minus cancelled; captured minus refunded minus charged back) is the business-level guard against double refunds and over-captures, and it works without any idempotency key.

---

## PART 3: API families and their conventions (chapters 17, 11, 47)

### 3.1 The families

Adyen describes "different layers (internal and external) and families (payments, banking, platform) of REST APIs sitting on top of a large dynamic platform" [VERIFIED: https://www.adyen.com/knowledge-hub/api-first-adyen, published 2022-09-27] **(evidence age: 4 years; the current OpenAPI repository confirms the grouping)**. The OpenAPI repository held 129 specification files across about 50 services on 17 November 2026 [VERIFIED: https://github.com/Adyen/adyen-openapi, `json/` directory listing via api.github.com, accessed 2026-11]. The families a chapter writer needs:

| API | Latest version ⚠ | Test host and path | Live host | Purpose |
| --- | --- | --- | --- | --- |
| Checkout API | v72 | `checkout-test.adyen.com/v72` | `{PREFIX}-checkout-live.adyenpayments.com/checkout/v72` | Online payments, sessions, modifications, payment links, stored payment methods |
| Classic Payment API | v68 (inactive) | `pal-test.adyen.com/pal/servlet/Payment/v68` | `{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payment/v68` | `/authorise`, `/capture`, `/refund`, `/cancel`, `/cancelOrRefund`, `/adjustAuthorisation`, `/technicalCancel` |
| Management API | v3 | `management-test.adyen.com/v3` | `management-live.adyen.com/v3` | Company and merchant accounts, stores, terminals, API credentials, webhooks |
| Configuration API (Balance Platform) | v2 | `balanceplatform-api-test.adyen.com/bcl/v2` | `balanceplatform-api-live.adyen.com/bcl/v2` | Account holders, balance accounts, payment instruments, sweeps, transaction rules |
| Transfers API | v4 | `balanceplatform-api-test.adyen.com/btl/v4` | `balanceplatform-api-live.adyen.com/btl/v4` | Transfers, transactions, grants |
| Legal Entity Management API | v4 | `kyc-test.adyen.com/lem/v4` | `kyc-live.adyen.com/lem/v4` | Legal entities, documents, transfer instruments, onboarding links |
| Terminal API | nexo protocol 3.0 | `device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` or `/async` (cloud), or the terminal's IP address (local) | Regional `device-api-live-*.adyen.com` | In-person payments |

[VERIFIED: `info` and `servers` blocks of CheckoutService-v72.json, PaymentService-v68.json, ManagementService-v3.json, BalancePlatformService-v2.json, TransferService-v4.json, LegalEntityService-v4.json, TerminalAPI-v1.json in https://github.com/Adyen/adyen-openapi, accessed 2026-11]

Other services in the repository include Recurring (v25–v68), Payout (v30–v68), BinLookup (v40–v54), Disputes (v30), Stored Value (v46), Capital, Foreign Exchange, Open Banking, Data Protection, Session Authentication, and the classic platform APIs (Account, Fund, Hop, NotificationConfiguration, all at v6) [VERIFIED: same directory listing]. The Balance Platform's Configuration API is named `BalancePlatformService` in the repository and "Configuration API" in its title.

### 3.2 The live URL prefix per company

- "Each company account is provided with a unique hostname to communicate with Adyen's APIs. By connecting to this merchant-specific hostname, Adyen has more control over the routing of transactions. This allows Adyen to improve service robustness and availability for our merchants" [VERIFIED: https://docs.adyen.com/development-resources/live-endpoints.md, n.d., accessed 2026-11].
- "The live URL prefix is a string composed of a hex-encoded random part and your company name", for example `1797a841fbb37ca7-AdyenDemo` [same page].
- "By default, all transactions for a merchant-specific endpoint are routed to the same infrastructure as the standard endpoint, however in case of an infrastructure problem on the standard endpoint, especially if the cause is outside of Adyen's scope of control, alternative routing can be enabled to backup infrastructure and new infrastructure can be provisioned on demand" [same page].
- Location-based live endpoints exist ("for example, US or AU data centers") and are set up by Support; the client library must then load from the matching regional URL [same page].
- Only the payments-era APIs use the prefix. The Management, Configuration, Transfers and Legal Entity Management APIs use fixed live hosts (table above) [VERIFIED: OpenAPI `info` blocks].
- Network guidance on the same page: MTU 1500 bytes, and "Adyen endpoints have a 60-second time-out for inactive HTTP connections with keepalive enabled".

### 3.3 Conventions differ by family

The specifications show three generations of convention living side by side [VERIFIED for each cell: the named OpenAPI files, accessed 2026-11; the label "three generations" is ASSUMPTION/JUDGEMENT]:

| Convention | Checkout API v72 (and classic Payment v68) | Management API v3 | Configuration API v2 / Transfers API v4 |
| --- | --- | --- | --- |
| Style | Commands: 25 of 31 operations are POST, including reads such as `POST /paymentMethods` | Resources: 69 GET, 55 POST, 29 PATCH, 13 DELETE over nested paths such as `/companies/{companyId}/webhooks/{webhookId}` | Resources: `/accountHolders/{id}`, `/balanceAccounts/{id}`, `/transfers/{id}` with GET, POST, PATCH, DELETE |
| Identifier | `pspReference`, 16 alphanumeric characters, one per request | `companyId`, `merchantId`, `storeId`, `webhookId` | Prefixed identifiers in the examples: `AH…` (account holder), `BA…` (balance account), `PI…` (payment instrument), `LE…` (legal entity), `SE…` (transfer instrument), `TR…` (transaction rule), `SW…` (sweep), `EV…` (transfer event), mostly 25 characters long |
| Tenant in the request | `merchantAccount` in the body of every request | In the path | Implied by the credential; `balancePlatform` as a filter |
| Pagination | None (no list endpoints) | Page-based: `pageNumber` and `pageSize`; response has `itemsTotal`, `pagesTotal` and `_links` with `first`, `last`, `next`, `prev`, `self` | Configuration: `offset` and `limit`, response has `hasNext` and `hasPrevious`. Transfers: "cursor-based pagination" with `cursor` and `limit`, and links to next and previous pages |
| Error body | `status`, `errorCode`, `message`, `errorType` (one of `internal`, `validation`, `security`, `configuration`), `pspReference` | Problem-details shape: `type`, `title`, `status`, `detail`, `errorCode`, `instance`, `invalidFields`, `requestId` | Same problem-details shape (`RestServiceError`) |
| Request identifier in errors | `pspReference` | `requestId`, described as "A unique reference for the request, essentially the same as `pspReference`" | `requestId` |
| Authentication | `X-API-Key`; the classic API also accepts basic authentication with a `ws@Company.…` user | `X-API-Key` | `X-API-Key` |
| Amounts | Minor units with a currency code ("20000 is 200 euros") | — | Minor units |

- The error fields for the payments family are also documented in prose, including "If the `pspReference` is not present in the response body, check the HTTP headers of the response" and "The maximum request size is 10 MB" [VERIFIED: https://docs.adyen.com/development-resources/response-handling.md, n.d., accessed 2026-11].
- 4xx and 5xx responses mean the request left no trace: "the Adyen payments platform does not accept or store submitted requests" when it fails validation, a security constraint, a configuration constraint, or on an internal error. "There is no charge for rejected payment requests accompanied by an error message" [same page].
- A payment **refusal is not an error**: it is HTTP 200 with `resultCode` Refused and a `refusalReason` [same page].
- The Checkout API has no generic free-form expansion of related objects, and the specification defines none [VERIFIED: CheckoutService-v72.json has no `expand`-style parameter; only three query parameters exist in the whole API: `merchantAccount`, `sessionResult`, `shopperReference`]. Extra data is switched on per account and delivered in an `additionalData` map of string keys such as `additionalData.manualCapture`; for webhooks the merchant selects "additional settings" in the Customer Area [VERIFIED: capture page; https://docs.adyen.com/development-resources/webhooks/configure-and-manage.md, n.d., accessed 2026-11].
- A `metadata` field exists on payments and sessions; v72 added validation of it, and on payment links "more than 80 characters will result in a validation error" (v71) [VERIFIED: release-notes page, entries 2026-04-15 and 2023-11-01].

### 3.4 Account structure behind the API

"With Adyen, you have a single company account, and one or more sub-accounts called merchant accounts." "Your payments are processed in sub-accounts called merchant accounts. The merchant account is where you receive the payout of funds, as well as the reports used for reconciliation." Stores sit under merchant accounts for point of sale, and account groups collect merchant accounts for user access [VERIFIED: https://docs.adyen.com/account/account-structure.md, n.d., accessed 2026-11]. Credentials, webhooks, idempotency keys and the live prefix all attach to the company account (PARTS 4, 6, 7).

### 3.5 Terminal API (chapter 11)

- "The architecture of Terminal API is determined by the nexo Sale to POI Protocol Specifications." A request is a JSON `SaleToPOIRequest` with a `MessageHeader` and a body such as `PaymentRequest`; the current protocol version is 3.0 [VERIFIED: TerminalAPI-v1.json in https://github.com/Adyen/adyen-openapi; https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api.md, n.d., accessed 2026-11].
- Two transports: **local** ("your POS system sends the request directly to the IP address of the terminal, and receives the result synchronously") and **cloud** ("your POS system sends the request to an Adyen endpoint, and Adyen forwards the request to the terminal"), the latter with `/sync` (hold the connection) or `/async` (result by event notification) [VERIFIED: TerminalAPI-v1.json].
- The request identity is nexo's, not an idempotency key: `ServiceID` is "Your unique ID for this request, consisting of 1-10 alphanumeric characters. Must be unique within the last 48 hours for the terminal (`POIID`) being used" [VERIFIED: terminal-api docs page].
- A terminal transaction has two identifiers, a **tender reference** "generated by the terminal" and a **PSP reference** "generated by the Adyen payments platform"; with offline or store-and-forward transactions over local communications "an approved payment will only generate a transaction identifier with the tender reference" [same page].
- Online and in-person payments report through the same Standard webhook and the same `pspReference` scheme [ASSUMPTION/JUDGEMENT from the shared webhook reference; see `brief-acquiring-methods-and-terminals.md` for the unified-commerce evidence].

### 3.6 OpenAPI as the source of truth, and generated libraries

- "Adyen's OpenAPI specifications are generated internally and published to Github for both our users and the tools we offer." "Whenever a new API version is released, we publish the corresponding OpenAPI file on Github." "From the OpenAPI specification files we create services, models, documentation and code snippets. The source code is reviewed, tested and merged into the existing libraries, and swiftly released." Stated aim: "general availability across all API Libraries within 2 weeks of new releases" [VERIFIED: https://www.adyen.com/knowledge-hub/adyen-api-libraries, published 2023-03-28] **(evidence age: 3.6 years; confirmed by the current repositories below)**.
- The generation tooling is public: `Adyen/adyen-sdk-automation` is "a set of Gradle build scripts to generate code for `Adyen/adyen-*-api-library` repositories", pinning OpenAPI Generator versions per language (the README shows 5.4.0 for Node and 7.11.0 for Java and .NET) [VERIFIED: https://github.com/Adyen/adyen-sdk-automation README, accessed 2026-11].
- The specifications carry Adyen vendor extensions: `x-addedInVersion`, `x-deprecatedInVersion` and `x-deprecatedMessage` ("a human-readable message explaining what to use instead"), `x-groupName` and `x-sortIndex` for the API Explorer, and `x-publicVersion` [VERIFIED: https://github.com/Adyen/adyen-openapi README, accessed 2026-11].
- Server libraries: Java, PHP, Node.js, .NET, Go, Python, Ruby, and "Apex (beta)" [VERIFIED: `info.description` of CheckoutService-v72.json]. They "use semantic versioning"; a library release states which API versions it wraps (the Java library README lists Checkout v72, Management v3, Configuration v2, Transfers v4, Legal Entity Management v4, classic Payments v68) [VERIFIED: https://docs.adyen.com/development-resources/versioning.md, n.d.; https://github.com/Adyen/adyen-java-api-library README, accessed 2026-11].
- Postman collections "are automatically generated based on the latest adyen-openapi definition files" and published in the AdyenDev Postman workspace [VERIFIED: https://github.com/adyen/adyen-postman README, accessed 2026-11].
- An **API Diff Tool** compares any two versions of an API (announced on the tech blog on 2025-08-19) [VERIFIED: versioning page for the tool; https://medium.com/feed/adyen for the date].

### 3.7 What Adyen has published about how it designs APIs

One article, from 2022 **(evidence age: 4 years; no newer statement found)** [VERIFIED: https://www.adyen.com/knowledge-hub/api-first-adyen, published 2022-09-27]:

- "The outcome is a company-wide culture where APIs are products, teams are the owners and everyone plays a part in shaping the API strategy."
- There is an **API Review group**: "Governance sets the tone but doesn't take all decisions. The API Review group recruits API stakeholders and champions to establish best practices and help teams to make good decisions (typically at design time) but does not dictate how and when things get done."
- "Open standards (OpenAPI, REST, JSON) play a pivotal role, but our tech stack is open source or built in-house: we have created our own frameworks to empower development teams."
- Design tooling named: Stoplight for design, Postman for testing.
- On deprecation: "It is consistently applied both to the OpenAPI specifications and the documentation while the deprecated elements are deleted only after one or more versions."
- The article cites an external award (TSG "Overall API Assessment", 2022) [same source; the award itself was not verified at TSG].

Nothing public was found on Adyen's internal API gateway, request routing, or the frameworks the article mentions.

### Stripe vs Adyen (API design)

| Aspect | Adyen (documented) | Stripe (fetched for contrast) | Suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Shape | Several API families with different hosts, version counters, pagination and error formats | One API with resource objects; "All top-level API resources have support for bulk fetches"; cursor pagination with `starting_after` / `ending_before` [VERIFIED: https://docs.stripe.com/api/pagination.md, n.d., accessed 2026-11] | Adyen's surface shows its history: a payments API from the SOAP era, and resource-style APIs added with the platform and banking products. Stripe's shows one design applied throughout |
| Identifiers | Opaque 16-character `pspReference` for payments; prefixed IDs (`AH`, `BA`, `PI`, `LE`) only in the newer platform APIs | Prefixed object IDs everywhere (see the Stripe brief) | Adyen adopted the prefixed-ID convention late and only for new families |
| Reading state | No GET for payments | GET on every resource | See PART 1 |
| Published design process | One 2022 blog post naming an API Review group | See the Stripe brief | Adyen has published far less about how it designs APIs |
| Machine-readable contract | Full OpenAPI 3.1 for every version of every API, public since 2017, with deprecation extensions | See the Stripe brief (Stripe also publishes an OpenAPI specification) | Adyen's versioned specification archive is unusually complete: all 18 public Checkout versions from v37 to v72 are present |

### For readers new to payments

- **Merchant account (Adyen's sense)**: the sub-account under a company in which payments are processed, paid out and reported; every payment request names one.
- **nexo**: an international standard for messages between a point-of-sale system and a payment terminal; Adyen's Terminal API follows it.
- **Minor units**: an amount written as an integer in the currency's smallest unit, so EUR 10.00 is `1000`.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- An adapter over Adyen must speak several dialects: page-number, offset and cursor pagination, and two error formats. Generated libraries hide most of this; a hand-written HTTP client does not.
- The company-specific hostname is a routing lever on Adyen's side (it can move one company's traffic by DNS without touching others) and a configuration item on the integrator's side that differs between test and live.
- Because the contract is a published OpenAPI file per version, an integrator can diff versions mechanically before an upgrade; chapter 19 can use this as the constructive counterpart to Stripe's changelog.

---

## PART 4: Idempotency (chapter 18)

Adyen documents idempotency on one page [all VERIFIED: https://docs.adyen.com/development-resources/api-idempotency.md, n.d., accessed 2026-11, unless another source is named].

**The mechanism**

- Header: `idempotency-key:<key>`. "The `<key>` is a unique identifier for the message with a maximum of 64 characters. We recommend using a UUID."
- Which requests: "The Adyen API supports idempotency on POST requests (other request types such as GET, DELETE and PUT are idempotent by definition)."
- Replay: "If the Adyen payments platform already processed the request, the response to the first attempt will be returned without duplication."
- Confirmation: "To verify that a request was processed idempotently, check the `idempotency-key` HTTP header returned in the response."
- "Make sure that you code for case-insensitive HTTP headers."

**Scope and lifetime**

- "Keys are stored at a company account level. The system checks that the idempotency keys are unique to the company account."
- "Idempotency keys are valid for a period of 7 to 14 days after first submission." The page does not say what determines the point within that range.
- "If you are targeting multiple regional endpoints simultaneously, idempotency keys will not be checked for duplication in other regions."

**Security consequence of company-level scope**

- "Generate unique idempotency keys per request using the **version 4 (random)** UUID type to prevent two API credentials under the same account from accessing each others responses."
- "Lowering the access level for an API credential does not prevent them from retrieving past responses if the user still has access to previously used keys."

**Concurrent requests and transient errors**

- "it could come from a race condition of sending two payment requests with the same idempotency key at the same time. One will end up being processed while the other will return a transient error."
- "The response will contain an HTTP header **transient-error** with the value **true**, which indicates that the request can be retried at a later time using the same idempotency key. If the API does not return a transient error header, or returns a header with a value of false, do not retry the request."
- "If you submit a duplicate request before the first request has completed, the API returns an **HTTP 422 – Unprocessable Entity** or **HTTP 409 - Conflict** status with the error code **704: "request already processed or in progress"**."
- The HTTP status table describes 409 as "Resource is locked. A conflict occurred because the request was already processed or is in progress" [VERIFIED: https://docs.adyen.com/development-resources/response-handling.md, n.d., accessed 2026-11].

**When the idempotency store is down**

- "To enable idempotent behavior, Adyen must retain a consistent, stateful data store to compare each request against. Idempotent processing relies on this data store being available. In the unlikely event that this data store should become unavailable, the API returns an **HTTP 503 – Service Unavailable** status with the error code **703: "required resource temporarily unavailable"**. The system marks the request as a transient error."
- The advice that follows is unusual and worth quoting in chapter 18: "you can either: Pause processing and retry the requests later (if this is feasible). Fall back to non-idempotent processing by not submitting the `idempotency-key` HTTP header."

**Retries**

- "Use an exponential backoff strategy when retrying transactions to avoid flooding the API and running into rate-limiting."
- For HTTP 429 the status-code page recommends "a retry mechanism that uses exponential backoff with jitter" [VERIFIED: response-handling page].

**Idempotency is presented as the second line of defence**

- The page opens with the business rules: "The accounting rules in the Adyen payments platform take care of most potential double-processing issues that can impact payment modifications", naming two: with partial captures "it is not possible to capture a higher amount than the authorized one", and "by default the total refunded value cannot exceed the captured amount."
- It then lists webhooks as a remedy for lost responses: "this approach helps keep track of missing responses, a common consequence of a data transmission timeout."

**What the specifications add**

- The `Idempotency-Key` header is declared on 22 of the 25 POST operations of Checkout API v72 (all except `/calculateTax`, `/validateShopperId` and `/verifyShopperTaxIdentification`) and on 5 of the 6 POST operations of Transfers API v4. It is **not declared** in the specifications of the Management API v3, Configuration API v2, Legal Entity Management API v4 or the classic Payment API v68 [VERIFIED: the named files in https://github.com/Adyen/adyen-openapi, accessed 2026-11]. Whether those APIs honour the header anyway is not stated; the prose page says "the Adyen API" without listing APIs [ASSUMPTION/JUDGEMENT: absence from a specification does not prove the header is ignored].

**What is not documented**

- **A reused key with a different request body.** The page does not say whether Adyen compares the new request with the original, returns the first response regardless, or returns an error. This was checked against the idempotency page, the HTTP status page and the error-code list (which has only 703 and 704 for idempotency).
- Whether a stored response includes error responses (for example a 500), and from which moment a key counts as "first submitted".
- How the store is implemented, how keys expire, and how the 7–14 day range arises. Nothing was found on the tech blog (PART 8).
- Terminal API: no idempotency key; nexo's `ServiceID` uniqueness rule (48 hours per terminal) and the transaction status request play that role (section 3.5).

### Stripe vs Adyen (idempotency)

| Aspect | Adyen (documented) | Stripe (documented) | Suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Header and length | `idempotency-key`, max 64 characters | `Idempotency-Key`, "up to 255 characters long" | — |
| Key lifetime | "7 to 14 days" | API v1: keys can be removed "after they're at least 24 hours old" | Adyen's window covers a retry after a weekend outage; Stripe's covers a retry storm. A job that retries on Monday what failed on Friday is safe on Adyen and not on Stripe v1 |
| Scope | Company account, per region; shared across API credentials | See the Stripe brief | Adyen's scope makes key guessing a cross-credential leak, hence the v4 UUID advice |
| Same key, different parameters | Not documented | "The idempotency layer compares incoming parameters to those of the original request and errors if they're not the same" | Stripe documents request fingerprinting; Adyen's behaviour must be tested, not assumed |
| Concurrent duplicate | 422 or 409 with error 704, and a `transient-error: true` header that says whether to retry | See the Stripe brief | Adyen gives the client an explicit machine-readable retry signal |
| Stored result | "the response to the first attempt will be returned" | v1 saves "the status code and body of the first request … including `500` errors"; API v2 retries failed work to completion | Stripe has published a second-generation semantics (v2); Adyen has one |
| Store unavailable | 503 with error 703; documented option to drop the header | Not fetched | Adyen tells integrators that availability and exactly-once are in tension and lets them choose |
| Published implementation | None found | Engineering posts (see the Stripe brief; dated, flag age) | Chapter 18's "how a server implements it" section rests on Stripe's publications and on inference for Adyen |

[Stripe cells VERIFIED: https://docs.stripe.com/api/idempotent_requests.md, n.d., accessed 2026-11]

### For readers new to payments

- **Idempotency key**: a unique value the client attaches to a request so that the server performs the operation once however many times the request is sent.
- **Transient error**: a temporary failure with no side effects, after which the same request can safely be sent again.
- **Unknown outcome**: the state after a timeout, when the client cannot tell whether the provider processed the request.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- The statement that the idempotency store is "a consistent, stateful data store" whose unavailability yields 503 implies a design that fails closed: Adyen refuses the request rather than risk a duplicate, and hands the availability decision to the merchant.
- Region-local keys imply the store is not globally replicated in the request path; an integrator that fails over between regional endpoints loses duplicate protection at exactly the moment it is most likely to retry.
- Deriving the key from business identity (order ID plus attempt number) conflicts with Adyen's advice to use random v4 UUIDs. The reconciliation: store a random key per logical attempt in your own database before the first send, and reuse that stored key on every retry.
- For modifications, the payment-balance rules mean a duplicated full capture or full refund fails validation even without a key; a duplicated *partial* refund does not, so partial operations need keys.

---

## PART 5: API versioning and deprecation (chapter 19)

### 5.1 Version in the URL, one counter per API

- "Each API URL contains a version suffix starting with either "v" or "V" character followed by a whole number to indicate the API version. We increment the number for every version, but we may skip numbers when needed" [VERIFIED: https://docs.adyen.com/development-resources/versioning.md, n.d., accessed 2026-11].
- "Most integrations use multiple Adyen APIs … Each API has a different version" [same page].
- The version is chosen by the caller in every request URL; there is no account-level default version and no version header in the Checkout API [VERIFIED: `info.description` of CheckoutService-v72.json: "Checkout API supports versioning using a version suffix in the endpoint URL"].
- "In some cases, we may introduce a new API version without visible changes to API consumers. We do so to improve stability and consistency of our APIs, or to implement some groundwork for bigger changes in the future" [versioning page].

### 5.2 What counts as breaking depends on the API's generation

"We categorize our APIs into two types: *new* or *classic* APIs." Classic APIs are Payment, Recurring, Payout and BinLookup; "All other APIs … are new APIs, such as Checkout and Balance Platform" [versioning page].

| Change | New APIs | Classic APIs |
| --- | --- | --- |
| Adding a new endpoint; adding an optional request field or header; adding a response header | Non-breaking | Non-breaking |
| **Adding any field to a response body** | **Non-breaking** | **Breaking** |
| Changing the text of an error message; adding a new HTTP status code | Non-breaking | Non-breaking |
| Deprecating a field (in documentation) | Non-breaking | Non-breaking |
| Adding a required request field or header; removing an endpoint, field or header | Breaking | Breaking |
| Changing an HTTP status code or an error code of an existing error | Breaking | Breaking |
| Renaming a field; changing a field's type; optional→required in a request; required→optional in a response | Breaking | Breaking |
| "Changing the behavior in a way that requires API consumers to change their integration" | Breaking | Breaking |

[VERIFIED: versioning page]

- Method: "for our REST APIs, we follow the API expand-contract pattern to add new elements without changing the version" [same page].
- Non-breaking changes go to every version: "We implement non-breaking changes in all versions of an API, so that you benefit from it without having to upgrade your API version" [same page]. The release notes confirm it: most dated Checkout API entries carry no version number, and some say "For v72 or later" for a change applied only from one version up [VERIFIED: release-notes page, entry of 2026-09-18].
- "For our Checkout API, we only release major versions" [VERIFIED: https://docs.adyen.com/online-payments/upgrade-your-integration.md, n.d., accessed 2026-11].
- Consequence the documentation states for receivers: "you should set up your server to be able to accept webhooks of more types and receive more event type values than are listed" [VERIFIED: webhook-types page].

### 5.3 The lifecycle and the deprecation clock

Adyen publishes a four-state lifecycle for Checkout API versions and for each Drop-in/Components major version [VERIFIED: upgrade-your-integration page]:

| State | Checkout API | Drop-in/Components |
| --- | --- | --- |
| **Active** | "The latest major version" | The latest major version |
| **Inactive** | "only receives bug fixes and changes required to comply with new regulations" | Same |
| **Deprecated** | No fixes at all. "After a version reaches this state, you have **2 years** to upgrade" | "you have **1 year** to upgrade" |
| **End-of-Life** | "you no longer receive support from Adyen and payment processing can be suspended anytime" | Same |

- The reason given: "We deprecate older versions to protect your data and maintain compliance with financial regulations" [same page].
- The general versioning page still says, more softly: "if you decide stay in your current version, you can continue to do so. We maintain older versions of our APIs that you can continue to use until you are ready to upgrade" [versioning page]. The two statements are not reconciled in the documentation; the lifecycle page is the more specific and applies to Checkout [ASSUMPTION/JUDGEMENT].
- **Dated removals found**: "Checkout API v37 is no longer supported … Features that were previously available from v37 now apply from v40" (release note of 2026-09-18). Web Drop-in/Components 4.x releases are marked "Deprecated … will be End-of-Life on August 1, 2026" (a date already past on the day of access, so the label had not been updated), and iOS 3.x releases "End-of-Life since October 1, 2025" ⚠ [VERIFIED: release-notes page].
- Which Checkout API versions are Inactive or Deprecated today is shown only in the API Explorer and could not be read (Research limitation).
- The Transfers API states in its own description: "Versions 1 and 2 of the Transfers API are deprecated" [VERIFIED: TransferService-v4.json].
- The classic Payment API as a whole is labelled "inactive" and points to the Checkout lifecycle [VERIFIED: PaymentService-v68.json].

### 5.4 Client libraries and API versions are coupled

- Each client-library version requires a minimum API version: "Web Drop-in/Components v5.0.0 is only compatible with Checkout API v68 or later"; every Web release note opens with "This release requires Checkout API v69 or later" (6.48.1, 2026-11-05) ⚠ [VERIFIED: upgrade-your-integration and release-notes pages].
- Mobile has compatibility tables: iOS Drop-in 5.5.0–5.13.0 needs Checkout v71; Android 5.1.0 and later needs v71 [VERIFIED: upgrade-your-integration page].
- Server libraries hide the API version: "Each library provides classes and methods that lets you use multiple Adyen APIs without needing to know the API versions. Instead, you need to consider the library version" [versioning page].

### 5.5 Webhook versions

- Webhooks are versioned separately from the API that triggered them. The webhook configuration has a "**Version**: The webhook version" setting [VERIFIED: https://docs.adyen.com/development-resources/webhooks/configure-and-manage.md, n.d., accessed 2026-11].
- The repository holds versioned webhook specifications: payments `Webhooks` v1 (51 webhook definitions), Transfer webhooks v3–v4, Configuration webhooks v1–v2, Transaction webhooks v4, Management webhooks v1–v3 [VERIFIED: https://github.com/Adyen/adyen-openapi directory listing].
- New fields arrive within a webhook version with a marker: `sequenceNumber` and `events` on transfer webhooks carry `x-addedInVersion: 3` [VERIFIED: BalancePlatformTransferNotification-v4.json].
- No statement was found on how long old webhook versions are delivered, or on whether changing the API version of a request changes the webhook payload.

### Stripe vs Adyen (versioning)

| Aspect | Adyen (documented) | Stripe (fetched for contrast) | Suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Where the version lives | In the URL path, per API, chosen per request | In the account ("default API version") or the `Stripe-Version` header, for example `2026-10-28.endive` [VERIFIED: https://docs.stripe.com/upgrades.md, n.d., accessed 2026-11] | Adyen's version is visible in code and logs; nothing changes unless the integrator edits a URL or upgrades a library. Stripe's can be implicit in the account |
| Format | Integer per API (v72, v3, v4) | Date plus release name | — |
| Cadence | Checkout: 18 public versions in 8 years; 29 months between v71 and v72 | See the Stripe brief (named major releases and monthly additive releases) | Adyen ships most change as additive updates to all versions and saves version bumps for removals |
| Forced upgrade | Documented: 2 years after "Deprecated", then "payment processing can be suspended anytime" | See the Stripe brief | Adyen publishes an explicit end date policy for the payments API |
| Webhook payload version | A per-webhook "Version" setting | Tied to the API version of the endpoint; the upgrade guide describes running two endpoints during migration [VERIFIED: same Stripe page] | Both decouple webhook shape from request version in practice |
| Published mechanism for keeping old versions alive | None found | Engineering post on version-change modules (see the Stripe brief; dated) | The cost side of chapter 19 has public evidence only from Stripe |

### For readers new to payments

- **Breaking change**: a change to an API after which an existing integration stops working unless its code is changed.
- **Expand-contract**: adding the new form of something alongside the old, moving users over, and only then removing the old.
- **End-of-life**: the date after which a version is no longer supported and may stop working.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- The rule "adding a response field is non-breaking" obliges every integrator to parse leniently; a strict deserialiser on a new-API response is a latent outage. The classic APIs promised the opposite, which is one reason they needed a new version number for every addition and reached v68.
- A URL version makes the Version Cliff (the Larkfield thread) a dated, announced event rather than a silent one, but the coupling between client library versions and API versions means a front-end upgrade can force a back-end upgrade.

---

## PART 6: Webhooks (chapter 20)

### 6.1 Two payload shapes

**Payments webhooks ("Standard webhook")** [VERIFIED: https://docs.adyen.com/development-resources/webhooks/webhook-types.md, n.d., accessed 2026-11]:

- Top level: `live` ("whether the event happened on the test or live environment") and `notificationItems`, "An array of `NotificationRequestItem` objects".
- "JSON and HTTP POST webhooks contain only one `NotificationRequestItem` object in the `notificationItems` array. SOAP webhooks may contain up to six `NotificationRequestItem` objects, in case the events happen within a very short period of time."
- Item fields: `eventCode`, `success` ("either **true** or **false**"), `eventDate` (ISO 8601), `pspReference`, `originalReference` (on modifications), `merchantAccountCode`, `merchantReference`, `amount`, `paymentMethod`, `reason`, `additionalData` [VERIFIED: same page; `Webhooks-v1.json` in https://github.com/Adyen/adyen-openapi].
- Default event codes "cannot be disabled" and fall into transaction events (AUTHORISATION, CAPTURE, CAPTURE_FAILED, CANCELLATION, CANCEL_OR_REFUND, REFUND, REFUND_FAILED, REFUNDED_REVERSED, EXPIRE, REPORT_AVAILABLE, …), dispute events (NOTIFICATION_OF_CHARGEBACK, CHARGEBACK, CHARGEBACK_REVERSED, SECOND_CHARGEBACK, PREARBITRATION_*, NOTIFICATION_OF_FRAUD, …) and payout events.
- Delivery format is a setting: "JSON, HTTP POST, or SOAP" [VERIFIED: configure-and-manage page].

**Platforms webhooks** (Balance Platform: configuration, transfer, transaction, balance, report and others) [VERIFIED: webhook-types page; https://docs.adyen.com/platforms/webhook-types.md, n.d., accessed 2026-11]:

- Top level: `data`, `environment` ("**test** or **live**"), `timestamp`, `type`.
- Event types are dotted names: `balancePlatform.accountHolder.created`, `balancePlatform.balanceAccount.updated`, `balancePlatform.transfer.created`, `balancePlatform.transfer.updated`.
- "Webhook messages contain a snapshot of the resource so your system can update its state accordingly" [VERIFIED: https://docs.adyen.com/development-resources/webhooks.md].

Adyen's own summary of the split: "In Payments webhooks, the event type is typically in the `eventCode` field. In Platforms webhooks, the event type is typically in the `type` field" [webhook-types page].

### 6.2 Transfer webhooks carry their own ordering and history

- `balancePlatform.transfer.created` is sent "when there are fund movements on your platform"; `balancePlatform.transfer.updated` "when the status of a transfer changes. Use the `data.id` to track the original transfer resource" [VERIFIED: BalancePlatformTransferNotification-v4.json in https://github.com/Adyen/adyen-openapi].
- `sequenceNumber`: "The sequence number of the transfer webhook. The numbers start from 1 and increase with each new webhook for a specific transfer. The sequence number can help you restore the correct sequence of events even if they arrive out of order" [same file].
- `events`: "The list of events leading up to the current status of the transfer", each with its own `id`, `status`, `bookingDate`, `valueDate` and `mutations` [same file]. The payload also carries `balances`.
- The transfer `status` enumeration has 71 values (`received`, `authorised`, `booked`, `captured`, `refunded`, `chargeback`, `failed`, `returned`, …) [VERIFIED: TransferService-v4.json].

### 6.3 Acceptance: what counts as delivered

- Current rule: "We require you to acknowledge every webhook event with a successful HTTP response status code, for example **200** or **202**. If we do not receive this response within 10 seconds for an reason, such as your server is down or your service is unavailable, all webhook events to your endpoint go to the retry queue" [VERIFIED: configure-and-manage page].
- Three terminal-management webhooks accept only 200 [VERIFIED: https://docs.adyen.com/development-resources/webhooks/handle-webhook-events.md, n.d., accessed 2026-11].
- **The rule changed in 2024.** Before: "All integrations built with Adyen have been accepting webhooks by responding with a response body containing the string '[accepted]'." After: "all webhook handlers must respond only with a successful HTTP status code (2XX)." "Every newly created webhook on the Adyen platform will work with the 2XX HTTP status code option"; "All existing webhooks, however, are not automatically updated and keep functioning as before" [VERIFIED: https://www.adyen.com/knowledge-hub/webhooks-accept-2xx, published 2024-05-01].
- Why it changed, in Adyen's words: "Exclusively relying on the content of the response body has presented scenarios where webhooks were successfully acknowledged even when responding with status codes in the 4XX and 5XX ranges … This has resulted in false negatives" [same article].
- Recommended handler order: verify, "Store the webhook message in your database or a queue so you can process it later", accept, then process; "Make sure that you acknowledge the webhook before applying any business logic, because errors in your business logic could lead to failing webhooks" [VERIFIED: handle-webhook-events page].
- Endpoint requirements: HTTPS with TLS 1.2 or 1.3 on ports 443, 8443 or 8843 in live; "publicly accessible without any redirects" [VERIFIED: configure-and-manage and handle-webhook-events pages].

### 6.4 The retry queue

[All VERIFIED: https://docs.adyen.com/development-resources/webhooks/troubleshoot.md, n.d., accessed 2026-11, unless noted] ⚠

- "We retry sending the webhook message a few more times before we set the status of the webhook to **Failing** and place the webhook into a retry queue."
- "From the retry queue, we automatically try to send the webhook for up to 30 days at the following retry intervals": 30 seconds, 30 seconds, 1 minute, 2 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 2 hours, 4 hours, 8 hours. The page does not say what happens after the twelfth interval; the natural reading is a retry every 8 hours until day 30 [ASSUMPTION/JUDGEMENT].
- "If a retry is successful, we continue with the next webhook in the queue."
- The queue is per endpoint and holds everything: when the first acknowledgement fails, "all webhook events to your endpoint go to the retry queue" [VERIFIED: configure-and-manage page].
- Recovery produces a burst: a 429 from the merchant "can happen after you fix a failing endpoint, as the queued webhooks are sent in a short timeframe. Ensure your server can handle the load."
- Manual controls in the Customer Area: **Retry** and **Ignore** ("permanently removed from the queue and cannot be retried").
- Alerts: "Adyen sends an alert after 5 retry attempts", again "after 7 days of a webhook failing", and on recovery.
- A disabled webhook also queues: "We will then queue all webhook events to this endpoint. You will receive the queued webhook events when you reactivate". "Webhook configurations that have been inactive for more than six months are automatically deleted" [VERIFIED: configure-and-manage page].
- "Multiple Adyen products use webhooks. Successfully receiving one type of webhook (for example, for a payment authorisation) does not guarantee successful delivery of all types."
- An earlier description, from 2023 **(evidence age: 3.8 years; superseded in detail by the schedule above)**: "The first retry occurs after a few minutes but the following attempts (until the acknowledgement is received) are scheduled with an increasing delay" [VERIFIED: https://www.adyen.com/knowledge-hub/consuming-webhooks, published 2023-02-02].

### 6.5 Duplicates, ordering and delay

- Duplicates: "In some cases it is possible that you receive the same webhook event twice, so make sure that your system is able to deal with duplicates. These duplicate webhook events have the same values in the `eventCode` and `pspReference` fields, while the `eventDate` and other fields can be different. Your server should use the details from the latest webhook event" [VERIFIED: handle-webhook-events page].
- There is **no event identifier** on a Standard webhook item; the deduplication key Adyen prescribes is the pair (`eventCode`, `pspReference`) [VERIFIED: same page; item fields in Webhooks-v1.json]. Platform transfer webhooks do carry identifiers (`data.id`, `sequenceNumber`, event `id`).
- Ordering: "To ensure you are processing events in the correct chronological order, always check the timestamp. Some webhooks also contain unique identifiers such as `sequenceNumber` that you can also use to handle the data in the correct order" [same page]. No page states that delivery order is guaranteed, and none states explicitly that it is not.
- Delay: "Webhook events are delivered with a certain delay (few seconds to minutes) … we strive to minimize the delay but often that depends on external factors (response from third-party systems)" [VERIFIED: consuming-webhooks article, 2023-02-02] **(evidence age: 3.8 years; no newer figure found)**.

### 6.6 Authenticating the sender

- Three mechanisms: **OAuth 2.0** ("strongly recommended and supported for the Standard webhook and all Balance Platform webhook types"; Adyen fetches a token from the merchant's identity provider and sends it with each event), **basic authentication** (all webhook types), and **HMAC signatures** [VERIFIED: https://docs.adyen.com/development-resources/webhooks/secure-webhooks.md, n.d., accessed 2026-11].
- "Basic authentication only guarantees that the webhook event was sent by Adyen, not that it wasn't modified during transmission" [same page].
- **Standard webhook HMAC signs eight fields, not the body.** The signed string is the colon-delimited concatenation of `pspReference`, `originalReference`, `merchantAccountCode`, `merchantReference`, `value`, `currency`, `eventCode`, `success`, with HMAC-SHA256 over the UTF-8 bytes using the hex-decoded key, Base64-encoded. The signature travels **inside the payload**, in `additionalData.hmacSignature` [VERIFIED: https://docs.adyen.com/development-resources/webhooks/secure-webhooks/verify-hmac-signatures.md, n.d., accessed 2026-11].
- Other webhooks sign the whole body and send the signature in a header: "For non-standard webhooks, the signature is calculated using the entire JSON payload. Instead of being included in the payload itself, the signature is provided in the HTTP Header `hmacSignature`", with a `protocol` header of `HmacSHA256` [VERIFIED: https://www.adyen.com/knowledge-hub/hmac-validation-guide, published 2025-06-16; verify-hmac-signatures page].
- "Each secret HMAC key is linked to one webhook endpoint"; test and live keys differ [verify-hmac-signatures page].
- Key rotation: "it can take some time to propagate this in our infrastructure, so make sure that you can still accept webhook events signed with your previous HMAC key for some time" [secure-webhooks page].
- No IP allowlist: "We do not provide a list of IP addresses." Use the domain `out.adyen.com`, or resolve it ("We recommend that you check every hour") [same page].
- A practical failure cause: "Check if any infrastructure (web servers, API gateways, proxies) between Adyen and your application could be altering the payload … capture the raw webhook body" [hmac-validation-guide article].
- The Standard webhook's signed fields include **no timestamp**, and no replay-tolerance window is documented. `eventDate` is outside the signed string [VERIFIED: the field list on the verify-hmac-signatures page]. That a captured Standard webhook could be replayed with a valid signature, and that deduplication on (`eventCode`, `pspReference`) is the only defence, is the analyst's reading [ASSUMPTION/JUDGEMENT].

### 6.7 Configuration and observability

- Scope: "You can configure Payments webhooks on the company, merchant account, and merchant account groups. You can configure Platforms webhooks on the company account level only." Adyen recommends company level, and "that you limit the number of webhooks you configure for each company account" for performance [VERIFIED: configure-and-manage page].
- "Each endpoint that you set up can receive only one type of webhook" [VERIFIED: webhook-types page].
- Webhooks are also managed by API: the Management API has `/companies/{companyId}/webhooks`, `/merchants/{merchantId}/webhooks`, and for each a `/generateHmac` and a `/test` operation [VERIFIED: ManagementService-v3.json].
- No copy from test to live: "Adyen does not provide a "copy" function for moving your webhook configurations from the test environment to the live environment" [configure-and-manage page].
- Webhook event logs keep 30 days: "a list of all your webhook events on the test environment in the past thirty days", with "Relevant timestamps and your response time" and "Request and response bodies" [VERIFIED: https://docs.adyen.com/development-resources/logs-resources/webhook-event-logs.md, n.d., accessed 2026-11].

### Stripe vs Adyen (webhooks)

| Aspect | Adyen (documented) | Stripe (documented) | Suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Acknowledgement | Any 2xx within 10 seconds (new webhooks since 2024-05); legacy webhooks need the body `[accepted]` | "Quickly returns a successful status code (`2xx`)" | Adyen states its timeout; and it carried a non-HTTP acknowledgement convention for years |
| Retry window | "up to 30 days", published interval list ending at 8 hours | "up to three days with an exponential back off in live mode"; three times over a few hours in a sandbox | Adyen's window is ten times longer; an endpoint down for a week loses nothing on Adyen and loses events on Stripe unless they are fetched from the API |
| Behaviour while failing | All events for the endpoint queue behind the failure; released in order when a retry succeeds | See the Stripe brief | Adyen's documented model is a per-endpoint queue with head-of-line blocking, which favours order over freshness |
| Ordering | "always check the timestamp"; `sequenceNumber` on transfer webhooks | "Stripe doesn't guarantee the delivery of events in the order that they're generated" | Stripe says so outright; Adyen implies it and adds a sequence number only in the newer family |
| Duplicates | Same `eventCode` and `pspReference`; "use the details from the latest" | "logging the event IDs you've processed" | Stripe has an event ID; Adyen's Standard webhook does not |
| Signature | Standard: HMAC-SHA256 over eight fields, inside the payload, no timestamp. Others: whole body, in a header | `Stripe-Signature` header with a timestamp `t` and signature `v1` over payload and timestamp; libraries default to a 5-minute tolerance | Stripe's scheme includes replay protection by design; Adyen's Standard scheme protects the money-relevant fields only |
| Recovery if events are lost | Retry queue, Customer Area, reports; no payment GET | Events and objects can be fetched from the API | The receiver's obligation to persist before acknowledging is stricter on Adyen |
| Sender authentication to the endpoint | OAuth 2.0 client credentials, basic auth | Not fetched | Adyen can authenticate itself to the merchant's gateway, which suits enterprises with API gateways |
| Payload | Snapshot fields in the item; platform webhooks "contain a snapshot of the resource" | Snapshot events, and thin events for new integrations | Adyen has no thin-event option documented |
| Destinations other than HTTP | None documented (JSON, HTTP POST form, SOAP) | Event destinations (see the Stripe brief) | — |

[Stripe cells VERIFIED: https://docs.stripe.com/webhooks.md, n.d., accessed 2026-11]

### For readers new to payments

- **Webhook**: an HTTP request the provider sends to the merchant's server to report that something happened.
- **HMAC signature**: a code computed from the message and a shared secret, which lets the receiver check who sent the message and that it was not altered.
- **At-least-once delivery**: the sender repeats a message until it is acknowledged, so the receiver may see it more than once and must cope.
- **Standard webhook**: Adyen's main webhook type for payments, carrying events such as AUTHORISATION, CAPTURE and REFUND.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- A per-endpoint queue that stops at the first failure means one poison message (a handler bug that returns 500 for one payload) delays every later event for that endpoint. Adyen's instruction to acknowledge before running business logic is the mitigation; the Silent Webhook thread can use this.
- The burst on recovery is a load test the integrator did not schedule; the receiver should enqueue and return, never process inline.
- Without an event ID, the receiver's deduplication table must be keyed on (`eventCode`, `pspReference`) for payments and on (`data.id`, `sequenceNumber`) for transfers: two schemes in one integration.
- Head-of-line blocking plus a 30-day window implies durable per-endpoint storage on Adyen's side sized for a month of a merchant's events. Nothing is published about how it is built.

---

## PART 7: The developer platform (chapter 21)

### 7.1 Test and live are separate environments

- Separate hosts (`checkout-test.adyen.com` versus `{PREFIX}-checkout-live.adyenpayments.com`), separate Customer Areas (`ca-test.adyen.com`, `ca-live.adyen.com`), and separate credentials: "When you switch to your live environment, you must generate a new API key in your live Customer Area" [VERIFIED: https://docs.adyen.com/development-resources/api-credentials.md and /live-endpoints.md, n.d., accessed 2026-11].
- Configuration does not carry over: webhooks must be recreated in live, and HMAC keys differ (section 6.7). A live account must be applied for [VERIFIED: live-endpoints page].
- The client key shows its environment: it has "A human-readable prefix, **test** or **live**" [VERIFIED: https://docs.adyen.com/development-resources/client-side-authentication.md, n.d., accessed 2026-11].

### 7.2 Credentials, roles and keys

- An API credential is "**Username**: An identifier in the format `ws_123456@Company.[YourCompanyAccount]`. **API key**: A password to authenticate API requests. **Roles**: Permissions that define what the credential is allowed to do" [VERIFIED: api-credentials page].
- Scope: "Credentials created on a company account can access the company account, including all linked merchant accounts. Credentials created on a merchant account can only access that merchant account"; the scope can be narrowed to selected merchant accounts [same page].
- Roles are per API and per action, for example "Checkout webservice role", "Merchant PAL webservice role", "Management API—Account read", "Management API—Terminal actions read and write", and for platforms "TransferService Webservice Initiate" [VERIFIED: https://docs.adyen.com/development-resources/mcp-server.md; TransferService-v4.json]. "An API credential must have at least one enabled role."
- Adyen's advice on separation: a separate credential per sales channel, and "If you are doing unreferenced refunds for online payments, we strongly recommend creating a separate credential for processing these refunds" [api-credentials page].
- **Key rotation**: "When you generate a new API key, it becomes active immediately. The previous key remains active for 24 hours to allow you to update your systems." The expiry of the old key can be reset to 24 hours or forced immediately. A basic-authentication password has no overlap: "the previous password is deactivated immediately" [same page].
- "API credentials cannot be deleted. However, you can deactivate a credential" [same page].
- Network controls: an allowed IP range per credential, and **mutual TLS** with client certificates issued by Adyen ("a maximum of 10 valid client certificates per company account"; "Each certificate is valid for 397 days") on supported APIs [VERIFIED: api-credentials page; https://docs.adyen.com/development-resources/mtls.md, n.d., accessed 2026-11].
- Two authentication types for requests: `X-API-Key`, and basic authentication with the `ws_…` user [VERIFIED: https://docs.adyen.com/development-resources/api-authentication.md, n.d., accessed 2026-11].
- **Client key** (front end): "We use your client key to authenticate requests from your payment environment"; "The client key is not used when making requests to our APIs"; "A single key for all your allowed origins in an environment" [client-side-authentication page].
- **Origin key** (predecessor): one key per origin. "Starting 4.0.0 the client key is the only way to do client-side authentication" for Web Drop-in and Components; the client key is "Available for 3.10.1 and later" [VERIFIED: https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key.md, n.d., accessed 2026-11]. The `/originKeys` endpoint is still in Checkout v72 [VERIFIED: CheckoutService-v72.json].

### 7.3 Rate limits

**No general rate-limit documentation exists for the payments APIs.** The documentation index lists no rate-limit page, and the Checkout API v72 specification does not contain the phrase [VERIFIED: https://docs.adyen.com/llms.txt and CheckoutService-v72.json, accessed 2026-11]. What is documented:

- A 429 status exists: "You have sent too many requests in a short period. To handle this issue, implement a retry mechanism that uses exponential backoff with jitter" [VERIFIED: response-handling page].
- **Legal Entity Management API** ⚠: "Live environments: 700 requests per 5 seconds. Test environments: 200 requests per 5 seconds. Failed requests are subject to a limit of 5 failures per 10 seconds." "additional requests are blocked until the time frame ends" [VERIFIED: LegalEntityService-v4.json, `info.description`].
- **Management API**, terminal-management and store endpoints, live only ⚠: limits per group of endpoints, for example "Total 160 requests/minute", "210 requests/minute … (rolling 60-second window)" and "2000 requests/minute"; the failure response includes `"detail": "too many requests"`; "these limits are indicative and can change as needed to maintain the stability of the live environment" [VERIFIED: https://docs.adyen.com/point-of-sale/automating-terminal-management.md, n.d., accessed 2026-11].
- **Transfers API**: a 429 response is declared ("Too Many Requests - Request rate limit exceeded") with no figure [VERIFIED: TransferService-v4.json].
- Nothing was found on how Adyen sheds load, on per-merchant quotas for payment requests, or on concurrency limits.

### 7.4 Logs, dashboards and tooling

- **API logs**: "all API requests made in your test or live environment in the past thirty days"; "API logs only support API requests that use JSON"; searchable by PSP reference, with full request and response [VERIFIED: https://docs.adyen.com/development-resources/logs-resources/api-logs.md, n.d., accessed 2026-11].
- **Developer dashboard**: "the activity and errors that occurred with your API requests and webhooks in the past seven days", with a breakdown of which APIs, libraries, plugins and checkout SDKs the account uses. It classifies the integration type, including "Classic API (deprecated)" [VERIFIED: https://docs.adyen.com/development-resources/developer-dashboard.md, n.d., accessed 2026-11].
- **Customer Area consolidation** ⚠: "Starting in Q3 2025, all Balance Platform Customer Area users will transition to Adyen's unified platform - the Customer Area … The Balance Platform Customer Area will be no longer be accessible after February 28, 2026" [VERIFIED: https://docs.adyen.com/about-our-customer-area.md, n.d., accessed 2026-11].
- **API Explorer** for reference documentation, the **API Diff Tool**, **Postman** collections generated from the specifications (section 3.6).
- **Documentation for machines**: every page as Markdown, an `llms.txt` index and an `llms-full.txt` corpus [VERIFIED: https://docs.adyen.com/llms.txt].
- **MCP server** ⚠ (alpha): lets an LLM client call the Checkout and Management APIs "through function calling"; launched 2025-06-10 [VERIFIED: https://docs.adyen.com/development-resources/mcp-server.md; https://www.adyen.com/knowledge-hub/mcp-release, published 2025-06-10].
- No Adyen command-line tool comparable to a provider CLI was found in the documentation index.

### 7.5 Testing and what the test environment does not show

- Outcomes are triggered by magic values. For cards: "you need to include a specific value either in the `holderName` or `RequestedTestAcquirerResponseCode` field" to get a given result code and refusal reason [VERIFIED: https://docs.adyen.com/development-resources/testing/result-codes.md, n.d., accessed 2026-11].
- Late failures can be simulated: a card payment with `holderName` **capture failed** or **refund failed** produces CAPTURE_FAILED or REFUND_FAILED, but "It can take up to 24 hours for the failed modification simulation to finish" [VERIFIED: https://docs.adyen.com/development-resources/testing/payments-and-modifications.md and capture page, n.d., accessed 2026-11].
- "Some card-related payment methods, for example Alipay, redirect you to a simulator where you can select the payment result" [result-codes testing page].
- Merchants can create their own test cards through a Test Cards API [VERIFIED: https://docs.adyen.com/llms.txt lists the page; `TestCardService-v1` in the repository].
- Adyen's engineers on the limits of happy-path testing: "Getting a green happy-path response during integration testing doesn't prove your integration will hold up under the conditions that actually matter at go-live. In live, many payment methods finish outside your checkout … A test that only checks the first response never sees that." Their answer is the **Adyen Payment Simulator**, where "the tester lands on a simulator page and selects the outcome: authorized, refused or canceled", after which the platform "sends your integration the AUTHORISATION webhook message" [VERIFIED: https://medium.com/feed/adyen, article published 2026-11-09].
- Adyen publishes no list of what test cannot simulate. From the pages above, the gaps are: real issuer behaviour and authorisation rates, real 3D Secure challenge behaviour, scheme-side authorisation expiry, settlement timing and real funds, and live rate limits (the Management API limits are stated for live only) [ASSUMPTION/JUDGEMENT].

### Stripe vs Adyen (developer platform)

| Aspect | Adyen (documented) | Stripe (fetched for contrast) | Suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Environments | Two separate environments with separate hosts, portals, accounts and configuration; live requires an application | Sandboxes and live mode within one account, distinguished by key prefix (live keys "start with `pk_live_`, `rk_live_`, and `sk_live_`") [VERIFIED: https://docs.stripe.com/keys.md, n.d., accessed 2026-11] | Adyen's separation is physical; Stripe's is logical. Adyen's makes test-to-live drift likelier and accidental live calls less likely |
| Server key model | Credential = user + API key + roles, scoped to company or merchant accounts; IP ranges; mTLS | Secret keys, and restricted keys "with permissions you control" | Both now steer integrators to least-privilege keys; Adyen's roles predate it and are per API |
| Key rotation overlap | 24 hours, extendable | See the Stripe brief | — |
| Rate limits | Not published for payments; published for LEM and parts of the Management API | Published: "Live mode: 100 requests per second", "Sandbox: 25 requests per second" globally, plus per-endpoint limits [VERIFIED: https://docs.stripe.com/rate-limits.md, n.d., accessed 2026-11] ⚠ | Stripe treats limits as part of a self-serve contract; Adyen, selling to enterprises with account managers, appears to handle payment throughput by arrangement. The Renewal Wave thread has documented numbers only on the Stripe side |
| Published limiter design | None found | Engineering post (see the Stripe brief; dated) | — |
| Request logs | 30 days of API logs and webhook logs in the Customer Area; 7-day dashboard | See the Stripe brief (Workbench) | — |
| Tooling | API Explorer, Diff Tool, Postman, MCP server; no CLI found | CLI, Workbench (see the Stripe brief) | — |

### For readers new to payments

- **Customer Area**: Adyen's web portal for merchants, where payments, settings, credentials, webhooks and logs are managed.
- **Client key**: a public key embedded in the checkout page so Adyen's client library can identify the merchant; it cannot make API calls.
- **Test card**: a card number that works only in the test environment and produces a known result.

### Architecture implications [ASSUMPTION/JUDGEMENT]

- With no published payment rate limit, an integrator planning a batch (the Renewal Wave) must agree throughput with Adyen in advance and still implement backoff on 429; a figure cannot be designed against from documentation.
- Separate environments mean infrastructure-as-code for Adyen configuration (webhooks, credentials, allowed origins) through the Management API is worth the effort; otherwise live is configured by hand.

---

## PART 8: Adyen's own technical publications on these topics

Searched: the Adyen knowledge hub tech stories (`adyen.com/knowledge-hub`), the Adyen Tech publication on Medium through its RSS feed (ten most recent items, February 2025 to November 2026), and two web searches for API design, webhook delivery infrastructure and idempotency implementation.

| Article | Date | What it contributes |
| --- | --- | --- |
| "API-first approach at Adyen platform" | 2022-09-27 **(4 years)** | API Review group, APIs as products, OpenAPI adoption, deprecation practice (section 3.7) |
| "Consuming webhooks explained" | 2023-02-02 **(3.8 years)** | Duplicates, delay of "few seconds to minutes", retry in general terms; calls the webhook system "a sophisticated framework" for "flexibility … reliability (retry and event logging), and consistency (events are delivered as they happen)" |
| "Building better applications with Adyen API libraries" | 2023-03-28 **(3.6 years)** | Specifications generated internally, libraries generated from them, two-week target (section 3.6) |
| "Optimizing Webhook Integration: a new approach to accept events from the Adyen platform" | 2024-05-01 | The change from `[accepted]` to 2xx and the reasons (section 6.3) |
| "Powering effortless integrations: Introducing Adyen's Model Context Protocol server" | 2025-06-10 | MCP server |
| "A developer's guide to HMAC validation for Adyen webhooks" | 2025-06-16 | Two signature schemes, payload-alteration pitfalls (section 6.6) |
| "Adyen API Diff Tool" | 2025-08-19 | Tool announcement (title and date only; body not read) |
| "Making payment method testing repeatable: building the Adyen Payment Simulator" | 2026-11-09 | Asynchronous method lifecycles and test determinism (sections 1.5, 7.5) |

[VERIFIED: each article's page on https://www.adyen.com/knowledge-hub/ (slugs `api-first-adyen`, `consuming-webhooks`, `adyen-api-libraries`, `webhooks-accept-2xx`, `mcp-release`, `hmac-validation-guide`) with its `datePublished`, and https://medium.com/feed/adyen for the two 2025–2026 items listed by title]

**Honest summary: little exists.** All eight are written for integrators or describe tooling. **Nothing was found that describes how Adyen implements** idempotency (the store, fingerprinting, expiry), webhook delivery (the queue, fan-out, isolation between merchants, storage of 30 days of backlog), API version maintenance (how one code base serves v37–v72), rate limiting, or the API gateway. Adyen's infrastructure articles in the same feed (table partitioning, replication, Kubernetes networking) are about data stores and platform operations and belong to `brief-reliability-and-scale.md`.

---

## Key numbers

| Number | Value | Exact definition | Source and date |
| --- | --- | --- | --- |
| PSP reference length | 16 characters | Alphanumeric identifier assigned to every payment or modification request | Adyen glossary, n.d., accessed 2026-11 |
| Latest Checkout API version ⚠ | v72 | Released 2026-04-15; previous v71 on 2023-11-01 | Release notes |
| Public Checkout API versions | 18 | Specification files v37–v72 present in `adyen-openapi` | GitHub, accessed 2026-11 |
| `/sessions` introduced | 2021-10-06 | Checkout API v68 | Release notes |
| `action` object introduced | 2019-05-14 | Checkout API v49 | Release notes |
| Modification endpoints in Checkout API | 2021-06-03 | Captures, refunds, cancels, reversals, amount updates | Release notes |
| Session default expiry | 1 hour; maximum 24 hours | Time after `/sessions` creation | Sessions flow guide, n.d. |
| Card offer expiry | 12 hours | Default before `OFFER_CLOSED` | Webhook types, n.d. |
| Adyen authorisation expiry | 28 days | Default after which Adyen expires a card (pre-)authorisation, "global card schemes" | Authorization adjustment, n.d. |
| Capture delay setting | immediate, 1–7 days, or manual | Merchant-account setting; `captureDelayHours` per request | Capture, n.d. |
| Cancel by merchant reference | 24 hours | Window after authorisation for `POST /cancels` | Cancel, n.d. |
| Refund arrival | up to 40 business days | Time for funds to reach the shopper, by payment method | Refund, n.d. |
| Automatic re-capture | within 10 business days | Technical capture failures retried by Adyen | Webhook types, n.d. |
| Idempotency key length | 64 characters maximum | `idempotency-key` header | API idempotency, n.d. |
| Idempotency key validity | 7 to 14 days | "after first submission", per company account, per region | API idempotency, n.d. |
| Deprecation notice, Checkout API | 2 years | From "Deprecated" state to end-of-life | Upgrade your integration, n.d. |
| Deprecation notice, Drop-in/Components | 1 year | Same, for client libraries | Upgrade your integration, n.d. |
| Webhook acknowledgement timeout | 10 seconds | Time to return a 2xx before the event counts as failed | Configure and manage webhooks, n.d. |
| Webhook retry window ⚠ | up to 30 days | Automatic retries from the retry queue; intervals 30 s to 8 h | Troubleshoot webhooks, n.d. |
| Webhook failure alerts | after 5 retries; after 7 days | Initial and ongoing failure alerts | Troubleshoot webhooks, n.d. |
| Inactive webhook deletion | 6 months | Disabled webhook configurations removed automatically | Configure and manage webhooks, n.d. |
| API log retention | 30 days | API logs and webhook event logs in the Customer Area | API logs; Webhook event logs, n.d. |
| API key overlap on rotation | 24 hours | Previous key stays valid after a new one is generated | API credentials, n.d. |
| LEM API rate limit ⚠ | 700 requests per 5 seconds (live); 200 (test) | Legal Entity Management API only | LegalEntityService-v4.json, accessed 2026-11 |
| Maximum request size | 10 MB | HTTP 413 above this | HTTP status codes, n.d. |
| Idle connection timeout | 60 seconds | Inactive keep-alive HTTP connections | Live endpoints, n.d. |
| Library availability target | 2 weeks | Aim after a new API release (**2023 statement**) | Adyen tech blog, 2023-03-28 |

## Open questions / not verifiable

These are candidates for the book's "where the evidence stops" statements.

1. **Idempotency with a changed request body.** Adyen does not document whether a reused key with different parameters returns the stored response or an error. Not verifiable without testing.
2. **How Adyen implements idempotency.** Only one sentence is public ("a consistent, stateful data store"). The reason for a "7 to 14 days" range, and whether error responses are stored, are not stated.
3. **Which non-payment APIs honour the `Idempotency-Key` header.** It is declared only in the Checkout and Transfers specifications.
4. **Webhook ordering guarantee.** Adyen neither guarantees nor disclaims ordering in so many words; the retry-queue text implies per-endpoint order during failure.
5. **Retry schedule after the twelfth interval**, and the number of immediate attempts before a webhook is marked Failing ("a few more times").
6. **Webhook delivery infrastructure.** Nothing public on queueing, isolation between merchants, or storage.
7. **Rate limits for the Checkout API.** None published. Whether limits are per company, per credential or negotiated is unknown.
8. **Current lifecycle state of each Checkout API version** (which of v40–v71 are Inactive, Deprecated or End-of-Life, and their end dates): shown only in the client-rendered API Explorer.
9. **HPP end-of-life date.** The docs timeline is an image; "October 2022" rests on a search snippet.
10. **Launch dates of the Checkout API (before v37) and of Drop-in.** The release notes start at v37 on 2018-02-23; the product launch announcement was not found.
11. **Whether the Checkout and classic Payment APIs share one version counter.** Inferred from the numbering and from "Classic API v68 endpoints to Checkout API v68"; not stated.
12. **How one platform serves 18 Checkout versions.** No equivalent of Stripe's version-change-module description was found.
13. **Legacy `[accepted]` webhooks.** How many remain, and whether Adyen has set a date to end that acknowledgement mode, is not stated.
14. **Replay protection for Standard webhooks.** No timestamp is signed and no tolerance window is documented; whether Adyen relies on TLS plus deduplication alone is the analyst's reading.
15. **What the test environment cannot simulate.** Adyen publishes no such list.

## Source list

**Adyen documentation** (docs.adyen.com; undated living pages, all accessed 17 November 2026 in their `.md` form)

- "Build your integration", "Sessions flow integration guide", "Advanced flow integration guide", `/online-payments/build-your-integration…` — flows, session expiry, session result, actions.
- "Result codes", `/online-payments/build-your-integration/payment-result-codes` — the 13 result codes and the advice not to drive order state from them.
- "Capture", "Cancel", "Refund", "Reversal", `/online-payments/capture|cancel|refund|reversal` — modification endpoints, webhooks, failure reasons, two-stage outcomes.
- "Authorization adjustment" and "Adjust an authorization", `/online-payments/adjust-authorisation…` — authorisation types, synchronous and asynchronous adjustment, expiry tables.
- "Payments lifecycle", `/account/payments-lifecycle` — offers and the 70+ payment statuses.
- "Account structure", `/account/account-structure` — company, merchant account, account group, store.
- "Adyen glossary", `/adyen-glossary` — PSP reference definition.
- "Release notes", `/online-payments/release-notes` — dated Checkout API versions v37–v72 and client-library releases (each entry dated).
- "Upgrade your integration", `/online-payments/upgrade-your-integration` — lifecycle states, 2-year and 1-year clocks, compatibility tables.
- "Migrate to Checkout API", `/online-payments/upgrade-your-integration/migrate-to-checkout-api` — Classic to Checkout, CSE replaced by JWE.
- "Classic integrations for Ecommerce", "Classic API integration", "Client-Side Encryption (CSE)", "Hosted Payment Pages", "HPP is end-of-life", `/online-payments/classic-integrations/…` — status of the older generations.
- "Versioning", `/development-resources/versioning` — URL versions, new versus classic APIs, breaking-change tables, library semantic versioning.
- "API idempotency", `/development-resources/api-idempotency` — the whole of PART 4.
- "HTTP status codes", `/development-resources/response-handling` — status codes, error fields, the meaning of a 200 on a modification.
- "Error codes and messages", `/development-resources/error-codes` — codes 703 and 704.
- "Live endpoints", `/development-resources/live-endpoints` — company prefix, routing rationale, keep-alive timeout.
- "Webhooks", "Configure and manage webhooks", "Handle webhook events", "Secure webhooks", "Verify HMAC signatures", "Troubleshoot webhooks", "Webhook structure and types", `/development-resources/webhooks/…` — the whole of PART 6.
- "Webhook structures and types for platforms", `/platforms/webhook-types` — platform event types.
- "API credentials", "API authentication types", "Client-side authentication", "Migrate to client key", "Mutual authentication", `/development-resources/…` — credentials, roles, keys.
- "API logs", "Webhook event logs", "Developer dashboard", `/development-resources/…` — retention and tooling.
- "Automating terminal management", `/point-of-sale/automating-terminal-management` — Management API rate limits.
- "Terminal API", `/point-of-sale/design-your-integration/terminal-api` — nexo, ServiceID, tender reference.
- "Libraries", `/development-resources/libraries` — server libraries.
- "Testing your online payments integration", "Testing result codes and refusal reasons", "Testing payments and modifications", "Test card numbers" — test triggers.
- "Adyen Model Context Protocol (MCP) server", `/development-resources/mcp-server` — MCP server and roles.
- "Transitioning to our unified Customer Area", `/about-our-customer-area` — Customer Area consolidation dates.
- `https://docs.adyen.com/llms.txt` — documentation index; evidence that no rate-limit or pagination page exists.

**Adyen on GitHub** (accessed 17 November 2026)

- `Adyen/adyen-openapi`, https://github.com/Adyen/adyen-openapi (created 2017-11-20, pushed 2026-11-13) — README (vendor extensions) and the specification files CheckoutService-v72, PaymentService-v68, ManagementService-v3, BalancePlatformService-v2, TransferService-v4, LegalEntityService-v4, TerminalAPI-v1, Webhooks-v1, BalancePlatformTransferNotification-v4 — endpoints, absence of a payment GET, pagination and error schemas, idempotency header coverage, LEM rate limits, transfer webhook sequence numbers.
- `Adyen/adyen-sdk-automation`, https://github.com/Adyen/adyen-sdk-automation — README: Gradle scripts that generate the API libraries with OpenAPI Generator.
- `Adyen/adyen-java-api-library`, https://github.com/Adyen/adyen-java-api-library — README: API versions wrapped by the library.
- `adyen/adyen-postman`, https://github.com/adyen/adyen-postman — README: Postman collections generated from the specifications.

**Adyen tech blog**

- "API-first approach at Adyen platform", Adyen knowledge hub, 2022-09-27, https://www.adyen.com/knowledge-hub/api-first-adyen — API Review group, API families, deprecation practice. **Evidence age 4 years.**
- "Consuming webhooks explained", Adyen knowledge hub, 2023-02-02, https://www.adyen.com/knowledge-hub/consuming-webhooks — duplicates, delay, retries. **Evidence age 3.8 years.**
- "Building better applications with Adyen API libraries", Adyen knowledge hub, 2023-03-28, https://www.adyen.com/knowledge-hub/adyen-api-libraries — OpenAPI-driven library pipeline. **Evidence age 3.6 years.**
- "Optimizing Webhook Integration: a new approach to accept events from the Adyen platform", Adyen knowledge hub, 2024-05-01, https://www.adyen.com/knowledge-hub/webhooks-accept-2xx — acknowledgement change from `[accepted]` to 2xx.
- "Powering effortless integrations: Introducing Adyen's Model Context Protocol server", Adyen knowledge hub, 2025-06-10, https://www.adyen.com/knowledge-hub/mcp-release — MCP launch date.
- "A developer's guide to HMAC validation for Adyen webhooks", Adyen knowledge hub, 2025-06-16, https://www.adyen.com/knowledge-hub/hmac-validation-guide — two HMAC schemes.
- Adyen Tech on Medium, RSS feed https://medium.com/feed/adyen — "Adyen API Diff Tool" (2025-08-19, title and date only); Ayodeji Ogundare, Henk Grent, Marc Sernatinger and Shantanu Tarey, "Making payment method testing repeatable: building the Adyen Payment Simulator" (2026-11-09) — asynchronous method lifecycles and testing.
- Adyen blog, "HPP end of life", https://www.adyen.com/blog/HPP-end-of-life, 2022 — search snippet only; page not readable.

**Stripe documentation, for contrast only** (docs.stripe.com, undated, accessed 17 November 2026)

- "Idempotent requests", https://docs.stripe.com/api/idempotent_requests.md — 24-hour pruning, parameter comparison, 255 characters, v1 and v2 semantics.
- "Receive Stripe events in your webhook endpoint", https://docs.stripe.com/webhooks.md — three-day retry, ordering and duplicate statements, `Stripe-Signature` with timestamp and 5-minute tolerance.
- "Rate limits", https://docs.stripe.com/rate-limits.md — 100 and 25 requests per second.
- "API upgrades", https://docs.stripe.com/upgrades.md — account default version, `Stripe-Version` header, version string format.
- "How PaymentIntents work" (lifecycle), https://docs.stripe.com/payments/paymentintents/lifecycle.md — statuses.
- "Pagination", https://docs.stripe.com/api/pagination.md; "API keys", https://docs.stripe.com/keys.md — cursor pagination; key types.
