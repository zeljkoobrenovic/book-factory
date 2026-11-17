---
title: "From Invoice to Cash: Invoicing, Collections and Dunning"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What happens between “an amount is owed” and “it has been paid”, especially when the first attempt fails? Between the two stands the invoice, a frozen record of a debt that is collected through as many attempts and payment methods as it takes; Stripe retries an invoice it holds, while Adyen retries a payment that the merchant ties to its own invoice by a reference."
permalink: invoicing-collections-and-dunning
timetoread: 28 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what an invoice freezes, how one debt is collected through many payment attempts, and how to design the collection process on Stripe and on Adyen.

> **KEY POINTS:**
>
> * **The invoice is the debt, and it is frozen when issued.** Finalizing an invoice fixes its number, amounts and customer details, for tax reasons. Every later change is a new document, a credit note or a void and a reissue, and a failed payment changes nothing about the invoice.
> * **The next step depends on why the attempt failed and on how the customer pays.** A hard decline needs a new card, a soft decline needs time inside the card networks' limits, and a direct debit needs a slower schedule with at most two more tries. A message goes out only after an attempt has failed.
> * **Who holds the invoice decides what a provider can recover.** Stripe's Smart Retries retry an invoice Stripe holds, by default up to 8 times within 2 weeks on new accounts. Adyen's Auto Rescue retries a payment, tied to your billing cycle only by a reference you supply. Each has one engineering post on its retry model; neither gives a recovery rate with a stated basis.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The First of the Month** — a renewal peak delays the scheduler, and a collection process started by “no payment yet” writes to members whose cards were never charged.
> * **The Double Charge** — a scheduled retry and the customer's own payment both succeed, because nothing checks them against one open invoice.
> * **A Card by Any Other Name** — a direct debit is retried on a card schedule, although its failure arrives days later and only two more attempts are allowed.

<br>
On 1 April 2027 the card payment for Mila Janssen's €49.00 monthly membership at Studio Noord is declined: not enough money in the account. On 4 April the same card is charged again, and her bank approves. Everyone calls this “the payment was retried”. But the payment of 1 April failed and stays failed, and the charge of 4 April is a different payment with its own identifier. So what was retried? Something outlived the failure and was still there to be paid three days later.

That something is **the invoice**: the record of a debt, with a number, an amount and a period. Once issued it is frozen, and it is then **collected as one debt through as many attempts, payment methods and partial payments as it takes**. It also decides what a provider can do for you. **Stripe retries an invoice it holds. Adyen's Auto Rescue retries a payment**, linked to your billing cycle only by a reference you supply, and the invoice stays in your system.

**Where we are in the payment's journey.** Mila's €120.00 class pass of 9 March 2027 needed none of this: the amount was owed and paid in the same minute, so the debt and the payment were never seen apart. Her membership is different. [[subscriptions-and-billing-engines]] showed how a billing engine decides that €49.00 is owed on the 1st, and [[usage-metering-and-rating]] how an amount is counted from usage. This chapter covers the days between 1 April, when the amount is owed and the first attempt fails, and 4 April, when it is paid.

The chapter starts at Larkfield, the fictional studio-software platform this book follows, with 7,900 failure emails about payments nobody had attempted. It then defines the invoice and its states, shows why one invoice has many payment attempts, and works out when another attempt can succeed. Money that arrives by bank transfer follows, then three designs for who runs the collection and the comparison of Stripe and Adyen. The chapter returns to Larkfield for a record of each period's debt and a collection policy, and ends with the ways collection goes wrong.

## Setting the Scene at Larkfield: 7,900 Emails About Payments Nobody Attempted

On 1 October 2026 Larkfield's renewal job ran into a provider's rate limit. This was the Renewal Wave: 38% of monthly membership volume is attempted in the first six hours of the 1st. That night **7,900 renewals were put off to the next day**. In the evening every one of those members received an email: “Your payment failed. Please update your payment details.” No payment had failed. None had been attempted: the provider had turned the requests away at its rate limit, before any card was charged.

In 2027 Femke de Graaf, Larkfield's new Head of Payments Engineering, reads the job that sent the emails. It selected memberships whose renewal date had passed and which had no successful payment. The booking app held a membership with a next-renewal date, and the payment record store held payments. Nothing stood for “the €49.00 owed for October”, and nothing listed the attempts made against it. So **“not paid” was the only fact the job could read**, and it covers two different situations: a card the bank declined, and a card nobody had charged yet.

Femke writes three questions on the whiteboard. **What exactly is owed, and is that final? What has been tried, and how did it end? What happens next, and where does it stop?** The next three sections take them in order.

## The Invoice: A Debt With a Number and a Freeze Point

An **invoice** is a numbered, dated statement of what one customer owes one seller, for which goods or which period. It is a legal document, in most countries the basis for sales tax or value-added tax (VAT), and a financial one: until it is paid it is a receivable, money the seller is owed. A **payment** is something else: one attempt to move money. Stripe's documentation (n.d., accessed November 2026) defines invoices as “statements of amounts owed by a customer” and holds them as objects. Adyen's documentation describes payments and stored payment details and no invoice, a difference that [[subscriptions-and-billing-engines]] examines and this chapter uses.

Stripe documents five invoice states and the transitions between them, each with an API endpoint and a webhook (its page on status transitions and finalization, n.d., accessed November 2026). The table shows seven; it leaves out deleting a draft, sending an open invoice, and a failed payment on an uncollectible invoice. Stripe's overview calls `void` and `paid` terminal, though the same page lets a paid invoice return to open when its payments are taken off it. The row to notice is the third: **a failed payment moves an open invoice to open**. Nothing about the debt changes when an attempt fails.

