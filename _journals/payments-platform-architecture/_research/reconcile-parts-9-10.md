# Reconcile log — parts-9-10 (17 November 2026)

Scope: `part-9.json`, `part-10.json`; pages `part-9-intro`, `42`–`45`, `46-case-stripe`, `47-case-adyen`, `49-contrast-cases`, `50-what-is-moving`. `part-10-intro` and `48-the-bets-compared` have no page yet: only their journal entries were corrected. Every entry change below was applied to the fragment and, word for word, to the page spec's `intent`, `thesis` and `role`. One changelog entry dated 2026-11-17 was added to each of the nine specs.

## Part IX (part-level fields)

- `thesis.so_what`: "a nightly reconciliation of both providers (K3)" → "a reconciliation of both providers run when each one's reports are ready (K3)" (ruling 28). Re-synced in `part-9-intro/spec.json`.
- Part claim: no clause found false (see the end of this file).

## part-9-intro

- Journal entry: no change. Page: no change (26 of 26 statements agreed at verification; re-read against rulings 28, 29, 41).

## 42-journey-card-payment (`journey-card-payment`)

- `know[1]`: "the payout that contains it arriving on Thursday 11 March" → "…sent on Thursday 11 March" (ledger: sent 11 March, marked arrived 25 March).
- `know[2]`: "with no endpoint that returns a payment by its identifier" → "with no endpoint in the Checkout API that returns…" (ruling 29).
- AC-2 `expected`: same scoping, "no endpoint in the Checkout API that returns the payment by its identifier".
- `know[3]`: "whether Stripe makes funds available before it has received them" → "whether Stripe's standard payout schedule makes funds available before Stripe has received them (Stripe documents paying ahead only for Instant Payouts)" (ruling 18).
- `thesis.so_what`: "a nightly reconciliation of both providers' reports against the ledger (K3)" → "a reconciliation … run when each provider's reports are ready (K3)" (ruling 28).
- `thesis.how_why`: "Stripe publishes an availability schedule and nothing on whether its own receipt of funds comes first" → "…and, outside Instant Payouts, where it documents paying ahead, nothing on whether…" (ruling 18).
- Page: no change needed (the verifier had applied rulings 18, 27, 28, 29, 30, 32).

## 43-journey-failed-renewal (`journey-failed-renewal`)

- `know[3]`: "…and Adyen's account-updater page is dated 2019." → "…; the one recovery figure Adyen publishes for Auto Rescue is a single customer's, with no baseline." (rulings 30, 37b).
- Page, cross-page fix (ruling 44): "the Visa Core Rules of 24 October 2026 (Table 7-2)" → "Visa's rules (Product and Service Rules, edition of 24 October 2026, Table 7-2)".

## 44-journey-platform-payment (`journey-platform-payment`)

- `know[3]`: "Adyen publishes no option for the provider to take a seller's loss, no waiting period before the liable account is debited and no price list for platforms" → "Adyen documents an option in which it takes a seller's loss only as a pilot with limited availability (Managed Risk), and no Adyen price list for platforms was found" (ruling 41).
- AC-1 `expected`: "The parent gets the €60 either way…" → "On Adyen, and on Stripe with a destination charge, the parent gets the €60 at once…"; the Adyen sentence now adds the 30 days, the reserved compensation account and the Managed Risk pilot; "with a direct charge the tutor's connected account is debited and goes negative, Stripe first tries the tutor's bank account…" → "with a direct charge the refund is debited from the tutor's connected account, and while that balance is short the refund waits as pending and fails after 45 days, so the parent is not repaid until the balance is funded" (verification rows 44, 49, 50).
- `thesis.how_why`, last sentence: "Adyen publishes no equivalent of the provider taking the seller's loss and no waiting period…" → "Adyen documents a negative balance for up to 30 days before the platform's reserved compensation account is debited, and an arrangement in which Adyen itself bears the loss only as a pilot (Managed Risk), so the walkthrough states the default and names the pilot."
- Page: no change needed. Not changed, for the author: the excerpt, key point 2, the lead and three figure captions say the refund is debited from "a balance the payout emptied", while Studio Noord's balance on 18 March holds €212.40 (ruling 26). The phrase is the chapter's and the part's thesis wording (the €117.47 had been paid out); the text explains it in the paragraph "What paid Mila on 18 March was other members' money".

## 45-journey-dispute (`journey-dispute`)

