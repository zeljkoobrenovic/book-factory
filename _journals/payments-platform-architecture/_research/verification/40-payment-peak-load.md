# Verification — 40-payment-peak-load (`payment-peak-load`)

Verification pass of 17 November 2026. Every source below was fetched and read in this session. Stripe's newsroom redirects by location to a Dutch translation; the English text was read through `?locale=en-US`. The URLs in Sources keep the `/us/` form, which resolves (HTTP 200 after redirect).

Totals: 51 claims checked — 40 confirmed, 7 corrected, 4 hedged, 0 unsupported, 0 unreachable.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe 2025: "More than 152,000 transactions per minute at peak volume" (lead, table, scene) | stripe.com/us/newsroom/news/bfcm2025 | confirmed | Inline link removed (ruling 22) |
| 2 | Adyen 2025: "handling up to 199,000 transactions per minute without disruption" | adyen.com/knowledge-hub/bfcm | confirmed | Inline link removed |
| 3 | Stripe 2023 row: "more than $18.6 billion", "more than 300 million", "93,304 transactions per minute", "a peak of 27,395 requests per second", "API uptime greater than 99.999%"; dated 28 Nov 2023 | stripe.com/us/newsroom/news/bfcm2023 | confirmed | Link removed from table cell |
| 4 | Stripe 2024 row: "more than $31 billion", 465 million, "137,000 transactions per minute", "greater than 99.9999%"; dated 3 Dec 2024 | stripe.com/us/newsroom/news/bfcm2024 | confirmed | Link removed from table cell |
| 5 | Stripe 2025 row: "more than $40 billion", "more than 578 million", "more than 99.9999%"; dated 2 Dec 2025 | stripe.com/us/newsroom/news/bfcm2025 | confirmed | — |
| 6 | Adyen 2024 row: "$34 billion", "670 million"; no peak rate, no uptime wording; dated 9 Dec 2024 | adyen.com/knowledge-hub/black-friday-cyber-monday-payment-insights | confirmed | Cell "Not found" changed to "Not given" (page read in full; no uptime or per-minute figure). Source title corrected to the displayed headline |
| 7 | Adyen 2025 row: "$43 billion", "up to 199,000 transactions per minute" (article, 9 Dec 2025); "837 million", "99.9999% uptime" (results release, 12 Feb 2026) | adyen.com/knowledge-hub/bfcm; adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2 | confirmed | Links removed; cell now says which document is which |
| 8 | "None of the five sources defines 'transaction'" | all six peak documents | corrected | Six documents, not five. None defines the term; Adyen's 2024 article has a methodology note (period; "transactions processed on the Adyen platform"), now mentioned |
| 9 | Adyen's totals very likely include terminals: "over 127M in-person payment transactions" (2025) | adyen.com/knowledge-hub/bfcm | confirmed | Added the 2024 article's "nearly 100 million in-person payments", which supports the same reading for 2024 |
| 10 | Stripe's releases do not say what share is in person | three Stripe releases | confirmed | — |
| 11 | None defines how uptime was measured; both report they stayed up | six documents | confirmed | — |
| 12 | 199,000 against 152,000 "shows that more arrived" | — | hedged | "shows at most": the units are undefined, as the same paragraph says |
| 13 | Stripe 2023 release is the only one that gives a request rate | six documents | confirmed | — |
| 14 | Both providers report BFCM as a four-day period | Stripe releases; Adyen 2024 methodology note | confirmed | — |
| 15 | AWS is "Stripe's long-standing cloud infrastructure provider" (press release, 23 Jan 2023) | stripe.com/us/newsroom/news/amazon-and-stripe | confirmed | Link removed; source title corrected to the displayed headline |
| 16 | "later Stripe sources say the same" (about AWS) | stripe.dev docdb post | hedged | No later source in the page repeats the sentence; the 2024 database post names Amazon S3 as storage it uses. Evidence note now says exactly that |
| 17 | Stripe 2024 database post: "can split database shards … bin packing when traffic is low"; shard autoscaling still an investment; authors, 2024-06-06 | stripe.dev/blog/how-stripes-document-databases-… | confirmed | Link removed |
| 18 | Patil, Sessions 2024: "We use massive synthetic traffic … 20x the worst-case scenario"; "we repeat this in production …" | stripe.com/us/sessions/2024/building-a-culture-of-system-reliability | confirmed | Link removed. Day of the talk (2024-04-25 in Sources) is not shown on the page: not checked |
| 19 | Patil: "today's Sessions, there's no code freeze" (said of the conference day) | same | confirmed | — |
| 20 | Stripe 2026 proxy post: "gives us 15–20% more headroom …"; authors; 2026-08-26 | stripe.dev/blog/building-a-data-plane-from-scratch-… | confirmed | Link removed |
| 21 | Adyen 2021: "We manage our own infrastructure in several data centers …"; "… internal cloud." | adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | Link removed. Page displays "Updated June 2022"; noted in the source entry |
| 22 | Adyen 2021 part 2: "The 20x scaling factor is a rule of thumb …"; Willem Pino, 23 Aug 2021 | adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2 | confirmed | Link removed |
| 23 | Adyen H1 2026 results (13 Aug 2026): "We are proactively pulling investment from 2027 into H2 2026 …" | adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne | confirmed | Link removed |
| 24 | INFERENCE block: "Neither Stripe nor Adyen says how far ahead it plans for a peak" | docs.adyen.com/industries/peak-season.md | hedged | Adyen's documentation says preparation is "an ongoing project that we work on throughout the year"; block now says neither gives a lead time and quotes that |
| 25 | Adyen partition post quotation (incident number 2016); Derk van Veen; 16 Sep 2025 | adyen.com/knowledge-hub/partitioning-an-environment-not-individual-tables | corrected | Quotation matched to the source character for character (source prints "December shopping– when"). Link removed; source title set to the displayed headline. "the one near miss either company has published" weakened to "that I found" |
| 26 | "I found no Adyen description of load testing" (body, Differ row, take-away) | docs.adyen.com/industries/peak-season.md | corrected | Adyen documents it: "We periodically load test this system with merchants who hold transactions and then release the transactions in bulk." Body, table cell and take-away rewritten |
| 27 | "… and none of a change freeze at peak" (body, Differ row, take-away) | docs.adyen.com/industries/peak-season.md | corrected | Adyen documents it: "We therefore freeze our code deployment around the following peak season days" (Singles Day, Black Friday, Cyber Monday, Giving Tuesday, Christmas, New Year), critical bug fixes excepted. Body, table cell and take-away rewritten |
| 28 | "Neither company publishes its capacity or its headroom" | docs.adyen.com/industries/peak-season.md | corrected | Adyen publishes a utilization rate ("generally less than 30%") and answers its own question on transactions per second without a number. Page now: neither publishes a capacity figure; the utilization quote added to the text and the Differ table |
| 29 | Stripe: no statement on changes during Black Friday | docs.stripe.com/llms.txt (no page on peak, freeze, holiday); the three releases; the Sessions talk | confirmed | As far as searched; worded "I found no Stripe statement" |
| 30 | Stripe 2017: "every Stripe user has a bucket …"; "we added the ability to briefly burst above the cap … (e.g. a flash sale.)"; non-critical requests rejected with 503 by the fleet load shedder; Paul Tarjan, 30 Mar 2017 | stripe.com/blog/rate-limiters | confirmed | — |
| 31 | Stripe rate-limit page: "A sudden increase in charge volume, such as a flash sale, might result in rate limiting."; "We try to set our rates high enough …" | docs.stripe.com/rate-limits.md | confirmed | — |
| 32 | Stripe limits: 100 requests a second per account in live mode, 25 per endpoint unless otherwise noted, 50 in progress (default) | docs.stripe.com/rate-limits.md | confirmed | Agrees with chapter 21 (ruling 5) |
| 33 | Adyen publishes no rate limit for payment requests; documentation index lists no such page | docs.adyen.com/llms.txt (2,697 lines searched: rate limit, throttl, 429, too many requests, request limit, quota, capacity: no hits) | confirmed | Agrees with chapter 21 |
| 34 | Adyen response handling: 429, "You have sent too many requests in a short period"; backoff with jitter | docs.adyen.com/development-resources/response-handling.md | confirmed | — |
| 35 | Stripe: "Errors that occur before execution begins, such as … rate limiting, don't cache a result." | docs.stripe.com/error-low-level.md | confirmed | — |
| 36 | Adyen 2020: "we have better control over how and when the requests are executed" (Adyen for Platforms, synchronous to asynchronous); Miguel Gonzalez, 22 Oct 2020 | adyen.com/knowledge-hub/the-adyen-way-of-engineering--we-design-for-20x | confirmed | Link removed |
| 37 | Visa Core Rules, 24 Oct 2026: Stand-In Processing definition | usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf (glossary, ID# 0025121) | confirmed | — |
| 38 | Visa: response code 91 in a category where reattempt is permitted, up to 20 attempts in 30 days | same PDF, Table 7-2 (code 91 listed under Category 2) | confirmed | — |
| 39 | Adyen's documentation still gives 15 | docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees.md | confirmed | Source was missing from the page; added, with "n.d., accessed November 2026" in the sentence |
| 40 | Stripe decline code issuer_not_available: "The card issuer couldn't be reached, so the payment couldn't be authorized." | docs.stripe.com/declines/codes.md | confirmed | — |
| 41 | Adyen refusal reason 9 "Issuer Unavailable": "It is not possible to contact the shopper's bank to authorize the transaction." | docs.adyen.com/development-resources/refusal-reasons.md | confirmed | — |
| 42 | Neither documents pacing toward networks; neither says whether an approval was stand-in; neither publishes issuer response times | docs.adyen.com/llms.txt (stand-in, STIP, issuer response: no hits); docs.stripe.com/llms.txt | hedged | Stripe's index is a short top-level list and cannot prove absence; sentence now says "I found no Stripe or Adyen document" |
| 43 | Adyen webhooks: "This can happen after you fix a failing endpoint, as the queued webhooks are sent in a short timeframe. Ensure your server can handle the load." | docs.adyen.com/development-resources/webhooks/troubleshoot.md | confirmed | — |
| 44 | Stripe: "If you request a large increase, contact Stripe Support at least 6 weeks in advance." | docs.stripe.com/rate-limits.md | confirmed | — |
| 45 | Stripe load-testing advice: three quotations (sandbox discouraged; mock; sampled latencies) | docs.stripe.com/rate-limits.md | confirmed | — |
| 46 | "I found no equivalent Adyen page" (on testing before a peak) | docs.adyen.com/industries/peak-season.md; docs.adyen.com/development-resources/batch-processing.md | corrected | Adyen has a peak season guide that asks customers to plan and test in advance, and a batch processing page (bulk requests "by uploading an input file"). Neither advises on load testing or gives a rate; sentence rewritten to say so |
| 47 | Differ row "Guidance for a customer's own peak", Adyen cell: "no page on planning a batch found" | same two pages | corrected | Cell now names the peak season page and the file-based batch route, and says no rate figure is given |
| 48 | Differ row "Published peak figures" (both cells) | rows 3–7 | confirmed | — |
| 49 | Differ row "How capacity is obtained" (both cells) | rows 15, 17, 21–23 | confirmed | Adyen cell gains the utilization figure |
| 50 | Differ row "Per-customer limit" (both cells) | rows 32–34 | confirmed | — |
| 51 | Stripe: "add randomness to the backoff schedule to avoid a thundering herd effect" | docs.stripe.com/rate-limits.md | confirmed | — |

## Could not verify, or not checked

- **Date of the Sessions talk (2024-04-25 in Sources).** The talk page shows the year and no day. Not checked; left as it was. The running text says only "Stripe Sessions 2024".
- **Absence claims about Stripe** (no statement on changes during Black Friday; no document on stand-in approvals or pacing toward issuers). Searched `docs.stripe.com/llms.txt`, the three press releases and the Sessions transcript. The index is a short top-level list, so these are worded "I found no …", not "not public", except in the Differ table where the cell says "Not public for Black Friday".
- **Adyen knowledge hub** was not searched beyond the six posts the page cites; the corrections about load testing and the freeze come from the documentation site.
- **Refusal for volume means "not attempted" at Adyen.** Documented for Stripe only (row 35). The page states it generally, as chapter 21 does; Adyen's page says only "too many requests". Left as written, to stay in agreement with chapter 21; flagged for the author.

## Links

All 27 URLs in Sources and Evidence return HTTP 200 (17 November 2026). All `[[permalink]]` links are in the style guide's list; the render check reports none unresolved. No external URL remains in the running text (ruling 22): 15 inline links were reduced to attributions.

## Rulings and format

- Ruling 5: the limits (100 a second per account, 25 per endpoint, 50 in progress, six weeks' notice, Adyen none for payments) and the Larkfield settings (48 workers, 10 and 5 a second, 157,000 and 200,000 renewals) agree with `posts/21-developer-platform/index.md`.
- Ruling 19: Visa's 20 in 30 days cited from the rules; Adyen's 15 noted, and its source added.
- Rulings 25 and 30: displayed dates used; documentation pages cited "n.d., accessed November 2026".
- Evidence age: sources from 2017, 2020, 2021 and January 2023 are flagged in the text and in Sources.
- Length: the additions were offset by trims; `check_draft.py structure` reports 5,699 words (limit 5,700). `timetoread` changed from 24 to 25 minutes.
- One term gloss added (dispute).

## Larkfield consistency

All figures agree with the ledger (Renewal Wave, Double Charge, K1, K5, the chapter 21 and chapter 40 additions). Arithmetic rechecked: about 1,000 a minute; 17 a second; 2,500 and 3,300 a second; 0.4%; 4.4 and 11.1 hours; 62% and 38%; 50 and 17 events a second. No weekday is named.

## Ledger conflicts

None.

## Spec

Wording inside units changed; no unit added, dropped, merged or reordered. `spec.json` updated to match in: section 3 controlling idea and p15, the evidence of the peak-figures paragraph, the load-testing paragraph, the Differ paragraph, open question 2, changelog. **Not changed, because they are copied from `journal-spec.json`, which this pass may not write:** acceptance criterion AC-4 ("no Adyen description of load testing, of a change freeze at peak, or of payment rate limits was found") and the last sentence of the thesis `how_why`, and the third supporting claim of the thesis. All three are now false for load testing and the freeze. The author must correct them in the journal spec and the post spec; until then a draft check will fail AC-4 (a blocker) against the corrected page.

## For other pages

- **`41-safe-change`** (and any page that says Adyen's peak practice is not public): Adyen's documentation page `docs.adyen.com/industries/peak-season` documents a code freeze around named peak days, periodic load tests with merchants, no maintenance windows ("Releases, patches and upgrades are continuously applied without interruption of service"), an active/active stateless architecture across data centers and utilization "generally less than 30%". Chapters 37, 39, 41 and 47 should check their "not public" statements against it. Chapter 41's hand-in sentence says chapter 40 "ended with a system that cannot be stopped or frozen for its peaks"; chapter 40 says "cannot be stopped".
- **`38-payment-data-stores-and-consistency`, `41-safe-change`**: they date the Adyen partitioning post 2025-09-17; the page displays 16 September 2025 (ruling 25).
- **`41-safe-change`, `46-case-stripe`**: the Stripe release at `/newsroom/news/amazon-and-stripe` is headlined "Amazon-Stripe partnership accelerates ecommerce and streamlines online payments"; "Amazon and Stripe sign an expanded global agreement" is its first line.
- **`21-developer-platform`**: its statement that Adyen publishes no limit for payments stands. It could mention Adyen's file-based batch processing page as the documented bulk route.
