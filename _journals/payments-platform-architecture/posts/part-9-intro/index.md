---
title: "Part IX — JOURNEYS: One Payment, End to End"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What do four payments followed from start to finish show that the chapters on single mechanisms could not? Part IX argues that every mechanism can work and the payment can still go wrong, because the failures sit at the hand-offs, where one step's promise is taken by the next as a finished fact."
permalink: part-9
timetoread: 5 min read
---

> **KEY POINTS:**
>
> * **Payments go wrong at hand-offs.** In four payments followed end to end, every failure appears where one step's answer is taken by the next system as final.
> * **A success message reports a promise.** Whether it was kept is reported later, in another record, so a payment's record stays open until the dispute window closes, not the payout.
> * **Each provider puts the later record somewhere else.** Stripe gives objects whose status can be read again; Adyen gives events and report lines keyed by a reference.

<br>
At the end of 2025, every payment in the records of **Larkfield, the fictional studio-software platform this book follows**, had the right status. Yet its books said it owed its studios €412,000 more than the balances at its two providers, Stripe and Adyen, showed. The difference was found in January 2026 and took three weeks to trace: to refunds made after a studio had been paid, fees on chargebacks (card payments taken back by the customer's bank) and a rounding rule for currency conversion ([[payment-ledgers]] gives the amounts). **None of the three was a payment that had failed.**

<!-- illustration-placeholder
{
  "id": "part-9-all-paid-books-apart",
  "status": "pending",
  "asset": "assets/images/part-9-intro/part-9-all-paid-books-apart.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the opening paragraph",
  "visual_goal": "Show that every payment record is correct while the platform's books and the providers' balances stand apart, with three later movements in the gap.",
  "prompt": "Create a wide explainer illustration. On the left, a neat grid of small payment record cards, every one carrying a green check mark, under a small tag labeled \"All paid\". On the right, two tall stacks of euro coins standing side by side on a table: the left stack, beside an open ledger book, is labeled \"Books\"; the right stack, beside a generic office building, is labeled \"Providers\" and is visibly shorter. A horizontal bracket marks the difference in height between the two stacks, with an orange tag labeled \"€412,000\". Inside the gap above the shorter stack float three small items with no text: a receipt slip with a backward arrow, a price tag with a euro sign, and a small coin cut by a rounding symbol. A generic finance professional stands between the grid and the stacks, looking from one to the other. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A grid of payment records all marked with a check, beside two coin stacks labeled Books and Providers whose heights differ by a gap tagged €412,000, with a refund slip, a fee tag and a rounded coin in the gap.",
  "caption": "At year-end 2025 every payment at Larkfield had the right status, and its books and its providers' balances were €412,000 apart."
}
-->

The chapters so far could not have shown that difference. Parts I to VIII explained one mechanism per chapter, ending in [[part-8]] with the rule that a money path must be correct before it is available. Part IX teaches no new mechanism. It takes **four payments at Larkfield and follows each through every party and system, in the order the payment meets them** to show what passes from each step to the next.

The four make one claim: **every failure they show appears at a hand-off**, the point where one mechanism's answer (an approval, a decline, a payout, a payment marked complete) is taken by the next system as final. The mechanisms belong to different parties and run on different clocks, from seconds for an approval to about four months for a chargeback. So each step can tell the next only what it knows when it finishes, which is a promise. Whether the promise was kept is reported later, by another record, usually on another channel.

<!-- illustration-placeholder
{
  "id": "part-9-four-chains-marked-joints",
  "status": "pending",
  "asset": "assets/images/part-9-intro/part-9-four-chains-marked-joints.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that states the part's claim",
  "visual_goal": "Show the part's shape: four payments, each a chain of working mechanisms, with attention on the joints between them and not on the links.",
  "prompt": "Create a wide conceptual diagram. Four horizontal chains run from left to right, stacked one above the other with even spacing. Each chain is made of five solid rounded links drawn in blue or teal, and every link carries a small green check mark. Between each pair of neighboring links, the joint is drawn as a small orange ring, clearly brighter than the links. At the left end of each chain sits one small icon and a short label: a phone with a check mark labeled \"Pass\"; a calendar page with a circular arrow labeled \"Renewal\"; a euro coin split in three with a backward arrow labeled \"Refund\"; a bank building with a backward arrow labeled \"Dispute\". A generic engineer stands at the right holding a magnifying glass over one orange joint of the first chain, and a single callout from that joint is labeled \"Hand-off\". The fourth chain is visibly the longest and the first the shortest. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Four chains labeled Pass, Renewal, Refund and Dispute, each made of links with check marks, with the joints between links marked in orange and one joint under a magnifying glass labeled Hand-off.",
  "caption": "The shape of Part IX: four payments, each a chain of mechanisms that work, read at the joints where one hands to the next."
}
-->

Every journey has the same form: a narrative, one sequence figure and a **step table**, which the first journey sets up. Each row names the party or system that acts, the record it leaves, the promise that record makes and what can fail there, with the chapter that owns the mechanism. Read a row by asking **which later record confirms or corrects it**. The failures to look for are between rows, not inside one. Each journey is told on Adyen, the provider of Studio Noord, the yoga studio where all four payments are made, with the Stripe record beside it. The two report the same step through different records at different moments: Stripe as objects whose status can be read again, Adyen as events and report lines keyed by a reference. An integration that waits for the right record on one waits for the wrong one on the other.

Those records are from the two providers' documentation as read in November 2026, and the journeys say where it stops. The pairing of the two vocabularies is this book's own, since neither company publishes one. The timing of clearing and settlement between banks is industry practice, not a cited rule. Mastercard's rule documents could not be read, and Adyen's chargeback fee is set by contract, so the last journey's €15 fee is an illustration.

The four journeys are read in the order of what each adds, not the calendar's. The disputed payment was made first, on 2 February 2027, five weeks before the first journey's payment. It comes last because a chargeback debits a balance, and you should first see that balance filled, paid out and refunded.

## Chapters in this part

[[journey-card-payment]] asks **what happens to one €120 card payment between the tap and the studio's reconciled payout, and what each step promises**. Mila Janssen buys a ten-class pass at 19:42 on Tuesday 9 March 2027, and Studio Noord is paid on Thursday 11 March. In between are twelve steps. Eleven end in a promise, the “Payment successful” on her screen reports the fifth, and only the twelfth, matching the payout to the provider's settlement record, establishes that the studio's €117.47 arrived. On Stripe the payment is an object that can be read again; Adyen's Checkout API has no call that returns a payment, and a capture it reported as successful can fail days later.

[[journey-failed-renewal]] keeps the member and her stored card, removes her presence and the approval, and asks **who decides whether and when to try again, and which system holds the membership until the money arrives**. Mila's €49 renewal is declined on 1 April 2027 and collected on 4 April; a second branch is never collected. A declined renewal is an open debt with a clock: the decline code decides whether a retry is allowed, Visa's rules of 24 October 2026 cap the number, and no payment record says what Mila is in between. Stripe Billing retries an invoice it holds. On Adyen the provider can retry a payment, and the schedule, the membership state and the notice are Larkfield's.

[[journey-platform-payment]] returns to the pass and opens two rows the first journey only named, the split and the payout, to ask **how the €120 is divided, and whose money pays a refund after the studio has been paid**. An instruction attached to the payment divides it into €117.47 for the studio and €2.53 for Larkfield, and the provider's cost, an illustrative €0.61, comes out of Larkfield's share. On 18 March, a week after the payout, Mila gets €84 back, debited from a balance the payout had emptied and so paid from other members' later payments. The account model chosen at integration decides who goes short: on Adyen the platform's own balance account stands behind the studio's, and on Stripe the charge type decides whose balance is debited first.

[[journey-dispute]] turns from money that goes back by agreement to money a bank takes back, and asks **what a chargeback costs in money, deadlines and records, and who carries the loss**. Bram de Wit, another member, paid €120 on 2 February 2027, and his bank charged it back on 24 February. The €120 and an illustrative €15 fee left the studio's balance before anyone had read any evidence. Larkfield could answer once, within the 40 days Adyen gives for a Mastercard. The money came back provisionally on 5 March, the dispute was won on 12 May, and the card network counted it either way. Who paid had been decided at the sale. The journey ends in Larkfield's ledger and closes the part by setting all four against the €412,000.

## Where to Begin

The four can be read as a set or one at a time: if you are tracing a payment, a renewal, a refund or a dispute of your own, start at the matching journey and fill in the same table. Read through, they turn the €412,000 into three kinds of later record that reached a provider's balance and never Larkfield's books; the third and fourth journeys write two of them as ledger entries. Begin with [[journey-card-payment]].

## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Larkfield is fictional, and its figures are the same in every chapter.
