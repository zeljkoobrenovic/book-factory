# Verification — 27-subscriptions-and-billing-engines (`subscriptions-and-billing-engines`)

Verification pass of 17 November 2026. Every source below was fetched in this session (all returned HTTP 200) and the passage read. Quotations were compared with the fetched text after normalizing typographic quotes and markdown markers. Documentation pages are cited "n.d., accessed November 2026" (ruling 30).

**Counts:** 58 claims listed; 48 confirmed, 8 corrected, 0 hedged, 0 unsupported, 0 unreachable, 2 not checked.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | "When you create a subscription, Stripe automatically generates invoices, attempts payment collection, and manages the subscription status throughout its lifecycle" | https://docs.stripe.com/billing/subscriptions/overview.md | confirmed | Inline link removed (ruling 22) |
| 2 | "Products define what your business offers"; "Prices define how much and how often to charge for products" | https://docs.stripe.com/products-prices/how-products-and-prices-work.md | confirmed | Inline link removed |
| 3 | "Stripe generates an invoice for every subscription billing period" | https://docs.stripe.com/billing/invoices/subscription.md | confirmed | Inline link removed |
| 4 | Invoices are "statements of amounts owed by a customer" | https://docs.stripe.com/billing/invoices/subscription.md | confirmed | Cell had no attribution; "(same page)" added. The phrase is not on the overview page |
| 5 | InvoicePayment: "the mapping between payment objects, such as Payment Intent, and Invoices" | https://docs.stripe.com/api/invoice-payment.md | confirmed | Inline link removed |
| 6 | A PaymentIntent is created with the invoice | https://docs.stripe.com/billing/subscriptions/overview.md | confirmed | Cell reworded to what the page says ("When you create a subscription that requires an immediate payment, Stripe also creates an Invoice and a PaymentIntent") and attributed |
| 7 | Month-end rule: anchor of January 31 bills February 28 (29), March 31, April 30 | https://docs.stripe.com/billing/subscriptions/billing-cycle.md | confirmed | — |
| 8 | "Billing cycle anchors are UNIX timestamps in seconds from the current epoch" | same | confirmed | — |
| 9 | "The billing cycle anchor uses Coordinated Universal Time (UTC)" | same | confirmed | Inline link removed |
| 10 | "By default, Stripe calculates prorations down to the second." | https://docs.stripe.com/billing/subscriptions/prorations.md | confirmed | — |
| 11 | "Negative prorations aren’t automatically refunded and positive prorations aren’t immediately billed, although you can do both manually." | same | confirmed | — |
| 12 | 10 to 20 USD upgrade halfway: 5 USD credit, 10 USD debit | same | confirmed | Table on the page: -5 USD, +10 USD, total +5 USD |
| 13 | `proration_behavior`: create prorations, invoice at once, none | same | confirmed | `create_prorations` (default), `always_invoice`, `none`. Inline link removed |
| 14 | Two billing modes; flexible recommended; classic "maintained for backward compatibility with older integrations" | https://docs.stripe.com/billing/subscriptions/billing-mode.md | confirmed | — |
| 15 | "For API version `2025-09-30.clover` and later, the default is `flexible`. For earlier versions, the default is `classic`." | same | confirmed | — |
| 16 | "You can’t migrate a subscription from flexible billing mode to classic billing mode" | same | confirmed | Inline link removed |
| 17 | April 11 / April 21 scenario: classic credits "a third of the month for 20 USD (-6.67 USD), even though the customer never paid for" it; flexible credits 3.33 USD, total 0 USD | https://docs.stripe.com/billing/subscriptions/prorations.md | corrected | Content confirmed; the sentence followed a billing-mode citation, but the scenario is on the prorations page. Now reads "In the scenario on Stripe's prorations page" |
| 18 | Eight subscription statuses | https://docs.stripe.com/billing/subscriptions/overview.md | confirmed | incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, paused |
| 19 | "`active` doesn’t necessarily indicate that all outstanding invoices associated with the subscription have been paid." | same | confirmed | — |
| 20 | Failed payment settings "determine whether the subscription remains `past_due` or changes to `unpaid` or `canceled`" | same | confirmed | — |
| 21 | Status table, eight rows (23 hours; "so you can track customers that failed to activate"; "The subscription is in good standing"; `past_due` quotes; `unpaid` only by settings, invoices generated, payment not attempted; "This is a terminal state that can’t be updated"; `paused`) | same; https://docs.stripe.com/billing/subscriptions/pause.md for the second cause of `paused` | confirmed | — |
| 22 | Pausing payment collection: subscription stays `active`, invoices keep being generated, not collected | https://docs.stripe.com/billing/subscriptions/pause-payment.md | confirmed | Inline link removed |
| 23 | Pausing the subscription: status `paused`; "Stripe pauses invoice generation until you resume the subscription"; requires flexible billing mode | https://docs.stripe.com/billing/subscriptions/pause.md | confirmed | Inline link removed |
| 24 | Subscription schedules hold "up to ten phases" | https://docs.stripe.com/billing/subscriptions/subscription-schedules.md | corrected | Page: "You can only define up to 10 current or future phases at a time on a subscription schedule. Past phases don’t count against this limit." Now "up to ten current or future phases" (article, spec p24, source entry) |
| 25 | "Phase transitions happen automatically after the `end_date` on a phase is reached" | same | confirmed | Inline link removed; "n.d., accessed November 2026" added |
| 26 | At renewal Stripe "Leaves the invoice in a `draft` status for about an hour" | https://docs.stripe.com/billing/invoices/subscription.md | corrected | Quotation confirmed, but the page attributed it to workflow-transitions, where it does not appear. Attributed to the subscription invoices page |
| 27 | "We wait 1 hour after receiving a successful response to the `invoice.created` event … within 72 hours, we attempt to finalize and send the invoice" | https://docs.stripe.com/invoicing/integration/workflow-transitions.md | confirmed | Inline link removed |
| 28 | 2017 post: "Stripe has hundreds of millions of Subscriptions objects" (evidence age 9 years) | https://stripe.com/blog/online-migrations | confirmed | Dated February 2, 2017; Jacqueline Xu |
| 29 | Two 2025 Stripe engineering posts cover usage metering and analytics | https://stripe.com/blog/how-we-built-it-usage-based-billing (January 28, 2025); https://stripe.dev/blog/how-we-built-it-real-time-analytics-for-stripe-billing (2025.9.16) | confirmed | Both were cited in the text without a source entry; two entries added |
| 30 | "Stripe's engineering posts touch Billing three times … None describes how renewals are scheduled, partitioned or kept from running twice." | https://stripe.dev/blog/test-clocks-how-we-made-it-easier-to-test-stripe-billing-integrations (Ji Huang, 2024.5.09) | corrected | **Wrong.** A fourth post exists and it describes the scheduler: "we used a scheduling service that looks for database records meeting certain criteria, and which triggers certain events when it finds them"; a Subscription "gets picked up by a part of the scheduling service that looks for Subscriptions whose billing periods have just ended, and triggers the creation of a new Invoice"; "database scans done by the asynchronous scheduling service". The paragraph now quotes that passage and narrows the gap to what is still unpublished: how the scan is partitioned, paced or kept from creating two invoices. The count "three times" is replaced by "the other … posts found for this book". Source entry added |
| 31 | Adyen: "**Subscription** (`Subscription`): A payment where you initiate a subscription payment to bill the shopper at regular intervals." | https://docs.adyen.com/online-payments/tokenization/make-token-payments.md | confirmed | — |
| 32 | The other two models (one-click `CardOnFile`, `UnscheduledCardOnFile` at non-fixed intervals); merchant-started payments carry `ContAuth` | same | confirmed | Subscription request examples set `shopperInteraction: ContAuth` |
| 33 | That page is "last modified July 2023", "Evidence age: 3 years" | same (front matter `last_modified: 2023-07-28`) | corrected | Ruling 30: `.md` front-matter stamps are not used as dates. Now "n.d., accessed November 2026"; evidence-age flag removed from the text, the table cell, the source entry and spec p26 |
| 34 | Adyen's tokenization overview describes the same three types | https://docs.adyen.com/online-payments/tokenization.md | confirmed | One-click payments, Subscriptions ("recurring transactions you initiate at regular intervals"), automatic top-ups and other non-fixed schedule contracts |
| 35 | The Adyen documentation describes no plan, price, subscription object, billing cycle, proration or invoice | https://docs.adyen.com/llms.txt (2,697 lines searched for subscription, invoice, billing, prorat, recurring, dunning, orb) | confirmed (absence) | The only "invoice" pages are Adyen's own invoices to merchants and Klarna invoice lines; "subscriptions" appears only for webhook subscriptions. The page already labels this an inference from absence |
| 36 | Auto Rescue: "provide a unique `merchantOrderReference`. This should represent a specific billing cycle or subscription" | https://docs.adyen.com/online-payments/auto-rescue/cards.md | confirmed | Inline link removed |
| 37 | Orb "integrates with payment gateways like Adyen and Stripe for payment processing" | https://docs.withorb.com/invoicing/payments.md | confirmed | Inline link removed |
| 38 | Adyen (knowledge hub, 2026): seat and month billing "is well-served today, including by partners we work with closely" | https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb | confirmed | Displayed date "September 29th, 2026" (rulings 21, 25). Sentence now gives the date; the source entry no longer carries the metadata "modified" date. The sentence "We completed our acquisition of Orb on 1 July." is not on the page (it reads "On July 1st, we acquired Orb") and is not quoted anywhere in the article |
| 39 | Orb acquisition announced 11 June 2026; "The total consideration for the transaction is $335 million" | https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj | confirmed | Inline link removed |
| 40 | Deal "officially closed on July 1, 2026" | https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates | confirmed | Inline link removed |
| 41 | "Adyen is adopting an incubator model, preserving Orb’s operational continuity during the first phase of the acquisition and continuing to support multi-PSP environments" | https://www.adyen.com/press-and-media/jtrg4qd7j3p4rj | confirmed | Now attributed to "the June release" |
| 42 | "Beyond this first phase, the strategic intent is convergence" | same | confirmed | — |
| 43 | "You'll soon see how we bring this unified Adyen and Orb experience to life across our platform." | https://www.adyen.com/knowledge-hub/why-adyen-acquired-orb | confirmed | — |
| 44 | As of 17 November 2026 no Adyen page describes a billing product integrated into its platform | https://docs.adyen.com/llms.txt; https://www.adyen.com/sitemap-en.xml; https://www.adyen.com/partners/orb; https://www.adyen.com/knowledge-hub/talon-one-orb-acquisitions; https://www.adyen.com/knowledge-hub/usage-based-billing; https://www.adyen.com/industries/use-cases/subscriptions | confirmed (absence) | No "Orb" entry in the documentation index. The sitemap lists four Orb or billing pages; none documents an integrated product (the completion article says "we are beginning the integration"). These pages are not cited in the article |
| 45 | "Like Stripe, Adyen has published no design of a renewal scheduler" | as #30 | corrected | Now: "Stripe has published one passage about its renewal scheduler; Adyen documents no first-party scheduler at all." |
| 46 | October 2024: "the ability to manage subscriptions with Stripe while processing transactions with other payments providers" | https://stripe.com/blog/our-biggest-ever-upgrades-to-stripe-billing | confirmed | Dated October 29, 2024, Wisam Hirzalla. Current availability still not re-checked; the page says so |
| 47 | Stripe completed the Metronome acquisition on 14 January 2026 | https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition | confirmed | The request was redirected to the Dutch edition (/nl/), dated "14 januari 2026"; the English URL is kept |
| 48 | Metronome is "Stripe’s primary usage-based billing platform" | https://docs.stripe.com/billing/subscriptions/usage-based.md | confirmed | Inline link removed |
| 49 | Chargebee, Recurly, Zuora and Orb are dedicated billing systems | https://www.chargebee.com/docs/billing/2.0/subscriptions/proration; https://docs.withorb.com/invoicing/payments.md; https://recurly.com/; https://www.zuora.com/ | confirmed | Recurly and Zuora checked on their home pages only (page titles: "Grow, retain, and recover subscription revenue", "The Leading Quote to Cash & Subscription Management Platform"); they are named without characterization and have no source entry |
| 50 | Chargebee: "There are two proration modes: day-based and millisecond-based", a site-wide setting | https://www.chargebee.com/docs/billing/2.0/subscriptions/proration | confirmed | Inline link removed |
| 51 | "I could not fetch Zuora's documentation" | — | not checked | The writer's statement about their own fetch; Zuora's documentation was not tried again in this pass |
| 52 | Where They Differ, row 1 (eight statuses; no subscription object, `Subscription` as a processing model) | as #18, #31, #35 | confirmed | Adyen cell's date changed to "n.d., accessed November 2026" (ruling 30) |
| 53 | Where They Differ, rows 2 to 4 (schedule and amount; who holds the invoice; company bought in 2026) | as #7–#16, #3, #36, #39–#41, #47, #48 | confirmed | Source kinds and years added to the row 4 cells |
| 54 | Where They Differ, row 5: Stripe scheduler design "Not public; only observable timing is documented" | as #30 | corrected | "Not public" was not true. Cell now states the documented fact (engineering post, 2024) and keeps "Not public" for partitioning, pacing and duplicate protection. Adyen cell unchanged (index searched, #35) |
| 55 | "we won’t attempt to charge the customer unless we receive a successful response", for up to 72 hours | https://docs.stripe.com/invoicing/integration/workflow-transitions.md | confirmed | Page: webhook retried "for up to 3 days" in live mode. Inline link removed |
| 56 | "Upgrading your API version to `2025-09-30.clover` or later changes the default billing mode for new subscriptions from `classic` to `flexible`. Flexible billing mode changes how subscriptions calculate prorations, handle trials, and process cancellations." | https://docs.stripe.com/billing/subscriptions/billing-mode.md | confirmed | Attribution and "n.d., accessed November 2026" added to the sentence |
| 57 | Take-away "Neither company has published the design of a renewal scheduler"; Larkfield table cell "Stripe's scheduler; design not public" | as #30 | corrected | Bullet rewritten to the narrower claim; cell now "its pacing is not public" |
| 58 | Card networks call a stored-credential charge with the customer absent a "merchant-initiated transaction" | — | not checked | No network document is cited on this page; the term is owned by `payment-authorization` and linked there |

