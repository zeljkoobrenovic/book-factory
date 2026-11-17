# Verification — 39-multi-region-and-data-residency (`payment-multi-region-and-data-residency`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Adyen documentation through the `.md` variants; DORA from the Publications Office with `Accept: application/xhtml+xml` and `Accept-Language: eng`). Quotations were compared as strings after normalizing typographic quotes and white space. stripe.com pages redirect by the reader's location (`/us/…` was served as `/nl/…` here); the English text was read from the `/in/` and `/nl/` variants, which carry the same English legal text. Searches for the "Not public" statements covered: `docs.stripe.com/llms.txt` and `docs.adyen.com/llms.txt`; the sitemaps of docs.stripe.com (5,148 URLs), docs.adyen.com (2,619), support.stripe.com (1,889) and help.adyen.com (9,472); the post lists of stripe.dev/blog and the adyen.com knowledge hub (574 slugs in the English sitemap); both companies' privacy, data-processing and sub-processor pages; Adyen's corporate pages; and web searches.

**The main finding.** The page was written as if Adyen had published no data-center locations, nothing on where Indian payment data is stored and nothing on failover, and as if Stripe named no place at all. Four first-party pages the writer had not read say otherwise (rows 31, 39–43, 47, 55). The page's argument (law first, hosting second; how takeover works is not public; ask in writing) stands; the statements of fact were corrected.

