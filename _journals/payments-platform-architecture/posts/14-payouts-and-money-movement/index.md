---
title: "Getting Money Out: Payouts and Money Movement"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How does money leave a payment provider and reach a bank account, and what happens when it does not arrive? In two steps that finish at different times: the provider debits the balance, a bank network delivers or returns the transfer later, and “paid” means sent, not received."
permalink: payouts-and-money-movement
timetoread: 24 min read
---

> **IN THIS CHAPTER, YOU WILL:** Follow a payout from the provider's balance onto a bank network and learn to record it so that a transfer that comes back days later has somewhere to land.

> **KEY POINTS:**
>
> * **“Paid” means sent.** The provider debits the balance when it instructs the transfer; a bank network then delivers it on its own schedule. Stripe's documentation (accessed November 2026) says a failed payout "might initially show as `paid`"; Adyen's says a non-instant payout "cannot fail" but can be returned.
> * **A payout that fails comes back as a new credit, days later.** Both providers book the return as a separate transaction. A payout record needs four states (instructed, sent, arrived, returned) and must stay open through the return window.
> * **Check the payee before the money leaves.** A transfer to a valid account that belongs to someone else does not come back. Since 9 October 2025, euro-area payment providers must check the payee's name before a credit transfer is authorized; the result is a warning, and the decision stays with the sender.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Stranded Payout** — a payout is closed when the provider says "paid", the bank returns it a week later, and the credit has no payout to attach to and no owner.
> * **The Black-Box Balance** — a returned payout raises a seller's balance with a line nobody can explain, because the record that would explain it was already closed.

<br>
A studio owner calls support. Her dashboard has shown this week's payout as "Paid" for eight days, and **her bank account shows nothing**. The support agent checks the provider: the balance was debited that day, for the right amount. No system is broken. Both statements are true.

They are true because a payout is **two processes that finish at different times**. The first is accounting: the provider debits the balance it owes and instructs a transfer. The second is delivery: a bank network carries the instruction to the receiving bank, which credits the account or refuses. The provider runs only the first, reports it as "paid", and learns of a failure only when the money comes back days later **as a new credit**. Reading "paid" like an HTTP 200 answers a different question.

**Where we are in the payment's journey.** Mila Janssen's €120.00 class pass, bought on Tuesday 9 March 2027 at 19:42, left €117.47 owed to Studio Noord in Adyen's books ([[balances-and-funds-flows]]). This chapter is the step where that amount leaves the provider for the bank account of Ines Bakker, the studio's owner. It is the first movement outside the provider's ledger. The money is due in her account on Thursday 11 March; Larkfield's record calls the payout arrived only on Thursday 25 March, and the chapter explains why those are two different facts.

The chapter starts at Larkfield with 412 payouts that were marked paid and came back. It then separates the provider's accounting from the bank's delivery and describes the networks a payout travels on. Next come the payout states Stripe and Adyen document, including the return, and the check of the payee's name before sending. Three ways to record a payout and a comparison of the two providers follow. It ends with one payout worked through Larkfield's record and the failures that remain.

## Setting the Scene at Larkfield: 412 Payouts Marked Paid

Larkfield is the fictional studio-software platform this book follows ([[meet-larkfield]]): studios sell classes through it, and Stripe or Adyen pays each studio out. In June 2026 a form in the studio back office let owners change their bank details, and nothing checked that the new account belonged to the studio. Over three weeks, receiving banks sent back **412 payouts worth €386,000**. Larkfield calls it the Payout That Bounced.

The returns were ordinary. The damage came from Larkfield's payout record, which had one final state: when the provider's notification said paid, the record was closed. A credit that arrived at the provider days later therefore had no open payout to attach to and no team that owned it. The returns **sat unreconciled** while Aylin Demir's support team heard from studios. It took 19 days to pay every studio, and two studios left.

When Femke de Graaf takes over payments engineering in January 2027, the incident gives her three questions, and they are this chapter's. What does "paid" assert? For how long after it can a payout still come back? And what should have stopped these transfers before they left?

## Two Processes, Two Clocks: Why “Paid” Means Sent

A **payout** is the provider sending money it owes you, from a balance in its own books, to a bank account outside the provider; a transfer between two balances inside the provider never leaves the ledger. Stripe's documentation (n.d., accessed November 2026) puts it in one line: Stripe "sends funds from your available balance to your bank account as payouts". The balance is the provider's debt to the merchant ([[balances-and-funds-flows]]); the payout is that debt being paid.

The first process is accounting, inside the provider's ledger ([[payment-ledgers]]). Adyen's payout lifecycle page (n.d., accessed November 2026) names its steps: received, then authorised ("we reserve the payout amount on your balance account"), then booked ("Adyen deducts the funds from your balance account and creates a transaction"). All of it finishes before any bank is involved.

