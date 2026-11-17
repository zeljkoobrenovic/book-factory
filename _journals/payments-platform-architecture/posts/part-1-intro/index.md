---
title: "Part I — MONEY: How a Payment Actually Moves"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What happens between the moment an app says “Payment successful” and the moment the merchant has money it can keep? A chain of separate promises by different parties on different clocks, none of which makes the payment final, and a fee divided among the same parties."
permalink: part-1
timetoread: 5 min read
---

> **KEY POINTS:**
>
> * **“Payment successful” is one bank's promise, not money.** The cardholder's bank reserves the amount in seconds; money moves a day or more later, as net amounts between banks.
> * **No step makes a payment final.** The cardholder can dispute it for about 120 days, which outlasts the approval, the settlement and the payout.
> * **Every promise has an owner, a clock and a price.** Store which promise you hold, from whom and until when, and read a card fee as three payments.

<br>
On 2 February 2027 a ten-class pass for €120.00 is bought with Bram de Wit's card at Studio Noord, a yoga studio that sells through **Larkfield, the fictional studio-software platform this book follows**. The payment is approved, and within days the studio has its money. On 24 February a **chargeback** arrives: Bram has told his bank he does not recognize the charge, the bank takes the €120 back, and a €15.00 dispute fee *(illustrative)* comes with it. No step of the payment had failed.

Nothing had failed, yet the money came back. To an engineer, a payment is a request that returned success. Behind the API, that success was one bank's promise: **a card payment is a chain of separate promises made by different parties on different clocks**. The cardholder's bank, called the **issuer**, approves in seconds and moves no money. The merchant claims the amount, the banks settle through the card network a day or more later, and the provider pays the merchant on its own schedule. None of these makes the payment final: Visa's public rules (edition of 24 October 2026) give the issuer 120 calendar days for most kinds of dispute ([[journey-of-a-payment]]), and that right outlasts all four.

<!-- illustration-placeholder
{
  "id": "part-1-chain-of-promises",
  "status": "pending",
  "asset": "assets/images/part-1-intro/part-1-chain-of-promises.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the lead paragraph that states the part's claim, a card payment is a chain of separate promises",
  "visual_goal": "Show one payment as a chain of four links, each held by a different party with its own clock, followed by a long open stretch from which the payment can still be pulled back.",
  "prompt": "Create a conceptual explainer illustration of a chain drawn left to right across the middle of the image. The chain has four large links, each a different color and each held up by a different generic figure standing behind it. The first link is labeled \"Approved\" and is held by a bank building; the second is labeled \"Claimed\" and is held by a small yoga studio shopfront; the third is labeled \"Settled\" and is held by a hub of connected nodes between two small bank buildings; the fourth is labeled \"Paid out\" and is held by an office block with a payout chute. A small clock sits above each link, and the four clocks show visibly different times. To the left of the first link, a smartphone shows one green check mark. To the right of the fourth link the chain does not close: a long dotted line runs on to a calendar page labeled \"120 days\". From the calendar page a curved orange arrow labeled \"Dispute\" runs back over the top of the chain to the first link, carrying a euro coin labeled \"€120\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A chain of four links labeled Approved, Claimed, Settled and Paid out, each held by a different party with its own clock, and a dispute arrow running back from a calendar page labeled 120 days.",
  "caption": "One payment is four promises held by four parties on four clocks, and for about 120 days a dispute can still pull the €120 back."
}
-->

The promises cannot be folded into one status, because none of them is the provider's own. Each belongs to another party, which keeps its own record on its own clock, and the provider that answers your API call can only report them as they arrive. So “approved”, “captured”, “settled” and “paid out” are four facts held by four parties, and **a system that stores one status word for them is wrong for days at a time**.

Part I follows the payment in the order it happens. The first chapter lays out the whole journey. The next three take its stretches in turn: the authorization, which is the first promise; capture, clearing and settlement, where money actually moves; and refunds, reversals and disputes, where it moves back. The last says who earns what at each step. On the way, three beliefs an integrator arrives with are overturned: that approved means paid, that paid out means final, and that the fee is one charge.

