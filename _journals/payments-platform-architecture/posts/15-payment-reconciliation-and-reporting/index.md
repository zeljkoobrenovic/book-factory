---
title: "Proving the Money: Reconciliation Inside the Provider and Out"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How does a payment provider prove its own books against the networks and banks, and what does it give customers to prove theirs? It matches every movement its ledger expects against a record it did not write and ages what stays unmatched, then hands customers the same proof one level down as scheduled reports: by payout at Stripe, by payable batch at Adyen."
permalink: payment-reconciliation-and-reporting
timetoread: 25 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn how a provider proves its ledger against networks and banks, which reports Stripe and Adyen give you to repeat that proof, and how to close a day from them.

> **KEY POINTS:**
>
> * **A balanced ledger is consistent, not proven.** Double entry shows that the provider's own entries agree with each other. Whether an expected movement happened is known only from a record someone else wrote: a card network's clearing file or a bank's statement.
> * **The report is the provider's proof passed down one level.** Stripe itemizes each payout and states that its reports are ready “Within 12 hours” after the day ends. Adyen itemizes each payable batch, creates the report when the batch closes and says to expect it “within 3 hours after the batch closes”.
> * **Reports and webhooks are different contracts.** A webhook is prompt and may be missing; a report is complete and late. Book from the report, wait for the provider's signal that it is ready, and on two providers keep two matching keys: the payout and the batch.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Black-Box Balance** — a bank credit nobody can break down into payments, fees, refunds and holds lacks the itemized report this chapter is about.
> * **The Trusted Doorbell** — books kept from the webhook stream treat a prompt notice as a complete record, and miss every movement that has no event.
> * **The Orphaned Refund** — refunds and chargebacks land in a later payout or batch than the sale, and only a line-level match ties them back to it.

<br>
A provider's record says a payout is **paid**. The payee's bank account shows nothing, because the receiving bank sent the transfer back. Those are two records of the same money, and they disagree. In June 2026 Larkfield, the fictional studio-software platform this book follows, had 412 such payouts worth €386,000 unreconciled for three weeks ([[payouts-and-money-movement]]). Nothing inside the provider's ledger said which record was right: the ledger balanced the whole time.

The standing answer is this chapter's claim. **A provider proves its books by matching each movement its ledger expects against a record it did not write**, and by putting an age and an owner on whatever stays unmatched. What it gives customers is **the same proof one level down**: scheduled reports that itemize each amount it paid, per payout at Stripe and per payable batch at Adyen. Those reports are complete where webhooks are only prompt.

**Where we are in the payment's journey.** For example, take Mila's class pass: €120.00 paid to Studio Noord on Tuesday 9 March 2027 at 19:42, with the studio's payout arriving on Thursday 11 March. By then the provider, the card network, two banks and Larkfield each hold a record of her €120. This chapter covers the days in which those records are compared.

The chapter starts with Larkfield's close, which covered one provider and not the other. It then explains why a balanced ledger is not yet a proven one, reports what Stripe and Adyen have published about their own reconciliation, and describes the reports customers get. Next it shows why reports and webhooks are different contracts, compares three ways to run a close and compares the two providers. It ends with a worked close of 9 March and the ways a close goes wrong.

## Setting the Scene at Larkfield: A Close That Covered One Provider

Until the Keel program of 2027, Larkfield's nightly reconciliation job covered Adyen only, comparing the provider's reports with Larkfield's payment records and its small double-entry ledger. Stripe carried 44% of 2026 member payment volume (€493 million), and its side of the ledger was written from the payment record store, which is fed by webhooks. Almost half of the money was booked from notifications, with nothing outside to check them against.