| From | Action | Event | To |
| --- | --- | --- | --- |
| `draft` | Finalize | `invoice.finalized` | `open` |
| `open` | Pay, and the payment succeeds | `invoice.paid` | `paid` |
| `open` | Pay, and the payment fails | `invoice.payment_failed` | `open` |
| `open` | Void | `invoice.voided` | `void` |
| `open` | Mark uncollectible | `invoice.marked_uncollectible` | `uncollectible` |
| `uncollectible` | Pay, and the payment succeeds | `invoice.paid` | `paid` |
| `uncollectible` | Void | `invoice.voided` | `void` |

<!-- illustration-placeholder
{
  "id": "29-invoice-state-machine",
  "status": "pending",
  "asset": "assets/images/29-invoicing-collections-and-dunning/29-invoice-state-machine.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of invoice states and transitions",
  "visual_goal": "Show the five invoice states, that finalization is the point after which the invoice is frozen, and that a failed payment leaves the invoice open.",
  "prompt": "Create a state diagram with five rounded boxes. On the far left a box labeled \"Draft\" drawn with a dashed outline and a small pencil icon. In the center a large box labeled \"Open\". On the right, stacked top to bottom, three boxes labeled \"Paid\" (green), \"Void\" (grey) and \"Uncollectible\" (orange). An arrow named 'finalize' runs from Draft to Open and passes through a vertical teal line with a small padlock icon, labeled \"Frozen\". An arrow named 'payment succeeds' runs from Open to Paid. A curved arrow named 'payment fails' leaves Open and returns to Open as a loop. An arrow named 'void' runs from Open to Void. An arrow named 'write off' runs from Open to Uncollectible. A thin arrow named 'paid later' runs from Uncollectible up to Paid. Everything to the right of the padlock line sits on a slightly tinted background to show it can no longer be edited. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "State diagram of an invoice: draft, then a freeze line at finalization, then open with a loop for failed payments, ending in paid, void or uncollectible.",
  "caption": "An invoice can be edited only as a draft; after finalization it is frozen, and a failed payment returns it to open."
}
-->

Finalization is the freeze point. A draft can be edited, and Stripe's list of what finalizing does includes: “It allows the invoice to be paid. It ensures that an invoice number is present. It makes certain properties immutable on the invoice. It creates an incomplete payment intent for the invoice.” (The payment intent is Stripe's object for one payment; see [[payment-state-machines]].) After that, “you can’t change most of its details, including fields related to the amount or customer”, and Stripe gives the reason: “This is to satisfy the common tax-compliance requirement that finalized invoices be retained—as they were finalized—for a legally required minimum time period.” The customer's name, address and tax identifiers are copied onto the invoice at that moment and frozen with it.

So a finalized invoice is corrected by a new document. A **credit note** reduces what is owed and leaves the original as it was. Stripe's credit note page (n.d., accessed November 2026) says “a credit note doesn’t void and replace the original invoice”, and bounds the correction: “The sum of all credit notes issued for an invoice can’t exceed the total amount of the invoice.” Take a Larkfield example *(illustrative)*. Studio Noord's invoice for March 2027 is €146.68 before tax: the €89 plan plus €57.68 for text messages over its allowance, at €0.07 each. Then 180 of those messages turn out to have been counted twice ([[usage-metering-and-rating]]). A credit note for 180 × €0.07 = €12.60 leaves €134.08 due, and the invoice still says €146.68. A wrong customer detail cannot be credited away. For that Stripe documents three steps: void the invoice, duplicate it, and correct the customer information on the copy.

Two states close an invoice without money, and they mean opposite things. **Void** says the amount is not owed: the invoice was issued in error and is canceled, though its number stays on record. **Uncollectible** says the amount is owed and the seller has stopped expecting it. Stripe's invoicing overview (n.d., accessed November 2026) puts it this way: “The customer is unlikely to pay the invoice. Normally, you treat it as bad debt in your accounting process.” Bad debt is an accounting loss on money that was earned. The transitions show the difference: an uncollectible invoice can still become paid, and a void one cannot. A collection process needs both ends, because finance reports a canceled debt and a lost one differently ([[billing-revenue-recognition]]).

The document itself is becoming regulated data. The EU's VAT in the Digital Age package, according to the European Commission's page on the package (n.d., accessed November 2026), “was adopted on 11 March 2025” and “will be rolled out progressively until January 2035”. Since 14 April 2025 “Member States are able to introduce mandatory e-invoicing under specific conditions”, and “Digital Reporting Requirements will affect cross-border B2B transactions from 1 July 2030”. An electronic invoice in this sense is data, not a PDF: the directive in the package (Council Directive (EU) 2025/516 of 11 March 2025) limits the term to invoices “issued, transmitted and received in a structured electronic format allowing for their automated and electronic processing”. I verified no national mandate for this chapter. The trend is one more reason to store the finalized invoice as an immutable record and render documents from it.

## Attempts Against a Debt: Why the Invoice Outlives Its Payments

Femke's second question is about attempts. Each payment attempt is a record of its own, with its own identifier and outcome, attached to the invoice. When one fails, the attempt is marked failed, a counter goes up, and the invoice stays open: Stripe's `invoice.payment_failed` event carries an `attempt_count` that, in the words of Stripe's Smart Retries documentation (n.d., accessed November 2026), “indicates how many attempts have been made so far”. The attempts need not look alike: a card, the same card three days later, then a new card the customer typed in after an email. The debt is the only constant.

