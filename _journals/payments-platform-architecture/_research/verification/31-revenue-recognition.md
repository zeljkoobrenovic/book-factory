# Verification — 31-revenue-recognition (`billing-revenue-recognition`)

Verification pass of 17 November 2026. Every source below was fetched in this session (curl, `.md` variants for Stripe, Adyen and Orb documentation). Quotations were compared with the fetched text by script after normalizing typographic quotes, whitespace and markdown emphasis.

Totals: 58 claims checked — 45 confirmed, 7 corrected, 5 hedged, 0 unsupported, 1 unreachable.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe RR treats "each invoice line item as its own performance obligation" (key points, section, table) | https://docs.stripe.com/revenue-recognition/methodology.md | confirmed | — |
| 2 | Adyen has owned Orb since 1 July 2026; acquisitions "officially closed on July 1, 2026" | https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates | confirmed | Page shows "July 1st, 2026"; quote matches |
| 3 | IFRS Foundation: "In May 2014 the Board issued IFRS 15 … together with the introduction of Topic 606 …" | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ | confirmed | — |
| 4 | IFRS and ASC "share one rule"; ASC 606 cited only through the IFRS page | FASB release (archived): http://web.archive.org/web/20210924180526/https://www.fasb.org/jsp/FASB/FASBContent_C/NewsPage&cid=1176164075286 ; IASB copy: https://www.ifrs.org/news-and-events/news/2014/05/iasb-and-fasb-issue-converged-standard-on-revenue-recognition/ | hedged | "share one rule" became "took their revenue rule from one joint project"; the boards' joint release of 28 May 2014 is now quoted ("today issued jointly a converged standard …", "as Topic 606") with an evidence-age mark (12 years); both copies added to Sources |
| 5 | "effective from 2018" (attached to both standards) | IFRS 15 page | corrected | Now: IFRS 15 applies to annual periods beginning on or after 1 January 2018 (the page's words). No effective date is stated for ASC 606 (the 2014 release gives the original dates, later deferred; not used) |
| 6 | Text of ASC 606 in the FASB codification | https://www.fasb.org/…, https://asc.fasb.org/606/… | unreachable | 403 (Cloudflare) on six fasb.org URLs by curl and WebFetch. Used the FASB's own news release in an Internet Archive copy (captured 2021-09-24) and the identical IASB release on ifrs.org. The page says the codification text was not read |
| 7 | Step 1 "identify the contract(s) with a customer" | IFRS 15 page | confirmed | — |
| 8 | Step 2 "identify the performance obligations in the contract" | IFRS 15 page | confirmed | — |
| 9 | Step 3 "determine the transaction price" (gloss: what the seller expects to receive) | IFRS 15 page | confirmed | Page: "amount of consideration to which an entity expects to be entitled" |
| 10 | Step 4 "allocate the transaction price to each performance obligation" (gloss: by what each would sell for alone) | IFRS 15 page | confirmed | Page: "on the basis of the relative stand-alone selling prices" |
| 11 | Step 5 "recognise revenue when a performance obligation is satisfied" | IFRS 15 page | confirmed | — |
| 12 | Performance obligations are "promises in a contract to transfer … goods or services that are distinct", "in the standard's words" | IFRS 15 page | hedged | Quote confirmed, but it is the IFRS Foundation's summary page, not the standard's text: attribution changed to "in the IFRS Foundation's summary of the standard" |
| 13 | "may be satisfied at a point in time (…) or over time (…)" | IFRS 15 page | confirmed | — |
| 14 | Deferred revenue is a liability | https://docs.stripe.com/revenue-recognition/methodology.md ("Deferred revenue is a liability on your balance sheet") | confirmed | — |
| 15 | Established bullet: under IFRS 15 and ASC 606 "money received before then is a liability" | IFRS 15 page (does not say this) | hedged | Neither fetched standard-setter page uses "liability"; the sentence was split so the liability statement is no longer attributed to the standards |
| 16 | Stripe journal entries quote (finalize: debit AccountsReceivable, credit DeferredRevenue; pay: debit Cash, credit AccountsReceivable) | methodology.md | confirmed | — |
| 17 | Orb: "the payment status of an individual invoice is not factored into accounting treatment." | https://docs.withorb.com/revenue-reporting/revenue-recognition.md | confirmed | — |
| 18 | Tax is not revenue (inputs and export tables) | methodology.md ("recognizable portion is only 90 USD"); Orb ("revenue numbers always exclude tax") | confirmed | — |
| 19 | Missing service period: whole amount recognized on one day (Stripe default) | methodology.md | confirmed | — |
| 20 | Stripe refund example (120 USD refund, 20 USD contra revenue, 100 USD deferred) | methodology.md | confirmed | — |
| 21 | Orb: usage "requires understanding exactly when usage occurs. This can be particularly difficult …" | Orb recognition page | confirmed | — |
| 22 | Orb: "Revenue is recognized for usage as it occurs on a daily basis, regardless of the associated line item’s service period." | Orb recognition page | confirmed | — |
| 23 | Stripe accounting periods close automatically or by hand; reopen to "make adjustments to past data without creating corrections in the current period" | https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control.md | confirmed | — |
| 24 | Orb: "Closing an accounting period ensures that there will be no subsequent changes to that period" | Orb recognition page | confirmed | — |
| 25 | "Stripe built Revenue Recognition on top of a double-entry accounting ledger …"; "automatically calculates all transactions that happen within Stripe" | methodology.md | confirmed | — |
| 26 | "… When the invoice finalizes, Revenue Recognition defers the total recognizable amount and subsequently amortizes it evenly …" | methodology.md | confirmed | — |
| 27 | "By default, Stripe Revenue Recognition recognizes revenue by the day"; by-second and by-month settings | https://docs.stripe.com/revenue-recognition/revenue-settings.md | hedged | Confirmed on the settings page, but the subscriptions-and-invoicing page says "Revenue recognition amortizes revenue by the second, but our example uses a daily interval". The discrepancy is now stated in the text and the table cell says "according to its settings page" |
| 28 | "If you don’t set a period on an invoice line item, … recognizes the full amount … when the invoice is finalized." | methodology.md | confirmed | Source entry for subscriptions-and-invoicing re-described (the quote is on the methodology page) |
| 29 | Payment without invoice: "By default, Revenue Recognition recognizes these payments immediately when the payment occurs." | methodology.md | confirmed | — |
| 30 | Connect destination charge: fee "is immediately recognized as the revenue" | https://docs.stripe.com/revenue-recognition/connect/destination-charges.md | confirmed | "the platform's cut" reworded to "the platform's fee" and "destination charge" glossed |
| 31 | Destination charges available to all users; other charge types on request | https://docs.stripe.com/revenue-recognition/connect.md | confirmed | — |
| 32 | Rules: "Each transaction can only have one rule applied to it"; "Rules are typically applied to reports within 24 hours."; amortize over a custom period | https://docs.stripe.com/revenue-recognition/rules.md | confirmed | — |
| 33 | Imports: add or override a period, split a payment, "an external payment processor’s data with a service period, amount, and currency"; reports "take approximately 3-4 hours to update after you upload data" | https://docs.stripe.com/revenue-recognition/data-import.md | confirmed | — |
| 34 | Performance Obligations API in preview, access on request, recognizes on reported fulfillment | https://docs.stripe.com/revenue-recognition/performance-obligations-api.md | confirmed | Page still says "Request to join the preview" |
| 35 | "Stripe documents three ways past these defaults" | https://docs.stripe.com/revenue-recognition/standalone-selling-price.md | corrected | A fourth documented mechanism exists (standalone selling prices for bundles). Text now says four and describes it; spec p18 updated |
| 36 | Stripe's pages "do not describe allocating one price across several promises by what each would sell for alone" | https://docs.stripe.com/revenue-recognition/standalone-selling-price.md | corrected | Wrong as written: "The standalone selling price (SSP) feature helps businesses allocate revenue across products sold as a bundle." The page is linked from the activity-logs page and is not in `llms.txt`. Text now says allocation is documented for a product set up as a bundle, and that nothing was found on a contract spanning several lines or invoices; spec p20 updated; the "options" sentence in the third design names bundles |
| 37 | Stripe's pages do not describe estimating a price that varies | 38 Revenue Recognition pages fetched (all listed in llms.txt plus linked ones) | confirmed | Absence: no "variable consideration" on any page; "estimates" appears only for unbilled usage |
| 38 | "This is only used when working with revenue contracts" (two account descriptions); no page explains revenue contracts | methodology.md; https://docs.stripe.com/llms.txt; 38 pages | confirmed | Scope of the search stated more exactly (index and pages read); the text now notes the index is incomplete. Four guessed URLs (`/revenue-contracts`, `/contracts`, …) return 404 |
| 39 | New activity "appears within approximately 3-4 hours after transaction completion"; warehouse sync "once every 6 hours" | https://docs.stripe.com/revenue-recognition/data-freshness.md | confirmed | — |
| 40 | Mapping to the business's general-ledger account names and numbers | https://docs.stripe.com/revenue-recognition/chart-of-accounts.md | confirmed | — |
| 41 | Report API: "Because this feature is in beta, the data fields might change." | https://docs.stripe.com/revenue-recognition/api.md | confirmed | — |
| 42 | Inference block: "a separate connector for one accounting system" | https://docs.stripe.com/use-stripe-apps/netsuite/overview.md | confirmed | Fact had no source entry; NetSuite named in the text and the page added to Sources |
| 43 | Adyen: "Adyen reports show you information about your transactions" | https://docs.adyen.com/reporting.md | confirmed | — |
| 44 | Settlement details report "includes the details of payments that have been settled and paid out to you by Adyen" | https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report.md | confirmed | — |
| 45 | "(page last modified in October 2022; evidence age: 4 years)" and "settlement report page 2022" in the table | same | corrected | Ruling 30: "last modified" stamps are not dates. Removed from text, table and source entry; cited "n.d., accessed 2026-11" |
| 46 | Adyen documentation index "lists about 2,700 pages" | https://docs.adyen.com/llms.txt | corrected | The file has 2,573 entries (2,697 lines): now "about 2,600" |
| 47 | None of them has "revenue recognition", "deferred" or "billing" in title or description | https://docs.adyen.com/llms.txt | confirmed | Re-searched: 0 matches for revenue recognition, recogni, deferred, defer, accrual, billing, revenue, Orb, ASC 606, IFRS, usage-based, metering. "Invoice" matches 8 pages, all about Adyen's invoices to merchants or Klarna invoice lines; "Closing your fiscal period" works from payment balances (one sentence and a source added). "Orb" added to the terms named in the text |
| 48 | Adyen help center: no revenue-recognition article (new check asked for in this pass) | https://help.adyen.com/sitemap.xml | confirmed | 9,472 addresses, 978 English: none for revenue recognition, defer, Orb, subscription, accrual; two with "billing" (`what-is-adyens-billing-structure`, `how-can-i-activate-merchant-billing`) both redirect to documentation pages on Adyen's own invoices. The help-center search URL itself returns 404 to curl, so the sitemap was used. Sentence and source added |
| 49 | adyen.com: no revenue-recognition product (new check) | https://www.adyen.com/sitemap-en.xml (1,892 addresses); https://www.adyen.com/partners/orb; https://www.adyen.com/knowledge-hub/usage-based-billing | hedged | No product page found. Adyen's site does mention revenue recognition twice: the Orb partner page ("finance teams get fine-grained reporting to facilitate revenue recognition") and "Usage-based billing, explained" (displayed date October 22nd, 2026). Both now cited, so "none found" is scoped to a product and its documentation |
| 50 | Orb: "Orb automatically calculates recognized revenue in a way that accords with ASC606 guidelines" | Orb recognition page | confirmed | — |
| 51 | Orb: "the lineage of revenue from a summary entry → invoice → raw product usage data" | Orb recognition page | confirmed | — |
| 52 | Orb's product "bills on several payment providers" | https://docs.withorb.com/invoicing/payments.md; https://docs.withorb.com/integrations-and-exports/adyen.md | corrected | No source in the page supported it. Orb's documentation says "Orb integrates with payment gateways like Adyen and Stripe for payment processing" and has a page on connecting an Adyen merchant account. Sentence rewritten with the quote; both pages added to Sources |
| 53 | Adyen article of 29 September 2026: "You'll soon see how we bring this unified Adyen and Orb experience to life across our platform." | https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb | confirmed | Rulings 21 and 25: displayed date is "September 29th, 2026", byline Blake Breathitt; the sentence "We completed our acquisition of Orb on 1 July." is not on the page and is not quoted in the chapter |
| 54 | "As of November 2026 I found no Adyen documentation of an integrated product" | docs.adyen.com/llms.txt; Orb Adyen page | corrected | Narrowed: Orb documents collecting through Adyen as a gateway (Orb's documentation, not Adyen's); the sentence now reads "no Adyen documentation of a revenue-recognition product or of Orb's reporting as part of Adyen's platform" |
| 55 | Table, Adyen cells ("Not public" ×3; reports cell) | rows 43–49 above | confirmed | Row 1 cell now names the help center as well; row 4 cell lost the 2022 date. "Not public" holds for a first-party recognition product, the source of a schedule and imports, after the searches in rows 47–49 |
| 56 | Stripe reconciliation guide: open invoices "continue to be recognized as revenue in the Revenue Recognition report"; advises `uncollectible` or `void` | https://docs.stripe.com/revenue-recognition/data-reconciliation.md | confirmed | — |
| 57 | Rules page: "If the effective period for a new rule overlaps with a closed accounting period, it generates corrections …" | rules.md | confirmed | — |
| 58 | The two reports "use different timestamps for payments" | data-reconciliation.md | confirmed | — |

## Could not verify, and what I did

- **ASC 606 itself.** fasb.org and asc.fasb.org return 403 to automated requests. The joint issue and "Topic 606" are now quoted from the FASB's own news release of 28 May 2014 in an Internet Archive copy, with the IASB's live copy of the same release beside it. The chapter says the codification text was not read. The five steps and the definitions are quoted from the IFRS Foundation's summary page, not from the paragraphs of IFRS 15; the attribution says so.
- **Absences are absences.** "None found" for Adyen rests on the documentation index, the help-center sitemap and the English sitemap of adyen.com, all fetched on 17 November 2026. A sitemap can be incomplete (Stripe's index is: the standalone-selling-price page is missing from it), and the help center's own search could not be run by script.
- **Stripe "revenue contracts".** Still unexplained in public documentation; left as the chapter states it.

## Rulings and format

- Ruling 21: applied (date 29 September 2026; forbidden sentence absent). Ruling 25: displayed dates used (1 July 2026, 29 September 2026, 22 October 2026). Ruling 30: one violation fixed (row 45). Ruling 22: no external URLs in the running text.
- All 31 URLs in Sources and Evidence return 200 with no redirect. All `[[permalinks]]` are in the valid list.
- Sources: 9 entries added (standalone selling prices, NetSuite connector, closing your fiscal period, help-center sitemap, Orb partner page, usage-based billing article, Orb payments page, Orb Adyen page, the two copies of the 2014 release); none removed; every entry is used in the text.
- "Dunning" and "destination charge" were used without a definition in this page; one clause added to each.
- `timetoread` changed from 21 to 23 (5,333 words ÷ 230).
- Units: none added, dropped, merged or reordered. Spec changed in wording only: p08, p09, p16, p18, p20, p21, p22 evidence and controlling ideas, two open questions, one sources entry, changelog.

## Larkfield consistency

All figures agree with the ledger: €1,890 on 1 February 2027; 28, 59, 334 and 365 days giving €144.99, €305.51 / €1,584.49, €1,729.48 / €160.52; €5.18 a day; by-month €157.50, €315.00, €1,575.00; the hypothetical dispute on 1 August 2027 (181 days: €937.23 and €952.77); SMS 1,000 × €0.07; €24.5M and €19.8M; 44% and 56%; the Version Cliff (March 2026, six days); K7; May 2027 hand-over; Mila's €120.00, €2.53, €84.00; 9 March 2027 is a Tuesday. Stripe studios are described with destination charges (ruling 23).

## Ledger conflicts

None.

## For other pages

- `27-subscriptions-and-billing-engines` and `29-invoicing-collections-and-dunning` (ruling 6, "Adyen holds payments and no invoice"): Orb's documentation now has a page "Adyen" (`docs.withorb.com/integrations-and-exports/adyen.md`, n.d., accessed November 2026) describing Adyen as a payment gateway for Orb invoices, with auto-collection and an Adyen Drop-in in Orb's invoice portal. Any sentence saying no connection between Orb and Adyen is documented should be checked against it. The invoice is still held by Orb, not by Adyen's platform.
- Any page that reasons from `docs.stripe.com/llms.txt` to "Stripe documents no page on X": the index is not complete (the standalone-selling-price page is absent).
- `_research/brief-billing-and-revenue.md`: does not mention Stripe's standalone selling prices.

## For the author

- The trade-off table still lists "Bundles on one line" under what recognition in the billing system gets wrong. As a statement about the design in general it stands; on Stripe a bundle on one line can now be configured (row 36). I left the cell and the "Depends on context" bullet as they are because changing them touches the argument.
- Ironworks Climbing is a Manchester company billed in euros, and the €1,890 is taken as net of tax (labeled assumption). Both come from the ledger; I did not change them.
