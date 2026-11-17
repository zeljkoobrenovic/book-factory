# Reconcile log — preface-parts-1-3

17 November 2026. Scope: fragments `preface.json`, `part-1.json`, `part-2.json`, `part-3.json` and their written pages. Evidence: `_research/verification/*.md` and `consistency-issues.md` (ruling numbers in brackets). No unit was added, dropped, merged or reordered; no part thesis claim was changed.

## Changes, per fragment and page

### preface
- part `preface` thesis.how_why (ruling 45, ch39 verification): “and neither company publishes how it delivers webhooks or where its data centers are.” → “and neither company publishes how its webhook sender is built or how one of its data centers takes over from another.”

### introduction
- journal entry `introduction` thesis.how_why (plain factual error: both name places; rulings 42, 45, ch39 verification): “neither publishes how it delivers webhooks or where its infrastructure is located.” → “neither publishes how its webhook sender is built or how one of its regions takes over from another.”

### where-payment-systems-go-wrong
- spec.json body (ruling 28 / K3: not nightly): “a nightly reconciliation against each provider's itemized report” → “a reconciliation against each provider's itemized report, run when that provider's reports are ready”
- spec.json body (stale open question closed): “The journal spec's part-level outcome still says 'eight incidents in 2026' and the meet-larkfield entry's AC-2 expected answer still says 'S” → “Resolved 17 November 2026: the journal spec's part-level outcome and the meet-larkfield entry's AC-2 now follow consistency rulings 24 and 20 (eight incidents, seven of them in 2026; the Silent Webhoo”
- index.md (ruling 28 / K3: Keel job is not nightly): “a nightly reconciliation against each provider's itemized report;” → “a reconciliation against each provider’s itemized report;” (the word “nightly” removed; no words added, to stay within 6,500)

### meet-larkfield
- spec.json body (stale open question closed): “The journal spec's AC-2 'expected' answer places the Silent Webhook on 'a Saturday night' and 'Sunday morning' and says under K2 'state chan” → “Resolved 17 November 2026: the journal spec's AC-2 'expected' answer now follows rulings 20 and 12 (the Silent Webhook on Monday 14 September 2026; on Adyen the confirming record is the webhook plus t”
- spec.json body (stale open question closed): “and keeps the thesis wording 'incidents of 2026' in the claim.” → “; the thesis claim now reads 'eight incidents of 2025–2026' (ruling 24).”
- spec.json body (stale open question updated): “K3 says 'the nightly reconciliation covers both providers'; chapter 15's addition says” → “K3 in the ledger now reads 'the reconciliation job covers both providers, one run per provider, started when that provider's reports are ready'; chapter 15's addition says”
- spec.json body (ruling 28 / K3: not nightly): “clearing accounts return to zero; nightly reconciliation covers both providers, written only from report lines” → “clearing accounts return to zero; the reconciliation job covers both providers, one run per provider when its reports are ready, written only from report lines”

### part-1
- part `part-1` thesis.how_why (ch2 verification row 52: Table 5-12 has country windows from 1 day): “Visa's public rules give an authorization 5 to 30 days of validity” → “Visa's public rules give an authorization, in their general table, 5 to 30 days of validity”

### 01-journey-of-a-payment
- journal entry `journey-of-a-payment` thesis.how_why (ruling 27a, 27b): “names Stripe entities as acquirer in Europe and partner banks in the United States, where Stripe acts as a payment facilitator; Adyen holds a banking license from the Dutch central bank and does not publish a per-country list.” → “names Stripe entities as acquirer in Europe and six acquirers in the United States (five banks and Stripe's own limited-purpose bank), where Stripe acts as a payment facilitator; Adyen holds a banking license from the Dutch central bank and lists the countries and regions where it has an acquiring connection without naming the acquiring entity in each.”
- spec.json body (ruling 27b): “since Adyen publishes no per-country list)” → “since Adyen names no acquiring entity per country)”
- spec.json body (ruling 27b): “Adyen publishes no per-country list of the acquirer of record; the chapter” → “Adyen lists the countries and regions where it has an acquiring connection but names no acquiring entity per country; the chapter”

### 02-authorization
- journal entry `payment-authorization` thesis.claim (ch2 verification row 52): “which Visa's rules set at 5 to 30 days depending on the kind of transaction.” → “which Visa's rules set, in their general table, at 5 to 30 days depending on the kind of transaction.”
- spec.json body (ch2 verification row 32): “Adyen reason 38, "Retry with 3D Secure")” → “Adyen reason 38, "Authentication required")”

