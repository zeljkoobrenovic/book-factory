# Verification — 28-usage-metering-and-rating (`usage-metering-and-rating`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Orb documentation as `.md` variants, with the HTML URLs checked separately for status 200; Stripe's blog and newsroom and the three Adyen pages as HTML). All 78 double-quoted strings in the article were matched mechanically against the fetched texts (typographic quotes, markdown and whitespace normalized) and the load-bearing ones were then read in context. Short URLs: S = `https://docs.stripe.com`, O = `https://docs.withorb.com`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe meters accept events up to 35 days old (key point 1, body, take-away) | S/billing/subscriptions/usage-based/recording-usage-api | confirmed | — |
| 2 | Grace period "of 1 to 72 hours" (key point 1; Where They Differ, Time rules) | S/billing/subscriptions/usage-based/configure-grace-period | corrected | Source: default 1 hour, "up to 72 hours", and the default can be changed for "more or less time"; 1 hour is not a minimum. Both places now say one hour by default and at most 72. The table cell also said "finalization plus 1 to 72 hours"; it now says the invoice is finalized one hour after its creation by default |
| 3 | Identifier uniqueness "at least 24 hours" (key point 2, body, table, take-away) | S/api/billing/meter-event/create | confirmed | — |
| 4 | Stripe's post is from 2025; Orb documents the query design about itself (key point 3, lead) | stripe.com/blog/how-we-built-it-usage-based-billing; O/architecture/query-based-billing | confirmed | — |
| 5 | Adyen bought Orb, closed July 2026 (key point 3) | adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates | confirmed | — |
| 6 | Limit of 1,000 meter-event calls per second per account | S/…/recording-usage-api | confirmed | Added "(n.d., accessed November 2026)" and "in live mode" (the page limits the statement to live mode) |
| 7 | Documentation lists event name, customer, value and an optional timestamp; "an identifier that you can specify in your request" | S/…/recording-usage-api | confirmed | — |
| 8 | Timestamp and identifier are both optional in the API | S/api/billing/meter-event/create | confirmed | — |
| 9 | "Meters specify how to aggregate meter events over a billing period"; sum, count, last | S/billing/subscriptions/usage-based/meters/configure | confirmed | — |
| 10 | A configured meter cannot be changed except for its display name | S/…/meters/configure | confirmed | — |
| 11 | "If you don’t specify an identifier, we auto-generate one for you." | S/…/recording-usage-api | confirmed | — |
| 12 | "within the past 35 calendar days", not "more than 5 minutes in the future" | S/…/recording-usage-api | confirmed | — |
| 13 | "The 35-day window determines whether Stripe accepts a meter event. It doesn’t guarantee…" | S/…/recording-usage-api | confirmed | — |
| 14 | "might accept an event after finalization and include it in meter summaries without updating the finalized invoice or adding the usage to the next invoice" | S/…/recording-usage-api | confirmed | — |
| 15 | "All invoices have a default finalization grace period of 1 hour" | S/…/configure-grace-period | confirmed | — |
| 16 | "You can set a delay of up to 72 hours (3 days)." | S/…/configure-grace-period | confirmed | — |
| 17 | Only subscription-cycle invoices and schedule phase-transition invoices take grace-period usage | S/…/configure-grace-period | confirmed | — |
| 18 | Threshold invoice reflects "only the usage accrued up to the point the invoice is created" | S/…/configure-grace-period | confirmed | — |
| 19 | Cancel by identifier; "You can only cancel events sent to Stripe within the last 24 hours." | S/…/meters/configure | confirmed | — |
| 20 | Usage can be offset by recording a negative quantity | S/…/meters/configure | confirmed | — |
| 21 | "If you cancel usage that’s included on a finalized invoice, we won’t update the invoice or issue a corrected invoice…" | S/…/meters/configure | confirmed | — |
| 22 | Identifier: unique, generated if not provided; "Stripe enforces uniqueness within a rolling period of at least 24 hours." | S/api/billing/meter-event/create | confirmed | — |
| 23 | Purpose: "accidental retries or other problems occurring within extremely brief time intervals" | S/api/billing/meter-event/create | confirmed | — |
| 24 | "The Meter Event limit is 1000 calls per second per Stripe account"; one concurrent call per customer per meter | S/…/recording-usage-api | confirmed | — |
| 25 | Up to 10,000 events per second on API v2 meter event streams; 200,000 through sales | S/…/recording-usage-api | confirmed | — |
| 26 | A platform calling on behalf of a connected account gets 100 operations per second | S/…/recording-usage-api | confirmed | Cell reworded so that it reads as an exception to the limit (it sits in the "does not promise" column) |
| 27 | "Stripe processes meter events asynchronously, so aggregated usage… might not immediately reflect recently received meter events" | S/…/recording-usage-api | confirmed | — |
| 28 | Error events `v1.billing.meter.error_report_triggered`, `v1.billing.meter.no_meter_found`; code `timestamp_too_far_in_past` | S/…/recording-usage-api | confirmed | — |
| 29 | Post dated January 2025, by Taras Mitran and Karan Dhabalia, titled "How we built it: Usage-based billing" | stripe.com/blog/how-we-built-it-usage-based-billing (displays "January 28, 2025") | confirmed | — |
| 30 | "an edge router, which does stateless authentication and API validation, then loads them directly onto an event bus" | same | confirmed | — |
| 31 | Apache Flink, chosen in part for "exactly-once processing guarantees" | same | confirmed | — |
| 32 | "we process the same event in two geographic regions simultaneously"; "a standardized time stamp, generated before reaching the two Flink applications" | same | confirmed | — |
| 33 | Fast path: "30-second tumbling window, which we store in memory in real time", used for alerts | same | confirmed | — |
| 34 | Slow path: five-minute window, written to disk "in a kind of transactional ledger"; "allows us to accommodate any delayed or out-of-order events"; produces invoicing data | same | confirmed | — |
| 35 | Pricing "into a stream of changes", "like two sides of a zipper"; retroactive discount "means opening a lookback window" | same | confirmed | — |
| 36 | Post's capacity figure is 100,000 events per second | same ("100,000 events per second per business" / "per user") | confirmed | — |
| 37 | The post does not describe deduplication, the storage behind the durable path, or whether raw events are kept | same (searched the text for dedup, duplicate, idempot, raw, retain, database: no passage) | confirmed | — |
| 38 | Orb: "treats billing as the output of a deterministic query, not a side effect of streaming state mutations" | O/architecture/query-based-billing | confirmed | — |
| 39 | Orb: "Every usage event is stored immutably in a columnar data store…"; "The invoice is computed, not retrieved." | same | confirmed | — |
| 40 | Orb: "once an event is processed and the counter is incremented, the original context is lost" | same | confirmed | — |
| 41 | Orb: "a dependency graph and invalidation system" marks only affected invoice fragments | same | confirmed | — |
| 42 | Orb: events may be reported "up to 12 hours after the `timestamp`" by default | O/events-and-metrics/reporting-errors (page adds that the grace period is configurable account-wide) | confirmed | — |
| 43 | Orb: "Orb never overwrites or permanently deletes ingested usage data" | same | confirmed | — |
| 44 | Orb: "running totals in Redis (MemoryDB) as events arrive", used for alerts; "But the billing logic never touches these counters…" | O/architecture/query-based-billing | confirmed | — |
| 45 | Orb hosted rollups: "generally north of 500,000 events per second", "to pre-aggregate that data in real time rather than storing every raw event"; separate product; 10-minute window, 30-second partial rollups | O/events-and-metrics/high-throughput-ingestion; "separate product" from O/architecture/query-based-billing | confirmed | — |
| 46 | Trade-off table: Orb "the historical events are still there", "Every line item is traceable to specific events"; Stripe lookback (2025 post) | O/architecture/query-based-billing; Stripe post | confirmed | — |
| 47 | Heading "Mid-cycle price changes drop grace period usage"; "Stripe skips invoice recomputation during finalization, so any usage reported during the grace period doesn’t appear on current or subsequent invoices." | S/…/configure-grace-period | confirmed | Added "(n.d., accessed November 2026)" |
| 48 | Orb lists "Versioned pricing objects" among an invoice's inputs | O/architecture/query-based-billing | confirmed | Added "(n.d., accessed November 2026)" |
| 49 | "Billing credits are prepaid or promotional usage credit allocated through credit grants"; distinct from invoice balance and cash balance | S/billing/subscriptions/usage-based/billing-credits | confirmed | — |
| 50 | "You can’t offer billing credits as stored value to your customers." | same | confirmed | — |
| 51 | Orb commitments feature "is in early access"; prepaid invoiced up front as a pool of credits; postpaid "Orb bills the difference as a true-up" | O/enterprise/commitments | confirmed | — |
| 52 | Compare page: basic meters credit-based pricing "Supported (invoice time)" with footnote "Credits are only reconciled at invoice time. Customers can exceed their balance during the cycle."; Metronome "Supported (real-time)" | S/billing/subscriptions/usage-based/compare-metronome (the cell reads "Supported (invoice time¹)", with the footnote mark) | confirmed | — |
| 53 | Metronome "the usage engine Stripe bought in 2026" | stripe.com/newsroom/news/stripe-completes-metronome-acquisition | hedged | The release fetched covers only the completion (14 January 2026); the signing date is not in any source of the page. Sentence now says "whose acquisition Stripe completed in January 2026" |
| 54 | Fast path triggers alerts "when someone has spent too much money or is running out of credits"; "P95 latency under 30 seconds" | Stripe post | confirmed | — |
| 55 | Stripe announced on 14 January 2026 that it "has completed its acquisition of Metronome" | Stripe newsroom (displays "14 January 2026"; read in the English `/en-nl/` variant, the bare URL served Dutch to this network) | confirmed | — |
| 56 | "Metronome is Stripe’s primary usage-based billing platform and the recommended starting point for all new integrations"; meters "a lower-level primitive that remains fully supported for existing integrations" | S/billing/subscriptions/usage-based | confirmed | — |
| 57 | "Metronome handles metering, rating, and billing, while Stripe handles payment collection, tax calculation, and revenue recognition." | S/…/compare-metronome | confirmed | — |
| 58 | Metronome pushes finalized invoices; "This invoicing sync is one way, meaning Stripe doesn’t send invoice data back to Metronome." | S/billing/how-metronome-works-with-stripe | confirmed | — |
| 59 | Connect is listed as not supported with Metronome | S/…/compare-metronome (Connect: "—") | confirmed | — |
| 60 | Adyen press release of 11 June 2026; "The total consideration for the transaction is $335 million" | adyen.com/press-and-media/jtrg4qd7j3p4rj (displays "June 11, 2026") | confirmed | — |
| 61 | "Both transactions officially closed on July 1, 2026"; the other was Talon.One, a loyalty company | Adyen closing release (displays "July 1st, 2026") | confirmed | — |
| 62 | "Orb stores the full event stream at scale, decoupling ingestion from invoicing" | June release | confirmed | — |
| 63 | "incubator model"; "continuing to support multi-PSP environments"; "the strategic intent is convergence" | June release | confirmed | — |
| 64 | 29 September 2026: "You’ll soon see how we bring this unified Adyen and Orb experience to life across our platform." (rulings 21 and 25) | adyen.com/knowledge-hub/why-adyen-acquired-orb (displays "September 29th, 2026", Blake Breathitt; metadata datePublished 2026-09-29) | confirmed | The page already used the displayed date and does not quote the sentence ruling 21 forbids; that sentence is not on the page (searched) |
| 65 | No meter, usage or billing object in Adyen's documentation (November 2026) | docs.adyen.com/llms.txt (2,697 lines searched for meter, usage-based, Orb, rating, billing, subscription, invoice: only Adyen's own fee invoices, webhook subscriptions and a terminal "ask for a rating" prompt) | confirmed | — |
| 66 | Adyen documents recurring charges as a stored token charged on the merchant's schedule | not checked here (owned by chapter 27; the sentence links there and this page lists no source for it) | not checked | — |
| 67 | "Stripe's release says Metronome's metering engine “already powers some of the most ambitious AI companies”" | Stripe newsroom | corrected | The words are Patrick Collison's, quoted in the release from LinkedIn ("Scott and the team have built an exceptionally powerful metering engine that already powers…"). Sentence now attributes them to him as quoted in the release; source entry extended |
| 68 | "Billing for LLM tokens is in public preview and available to all users with a Metronome account"; Stripe syncs model prices; metering by model and token type | S/billing/token-billing | confirmed | — |
| 69 | Adyen's article: "AI models and modern APIs carry significant, variable compute and token costs" | Adyen knowledge hub, 29 September 2026 | confirmed | — |
| 70 | The sources describe how Metronome connects to Stripe, not how it is built | S pages above (read in full) | confirmed | — |
| 71 | Where They Differ, row 1: Billing Meters sum, count, last / Not public | rows 9 and 65 | confirmed | — |
| 72 | Row 2: Metronome completed 14 January 2026, recommended starting point, one-way push / Orb closed 1 July 2026, multi-PSP, "soon" | rows 55, 56, 58, 61, 63, 64 | confirmed | — |
| 73 | Row 3: Flink in two regions, two paths / Orb immutable events | rows 31–34, 39 | confirmed | — |
| 74 | Row 4, Orb: 12 hours by default, amendments archive events | O/events-and-metrics/reporting-errors ("Old events are marked as archived") | confirmed | — |
| 75 | Row 5: meters apply credits at invoice time, Metronome real-time drawdown / "Orb documents a credit ledger" | S/…/compare-metronome ("Real-time credit burndown"); O/product-catalog/prepurchase | corrected | No source of the page supported the Orb half. Fetched Orb's "Configure prepaid credits": "an append-only ledger of transactions that affect the credit balance", and "Orb reflects changes to the credit balance as soon as events are ingested". Cell now states that, and the page is added to Sources |
| 76 | Row 6: token billing in public preview through Metronome / named in Adyen's rationale, no product documented | rows 68, 69, 65 | confirmed | — |
| 77 | Orb amendments: "Old events are marked as archived" (reading of the table) | O/events-and-metrics/reporting-errors | confirmed | — |
| 78 | Stripe tells existing meter users "you don’t need to migrate" | S/billing/subscriptions/usage-based | confirmed | Added "(n.d., accessed November 2026)" |
| 79 | Orb guarantees "that duplicates are never processed within the account grace period" | O/events-and-metrics/event-ingestion | confirmed | Added "(n.d., accessed November 2026)" to the sentence |
| 80 | Error code `meter_event_customer_not_found` | S/…/recording-usage-api | confirmed | — |
| 81 | 2025 post: "when processing does fail, developers don’t necessarily know it right away." | Stripe post | confirmed | — |
| 82 | Usage beyond the grace period is in summaries "but we don’t add that usage to the finalized invoice or the next invoice" | S/…/configure-grace-period | confirmed | — |
| 83 | After a mid-cycle price change "the grace period doesn’t capture late usage" | S/…/configure-grace-period | confirmed | — |
| 84 | Take-away bullets (35 days, "doesn’t guarantee…", 24 hours, account grace period, two designs, 14 January and 1 July) | rows 1, 13, 3, 79, 4, 55, 61 | confirmed | — |