<!-- illustration-placeholder
{
  "id": "29-one-debt-many-attempts",
  "status": "pending",
  "asset": "assets/images/29-invoicing-collections-and-dunning/29-one-debt-many-attempts.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that says each payment attempt is a record of its own attached to the invoice",
  "visual_goal": "Show that one invoice stays the same while several different payment attempts are made against it, and that only the last one changes its state.",
  "prompt": "Create a horizontal timeline illustration. Along the top runs one long document-shaped bar, a generic invoice with a padlock icon, labeled \"Invoice €49\". Its left three quarters are tinted orange and labeled \"Open\"; its right quarter is tinted green and labeled \"Paid\". Below the bar, three small payment cards hang from it on thin vertical lines at three points in time, left to right. The first is a generic bank card with a red cross, labeled \"Attempt 1\". The second is the same generic bank card with a red cross, labeled \"Attempt 2\". The third is a different-colored generic bank card with a green check mark, labeled \"Attempt 3\", and its vertical line meets the bar exactly where orange turns to green. A small envelope icon sits between the second and third attempts with an arrow named 'new card' pointing to the third card. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "One invoice bar that stays open across two failed payment attempts and turns to paid at a third attempt made with a new card.",
  "caption": "The attempts fail one by one and may use different cards; the invoice stays open until one of them pays it."
}
-->

The process that works through those attempts has an old name. **Dunning** is the collection of an invoice whose payment failed or is overdue: retries, messages to the customer, and a defined end. When it fails, the business loses a customer who never decided to leave. Billing vendors call that loss involuntary churn. Recurly, one of them, defines it in its documentation (updated July 2026): “Involuntary churn refers to customer loss caused by factors outside their direct intent — expired credit cards, bank account changes, or failed payment attempts”.

How large that loss is, nobody independent says. Stripe's Billing product page (n.d., accessed November 2026) states that “Businesses using Stripe recover 55% of failed payments on average” and counts “US$8.2bn in failed payments recovered in 2025”. These are marketing claims. The 55% follows a sentence that names Smart Retries, the card account updater and cancellation surveys together, so it is not a figure for Smart Retries alone, and the page defines neither a failed payment, nor recovery, nor the businesses averaged. Stripe's documentation defines a recovery rate for a merchant's dashboard, “The percentage of subscription payment volume successfully recovered by any means after a failure”, but the product page does not say its 55% is that measure. Adyen publishes no average. Its knowledge-hub guide to recurring payments (16 June 2026) gives one customer's result for its retry feature, Auto Rescue: “Pinterest saw a 4% improvement in recovery rate on retried transactions, with expectation of reaching 10% over time”. That is Adyen's claim about one customer, first published as the customer's words in an Adyen article of 4 December 2020 **(Evidence age: 6 years; the current system may differ.)**, and neither page gives a baseline or says whether 4% means percentage points. I found no independent, dated measurement of the share of churn that is involuntary, so this chapter quotes none; its argument needs none.

Whatever its schedule, a collection process has to guarantee five things. Each row below names a failure that appears later in the chapter; the limits in the fourth row are explained in the next section.

| Requirement | Why | Without it |
| --- | --- | --- |
| The debt is paid at most once | Several attempts and several methods can be in flight | A retry and the customer's own payment both succeed |
| Every attempt is tied to its invoice | The outcome must change the right debt | A retry result that nothing can place |
| A failure message follows a failed attempt | “Not paid yet” is not a failure | Larkfield's 7,900 emails |
| Attempts are bounded for each card | Card networks limit retries and charge for excess | Fees, and more declines |
| The process ends in a named state | Access, the next invoice and finance depend on it | Debts that stay open forever |

## Can Another Attempt Succeed? Decline Type and Payment Method

The third question, what happens next, starts with whether another attempt can succeed at all. The industry shorthand is hard and soft declines. Neither is a card-network term: Visa's rules sort response codes into four categories, of which the first may never be resubmitted ([[authorization-optimization]]). A **hard decline** means the issuer, the customer's bank, will not approve this card however often it is asked. Stripe's Smart Retries documentation (n.d., accessed November 2026) lists the codes it treats this way, among them `lost_card`, `stolen_card`, `incorrect_number`, `revocation_of_authorization` and `authentication_required`. It also says what happens to the invoice: “Retries continue to be scheduled, and attempt_count continues to increment, but retries only execute after detecting a new payment method.” The debt stays open, and the card is treated as dead.

A **soft decline** may succeed later: the account is short of funds today, the bank's systems are down, or a limit is reached. The question becomes when to try. A fixed schedule picks the days in advance. Stripe's custom schedule allows “up to three retries, each with a specific number of days after the previous attempt”, and Orb, a billing system, says in its documentation (n.d., accessed November 2026) that it retries “after 1, 4, and 9 days from the initial payment attempt”. The alternative is learned timing. With Stripe's Smart Retries the merchant sets the envelope, a number of retries within 1, 2 or 3 weeks, 1 month or 2 months, and Stripe chooses the moments inside it: “For new Stripe accounts, Stripe enables Smart Retries by default and configures it for up to 8 retries within 2 weeks.” The documentation names two example signals, “The number of different devices that have presented a given payment method in the last N hours” and “The best time to pay (payments made for debit cards in certain countries might be slightly more successful at 12:01 am in local time zones)”. That is all the documentation says of the model.

Any schedule runs inside limits that neither merchant nor provider sets. Visa's rules of 24 October 2026 forbid resubmitting after a category 1 code and, for the other categories, permit “up to 20 attempts in 30 days”. Adyen's documentation (n.d., accessed November 2026) says Visa charges an “excessive retry fee” beyond the limit; that page still gives the limit as 15. Stripe's card declines page (n.d., accessed November 2026) “recommends a maximum of eight retries”. Visa's rule binds the merchant and not one of its systems, so, as I read it, a billing engine, a provider's scheduler and a checkout page all draw on one allowance. For collection the limit is an input to the schedule.