The result came at year-end 2025. The ledger's “owed to studios” balance differed from the two providers' balances by **€412,000**, and Priya Raman, the finance controller, got an audit finding. Three weeks of work traced the difference to refunds made after payout, chargeback fees (a chargeback is a payment reversed through the card network at the cardholder's request) and a currency-conversion rounding rule. A “payment succeeded” notification carries none of the three. A ledger fed by payment events had no place for what happened after the payment.

Keel decision K3 is meant to prevent the next such search: an entry for every movement, clearing accounts that return to zero, and a reconciliation that covers both providers. Femke de Graaf, who leads Keel, turned it into a design question: **on each provider, which record do we write the books from, and what do we do with an amount the two sides do not explain?**

## Why a Balanced Ledger Is Not Yet a Proven One

Double entry proves less than it seems to. It guarantees that every recorded movement has two sides that sum to zero ([[payment-ledgers]]). It does not show that the movement took place, because the same party wrote both sides. An entry “expect €120 from the card network” balances whether or not the network pays. The amount waits in a clearing account, an account that should return to zero, and only the network's file and the bank's statement can empty it truthfully.

The activity that supplies the missing proof is **reconciliation**: showing that two independently written records of the same money agree, and explaining every difference. **Provider-side reconciliation** is the provider doing this for its own ledger. It compares that ledger with two outside records: the **clearing file**, the file a card network or acquirer (the bank-side party that collects card payments for merchants) sends to list each transaction it processed and what it will pay, and the **bank statement**, the bank's list of what was credited and debited. The table shows the three records as they are commonly kept; it is industry practice, not a description of either company.

| Record | Written by | One line is | Arrives |
| --- | --- | --- | --- |
| The provider's ledger | The provider | One movement of one payment | When the event happens |
| The clearing file | The card network or acquirer | One transaction it processed | Typically daily, after the fact |
| The bank statement | The bank | One credit or debit, often a net amount for many transactions | When the money moves, often a day or more later |

Because the three records differ in this way, comparing them cannot be a comparison of totals. Networks settle net ([[clearing-and-settlement]]): one amount per cycle, after fees, reduced by refunds and chargebacks from earlier days. A bank line is one figure standing for thousands of payments, on a later date. A total that fails to tie does not say which of them is wrong, so the match has to be made item by item, on a key the records share.

Then come the items that do not match. Each is an **exception**, and **exception aging** means recording how long each has been open and who owns it. Most exceptions are timing: the other record has not arrived yet. The ones that stay open are a missing file, a duplicate, a wrong amount or money that never came. Age separates the two groups without anyone inspecting each item, and in my experience an unexplained amount is harder to recover the longer it is left.

<!-- illustration-placeholder
{
  "id": "15-three-records-one-payment",
  "status": "pending",
  "asset": "assets/images/15-payment-reconciliation-and-reporting/15-three-records-one-payment.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on exception aging",
  "visual_goal": "Show one payment as three records matched item by item, with unmatched items kept on a dated, owned list.",
  "prompt": "Create a structural explainer diagram. On the left, three stacked documents: a ledger book labeled \"Ledger\", a file labeled \"Clearing file\", a sheet labeled \"Bank statement\". Three arrows, one from each, run right into a central station of two interlocking puzzle pieces labeled \"Match\". From it a green arrow labeled \"Matched\" goes right to a green checkmark box, and an orange arrow labeled \"Unmatched\" goes down-right to a clipboard labeled \"Open items\" with three rows, each with a calendar icon and a person icon. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Diagram of a ledger, a clearing file and a bank statement feeding a matching step, with matched items closed and unmatched items placed on a list with an age and an owner.",
  "caption": "One payment is three records with three writers; reconciliation matches them item by item and keeps what does not match on a list with an age and an owner."
}
-->

## What Stripe and Adyen Have Published About Proving Their Own Books

Stripe's fullest public account is its engineering post on Ledger from February 2024, which [[payment-ledgers]] reads in detail. Two things in the 2024 post matter here. It places reconciliation inside the fund flows the ledger models: a business adding funds to its balance “requires moving funds between banks, reconciling money movement with third-party reporting, and matching regulatory reporting with financial reporting”. And it names bad outside records as a normal condition: “We witness basic and obvious failures like malformed reports or propagated errors from banking or network partners”. In the post's own terms, “a single missing, late, or incorrect transaction” shows up as a clearing account that does not empty, found with a query the post quotes: “Find the clearing Accounts with nonzero balance.”

The same post also describes what happens to what does not clear: aging and ownership. A team's dashboard scores old items (“the 50% score for Aging Balances means that some clearing issues have persisted over time”) and comes with “auto-generated tickets”. When “the root cause is related to an infrastructure or third-party incident outside their control”, a team can “reassign ownership to the right internal stakeholders”. The clock is in days, with a manual remainder: “99.99% of our dollar volume is fully ingested and verified within four days”, while “the remaining long-tail is reliably handled through manual analysis”.

Stripe's current documentation adds one sentence about the comparison with a bank, for a US financial account backed by an FBO arrangement, a pooled account in which a bank holds funds “for the benefit of” many customers. There, the Treasury documentation (n.d., accessed November 2026) says, “Stripe records how much of the total balance belongs to your business and reconciles that record against the funds held at the bank.”

Adyen, in contrast, has published the matching step and not the control around it, and the account is old. Its 2021 engineering post explains that splitting the accounting database into several clusters complicated reconciliation: “if we received reports on processed transactions from our partners, we needed to match them to transactions in different clusters.” The solution was “a two-step framework that would first parse a file and then split it into the relevant parts for each cluster. The second step was to match the relevant transactions within the clusters.” It adds that “the reconciliation needs to happen for a lot of different very custom integrations so this was a real team effort.” **(Evidence age: 5 years; the current system may differ.)** I found no newer Adyen engineering source.

Adyen's current documentation shows the result of that matching to merchants. Its page on the payment accounting report (n.d., accessed November 2026) separates a claim from its confirmation: **SentForSettle** is the “Request to transfer the payment sent to the financial institution” and **Settled** means “Payment has been settled, and the funds have been received by Adyen.” It also publishes an aging rule. Adyen can pay merchants before it is paid itself ([[balances-and-funds-flows]]), and its page on upgrading to Sales day payout (n.d., accessed November 2026) says “Prefinancing is capped at 30 days”. After that a **SettledReversed** entry takes the amount back: “Payment has not been settled because Adyen has not received the funds 30 days after capture.”

And there the public record stops. Neither company publishes its matching rules, the formats of the files it receives from networks and banks, its match rates or its exception volumes. Stripe describes scores and tickets, not the matching; Adyen describes a 2021 matching framework, not what happens to an unmatched line. The picture connecting the fragments is mine.

> **INFERENCE, NOT DOCUMENTED:** Provider-side reconciliation at Stripe and Adyen is plausibly a three-way match of the internal ledger, the networks' and partners' files and the banks' statements, with a clearing account holding each expectation until the outside records confirm it. Both have published pieces consistent with that reference model; neither has published the model.

## What Customers Get: Reports Itemized by Payout and by Batch

A customer stands to its provider as the provider stands to the network. It has its own record of sales, and its bank shows one net credit. Only the provider knows which payments, refunds, disputes and fees that credit nets. So the customer needs the provider's itemized record, as the provider needs the clearing file. That record is a report, not a dashboard balance and not a notification.

Stripe's main one, for example, is the payout reconciliation report (documentation n.d., accessed November 2026), and its unit is the **payout**, the transfer from the Stripe balance to the customer's bank. Its itemized download lists “every payment, refund, dispute, fee, and other balance transaction included in the payout”; each row carries the payout's ID and the ID of the balance transaction, Stripe's record of one change to a balance. There are two limits. The report “is only available for users with automatic payouts enabled, or a platform on manual payouts whose Connected Accounts have automatic payouts enabled”: for payouts whose timing and amount the customer chooses, “Stripe can’t identify which transactions are included in each payout. You’re responsible for reconciling”. And its sibling, the balance summary report (n.d., accessed November 2026), “works like a bank statement” and “doesn’t associate payouts with payment transactions”.

Stripe also says when these reports are ready. Its report options page (n.d., accessed November 2026) gives a processing time of “Within 12 hours” for both: “A day’s report is normally available by 12:00 pm on the following day.” The reconciliation page then warns: “Report data follows a separate processing schedule, so a payout might arrive before its reconciliation data is ready.” For automation, the guide to its Reports v1 API (n.d., accessed November 2026) says Stripe publishes a `reporting.report_type.updated` event “twice per day (at 00:00 and 12:00 UTC)”, only to endpoints that subscribe to it explicitly and not to Connect webhook endpoints, the endpoints that receive events from a platform's connected accounts. As of November 2026 that guide points new integrations to a Reports v2 API, whose own guide documents events for a finished report run and whose examples carry a preview API version.

Beyond files, Stripe sells access to the same data as tables. Sigma (documentation n.d., accessed November 2026) is “an interactive SQL environment in the Stripe Dashboard”; Stripe's data-freshness page says it makes “most of your Stripe transaction data available to query within three hours”, and a comment in an example query on that page calls the `balance_transactions` table “the canonical record of changes to your Stripe balance”. Data Pipeline (n.d., accessed November 2026) sends the data to a warehouse such as Snowflake or BigQuery, “delivering a full load of data every 3 hours”. Matching payouts to bank deposits inside Stripe is narrower: bank reconciliation “is currently only available for users with direct US-based Stripe accounts using an automated payout schedule” (as of November 2026; likely to change).

Adyen's main report is built on a different unit: the **payable batch**, the set of entries Adyen pays out together for one merchant account (Adyen's term for the sub-account in which payments are processed and paid out). Under Sales day payout, Adyen's default model, “You get all the funds from a particular sales day in a single payout batch” (documentation, n.d., accessed November 2026). The settlement details report (n.d., accessed November 2026) is generated by default “per merchant account, per batch”, one line per entry: **Settled** payments, **Refunded**, **Chargeback**, fees, **DepositCorrection** when the security deposit Adyen withholds changes, **InvoiceDeduction** for amounts owed on the monthly invoice, and **MerchantPayout** for the payout itself, with “the unique payout reference (TX...XT), which can also be found on the bank statement”. A batch is not purely a day of sales: “Refunds, chargebacks, and other adjustments are added to the payable batch as they occur and are not related to the sales day of the original transaction.”

