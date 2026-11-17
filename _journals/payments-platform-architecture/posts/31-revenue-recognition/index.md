---
title: "Cash Is Not Revenue: Revenue Recognition and the Hand-off to Finance"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How does a billing system turn invoices and payments into recognized revenue, and where should it stop? It gives each invoice line a service period, defers the amount and releases it as the service is delivered; it should stop where contracts stop matching invoices, and hand finance a line-level export either way."
permalink: billing-revenue-recognition
timetoread: 23 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn why cash, billings and revenue differ, how an invoice line becomes a revenue schedule, and what a billing system owes finance.

> **KEY POINTS:**
>
> * **A payments report is not a revenue report.** Revenue counts when a service is delivered, not when it is charged. Money paid up front is deferred revenue, a liability, until it is earned, and every refund, dispute and credit note is a dated adjustment to the schedule.
> * **Stripe documents a recognition ledger built on its own invoices; for Adyen none was found.** Stripe Revenue Recognition treats "each invoice line item as its own performance obligation" and spreads it evenly over the line's period. Adyen's reports describe transactions. Orb, which Adyen has owned since 1 July 2026, documents recognition for Orb's own product.
> * **Recognition inside the billing system fits a business whose contracts equal its invoices.** Past that point the schedule belongs in a finance system. In both cases the billing side owes the same export per invoice line: net amount, service period, product and every later adjustment with its own date.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Orphaned Refund** — a refund or dispute that cannot be tied to its original invoice line cannot be split between revenue already earned and revenue still owed.
> * **The Version Cliff** — finance's revenue numbers depend on an export from the billing integration, and an API upgrade that drops one field makes them wrong without an error.

<br>
On 1 February 2027 Ironworks Climbing pays €1,890 for a year of software from Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]). At the end of the month, what did Larkfield make from that customer in February? The invoice says €1,890. The bank says €1,890. The accountant says €144.99, the share of the year that has been delivered: 28 days of 365. **All three are correct, and only the last is revenue.**

The rule that separates them is the subject of this chapter. **A billing system turns an invoice line into revenue by giving it a service period, deferring its amount and releasing it as the service is delivered**, with every refund, dispute and credit note as a dated adjustment. It should stop where contracts stop matching invoices. Stripe Revenue Recognition is documented on that assumption. For Adyen I found no revenue-recognition product; its reports describe payments, settlement and fees. This is the third of this part's failures of time: not late, not twice, but **in the wrong period**.

**Where we are in the payment's journey.** This chapter is off the path of Mila Janssen's class pass, but it reads the same records. Larkfield's €2.53 fee on her €120.00 pass is earned on Tuesday 9 March 2027, the moment the payment is processed. The pass itself is ten classes Studio Noord still owes her, which is why her refund on 18 March is €84.00: seven classes not yet delivered. One payment holds both kinds of revenue this chapter separates, a fee earned at one moment and a prepaid service earned class by class.

The chapter starts with two Larkfield reports that disagree about February. It then defines cash, billings, revenue and the terms the accounting standards add, and shows how an invoice line becomes a schedule. Next come what Stripe documents and what was and was not found for Adyen, then the three places a schedule can be kept and where billing should stop. The chapter then puts Stripe and Adyen side by side, works the annual plan month by month and ends with the quiet ways recognition goes wrong.

## Setting the Scene at Larkfield: Three Numbers for February

At the February 2027 close, two Larkfield reports disagree. The billing integration that charges studios for their Larkfield subscriptions was owned by the growth team until 2027, and its dashboard has a tile called "subscription revenue" that sums the invoices paid in the month. For Ironworks Climbing, Ravi Shah's chain in Manchester, it shows €1,890. Priya Raman, the finance controller, has €144.99 in her books for the same customer and the same month. The two numbers are thirteen times apart, and both were computed from the same Stripe invoice.

Femke de Graaf, whose payments team takes over the billing integration in May 2027, inherits the question behind the gap. Priya's number comes from an export that the billing integration sends to finance, and that export has failed before: in the Version Cliff of March 2026 an API upgrade removed a field it read, and subscription revenue reports were wrong for six days. So the question is a design question: **what must the billing side hand finance so that the second number can be computed and defended, and should the provider compute it instead?**

## Cash, Billings and Revenue: Three Numbers, Three Dates

The gap has three names. **Billings** are the amounts invoiced in a period. **Cash** is what was collected. **Revenue** is what was earned by delivering what was promised. For a sale delivered in the month it is paid, the three coincide. For anything paid in advance or in arrears they fall in different months, as two Larkfield cases show; the second is an illustrative studio that sends 1,000 text messages over its plan's allowance in March, at €0.07 each, and is invoiced for them in April.