A failing card can sometimes be repaired without the customer. Card networks run **account updater** services, through which issuers pass on a reissued card's new number and expiry date; Adyen's Account Updater page (n.d., accessed November 2026) names Visa, Mastercard and Cartes Bancaires. Stripe's card documentation (n.d., accessed November 2026) says “Stripe works with card networks and automatically attempts to update saved card details whenever a customer receives a new card”, and adds: “International support varies from country to country. It isn’t possible to identify cards that support automatic updates.” Adyen's Real Time Account Updater (documentation n.d., accessed November 2026) does the repair inside the failing payment: “When you submit a payment that is refused, our Real Time Account Updater instantly checks for updated card details. If there is an update, we immediately retry the payment with the updated card details. This all happens while the payment is being processed, and appears as a single transaction.” It covers Visa, Mastercard and Cartes Bancaires cards, on payments the merchant initiates from stored details, once Adyen's support team has enabled it. A network token, the card network's stand-in for the card number, stays valid through a reissue by design ([[network-tokens]]). None can be relied on for a given card, so they reduce dunning without replacing it.

A direct debit breaks the card pattern. A **direct debit** pulls money from a bank account under a **mandate**, the payer's standing permission ([[local-payment-methods]]); SEPA Direct Debit is the scheme of the Single Euro Payments Area (SEPA) and Bacs the British one. Its failure does not come back in seconds. Stripe's SEPA Direct Debit page (n.d., accessed November 2026) says “Most failures occur within 6 business days after initiation”. On Adyen the first answer is always positive and the failure arrives later as what Adyen calls a chargeback, here the payer's bank returning the debit: “Because SEPA transactions always have `eventCode` **AUTHORISED** in the response, these require a different rescue logic compared to card transactions.” Both providers then cap the retries at two. Stripe retries SEPA and Bacs debits only if the merchant has turned those retries on, only for “Insufficient funds” and at most 2 times within 30 days, and notes that “Direct debit retries use the payment method’s retry configuration, not the general card retry policy.” Adyen's Auto Rescue for SEPA (documentation n.d., accessed November 2026) applies to two return reasons, AM04 for insufficient funds and MS03 for no reason given, with “a maximum of two rescue attempts within the rescue window”. It gives two reasons: the first refusal arrives later, which leaves fewer days, and “chargebacks are typically fined by the issuing bank”.

The last instrument is the customer. A message works on every branch, and after a hard decline it is the only thing that works. Stripe's customer email documentation (n.d., accessed November 2026) describes emails for failed payments and expiring cards that “include a link to a page where the customer can update their payment method”. Adyen documents an optional payment link, “Valid for 5 days”, that the merchant receives by webhook when Auto Rescue ends without success and can send to the customer. Two rules of mine follow. The message must say what the customer can do: “add a new card” after a stolen-card decline, “we will try again on Friday” after insufficient funds. And it must be triggered by a failed attempt, never by the absence of a payment, which was the fault in Larkfield's October emails.

<!-- illustration-placeholder
{
  "id": "29-next-step-after-a-failed-attempt",
  "status": "pending",
  "asset": "assets/images/29-invoicing-collections-and-dunning/29-next-step-after-a-failed-attempt.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on the message to the customer, at the end of the section on decline type and payment method",
  "visual_goal": "Show that the next step after a failed attempt branches by the reason for the failure and the payment method, and that every branch ends either in payment or in a named end state.",
  "prompt": "Create a left-to-right decision tree. On the far left a generic invoice icon with a red cross beside it, labeled \"Attempt failed\". From it three branches fan out to the right. Top branch: a generic bank card with a broken-chain icon, labeled \"Hard decline\", followed by an arrow named 'ask customer' to an envelope icon labeled \"New card\". Middle branch: a generic bank card with a small clock icon, labeled \"Soft decline\", followed by an arrow named 'wait' to a calendar icon labeled \"Retry later\". Bottom branch: a generic bank building icon with a slow snail-shaped clock, labeled \"Direct debit\", followed by an arrow named 'wait longer' to a calendar icon labeled \"Two tries\". On the far right all three branches converge on two stacked boxes: a green box labeled \"Paid\" reached by an arrow named 'success', and an orange box labeled \"Paused\" reached by an arrow named 'window ends'. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Decision tree from a failed attempt to three branches, hard decline, soft decline and direct debit, each leading to paid or paused.",
  "caption": "A hard decline needs a new card, a soft decline needs time, and a direct debit needs more time and allows two more tries; every branch ends paid or in a named state."
}
-->

## Money That Arrives on Its Own: Bank Transfers, Partial Payments and Cash Application

Everything so far assumed that the merchant starts the payment. With a bank transfer the customer does, and decides how much to send and when. Collection turns into **cash application**: matching money that has arrived to the invoices it was meant to pay. Stripe's bank transfer documentation (n.d., accessed November 2026) states the problem: “bank transfers don’t allow you to control the amount a customer sends to you, which means that customers might send too much or too little money by accident”. Each customer gets “a unique virtual bank account number” shown on the invoice, so the sender is known. And money that arrives is held “in a customer balance” until it is applied.

Stripe's reconciliation page (n.d., accessed November 2026) publishes the order in which it applies that balance. It first looks for an invoice number in the transfer's reference, then for a payment reference, then for “a group of between one and five invoices and PaymentIntents awaiting the exact amount available”. Failing that, it pays the invoices it can pay in full, oldest due first. A transfer smaller than an invoice is applied as a partial payment only if the merchant has enabled that and the customer wrote the invoice number in the transfer. What cannot be matched stays visible and ages: after 75 days in the balance Stripe “automatically attempts to return the funds to the customer’s bank account”. I would copy both ideas into any system that accepts transfers.

