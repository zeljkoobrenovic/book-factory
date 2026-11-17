# Research brief: Reliability, data stores, regions, peak load and safe change at Stripe and Adyen

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 37 (reliability and availability), 38 (data stores and consistency), 39 (multi-region and data residency), 40 (peak load), 41 (safe change: deploys, migrations, incidents), and parts of 12, 18, 20, 21, 46 and 47. This is the brief where invented internals are the biggest risk. It is an inventory: what each company has published about its own infrastructure and engineering practice, with dates, and a plain statement of what does not exist in public.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted from the fetched page. The date is the source's publication date; undated documentation, legal and status pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a secondary source (trade press, a search-result summary of a talk's slides, a third-party copy), not a primary page read in this session. The kind of source is named.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including **every** statement about how Stripe or Adyen works internally beyond what the company has published.

**Evidence age matters more here than in any other brief.** Engineering blog posts describe a system at one moment. Stripe's best-known infrastructure posts are from 2017 to 2019; Adyen's architecture series is from 2018 to 2021. Every source published before November 2023 is flagged **(evidence age: N years)** with a note on whether newer material confirms, updates or contradicts it. A writer may say "in 2017 Stripe described …", never "Stripe uses …", for a flagged source.

**The asymmetry to keep in mind.** Stripe publishes many named-author engineering posts with numbers, plus reliability figures in its annual letters and Black Friday press releases, but almost nothing about where its systems run. Adyen publishes fewer posts, mostly about PostgreSQL, but is explicit that it runs its own data centers, and as a listed bank it publishes an audited annual report with a risk section. Neither publishes its topology, its failover design, or routine postmortems.

**Research limitation.**

- **Stripe's localized site.** stripe.com serves Dutch text to this session's IP address by default. Press releases were re-fetched from `stripe.com/us/…` and quotes below are from the English pages. The BFCM 2022 press page (`/newsroom/news/bfcm2022`) returned 404; the 2022 figure comes from the annual letter instead.
- **Stripe's "Game day exercises at Stripe" (2014)** no longer exists at its original URL (it redirects to the blog index). It was read from an Internet Archive snapshot of 22 June 2021; the original publication date is not visible in the snapshot and is given as 2014 from memory of the post, which is an assumption.
- **Stripe's status page** has moved: `status.stripe.com` now loads a shell whose incident feed points to `www.stripestatus.com`. The old endpoint `status.stripe.com/current/full` still answers, but with a snapshot frozen on 9 February 2024. Incident history was read from `www.stripestatus.com/history.json` (pages 1 to 12, back to December 2023). No incident in the 50 most recent carried a postmortem update.
- **Adyen's status page** is rendered client-side. Its history endpoint (`status.adyen.com/api/incident-messages/history?year=…`) returned exactly three items per month for 2024 to 2026 and nothing for 2023, so it is a truncated view. Nothing below may be read as "Adyen had no incident of type X".
- **Adyen's Annual Report 2025** could not be downloaded from `investors.adyen.com` (the link is generated client-side). The text was read from a copy of the printed version hosted by the German Bundestag lobby register; that copy states it is not the official ESEF filing. Page references are omitted for that reason.
- **Kafka Summit London 2022 talk by Stripe**: only the abstract on Confluent's site was read. Slide-level figures (the SLO wording) come from a search-result summary and are tagged WIDELY REPORTED.
- **Not found after searching**: any Stripe statement naming its cloud regions or the number of regions the API runs in; any Stripe public SLA with a percentage; any Adyen statement naming data-center cities, colocation providers or the count of data centers; any Adyen engineering post on deployment frequency for the whole platform after 2018; any Checkout.com first-party architecture source (the AWS case-study URLs tried returned 404); any public detailed postmortem by Adyen; any public Stripe root-cause analysis after July 2019 other than the one paragraph in the 2023 annual letter.
- **PayPal** is not covered beyond a pointer: its Medium engineering feed was fetched and contains no reliability or data-store post in its last ten items (2023 to 2026). No PayPal claim is made in this brief.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: status-page figures (rolling 30-day windows), documented rate limits, BFCM figures (new ones are due in early December 2026), Adyen's capital-expenditure guidance, the location of Stripe's engineering blog (it moved from `stripe.com/blog/engineering` to `stripe.dev/blog`), and regulation in progress.

---

## PART 0: The inventory

### 0.1 Stripe: what exists, by date

Stripe's engineering posts now live at `stripe.dev/blog`; older posts are still served at `stripe.com/blog/<slug>`. The index listed 128 posts on 17 November 2026, of which 28 are tagged Engineering and 7 Infrastructure [VERIFIED: https://stripe.dev/blog, n.d., accessed 2026-11]. Most of the 128 are integration tutorials for Stripe's customers, not accounts of Stripe's own systems [ASSUMPTION/JUDGEMENT from reading the titles].

| Date | Title | Author(s) | What it documents | Age flag |
| --- | --- | --- | --- | --- |
| 2014 (see limitation) | Game day exercises at Stripe | not captured | Failure-injection exercise on a fraud-scoring service; a Redis failover lost all data | **(evidence age: about 12 years)** |
| 2016-10-18 | Introducing Veneur: high performance and global aggregation for Datadog | Cory Watson | Metrics pipeline; migration to Datadog | **(evidence age: 10 years)**; updated by the 2024 AWS post |
| 2017-02-02 | Online migrations at scale | Jacqueline Xu | Four-step dual-write migration of Subscriptions | **(evidence age: 9 years)** |
| 2017-02-22 | Designing robust and predictable APIs with idempotency | Brandur Leach | Idempotency keys, backoff, jitter | **(evidence age: 9 years)**; current behavior is in the API reference |
| 2017-03-30 | Scaling your API with rate limiters | Paul Tarjan | Four limiters, load shedding | **(evidence age: 9 years)**; limits themselves are in current docs |
| 2017-12-20 | Learning to operate Kubernetes reliably | Julia Evans | Cron-job scheduling on Kubernetes | **(evidence age: 8 years)** |
| 2019-05-07 | Railyard: how we rapidly train machine learning models with Kubernetes | Rob Story | ML training service | **(evidence age: 7 years)** |
| 2019-05-21 | The secret life of DNS packets | Jeff Jo | Internal DNS on Unbound, an hourly SERVFAIL investigation | **(evidence age: 7 years)** |
| 2019-07 | Root cause analysis: significantly elevated error rates on 2019-07-10 | Stripe | The only full public RCA found | **(evidence age: 7 years)** |
| 2019-07-30 | Fast and flexible observability with canonical log lines | Brandur Leach | One wide log line per request | **(evidence age: 7 years)** |
| 2020-12-15 | Stripe's payments APIs: the first 10 years | Michelle Bu | API design history (not infrastructure) | **(evidence age: 5 years)** |
| 2022-03-28 | Sorbet: Stripe's type checker for Ruby | Jake Zimmerman | Ruby codebase size, typing | **(evidence age: 4 years)**; size updated in 2026 |
| 2022-04 | 6 Nines: How Stripe keeps Kafka highly-available across the globe (Kafka Summit London talk) | Donny Nadolny | Multi-cluster Kafka behind an in-house proxy | **(evidence age: 4 years)** |
| 2023-01-23 | Amazon and Stripe sign expanded global agreement (press) | Stripe | AWS as infrastructure provider | **(evidence age: 3 years)**; consistent with 2024 and 2026 sources |
| 2023-03-29 | How we built it: Stripe Radar | Ryan Drapeau | Fraud model architecture, latency budget | **(evidence age: 3 years)**; a 2026 Radar post exists |
| 2023-04-05 | Annual letter 2022 | Collison brothers | API reliability figure | **(evidence age: 3 years)** |
| 2023-11-28 | BFCM 2023 press release | Stripe | Uptime, peak figures | current (3 years on 28 Nov 2026) |
| 2024-02-16 | Ledger: Stripe's system for tracking and validating money movement | Ilya Ganelin | Ledger and data-quality platform | current |
| 2024-03-13 | Annual letter 2023, section "How we engineer for reliability" | Collison brothers | Deploy pipeline, incident practice | current |
| 2024-04-15 | Shepherd: How Stripe adapted Chronon to scale ML feature development | Ben Mears | Feature platform | current |
| 2024-04-25 | Building a culture of system reliability (Sessions talk) | Rahul Patil, with Farhan Thawar of Shopify | Availability target, chaos testing, incident review | current |
| 2024-06-06 | How Stripe's document databases supported 99.999% uptime with zero-downtime data migrations | Jimmy Morzaria, Suraj Narkhede | DocDB, Data Movement Platform | current |
| 2024-10-24 | How Stripe architected massive scale observability solution on AWS (AWS blog, co-written with Stripe staff) | Tariq, Singh, Prado with Cody Rioux and Michael Cowgill | Metrics migration to Amazon Managed Service for Prometheus | current |
| 2024-12-03 | BFCM 2024 press release | Stripe | Uptime, peak figures | current |
| 2025-02-27 | Annual letter 2024 | Collison brothers | Volume only; no reliability figure | current |
| 2025-09-16 | How we built it: Real-time analytics for Stripe Billing | Reed Trevelyan | Flink-based analytics | current |
| 2025-12-02 | BFCM 2025 press release | Stripe | Uptime, peak figures | current |
| 2026-02-24 | Annual letter 2025 | Collison brothers | Volume only; no reliability figure | current |
| 2026-04-09 | Selective Test Execution at Stripe: Fast CI for a 50M-line Ruby monorepo | Aditya Anchuri | Monorepo size, test selection | current |
| 2026-04-28 | Formatting an entire 25 million line codebase overnight: the rubyfmt story | Fable Tales, Anna Mason | Ruby codebase | current |
| 2026-05-27 | Modern Java at Stripe: Language upgrades as a service | Mahib Hosain, Cara Mecozzi | JVM services | current |
| 2026-07-16 | How Stripe uses graph search and state machines to auto-remediate a global database fleet | Pragya Mehta, Sai Samant | MongoDB shard remediation | current |
| 2026-08-26 | Building a data plane from scratch: Stripe's own high-performance distributed proxy | Jack Loughran, Cara Mecozzi | Service-mesh proxy replacing Envoy | current |

Dates and authors: [VERIFIED: https://stripe.dev/blog and each post page, accessed 2026-11]; the annual letters are PDFs linked from `https://stripe.com/annual-updates/2022` to `/2025`.

**Not found for Stripe** (searched the stripe.dev index, stripe.com/blog, web search): a post on cell-based or regional architecture; a post on multi-region failover of the API; a post on its Kafka operations other than the 2022 talk; a "Stripe Data Pipeline" internals post; a deployment-system post (the 2023 letter is the only description).

### 0.2 Adyen: what exists, by date

Adyen's technical posts are published on `adyen.com/knowledge-hub` and mirrored on Medium ("Adyen Tech"). The English sitemap lists 573 knowledge-hub pages; roughly 40 are engineering posts, the rest are marketing, case studies and payment guides [VERIFIED: https://www.adyen.com/sitemap-en.xml, n.d., accessed 2026-11; the 40 is the analyst's count from slugs].

