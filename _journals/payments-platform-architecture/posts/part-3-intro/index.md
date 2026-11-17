---
title: "Part III — LEDGER: Recording and Moving Money"
date: 2026-11-17
author: Željko Obrenović
excerpt: "Between the customer paying and the merchant being paid, how does a payment provider know where the money is and whose it is? Part III argues that it knows only from a double-entry ledger it keeps itself and keeps proving against the networks' and banks' records, and that a balance, a payout, a report and a license are each that ledger seen from one side."
permalink: part-3
timetoread: 5 min read
---

> **KEY POINTS:**
>
> * **A balance is a record of a debt, not a count of cash.** The cash is in transit or pooled at banks; what a provider holds is a double-entry ledger of who owes whom.
> * **The record is knowledge only while someone else's record agrees.** Network files and bank statements prove the provider's entries; the provider's reports prove yours.
> * **“Available”, “paid” and “settled” are one party's statement at one moment.** A later entry can reverse each, so keep an entry of your own for every movement.

<br>
At the end of 2025, every payment at **Larkfield, the fictional studio-software platform this book follows**, had the right status. Yet Larkfield's books said it owed its studios **€412,000 more** than the balances at its two providers, Stripe and Adyen, showed. It took three weeks to trace the difference to three things: refunds made after the payout (the provider's transfer of a studio's money to its bank account), fees on chargebacks (card payments reversed by the cardholder's bank after a dispute) and a currency-conversion rounding rule.

The record that [[part-2]] ended with could not have contained that difference. Part II left an approved payment in a state machine that says what happened to it: authorized, captured, refunded. But every approval also creates debts. The card network owes the provider, the provider owes the merchant, and both are paid over days. **A payment's state does not say who owes whom.** That takes a second record, and a way to prove it.

Part III argues that a provider knows where money is, and whose it is, only from a **double-entry ledger** it keeps itself: an append-only record in which every movement is written as lines that balance, so that a missing movement shows up as an account that does not empty. And that record counts as knowledge only while it is **matched against records the provider did not write**, the networks' files and the banks' statements. The rest of the part is that ledger seen from one side at a time. A balance and a report are the ledger read at a given moment, a payout is one of its entries becoming a bank transfer, and the provider's license decides which accounts it must contain. The view to give up is that the money is simply “at the provider” and that a dashboard balance counts cash the way a bank balance does.

<!-- illustration-placeholder
{
  "id": "part-3-one-ledger-seen-from-four-sides",
  "status": "pending",
  "asset": "assets/images/part-3-intro/part-3-one-ledger-seen-from-four-sides.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that states the part's claim",
  "visual_goal": "Show the ledger at the center, with the balance, the payout and the report read from it, outside records proving it, and the license as the frame around it.",
  "prompt": "Create a wide structural explainer diagram. At the center, a large open ledger book labeled \"Ledger\", its pages showing pairs of plus and minus lines of equal length. To the right of the book, three items stacked vertically, each joined to the book by a thin blue arrow labeled once as \"read from\": a small gauge labeled \"Balance\", an envelope with a euro coin labeled \"Payout\", and an itemized sheet labeled \"Report\". From the envelope a teal arrow labeled \"transfer\" continues right to a small generic bank building. To the left of the book, two documents, a file labeled \"Network file\" and a sheet labeled \"Bank statement\", each joined to the book by a green double-headed arrow labeled once as \"matched\". Around the ledger book only, a dashed orange frame with a small shield on its top edge, labeled \"License\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A ledger book at the center; a balance, a payout and a report are read from it on the right; a network file and a bank statement are matched against it on the left; a dashed frame labeled license surrounds the ledger.",
  "caption": "The shape of Part III: the balance, the payout and the report are read from one ledger, records written by others prove it, and the license decides what it must contain."
}
-->

Five chapters take five questions, and each needs the one before. They ask how a provider builds the ledger that records every movement twice; what a merchant's balance says and does not say; how money leaves the provider, and what happens when it does not arrive; how the provider proves its books against networks and banks, and what it gives customers to prove theirs; and who is legally allowed to hold the money. **The ledger comes first because balances, payouts and reports are all read from it.** Licenses come last because safeguarding, the legal duty to keep customers' money apart from the firm's own, is by then one more comparison between a ledger and a bank account, this time required by law.

