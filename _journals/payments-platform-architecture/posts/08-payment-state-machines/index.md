---
title: "One Object, Many Outcomes: The Payment State Machine"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How do you model a payment that can be pending, need a customer action, succeed later, be partly captured and partly refunded? As one long-lived record with explicit states, which Stripe lets you read again as an object and Adyen reports as results, modifications and webhooks, and which your own system mirrors in a small vocabulary it controls."
permalink: payment-state-machines
timetoread: 24 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn to model a payment as a record with explicit states, read Stripe's and Adyen's versions of that record, and design your own over both.

> **KEY POINTS:**
>
> * **A payment is a record with states, not a request with an answer.** Waiting for the customer and waiting for the network are different states, the API response is one transition among several, and captures and refunds are separate operations with their own amounts and outcomes.
> * **Stripe and Adyen expose the same model in different ways.** Stripe's PaymentIntent (2018) is an object you can retrieve and retry. Adyen returns a result code per request and reports outcomes by webhook; its Checkout API has no endpoint that returns a payment by its identifier.
> * **Your own payment record is designed, not copied.** Keep each provider's status as received, map it to a small vocabulary of your own, change state only on the provider's confirmed record, and treat "succeeded" as a state with exits.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Phantom Payment** — a record set from the API response or the returning browser says "paid" without the provider's confirmed record saying so.
> * **The Trusted Doorbell** — a state machine that assumes each event arrives once and in order breaks on the first repeat or late contradiction.
> * **A Card by Any Other Name** — a record with only "paid" and "not paid" assumes every method answers at once.

<br>
On 12 January 2027 Mila Janssen types her Visa debit card into the member app of Larkfield, the fictional studio-software platform this book follows, to start a €49 membership at her yoga studio. Larkfield's server calls its payment provider and has an answer in under a second. The answer is neither "approved" nor "declined": **her bank wants her to confirm the payment in its app**.

A payment record that can say only "paid" or "not paid" has to guess what to write during that wait, and each wrong guess costs someone. Guess "not paid", and a member who has been charged is turned away at the studio door. Guess "paid", and the studio gives a month of classes for money that never arrives. It is the gap between the instant answer and the slow truth at its smallest scale.

The model that removes the guess: **a payment is one long-lived record that moves through explicit states**, and what happens to it afterwards (a capture, a refund, a dispute) is recorded against it as a separate operation with its own amount. Stripe and Adyen both arrived at this model and present it differently: one as an object you can read again, the other as results and events you assemble yourself.

**Where we are in the payment's journey.** Mila's class pass is the book's recurring payment: €120.00, bought at Studio Noord on Tuesday 9 March 2027 at 19:42. This chapter covers the record that exists from the moment she taps "pay" until the provider confirms the outcome, and that every later step (the capture, the payout on 11 March, a refund a week later) writes to.

The chapter starts at Larkfield's five-state payment record. It explains why a yes-or-no charge request stopped working, sets out the model, and shows how Stripe and then Adyen expose it. It then states what a state machine must guarantee, compares four ways to mirror one, puts the two providers side by side, works Mila's payments through the redesigned record, and ends with events that arrive late, twice or in contradiction.

## Setting the Scene at Larkfield: Five Words, Two Providers

In late March 2027 Femke de Graaf, Larkfield's head of payments engineering, reviews the payment record store with Tom Hendriks, the engineer who built the payment service in 2024. Each row of the table carries one of five states (`pending`, `authorized`, `paid`, `refunded`, `disputed`) and the references of whichever provider took the payment, Stripe or Adyen. Webhooks, the providers' server-to-server notifications ([[payment-webhooks-and-events]]), feed it through an inbox table.

Three ordinary payments have no clear place in those five words. Mila's membership set-up sat in `pending` while she confirmed in her banking app, and nothing in the row said it waited for her. Another member's SEPA (Single Euro Payments Area) Direct Debit, a payment pulled from a bank account and confirmed days later, had no state for its wait at all: the row was marked `paid` when the provider accepted the debit, most of a week before the bank's answer ([[local-payment-methods]]). One waited for a person, the other for a bank, and the record could say neither. And on 18 March Mila was refunded €84.00, the unused part of her €120.00 pass: the row says `refunded`, as if all of it went back.

In the Silent Webhook of September 2026, the certificate on Larkfield's Stripe webhook receiver expired and events failed for nine hours. Larkfield's rows said **3,200 memberships were unpaid** while Stripe's own objects said they were paid, and members were turned away at check-in. The row is a copy: the payment's state lived at the provider, and the copy changed only when an event got through.