On timing Adyen names an event for this report, and one number. “When the payable batch closes, we create a Settlement details report” (its Getting paid page, n.d., accessed November 2026). Under Sales day payout “the payable batch always closes two hours after your sales day closing time”. A customer learns that a report exists from a webhook: “When a new report has been generated, you will receive a **REPORT_AVAILABLE** webhook” with the download URL (documentation, n.d., accessed November 2026). The number is on its page about report time zones (n.d., accessed November 2026): “If you have configured automatic generation of the Settlement details report at batch closure, you can expect the report to be generated within 3 hours after the batch closes.” For other ways of producing a report Adyen publishes (n.d., accessed November 2026) a window and a warning: reports on a daily schedule are generated “each day between 02:00 and 10:00 CET” (Central European Time), and a report requested by hand “may take several hours to generate, depending on its size”.

<!-- illustration-placeholder
{
  "id": "15-payout-versus-batch",
  "status": "pending",
  "asset": "assets/images/15-payment-reconciliation-and-reporting/15-payout-versus-batch.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on the timing of Adyen's settlement details report",
  "visual_goal": "Show the two units of reconciliation side by side: the payout and the sales-day batch.",
  "prompt": "Create a side-by-side comparison diagram split by a thin vertical divider. Left half tagged \"Provider A\": coins and receipt icons flow through a funnel into an envelope labeled \"Payout\" with a tag labeled \"Payout ID\"; an arrow labeled \"one credit\" goes from the envelope to a generic bank building. Right half tagged \"Provider B\": a calendar page labeled \"Sales day\" pours coins and receipt icons into an open box labeled \"Batch\" with a tag labeled \"Batch number\"; a small arrow labeled \"adjustments\" drops a refund icon into the box from above; an arrow labeled \"one credit\" goes from the box to a generic bank building. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two panels: movements grouped into a payout with a payout ID, and a sales day with its adjustments grouped into a batch with a batch number; each ends in one bank credit.",
  "caption": "Provider A is Stripe, whose report is keyed on the payout; Provider B is Adyen, whose report is keyed on the payable batch, by default one sales day plus the adjustments that occurred on it."
}
-->

