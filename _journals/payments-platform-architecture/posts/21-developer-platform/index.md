---
title: "Keys, Sandboxes and Limits: The Developer Platform Around the API"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What else has to exist around a payment API before developers can safely build on it? Credentials that limit what each caller can do, a test environment whose gaps are stated and request limits you can plan for; each is a term of the API's contract, and Stripe and Adyen publish very different amounts about them."
permalink: payment-developer-platform
timetoread: 22 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what an API key may do, what a passing test run proves, and how to plan a batch against a request limit at Stripe and Adyen.

> **KEY POINTS:**
>
> * **Keys, test environments and limits are terms of the API.** Each decides something no endpoint does: what a leaked key can do, what a green test run has shown, and whether a request sent at a peak is accepted.
> * **Stripe publishes its limits and its test gaps; Adyen publishes neither for payments.** Stripe's documentation (accessed November 2026) gives 100 requests a second per account in live mode and 25 per endpoint. Adyen's lists no rate limit for its payments APIs, so a throughput has to be agreed in advance.
> * **A refusal is not a decline.** HTTP 429 means the provider did not try the payment. Pace a predictable peak yourself, repeat a refused request with the same key, and never tell a customer that their payment failed because of it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The First of the Month** — a renewal peak everyone could predict met a per-endpoint limit nobody had read.
> * **The Phantom Payment** — a request refused for volume was recorded as a failed payment, although the provider had never tried it.
> * **The Borrowed Blueprint** — Stripe's four limiters explain a provider that serves every customer at once; an integrator needs one bucket per endpoint.

<br>
On 1 October 2026 the renewal job at Larkfield, the fictional studio-software platform this book follows ([[meet-larkfield]]), ran code that had passed every test. By the next morning 7,900 members had an email saying their membership payment had failed. No bank had declined any of those payments, and nobody had asked a bank. **The provider had refused the requests because too many arrived at once.**

Nobody had planned for that refusal, and it points at what this chapter claims. The earlier chapters of this part produced a careful integrator: a payment service that retries with stored keys, receivers that read the provider's record after every event, a sweep over pending payments, a rehearsal before each version upgrade. All of that is traffic on a shared API, sent with credentials and rehearsed in a test environment. So three things have to exist around a payment API before anyone can safely build on it: **credentials that limit what each caller can do, a test environment whose gaps are stated, and request limits an integrator can plan for.** Each is a term of the API's contract, to be designed against like any field, because each decides something the endpoints do not: what a leaked key can do, what a passing test has shown, and whether a request sent at a peak is accepted.

**Where we are in the payment's journey.** This chapter is off the path of Mila Janssen's €120.00 class pass, bought from Studio Noord on Tuesday 9 March 2027 at 19:42, and it bears on every step of it. The request that created her payment carried a credential, counted against a limit, and ran code that was first exercised in a test environment.

The chapter starts with that Larkfield morning and the three questions it left. It then takes the three terms in the order an integration meets them: credentials, test environments and request limits. Next it sets Stripe and Adyen side by side, paces the Renewal Wave with Larkfield's numbers, and ends with the ways these terms go wrong.

## Setting the Scene at Larkfield: Three Questions About One Morning

For years the renewal job had a simple shape. On the 1st of each month, 38% of Larkfield's monthly renewals, about 357,000 payments worth €17.5 million, were attempted in a six-hour window. The job had no rate of its own: a pool of workers took renewals from a queue and sent each one as soon as the previous answer came back. In September 2026 the team raised the pool from 12 workers to 48 to finish sooner. On 1 October the part of the job that charges through Stripe began to receive HTTP 429, "Too Many Requests". The job treated every answer other than success as a failed attempt, retried three times at once and then marked the renewal failed. That status triggered the dunning email, the reminder a billing system sends after a failed payment ([[invoicing-collections-and-dunning]]). 7,900 renewals ended the day that way and were run again on 2 October.

Because of what the job did, the review looked for a bug and found none. When Femke de Graaf, who joined as head of payments engineering in January 2027, went through the incident with Tom Hendriks, the engineer who built the payment service, they found three questions that nobody had asked. Which key was the job using? It was an unrestricted Stripe secret key from 2017, shared with four other systems, and it could refund or pay out anything in the account. What had the test run shown? The job's tests sent a few hundred renewals to the test environment, never a wave. And which limit applied, and where was it written? The key did no harm that day; it is here because the review found it in the same place as the limit, among the terms of the API that nobody had read. The figure below shows the three.