The second process starts there. The provider, or a bank it works with, submits a payment instruction to a **payout rail**: the bank network that carries a transfer to the receiving bank. Many rails process instructions in batches, a few times per business day, and each has a **cut-off time**, after which an instruction waits for the next cycle. The receiving bank then credits the payee and sets the **value date**, the date from which it counts the money as the payee's.

| Step | Who holds the money | Who can see the state |
| --- | --- | --- |
| Balance at the provider | The provider, as its debt to the merchant | Provider and merchant |
| Instruction submitted to the rail | In transit between banks | The provider sees "submitted" |
| At the receiving bank, before credit | The receiving bank | The receiving bank only |
| Credited to the account | The account holder, who may not be the intended payee | The account holder and their bank |

Because a batch rail sends the sender no confirmation that the payee was credited, the status a provider shows after sending describes **the provider's own action**. Both say so. Stripe's status table for its third-party payout product (n.d., accessed November 2026) reads: "A posted status doesn’t guarantee that your recipient has received money, because their bank might delay the release of funds." Adyen gives a bank transfer on a non-instant route a `tracking.estimatedArrivalTime`, which is a forecast.

<!-- illustration-placeholder
{
  "id": "14-two-clocks",
  "status": "pending",
  "asset": "assets/images/14-payouts-and-money-movement/14-two-clocks.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that says the provider's status describes its own action",
  "visual_goal": "Show a payout as two processes: accounting that ends with a debit, and delivery that ends later with a credit or a return.",
  "prompt": "Two horizontal timelines, one above the other. Upper timeline, blue, labeled \"Provider ledger\": three nodes left to right labeled \"Instructed\", \"Reserved\", \"Debited\", with a flag above the last node labeled \"Paid\". An orange arrow named \"instruction\" drops from \"Debited\" to the start of the lower timeline. Lower timeline, teal, labeled \"Bank rail\" and visibly longer: nodes labeled \"Submitted\", \"Cut-off\", \"Receiving bank\". From \"Receiving bank\" a green arrow named \"credit\" runs to a bank-account icon labeled \"Arrived\", and an orange curved arrow named \"return\" bends back up to the upper timeline, ending at a plus sign labeled \"New credit\". A clock icon ends each timeline; the lower clock shows a later time. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two timelines: the provider's ledger ends at a debit flagged paid; the bank rail ends later in a credit or a return.",
  "caption": "The provider's accounting ends with a debit it reports as paid; the bank rail's delivery ends later, with a credit or with a return that arrives as a new credit."
}
-->

The second process does send one signal back. A **payout return** is the receiving bank sending the money back after the rail accepted the transfer. Stripe's Global Payouts documentation (n.d., accessed November 2026) gives the usual causes: "Incorrect destination information causes most returned payouts (for example, the provided bank account is closed, or the account holder’s details don’t match the recipient’s information)." The return travels a rail too, so it reaches the sender as a new transaction, days after the payout was marked sent.

<!-- illustration-placeholder
{
  "id": "14-letter-in-the-post",
  "status": "pending",
  "asset": "assets/images/14-payouts-and-money-movement/14-letter-in-the-post.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that defines a payout return",
  "visual_goal": "A posting receipt proves sending, not delivery; an undeliverable letter comes back days later.",
  "prompt": "A three-part scene read left to right. Left: a person at a post-office counter holding a small receipt slip labeled \"Sent\", with a blue arrow named \"posted\" leaving toward the middle. Middle: a van on a road under a small calendar icon, labeled \"In transit\". Right: a house with a closed mailbox and a question mark above it, labeled \"Arrived?\". Below the road, an orange arrow named \"return to sender\" curves from the house back to the left, ending at the sender's own mailbox, which holds an envelope labeled \"Returned\" and a second calendar icon showing a later day. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A sender holds a receipt marked sent; the letter travels to a house and comes back to the sender's mailbox days later.",
  "caption": "A receipt for posting proves the letter was sent; whether it was delivered is known only if it comes back, days later, as a new item in the sender's own mailbox."
}
-->

## The Rails a Payout Travels On

Rails differ in whether they process in batches or one transfer at a time, when they operate, and whether the sender learns the outcome. The behavior column below is industry practice in general terms. The bank rails are named as in Stripe's Global Payouts price list and network options (n.d., accessed November 2026); its overview page adds payouts "to debit cards".