| Case | Month | Billings | Cash | Revenue |
| --- | --- | --- | --- | --- |
| Annual plan, €1,890 paid 1 February 2027 | February | €1,890.00 | €1,890.00 | €144.99 |
| Annual plan | March | €0 | €0 | €160.52 |
| SMS overage, 1,000 messages *(assumption)* | March | €0 | €0 | €70.00 |
| SMS overage | April | €70.00 | €70.00 | €0 |

Which of the three counts as revenue is not a matter of taste. The two main accounting frameworks, International Financial Reporting Standards (IFRS) and the US Accounting Standards Codification (ASC), took their revenue rule from one joint project. In their news release of 28 May 2014 the two standard setters, the International Accounting Standards Board (IASB) and the US Financial Accounting Standards Board (FASB), said they had "today issued jointly a converged standard on the recognition of revenue from contracts with customers", to enter US rules "as Topic 606" **(Evidence age: 12 years; the standard is in force.)** The IFRS Foundation's page on the standard (n.d., accessed November 2026) records the same event: "In May 2014 the Board issued IFRS 15 *Revenue from Contracts with Customers*, together with the introduction of Topic 606 into the Financial Accounting Standards Board's *Accounting Standards Codification*", and says IFRS 15 applies to annual periods beginning on or after 1 January 2018. The FASB's website refused automated requests on 17 November 2026, so I read its release in an archived copy and did not read the text of ASC 606 itself; the steps below are quoted from the IFRS Foundation's summary. The rule has five steps, and none of them starts from the payment.

| Step, in the IFRS Foundation's words | In one line | What a billing system holds |
| --- | --- | --- |
| "identify the contract(s) with a customer" | What was agreed | Often outside billing: an order form, terms |
| "identify the performance obligations in the contract" | List the separate promises | Products and invoice lines, which may or may not match the promises |
| "determine the transaction price" | What the seller expects to receive | The invoice amount, net of tax |
| "allocate the transaction price to each performance obligation" | Split the price across the promises by what each would sell for alone | Line amounts, if each line is one promise |
| "recognise revenue when a performance obligation is satisfied" | Count each share as its promise is kept | The line's service period |

Step two introduces the term this chapter owns. A **performance obligation** is, in the IFRS Foundation's summary of the standard, one of the "promises in a contract to transfer to a customer goods or services that are distinct"; one contract may hold several. Each "may be satisfied at a point in time (typically for promises to transfer goods to a customer) or over time (typically for promises to transfer services to a customer)". A year of software access is satisfied over time. A one-day onboarding workshop is satisfied on its day. Larkfield's fee on one member payment is satisfied when the payment is processed.

A promise satisfied over time splits an up-front payment in two. The part not yet earned is **deferred revenue**: a liability, because the seller owes either the service or the money back. The **revenue schedule** is the dated plan by which that liability becomes revenue. On 31 March 2027, 59 of the 365 days of Ironworks' plan have been delivered, so €305.51 is revenue and €1,584.49 is deferred. Counted as two of twelve equal months, the figures are €315.00 and €1,575.00. By the day or by the month is a convention that finance chooses once and applies consistently; this chapter counts by the day. [[accounting-for-architects]], in this book's finance-side sibling, covers the standard in more depth.

<!-- illustration-placeholder
{
  "id": "31-cash-is-not-revenue",
  "status": "pending",
  "asset": "assets/images/31-revenue-recognition/31-cash-is-not-revenue.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that defines deferred revenue and the revenue schedule",
  "visual_goal": "Show that the money for an annual plan arrives once while the revenue arrives month by month.",
  "prompt": "Wide conceptual illustration with two horizontal lanes sharing a twelve-step timeline along the bottom. Top lane, labeled \"Cash\": one tall stack of coins standing on the first step only, with an orange arrow labeled \"paid once\" pointing down to it; the remaining eleven steps of this lane are empty. Bottom lane, labeled \"Revenue\": twelve small equal green blocks, one on each step, with a teal arrow labeled \"earned monthly\" running left to right above them. Between the lanes, on the left, a glass jar labeled \"Deferred\" that is nearly full of blue liquid; a thin blue dashed arrow labeled \"released\" leads from the jar to the row of green blocks. Under the first step a small calendar icon labeled \"1 Feb\"; under the last step a small calendar icon labeled \"31 Jan\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Top lane: one stack of coins on the first of twelve steps. Bottom lane: twelve equal blocks of revenue, one per step, fed from a jar labeled Deferred.",
  "caption": "The €1,890 arrives on 1 February; the revenue is released from deferred revenue over the 365 days that follow."
}
-->

## How an Invoice Line Becomes a Schedule

The schedule is computed from the invoice, in three entries. When the invoice is finalized (frozen and issued; [[invoicing-collections-and-dunning]] owns that step), each line's amount is booked as owed by the customer and as deferred revenue. When it is paid, cash replaces the amount owed. As each day of the service period passes, a slice moves from deferred revenue to revenue. Stripe's documentation (n.d., accessed November 2026) describes the first two: "an entry which finalizes an invoice would debit AccountsReceivable and credit DeferredRevenue. Paying an invoice would debit Cash and credit AccountsReceivable." Note what the payment does not touch. Orb's documentation (n.d., accessed November 2026) says it outright: "the payment status of an individual invoice is not factored into accounting treatment." **Payment moves cash; delivery moves revenue.**