<!-- illustration-placeholder
{
  "id": "21-three-terms-around-the-api",
  "status": "pending",
  "asset": "assets/images/21-developer-platform/21-three-terms-around-the-api.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph listing the review's three questions",
  "visual_goal": "Show a key, a rehearsal and a turnstile as three things a caller passes before reaching the API.",
  "prompt": "Conceptual scene, left to right. Far left: a small software-window icon with a worker figure beside it, the caller. Next: a wall rack holding five keys of different sizes, one large and four small, labeled \"Keys\". Next: a small stage with a curtain and a cardboard cut-out of a bank building, labeled \"Test\". Next: a turnstile with a counter display, labeled \"Limit\". Far right: a service counter with a clerk and a euro coin on it, labeled \"API\". A single blue arrow labeled \"request\" runs from the caller past the key rack and through the turnstile to the counter; a dashed teal arrow labeled \"rehearsal\" loops from the caller to the stage and back. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A caller's request passes a rack of keys and a turnstile on its way to a service counter, with a side loop to a rehearsal stage.",
  "caption": "Three terms stand between a caller and a payment API: the key it holds, the rehearsal it ran and the limit it sends into."
}
-->

## Credentials: What One Key Is Allowed to Do

A key to most APIs reads data. A key to a payment API can create refunds and payouts, which send money out of the account. The reach of each key is therefore a design decision: if a key leaks, or the system that holds it has a bug, the damage is whatever that key is allowed to do. **Least privilege** is the rule that follows: each calling system holds a credential that can do its own task and nothing else. Stripe's guidance on keys (n.d., accessed November 2026) states the rule as "People and systems must have only the privileges required to perform their jobs", and its keys page states the risk: "If a fraudulent actor obtains your secret key, they can harm your business."

Stripe, for example, lists four types of key (documentation n.d., accessed November 2026). An integration of one account uses three; the fourth, an organization key, spans several accounts. A **publishable key** (`pk_…`) identifies the account from a browser or an app, and Stripe says it is safe to embed in client code ([[tokenization-vaulting-and-pci]] covers what it is for). A **secret key** (`sk_…`) is an "API key that has unrestricted permissions on all Stripe APIs". A **restricted key** (`rk_…`) is a key whose permission you set per resource to None, Read or Write, and "The default value for all permissions is None". Test or live is part of the key: live keys "start with `pk_live_`, `rk_live_`, and `sk_live_`". What has changed is the advice. Of secret keys Stripe now writes: "Because you can’t limit their permissions, we don’t recommend using secret keys for new use cases, and for existing integrations, we recommend migrating secret key usage to RAKs", its abbreviation for restricted API keys. In server code, it adds, "restricted API keys are drop-in replacements for secret API keys".

Where Stripe makes restriction a kind of key, Adyen makes it part of every credential. Two terms first: an Adyen customer has one **company account** and, under it, one or more **merchant accounts**, the sub-accounts in which payments are processed. Adyen's documentation (n.d., accessed November 2026) defines an API credential as a username, an API key and "**Roles**: Permissions that define what the credential is allowed to do". Its scope follows the account: "Credentials created on a company account can access the company account, including all linked merchant accounts. Credentials created on a merchant account can only access that merchant account." Roles are per API and action, such as the "Checkout webservice role", and a credential can be tied to an allowed range of IP addresses. Adyen's advice is to split: "we strongly recommend creating a separate API credential for each channel" where a business sells both online and in person. The browser gets its own **client key**, which "is not used when making requests to our APIs".

## Test Environments: What a Passing Run Has Shown