Short names: **INFRA** = `https://www.adyen.com/infrastructure`; **PEAK** = `https://docs.adyen.com/industries/peak-season`; **PC** = Stripe Privacy Center; **IND** = `https://stripe.com/india-data-storage-faq`; **SP** = `https://stripe.com/us/legal/service-providers`.

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Lead: the public record supports "AWS" in the design-document sentence | stripe.com/us/newsroom/news/amazon-and-stripe; rows 27–31 | confirmed | Inline link removed (ruling 22) |
| 2 | Adyen, October 2025: "data must remain close to producers to reduce latency and meet regulations, while also being centralized for analytics" | adyen.com/knowledge-hub/building-a-global-stream | confirmed | Displayed date "October 6th, 2025"; authors Gaurav Singh and Luciano Sabença |
| 3 | Same post: a cashier in Australia "while your payment was being sent to Europe" | same | confirmed | — |
| 4 | Stripe DPA FAQ: SCCs as a way to "transfer personal data to certain countries, outside of the European Economic Area, including the United States" | stripe.com/us/legal/dpa/faqs | confirmed | GDPR expanded; SCCs glossed from the page ("a data transfer mechanism issued by the European Commission") |
| 5 | DORA applied from 17 January 2025 | publications.europa.eu/resource/celex/32022R2554, Art. 64 | confirmed | Acronym expanded |
| 6 | DORA recital 82: "does not impose a data localisation obligation as it does not require data storage or processing to be undertaken in the Union" | same | confirmed | URL corrected: the page's `…32022R2554.ENG` returns 404 for an HTML request; replaced by the form chapter 26 uses. Evidence-age note added (adopted 14 December 2022, OJ 27 December 2022) |
| 7 | Uber 2018: "high reliability through an active-active architecture" among its design goals | uber.com/blog/payments-platform/ | confirmed | Displayed date December 5, 2018; "the current system may differ" added to the age mark |
| 8 | Placement table: active-passive "Not public" for both | searches above | confirmed (as an absence) | Reworded "Not stated by either" |
| 9 | Placement table: active-active "Not public" for both | PEAK; INFRA | corrected | Adyen's documentation says "Our active/active, stateless architecture"; cell now cites it and keeps "Not public" for the write rule |
| 10 | Placement table: partition by jurisdiction documented only for Stripe | INFRA | corrected | Adyen's "isolated India environment" added |
| 11 | RBI circular of 6 April 2018: "All system providers shall ensure that the entire data relating to payment systems operated by them are stored in a system only in India." | rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0 | confirmed | RBI/2017-18/153, dated "6 April 2018" |
| 12 | Reason: "it is important to have unfettered supervisory access to data" | same | confirmed | — |
| 13 | RBI clarification of 26 June 2019: "no bar on processing of payment transactions outside India" | rbi.org.in/Scripts/FAQView.aspx?Id=130 | confirmed | Page shows "Date : Jun 26, 2019"; described as FAQ in the sentence |
| 14 | Same: "should be deleted from the systems abroad and brought back to India not later than the one business day or 24 hours from payment processing, whichever is earlier" | same | confirmed | Take-away bullet now gives the full condition, not "within 24 hours" |
| 15 | Same: reaches "payment gateways, third party vendors and other entities" engaged by licensed firms | same | confirmed | Page: "retained or engaged by the authorised / approved entities" |
| 16 | The rule is still in force ("India requires") | rbi.org.in/scripts/NotificationUserWithdrawnCircular.aspx | hedged | The circular is not on the RBI's list of withdrawn circulars as fetched today (searched by title and number). The RBI's November 2025 consolidation of circulars was not read; the age mark now says what was checked |
| 17 | Stripe's India page was last updated on 16 May 2023 | IND | confirmed | "Last updated: May 16, 2023" |
| 18 | "we’re moving the servers that store India data to be located within the country" | IND | confirmed | — |
| 19 | "a substantive infrastructure change" | IND | confirmed | — |
| 20 | "Payment information can no longer be cloned into or out of India"; gloss of cloning | IND | confirmed | The page's next sentences (platforms cloning to connected merchants) support the gloss |
| 21 | "the same card details can have two different fingerprints, one for India and another for the rest of the world" | IND | confirmed | — |
| 22 | Card Updater, Revenue Recognition and Sigma "temporarily disabled in India" from 30 April 2021 | IND | confirmed | All three carry "April 30, 2021". Revenue recognition glossed. Not added: Card Updater "impacts only internationally issued cards"; the cloning and fingerprint changes started 20 April 2021 |
| 23 | The page does not say whether the features returned | IND | confirmed | — |
| 24 | PC: "Where required payment system data will be stored only on servers in India in accordance with the RBI data localization requirements." | stripe.com/us/legal/privacy-center | confirmed | — |
| 25 | KEY POINT and table: Stripe "moved" its India data / "Servers moved" | IND; PC; SP | hedged | IND says "we’re moving". Now: "Stripe says it stores Indian payment data only in India"; table "Servers moving … (page updated 2023); data stored on servers in India". SP (last updated 27 September 2026) added: "Stripe India Private Limited stores certain data on servers located in India" |
| 26 | The fingerprint identifies the same card number across customers | IND ("which uniquely identifies a particular card number") | confirmed | — |
| 27 | Stripe press release of 23 January 2023: "Stripe has long relied on AWS to provide the core compute infrastructure on which Stripe is built" | stripe.com/us/newsroom/news/amazon-and-stripe | confirmed | Source title corrected to the page's headline, "Amazon-Stripe partnership accelerates ecommerce and streamlines online payments" ("Amazon and Stripe sign an expanded global agreement" is its subheading) |
| 28 | David Singleton: "We couldn’t run without AWS—and we wouldn’t want to." | same | confirmed | The page ends the quotation with a comma before "said David Singleton, chief technology officer of Stripe" |
| 29 | Singleton was "then" chief technology officer | web search only (trade press, August 2024) | not checked against a primary source | Trade press reports he stepped down in 2024; "then" kept |
| 30 | AWS post co-written with Stripe engineers, October 2024: "a sophisticated microservice environment built on top of AWS" | aws.amazon.com/blogs/mt/how-stripe-architected-massive-scale-observability-solution-on-aws/ | confirmed | Dated 24 OCT 2024; two authors are Stripe staff engineers |
| 31 | "No Stripe source names a region" / KEY POINT "names no regions" / table "None" | PC | corrected | PC, "Why is Stripe storing authentication and authorization data globally?": "a robust, multi-region infrastructure dedicated to optimizing authentication, authorization, and identity management. This infrastructure spans multiple geographic regions, specifically including our data centers located in the United States and India"; "this global storage strategy does not extend to any transactional information or other data related to End Customers". Now: "names no AWS region … The only places named are countries, and not for payment data" |
| 32 | Security documentation: card data vault "in an isolated Amazon Web Services (AWS) environment" | docs.stripe.com/security | confirmed | — |
| 33 | One base URL, `https://api.stripe.com` | docs.stripe.com/api | confirmed | — |
| 34 | PC: "Personal Data may be transferred to, and processed, in any country where we do business", "including to the United States" | PC | confirmed | Two passages of the same page |
| 35 | Adyen 2021: "We manage our own infrastructure in several data centers around the world" | adyen.com/knowledge-hub/design-to-duty-adyen-architecture | confirmed | "July 28th, 2021", "Updated June 2022" |
| 36 | Same: "The reasons we are not deploying to the cloud are part historical, part legal, and part technical." | same | confirmed | — |
| 37 | Adyen CTO, October 2025: "end-to-end ownership over every layer, from our data centers to our application logic" | adyen.com/knowledge-hub/strengthening-our-platform-resilience | confirmed | Tom Adams, "October 31st, 2025" |
| 38 | August 2026 post: "tens of thousands of hosts spread across tens of data centres" | adyen.com/knowledge-hub/architect-blog-1 | confirmed | "August 23rd, 2026"; source title completed |
| 39 | H1 2026 results: "The majority of our CapEx is invested in data centers" | adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne | confirmed | 13 August 2026 |
| 40 | "None of these names a place" and KEY POINT "five integration regions without locations" | INFRA | corrected | INFRA (n.d.): "Adyen currently hosts its main systems in separate data centers in Europe, the United States, India, Singapore, Japan and Australia." The English, en_GB, en_IN and en_AE versions agree; nl_NL lists Europe, the United States and Australia; pt_PT "two data centers in Europe and two in the US". The page now quotes INFRA and says the translations list fewer places |
| 41 | "Adyen makes no public residency promise" | INFRA; adyen.com/privacy-policy | corrected | INFRA: "All payments processed are stored in Europe and our isolated India environment." Quoted, and labeled by the author as a summary on an undated page, not a commitment |
| 42 | Adyen on serving from several locations: none in the page | INFRA | corrected | INFRA: "a redundant and stateless service-oriented architecture (SOA) that simultaneously accepts payments on multiple physical hosting locations". Added |
| 43 | "Takeover between regions: Not public" for Adyen (KEY POINT 3, table, list, take-away) | PEAK | corrected | PEAK (n.d.): "Our active/active, stateless architecture"; "With load balancers in front of every data center, transactions can be equally processed through any available data center. In the event that a data center is unavailable, these load balancers also manage the failover to the other data centers." No topology, timings or treatment of stateful systems. Reworded throughout per ruling 45 |
| 44 | Five live regions: EU, US, AU, NEA, IN | docs.adyen.com/online-payments/web-best-practices | confirmed | "last modified September 2025" removed (ruling 30); scoped to online payments. The cloud Terminal API page also carries an older "Asia Pacific & Southeast (APSE)" endpoint label (not added) |
| 45 | Live endpoints: "you can see the configured data centres and prefixes for your company account"; "a certain data center"; location-based endpoints through support | docs.adyen.com/development-resources/live-endpoints | confirmed | "last modified January 2024" removed (ruling 30); Customer Area and company account glossed |
| 46 | "Its one sentence on rerouting", "alternative routing can be enabled to backup infrastructure" | same; PEAK; adyen.com/knowledge-hub/mitigating-a-ddos-april-2025 | corrected | The quotation is right; "one sentence" was not. Now cites PEAK (row 43) and the incident update displayed as 21 April 2025 ("a DDoS attack targeting services across our European datacenters"; no other region named) |
| 47 | Adyen names no region for terminals (not in the page) | docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud | corrected (added) | "Regional data center overview" assigns each country to a data center region (NL and DE: EU, prefix `live`); "make sure to select the data center closest to your geographical location in your live Customer Area". Added, because Larkfield's Adyen use at these studios is terminals |
| 48 | Adyen privacy statement, version of 4 August 2025: information "may be disclosed to other Adyen group companies outside of the European Economic Area" | adyen.com/privacy-policy | confirmed | URL changed: `/policies-and-disclaimer/privacy-policy` redirects to `/privacy-policy` |
| 49 | India compliance guide requires "a separate company account for your business in India" | docs.adyen.com/online-payments/payments-india-compliance-guide | confirmed | "last modified December 2021" and its "evidence age: 5 years" removed (ruling 30) |
| 50 | The guide "is silent on where Adyen stores the data"; KEY POINT "Adyen has published nothing on where Indian payment data is stored" | INFRA; adyen.com/the-latest/india-expansion-made-easy | corrected | True of the guide, false of Adyen: INFRA (rows 40–41); a product update dated January 2026 says "our own in-country data centers" (read, not cited in the page) |
| 51 | Adyen documents no product cost of its India set-up (table: "Only Stripe has documented the product cost") | docs.adyen.com/online-payments/payments-india-compliance-guide/go-live-india | corrected | Checklist: velocity risk rules "will not work as well for your India company account at first, because they rely on historical transaction data"; block and trust lists are created "in your India company account". Table now: "Both document a product cost; Stripe's list is the more detailed" |
| 52 | Table: Hosting, Stripe | rows 27, 30, 32 | confirmed | — |
| 53 | Table: Hosting, Adyen | rows 35, 37–39 | confirmed | — |
| 54 | Table: Regions an integrator can name, Stripe "None; one base URL" | row 33; sitemap searches | confirmed | — |
| 55 | Table: Regions, Adyen "(2025) … (2024)" | rows 44, 45, 47 | corrected | Dates to "n.d., accessed November 2026"; terminals added |
| 56 | Table: "Size of the footprint", Stripe "Not public", Adyen "no locations" | rows 31, 40 | corrected | Row is now "Where the data centers are", with both documented statements |
| 57 | Table: India, Stripe | rows 18–25 | hedged | See row 25 |
| 58 | Table: India, Adyen "storage location: Not public" | rows 40, 41, 51 | corrected | — |
| 59 | Table: "Personal data leaving Europe … No material difference" | rows 34, 41, 48 | corrected | Adyen states where payments are stored; Stripe does not. Last column rewritten |
| 60 | Table: takeover "Not public / Not public" | row 43; searches | corrected | Stripe cell worded per ruling 39; Adyen cell cites PEAK |
| 61 | Larkfield table, Stripe "Documented" | rows 27, 31, 34 | confirmed | "names no AWS region" |
| 62 | Larkfield table, Adyen "Documented" | rows 41, 43, 47, 48 | corrected | Adds failover stated, EU data center region for German terminals, "stored in Europe" on an undated page; questions adjusted |
| 63 | Scene: "nothing in the draft is on a page either provider has published" | INFRA | corrected | Tom now finds a source for half a clause (Adyen, "stored in Europe"; Europe is not the EU). Still withdrawn as unsourced, as the ledger says |
| 64 | Evidence stops: Stripe's AWS regions and count | searches; row 31 | confirmed (as an absence) | One AWS region name appears in a Terminal hostname on docs.stripe.com/ips (`stripe-point-of-sale-us-west-2.s3.us-west-2.amazonaws.com`); it says nothing about where Stripe runs and was not added |
| 65 | Evidence stops: Stripe's serving model | searches | confirmed (as an absence) | A Stripe job listing (High Availability and Disaster Recovery, n.d.) mentions "cross-region TLS handshakes" and work to "automate disaster detection and failovers"; a July 2026 stripe.dev post on its database fleet mentions "regional distribution", "availability zone imbalance" and "a planned failover". Neither states a serving model; not added |
| 66 | Evidence stops: no Stripe commitment on European residency; "Third-party pages claim one exists; none cites Stripe" | PC; DPA FAQ; SP; support.stripe.com sitemap; dev.to article read | hedged | One third-party page was read (it claims "data localisation options for larger merchants" and links no Stripe page); now "the one I read cites no Stripe page" |
| 67 | Evidence stops: Adyen's cities, operators, exact count | rows 38, 40 | confirmed (as an absence) | — |
| 68 | Evidence stops: "which region holds which merchant's data" | INFRA | unsupported, replaced | Now: whether "stored in Europe" is a commitment, what "Europe" covers, where other data is kept |
| 69 | Evidence stops: "Adyen and India: where Indian payment data is stored" | INFRA | unsupported, replaced | Now: what the isolated India environment changes in features |
| 70 | Evidence stops: takeover "whether one region can take another's traffic" | PEAK | unsupported, replaced | Now: Adyen states failover between data centers; between which, how fast and with what effect on records is not public |
| 71 | Take-away, Established 1 (RBI, DORA) | rows 5, 6, 11–14 | confirmed | 24-hour condition completed |
| 72 | Take-away, Established 2 (hosting, regions) | rows 27–47 | corrected | Adyen's website list and active/active statement added |
| 73 | Take-away, Established 3 (Stripe's India cost) | rows 20–22 | confirmed | "(page updated 2023)" |
| 74 | Synthesis: "the providers say almost nothing" | rows 40–43 | hedged | "Stripe says almost nothing and Adyen a few undated sentences" |
| 75 | Excerpt and lead: "four statements and no more" | rows 31, 40–43 | corrected | "four kinds of statement", with Adyen's regions and failover statement |
| 76 | Figure 3 caption and alt: Adyen's regions "without locations" | row 40 | corrected | Caption and alt only; prompt untouched |
| 77 | Hand-off: Stripe rents cloud capacity, Adyen owns its data centers | rows 27, 35 | confirmed | — |
| 78 | Source dates and titles in Sources and Evidence | each page | confirmed, with corrections above | Unused entries: none. Added: INFRA, PEAK, cloud integration, India go-live checklist, incident update, SP |

Counts: 78 rows; 48 confirmed (5 of them absences), 21 corrected, 5 hedged, 3 unsupported and replaced, 0 unreachable, 1 not checked against a primary source.

## Could not verify, and what I did

- **Whether the RBI rule was touched by the RBI's November 2025 consolidation of circulars.** Not read. The circular and FAQ are live on rbi.org.in and absent from its withdrawn list; the page says exactly that.
- **"Then" chief technology officer (Singleton).** Trade press only.
- **Adyen's Customer Area ("configured data centres", "Select a data center").** Behind login; quoted from documentation only.
- **`status.stripe.com` and `status.adyen.com`** were not read (ruling 43e); the page makes no claim about them.
- An absence cannot be proved. The seven "not public" items are worded as "not found", with the places searched.

## Stripe's India page: exact wording on Radar (for the author's reconciliation list)

From `https://stripe.com/india-data-storage-faq` ("Last updated: May 16, 2023"), section "Radar":

> Radar core machine learning fraud detection remains live, along with ZIP/CVC check rules.
>
> Radar for Fraud Teams features will be temporarily free in India until further notice. These include: Modifying Radar’s block threshold for high-risk payments; Manual review rules and the review queue; Risk Insights and the related payments list; Blocklists and allowlists; Dispute win ratings; API access to lists and reviews; API access to specific risk scores
>
> Stripe Radar & Radar for Fraud Teams will be free for India until further notice.

No fraud feature is described as disabled. The features described as "temporarily disabled in India" are Card Updater, Revenue Recognition in Stripe Billing, and Sigma. The API Reference "remains live, but some personalized content, such as sample API responses will be unavailable until further notice".

## Sentences in the journal-spec entry (copied into spec.json, locked by the validator) that the sources contradict

Only the author may change `journal-spec.json`; the post spec must equal it in these fields, so they are unchanged and listed in the spec's open questions.

1. `thesis.claim`: "Stripe runs on Amazon Web Services and names no regions" — PC names "our data centers located in the United States and India" (login and identity data).
2. `thesis.claim`: "Adyen runs its own infrastructure and names five integration regions without locations" — INFRA names Europe, the United States, India, Singapore, Japan and Australia.
3. `thesis.claim`: "while Adyen has published nothing on where Indian payment data is stored" — INFRA: "All payments processed are stored in Europe and our isolated India environment."
4. `thesis.claim`: "and neither says how one region takes over from another" — holds for *how*; PEAK states that load balancers "manage the failover to the other data centers".
5. `thesis.how_why`: "Adyen's documentation (last modified 2025) names five regions" (ruling 30); "Nothing first-party names Stripe's regions, Adyen's locations, or either company's failover between regions, and no Adyen statement on the storage of Indian payment data was found."
6. `thesis.so_what`: "a set of named regions without addresses".
7. `intent.outcome.know[3]`: "What is not public for either company: region names and counts for Stripe, data-center locations for Adyen, and whether or how one region takes over from another."
8. AC-2 `expected`: "some features (Stripe listed its card updater and some billing and fraud features) are disabled or changed" — see the Radar wording above: fraud features were made free, not disabled.
9. AC-4: "does not exceed about 3,000 words" — the corrected page is 3,777 words by `check_draft.py`; `length.max_words` in spec.json was raised from 3,200 to 3,800.

## Ledger conflicts

None. The ledger line for this chapter says Tom's draft "was withdrawn as unsourced"; the page now says he found a source for half a clause and none for the rest, which agrees.

## For other pages

- Chapters 40, 41 and 46 title the 2023 Stripe press release "Amazon and Stripe sign expanded global agreement"; the page's headline is "Amazon-Stripe partnership accelerates ecommerce and streamlines online payments".
- Chapters 37, 41 and 47 date Adyen's DDoS incident update 2025-04-22; the page displays "April 21st, 2025" (rulings 25 and 43d).
- Chapter 41 dates the Architect post 2026-08-24; displayed date is 23 August 2026 (ruling 25).
- Any page saying Stripe publishes no data-center location should see row 31; any page on Adyen's India set-up should see rows 40, 41, 50 and 51.
- The scenario-ledger line for chapter 39 needs no change.
