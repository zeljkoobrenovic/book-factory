---
title: "Where the Data Lives: Multi-Region Operation and Data Residency"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What decides where a payment platform runs and where its data stays? A localization law where one applies, and the provider's hosting model elsewhere; Stripe and Adyen have documented their hosting and a few sentences about regions, so the rest is a question to put to them in writing."
permalink: payment-multi-region-and-data-residency
timetoread: 16 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what decides where payment data is stored, what Stripe and Adyen have published about their regions, and exactly where that record stops.

> **KEY POINTS:**
>
> * **Law decides first, hosting second.** Where a localization law applies, it fixes where payment data is stored before any latency or availability goal. India's 2018 rule did, and Stripe's page on its response lists the cost in features.
> * **The documented record is short.** Stripe runs on Amazon Web Services and names no AWS region; Adyen runs its own data centers and lists them by continent or country, no finer. Stripe says it stores Indian payment data only in India, and Adyen describes an isolated India environment.
> * **How takeover works is not public for either.** Adyen documents an "active/active" architecture whose load balancers fail over between data centers, without topology or timings; Stripe describes it only for billing usage events. Ask in writing; do not infer.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Single Rail** — a team that assumes its provider survives the loss of a region depends on something it has never checked.
> * **The Borrowed Blueprint** — a multi-region design is copied from a topology the provider has never published.

<br>
The shards of [[payment-data-stores-and-consistency]] were divided by engineers, for size and load, and both companies have described them at length. This chapter's divisions are made by countries and laws, and here both companies have published very little. Take one from a design document: "Stripe runs active-active in three AWS regions, so our European members' data never leaves the EU." As of November 2026 the public record supports one word of it: Stripe has said, in a 2023 press release and since, that it runs on AWS (Amazon Web Services).

**Where a localization law applies, it settles where payment data is stored before any latency or availability goal; elsewhere the provider's hosting model does.** About the two providers the record supports four kinds of statement and no more: Stripe's hosting, Adyen's hosting and the regions it names, what each has said about India, and Adyen's statement that it serves from several data centers at once and fails over between them. **Neither describes how takeover works, between which places or how fast**.

**Where we are in the payment's journey.** When Mila Janssen bought a €120.00 ten-class pass from Studio Noord on Tuesday 9 March 2027 at 19:42, the answer came from systems whose location this book has not asked about. This chapter asks where the record of that payment is kept, and who decided.

The chapter starts with a questionnaire that reaches Larkfield in April 2027. It then names the two pulls toward regions and the three ways to place data, reads India's storage rule, sets out what each company has published about where it runs, and compares them. It ends with Larkfield's answer, the way an unsourced answer fails, and a list of where the evidence stops.

## Setting the Scene at Larkfield: One Question, Two Providers

In April 2027 a pilates chain in Hamburg sends a data-protection questionnaire to Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]). One line reads: "Where is our members' payment data stored, and does it leave the European Union?" The chain is one of the 1,140 studios that take online payments through Stripe and front-desk payments on Adyen terminals, so its members' data is held by both providers. Jonas Weber, who leads risk and compliance, forwards it to Femke de Graaf, the head of payments engineering.

Tom Hendriks, who built the payment service, drafts a reply in ten minutes: both providers keep European data in EU regions and fail over inside the EU. Femke returns it asking for a source for each clause. He finds one, for half a clause: Adyen's website says the payments it processes are stored in Europe. Europe is not the EU, and nothing either provider has published says where Stripe stores European data or between which places either provider fails over.

## Two Pulls Toward Regions: Distance and Law

Distance is the pull engineers choose: a payment waits on every network hop, so a platform puts the systems that answer close to where payments start. An Adyen engineering post of October 2025 puts both pulls in one sentence, "data must remain close to producers to reduce latency and meet regulations, while also being centralized for analytics", and adds that nobody wants to wait at a cashier in Australia "while your payment was being sent to Europe".

