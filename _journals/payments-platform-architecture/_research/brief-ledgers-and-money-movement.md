# Research brief: Ledgers, balances, payouts, reconciliation, licences and safeguarding

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 12 (payment ledgers), 13 (balances and funds flows), 14 (payouts and money movement), 15 (payment reconciliation and reporting, provider side), 16 (licences and safeguarding), and parts of 03 (clearing and settlement), 35 (data stores and consistency) and 38 (safe change). The two anchors are Stripe and Adyen. Square, Uber, TigerBeetle and Modern Treasury appear only where they clarify a ledger design choice.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated documentation, legal and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade association, trade press, law firm), not from a primary document fetched in this session. The kind of source is named.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including **every** statement about how Stripe, Adyen or any other company works internally beyond what it has published.

**Evidence age matters.** Sources published before November 2023 are flagged **(evidence age: N years)** with a note on whether newer material confirms them. The two most important engineering sources differ in age: Stripe's Ledger post is from February 2024 (2.75 years, just inside the three-year line) and Stripe's Fee Credits post is from April 2026; Adyen's only engineering account of its accounting system is from August 2021 (**evidence age: 5 years**) and nothing newer was found. Documentation pages are living documents with no publication date; what they say today may differ next quarter.

**Research limitation.**

- **Adyen's 2025 Annual Report** (published 5 March 2026) could not be located as a fetchable PDF; the investor pages render their download links client-side. Nothing in this brief is taken from it. Statements about what Adyen's bank status lets it do come from its licences pages, its April 2026 press release and its documentation, not from its financial statements. The `companies` brief should carry the balance-sheet facts (payables to merchants, cash at central banks).
- **Airbnb's** 2017 engineering post on double-entry financial reporting returned HTTP 403 (Medium) by curl and by WebFetch; it is not used. **Coinbase** ledger material was not researched.
- **The European Payments Council's Verification Of Payee scheme page** returned HTTP 403; the EU rule is verified from the regulation's text instead, and the scheme rulebook's details are tagged as judgement.
- **Stripe's UK safeguarding support article** renders client-side; its content was read through a summarising fetch, so only the short phrases quoted here should be reused, and each should be checked against the page.
- **Stripe pricing pages** were served in Dutch to this session (Netherlands locale) regardless of the URL's locale; the Instant Payouts fee quoted is the one shown to a Netherlands visitor. The US fee was not verified.
- **Stripe's reserves** are documented for direct accounts only in support articles; no `docs.stripe.com` page for direct-account reserves was found (three candidate URLs returned 404).
- **Adyen's Balances sub-pages** on the reserve, the deposit and the next payout (`/account/balances-pilot/...`) returned 404; the parent Balances page was read.
- **Regulator registers** (Central Bank of Ireland, FCA, DNB) were not queried directly; licence statements are the companies' own, on their own legal pages.
- **PSD3 and the Payment Services Regulation**: status is from law-firm and trade sources found by search, not from the Official Journal.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: Global Payouts availability and preview status, pricing, payout limits and cut-off times, the Stripe acquirer list, the Bridge and Georgia charters, PSD3/PSR, and the UK safeguarding regime.

---

## PART 1: Ledgers (chapter 12; also 03, 35, 38)

### 1.1 Stripe's Ledger as publicly described (February 2024)

The primary source is one engineering post by Ilya Ganelin, "an engineer at Stripe who works on Ledger Platform", dated 16 February 2024 [VERIFIED: https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement, published 2024-02-16]. All quotes in this section are from that post.

**What it is.**

- "We built Ledger, an immutable and auditable log, as a trustworthy system of record for all of our financial data. Ledger standardizes our representation of money movement, and it serves as the scalable foundation for our automated Data Quality (DQ) Platform" [VERIFIED: same].
- Stripe names the network it runs on: the "Global Payments and Treasury Network (GPTN) that manages the complexity of accepting payments, money storage, and money movement" [VERIFIED: same].
- The stated reason for building it is not that accounting primitives were missing but that inputs are unreliable: "Many existing systems provide primitives for accurate accounting, but the real world is imperfect, incomplete, and constantly changing. We witness basic and obvious failures like malformed reports or propagated errors from banking or network partners, and also broad macroeconomic changes such as currencies ceasing to exist or large banks collapsing overnight." The goal is "a system that keeps these imperfections manageable and bounded" [VERIFIED: same].

**Why a ledger separate from the product systems.**

- Stripe segments its platform "into discrete services, databases, and APIs/gRPC interfaces", and "there is no intrinsic mechanism forcing these systems to represent or deliver data in the same way. Some might operate in real time, while others may operate on a monthly cadence with vastly different data volumes; some producers generate billions of events per day, while others may only generate a few hundred." Hence: "We require a mechanism that can deal with these variations and prove that these individual systems are collectively modeling our financials correctly" [VERIFIED: same].
- The design goal: "we want to represent all activity on the Stripe platform in a common data structure that can be analyzed by a single system" [VERIFIED: same].

**Fund flows as state machines.**

- "Ledger encodes a state machine representation of producer systems, and models its behavior as a logical fund flow—the movement of balances (events) between accounts (states)" [VERIFIED: same].
- "Accounts are buckets of money distinguished by their type (e.g., `charge_unsubmitted`) and properties (e.g., `id`, `business`)." "Events move money between accounts (e.g., `charge.creation` and `charge.release`)" [VERIFIED: same].
- Worked example in the post: "At time T0, the `charge.creation` event sets up a balance in the undisbursed account; then at T1, `charge.release` completes the flow and moves the funds to the `business_balance` account" [VERIFIED: same].
- Events are independent and may arrive out of order: "the creation and release events are completely independent. Even if they arrive out of order, or are created by different sources, Ledger maintains accurate fund flows through the identifier for `business` and `id`" [VERIFIED: same].
- Ledger models the producers' work, not a derived summary: "Instead of computing a derived dataset based on incoming data pipelines, Ledger models the actual work of producer systems, recording each operation as a transaction" [VERIFIED: same].
- Fund flows cross team boundaries. The post's example is "a business adding funds to its balance", which "requires moving funds between banks, reconciling money movement with third-party reporting, and matching regulatory reporting with financial reporting" [VERIFIED: same].
- Stripe calls following one transaction across systems "tracing": "we track individual transactions through their entire lifecycle. We call this tracing, and, at our scale, this totals to billions of daily transactions" [VERIFIED: same].

**Double entry and clearing accounts.**

- "Ledger is based on double-entry bookkeeping, a standard method for guaranteeing that all money in a system is fully accounted for by balancing credits and debits. Grounding our analysis in this construct gives us a mathematical proof of correctness" [VERIFIED: same].
- The pipes-and-reservoirs image: "At steady state, terminal (nonclearing) reservoirs are full, and intermediate (clearing) pipes are empty. If there is water stuck in the pipes, then you have a problem—in other words, unresolved balances on the balance sheet" [VERIFIED: same].
- Stripe applies bookkeeping to things that are not money movements: "we’re simultaneously modeling internal data system behaviors that may have nothing to do with physical movement of money—for example, currency conversion, report parsing, estimation, or billing analysis" [VERIFIED: same].
- How an error shows up: if a release event "is never published or has the wrong `id`, Ledger would not clear the balance in the associated `charge_undisbursed` account, and it would instead hold the balance in a different instance of `charge_undisbursed`". The detection query is simple: "Even when we have billions of transactions, a single missing, late, or incorrect transaction immediately creates a detectable accuracy issue with a simple query—for example, 'Find the clearing Accounts with nonzero balance.'" [VERIFIED: same].
- The post's account names are not consistent with each other (`charge_unsubmitted`, "the undisbursed account", `charge_undisbursed`); writers should quote them as examples, not as a schema [ASSUMPTION/JUDGEMENT].

**Immutability and correction.**

- "At its core, Ledger is an immutable log of events. Transactions previously published into Ledger cannot be deleted or modified, and we can always reconstruct past state by processing all events up to that point. All constructs—balances, fund flows, data quality controls, and so on—are transformations of the static underlying structure" [VERIFIED: same].
- Correction is by reversal and reprocessing, under review: "Because Ledger is an immutable log of events, we can’t run simple queries to mutate the state; instead, we have to revert and reprocess prior operations." Stripe "built a supporting utility to create and safely execute migrations, protected by a data quality tool that generates out-of-band reports on the production impact of proposed changes. Together, these tools approximate a CI pipeline for ad-hoc data repair operations. All operations must go through a two-phase review and commit of the data—and its associated DQ impact" [VERIFIED: same]. This is the passage chapter 38 (safe change) can use.
- Where problems come from: "Ledger problems are not usually problems of transcription or data modeling in Ledger. They primarily reveal real problems with system implementations, integrations, or physical money movement" [VERIFIED: same].

**Detection, not prevention: the three data-quality metrics.**

- "Clearing: Did the fund flow complete correctly? Timeliness: Did the data arrive on time? Completeness: Do we have a complete representation of the underlying data system?" [VERIFIED: same].
- "Clearing measures the fraction of Ledger that is appropriately zeroed out at steady state" [VERIFIED: same].
- Timeliness: "Producers create time stamps when integrating with Ledger, and we measure the delta between when data first enters the Stripe platform and when it reaches Ledger" [VERIFIED: same].
- Completeness: "we ensure that every ID in a producer database has a matching Ledger event", plus statistical models "for every account type that use historical trends to calculate expected data arrival time and, if events do not appear, we interpret this as potentially missing data" [VERIFIED: same].
- The metrics roll up into a score per team; the post shows a team-level view for "our periodic financial reporting, which we call Accounting Close", with "auto-generated tickets" and, for leaders, "the exact dollar impact of DQ issues". An example reads: "the 50% score for Aging Balances means that some clearing issues have persisted over time" [VERIFIED: same].
- Investigation tooling "generates SQL queries in Presto (our ad-hoc SQL query engine)" [VERIFIED: same].
- The post describes a system that **detects** errors after the fact; it says nothing about Ledger rejecting or blocking a money movement before it happens [ASSUMPTION/JUDGEMENT]. Its own roadmap confirms the latency: "In the future, we want to improve timeliness to minute-level analysis and response" [VERIFIED: same].