| Date | Title | Author | What it documents | Age flag |
| --- | --- | --- | --- | --- |
| 2018-01-03 | From 0 to $100 billion: Scaling infrastructure and workflow at Adyen | Michiel Toneman, SVP System Architecture | Mainline development, release branches, feature toggles, technology selection | **(evidence age: 8 years)** |
| 2018-03-14 | Updating a 50 terabyte PostgreSQL database | Reinier Haasjes, Senior System Administrator | PostgreSQL cluster shape, upgrade procedure | **(evidence age: 8 years)**; sizes updated by 2021 and 2023 posts |
| 2019-10-09 | Predicting and monitoring payment volumes with Spark and Elasticsearch | Adyen | Monitoring by volume prediction | **(evidence age: 7 years)** |
| 2020-09-16 | The Adyen way of engineering: expose your work early | Sarpkan Selcuk | Engineering practice | **(evidence age: 6 years)** |
| 2020-10-22 | The Adyen way of engineering: we design for 20x | Miguel Gonzalez, Tech Lead, Adyen for Platforms | 20x rule, asynchronous API processing | **(evidence age: 6 years)** |
| 2021-01-13 | The Adyen way of engineering: our tech stack is open source or built in-house | Burak Yildirim | In-house graph database on PostgreSQL | **(evidence age: 5 years)** |
| 2021-02-24 | The Adyen way of engineering: engineers as designers, architects, coders and testers | Laurens de Gilde | One team's weekly release cycle | **(evidence age: 5 years)** |
| 2021-07-28 | Design to Duty: How we make architecture decisions at Adyen (part 1, edge) | Willem Pino, Tech Lead (named on part 2) | Stateless edge, idempotency store, own data centers | **(evidence age: 5 years)** |
| 2021-08-23 | Design to Duty: The Accounting and Reporting Systems at Adyen (part 2) | Willem Pino | Accounting clusters, sharding, queue, streaming | **(evidence age: 5 years)** |
| 2022-05-31 | Adyen Tech Radar | Adyen | Technology list | **(evidence age: 4 years)** |
| 2023-09-28 | Building a guided data platform (feature platform) | Adyen | Real-time versus big-data platform | **(evidence age: 3 years)** |
| 2023-10-06 | Partitioning at Adyen (part 1 of a five-part series, to 2025-09-17) | Derk van Veen, Cosmin Octavian Pene | Table sizes, partitioning practice | **(evidence age: 3 years)** for part 1; parts 3 to 5 are current |
| 2023-10-30 | Implementing Service Level Objectives | Alessandro Niciforo, Platform Observability | SLO tooling on Prometheus and Grafana | **(evidence age: 3 years)** |
| 2024-09-23 | Test selection at Adyen | Mauricio Aniche | CI test selection | current |
| 2024-12-06 | How the default partition saved the day | Derk van Veen | Sharding and aggregated databases | current |
| 2025-01-10 | Database corruption in PostgreSQL | Cagri Biroglu, Derk van Veen | Corruption handling | current |
| 2025-01-16 | Checkpoint tuning for RTO improvements | Dwarka Rao, Huseyin Demir | Recovery-time tuning | current |
| 2025-04-22 | Incident update: Mitigating a DDoS attack on April 21, 2025 | Adyen | The only public incident account found | current |
| 2025-10-07 | Building a GlobalStream: Replication challenges and optimizations | Gaurav Singh, Luciano Sabença | Cross-continent Kafka replication | current |
| 2025-10-31 | Strengthening our platform resilience | Adyen | Follow-up to the DDoS | current |
| 2025-12-09 | BFCM 2025 insights | Adyen | Peak volume figure | current |
| 2026-02-12 | H2 2025 results press release | Adyen | BFCM uptime figure | current |
| 2026-03-05 | Annual Report 2025 | Adyen N.V. | Risk section, capex, data centers | current |
| 2026-07-09 | Inside Cilium CNI: solving mysterious Kubernetes pod setup timeouts | Data Platform Engineering | Kubernetes estate size | current |
| 2026-08-24 | We built Architect for humans. Agents made it transformative. | Adyen | Service, host and data-center counts | current |