<!-- illustration-placeholder
{
  "id": "part-1-five-chapters-on-the-timeline",
  "status": "pending",
  "asset": "assets/images/part-1-intro/part-1-five-chapters-on-the-timeline.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the roadmap paragraph that names the five chapters in the order a payment happens",
  "visual_goal": "Show the shape of Part I: five chapters laid along one payment's timeline, the first spanning the whole line, three covering its stretches in order, and the fifth running underneath as the fee paid at each step.",
  "prompt": "Create a structural timeline diagram. One horizontal line runs left to right across the middle with four round stations labeled \"Approval\", \"Settlement\", \"Payout\" and, after a long dotted stretch, \"Dispute window\". Above the line, a wide blue bracket spans the whole line from the first station to the last and carries a round badge labeled \"1\" and the label \"Journey\". Directly on the line, three shorter colored bands mark its stretches: a teal band around the first station with a badge labeled \"2\" and the label \"Promise\"; a green band from just after the first station to the third station with a badge labeled \"3\" and the label \"Money moves\"; and an orange band over the dotted stretch and the last station with a badge labeled \"4\" and the label \"Money back\", with a curved orange arrow pointing from right to left above it. Below the line, a thin grey strip runs under the first three stations with a small euro coin under each station, a badge labeled \"5\" and the label \"Who earns\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A payment timeline from approval to the dispute window with five numbered chapter markers: one spanning the whole line, three covering its stretches in order, and one underneath showing a fee at each step.",
  "caption": "The five chapters of Part I on one payment's timeline: the whole journey, the first promise, the money moving forward, the money moving back, and who earns what at each step."
}
-->

## Chapters in this part

[[journey-of-a-payment]] asks **what has to happen, between which parties, for one card payment to be approved, collected, moved, paid out and possibly taken back**. Its answer is six steps spread over days and carried out by at least five parties, in which a message moves first, then a record, then money. It names the parties, among them the **acquirer**, the institution that accepts card payments on the merchant's behalf, and shows that the provider answering the API call controls none of the three steps that decide the outcome. The case is Mila Janssen's €120.00 class pass, bought at 19:42 on Tuesday 9 March 2027 and paid out to Studio Noord on Thursday 11 March, with the studio owner's question in between: “It says paid. Paid to whom?” The first question for any provider follows: which legal entity is the acquirer in this country?

[[payment-authorization]] opens the first step and asks **what exactly an authorization promises, who decides, and what can change before the money moves**. The promise is the issuer's: to honor a claim for up to an approved amount inside a window that Visa's general table sets at 5 to 30 days. It moves no money and can lapse, and a request that gets no answer has an unknown outcome, not a failed one. The case is the Double Charge of 1 November 2026, when Larkfield's renewal job read a timeout as a refusal and sent each charge again: 1,840 members paid twice, and €71,300 had to be refunded.

[[clearing-and-settlement]] turns to the steps that do move money, and asks **how an approved payment becomes money in the acquirer's account, and why it takes days**. The merchant's capture is a claim, the acquirer presents a clearing record through the network, the network moves one net amount per member bank per day, and the provider pays the merchant on its own schedule. So “settled” names a different event at the network, at the provider and at the merchant's bank. Stripe counts its settlement timing from the capture; Adyen pays a whole sales day on a fixed delay, whether or not it has received the funds (its terms of 17 June 2024). The case is Wednesday 10 March 2027: Larkfield's record shows Mila's €120 as paid, the provider's balance shows it as not yet paid out, and the studio's bank shows nothing. All three are right; €117.47 arrives on Thursday.

[[refunds-reversals-and-disputes]] begins after the payout and asks **how money goes back, who decides, and why a payment can be undone months later**. There are three routes with three owners: a cancel or reversal withdraws the issuer's promise before any money has moved; a refund is a new transaction that the merchant starts and that can fail; a dispute is the issuer taking the money back under the network's rules, with the merchant allowed one answer. Visa's rules give the issuer 120 days for most disputes and up to 540 where a service is delivered later. The case is Bram's €120, whose financial effect stays open until at least 2 June 2027, 120 days after the sale.

[[payment-economics]] comes last, because a fee can be assigned to a party and a step only once you know both. It asks **where the fee on a payment goes, and how the way a provider earns its share shapes what it builds**. The fee is three payments: **interchange** to the issuer, **scheme fees** to the card network and a markup to the provider. EU law caps only the first, at 0.2% for consumer debit cards and 0.3% for consumer credit cards. As of November 2026 Stripe's published standard price blends the three into one rate, and Adyen's passes interchange and scheme fees through at cost; that choice decides which costs you can see. The case is the fee on Mila's €120, with illustrative figures: of Larkfield's €2.53 fee, €0.24 goes to her bank, €0.06 to the network and €0.31 to the provider.

## Where to Begin

Read in that order, the five chapters turn Bram's €120 from a surprise into a sequence. By the end you can name each party that said yes on 2 February, what each was paid for saying it, and why none of those yeses stopped the chargeback of 24 February. With one question in hand, about a status, a delay, a reversal or a fee, open the chapter that answers it. Otherwise follow Mila's class pass from end to end. Begin with [[journey-of-a-payment]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
