---
title: "Down Is Not an Option: Reliability and Availability"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How do payment providers stay up, and what happens when they do not? They decide beforehand what may lag or be dropped so that no payment is recorded twice or lost, and when the path fails anyway, what you have to repair is the set of payments whose outcome nobody knows, not the minutes of downtime."
permalink: payment-reliability-and-availability
timetoread: 28 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what Stripe's and Adyen's uptime figures measure, how a payment path is kept answering, and what you must repair after an outage.

> **KEY POINTS:**
>
> * **“Uptime” is five different figures.** The two providers publish a target, an achieved yearly figure, peak-weekend figures, rolling 30-day and 90-day figures and one contractual commitment. They cannot be compared. Plan against the commitment and its exclusions, and measure payment success yourself.
> * **A payment path stays up because something else gives way.** Adyen described in 2021 an edge that keeps answering while accounting runs behind. Stripe described in 2017 shedding non-critical requests to protect the creation of charges. In neither design is the record of a payment the thing that is relaxed.
> * **An outage ends when every outcome is known.** A request that timed out may have moved money. What you repair afterwards is the set of payments with unknown outcomes, so build the sweep that resolves them before you build a second provider connection.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Phantom Payment** — a timeout recorded as “failed” during an outage is a belief about a payment that the provider's record may contradict.
> * **The Double Charge** — a customer or a job that pays again after an unanswered request produces the outage's most expensive leftover.
> * **The Single Rail** — a second provider that has never carried traffic, or that is sent payments whose first attempt is still unknown, does not make the path more reliable.

<br>
The opening of [[part-8]] set two first-of-month runs side by side: 7,900 renewals a day late in October 2026, and 1,840 members charged twice in November. Something must give way so that the record does not. This chapter is about the first thing that gives way, under failure, and the best public illustration is seven years old. On 10 July 2019 the Stripe API was severely degraded for 27 minutes and then for 93. Stripe's account of that day includes a sentence about email: “We've sent you an email if you had five or more failed POST requests.” **The provider measured the aftermath in requests per customer, not in minutes.**

If you have run other web systems, you count a failure in minutes of downtime and you compare providers by their count of nines. A failed page view is gone when the page reloads. A payment request can time out after the customer's bank has already approved it: the unknown outcome of [[idempotency-and-retries]]. An outage multiplies it by every request in flight, so **what an outage leaves behind is a set of payments whose outcome nobody knows**.

Those payments are what this chapter's claim turns on. A payment path is kept answering by an operator that has **decided beforehand what may lag or be dropped**, the books or the non-critical requests, so that no payment is recorded twice or lost. When the path fails anyway, the provider restores service and publishes little about it. What you, the merchant, have to repair is **the payments with unknown outcomes, not the minutes of downtime**.

**Where we are in the payment's journey.** Take Mila's class pass: €120.00 paid to Studio Noord at 19:42 on Tuesday 9 March 2027, approved and captured (claimed for payment) within seconds. This chapter covers no single step of that payment. It covers every step on an evening when the request for her €120.00 gets no answer.

The chapter starts with a question asked at Larkfield: which provider is more reliable? It then says what the published uptime figures measure, explains how a payment path is kept answering, and gives the three choices for a step whose dependency fails. After that it reads the public incident accounts and compares the two providers. It ends with an outage drill at Larkfield and the recoveries that make an outage worse.

## Setting the Scene at Larkfield: Which Provider Is More Reliable?

The question comes up in May 2027 at Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]). The payments team is preparing the second quarterly rehearsal of its provider switch, decision K8 of Keel, the 2027 program that puts its payments estate in order. Sofie Vermeer, the CEO, asks which of the two providers is more reliable. Daniel Osei, the CTO, answers with two published figures: 99.9995% for Stripe and 99.999% for Adyen. They are not one scale: Stripe's 2026 engineering post says “we target 99.9995% reliability”, which is a goal, and Adyen's status page (accessed 17 November 2026) says “Last 30 days: 99.999% uptime”, which is a measurement of one month.

Neither figure, however, would have shown Larkfield's costliest payment incident. The Double Charge of 1 November 2026 began with provider calls that timed out during the renewal run. Each first request had in fact been approved and captured. The renewal job treated the silence as a failure and sent again under a new key, and 1,840 members paid twice: €71,300 refunded, and 212 disputes anyway. **The cost came from what Larkfield did with requests whose outcome it did not know.**

So Femke de Graaf, who leads payments engineering, replaces Sofie's question with three that can be answered. What does each published figure measure? What gives way, at the provider and at Larkfield, when a dependency fails? And after an outage, how long does it take until no payment has an unknown outcome? For the third she adds an outage drill to the rehearsal.

## Five Figures Under One Word: What Uptime Measures