The table lists these and the other reports this chapter uses. Platforms such as Larkfield need one more. Adyen's platform reporting documentation (n.d., accessed November 2026) marks the Balance Platform Accounting Report, the payment accounting report and the monthly invoice as “Required for full financial reconciliation”, and the settlement details report as “Optional for full financial reconciliation”. The balance platform is the part of Adyen that holds a balance account for each of the platform's users, so its daily report, not the batch report, is where a platform sees each user's money. Balance platform reports have their own readiness signal, a `balancePlatform.report.created` webhook that carries the download URL, and Adyen also documents a Balance Platform Payout Report that lists the transactions in each scheduled payout to a platform's user.

| Report | Provider | One line is | Use it to |
| --- | --- | --- | --- |
| Payout reconciliation | Stripe | One balance transaction, grouped by payout | Tie a bank credit to its payments, refunds, disputes and fees |
| Balance summary | Stripe | One balance transaction in a period | Reconcile the balance like a bank account; no link to payouts |
| Settlement details | Adyen | One journal entry in a payable batch | Tie a batch and its payout to payments, fees and adjustments |
| Aggregate settlement details | Adyen | Totals per batch, payment method and journal type | Match batches to the bank statement; find a returned payout (**BankInstructionReturned**) |
| Payment accounting | Adyen | One lifecycle status of one payment | Follow a payment from received to settled; check the monthly invoice |
| Balance Platform Accounting Report | Adyen (platforms) | One balance change on one balance account, per day in Central European Time | Reconcile each user's and the platform's own balance account |

## Reports and Webhooks Are Different Contracts

There is a serious case for keeping the books from webhooks instead. The events arrive within seconds, carry amounts, and are already consumed to update payment state, so posting them to the ledger costs almost nothing. Larkfield's Stripe side did this before Keel, and was right on most days.

The trouble is that the two channels promise different things, and the providers themselves say so. Stripe's report options page separates them in one line: “SLAs indicate when the reports are available for download. Webhook notifications might take additional time.” Adyen's Sales day payout page notes that the `SETTLED_REVERSED` and `REFUND_NOT_CLEARED` event types, which report money being taken back or returned, “apply to all payment methods and are disabled by default”. And Adyen describes its Balance Platform Accounting Report as the place to “Confirm the balance changes that you are informed of through webhooks” (all three pages n.d., accessed November 2026). In both providers' own words the webhook informs and the report confirms.

| | What it promises | What it does not promise |
| --- | --- | --- |
| **Webhook** | Prompt notice that one event happened | Delivery, order, or an event for every balance change ([[payment-webhooks-and-events]]) |
| **Report** | Every movement behind a payout or batch, with fees and adjustments, as of a stated cut-off | Speed: the money can arrive first |