- `thesis.claim` (chapter claim, one clause): "18 for a Visa card outside the US and Canada" → "18 for a Visa payment processed outside the US and Canada" (Adyen ties the figure to where the payment is processed, verification row 4). Rubric result: see below.
- `thesis.how_why`: "moves money when it is created and when it ends" → "moves money when it is created and, if the dispute is won, again when it ends" (verification row 72).
- Spec body: conclusion p7 evidence "K3 … with a nightly reconciliation" → "…with a reconciliation run when each provider's reports are ready" (ruling 28).
- Not changed, noted: `thesis.how_why` still describes the Visa flow Adyen calls Allocation; the page (a Mastercard dispute) does not use it. The sentence is not contradicted by any verification row.

## Part X (part-level fields)

- `intent.outcome.know[0]`: "partner banks named in the United States, Canada, Japan, India and Thailand" → "other acquirers, most of them banks, named in markets that include the United States, Canada, Japan, India and Thailand" (ruling 27a).
- `intent.outcome.know[1]`: "on its own data-center capacity" → "on servers it manages itself in six named data-center regions" (verification of 47, rows 1, 131; ruling 45).
- AC-3 `expected`: "its billing product (Orb) was bought and runs apart" → "…was bought; Adyen described it in June 2026 as run under an incubator model and says it is being integrated".
- `thesis.how_why`: "(trade press dates its approval to 2025, and reports a conditional national trust charter for Stripe's Bridge in February 2026)" → "(the Georgia regulator's bulletin dates its approval to 30 June 2025 and its start of business to 28 May 2026; the US regulator of national banks gave Stripe's Bridge preliminary conditional approval for a trust charter in February 2026)" (ruling 33a, d).
- `thesis.how_why`: "discloses partner banks where it has no license; on 1 July 2026 Adyen closed its first two acquisitions, one of which runs apart from the platform" → "names banking partners in locations where it has no acquiring license; on 1 July 2026 Adyen closed two acquisitions, the only ones its history page lists, one of which it described in June 2026 as run under an incubator model".
- `thesis.how_why`: "neither company publishes its network membership per country; Adyen gives no date for integrating what it bought" → "Adyen lists the countries and regions where it has an acquiring connection and names no acquiring entity per country; it says the integration of what it bought has begun and gives no date for its completion" (ruling 27b).
- Entry `part-10` (intro page, not written): no false statement found; no change.

## 46-case-stripe (`case-stripe`)