Law is the pull engineers do not choose, and it comes in two strengths that are often confused. **Data residency** is a fact: where data is stored. **Data localization** is a law that requires data to be stored, sometimes only, in one country. The European rules a Dutch platform meets are not localization laws. The General Data Protection Regulation (GDPR), the privacy law, conditions transfers: Stripe's data processing agreement FAQ (n.d., accessed November 2026) describes standard contractual clauses, contract terms issued by the European Commission, as a way to "transfer personal data to certain countries, outside of the European Economic Area, including the United States". The Digital Operational Resilience Act (DORA), the EU regulation on the operational resilience of financial firms (adopted in December 2022, applied from 17 January 2025; evidence age: nearly 4 years, in application), says in recital 82 that it "does not impose a data localisation obligation as it does not require data storage or processing to be undertaken in the Union".

Regions must then share the work. In **active-passive** operation one region serves and another waits to take over. In **active-active** operation several serve at once. On a money path the second raises a question from the previous chapter, which region may write a given balance, and any takeover leaves payments in flight with the unknown outcome of [[payment-reliability-and-availability]]. Some companies publish their choice: Uber's 2018 engineering account of its payments platform lists "high reliability through an active-active architecture" among its design goals. **(Evidence age: 8 years; the current system may differ.)**

A law adds a third placement, a partition by country. The three cost a money path different things, and the table's last column is the point of this chapter.

| Placement | What it buys | What it costs on a money path | Documented for Stripe or Adyen? |
| --- | --- | --- | --- |
| Active-passive | One place writes each record | Idle capacity, and a takeover that is rarely exercised | Not stated by either |
| Active-active | No idle region; losing one removes a share of capacity | A rule for which region writes which record | Stripe: not found for payments; for billing usage events, two regions at once (2025). Adyen: "active/active", with failover between data centers (documentation, n.d., accessed November 2026); the write rule: Not public |
| Partition by jurisdiction | Compliance with a localization law | Identifiers and features that stop at the border | Stripe, India (page updated 2023); Adyen, an "isolated India environment" (n.d., accessed November 2026) |

<!-- illustration-placeholder
{
  "id": "39-three-placements",
  "status": "pending",
  "asset": "assets/images/39-multi-region-and-data-residency/39-three-placements.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of the three placements",
  "visual_goal": "Show the three ways to place payment data across regions: one writer with a standby, several writers, and a country walled off by law.",
  "prompt": "Three-panel structural diagram with thin dividers, panels tagged \"Active-passive\", \"Active-active\" and \"Partitioned\". Panel one: two generic server racks side by side; the left rack is bright blue with a pen icon above it labeled \"writes\", the right rack is pale gray with a small clock icon labeled \"waits\"; a thin dashed arrow labeled \"copy\" runs from the left rack to the right rack. Panel two: two bright blue server racks, each with a pen icon above it labeled \"writes\"; a double-headed teal arrow labeled \"agree\" connects them, with a small orange question mark sitting on the arrow. Panel three: two server racks separated by a tall green wall with a small courthouse icon on top labeled \"law\"; each rack holds its own stack of records; an orange arrow labeled \"blocked\" starts at the left rack and stops at the wall. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Three panels: one server writes while a second waits; two servers both write and must agree; two servers stand on either side of a wall set by law, and a copy is blocked at the wall.",
  "caption": "Three placements: one region writes and another waits, several regions write and must agree, or a law walls one country's data off from the rest."
}
-->

## When a Law Decides: India's Storage Rule