### 03-clearing-and-settlement
- journal entry `clearing-and-settlement` thesis.claim (ruling 18: a payout is not necessarily after network settlement): “and the provider's payout to the merchant is a fourth step after that.” → “and the provider's payout to the merchant is a fourth step, on the provider's own schedule.”
- journal entry `clearing-and-settlement` AC-1 expected (ruling 18): “Money moves between the banks as net amounts a day or more after the approval, and the payout follows that.” → “Money moves between the banks as net amounts a day or more after the approval, and the payout follows on the provider's own schedule.”

### 05-payment-economics
- journal entry `payment-economics` thesis.how_why (ch5 verification row 64: one product-family run rate is published): “Stripe publishes total volume and no revenue, so its take rate cannot be computed.” → “Stripe publishes total volume and no revenue for the company, so its take rate cannot be computed.”
- spec.json body (ch5 verification row 64): “Stripe publishes the value its customers moved and no revenue, so” → “Stripe publishes the value its customers moved and no revenue for the company, so”
- spec.json body (ch5 verification row 64): “but no revenue, so its take rate cannot be computed from public figures.” → “but no revenue for the company, so its take rate cannot be computed from public figures.”
- spec.json body (ch5 verification row 64): “The letter gives no revenue or net revenue figure and does not define total volume.” → “The letter gives no revenue or net revenue figure for the company (its one revenue number is a run rate for the Revenue suite) and does not define total volume.”
- spec.json body (stale open question closed): “, although the journal-spec thesis wording says 'per successful payment'.” → “; the journal-spec thesis wording was corrected to match on 17 November 2026.”