**Availability** is the share of time, or the share of requests, in which a service answers correctly; “five nines” means 99.999%. A published figure for it is one of three kinds of statement. An **availability target** is an internal goal the operator engineers toward. An achieved figure is a report of what happened over some period. A contractual commitment, usually called a service-level agreement (SLA), is a promise with consequences if it is missed. The period matters as much as the percentage, as the arithmetic below shows (mine, except the last row, where Stripe's 2024 Sessions talk gives the same number: “Five and a half nine means in a month we can only tolerate 13 seconds of unavailability.”).

| Figure | Over | Allows about |
| --- | --- | --- |
| 99.9% | a quarter of 91 days | 131 minutes |
| 99.999% | 30 days | 26 seconds |
| 99.9995% | a month of 30 days | 13 seconds |

The target is 99.9995%, stated in the 2024 Sessions talk as “five and a half nines” and again in an engineering post of August 2026 (“maintaining 99.9995% public API uptime”); neither gives a formula. The achieved figures are scattered. The 2023 annual letter (published March 2024) says “Stripe was only 99.999% available last year”; the letters for 2024 and 2025 carry no reliability figure, and the Sessions keynote of 2026 says “last year, our critical APIs retained 99.9996% availability”. Press releases for the Black Friday to Cyber Monday weekends of 2024 and 2025 report API uptime of more than 99.9999%. Stripe's status page (n.d., accessed 17 November 2026) shows, for the Stripe API, “99.999% uptime for the last 90 days”, and does not say on the page how that is computed. The only hint of a definition is in the 2022 annual letter (published April 2023), which mentions “a live tracker of our 90-day trailing API availability, measured at the individual transaction level”. **(Evidence age: 3 years; the current system may differ.)**

Adyen's figures are of a similar spread but different kinds. I found no published target. Its status page (n.d., accessed 17 November 2026) shows “Last 30 days: 99.999% uptime” and defines it in one sentence: “Based on the percentage of successful requests to our Payments API”. Its H2 2025 results (February 2026) say it “processed 837 million transactions during Black Friday Cyber Monday with 99.9999% uptime”. Set beside Stripe's, and with the contractual figure discussed next, these are five kinds of measurement on different periods and bases. No row of the table can be ranked against another.

| Kind of figure | Stripe | Adyen | Definition as published |
| --- | --- | --- | --- |
| Target | 99.9995% (2024, 2026) | None found | None given |
| Achieved, year | 99.999% for 2023; 99.9996% for “critical APIs”, 2025 | None found for the platform; 100% for card acceptance in Australia, third quarter of 2026 (regulatory disclosure) | None given, except Australia's regulatory definition |
| Achieved, peak weekend | More than 99.9999% (2024, 2025) | 99.9999% (2025) | None given |
| Achieved, rolling window | 99.999%, last 90 days, Stripe API (17 November 2026) | 99.999%, last 30 days (17 November 2026) | Adyen: share of successful requests to the Payments API. Stripe: none on the page |
| Contractual commitment | No public percentage found | 99.9% per quarter, by “commercially reasonable efforts” (terms of November 2023) | Uptime of the Payment Interface “as measured by its ability to receive Transaction messages”, with exclusions |

<!-- illustration-placeholder
{
  "id": "37-five-figures-one-word",
  "status": "pending",
  "asset": "assets/images/37-payment-reliability/37-five-figures-one-word.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of the five kinds of figure",
  "visual_goal": "Show that five different measuring instruments hang under one sign, and that only one of them is a signed promise.",
  "prompt": "Create a conceptual explainer illustration. At the top center, one wide signboard labeled \"Uptime\". Hanging from it on five strings, left to right, five different objects. First, an archery target labeled \"Target\". Second, a wall calendar showing a full year labeled \"Last year\". Third, a small shopping bag with a stopwatch labeled \"Peak weekend\". Fourth, a round gauge with a needle labeled \"Rolling\". Fifth, a paper document with a signature line and a seal labeled \"Contract\", drawn slightly larger and outlined in green. A person with a clipboard stands at the lower right looking up, and a green arrow labeled \"Plan here\" points from the person to the contract document. The first four objects have thin grey outlines; none of the five objects touches another. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Five different objects hang under one sign reading Uptime: a target, a yearly calendar, a peak-weekend stopwatch, a rolling-window gauge and a signed contract, with an arrow telling a planner to plan against the contract.",
  "caption": "Five different figures are published under the word uptime; only the contractual commitment is a promise, and it is the one to plan against."
}
-->

Adyen's public terms and conditions (last updated 1 November 2023, for agreements made from that date; still published in November 2026) say that Adyen “will use commercially reasonable efforts to achieve a quarterly-average minimum uptime of 99.9% of the Payment Interface, as measured by its ability to receive Transaction messages”; the Payment Interface is the contract's name for the connection through which a merchant submits payments. **(Evidence age: 3 years.)** The calculation excludes downtime caused by “acts or omissions of Merchant, Issuing Banks, Acquirers or Scheme Owners”, by “general internet failures”, by “failures of individual Payment Methods” and by force majeure. An issuing bank is the bank that issued the customer's card, an acquirer is the institution that processes card payments for a merchant, and scheme owners are the card networks such as Visa and Mastercard. The consequence the terms name is a right to leave: the merchant may terminate at once if the commitment is “not met during two consecutive quarters”. The older terms (March 2023), still published for earlier agreements, carry the same 99.9%. Adyen's status page draws the line itself: it “does not represent the service level commitments in your agreement with Adyen”. The two numbers are 131 minutes a quarter and 26 seconds a month apart.

Stripe's public terms, by contrast, contain no such figure. I found no public service-level percentage for Stripe. The General Terms of its Services Agreement (last modified 28 September 2026, accessed 17 November 2026) contain neither the word “uptime” nor the phrase “service level”, and their disclaimer says: “Stripe does not warrant that User’s use of the Services and Stripe Technology will be uninterrupted or error-free”. Whether contracts negotiated with large customers carry a percentage is not public.

Taken together, the five figures leave out two things a merchant experiences. First, a payment needs parties beyond the provider: the issuer (the bank that issued the customer's card), the card network, or a local payment method's own operator. Adyen's contract excludes their failures, and they are most of what a status page reports. Adyen's page says it “tracks performance across a variety of products, services, and payment methods”. By my count on 17 November 2026, Stripe's status history for October 2026 lists 160 entries; 149 of them are scheduled maintenance at partner payment methods, and an entry of 20 October 2025 says that “Affirm, Klarna, and Amazon Pay had brief periods of unavailability due to a widespread outage external to Stripe.” Second, no figure says what became of requests that timed out. So the availability you experience is lower than any published number. **Plan against the contractual figure and its exclusions, and trust the payment success rate you measure on your own side.**

## How a Payment Path Stays Up: Deciding What Gives Way

The figures report how often a path answered; they do not say how it is kept answering. The usual first answer, redundancy, is not enough on its own, because copies share dependencies: three replicas of a service that all need the same database fail together. **Failure isolation** means arranging a system so that one broken part cannot take the rest down. **Graceful degradation** means continuing to serve the important requests, in a reduced way, while something is broken. Both require a decision made in advance: what is allowed to give way.

Adyen's 2021 architecture posts show isolation at the edge. **(Evidence age: 5 years; the current system may differ.)** Every payment enters through what Adyen calls the Payments Acceptance Layer, or PAL: “All payments pass through it.” The first post (July 2021, marked “Updated June 2022”) says the layer is built to hold no state of its own: “any PAL instance can be shut down without impacting our ability to process payments, and a new PAL can immediately be as effective as the other PALs already running. This makes our horizontal scaling linear.”

An edge without state has to put the state somewhere, and the second post (August 2021) says where and with what priority. It contrasts the edge with the accounting systems, the databases that hold the books: “Whereas for the latter the priority was uptime, for the accounting systems we don't mind if they are down for a little bit as long as we can guarantee their reliability and consistency.” Between the two sits a buffer. The PAL “saves the payment in a local database and a separate process picks it up when possible. This process will run behind if we have doubt about whether we can guarantee consistency in the accounting or if an accounting database is not available but that will not impact the availability of the PAL itself.” **What gives way is the freshness of the books.** The payment is answered now and booked later, from a durable queue.

<!-- illustration-placeholder
{
  "id": "37-path-and-record",
  "status": "pending",
  "asset": "assets/images/37-payment-reliability/37-path-and-record.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on the local database queue between the edge and the accounting systems",
  "visual_goal": "Show an answering path that keeps replying while the books run behind through a local queue.",
  "prompt": "Create a structural component diagram that reads left to right in two rows. Top row, the fast path: a customer with a phone at the far left sends a blue arrow labeled \"Pay\" to a row of three identical small server boxes grouped under the label \"Edge\"; one of the three boxes is greyed out with a small cross, and the other two still pass the arrow on. From the edge a blue arrow labeled \"Ask bank\" goes right to a generic bank building, and a green return arrow labeled \"Answer\" comes back through the edge to the customer. Bottom row, the slow path: from the edge a teal arrow labeled \"Save\" drops down into a small database cylinder labeled \"Local queue\" holding a stack of four paper slips. From the queue an orange dashed arrow labeled \"Later\" goes right to a large ledger book labeled \"Books\", with a small clock beside the arrow. A horizontal dashed line separates the two rows; at its left end a tag labeled \"Must answer\" above the line and a tag labeled \"Must be right\" below it. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Two rows: on top a customer's payment passes through interchangeable edge servers to a bank and gets an answer; below, the edge saves the payment to a local queue from which it reaches the books later.",
  "caption": "The split Adyen described in 2021: the edge must answer, the books must be right, and a local queue lets the books run behind without stopping the edge."
}
-->

Stripe described a different lever. Where Adyen lets the books lag, Stripe's engineering post of March 2017 on rate limiters refuses the less important request: “We divide up our traffic into two types: critical API methods (e.g. creating charges) and non-critical methods (e.g. listing charges.)” and “We always reserve a fraction of our infrastructure for critical requests.” **(Evidence age: 9 years; the current system may differ.)** Under overload a call that lists charges is turned away so that a call that creates one gets through ([[payment-developer-platform]] covers the limiters). No current source confirms those shedders in that form. The August 2026 post says only that Stripe's in-house proxy “supports retries, hedging, rate limiting, and dynamic priority-based request routing”. That hints that request priorities still exist; it does not confirm the 2017 design.

Stripe's isolation work is documented too, and it is documented from a failure. Its root-cause analysis of July 2019 describes the layout: “Stripe splits data by kind into different database clusters and by quantity into different shards. Each cluster has many shards, and each shard has multiple redundant nodes.” A shard is one slice of a database's data, held on its own set of machines. **(Evidence age: 7 years; the current system may differ.)** Redundant nodes did not save the API when one widely shared shard stopped working; a later section tells that outage. The remedies Stripe committed to were isolation: “additional circuit-breaking on failed operations to particular clusters” and “additional fault isolation techniques to contain the impact of a single failed shard and limit resource consumption by clients attempting repeated retries of failed requests”. The 2024 talk names “cell architecture” once, in a list of practices, with no detail; that phrase is the whole public record on cells at Stripe.

Beyond these accounts the public record thins out, well short of a design for either company. I found no Stripe account of where state sits on its API path, or of which steps of a payment it would skip under failure, and no Adyen account of shedding by request class. On failover between data centers Adyen says a few sentences and Stripe, for payments, none. Adyen's documentation on peak-season readiness (n.d., accessed November 2026) says: “With load balancers in front of every data center, transactions can be equally processed through any available data center. In the event that a data center is unavailable, these load balancers also manage the failover to the other data centers.” Its documentation on live endpoints (n.d., accessed November 2026) adds that in case of an infrastructure problem “alternative routing can be enabled to backup infrastructure and new infrastructure can be provisioned on demand”, and its Annual Report 2025 says “Adyen designs its platform to avoid single points of failure”. They give no topology and no timings. For Stripe I found no statement on failover of the payment path between data centers or regions; its 2023 annual letter says only that its systems “can automatically remediate many incidents by invoking redundant rails or enabling emergency fallback capabilities”. [[payment-multi-region-and-data-residency]] takes up what is known about where each runs.

What the two documented levers have in common is my reading, not either company's statement.

> **INFERENCE, NOT DOCUMENTED:** Both published designs relax something other than the record of a payment. At Adyen the books may be minutes behind; at Stripe a list call may be refused. In neither account is a payment allowed to be recorded twice or dropped to keep the path up. I read both as the same ordering: late before wrong. Neither company states this as a principle.

## The Designs: Skip, Queue or Refuse, Step by Step

Your own payment path needs the same decision, made one step at a time. When a step's dependency is unreachable, there are three designs. To **fail open** is to skip the step and let the payment proceed. To **queue** is to accept the payment and do the step later, from a durable record, as Adyen does with its accounting. To **fail closed** is to refuse or hold the payment. Failing open risks whatever the skipped step would have caught, queueing risks a late result, and failing closed risks the sale.

Which design fits follows from the step's job, and there are three jobs. A step that **records or reports** a payment can be queued: it may be late, but it may not be lost, so the queue must be durable. A step that **tells someone** (a receipt, a notification) can be queued or even skipped. A step that **decides whether money may move** is the hard kind. I refuse by default, and fail open only as a written decision with a bound on the loss, because that step exists to stop some payments. The table applies the rule; the defaults are my recommendations.

| Step | Its job | Default when its dependency fails | What the choice risks |
| --- | --- | --- | --- |
| Receipt or notification | Tells | Queue; the payment goes ahead | A late email |
| Ledger entry or report | Records | Queue durably; the payment goes ahead | Books behind for a while; a lost queue would be a lost record |
| Fraud score ([[payment-fraud-and-risk]]) | Decides | Fail open below an amount you set, refuse above it | Fraud losses up to the bound, for as long as the scorer is down |
| Check that the seller may take payments ([[platform-onboarding-and-verification]]) | Decides | Refuse, or hold | Lost sales if you refuse; a compliance breach and a loss if you let it through |
| Store of idempotency keys | Decides (whether this is a repeat) | Refuse or pause | A duplicate charge if you proceed without it |
| The issuer's authorization | Decides | Nothing to choose: without an answer there is no payment | An unknown outcome if the answer was lost on the way back |

Adyen's accounting queue is the queue. Adyen also documents a refusal: its documentation on API idempotency (n.d., accessed November 2026) says that when the store of keys is unavailable the API answers HTTP 503 with error 703, “required resource temporarily unavailable”, and leaves the next move to you: “Pause processing and retry the requests later (if this is feasible)” or “Fall back to non-idempotent processing by not submitting the `idempotency-key` HTTP header.” The provider fails closed and hands you the decision to fail open. For failing open the public case is old. In an engineering post of October 2014, read from an Internet Archive copy, Stripe's engineers guessed that cutting the network between charge processing and the fraud-scoring service “would cause these calls to time out and fail open (that is, allow the charge to go through immediately)”. The test instead “caused a spike in latency, where we’d expected calls to scoring-srv to time out and fail open quickly”. **(Evidence age: 12 years; the current system may differ.)** A fail-open path that has not been tested is a hope.

That 2014 surprise points at the commoner case: a failing dependency is more often slow than down. So every step needs a deadline, and at the outer edge a deadline turns slowness into unknown outcomes, by the thousand during an outage. Stripe's guide to advanced error handling (n.d., accessed November 2026) states it from the provider's side: “When a connection fails, you might not know whether Stripe received or executed the request.” Slowness also spreads: clients that retry at once add load to the system that is failing, which is why Stripe's 2019 remediation list includes limiting “resource consumption by clients attempting repeated retries of failed requests”. A retry therefore waits, with backoff and jitter, and carries the same idempotency key, the client-chosen identifier that lets the provider recognize a repeat ([[idempotency-and-retries]]).

## When It Fails Anyway: What the Public Incident Accounts Show

Designs like these reduce failures; they do not end them, and the question becomes what the providers tell you afterwards. An **incident report**, also called a root-cause analysis or postmortem, is a written account of what failed, why, and what will change. A merchant reads it for a fourth thing it rarely contains: what happened to the requests in flight. For failures of the payment path I found four such public documents from the two companies. (A second Stripe analysis, of January 2020, concerns customer data exposed at a vendor, not availability.)

The fullest is Stripe's analysis of 10 July 2019, and it describes a cascade. **(Evidence age: 7 years; the current system may differ, and [[payment-data-stores-and-consistency]] covers Stripe's later accounts of its databases.)** The summary: “two different database bugs and a configuration change interacted in an unforeseen way, causing a cascading failure across several critical services.” Two nodes of one shard “stopped emitting metrics reporting their replication lag but continued to respond as healthy to active checks”, and the shard could not elect a new primary. Then the isolation failed: “Because of widespread use of this shard across applications, including the API, the unavailability of this shard starved compute resources for the API and cascaded into a severe API degradation.” The second, longer window came from the repair: “our revert to a known stable version interacted poorly with a recently-introduced configuration change to the production shards.” Detection was not the problem: “Automated monitoring detected the failed election within a minute.”

For a merchant the telling part of that account is its unit. “We've sent you an email if you had five or more failed POST requests”: in Stripe's API a POST is the kind of request that creates or changes something, a payment included. And a failed POST is not a payment that did not happen. Stripe's current guide says: “Treat the outcome of a request that returns `500` as indeterminate: the operation might have produced side effects even though you received an error.” It also says what the provider does afterwards, and what it does not promise: “During incident recovery, Stripe attempts to reconcile failed operations and send webhook events for any objects created during reconciliation. The cached response doesn’t change, and reconciliation isn’t guaranteed to resolve every operation.” After an incident, objects may exist that no API response told you about, and **the provider documents that it may not resolve them all**.

Stripe's only later account is shorter. The 2023 annual letter gives a paragraph to “the most significant recent issue which happened on February 8, 2024 between 21:46 and 21:52 UTC”. It “affected a small subset of traffic—the three most impacted users had 39, 15, and 12 payments fail, respectively”, and the cause was “an erroneous change rolled out all the way to 1% of the critical tier of traffic”. Again the unit is payments per user, and again the trigger is a change, which [[payment-safe-change]] takes up. The status feed adds dates but not accounts. Its entry of 27 September 2026, marked major, reads in full: “From 00:32 UTC to 01:01 UTC, we saw elevated API errors. This issue is now resolved.” That is evidence that something happened, not an incident report.

Adyen's one public account concerns a failure set off from outside, where Stripe's two arose inside its own systems. On 21 April 2025 Adyen was hit by a distributed denial-of-service (DDoS) attack, a flood of requests from many sources meant to crowd out real ones. Its incident update (dated 21 April 2025) describes “a DDoS attack targeting services across our European datacenters”, with “the main impact for Ecommerce and In-Person Payment Transaction processing occurring between 18:51 CEST and 19:35 CEST”: 44 minutes. One sentence shows graceful degradation chosen under attack: “As a result of our deliberate mitigations, checkout services such as Session Integrations, Secured Fields, and Pay by Link, remained impacted throughout the entire incident.” The detail went elsewhere: “A detailed post-incident review, including root cause analysis and long term prevention measures, will be made available to our customers.” A follow-up of October 2025 names four changes, among them more DDoS mitigation partners and a re-architected load-balancing layer. The Annual Report 2025 records the year in one line: “In 2025, there was one instance of reduced availability, linked to the disruption incident referenced earlier.”

Each of the four says what broke and what was kept. None describes a failover between regions. None says how many payments ended with an unknown outcome. And neither company publishes postmortems as a routine: Adyen's Annual Report 2025 says “Each incident triggers a root-cause analysis”, but not that the analyses are published; the one review on record went to customers. You get that detail only by asking for incident reports under your contract, and by counting on your own side.

## Stripe and Adyen: Where They Differ

Gathered into one table, the documented differences are in what each company states and promises in public, which lever each has described, and how each has reported incidents. The last column is my reading and is inference throughout.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Stated availability target | 99.9995% (“five and a half nines” in the 2024 talk, the number in the 2026 post); no formula given | Not found (documentation, help center, site; November 2026); a 2023 post on internal service-level objectives gives no number | Stripe uses the number in public as an engineering constraint; Adyen reports outcomes |
| Reported figures | 99.999% for 2023 (letter of 2024); more than 99.9999% on peak weekends (2024, 2025); 99.999% over the last 90 days (status page, 17 November 2026); 99.9996% for critical APIs in 2025 (keynote, 2026) | 99.999% of Payments API requests over the last 30 days (status page, 17 November 2026); 99.9999% on the 2025 peak weekend; 100% in Australia (Q3 2026) | Neither publishes a consistent yearly series, so the figures cannot rank the two |
| Contractual commitment | Not found (documentation, help center, site; November 2026); the Services Agreement (General Terms, last modified September 2026) does not warrant uninterrupted use; paid support plans promise a 15-minute response, not availability | 99.9% per quarter by “commercially reasonable efforts”, with exclusions for issuing banks, acquirers, card networks and payment methods (terms of November 2023) | Plan against a written commitment; where none is public, ask for one |
| Documented lever: what gives way | Non-critical API methods are shed first (2017); circuit breaking and per-shard isolation committed after an outage (2019) | Accounting runs behind the edge through a local database queue (2021) | Both protect the answering path; each has published a different half of the design |
| Public incident accounts | One full root-cause analysis of an outage (2019); one paragraph in an annual letter (2024) | One incident update (April 2025) and one follow-up (October 2025); the detailed review went to customers | Public postmortems are rare at both; the detail has to be asked for under contract |
| Failover between data centers | Not found for payments (documentation, help center, site; November 2026); described for billing usage events (2025) | Stated in general terms: load balancers “manage the failover to the other data centers” (documentation, n.d., accessed November 2026); no timings or topology | No plan of yours can rest on either provider's failover |

On Stripe, ask for an availability commitment when you negotiate, since the public terms give none, and read the status history by machine, since it is published as a feed. On Adyen, read the exclusions before you rely on the 99.9%, because a failure at a card network or a payment method does not count against it. On both, ask for incident reports as a contractual right, and measure payment success yourself.

## In Practice at Larkfield: A Scripted Forty-Four Minutes

Larkfield depends on both providers, but one studio at a time. A studio is on one provider, so for most studios an outage of that provider means waiting, and Keel accepts this. The K8 switch moves online card payments at the 50 largest studios, which keep a verified account at both providers, and only payments that bring their own credential, such as a wallet payment or a typed card ([[payment-routing-and-orchestration]]). Renewals on a stored card wait for the provider that holds the card. The front desk has no second provider at all ([[in-person-payments]]).

What Larkfield controls completely is its own side of the path, and under Keel it has written down what gives way there when a provider is slow. The last line of the table is the one that matters: no step may record a payment as failed, or create a second one, because an answer did not come.

| Larkfield step | When the provider is slow or silent | Keel decision |
| --- | --- | --- |
| Checkout request from the member app | Deadline, then the row stays `pending` (waiting on the provider) and the member sees “checking” | K1, K2 |
| Renewal batch | Paused and paced; a late renewal is acceptable | K5 |
| Receipt email | Queued until the payment is confirmed | K2 |
| Ledger entry | Posted later, from the provider's report | K3 |
| Check that the studio may take payments | Read from Larkfield's mirror of the provider's status; refuse if it says no | K6 |
| Any timeout or server error | Never recorded as failed; never retried under a new key | K1 |

The drill of June 2027 tests that table. It injects faults at Larkfield's own provider adapter, in the provider's test environment, so it says nothing about either provider. The script is a degradation of 44 minutes, the length of the main impact window Adyen published for April 2025. Assume 2,000 payment attempts in the window, of which 1,240 are answered and **760 get no usable answer** *(assumptions for the drill)*. Now measure those 44 minutes against a contract. A 91-day quarter has 131,040 minutes; 44 of them are 0.034%. The quarter would stand at about 99.966%, inside a 99.9% commitment that allows about 131 minutes. An evening that leaves 760 unknown outcomes is no breach.

The 760 are then resolved one by one, without a new charge. Each row stays `pending`. The payment service resends each request under its stored idempotency key, inside Larkfield's limits of 20 hours on Stripe and 6 days on Adyen, and the provider answers a repeat with the result of the first attempt. What is still open goes to the sweep of decision K2, which confirms against the provider's own record ([[payment-webhooks-and-events]]). On Stripe that is the payment object, found by the Larkfield identifier stored in its metadata. Adyen's Checkout API has no call that returns a payment ([[payment-state-machines]]), so there it is the webhook and, failing that, the settlement report, Adyen's itemized record of what it processed ([[payment-reconciliation-and-reporting]]). In the drill 310 of the 760 turn out to have been approved and 450 never executed *(assumption)*. Had the 760 been marked failed, 310 members would have paid for a pass they did not hold.

The drill ends when the count of unknown payments is zero. That is hours after the scripted recovery on the Stripe side, and on the Adyen side it can be the next report. The time from recovery to zero, per provider, is the drill's result, and it is Femke's answer to Sofie. The switch plays a small part: thrown during the window, it sends new wallet and typed-card payments at the 50 largest studios to the other provider. The 760 stay where they are: a payment whose first attempt is unknown is never retried on the second provider. The sweep did the repair, which is why Larkfield built it before the switch.

## When It Goes Wrong: Recoveries That Make an Outage Worse

In the drill every prepared decision held. In practice the merchant's own recovery goes wrong in four ways, and the first is the most common: **a timeout recorded as a failure**. That is The Phantom Payment, and it invites The Double Charge, because the customer, or a job, then pays again. Larkfield's 1,840 double charges of November 2026 and the drill's 310 are the same error at two scales. Reconciliation detects it (payments in the provider's record with no successful row on your side); a state that means “unknown” prevents it.