| Rail | Where | How it commonly behaves |
| --- | --- | --- |
| SEPA Credit Transfer | Euro transfers in the Single Euro Payments Area | Batches on business days; a failure comes back as a return |
| SEPA Instant Credit Transfer | Same area | One transfer at a time, around the clock, with an immediate answer |
| ACH (Automated Clearing House) | United States | Batches, next day or same day; returns arrive on later days |
| Faster Payments | United Kingdom | One transfer at a time, around the clock, usually within seconds or minutes |
| Wires: Fedwire, SWIFT | US high-value; international | One at a time in operating hours; across borders through intermediary banks |
| Push to card | Debit cards on the card networks | The card network delivers to the card's account, typically in minutes |

Cut-off times turn the time of day into a processing date. Adyen's published examples list, as of November 2026, a `regular` transfer cut-off of 15:45 CET in the euro area with same-day settlement; transfers "initiated after the cut-off time will be processed the next day". At Stripe, a manual payout in euros can arrive the same day if initiated "before 4 pm Europe/Copenhagen". These settings will change; read the current page before you design around one.

Weekends, holidays and the receiving bank add to that. Stripe's API reference (n.d., accessed November 2026) describes a payout's `arrival_date` as the "Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays". Adyen's Getting paid page (n.d., accessed November 2026) says it "cannot process payouts on bank holidays" and that after initiation "your bank may need up to three more business days to post the funds". The value date is the receiving bank's, and no provider promises it.

An instant rail replaces the schedule with a synchronous answer. Regulation (EU) 2024/886 of 13 March 2024 defines an instant credit transfer as one "executed immediately, 24 hours a day and on any calendar day", with the money available to the payee "within 10 seconds"; euro-area payment service providers had to offer sending them by 9 October 2025. The price is a ceiling and gaps in reach: as of November 2026 Adyen caps an `instant` euro transfer at 100,000.00 EUR, and notes that "while most banks can process **regular** transfers, some do not support **instant** transfers". One payout API has to cover both contracts.

| Requirement | Batch rail | Instant rail |
| --- | --- | --- |
| How fast | Same day to several business days | Seconds |
| How definite the answer | "Sent"; arrival is inferred | Credited or failed |
| When it operates | Business days, before the cut-off | Around the clock |
| What failure looks like | A return, days later, as a new credit | An immediate failure; retry or fall back |

A payout that crosses a border adds intermediary banks and a currency conversion (foreign exchange, FX). Adyen says of its `crossBorder` priority that "payout delays and additional fees may occur due to intermediary banks. As a result, the beneficiary may receive a lower amount than the instructed value." Stripe's price list, as of November 2026, charges 20.00 EUR for a payout over SWIFT and an FX fee of 0.50% on 20 listed currencies and 1.00% on all others, applying the higher of the two currencies' rates.

## How a Payout Leaves, and How It Comes Back, at Each Provider

### Schedules and batches