Dates and authors: [VERIFIED: each page under https://www.adyen.com/knowledge-hub/, accessed 2026-11].

**Not found for Adyen**: a post on its HBase or Hadoop storage design beyond a mention; a post on its hardware security modules; a post naming a deployment frequency for the payment platform; a containerization post promised in 2021 ("A blog on the containerization effort is forthcoming") was not located under that description, although the 2026 Cilium post shows the result.

---

## PART 1: Reliability and availability (chapter 37)

### 1.1 What "availability" means in each company's own words

Four different things are published under the word "uptime", and they are not comparable:

| Figure | Who | Definition given | Source |
| --- | --- | --- | --- |
| Target of 99.9995% | Stripe | "we target 99.9995% reliability"; "maintaining 99.9995% public API uptime"; the metric's formula is not given | [VERIFIED: https://stripe.dev/blog/building-a-data-plane-from-scratch-stripes-own-high-performance-distributed-proxy, published 2026-08-26] |
| Same target, earlier | Stripe | "Five and a half nine means in a month we can only tolerate 13 seconds of unavailability." | [VERIFIED: https://stripe.com/us/sessions/2024/building-a-culture-of-system-reliability, published 2024-04-25] |
| Achieved, year | Stripe | "Stripe was only 99.999% available last year" (2023) | [VERIFIED: Stripe 2023 annual letter, https://stripe.com/annual-updates/2023, published 2024-03-13] |
| Achieved, peak weekend | Stripe | "API uptime greater than 99.9999%" over BFCM 2024 and 2025 | see PART 4 |
| Rolling 30 days | Adyen | "Last 30 days: 99.999% uptime", "Based on the percentage of successful requests to our Payments API in the last [UPTIME_DAYS] days" | [VERIFIED: https://status.adyen.com/, n.d., accessed 2026-11-17] ⚠ |
| Achieved, peak weekend | Adyen | "processed 837 million transactions during Black Friday Cyber Monday with 99.9999% uptime" | [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2, published 2026-02-12] |
| Contractual commitment | Adyen | "an average minimum uptime of 99.9% (measured on a quarterly basis) of the Payment Interface, to receive Transaction requests" | [VERIFIED: https://www.adyen.com/legal/terms-and-conditions, effective 2023-03-07, accessed 2026-11] **(evidence age: 3 years, still the published terms)** |

- Adyen's status page states its own limit: it "does not represent the service level commitments in your agreement with Adyen" [VERIFIED: https://status.adyen.com/, accessed 2026-11].
- Adyen's 99.9% commitment excludes "any downtime of the Payment Interface caused by acts or omissions of Merchant, Acquirers or Scheme Owners, changes implemented on specific Merchant request, general internet failures, failures of individual Payment Methods or force majeure" [VERIFIED: same terms].
- Adyen's terms also say the company "uses all reasonable efforts to avoid having to take the Payment Interface offline for executing planned maintenance", while the Customer Area has a "standard weekly maintenance window on Tuesdays 07:00 – 07:15 hours CET" [VERIFIED: same terms].
- Stripe's 2022 letter gives an earlier data point: "Our API reliability is now consistently in excess of 99.999%, and, during the peak week of Black Friday and Cyber Monday, exceeded six nines (that is, 99.9999%)—the equivalent of around 600 milliseconds of unavailability." [VERIFIED: Stripe 2022 annual letter, https://stripe.com/annual-updates/2022, published 2023-04-05] **(evidence age: 3 years; confirmed in direction by the 2023 to 2025 figures)**.
- **No public Stripe SLA percentage was found.** Stripe's Services Agreement page contains neither "uptime" nor "service level" [VERIFIED by text search of https://stripe.com/us/legal/ssa, n.d., accessed 2026-11]; `stripe.com/legal/sla` returns 404. Whether enterprise contracts carry one is not public [ASSUMPTION/JUDGEMENT].
- The arithmetic behind the gap: 99.9% per quarter allows about 2.2 hours of downtime; 99.999% over 30 days allows about 26 seconds; 99.9995% per month allows the 13 seconds Stripe cites [ASSUMPTION/JUDGEMENT: analyst's arithmetic; only the 13 seconds is from a source].
- None of the published figures says whether a request that fails because an issuer, a card network or a payment method is down counts against the provider's uptime. Adyen's contract excludes it; Adyen's status page counts "successful requests to our Payments API" without saying how a refusal is treated; Stripe gives no formula [ASSUMPTION/JUDGEMENT on what is missing].

**Stripe vs Adyen**

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Stated target | 99.9995% (2024, 2026) | none published as a target | Stripe uses the number as an engineering constraint in public; Adyen states outcomes |
| Achieved figure | 99.999% for 2023; no annual figure for 2024 or 2025 in the letters | rolling 30-day figure on the status page; no annual figure in the 2025 annual report | Neither publishes a consistent yearly series |
| Contractual figure | not public | 99.9% quarterly, public terms | The gap between 99.9% contracted and 99.999% reported is the margin a provider keeps for itself |
| Definition | not given | one sentence on the status page | A reader cannot audit either number |

**For readers new to payments**

- **Availability (uptime)**: the share of time, or of requests, in which a service answers correctly; "five nines" means 99.999%.
- **Service level agreement (SLA)**: the availability a provider promises in the contract, usually lower than what it reports achieving.
- **Payment method or scheme outage**: a failure at a card network, bank or wallet that makes payments fail even though the provider's own systems are up.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A merchant should plan against the contractual number and its exclusions, not the marketing number. A 13-second monthly budget cannot be met by people reacting to pages, which is the reason Stripe gives for automating detection and rollback (PART 5). Because neither provider counts downstream failures the same way, the availability a merchant experiences is lower than either figure and has to be measured on the merchant's side.

### 1.2 Redundancy, failure isolation and graceful degradation

**Stripe, as published:**

- "Stripe splits data by kind into different database clusters and by quantity into different shards. Each cluster has many shards, and each shard has multiple redundant nodes." [VERIFIED: https://stripe.com/rcas/2019-07-10, published 2019-07] **(evidence age: 7 years; the 2024 DocDB post confirms shards as replica sets with "a primary node and several secondary nodes with replication and automated failover")**.
- After the 2019 outage Stripe committed to "additional circuit-breaking on failed operations to particular clusters" and "additional fault isolation techniques to contain the impact of a single failed shard and limit resource consumption by clients attempting repeated retries of failed requests" [VERIFIED: same RCA].
- The reliability talk lists the practices in order: load testing in production, single-fault injection ("We add latency networking, we drop network packets, we turn off computers, we pull out the disc, we make a service unavailable completely"), which "only still gets us to four nines", then "Using our chaos testing engine, we trigger multiple complex faults in production" [VERIFIED: Sessions 2024 talk, published 2024-04-25].
- The same talk mentions "cell architecture" once, in a list of standard practices Stripe says it adopts ("excellent network design, data design, computer resiliency, cell architecture, and so on. We fully adopt these best technologies"). It gives no detail of cells at Stripe [VERIFIED: same talk]. This single phrase is the whole public record on cells at Stripe.
- Degradation is described as failing open: "what is the minimum quality of experience we can provide despite single faults?" [VERIFIED: same talk]. The 2014 game-day post gives a concrete case: the team expected a network partition between charge processing and fraud scoring to "time out and fail open (that is, allow the charge to go through immediately)", and found instead a latency spike [VERIFIED: Internet Archive copy of https://stripe.com/blog/game-day-exercises-at-stripe, snapshot 2021-06-22] **(evidence age: about 12 years)**.
- Load shedding by request class is documented in 2017: "We divide up our traffic into two types: critical API methods (e.g. creating charges) and non-critical methods (e.g. listing charges.)" and "We always reserve a fraction of our infrastructure for critical requests." [VERIFIED: https://stripe.com/blog/rate-limiters, published 2017-03-30] **(evidence age: 9 years; the 2026 proxy post mentions "dynamic priority-based request routing" and "an overhaul of our priority-based routing system", which suggests the idea persists in a different implementation)**.
- Monitoring scale: "We have more than a million CPUs dedicated just to monitor[ing] our systems. Our production system emits millions of health indicators per second." [VERIFIED: Sessions 2024 talk]. Before a 2024 migration, the metrics footprint was "approximately 300M metrics, 40k alerts and 100k dashboard queries produced by ~7k employees" [VERIFIED: https://aws.amazon.com/blogs/mt/how-stripe-architected-massive-scale-observability-solution-on-aws/, published 2024-10-24].
- The service mesh: "Stripe's service mesh handles millions of requests per second between thousands of services. One public API request relies on many internal service requests". Stripe replaced Envoy, used "For almost 10 years", with an in-house Go proxy called mesh-proxy that "supports retries, hedging, rate limiting, and dynamic priority-based request routing"; it reports "around half the CPU under high load, and roughly a 50% latency reduction" [VERIFIED: stripe.dev proxy post, published 2026-08-26].

**Adyen, as published:**

- The edge is stateless by design: "any PAL instance can be shut down without impacting our ability to process payments, and a new PAL can immediately be as effective as the other PALs already running. This makes our horizontal scaling linear." PAL is the Payments Acceptance Layer; "All payments pass through it." [VERIFIED: https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture, published 2021-07-28] **(evidence age: 5 years; no newer post contradicts it, and the 2025 annual report repeats the single-platform claim without technical detail)**.
- The edge and the books have opposite priorities, stated plainly: "Whereas for the latter the priority was uptime, for the accounting systems we don't mind if they are down for a little bit as long as we can guarantee their reliability and consistency." [VERIFIED: https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2, published 2021-08-23] **(evidence age: 5 years)**.
- The mechanism that decouples them: the PAL "saves the payment in a local database and a separate process picks it up when possible. This process will run behind if we have doubt about whether we can guarantee consistency in the accounting or if an accounting database is not available but that will not impact the availability of the PAL itself." [VERIFIED: same post].
- A security property is tied to the same design: "All our externally exposed systems are prohibited from writing to central databases" [VERIFIED: part 1].
- Per-merchant hostnames are a routing lever: "Each company account is provided with a unique hostname", and "in case of an infrastructure problem on the standard endpoint, especially if the cause is outside of Adyen's scope of control, alternative routing can be enabled to backup infrastructure and new infrastructure can be provisioned on demand" [VERIFIED: https://docs.adyen.com/development-resources/live-endpoints, last modified 2024-01-18].
- The 2025 annual report's wording: "Adyen designs its platform to avoid single points of failure and to maintain sufficient capacity to support critical processes in the event of resource unavailability" and "Our highly available platform is built to withstand individual failures in telecommunications, systems, or data center instances." [VERIFIED: Adyen Annual Report 2025, printed version, published 2026-03-05, read from https://www.lobbyregister.bundestag.de/media/a2/c7/860214/Annual-Report-and-Consolidated-Financial-Statements_compressed.pdf].
- Observability: Adyen built SLO tooling on the OpenSLO specification, with "Prometheus … already a core component of our monitoring infrastructure" and Grafana dashboards [VERIFIED: https://www.adyen.com/knowledge-hub/implementing-service-level-objectives, published 2023-10-30] **(evidence age: 3 years)**. A 2026 post describes "around 3,000 live services and the ~470,000 calls between them", "tens of thousands of hosts spread across tens of data centres", and "up to 7 million tracing spans per second" [VERIFIED: https://www.adyen.com/knowledge-hub/architect-blog-1, published 2026-08-24].

**Stripe vs Adyen**

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Where state lives on the request path | not described for the API tier | stateless edge with a local database queue to accounting (2021) | Adyen has published the decoupling; Stripe has published the isolation work that followed an outage |
| Fault injection | game days (2014), chaos engine in production (2024) | "additional automated testing" after the 2025 DDoS; no chaos-engineering post found | Stripe documents the practice; Adyen does not, which is not evidence that it lacks one |
| Service count | "thousands of services" (2026) | "around 3,000 live services" (2026) | Both are large service estates; Adyen's "single platform" is not a single process |
| Cells | one phrase in a 2024 talk | nothing public found | No writer should describe either as cell-based |

**For readers new to payments**

- **Failure isolation**: arranging a system so that one broken part (a database shard, a payment method, a region) cannot take the rest down.
- **Graceful degradation**: continuing to serve the important requests in a reduced way when something is broken, for example taking a payment without a fraud score.
- **Fail open / fail closed**: when a dependency is unreachable, either let the request proceed (open) or refuse it (closed).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Both companies split the system the same way in principle: an authorization path that must answer, and a record-keeping path that must be right and may lag. The published difference is where the buffer sits (Adyen: a database queue at the edge) and what is shed first (Stripe: non-critical API methods). A builder can copy both ideas at small scale. Neither company has published which payment-path steps it is willing to skip under failure beyond the fraud-scoring example from 2014.

### 1.3 Public incident reports

**Stripe, 10 July 2019** (the only full root-cause analysis found) [VERIFIED: https://stripe.com/rcas/2019-07-10, published 2019-07] **(evidence age: 7 years; the database layer it describes has since been rebuilt around the Data Movement Platform and automated remediation, see PART 2)**:

- "on 2019-07-10 from 16:35 to 17:02 UTC, and again from 21:14 to 22:47 UTC, the Stripe API was severely degraded. A substantial majority of API requests during these windows failed."
- Cause in one sentence: "two different database bugs and a configuration change interacted in an unforeseen way, causing a cascading failure across several critical services."
- The first window: a database minor version installed three months earlier "introduced a subtle fault in the database's failover system that only manifested in the presence of multiple stalled nodes"; two nodes had "stopped emitting metrics reporting their replication lag but continued to respond as healthy to active checks"; "the shard was unable to elect a new primary".
- Why one shard took down the API: "Because of widespread use of this shard across applications, including the API, the unavailability of this shard starved compute resources for the API and cascaded into a severe API degradation."
- The second window was caused by the fix: "our revert to a known stable version interacted poorly with a recently-introduced configuration change to the production shards. This interaction resulted in CPU starvation on all affected shards."
- Detection and response times: "Automated monitoring detected the failed election within a minute. We began incident response within two minutes."
- Remediation items: monitoring for nodes that stop reporting replication lag, circuit breaking and fault isolation per shard, and "further procedures and tooling to increase the safety with which operators can make rapid configuration changes during incident response".
- Customer communication: "We've sent you an email if you had five or more failed POST requests."

**Stripe, 8 February 2024** (one paragraph in the annual letter): "the most significant recent issue which happened on February 8, 2024 between 21:46 and 21:52 UTC (as shown on status.stripe.com). It affected a small subset of traffic—the three most impacted users had 39, 15, and 12 payments fail, respectively." The cause: "an erroneous change rolled out all the way to 1% of the critical tier of traffic. As is common for incidents in highly redundant systems, multiple problems had to coincide for users to be impacted." [VERIFIED: Stripe 2023 annual letter, published 2024-03-13]. No separate RCA page was found.

**Stripe, 2024 near miss**: an Envoy upgrade pulled in an HTTP/2 rapid-reset defense that "accidentally rejected some legitimate traffic to one of our services. Luckily, we caught this in a QA load test"; "A single production incident like this could jeopardize our 99.9995% reliability goal for the whole year." [VERIFIED: stripe.dev proxy post, published 2026-08-26].

**Adyen, 21 April 2025** [VERIFIED: https://www.adyen.com/knowledge-hub/mitigating-a-ddos-april-2025, published 2025-04-22]:

- "At 18:51 CEST on April 21, 2025, our monitoring systems detected elevated error rates and latency across multiple payment services hosted in the European region." The cause was "a DDoS attack targeting services across our European datacenters."
- "The attack unfolded in three distinct waves, each with a unique pattern"; "At peak, the attack generated millions of requests per minute, originating from a globally distributed and constantly shifting set of IP addresses. This caused saturation of key infrastructure components".
- Impact window: "the main impact for Ecommerce and In-Person Payment Transaction processing occurring between 18:51 CEST and 19:35 CEST." Customer Area, Hosted Onboarding and the Transfer API were also degraded.
- A deliberate trade: "As a result of our deliberate mitigations, checkout services such as Session Integrations, Secured Fields, and Pay by Link, remained impacted throughout the entire incident."
- The detailed review is not public: "A detailed post-incident review, including root cause analysis and long term prevention measures, will be made available to our customers."
- Trade press reported the incident as resolved at 03:20 CEST on 22 April 2025 [WIDELY REPORTED: https://www.paymentsdive.com/news/adyen-hit-with-cyberattack-in-europe/746064, 2025; trade press, via search summary].

**Adyen's follow-up, 31 October 2025** [VERIFIED: https://www.adyen.com/knowledge-hub/strengthening-our-platform-resilience, published 2025-10-31]: four changes are named. "introducing additional global DDoS mitigation partners, such as Cloudflare, alongside existing global providers"; "We've scaled and re-architected our load-balancing layer to better segment and distribute network flows across multiple points of presence"; "We've accelerated planned geographic distribution of key services"; and "additional automated testing and monitoring".

**Adyen's annual report on the same event**: "One regulatory reportable DDoS incident occurred, triggering Adyen's early-warning alert and causing temporary disruption … The event did not exceed Adyen's risk appetite limits." And: "In 2025, there was one instance of reduced availability, linked to the disruption incident referenced earlier." It adds that "Each incident triggers a root-cause analysis and an assessment of its impact on the broader risk and control framework." [VERIFIED: Adyen Annual Report 2025, printed version, published 2026-03-05].

**Stripe vs Adyen**

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Full public RCA | one, July 2019 | none; one incident update (April 2025) and a six-month follow-up | Public postmortems are rare at both; neither has a standing practice |
| Cause disclosed | database failover bug plus configuration (2019); bad change reaching 1% of critical traffic (2024) | external attack on European data centers (2025) | Stripe's disclosed failures are self-inflicted changes; Adyen's is an edge-capacity event, which fits an operator of its own network edge |
| Regulatory framing | none public | "regulatory reportable" incident, risk-appetite limits | Adyen is a bank and reports to supervisors; the public sees the summary |
| Where detail goes | status page and annual letter | customers only | A merchant must ask for postmortems under contract |

**For readers new to payments**

- **Root-cause analysis (RCA) / postmortem**: a written account of what failed, why, and what will change.
- **DDoS (distributed denial of service)**: an attack that floods a service with requests from many sources so real requests cannot get through.
- **Critical tier of traffic**: Stripe's term, not defined publicly; by the 2017 post's example, methods like creating charges.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The 2019 RCA is the best public teaching case for cascading failure in a payment API: one shard used by many applications, health checks that passed while replication had stalled, and a rollback that caused the second outage. The Adyen case teaches a different lesson: a provider that owns its edge must own DDoS absorption too, and during an attack it may choose to keep server-to-server payments up at the cost of hosted checkout components.

### 1.4 Status pages as evidence

**Stripe** [VERIFIED: https://www.stripestatus.com/api/v2/components.json and https://www.stripestatus.com/history.json, n.d., accessed 2026-11-17] ⚠:

- Six top-level components: "Stripe API", "Global payments", "Revenue and finance automation", "Banking-as-a-service", "Stripe core components", "Acquirers and payment methods".
- The page records very many small events. Counts of history entries per month in 2026 run from 76 (January) to 156 (March); most are partner payment-method errors and scheduled partner maintenance (BLIK, TWINT, Swish, Bancontact).
- Stripe marks the boundary of responsibility in the entries themselves: "Stripe retrieves payment method planned maintenance information from payment method partners and the information may not be complete, accurate, or up to date."
- Recent entries affecting the API component: 27 September 2026, impact "major", "From 00:32 UTC to 01:01 UTC, we saw elevated API errors"; 22 September 2026, "From 19:13 to 22:19 UTC, we saw elevated error rates and response times with the API" (accounts and capability calls); 14 November 2026, "From 02:34 to 03:01 UTC on November 14th, we saw increased API error rates for the Stripe API." None has a postmortem attached.
- Dependency failures are visible: 20 October 2025, "Affirm, Klarna, and Amazon Pay had brief periods of unavailability due to a widespread outage external to Stripe"; 18 November 2025, "Paypal, Alma, FPX and Payto had brief periods of unavailability due to a widespread outage external to Stripe". These dates match widely reported outages at a cloud provider and at a content-delivery network; Stripe does not name them [ASSUMPTION/JUDGEMENT on the match].
- The old status page showed a 90-day uptime percentage per component (API, Webhooks, Dashboard, Stripe.js, Checkout, Support site); the frozen snapshot of 9 February 2024 shows 99.999 for each [VERIFIED: https://status.stripe.com/current/full, snapshot dated 2024-02-09, accessed 2026-11]. The current page was not seen to show a percentage in its fetched HTML [ASSUMPTION/JUDGEMENT: the page is partly client-rendered].

**Adyen** [VERIFIED: https://status.adyen.com/ and its `/api/incident-messages/history` endpoint, n.d., accessed 2026-11-17] ⚠:

- One headline number ("Last 30 days: 99.999% uptime") and incident categories visible in the data: `ACQUIRER_PAYMENTS_PERFORMANCE`, `PLATFORM_AVAILABILITY`, `SETTLEMENT_PAYOUT`, `CUSTOMER_AREA_REPORTING`, `ADYEN_FOR_PLATFORMS`, with severities `GREY` and `YELLOW`.
- Entries are mostly about third parties: issuer refusal rates ("BARCLAYS BANK UK PLC"), payment methods (Pix, Twint, Trustly), and settlement delays ("Visa UK - Partial settlement delay on November 28, 2025").
- A 2024 example of a platform-availability entry: "Degraded performance for Mastercard transactions on US endpoints" (April 2024).
- The truncated view returned no entry for the April 2025 DDoS; because the view is truncated, this says nothing about whether one was posted (see Research limitation).

**Stripe vs Adyen**: Stripe's page is a high-volume feed with a public JSON history going back to December 2023; Adyen's is a summary page with a single uptime number and a definition. Both mostly report other parties' failures. Neither links incidents to postmortems [VERIFIED for the 50 latest Stripe incidents; ASSUMPTION/JUDGEMENT for Adyen given the truncated view].

**For readers new to payments**: a **status page** is the provider's public log of incidents; a **degraded payment method** entry means a bank, wallet or network behind the provider is failing, which the provider can report but not fix.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Status pages show that most payment failures a merchant sees originate downstream of the provider. A merchant integrating two providers should subscribe to both feeds by machine (Stripe offers a JSON history; Adyen's is not documented as an API) and should still rely on its own success-rate monitoring, because both pages are written after detection.

---

## PART 2: Data stores and consistency (chapter 38)

### 2.1 Stripe: a document database platform on MongoDB

All from [VERIFIED: https://stripe.dev/blog/how-stripes-document-databases-supported-99.999-uptime-with-zero-downtime-data-migrations, published 2024-06-06] unless noted:

- "Stripe's DocDB is an extension of MongoDB Community—a popular open-source database—and consists of a set of services that we built in-house. It serves over five million queries per second from Stripe's product applications."
- Scale as of 2024: "10,000+ distinct query shapes over petabytes of important financial data that lives in 5,000+ collections distributed over 2,000+ database shards."
- Origin: "When Stripe launched in 2011, we chose MongoDB as our online database because it offered better developer productivity than standard relational databases." "MongoDB Atlas didn't exist in 2011, so we built a self-managed cluster of MongoDB instances running in the cloud."
- Access path: applications reach data "through a fleet of database proxy servers, which we developed in-house in Go to enforce concerns of reliability, scalability, admission control, and access control." Proxies find shards through "a chunk metadata service that maps chunks to database shards".
- Change data capture: "We transport the oplog from every DocDB shard to Kafka, an event streaming platform, and then archive it to a cloud object storage service such as Amazon S3."
- The Data Movement Platform migrates chunks between shards in six steps: registration, bulk import (sorted insertion "boosting write throughput by 10x"), asynchronous replication (bidirectional, so traffic can be reverted), a correctness check "by comparing point-in-time snapshots", traffic switch, and deregistration.
- The switch uses "versioned gating": "We added a custom patch to MongoDB that allows a shard to enforce that the version token number it receives on requests from the proxy servers is newer than the version token number it knows of". "The entire traffic switch protocol takes less than two seconds to execute, and all failed reads and writes directed to the source shard succeed on retries."
- The stated bound for the switch: "shorter than the duration of a planned database primary failover—typically lasting a few seconds, and in line with the retry budget of our product applications."
- Use in 2023: "we bin-packed thousands of underutilized databases by migrating 1.5 petabytes of data transparent to product applications, and reduced the total number of underlying DocDB shards by approximately three quarters." Also a major-version upgrade "by fork-lifting data to a later version of MongoDB in one step".

Newer, from [VERIFIED: https://stripe.dev/blog/how-stripe-uses-graph-search-and-state-machines-to-auto-remediate-a-global-database-fleet, published 2026-07-16]:

- "A MongoDB shard—one of 2,000 that collectively processed $1.9 trillion in payments in 2025". The fleet spans "over 40 distinct shard layouts, from cost-optimized configurations to high-availability setups designed for disaster recovery."
- Recovery is computed, not scripted: the shard's state is a graph node, operations are edges, and breadth-first search (later Dijkstra's algorithm) finds a path to the healthy state "without ever violating safety invariants" such as "an even number of votes" or "a minority of healthy voting nodes". Result: "a 30% reduction in pager volume (~200 fewer pages per year), 12 fewer days of shards stuck in unhealthy states annually".
- Workflows run on "Temporal, a durable execution framework". Shard state includes "regional distribution" and an "availability zone imbalance" rule, which is the only published hint that shards span zones or regions [ASSUMPTION/JUDGEMENT on the reading].

Older, and to be used with the age flag:

- **Online migrations (2017)**: the "4 step dual writing pattern": "Dual writing to the existing and new tables to keep them in sync", "Changing all read paths in our codebase to read from the new table", "Changing all write paths in our codebase to only write to the new table", "Removing old data that relies on the outdated data model". The example moved "hundreds of millions of Subscriptions objects"; reads were verified with "GitHub's Scientist"; "We perform all infrastructure upgrades online, rather than relying on planned maintenance windows." [VERIFIED: https://stripe.com/blog/online-migrations, published 2017-02-02] **(evidence age: 9 years; this is an application-level data-model migration and is not replaced by the 2024 post, which covers moving data between shards; whether the same tooling is used today is not public)**.
- **Ledger (2024)**: "an immutable and auditable log" that "sees five billion events" a day, with "99.99% of our dollar volume … fully ingested and verified within four days" [VERIFIED: https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement, published 2024-02-16]. Its storage engine is not named in the post [VERIFIED by reading: no database product is named]. The `ledger` brief covers it in depth.
- **Analytics path**: Stripe Billing analytics run on "Apache Flink, which stores a highly compressed version of subscription history as a 'state'", with "latency as low as 15 minutes" [VERIFIED: https://stripe.dev/blog/how-we-built-it-real-time-analytics-for-stripe-billing, published 2025-09-16]. This is the eventually consistent side of the house.
- **Kafka**: "At Stripe our core business relies on Kafka, and as we outgrew a single Kafka cluster we had to build a multi-cluster system … supporting a target of 99.9999% availability for our most critical use cases", using "an in-house proxy layer and multi-cluster toplogy which we've built and operated over the past 3 years", with "global routing for constraints such as data locality" [VERIFIED: https://www.confluent.io/events/kafka-summit-london-2022/6-nines-how-stripe-keeps-kafka-highly-available-across-the-globe/, talk given 2022-04] **(evidence age: 4 years; the 2024 DocDB post confirms Kafka in the change-data path)**. The talk's slides are reported to state an SLO of 99.999% of high-priority publishes succeeding within 5 seconds [WIDELY REPORTED: search summary of the slide deck, 2022].

**Not public for Stripe**: which data lives outside DocDB (for example whether the ledger, the card vault or idempotency keys use it); transaction boundaries across collections; the consistency level of reads; replica counts per shard.

### 2.2 Adyen: PostgreSQL, sharded by cluster

- Shape of a cluster in 2018: "Our PostgreSQL database clusters consist of one primary and at least three replica servers, spread over multiple data centers. The database servers are dual socket machines with 768 GB of RAM." Scale then: "We currently process 5,000+ PostgreSQL transactions per second across multiple clusters"; "our biggest cluster has already grown to 74 terabytes." [VERIFIED: https://www.adyen.com/knowledge-hub/updating-a-50-terabyte-postgresql-database, published 2018-03-14] **(evidence age: 8 years; sizes are superseded, see below; the one-primary-plus-replicas shape is not restated in newer posts)**.
- Why PostgreSQL: "it provides consistency, isolation, and reliability we need … as we work with sensitive financial data, having a transactional database was key as it ensures we don't lose track of records." [VERIFIED: same post].
- A maintenance property that depends on the edge queue: "we built our software architecture in such a way that we can stop traffic to our PostgreSQL databases, queue the transactions, and run a PostgreSQL update without affecting payments acceptance." An upgrade rule: "Only when there are at least two replicas online, connected, and up-to-date, we allow access to the cluster again." [VERIFIED: same post].
- Accounting writes: "Over the lifetime of a payment transaction, about 50 rows have to be inserted into the accounting database." When "thousands of inserts a second started to cause issues", Adyen sharded: "Now we have several accounting databases, or clusters, processing side-by-side." [VERIFIED: design-to-duty part 2, published 2021-08-23] **(evidence age: 5 years)**.
- The sharding key is deliberately not a business key: "eventually decided to go for a simple round-robin strategy with some parameters we can adjust", because "At the moment we can just add a new cluster whenever we need more capacity or remove one from the routing when we see strange behavior we want to investigate." [VERIFIED: same post].
- The cost Adyen names: "The migration to a sharded accounting database was quite painful." A payout must draw on one account, so "the money needs to be transferred from one cluster to the other"; "we created several jobs and processes that use back and forth messages between the clusters to keep everything aligned." Reconciliation files had to be split per cluster. And "rebalancing the clusters … has not been implemented yet for this setup." [VERIFIED: same post].
- Correctness in the books is enforced at write time: "The only way to add new records to the accounting system is by means of templates … These templates are mathematically verified … we can guarantee that if at any time, we sum up all the records in the accounting system, the result will always be 0." [VERIFIED: same post]. The `ledger` brief owns this.
- Sizes in 2021: "dozens of local databases that can be instantiated dynamically at application startup and transactional databases of hundreds of terabytes running on the same technology." [VERIFIED: same post]. In 2023: "Some of our tables are already over 20TB in size"; "As a rule of thumb, we partition tables that might exceed the size of 100GB." [VERIFIED: https://www.adyen.com/knowledge-hub/partitioning-at-adyen, published 2023-10-06] **(evidence age: 3 years)**.
- A 2025 post revises the advice and records a near miss: "I still have nightmares about incident number 2016. We were preparing for one of the most critical seasons for our merchants – December shopping – when the CPU unexpectedly spiked. We realized that automatically adding one more partition to an already partitioned table would bring one of our most critical databases to its knees". The lesson: "We partitioned individual tables, not the environment." [VERIFIED: https://www.adyen.com/knowledge-hub/partitioning-an-environment-not-individual-tables, published 2025-09-17]. ("2016" is an incident number, not a year.)
- Sharding and reporting: "when the database became a bottleneck, we understood it was time to apply database sharding"; cross-shard queries were served from "an aggregated (and summarized) version of the original data from all shards" in a separate database [VERIFIED: https://www.adyen.com/knowledge-hub/how-the-default-partition-saved-the-day, published 2024-12-06].
- Uptime during maintenance: "Achieving close to zero downtime is our top priority, and this means all maintenance has to be done while the tables remain available. In most cases, it is not possible to lock the table for more than a few seconds." [VERIFIED: https://www.adyen.com/knowledge-hub/maintenance-under-pressure, published 2024-01-19].
- One non-PostgreSQL store on the money path: for API idempotency "we eventually decided on integrating Cockroach, a distributed database, with our PALs", because "The information needs to be available locally" [VERIFIED: design-to-duty part 1, published 2021-07-28] **(evidence age: 5 years; no newer confirmation found that CockroachDB is still used)**.
- Streaming: Adyen first built its own stream on PostgreSQL and Java because "exactly-once delivery was not yet supported by Kafka" at the time, and in 2021 was debating "whether we should swap it out for an open-source solution such as Kafka" [VERIFIED: part 2]. By 2025 it runs Kafka at "several hundred thousand messages per second" with MirrorMaker 2 replication "across continents" [VERIFIED: https://www.adyen.com/knowledge-hub/building-a-global-stream, published 2025-10-07]. The 2021 statement is updated, not contradicted.
- Analytics: "We run a Spark Hadoop cluster combined with Airflow" on its own servers [VERIFIED: part 2]; in 2026, "more than 500 datanodes" of HDFS and "100+ Kubernetes clusters" [VERIFIED: https://www.adyen.com/knowledge-hub/inside-cilium-cni-solving-kubernetes-pod-setup-timeouts, published 2026-07-09].
- A guest lecture by Adyen engineers reports that the main accounting system "was running > 70TB on a single PostgreSQL instance at up to 25k tps" before sharding [WIDELY REPORTED: https://se.ewi.tudelft.nl/delftswa/2021/slides/architecting-for-scalability.pdf, 2021; university-hosted slides by Bert Wolters and Angel Bravo of Adyen].

**Not public for Adyen**: the number of accounting clusters; how cross-cluster transfers are made atomic beyond "back and forth messages"; the replication mode (synchronous or asynchronous); failover procedure and time; whether HBase is used on any payment path.

### 2.3 Stripe vs Adyen on data stores

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Primary online store | MongoDB Community behind an in-house platform, DocDB (2024, 2026) | PostgreSQL (2018 to 2025) | A document store chosen in 2011 for developer speed versus a relational store chosen for transactions; each then built what its choice lacked |
| Unit of scaling | 2,000+ shards, chunks moved online between them | several accounting clusters filled round-robin, no rebalancing (2021) | Stripe invested in moving data; Adyen in never needing to |
| What was built in-house | proxies, chunk metadata, migration platform, a MongoDB patch, remediation planner | partition tooling (open-sourced), accounting templates, a PostgreSQL-based stream | Both avoid proprietary databases on core flows |
| Published numbers | 5 million queries per second; petabytes (2024) | 5,000+ transactions per second (2018); "hundreds of terabytes" (2021) | Not comparable: different years and units |
| Money correctness | Ledger verifies after the fact, with a four-day ingestion measure (2024) | templates proven to sum to zero at write time (2021) | Detection at Stripe, prevention at Adyen, as far as each has published |

**For readers new to payments**

- **Shard**: one of many databases that each hold a slice of the same kind of data.
- **Online migration**: moving or reshaping live data while the system keeps serving requests.
- **Consistency boundary**: the set of records that must change together or not at all; everything outside it is allowed to catch up later.
- **Change data capture (CDC)**: a stream of every write made to a database, used to feed other systems.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Neither company describes distributed transactions across its money path. Stripe's posts imply retries against a brief write block ("all failed reads and writes … succeed on retries"); Adyen's describe queues and messages between clusters. Both therefore rely on idempotent operations and later verification, not on a global transaction. That is the teachable point for chapter 38, and it is an inference from the published mechanisms, not a statement either company makes.

### 2.4 Contrasts that clarify a choice

- **Square (Block), 2019**: built "a new kind of database, called Books", on "Google Cloud Spanner and Google Kubernetes Engine"; "we picked Google Cloud Spanner. It is a fully managed, globally distributed SQL database which let us not worry about sharding" [VERIFIED: https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/, published 2019-10-16] **(evidence age: 7 years)**. The contrast: buy global consistency from a cloud database instead of building sharding.
- **Uber, 2018**: its payments platform's "primary design goals were high reliability through an active-active architecture, exactly-once payment processing by the means of idempotency and strong consistency, auditability via double-entry bookkeeping" [VERIFIED: https://www.uber.com/blog/payments-platform/, published 2018-12-05] **(evidence age: 8 years)**. The contrast: a payer of drivers, not a processor, stating active-active as a goal in public, which neither Stripe nor Adyen does.
- **Airbnb, 2019 (Orpheus)**: "a generic idempotency framework to achieve eventual consistency and correctness across our payments micro-service architecture"; "if a single operation to move money is called multiple times, the underlying system should move money at most once"; a stand-alone idempotency service was rejected because "We needed ultra low latency" [VERIFIED: Internet Archive copy of https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb, published 2019-04-16] **(evidence age: 7 years)**. The contrast: idempotency as a library inside each service, close to Adyen's "available locally" requirement.
- **TigerBeetle (design, not a company's production account)**: a database "designed specifically for OLTP" whose interface is debit and credit; it batches "up to 8,190 transfers per" request and uses a consensus protocol whose "cost of replication is paid only once per batch" [VERIFIED: https://docs.tigerbeetle.com/concepts/oltp/ and https://docs.tigerbeetle.com/concepts/performance/, n.d., accessed 2026-11]. The contrast: a purpose-built ledger database versus general-purpose stores with invariants enforced above them.
- **Shopify, 2022**: ten practices for payment resilience, starting with low timeouts ("an open timeout of one second with a write and read or query timeout of five seconds is a decent starting point") and circuit breakers through its Semian library [VERIFIED: https://shopify.engineering/building-resilient-payment-systems, published 2022-07-28] **(evidence age: 4 years)**. The contrast: the caller's side of the same problem.
- **Checkout.com**: no first-party architecture source was found; a vendor case study says it is "predominantly AWS" [WIDELY REPORTED: https://spacelift.io/case-studies/checkout, undated; vendor case study, via search summary]. Do not build a contrast on it.
- **PayPal**: nothing usable found (see Research limitation).

---

## PART 3: Multi-region operation and data residency (chapter 39)

This part is short because the record is short.

### 3.1 What each company has said about where it runs

**Stripe:**

- "Stripe will expand its use of Amazon Web Services, Stripe's long-standing cloud infrastructure provider"; "Stripe has long relied on AWS to provide the core compute infrastructure on which Stripe is built." David Singleton, then chief technology officer: "We couldn't run without AWS—and we wouldn't want to." [VERIFIED: https://stripe.com/us/newsroom/news/amazon-and-stripe, published 2023-01-23] **(evidence age: 3 years; confirmed by the 2024 AWS blog, "a sophisticated microservice environment built on top of AWS", and by current security documentation)**.
- The card vault is separated: "A dedicated team manages our CDV in an isolated Amazon Web Services (AWS) environment that's separate from the rest of the Stripe infrastructure." [VERIFIED: https://docs.stripe.com/security, n.d., accessed 2026-11].
- Stripe's Privacy Center names the provider among recipients of data: "a service provider - i.e., Amazon Web Services ("AWS")" [VERIFIED: https://stripe.com/us/legal/privacy-center, n.d., accessed 2026-11]. It does not list storage locations.
- European personal data is moved under transfer mechanisms, not kept in region by default: "Stripe's Data Transfers Addendum is incorporated into your Data Processing Agreement … If more than one data transfer mechanism applies, the DPF takes precedence." [VERIFIED: https://stripe.com/us/legal/dpa/faqs, n.d., accessed 2026-11].
- **No EU data-residency product statement was found.** A web search for one returned only third-party claims without sources. Stripe's blog for customers mentions residency as the customer's concern, not as a Stripe feature [VERIFIED: https://stripe.dev/blog/load-balancing-stripe-api-calls-multiple-aws-regions, published 2025-03-06, which is about the customer's own AWS regions].
- **Not public**: which AWS regions; how many; whether the API is served active-active across regions; failover time between regions.

**Adyen:**

- "We manage our own infrastructure in several data centers around the world and have bare metal available, but the hardware and software are still tightly coupled." "The reasons we are not deploying to the cloud are part historical, part legal, and part technical. In part, because we now need dynamic scaling, we are moving towards running our system on an internal cloud." [VERIFIED: design-to-duty part 1, published 2021-07-28] **(evidence age: 5 years; confirmed in 2025 and 2026 by the sources below)**.
- "Our single-platform architecture gives us end-to-end ownership over every layer, from our data centers to our application logic" [VERIFIED: resilience post, published 2025-10-31].
- Capital spending follows: "CapEx was €116.8 million and 5% of net revenues for the full year. The majority of our CapEx is related to our data centers, where we add capacity as we scale." [VERIFIED: Adyen Annual Report 2025, printed version, published 2026-03-05]. In H1 2026: "We are proactively pulling investment from 2027 into H2 2026 to secure compute and storage availability … We now expect CapEx to be approximately 7% of net revenue this year." [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13] ⚠.
- Growth of the footprint: the 2025 report attributes higher capital-goods emissions to "the opening of new data centers in APAC and EMEA", refers to "data center partners", and says Adyen "began testing data center operations in major cities" in Japan [VERIFIED: Adyen Annual Report 2025, printed version]. "Data center partners" indicates rented space in others' facilities; the report does not use the word colocation [ASSUMPTION/JUDGEMENT on the reading].
- Regions visible to integrators: the client-side library is served per region for "Europe (EU) live", "United States (US) live", "Australia (AU) live", "Northeast Asia (NEA) live" and "India (IN) live" [VERIFIED: https://docs.adyen.com/online-payments/web-best-practices, last modified 2025-09-04]. "If you need to connect to a certain data center of the Adyen payments platform (for example, US or AU data centers), you can set up location-based live endpoints." [VERIFIED: live-endpoints page, last modified 2024-01-18].
- A 2026 post gives the order of magnitude: "tens of thousands of hosts spread across tens of data centres" [VERIFIED: architect post, published 2026-08-24].
- On data placement, one engineering sentence: "data must remain close to producers to reduce latency and meet regulations, while also being centralized for analytics", illustrated by a payment in Australia that should not wait on Europe [VERIFIED: global-stream post, published 2025-10-07].
- **Not public**: the cities, the facility operators, the exact count, which regions hold which merchants' data, whether a region can take another's traffic, and what "alternative routing" to "backup infrastructure" consists of.

### 3.2 Localization rules that bind payment data: India

- The rule: "All system providers shall ensure that the entire data relating to payment systems operated by them are stored in a system only in India. This data should include the full end-to-end transaction details / information collected / carried / processed as part of the message / payment instruction. For the foreign leg of the transaction, if any, the data can also be stored in the foreign country, if required." Compliance was due "within a period of six months", reported "latest by October 15, 2018" [VERIFIED: Reserve Bank of India circular RBI/2017-18/153, DPSS.CO.OD No.2785/06.08.005/2017-2018, https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0, published 2018-04-06] **(evidence age: 8 years; still the governing circular as far as the RBI pages fetched show)**.
- The stated reason is supervision, not privacy: "it is important to have unfettered supervisory access to data stored with these system providers" [VERIFIED: same circular].
- The 2019 clarification: "There is no bar on processing of payment transactions outside India if so desired by the PSOs. However, the data shall be stored only in India after the processing." And: "the data should be deleted from the systems abroad and brought back to India not later than the one business day or 24 hours from payment processing, whichever is earlier." It applies also to "payment gateways, third party vendors and other entities … in the payments ecosystem". Data in scope includes customer data, account details, credentials and "Transaction data (originating & destination system information, transaction reference, timestamp, amount, etc.)" [VERIFIED: RBI FAQ "Storage of Payment System Data", https://www.rbi.org.in/Scripts/FAQView.aspx?Id=130, published 2019-06-26] **(evidence age: 7 years)**.
- **Stripe's response**: "to meet local data storage requirements, we're moving the servers that store India data to be located within the country. During our migration, Stripe's core services will remain unaffected. However, some features will be impacted at the end of April 2021." Consequences listed: "Payment information can no longer be cloned into or out of India"; "the same card details can have two different fingerprints, one for India and another for the rest of the world"; Card Updater and some Billing and Radar features were disabled or changed [VERIFIED: https://stripe.com/india-data-storage-faq, last updated 2023-05-16] **(evidence age: 3 years; the page is still published and describes itself as a migration notice)**. Stripe calls it "a substantive infrastructure change".
- **Adyen's response**: no statement about data storage in India was found. What is public is an India region for client resources ("India (IN) live") and two 2026 engineering posts on UPI and on an India card simulator that refer to "regional compliance and regulatory mandates" without describing data placement [VERIFIED: web-best-practices page; https://www.adyen.com/knowledge-hub/one-integration-global-reach-bringing-upi-to-adyens-single-platform, published 2026-07-27; https://www.adyen.com/knowledge-hub/engineering-a-regulatory-compliant-card-payment-simulator-for-india, published 2026-07-22].

### 3.3 European operational-resilience law (DORA)

- Regulation (EU) 2022/2554 "shall apply from 17 January 2025". Its scope lists "credit institutions", "payment institutions" and "electronic money institutions", and it covers "ICT third-party service providers" [VERIFIED: CELEX 32022R2554, http://publications.europa.eu/resource/celex/32022R2554, published 2022-12; adopted text] **(evidence age: 4 years as a text; in application since January 2025)**.
- "Financial entities shall report major ICT-related incidents to the relevant competent authority" (Article 19) [VERIFIED: same text]. Adyen's phrase "One regulatory reportable DDoS incident" in its 2025 report is consistent with this duty; the report does not cite the article [ASSUMPTION/JUDGEMENT on the link].
- It is not a localization law: "This Regulation does not impose a data localisation obligation as it does not require data storage or processing to be undertaken in the Union." [VERIFIED: same text, recital].
- It creates Union oversight of "critical ICT third-party service providers, including cloud computing service providers" [VERIFIED: same text]. A payment company on a public cloud therefore has a regulated dependency; one in its own data centers has moved that dependency to its facility and network suppliers [ASSUMPTION/JUDGEMENT].
- Which Stripe and Adyen entities fall under it: Adyen N.V. is a licensed credit institution (see the `companies` brief); Stripe's European licensed entities are covered in the `companies` and `risk` briefs. Not re-verified here.

### 3.4 Stripe vs Adyen on regions and residency

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Hosting | AWS, stated repeatedly (2023, 2024, current docs) | own infrastructure in its own or partners' data centers (2021, 2025, 2026) | The clearest documented architectural difference between the two |
| Regions named | none | EU, US, AU, NEA, IN as integration regions | Adyen exposes region to the integrator; Stripe exposes one global API hostname |
| Count | not public | "several" (2021), "tens of data centres" (2026) | Adyen's footprint has grown; the two phrases may count different things |
| India | servers moved in-country, features cut (2021 to 2023 page) | nothing published on storage | Stripe documented the product cost of localization; Adyen has not |
| EU residency | transfer mechanisms; no residency product found | not stated; EU is the home region | Neither sells "your data stays in the EU" in public documentation found |
| Active-active | not stated | not stated | No writer should assert either |

**For readers new to payments**

- **Data residency**: where data is stored. **Data localization**: a law requiring that certain data be stored (sometimes only) in a given country.
- **Payment system operator (PSO)**: the RBI's term for an entity authorized to run a payment system in India.
- **Active-active / active-passive**: two regions both serving traffic all the time, versus one serving and one waiting to take over.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Localization breaks global identifiers: Stripe's note that one card gets two fingerprints is the concrete cost, and it means fraud signals and saved cards stop crossing the border. A region is also a latency decision (Adyen's Australian example). For a merchant with two providers, "where is our customers' data" has two different kinds of answer: a cloud provider's regions that Stripe does not name, and a set of integration regions that Adyen names without locations.

---

## PART 4: Peak load and capacity (chapter 40)

### 4.1 Published peak figures

| Event | Company | Volume | Transactions | Peak rate | Uptime wording | Source |
| --- | --- | --- | --- | --- | --- | --- |
| BFCM 2022 | Stripe | not in letter | not in letter | not in letter | "exceeded six nines" in the peak week | [VERIFIED: 2022 annual letter, published 2023-04-05] **(evidence age: 3 years)** |
| BFCM 2023 | Stripe | "more than $18.6 billion" | "more than 300 million" | "93,304 transactions per minute"; "a peak of 27,395 requests per second" | "API uptime greater than 99.999%" | [VERIFIED: https://stripe.com/us/newsroom/news/bfcm2023, published 2023-11-28] |
| BFCM 2024 | Stripe | "more than $31 billion" | "more than 465 million" | "137,000 transactions per minute" | "API uptime greater than 99.9999%" | [VERIFIED: https://stripe.com/us/newsroom/news/bfcm2024, published 2024-12-03] |
| BFCM 2025 | Stripe | "more than $40 billion" | "more than 578 million" | "More than 152,000 transactions per minute at peak volume" | "an uptime of more than 99.9999%" | [VERIFIED: https://stripe.com/us/newsroom/news/bfcm2025, published 2025-12-02] |
| BFCM 2024 | Adyen | "$34 billion" | "670 million transactions" | not given | not found | [VERIFIED: https://www.adyen.com/knowledge-hub/black-friday-cyber-monday-payment-insights, published 2024-12-09] |
| BFCM 2025 | Adyen | "$43 billion", "a 27% increase from last year" | "837 million" (results release) | "up to 199,000 transactions per minute without disruption" | "99.9999% uptime" (results release) | [VERIFIED: https://www.adyen.com/knowledge-hub/bfcm, published 2025-12-09; and H2 2025 results release, published 2026-02-12] |

Definitions that are missing: neither company defines "transaction" (authorization attempts, successful payments, or all API-initiated payment events), and the two are unlikely to count the same thing, since Adyen's figure includes in-store terminals [ASSUMPTION/JUDGEMENT]. Stripe's 2023 release is the only one to give both a request rate and a transaction rate: 27,395 requests per second against about 1,555 transactions per second at peak, a ratio of roughly 18 API requests per payment transaction at peak [ASSUMPTION/JUDGEMENT: analyst's arithmetic, and the two peaks need not coincide]. BFCM is four days at both, Friday through Monday. ⚠ New figures are due in December 2026.

Stripe ran "a public microsite [that] tracked these and a dozen other BFCM metrics in real-time, including the uptime of the Stripe API" [VERIFIED: BFCM 2023 release]. No equivalent live Adyen page was found.

### 4.2 How each prepares, as published

**Stripe:**

- Load is tested in production: "We simulate this and then we repeat this in production, load testing our systems farther and farther" [VERIFIED: Sessions 2024 talk]. Deploys continue through events: "today's Sessions, there's no code freeze." [VERIFIED: same talk; said of the conference day, not of BFCM].
- Rate limiting, 2017: "At Stripe, we operate 4 different types of limiters in production." They are the request rate limiter ("restricts each user to N requests per second"), the concurrent requests limiter ("You can only have 20 API requests in progress at the same time"), the fleet usage load shedder and the worker utilization load shedder ("the final line of defense"). They use "the token bucket algorithm" and "We implement our rate limiters using Redis." They fail open: "if there were bugs in the rate limiting code (or if Redis were to go down), requests wouldn't be affected." [VERIFIED: https://stripe.com/blog/rate-limiters, published 2017-03-30] **(evidence age: 9 years; the concepts are confirmed by current documentation, the implementation is not)**.
- Current documented limits: "Live mode: 100 requests per second", "Sandbox: 25 requests per second"; "Individual API endpoints (unless otherwise noted) 25 requests per second"; "The default global concurrency limit for standard API traffic in live mode is 50 in-progress requests." A `Stripe-Rate-Limited-Reason` header carries values such as `global-rate`, `endpoint-rate`, `global-concurrency`. [VERIFIED: https://docs.stripe.com/rate-limits, n.d., accessed 2026-11] ⚠.
- Elastic data tier: "DocDB can split database shards during traffic surges and consolidate thousands of databases through bin packing when traffic is low"; in 2024 Stripe was "prototyping a heat management system" and "investing in shard autoscaling" [VERIFIED: DocDB post, published 2024-06-06].
- Headroom from the proxy: custom balancing across Ruby backends "gives us 15–20% more headroom before traffic bursts overwhelm the machines" [VERIFIED: proxy post, published 2026-08-26].

**Adyen:**

- The design rule: "The 20x scaling factor is a rule of thumb we often use internally when designing a solution or determining whether we are still satisfied with it." [VERIFIED: design-to-duty part 2, published 2021-08-23] **(evidence age: 5 years; the rule is restated in the 2020 "we design for 20x" post, not in anything newer found)**.
- Growth context: "a day's worth of processing volume on the Adyen platform in 2010 would now be done in five seconds" [VERIFIED: 0-to-100-billion post, published 2018-01-03] **(evidence age: 8 years)**.
- Queueing as control: moving an API from synchronous to asynchronous processing gave "better control over how and when the requests are executed", so that merchants "are not impacted anymore when we need to operate an internal maintenance" [VERIFIED: https://www.adyen.com/knowledge-hub/the-adyen-way-of-engineering--we-design-for-20x, published 2020-10-22] **(evidence age: 6 years; about Adyen for Platforms, not card authorization)**.
- Capacity is bought ahead: the 2026 capex pull-forward "to secure compute and storage availability" [VERIFIED: H1 2026 release]. An owner of hardware plans peak capacity in purchase lead times [ASSUMPTION/JUDGEMENT].
- Peak is a database risk too: the December partition incident in 2.2.
- **No Adyen description of load testing, of a peak freeze, or of its own rate limits was found.** The documentation URL tried for rate limits returned 404; the `adyen-api` brief may hold documented limits.

**Stripe vs Adyen**

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Peak figures | yearly press release since 2023, with rate and uptime | blog and results release, 2024 and 2025 | Both now market peak reliability; Adyen's 2025 per-minute peak is higher than Stripe's, on different definitions |
| Elasticity | cloud capacity; shard split and merge | owned hardware; capex pulled forward | Elastic rented capacity versus pre-bought capacity |
| Limiter design | published (2017) and documented limits (current) | not found here | Stripe treats limits as part of the developer contract |
| Load testing | stated (2024) | not stated | No inference about Adyen is warranted |

**For readers new to payments**

- **BFCM**: Black Friday through Cyber Monday, the four-day retail peak.
- **Rate limit**: a cap on how many requests one customer may send per second. **Load shedding**: the provider dropping less important requests for everyone when it is overloaded.
- **Backpressure**: a slow part of a system telling the faster part upstream to slow down.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A merchant's own peak (a renewal run on the first of the month) meets the provider's per-account limit long before it meets the provider's capacity; 100 requests per second in live mode is the number to design a batch against. Published peak rates show both providers run at a few thousand transactions per second at the yearly maximum, so the hard part is not raw throughput but keeping every dependency and every shard healthy at once.

---

## PART 5: Safe change: deploys, migrations, incidents (chapter 41)

### 5.1 Stripe

The fullest source is the 2023 annual letter [VERIFIED: https://stripe.com/annual-updates/2023, published 2024-03-13]:

- Frequency: new code is deployed "to one of our core API services approximately 400 times in a typical day."
- Tests: "it is evaluated by a battery of around 1.4 million tests. Stripe uses half a million CPU cores to execute more than 6 billion test runs each day."
- Pre-production: "a mock production environment with synthetic API traffic designed to mimic realistic integration patterns. Here we check that the change can not only be safely rolled out to production, but also that it can be safely undone if required."
- Progressive rollout: "a single production machine with a small sliver of traffic, before gradually advancing to 0.5%, then 1%, then 5%, then 20%, and so on, of actual production traffic—with pauses along the way to observe the effects". And: "We roll all changes out to test-mode API traffic before hitting live-mode traffic."
- Automatic rollback: "Each progressive rollout is inspected against 55,000 different metrics. If at any moment the system detects anomalous telemetry, the machines running the new code are automatically withdrawn from the pool and traffic is redirected to machines running an older, known-good version."
- Incidents: "we inspect every incident manually, and have dedicated operations staff on call 24×7. (On average, 520 calls per day go out to our staff.)" Remediation may be automatic "by invoking redundant rails or enabling emergency fallback capabilities."
- Principle: "Defense in depth is the core principle of our high-availability work."

Other Stripe sources:

- Ownership: "Incident reviews are not done by some central SRE team. They're done by the service-owning engineering team." "If an incident requires humans for remediation, we force a deep dive with the teams." An executive review picks an executive at random to present incidents [VERIFIED: Sessions 2024 talk, published 2024-04-25].
- Monorepo and language: "our monorepo is the order of 50 million lines of Ruby code, backed by … roughly 100,000 Ruby test files and approximately 1.2 million test units"; test selection runs "roughly 5% of our full Ruby test suite" per build [VERIFIED: https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo, published 2026-04-09]. "Stripe runs the world's largest Ruby codebase" [VERIFIED: https://stripe.dev/blog/formatting-an-entire-25-million-line-codebase-overnight-the-rubyfmt-story, published 2026-04-28]. The two 2026 posts give 50 million and 25 million lines; the posts do not reconcile the figures [VERIFIED that both appear; ASSUMPTION/JUDGEMENT that they count different scopes]. In 2022 the figure was "over 15 million lines of code spread across 150,000 files" [VERIFIED: https://stripe.dev/blog/sorbet-stripes-type-checker-for-ruby, published 2022-03-28] **(evidence age: 4 years; superseded by the 2026 figures)**.
- Other languages: infrastructure proxies in Go (DocDB proxies, mesh-proxy); JVM services with managed Java upgrades across "hundreds or even thousands of owners" [VERIFIED: DocDB post; proxy post; https://stripe.dev/blog/modern-java-at-stripe-language-upgrades-as-a-service, published 2026-05-27].
- Build versus adopt: Stripe replaced Envoy with its own proxy and says "It's a little counterintuitive that building something in-house would be more reliable than operating a battle-tested open-source project." [VERIFIED: proxy post]. It moved metrics from a vendor to a managed open-source-compatible service [VERIFIED: AWS observability post, 2024-10-24], having moved to Datadog about 2015 to 2016 [VERIFIED: https://stripe.com/blog/introducing-veneur-high-performance-and-global-aggregation-for-datadog, published 2016-10-18] **(evidence age: 10 years; updated by the 2024 post)**.
- Migration safety patterns in public: dual writes and read comparison (2017); bidirectional replication with a reversible traffic switch (2024); phased production rollout of database versions "starting with less critical clusters and moving on to increasingly critical ones" (2019 RCA); dark launch of rate limiters (2017 post) [VERIFIED: the posts cited above].
- Observability for change: canonical log lines, "one long log line at the end that includes many of their key characteristics", emitted "every time a webhook is sent, a credit card is tokenized by our PCI vault, or a page is loaded in the Stripe Dashboard" [VERIFIED: https://stripe.com/blog/canonical-log-lines, published 2019-07-30] **(evidence age: 7 years; no newer statement found)**.

### 5.2 Adyen

- Mainline development and release branches: "everybody develops on the main line". "When we want to do a new release, we create a new branch, which we stabilize, and once it gets pushed to production, the old branch is terminated." Fixes go to the main line first, with "a four-eyes policy" and porting "enforced with a commit hook" [VERIFIED: 0-to-100-billion post, published 2018-01-03] **(evidence age: 8 years; no newer platform-wide description found)**.
- Deploy is separated from activation: "we toggle features one-by-one on production, and then canary them to ensure the highest possible chance of a seamless rollout." [VERIFIED: same post].
- Cadence: the only figures found are one team's: "Our team has weekly release cycles, so effectively, every week sees new code going into production." [VERIFIED: https://www.adyen.com/knowledge-hub/the-adyen-way-of-engineering--engineers-as-designers-architects-coders-and-testers, published 2021-02-24] **(evidence age: 5 years)**. A 2025 post says "containers provide an optimal way of doing fast release cycles" without a number [VERIFIED: https://www.adyen.com/knowledge-hub/kubectl-rexec-a-plugin-for-auditing-exec-commands, published 2025-01-17]. **No platform-wide deployment frequency is public.**
- Code base: "a single platform, in a single repository (monorepo), almost exclusively written in Java." [VERIFIED: design-to-duty part 1, 2021] **(evidence age: 5 years)**. In 2026: "Our monorepo alone runs to hundreds of thousands of files, and it's far from the only one." [VERIFIED: architect post, 2026-08-24]. The 2021 "single repository" claim is therefore updated: one large monorepo plus others.
- Engineers operate what they design: "the design of our system is done by engineers who are also on duty" [VERIFIED: part 1].
- Build versus buy: "for [core flows] we never choose a proprietary solution because we want to have full control." "We buy instead of build, if the use case is peripheral, it does not have to be real-time, we do not have to embed it" [VERIFIED: part 1]. "At Adyen, we use open-source software or we build in-house." [VERIFIED: SLO post, 2023-10-30]. Technology choice is by "maturity against complexity", borrowed from Pinterest [VERIFIED: 0-to-100-billion post].
- The rule has bent at the edge: after the 2025 attack Adyen added "global DDoS mitigation partners, such as Cloudflare, alongside existing global providers" [VERIFIED: resilience post, 2025-10-31]. The 2026 acquisitions and what they change about "built, not bought" belong to the `companies` brief.
- Database change without downtime: the snapshot-based major-version upgrade (2018) with the two-replica rule; partition maintenance that may not "lock the table for more than a few seconds" (2024); checkpoint tuning against a recovery-time objective (2025) [VERIFIED: the posts cited in 2.2; https://www.adyen.com/knowledge-hub/checkpoint-tuning-for-rto-improvements, published 2025-01-16].
- Testing at scale: a test-selection service picks tests per merge request from coverage data; "Post-merge runs of the entire test suite" keep it current [VERIFIED: https://www.adyen.com/knowledge-hub/test-selection-at-adyen, published 2024-09-23]. Both companies have published the same solution to the same monorepo problem.

### 5.3 Stripe vs Adyen on safe change

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Deploy frequency | about 400 per day to one core API service (2024) | not public; one team weekly (2021); release branches (2018) | The public record cannot support a frequency comparison |
| Rollout | percentages of traffic with automatic withdrawal on 55,000 metrics (2024) | feature toggles activated one by one, then canaried (2018) | Stripe describes gating the binary; Adyen describes gating the feature. Each may do both |
| Language and repo | Ruby monorepo of tens of millions of lines; Go and JVM services | Java monorepo plus other repositories | Both chose one dominant language and paid for tooling to keep it workable |
| Build or buy | builds when open source stops fitting (proxy, database platform); rents cloud | open source or in-house for core flows; owns hardware | Same instinct about software; opposite about infrastructure |
| Postmortems | internal reviews by owning teams; rare public RCAs | root-cause analysis per incident; detail to customers and regulators | Similar internal practice as described; little is public at either |

**For readers new to payments**

- **Progressive rollout (canary)**: releasing a change to a small share of traffic first and widening only if metrics stay healthy.
- **Feature flag (toggle)**: a switch that turns code on or off in production without a new deployment.
- **Dark launch**: running new code on real traffic without letting its result affect the customer.
- **Zero-downtime migration**: changing a schema or moving data while requests continue.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Stripe's February 2024 incident shows the limit of progressive rollout: a bad change reached 1% of critical traffic and payments failed. On a money path, 1% is still real losses, which is why test-mode-first rollout and automatic withdrawal matter. Neither company has published how it verifies money correctness after a change (for example a reconciliation gate on deploy); Stripe's Ledger post implies continuous verification that would catch it within days, not minutes.

---

## PART 6: Facts for chapters 12, 18, 20, 21, 46 and 47

### 6.1 Idempotency (chapter 18)

- Stripe, design rationale (2017): "The Stripe API implements idempotency keys on mutating endpoints (i.e. anything under POST in our case)"; clients should retry with "exponential backoff" and "jitter" to avoid "the thundering herd problem" [VERIFIED: https://stripe.com/blog/idempotency, published 2017-02-22] **(evidence age: 9 years; the mechanism is confirmed and refined by the current API reference)**.
- Stripe, current behavior: "For API v1, Stripe saves the status code and body of the first request made with a given idempotency key after endpoint execution begins. Retries with the same key return the saved response, including `500` errors. With API v2, retries don't repeat successful operations. Stripe retries failed or partially failed work to completion when possible and returns an updated response." Keys are "up to 255 characters long" and for v1 may be removed "after they're at least 24 hours old"; "The idempotency layer compares incoming parameters to those of the original request and errors if they're not the same" [VERIFIED: https://docs.stripe.com/api/idempotent_requests, n.d., accessed 2026-11] ⚠.
- Adyen, documented behavior: a key of "a maximum of 64 characters"; "Keys are stored at a company account level"; "Idempotency keys are valid for a period of 7 to 14 days after first submission"; a `transient-error` header set to `true` marks a retryable failure; a duplicate sent while the first is in flight gets "HTTP 422 – Unprocessable Entity or HTTP 409 - Conflict" [VERIFIED: https://docs.adyen.com/development-resources/api-idempotency, last modified 2020-07-30] **(evidence age: 6 years by its last-modified date; still the published page)**.
- Adyen, implementation note: idempotency data must be "available locally" to stateless edge instances, hence a distributed database beside the PALs [VERIFIED: design-to-duty part 1, 2021] **(evidence age: 5 years)**.
- Stripe has published no account of where idempotency keys are stored [VERIFIED by absence in the posts read].

### 6.2 Webhooks and events (chapter 20), sender side only

- Stripe: "Stripe attempts to deliver events to your destination for up to three days with an exponential back off in live mode"; "Stripe doesn't guarantee the delivery of events in the order that they're generated"; endpoints "might occasionally receive the same event more than once" [VERIFIED: https://docs.stripe.com/webhooks, n.d., accessed 2026-11] ⚠. A canonical log line is emitted "every time a webhook is sent" [VERIFIED: canonical log lines post, 2019] **(evidence age: 7 years)**.
- Adyen: "You need to accept webhooks that you receive with a 2xx HTTP status code, store the message, and process the contents of the message." [VERIFIED: https://docs.adyen.com/development-resources/webhooks, last modified 2026-11-17]. Adyen's status history shows webhook delay as an incident class: "Partial Delay in Balance Platform Webhooks" (30 November 2025) [VERIFIED: status.adyen.com history endpoint, accessed 2026-11].
- **Neither company has published the design of its webhook sender** (fan-out, isolation of slow endpoints, backlog handling). Searches of both blogs found nothing. The delivery contracts are in the `stripe-api` and `adyen-api` briefs.

### 6.3 Rate limits and developer platform (chapter 21)

See 4.2 for Stripe's limiter design (2017) and current limits. One more fact: rate-limit behavior is observable per request, since the 2019 sample log line carries `rate_allowed=true rate_quota=100 rate_remaining=99` [VERIFIED: canonical log lines post, 2019] **(evidence age: 7 years)**. Adyen's limits were not found by this brief.

### 6.4 Ledger and data scale (chapters 12, 46, 47)

- Stripe: volume "passed the milestone of $1 trillion in total payment volume" in 2023, "$1.4 trillion … in 2024, up 38%", and "$1.9 trillion in total volume, up 34% from 2024" in 2025 [VERIFIED: annual letters, published 2024-03-13, 2025-02-27, 2026-02-24]. Engineering posts restate it as "around 1.6% of global GDP" [VERIFIED: proxy post, 2026-08-26].
- Adyen: "Processed volume for 2025 was €1,394.3 billion, up 8% YoY"; "point-of-sale volumes were €310.9 billion, comprising 22% of total processed volume" [VERIFIED: Adyen Annual Report 2025, printed version]. Self-description: "a single platform built entirely in-house … all operated end-to-end on our own infrastructure and banking licenses." [VERIFIED: same report].
- These are company-reported volumes with different definitions and currencies; the `companies` brief owns the comparison.

---

## PART 7: The blunt table

Topic by company. "Documented (year)" means a first-party source read in this session describes it. "Partially documented" means a first-party source mentions it without enough detail to describe a design. "Not public" means searches found nothing.

| Topic | Stripe | Adyen |
| --- | --- | --- |
| Availability target | Documented (2024, 2026): 99.9995% | Not public as a target |
| Achieved availability, annual | Documented for 2022 and 2023 only; not public for 2024 and 2025 | Not public; rolling 30-day figure on status page (2026) |
| Availability metric definition | Not public | Partially documented (one sentence, status page) |
| Contractual SLA | Not public | Documented (terms effective 2023): 99.9% quarterly, with exclusions |
| Peak figures (BFCM) | Documented (2023, 2024, 2025) | Documented (2024 volume; 2025 volume, rate and uptime) |
| Primary online database | Documented (2024, 2026): MongoDB-based DocDB | Documented (2018 to 2025): PostgreSQL |
| Sharding scheme | Documented (2024): chunks, proxies, metadata service | Documented (2021): round-robin accounting clusters |
| Online data migration between shards | Documented (2024) | Not public (rebalancing "not implemented", 2021) |
| Application-level data-model migration | Documented (2017) | Partially documented (partitioning existing tables, 2023 to 2025) |
| Database failover behavior | Partially documented (2019 RCA; 2026 remediation post) | Partially documented (replica rule, 2018; recovery tuning, 2025) |
| Replication mode and consistency level | Not public | Not public |
| Ledger or accounting store | Documented as a system (2024); storage engine not public | Documented (2021): PostgreSQL clusters, verified templates |
| Idempotency implementation | Documented design (2017) and behavior (current); storage not public | Documented behavior (2020 page); local distributed store (2021) |
| Webhook sender design | Not public | Not public |
| Rate-limiter design | Documented (2017); limits current | Not found by this brief |
| Load shedding by request class | Documented (2017); partially confirmed (2026) | Not public |
| Messaging and streaming | Partially documented (2022 talk abstract; 2024) | Documented (2021 in-house stream; 2025 Kafka replication) |
| Service architecture | Partially documented (2026): thousands of services, in-house mesh proxy | Partially documented (2021, 2026): stateless edge, about 3,000 services |
| Hosting | Documented (2023, 2024, current): AWS | Documented (2021, 2025, 2026): own infrastructure in data centers |
| Regions and locations | Not public | Partially documented: integration regions EU, US, AU, NEA, IN; "tens of data centres" (2026); no locations |
| Multi-region failover, active-active | Not public | Not public ("alternative routing … to backup infrastructure", docs 2024) |
| Cell-based architecture | Partially documented (one phrase, 2024) | Not public |
| India localization response | Documented (page updated 2023) | Not public |
| EU data residency offering | Not public (transfer mechanisms documented) | Not public |
| Deployment frequency | Documented (2024): about 400 per day to a core API service | Not public (one team weekly, 2021) |
| Progressive rollout and auto-rollback | Documented (2024) | Partially documented (toggles and canary, 2018) |
| Chaos or fault-injection testing | Documented (2014, 2024) | Not public |
| Load testing in production | Documented (2024) | Not public |
| Monorepo and language | Documented (2022, 2026): Ruby, plus Go and JVM | Documented (2021, 2026): Java |
| Build versus buy policy | Partially documented (examples, 2024 to 2026) | Documented (2018, 2021, 2023) |
| Observability stack | Documented (2016, 2019, 2024) | Documented (2019, 2023, 2026) |
| Public postmortems | One full RCA (2019); one paragraph (2024) | One incident update (2025) and a follow-up; detail not public |
| Status-page history as data | Documented, machine-readable to December 2023 | Partially available; truncated view |
| DDoS defense | Not public | Partially documented (2025): multi-provider mitigation, re-architected load balancing |
| Hardware security modules, key management | Not public (vault isolation documented, current) | Not public |

---

## Key numbers

| Number | Company | Exact definition as published | Source and date |
| --- | --- | --- | --- |
| 99.9995% | Stripe | reliability target; "public API uptime"; 13 seconds a month | Sessions talk 2024-04-25; proxy post 2026-08-26 |
| 99.999% | Stripe | "only 99.999% available last year" (2023) | 2023 letter, 2024-03-13 |
| > 99.9999% | Stripe | API uptime over the four BFCM days, 2024 and 2025 | press 2024-12-03, 2025-12-02 |
| 152,000 per minute | Stripe | "transactions per minute at peak volume", BFCM 2025 | press 2025-12-02 |
| 27,395 per second | Stripe | peak API requests per second, BFCM 2023 | press 2023-11-28 |
| about 400 per day | Stripe | deployments to "one of our core API services" | 2023 letter |
| 1.4 million; 6 billion | Stripe | tests per change; test runs per day | 2023 letter |
| 55,000 | Stripe | metrics inspected during each rollout | 2023 letter |
| 520 per day | Stripe | on-call "calls" to operations staff, average | 2023 letter |
| 5 million per second | Stripe | DocDB queries from product applications | DocDB post, 2024-06-06 |
| 2,000+; 5,000+ | Stripe | database shards; collections | DocDB post 2024; shard count restated 2026-07-16 |
| 1.5 petabytes | Stripe | data moved in 2023 to merge shards | DocDB post |
| < 2 seconds | Stripe | duration of the traffic-switch step of a chunk migration | DocDB post |
| 27 and 93 minutes | Stripe | the two degradation windows on 2019-07-10 | RCA, 2019 (age 7 years) |
| 100 per second; 50 | Stripe | live-mode global rate limit per account; default concurrent requests | docs, accessed 2026-11 ⚠ |
| 50 million lines | Stripe | Ruby in the monorepo, "the order of" | post 2026-04-09 |
| 99.999% | Adyen | successful requests to the Payments API, last 30 days | status page, 2026-11-17 ⚠ |
| 99.9% | Adyen | contractual "average minimum uptime", quarterly, Payment Interface | terms effective 2023-03-07 |
| 99.9999% | Adyen | uptime during BFCM 2025 | H2 2025 results, 2026-02-12 |
| 199,000 per minute | Adyen | "up to" transactions per minute, BFCM 2025 | blog 2025-12-09 |
| 837 million; $43 billion | Adyen | transactions; volume, BFCM 2025 | results 2026-02-12; blog 2025-12-09 |
| 44 minutes | Adyen | main impact window, 18:51 to 19:35 CEST, 21 April 2025 | incident update 2025-04-22 |
| about 50 rows | Adyen | accounting inserts per payment over its lifetime | part 2, 2021 (age 5 years) |
| 5,000+ per second | Adyen | PostgreSQL transactions across clusters | 2018 post (age 8 years) |
| 100 GB; 20 TB | Adyen | partitioning threshold; largest tables | 2023 post (age 3 years) |
| 20x | Adyen | design headroom rule of thumb | 2020, 2021 posts (age 5 to 6 years) |
| about 3,000; 7 million per second | Adyen | live services; tracing spans at peak | post 2026-08-24 |
| €116.8 million, 5% | Adyen | 2025 capital expenditure and share of net revenue, mostly data centers | Annual Report 2025 |
| 24 hours | RBI | time limit to delete payment data processed abroad | FAQ 2019-06-26 |
| 17 January 2025 | EU | date DORA applies | Regulation (EU) 2022/2554 |

---

## Open questions / not verifiable

These are the book's "where the evidence stops" statements.

1. **Stripe's regions.** No first-party source names an AWS region, a region count, or whether the API is active in more than one region at a time.
2. **Stripe's cells.** One phrase in a 2024 talk. No description of what a cell contains, how customers map to cells, or whether the term is used internally.
3. **Stripe's availability formula.** Whether 99.9995% is time-based or request-based, which endpoints count, and how downstream failures are treated.
4. **Stripe's annual availability for 2024 and 2025.** The letters for those years carry no figure.
5. **Stripe's public SLA.** None found; enterprise terms are private.
6. **Adyen's data centers.** No cities, operators or count beyond "several" (2021) and "tens" (2026); no statement of which are owned and which are rented space.
7. **Adyen's regional failover.** What "alternative routing … to backup infrastructure" is, and whether a region can serve another region's merchants.
8. **Adyen's deployment frequency** for the platform, and whether the 2018 release-branch model still holds.
9. **Adyen's DDoS post-incident review.** Promised to customers, not published. The attack vector, the saturated components and the peak rate are not public beyond "millions of requests per minute".
10. **Adyen's accounting clusters.** Their number, the cross-cluster transfer protocol, and whether rebalancing now exists.
11. **Adyen and CockroachDB.** One 2021 sentence; current use unconfirmed.
12. **Adyen and India.** No statement on where Indian payment data is stored.
13. **Either company's webhook sender design, key management hardware, and replication settings.**
14. **Comparability of peak figures.** "Transaction" is undefined at both; Adyen's includes in-store payments.
15. **The date of Stripe's game-day post** and whether game days continue in that form.
16. **Checkout.com and PayPal.** No first-party architecture evidence was read; they should not carry a contrast in these chapters.

---

## Source list

**Stripe, first party**

- "How Stripe's document databases supported 99.999% uptime with zero-downtime data migrations", J. Morzaria and S. Narkhede, 2024-06-06, https://stripe.dev/blog/how-stripes-document-databases-supported-99.999-uptime-with-zero-downtime-data-migrations. DocDB, shards, Data Movement Platform.
- "How Stripe uses graph search and state machines to auto-remediate a global database fleet", P. Mehta and S. Samant, 2026-07-16, https://stripe.dev/blog/how-stripe-uses-graph-search-and-state-machines-to-auto-remediate-a-global-database-fleet. Shard layouts, automated recovery.
- "Building a data plane from scratch: Stripe's own high-performance distributed proxy", J. Loughran and C. Mecozzi, 2026-08-26, https://stripe.dev/blog/building-a-data-plane-from-scratch-stripes-own-high-performance-distributed-proxy. Reliability target, service mesh, near miss.
- "Root cause analysis: significantly elevated error rates on 2019-07-10", Stripe, 2019-07, https://stripe.com/rcas/2019-07-10. The public RCA.
- Stripe annual letters for 2022 (2023-04-05), 2023 (2024-03-13), 2024 (2025-02-27), 2025 (2026-02-24), https://stripe.com/annual-updates/2022 to /2025. Reliability figures (2022, 2023), deploy pipeline (2023), volumes.
- "Building a culture of system reliability", R. Patil with F. Thawar, Stripe Sessions, 2024-04-25, https://stripe.com/us/sessions/2024/building-a-culture-of-system-reliability. Target, chaos testing, incident review.
- BFCM press releases, 2023-11-28, 2024-12-03, 2025-12-02, https://stripe.com/us/newsroom/news/bfcm2023, /bfcm2024, /bfcm2025. Peak figures.
- "Amazon and Stripe sign expanded global agreement", 2023-01-23, https://stripe.com/us/newsroom/news/amazon-and-stripe. AWS relationship.
- "Online migrations at scale", J. Xu, 2017-02-02, https://stripe.com/blog/online-migrations. Dual-write pattern.
- "Designing robust and predictable APIs with idempotency", B. Leach, 2017-02-22, https://stripe.com/blog/idempotency. Idempotency rationale.
- "Scaling your API with rate limiters", P. Tarjan, 2017-03-30, https://stripe.com/blog/rate-limiters. Limiters and load shedding.
- "Fast and flexible observability with canonical log lines", B. Leach, 2019-07-30, https://stripe.com/blog/canonical-log-lines. Logging.
- "Game day exercises at Stripe", about 2014, Internet Archive snapshot http://web.archive.org/web/20210622182916/https://stripe.com/blog/game-day-exercises-at-stripe. Failure injection, fail open.
- "Ledger: Stripe's system for tracking and validating money movement", I. Ganelin, 2024-02-16, https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement. Ledger scale.
- "How we built it: Real-time analytics for Stripe Billing", R. Trevelyan, 2025-09-16, https://stripe.dev/blog/how-we-built-it-real-time-analytics-for-stripe-billing. Flink analytics.
- "Selective Test Execution at Stripe", A. Anchuri, 2026-04-09; "the rubyfmt story", 2026-04-28; "Modern Java at Stripe", 2026-05-27; "Sorbet", J. Zimmerman, 2022-03-28; all under https://stripe.dev/blog/. Codebase and tooling.
- "Introducing Veneur", C. Watson, 2016-10-18, https://stripe.com/blog/introducing-veneur-high-performance-and-global-aggregation-for-datadog; "Learning to operate Kubernetes reliably", J. Evans, 2017-12-20, https://stripe.com/blog/operating-kubernetes; "The secret life of DNS packets", J. Jo, 2019-05-21, https://stripe.com/blog/secret-life-of-dns; "Railyard", R. Story, 2019-05-07, https://stripe.com/blog/railyard-training-models. Inventory entries; older infrastructure.
- Stripe documentation: rate limits https://docs.stripe.com/rate-limits; idempotent requests https://docs.stripe.com/api/idempotent_requests; webhooks https://docs.stripe.com/webhooks; security https://docs.stripe.com/security (all n.d., accessed 2026-11). Current behavior and limits.
- Stripe legal and support: India data storage FAQ, updated 2023-05-16, https://stripe.com/india-data-storage-faq; DPA FAQs https://stripe.com/us/legal/dpa/faqs; Privacy Center https://stripe.com/us/legal/privacy-center; Services Agreement https://stripe.com/us/legal/ssa. Localization, transfers, absence of SLA.
- Stripe status: https://www.stripestatus.com/ (components and `history.json`), accessed 2026-11-17; frozen snapshot https://status.stripe.com/current/full dated 2024-02-09. Incident evidence.

**Stripe, third-party venues**

- "6 Nines: How Stripe keeps Kafka highly-available across the globe", D. Nadolny, Kafka Summit London, 2022-04, https://www.confluent.io/events/kafka-summit-london-2022/6-nines-how-stripe-keeps-kafka-highly-available-across-the-globe/. Abstract only.
- "How Stripe architected massive scale observability solution on AWS", AWS Cloud Operations blog with Stripe co-authors, 2024-10-24, https://aws.amazon.com/blogs/mt/how-stripe-architected-massive-scale-observability-solution-on-aws/. Metrics scale, AWS.

**Adyen, first party**

- "Design to Duty: How we make architecture decisions at Adyen", 2021-07-28, https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture; part 2, W. Pino, 2021-08-23, https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2. Edge, accounting, sharding, data centers.
- "From 0 to $100 billion: Scaling infrastructure and workflow at Adyen", M. Toneman, 2018-01-03, https://www.adyen.com/knowledge-hub/from-0-100-billion-scaling-infrastructure-and-workflow-at-adyen. Release practice.
- "Updating a 50 terabyte PostgreSQL database", R. Haasjes, 2018-03-14, https://www.adyen.com/knowledge-hub/updating-a-50-terabyte-postgresql-database. Cluster shape, upgrades.
- Partitioning series, D. van Veen and others, 2023-10-06 to 2025-09-17: https://www.adyen.com/knowledge-hub/partitioning-at-adyen, /maintenance-under-pressure, /how-the-default-partition-saved-the-day, /partitioning-an-environment-not-individual-tables. Table sizes, maintenance, sharding.
- "Checkpoint tuning for RTO improvements", 2025-01-16, https://www.adyen.com/knowledge-hub/checkpoint-tuning-for-rto-improvements. Recovery objective.
- "Incident update: Mitigating a DDoS attack on April 21, 2025", 2025-04-22, https://www.adyen.com/knowledge-hub/mitigating-a-ddos-april-2025; "Strengthening our platform resilience", 2025-10-31, https://www.adyen.com/knowledge-hub/strengthening-our-platform-resilience. The incident and follow-up.
- "Building a GlobalStream", 2025-10-07, https://www.adyen.com/knowledge-hub/building-a-global-stream. Kafka replication, data placement.
- "Implementing Service Level Objectives", A. Niciforo, 2023-10-30, https://www.adyen.com/knowledge-hub/implementing-service-level-objectives. SLO tooling.
- "We built Architect for humans", 2026-08-24, https://www.adyen.com/knowledge-hub/architect-blog-1; "Inside Cilium CNI", 2026-07-09, https://www.adyen.com/knowledge-hub/inside-cilium-cni-solving-kubernetes-pod-setup-timeouts. Estate size.
- "The Adyen way of engineering" series, 2020-09 to 2021-02, https://www.adyen.com/knowledge-hub/the-adyen-way-of-engineering--we-design-for-20x and siblings; "Test selection at Adyen", 2024-09-23, https://www.adyen.com/knowledge-hub/test-selection-at-adyen. Practice.
- BFCM posts, 2024-12-09 and 2025-12-09, https://www.adyen.com/knowledge-hub/black-friday-cyber-monday-payment-insights and /bfcm. Peak figures.
- India posts, 2026-07-22 and 2026-07-27, https://www.adyen.com/knowledge-hub/engineering-a-regulatory-compliant-card-payment-simulator-for-india and /one-integration-global-reach-bringing-upi-to-adyens-single-platform. Absence of a storage statement.
- Adyen Annual Report 2025, 2026-03-05, official at https://investors.adyen.com/financials/2025; text read from https://www.lobbyregister.bundestag.de/media/a2/c7/860214/Annual-Report-and-Consolidated-Financial-Statements_compressed.pdf. Risk section, capex, data centers.
- H2 2025 and H1 2026 results releases, https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2 and /adyen-publishes-h1-2026-financial-results-3wjne. BFCM uptime, capex guidance.
- Adyen terms and conditions, effective 2023-03-07, https://www.adyen.com/legal/terms-and-conditions. The 99.9% commitment.
- Adyen documentation: live endpoints (modified 2024-01-18) https://docs.adyen.com/development-resources/live-endpoints; web best practices (modified 2025-09-04) https://docs.adyen.com/online-payments/web-best-practices; API idempotency (modified 2020-07-30) https://docs.adyen.com/development-resources/api-idempotency; webhooks https://docs.adyen.com/development-resources/webhooks. Regions, idempotency, webhooks.
- Adyen status: https://status.adyen.com/ and its history endpoint, accessed 2026-11-17. Uptime definition, incident classes.

**Regulators and law**

- Reserve Bank of India, "Storage of Payment System Data", RBI/2017-18/153, 2018-04-06, https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0; FAQ, 2019-06-26, https://www.rbi.org.in/Scripts/FAQView.aspx?Id=130. Localization rule.
- Regulation (EU) 2022/2554 (DORA), http://publications.europa.eu/resource/celex/32022R2554. Scope, incident reporting, no localization duty, application date.

**Contrasts**

- Square, "Books, an immutable double-entry accounting database service", 2019-10-16, https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/.
- Uber, "Engineering Uber's next-gen payments platform" (meetup recap), 2018-12-05, https://www.uber.com/blog/payments-platform/.
- Airbnb, "Avoiding Double Payments in a Distributed Payments System", 2019-04-16, https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb (read via Internet Archive).
- TigerBeetle documentation, https://docs.tigerbeetle.com/concepts/oltp/ and /concepts/performance/, accessed 2026-11.
- Shopify, "10 Tips for Building Resilient Payment Systems", 2022-07-28, https://shopify.engineering/building-resilient-payment-systems.
- TU Delft guest lecture slides by Adyen engineers, 2021, https://se.ewi.tudelft.nl/delftswa/2021/slides/architecting-for-scalability.pdf (secondary venue).
- Payments Dive, "Adyen hit with cyberattack in Europe", 2025, https://www.paymentsdive.com/news/adyen-hit-with-cyberattack-in-europe/746064 (trade press, search summary only).
