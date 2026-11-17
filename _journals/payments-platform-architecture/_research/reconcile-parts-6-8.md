# Reconcile log — parts-6-8 (17 November 2026)

Scope: `part-6.json`, `part-7.json`, `part-8.json`; pages `part-6-intro`, 27–32, `part-7-intro`, 33–36, `part-8-intro`, 37–41. Scopes below: `part:` = part-level fields of the fragment (and the intro spec's copy of the thesis), `entry:` = a post's journal entry and the copied fields of its page spec, `spec:` = unit-level fields of a page spec, `index:` = the page's `index.md` (cross-page fixes and placeholder fixes). Each line is old → new.

## Chapter 39 thesis rewritten under rule C

Besides the lines under `entry:payment-multi-region-and-data-residency` below, these fields were set directly: `thesis.claim`, `thesis.so_what`, `thesis.how_why` (last two sentences), `know[2]` (adds the list of data centers by continent or country), `know[3]`, AC-1 expected ("No AWS region is named"; "Stripe states active-active nowhere"), AC-2 expected (card updater, revenue recognition in Billing and Sigma; no fraud feature), AC-4 (3,000 → 3,800 words, the verified page's limit). The resolved author note was removed from the spec's open questions.

- Old claim: Where a localization law applies, it settles where payment data is stored before any latency or availability goal, and elsewhere the provider's hosting model does; the public record supports four statements about the two providers and no more: Stripe runs on Amazon Web Services and names no regions; Adyen runs its own infrastructure and names five integration regions without locations; Stripe moved its India data into the country and cut features to do it, while Adyen has published nothing on where Indian payment data is stored; and neither says how one region takes over from another.
- New claim: Where a localization law applies, it settles where payment data is stored before any latency or availability goal, and elsewhere the provider's hosting model does. About the two providers the public record supports four kinds of statement and no more: Stripe runs on Amazon Web Services and names no AWS region; Adyen runs its own data centers, names five integration regions and lists its sites by continent or country, no finer; Stripe says it stores Indian payment system data only in India and lists the features that cost, while Adyen describes an isolated India environment; and Adyen says it accepts payments in several data centers at once and that its load balancers fail over between them. Neither says between which places takeover happens or how fast, and Stripe says nothing about takeover.
- Rubric (fresh agent, thesis object only): all four questions pass. Its two notes (a mild tension between "no mechanism" and Adyen's load-balancer sentence; "no commitment" unexplained in so_what) were applied.
- Figure 3 placeholder (`39-two-shapes-of-answer`): the question-mark pins "showing that the place is unknown" were replaced by six map pins at continent or country level and a "no cities" tag; visual goal, alt and caption changed to match.

## `part:part-6`

- 'K1 derives the idempotency key for a renewal from the membership id plus the billing period, and' → 'K1 derives the idempotency key for a renewal from the membership id, the billing period and the number of the scheduled attempt, and'
- 'Not found in public sources: a subscription or invoice object, tax calculation, revenue recognition. Orb was acquired on 1 July 2026 and has billing and recognition features of its own, but no integrated Adyen product is documented.' → "Not found in public sources: a first-party subscription or invoice object, tax engine or revenue-recognition product; Adyen's terms leave each party its own tax obligations. Orb was acquired on 1 July 2026 and has billing and recognition features of its own, and Orb's documentation describes Adyen as a payment gateway for Orb invoices, but no billing product is documented as part of Adyen's platform."

## `entry:subscriptions-and-billing-engines`

- "and the chapter says that neither company has published its renewal scheduler's design." → 'and the chapter says where the public record on renewal scheduling stops: one 2024 Stripe engineering post describes a scheduling service, and neither company has published how that work is partitioned, paced or kept from running twice.'

## `entry:invoicing-collections-and-dunning`

- 'and its account updater, with the age of the Adyen pages stated.' → "and its account updater, with Adyen's documentation pages cited as undated."
- "Stripe's recovery figures are marketing claims without definitions, and no independent" → "Stripe's recovery figures and the one customer result Adyen has published for Auto Rescue are vendor claims without definitions, and no independent"

## `entry:billing-and-payment-tax`

- "The public record stops on the Adyen side: searches of Adyen's documentation, help center and product pages found only how Adyen taxes its own fees, which is absence of evidence and not a statement by Adyen, and Orb's tax handling was not verified. The chapter is short for that reason." → "The public record stops early on the Adyen side: searches of Adyen's documentation, help center and product pages found no product that calculates, collects or files tax on a merchant's sales, which is absence of evidence and not a statement by Adyen. They found how Adyen taxes its own fees, a tax amount the merchant may send with a payment, a `VAT` split type that books an amount the platform supplies, the filing of US form 1099-K for platform sellers, and a clause in Adyen's terms under which each party complies with its own tax obligations; Orb's documentation says it connects to third-party tax providers. The chapter is short for that reason."

## `entry:billing-revenue-recognition`

- "which describes Orb and not Adyen's platform; no Adyen product or documentation was found." → "which describes Orb and not Adyen's platform; no Adyen revenue-recognition product was found in its documentation, help center or site, where revenue recognition is mentioned only on an Orb partner page and in an article of 22 October 2026."

## `part:part-7`

- "No public source describes an Adyen arrangement in which Adyen bears seller losses, so the comparison on that point stops at Stripe's documented option." → "Adyen documents an arrangement in which it bears seller losses only as a pilot with limited availability (Managed Risk), so on that point the comparison is between Stripe's standing per-account option and an Adyen pilot."
- "its last chapter's question of who the legal seller is, answered there by handing the seller's role to the provider (merchant of record)." → "its last chapter's question of who sells to the customer, answered there by letting the provider sell in its own name (merchant of record)."
- 'and the liability the merchant of record took over in one piece is now divided among three parties by the account model.' → 'and the liability, of which a merchant of record takes over only the part its contract names, is now divided among three parties by the account model.'

## `entry:platform-payment-models`

- 'and the chapter says in plain words that the public record shows no Adyen equivalent of Stripe bearing seller losses.' → "and the chapter says in plain words that Adyen's default puts the platform behind its sellers and that Adyen bearing seller losses is documented only as a pilot with limited availability (Managed Risk)."
- "name the groomer's balance account, and the liable account stands behind a negative seller balance." → "name the groomer's balance account, and by default the liable account stands behind a negative seller balance (Adyen's Managed Risk pilot is the documented exception)."

## `entry:embedded-finance`

- 'is in public preview in the United Kingdom and private preview elsewhere, with a US legacy version closed to new builds' → 'is in public preview in the United Kingdom and private preview in the United States, Australia and the EU (and, on one page, Canada), with a US legacy version closed to new builds'

## `part:part-8`

- 'Where the public record stops for both companies: regions and locations, failover between regions, cells, replication settings and the design of the webhook sender.' → 'Where the public record stops for both companies: the topology and timing of a failover between data centers or regions, cells, which data is replicated synchronously and the design of the webhook sender; and what is published short of that (Adyen lists its data centers by continent or country and states that its load balancers fail over between them; Stripe names no AWS region).'
- "(2) documented (2021, 2025, 2026), with no cities or count beyond 'tens of data centres'; (3) not public; (4) documented in the public terms effective 2023, with exclusions; (5) not public, the documentation mentions only 'alternative routing' to 'backup infrastructure' without detail;" → "(2) documented (2021, 2025, 2026), with a list of sites by continent or country and no cities or count beyond 'tens of data centres'; (3) not public; (4) documented in the public terms (last updated 1 November 2023) as a 'commercially reasonable efforts' clause, with exclusions; (5) partially documented: Adyen's documentation says its load balancers 'manage the failover to the other data centers' and mentions 'alternative routing' to 'backup infrastructure', with no timing or topology, so 'within seconds' is not public;"
- 'On regions, cells, failover and replication settings the public record of both companies is silent, and the part says so instead of inferring.' → 'On the topology and timing of failover, on cells and on which data is replicated synchronously the public record of both companies stops (Adyen lists its data centers by continent or country and states that its load balancers fail over between them; Stripe names no AWS region and says nothing on takeover), and the part says so instead of inferring.'
- 'or by assumed regions that neither provider has documented.' → 'or by an assumed failover design that neither provider has documented.'
- "and the public record gives each provider's hosting and one documented localization case but not its regions or failover." → "and the public record gives each provider's hosting, the regions Adyen names and what each has said about India, but not the topology or timing of a failover."
- 'What neither has documented (regions, failover, cells, replication settings) is the part a merchant cannot verify.' → 'What neither has documented (the topology and timing of a failover, cells, which data is replicated synchronously) is the part a merchant cannot verify.'
- 'K1 removes the wrong outcome by deriving the key from the membership and the billing period.' → 'K1 removes the wrong outcome by deriving the key from the membership, the billing period and the number of the scheduled attempt.'

## `entry:part-8`

- 'that regions, cells, failover and the webhook sender are not public for either company.' → 'that a cell design, the topology and timing of a failover between regions, which data is replicated synchronously and the webhook sender are not public for either company.'

## `entry:payment-reliability-and-availability`

- 'a peak-weekend figure, a rolling 30-day figure, a contractual commitment)' → 'a peak-weekend figure, rolling 30-day and 90-day figures, a contractual commitment)'
- "Adyen's public terms (effective 2023) commit to 99.9% per quarter with exclusions while its status page reports successful requests over 30 days." → "Adyen's public terms (last updated 1 November 2023) commit it to 'commercially reasonable efforts' toward 99.9% per quarter, with exclusions, while its status page reports successful requests over 30 days and Stripe's status page displays 99.999% over 90 days with no definition."
- "Stripe's root-cause analysis of 10 July 2019, the one full public account found, reports" → "Stripe's root-cause analysis of 10 July 2019, the one full public account of an outage found, reports"

## `entry:payment-data-stores-and-consistency`

- 'What is not public for either company: replication mode, read consistency, and how' → 'What is not public for either company: which data is replicated synchronously, read consistency, and how'
- 'neither company states it, and replication mode, read consistency and the cross-cluster protocol are not public.' → 'neither company states it, and which data is replicated synchronously, read consistency and the cross-cluster protocol are not public.'

## `entry:payment-safe-change`

- 'What Adyen has published about release practice (2018, 2021) and database change without downtime (2018 to 2025), and that' → 'What Adyen has published about release practice (2018, 2021, and current documentation that says releases are applied continuously and frozen around named peak days) and database change without downtime (2018 to 2025), and that'
- 'a payment system cannot be stopped or frozen for its peaks, and the peak near miss' → 'a payment system cannot be stopped for its peaks, and the peak near miss'

## `entry:payment-multi-region-and-data-residency`

- 'or the topology, timing or mechanism of a failover at either company, and Stripe has published no statement on takeover.' → "or the topology or timing of a failover at either company, or any mechanism beyond Adyen's load-balancer sentence, and Stripe has published no statement on takeover."
- 'Neither describes how takeover works, between which places or how fast, and Stripe says nothing about it.' → 'Neither says between which places takeover happens or how fast, and Stripe says nothing about takeover.'
- 'a list of regions and countries with no cities and no commitment)' → 'a list of regions and countries with no cities and no commitment that data stays there)'

## `spec:27-subscriptions-and-billing-engines`

- 'and publishes nothing about how its scheduler is built.' → 'and has published one 2024 engineering post that describes a scheduling service, but not how that work is partitioned, paced or kept from running twice.'

## `spec:29-invoicing-collections-and-dunning`

- 'Visa Core Rules of 24 October 2026, Table 7-2:' → "Visa's rules (Product and Service Rules, edition of 24 October 2026), Table 7-2:"

## `spec:30-tax`

- 'stays with the seller unless the seller itself changes, which is what a merchant of record (a provider that becomes the legal seller) does.' → 'stays with the seller; the indirect tax itself moves only when a provider sells in its own name as merchant of record, the supplier for indirect tax where local rules allow.'

## `spec:31-revenue-recognition`

- 'A model that removes most of them by changing who the seller is, and what that costs in money, control and customer data.' → 'A model that moves some of them (the indirect tax, the handling of fraud and disputes, the name on the statement) by changing who sells to the customer, and what that costs in money, control and customer data.'
- 'the next chapter examines the model that removes most of that by making the provider the seller.' → 'the next chapter examines the model that moves part of that by letting the provider sell in its own name, and what stays with the business.'

## `spec:32-merchant-of-record`

- "This chapter handed the seller's role to the provider in one piece; Part VII" → "This chapter let a provider sell in its own name and found that only part of the seller's position moves with that, and that a platform cannot use the model; Part VII"
- "answered here by handing the seller's role to the provider." → 'answered here by letting the provider sell in its own name.'
- 'and the obligations a merchant of record takes over together are divided among three parties by the account model.' → 'and the liability, of which a merchant of record takes over only the part its contract names, is divided among three parties by the account model.'

## `spec:part-7-intro`

- "and chapter 32 handed the seller's role whole to a provider; Part VII" → 'and chapter 32 let a provider sell in its own name and take over the indirect tax and the handling of fraud and disputes; Part VII'
- "contrast with Part VI's merchant of record, which takes over the seller's obligations together; here" → "contrast with Part VI's merchant of record, which takes over only the part of the seller's liability its contract names; here"
- "and chapter 32's merchant of record, where a provider takes over the seller's role whole." → "and chapter 32's merchant of record, where a provider sells in its own name."
- 'are in public preview in the UK and private preview elsewhere at Stripe' → 'are in public preview in the UK and private preview in the US, Australia and the EU at Stripe'

## `spec:33-platform-payment-models`

- 'the Liable Balance Account Stands Behind Every Seller' → 'the Liable Balance Account Stands Behind Every Seller by Default'
- "Still open: the journal-spec fields copied here (intent.outcome.know[2], thesis.how_why, supporting claim S4) carry the old claim and wait for the author's correction of the journal spec." → 'The journal-spec fields copied here were corrected in the reconciliation pass of 17 November 2026.'

## `spec:34-platform-onboarding-and-verification`

- "The intent, thesis and acceptance criterion AC-3, copied from the journal spec, still say 'no conversion figures'; the author decides whether to reword them there." → ''

## `spec:36-embedded-finance`

- 'was in public preview in the United Kingdom and private preview elsewhere, with' → 'was in public preview in the United Kingdom and private preview in the United States, Australia and the EU (and, on one page, Canada), with'

## `spec:part-8-intro`

- '; and neither has published how its regions, cells or failover work.' → '; and neither has published a cell design or the topology or timing of a failover between regions.'
- 'neither names how one region takes over from another, and Stripe names no regions (chapter 39)' → 'neither describes between which places one region or data center takes over from another or how fast, and Stripe names no AWS region (chapter 39)'
- 'current documentation) and names no regions;' → 'current documentation) and names no AWS region;'
- 'The four statements the public record supports.' → 'The four kinds of statement the public record supports.'
- 'a payment system cannot be stopped or frozen for its peaks.' → 'a payment system cannot be stopped for its peaks.'

## `spec:37-payment-reliability`

- 'a peak-weekend figure, a rolling 30-day figure and a contractual commitment)' → 'a peak-weekend figure, rolling 30-day and 90-day figures and a contractual commitment)'

## `spec:38-payment-data-stores-and-consistency`

- 'the number of clusters and the replication mode are not public.' → 'the number of clusters and which data is replicated synchronously are not public.'
- 'the number of clusters or its replication mode.' → 'the number of clusters or which data it replicates synchronously.'
- 'the cross-cluster protocol, the replication mode, failover procedure and time.' → 'the cross-cluster protocol, which data is replicated synchronously, failover procedure and time.'
- '(replication mode, read consistency, the cross-cluster protocol)' → '(which data is replicated synchronously, read consistency, the cross-cluster protocol)'
- 'neither has published replication mode, read consistency or' → 'neither has published which data is replicated synchronously, read consistency or'
- 'clearing accounts must return to zero; nightly reconciliation)' → "clearing accounts must return to zero; reconciliation when each provider's reports are ready)"

## `spec:39-multi-region-and-data-residency`

- 'the public record supports four statements about the two providers and no more.' → 'the public record supports four kinds of statement about the two providers and no more, and neither says between which places takeover happens or how fast.'
- 'Provider B as five named integration regions placed no more exactly than a continent or a country.' → "Provider B as five named integration regions and six map pins at continent or country level, tagged 'no cities'."

## `spec:40-payment-peak-load`

- 'Visa Core Rules, 2026-10-24, glossary:' → "Visa's rules (Glossary, edition of 24 October 2026):"
- 'a payment system cannot be stopped or frozen for its peaks' → 'a payment system cannot be stopped for its peaks'
- 'Visa Core Rules of 24 October 2026.' → 'Visa Core Rules and Visa Product and Service Rules of 24 October 2026.'

## `spec:41-safe-change`

- 'a system that cannot be stopped or frozen for its peaks' → 'a system that cannot be stopped for its peaks'
- 'The database layer it describes has since been rebuilt (2024 post).' → "Stripe's 2024 post describes its database platform five years later."
- 'the nightly reconciliation covers both providers' → "the reconciliation job, run when each provider's reports are ready, covers both providers"
- 'by deriving the key from the membership and the billing period.' → 'by deriving the key from the membership, the billing period and the number of the scheduled attempt.'

## `index:29-invoicing-collections-and-dunning`

- '(Visa Core Rules, 24 October 2026: 20 attempts in 30 days)' → "(Visa's rules, 24 October 2026: 20 attempts in 30 days)"

## `index:30-tax`

- 'The only way to hand them over whole is to stop being the seller: a merchant of record is a provider that becomes the legal seller, and [[merchant-of-record]] covers that model.' → 'The only way to hand over the tax itself is to let a provider sell in its own name as merchant of record, the supplier for indirect tax where local rules allow ([[merchant-of-record]]).'

## `index:31-revenue-recognition`

- 'There is a model that removes most of that list at once, by changing who the seller is. [[merchant-of-record]] examines it, and what it costs in money, control and customer data.' → 'There is a model that moves part of that list, by changing who sells to the customer. [[merchant-of-record]] examines what moves, what stays, and what it costs in money, control and customer data.'

## `index:32-merchant-of-record`

- "This chapter handed the seller's role to a provider in one piece, and found that a platform cannot do that:" → "This chapter let a provider sell in its own name, found that only part of the seller's position moves, and found that a platform cannot do that:"
- 'and the obligations that a merchant of record takes over together are divided among three parties by the account model.' → 'and the liability, of which a merchant of record takes only the part its contract names, is divided among three parties by the account model.'

## `index:part-7-intro`

- 'in which a provider becomes the seller and takes over its obligations together ([[merchant-of-record]])' → 'in which a provider sells in its own name and takes over the indirect tax and the handling of fraud and disputes ([[merchant-of-record]])'

## `index:33-platform-payment-models`

- 'the Liable Balance Account Stands Behind Every Seller' → 'the Liable Balance Account Stands Behind Every Seller by Default'

## `index:40-payment-peak-load`

- 'The Visa Core Rules of 24 October 2026 define Stand-In Processing' → "Visa's rules of 24 October 2026 define Stand-In Processing in their glossary"

## `index:41-safe-change`

- 'ended with a system that cannot be stopped or frozen for its peaks,' → 'ended with a system that cannot be stopped for its peaks,'

## `index:39-multi-region-and-data-residency`

- 'a rented cloud with unnamed regions, and five named regions without addresses.' → 'a rented cloud with unnamed regions, and five named integration regions on sites listed by continent or country, with no cities.'
- 'under each building a blank map pin outline in gray with a question mark inside, showing that the place is unknown; a bracket above the five buildings labeled \\"own sites\\".' → 'a bracket above the five buildings labeled \\"own sites\\"; below the buildings a wide pale blue map strip with no borders drawn, carrying six solid teal map pins labeled \\"Europe\\", \\"United States\\", \\"India\\", \\"Singapore\\", \\"Japan\\" and \\"Australia\\", and beside the strip a small gray tag labeled \\"no cities\\".'
- 'Provider B is five named regions, each with no exact location.' → 'Provider B is five named regions on its own sites, with six map pins at continent or country level and a tag reading no cities.'
- 'Provider B (Adyen) is five named integration regions on its own sites, placed no more exactly than a continent or a country.' → 'Provider B (Adyen) names five integration regions and lists its own data centers by continent or country, with no cities.'

## `index:37-payment-reliability`

- 'a round gauge with a needle labeled \\"30 days\\"' → 'a round gauge with a needle labeled \\"Rolling\\"'
- 'a 30-day gauge and a signed contract' → 'a rolling-window gauge and a signed contract'

## Other direct edits

- `41-safe-change/spec.json`, `intent.audience.already_knows[1]`: 'the ledger and nightly reconciliation' → 'the ledger and reconciliation' (ledger editor line 1).
- `32-merchant-of-record/index.md` hand-off: after the replacement logged above it was shortened to stay under 5,500 words (now 5,498): 'This chapter let a provider sell in its own name and found that a platform cannot do that: … and the liability, of which a merchant of record takes only part, is divided among three parties by the account model.'
- One changelog entry dated 2026-11-17 added to each spec changed (27, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, part-7-intro, part-8-intro).

## Checked and left unchanged

- Entries for chapters 28, 32, 34, 35 and 40 and the `part-6` and `part-7` intro entries: no sentence found that the verification files or rulings contradict (32, 34 and 40 had been corrected earlier). Chapter 35's 'booked to the platform's liable balance account without an error' is Adyen's own wording on its split pages; the reserved incorrect splits account is one of the liable accounts and the page says so.
- 'Nightly' in chapters 35 (pre-Keel history), 38 and 41 (the comparison of paid payments with activated passes, and of export lines) are other jobs than the Keel reconciliation job.
- `32-merchant-of-record` line 201 says 'every chapter of Part VI' in plain text (a reference to its own part inside the closing synthesis); left.
- `part-8-intro/spec.json` `introduction.thesis_statement.text` was changed to what the page states (cell design, topology or timing of a failover); the `thesis.claim` copy is untouched.

## Part-claim clauses the author must decide

**Part VIII `thesis.claim`** (not edited): '…and neither has published how its regions, cells or failover work.'
- Evidence: ruling 45(a) and ruling 42(a). Adyen's documentation page 'Peak season readiness' describes an 'active/active, stateless architecture' and says load balancers 'manage the failover to the other data centers'; Adyen's Infrastructure page names data-center regions (Europe, the United States, India, Singapore, Japan, Australia) and says payments are 'stored in Europe and our isolated India environment'; its documentation names five integration regions. Stripe's Privacy Center names data centers in the United States and India for login and identity data. What remains unpublished for both is topology, timing, a cell design and which data is replicated synchronously (ruling 42b).
- Suggested wording: '…and neither has published a cell design or the topology or timing of a failover between its data centers or regions.' The intro page already says this in its key points and lead.
- The part's `how_why`, `so_what`, `know[1]`, AC-4 expected answers (2), (4), (5), supporting claim P8-3, the closing synthesis and the `part-8` AC-3 were corrected to this wording, so only the claim sentence still carries the old clause.

**Part VI and Part VII `thesis.claim`**: no clause found that the verification contradicts.

## For other scopes

- The K1 key was described without the attempt number in the Part VI and Part VIII closing callbacks (fixed here, ruling 13); other parts' closings and the preface may carry the same shortened form.
- `46-case-stripe` and any page that repeats 'a merchant of record takes over the seller's obligations together / in one piece' should follow chapter 32's corrected hand-off.
- `journal-spec.json` is listed as untracked in git (`_research/journal-spec-parts/` too), so there is no committed baseline to diff these fragments against.