Also checked by arithmetic, not from a source: 1 April 2027 00:00 UTC is 02:00 in Utrecht (summer time from 28 March 2027) and 20:00 on 31 March in New York; 365 / 30 = 12.17.

## Could not verify, and what was done

- **Current availability of Stripe Billing with third-party processors** (#46): not re-checked; the sentence and the source entry already say so.
- **Zuora documentation** (#51): not fetched; the page does not characterize Zuora.
- **"Merchant-initiated transaction" as a network term** (#58): not checked here; defined and sourced in chapter 2.
- **Completeness of the list of Stripe engineering posts on Billing** (#30): the stripe.dev engineering index was read and showed two Billing posts (2024 and 2025); the stripe.com posts are from the research brief. The text now says "found for this book" instead of giving a count.

## Rulings and format

- Ruling 20: "members were turned away on a Sunday morning" changed to "the Silent Webhook of Monday 14 September 2026 … turned away at check-in that Monday morning" (article and spec p-level evidence).
- Ruling 21: the knowledge-hub article is cited as 29 September 2026; the sentence that is not on the page is not quoted. The spec's open-question note now refers to the displayed date.
- Ruling 22: every inline external link reduced to attributions in the sentence; every URL is in Sources and Evidence.
- Ruling 30: no "last modified" date left in the article or the spec.
- Sources: three entries added (test clocks post 2024-05-09; usage-based billing post 2025-01-28; real-time analytics post 2025-09-16). No entry is unused. All 25 source URLs return 200.
- "Keel" is now glossed at its first use (the Larkfield scene) instead of its third.
- `timetoread`: 5,819 words / 230 = 25 min; unchanged.
- No unit added, dropped, merged or reordered. `validate_spec.py` and `check_draft.py structure` pass; build and render check pass.

## Larkfield consistency

All figures, names, dates and decisions agree with the ledger (business lines, incidents, K1, K2, K5, Mila's renewal, the chapter's own ledger line and the lines of chapters 2, 19, 29, 40 and 43). Weekdays: the only weekday named is Monday 14 September 2026, which is correct. The only contradiction was the Silent Webhook's "Sunday morning", fixed.

## Ledger conflicts

None found.

## For other pages

- `journal-spec.json`, entry for this chapter, `thesis.how_why`: "no Stripe or Adyen publication describes how renewals are scheduled, partitioned or kept from running twice" is no longer accurate (#30). The post spec must repeat that field word for word, so it was left unchanged in `spec.json`; supporting claim S3 and paragraphs p25 and p29 were updated. The author should change the journal spec and then the post spec's `how_why` to "…describes how renewals are partitioned, paced or kept from running twice".
- `_research/brief-billing-and-revenue.md` (sections 1.7 and 1.8) omits the 2024 test clocks engineering post. Chapters that draw on it for Stripe's scheduler (29, 40, 43, 46) should not say that nothing is public about it. A search of the current pages found no other page that makes the claim.