The second failure is in the rate of recovery, not the record. When service returns, every queued request and every waiting job retries at once. The burst lands on a provider that is just recovering and on your own request limit, and requests are refused when you can least afford it. This is Larkfield's Renewal Wave produced by an outage: on 1 October 2026 the renewal job hit the rate limit, 7,900 renewals were delayed, and a refusal was treated as a failed attempt. The provider plans to contain such bursts, as Stripe's 2019 commitment shows. The remedy is pacing: backoff with jitter, interactive payments before the backlog, and a refusal that changes no payment state ([[payment-peak-load]]).

The third failure adds a second provider to the first two. A payment with an unknown outcome is sent to the other provider, which approves it; the first had approved it too, and the two share no idempotency key. And a second provider that has never carried traffic fails on the day for reasons of its own. Both belong to The Single Rail, [[payment-routing-and-orchestration]] covers them, and both are found only by rehearsal.

The last failure hides the other three: **declaring the outage over when the status page turns green**. The unknown payments are then nobody's, and they keep changing. Stripe's guide tells you to expect this: “Prepare your webhook handlers to process objects your integration hasn’t received in an API response.” An outage therefore has two ends, as the figure below shows. The first is the provider's: service restored. The second is yours: the count of payments that have been in an unknown state for longer than a set age is zero. That count needs an owner and an alert, or the second end never comes.