The record is too coarse and it is only a copy. Femke's question to Tom is the chapter's: **for each of the five words, which message from which provider may move a record into it, and which may move it out?**

## Why a Yes-or-No Charge Stopped Working

In the **charge-request model**, a payment is one server call that carries the card details and returns the outcome, and the merchant's record is that answer. The model holds under two assumptions: the outcome is known within the call, and nobody but the merchant's server has to act.

The best documented instance is Stripe's first API. In the Stripe engineering post "Stripe's payments APIs: The first 10 years" (December 2020), Michelle Bu describes the original design of 2011 to 2015: a Token made in the browser from the card details and a Charge made on the server. US card payments allowed a charge request: the post says they "can be immediately finalized", where finalized means "a user has sufficient confidence the funds are guaranteed". **(Evidence age: 6 years; current documentation confirms the end state it describes.)**

In 2015 two methods broke the assumptions. ACH (Automated Clearing House) debit, the US bank debit, is finalized days later, so Stripe added a `pending` state to the Charge and merchants fulfilled orders "days later, when they received a webhook". Bitcoin had to be started by the customer, which took a second object; the post describes "managing two state machines to complete payment: BitcoinReceiver on the client and Charge on the server". The first repairs were an extra status value and an extra object.

The next design, the Sources API of 2015 to 2017, put the state in the browser as "a client-driven state machine". The server still had to create the Charge after the customer had acted, and with iDEAL, the Dutch method that sends the customer to their bank to approve, that second call could be lost. If the browser dropped its connection, the post says, "the next request to create a Charge wouldn't make it through, even though the customer believes they paid", and "we'd refund the money associated with the Source after a few hours. This is a conversion nightmare."

The post sorts payment methods on two questions, in the table below. Cards without authentication are the only family that answers no to both. "Global payment methods aren’t different; cards are!"

| | Finalized immediately | Finalized later |
| --- | --- | --- |
| **No customer action** | Cards | ACH, SEPA, Bacs and BECS direct debit (the US, euro-area, UK and Australian bank debits) |
| **Customer action required** | iDEAL, Alipay, giropay, Bancontact, WeChat Pay, Przelewy24, cards with 3-D Secure | Bitcoin, Multibanco (a voucher), paper checks |

More status values could not repair the Charge, because the fault was **where the state lived and who had to make the next call**: the payment came into existence only when the merchant's server made a second request, after a customer action that the server could not see. Stripe's own conclusion was that "Charges and Tokens were foundational in the API because they were the first APIs we had, not because they were the right abstraction for global payments." Between 2011 and 2018 the Charge had grown "from having 11 properties to 36 properties".

## One Record, Explicit States, Separate Operations

A **payment state machine** is a record created on the server before any money moves, which holds a state, the transitions allowed from that state, and every attempt made to pay. The *payment* is the customer's purchase. An *attempt* is one try to collect it with one payment method, and one payment can hold several.

Six states describe the model, and each is ended by a different party. The names are mine, not either provider's. An **authorization** is the promise by the customer's bank to hold the amount; a **capture** is the merchant's instruction to collect it ([[payment-authorization]], [[clearing-and-settlement]]).

| State | What it means | Who ends it |
| --- | --- | --- |
| Needs payment details | No usable payment method yet, or the last attempt failed | The customer, through the client |
| Needs customer action | The provider has said what the customer must do next | The customer, or a timeout |
| Processing | The bank or network has not answered | The bank or network, reported by the provider |
| Authorized | The amount is held, not collected | The merchant's server (capture or cancel), or expiry of the hold |
| Succeeded | The provider reports the payment collected | Nothing; refunds and disputes are separate records |
| Canceled | Closed without payment | Nothing |

<!-- illustration-placeholder
{
  "id": "08-payment-state-machine",
  "status": "pending",
  "asset": "assets/images/08-payment-state-machines/08-payment-state-machine.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the preceding paragraph",
  "visual_goal": "Show the six states, who moves each transition, and a failed attempt returning to the first state.",
  "prompt": "State-machine diagram. Six rounded boxes in two rows. Top row, left to right: \"needs details\", \"needs action\", \"processing\", \"succeeded\". Bottom row: \"authorized\" under processing, and \"canceled\" at the far right bottom. Arrows: from \"needs details\" to \"needs action\" labeled \"confirm\"; from \"needs action\" to \"processing\" labeled \"customer\"; from \"processing\" to \"succeeded\" labeled \"bank\"; from \"processing\" down to \"authorized\" labeled \"hold\"; from \"authorized\" up to \"succeeded\" labeled \"capture\"; a curved orange arrow from \"processing\" back to \"needs details\" labeled \"attempt failed\"; a grey arrow from \"authorized\" to \"canceled\" labeled \"cancel\". Under \"succeeded\" hang two small separate cards on thin lines labeled \"refund\" and \"dispute\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "State diagram of a payment record with six states and labeled transitions.",
  "caption": "Each state of a payment is ended by a different party, a failed attempt returns the payment to its first state, and refunds and disputes hang off the payment as separate records."
}
-->