The documented case of the third placement is India. On 6 April 2018 the Reserve Bank of India (RBI), the central bank, issued a circular: "All system providers shall ensure that the entire data relating to payment systems operated by them are stored in a system only in India." The stated reason is supervision, not privacy: "it is important to have unfettered supervisory access to data". A clarification of 26 June 2019, published as frequently asked questions, separated processing from storage. There is "no bar on processing of payment transactions outside India", but the data "should be deleted from the systems abroad and brought back to India not later than the one business day or 24 hours from payment processing, whichever is earlier". It reaches "payment gateways, third party vendors and other entities" engaged by licensed firms. **(Evidence age: 8 and 7 years; on 17 November 2026 the circular was not on the RBI's list of withdrawn circulars.)**

Stripe's page on its response, last updated on 16 May 2023, records what complying cost. It says "we’re moving the servers that store India data to be located within the country" and calls this "a substantive infrastructure change". "Payment information can no longer be cloned into or out of India" (cloning copies a saved payment method between a platform and its connected accounts). The card fingerprint changed: "the same card details can have two different fingerprints, one for India and another for the rest of the world". Card Updater (which replaces expired card numbers), revenue recognition in Billing (the accounting of when a sale counts as earned) and the Sigma reporting product were each "temporarily disabled in India" from 30 April 2021. The page does not say whether they have returned. **(Evidence age: 3.5 years.)** The 2023 page says "we’re moving"; two current pages state the result. Stripe's Privacy Center (n.d., accessed November 2026) says: "Where required payment system data will be stored only on servers in India in accordance with the RBI data localization requirements." Its list of service providers (last updated 27 September 2026) says "Stripe India Private Limited stores certain data on servers located in India".

The fingerprint is the telling line. It is an identifier that lets a merchant recognize the same card number across customers without seeing the number. It was global, and the law made it two. So **a localization rule is a product constraint as much as a storage one**: the disks move, and so does the edge of every feature built on an identifier that used to cross the border.

> **INFERENCE, NOT DOCUMENTED:** Stripe documents the two fingerprints and the end of cloning, not what follows for a merchant's own logic. I infer that duplicate-card checks, block lists and fraud signals keyed on the fingerprint stop matching between Indian and other accounts, and that saved cards have to be collected again on the other side of the border.

<!-- illustration-placeholder
{
  "id": "39-one-card-two-fingerprints",
  "status": "pending",
  "asset": "assets/images/39-multi-region-and-data-residency/39-one-card-two-fingerprints.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the inference block on the fingerprint",
  "visual_goal": "Make memorable that a localization law turns one global identifier for a card into two that do not match.",
  "prompt": "Conceptual before-and-after illustration in two halves separated by a thin vertical divider, the left half tagged \"Before\" and the right half tagged \"After\". Left half: one generic unbranded payment card at the top; a single teal arrow runs down from it to one round fingerprint icon labeled \"one ID\"; beneath the fingerprint a wide flat world map strip in pale blue with no borders drawn. Right half: the same generic payment card at the top; two arrows run down from it, a teal arrow to a fingerprint icon on the left labeled \"ID A\" and an orange arrow to a differently patterned fingerprint icon on the right labeled \"ID B\"; between the two fingerprints stands a tall green wall with a small courthouse icon on top labeled \"law\"; a dashed gray line labeled \"no match\" runs from one fingerprint toward the other and stops at the wall. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Before: one card maps to one identifier across the world. After: the same card maps to two different identifiers on either side of a wall set by law, and they no longer match.",
  "caption": "A localization law turns one global identifier for a card into two that do not match across the border."
}
-->

## What Each Company Has Published About Where It Runs

Outside such a law, the provider's hosting decides where data sits. Stripe's is rented. A Stripe press release of 23 January 2023 says "Stripe has long relied on AWS to provide the core compute infrastructure on which Stripe is built" and quotes its then chief technology officer, David Singleton: "We couldn’t run without AWS—and we wouldn’t want to." **(Evidence age: nearly 4 years; confirmed since.)** An AWS blog post co-written with Stripe engineers in October 2024 describes "a sophisticated microservice environment built on top of AWS", and Stripe's security documentation (n.d., accessed November 2026) puts its card data vault "in an isolated Amazon Web Services (AWS) environment". No Stripe source I found names an AWS region that Stripe runs in, or says whether several regions serve payments at once or how one takes over from another. Its one published two-region design, in a January 2025 post, processes billing usage events "in two geographic regions simultaneously", with automatic failover. The only places named are countries, and not for payment data: the Privacy Center describes a "multi-region infrastructure" for login and identity data that includes "our data centers located in the United States and India" and "does not extend to any transactional information". The API reference (n.d., accessed November 2026) gives one base URL, `https://api.stripe.com`, and the Privacy Center says "Personal Data may be transferred to, and processed, in any country where we do business", "including to the United States".

Adyen's hosting is owned. Its 2021 architecture post says: "We manage our own infrastructure in several data centers around the world", and "The reasons we are not deploying to the cloud are part historical, part legal, and part technical." **(Evidence age: 5 years; confirmed by the sources that follow.)** In October 2025 its chief technology officer wrote of "end-to-end ownership over every layer, from our data centers to our application logic". An August 2026 engineering post gives an order of magnitude, "tens of thousands of hosts spread across tens of data centres", and the H1 2026 results say "The majority of our CapEx is invested in data centers". None of these names a place. Adyen's corporate website does, down to a continent or a country. Its infrastructure page (n.d., accessed November 2026) says: "Adyen currently hosts its main systems in separate data centers in Europe, the United States, India, Singapore, Japan and Australia", and "All payments processed are stored in Europe and our isolated India environment." The same page describes an architecture that "simultaneously accepts payments on multiple physical hosting locations". Adyen's documentation on peak season readiness (n.d., accessed November 2026) calls it an "active/active, stateless architecture" and adds: "In the event that a data center is unavailable, these load balancers also manage the failover to the other data centers." Neither page says which data centers back which, how long a failover takes, or what happens to systems that hold state. The infrastructure page is undated and its Dutch and Portuguese versions list fewer places, so I read it as a summary, not a commitment.

What an integrator can see of that estate is a set of regions. Adyen's documentation for web integrations (n.d., accessed November 2026) serves its client-side library per region: "Europe (EU) live", "United States (US) live", "Australia (AU) live", "Northeast Asia (NEA) live" and "India (IN) live". The live endpoints page (n.d., accessed November 2026) says that in the Customer Area, Adyen's merchant dashboard, "you can see the configured data centres and prefixes for your company account" (the top level of an Adyen account), and that a merchant who needs "a certain data center" can ask support for location-based endpoints. For terminals, the cloud integration page (n.d., accessed November 2026) assigns each country to a data center region, the Netherlands and Germany to EU, and tells merchants to "select the data center closest to your geographical location". On rerouting, the live endpoints page says "alternative routing can be enabled to backup infrastructure", not where that is, and an incident update dated 21 April 2025 describes a denial-of-service attack on "our European datacenters" and names no other region. The storage sentence is not a promise that data stays put: Adyen's privacy statement (version of 4 August 2025) says information "may be disclosed to other Adyen group companies outside of the European Economic Area". On India, its compliance guide (n.d., accessed November 2026) requires "a separate company account for your business in India", and its go-live checklist for India (n.d., accessed November 2026) shows a cost: velocity risk rules, which count attempts over time, "will not work as well for your India company account at first, because they rely on historical transaction data".

<!-- illustration-placeholder
{
  "id": "39-two-shapes-of-answer",
  "status": "pending",
  "asset": "assets/images/39-multi-region-and-data-residency/39-two-shapes-of-answer.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on Adyen's five regions",
  "visual_goal": "Show that the documented answer to 'where is the data' has a different shape for each provider: a rented cloud with unnamed regions, and five named integration regions on sites listed by continent or country, with no cities.",
  "prompt": "Structural comparison in two halves separated by a thin vertical divider, the left half tagged \"Provider A\" and the right half tagged \"Provider B\". Left half: one large soft blue cloud shape labeled \"rented cloud\"; inside the cloud three small server racks, each covered by a gray question mark instead of a name; below the cloud a single thick teal line leads down to one plug icon labeled \"one address\". Right half: five separate small server buildings in a row, each with a flag-shaped tag reading \"EU\", \"US\", \"AU\", \"NEA\" and \"IN\"; a bracket above the five buildings labeled \"own sites\"; below the buildings a wide pale blue map strip with no borders drawn, carrying six solid teal map pins labeled \"Europe\", \"United States\", \"India\", \"Singapore\", \"Japan\" and \"Australia\", and beside the strip a small gray tag labeled \"no cities\". At the bottom center, spanning both halves, a small studio owner holding a clipboard looks up at both sides. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Provider A is a rented cloud whose regions are question marks behind one address; Provider B is five named regions on its own sites, with six map pins at continent or country level and a tag reading no cities.",
  "caption": "Two shapes of answer: Provider A (Stripe) is a rented cloud whose regions are not named; Provider B (Adyen) names five integration regions and lists its own data centers by continent or country, with no cities."
}
-->

## Stripe and Adyen: Where They Differ

The last column of this table is my reading, and is inference.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Hosting | AWS (2023; 2024; documentation n.d., accessed November 2026) | Own infrastructure in data centers (2021; 2025; 2026) | The clearest documented architectural difference between the two |
| Regions an integrator can name | None; one base URL (n.d., accessed November 2026) | Five for online payments: EU, US, AU, NEA, IN; location-based endpoints on request; a data center region per country for terminals (all n.d., accessed November 2026) | Region is part of Adyen's integration and not of Stripe's |
| Where the data centers are | No AWS region named; "data centers located in the United States and India" for login and identity data (n.d., accessed November 2026) | "Europe, the United States, India, Singapore, Japan and Australia" (n.d., accessed November 2026); "tens of data centres" (2026); no cities | Adyen states more than Stripe, and neither names a city |
| India | Servers moving into the country, features changed (page updated 2023); data stored on servers in India (n.d., accessed November 2026; 2026) | Data centers in India and an "isolated India environment" (n.d., accessed November 2026); a separate company account whose velocity risk rules start without history (n.d., accessed November 2026) | Both document a product cost; Stripe's list is the more detailed |
| European data | No storage location stated; personal data may be transferred, "including to the United States" (n.d., accessed November 2026) | Payments "stored in Europe" (n.d., accessed November 2026); information may go to group companies outside the EEA (2025) | Adyen states where payments are stored and Stripe does not; neither promises that data stays in the EU |
| Several data centers at once, and takeover | Not found for payments (documentation, help center, site, engineering posts; November 2026); two regions with failover for billing usage events (2025) | "active/active"; load balancers "manage the failover to the other data centers" (n.d., accessed November 2026); topology, timings and mechanism: Not public | Adyen states that it fails over and Stripe does not; how is a question to ask of both |

On Stripe there is no region to choose, so residency is a question for the contract. On Adyen the region is a setting: check which data centers your company account is configured for, and load the client-side resources that match. On both, whether another region can take your traffic is a question to put in writing.

## In Practice at Larkfield: The Answer That Went Back

Femke's reply says first that the chain's members' payment data is held by two providers under two hosting models, as Larkfield's is as a whole: 44% of 2026 member payment volume went through Stripe and 56% through Adyen. Then it gives each provider two columns.

| Provider | Documented | Asked in writing |
| --- | --- | --- |
| Stripe (online payments) | Runs on AWS; names no AWS region; data may be processed outside the EEA | In which regions is our data stored? Is an EU-only commitment available by contract? |
| Adyen (terminals) | Own data centers, with failover between them stated; German terminals assigned to the EU data center region; payments "stored in Europe", on an undated web page; data may go to group companies outside the EEA | Where are our account's configured data centers? Is "stored in Europe" a commitment, and does Europe mean the EEA? Which data centers take over our traffic, and how fast? |

Larkfield has no market with a localization law, so Femke also writes the India lesson into the market-entry checklist. In such a country stored cards would have to be collected again, since provider tokens (K4) would not cross the border. Larkfield's own member id would be the only payer identifier that does. The rehearsed switch between providers (K8) would need a second provider inside the country, and every export to the data warehouse would need review.

## When It Goes Wrong: The Sentence Nobody Can Source

An inferred topology fails late. Had Tom's draft gone out, "fail over inside the EU" would have become a commitment to a customer, found to be a guess when an auditor asked for evidence or a regional outage behaved differently from the recovery plan. Detection is cheap: every clause about a provider's regions carries a source and a date, or is deleted; recovery is the provider's written answer. The one failover Larkfield can rehearse is its own, the K8 switch. The two providers' hosting is documented as different; I judge that this makes one cause less likely to stop both, but nothing either has published shows it.

## Where the Evidence Stops

As of 17 November 2026 I found none of these in either company's documentation (index and sitemap), help center, engineering blog, legal pages or site.

- **Stripe's regions:** which AWS regions it uses, and how many.
- **Stripe's serving model:** whether the API is served from several regions at once.
- **Stripe and European residency:** where European payment data is stored, and any commitment to keep it in Europe. Third-party pages claim one exists; the one I read cites no Stripe page.
- **Adyen's sites:** the cities, the operators of the facilities, and a count more exact than "tens".
- **Adyen's data placement:** whether "stored in Europe" on its website is a commitment, which countries "Europe" covers, and where data other than payments is kept.
- **Adyen and India:** what its "isolated India environment" changes in features, as a list like Stripe's.
- **Takeover:** Stripe says nothing for payments. Adyen says its load balancers fail over between data centers, and not between which ones, how fast, or what happens to a record being written.

## What to Take Away

**Established.**

- India requires payment system data to be stored only in India (RBI, 2018) and allows processing abroad if the data returns within one business day or 24 hours, whichever is earlier (2019). The EU's resilience regulation imposes no localization duty (recital 82).
- Stripe runs on AWS (2023, 2024, current documentation); Adyen runs its own infrastructure (2021, 2025, 2026), documents five integration regions, lists its data centers by continent or country on its website, and states that it runs "active/active" with failover between data centers (all n.d., accessed November 2026).
- Stripe documented what localization cost in India: no cloning across the border, two fingerprints for one card, features switched off (page updated 2023).

**Depends on context.**

- Whether residency matters to you depends on your markets and your customers' contracts.
- Whether a region is yours to choose depends on the provider: on Adyen it is a setting, on Stripe none is offered in public documentation.
- What a localization rule costs depends on how many of your features hang on an identifier that crosses borders.

**The author's synthesis.**

- The best-documented topology in this chapter is the one a regulator forced into the open. Where no law speaks, Stripe says almost nothing and Adyen a few undated sentences, so the opening sentence keeps one word, AWS, and I would rewrite the rest as three questions to Stripe: which regions, served how, and what is committed about European data.
- For each provider I keep one page with two columns, "documented, with source and date" and "asked in writing, with the answer". No sentence about regions or failover goes into a contract or a recovery plan unless it is in one of them.

## Questions to Ask

1. In which country or region is our account's payment data stored, and where is that written?
2. Does any market we serve, or plan to enter, have a localization law for payment data?
3. Which of our features rely on an identifier (a card fingerprint, a token, a customer id) that would stop at a border?
4. Can we choose or see the region our account uses, and does our client-side code match it?
5. Can one of the provider's regions take over from another, and what has it said in writing?
6. How do we find the payments that were in flight during such a takeover?
7. Which sentences in our contracts and recovery plans describe a provider's regions, and what is each one's source?

This chapter documented one clear difference in hosting: Stripe rents cloud capacity and Adyen owns its data centers. That has a consequence when load arrives all at once: capacity is scaled on demand on one side and bought ahead on the other, and on both a merchant meets its own per-customer limit first. [[payment-peak-load]] takes that up.

## Sources and Evidence

*Company, product and investor sources*

- [How we built it: Usage-based billing](https://stripe.com/blog/how-we-built-it-usage-based-billing), Taras Mitran and Karan Dhabalia, Stripe, 2025-01-28 — usage events processed in two regions at once with automatic failover; not about payments.
- [Amazon-Stripe partnership accelerates ecommerce and streamlines online payments](https://stripe.com/us/newsroom/news/amazon-and-stripe), Stripe newsroom, 2023-01-23 — Stripe's reliance on AWS; the Singleton quotation (evidence age: nearly 4 years).
- [How Stripe architected massive scale observability solution on AWS](https://aws.amazon.com/blogs/mt/how-stripe-architected-massive-scale-observability-solution-on-aws/), AWS Cloud Operations blog, co-written with Stripe engineers, 2024-10-24 — "built on top of AWS".
- [Security at Stripe](https://docs.stripe.com/security), Stripe documentation, n.d., accessed 2026-11 — the card data vault in an isolated AWS environment.
- [API reference](https://docs.stripe.com/api), Stripe documentation, n.d., accessed 2026-11 — the single base URL.
- [Important updates on Stripe data storage migration in India](https://stripe.com/india-data-storage-faq), Stripe, last updated 2023-05-16 — the move of the servers that store India data; cloning, fingerprint and feature changes (evidence age: 3.5 years).
- [Privacy Center](https://stripe.com/us/legal/privacy-center), Stripe, n.d., accessed 2026-11 — storage of payment system data in India; international transfers of personal data; data centers in the United States and India for login and identity data.
- [Stripe Service Providers, Sub-Processors & Affiliates](https://stripe.com/us/legal/service-providers), Stripe, last updated 2026-09-27 — certain data stored on servers in India.
- [Data Processing Agreement FAQs](https://stripe.com/us/legal/dpa/faqs), Stripe, n.d., accessed 2026-11 — transfer mechanisms for European personal data.
- [Design to Duty: How we make architecture decisions at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture), Adyen, 2021-07-28 (updated June 2022) — own infrastructure in several data centers; reasons for not using a public cloud (evidence age: 5 years).
- [Strengthening our platform resilience](https://www.adyen.com/knowledge-hub/strengthening-our-platform-resilience), Tom Adams, Adyen, 2025-10-31 — ownership "from our data centers to our application logic".
- [Building a GlobalStream: Replication Challenges and Optimizations](https://www.adyen.com/knowledge-hub/building-a-global-stream), Gaurav Singh and Luciano Sabença, Adyen, 2025-10-06 — data close to producers for latency and regulation.
- [We built Architect for humans. Agents made it transformative.](https://www.adyen.com/knowledge-hub/architect-blog-1), Mat Jones, Omar Hommos and Micaela Stump, Adyen, 2026-08-23 — "tens of data centres".
- [Adyen publishes H1 2026 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne), Adyen, 2026-08-13 — capital expenditure invested in data centers.
- [Infrastructure](https://www.adyen.com/infrastructure), Adyen corporate website, n.d., accessed 2026-11 — where Adyen hosts its main systems; where processed payments are stored; acceptance in several hosting locations at once (the Dutch and Portuguese versions of the page list fewer places).
- [Incident update: Mitigating a DDoS attack on April 21, 2025](https://www.adyen.com/knowledge-hub/mitigating-a-ddos-april-2025), Tom Adams, Adyen, 2025-04-21 — the attack on "our European datacenters".
- [Peak season readiness](https://docs.adyen.com/industries/peak-season), Adyen documentation, n.d., accessed 2026-11 — the "active/active, stateless architecture"; load balancers that manage failover between data centers.
- [Best practices for web integrations](https://docs.adyen.com/online-payments/web-best-practices), Adyen documentation, n.d., accessed 2026-11 — the five live regions for client-side resources.
- [Live endpoints](https://docs.adyen.com/development-resources/live-endpoints), Adyen documentation, n.d., accessed 2026-11 — configured data centers per company account; location-based endpoints; alternative routing.
- [Building a cloud integration](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud), Adyen documentation, n.d., accessed 2026-11 — the data center region per country for terminals; selecting a data center.
- [Payments India compliance guide](https://docs.adyen.com/online-payments/payments-india-compliance-guide), Adyen documentation, n.d., accessed 2026-11 — a separate company account for local processing in India.
- [India go-live checklist](https://docs.adyen.com/online-payments/payments-india-compliance-guide/go-live-india), Adyen documentation, n.d., accessed 2026-11 — velocity risk rules start without history in the India company account.
- [Privacy statement](https://www.adyen.com/privacy-policy), Adyen, version of 2025-08-04 — disclosure to group companies outside the EEA.

*Standards, regulation and official documentation*

- [Storage of Payment System Data, RBI/2017-18/153](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0), Reserve Bank of India, 2018-04-06 — the storage rule and its reason (evidence age: 8 years).
- [Frequently Asked Questions: Storage of Payment System Data](https://www.rbi.org.in/Scripts/FAQView.aspx?Id=130), Reserve Bank of India, 2019-06-26 — processing abroad, the 24-hour return, the entities in scope (evidence age: 7 years).
- [Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (DORA)](http://publications.europa.eu/resource/celex/32022R2554), Official Journal of the European Union, 2022-12-27 (adopted 2022-12-14) — recital 82 on localization; application from 17 January 2025 (evidence age: nearly 4 years; in application).

*Research and practitioner sources*

- [Engineering Uber's Next-Gen Payments Platform](https://www.uber.com/blog/payments-platform/), Uber Engineering, 2018-12-05 — an example of a published active-active design goal (evidence age: 8 years).

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