<!-- illustration-placeholder
{
  "id": "37-two-ends-of-an-outage",
  "status": "pending",
  "asset": "assets/images/37-payment-reliability/37-two-ends-of-an-outage.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on declaring the outage over when the status page turns green",
  "visual_goal": "Show that an outage has two ends: the provider's recovery, and the later moment when the merchant has no payment left with an unknown outcome.",
  "prompt": "Create a structural timeline illustration that reads left to right. A long horizontal time axis runs across the middle. On the left part of the axis, an orange shaded band labeled \"Outage\" covers a short stretch. At the right edge of the band, a vertical green flag on the axis labeled \"Service restored\", with a small status screen above it showing a green dot. Far to the right on the axis, a second, taller teal flag labeled \"Every outcome known\". Above the axis, between the two flags, a descending staircase of stacked paper slips, each slip marked with a question mark: a tall stack next to the first flag labeled \"760\", shrinking step by step to an empty tray next to the second flag labeled \"0\". Below the axis, between the two flags, a person at a desk with a magnifying glass over a record book, and a curved blue arrow labeled \"Sweep\" pointing from the person up to the shrinking stacks. A bracket under the stretch between the two flags is labeled \"Your part\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A timeline with a short outage band, a flag where service is restored, and a later flag where every outcome is known; between them a stack of 760 unknown payments shrinks to zero as a person sweeps them against a record book.",
  "caption": "An outage has two ends: the provider's, when service is restored, and yours, when the 760 payments with unknown outcomes have fallen to 0."
}
-->