**Scale numbers (all Stripe's own, as of February 2024).**

- "Each day, Ledger sees five billion events and 99.99% of our dollar volume is fully ingested and verified within four days. Of that activity, 99.999% is monitored, categorized, and triaged through rich investigative tooling—while the remaining long-tail is reliably handled through manual analysis. Together, Ledger and the DQ Platform ensure over 99.9999% explainability of money movement, even as Stripe’s data volume has grown 10x" [VERIFIED: same].
- "we maintained a 99.999% readiness target, even as data volume grew 10x" [VERIFIED: same].
- Context given in the post's opening: Black Friday to Cyber Monday (2023) "300 million transactions with a total payment volume of $18.6B", API availability "greater than 99.999%" [VERIFIED: same].
- "Four days" for ingest-and-verify means the Ledger described is an after-the-fact proof system, not the system that answers a balance query during an API call [ASSUMPTION/JUDGEMENT].

**What the post does not say.** It names no storage engine for Ledger, no schema, no partitioning or consistency model, and does not say how the customer-facing balance (Balance and BalanceTransaction objects) is computed from or related to Ledger [ASSUMPTION/JUDGEMENT: absence checked by reading the full post].

### 1.2 Stripe's money-movement platform as described in the Fee Credits post (April 2026)

A second, newer post describes how a new balance type was added on top of Stripe's money-movement infrastructure [VERIFIED: https://stripe.dev/blog/how-we-built-stripe-credits-a-programmable-auditable-way-to-pay-your-stripe-fees, published 2026-04-16, authors Pratik Gupta and Sai Samant]. It is the best public evidence that the 2024 design is still current, and it names internal components. All quotes below are from it.

- **Money Movement and Storage (MMS).** "Rather than building a bespoke balance system just for credits, we extended Stripe’s existing Money Movement and Storage (MMS) platform, the infrastructure that handles real money movement across all of Stripe."
- **The financial account as the primitive.** "We used our existing well-tested primitive, the financial account, which represents an entity capable of holding a balance and participating in money transfers. Every real Stripe financial account—merchant payment balances, bank settlement accounts, treasury accounts—is backed by a real bank account."
- **Logical accounts.** "We created a new variant: purely logical financial accounts that aren’t backed by any real bank account. They carry a balance through Stripe’s internal ledger, but it never corresponds to real cash."
- **A three-phase transfer lifecycle.** "The mechanism for all value movement between logical accounts is the Originated Money Transfer (OMT), an existing MMS workflow that we repurposed for cashless operations. Every OMT follows a three-phase lifecycle through the ledger: submitted → prepared → disbursed."
- **A guardrail between logical and real money.** "We reject attempts to create a transfer between a logical account and a real account at the platform level, an important boundary that prevents logical ledger entries from accidentally triggering real cash movements downstream."
- **Cash sweeps are driven by ledger data.** "MMS runs automated intercompany sweeps based on ledger data. If logical financial accounts were allowed in sweeps calculations, the system could see a $100 incentive credit and attempt to sweep $100 in real cash—cash that doesn’t exist—between Stripe entities." Ledger entries on logical accounts are therefore "excluded from sweep calculations."
- **User funds versus corporate funds as an architectural classification.** Credits "aren’t user funds in the regulatory sense... we can classify the money sitting behind a credit as corporate funds. It doesn’t need to be safeguarded, swept to a bank account, or reconciled against a real cash position." This is direct evidence that safeguarding status is a property the ledger model carries (chapter 16).
- **One funds flow per economic case.** Prepaid and Stripe-funded credits "look identical to users but have fundamentally different ledger models. Collapsing them into a single accounting flow would have been an auditing nightmare." "Every step produces structured ledger events that downstream systems—reporting, data warehouse, general ledger—can consume without needing to recompute."
- **Fees before 2026.** "For years, Stripe collected all fees from a user’s primary payment balance." The fee settlement engine now "queries applicable credits and applies them just in time—fees are paid using credits before they touch the user’s primary balance."
- **Audit as a build requirement.** "Every state change is logged with an actor, timestamp, and approval link." The credit lifecycle is "a finite-state machine" with a "credit papertrail that ensures strict dual-approval flows."

How MMS, the "internal ledger" of this post and the "Ledger" of the 2024 post relate (same system, layers, or successors) is not stated in either post [ASSUMPTION/JUDGEMENT].

### 1.3 Adyen's accounting system as publicly described (August 2021)

The primary source is "Design to Duty: The Accounting and Reporting Systems at Adyen" by Willem Pino, Tech Lead, Adyen [VERIFIED: https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2, published 2021-08-23] **(evidence age: 5 years; no newer Adyen engineering account of the accounting system was found, so the numbers and the storage design may describe a replaced system)**. All quotes are from it.

- **Double entry, enforced by templates.** "For every payment that enters the system, we do double-entry bookkeeping. The way we ensure that we do so correctly is quite unique to Adyen. The only way to add new records to the accounting system is by means of templates. A template in this context is a recipe that takes certain amounts and accounts as input and converts them into specific journals that can be inserted into the ledger."
- **Templates are verified automatically.** "These templates are mathematically verified. To achieve this, we represent the amounts that serve as inputs by logical entities and prove that every combination of amounts will result in a net sum of 0. This verification is fully automated and runs on every change to the templates."
- **The invariant.** "All of this means we can guarantee that if at any time, we sum up all the records in the accounting system, the result will always be 0... for every euro that ever went through Adyen, we know exactly where it came from and where it went."
- **One accounting system for payments and the bank.** "We leverage this same system of accounting for our banking platform."
- **Built in-house.** "our accounting framework is also written in-house. Here the choice was evident, it is as core as can be to our business, and nothing in the open-source landscape came close to what we wanted."
- **Write volume.** "Over the lifetime of a payment transaction, about 50 rows have to be inserted into the accounting database. This means that per second, just for the accounting system, the amount of inserts is an order of magnitude higher than the hundreds of transactions we process every second."
- **Storage and sharding.** The accounting database is PostgreSQL; when it stopped scaling "we decided to shard our accounting database into several accounting clusters" using "a simple round-robin strategy with some parameters we can adjust", not merchant- or method-based routing, because "every rule we considered would bring its own problems". "At this point, we have... transactional databases of hundreds of terabytes running on the same technology."
- **The cost of sharding a ledger.** "consider a payout to a merchant. This needs to come from one account. However, because you processed these transactions on different clusters, the money needs to be transferred from one cluster to the other in order to end up in the same account. To do this without compromising on the strict correctness requirement was quite difficult. In the end, we created several jobs and processes that use back and forth messages between the clusters to keep everything aligned."
- **Availability versus consistency, decided per layer.** "Whereas for the latter [edge services] the priority was uptime, for the accounting systems we don't mind if they are down for a little bit as long as we can guarantee their reliability and consistency." The payment layer "saves the payment in a local database and a separate process picks it up when possible. This process will run behind if we have doubt about whether we can guarantee consistency in the accounting or if an accounting database is not available but that will not impact the availability of the PAL itself."
- **Reporting is split from accounting.** A separate reporting database holds "the relevant data in a denormalized form", fed by an in-house streaming system built on PostgreSQL and Java, chosen because, at the time, "exactly-once delivery was not yet supported by Kafka".

Nothing public was found on the internals of the Balance Platform's balance accounts (how a balance account relates to the accounting clusters, or how available balance is computed at authorisation time). Searched: Adyen knowledge hub and tech blog via web search for "accounting", "ledger", "double-entry", "balance platform" [ASSUMPTION/JUDGEMENT on absence].

### 1.4 Contrast accounts that clarify a design choice

**Square: Books (October 2019)** [VERIFIED: https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/, published 2019-10-16, author Łukasz Strzałkowski] **(evidence age: 7 years; describes Square in 2019)**.

- The problem with a single-entry settlement table: "when you want to trigger a bank settlement, you have to calculate the balance for a merchant. This requires doing an expensive group-by aggregate for each merchant", and "It’s impossible to split a single payment into multiple payouts, since there is a many-to-one relationship of payments to payouts."
- Prevention by construction: "you should never be able to transact with the database in a way that results in an illogical financial transaction. '$100 of paid-out ledger entries but $50 of payouts' should be impossible."
- Books as states: "we have four different books, called 'Payments', 'Refunds', 'Pending Balance' and 'Payouts'. Think of these as states in a state machine and we’re moving pennies between these states in bulk."
- Schema: three tables, `books`, `journal_entries`, `book_entries`, on Google Cloud Spanner; balances are cached on the book and each book carries "a monotonic counter... reflecting its current version".
- Correction: "You can’t update the data in place... what you want to do instead of updating is to write a new entry that corrects the previous one."
- Scale at the time: "the service is managing ~20TB of data and is developed and maintained by a small team of three people."

**Uber: Gulfstream and LedgerStore (2018–2021)** **(evidence age: 5–8 years)**.

- Design goals of the 2017 platform: "high reliability through an active-active architecture, exactly-once payment processing by the means of idempotency and strong consistency, auditability via double-entry bookkeeping", built on "asynchronous stream processing of immutable orders" [VERIFIED: https://www.uber.com/blog/payments-platform/, published 2018-12-05].
- "Gulfstream, Uber’s fifth generation collection and disbursement payment platform... is a single, integrated, SOX-compliant system built on the principles of double-entry accounting and can reconcile itself." The legacy design had separate collection and disbursement systems with "no holistic view of end-to-end money movements" [VERIFIED: https://www.uber.com/blog/money-scale-strong-data/, published 2020-10-02].
- "LedgerStore is an immutable, ledger-style database storing business transactions. LedgerStore provides signing/sealing of data to guarantee data completeness/correctness, strongly consistent indexes, and automatic data tiering." Its guarantees: "Individual records are immutable; Corrections are trackable; Unauthorized data changes and inconsistencies must be detected; Queries are reproducible a bounded time after write" [VERIFIED: https://www.uber.com/blog/dynamodb-to-docstore-migration/, published 2021-11-10].

**TigerBeetle (design documentation)**: a database whose only schema is debit/credit.

- "Another critical element of Debit/Credit systems is immutability: once transfers are recorded, they cannot be erased. Reversals are implemented with separate transfers to provide a full and auditable log of business events." "Where SQL allows destructive UPDATE and DELETE, TigerBeetle enforces append-only immutability" [VERIFIED: https://docs.tigerbeetle.com/concepts/debit-credit/, n.d., accessed 2026-11].
- Pending amounts are first-class: "A two-phase transfer moves funds in stages: Reserve funds (pending); Resolve funds (post, void, or expire)." A pending transfer "reserves its amount in the debit/credit accounts’ `debits_pending`/`credits_pending` fields" and leaves the posted fields unmodified [VERIFIED: https://docs.tigerbeetle.com/coding/two-phase-transfers/, n.d., accessed 2026-11].

**Modern Treasury (developer guide)**: "While mutating a balance directly is more efficient and simpler to implement, it’s more accurate to store immutable transactions and always compute balances from those transactions"; "in most cases, companies need to retrofit [accounting concepts] after painful incidents involving missing funds, broken payout flows, or inconsistent balances" [VERIFIED: https://www.moderntreasury.com/journal/accounting-for-developers-part-i, published 2022-08-17, updated 2025-08-13].

| Design choice | Stripe (2024, 2026) | Adyen (2021) | Square Books (2019) | TigerBeetle |
| --- | --- | --- | --- | --- |
| Where correctness is enforced | Detected afterwards: clearing accounts with nonzero balance, timeliness, completeness | Prevented at write: only verified templates may write journals | Prevented at write: the service rejects unbalanced entries | Prevented at write: the database only accepts transfers |
| Who writes | Many producer systems publish events | The payment layer, through a queue, into accounting clusters | Tenant services ("shelves") call one service | Application code |
| Balance | A transformation of the immutable log | Not described | Cached on the book row, versioned | Fields on the account (pending and posted) |
| Stated storage | Not stated | PostgreSQL, sharded round-robin | Google Cloud Spanner | Its own engine |
| Correction | Revert and reprocess, two-phase reviewed | Not described | New correcting entry | New correcting transfer |

[ASSUMPTION/JUDGEMENT] The table's first row is the analyst's reading. "Detected" and "prevented" are not exclusive: Stripe's 2026 post shows platform-level rejections too (logical-to-real transfers), and Adyen reconciles against partner reports after the fact (PART 4).

### 1.5 Stripe vs Adyen: ledgers

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Public engineering account | Two posts, Feb 2024 and Apr 2026 | One post, Aug 2021 (5 years old) | Stripe's public record is newer and deeper; Adyen's may be out of date |
| Invariant | Clearing accounts return to zero at steady state | Sum of all records is always zero, by verified templates | Same double-entry idea; Stripe stresses finding failures, Adyen stresses making them unrepresentable |
| Number of writers | Many independent producers with different cadences | One in-house accounting framework | Consistent with Stripe's service-per-product organisation and Adyen's single platform; not stated by either |
| Scale figure | Five billion events a day (2024) | About 50 rows per payment; thousands of inserts a second (2021) | Not comparable: different units and years |
| Storage | Not public | PostgreSQL clusters (2021) | — |
| Ledger also serves the bank/treasury product | Financial accounts back merchant balances, bank settlement accounts and treasury accounts (2026) | "We leverage this same system of accounting for our banking platform" (2021) | Both reuse one accounting core across payments and stored-value products |

**For readers new to payments.**

- **Double-entry bookkeeping**: every movement of value is recorded twice, as a debit to one account and an equal credit to another, so the total of all entries is always zero and a missing half is visible.
- **Ledger**: the append-only record of those entries; balances are computed from it and never edited directly.
- **Clearing account**: a temporary account that holds an amount while a multi-step process is in flight and must return to zero when the process completes; a balance that stays is an unfinished or broken process.
- **Fund flow** (funds flow): the defined path an amount takes through accounts for one kind of business event, for example charge created, funds released to the merchant balance, paid out.

**Architecture implications** [ASSUMPTION/JUDGEMENT].

- A payment company runs at least three stores that all contain "the money": the payment database (fast, mutable state per payment), the ledger (immutable, complete, slower) and the reporting store (denormalised). Both companies' posts show the split; neither treats the ledger as the request-path database for authorisation.
- The choice between validating at write (Adyen, Square, TigerBeetle) and proving after the fact (Stripe 2024) follows from how many systems write. One writer can enforce a template; hundreds of producers with monthly files and real-time events cannot be forced through one synchronous gate, so the invariant is checked continuously instead.
- Sharding a ledger moves the hard problem to the points where money crosses shards (Adyen's payout example). A design that shards by merchant avoids that for payouts and reintroduces it for scheme-level aggregates.
- A platform builder should copy the invariants (immutability, zero-sum, clearing accounts that must empty, corrections as new entries) and not the scale machinery.

---

## PART 2: Balances and funds flows (chapter 13; also 03)

### 2.1 Stripe: balances and their states

- A Stripe account "can have one or more balances that hold funds for different products and currencies". Documented types: the **payments balance** ("all of your incoming transactions from customer charges"; refunds and disputes are deducted from it), the **refunds and disputes balance** ("set aside funds for future refunds or disputes", funded by an external top-up), the **reserve balance** (created by Stripe; "holds funds that you can’t pay out or transfer until the reserve hold period is complete") and the **financial account**, "US and UK only", which "lets you store funds with Stripe in USD, GBP, or EUR" [VERIFIED: https://docs.stripe.com/payments/balances.md, n.d., accessed 2026-11].
- Two states: "Funds in the pending state represent incoming transactions that haven’t settled into your balance... the charge amount (minus Stripe’s fee) appears in your pending balance until settlement." "After the funds settle, they move to your available balance." The transition happens "at the corresponding `available_on` time for each balance transaction" [VERIFIED: same].
- Each change to a balance is a **balance transaction** with `amount`, `fee`, `fee_details`, `net` ("You can calculate the net impact of a transaction on a balance by `amount` - `fee`"), `status` ("either `available` or `pending`"), `available_on`, `exchange_rate`, `reporting_category`, `source` and a `balance_type` of `payments`, `issuing`, `refund_and_dispute_prefunding` or `risk_reserved` [VERIFIED: https://docs.stripe.com/api/balance_transactions/object.md, n.d., accessed 2026-11].
- Stripe's Sigma documentation calls the table "the canonical record of changes to your Stripe balance" [VERIFIED: https://docs.stripe.com/stripe-data/available-data.md, n.d., accessed 2026-11].
- The `type` enum shows the funds flows a balance can see, including `charge`, `payment`, `refund`, `refund_failure`, `payout`, `payout_failure`, `payout_cancel`, `transfer`, `topup`, `stripe_fee`, `stripe_fx_fee`, `reserve_hold`, `reserve_release`, `reserved_funds`, `reserve_transaction`, `payment_network_reserve_hold`, `payout_minimum_balance_hold`, `connect_collection_transfer`, `fee_credit_funding` and `payment_unreconciled` [VERIFIED: same balance transaction object page].
- With Connect, "your platform account and each connected account has its own `pending` and `available` balances", and "a platform account can also have a `connect_reserved` balance, used to offset negative balances on connected accounts" [VERIFIED: https://docs.stripe.com/connect/account-balances.md, n.d., accessed 2026-11].
- The balance transaction is a single-sided statement line (one amount, one fee, one net against one balance), not a double-entry journal; its relation to the internal Ledger of PART 1 is not documented [ASSUMPTION/JUDGEMENT].

### 2.2 Stripe: settlement timing

- "Settlement time is the time between when a payment or a funding transaction is made and when the funds become available in your Stripe balance." Example: a 100 USD US card payment on Monday is "available in your balance on Wednesday, 2 business days later" [VERIFIED: https://docs.stripe.com/payments/balances.md, n.d., accessed 2026-11].
- ⚠ By country (initial timing for the first payout, then default): United States 2 business days; most European countries including the Netherlands, Germany, France, Ireland and the United Kingdom "7 calendar days" initially, then "3 business days"; Japan 7 calendar days then 4 business days; Australia 2 business days; Brazil 30 calendar days; India 2 business days domestic, 5 international. "In some cases, risk criteria might prevent your account from changing to the default settlement timing" [VERIFIED: same].
- ⚠ By payment method: ACH Debit 4 business days, SEPA Direct Debit 6, Bacs Direct Debit 4, PAD Canada 5, USD bank transfers 5. Stated reason: "These payments have a higher risk of returns or reversals, which factors into their longer settlement periods" [VERIFIED: same].
- The documentation defines availability by a schedule per country and method. It does not say that availability waits for the card networks' own settlement of each transaction, nor that it does not [ASSUMPTION/JUDGEMENT: see 2.7].

### 2.3 Stripe: fees, reserves, negative balances, multi-currency

**Fees.** Fees are netted per transaction: the pending amount is "the charge amount (minus Stripe’s fee)" [VERIFIED: https://docs.stripe.com/payments/balances.md, n.d., accessed 2026-11]. Other fees are debited from the balance: "Your account might have fees debited from your balance on a daily or monthly basis" [VERIFIED: same]. Since 2026 eligible fees can be paid from a separate fee-credit balance first (1.2).

**Reserves.**

- "A reserve is a temporary hold on a portion of a business's funds for a predetermined period of time"; "Stripe uses two different types of reserves: fixed and rolling"; "Reserves are intended to cover any anticipated losses that may result from a business's processing activity" [VERIFIED via summarising fetch: https://support.stripe.com/questions/reserves-frequently-asked-questions, n.d., accessed 2026-11].
- Platforms can create reserves on connected accounts as a hold ("a single amount that releases on a specified date") or a plan ("automatically creates a hold for a percentage of each charge"). "You can’t reserve funds for longer than 180 days." "Any refunds or disputed funds from a transaction are automatically taken first from reserved amounts associated with that transaction" [VERIFIED: https://docs.stripe.com/connect/connected-account-reserves.md, n.d., accessed 2026-11]. ⚠ The Reserves API is referenced at a preview API version (`2025-08-27.preview`).
- A voluntary equivalent is the **minimum balance**: "Automatic payouts only pay out funds exceeding this minimum balance to your bank account"; not supported in Brazil, India and Thailand [VERIFIED: https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md, n.d., accessed 2026-11].

**Negative balances.**

- "if you receive 100 USD in payments but refund 200 USD of prior payments, your account balance would be -100 USD. If you don’t receive further payments to balance out the negative amount, Stripe creates a payout that *debits* your bank account." "A negative payout is a Payout object with a negative `amount`" [VERIFIED: https://docs.stripe.com/payouts.md, n.d., accessed 2026-11].
- A merchant can also add funds by bank transfer "when your account has a negative balance or when you expect an increase in customer refunds or disputes"; in the US, UK, euro markets and Japan the funds go to "a Stripe VBAN (which helps reconciliation speed)" [VERIFIED: https://docs.stripe.com/get-started/account/add-funds.md, n.d., accessed 2026-11].
- On a platform: "If at all possible, Stripe automatically offsets negative transactions against future payments." Who covers a connected account's negative balance is a property of the account (`controller.losses.payments` in Accounts v1, `defaults.responsibilities.losses_collector` in v2), with the value "`stripe` if Stripe is responsible and `application` if your platform is responsible" [VERIFIED: https://docs.stripe.com/connect/account-balances.md, n.d., accessed 2026-11].
- Where the platform is responsible, "Stripe holds a reserve on your platform account’s `available` balance"; "When a connected account holds a negative balance amount for 180 days, Stripe transfers a portion of your balance to zero out that account’s balance by creating a balance transaction with the type `connect_collection_transfer`" [VERIFIED: same].
- Holding funds is limited: "For compliance reasons, we can hold funds in reserve for a period of time that’s based on the country the business is in": Thailand 10 days, United States 2 years, all other countries 90 days [VERIFIED: same]. ⚠

**Multi-currency.**

- "Stripe automatically converts all incoming funds into your default currency. With multi-currency settlement, you can configure your account to accrue balances and get paid out in up to 18 supported currencies" [VERIFIED: https://docs.stripe.com/payouts/multicurrency-settlement.md, n.d., accessed 2026-11]. ⚠ Available for accounts in AE, AU, CH, EU, GB, HK, LI, NO, SG, US.
- "To receive payouts in a settlement currency, you must add a separate supported bank account with the same currency." "Stripe charges the applicable fee when funds settle into a non-primary settlement currency, not when you initiate a payout" [VERIFIED: same].
- Conversions carry the rate on the balance transaction: "If money converts from currency A to currency B, then the `amount` in currency A, multiplied by the `exchange_rate`, equals the `amount` in currency B" [VERIFIED: https://docs.stripe.com/api/balance_transactions/object.md, n.d., accessed 2026-11].

### 2.4 Adyen: payable batches, Sales day payout and Pass-through payout

- The steps "From capture to payout": "**Capture**: A payment is captured, and the card scheme or payment method sends the funds to Adyen. **Adyen processing**: The funds are assigned to a payable batch based on your payout model. The payable batch closes according to your payout frequency. If the payable balance is positive when the payable batch closes, Adyen instructs the payout to you. **Bank processing**: Your bank processes and clears the funds" [VERIFIED: https://docs.adyen.com/account/getting-paid.md, n.d., accessed 2026-11].
- "Payouts are sent separately to each of your merchant accounts" [VERIFIED: same].
- **Sales day payout** (default, recommended): "the funds you get do not depend on the settlement timelines of the schemes and payment methods used by your shoppers. You get all the funds from a particular sales day in a single payout batch, with a fixed payout delay" [VERIFIED: https://docs.adyen.com/account/sales-day-payout.md, n.d., accessed 2026-11].
- **Pass-through payout**: "Sales are assigned to the payable batch as soon as the schemes or payment methods send the funds to Adyen", so "The sales from Monday, January 1 are paid out in separate batches over the subsequent days, from January 2 to January 7"; it "Requires automated reconciliation". It is "the only available payout model in Africa, Brazil, and India" [VERIFIED: https://docs.adyen.com/account/pass-through-payout.md and https://docs.adyen.com/account/sales-day-payout.md, n.d., accessed 2026-11].
- **Payout delay** is derived, not arbitrary: "The payout delay is calculated to be the break-even point, where faster payment methods settle enough funds to make up for the funds not yet settled by the slower payment methods." ⚠ Typical values: 2 business days when "At least 80% of the transactions are in AUD, CAD, EUR, GBP, NZD, RON, SEK or USD" and acquired in the currency's own region; 3 business days otherwise; "3, 7, or 12 business days" for accounts onboarded through a partner. "American Express has a settlement delay of 7 days. If you process most payments through American Express, Adyen will set your payout delay to 7 business days" [VERIFIED: https://docs.adyen.com/account/sales-day-payout.md, n.d., accessed 2026-11].
- **Sales day and batch close**: a sales day is by default midnight to midnight in the merchant account's time zone, configurable up to 6:00 AM; "the payable batch always closes two hours after your sales day closing time"; "After the payable batch closes we create a bank instruction to pay out to you" and report generation starts [VERIFIED: same].
- **Adjustments are not tied to the original sales day**: "Refunds, chargebacks, and other adjustments are added to the payable batch as they occur and are not related to the sales day of the original transaction" [VERIFIED: same].
- **Bank holidays** stop both directions: "clearing for a specific currency may be closed and therefore Adyen cannot process payouts. Adyen also cannot receive funds" [VERIFIED: https://docs.adyen.com/account/getting-paid.md, n.d., accessed 2026-11].

### 2.5 Adyen: balances, reserve, deposit, and how fees reach the merchant

- A merchant account's **available funds** are the sum of: "**Pending**: the gross amount of sales and refunds that have not yet been settled by the respective card scheme or payment method"; "**Next payout**: the current amount to be settled to your bank account at the next moment of payout"; "**Reserve**: the available amount you configure to cover for refunds, chargebacks, and other operational expenses. The reserve is only used if you have insufficient in-process funds"; and a "**Negative refund allowance**", which "Adyen decides who is eligible to get" [VERIFIED: https://docs.adyen.com/account/balances.md, n.d., accessed 2026-11].
- The **Deposit** is separate and set by Adyen: "the amount withheld by Adyen to cover potential losses and liabilities due to payment processing... Unlike the reserve, you cannot determine your own deposit amount. Adyen calculates the deposit requirement for your account daily, based on variables such as your processing volume and the number of chargebacks and refunds." "If the deposit requirement increases, funds from your sales are booked to the deposit. If the deposit requirement decreases, the excess deposit is released and added to the next payout amount" [VERIFIED: same].
- Note the naming trap: Adyen's "Reserve" is merchant-configured and its "Deposit" is provider-imposed, the reverse of how Stripe uses "reserve" (provider-imposed) [ASSUMPTION/JUDGEMENT: comparison of the two quoted definitions].
- **Fees are netted from the batch and also invoiced monthly.** "Adyen pays you on a net basis. This means your payable batch is made up from your sales figure from which we deduct: Transaction costs; Refunds; Chargebacks; Other adjustments, for example balance transfers" [VERIFIED: https://docs.adyen.com/account/getting-paid.md, n.d., accessed 2026-11]. "Each month, Adyen gives you a Payment processing invoice for your company account." "There can be a difference between the costs in the invoice and the deductions from your settlement batches during the month. Adyen will credit or debit the difference to the next settlement batch for the corresponding merchant account." "Adyen does not deduct sales tax or value-added tax (VAT) from your settlement batches" [VERIFIED: https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice.md, n.d., accessed 2026-11].
- In the settlement details report these appear as journal types: **InvoiceDeduction** ("if we debit an amount that you owe or credited an amount that you overpaid"), **DepositCorrection** ("when a deposit change happens in your account"), **ReserveAdjustment** and **MerchantPayout** ("the payout from Adyen to your bank account. It includes a reference, batch number, and the bank account") [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report.md, n.d., accessed 2026-11].
- **Negative balance**: "If the amount to be paid out on the Payout Day... is negative, Adyen may in its discretion (i) transfer such negative balance to the immediately following Payout Day, or (ii) exercise its set-off right or other rights in accordance with the terms of the Agreement" [VERIFIED: https://www.adyen.com/legal/sales-day-payout-terms-of-service, last update 2024-06-17].

### 2.6 Adyen for Platforms: balance accounts and sales day settlement

- "After processing transactions for your users, Adyen sends the funds to one of your merchant accounts. These funds are split among your users and your platform, and then settled in the corresponding balance accounts" [VERIFIED: https://docs.adyen.com/platforms/settle-funds.md, n.d., accessed 2026-11].
- Structure: "you must have a balance platform and merchant account in each region that you are registered and wish to acquire payments"; the platform has "A liable account holder for your platform, and a liable balance account to hold your platform's funds" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources/platform-structure.md, n.d., accessed 2026-11].
- "Adyen uses a sales day settlement model where the funds are settled independently of the timelines of schemes and payment methods involved in the transaction." "Adyen settles a settlement batch after its sales day ends and the configured settlement delay has passed. The date when the schemes or payment methods transfer the funds to Adyen does not affect this timing" [VERIFIED: https://docs.adyen.com/platforms/settle-funds.md, n.d., accessed 2026-11].
- ⚠ "The pass-through settlement model is deprecated and not available for new integrations", except for Affirm and `maestro_USA` [VERIFIED: same].
- The **settlement delay** is "a waiting period for any adjustments before settlement. The default delay is defined in your contract and varies by region and payment method"; with managed payouts Adyen "automatically optimizes the settlement delay"; with custom payouts the platform can configure it [VERIFIED: same].
- The Balance Platform accounting report "uses *value-date accounting*... The booking date is when the event (like a payment) took place, and the value date is when the actual balance is credited or debited to a balance account" [VERIFIED: https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report.md, n.d., accessed 2026-11].

### 2.7 Pre-funding: who pays out before the network settles, and who carries the risk

**Adyen documents it explicitly.**

- Under Sales day payout "Adyen will (in deviation of the Settlement arrangements included in the Agreement) initiate payout of the Net Captured Volume to Merchant on the Payout Day, irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner" [VERIFIED: https://www.adyen.com/legal/sales-day-payout-terms-of-service, last update 2024-06-17].
- The advance is time-limited and reversible: "Prefinancing is capped at 30 days. If the card scheme, payment method, or acquirer does not settle the funds within 30 days, Adyen reverses the prefinanced amount from your payable batch. These reversals appear as **SettledReversed** and **RefundNotCleared** entries" [VERIFIED: https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp.md, n.d., accessed 2026-11]. "If Adyen receives the funds after 30 days, you see an additional Settled booking" [VERIFIED: same].
- "If Adyen cannot capture the funds for a sales transaction that we already paid out, we subtract those funds from the current payable batch" [VERIFIED: https://docs.adyen.com/account/sales-day-payout.md, n.d., accessed 2026-11].
- The `SETTLED_REVERSED` and `REFUND_NOT_CLEARED` webhook event types "apply to all payment methods and are disabled by default" [VERIFIED: same].
- Adyen protects itself by eligibility and by contract: "If more than 25% of the Captured Volume on a sub-account consists of Payment Methods that structurally settle to Adyen later than the Payout Day, Adyen will have the right to accordingly delay the Payout Day", and activation is "subject to regional availability and Adyen’s ongoing review and approval"; the merchant "commits to provide Adyen with insight into its financial standing" [VERIFIED: https://www.adyen.com/legal/sales-day-payout-terms-of-service, last update 2024-06-17].
- Reading: Adyen carries the timing risk (it pays before it is paid) for up to 30 days; the merchant carries the outcome risk (an unsettled amount is taken back by set-off) [ASSUMPTION/JUDGEMENT].

**Stripe documents one explicit case: Instant Payouts.**

- "Funds acquired from card payments are available for Instant Payouts as soon as the charge is complete. ACH or bank debits are only available for Instant Payouts after the payment has settled." "Card payment funds are available immediately, including pending funds within your payout schedule window" [VERIFIED: https://docs.stripe.com/payouts/instant-payouts.md, n.d., accessed 2026-11].
- On platforms the loss falls on whoever is liable for the account: "When platforms and marketplaces are liable for losses, you’re liable for uncovered negative balances due to refunds or disputes on instantly paid out funds" [VERIFIED: https://docs.stripe.com/connect/instant-payouts.md, n.d., accessed 2026-11].
- For standard payouts Stripe documents a fixed availability schedule (2.2) but publishes nothing on whether its own receipt of network funds precedes availability, and uses no term such as "pre-financing". Nothing public found; searched the balances, payouts and Connect balance pages [ASSUMPTION/JUDGEMENT on absence].

### 2.8 Stripe vs Adyen: balances and funds flows

| Aspect | Stripe (docs, accessed 2026-11) | Adyen (docs and terms, accessed 2026-11) | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Unit of money owed to the merchant | A balance per account, product and currency; one balance transaction per change | A payable batch per merchant account; on platforms, balance accounts | Stripe's model is account-like; Adyen's classic model is batch-like, its platform model account-like |
| When funds become payable | Per transaction, at `available_on`, by a country and method schedule | Per sales day, after a payout delay computed as a break-even of settlement times | Stripe ages each transaction; Adyen ages a day |
| Tie to network settlement | Not stated | Stated: sales day payout is independent of scheme settlement; pass-through follows it | Only Adyen documents pre-financing for standard payouts |
| Fees | Netted per transaction (`fee`, `net`); some fees debited daily or monthly | Netted in the batch, plus a monthly invoice trued up against the next batch | Adyen's merchant needs an invoice reconciliation; Stripe's sees fees on each transaction |
| Provider-imposed hold | Reserve (fixed or rolling) | Deposit (recalculated daily) | Same function, opposite names |
| Merchant-set buffer | Minimum balance | Reserve | — |
| Negative balance | Debit of the bank account as a negative payout; platform reserve and 180-day collection transfer | Carried to the next payout day or set off | Stripe pulls; Adyen's documented default is to net forward |

**For readers new to payments.**

- **Settlement** (to the merchant): the moment the provider treats funds from a payment as the merchant's to withdraw; it is a different event from the card network settling with the provider.
- **Pending and available funds**: pending is money the merchant is expected to get but cannot use yet; available is money it can pay out, refund from or transfer.
- **Reserve** (or deposit): money that belongs to the merchant but that the provider holds back to cover refunds and chargebacks that may arrive later.
- **Pre-funding** (pre-financing): the provider pays the merchant before the provider itself has been paid by the network, using its own liquidity and taking the money back if it never arrives.

**Architecture implications** [ASSUMPTION/JUDGEMENT].

- "Available balance" is a risk decision expressed as a timestamp. It needs its own state on each ledger entry (`available_on`, value date), separate from the booking time.
- Pre-financing requires the provider to track, per transaction, both what it paid the merchant and what it has received from the network, and to age the difference (Adyen's 30-day cap). That is a clearing account per scheme with an aging rule.
- Adjustments arrive unrelated to the original day or payout, so payouts cannot be recomputed from "that day's sales"; they must be built from whatever entries are open when the batch closes.
- A platform integrating both providers must map one vocabulary to the other, and "reserve" cannot be mapped by name.

---

## PART 3: Payouts and money movement (chapter 14)

### 3.1 Stripe: payout schedules, speed, failures

- "Stripe sends funds from your available balance to your bank account as payouts." First payout: "Stripe typically schedules your initial payout to complete within 7–14 days" after the first live payment [VERIFIED: https://docs.stripe.com/payouts.md, n.d., accessed 2026-11].
- Schedules: manual, daily ("every business day"), weekly or monthly on chosen days. "Choosing a payout schedule doesn’t change how long it takes for your pending balance to become available. It only controls when payouts are sent." "All payments and payouts are processed according to UTC time, except for Asia-Pacific (APAC) markets" [VERIFIED: same].
- Country limits: "Brazil and India: Payouts are always automatic and daily. Japan: Daily payouts aren’t available" [VERIFIED: same].
- ⚠ Manual payouts "typically take 1–4 business days"; same-day manual payouts exist in the US (before 5 pm US/Eastern), for GBP (before 5 pm Europe/London) and for EUR (before 4 pm Europe/Copenhagen), each limited to "10 same-day manual payouts per day with a maximum of 1 million" in the currency [VERIFIED: same].
- "Stripe doesn’t charge you a fee to initiate normal payouts" [VERIFIED: same].
- **Sent is not arrived.** "If your bank account can’t receive a payout for any reason, your bank returns the funds to us... It can take up to 5 additional business days for your bank to return the payout and inform us that it failed." "When a payout fails, the status might initially show as `paid`, but then change to `failed` within 5 business days." After the details are fixed, "Stripe then reattempts the payout at the next scheduled payout interval" [VERIFIED: same].
- Misdirected funds are the merchant's loss: "If you provide incorrect information, such as a mistyped account number or an incorrect routing number, Stripe might send payouts to the wrong bank account and might not be able to recover the funds" [VERIFIED: same].
- Minimum payout: "The minimum payout amount depends on the lowest amount we can support with our banking partners" [VERIFIED: same].
- The documentation does not name the rail used for a standard payout in each country [ASSUMPTION/JUDGEMENT on absence; the Global Payouts pages do name rails, see 3.3].

### 3.2 Stripe: Instant Payouts

- "You can request an Instant Payout any day or time, including weekends and holidays, and funds typically settle in the associated payout account within 30 minutes" [VERIFIED: https://docs.stripe.com/payouts/instant-payouts.md, n.d., accessed 2026-11].
- ⚠ Available for accounts in 36 listed countries, including the US, UK, Canada, Australia, Singapore and most EU countries [VERIFIED: same].
- ⚠ Limits: "a maximum of 10 Instant Payouts per day"; a daily volume limit per account; per-payout amounts of 0.50–9,999 USD in the US, 0.40–9,999 EUR in the euro area and 0.40–9,999 GBP in the UK. "New Stripe users aren’t immediately eligible" [VERIFIED: same].
- Destination: debit card, and "some bank accounts" in the US, UK, euro area, Sweden, Denmark, Australia and Singapore; debit card only in Canada and several others [VERIFIED: same].
- Fee: "Stripe assesses a fee on each Instant Payout", and "The Instant Payout fee is pre-deducted so the balance shown reflects what you’d actually receive" [VERIFIED: same]. ⚠ The Connect pricing page, as served to a Netherlands visitor, lists Instant Payouts at 1% of payout volume [VERIFIED: https://stripe.com/connect/pricing, n.d., accessed 2026-11, Dutch-language rendering]. The US rate was not verified.
- Reconciliation consequence: "You control the timing and amount of instant payouts, so Stripe can’t identify which transactions are included in each payout. You’re responsible for reconciling instant payouts against your transaction history" [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation.md, n.d., accessed 2026-11].
- "Instant Payouts can’t use multi-currency settlement" [VERIFIED: https://docs.stripe.com/payouts/instant-payouts.md, n.d., accessed 2026-11].

### 3.3 Stripe: Global Payouts and Connect cross-border payouts

**Global Payouts** ⚠ (availability and API are changing; several endpoints are at a preview API version).

- "Use Global Payouts to send payouts to customers, affiliates, sellers, or any third party. Send payouts to bank accounts through local bank networks, Fedwire, or SWIFT, or send payouts to debit cards or crypto wallets." Headline: "Send payouts to more than 160 markets" [VERIFIED: https://docs.stripe.com/global-payouts.md, n.d., accessed 2026-11].
- Who can send: "Businesses located in the following countries can use Global Payouts to send payouts: GB, US." Private preview for businesses in AT, AU, BE, BG, CY, DE, EE, ES, FI, FR, GR, HR, IE, IT, LT, LU, LV, MT, NL, PT, SI, SK [VERIFIED: same].
- Funding: "Global Payouts requires Treasury"; the sender funds a financial account and pays from it [VERIFIED: same]. Treasury itself is available in the United States and United Kingdom, with Australia in private preview [VERIFIED: https://docs.stripe.com/treasury.md, n.d., accessed 2026-11].
- Positioning and licences: "Global Payouts is best for businesses that already hold the licenses required to move money themselves and want a payouts-only solution decoupled from payments." In the comparison table: "If you manage your customers’ funds, you might need a license such as an MTL", whereas Connect payouts are "Covered by Stripe’s licensing" and "your platform isn’t part of the payout funds flow" [VERIFIED: https://docs.stripe.com/global-payouts.md and https://docs.stripe.com/connect/cross-border-payouts-to-recipients/compare-global-payouts.md, n.d., accessed 2026-11].
- Ledgering falls to the sender: "Payouts don’t flow through a Stripe balance belonging to the recipient, so you’re responsible for any desired tracking of recipient funds" [VERIFIED: same comparison page].
- Networks selectable through the API: US domestic `ach`, `fedwire`; UK domestic `fps`; Eurozone domestic `sepa`; cross-border `ach`, `fps`, `sepa`, `swift` [VERIFIED: https://docs.stripe.com/global-payouts/send-money.md, n.d., accessed 2026-11].
- ⚠ Per-payout fees for cross-border payouts on local rails: US "ACH next day 0.50 USD", "ACH same day 1.00 USD", "RTP 2.50 USD", "Fedwire 25.00 USD"; Eurozone SEPA Credit Transfer and SEPA Instant Credit Transfer 0.50 EUR each; UK Faster Payments 0.50 GBP; other countries local rail 2.50 EUR; SWIFT 20.00 EUR. FX fee 0.50% for 20 major currencies and 1.00% for "All 135 other currencies"; a platform fee applies above 1M EUR a month [VERIFIED: https://docs.stripe.com/global-payouts/pricing.md, n.d., accessed 2026-11].
- Statuses and the sent/arrived gap: an OutboundPayment is `processing`, `failed`, `canceled`, `posted` or `returned`. "A posted status doesn’t guarantee that your recipient has received money, because their bank might delay the release of funds." `returned`: "The payout failed to arrive at the destination. Stripe returns the funds to you in a separate transaction... Payouts are typically returned within 2–3 business days, but might take longer depending on the recipient country" [VERIFIED: https://docs.stripe.com/global-payouts/manage-payouts.md, n.d., accessed 2026-11].
- No automatic retry: "Stripe doesn’t retry or reroute payouts automatically." A failed or returned payout moves the PayoutIntent to `requires_action` [VERIFIED: https://docs.stripe.com/global-payouts/send-money.md, n.d., accessed 2026-11].
- Reversal: "You can only cancel a payout while it’s in progress. Only certain payout types support payout reversals, and reversals aren’t guaranteed. To request reversing an eligible completed payout, you must contact Stripe support within 24 hours" [VERIFIED: comparison page as above].

**Connect cross-border payouts.**

- "Platforms based in the US, UK, EEA, Canada, or Switzerland can transfer funds to connected accounts in any of those regions, regardless of the payment settlement currency." "Stripe doesn’t support self-serve cross-border payouts to countries outside the listed regions" [VERIFIED: https://docs.stripe.com/connect/cross-border-payouts.md, n.d., accessed 2026-11].
- Supported funds flows: separate charges and transfers without `on_behalf_of`, top-ups and transfers, destination charges without `on_behalf_of`. Accounts under a recipient service agreement are excluded and pointed to Global Payouts [VERIFIED: same].
- The payouts page still lists many countries (for example Albania, Algeria, Bangladesh) as "only available for Connect cross-border payouts accounts" [VERIFIED: https://docs.stripe.com/payouts.md, n.d., accessed 2026-11]. The two statements describe different programmes (self-serve regional transfers versus payouts to recipient-agreement accounts); writers should not merge them [ASSUMPTION/JUDGEMENT].

### 3.4 Adyen: merchant payouts, the Transfers API and the payout lifecycle

**Merchant payouts (classic accounts).** Timing after batch close: "it can take one to two business days for the payout to be initiated. Depending on the currencies and banks involved, your bank may need up to three more business days to post the funds." If nothing has arrived "five business days after the payable batch closed", the merchant filters the Aggregate settlement details report "on the journal type **BankInstructionReturned**. This journal type shows when the payout was not processed successfully, or when your bank returned the payout" [VERIFIED: https://docs.adyen.com/account/getting-paid.md, n.d., accessed 2026-11].

**Payouts service (balance platform).**

- "Adyen offers a payouts service in combination with processing online or in-person payments. However, the payout may or may not be directly related to an acquired payment. The payout may also be completely standalone to a third-party beneficiary." Funding: "Use funds acquired through payments with Adyen or externally transferred funds" [VERIFIED: https://docs.adyen.com/payouts/payout-service.md, n.d., accessed 2026-11].
- Payouts to bank accounts go "from your balance account to third-party bank accounts by using the Transfers API". "Adyen only supports paying out to third parties in local currencies", with two exceptions (EUR in non-euro SEPA countries; USD in Canada), plus a `crossBorder` priority in EUR, GBP and USD [VERIFIED: https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts.md, n.d., accessed 2026-11].
- **Priority instead of rail.** The caller chooses `regular`, `instant`, `fast`, `wire` or `crossBorder`; "A payout with a higher priority incurs higher fees." Instant "Transfers funds instantly within the United States, Australia, the United Kingdom, and the Single Euro Payments Area (SEPA)." Cross-border: "payout delays and additional fees may occur due to intermediary banks. As a result, the beneficiary may receive a lower amount than the instructed value" [VERIFIED: same].
- **Routes.** "To pay out your funds, Adyen must connect to transfer routes. Transfer routes depend on the parameters that you include in your transfer requests, such as priority, currency, and counterparty's location." A route calculation endpoint exists [VERIFIED: same].
- ⚠ **Cut-offs.** "There are specific times during a business day, called cut-off times, when Adyen stops processing bank transfers for settlement within the settlement delay." Examples: SEPA wire 16:30 CET; US regular 01:45 ET, fast 16:15 ET, wire 18:30 ET, instant "24/7" with a 1,000,000 USD maximum; UK regular 19:30 GMT with settlement delay "T+3", fast 21:00 GMT, wire 15:15 GMT [VERIFIED: same]. No per-priority prices are published on the page.
- **Lifecycle: accounting events, then tracking events.** Received → authorised ("we reserve the payout amount on your balance account") → booked ("Adyen deducts the funds from your balance account and creates a transaction"), each with a `balancePlatform.transfer.*` webhook. After `booked`, tracking: instant bank transfers get "**credited** `status` when the funds arrive, or **failed**"; card payouts get **accepted**; non-instant transfers get `tracking.estimatedArrivalTime` [VERIFIED: https://docs.adyen.com/payouts/payout-service/payout-lifecycle.md, last modified 2026-11-17].
- **Review after booking.** "After a payout reaches the **booked** `status`, but before the funds leave Adyen, the payout is automatically analyzed to ensure it complies with Adyen's policies. If the payout is flagged, Adyen must manually review it." If it fails review, "Adyen freezes the funds and does not pay them out externally... In some cases, this may involve the regulator" [VERIFIED: same].
- **Returns.** "Payouts that do not have an **instant** `priority` cannot fail, but they can be returned by the counterparty's bank." On return "A new transaction is created for the return", with a `returned` status webhook carrying a reason code and a transaction webhook crediting the balance account [VERIFIED: same].
- An optional approval flow lets a team member approve or cancel; unapproved payouts are cancelled after 30 days with reason `approvalExpired` [VERIFIED: same].
- **Card payouts.** To Mastercard or Visa cards in the EEA, UK and US; "Funds typically become available to the cardholder within 30 minutes" [VERIFIED: https://docs.adyen.com/payouts/payout-service/pay-out-to-cards.md, n.d., accessed 2026-11].

### 3.5 Adyen: "Intelligent Money Movement" (April 2026)

- Announced 9 April 2026 as "a new product offering that connects payments, liquidity management, and payouts together on a single platform. Designed for large global enterprises", naming Etsy, Expedia Group and Vinted [VERIFIED: https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement, published 2026-04-09].
- The two capabilities Adyen says power it: "One Unified Platform: Unlike many providers that rely on a patchwork of acquired technologies and third-party integrations, Adyen has built its entire financial technology stack on a single platform" and "Global Banking Licenses: Adyen is one of the select fintech companies that holds its own banking licenses across the U.S., the U.K., and Europe. This infrastructure enables direct connections to payment rails and card schemes, reducing intermediaries and fund settlement times" [VERIFIED: same].
- Context figures in the release (from a joint Adyen and Boston Consulting Group treasury report, not fetched): "The average enterprise works with five to six primary banks, manages over 40 separate bank accounts, and has 12 pay-in and payout providers"; "48% of CFOs cite transparency and accurate liquidity projection as a top challenge" [VERIFIED as quoted in the release: same].
- ⚠ The product page groups existing capabilities under the name: unified payments, "Enterprise Accounts", "Enterprise Funding" ("Use incoming payments to directly fund outgoing payouts"), card issuing and payouts "to 190+ countries" [VERIFIED: https://www.adyen.com/intelligent-money-movement, n.d., accessed 2026-11]. The "190+ countries" figure is marketing; the documentation's list of local-currency payout countries is far shorter, with the rest reached by the cross-border priority [ASSUMPTION/JUDGEMENT].
- Adyen's H1 2026 release lists the launch among the half-year's milestones and adds: "Secured direct access to France's domestic interbank clearing system" [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13].
- No engineering description of Intelligent Money Movement was found [ASSUMPTION/JUDGEMENT on absence].

### 3.6 Checking the beneficiary: Verification of Payee (EU) and Confirmation of Payee (UK)

**The EU rule.** Regulation (EU) 2024/886 of 13 March 2024 (the Instant Payments Regulation) inserts Article 5c into the SEPA Regulation: "A payer’s PSP shall offer the payer a service ensuring verification of the payee to whom the payer intends to send a credit transfer... immediately after the payer provides relevant information about the payee and before the payer is offered the possibility of authorising that credit transfer." Where name and account identifier "almost match, the payer’s PSP shall indicate to the payer the name of the payee associated with the payment account identifier". The service is "free of charge". "PSPs located in a Member State whose currency is the euro shall comply with this Article by 9 October 2025. PSPs located in a Member State whose currency is not the euro shall comply with this Article by 9 July 2027" [VERIFIED: http://publications.europa.eu/resource/celex/32024R0886, published 2024-03-19].

- The same regulation requires euro-area PSPs to offer receiving instant credit transfers in euro "by 9 January 2025" and sending "by 9 October 2025"; non-euro Member States by 9 January 2027 and 9 July 2027; and charges for instant transfers "shall not be higher than the charges levied by that PSP in respect of sending and receiving other credit transfers of corresponding type" [VERIFIED: same].
- The European Payments Council runs the scheme PSPs use to exchange these checks; its page could not be fetched [ASSUMPTION/JUDGEMENT].

**The UK service.** "Since launching in 2020, over 300 organisations have already implemented CoP, with more than 2m checks being completed every day." "CoP is an API-based peer-to-peer service, with no central infrastructure in place, but with a directory identifying the organisations in the ecosystem." The page refers to "the Payment System Regulator’s mandate for the expansion of CoP in 2024" [VERIFIED: https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/, n.d., accessed 2026-11].

**What each provider documents.**

- Stripe, Global Payouts: "When you send a GBP payout from a UK financial account to a UK bank account, Confirmation of Payee (CoP) requires you to check that the recipient’s legal name and business type match the details their bank has on file." Results: match, close match, no match, unavailable; the sender may "Continue without match", and "Funds sent to the wrong bank account might not be recoverable." The result is reused: "You complete CoP once for each recipient and bank account" [VERIFIED: https://docs.stripe.com/global-payouts/send-money.md, n.d., accessed 2026-11].
- Stripe, EU: "Verification of Payee (VoP) regulation launched in October 2025"; "When initiating a payout to an EU recipient in the Dashboard, Stripe will perform the VoP check"; on a mismatch "you will be prompted to acknowledge the difference and either edit the details or cancel the payout" [VERIFIED via summarising fetch: https://support.stripe.com/questions/verification-of-payee-support-for-treasury, n.d., accessed 2026-11].
- Stripe publishes nothing found on a payee check for standard payouts to a merchant's own bank account [ASSUMPTION/JUDGEMENT on absence].
- Adyen: "Adyen's verification of counterparty name service allows enterprise bank account holders to check the intended recipient before making a payment to domestic bank accounts registered in the EU or UK regions." The platform calls `POST /verifyCounterpartyName`; responses include `nameMatch`, `partialNameMatch`, `noNameMatch`, `nameMatchNotSupported`. "If the `response` is a partial name match, Adyen returns the name on the account in the response. To safeguard against name-guessing, for all other `response` values, Adyen does not return a name" [VERIFIED: https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/verify-counterparty.md, n.d., accessed 2026-11].

### 3.7 Stripe vs Adyen: payouts

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Payout of own sales | From the available balance on a schedule; no fee | From a payable batch per merchant account; net | Same function |
| Standalone payouts to third parties | Global Payouts: senders in US and GB, 22 more countries in private preview; requires a Treasury financial account | Payouts service on the balance platform through the Transfers API; funded by acquired or transferred funds | Stripe's product is newer and narrower in sender coverage; both fund from a stored balance |
| How the sender picks speed | Names a network (`ach`, `fedwire`, `fps`, `sepa`, `swift`) or lets Stripe choose | Names a priority (`regular`, `fast`, `instant`, `wire`, `crossBorder`); Adyen maps it to a route | Stripe exposes the rail; Adyen abstracts it |
| Published prices | Per-rail fees on a docs page | "higher priority incurs higher fees"; no public table | — |
| Instant | Instant Payouts to cards and some banks, about 30 minutes, capped at 9,999 per payout, 10 a day | `instant` priority in SEPA, UK, US, Australia; US maximum 1,000,000 USD | Stripe's instant product is sized for small merchants; Adyen's for platform and enterprise transfers |
| Status after sending | `posted`, later possibly `returned`; payout `paid` may become `failed` within 5 business days | `booked`, then tracking `credited` (instant) or an estimated arrival time; later possibly `returned` | Both model "sent" and "arrived" as different states; Adyen confirms arrival for instant transfers |
| Payee check | CoP in the UK and VoP in the EU on Global Payouts | Counterparty name verification endpoint for EU and UK | Both expose the result to the sender and let the sender decide |
| Licence statement | Sender "might need a license such as an MTL" for Global Payouts | Press release ties payouts to Adyen's own banking licences | PART 5 |

**For readers new to payments.**

- **Payout**: the provider sending money from the merchant's balance with the provider to the merchant's own bank account or to a third party.
- **Payment rail**: the bank network a transfer travels on (SEPA Credit Transfer, SEPA Instant, ACH, Faster Payments, Fedwire, SWIFT, a card network's push-to-card service); each has its own speed, cost, limits, opening hours and rules for returns.
- **Cut-off time**: the time of day after which a transfer misses that day's processing cycle on a rail and goes with the next one.
- **Payout return**: the receiving bank sends the money back after the transfer was accepted, for example because the account is closed; it arrives as a new transaction days later.

**Architecture implications** [ASSUMPTION/JUDGEMENT].

- A payout is at least two state machines: the provider's accounting (reserve, debit) and the rail's delivery (sent, credited, returned). Integrations that treat "debited" as "delivered" are wrong on both providers.
- A return is a new credit, not an undo; ledgers must link it to the original payout and re-open the liability to the payee.
- Batch rails make payout a scheduling problem (cut-offs, holidays, time zones); instant rails make it a synchronous call with a definite answer and a limit. One API has to cover both.
- The payee check moves an error from "money gone" to "warning before sending", and the liability moves with the sender's decision to continue.

---

## PART 4: Reconciliation and reporting, provider side (chapter 15)

Customer-side reconciliation is covered in RECONCILED; this part is limited to what each provider has said about proving its own books and to the timing of the reports it exposes.

### 4.1 What each has published about its own reconciliation

**Stripe.**

- The Ledger post is Stripe's account of internal reconciliation: fund flows that include "moving funds between banks, reconciling money movement with third-party reporting, and matching regulatory reporting with financial reporting", checked by clearing, timeliness and completeness (1.1). Inputs it must absorb include "malformed reports or propagated errors from banking or network partners" [VERIFIED: https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement, published 2024-02-16].
- Exceptions are aged and owned: the "Aging Balances" score, auto-generated tickets, and reassignment when "the root cause is related to an infrastructure or third-party incident outside their control" [VERIFIED: same].
- For pooled bank accounts Stripe states the control in one sentence: in an FBO-backed account "Stripe records how much of the total balance belongs to your business and reconciles that record against the funds held at the bank" [VERIFIED: https://docs.stripe.com/treasury.md, n.d., accessed 2026-11].
- The balance transaction type `payment_unreconciled` exists in the public enum; its meaning is not explained on the object page [VERIFIED for existence: https://docs.stripe.com/api/balance_transactions/object.md, n.d., accessed 2026-11].
- Nothing found on file formats, matching rules or volumes for Stripe's reconciliation against card-network clearing files or bank statements. Searched: web search for Stripe engineering posts and talks on reconciliation, which returned only customer-facing product pages [ASSUMPTION/JUDGEMENT on absence].

**Adyen.**

- Partner reports are matched to accounting records: "if we received reports on processed transactions from our partners, we needed to match them to transactions in different clusters. Instead of parsing a file and matching it directly to the transactions, we introduced a two-step framework that would first parse a file and then split it into the relevant parts for each cluster. The second step was to match the relevant transactions within the clusters." "the reconciliation needs to happen for a lot of different very custom integrations so this was a real team effort" [VERIFIED: https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2, published 2021-08-23] **(evidence age: 5 years)**.
- The merchant-visible result of that matching is the record type "Settled: Payment has been settled, and the funds have been received by Adyen", as distinct from "SentForSettle: Request to transfer the payment sent to the financial institution" [VERIFIED: https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report.md, n.d., accessed 2026-11].
- The 30-day rule (2.7) is a published exception-aging policy: an amount not received from a scheme within 30 days is reversed [VERIFIED: https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp.md, n.d., accessed 2026-11].
- Nothing found on Adyen's reconciliation against bank statements or on its exception tooling [ASSUMPTION/JUDGEMENT on absence].

### 4.2 Reports each exposes and their timing

**Stripe.**

- **Payout reconciliation report**: "helps you match the payouts you receive in your bank account with the batches of payments and other transactions that they relate to"; available only with automatic payouts. **Balance summary report**: "works like a bank statement"; "doesn’t associate payouts with payment transactions" [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation.md and https://docs.stripe.com/reports/balance.md, n.d., accessed 2026-11].
- **Timing.** Both: "Within 12 hours". "Stripe computes all your data on a daily basis beginning at 12:00 am... A day’s report is normally available by 12:00 pm on the following day." "SLAs indicate when the reports are available for download. Webhook notifications might take additional time." The 12-hour figure does not apply to first automatic payouts after manual, or after a gap of more than 180 days [VERIFIED: https://docs.stripe.com/reports/options.md, n.d., accessed 2026-11].
- "Report data follows a separate processing schedule, so a payout might arrive before its reconciliation data is ready" [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation.md, n.d., accessed 2026-11].
- **Sigma**: "an interactive SQL environment in the Stripe Dashboard"; "All data is read-only". Freshness: "Sigma makes most of your Stripe transaction data available to query within three hours" [VERIFIED: https://docs.stripe.com/stripe-data/how-sigma-works.md and https://docs.stripe.com/stripe-data/available-data.md, n.d., accessed 2026-11].
- **Data Pipeline**: sends Stripe data to Snowflake, Amazon Redshift, Databricks, BigQuery, or as Parquet files to cloud storage; "delivering a full load of data every 3 hours". Freshness is stated as percentiles (P50, P90, maximum delay) per dataset, and "Data delivery varies from customer to customer and is largely determined by the data sizes." Not offered in India "due to data localization requirements" [VERIFIED: https://docs.stripe.com/stripe-data/access-data-in-warehouse.md and https://docs.stripe.com/data/data-pipeline/data-freshness.md, n.d., accessed 2026-11].
- **Bank reconciliation** (matching payouts to deposits in a linked bank account) is "currently only available for users with direct US-based Stripe accounts using an automated payout schedule" [VERIFIED: https://docs.stripe.com/bank-reconciliation.md, n.d., accessed 2026-11]. ⚠

**Adyen.**

- **Settlement details report**: "includes the details of payments that have been settled and paid out to you by Adyen"; created "When the payable batch closes" [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report.md and https://docs.adyen.com/account/getting-paid.md, n.d., accessed 2026-11].
- **Aggregate settlement details report**: batch-level credits, debits and counts per merchant account, store, terminal, payment method, journal type and creation date [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report.md, n.d., accessed 2026-11].
- **Payment accounting report**: one row per lifecycle status (Received, Authorised, SentForSettle, Settled...), used with the monthly invoice; "Your invoice is always based on the CET time zone" [VERIFIED: https://docs.adyen.com/reporting/invoice-reconciliation.md and https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice.md, n.d., accessed 2026-11].
- **Balance Platform accounting report**: "a daily report that tracks all balance changes on all balance accounts in your balance platform", covering bookings "between opening (00:00 AM) and closing (00:00 AM the next day) for your selected day in Central European Time (CET)" [VERIFIED: https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report.md, n.d., accessed 2026-11].
- Timing is tied to events, not to a stated number of hours: batch close is two hours after the sales day closes, and report generation starts then (2.4). No published completion-time commitment was found for any Adyen report [ASSUMPTION/JUDGEMENT on absence; the sibling brief's "before 10:00" claim for the aggregate report was not found on the page in this session].

### 4.3 Stripe vs Adyen: reconciliation and reporting

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| Own reconciliation, published | Ledger post (2024): clearing accounts, DQ metrics, aging, tooling | Design to Duty (2021): two-step matching of partner files across accounting clusters | Stripe describes the control system; Adyen describes the matching mechanics |
| Unit of the settlement report | The payout | The payable batch (a sales day under Sales day payout) | Adyen's default report matches a day of sales; Stripe's matches a bank credit |
| Timing statement | "Within 12 hours" after the day ends, with exceptions | Generated when the batch closes; no stated duration | Only Stripe publishes a number |
| Data products | Sigma (SQL, about 3 hours), Data Pipeline (warehouse, 3-hour cadence) | Reports by file and webhook; no SQL or warehouse product found in this session | Stripe sells access to the data; Adyen delivers files |
| Report versus event | "a payout might arrive before its reconciliation data is ready" | Reversal webhooks for pre-financed amounts are off by default | Both treat reports as the complete record and webhooks as notification |

**For readers new to payments.**

- **Reconciliation**: proving that two independent records of the same money (for example the provider's ledger and the bank's statement) agree, and explaining every difference.
- **Clearing file**: the file a card network or acquirer sends, usually daily, listing each transaction it has processed and the amounts it will settle.
- **Exception aging**: tracking how long each unmatched item has been open, because the older an unexplained amount is, the more likely it is a loss.

**Architecture implications** [ASSUMPTION/JUDGEMENT].

- Provider-side reconciliation is three-way: the provider's ledger, the network's files and the banks' statements. The Ledger's clearing accounts are the place where "we expect money from Visa" waits until a file and a bank credit clear it.
- Reports are computed on a schedule from the ledger; webhooks are emitted by product systems as events happen. They can disagree for hours, and the report is the one to book from.
- A published timing number (12 hours, 3 hours) is a contract a customer can build a close process on; an event-tied one requires the customer to wait for a "report available" notification.

---

## PART 5: Licences and safeguarding (chapter 16)

### 5.1 The EU regime

Under PSD2 a **payment institution** is a non-bank authorised to provide payment services. ⚠ PSD2 is being replaced (see below), so article numbers will change. Its funds are not deposits: "Any funds received by payment institutions from payment service users with a view to the provision of payment services shall not constitute a deposit or other repayable funds... or electronic money", and "they may hold only payment accounts which are used exclusively for payment transactions" (Article 18). Initial capital is modest: "not less than EUR 125 000" for the main payment services, EUR 50 000 for payment initiation, EUR 20 000 for money remittance only (Article 7). Because customers are not depositors, Article 10 requires the institution to **safeguard** "all funds which have been received from the payment service users or through another payment service provider for the execution of payment transactions" in one of two ways: (a) "funds shall not be commingled at any time with the funds of any natural or legal person other than payment service users on whose behalf the funds are held and, where they are still held by the payment institution and not yet delivered to the payee or transferred to another payment service provider by the end of the business day following the day when the funds have been received, they shall be deposited in a separate account in a credit institution or invested in secure, liquid low-risk assets... and they shall be insulated... against the claims of other creditors of the payment institution, in particular in the event of insolvency"; or (b) "funds shall be covered by an insurance policy or some other comparable guarantee from an insurance company or a credit institution, which does not belong to the same group" [VERIFIED: http://publications.europa.eu/resource/celex/32015L2366, published 2015-12-23] **(evidence age: 11 years; in force, replacement agreed)**.

An **electronic money institution** may in addition issue e-money, a stored balance redeemable at par, and must safeguard "funds that have been received in exchange for electronic money that has been issued"; funds received by payment instrument "need not be safeguarded until they are credited to the electronic money institution’s payment account", and "In any event, such funds shall be safeguarded by no later than five business days... after the issuance of electronic money" (Directive 2009/110/EC, Article 7) [VERIFIED: http://publications.europa.eu/resource/celex/32009L0110, published 2009-10-10] **(evidence age: 17 years; in force)**. A **credit institution** (a bank) takes deposits, may lend them, is subject to bank capital and liquidity rules and deposit-guarantee schemes, and is not subject to Article 10 safeguarding for its payment business; an authorisation in one Member State can be used across the EEA by passporting [ASSUMPTION/JUDGEMENT: standard description; the Capital Requirements texts were not fetched]. ⚠ **PSD3 and the Payment Services Regulation**: a provisional political agreement was reached on 27 November 2025 [WIDELY REPORTED: https://www.williamfry.com/knowledge/psr-psd3-eu-payment-services-legislation-is-agreed/, 2025, law-firm briefing]; later steps (final texts in April 2026, formal adoption and Official Journal publication pending as of mid-2026) were seen only in search summaries and must be checked before publication [ASSUMPTION/JUDGEMENT].

### 5.2 The UK regime

The UK kept the PSD2 and e-money structure after Brexit in the Payment Services Regulations 2017 and the Electronic Money Regulations 2011, with authorised payment institutions and e-money institutions supervised by the FCA and safeguarding by segregation or by insurance or guarantee [ASSUMPTION/JUDGEMENT: the UK regulations were not fetched; the structure is confirmed indirectly by the FCA policy statement below]. A UK e-money institution's customers are not protected by the deposit-guarantee scheme; Stripe says of its own UK entity: "As Stripe is an EMI, it isn't covered by the Financial Services Compensation Scheme" [VERIFIED via summarising fetch: https://support.stripe.com/questions/safeguarding-stripe-users-funds-in-the-uk, n.d., accessed 2026-11].

⚠ The FCA is changing safeguarding in two stages. Policy Statement PS25/12 (7 August 2025) sets "'Interim rules' (the Supplementary Regime) to encourage greater compliance with existing safeguarding requirements, support more consistent record keeping, and strengthen reporting and monitoring requirements" and describes "'End-state rules' (the Post-Repeal Regime) to replace the safeguarding requirements of the EMRs and PSRs with a 'CASS' style regime". "The Supplementary Regime... will come into force on 7 May 2026." It applies to authorised payment institutions (except those providing only payment initiation or account information services), authorised and small e-money institutions and credit unions that issue e-money [VERIFIED: https://www.fca.org.uk/publications/policy-statements/ps25-12-changes-safeguarding-regime-payments-and-e-money-firms, published 2025-08-07]. The rules sit in the FCA Handbook's client assets sourcebook: firms must comply with "CASS 10A, CASS 15, SUP 3A and SUP 16.14A"; the regime includes annual safeguarding audits by a qualified auditor, a monthly regulatory return, and an internal reconciliation that compares the "D+1 segregation requirement" (the funds that should be in safeguarding accounts) with the "D+1 segregation resource" (the balances of those accounts); "If the D+1 segregation resource is lower than the D+1 segregation requirement, a payments firm will be required to remedy the shortfall. If it is not possible to use relevant funds to do so, the firm must use its own funds" (the required frequency of that reconciliation was not checked in this session). The end-state proposal would hold relevant funds "on trust for consumers", but the FCA says it is "not proposing to implement the proposals without further consideration and consultation. Once a full audit period has been completed, after the Supplementary Regime has come into force, we will review its implementation" [VERIFIED: https://www.fca.org.uk/publication/policy/ps25-12.pdf, published 2025-08-07]. So in November 2026 CASS 15 is in force as the interim regime; the statutory-trust end state has no date [ASSUMPTION/JUDGEMENT: reading of the two FCA documents; confirm that the 7 May 2026 commencement happened as planned].

### 5.3 The United States: money transmission and bank partnerships

- There is no federal payments licence equivalent to the EU payment institution. A non-bank that receives money for transmission is licensed state by state as a money transmitter and registers federally as a money services business [ASSUMPTION/JUDGEMENT: standard description; FinCEN texts were not fetched].
- The states' model law: "The Money Transmission Modernization Act (MTMA) is a single set of nationwide standards, including net worth (capital), surety bond, and permissible investments (liquidity) requirements... To date, thirty-one states have enacted the law in full or in part", with "uneven adoption and interpretation" [VERIFIED: https://www.csbs.org/csbs-money-transmission-modernization-act-mtma, status as of 2026-09]. ⚠ "Permissible investments" is the US counterpart of safeguarding: the licensee must hold eligible assets at least equal to its outstanding transmission obligations [ASSUMPTION/JUDGEMENT].
- Card acquiring requires a network member. A non-bank processor in the US works as a payment facilitator of one or more sponsoring banks, and stored balances are typically held at a partner bank in an account "for the benefit of" (FBO) the customers [ASSUMPTION/JUDGEMENT; Stripe's own disclosures in 5.5 confirm both for Stripe].
- A newer route is a limited charter. Under Georgia's merchant acquirer limited purpose bank (MALPB) charter, "MALPBs are limited in their activity... prohibited from engaging in general banking activities, may not solicit or accept deposits from the general public, and may not sponsor ATMs or issue payment cards"; the charter allows "direct membership with Visa and Mastercard and to process payments without a sponsoring bank" [WIDELY REPORTED: https://www.icba.org/newsroom/news-and-articles/2025/07/08/georgia-approves-stripe-application-to-form-malpb, 2025, trade association news item].

### 5.4 Adyen: licences per region and what its bank status lets it do, per its own statements

- **EEA.** "Adyen N.V. is authorised as a credit Institution under the supervision of Dutch Central Bank (De Nederlandsche Bank) ('DNB'). This is commonly referred to as a 'banking license' and includes the ability to provide cross-border acquiring, payment and banking services in all EEA countries in accordance with the passporting rules under CRD IV." Switzerland is served "as non-regulated activities" [VERIFIED: https://www.adyen.com/licenses/emea, n.d., accessed 2026-11].
- **UK.** "Adyen N.V. is authorised as an overseas branch of an EEA credit institution in the UK with a Part 4A permission to provide acquiring, payment and financial services under the supervision of the Prudential Regulatory Authority ('PRA') and the Financial Conduct Authority ('FCA')" [VERIFIED: same]. It is a branch of the Dutch bank, not a separate UK bank [ASSUMPTION/JUDGEMENT: reading of the quoted sentence].
- **US.** "Adyen N.V. San Francisco Branch is a federal Branch of Adyen, N.V., licensed by the Office of the Comptroller of the Currency and the Federal Reserve Board of Governors" [VERIFIED: https://www.adyen.com/licenses/united-states, n.d., accessed 2026-11]. The 2021 announcement: the OCC approved "a Federal Foreign Branch in San Francisco", with the Federal Reserve's approval on 24 May 2021; it "allows Adyen to enhance its US activities and operations in line with those conducted in Europe under its European banking license (obtained in 2017)" [VERIFIED: https://www.adyen.com/press-and-media/adyen-granted-us-branch-license, published 2021-06-14] **(evidence age: 5 years; confirmed by the current licences page and the April 2026 release)**.
- **Other regions (not bank licences).** UAE: "Adyen MEA FZ-LLC... holding a Retail Payment Services Licence (Category II)" from the Central Bank of the UAE [VERIFIED: https://www.adyen.com/licenses/emea, n.d., accessed 2026-11]. Singapore: "licensed by the Monetary Authority of Singapore under the Payment Services Act as a Major Payments Institution for 3 regulated activities - merchant acquisition, domestic money transfers, and cross-border money transfers" [VERIFIED: https://www.adyen.com/licenses/singapore, n.d., accessed 2026-11]. The licences index also lists Australia, Canada, India, Malaysia, New Zealand, Hong Kong and Japan [VERIFIED: https://www.adyen.com/licenses, n.d., accessed 2026-11]; the Australian page shows Adyen Australia Pty Ltd reporting as a "RITS Member" (the Reserve Bank of Australia's settlement system) [VERIFIED: https://www.adyen.com/licenses/australia, n.d., accessed 2026-11].
- **What the licences let it do, in Adyen's words.** "Adyen is one of the select fintech companies that holds its own banking licenses across the U.S., the U.K., and Europe. This infrastructure enables direct connections to payment rails and card schemes, reducing intermediaries and fund settlement times" [VERIFIED: https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement, published 2026-04-09]. For platforms' users: "Submerchants in the US and EU can earn interest on deposited funds" [VERIFIED: https://www.adyen.com/accounts, n.d., accessed 2026-11].
- As a credit institution Adyen holds merchant funds as a bank's liabilities under bank prudential rules, not as safeguarded funds under PSD2 Article 10; the pre-financing of Sales day payout (2.7) is consistent with a bank using its own balance sheet [ASSUMPTION/JUDGEMENT: Adyen's pages do not put it this way, and the Annual Report was not read].
- **Not public or not verified here**: where Adyen holds the funds (central bank accounts, commercial banks), the split by currency, which rails it joins directly in each country beyond the French clearing system named in 2026, and the regulatory treatment of balance accounts for platform users in each region.

### 5.5 Stripe: legal entities, licences and partner banks

- **Contracting entities.** In the EEA the Services Agreement is with "Stripe Payments Europe, Limited", with "Stripe Technology Europe, Limited*" as an additional party for regulated services; for Gibraltar, Switzerland and the United Kingdom, "Stripe Payments Europe, Limited" and "Stripe Payments UK Ltd*" [VERIFIED: https://stripe.com/gb/legal/ssa, last modified 2026-09-28].
- **EEA licence.** "STEL is authorised as an electronic money institution by the Central Bank of Ireland (reference number: C187865) to issue electronic money, execute payment transactions, make money remittances, issue payment instruments and acquire payment transactions, and provide payment initiation services and account information services" [VERIFIED: https://stripe.com/stel/legal, last updated 2019-04-05] **(evidence age: 7.5 years; confirmed by the 2024 FAQ below and the current acquirer disclosure)**. "STEL passports its electronic money institution licence on a 'freedom of services' basis to all countries across the EEA" [VERIFIED: https://stripe.com/ie/guides/frequently-asked-questions-about-stripe-connect-and-psd2, last updated 2024-01-18].
- **UK licence.** "SPUKL is authorised as an electronic money institution by the U.K. Financial Conduct Authority (reference number: 900461) to issue electronic money, enable cash placement and cash withdrawal services on payment accounts, execute payment transactions, make money remittances, and acquire payment transactions" [VERIFIED: https://stripe.com/gb/legal/spukl, last updated 2017-01-26] **(evidence age: almost 10 years; the entity is still named in the 2026 Services Agreement and acquirer disclosure)**.
- **Safeguarding.** EU platforms: user funds "are settled to Stripe’s safeguarding accounts, before payout"; "only Stripe has control over the funds held in the Stripe-titled safeguarded bank account"; "the platform does not have possession of user’s funds at any point" [VERIFIED: same FAQ, last updated 2024-01-18]. UK: Stripe keeps user funds separate from its own and has "established dedicated safeguarding bank accounts with credit institutions" [VERIFIED via summarising fetch: https://support.stripe.com/questions/safeguarding-stripe-users-funds-in-the-uk, n.d., accessed 2026-11]. The banks are not named.
- **Acquiring.** ⚠ Stripe's acquirer disclosure: in the EEA "Payment Method Acquirer is Stripe Technology Europe, Ltd."; in the United Kingdom, Gibraltar and Switzerland "Payment Method Acquirer is Stripe Payments UK, Ltd."; in the United States "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers": Cross River Bank, Deutsche Bank Trust Company Americas, Fifth Third Bank, Pathward N.A., PNC Bank, N.A., and "Stripe MALPB, 505 N Angier Avenue NE, Atlanta, GA". In Canada Stripe is a payment facilitator of Peoples Trust Company and PNC Bank Canada; in the UAE an independent sales organisation of Network International [VERIFIED: https://stripe.com/en-us/legal/acquirer-disclosure, n.d., accessed 2026-11].
- **US money transmission.** Stripe Payments Company (NMLS #1280479) lists licences or authorities in 53 jurisdictions: 49 states (all except Montana), the District of Columbia, Guam, Puerto Rico and the US Virgin Islands [VERIFIED: https://stripe.com/legal/spc/licenses, n.d., accessed 2026-11; count made from the page's list].
- **Stored balances (Treasury).** "Stripe is not a bank." "In the US, a financial account is backed by either a demand deposit account (DDA) that’s opened directly with Stripe’s banking partner or a for-benefit-of (FBO) arrangement, where Stripe administers your funds on your behalf." In the FBO case "The bank’s records show that the account holds funds for the benefit of Stripe customers" and Stripe keeps the per-customer record. "Funds that are eligible for FDIC pass-through deposit insurance are held at Fifth Third Bank, N.A., Member FDIC"; "Checking accounts are provided exclusively by Fifth Third Bank, National Association" [VERIFIED: https://docs.stripe.com/treasury.md, n.d., accessed 2026-11]. ⚠
- **Issuing.** One US card programme's terms are between the customer and "Celtic Bank Corporation ('Issuing Bank')", with "Stripe, LLC ('Stripe')" as "the program manager appointed by Issuing Bank" [VERIFIED: https://stripe.com/legal/celtic-spend-card, n.d., accessed 2026-11]. Other issuing banks were not checked in this session.
- **The licence shows up in product rules.** Global Payouts tells senders they "might need a license such as an MTL", while Connect is "Covered by Stripe’s licensing" (3.3); fee credits are classed as "corporate funds" that need not "be safeguarded, swept to a bank account, or reconciled against a real cash position" (1.2).

### 5.6 Bank charter news, 2025–2026, with status

- ⚠ **Georgia MALPB (card acquiring).** Georgia approved Stripe's application for a merchant acquirer limited purpose bank charter [WIDELY REPORTED: https://www.icba.org/newsroom/news-and-articles/2025/07/08/georgia-approves-stripe-application-to-form-malpb, 2025, trade association news item]. Stripe's own acquirer disclosure now lists "Stripe MALPB" in Atlanta among its US payment method acquirers [VERIFIED: https://stripe.com/en-us/legal/acquirer-disclosure, n.d., accessed 2026-11]. The share of US volume it acquires is not public, and the Georgia regulator's own notice was not fetched. It is not a deposit-taking bank.
- ⚠ **Bridge National Trust Bank (stablecoin subsidiary).** The OCC's letter of 12 February 2026 to "Bridge Ventures LLC – a Stripe, Inc. company" states: "The OCC hereby grants preliminary conditional approval of your charter application" for "Bridge National Trust Bank, New York, New York (Proposed)", a national trust bank that "will engage in operations of a trust company and activities related thereto, including fiduciary activities". "The OCC has granted preliminary conditional approval only. Final approval and authorization... for the Bank to commence business will not be granted until all preopening requirements are met" [VERIFIED: https://www.occ.treas.gov/topics/charters-and-licensing/interpretations-and-actions/2026/cd1365.pdf, published 2026-02-12]. Reported by trade press on 18 February 2026 [WIDELY REPORTED: https://www.bankingdive.com/news/stripe-bridge-occ-conditional-approval-national-trust-bank-charter/812417/, 2026, trade press]. **Status at the research cut-off: conditional approval verified; final approval not verified.** A trust bank does not take insured retail deposits [ASSUMPTION/JUDGEMENT].
- Neither is a full banking licence, and "Stripe is not a bank" remains on Stripe's Treasury documentation (5.5). No application by Stripe for a full bank charter in any jurisdiction was found [ASSUMPTION/JUDGEMENT on absence].

### 5.7 Stripe vs Adyen: licences and safeguarding

| Aspect | Stripe | Adyen | What the difference suggests (inference) |
| --- | --- | --- | --- |
| EEA | E-money institution (Stripe Technology Europe, Central Bank of Ireland), passported | Credit institution (Adyen N.V., DNB), passported | Stripe must safeguard user funds at banks; Adyen is the bank |
| UK | E-money institution (Stripe Payments UK, FCA 900461); not covered by the FSCS | UK branch of the Dutch credit institution (PRA and FCA) | Same contrast; Stripe is subject to CASS 15, Adyen to bank supervision |
| US | State money transmitter licences (53 jurisdictions); payment facilitator of five sponsor banks plus its own Georgia limited-purpose acquiring bank; balances at Fifth Third | Federal branch of the Dutch bank (OCC, Federal Reserve) | Stripe assembles licences and partners per function; Adyen extends one bank |
| Where customer funds sit | Safeguarding accounts at unnamed credit institutions (EU, UK); partner bank DDA or FBO (US) | Not stated on the pages read | Stripe documents the structure; Adyen's is implied by its status |
| Pre-financing of payouts | Not documented for standard payouts | Documented, capped at 30 days | Consistent with balance-sheet capacity, but Adyen does not say so |
| Interest and accounts for users | Through partner banks; "Stripe is not a bank" | "Submerchants in the US and EU can earn interest on deposited funds" | Product reach follows the licence |
| Direction of travel 2025–2026 | Narrow charters: Georgia acquiring bank; conditional national trust bank for Bridge | More direct rail access (French clearing system, UAE licence) | Stripe is adding bank-like permissions function by function |

**For readers new to payments.**

- **Payment institution / e-money institution**: a licensed non-bank that may move customers' money (and, for e-money, keep it as a stored balance) but may not lend it or treat it as its own.
- **Safeguarding**: the legal duty of such an institution to keep customers' money separate from its own, in a dedicated bank account or secure assets, so that it can be returned if the institution fails.
- **Banking licence (credit institution)**: permission to take deposits and use them on the bank's own balance sheet, under much heavier capital and supervision rules; it also gives direct access to payment systems.
- **Partner bank / sponsor bank**: a licensed bank that provides the regulated part of a service (network membership, deposit accounts, card issuing) for a non-bank that runs the technology and the customer relationship.
- **FBO account**: one bank account held "for the benefit of" many customers, where the bank sees one balance and the non-bank's ledger records who owns how much.

**Architecture implications** [ASSUMPTION/JUDGEMENT].

- The licence decides which accounts exist in the ledger. An e-money institution needs a provable, regularly checked equality between "what we owe users" (ledger) and "what sits in safeguarding accounts" (bank), which is exactly Stripe's "reconciles that record against the funds held at the bank". Under CASS 15 that comparison is a dated, audited control.
- An FBO or safeguarding structure makes the provider's sub-ledger the only record of ownership; its correctness is a legal matter, not only an engineering one.
- A provider that is a bank can pay out before it is paid and can keep balances as deposits; a provider that is not must fund any advance from corporate money and keep it apart from user money. The "user funds versus corporate funds" flag on Stripe's financial accounts is that separation in code.
- Regional entities are money boundaries: one balance platform per acquiring region at Adyen, one licensed entity per region at Stripe. Cross-region payouts are transfers between legal entities, not rows moving between tables.
- A platform builder that never holds user funds (Larkfield) stays outside all of this only as long as the provider is the one in "possession or control"; Stripe's PSD2 FAQ and its Global Payouts comparison show where that line is.

---

## Key numbers

| Number | Definition | Source | Date |
| --- | --- | --- | --- |
| 5 billion events a day | Events Stripe's Ledger "sees" each day | stripe.dev Ledger post | 2024-02 |
| 99.99% within 4 days | Share of Stripe's dollar volume "fully ingested and verified" by Ledger within four days | same | 2024-02 |
| 99.999% | Share of Ledger activity "monitored, categorized, and triaged" through tooling; also the DQ Platform's "readiness target" and timeliness guarantee | same | 2024-02 |
| over 99.9999% | "explainability of money movement" | same | 2024-02 |
| 10x | Growth in Stripe's data volume over an unstated period | same | 2024-02 |
| About 50 rows | Rows inserted into Adyen's accounting database over the lifetime of one payment | Adyen Design to Duty part 2 | 2021-08 (5 years old) |
| Hundreds of terabytes | Size of Adyen's transactional PostgreSQL databases | same | 2021-08 (5 years old) |
| ~20 TB, 3 people | Data managed by Square's Books and the team maintaining it | Square engineering blog | 2019-10 (7 years old) |
| 2 business days (US); 7 calendar days then 3 business days (most of Europe, UK) | Stripe settlement timing: time from payment to available balance, initial then default | docs.stripe.com/payments/balances | accessed 2026-11 |
| 6 business days | Stripe settlement timing for SEPA Direct Debit (ACH Debit 4, Bacs 4) | same | accessed 2026-11 |
| 2 or 3 business days | Adyen Sales day payout delay for a typical method mix (3, 7 or 12 for partner-onboarded accounts) | docs.adyen.com/account/sales-day-payout | accessed 2026-11 |
| 30 days | Cap on Adyen's pre-financing before an unsettled amount is reversed | docs.adyen.com upgrade-to-sdp | accessed 2026-11 |
| 25% | Share of captured volume in late-settling methods above which Adyen may delay the payout day | Adyen Sales Day Payout Terms | last update 2024-06-17 |
| 2 hours | Time after sales day close at which Adyen's payable batch closes | docs.adyen.com/account/sales-day-payout | accessed 2026-11 |
| 180 days | Stripe: negative connected-account balance age at which the platform's reserve is transferred; also the maximum length of a platform-created reserve | docs.stripe.com Connect pages | accessed 2026-11 |
| 30 minutes | Typical arrival of a Stripe Instant Payout; also Adyen card payouts | both providers' docs | accessed 2026-11 |
| 10 a day; 9,999 USD/EUR/GBP | Stripe Instant Payout count limit and per-payout maximum | docs.stripe.com/payouts/instant-payouts | accessed 2026-11 |
| 1,000,000 USD | Adyen maximum for a US `instant` priority transfer | docs.adyen.com pay-out-to-bank-accounts | accessed 2026-11 |
| Up to 5 business days | Time for a failed Stripe payout to be returned and its status to change from `paid` to `failed` | docs.stripe.com/payouts | accessed 2026-11 |
| 2 senders (US, GB) + 22 preview | Countries whose businesses can send Stripe Global Payouts; "more than 160 markets" as destinations | docs.stripe.com/global-payouts | accessed 2026-11 |
| 0.50 EUR / 0.50 GBP / 0.50–25.00 USD | Stripe Global Payouts per-payout fees on SEPA, Faster Payments and US rails (ACH to Fedwire) | docs.stripe.com/global-payouts/pricing | accessed 2026-11 |
| Within 12 hours | Stripe processing time for balance and payout reconciliation reports after the day ends | docs.stripe.com/reports/options | accessed 2026-11 |
| 3 hours | Sigma data availability; Data Pipeline delivery cadence | docs.stripe.com stripe-data pages | accessed 2026-11 |
| 9 October 2025 | Date by which euro-area PSPs must offer verification of the payee and sending of instant euro transfers (9 July 2027 outside the euro area) | Regulation (EU) 2024/886 | 2024-03 |
| 2 million a day; 300+ | UK Confirmation of Payee checks per day and implementing organisations | Pay.UK | accessed 2026-11 |
| 7 May 2026 | Commencement of the FCA's Supplementary Regime for safeguarding (CASS 15) | FCA PS25/12 | 2025-08 |
| EUR 125,000 | PSD2 minimum initial capital for a payment institution providing the main payment services | Directive (EU) 2015/2366 Art. 7 | 2015 |
| 53 | US jurisdictions in which Stripe Payments Company lists a licence or authority | stripe.com/legal/spc/licenses | accessed 2026-11 |
| 31 states | States that have enacted the Money Transmission Modernization Act in full or in part | CSBS | 2026-09 |

## Open questions / not verifiable

1. **How Stripe's customer-facing balance relates to Ledger.** Neither post says whether Balance and BalanceTransaction are read from Ledger, from MMS, or from a separate store, or how fast a ledger event becomes visible in the API.
2. **Stripe Ledger's storage and consistency model.** No database, partitioning scheme or write path is named.
3. **Whether Adyen's 2021 accounting design is current.** No newer engineering source exists; the number of clusters, the round-robin sharding and the PostgreSQL choice may have changed.
4. **Balance Platform internals at Adyen.** How balance accounts are implemented, and how an available balance is checked at authorisation for issued cards, is not public.
5. **Whether Stripe pre-finances standard payouts.** The docs give a fixed availability schedule and are silent on Stripe's own receipt of funds.
6. **Stripe's reconciliation against networks and banks.** File formats, match rates, exception volumes and tooling beyond the DQ description are not public. The same holds for Adyen beyond the 2021 two-step matching description.
7. **Where each company holds customer funds.** Stripe does not name its EU or UK safeguarding banks; Adyen's use of central bank accounts was not verified (Annual Report not read).
8. **What share of Stripe's US volume the Georgia MALPB acquires**, and the date it began processing.
9. **Final approval of Bridge National Trust Bank.** Only the OCC's preliminary conditional approval of 12 February 2026 was verified.
10. **PSD3/PSR publication date and the new safeguarding text.** To be checked against the Official Journal before publication of chapter 16.
11. **Whether the FCA's Supplementary Regime commenced on 7 May 2026 as planned**, and whether any consultation on the end-state regime has started.
12. **Instant payout pricing by country** (Stripe) and **any price list for transfer priorities** (Adyen).
13. **Report completion times at Adyen.** No published duration was found.
14. **The EPC Verification Of Payee scheme rules** (response time, result codes) were not read from the EPC.
15. **Airbnb and Coinbase ledger material** was not read.

## Source list

**Stripe engineering and documentation**

- "Ledger: Stripe's system for tracking and validating money movement", Ilya Ganelin, Stripe, 2024-02-16, https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement — Ledger design, DQ metrics, scale numbers.
- "How we built Stripe Credits: A programmable, auditable way to pay your Stripe fees", Pratik Gupta and Sai Samant, Stripe, 2026-04-16, https://stripe.dev/blog/how-we-built-stripe-credits-a-programmable-auditable-way-to-pay-your-stripe-fees — MMS, financial accounts, OMT lifecycle, logical accounts, user versus corporate funds.
- "Balances and settlement time", Stripe docs, n.d., https://docs.stripe.com/payments/balances.md — balance types, pending and available, settlement timing tables.
- "Balance transaction object", Stripe API reference, n.d., https://docs.stripe.com/api/balance_transactions/object.md — fields, balance types, type enum.
- "Receive payouts from Stripe", Stripe docs, n.d., https://docs.stripe.com/payouts.md — schedules, same-day payouts, negative payouts, failures, fees.
- "Instant Payouts for Stripe Dashboard users", Stripe docs, n.d., https://docs.stripe.com/payouts/instant-payouts.md — availability, limits, funds eligibility.
- "Instant Payouts for Connect", Stripe docs, n.d., https://docs.stripe.com/connect/instant-payouts.md — platform liability for instantly paid funds.
- "Understanding Connect account balances", Stripe docs, n.d., https://docs.stripe.com/connect/account-balances.md — negative balances, platform reserve, 180-day collection, holding periods.
- "Set reserves on your connected accounts", Stripe docs, n.d., https://docs.stripe.com/connect/connected-account-reserves.md — reserve holds and plans.
- "Reserves – Frequently asked questions", Stripe support, n.d., https://support.stripe.com/questions/reserves-frequently-asked-questions — fixed and rolling reserves (read through a summarising fetch).
- "Minimum balances for automatic payouts", Stripe docs, n.d., https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md — merchant-set buffer.
- "Add funds to your Stripe balance", Stripe docs, n.d., https://docs.stripe.com/get-started/account/add-funds.md — top-ups, VBAN.
- "Multi-currency settlement", Stripe docs, n.d., https://docs.stripe.com/payouts/multicurrency-settlement.md — settlement currencies and fees.
- "Global Payouts", Stripe docs, n.d., https://docs.stripe.com/global-payouts.md — availability, funding, positioning.
- "Understand differences between Global Payouts and Connect cross-border payouts", Stripe docs, n.d., https://docs.stripe.com/connect/cross-border-payouts-to-recipients/compare-global-payouts.md — licences, ledgering, reversals.
- "Send payouts", Stripe docs, n.d., https://docs.stripe.com/global-payouts/send-money.md — networks, Confirmation of Payee, failure handling.
- "Manage payouts", Stripe docs, n.d., https://docs.stripe.com/global-payouts/manage-payouts.md — statuses, returns.
- "Supplemental pricing information" (Global Payouts), Stripe docs, n.d., https://docs.stripe.com/global-payouts/pricing.md — per-rail and FX fees.
- "Connect cross-border payouts", Stripe docs, n.d., https://docs.stripe.com/connect/cross-border-payouts.md — supported regions and funds flows.
- "Connect pricing", Stripe, n.d., https://stripe.com/connect/pricing — Instant Payouts fee as shown to a Netherlands visitor.
- "Treasury", Stripe docs, n.d., https://docs.stripe.com/treasury.md — financial accounts, DDA versus FBO, Fifth Third Bank, availability.
- "Payout reconciliation report" and "Balance summary report", Stripe docs, n.d., https://docs.stripe.com/reports/payout-reconciliation.md, https://docs.stripe.com/reports/balance.md — report purposes, instant payout caveat.
- "How report configuration works", Stripe docs, n.d., https://docs.stripe.com/reports/options.md — 12-hour data availability.
- "How Sigma works" and "Sigma data freshness", Stripe docs, n.d., https://docs.stripe.com/stripe-data/how-sigma-works.md, https://docs.stripe.com/stripe-data/available-data.md — Sigma and its freshness.
- "How Data Pipeline works" and "Data Pipeline data freshness", Stripe docs, n.d., https://docs.stripe.com/stripe-data/access-data-in-warehouse.md, https://docs.stripe.com/data/data-pipeline/data-freshness.md — destinations, cadence.
- "Bank reconciliation", Stripe docs, n.d., https://docs.stripe.com/bank-reconciliation.md — US-only availability.
- "Verification of Payee support for Treasury", Stripe support, n.d., https://support.stripe.com/questions/verification-of-payee-support-for-treasury — VoP on EU payouts (summarising fetch).

**Stripe legal and regulatory pages**

- "Stripe Services Agreement" (UK), Stripe, last modified 2026-09-28, https://stripe.com/gb/legal/ssa — contracting entities per region.
- "Authorised Payment Services" (STEL), Stripe, last updated 2019-04-05, https://stripe.com/stel/legal — Irish e-money authorisation C187865.
- "Authorised Payment Services" (SPUKL), Stripe, last updated 2017-01-26, https://stripe.com/gb/legal/spukl — UK e-money authorisation 900461.
- "Frequently asked questions about Stripe Connect and PSD2", Stripe, last updated 2024-01-18, https://stripe.com/ie/guides/frequently-asked-questions-about-stripe-connect-and-psd2 — passporting, safeguarding accounts, platform possession and control.
- "Safeguarding Stripe users' funds in the UK", Stripe support, n.d., https://support.stripe.com/questions/safeguarding-stripe-users-funds-in-the-uk — safeguarding accounts, FSCS (summarising fetch).
- "Acquirer Disclosure & Acquirer Terms", Stripe, n.d., https://stripe.com/en-us/legal/acquirer-disclosure — acquirers per country, US sponsor banks, Stripe MALPB.
- "Stripe Payments Company Licenses", Stripe, n.d., https://stripe.com/legal/spc/licenses — US money transmitter licences.
- "Issuing Bank Terms - Celtic Bank", Stripe, n.d., https://stripe.com/legal/celtic-spend-card — issuing bank and programme manager roles.

**Adyen engineering, documentation and corporate pages**

- "Design to Duty: The Accounting and Reporting Systems at Adyen", Willem Pino, Adyen, 2021-08-23, https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2 — templates, zero-sum proof, sharding, partner-report matching.
- "Getting paid", Adyen docs, n.d., https://docs.adyen.com/account/getting-paid.md — payable batch, payout models, timing, net payouts.
- "Sales day payout", Adyen docs, n.d., https://docs.adyen.com/account/sales-day-payout.md — payout delay, batch close, adjustments.
- "Upgrade to Sales day payout", Adyen docs, n.d., https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp.md — 30-day pre-financing cap, reversal journal types.
- "Pass-through payout", Adyen docs, n.d., https://docs.adyen.com/account/pass-through-payout.md — settlement-driven batches.
- "Sales Day Payout Terms of Service", Adyen, last update 2024-06-17, https://www.adyen.com/legal/sales-day-payout-terms-of-service — payout irrespective of receipt, set-off, negative balance.
- "Balances", Adyen docs, n.d., https://docs.adyen.com/account/balances.md — pending, next payout, reserve, deposit.
- "Payment processing invoice" and "Invoice reconciliation guide", Adyen docs, n.d., https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice.md, https://docs.adyen.com/reporting/invoice-reconciliation.md — monthly invoice and true-up.
- "Settlement details report", "Aggregate settlement details report", "Payment accounting report", Adyen docs, n.d., under https://docs.adyen.com/reporting/ — journal types, record types.
- "Balance Platform Accounting Report", Adyen docs, n.d., https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report.md — booking and value dates.
- "Settle funds" and "Platform account structure", Adyen docs, n.d., https://docs.adyen.com/platforms/settle-funds.md, https://docs.adyen.com/platforms/account-structure-resources/platform-structure.md — sales day settlement, balance accounts.
- "Payouts and Payments", "Pay out to bank accounts", "Pay out to third-party cards", "Payout lifecycle" (last modified 2026-11-17), "Verify counterparty name", Adyen docs, under https://docs.adyen.com/payouts/payout-service/ — priorities, routes, cut-offs, statuses, returns, name check.
- "Adyen Launches Intelligent Money Movement...", Adyen press release, 2026-04-09, https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement — product, licences statement.
- "Intelligent Money Movement", Adyen product page, n.d., https://www.adyen.com/intelligent-money-movement — components.
- "Adyen publishes H1 2026 financial results", Adyen, 2026-08-13, https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne — French clearing access, UAE licence.
- "Licenses & Disclosures" (index, EMEA, United States, Singapore, Australia), Adyen, n.d., https://www.adyen.com/licenses — licences per region.
- "Adyen granted US branch license", Adyen, 2021-06-14, https://www.adyen.com/press-and-media/adyen-granted-us-branch-license — OCC and Federal Reserve approvals.
- "Embedded Accounts and Card Issuing", Adyen, n.d., https://www.adyen.com/accounts — interest on deposited funds.

**Contrast companies**

- "Books, an immutable double-entry accounting database service", Łukasz Strzałkowski, Square, 2019-10-16, https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/ — prevention by construction, schema.
- "Engineering Uber's Next-Gen Payments Platform", Dmitry Chornyi, Uber, 2018-12-05, https://www.uber.com/blog/payments-platform/ — design goals.
- "Revolutionizing Money Movements at Scale with Strong Data Consistency", Uber, 2020-10-02, https://www.uber.com/blog/money-scale-strong-data/ — Gulfstream.
- "How Uber Migrated Financial Data from DynamoDB to Docstore", Uber, 2021-11-10, https://www.uber.com/blog/dynamodb-to-docstore-migration/ — LedgerStore guarantees.
- "Debit/Credit: The Schema for OLTP" and "Two-Phase Transfers", TigerBeetle docs, n.d., https://docs.tigerbeetle.com/concepts/debit-credit/, https://docs.tigerbeetle.com/coding/two-phase-transfers/ — immutability, pending transfers.
- "Accounting for Developers, Part I", Modern Treasury, 2022-08-17 (updated 2025-08-13), https://www.moderntreasury.com/journal/accounting-for-developers-part-i — immutable transactions versus mutable balances.

**Regulators, legal texts and standards bodies**

- Directive (EU) 2015/2366 (PSD2), Official Journal, 2015-12-23, http://publications.europa.eu/resource/celex/32015L2366 — Articles 7, 10, 18.
- Directive 2009/110/EC (second E-Money Directive), Official Journal, 2009-10-10, http://publications.europa.eu/resource/celex/32009L0110 — Article 7.
- Regulation (EU) 2024/886 (Instant Payments Regulation), Official Journal, 2024-03-19, http://publications.europa.eu/resource/celex/32024R0886 — verification of the payee, instant transfer deadlines.
- "PS25/12: Changes to the safeguarding regime for payments and e-money firms", FCA, 2025-08-07, https://www.fca.org.uk/publications/policy-statements/ps25-12-changes-safeguarding-regime-payments-and-e-money-firms and https://www.fca.org.uk/publication/policy/ps25-12.pdf — Supplementary Regime, CASS 15, end-state position.
- "Confirmation of Payee", Pay.UK, n.d., https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/ — service description and volumes.
- "CSBS Money Transmission Modernization Act (MTMA)", Conference of State Bank Supervisors, status as of 2026-09, https://www.csbs.org/csbs-money-transmission-modernization-act-mtma — US state standards and adoption.
- Corporate Decision #1365, Office of the Comptroller of the Currency, 2026-02-12, https://www.occ.treas.gov/topics/charters-and-licensing/interpretations-and-actions/2026/cd1365.pdf — preliminary conditional approval of Bridge National Trust Bank.

**Secondary sources**

- "Georgia approves Stripe application to form MALPB", ICBA, 2025-07-08, https://www.icba.org/newsroom/news-and-articles/2025/07/08/georgia-approves-stripe-application-to-form-malpb — trade association news item.
- "OCC conditionally approves Stripe subsidiary Bridge for trust charter", Banking Dive, 2026-02-18, https://www.bankingdive.com/news/stripe-bridge-occ-conditional-approval-national-trust-bank-charter/812417/ — trade press.
- "PSR/PSD3: EU Payment Services Legislation is Agreed", William Fry, 2025-11-28, https://www.williamfry.com/knowledge/psr-psd3-eu-payment-services-legislation-is-agreed/ — law-firm briefing on the provisional agreement.