Counts: 84 rows; 79 confirmed, 3 corrected (2, 67, 75), 1 hedged (53), 0 unsupported, 0 unreachable, 1 not checked (66).

## Could not verify, and what I did

- **Row 66** (Adyen's recurring model as a stored token charged on the merchant's schedule): this page cites no source for it and hands the reader to chapter 27, which owns it. I did not fetch Adyen's tokenization pages in this session, so it is "not checked", not confirmed. The sentence is unchanged.
- **Signing date of the Metronome acquisition**: the Stripe release covers completion only. The page no longer says Stripe "bought" Metronome in 2026 in the sentence that introduces it. The section heading "Two Acquisitions in 2026" and the take-away "Both providers bought a usage engine in 2026" remain; they are true of the completion dates, which the same bullet gives. The author may want to reword them if the signing (trade press: December 2025) matters.
- **Stripe newsroom URL**: `stripe.com/newsroom/news/stripe-completes-metronome-acquisition` returns 200 but redirects by location to a localized copy (Dutch here). The quotations were read in the English variant. The source entry keeps the unlocalized URL.

## Links

All 19 original source URLs return 200 with no change of path (the Stripe newsroom URL redirects only to a locale prefix). One entry added: `https://docs.withorb.com/product-catalog/prepurchase` (200). Every entry is used in the text. All `[[permalink]]` links are in the style guide's list; the render check reports `[[stripe-and-adyen-bets-compared]]` as unresolved only because that page is not written yet.