On Adyen I found nothing equivalent. Its documentation describes bank transfers and direct debits as payment methods. The Bank Transfer page (n.d., accessed November 2026) gives each payment “a unique virtual bank account number”, which matches a transfer to one payment, not to a customer's invoices. I found no invoice object, no customer balance for receivables and no cash-application feature (documentation and help center, November 2026). That is an absence in the public record, not a statement by Adyen. For a merchant it means that transfers arriving through Adyen are applied to invoices in the merchant's own system, or in a billing product connected to it.

## Who Runs the Collection: Three Designs

Three designs cover most of what is built. In the first, **the provider holds the invoice and runs the dunning**. This is Stripe Billing. Smart Retries choose times “to increase the chance of successfully paying an invoice”. Because the retry belongs to the invoice, it uses whatever payment method is current, in a documented order that starts with the subscription's default payment method. The end is documented too: “If recovery fails, the subscription transitions according to your settings”, which can cancel it, mark it unpaid, leave it past due or pause it.

In the second design **the merchant holds the invoice and the provider retries the payment**. This is Adyen's Auto Rescue, which, in the words of Adyen's documentation (n.d., accessed November 2026), “automatically retries refused or charged back shopper-not-present transactions such as subscription renewals. It uses smart logic to decide which payments can succeed when retried later, and performs these retries at optimal times”. “Smart” and “optimal” are Adyen's words, with no measure behind them. Adyen's support team or account manager enables the feature. For cards the retries happen inside a rescue window, the period during which Adyen keeps trying: “one calendar month” when enabled for the account, or between 1 and 48 days when set on a payment. The response to a refused payment says whether a rescue is scheduled, each retry “is a separate transaction, and thus generates a unique `pspReference`”, and results arrive by webhook. What ties them to a debt is a field the merchant fills: “a unique `merchantOrderReference`. This should represent a specific billing cycle or subscription”.

In the third design **the merchant's own billing system holds the invoice and schedules every attempt**, and the provider only charges. Orb's documentation (n.d., accessed November 2026) shows the pattern on top of a payment gateway, with integration pages for Stripe and for Adyen: retries after 1, 4 and 9 days, and “If payment method is updated prior to exhaustion of the dunning period, Orb will immediately try to collect on the invoice.” Adyen's press release of 1 July 2026 announced that its acquisition of Orb had closed that day ([[subscriptions-and-billing-engines]]). As of November 2026 I found no Adyen documentation of an integrated billing product, so this is Orb's documentation about Orb, not a description of Adyen's platform.

The rule I use: **the system that holds the invoice owns the schedule, and no debt has two schedulers.** A scheduler that does not hold the invoice cannot know that the customer paid another way, saved a new card or canceled. Adyen's instruction to cancel a rescue in exactly those cases shows the gap. Two schedulers also spend one network allowance twice. The second design is still reasonable for a merchant with no billing system, provided it keeps a small invoice table and joins every retry to it by reference.

| Design | Holds the invoice | Schedules retries | What you build | Right when | Main risk |
| --- | --- | --- | --- | --- | --- |
| Provider billing (Stripe Billing) | The provider | The provider, for each invoice | A mirror of invoice state; the choice of end state | Your billing runs on the provider | A stale copy; defaults nobody chose |
| Provider retries payments (Adyen Auto Rescue) | You | The provider, for each payment | An invoice table, a reference scheme, webhook handling, cancellation | Your invoices are simple and you want the provider's timing | A retry racing an event only you know about |
| Own billing system | You, or a billing product | You | A schedule by decline type and method, messages, limits | You have several providers, or rules of your own | Building and measuring it yourself |

One limit applies to both provider designs: the public record of the retry logic is thin and dated. Stripe's documentation publishes two example signals and, on its revenue recovery page (n.d., accessed November 2026), the sentence that Smart Retries “are more effective than scheduled retries”, with no figure. Adyen's publishes “smart logic” and “optimal times”. Each has one blog post on its model: Stripe on 23 January 2024 (a model that “predicts the optimal time to retry a failed payment” from “more than 500 attributes”), Adyen on 3 December 2020 (a contextual multi-armed bandit that, in one experiment, converted “about 6% more orders than the baseline”, a retry every four days) **(Evidence age: 2 and 6 years; the current systems may differ.)**. Neither documents the model now running or a recovery rate with a stated basis.

> **INFERENCE, NOT DOCUMENTED:** Both posts describe a model that predicts when a retry of a failed payment is most likely to be approved, trained on the provider's own payment history. That the models running in November 2026 still work this way is my assumption, and nothing public allows the two to be compared. A merchant choosing between them on recovery has to measure on its own renewals; [[authorization-optimization]] shows how.

<!-- illustration-placeholder
{
  "id": "29-who-holds-the-invoice",
  "status": "pending",
  "asset": "assets/images/29-invoicing-collections-and-dunning/29-who-holds-the-invoice.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the inference block that closes the section on the three designs",
  "visual_goal": "Contrast a provider that holds the invoice and retries it with a provider that sees only payments and retries a payment the merchant links to its own invoice by a reference.",
  "prompt": "Create a side-by-side comparison in two panels separated by a thin vertical line. Left panel, headed by a generic payment-company building labeled \"Provider A\": inside the building sits a generic invoice icon with a padlock, and a circular arrow named 'retry' loops from the invoice to a generic bank card and back; a small merchant shop stands outside to the left, connected to the building by a single arrow named 'mirror'. Right panel, headed by a generic payment-company building labeled \"Provider B\": inside the building sits only a generic bank card with a circular arrow named 'retry' around it; the generic invoice icon with a padlock sits outside, inside a small merchant shop to the left; a dashed line with a tag icon labeled \"Reference\" connects the merchant's invoice to the provider's card. Under the left panel a short label \"Retries the invoice\"; under the right panel a short label \"Retries the payment\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two panels: in the first the invoice sits inside the provider, which retries it; in the second the invoice sits with the merchant and is linked by a reference to a payment the provider retries.",
  "caption": "Provider A (Stripe) retries an invoice it holds; Provider B (Adyen) retries a payment that the merchant ties to its own invoice by a reference."
}
-->