## What to Take Away

**Established.**

- The published figures are different measurements: a target (Stripe, 99.9995%), a yearly figure (Stripe, 2023), peak-weekend figures (both), rolling figures (Adyen over 30 days, Stripe over 90) and a contractual commitment (Adyen).
- Adyen's public terms (November 2023) commit it to commercially reasonable efforts toward 99.9% per quarter and exclude failures at issuing banks, acquirers, card networks and payment methods. I found no public service-level percentage for Stripe.
- Each company has documented a design in which something other than the payment gives way: accounting that runs behind the edge (Adyen, 2021), non-critical requests shed first and per-shard isolation (Stripe, 2017 and 2019).
- A timeout or a `500` is an unknown outcome, in Stripe's own documentation, and Stripe says its post-incident reconciliation “isn’t guaranteed to resolve every operation”.
- Neither company publishes a failover design or routine postmortems. Adyen's documentation says only that load balancers fail over between its data centers.

**Depends on context.**

- Whether a deciding step may fail open depends on the loss you can bound. A fraud score on a €16.00 drop-in can be skipped; a check on whether a seller may be paid usually cannot.
- How long a customer-facing request may wait depends on the customer. A checkout can hold for seconds; a renewal batch can hold for hours.
- Whether a second provider is worth its cost depends on which payments can move at all. Stored cards and platform balances tie most of Larkfield's payments to one provider.
- How far to rely on a provider's own post-incident reconciliation depends on whether you can read its record. On Stripe you can fetch the object; on Adyen you wait for the webhook and the report.