## Rulings and format

- Ruling 21: the knowledge-hub article is dated 29 September 2026 in every place; the forbidden sentence is not quoted.
- Ruling 25: displayed dates used (Stripe post 28 January 2025; Stripe release 14 January 2026; Adyen releases 11 June and 1 July 2026; article 29 September 2026).
- Ruling 30: all Stripe and Orb documentation pages are cited "n.d., accessed November 2026" in the text and "n.d., accessed 2026-11" in Sources. The marker was missing in five sentences outside the section that declares it once; added.
- Ruling 22: no external URL in the running text.
- Evidence age: no source is older than three years (the oldest is the January 2025 post).
- `timetoread` changed from 25 to 26 (5,934 words ÷ 230 = 25.8).
- No unit added, dropped, merged or reordered; spec unchanged except its changelog.

## Larkfield consistency

Checked against the ledger line for chapter 28 and the lines of chapters 27 and 29: plans and allowances, €0.07, 1,240 / 1,324 / 180 / 96, 17 March, 31 March 21:40 to 03:20 UTC and finalization at about 01:00 UTC, €51.80 / €57.68 / €12.60 / €6.72, the May 2027 policy and takeover, 6,200 studios, 9 million messages (labeled illustrative), Studio Noord's plan change of 16 April 2027. Arithmetic rechecked (1,240 + 180 − 96 = 1,324; 1,240 − 96 = 1,144; 9 million ÷ 2,592,000 seconds ≈ 3.5 per second; 10,000 × 2,592,000 ≈ 26 billion). No weekday is named. No contradiction found.

## Ledger conflicts

None.

## For other pages

- `_research/brief-billing-and-revenue.md` section 1.10 still carries the two errors of ruling 21 (the date 2026-10-19 and the sentence "We completed our acquisition of Orb on 1 July."). Any page drafted from it should be checked for both.
- Orb documents real-time deduction from a prepaid credit balance (`docs.withorb.com/product-catalog/prepurchase`). Chapters 27 and 48, if they describe Orb's credits, can cite it.