<!-- illustration-placeholder
{
  "id": "15-doorbell-and-statement",
  "status": "pending",
  "asset": "assets/images/15-payment-reconciliation-and-reporting/15-doorbell-and-statement.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table that contrasts what a webhook and a report promise",
  "visual_goal": "Contrast a prompt signal that can be missed with a complete statement that arrives later.",
  "prompt": "Create a conceptual two-panel illustration. Left panel: a front door with a ringing doorbell, a clock showing an early time, and three notification cards flying toward the door, one drawn as a faded dotted outline because it never arrived. Label under the panel: \"Prompt\". Right panel: a desk with a long itemized statement, every line ticked, a total line with a euro sign, and a clock showing a later time. Label under the panel: \"Complete\". Between the panels an arrow from left to right labeled \"confirm\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Left: a ringing doorbell with notification cards, one of them missing. Right: a complete itemized statement being checked later in the day.",
  "caption": "A webhook is the doorbell: prompt, and possibly missing. A report is the statement: complete, and later. The books are written from the statement."
}
-->

The difference shows as money once the event stream is used as the complete record. Suppose a team books each night from that day's “payment succeeded” notifications, and on Thursday the bank credit is €1,930 lower than their sum *(an illustrative figure)*. The €1,930 is probably made of things those notifications never carried: the provider's fees, refunds, chargebacks, an increase in a reserve or deposit the provider holds back, and sales that belong to a different payout or batch than the day they were notified. Each of those is a line in the itemized report of the payout or batch.

The rule I use follows from that. Write the books from the report. Start the close on the provider's signal that the data is ready (Stripe's `reporting.report_type.updated` event; Adyen's `REPORT_AVAILABLE` webhook, or `balancePlatform.report.created` for balance platform reports), not on the bank credit and not at a fixed hour. Use payment webhooks to update state and to prompt a check. When the report leaves an amount unexplained, hold it as an open item with an age and an owner; do not write it off or fold it into a total. This is Larkfield's K2 applied to the books. It is stricter than Adyen's own advice for platforms, which is to “use API responses and webhooks to track individual payment transactions, and update your ledgers accordingly”, and then to reconcile daily against the Balance Platform Accounting Report (n.d., accessed November 2026). The rule has a limit: a decision that cannot wait hours, such as letting a member into a class, belongs to payment state ([[payment-state-machines]]).

## Three Ways to Run a Close on Provider Data

The first design is the one the rule argues against. An **event-fed close** posts every webhook to the books as it arrives. It is the earliest and the cheapest. Its weakness is structural: completeness rests on delivery. A movement with no event, or whose event type was never enabled or whose delivery was lost, does not reach the books, and nothing in the design can show that it is missing.

A **report-driven close**, in contrast, trusts a cut-off instead of delivery. It takes each payout (Stripe) or batch (Adyen), books every line of its itemized report and matches the report's total to one bank line. Whatever is left on either side becomes an open item. Completeness comes from the provider's own statement of what the payout or batch contains; the price is a day or more before a difference is seen. Both providers' reports are built for this design, and RECONCILED's [[payments-to-ledger]] covers the accounting entries on the customer's side.

A **warehouse-driven close** makes the same match with queries instead of files. The provider's transaction data is loaded into the customer's warehouse next to its own records, and the comparison runs as often as the data refreshes. On Stripe that can be every few hours, given Data Pipeline's 3-hour loads. For Adyen's payment and settlement reports I found only files documented, so the design there means ingesting each report file as it becomes available; for platforms Adyen also documents a Transfers API that returns the transactions of a balance account on request (n.d., accessed November 2026).

To sum up the choice: I would book from reports per payout or batch, add the warehouse when volume or a second provider makes file handling the bottleneck, and keep event-fed figures only as an early estimate that the report replaces. The table says why.

| Design | What proves completeness | Delay before a difference is seen | When it is right |
| --- | --- | --- | --- |
| Event-fed | Nothing: a missing event is never seen | Seconds for what arrives | As an early estimate; never as the books |
| Report-driven | The provider's cut-off per payout or batch | A day or more | The default |
| Warehouse-driven | The provider's data set plus your own queries | Hours, where the provider delivers tables | High volume, several providers, or a daily close |

## Stripe and Adyen: Where They Differ