A standard payout is a scheduled batch that sweeps up many payments, minus refunds and fees. (Both providers' documentation quoted in this section is undated and was read in November 2026.) At Stripe the merchant picks a schedule (manual, daily, weekly, monthly), and "Choosing a payout schedule doesn’t change how long it takes for your pending balance to become available. It only controls when payouts are sent." At Adyen the unit is the payable batch, which under its sales-day payout model holds one sales day's payments paid out together: "After the payable batch closes, it can take one to two business days for the payout to be initiated." On Adyen's platform product a managed payout schedule (n.d., accessed November 2026) is Standard, with funds arriving "two business days after capture", or Accelerated, one. Per-seller schedules belong to [[splits-balances-and-platform-payouts]].

### Stripe: two objects, two vocabularies

Stripe's Payout object (API reference, n.d., accessed November 2026) has a status: "A payout is `pending` until it’s submitted to the bank, when it becomes `in_transit`. The status changes to `paid` if the transaction succeeds, or to `failed` or `canceled` (within 5 business days). Some payouts that fail might initially show as `paid`, then change to `failed`." The state that looks final is documented as reversible.

Stripe's second payout product has its own object. Global Payouts sends money to third parties who are not merchants on Stripe; each payout is an OutboundPayment (created directly or, in the API version in preview in November 2026, through a PayoutIntent) with the statuses `processing`, `failed`, `canceled`, `posted` and `returned`. Here `posted` plays the part of `paid`: "The payout posts and funds leave the financial account" (the stored balance the sender pays from). Stripe may review a payout first: "Creating an OutboundPayment doesn’t mean that Stripe has sent the funds."

### Adyen: accounting events, then tracking events

Adyen splits the lifecycle in two. Accounting events end at `booked`, the debit. Tracking events follow and differ by route: instant bank transfers "receive a **credited** `status` when the funds arrive, or **failed**"; payouts to cards receive `accepted`; non-instant bank transfers receive only the estimate. Booked is not departure either: "After a payout reaches the **booked** `status`, but before the funds leave Adyen, the payout is automatically analyzed", and one that fails manual review is frozen. Adyen's payout webhooks page for platforms (n.d., accessed November 2026) says of `booked`: "This status is not final."

Three vocabularies describe one lifecycle, and an integrator needs four states. The empty cells are the point: on a batch rail neither provider has a status that means arrived.

| State you need | Stripe Payout | Stripe Global Payouts | Adyen transfer |
| --- | --- | --- | --- |
| Instructed | `pending` | `processing` | `received`, `authorised` |
| Sent | `in_transit`, then `paid` | `posted` | `booked`, then an estimated arrival time |
| Arrived | No status | No status | `credited`, instant bank transfers only |
| Returned | `failed` after `paid` | `returned` | `returned` |

### The return is a new movement

Both providers document a failed delivery as a new movement that credits the balance. Stripe: "It can take up to 5 additional business days for your bank to return the payout and inform us that it failed", and the Payout then carries a `failure_balance_transaction`, "the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance". For Global Payouts: "Stripe returns the funds to you in a separate transaction", typically "within 2–3 business days, but might take longer depending on the recipient country". Adyen: "Payouts that do not have an **instant** `priority` cannot fail, but they can be returned by the counterparty's bank", and "A new transaction is created for the return". For an Adyen merchant's ordinary payout the return shows in a report, under the journal type `BankInstructionReturned`. In every case the original debit stands and a second entry answers it.

Who sends the money again differs by product. For a merchant's own scheduled payout Stripe does, once the bank details are corrected: "Stripe then reattempts the payout at the next scheduled payout interval." For Global Payouts, "Stripe doesn’t retry or reroute payouts automatically." Adyen lets the sender list several priorities and tries the next "If that route is unavailable", but that happens before sending. After a return the resend is the sender's: Adyen's webhook documentation (n.d., accessed November 2026) gives each return a reason code with advice to retry or not, and says "Adyen blocks subsequent transfer attempts when a reason code indicates a permanent issue" until the bank details are updated.

That is where the public record stops. Stripe's payouts page names no rail for a standard payout. Adyen's press release of 9 April 2026 says its banking licenses enable "direct connections to payment rails" and does not list them. Neither publishes which bank or rail carries a merchant payout in each country, or how often payouts are returned.

> **INFERENCE, NOT DOCUMENTED:** A provider that pays very many merchants each business day most plausibly submits standard payouts in bulk on each country's domestic batch rail, directly where it is a participant and through partner banks elsewhere, and matches the banks' return files back to payouts. That would explain the cut-offs and five-business-day windows both document.

One failure never comes back. A transfer to a valid account that belongs to someone else is, to every bank involved, a success. Stripe: "If you provide incorrect information, such as a mistyped account number or an incorrect routing number, Stripe might send payouts to the wrong bank account and might not be able to recover the funds. Any fees or losses that you incur because of incorrect information fall under your responsibility." There is no general undo: Stripe lists Global Payouts reversals as possible for US domestic payouts "within 24 hours", not for UK Faster Payments or cross-border payouts, and "can’t guarantee a reversal".

## Checking the Payee Before the Money Leaves

A misdirected payout succeeds because bank transfers are routed by account identifier, such as the IBAN (international bank account number), and not by name. EU law says as much: Regulation 2024/886 speaks of "the execution of a credit transfer to an unintended payee on the basis of an incorrect unique identifier". A number that is valid and belongs to someone else is not an error any system on the rail can see.

The EU's answer is **verification of payee**. Article 5c, which the same regulation inserts into the SEPA Regulation (EU) No 260/2012, requires that "A payer’s PSP shall offer the payer a service ensuring verification of the payee", performed "before the payer is offered the possibility of authorising that credit transfer". A PSP is a payment service provider, here the sender's bank or payment company; it asks the payee's provider whether name and account match, and on an almost-match shows the payer the name on the account. The service is free, has applied in the euro area since 9 October 2025, and may not block the payer from going ahead. Business users who submit payment orders "as a package" may opt out, which matters for bulk payouts.

The United Kingdom has run the equivalent, **Confirmation of Payee**, for longer. Its operator Pay.UK says (n.d., accessed November 2026): "Since launching in 2020, over 300 organisations have already implemented CoP, with more than 2m checks being completed every day." It is "an API-based peer-to-peer service, with no central infrastructure in place, but with a directory identifying the organisations in the ecosystem".

Both providers pass the result to the sender. In Stripe's Global Payouts (documentation n.d., accessed November 2026), a payout in pounds between UK accounts requires a Confirmation of Payee check. In the Dashboard its outcomes are Match, "Partial Match or No Match", and Unavailable, and the last two offer "Continue without match"; through the API the result is returned in a `recipient_verification` field and anything but a match must be acknowledged before the payout is sent. For EU recipients, a Stripe support article (n.d., accessed November 2026) says: "When initiating a payout to an EU recipient in the Dashboard, Stripe will perform the VoP check", and on a mismatch or close match the sender is "prompted to acknowledge the difference and either edit the details or cancel the payout". Adyen offers `POST /verifyCounterpartyName` (n.d., accessed November 2026) for its enterprise payouts to domestic EU and UK accounts. It answers `nameMatch`, `partialNameMatch`, `noNameMatch` or `nameMatchNotSupported`, and returns the account's name only for a partial match, "To safeguard against name-guessing". I found nothing from either about such a check on a merchant's standard payout; there the account is verified at onboarding ([[platform-onboarding-and-verification]]).

What to do with the result is the sender's decision, and this is the rule I use. A no-match stops the payout until someone has spoken to the payee. A partial match goes to a person who sees the bank's name next to the name on file. Whoever continues is recorded. The strictness follows the loss. Stripe: "Only continue without a match if you’re confident the bank account belongs to the intended recipient. Funds sent to the wrong bank account might not be recoverable." Under Article 5c a provider that performed the check "shall not be held liable for the execution of a credit transfer to an unintended payee". After a warning, the misdirected payout is the sender's.

## Three Ways to Record a Payout, and What Speed Costs

The simplest record copies the provider's status into one field and treats "paid" as final. It is right for most payouts, and it is the record Larkfield had in June 2026. Its weakness is that it has nowhere to put the correction: a return arrives for a payout the system considers finished.

The second design keeps four states (instructed, sent, arrived, returned) and leaves a sent payout open for a **return window**; if the window passes with no return, the payout is marked arrived, by inference. The window's length is partly documented (all three pages n.d., accessed November 2026): Stripe's `paid` can become `failed` within 5 business days, Global Payouts returns "typically" take 2–3, and Adyen advises looking for a returned instruction five business days after the batch closed. No source gives an upper bound, so the window is a policy you choose, and a later return must still be handled.

<!-- illustration-placeholder
{
  "id": "14-payout-states",
  "status": "pending",
  "asset": "assets/images/14-payouts-and-money-movement/14-payout-states.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that describes the four-state design and its return window",
  "visual_goal": "Show the payout record as four states, with arrival confirmed or inferred and a return reopening the debt.",
  "prompt": "A state-machine diagram with four rounded boxes. Left to right: a blue box labeled \"Instructed\"; a teal box labeled \"Sent\" with an hourglass icon labeled \"Window\"; upper right, a green box labeled \"Arrived\"; lower right, an orange box labeled \"Returned\". Arrows: a blue arrow named \"debit\" from \"Instructed\" to \"Sent\"; a green arrow named \"confirmed\" and, below it, a dashed green arrow named \"window closed\", both from \"Sent\" to \"Arrived\"; an orange arrow named \"return\" from \"Sent\" to \"Returned\"; a thin dashed orange arrow named \"late return\" from \"Arrived\" down to \"Returned\"; a curved orange arrow from \"Returned\" to a ledger-page icon labeled \"Owed again\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "State machine with four payout states: instructed, sent, arrived and returned, with a late return possible after arrived.",
  "caption": "A payout record with four states: arrival is confirmed or inferred when the return window closes, and a return, even a late one, makes the amount owed again."
}
-->

The third design buys certainty from a rail that reports the credit, and both providers sell it with a fee and a ceiling. Stripe's Instant Payouts (n.d., accessed November 2026) "typically settle in the associated payout account within 30 minutes"; an account may make at most 10 a day, each up to 9,999 EUR in the euro area, and "Stripe assesses a fee on each Instant Payout". The pricing page for Connect, Stripe's platform product, as shown in euros in November 2026, lists 1% of payout volume; I did not check other countries. At Adyen instant is a transfer priority: "A payout with a higher priority incurs higher fees", no price list is public, and `credited` is the confirmation. At 1%, receiving Mila's €117.47 instantly would cost about €1.17 *(illustration)*.

The three designs trade cost against how soon and how surely you know the money arrived. For scheduled payouts to sellers I would build the second first and offer the third where a payee will pay for speed.

| Design | "Arrived" rests on | Cost | What it misses | When it is right |
| --- | --- | --- | --- | --- |
| Copy the provider's status | The provider's "paid" | None | Every return | One merchant paid to one long-standing account |
| Four states and a window | No return within the window | An open-items list with an owner | Late returns; misdirected payouts | Platforms; many payees on batch rails |
| Confirmed arrival | The rail's credited status | A fee; amount limits; not every bank | Misdirected payouts | Payees who need the money today |

Paying someone who is not a merchant on the provider uses a separate product at each company, and the same record applies. As of November 2026, Stripe's Global Payouts is open to senders located in the United Kingdom or the United States, with 22 more countries in private preview; it "requires Treasury", Stripe's stored-balance product, and is "best for businesses that already hold the licenses required to move money themselves" ([[licences-and-safeguarding]]). Such payouts "don’t flow through a Stripe balance belonging to the recipient", so tracking what each recipient is owed is the sender's job. Adyen's payouts service (n.d., accessed November 2026) pays third parties from a balance account through its Transfers API, funded by "funds acquired through payments with Adyen or externally transferred funds". Availability of both will change faster than this book.

## Stripe and Adyen: Where They Differ

The table sets this chapter's documented facts side by side; the last column is my reading and is inference. The Stripe and Adyen cells come from the documentation cited above, accessed in November 2026.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Status after sending | `paid`, which may change to `failed` "within 5 business days"; Global Payouts: `posted`, then possibly `returned` | `booked` ("This status is not final"), tracking events, then possibly `returned` | No material difference: both treat sent and arrived as separate facts |
| How the sender picks speed (third-party payouts) | Names networks in `preferred_networks`: `ach`, `fedwire`, `fps`, `sepa`, `swift`; otherwise "Stripe selects the most appropriate network" | Names a `priority`: regular, fast, instant, wire, cross-border; Adyen maps it to a transfer route | Stripe exposes the rail and Adyen abstracts it; an adapter should carry the intent |
| Confirmation of arrival | None; `posted` "doesn’t guarantee that your recipient has received money" | `credited` for instant bank transfers; an estimate otherwise | Only Adyen's instant route gives a machine-readable "arrived" |
| After a failed delivery | Standard payout reattempted "at the next scheduled payout interval"; Global Payouts "doesn’t retry or reroute payouts automatically" | A new transaction credits the balance account; the sender retries by reason code, and Adyen blocks transfers to an account with a permanent issue | Outside a merchant's own scheduled payout at Stripe, resending is the sender's job |
| Payee-name check | Confirmation of Payee on UK domestic Global Payouts in pounds, in the Dashboard and the API; an EU check in the Dashboard per a support article | `POST /verifyCounterpartyName` for enterprise payouts, EU and UK | Both hand the result to the sender, who decides what to do with it |
| Published prices | A per-rail fee table | "A payout with a higher priority incurs higher fees"; no price list found in documentation, pricing page or help center (November 2026) | A Stripe payout can be costed from the documentation; an Adyen one needs a quote |

Have your payout request carry an intent (amount, payee, latest acceptable arrival) and let each adapter translate it: into a network list at Stripe, a priority list at Adyen. On both, store the return as a record of its own, linked to the payout. On Adyen, use `credited` where you get it; on Stripe, plan for inference everywhere.

## In Practice at Larkfield: One Payout Record for Two Providers

Take the payout that carries Mila's €117.47. Studio Noord is on Adyen with the Standard schedule, so the pass captured on Tuesday 9 March 2027 is due in Ines Bakker's account two business days later, on Thursday 11 March. That is the best case: Adyen's Getting paid page allows up to five business days from the close of a batch until the bank posts the funds. On Thursday 11 March Adyen's transfer webhook reports `booked`, and Larkfield's payment record store moves the payout from instructed to **sent**. In this example the money does reach Ines's account that day, but the record does not move to arrived: Larkfield cannot see her bank account and the route is not instant, so it has no evidence of the credit. Under Keel, Larkfield's 2027 program to repair its payments, a sent payout stays open for 10 business days *(Larkfield's choice, an assumption for teaching)*. On Thursday 25 March, with no return, a job marks it **arrived**. The state `arrived` is a statement about Larkfield's record: it gives the day Larkfield stopped expecting a return, two weeks after the money landed, and is never shown to a studio as the date it was paid.