**The author's synthesis.**

- I judge an outage by the time until every payment attempted during it has a known outcome. It is the only reliability measure that is wholly in my hands, on any provider.
- I build the sweep before the second provider connection, because the sweep repairs every outage and the second connection only shortens some.
- The provider and the merchant make the same decision at different scales: the provider lets its books lag or its list calls fail, and I let my answer to the customer be late, “checking”, before I let my record be wrong.

## Questions to Ask

1. Which availability figure is in our contract, over what period, and what does it exclude?
2. What do we measure ourselves: payment success per provider and per payment method, and who is alerted when it drops?
3. For each step of our payment path, is it skipped, queued or refused when its dependency fails, and who signed off on every step that fails open?
4. What does a payment look like in our records while its outcome is unknown, and can any code path turn that state into “failed” without the provider's record?
5. After a provider outage, which job finds every payment with an unknown outcome, and how do we confirm each one on each provider?
6. How long after the last outage or drill did it take until that count was zero?
7. When service returns, what stops our queues and jobs from retrying everything at once?
8. Which payments can move to a second provider, which cannot, and when did real payments last go through the second one?
9. Does our contract give us the provider's incident reports, and have we ever asked for one?

When Stripe emailed its users in July 2019, it was handing each customer its share of the outage; reliability, for a merchant, is how fast that share reaches zero. Everything in this chapter rests on one split: the path that must answer is kept independent of the record, and the record may lag but may not be wrong. That has a consequence. The record has to be kept right on its own terms, in databases that have themselves been divided into shards, with no transaction that covers all of them. [[payment-data-stores-and-consistency]] shows how.