Taken together, the documented facts above differ on five aspects. The Stripe and Adyen columns repeat what the earlier sections cite; the last column is my inference from the difference.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Own reconciliation, as published | 2024 post: outside reports inside fund flows, aging scores, tickets, 99.99% of dollar volume verified “within four days” | 2021 post (5 years old): two-step matching of partner files across accounting clusters; documentation (n.d., accessed November 2026) reverses an unreceived amount after 30 days | Stripe published the control, Adyen the matching step; neither publishes rules or rates, so do not rank them on this |
| Unit of the main reconciliation report | The payout; accounts with automatic payouts, or platforms whose connected accounts have them (n.d., accessed November 2026) | The payable batch per merchant account, by default one sales day (n.d., accessed November 2026) | The matching key differs: a bank credit on Stripe, a day of sales plus that day's adjustments on Adyen |
| Timing statement | “Within 12 hours” after the day ends; the payout can arrive first (n.d., accessed November 2026) | Created “When the payable batch closes” and expected “within 3 hours after the batch closes”; scheduled daily reports “between 02:00 and 10:00 CET” (n.d., accessed November 2026) | Each states an expected time, not a guarantee: Stripe 12 hours after the day ends, Adyen 3 hours after the batch closes |
| Signal that data is ready | `reporting.report_type.updated` (Reports v1 API), twice a day, by explicit subscription (n.d., accessed November 2026) | `REPORT_AVAILABLE` webhook with the download URL; `balancePlatform.report.created` for balance platform reports (n.d., accessed November 2026) | Adyen signals per report file; Stripe per report type, so the consumer checks which period is covered |
| Access to the underlying data | Sigma (SQL, about three hours) and Data Pipeline (warehouse, every 3 hours) (n.d., accessed November 2026) | Report files in CSV and other formats; for platforms, a Transfers API that lists balance account transactions (n.d., accessed November 2026) | Stripe sells the data as tables; for Adyen I found files and an API query documented and no SQL or warehouse product, which is not proof that none exists |

It follows that an integrator builds two slightly different closes. On Stripe, key the reconciliation on the payout ID, trigger it on data availability, and remember that manual and instant payouts come with no itemization. On Adyen, key it on merchant account and batch number, trigger it on `REPORT_AVAILABLE`, expect refunds and chargebacks in the batch of the day they occur and, as a platform, add the balance platform's daily report and its `balancePlatform.report.created` signal. On both, what does not match goes to one list of open items.

## In Practice at Larkfield: Closing Tuesday 9 March on Two Providers

For example, take the day Mila bought her pass. Under Keel the reconciliation job runs once per provider, on that provider's signal *(a local illustrative detail)*, and it follows one rule from K3: a ledger entry is written only from a report line, never from a webhook.

On the Adyen side, Mila's €120.00 at 19:42 falls in the sales day of 9 March, whose batch closes two hours after midnight, at 02:00 on 10 March. The job finds the payment by the PSP reference, Adyen's payment identifier (PSP stands for payment service provider). Because Larkfield is a platform, the split is in the Balance Platform Accounting Report, where Adyen's documentation (n.d., accessed November 2026) says a split payment appears as separate lines that share the PSP reference: **€117.47** to Studio Noord's balance account and **€2.53**, Larkfield's fee, to Larkfield's own. Adyen by default debits its fees from the platform's liable balance account, which is Larkfield's own, so the illustrative **€0.61** provider cost *(assumption)* is a further line there, leaving Larkfield €1.92. Each amount becomes a ledger entry with the report line as its source, and the studio's payout arrives on Thursday 11 March.

Had Studio Noord been on Stripe, by contrast, the job would look for the same €120.00 under the payout that carries it. Each row of the itemized report holds the payout's ID and the balance transaction's ID, and Stripe's documentation (n.d., accessed November 2026) says a platform can view the financial reports for connected accounts (the studios' accounts under Stripe Connect) that it controls. The match starts from a bank credit, not from a day of sales, and it cannot finish on the bank credit alone: “a payout might arrive before its reconciliation data is ready”. Until then the credit is recorded as received and not yet explained.

Next come the lines that do not match. After the close of 9 March the job's open items look like the table below *(all three are illustrative assumptions)*. Nothing is adjusted to make the day tie. Each item has an amount, an age and an owner, and an item open for more than five business days goes to Priya Raman's weekly review.

| Open item | Provider | Amount | Likely cause | Owner | Age at close |
| --- | --- | --- | --- | --- | --- |
| A drop-in marked `paid` in the payment record store, absent from the batch | Adyen | €16.00 | Captured after the sales day closed; expected in the next batch | The reconciliation job (closes itself on a match) | 0 days |
| A refund line in the batch with no refund request in Larkfield's records | Adyen | €49.00 | Refund made by hand in the provider's console, outside the payment service | Tom Hendriks, payments team | 1 day |
| A difference on a currency conversion | Stripe | £0.03 | Rounding rule differs between Larkfield's ledger and the provider | Priya Raman; booked to a rounding account under a written rule | 0 days |

Consequently the three causes of the €412,000 would each have surfaced early. A refund after payout, a chargeback fee and a rounding difference are the kinds of line in that table: a movement in a later batch than its sale, a fee nobody requested, a rule that differs. The old close and the new one differ in when a difference becomes visible and whether anyone owns it, not in whether differences occur.

## When It Goes Wrong: Late Reports, Late Reversals and Totals Forced to Tie

The most common failure is the mildest: the money arrives before the report, or the report is late. Stripe documents the first case, and Adyen's three hours after the batch closes is an expectation, not a guarantee. The recovery is a state, not a workaround: the bank credit is booked as cash received from the provider and left unmatched, and the close for that payout or batch waits. The credit must not be booked as sales from the day's notifications because the detail is missing.