Keel decision K3 demands a ledger entry for every movement. The payout's entries pass through a clearing account, payouts in transit, for money that has left the provider and is not yet known to have landed. A clearing account must return to zero ([[payment-ledgers]]), so whatever stays in it beyond the window is the list of stranded payouts.

| Event | Debit | Credit | Effect |
| --- | --- | --- | --- |
| Sent | Payouts in transit | Funds at provider | The money is on the rail; the studio is still owed |
| Arrived (confirmed, or window closed) | Owed to studio | Payouts in transit | The debt is settled |
| Returned within the window | Funds at provider | Payouts in transit | The money is back; the debt was never closed |
| Returned after the window | Funds at provider | Owed to studio | A new entry reopens the debt |

Replay June 2026 against this record. Each of the 412 returns, about €937 on average, would have arrived carrying the provider's reference for a payout that was still open. The matching entry would have left the studio's debt visibly unpaid and the payout in a state a named team works through. The €386,000 would have been a queue on day one instead of a discovery over 19 days. The record would not have prevented the returns; a second Keel change does that: a change of bank details now triggers a check of the account holder's name and holds the studio's next payout until it passes or a person approves it.

For Ironworks Climbing, Ravi Shah's three locations in Manchester on Stripe Connect, the record is the same and the signals differ. The `payout.paid` event sets sent. A later `payout.failed` on the same payout sets returned, and the `failure_balance_transaction` is the entry to match. There is no arrived signal, so the window does all the work. Webhooks only move the record's state; the ledger entries are written from the provider's report lines, which is decision K2 ([[payment-webhooks-and-events]]).