### part-2
- part `part-2` thesis.how_why (Stripe's disclosure names the acquirer per country; what is unpublished is the membership class, as chapter 6 says): “neither publishes network membership per country, volume per acquirer” → “neither publishes network membership class per country, volume per acquirer”

### 06-acquiring-and-network-connectivity
- journal entry `acquiring-and-network-connectivity` thesis.claim (ruling 27a): “a payment facilitator under named partner banks in markets such as the United States” → “a payment facilitator under named acquirers, most of them banks, in markets such as the United States”
- journal entry `acquiring-and-network-connectivity` thesis.how_why (ruling 27c): “and it discloses reliance on banking partners where it has no acquiring license of its own.” → “and its annual report places concentration risk at banking partners 'in locations where there are no own direct acquiring licenses', which the chapter reads, as an inference, as reliance on partners there.”
- spec.json body (rulings 27b, 27c): “it relies on banking partners where it has no acquiring license, and it publishes no list of network memberships.” → “its annual report names banking partners 'in locations where there are no own direct acquiring licenses' (read, as an inference, as reliance on them), and it publishes no list of network memberships w”
- spec.json body (ruling 27c): “Adyen uses partner banks in some markets and does not name them.” → “The author's inference from a concentration-risk sentence: Adyen uses partner banks in some markets; it does not name them.”
- spec.json body (ruling 33a): “Trade press, September 2026: 'Stripe's MALPB received permission to begin business in May of this year'.” → “Georgia Department of Banking and Finance, bulletin of May 2026: Stripe MALPB, Atlanta, approved 30 June 2025, began business 28 May 2026.”
- spec.json body (ruling 33a): “Georgia approved Stripe's charter application in July 2025 (ICBA); trade press reports permission to begin business in May 2026.” → “The Georgia regulator's May 2026 bulletin gives approval on 30 June 2025 and the start of business on 28 May 2026; Stripe's terms for the bank carry the same date.”
- spec.json body (ruling 33a): “is not stated by Stripe; the dates come from trade press.” → “is not stated by Stripe; the dates come from the Georgia regulator's May 2026 bulletin and Stripe's terms for the bank.”
- spec.json body (ruling 30): “(documentation page last modified 2020, sentence live in November 2026)” → “(documentation, n.d., accessed November 2026)”
- index.md (ruling 33a: primary source for the Georgia bank): “According to trade press of September 2026 (secondary source), "Stripe's MALPB received permission to begin business in May of this year".” → “The bulletin of Georgia's Department of Banking and Finance for May 2026 lists Stripe MALPB, Atlanta, with an approval date of 30 June 2025 and a date to begin business of 28 May 2026.”
- index.md (ruling 33a: source entry replaced): “- [Payments Firms Put Georgia's Limited Purpose Bank Charter to Work](https://www.pymnts.com/news/acquiring/2026/payments-firms-put-georgia-limited-purpose-bank” → “- [Financial Institutions Today, May 2026](https://dbf.georgia.gov/financial-institutions-bulletin-2026), Georgia Department of Banking and Finance, 2026-05 — Stripe MALPB: approved 30 June 2025, began business 28 May 20”
- index.md (ruling 30): Adyen documentation "last modified" dates in two body sentences and two Sources entries → "n.d., accessed November 2026"; evidence-age marks derived from them removed
- journal entry `acquiring-and-network-connectivity` thesis.claim (ruling 27a: in Japan the sponsor is a card company): “none where the provider is itself the acquirer, a sponsoring bank where it is not.” → “none where the provider is itself the acquirer, a sponsoring acquirer where it is not.”

### 07-local-payment-methods
- journal entry `local-payment-methods` thesis.how_why (ch7 verification rows 69, 70): “Neither publishes which methods it reaches through another payment company, so the chapter” → “Neither publishes a list of the methods it reaches through another payment company (single method pages name a partner), so the chapter”
- spec.json body (ch7 verification rows 69, 70): “How either company adds a method, and which methods it reaches through another payment company, is not public, so” → “No page found at either company says how it adds a method or lists the methods it reaches through another payment company (single method pages name a partner), so”
- spec.json body (ch7 verification rows 69, 70): “Which methods either provider delivers through another payment company is not public.” → “No list of the methods either provider delivers through another payment company was found; single method pages name a partner (Ebanx for Pix and PPRO in a SEPA mandate text at Stripe, a legacy bank ac”
- spec.json body (ruling 30): “; the brief records last modified 2023-08-29” → “”
- spec.json body (ruling 30): “, last modified 2023-05-08, evidence age 3 years)” → “, n.d., accessed 2026-11)”
- spec.json body (ruling 30): Adyen documentation "last modified" dates in evidence and source strings → "n.d., accessed 2026-11"
- index.md (ruling 30): 12 Adyen "last modified" dates in the text and 10 in Sources → "n.d., accessed November 2026"; three evidence-age marks derived from them and the Sources note on metadata dates removed

### 08-payment-state-machines
- journal entry `payment-state-machines` thesis.how_why (ruling 29): “Adyen has published no design history comparable to Stripe's, so its reasons are not on record;” → “Adyen has published no design history comparable to Stripe's: a knowledge-hub post of 5 October 2021 gives the reason for `/sessions` (API calls 'reduced from three to only one'), and its reasons for result codes and asynchronous modifications are not on record;”
- spec.json body (ruling 29): “the reasons are not on record.” → “the reasons are not on record, except the one Adyen gave for /sessions in 2021.”
- index.md (ruling 29: scoped to online payments): “On Adyen there is nothing to read back: store” → “On Adyen there is nothing to read back for an online payment: store”
- index.md (ruling 28 / K3: not nightly): “and in the nightly reconciliation job against the providers' reports.” → “and in the reconciliation job against the providers' reports.”

### 10-routing-and-orchestration
- journal entry `payment-routing-and-orchestration` know[1] (ch9 row 57, ch10 row 73: the guide does not say 'its own'; external acquirer connections are documented): “Adyen documents (routing among its own routes, a forward endpoint” → “Adyen documents (routing among acquirers and networks, a forward endpoint”
- journal entry `payment-routing-and-orchestration` thesis.how_why (same): “Adyen documents routing among its own acquiring routes and networks (a US debit product” → “Adyen documents routing among acquirers and networks (a US debit product”
- journal entry `payment-routing-and-orchestration` thesis.how_why (ruling 31a wording, as chapters 22 and 23): “Whether network tokens survive a move between providers is not documented by either,” → “No Stripe or Adyen page read says whether network tokens survive a move between providers,”
- index.md (key point hedged as in chapters 22, 23 and the patterns page): “Neither Stripe nor Adyen documents whether network tokens survive a move.” → “No Stripe or Adyen page I read says whether network tokens survive a move.”
- index.md (ruling 28 / K3: not nightly): “a refund and the nightly reconciliation of both providers” → “a refund and the reconciliation of both providers”
- spec.json body (ruling 28 / K3): “K3: the nightly reconciliation covers both providers.” → “K3: the reconciliation job covers both providers.”
- spec.json body (ruling 31b): “No Stripe page on first-attempt least-cost routing was found.” → “No Stripe page on first-attempt least-cost routing of US debit was found; Stripe's support site documents it for Australian merchants.”
- spec.json body (ruling 31a): “No Adyen documentation page describing an export procedure was found.” → “An export article is listed in Adyen's help center, but its link redirects and the procedure could not be read on 17 November 2026.”
- spec.json body (ruling 31a): “Adyen's export procedure, timeline and fees, and the destinations its forward endpoint supports: no public documentation found.” → “Adyen's export procedure (an article is listed in its help center but could not be read on 17 November 2026), its timeline and fees, and the destinations its forward endpoint supports: no readable pub”
- spec.json body (ch10 verification row 66): “at the one merchant that has described it in public?” → “at the merchant that has given the most detailed public account of it?”

### 11-in-person-payments
- spec.json body (ruling 28 / K3): “and the nightly reconciliation job reads both providers' reports.” → “and the reconciliation job reads both providers' reports.”
- index.md (ruling 28 / K3: not nightly): “And the nightly reconciliation job, extended to both providers” → “And the reconciliation job, extended to both providers”
- spec.json body (ruling 30): Adyen documentation "last modified" dates in evidence and source strings → "n.d., accessed 2026-11"
- index.md (ruling 30): Adyen "last modified" dates and metadata-derived years in the text (8) and Sources (13) → "n.d., accessed November 2026"; evidence-age marks derived from them removed
- index.md (format): timetoread 27 → 26 min read (6,083 words ÷ 230 after the ruling-30 cleanup)

### 09-authorization-optimization
- index.md (ruling 37b, 37c): “Neither publishes a recovery rate. The process” → “Neither publishes a recovery rate across merchants: Adyen's knowledge-hub guide of 16 June 2026 quotes one customer's 4% improvement, with no baseline, and Stripe's "55%" covers its recovery tools together. The process”
- index.md (ruling 37b): “a recovery rate for Smart Retries or Auto Rescue, or an audited lift.” → “a recovery rate across merchants for Smart Retries or Auto Rescue, or an audited lift.”
- index.md (ruling 44): “in the Visa Core Rules of 24 October 2026 (Table 7-2)” → “in Visa's rules (Product and Service Rules, edition of 24 October 2026, Table 7-2)”
- index.md (ruling 44): “for the others (Visa Core Rules, 24 October 2026).” → “for the others (Visa's rules, Product and Service Rules, edition of 24 October 2026).”
- spec.json body (ruling 37b): “recovery rates for scheduled retries and any audited lift” → “recovery rates across merchants for scheduled retries and any audited lift”
- spec.json body (stale open question closed): “The article says so; the journal-spec sentence could be narrowed to Mastercard by its author.” → “The article says so, and the journal-spec sentence now says the same.”

### 15-payment-reconciliation-and-reporting
- journal entry `payment-reconciliation-and-reporting` thesis.claim (ruling 32c): “scheduled reports itemized per payout at Stripe and per payable batch at Adyen, which are complete” → “scheduled reports itemized per payout at Stripe and per payable batch at Adyen (for a platform, also per day and balance account), which are complete”
- journal entry `payment-reconciliation-and-reporting` know[2] (ruling 32c): “the unit each reconciles on (the payout at Stripe, the payable batch at Adyen)” → “the unit each reconciles on (the payout at Stripe; the payable batch at Adyen, with a daily report per balance account for platforms)”
- index.md (ruling 28 / K3: not nightly): “and a nightly reconciliation that covers both providers.” → “and a reconciliation that covers both providers.”
- spec.json body (ledger K3 wording): “clearing accounts must return to zero; the nightly reconciliation covers both providers.'” → “clearing accounts must return to zero; the reconciliation job covers both providers, one run per provider, started when that provider's reports are ready.'”
- spec.json body (ruling 32a): “No published completion time was found for any Adyen report (research brief, open question 13).” → “Adyen publishes when scheduled daily reports are generated (between 02:00 and 10:00 CET) and that a manual report 'may take several hours'; no time from batch close to report was found.”
- spec.json body (ruling 32b): “and data_available_end; Adyen's REPORT_AVAILABLE webhook.” → “and data_available_end; Adyen's REPORT_AVAILABLE webhook, and balancePlatform.report.created for balance platform reports.”
- spec.json body (ruling 32a): “created when the batch closes, no duration published.” → “created when the batch closes, a daily window for scheduled reports (02:00 to 10:00 CET), no time from batch close published.”
- spec.json body (ruling 32b): “/ REPORT_AVAILABLE webhook with a download URL. (5)” → “/ REPORT_AVAILABLE webhook with a download URL, and balancePlatform.report.created for balance platform reports. (5)”
- spec.json body (ruling 32d): “/ report files in CSV and other formats.” → “/ report files in CSV and other formats, and for platforms the Transfers API's transactions endpoint.”
- spec.json body (ruling 32b): “the Adyen run starts on the REPORT_AVAILABLE webhook for each merchant account's batch,” → “the Adyen run starts on the REPORT_AVAILABLE webhook for each merchant account's batch and on balancePlatform.report.created for the balance platform's daily report,”

### 16-licences-and-safeguarding
- journal entry `licences-and-safeguarding` know[1] (ruling 33b): “a state-licensed money transmitter and a payment facilitator of sponsor banks,” → “a state-licensed money transmitter and a payment facilitator of six named acquirers (five banks and its own limited-purpose bank),”
- journal entry `licences-and-safeguarding` thesis.how_why (ruling 33c): “The UK regulator's 2025 policy statement, with commencement set for 7 May 2026, adds” → “The UK regulator's 2025 policy statement, in force since 7 May 2026, adds”
- journal entry `licences-and-safeguarding` thesis.how_why (ruling 33d): “and a conditionally approved national trust bank for its stablecoin subsidiary” → “and a national trust bank for its stablecoin subsidiary that has the OCC's preliminary conditional approval only”

## Chapter thesis claims rewritten (each judged SOUND on all four rubric questions by a fresh agent given only the thesis object)

- `payment-authorization`: “which Visa's rules set at 5 to 30 days” → “which Visa's rules set, in their general table, at 5 to 30 days”.
- `clearing-and-settlement`: “the provider's payout to the merchant is a fourth step after that” → “… is a fourth step, on the provider's own schedule”.
- `acquiring-and-network-connectivity`: “a payment facilitator under named partner banks” → “under named acquirers, most of them banks”; “a sponsoring bank where it is not” → “a sponsoring acquirer where it is not”.
- `payment-reconciliation-and-reporting`: “per payable batch at Adyen” → “per payable batch at Adyen (for a platform, also per day and balance account)”.

Rubric readers' optional wording notes (not applied; argument-level or stylistic): ch. 3 question ends at “the acquirer's account” while the claim adds the payout as a fourth step; ch. 6 claim chains two colons and its question names local schemes the claim does not; ch. 15 “the same proof one level down” is soft; ch. 2 “one thing” sits awkwardly with a three-condition promise.

## Part-claim clauses not changed (author to decide)

- **Part I thesis claim**, clause “and the provider's payout after that”. Evidence: ruling 18 (Adyen's Sales Day Payout terms of 17 June 2024 pay “irrespective of whether the funds are actually received by Adyen”; a provider's payout runs on its own schedule, not necessarily after network settlement); chapter 3's page says “the provider pays the merchant on its own schedule”. Suggested wording: “and the provider's payout on its own schedule”. The copy in `part-1-intro/spec.json` must change with it.
- Preface, Part II and Part III thesis claims: no clause found that verification made false.

## Illustration placeholders

All placeholders on the 21 pages parse; captions, alt texts and prompts were scanned against the rulings and none was found false, so none was changed.

## Not changed, noted

- `introduction` and `how-payments-got-complicated` entries left as they are, except one plain factual error in `introduction` thesis.how_why (listed above). The `introduction` entry's know[4] (“no revenue”; “data-center or cloud-region layout”) is loose but not false; tighten when the page is written (Stripe's letter gives one product-family run rate; both companies name regions).
- Chapter 3 keeps “the fee … is fixed from the clearing record” in its key points, know[1] and how_why; the verifier (row 78) hedged only the take-away bullet, since neither source says it in those words. Left for the author.
- Spec evidence strings that cite numbered rules as “Visa Core Rules 5.3.1.x” (chapters 1 and 6) were left; ruling 44 was applied to the running text of chapter 9 only.
- Chapter 13 open question still mentions a 2021 front-matter date for Adyen's Balances page (a research note, not a citation).

## For other scopes

- The scenario ledger's `41-safe-change` line still calls the Keel reconciliation “nightly” (ledger not edited here).
- Chapters 22 and 23 and the patterns page now share the wording “no Stripe or Adyen page I read says whether network tokens survive a move” with chapter 10; check that 22/23 match.
- Chapter 39 and Part VIII: the preface how_why now says neither company publishes “how one of its data centers takes over from another”; keep the Part VIII wording consistent with it.

## Validation

`validate_spec.py payments-platform-architecture`: ok for the journal spec and every page spec. `check_draft.py structure`: passes on all 21 pages (patterns page 6,497 of 6,500 words). Placeholder extraction parses on all 21. Build: `[built] payments-platform-architecture`, only “missing post” warnings for pages not yet written. Check reports of the edited pages are now stale and need a new draft check.