## Sources and Evidence

*Company, product and investor sources*

- [Root cause analysis: significantly elevated error rates on 2019-07-10](https://stripe.com/rcas/2019-07-10), Stripe, 2019-07-12 — the two windows, the cascade from one shard, the revert that caused the second window, remediation items, the email to users with five or more failed POST requests (evidence age: 7 years).
- [Root cause analysis: Stripe Atlas founder data potentially accessible](https://stripe.com/rcas/2020-01-06), Alex Kehayias, Stripe, 2020-01-06 — Stripe's only other published root-cause analysis; it concerns data exposure, not availability (evidence age: 6 years).
- [Scaling your API with rate limiters](https://stripe.com/blog/rate-limiters), Paul Tarjan, Stripe, 2017-03-30 — critical and non-critical API methods; capacity reserved for critical requests (evidence age: 9 years).
- [Building a data plane from scratch: Stripe's own high-performance distributed proxy](https://stripe.dev/blog/building-a-data-plane-from-scratch-stripes-own-high-performance-distributed-proxy), Jack Loughran and Cara Mecozzi, Stripe, 2026-08-26 — the 99.9995% target; priority-based request routing.
- [Building a culture of system reliability](https://stripe.com/sessions/2024/building-a-culture-of-system-reliability), Rahul Patil with Farhan Thawar, Stripe Sessions, 2024-04-25 — the “five and a half nines” target and its 13 seconds a month; the single mention of cell architecture.
- [Stripe's annual letter 2023](https://stripe.com/annual-updates/2023), Patrick and John Collison, published 2024-03-13 — “only 99.999% available last year”; the incident of 8 February 2024; “redundant rails” and “emergency fallback capabilities” (quoted from the US edition of the letter's PDF).
- [Stripe annual letter 2024](https://stripe.com/annual-updates/2024), Patrick and John Collison, published 2025-02-27 — carries no reliability figure.
- [Stripe's 2025 annual letter](https://stripe.com/annual-updates/2025), Patrick and John Collison, published 2026-02-24 — carries no reliability figure.
- [Stripe annual letter 2022](https://stripe.com/annual-updates/2022), Patrick and John Collison, published 2023-04-05 — 90-day trailing availability “measured at the individual transaction level” (evidence age: 3 years).
- [Stripe's Black Friday and Cyber Monday 2024 release](https://stripe.com/newsroom/news/bfcm2024), Stripe newsroom, 2024-12-03 — API uptime greater than 99.9999% over the weekend.
- [Businesses on Stripe processed more than $40 billion from Black Friday through Cyber Monday](https://stripe.com/newsroom/news/bfcm2025), Stripe newsroom, 2025-12-02 — API uptime of more than 99.9999% over the weekend.
- [Stripe Services Agreement, General Terms](https://stripe.com/legal/ssa), Stripe, last modified 2026-09-28, accessed 2026-11-17 — no uptime or service-level figure; the disclaimer on uninterrupted use.
- [Advanced error handling](https://docs.stripe.com/error-low-level), Stripe, n.d., accessed 2026-11 — unknown outcome on a failed connection, indeterminate `500`, reconciliation during incident recovery.
- [Stripe status](https://www.stripestatus.com/), Stripe, n.d., accessed 2026-11-17 — “99.999% uptime for the last 90 days” for the Stripe API, as the page displayed it that day.
- [Stripe status history](https://www.stripestatus.com/history.json), Stripe, n.d., accessed 2026-11-17 — the author's count of entries for October 2026 on that date (160, of which 149 scheduled maintenance), the entries of 27 September 2026 and 20 October 2025.
- [Game Day Exercises at Stripe: Learning from `kill -9`](http://web.archive.org/web/20210622182916/https://stripe.com/blog/game-day-exercises-at-stripe), Marc Hedlund, Stripe, 2014-10-28, read from an Internet Archive snapshot of 2021-06-22 — fraud scoring expected to fail open (evidence age: 12 years).
- [Design to Duty: How we make architecture decisions at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture), Adyen, 2021-07-28 (marked “Updated June 2022”) — the stateless Payments Acceptance Layer (evidence age: 5 years).
- [Observability: Implementing Service Level Objectives](https://www.adyen.com/knowledge-hub/implementing-service-level-objectives), Alessandro Niciforo, Adyen, 2023-10-30 — internal service-level objectives with a “reliability target as a percentage”; no number given (evidence age: 3 years).
- [Design to Duty: The Accounting and Reporting Systems at Adyen](https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2), Willem Pino, Adyen, 2021-08-23 — uptime for the edge, consistency for accounting, the local database queue (evidence age: 5 years).
- [Adyen Terms and Conditions](https://www.adyen.com/legal/adyen-terms-and-conditions), Adyen, last updated 2023-11-01, accessed 2026-11-17 — clause 7.2, the 99.9% quarterly uptime commitment and its exclusions; clause 11.2, termination when it is missed for two consecutive quarters (evidence age: 3 years; the terms published for agreements from 1 November 2023).
- [Terms and conditions](https://www.adyen.com/legal/terms-and-conditions), Adyen, effective 2023-03-07, accessed 2026-11-17 — the same 99.9% commitment in the terms for agreements made before 1 November 2023 (evidence age: 3 years).
- [Adyen status](https://status.adyen.com/), Adyen, n.d., accessed 2026-11-17 — the 30-day figure, its definition, the statement that it is not the contractual commitment.
- [Adyen publishes H2 2025 financial results](https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2), Adyen, 2026-02-12 — the 2025 peak-weekend uptime figure.
- [Incident update: Mitigating a DDoS attack on April 21, 2025](https://www.adyen.com/knowledge-hub/mitigating-a-ddos-april-2025), Adyen, 2025-04-21 — the attack, the main impact window, the deliberate mitigations, the review for customers.
- [Strengthening Our Platform Resilience: An Update](https://www.adyen.com/knowledge-hub/strengthening-our-platform-resilience), Tom Adams, Adyen, 2025-10-31 — the four changes after the attack.
- [Annual Report 2025](https://investors.adyen.com/financials/2025), Adyen N.V., 2026-03-05 — single points of failure, one instance of reduced availability, root-cause analysis per incident (quoted from the PDF that this investor page offers for download; the PDF calls itself a “printed version” and names the report package filed with the regulator as the official one).
- [Live endpoints](https://docs.adyen.com/development-resources/live-endpoints), Adyen, n.d., accessed 2026-11 — alternative routing to backup infrastructure.
- [Opening remarks and product keynote](https://stripe.com/sessions/2026/opening-remarks-and-product), Stripe Sessions 2026, transcript accessed 2026-11-17 — “last year, our critical APIs retained 99.9996% availability” (vendor claim, no definition).
- [Support plans](https://stripe.com/support-plans), Stripe, n.d., accessed 2026-11-17 — “15-minute response SLA” for critical issues; “99.999%+ historical uptime”; no availability commitment.
- [How we built it: Usage-based billing](https://stripe.com/blog/how-we-built-it-usage-based-billing), Taras Mitran and Karan Dhabalia, Stripe, 2025-01-28 — usage events processed in two regions with automatic failover; not about payments.
- [Licenses and disclosures: Australia](https://www.adyen.com/licenses/australia), Adyen Australia Pty Ltd, n.d., accessed 2026-11-17 — quarterly availability disclosure required of members of the Reserve Bank of Australia's settlement system: “Accept card payments (businesses) 100%”, third quarter of 2026.
- [Peak season readiness](https://docs.adyen.com/industries/peak-season), Adyen, n.d., accessed 2026-11 — load balancers that manage failover between data centers.
- [API idempotency](https://docs.adyen.com/development-resources/api-idempotency), Adyen, n.d., accessed 2026-11 — HTTP 503 and error 703 when the key store is unavailable, and the caller's two choices.

*Standards, regulation and official documentation*

- None.

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