## When It Goes Wrong

The first failure happens before any rail. Where Larkfield initiates a payout itself and the call times out, a retry with a fresh key can instruct the same payout twice. The defense is Keel decision K1: one writer, and an idempotency key derived from the payout's business identity (studio, currency, payout period), so the provider recognizes the retry ([[idempotency-and-retries]]).

Next, a payout can be debited and still not have left, because both providers document (n.d., accessed November 2026) a review of payouts after the accounting step. At Adyen a flagged payout goes to `pending` after `booked`; at Stripe a Global Payout held for review stays `processing` with the reason `under_review`, typically for up to 2 business days. A missed verification deadline also pauses payouts ([[payment-compliance-and-regulation]]).

Later, a return can arrive after the window closed and the payout was marked arrived; Stripe says returns "might take longer depending on the recipient country". The recovery is the last row of the table above: a new entry, linked to the original payout, that reopens the debt. Do not edit the closed payout.

Last comes the failure with no signal: the misdirected payout the receiving bank keeps. No webhook fires, so the detector is the payee's complaint. Stripe's Payout carries a `trace_id`, "A value that generates from the beneficiary’s bank that allows users to track payouts with their bank"; Adyen tells merchants to "download the bank instruction letter" and share it with their bank. Both help a bank find a transfer and neither brings it back.