## Stripe and Adyen: Where They Differ

The table gathers what the chapter has cited. Every Stripe and Adyen cell comes from the documentation and vendor pages quoted above (n.d., accessed November 2026, unless a date is given there), and the last column is my inference.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Unit being recovered | The invoice: retries aim at “successfully paying an invoice” | The payment: a refused or charged-back shopper-not-present transaction, tied to a billing cycle by `merchantOrderReference` | The provider that holds the debt retries the debt; the other retries what it can see |
| Invoice and corrections | Five states; credit notes; void and reissue | No invoice object found in Adyen's documentation | On Adyen the invoice is yours to build or buy |
| Default envelope | On by default for new accounts: up to 8 retries within 2 weeks; window from 1 week to 2 months | Off until Adyen's support enables it; for cards one calendar month, or 1 to 48 days set on a payment | A self-service default against an account-managed setting |
| Hard declines | Listed codes; retries stay scheduled and run only after a new payment method | The response says no rescue is scheduled, “For example, because of account closure or fraud”; no code list on the page | Stripe keeps the debt waiting for a new card; on Adyen the waiting is your logic |
| Direct debit | SEPA and Bacs, when the merchant turns retries on: insufficient funds only, at most 2 retries in 30 days | SEPA: return reasons AM04 and MS03, at most two attempts; a 42-day window for the account | No material difference in the public record |
| Card repair | Automatic updates of saved cards; coverage varies by country and cannot be checked for a given card | Real Time Account Updater inside the refused payment, for Visa, Mastercard and Cartes Bancaires | Documented at different points of the payment; on either, do not count on it for a given card |
| Published logic and results | Two example signals; a 2024 post on the model; a marketing average of 55% for its recovery tools together, without definitions | “smart logic”, “optimal times”; a 2020 post on the model; one customer's 4% improvement in a 2026 guide, without a baseline | Not comparable; measure your own |

On Stripe, mirror the invoice's state from Stripe's record, decide on purpose what a subscription becomes when recovery fails, and save a new card where the retry looks for it, since the payment-method order is documented. On Adyen, build the invoice table first. Derive `merchantOrderReference` from invoice and period, treat every rescue webhook as an attempt against that invoice, and cancel the rescue the moment the customer pays another way or leaves.

## In Practice at Larkfield: One Period Record, Two Providers

Larkfield has both problems. Its own studio subscriptions, the €89, €189 and €349 plans, have been billed with Stripe Billing since 2018, so Stripe holds those invoices: the first design. Member renewals are different. The studio is the seller, the booking app decides that Mila owes Studio Noord €49.00 on the 1st, and the payment service charges through whichever provider the studio is on. Larkfield therefore holds that debt itself on both providers, which is the third design. Under decision K5 of Keel, its 2027 program to repair the payments estate, it runs the only retry schedule for member renewals, and the providers' scheduled retries are not used for them *(Larkfield's choice, an illustration)*.

Keel gives the debt a record: the period record of [[subscriptions-and-billing-engines]], one row for each membership and billing period, written before the first attempt with the amount due. Its states follow the invoice vocabulary (open, paid, void, and now uncollectible), and each attempt is a child row with the provider's reference and outcome. Decision K1 derives the idempotency key, the token that makes a repeated request safe ([[idempotency-and-retries]]), from membership, period and attempt number, and on Adyen the period record's identifier also travels as the order reference. “Open with no attempts” and “open with one declined attempt” are now different facts, which the October job could not tell apart.