- `know[1]`: "partner banks in the United States, Canada, Japan, India and Thailand, and a Stripe limited-purpose bank among the US acquirers" → "other named acquirers, most of them banks, in markets that include the United States, Canada, Japan, India and Thailand, and a Stripe limited-purpose bank, in business since 28 May 2026, among the six US acquirers" (rulings 27a, 33a, b).
- `know[2]`: "valuations that are tender-offer prices" → "valuations that are prices from funding rounds and tender offers".
- `know[3]`: "anything about regions" → "which regions it runs in" (a 2025 talk says replicas span regions).
- AC-1 `expected`: "under named partner banks" → "under named acquirers, most of them banks (card companies in Japan)"; Georgia bank "in business since 28 May 2026"; "whether and how much the Georgia bank processes" → "which merchants the Georgia bank acquires for and how much it processes".
- `thesis.so_what`: "the named partner bank" → "the named acquirer".
- `thesis.how_why`: "partner banks are named for North America, Japan, India and Thailand; … trade press reports its approval in 2025 and a conditional trust charter for Bridge in 2026" → "other acquirers, most of them banks, are named for markets that include North America, Japan, India and Thailand; … (the state regulator's bulletin dates its approval to 30 June 2025 and its start of business to 28 May 2026), and a February 2026 letter from the US regulator of national banks gives Bridge preliminary conditional approval for a trust charter".
- `thesis.claim`: not changed ("partner banks" there is one of three components of the regulated layer and is true as such).
- Spec body: S3 "partner banks are named in…" → "other acquirers, most of them banks, are named in markets that include…"; S4 and section 6 controlling idea "tender-offer price(s)" → "price(s) of funding rounds and tender offers".
- Page: table row "Merchant of record (the legal seller to the customer, which owes the tax on the sale)" → "(the party that sells to the customer in its own name and takes over the indirect tax; on Stripe the cost of a lost dispute stays with the business)"; "Managed Payments (API changelog, 22 April 2026)" → "Managed Payments (announced May 2025; in a release version of the API since 22 April 2026)" (chapter 32).
- Page, Sources: press-release title "Amazon and Stripe sign expanded global agreement" → "Amazon-Stripe partnership accelerates ecommerce and streamlines online payments" (the page's headline; verification of chapters 39 and 40).
- Placeholder `46-regulated-layer-by-region`, caption: "in Region B (for Stripe, the United States) a partner bank is" → "in Region B (for Stripe, the United States with five of its six named acquirers) a partner bank is" (ruling 33b).

## 47-case-adyen (`case-adyen`)

- `know[0]`: "founded in Amsterdam in 2006 with a European acquiring license" → "founded in Amsterdam in 2006; a European acquiring license, which its history page dates only to the period 2006 to 2012".
- `know[3]`: "banking partners where it has no acquiring license" → "banking partners named as a concentration risk in locations where…"; "Orb run as an 'incubator'" → "Orb described in June 2026 as run as an 'incubator'"; "data-center locations and ownership" → "the cities, operators and number of its data centers beyond six named regions"; "the depth of integration of the acquired products" → "what has been integrated of the acquired products".
- AC-1 `expected`: the Orb statements dated to June 2026; added "on 28 October 2026 it wrote of 'the successful ongoing integration of Talon.One and Orb' without saying what has been joined".
- `thesis.claim` (chapter claim, one clause): "it uses banking partners where it has no acquiring license" → "it names banking partners in locations where it has no acquiring license" (ruling 27c). Rubric result: see below. "its own data-center capacity" kept: the annual report's "data center partners" qualifies it and does not contradict it (Adyen: "We administer and manage all our own servers").
- `thesis.disputed_by`: "that 'built, not bought' still describes the company" → "that the company still builds and does not buy" (ruling 16).
- `thesis.how_why`: "Its engineering publications are few and mostly from 2018 to 2021…; data-center locations, the integration plan for the acquisitions and the identity…" → "Its posts on the platform's architecture are mostly from 2018 to 2021, with later ones on partitioning (2023 to 2025) and one of 2026 that adds scale…; the cities and operators of its data centers (it names six regions), what has been integrated of the acquisitions and the identity…".
- Spec body: S3 (banking partners as a named concentration risk, the stand-in reading labeled inference; Orb dated to June 2026); S5 ("architecture posts are mostly from 2018 to 2021"); conclusion callback ("on the author's reading, true of everything Adyen sold until 30 June 2026"); two "last modified" dates → "n.d., accessed November 2026" (ruling 30); non-goal 5 no longer calls deployment frequency and failover "not public" (rulings 43b, 45a).
- Page: "merchant of record, the party that is legally the seller to the end customer and so owes the tax and answers the disputes" → "…the party that sells to the end customer in its own name, taking over the indirect tax and dispute handling" (chapter 32). The DDoS update was already dated 21 April 2025 in text and Sources.
- Placeholder `47-order-of-construction`: tick label and block position "2006" → "2006–2012" in the prompt; alt "acquiring from 2006" → "acquiring from the 2006 to 2012 period".

## 48-the-bets-compared (`stripe-and-adyen-bets-compared`; entry only)

- `know[0]`: license row adds "and, in business since 28 May 2026, a Georgia limited-purpose acquiring bank of Stripe's own" (ruling 33a); acquiring row: "partner banks elsewhere" → "other named acquirers, most of them banks, elsewhere", and adds "14 countries and regions listed as having an Adyen acquiring connection" (ruling 27); hosting row: "own data-center capacity against AWS" → "data centers whose servers Adyen manages itself, with six regions named and no cities or operators, against AWS by Stripe's 2023 statement, with no AWS region named" (rulings 42, 45); billing row: "none of its own until Orb" → "no billing product and no first-party tax engine of Adyen's own found until Orb, and Adyen's statement that it is not a merchant of record" … "a merchant-of-record product for digital goods" (rulings 38, 39; chapter 32).
- `know[1]`: "network membership per country at either company" → "the acquiring entity per country at Adyen" (ruling 27b).
- AC-1 `expected`: Orb "which runs apart for now" → "which it described in June 2026 as run under an incubator model and says it is integrating".
- AC-2 `expected` (2): Adyen's 14 listed acquiring countries and regions added; "partner banks in North America and some Asian markets" → "other named acquirers, most of them banks, …"; Georgia bank "in business since 28 May 2026". (3): "Adyen closed its first two acquisitions" → "Adyen closed two acquisitions on 1 July 2026, the only ones its history page lists". (4): adds "and names six data-center regions".
- `thesis.how_why`: "(2023, the latest of its kind)" → "(2023; a 2024 AWS post co-written by Stripe engineers is consistent with it)"; "either one's network memberships or realized prices" → "Adyen's … acquiring entity per country; either one's realized prices".
- `thesis.claim`: not changed.

## 49-contrast-cases (`payment-contrast-cases`)

- `know[1]`: "live on 9 September 2026" → "announced on 9 September 2026 (the Georgia regulator dates the bank's start of business to 16 July 2026)".
- AC-2 `expected`: "since September 2026" → "since 2026 (in business from 16 July, announced on 9 September)"; Link "over 250 million users in April 2026" + "and over 300 million in September 2026".
- `thesis.claim` (chapter claim, one clause): "in 2026 took the same narrow US acquiring charter that Stripe obtained" → "in 2026 began acquiring in the United States under the same narrow charter that Stripe obtained" (the charter was approved on 15 September 2025; business began in 2026). Rubric result: see below.
- Spec body: Link figure updated in one controlling idea and one evidence item; "licenses and partner banks per market (Stripe)" → "licenses and named acquirers per market".
- Page: no change needed.

## 50-what-is-moving (`payments-what-is-moving`)

- `know[0]`: "Adyen Agentic in limited availability" → "Adyen Agentic released in limited availability" (the product page now names no phase).
- `know[3]`: "not confirmed as published in the Official Journal on 17 November 2026, with secondary sources disagreeing on the application period" → "awaiting the European Parliament's second reading and not in the Official Journal on 17 November 2026, so with no application date yet" (ruling 33e).
- AC-1 `expected`: Adyen's product "was released in limited availability … (its product page now says only that it is available in the US)"; PSD3 sentence restated with the second-reading status.
- `thesis.how_why`: "Adyen's product is in limited availability" → "was released in limited availability"; "sells a suite on them" → "sells a suite that connects a business to several agents" (verification row 19).
- Spec body: four "last modified 2026-11-17" stamps for Adyen's Wero page → "n.d." (ruling 30); "Adyen Agentic (is) in limited availability" → "released in limited availability" (two places); "partner banks and its own entities per market" → "named acquirers and its own entities per market"; "beside partner banks" → "beside five partner banks".
- Page: no change needed.

## Chapter thesis claims changed, and the rubric

Each new thesis object was given alone to a fresh agent with the four rubric questions (does the claim answer the question; could a reasonable reader hold `disputed_by`; free of vague evaluative words; are `so_what` and `how_why` more than restatements).

- `journey-dispute`: pass on all four. Optional note, not acted on: the Stripe half names the mechanism (the charge type) but not the party that ends up carrying the loss, unlike the Adyen half.
- `case-adyen`: pass on all four. Notes, not acted on: "the phrase" in the claim has no explicit antecedent (it means "single platform"); "one place for every change" is looser than the rest.
- `payment-contrast-cases`: pass on all four. Notes, not acted on: "higher expense rates" has no comparand; "the same narrow charter" could be named (Georgia limited-purpose bank charter); the Checkout.com clause is the weakest link to the inference.

## Part-claim clauses for the author (not edited)

Part X `thesis.claim`:

1. "Adyen, founded in 2006, **started from an acquiring license** and enterprise customers". Evidence: Adyen's history page dates the acquiring license only to the period 2006–2012 (verification of 47, "For other pages" item 1). Suggested: "Adyen, founded in 2006, built on an acquiring license it obtained in its first years and on enterprise customers".
2. "on one platform it built **and hosts itself**". Evidence: the Annual Report 2025 mentions "data center partners" and lists data centers among third-party providers; Adyen's Infrastructure page says "We administer and manage all our own servers" (verification of 47, rows 1, 131). Suggested: "on one platform it built and runs on servers it manages itself".
3. "from e-money licenses, **partner banks** and, since 2025, narrow charters" and "how much volume its **partner banks** carry". Evidence: ruling 27(a): the named acquirers are not all banks (card companies in Japan, Network International in the UAE). Suggested: "named acquirers, most of them partner banks," and "how much volume each named acquirer carries".
4. No statement in the claim about what is not public was overturned: Stripe has still published neither its motives nor volume per acquirer.

Part IX `thesis.claim`: no clause found false or too strong. (Supporting claim P9-3, "a refund after payout is debited from a balance the payout already emptied", carries the same rhetorical "emptied" as chapter 44; see the note there.)

## For other scopes

- Chapters 40 and 41 already carry the press-release headline; no action.
- `part-10-intro` and chapter 48 are to be written from the corrected entries; `[[part-10]]` and `[[stripe-and-adyen-bets-compared]]` resolve only when those pages exist.
- Open point from the verification of chapter 50 stands: whether the OpenRouter and Parafin purchases have closed (the `case-stripe` entry says "not confirmed closed on 17 November 2026").

## Finish

- `validate_spec.py payments-platform-architecture`: ok for the journal spec and all 61 page specs.
- `check_draft.py structure`: passes for the nine pages (1,197; 5,117; 5,284; 5,929; 5,977; 6,394; 6,000; 3,497; 5,798 words); `timetoread` values unchanged and correct.
- Placeholder extraction parses on the nine pages; build clean for this journal.