## What to Take Away

**Established.**

- A payout status reports that the provider sent the money. As of November 2026, Stripe documents that `paid` may become `failed` within five business days; Adyen documents that `booked` "is not final".
- A failed delivery comes back as a new movement: both providers book the return as a separate transaction that credits the balance, days later.
- Transfers are executed on the account identifier. A payee-name check before authorization is required of euro-area providers since 9 October 2025 (Regulation (EU) 2024/886) and has existed in the UK since 2020.

**Depends on context.**

- The return window. Five business days covers what both providers document for domestic payouts; cross-border needs longer, and no source gives a maximum.
- Whether instant payout is worth its fee. It is where the payee values the day more than the fee; it does not replace the four-state record, because instant routes fail and fall back.
- How strictly to stop on a partial name match. A platform paying verified businesses can let a person approve it; one paying strangers should stop.

**The author's synthesis.**

- "Arrived" is a state you have to earn: buy it from an instant rail, infer it from a closed window, or hear it from the payee. The studio owner of the opening was told the truth by her dashboard; the return was already in her balance, in a record with no place to show it.
- Put the control where the money can still be stopped. After sending, the best record only shows a loss sooner; the payee check and a hold on changed bank details are the steps that prevent one.

## Questions to Ask

1. Which of our payout states is set by the provider's "paid", and what do we call a payout between that moment and the money landing?
2. How long does a sent payout stay open, who chose that number, and what happens to a return that arrives later?
3. When a return arrives, which field links it to the original payout, and which entry reopens what we owe the payee?
4. Which clearing account holds payouts in transit, and who looks at its balance by age?
5. On each provider and route, do we get a confirmation of arrival, an estimate, or nothing?
6. What runs when a payee changes bank details: a name check, a hold on the next payout, a person?
7. Who may continue past a partial match or a no-match, and where is that recorded?
8. If we pay people who are not merchants on our provider, whose license covers the money while we hold it?

A returned payout leaves two records of the same money that disagree: paid at the provider, nothing at the bank, and nothing in either record alone to say which is right. This chapter handled that one case by keeping the payout open. The general answer is to match every movement you expect against the other party's record of it, give whatever does not match an age and an owner, and use the reports providers publish for that purpose. That is the subject of [[payment-reconciliation-and-reporting]].