After that comes the movement that arrives once its day has been closed. Adyen's 30-day rule is one source: after a **SettledReversed** entry, “If Adyen receives the funds after 30 days, you see an additional Settled booking”. Stripe's payouts are another: its payout documentation (n.d., accessed November 2026) says that when a payout fails, “the status might initially show as `paid`, but then change to `failed` within 5 business days” ([[payouts-and-money-movement]]). Larkfield's own example is Mila's €84.00 refund on 18 March for a pass paid out on 11 March. In each case the provider reports a new line in a later report, and the books do the same: a new entry in the period it is reported, linked to the original, with the closed day left closed.

A related failure only looks like lateness. Two records that cut the day at different times disagree about items near midnight, and the difference reverses the next day. Stripe's reports run in the account's time zone or in UTC. Adyen's settlement details report uses the account's time-zone setting, its Balance Platform Accounting Report covers a day in Central European Time, and its invoice documentation (all n.d., accessed November 2026) says “Your invoice is always based on the CET time zone.” The fix is to reconcile each match on the provider's unit and clock, and to derive your own calendar-day figures afterward.

Above all, the failure that does lasting damage is a human one: adjusting a total so that the day ties. The difference disappears from view, keeps its cause and comes back larger. Larkfield's €412,000, as I read it, accumulated over a year in which no day's difference had an owner. Stripe's 2024 post describes the opposite habit: unresolved balances scored by age, with tickets assigned to teams. An aged open item is the control. A plug removes it.

## What to Take Away

**Established.**

- A ledger that balances is consistent; it becomes proof only when its expected movements are matched to records another party wrote. Stripe's 2024 post puts “reconciling money movement with third-party reporting” inside its fund flows, and Adyen's 2021 post describes matching partner files to its accounting records.
- Both providers give customers itemized reports for that purpose, on different units: the payout at Stripe, the payable batch at Adyen (documentation accessed November 2026).
- Both treat the report as the confirming record: Stripe says a payout can arrive before its report data, and Adyen describes a report as confirming balance changes notified by webhook.

**Depends on context.**

- Files or a warehouse: report files are enough at low volume on one provider; tables in your own warehouse pay off with high volume, a second provider or a daily close.
- How long an open item may age: Larkfield's five business days suits daily payouts; monthly payouts or slow payment methods need a longer limit.
- A daily close is worth its cost when you owe other people money every day, as a platform does; a single merchant can often close weekly.

**The author's synthesis.**

- The report is the provider's own reconciliation passed down one level. I book from it because it is the only record whose completeness someone else has taken responsibility for.
- The output of a close is the list of open items, not the tied total. A close that always ties on the first try is, in my experience, one in which someone is adjusting.

## Questions to Ask

1. For each provider, which report do we write the books from, and what is one line of it?
2. What signal tells us the report is ready, and does our close wait for it?
3. What key ties a bank credit to its report lines on each provider?
4. Which balance changes have no webhook we subscribe to, and where do we see them?
5. Who owns an amount the report does not explain, and at what age is it escalated?
6. When a refund, chargeback or reversal arrives after its day was closed, do we book a new linked entry or reopen the day?
7. In which time zone does each report cut the day, and does our reconciliation use that cut?
8. What has the provider published about proving its own books, how old is that account, and what do we still take on trust?

Reconciliation, as this chapter has used the word, compares the provider's ledger with a bank's record of the same money. That takes one thing for granted: whose bank account it is, and who is allowed to hold other people's money in it. [[licences-and-safeguarding]] answers that, and shows that for a provider that is not a bank the comparison is a duty set by law.

## Sources and Evidence

*Company, product and investor sources*