Those entries need four inputs per invoice line, and a missing input does not raise an error. It falls into a default.

| Input per invoice line | Where it comes from | If it is missing |
| --- | --- | --- |
| Amount net of tax | The line, with tax as a separate amount ([[billing-and-payment-tax]]) | Tax is counted as revenue |
| Service period, start and end | The subscription's billing period, or set by hand on a one-off invoice | The whole amount is recognized on one day (Stripe's documented default, below) |
| Product | The price and product behind the line | A workshop cannot be treated differently from access |
| Currency | The invoice | Amounts in different currencies are summed or converted at the wrong date |

Money that goes back is a dated adjustment, and it splits in two. A refund, a dispute (the cardholder's bank takes the money back; [[refunds-reversals-and-disputes]]) or a credit note (a document that reduces a finalized invoice) can arrive months into the period. The part of the amount already recognized becomes **contra revenue**, an account that reduces revenue without deleting the original entry. The part still deferred is removed from the liability. Stripe's example: "if you issue a 120 USD refund on an annual subscription during the second month, 20 USD for the first 2 months is contra revenue. The remaining 100 USD is adjusted and reflected in your deferred revenue balance". Had Ironworks disputed its whole €1,890 on 1 August 2027 (a hypothetical), 181 days would have been delivered: €937.23 would become contra revenue and €952.77 would leave deferred revenue. The split cannot be computed at all unless the adjustment carries its own date and points at the original line.

<!-- illustration-placeholder
{
  "id": "31-line-to-schedule",
  "status": "pending",
  "asset": "assets/images/31-revenue-recognition/31-line-to-schedule.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on refunds, disputes and credit notes",
  "visual_goal": "Show the mechanism: an invoice line fills deferred revenue, time releases it into revenue, and a refund draws from both sides.",
  "prompt": "Left-to-right flow diagram with four elements. Far left: a document icon with one highlighted row, labeled \"Invoice line\". Center: a tall transparent tank labeled \"Deferred\", about half full of blue liquid, with a small clock icon on its side. Right: a row of green blocks on a shelf labeled \"Revenue\". Bottom right: a small red-orange tray labeled \"Contra revenue\". Arrows: a blue arrow labeled \"finalized\" from the invoice line into the top of the tank; a teal arrow labeled \"each day\" from the bottom of the tank to the revenue shelf; an orange arrow labeled \"refund\" entering from the lower left and forking in two, one branch labeled \"unearned part\" drawing liquid out of the tank, the other branch labeled \"earned part\" dropping one green block from the shelf into the contra revenue tray. A separate small coin icon labeled \"paid\" sits below the invoice line with no arrow to the tank or the shelf. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "An invoice line fills a deferred-revenue tank that drains daily into revenue; a refund forks into an unearned part taken from the tank and an earned part moved to contra revenue.",
  "caption": "A finalized invoice line fills deferred revenue, each day of the service period releases a slice into revenue, and a refund is split between the part still deferred and the part already earned; the payment itself moves neither."
}
-->

Usage runs the other way: it is earned first and invoiced later. The text messages a studio sends on 30 March are March revenue, though the invoice that carries them is dated April ([[usage-metering-and-rating]] owns the counting). So at every month end some revenue belongs to a month whose invoice does not exist yet, and the schedule needs the **date of use** as well as the date of the invoice. Orb states both the problem and its own rule. Recognizing usage "requires understanding exactly when usage occurs. This can be particularly difficult when invoicing and accounting periods do not align", and "Revenue is recognized for usage as it occurs on a daily basis, regardless of the associated line item’s service period."

The last input is a state, not a field: which accounting periods finance has closed. Once the books for February are closed, a refund or a backdated cancellation that belongs to February cannot rewrite February. It is booked as a correction in the current period. Both vendors' products model this. Stripe documents accounting periods that close automatically or by hand and can be reopened to "make adjustments to past data without creating corrections in the current period"; Orb documents period locks, saying that "Closing an accounting period ensures that there will be no subsequent changes to that period". A schedule that ignores the close produces history that changes after it has been reported.

## What Stripe Documents: A Ledger Over What Stripe Sees

Stripe's documentation (n.d., accessed November 2026) describes its product in two sentences that carry most of this chapter. The first is the basis: "Stripe built Revenue Recognition on top of a double-entry accounting ledger that tracks debits and credits resulting from your business activity", and it "automatically calculates all transactions that happen within Stripe". The second is the simplifying assumption: "Revenue Recognition treats each invoice line item as its own performance obligation. When the invoice finalizes, Revenue Recognition defers the total recognizable amount and subsequently amortizes it evenly over the period of each invoice line item." To amortize is to release in equal slices; "By default, Stripe Revenue Recognition recognizes revenue by the day", with by-the-second and by-the-month settings. (Another page of the same documentation, on subscriptions, says the product "amortizes revenue by the second"; I follow the settings page.) Step two of the standard is mapped onto the structure of the invoice.

What has no service period is recognized at once. "If you don’t set a period on an invoice line item, Revenue Recognition recognizes the full amount on the invoice line item when the invoice is finalized." A payment made without an invoice has no period either: "By default, Revenue Recognition recognizes these payments immediately when the payment occurs." For a platform on Connect, Stripe's product for businesses that take payments for others, the platform's fee on a destination charge (a payment taken on the platform's account and passed on to the seller) "is immediately recognized as the revenue"; Stripe says destination charges are available to all users of the product and other charge types on request.

Stripe documents four ways past these defaults. **Rules** change the treatment of a product, a customer or a line, for example to amortize over a custom period; "Each transaction can only have one rule applied to it", and "Rules are typically applied to reports within 24 hours." **Imports** are CSV files that add or override a service period, split a payment into several schedules, or bring in "an external payment processor’s data with a service period, amount, and currency"; reports "take approximately 3-4 hours to update after you upload data". **Standalone selling prices** split the amount of a product sold as a bundle across its components, by amounts or percentages that the business enters, and give each component its own schedule; a product that has a rule cannot be a bundle, and "You can’t apply bundles alongside data imports." And a **Performance Obligations API**, in preview with access on request as of November 2026, recognizes a line as fulfillment is reported instead of evenly over time. All four are maintained by finance, beside the billing integration.

What comes out is reports. New activity "appears within approximately 3-4 hours after transaction completion"; a warehouse sync runs "once every 6 hours"; a mapping lets the reports use the account names and numbers of the business's own general ledger, the master set of accounts from which financial statements are drawn; and the report API carries the note "Because this feature is in beta, the data fields might change." [[stripe]], in the finance-side sibling book, looks at this product from the enterprise's side, and [[payments-to-ledger]] at the posting.

> **INFERENCE, NOT DOCUMENTED:** Stripe uses the word subledger itself: its product page (n.d., accessed November 2026) carries the heading "A centralised revenue subledger", and its activity breakdown report has a column "Stripe subledger account". What the word implies is my reading: a detailed ledger for one kind of activity whose totals still have to be posted to the general ledger by something else, on finance's schedule. Stripe's pages describe reports, exports, an account mapping and a separate connector for one accounting system (NetSuite); I found none that says the product is the book of record (documentation, support site and product pages, November 2026).

The pages I read stop short of three things. Step four, allocating one price across several promises by what each would sell for alone, is documented only for a product set up as a bundle, with selling prices the business enters; I found no description of allocation across a contract that spans several lines or invoices. They do not describe estimating a price that varies. And two account descriptions on the methodology page say "This is only used when working with revenue contracts", while neither Stripe's documentation index and sitemap, fetched on 17 November 2026, nor any of the Revenue Recognition pages I read, nor a web search of Stripe's sites, explains what a revenue contract is. (The index is not complete: the page on standalone selling prices is linked from other pages and absent from it.) That is where the public record ended on that date. It is not a statement that the product cannot do these things.

## What Adyen Documents: Payments, Settlement and Fees

For Adyen I found no counterpart. Its documentation (n.d., accessed November 2026) opens the reporting section with "Adyen reports show you information about your transactions", and its Settlement details report "includes the details of payments that have been settled and paid out to you by Adyen". Its guide to closing a fiscal period works from the balances in its Monthly finance report. Those are cash-side records. Adyen's documentation index, fetched on 17 November 2026, lists about 2,600 pages; none has "revenue recognition", "deferred", "billing" or "Orb" in its title or description, and the full text of the documentation, searched the same day, never uses the phrase "revenue recognition". The sitemap of Adyen's help center, fetched the same day, lists no article on revenue recognition; its two articles with "billing" in the address concern Adyen's own invoices to its merchants. This is an absence in public sources, not a statement by Adyen, and it is consistent with the earlier finding that Adyen's platform holds payments and no invoice ([[subscriptions-and-billing-engines]]).

Adyen does now own a company that documents revenue recognition. Its press release of 1 July 2026 says the acquisitions of Talon.One and the billing company Orb "officially closed on July 1, 2026". Orb's documentation (n.d., accessed November 2026) says "Orb automatically calculates recognized revenue in a way that accords with ASC606 guidelines", and promises "the lineage of revenue from a summary entry → invoice → raw product usage data". That describes Orb's own product, which collects its invoices through more than one provider: "Orb integrates with payment gateways like Adyen and Stripe for payment processing", and a page of Orb's documentation describes connecting an Adyen merchant account. That is Orb collecting through Adyen, documented by Orb. On Adyen's own website I found revenue recognition mentioned twice, both times about Orb or billing in general: the partner page for Orb (n.d., accessed November 2026) says "finance teams get fine-grained reporting to facilitate revenue recognition", and the article "Usage-based billing, explained" of 22 October 2026 names revenue recognition as one of two things to consider when setting such billing up. Adyen's article of 29 September 2026 on the acquisition speaks of integration in the future tense: "You'll soon see how we bring this unified Adyen and Orb experience to life across our platform." As of November 2026 I found no Adyen documentation of a revenue-recognition product or of Orb's reporting as part of Adyen's platform.

## Three Places to Keep the Schedule, and Where Billing Should Stop

There are three places to compute revenue, and the first is where most teams start: the payment report. A query sums successful payments per month and the result is labeled revenue. A payment record has an amount and a date and no service period, so for Ironworks this design reports €1,890 in February and nothing for eleven months. It is right only for a business in which every sale is delivered in the month it is paid.

The second design keeps the schedule in the billing system. The billing system already holds the line, its period and every adjustment, so the schedule follows each proration (a part-period charge when a plan changes mid-cycle), credit note and refund without anyone copying data, and every revenue figure traces back to a line. This is the design Stripe documents, and the one Orb documents with usage. It holds as long as each invoice line is one promise, delivered evenly over the line's period.

The third design keeps the schedule in a finance system, fed by the billing system. It becomes necessary when a contract and its invoices diverge. Suppose a sales team sells, on one invoice line, a year of access together with a one-day onboarding workshop held in the first week. The default spreads the whole amount over the year, but the workshop is a separate promise kept on one day. The options are to split the line, to configure the split in the recognition product (on Stripe a rule, an import or a bundle with standalone selling prices), or to keep the schedule where the contract is known. Negotiated deals, bundles and revenue that arrives through more than one provider all push the same way.

| | From payment reports | In the billing system | In a finance system |
| --- | --- | --- | --- |
| Sees | Payments, refunds, disputes | Invoice lines, periods, adjustments it issued | Contracts, plus whatever each billing system exports |
| Gets wrong | Anything prepaid or billed in arrears | Bundles on one line, negotiated terms, sales made elsewhere | Nothing by design; everything if the export is poor |
| Trace for an auditor | Payment to bank | Revenue entry to invoice line | Revenue entry to contract, through the export |
| Right when | Every sale is delivered in the month it is paid | Contracts equal invoices | Contracts differ from invoices, or revenue comes from several systems |

So where should a billing system stop? My answer: it may compute the schedule while contracts equal invoices, and it must always be able to hand over the data from which finance could compute it. That export is the same in the second and third designs. The accounting judgement (what the promises are, when each is kept) stays with finance in both.

| Per invoice line, the billing side exports | Why finance needs it | Without it |
| --- | --- | --- |
| Amount net of tax, and currency | Tax is not revenue | Revenue is overstated by the tax |
| Service period, start and end | The schedule is a function of these two dates | The amount lands in one month |
| Product, with a stable identifier | The product identifies the promise | Every line is treated as access over time |
| Each refund, dispute and credit note, with its own date and the line it applies to | The earned and unearned parts are split at that date | The adjustment lands in the wrong period or on no line |
| For usage, the date of use | Usage is earned when it happens | A month of usage is counted in the next month |

<!-- illustration-placeholder
{
  "id": "31-billing-finance-boundary",
  "status": "pending",
  "asset": "assets/images/31-revenue-recognition/31-billing-finance-boundary.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the export specification table",
  "visual_goal": "Show the hand-off from billing to finance as an interface with named contents.",
  "prompt": "Two-zone illustration divided by a vertical dashed line labeled \"Hand-off\". Left zone, labeled \"Billing\": a machine with a calendar and gears producing a stack of documents. Right zone, labeled \"Finance\": a desk with an open ledger book and a person in office clothes reviewing it. Crossing the dashed line, a conveyor belt carries one open parcel from left to right, drawn with a blue arrow labeled \"export\". Above the parcel, five small tags fan out, each with a simple icon and a short label: a coin tag labeled \"Net amount\", a two-date calendar tag labeled \"Service period\", a box tag labeled \"Product\", a curved-back-arrow tag labeled \"Adjustments\", a gauge tag labeled \"Usage date\". In the lower left corner, far from the belt, a small faded stack of coins labeled \"Payments\" with a thin gray dotted arrow that stops at the dashed line and does not cross it. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A parcel crosses from a billing machine to a finance desk carrying five tags: net amount, service period, product, adjustments, usage date. A stack of payments stays behind the line.",
  "caption": "What billing owes finance for each invoice line: the net amount, the service period, the product, every adjustment with its own date and, for usage, the date of use; a total of payments does not cross the line."
}
-->

## Stripe and Adyen: Where They Differ

The Stripe and Adyen columns restate facts cited above; the last column is my inference throughout.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| First-party recognition product | Stripe Revenue Recognition, "built ... on top of a double-entry accounting ledger" (documentation, n.d., accessed November 2026) | Not public: none found in the documentation (index and full text), the help center or adyen.com on 17 November 2026. Orb, owned since 1 July 2026, documents one for its own product | The product follows the invoice: the provider that holds invoices can schedule them |
| Source of the schedule | Its own invoice lines, each "its own performance obligation", amortized by the day by default according to its settings page (n.d.) | Not public. Reports cover "your transactions" (n.d.) | On Adyen the schedule starts in the merchant's own billing system |
| Revenue from elsewhere | CSV import, including "an external payment processor’s data" (n.d.) | Not public | Stripe's product can hold the whole schedule, through files finance maintains |
| Output | Reports about 3 to 4 hours behind activity; general-ledger account mapping; report API "in beta" (n.d.) | Transaction and settlement reports (n.d.) | Both stop before the general ledger; Stripe stops one step later |

On Stripe, decide with finance whether your contracts equal your invoices before the product is switched on, and check that every recurring line carries a period. On Adyen, the schedule is built from your own billing system's invoices, and Adyen's reports supply the cash side only: what was paid, refunded, charged back and paid out ([[payment-reconciliation-and-reporting]]). [[case-stripe]] and [[case-adyen]] place this difference in each company's wider bet.

## In Practice at Larkfield: The Annual Plan, Month by Month

Here is Ironworks' plan as Priya Raman's books carry it. The €1,890 is taken as net of tax *(assumption)*, the service period runs from 1 February 2027 to 31 January 2028, and one day is worth €1,890 ÷ 365 = €5.18. Larkfield's fiscal year is the calendar year, so its 2027 accounts show €1,729.48 of revenue from this customer and a liability of €160.52, although all the cash arrived in February.

| Period | Days | Revenue in the period | Recognized to date | Deferred at period end |
| --- | --- | --- | --- | --- |
| February 2027 | 28 | €144.99 | €144.99 | €1,745.01 |
| March 2027 | 31 | €160.52 | €305.51 | €1,584.49 |
| April to December 2027 | 275 | €1,423.97 | €1,729.48 | €160.52 |
| January 2028 | 31 | €160.52 | €1,890.00 | €0 |

One subscription is the easy part; the whole of Larkfield's revenue is harder. In 2026 it had €24.5 million of subscriptions, billed with Stripe Billing and earned over time, and €19.8 million of payment fees, each earned at the moment of a member's payment. Stripe carried 44% of member payment volume and Adyen 56%. A recognition ledger over "all transactions that happen within Stripe" would hold the subscriptions and the fees on the Stripe side, and none of the fees on the 56% that Adyen carried unless finance imported them as files.

So Priya keeps the schedule in the finance system, and the growth dashboard's tile is renamed "billings". What Femke's team builds is the export: one row per invoice line with the fields in the table above, and one row per adjustment. Before 2027 it was a script nobody tested. Now it is a versioned interface, and under Keel decision K7 (one planned API upgrade per provider per half-year, tested against recorded traffic) each upgrade is tested against it, because the Version Cliff was this export losing one field.

## When It Goes Wrong

Recognition rarely fails with an error. The first quiet failure is a line with no service period. On Stripe the documented default recognizes it in full on the day the invoice is finalized, so a one-off invoice for an annual plan, created by hand without a period, moves a year of revenue into one month. The check is a query: lines for recurring products whose period is empty, or shorter than the plan's interval.

The second is an invoice nobody decides about. Stripe's reconciliation guide says unpaid invoices that stay open "continue to be recognized as revenue in the Revenue Recognition report", and advises marking them uncollectible or void. So collections and recognition have to agree on the day a debt is given up; if dunning, the scheduled retries and reminders for an unpaid invoice ([[invoicing-collections-and-dunning]]), ends without changing the invoice's status, revenue keeps accruing for a customer who will never pay.

The third is a late change to a closed month. Stripe's rules page warns: "If the effective period for a new rule overlaps with a closed accounting period, it generates corrections if you retroactively apply the rules to transactions from past (closed) accounting periods." A backdated cancellation or a late refund does the same. Corrections are the right behavior. The failure is a team that does not expect them and reads each one as a bug, or reopens closed periods by habit.

The fourth is the hand-off itself. An export breaks as any integration does: a field disappears in an upgrade, as in the Version Cliff, or the export covers one provider and the business has two. The control is a monthly comparison of what the recognition ledger says was invoiced and collected with the provider's own balance report. Stripe documents that comparison for its product and warns that the two reports "use different timestamps for payments", so small timing differences at month end are expected and large ones are not.

## What to Take Away

**Established.**

- Under IFRS 15 and ASC 606, issued together in May 2014, revenue is recognized when a performance obligation is satisfied; for a service that is over time. Money received before then is carried as deferred revenue, a liability.
- Payment status does not drive recognition. A schedule is computed from the invoice line's net amount and service period and changed by dated adjustments.
- Stripe documents a recognition ledger in which each invoice line is its own performance obligation, amortized evenly over its period. No Adyen revenue-recognition product was found in public sources as of November 2026; Orb documents its own.

**Depends on context.**

- Recognition in the billing system is right while contracts equal invoices. One bundled line, one negotiated deal or a second provider changes that.
- By the day or by the month is finance's convention. Stripe's default is by the day; €144.99 and €157.50 are both defensible for Ironworks' February if applied consistently.
- Importing another provider's revenue into Stripe's product gives one schedule at the price of files that finance must maintain; it suits a business with one small second source better than one split 44 to 56.

**The author's synthesis.**

- I specify the line-level export first and choose the recognition tool second. With the export, the tool can be replaced; without it, no tool produces a number an auditor accepts.
- I do not let a payments total appear under the word "revenue" on any dashboard. The Larkfield tile was wrong by a factor of thirteen on one customer and nobody had made a mistake.

Collection, tax and recognition turn out to be three readings of one invoice line: by debtor, by place and by period. Recognition is the reading in which time is the whole answer, which is why it needs the two dates a payment report does not carry and why every adjustment needs its own. The three February numbers for Ironworks differ only in the date each keys on: €1,890 billed and collected on 1 February, €144.99 earned by the 28th, €1,745.01 still owed as service. A provider can do this reading only for the lines it holds, so before choosing where recognition runs, write the export and decide with finance whether your contracts equal your invoices.

## Questions to Ask

1. Which of our reports says "revenue", and does it count payments, invoices or delivered service?
2. Does every recurring invoice line carry a service period, and what happens to a line that does not?
3. Is tax a separate amount on every line, or inside the amount we would recognize?
4. Can a refund, dispute or credit note be tied to its original invoice line and dated on its own day?
5. For usage, do we keep the date of use as well as the invoice date?
6. Do our contracts equal our invoices? Which products, bundles or negotiated deals break that?
7. Which of our revenue does the provider's recognition product never see?
8. Who owns the export from billing to finance, is it versioned, and is it tested in every API upgrade?

Chapters 27 to 31 have left the seller with a long list: a billing engine to run, tax to register for and file, disputes to answer, and an export that finance depends on. There is a model that moves part of that list, by changing who sells to the customer. [[merchant-of-record]] examines what moves, what stays, and what it costs in money, control and customer data.

## Sources and Evidence

*Company, product and investor sources*

- [How Revenue Recognition works](https://docs.stripe.com/revenue-recognition/methodology.md), Stripe documentation, n.d., accessed 2026-11 — the double-entry ledger, invoice line as performance obligation, journal entries, the refund example, "revenue contracts" in account descriptions.
- [Revenue Recognition with subscriptions and invoicing](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing.md), Stripe documentation, n.d., accessed 2026-11 — recognition on finalized invoices; the statement that revenue is amortized by the second.
- [Revenue Recognition settings](https://docs.stripe.com/revenue-recognition/revenue-settings.md), Stripe documentation, n.d., accessed 2026-11 — amortization by the day by default.
- [Revenue Recognition accounting period control](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control.md), Stripe documentation, n.d., accessed 2026-11 — closing and reopening periods.
- [Revenue Recognition rules](https://docs.stripe.com/revenue-recognition/rules.md), Stripe documentation, n.d., accessed 2026-11 — one rule per transaction, 24 hours, corrections on closed periods.
- [Revenue Recognition data import](https://docs.stripe.com/revenue-recognition/data-import.md), Stripe documentation, n.d., accessed 2026-11 — CSV imports, external processor data, 3 to 4 hours.
- [Standalone selling prices](https://docs.stripe.com/revenue-recognition/standalone-selling-price.md), Stripe documentation, n.d., accessed 2026-11 — allocation across the components of a bundle; no bundles with rules or imports (page not listed in the documentation index).
- [Revenue Recognition Performance Obligations API](https://docs.stripe.com/revenue-recognition/performance-obligations-api.md), Stripe documentation, n.d., accessed 2026-11 — preview status, recognition on reported fulfillment (volatile).
- [Revenue Recognition data freshness](https://docs.stripe.com/revenue-recognition/data-freshness.md), Stripe documentation, n.d., accessed 2026-11 — report delay, warehouse sync interval.
- [Map to your chart of accounts](https://docs.stripe.com/revenue-recognition/chart-of-accounts.md), Stripe documentation, n.d., accessed 2026-11 — general-ledger account mapping on reports.
- [Revenue Recognition API](https://docs.stripe.com/revenue-recognition/api.md), Stripe documentation, n.d., accessed 2026-11 — report types and the beta note (volatile).
- [Revenue Recognition for Connect platforms](https://docs.stripe.com/revenue-recognition/connect.md) and [for destination charges](https://docs.stripe.com/revenue-recognition/connect/destination-charges.md), Stripe documentation, n.d., accessed 2026-11 — application fees recognized immediately; availability by charge type.
- [Reconcile your Stripe balance with Revenue Recognition](https://docs.stripe.com/revenue-recognition/data-reconciliation.md), Stripe documentation, n.d., accessed 2026-11 — open invoices keep being recognized; timestamp differences.
- [Stripe Connector for NetSuite](https://docs.stripe.com/use-stripe-apps/netsuite/overview.md), Stripe documentation, n.d., accessed 2026-11 — the separate connector for one accounting system.
- [Stripe documentation index](https://docs.stripe.com/llms.txt) and [sitemap](https://docs.stripe.com/sitemap.xml), Stripe, fetched 2026-11-17 — searched for a page on revenue contracts; none found (the index does not list every page).
- [Stripe Revenue Recognition](https://stripe.com/revenue-recognition), Stripe product page, n.d., accessed 2026-11 — the heading "A centralised revenue subledger" (English edition served for the Netherlands; vendor marketing page).
- [Activity breakdown](https://docs.stripe.com/revenue-recognition/reports/activity-breakdown.md), Stripe documentation, n.d., accessed 2026-11 — the report column "Stripe subledger account".
- [Reporting](https://docs.adyen.com/reporting.md), Adyen documentation, n.d., accessed 2026-11 — what Adyen's reports describe.
- [Settlement details report](https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report.md), Adyen documentation, n.d., accessed 2026-11 — contents of the settlement report.
- [Closing your fiscal period](https://docs.adyen.com/reporting/closing-your-fiscal-period.md), Adyen documentation, n.d., accessed 2026-11 — the period close works from payment balances in the finance reports.
- [Adyen documentation index](https://docs.adyen.com/llms.txt), Adyen, fetched 2026-11-17 — about 2,600 entries, searched for revenue recognition, deferred, billing, revenue and Orb; none found.
- [Adyen documentation, full text](https://docs.adyen.com/llms-full.txt), Adyen, fetched 2026-11-17 — no occurrence of "revenue recognition"; names Orb only as a partner integration link.
- [Adyen help center sitemap](https://help.adyen.com/sitemap.xml), Adyen, fetched 2026-11-17 — searched article addresses for revenue recognition, deferred, billing and Orb; only articles on Adyen's own invoices to merchants.
- [Orb](https://www.adyen.com/partners/orb), Adyen partner page, n.d., accessed 2026-11 — Adyen's description of Orb's reporting for revenue recognition.
- [Usage-based billing, explained](https://www.adyen.com/knowledge-hub/usage-based-billing), Adyen, 2026-10-22 — revenue recognition named as a concern of usage-based billing.
- [Adyen Closes Talon.One and Orb Acquisitions; Announces Leadership Updates Across Product and Finance](https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates), Adyen, 2026-07-01 — closing date.
- [Why billing and payments belong together](https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb), Blake Breathitt, Adyen, 2026-09-29 — integration stated as future.
- [Recognition methodology](https://docs.withorb.com/revenue-reporting/revenue-recognition.md), Orb documentation, n.d., accessed 2026-11 — Orb's recognition principles, usage timing, payment status, period locks (describes Orb's product, not Adyen's platform).
- [Payments](https://docs.withorb.com/invoicing/payments.md), Orb documentation, n.d., accessed 2026-11 — Orb collects through payment gateways "like Adyen and Stripe".
- [Adyen](https://docs.withorb.com/integrations-and-exports/adyen.md), Orb documentation, n.d., accessed 2026-11 — connecting an Adyen merchant account to Orb as a payment gateway.

*Standards, regulation and official documentation*

- [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), IFRS Foundation, n.d., accessed 2026-11 — joint issue with Topic 606 in May 2014, effective date, the five steps, point in time and over time (the standard is 12 years old and in force).
- [IASB and FASB Issue Converged Standard on Revenue Recognition](http://web.archive.org/web/20210924180526/https://www.fasb.org/jsp/FASB/FASBContent_C/NewsPage&cid=1176164075286), Financial Accounting Standards Board, 2014-05-28, archived copy of 2021-09-24 — the joint issue and Topic 606 in the FASB's own words (evidence age: 12 years; fasb.org returned 403 to automated requests on 2026-11-17, and the text of ASC 606 was not read).
- [IASB and FASB issue converged Standard on Revenue Recognition](https://www.ifrs.org/news-and-events/news/2014/05/iasb-and-fasb-issue-converged-standard-on-revenue-recognition/), IFRS Foundation, 2014-05-28 — the same joint release on the IASB's side (evidence age: 12 years).

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