## Sources and Evidence

*Company, product and investor sources*

- [Receive payouts from Stripe](https://docs.stripe.com/payouts), Stripe, n.d., accessed 2026-11 — payout schedules, same-day manual payouts, payout failures ("might initially show as `paid`"), misdirected funds, reattempts, the `payout.paid` and `payout.failed` events.
- [The Payout object](https://docs.stripe.com/api/payouts/object), Stripe API reference, n.d., accessed 2026-11 — statuses, `arrival_date`, `failure_balance_transaction`, `trace_id`.
- [Global Payouts](https://docs.stripe.com/global-payouts), Stripe, n.d., accessed 2026-11 — sender availability (GB, US; 22 countries in private preview), the Treasury requirement, positioning (volatile).
- [Manage payouts](https://docs.stripe.com/global-payouts/manage-payouts), Stripe, n.d., accessed 2026-11 — OutboundPayment statuses, `posted` and `returned`, risk review, reversals, causes of returns.
- [Send payouts](https://docs.stripe.com/global-payouts/send-money), Stripe, n.d., accessed 2026-11 — `preferred_networks`, no automatic retry, Confirmation of Payee outcomes in the Dashboard and the API.
- [Supplemental pricing information](https://docs.stripe.com/global-payouts/supplemental-pricing-information), Stripe, n.d., accessed 2026-11 — per-rail and FX fees for Global Payouts (volatile).
- [Understand differences between Global Payouts and Connect cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts-to-recipients/compare-global-payouts), Stripe, n.d., accessed 2026-11 — ledgering responsibility for recipient funds.
- [Instant Payouts for Stripe Dashboard users](https://docs.stripe.com/payouts/instant-payouts), Stripe, n.d., accessed 2026-11 — timing, daily and per-payout limits, fee (volatile).
- [Connect pricing](https://stripe.com/connect/pricing), Stripe, n.d., accessed 2026-11 — Instant Payouts at 1% of payout volume as shown in euros; other countries not checked (volatile).
- [Verification of Payee support for Treasury](https://support.stripe.com/questions/verification-of-payee-support-for-treasury), Stripe Support, n.d., accessed 2026-11 — the EU check on Dashboard payouts and what the sender is asked to do on a mismatch.
- [Payout lifecycle](https://docs.adyen.com/payouts/payout-service/payout-lifecycle), Adyen, n.d., accessed 2026-11 — accounting and tracking events, review after booking, returns as new transactions.
- [Pay out to bank accounts](https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts), Adyen, n.d., accessed 2026-11 — priorities, transfer routes, cut-off times and maximum amounts, cross-border caveat (volatile).
- [Verify counterparty name](https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/verify-counterparty), Adyen, n.d., accessed 2026-11 — the name-check endpoint and its responses.
- [Getting paid](https://docs.adyen.com/account/getting-paid), Adyen, n.d., accessed 2026-11 — payout initiation timing, bank holidays, `BankInstructionReturned`, the bank instruction letter.
- [Payouts and Payments](https://docs.adyen.com/payouts/payout-service), Adyen, n.d., accessed 2026-11 — third-party payouts and their funding.
- [Managed payouts](https://docs.adyen.com/platforms/managed-payouts), Adyen, n.d., accessed 2026-11 — Standard and Accelerated payout schedules.
- [Initiate on-demand payouts](https://docs.adyen.com/platforms/custom-payouts/on-demand-payouts), Adyen, n.d., accessed 2026-11 — the priority list and bank reach.
- [Payout transfer webhooks](https://docs.adyen.com/platforms/payout-webhooks), Adyen, n.d., accessed 2026-11 — "This status is not final"; return reason codes, which to retry, and the block on transfers after a permanent reason.
- [Adyen launches Intelligent Money Movement](https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement), Adyen, 2026-04-09 — the packaging of payouts with liquidity management; "direct connections to payment rails".

*Standards, regulation and official documentation*

- [Regulation (EU) 2024/886 (instant payments)](http://publications.europa.eu/resource/celex/32024R0886), Official Journal, 2024-03-19 — the definition of an instant credit transfer, the 10 seconds, sending and receiving deadlines, charges, and verification of the payee (Article 5c) with its dates and liability rule; the Publications Office link serves the English text to a browser (a client that sends no language header gets an error).
- [Confirmation of Payee](https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/), Pay.UK, n.d., accessed 2026-11 — launch year, adoption, peer-to-peer design.

*Research and practitioner sources*

- None. The European Payments Council's page on its Verification Of Payee scheme returned HTTP 403 and is not used; the rule is cited from the regulation.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