<!-- illustration-placeholder
{
  "id": "part-3-five-questions-in-order",
  "status": "pending",
  "asset": "assets/images/part-3-intro/part-3-five-questions-in-order.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that gives the five questions and the reason for their order",
  "visual_goal": "Show the reading order as five steps that each stand on the one before, starting with the ledger.",
  "prompt": "Create a wide explainer illustration of a staircase of five broad steps rising from left to right, each step resting on the one before it. On each step stands one icon with one label beneath it. Step one: an open ledger book, labeled \"Ledger\". Step two: a gauge with a euro sign, labeled \"Balance\". Step three: an envelope with a euro coin flying toward a small bank building, labeled \"Payout\". Step four: two documents joined by a green check mark, labeled \"Proof\". Step five: a shield with a small keyhole, labeled \"License\". A single blue arrow labeled \"read in order\" runs along the foot of the staircase from the first step to the last. The first step is drawn slightly wider and in a stronger blue than the others to show that the rest stand on it. No people. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A staircase of five steps labeled Ledger, Balance, Payout, Proof and License, with an arrow along its foot showing the reading order.",
  "caption": "Five chapters in the order each needs the one before: the ledger, the balance read from it, the payout that leaves it, the proof against outside records, and the license."
}
-->

## Chapters in this part

[[payment-ledgers]] answers **how a payment company knows whose money it holds and where it is**: from balanced entries that are never edited, and from clearing accounts, which hold an amount in flight and must return to zero. Two published designs enforce the rule at different points. Adyen's 2021 engineering post describes refusing an unbalanced entry at the write; Stripe's 2024 post describes many systems writing into a log that is checked afterwards, with 99.99% of dollar volume verified within four days. The chapter replays Larkfield's €412,000 through six accounts and one posting function.

[[balances-and-funds-flows]] then narrows to one merchant and asks **where the money is, and whose, between the customer paying and the merchant being paid**. A balance is the merchant's claim on the provider, and “pending”, “available” and “reserved” are the provider's decisions about when and how much of that debt it will pay. Adyen documents that it pays whether or not the card network has paid it, and takes back what has not settled within 30 days; Stripe publishes a schedule and, for standard payouts, does not say, beyond terms that let a payout wait when a network fails to pay Stripe. The case is Mila's €120.00 class pass, the book's recurring payment, which becomes three figures in the provider's books, €117.47 of them owed to her studio.

[[payouts-and-money-movement]] follows that amount out of the ledger and asks **how money leaves the provider and reaches a bank account, and what happens when it does not arrive**. “Paid” means sent: a bank network delivers the transfer on its own schedule, and one that fails comes back days later as a new credit. In Larkfield's Payout That Bounced, 412 payouts worth €386,000 were returned in June 2026 to a record that had already closed them, and paying every studio took 19 days.

[[payment-reconciliation-and-reporting]] turns that case, two records of the same money that disagree, into the general question: **how a provider proves its own books against the networks and banks, and what it gives customers to prove theirs**. The proof is reconciliation, matching each movement the ledger expects against a record someone else wrote. Customers get it one level down as scheduled reports, itemized per payout at Stripe and per payable batch at Adyen, and the chapter argues for writing your books from those reports and not from webhooks. It closes one Larkfield day, Tuesday 9 March 2027, on both providers.

[[licences-and-safeguarding]] asks last **who is legally allowed to hold customer money, and where it sits**. Only a licensed institution may. Stripe states that it is an e-money institution in Europe and “not a bank” in the United States; Adyen states that it is a Dutch credit institution, which is a bank. Neither names the banks that hold the money. The case is a Larkfield proposal to hold studio payouts in its own account for 14 days, about €43 million of other people's money, stopped in review.

## Where to Begin

If you arrive with a problem, open its chapter. An unexplained difference belongs to [[payment-ledgers]], and a balance that moved without a payout to [[balances-and-funds-flows]]. A payout marked paid that has not arrived belongs to [[payouts-and-money-movement]], and a close that will not tie to [[payment-reconciliation-and-reporting]]. A funds flow that passes through your own bank account belongs to [[licences-and-safeguarding]].

Otherwise read in order. The five chapters ask one question five times: what does this record say is owed, and whose independent record agrees? That question explains the opening. Every payment status at Larkfield was right, and the €412,000 sat in movements that came after the payment and in a rounding rule, which a record of payments has no place for. Begin with [[payment-ledgers]].

## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Larkfield is fictional, and its figures are the same in every chapter.