The policy that runs over the record branches on decline type and payment method, and every branch ends somewhere *(Larkfield's policy; the days are illustrative)*. A member keeps access while the record is open inside the 14-day window. Mila's renewal takes the first row. Her €49.00 is declined on 1 April 2027 with Visa code 51, insufficient funds, a soft decline. She gets an email the same day, scheduled attempt 2 runs on day 3, 4 April, and it is approved. That is one period record with two attempt rows, and the record moves from open to paid; [[journey-failed-renewal]] follows it across every system.

| Situation | Action | Limit |
| --- | --- | --- |
| Card, soft decline | Email on the first failure; retry on days 3, 7 and 12 | 3 retries in 14 days |
| Card, hard decline | No retry; email and in-app request for a new card; attempt as soon as one is saved | None on the old card |
| Direct debit, insufficient funds | One new collection after 7 days | Two retries at most, as the providers allow |
| Direct debit, any other failure | Ask for a new mandate or another payment method | No retry |
| Still unpaid on day 14 | Membership paused; the period record stays open | — |
| Still unpaid on day 30 | Period record marked uncollectible; membership ended | — |

Counted for each renewal, the policy's result is a curve. The table below uses the December 2026 card renewals from [[authorization-optimization]], and every figure in it is an illustrative assumption. Of 51,240 failed first attempts, 25,620 were paid within fourteen days: half. More than half of that recovery came by day 3, and the second week added 4,560 renewals. The 25,620 still unpaid, about €1.26 million of studio revenue at the typical €49, are mostly waiting on a member, not on a schedule. The “half” is Larkfield's ratio on a stated basis, and it cannot be set beside a vendor's undefined 55%.

| Card renewals, December 2026 *(assumptions)* | Renewals | Share of 540,000 due |
| --- | --- | --- |
| Paid at the first attempt | 488,760 | 90.5% |
| Paid by day 3 | 502,260 | 93.0% |
| Paid by day 7 | 509,820 | 94.4% |
| Paid by day 14 | 514,380 | 95.3% |
| Unpaid after day 14 | 25,620 | 4.7% |

The October failure needs one rule on top of this. A failure message is sent for a declined attempt row on an open period record, and for nothing else. Under K5 the renewal job paces itself over 18 hours, so on any 1st most renewals are due and unattempted for hours. Had the rule existed on 1 October 2026, the 7,900 delayed renewals would have been open, unattempted and silent.

## When It Goes Wrong

The first failure is a debt paid twice. A member gets the failure email, opens the link and pays with a new card, while a scheduled retry of the old card is approved the same hour. Larkfield's Double Charge of 1 November 2026, when 1,840 members were charged twice after a timeout was retried under a new idempotency key, was the same damage by another route. Where the scheduler does not hold the invoice, stopping it is a separate call. Adyen tells merchants that when a shopper provides a new payment method or cancels, “you should cancel the Auto Rescue process for the refused payment”, and it confirms the cancellation later by webhook. Such a call can lose a race. The guard belongs on the invoice: it accepts one successful attempt, and a second success is detected and refunded automatically.

The second failure is a result that arrives after the process has ended. The merchant's timer pauses the membership on day 14 while a direct debit sent on day 12 is still on its way, or while a provider's rescue is still running. For a SEPA rescue attempt Adyen says “You will receive the webhook 16 days after the rescue attempt”. The end of dunning therefore has to wait for the slowest attempt still outstanding, or be able to reopen. A direct debit also counts as paid when its collection is confirmed, not when it is sent ([[local-payment-methods]]), and a webhook that never arrives is found by a sweep of open attempts ([[payment-webhooks-and-events]]).

The third failure comes after payment. Support refunds €12.60 on the payment and nobody issues a credit note, so the invoice says €146.68 paid in full while the bank statement says €134.08. Stripe keeps the two operations separate on purpose: “Issuing a credit note doesn’t automatically refund the customer’s payment method”, and for a paid invoice “the sum of the refund, credit, and out-of-band payment amounts must equal the credit note total”. The repair is a rule of order: the document first, the money as its consequence. A reconciliation then compares invoices net of credit notes with payments net of refunds ([[payment-reconciliation-and-reporting]]).

## What to Take Away

**Established.**

- A finalized invoice is kept as issued and corrected by a credit note, or by voiding and reissuing; Stripe's documentation gives tax retention rules as the reason.
- A failed attempt leaves the invoice open. The attempt fails and the debt does not (Stripe's documented transitions).
- A hard decline is not retried on the same card, and card networks cap retries of the rest (Visa's rules, 24 October 2026: 20 attempts in 30 days).
- A direct debit fails days later and is retried at most twice, in both providers' documentation.

**Depends on context.**

- Who schedules: the provider when it holds the invoice; your own system when you hold it and have several providers; Adyen's Auto Rescue when your invoices are simple and you join retries to them by reference.
- How long to try: Stripe's default for new accounts is up to 8 retries in 2 weeks, Adyen's account-level window for cards a calendar month. A monthly product gains little from chasing past the next invoice.
- Learned or fixed timing: the gain is unmeasured in public. With enough volume, test one against the other; without, take the default.
- Where to end: pausing, canceling or leaving a subscription unpaid depends on what access costs you while the debt is open.

**The author's synthesis.**

- Model the debt before the payment. The freeze, the attempts, the branches, cash application and the three designs are one idea applied five times: the debt is the stable object, and every payment is an event against it. The schedule, the payment method and the provider can then change without changing what is owed.
- The holder of the invoice owns the one schedule. A retry feature is only as aware of new cards, other payments and cancellations as the system that holds the debt lets it be, which is why Stripe and Adyen differ where they do.
- I treat every published recovery percentage as a hypothesis about my own renewals, because none is both current and defined.

## Questions to Ask

1. Where does the record of each amount owed live, and what freezes it?
2. For any unpaid invoice, can we list every attempt made, its payment method and its outcome?
3. What triggers a failure message: a failed attempt, or the absence of a payment?
4. Which declines do we never retry on the same card, what do we ask the customer instead, and what are our separate rules for direct debit?
5. How many systems can schedule a retry of the same debt, and which of them is switched off?
6. In what state does dunning end, after how many days, and what happens then to the invoice, to access and to the next invoice?
7. If a customer pays while a retry is in flight, what stops the second payment or refunds it?
8. How do we correct a finalized invoice, and is every refund matched by a credit note?

So what was retried on 4 April? Nothing was. April's debt stayed open after a soft decline, a second attempt was made against it, and the debt, not the payment of 1 April, became paid. Where that debt is a tax invoice, finalization froze the customer's address and tax number along with the amounts, because one line of the invoice is a tax amount that had to be right before the freeze. [[billing-and-payment-tax]] takes up that line: who owes the tax, what decides the rate, and how much of the work a payment provider's tax product does.

## Sources and Evidence

*Company, product and investor sources*

- [Status transitions and finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions), Stripe documentation, n.d., accessed 2026-11 — invoice states and transitions, what finalization does, the tax reason for immutability, void and duplicate.
- [Invoicing overview](https://docs.stripe.com/invoicing/overview), Stripe documentation, n.d., accessed 2026-11 — the meaning of void and uncollectible.
- [Issue credit notes](https://docs.stripe.com/invoicing/dashboard/credit-notes), Stripe documentation, n.d., accessed 2026-11 — the definition of an invoice, credit notes and their limit, credit notes and refunds.
- [Automate payment retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries), Stripe documentation, n.d., accessed 2026-11 — Smart Retries defaults and signals, hard decline codes, custom schedules, end states, direct debit retries.
- [Revenue recovery](https://docs.stripe.com/billing/revenue-recovery), Stripe documentation, n.d., accessed 2026-11 — the statement that Smart Retries are more effective than scheduled retries.
- [Automate customer emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails), Stripe documentation, n.d., accessed 2026-11 — failed-payment and expiring-card emails with a link to update the payment method.
- [Card declines](https://docs.stripe.com/declines/card), Stripe documentation, n.d., accessed 2026-11 — the recommendation of at most eight retries.
- [How cards work](https://docs.stripe.com/payments/cards/overview), Stripe documentation, n.d., accessed 2026-11 — automatic card updates and their coverage.
- [SEPA Direct Debit payments](https://docs.stripe.com/payments/sepa-debit), Stripe documentation, n.d., accessed 2026-11 — failure reasons and timing of a failed debit.
- [Bank transfers](https://docs.stripe.com/payments/bank-transfers), Stripe documentation, n.d., accessed 2026-11 — the customer balance and the 75-day return of unreconciled funds.
- [Bank transfer payments on invoices](https://docs.stripe.com/invoicing/bank-transfer), Stripe documentation, n.d., accessed 2026-11 — virtual bank account numbers and partial payments.
- [Reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation), Stripe documentation, n.d., accessed 2026-11 — the order in which arrived funds are applied to invoices.
- [How we built it: Smart Retries](https://stripe.com/blog/how-we-built-it-smart-retries), Kiran Chandran, Stripe blog, 2024-01-23 — the Smart Retries model: prediction of retry time, more than 500 attributes, the 2023 ensemble replacing XGBoost (vendor post; evidence age 2 years).
- [Revenue recovery analytics](https://docs.stripe.com/billing/revenue-recovery/recovery-analytics), Stripe documentation, n.d., accessed 2026-11 — the dashboard definition of recovery rate.
- [Stripe Billing](https://stripe.com/billing), Stripe product page, n.d., accessed 2026-11 — the 55% and US$8.2bn recovery claims (vendor marketing page).
- [Auto Rescue](https://docs.adyen.com/online-payments/auto-rescue), Adyen documentation, n.d., accessed 2026-11 — what Auto Rescue retries and Adyen's wording on its logic.
- [Auto Rescue for card payments](https://docs.adyen.com/online-payments/auto-rescue/cards), Adyen documentation, n.d., accessed 2026-11 — enablement, rescue window, order reference, webhooks, payment link, cancellation.
- [Auto Rescue for SEPA payments](https://docs.adyen.com/online-payments/auto-rescue/sepa), Adyen documentation, n.d., accessed 2026-11 — return reasons, the two-attempt limit and its reasons, the 42-day window, the 16-day webhook.
- [Account Updater](https://docs.adyen.com/online-payments/account-updater), Adyen documentation, n.d., accessed 2026-11 — the card networks that offer an account updater service.
- [Real Time Account Updater](https://docs.adyen.com/online-payments/account-updater/real-time-account-updater), Adyen documentation, n.d., accessed 2026-11 — the update and retry inside a refused payment.
- [Mapping to Visa system integrity fee categories](https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees), Adyen documentation, n.d., accessed 2026-11 — Visa's excessive retry fee; the page still gives the limit as 15.
- [Bank Transfer](https://docs.adyen.com/payment-methods/bank-transfer), Adyen documentation, n.d., accessed 2026-11 — a virtual bank account number for each payment.
- [Rescuing failed subscription payments using contextual multi-armed bandits](https://www.adyen.com/knowledge-hub/rescuing-failed-subscription-payments-using-contextual-multi-armed-bandits), Ralph Myers and Richard Price, Adyen, 2020-12-03 — the Auto Rescue model (contextual bandit on a random forest) and one experiment against a four-day fixed schedule (vendor post; evidence age 6 years).
- [Recurring payments: A guide for enterprise businesses](https://www.adyen.com/knowledge-hub/recurring-payments), Adyen knowledge hub, 2026-06-16 — one customer's Auto Rescue result (vendor marketing article).
- [Rescuing failed payments to make subscriptions unstoppable](https://www.adyen.com/en_GB/knowledge-hub/rescue-failed-subscription-payments), Gill Wells, Adyen knowledge hub, 2020-12-04 — the customer quotation behind that result (evidence age: 6 years).
- [Adyen Closes Talon.One and Orb Acquisitions; Announces Leadership Updates Across Product and Finance](https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates), Adyen press release, 2026-07-01 — the closing date of the Orb acquisition.
- [Essential dunning](https://docs.withorb.com/financial-operations/essential-dunning), Orb documentation, n.d., accessed 2026-11 — a fixed retry schedule in a billing system above the payment provider.
- [Adyen](https://docs.withorb.com/integrations-and-exports/adyen), Orb documentation, n.d., accessed 2026-11 — Adyen as one of the payment gateways Orb collects through.
- [Involuntary churn](https://docs.recurly.com/recurly-subscriptions/docs/involuntary-churn), Recurly documentation, updated 2026-07 — a vendor's definition of involuntary churn.

*Standards, regulation and official documentation*

- [VAT in the Digital Age (ViDA)](https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en), European Commission, n.d., accessed 2026-11 — adoption and roll-out dates for e-invoicing and digital reporting.
- [Council Directive (EU) 2025/516](http://publications.europa.eu/resource/celex/32025L0516), Council of the European Union, 2025-03-11 — recital 9, what counts as an electronic invoice.
- [Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf), Visa, 2026-10-24 — Table 7-2, reattempt limits by decline category.

*Research and practitioner sources*

- None. No independent measurement of involuntary churn or of dunning recovery rates was found.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