The second and third states are the ones most often merged into one "pending". A customer action takes seconds or minutes and may never happen: the customer puts the phone down. A bank debit takes days and almost always resolves. The first needs a prompt and an expiry; the second needs patience and no prompt. One word for both forces the wrong follow-up on one of them.

What the provider returns in the second state is a **next action**: its instruction to the client about what the customer must do before the payment can go on. A *redirect* sends the customer to their bank. A *3-D Secure challenge* runs the card networks' protocol by which the customer's bank authenticates them, used in Europe to meet the rule of strong customer authentication ([[three-d-secure-and-sca]]). A *display* action hands over a voucher or QR code to show. In each case the client carries out the action, not your server.

The synchronous API response therefore cannot be the outcome. It reports the state reached so far, and it is **one transition among several**. The last transition comes from the provider's server-to-server notification, because a client you do not control may never come back to tell you.

| Requirement | The API response | The final outcome |
| --- | --- | --- |
| How fast | Seconds *(assumption)* | Seconds for most cards; days for a bank debit |
| How consistent | A snapshot of the state reached so far | The provider's record wins over yours |
| How available | Returned to whoever made the call | Must reach you when the client is gone |
| On failure | A timeout leaves the outcome unknown ([[idempotency-and-retries]]) | The payment stays in its state until the provider reports |

The notification is delivered at least once and in no guaranteed order ([[payment-webhooks-and-events]] has the full contract). Stripe's documentation says "Webhook endpoints might occasionally receive the same event more than once" and "Stripe doesn’t guarantee the delivery of events in the order that they’re generated"; the guard it gives is the event's ID. Adyen's says (both n.d., accessed November 2026) duplicates "have the same values in the `eventCode` and `pspReference` fields" and tells receivers to "always check the timestamp".