- [Ledger: Stripe's system for tracking and validating money movement](https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement), Ilya Ganelin, Stripe, 2024-02-16 — reconciliation with third-party reporting inside fund flows, malformed partner reports, the clearing-account query, Aging Balances, tickets and reassignment, verification within four days.
- [Design to Duty: The Accounting and Reporting Systems at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2), Willem Pino, Adyen, 2021-08-23 — two-step matching of partner files across accounting clusters (evidence age: 5 years).
- [Payout reconciliation report](https://docs.stripe.com/reports/payout-reconciliation), Stripe, n.d., accessed 2026-11 — unit, itemized contents, automatic-payout limit, instant payouts, “a payout might arrive before its reconciliation data is ready”.
- [Balance summary report](https://docs.stripe.com/reports/balance), Stripe, n.d., accessed 2026-11 — “works like a bank statement”; no link between payouts and payments.
- [How report configuration works](https://docs.stripe.com/reports/options), Stripe, n.d., accessed 2026-11 — “Within 12 hours”, daily computation, exceptions, time zone, reports for connected accounts.
- [Run a report from the Reports v1 API](https://docs.stripe.com/reports/v1-api), Stripe, n.d., accessed 2026-11 — `reporting.report_type.updated` twice a day, `data_available_end`, not sent to Connect endpoints; new integrations pointed to the Reports v2 API.
- [Run a report from the Reports v2 API](https://docs.stripe.com/data/api/reports), Stripe, n.d., accessed 2026-11 — report-run events; examples carry a preview API version.
- [Payout reconciliation](https://docs.stripe.com/payouts/reconciliation), Stripe, n.d., accessed 2026-11 — listing balance transactions by payout; manual payouts are reconciled by the customer.
- [How Sigma works](https://docs.stripe.com/data/how-sigma-works), Stripe, n.d., accessed 2026-11 — “an interactive SQL environment in the Stripe Dashboard”; read-only data.
- [Sigma data freshness](https://docs.stripe.com/data/data-freshness), Stripe, n.d., accessed 2026-11 — three-hour availability; the example query that calls `balance_transactions` the canonical record.
- [How Data Pipeline works](https://docs.stripe.com/data/access-data-in-warehouse) and [Data Pipeline data freshness](https://docs.stripe.com/data/data-pipeline/data-freshness), Stripe, n.d., accessed 2026-11 — destinations, 3-hour cadence, delivery varies by data size.
- [Bank reconciliation](https://docs.stripe.com/bank-reconciliation), Stripe, n.d., accessed 2026-11 — availability limited to direct US-based accounts (volatile).
- [Treasury](https://docs.stripe.com/treasury), Stripe, n.d., accessed 2026-11 — the FBO-backed US account sentence on reconciling Stripe's record against funds held at the bank.
- [Payouts](https://docs.stripe.com/payouts), Stripe, n.d., accessed 2026-11 — a failed payout can first show as paid and change to failed within 5 business days.
- [Settlement details report](https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report), Adyen, n.d., accessed 2026-11 — per merchant account and batch, entry and journal types, the payout reference on the bank statement, time zone.
- [Aggregate settlement details report](https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report), Adyen, n.d., accessed 2026-11 — batch-level totals; BankInstructionReturned.
- [Payment accounting report](https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report), Adyen, n.d., accessed 2026-11 — SentForSettle, Settled and SettledReversed record types.
- [Getting paid](https://docs.adyen.com/account/getting-paid), Adyen, n.d., accessed 2026-11 — payable batch, report created when the batch closes, returned payouts.
- [Sales day payout](https://docs.adyen.com/account/sales-day-payout), Adyen, n.d., accessed 2026-11 — one batch per sales day, batch close two hours after the sales day, adjustments as they occur, event types disabled by default.
- [Upgrade to Sales day payout](https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp), Adyen, n.d., accessed 2026-11 — the 30-day cap on prefinancing and the later Settled booking.
- [Automatically get reports](https://docs.adyen.com/reporting/automatically-get-reports), Adyen, n.d., accessed 2026-11 — the REPORT_AVAILABLE webhook; scheduled daily reports generated between 02:00 and 10:00 CET.
- [Time zone setting](https://docs.adyen.com/reporting/time-zone-setting), Adyen, n.d., accessed 2026-11 — the settlement details report is expected within 3 hours after the batch closes.
- [Manually get reports](https://docs.adyen.com/reporting/manually-get-reports), Adyen, n.d., accessed 2026-11 — a manually generated report “may take several hours to generate”.
- [Reports and fee types](https://docs.adyen.com/platforms/reports-and-fees), Adyen, n.d., accessed 2026-11 — reports required for a platform's reconciliation, splits in reports, fees debited from the liable balance account, confirming webhook-notified balance changes.
- [Balance Platform Accounting Report](https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report), Adyen, n.d., accessed 2026-11 — daily report of balance changes, by day in Central European Time; Adyen's advice to update ledgers from webhooks and reconcile daily against the report.
- [Get platform reports](https://docs.adyen.com/platforms/prepare-reports/generate-download-reports), Adyen, n.d., accessed 2026-11 — the `balancePlatform.report.created` webhook with the download URL.
- [Balance Platform Payout Report](https://docs.adyen.com/platforms/reports-and-fees/payout-report), Adyen, n.d., accessed 2026-11 — the transactions in each scheduled payout to a platform's user.
- [Track transactions with API requests](https://docs.adyen.com/platforms/transfer-transactions/track-api), Adyen, n.d., accessed 2026-11 — the Transfers API query for the transactions of a balance platform, account holder or balance account.
- [Payment processing invoice](https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice), Adyen, n.d., accessed 2026-11 — invoice based on the CET time zone.

*Standards, regulation and official documentation*

- None.

*Research and practitioner sources*

- [[payments-to-ledger]] in RECONCILED — the customer's side of the same match: posting provider reports to the general ledger.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