After the key comes the rehearsal. A **test environment** (Stripe calls its own a sandbox; older material says test mode) is a copy of the API in which calls create simulated objects and no card network or bank is contacted. You choose the outcome. A **test card** is a card number that works only there and returns a known result, so a card that always answers "insufficient funds" lets you run your decline path. That is what a passing run shows: **your code handles each shape and state the API can return.** It cannot show how often real issuers (the cardholders' banks) decline, how long calls take or which limits apply, because the simulation produces none of these.

Stripe is the first example. It separates test from live by key, inside one account. Its documentation (n.d., accessed November 2026) lets an account "Use up to five sandboxes" besides a legacy test-mode sandbox, and says "API objects in one mode aren’t accessible to the other". Sandboxes are recent: Stripe's developer digest announced a private beta in June 2024 and wrote on 30 August 2024 that "Sandboxes is now in public beta"; its developer blog wrote on 7 May 2025 that "Stripe Sandboxes are now generally available (GA)". More useful is that Stripe states gaps. In a sandbox "the payments you create aren’t processed by card networks or payment providers". On load, "API limits are lower in a sandbox", and "creating a charge in live mode sends a request to a payment gateway and that request is mocked in a sandbox, resulting in significantly different latency profiles". On events ([[payment-webhooks-and-events]]), "We retry event deliveries created in a sandbox three times over the course of a few hours", against up to three days in live mode. A sandbox run therefore cannot rehearse the limit, the latency or the retry window you will meet in production.

Adyen, by contrast, separates by environment. Test and live have different endpoints, different Customer Areas (the Customer Area is Adyen's web portal for payments, settings, credentials and logs) and different credentials: "When you switch to your live environment, you must generate a new API key in your live Customer Area" (n.d., accessed November 2026). A live account is applied for, and each company account gets its own live hostname. Configuration does not travel either: "Adyen does not provide a "copy" function for moving your webhook configurations from the test environment to the live environment." **Adyen publishes no list of what its test environment cannot simulate.** It states gaps one payment method at a time, for example "MobilePay cannot be tested in the test environment". The nearest general statement is in a November 2026 engineering article about a simulator for payment methods that finish outside the checkout: "Getting a green happy-path response during integration testing doesn’t prove your integration will hold up under the conditions that actually matter at go-live."

Because only one provider lists the gaps, you have to write the list yourself and verify each item in production while someone watches. The Stripe entries below repeat its documentation. For Adyen they are my inference, not documentation: a simulation does not contact issuers, and the rate limits Adyen does publish for its Management API are given for live only.

- **Issuer behavior.** How many payments real banks decline, and with which codes. A test card returns what you asked for.
- **Latency.** How long a call takes when it passes through a card network.
- **Live limits.** The request limits of the live account: higher than a sandbox's at Stripe, unpublished for payments at Adyen.
- **The retry schedule for events.** At Stripe, three attempts in a sandbox against three days in live mode.
- **Live configuration.** Endpoints, credentials and roles, which at Adyen are created again in live and which a Stripe sandbox copies from live only "at creation time".

## Request Limits: Rate Limiting and Load Shedding

The third term is the one the renewal job met. One API serves every customer of the provider, so one customer's runaway script or sudden peak can slow payments for all the others. The provider's defense is to refuse requests, and there are two kinds of refusal. Stripe's engineering post of March 2017 defines both. "A rate limiter is used to control the rate of traffic sent or received on the network": a **rate limit** caps what one caller may send, and a caller who exceeds it gets HTTP 429. **Load shedding** is different: "A load shedder makes its decisions based on the whole state of the system rather than the user who is making the request." When the system itself is overloaded, it drops lower-priority requests from everyone so that critical ones keep working. You can plan against a rate limit; load shedding happens to you.

That post is also the only limiter design I found from either company. **(Evidence age: 9 years; the current system may differ.)** "At Stripe, we operate 4 different types of limiters in production", wrote its author, Paul Tarjan. Two act per user. The request rate limiter "restricts each user to N requests per second". The concurrent requests limiter caps work in progress: "You can only have 20 API requests in progress at the same time". Two are load shedders. The fleet usage load shedder splits traffic into "critical API methods (e.g. creating charges) and non-critical methods (e.g. listing charges.)" and reserves capacity for the first kind: with a 20% reservation, "any non-critical request over their 80% allocation would be rejected with status code 503". The worker utilization load shedder "is the final line of defense" and sheds by priority, "starting with test mode traffic" and reaching critical methods last. The post names its mechanism: "We use the token bucket algorithm", implemented with Redis. The figure below shows the four in one path.

<!-- illustration-placeholder
{
  "id": "21-four-limiters-in-one-path",
  "status": "pending",
  "asset": "assets/images/21-developer-platform/21-four-limiters-in-one-path.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph describing the four limiters of 2017",
  "visual_goal": "Show two per-caller limiters followed by two system-wide load shedders, with critical requests passing and lower-priority ones turned away.",
  "prompt": "Structural diagram, a horizontal path from left to right. Left: three stacks of envelopes of different heights, the callers; the tallest stack is orange. Four gates stand in a row on the path. Gate one, labeled \"Rate\": an orange arrow labeled \"too fast\" bends away from it back to the tallest stack. Gate two, labeled \"Concurrency\": a second orange arrow labeled \"too many open\" bends away. A bracket under gates one and two is labeled \"Per caller\". Gate three, labeled \"Fleet shedder\", and gate four, labeled \"Worker shedder\", share a bracket labeled \"Whole system\"; from each a gray arrow labeled \"low priority\" bends away downward. A thick green arrow labeled \"critical\" passes straight through all four gates to a row of worker figures at desks on the right. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Requests pass four gates in a row: a rate gate and a concurrency gate that turn back one fast caller, then two shedding gates that turn away low-priority requests while critical ones reach the workers.",
  "caption": "The four limiters Stripe described in 2017: two refuse one caller's excess, two shed lower-priority requests from everyone so that critical requests still reach a worker."
}
-->

Nine years later, Stripe's documentation (n.d., accessed November 2026) confirms part of that account. It confirms rate limits and concurrency limits per account, and it still speaks of the "concurrency limiter" shedding new requests. It contradicts one sentence: in 2017 "Our API provides the same rate limiting behavior in both test and live modes"; today sandbox limits are lower. It says nothing about the two load shedders, and no current source confirms that they still exist. What it adds is the numbers an integrator plans against. A refused request returns 429 with a `Stripe-Rate-Limited-Reason` header whose value names the limit that was hit, for example `global-rate` or `endpoint-rate`, and a large increase should be requested "at least 6 weeks in advance". Note the third row of the table: a batch that sends one kind of request meets the 25, not the 100.

| Limit, per Stripe account | Documented value |
| --- | --- |
| All API requests, live mode | 100 requests per second |
| All API requests, sandbox | 25 requests per second |
| One endpoint, unless noted ("each named API operation" is one) | 25 requests per second |
| Requests in progress at once, live mode | 50 by default |
| Creating payouts | 15 requests per second |
| Read requests | An average of at most 500 per transaction over 30 days |

Adyen publishes none of this for payments. Its documentation sitemap and help center (n.d., accessed November 2026) have no page on API rate limits, and the published definition of its Checkout API, version 72, contains neither the phrase nor a 429 response. Adyen does limit requests: its page on handling responses describes 429 as "You have sent too many requests in a short period" and advises "a retry mechanism that uses exponential backoff with jitter". It gives figures away from the payment path. The Legal Entity Management API, used to onboard a platform's sellers, states "Live environments: 700 requests per 5 seconds. Test environments: 200 requests per 5 seconds." Terminal-management endpoints of the Management API have per-minute limits that Adyen calls "indicative". Whether payment requests are limited per company account or per credential, and how Adyen sheds load, I found in neither its documentation nor its engineering posts.

The integrator has three designs for meeting a limit, compared in the table below. A **token bucket**, used in the second, is a counter refilled at a fixed rate: each request takes a token and waits when none is left. Both providers document the first design. Stripe documents the second ("a client-side token bucket rate-limiting algorithm") and the third. On Adyen the third is my recommendation, because there is no figure to pace against. None of the three calls for copying the four limiters of 2017: those protect a fleet from every caller at once, and an integrator needs one bucket per provider endpoint. [[payment-peak-load]] takes pacing, fairness and capacity further.

| Design | What it needs | What it costs | When it is right |
| --- | --- | --- | --- |
| **React**: back off with jitter on 429 and repeat | A retry path that keeps the idempotency key | Requests are delayed after the limit is already hit; a tight loop makes it worse | Always, as the floor; enough alone for interactive traffic |
| **Pace**: a client-side token bucket below the limit | A known figure; one place through which all calls pass | The batch takes longer | A predictable batch against a published limit |
| **Agree**: ask the provider for a figure or an increase | Lead time; your own computed rate | A dependency on an answer | No published limit, or a peak above it |

## Stripe and Adyen: Where They Differ

Taken together, the two providers document credentials and environments in comparable detail and differ most in what they publish about limits and test gaps. The last column of the table is my inference; the other cells are documented above or in "When It Goes Wrong" below (documentation n.d., accessed November 2026, unless a year is given).

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Server credentials | Secret keys with all permissions; restricted keys with None, Read or Write per resource, now advised over secret keys | Username, API key and roles; scoped to the company account or to merchant accounts; allowed IP range | Restriction is a choice of key at Stripe and a property of every credential at Adyen |
| Test environment | Sandboxes inside one account (up to five besides the legacy one), told apart by key prefix | A separate environment with its own endpoints, Customer Area and credentials; webhook configuration is not copied to live | A call to the wrong environment is harder at Adyen; drift between test and live configuration is likelier |
| Stated gaps of test | No card networks; lower limits; mocked latency; three webhook retries over a few hours | No list published; gaps stated per payment method; a 2026 engineering article says a green happy path proves little | At Adyen you write the list yourself |
| Rate limits for payment requests | 100 per second per account live, 25 in a sandbox, 25 per endpoint, 50 in progress | None published; 429 documented; figures only for Legal Entity Management and parts of the Management API | Stripe's limits can be read; Adyen's have to be asked for |
| Limiter design | Four limiters, described in 2017 (evidence age: 9 years) | Not public | No inference about Adyen is warranted |
| Request logs | Request logs in Workbench (2024) and a log link on each error; per a support article, 31 days for GET requests and 15 months for other requests | API logs for thirty days (JSON requests only); a seven-day dashboard | Stripe shows what you wrote for longer; keep your own request log on both |

So on Stripe, plan from the published page and ask only when your computed rate exceeds it. On Adyen, ask for the rate your company account may send before the first large batch, and write your own list of what test did not show. On both, treat live configuration as something you create and check deliberately.

## In Practice at Larkfield: Pacing the Renewal Wave

Start with Larkfield's arithmetic. The wave is about 357,000 renewals in six hours, which is 21,600 seconds: an average of about 17 requests a second, far below 100. Assume the wave splits between providers as volume does, 44% to Stripe and 56% to Adyen *(assumption)*: about 157,000 renewals on Stripe, or 7 a second, and about 200,000 on Adyen, or 9 a second. The average was never the problem. Each renewal is one request to the endpoint that creates a payment. Assume a call takes half a second *(assumption)*: 12 workers then send at most 24 requests a second, under Stripe's 25 per endpoint by luck, and 48 workers send up to 96. The rule: **requests ÷ seconds gives the average; workers ÷ seconds per call gives the burst; compare both with the per-endpoint and the per-account limit.**

<!-- illustration-placeholder
{
  "id": "21-burst-versus-paced",
  "status": "pending",
  "asset": "assets/images/21-developer-platform/21-burst-versus-paced.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that computes the wave's average and burst rates",
  "visual_goal": "Show that the same number of requests crosses a limit when sent in a burst and stays under it when paced.",
  "prompt": "Two-panel before/after chart illustration with a thin divider. Both panels share a horizontal dashed orange line labeled \"Limit\" at the same height and a horizontal time axis with a small clock icon. Left panel, labeled \"Burst\": one tall narrow blue block that rises far above the dashed line; the part above the line is hatched orange, with an orange arrow labeled \"refused\" pointing away from it. Right panel, labeled \"Paced\": a long low teal band of the same area, well under the dashed line, with a small funnel-and-bucket icon at its left edge releasing evenly spaced dots. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Left: a tall burst of requests crosses a limit line and its top is refused. Right: the same requests spread as a low band under the line.",
  "caption": "The same renewals sent as a burst cross the limit and are refused; paced over a longer window they stay under it."
}
-->

Decision K5 of Keel, Larkfield's 2027 program for its payment systems, answers the burst: renewals are spread and rate-limited by Larkfield, not by the provider. The wave now runs over 18 hours (64,800 seconds), which needs about 2.4 requests a second on Stripe and 3.1 on Adyen. The payment service holds one token bucket per provider and endpoint. The Stripe bucket for creating payments is set to 10 a second, well under 25, because members buying a pass in the app use the same endpoint and are waiting; they are served before the batch. The Adyen bucket is set to 5 a second, and is raised only after Larkfield has asked Adyen what its company account may send. A 429 changes no payment state: the renewal returns to the queue and is sent again after a backoff with the same idempotency key, as K1 requires ([[idempotency-and-retries]]). Stripe documents why that is safe: "Errors that occur before execution begins, such as invalid parameters, an invalid API key, or rate limiting, don’t cache a result."

With the limit planned for, the keys came next. Under K1 every money-moving call goes through the payment service, so only its credential can move money, and the shared 2017 secret key was retired once the last system had moved.

| Calling system | Task | On Stripe | On Adyen | What a leak allows |
| --- | --- | --- | --- | --- |
| Payment service | Create payments, refunds, payouts | Restricted key, write on those resources | Credential with the payment and transfer roles | Moving money; so it exists in one place |
| Webhook receivers | Re-read a payment after an event (K2) | Restricted key, read on payments | None: the Checkout API has no call that returns a payment ([[payment-state-machines]]) | Reading payment data |
| Reconciliation job, data warehouse | Fetch payouts and reports | Restricted key, read only | Credential with only the roles its reports need | Reading financial data |
| Billing integration | Studio subscriptions | Restricted key, write on billing resources | None | Changing subscriptions, not paying out |
| Front-desk app back end | Terminal payments | None | Its own credential, as Adyen advises per channel | In-person payments only |
| Booking app in the browser | Show the payment form | Publishable key | Client key | Nothing by API |

Finally, the first paced wave ran with people watching, because no test could show it. They watched four things: the count of 429s by reason, call latency, the share of issuer declines, and whether the wave finished inside 18 hours. A load test in a Stripe sandbox would have shown none of them, since its limit is 25 a second for everything and its latency is mocked; Stripe's own page says it "generally discourage[s]" the practice.

## When It Goes Wrong

The planning above still leaves three failures. The first is **a refusal recorded as a failed payment**. This is the Phantom Payment in reverse: your system believes a payment failed when the provider never tried it. It is detectable from the response alone. At both providers a refusal for volume is HTTP 429, and at Stripe it carries the reason header; Stripe adds that a 429 without that header "might be a lock timeout" on one object. A decline is a payment result with a refusal reason ([[payment-authorization]]). If your payment record has no way to say "not attempted", every refusal will be filed under "failed".

The second is **a key that leaks or does more than its task**. Permissions contain it first; rotation ends it. Stripe's documentation says "Rotating an API key revokes it and generates a replacement key that’s ready to use immediately", and a rotation in the Dashboard can keep the old key working "for up to 7 days". Adyen's overlap is fixed: "When you generate a new API key, it becomes active immediately. The previous key remains active for 24 hours to allow you to update your systems." A rotation you have never rehearsed is an outage of your own making.

The third is **a question about past requests that the logs can no longer answer**. Both recoveries begin with "what did we send?", and each provider shows you for a bounded time. Adyen's API logs hold "all API requests made in your test or live environment in the past thirty days", only for requests that use JSON; its developer dashboard covers seven days. Stripe's Workbench, announced in August 2024 as "our new home for developers within the Dashboard", shows request logs, and every Stripe error carries a `request_log_url`. Stripe's documentation pages give no retention period; an undated article on its support site (accessed November 2026) gives 31 days for GET request logs and 15 months for all other requests. Stripe's command-line tool can tail request logs, but "only supports displaying request logs from a sandbox"; Adyen's documentation index lists no command-line tool. The durable log of your requests is the one you keep.

## What to Take Away

**Established.**

- A payment key's permissions bound the damage of its leak. Stripe documents restricted keys and advises them over secret keys; Adyen documents roles and an account scope on every credential.
- A test environment simulates. Stripe states that sandbox payments reach no card network and that sandbox limits, latency and webhook retries differ from live.
- Stripe publishes its request limits (100 a second per account, 25 per endpoint) and described four limiters in 2017. Adyen publishes no general limit for its payments APIs and no limiter design.

**Depends on context.**

- One credential per calling system is right once more than one system calls the provider; a single service behind which everything passes needs fewer.
- Reacting to 429 is enough for interactive traffic. A batch whose size you know needs pacing, and needs an agreed figure where none is published.
- How much a green test run is worth depends on what the provider states about its gaps; where it states nothing, assume the gaps and verify in production.

**The author's synthesis.**

- I read a limit as a field of the API. The 7,900 emails of the opening were sent by code that was correct about every endpoint and had never read the page of numbers beside them.
- I give the money-moving key one home and treat a green test run as a statement about code paths only, because both mistakes stay invisible until the day they cost money.

Across this part, every protection the API offers turns out to have an edge. An idempotency key is remembered for at least 24 hours at Stripe and for 7 to 14 days at Adyen ([[idempotency-and-retries]]). An undelivered event is retried for up to three days at Stripe and up to 30 days at Adyen ([[payment-webhooks-and-events]]). A version is served until its notice runs out; Adyen gives two years after a Checkout version is deprecated ([[payment-api-versioning]]). A request is accepted up to a rate. Inside those edges the API can stand in for the slow process; outside them you are back in the gap between the instant answer and the slow truth, and only your own record of each payment, checked against the provider's, covers it. Each of Larkfield's four incidents assumed a contract wider than the documented one: a retry recognized without the same key (the Double Charge), a version that would never move (the Version Cliff), an event that always arrives (the Silent Webhook), a limit a predictable peak would not reach (the Renewal Wave). Keel decisions K1, K7, K2 and K5 restate those contracts in Larkfield's own terms. So for each provider, write down five terms from its documentation: what can be read back by identifier, key retention, the version pin and its notice period, the webhook retry window and acknowledgement deadline, and the request limits. Next to each, write what your own system does once that term runs out. That is why the payment service holds the keys, the receivers store before they acknowledge, and reconciliation against the provider's reports runs however reliable the webhooks have been.

## Questions to Ask

1. Which of our systems hold a credential that can create a refund or a payout, and why more than one?
2. If each key leaked today, what could its holder do, and how long would rotation take?
3. Which request limits does the provider publish per account and per endpoint, and how are a platform's requests on behalf of its sellers' accounts counted? (Stripe's rate-limit page says it for the read allocation only.)
4. Where no limit is published, what rate has the provider confirmed for our account, and in writing?
5. What is our batch's average rate and its burst rate, and which limit does each meet first?
6. Does our payment record have a state for "refused, not attempted" that sends no customer message?
7. What did our last test run not show, and who watched those things in production?
8. Which live configuration was created by hand, and how would we notice that it differs from test?
9. For how long can we answer "what did we send?" from our own logs?

This part showed what an API can hide when its contracts and their edges are designed in. Some things it cannot hide: the controls in the request path that decide who may hold a card number, who is trusted to be paying and who may be paid. Those do not disappear behind an interface; they assign data and losses to named parties, and [[part-5]] begins with them.

## Sources and Evidence

*Company, product and investor sources*

- [Scaling your API with rate limiters](https://stripe.com/blog/rate-limiters), Paul Tarjan, Stripe, 2017-03-30 — definitions of rate limiting and load shedding; the four limiters; token bucket and Redis (evidence age: 9 years).
- [Workbench: A new way to debug, monitor, and grow your Stripe integration](https://stripe.com/blog/workbench-a-new-way-to-debug-monitor-and-grow-your-stripe-integration), Michael Glukhovsky and Tomer Elmalem, Stripe, 2024-08-19 — Workbench announcement.
- [Stripe Developer Digest (June 2024)](https://stripe.dev/blog/stripe-developer-digest-june-2024-join-the-sandboxes-private-beta), Stripe, 2024-06-30 — Sandboxes private beta.
- [Stripe Developer Digest (August 2024)](https://stripe.dev/blog/stripe-developer-digest-august-2024-workbench-is-now-available-to-everyone), Stripe, 2024-08-30 — Sandboxes public beta.
- [Sessions 2025 Developer Track resources](https://stripe.dev/blog/sessions-2025-dev-track-resources), Ashley Ansari, James Beswick and Jon Byrum, Stripe, 2025-05-07 — Sandboxes generally available.
- [Making payment method testing repeatable: building the Adyen Payment Simulator](https://medium.com/adyen/making-payment-method-testing-repeatable-building-the-adyen-payment-simulator-5c11d6fcbe18), Ayodeji Ogundare, Henk Grent, Marc Sernatinger and Shantanu Tarey, Adyen, 2026-11-09 — what a green happy-path test does not prove (read through the publication's feed).

*Standards, regulation and official documentation*

- [API keys](https://docs.stripe.com/keys.md), Stripe documentation, n.d., accessed 2026-11 — the four key types and their prefixes, the advice against secret keys, rotation and its grace period (volatile).
- [Restricted API keys](https://docs.stripe.com/keys/restricted-api-keys.md), Stripe documentation, n.d., accessed 2026-11 — None, Read or Write per resource; drop-in replacement.
- [Best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md), Stripe documentation, n.d., accessed 2026-11 — least privilege.
- [Sandboxes](https://docs.stripe.com/sandboxes.md), Stripe documentation, n.d., accessed 2026-11 — sandbox payments are not processed by card networks.
- [Testing use cases](https://docs.stripe.com/testing-use-cases.md), Stripe documentation, n.d., accessed 2026-11 — up to five sandboxes; objects not shared between modes; settings copied at creation.
- [Rate limits](https://docs.stripe.com/rate-limits.md), Stripe documentation, n.d., accessed 2026-11 — every limit in the table, the reason header, load testing, limit increases (volatile).
- [Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks.md), Stripe documentation, n.d., accessed 2026-11 — retries in a sandbox and in live mode.
- [Advanced error handling](https://docs.stripe.com/error-low-level.md), Stripe documentation, n.d., accessed 2026-11 — rate-limited requests cache no idempotent result.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests.md), Stripe API reference, n.d., accessed 2026-11 — keys removable once at least 24 hours old.
- [Errors](https://docs.stripe.com/api/errors.md), Stripe API reference, n.d., accessed 2026-11 — `request_log_url`.
- [Stripe CLI](https://docs.stripe.com/cli.md), Stripe documentation, n.d., accessed 2026-11 — `logs tail` in a sandbox only.
- [Stripe request log retention period](https://support.stripe.com/questions/stripe-request-log-retention-period), Stripe Support, n.d., accessed 2026-11 — request logs viewable for 31 days (GET) and 15 months (other requests).
- [API credentials](https://docs.adyen.com/development-resources/api-credentials.md), Adyen documentation, n.d., accessed 2026-11 — username, key and roles; account scope; allowed IP range; separate credentials per channel; a new key in live; the 24-hour overlap on rotation.
- [Roles](https://docs.adyen.com/development-resources/api-credentials/roles.md), Adyen documentation, n.d., accessed 2026-11 — role names per API, including the Checkout webservice role.
- [Account structure](https://docs.adyen.com/account/account-structure.md), Adyen documentation, n.d., accessed 2026-11 — company and merchant accounts.
- [Client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication.md), Adyen documentation, n.d., accessed 2026-11 — the client key makes no API requests.
- [Live endpoints](https://docs.adyen.com/development-resources/live-endpoints.md), Adyen documentation, n.d., accessed 2026-11 — live account and hostname per company account.
- [Configure and manage webhooks](https://docs.adyen.com/development-resources/webhooks/configure-and-manage.md), Adyen documentation, n.d., accessed 2026-11 — no copy of webhook configuration from test to live.
- [Troubleshoot webhooks](https://docs.adyen.com/development-resources/webhooks/troubleshoot.md), Adyen documentation, n.d., accessed 2026-11 — retries for up to 30 days.
- [HTTP status codes](https://docs.adyen.com/development-resources/response-handling.md), Adyen documentation, n.d., accessed 2026-11 — HTTP 429 and backoff with jitter.
- [Alternative payment methods test credentials](https://docs.adyen.com/development-resources/test-cards-and-credentials/alternative-payment-method-credentials.md), Adyen documentation, n.d., accessed 2026-11 — MobilePay cannot be tested in the test environment.
- [Adyen documentation index](https://docs.adyen.com/llms.txt) and [sitemap](https://docs.adyen.com/sitemap.xml), Adyen documentation, n.d., accessed 2026-11 — no rate-limit page and no command-line tool listed; the help center and Adyen's knowledge hub were searched as well.
- [Adyen OpenAPI definitions](https://github.com/Adyen/adyen-openapi), Adyen, accessed 2026-11 — Legal Entity Management API v4 limits; Checkout API v72 declares no 429.
- [Automate the management of your terminals](https://docs.adyen.com/point-of-sale/automating-terminal-management.md), Adyen documentation, n.d., accessed 2026-11 — Management API limits, "indicative".
- [API idempotency](https://docs.adyen.com/development-resources/api-idempotency.md), Adyen documentation, n.d., accessed 2026-11 — keys valid 7 to 14 days.
- [Upgrade your integration](https://docs.adyen.com/online-payments/upgrade-your-integration.md), Adyen documentation, n.d., accessed 2026-11 — two years to upgrade after deprecation.
- [API logs](https://docs.adyen.com/development-resources/logs-resources/api-logs.md), Adyen documentation, n.d., accessed 2026-11 — thirty days of API logs, JSON requests only.
- [Developer dashboard](https://docs.adyen.com/development-resources/developer-dashboard.md), Adyen documentation, n.d., accessed 2026-11 — the seven-day dashboard.

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