After the payment reaches a state, things happen *to* it: a capture, a cancellation, a refund, a dispute (the customer's bank taking the money back, [[refunds-reversals-and-disputes]]). Each is a separate record against the payment, with its own amount and its own outcome. So "partly captured and partly refunded" is two amounts and not a state. Mila's pass after 18 March is: authorized €120.00, captured €120.00, refunded €84.00.

## Stripe: A PaymentIntent You Can Read Again

Stripe's version is the **PaymentIntent**, introduced in 2018. Stripe's documentation (n.d., accessed November 2026, like every Stripe page cited below) describes two actions. Your server creates the intent, which "typically correlates with a single shopping cart or customer session", and passes the client only a *client secret*, a key that "lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones". The client confirms. Each intent "has a unique ID that you can use to retrieve it": the record exists on the server before the customer acts, which is what Sources lacked.

The intent has seven statuses, and the lifecycle page says what each waits for.

| Status | Stripe's description |
| --- | --- |
| `requires_payment_method` | The status "until you attach a payment method" |
| `requires_confirmation` | "ready to confirm. Most integrations skip this state" |
| `requires_action` | "the payment requires additional actions, such as authenticating with 3D Secure" |
| `processing` | "the payment uses an asynchronous payment method, such as bank debits" |
| `requires_capture` | Reached "If you’re separately authorizing and capturing funds" |
| `succeeded` | "the corresponding payment flow is complete" |
| `canceled` | Cancellation "releases any held funds, and can’t be undone" |

There is no "failed" status. The 2020 post explains: "There’s no failed state because if a single payment attempt fails, the PaymentIntent goes back to the requires_payment_method state so that the customer can try again with a different payment method." Failure belongs to the attempt, and Stripe keeps each attempt as a Charge. The object reference lists `latest_charge`, "ID of the latest Charge object created by this PaymentIntent", and the lifecycle page advises creating the intent early "so Stripe can record all attempted payments".

An attempt in progress shows as one of the two waits. `requires_action` comes with a `next_action` field for the client, from "a generic redirect_to_url" to `oxxo_display_details` for a cash voucher (the 2020 post's examples). `processing` is the wait for the bank. For both, Stripe tells you to act on the server-side event. Its status guide says: "Don’t attempt to handle order fulfillment on the client side because customers can leave the page after payment is complete". Polling the intent is allowed, "but it’s much less reliable and might trigger rate limits".

After authorization the operations hang off the same record. In Stripe's API reference, capture is a call on an intent in `requires_capture`, with an `amount_to_capture` that "must be less than or equal to the original amount"; uncaptured intents "are cancelled a set number of days (7 by default) after their creation". A Refund is its own object whose status, the same reference says, "can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`", and a Dispute is another, tied to the charge it contests. These change the payment's outcome while the intent's status does not move, as the status guide puts it: "Subsequent refunds, disputes, and outcomes are reflected on the Charge. These might change what you see in the Dashboard, even though the PaymentIntent remains `succeeded`."

A **SetupIntent** saves a payment method for later use without charging it: the lifecycle page says Setup Intents "set up payment credentials but don’t process payments", and "Both Payment Intents and Setup Intents go through the same set of states."

## Adyen: Result Codes, Modifications and Webhooks

Adyen has published no design history comparable to Stripe's, so its model is described here from its documentation (n.d., accessed November 2026), its API specification and the dates in its release notes. The dates show the same shape arriving in the same years. **(Evidence age: the release-note entries are 5 to 7 years old; they are cited for the dates, and the features they announce are in the current specification.)** A `resultCode` for vouchers, `presentToShopper`, came in Checkout API version 41 (14 February 2019). Version 49 (14 May 2019) noted: "The response now contains an `action` object that indicates the action to be taken for completing the payment." Captures and refunds joined the Checkout API on 3 June 2021 and `POST /sessions` on 6 October 2021 (version 68). Two reasons are on record. For the last step, a post by an Adyen developer advocate (5 October 2021) says that with sessions "the number of API calls needed when integrating will be reduced from three to only one". For modifications, an Adyen engineering post on its architecture (July 2021) says: "Instead of keeping the state in our edge layer, we decided to process modifications asynchronously, which keeps the edge layer stateless." Why Adyen answers with a result code and offers no retrievable payment is not on record (knowledge hub, engineering blog and documentation searched, November 2026).

The first object an integrator meets is the **payment session**: a short-lived object your server creates, which Adyen's client libraries (Drop-in and Components) use to run the checkout. The sessions guide says a session expires "1 hour after session creation" unless you set otherwise, and never later than 24 hours. A session starts a payment and does not hold its state afterwards: "The `status` included in the response doesn't get updated. Do not make the request again to check for payment status updates."

A response states the payment's state as a **result code**. Adyen's result codes page groups the codes along the model's distinctions, carried on a response and not on an object.

| Group | Result codes | Adyen's description |
| --- | --- | --- |
| 3-D Secure 2 in progress | `IdentifyShopper`, `ChallengeShopper`, `RedirectShopper` | The issuer (the customer's bank) requires authentication from the device, from the shopper, or on another page |
| Intermediate | `Received`, `Pending`, `PresentToShopper` | "the payment has not reached a final state yet"; `Received` "is the initial state for all payments" |
| Partial | `PartiallyAuthorised` | "The payment was authorized for a partial amount" |
| Final | `Authorised`, `Refused`, `Cancelled`, `Error` | "the payment has reached a final state" |

When the customer has to act, the response carries an **action** object, Adyen's next action, which the client library performs. The advanced flow guide lists the types `redirect`, `threeDS2`, `qrCode`, `sdk`, `voucher` and `await`. If the shopper does not come back from a redirect, the sessions guide says, "You do not need to do anything to handle the redirect in this case. Instead, wait for the webhook".

Adyen says what the result code must not be used for: "The status of a payment can sometimes change after you get the result code, so we recommend that you do not use the result code to update your order management system." And on the `AUTHORISATION` webhook, the webhook types page says: "Although you can use the payment result from the API, we recommend that you rely on the webhook to trigger any business logic".

A **modification** is any operation on an existing payment: capture, cancel, refund, reversal, amount update. Each is a separate request with its own PSP (payment service provider) reference, the 16-character identifier Adyen gives every payment and modification request. The capture page shows the answer: "`status`: **received**. Your capture request will be processed asynchronously. You will receive the result in a webhook." Adyen's response-handling page spells out what an HTTP 200 means here: "We still do not know if the capture operation will be successful or not."

Even the webhook's success is a promise. After a `CAPTURE` event with `success` true, "In rare cases the card scheme can still reject the capture, and you will receive a CAPTURE_FAILED webhook"; this "can even happen a few days after you submitted the capture request" (card scheme is Adyen's term for a card network). The refund page says the same of refunds, with `REFUND_FAILED` and, for some bank methods, `REFUNDED_REVERSED`. Arrival of the money is not evented: "Adyen does not send a webhook message when a payment settles successfully."

Adyen's published OpenAPI definition of the Checkout API, version 72 (accessed November 2026), has three GET operations: `/paymentLinks/{linkId}`, `/sessions/{sessionId}` and `/storedPaymentMethods`. None returns a payment by its identifier. Outside your own record, the documentation gives two places to look up an online payment: Adyen's Customer Area, its back-office site, and its reports. Both use a second, longer vocabulary of statuses.

> **INFERENCE, NOT DOCUMENTED:** On Adyen the integrator's own table is the only record of a payment it can query by API, so it must store every result code and event; on Stripe it can re-read the provider's object. That is my reading of the two documented contracts for online payments. Adyen has published a reason for asynchronous modifications (a stateless edge layer, 2021) and none for offering no retrievable payment.

## What a State Machine Must Guarantee, and Four Ways to Mirror One

Any version of the model, your own copy included, owes its users three guarantees:

- **One terminal outcome.** A payment ends in exactly one final state, and a final state is never left.
- **Legal transitions only.** A message moves the record only if a rule allows that move from the current state.
- **Transitions safe to apply twice.** Applying the same message again changes nothing.

A state is terminal only if no later message from the provider can change what it promised. By that test `succeeded` and "captured" are **not terminal for the payment**, whatever the status field says. Stripe keeps the intent `succeeded` while refunds and disputes land on the Charge. Adyen sends `CAPTURE_FAILED` after a successful `CAPTURE`. A canceled payment, an expired one and a refused attempt are terminal. Success is a state with exits.

Legal transitions are a table of three columns, from-state, message and to-state, and a message with no row for the current state is recorded and not applied. A message is made safe to apply twice by the identity the provider documents for it: Stripe's event ID, and Adyen's pair of `eventCode` and `pspReference`. Stored under a unique constraint, it makes the second arrival a no-op.

Against those guarantees, a consumer can mirror the provider's machine in four ways.

| Design | What you store | What it gets right | Where it fails | When it fits |
| --- | --- | --- | --- | --- |
| A flag from the API response | `paid: true` | Nothing to maintain | Wrong whenever the response is not the outcome | A prototype |
| The provider's status, copied | One provider's status string | No mapping | Breaks when the provider adds or renames a status, or a second provider arrives | One provider whose object you can re-read |
| Your own vocabulary beside the status as received | A small state, the raw status, child records | Logic depends on a few words you control | A mapping to maintain per provider | Two providers, or one you expect to outlive |
| An event log with derived state | Every provider message, append-only | Replay after a mapping mistake; full history | More machinery; ordering rules are yours | Audit needs, or a provider with no read endpoint |

I would take the third design on the fourth's raw material: a small vocabulary of my own beside each provider's status as received, computed from provider messages stored before they are interpreted. Providers do rename states (PaymentIntent statuses were renamed in Stripe's API version 2019-02-11), two providers never share a vocabulary, and a stored message lets a mapping mistake be replayed. With one provider, a readable object and no plan for a second, the copied status is enough.

## Stripe and Adyen: Where They Differ

Seven aspects separate what each company documents from what the difference suggests. Unless a year is given, a cell cites the company's documentation or API specification (n.d., accessed November 2026), linked in the two sections above; the last column is my inference.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Where the state can be read | A PaymentIntent with a `status` field, retrievable by its ID | A result code per response and webhooks; Checkout API v72 has no operation that returns a payment by identifier | On Adyen your record is the only one you can query |
| A failed attempt | Returns the intent to `requires_payment_method`; no failed status; attempts kept as Charges | `Refused`, `Error` and `Cancelled` are final result codes; every request has its own PSP reference | Stripe links attempts for you; on Adyen, link them by your own reference |
| The two waits | `requires_action` with `next_action`; `processing` | An `action` object (since v49, May 2019) and codes such as `ChallengeShopper`; `Pending` and `Received` | Same distinction, different carrier |
| Operations after authorization | Capture is a call on the intent; a Refund is an object with a status, `failed` included | Modifications answered `received`, resolved by webhook; `CAPTURE_FAILED` and `REFUND_FAILED` can follow a success | On Adyen, plan a state for each of two asynchronous stages |
| Advice on the synchronous result | Do not fulfill on the client; use the `payment_intent.succeeded` event | "do not use the result code to update your order management system" | No material difference in the public record |
| Recommended entry point | "Stripe recommends using the Checkout Sessions API … over Payment Intents for most integrations" | "Sessions flow is the default integration that we recommend" (`/sessions` since v68, October 2021) | Both moved to a server-created session |
| Published design history | An engineering essay (2020) | Not public for result codes; an engineering post (2021) gives the reason for asynchronous modifications and a developer-advocate post (2021) the reason for `/sessions` | Stripe's reasons can be cited; most of Adyen's cannot |

On Stripe, treat an event as a prompt and read the object before you change state. On Adyen there is nothing to read back for an online payment: store every result code and webhook as received, key your record by your own reference and the PSP reference, and close what the events leave open with the settlement reports ([[payment-reconciliation-and-reporting]]).

<!-- illustration-placeholder
{
  "id": "08-two-exposures-one-record",
  "status": "pending",
  "asset": "assets/images/08-payment-state-machines/08-two-exposures-one-record.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the preceding paragraph",
  "visual_goal": "Show one integrator record fed two ways: by re-reading an object, and by assembling results and events.",
  "prompt": "Component layout in three columns. Left column: a generic payment provider box labeled \"Provider A\" containing one document card with a status tag, labeled \"object\". Right column: a generic payment provider box labeled \"Provider B\" emitting a row of four small envelopes labeled \"result\", \"event\", \"event\", \"event\". Center column: a database cylinder labeled \"your record\". Arrows: from Provider A to the center a thin dashed arrow labeled \"event\" and a thick solid two-way arrow labeled \"read again\"; from Provider B to the center a thick solid arrow passing through a small tray labeled \"inbox\" and ending at the record, labeled \"assemble\"; under Provider B a small report sheet with a thin arrow to the record labeled \"report\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "One integrator record fed by two providers in different ways.",
  "caption": "With Provider A (Stripe) an event prompts a read of the provider's object; with Provider B (Adyen) the integrator's record is assembled from result codes, events and reports."
}
-->

## In Practice at Larkfield: Mila's Payments in Five States

Under Keel, Larkfield's 2027 payments program, the record keeps the five words and adds what they could not say. Each row now also stores the provider's status as received, a `waiting_on` field (`customer`, `provider` or empty), a `closed_reason` for a pending payment that ended without money, and child rows for attempts, captures, refunds and disputes, each with an amount and a status. The mapping is Larkfield's and illustrative; the provider behavior in it is documented above.

| Larkfield state | What it promises | Moved into it on Stripe by | Moved into it on Adyen by |
| --- | --- | --- | --- |
| `pending` | No provider has confirmed an authorization | `requires_payment_method`, `requires_confirmation`, `requires_action` (customer) or `processing` (provider) | Request made; no `AUTHORISATION` webhook yet |
| `authorized` | A confirmed hold to capture or release | Intent read back as `requires_capture` | `AUTHORISATION` webhook, `success` true, where capture is manual |
| `paid` | The provider confirms the capture | Intent read back as `succeeded` | `AUTHORISATION` webhook, `success` true, where capture is automatic; or `CAPTURE` webhook, `success` true |
| `refunded` | At least one refund is confirmed | Refund object with status `succeeded` | `REFUND` webhook, `success` true |
| `disputed` | A dispute is open or lost | A Dispute object on the charge | `NOTIFICATION_OF_CHARGEBACK` or `CHARGEBACK` webhook |

At 19:42 on 9 March Mila pays €120.00 from her phone's wallet, which authenticates her on the device, so no next action is needed. Studio Noord is on Adyen. Adyen's client library shows her the result at once; the row stays `pending` and becomes `paid` when the `AUTHORISATION` webhook arrives with `success` true, seconds later *(assumption)*. There is no step through `authorized`: the account captures automatically, and Adyen's capture page says "A payment that is automatically captured does *not* trigger a separate CAPTURE webhook."

Had Studio Noord been on Stripe, the pass would have been a PaymentIntent created by the payment service and confirmed in the app. Stripe would send `payment_intent.succeeded`, and the event alone would not move the row. Keel decision K2 reads "the provider's record is the truth; the webhook is the doorbell", so the payment service retrieves the intent, finds `succeeded` and only then writes `paid`.

On 12 January, the first payment the old record could not place, the row was created `pending` with `waiting_on: customer` before the provider was called, and stayed so while the client library ran the 3-D Secure action and Mila approved in her banking app. That field tells the booking app to prompt her and a timeout job to close the attempt if she never taps.

The €84.00 refund of 18 March is a child row with its own status, `requested` until Adyen's `REFUND` webhook confirms it, and the payment's summary becomes `refunded` with two amounts beside it: captured €120.00, refunded €84.00. It needs its own status because a confirmed refund can still be followed by `REFUND_FAILED`.

None of the five words means *settled*, that the money has moved ([[clearing-and-settlement]]). `paid` promises only that the provider has confirmed the capture. Whether the money arrived is not a fact the event stream carries ("Adyen does not send a webhook message when a payment settles successfully"), so Larkfield establishes it elsewhere: in its ledger ([[payment-ledgers]]) and in the reconciliation job against the providers' reports.

## When It Goes Wrong: Late, Repeated and Contradictory Events

The cheapest failure is the repeat. The same event arrives twice; the inbox finds its identity already stored and nothing changes. For Adyen duplicates whose other fields differ, the documentation adds: "Your server should use the details from the latest webhook event."

Next, different events arrive in the wrong order, which neither provider rules out. The event is stored, then applied only if the transition table has a row for it from the current state. A "processing" notice that arrives after `paid` has no such row: it is kept and the state does not move. On Stripe the shortcut is to read the object.

Then the contradiction the table must accept. Two days after a row became `paid`, Adyen sends `CAPTURE_FAILED`. This is a legal transition, because `paid` was never terminal. The capture's child row becomes `failed`, the payment returns to `authorized`, and whatever acted on `paid` (the member's access, the studio's expected payout) is told. The same event a minute later is a repeat. The payment may come back: "Technical failures are automatically re-captured by Adyen within 10 business days."

<!-- illustration-placeholder
{
  "id": "08-late-capture-failure",
  "status": "pending",
  "asset": "assets/images/08-payment-state-machines/08-late-capture-failure.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the preceding paragraph",
  "visual_goal": "Show a success state legally left on a late contradicting event, and a repeat changing nothing.",
  "prompt": "A horizontal timeline with three day markers labeled \"day 0\", \"day 2\", \"day 2 +1 min\". Above the timeline at each marker an envelope arriving from a generic payment provider box at the top left: the first envelope labeled \"captured\" in green, the second labeled \"capture failed\" in orange, the third an identical orange envelope with a small duplicate mark labeled \"same again\". Below the timeline a single record card shown three times: under day 0 with a green tag \"paid\"; under day 2 with a blue tag \"authorized\" and a curved arrow stepping back from the first card labeled \"legal step back\"; under the third marker the same card unchanged labeled \"no change\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Timeline of a paid record stepping back to authorized after a late capture failure.",
  "caption": "A capture reported failed after the record said paid is a legal step back, and the same event arriving again changes nothing."
}
-->

Some events never arrive. A sweep finds rows still `pending` past the time their `waiting_on` allows, and what it can do next depends on the provider. On Stripe it retrieves the PaymentIntent. On Adyen, with no read endpoint, it relies on redelivery, the Customer Area's transaction list, the settlement report and documented expiries, such as card offers that "expire after 12 hours by default".

Last, a status arrives that the mapping has never seen. Stripe's lifecycle page notes that "Versions of the API before 2019-02-11 show `requires_source` instead of `requires_payment_method` and `requires_source_action` instead of `requires_action`." The rule is to store the value as received, leave the Larkfield state where it is, and raise the row for review.

## What to Take Away

**Established.**

- The API response is not the outcome. Stripe tells integrators not to fulfill from the client, Adyen not to update order systems from the result code (both n.d., accessed November 2026).
- Success can be withdrawn: Adyen documents `CAPTURE_FAILED` and `REFUND_FAILED` days after a success, and a Stripe Refund has a `failed` status.
- Both providers document repeated events, and neither guarantees their order.

**Depends on context.**

- Copying the provider's statuses is enough with one provider whose object you can re-read; with two providers, or a long horizon, keep your own vocabulary beside the status as received.
- "Read the object" is a recovery plan on Stripe; on Adyen the plan is the stored events plus the reports.

**The author's synthesis.**

- I treat every message about a payment, the API response and "succeeded" included, as a transition in someone else's record. I decide in advance which transitions I accept from which message, and write that down as a table.
- I count only states with no exits as terminal. That makes canceled final and success provisional, as both providers document.

## Questions to Ask

For a design review of your payment record, or a provider evaluation:

1. For each state in our record, which provider message or read may move a row into it?
2. Which states are terminal, and what happens to a message for a row in one of them?
3. Does "pending" say whether we wait for the customer or the bank, each with its own timeout?
4. Do we store the provider's status exactly as received, next to our own?
5. Are captures, refunds and disputes rows with amounts and statuses, or flags on the payment?
6. What identifies a repeated event at each provider, and is it stored under a unique constraint?
7. If an event never arrives, what does the sweep read at each provider?
8. What does our "paid" promise, and which system establishes that the money settled?

Mila's moment with her banking app is now a named state with a known exit: the payment waits for the customer, the provider has returned a next action, and only the provider's server-side message ends the wait, or a timeout if she never taps. One piece of the model is unopened: a failed attempt returns the payment to a state from which another can be made. [[authorization-optimization]] takes that up: why issuers (the customers' banks) decline, what providers change before trying again, and how to count an approval rate once one payment can hold several attempts.

## Sources and Evidence

*Company, product and investor sources*

- [Stripe's payments APIs: The first 10 years](https://stripe.dev/blog/payment-api-design), Michelle Bu, Stripe, 2020-12-15 — the history from Token and Charge through Sources to PaymentIntents, the two-question classification, the absence of a failed state (evidence age: 6 years).
- [How Payment Intents and Setup Intents work](https://docs.stripe.com/payments/paymentintents/lifecycle), Stripe, n.d., accessed 2026-11 — the seven statuses, SetupIntents, the 2019-02-11 renames, the Checkout Sessions recommendation.
- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents), Stripe, n.d., accessed 2026-11 — create and confirm, the client secret, one intent per cart, retrieval by ID.
- [The PaymentIntent object](https://docs.stripe.com/api/payment_intents/object), Stripe, n.d., accessed 2026-11 — the status enum and `latest_charge`.
- [Payment status updates](https://docs.stripe.com/payments/payment-intents/verifying-status), Stripe, n.d., accessed 2026-11 — fulfillment from the server-side event, polling, refunds and disputes reflected on the Charge.
- [Capture a PaymentIntent](https://docs.stripe.com/api/payment_intents/capture), [The Refund object](https://docs.stripe.com/api/refunds/object) and [The Dispute object](https://docs.stripe.com/api/disputes/object), Stripe, n.d., accessed 2026-11 — capture amounts and the seven-day default; refund statuses; a dispute as an object that names its charge.
- [Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks), Stripe, n.d., accessed 2026-11 — duplicate events and no ordering guarantee.
- [Release notes](https://docs.adyen.com/online-payments/release-notes), Adyen, entries of 2019-02-14, 2019-05-14, 2021-06-03 and 2021-10-06 — `presentToShopper`, the `action` object, modifications in the Checkout API, `/sessions` (evidence age: 5 to 7 years).
- [Faster and Simpler integration with a single API call](https://www.adyen.com/knowledge-hub/sessions-api-faster-integration), Julien Lengrand-Lambert, Adyen, 2021-10-05 — the stated reason for `/sessions`: one API call in place of three (evidence age: 5 years).
- [Design to Duty: How we make architecture decisions at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture), Adyen, 2021-07 (page metadata 2021-07-28; displayed date not read) — modifications are processed asynchronously to keep the edge layer stateless (evidence age: 5 years).
- [Result codes](https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes), Adyen, n.d., accessed 2026-11 — the result code groups and the advice not to update order systems from them.
- [Build your integration](https://docs.adyen.com/online-payments/build-your-integration), [Sessions flow](https://docs.adyen.com/online-payments/build-your-integration/sessions-flow) and [Advanced flow](https://docs.adyen.com/online-payments/build-your-integration/advanced-flow), Adyen, n.d., accessed 2026-11 — the recommended flow, session expiry and status, action types, the shopper who does not return.
- [Capture](https://docs.adyen.com/online-payments/capture) and [Refund](https://docs.adyen.com/online-payments/refund), Adyen, n.d., accessed 2026-11 — modifications answered `received`, automatic capture, failures after a successful webhook.
- [Webhook structure and types](https://docs.adyen.com/development-resources/webhooks/webhook-types) and [Handle webhook events](https://docs.adyen.com/development-resources/webhooks/handle-webhook-events), Adyen, n.d., accessed 2026-11 — the `AUTHORISATION` advice, no settlement webhook, re-capture, offer expiry, dispute events, duplicates and timestamps.
- [Response handling](https://docs.adyen.com/development-resources/response-handling), [Adyen glossary](https://docs.adyen.com/adyen-glossary) and [Payments lifecycle](https://docs.adyen.com/account/payments-lifecycle), Adyen, n.d., accessed 2026-11 — the meaning of an HTTP 200 on a capture, the PSP reference and modifications, the Customer Area's payment statuses.
- [Reports and the payments lifecycle](https://docs.adyen.com/reporting/reports-and-the-payments-lifecycle), Adyen, n.d., accessed 2026-11 — the same statuses as they appear in Adyen's reports.
- [Adyen OpenAPI definitions](https://github.com/Adyen/adyen-openapi), Adyen, Checkout API version 72, accessed 2026-11 — the list of operations, none of which returns a payment by identifier.

*Standards, regulation and official documentation*

- None.

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
