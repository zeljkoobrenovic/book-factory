# Sweep — second half (Parts VI–IX, chapters 27–47, 49, 50)

Sweep of 24 November 2026 for rulings 41–48. Pages checked: `part-6-intro` … `part-9-intro`, chapters 27–47, 49, 50 (prose, tables, evidence-stops sections, take-aways, captions, Sources notes, page specs, journal entries). Not touched: `48-the-bets-compared`, `part-10-intro`. No new research; every replacement uses the owning chapter's wording and Sources entry.

## Prose changes

| Page | Was | Now | Ruling |
| --- | --- | --- | --- |
| 42-journey-card-payment, step 7 | "No page I found lists the acquiring entity per country." | Adyen's license pages name an acquiring entity for some markets, Japan and Singapore among them; no page found gives a complete list per country. | 46j (owner ch. 6) |
| 42-journey-card-payment, evidence paragraph | "I found nothing in Stripe's documentation … they do not say whether funds become available before Stripe has received them." | The capture gap is kept. For standard payouts: Stripe's services terms (last modified 28 September 2026) count "a delay or failure of a Financial Provider to settle a Transaction to Stripe" as a "Payout Delay"; whether funds otherwise become available before Stripe's receipt is stated in neither the terms, the documentation nor the support site. | 47e (owner ch. 3, 13) |
| 42-journey-card-payment, same paragraph | Adyen's Sales Day Payout terms quoted without caveat | Adds: the Annual Report 2025 calls paying "only after funds have been received" the "default setup", and public text does not reconcile the two. | 47m (owner ch. 13, 47) |
| 42-journey-card-payment, Sources | "no acquiring entity named per country" | "no list of acquiring entities per country"; three entries added (Adyen license pages for Japan and Singapore; Annual Report 2025; Stripe Services Terms). | 46j, 47e, 47m |
| 34-platform-onboarding-and-verification, table row "Deadlines and what stops first" | "One deadline per account, no standard length published" | One deadline per account; for updated requirements on Custom accounts, "typically" 14 days to keep payouts and 28 to keep payments (support article). | 48g (owner ch. 26) |
| 34, paragraph after the table | "since no standard length is published" | "since its typical periods are not fixed"; two connective phrases trimmed for length ("One row is new here."; "while remembering they can be shortened" → "which can be shortened"). Source added: Stripe support, "Custom connected account onboarding requirements". | 48g |
| 37-payment-reliability | "For Stripe I found no statement on failover between data centers or regions" | "… on failover of the payment path between data centers or regions" (the table already said "for payments"). | 46g |
| 41-safe-change, take-away | "What neither has documented, its regions, failover, cells and replication settings" | "… the topology and timing of a failover, cells and which data is replicated synchronously" (Adyen names regions and states failover in general terms). | 45a, 46g |
| 47-case-adyen, Where the Evidence Stops | Bullet "Where merchants' funds are held." | Retitled "Which banks hold merchants' funds." (the terms state the holder and the documentation a country per settlement currency; the banks are unnamed). | 47g (owner ch. 16) |
| part-9-intro | "Adyen publishes no chargeback fee" | "Adyen's chargeback fee is set by contract" | 46f (owner ch. 45) |

## Page-spec units aligned (changelog line of 2026-11-24 in each)

- 42: p28 controlling idea and evidence (Payout Delay; Annual Report caveat).
- 34: p29 evidence (typical 14 and 28 days).
- 37: p20 controlling idea (Stripe: nothing for the payment path; billing usage events only).
- 41: conclusion synthesis and p37 evidence (topology and timing, cells, synchronous replication).
- 47: p31 evidence (weekly core releases are stated; no deploy count comparable to Stripe's, 46e); p37 (which banks hold funds).
- part-9-intro: p05 controlling idea and evidence (fee contractual; CAD 24.00).
- 32: p22 evidence no longer says Apple's agreement is not publicly readable (46c; prose was already right).
- part-8-intro: p04 evidence scoped to Stripe's payment path (46g; prose unchanged).
- 29: supporting claim C5 and one evidence note (one engineering post each on the retry model, 46a; prose was already right).

## Journal-entry sentences corrected

| Entry | Field | Was → now | Ruling |
| --- | --- | --- | --- |
| invoicing-collections-and-dunning | thesis.how_why | "The public record stops at the retry logic: Stripe names two example signals … Adyen says only 'smart logic' and 'optimal times'." → one engineering post each (Stripe 23 January 2024, "more than 500 attributes"; Adyen 3 December 2020, contextual bandit, "about 6% more orders than the baseline"); neither publishes the model now running or the timing for a given decline. | 46a |
| splits-balances-and-platform-payouts | thesis.how_why | "How either company stores and keeps these bookings consistent internally is not public." → each has published a general account of its ledger; how platform splits and transfers are booked in it is not public. | 46i / audit of ch. 35 |
| payment-multi-region-and-data-residency | thesis.how_why | "Stripe has published no statement on takeover." → "… no statement on takeover for payments, only a two-region design with failover for billing usage events (2025)." | 46g |
| journey-card-payment | thesis.how_why | "… nothing on whether its own receipt of funds comes first." → services terms count a network's failure to settle to Stripe as a "Payout Delay" and do not say whether its own receipt otherwise comes first. | 47e |
| journey-dispute | intent.outcome.know | "Adyen's chargeback fee is not published" → amount contractual, only CAD 24.00 published (Adyen Canada's fee disclosure). | 46f |
| journey-dispute | thesis.how_why | "Adyen does not publish its chargeback fee" → terms (clause 8.2) call the fee non-refundable and leave the amount to the merchant agreement. | 46f |
| part-8 (part level, edited in `journal-spec-parts/part-8.json`; mirrored in `part-8-intro/spec.json`) | thesis.how_why | "Stripe names no AWS region and says nothing on takeover" → "… and describes takeover only for billing usage events, not for payments". | 46g |

No chapter thesis `claim` was changed.

## Part or journal thesis clauses to review (not changed)

- Part VIII claim: "neither has published … the topology or timing of a failover between its data centers or regions". Stripe's blog post of 28 January 2025 describes a two-region design with automatic failover for billing usage events (ruling 46g). Suggested: "… of a failover of its payment path between its data centers or regions".

## Checked and found already in line (no change)

Chapters 33, 35, 46, 47, 49 on Stripe payouts (47e), Adyen report timing (47f) and Uplift (47c): no statement of these absences on the pages. Chapters 37, 40, 47 on Adyen fraud-model facts (48e) and chapters 33, 35 on Stripe reserve factors (48e): no such absence on the pages. Chapter 44: acquiring entities, payout terms and pre-financing are not asserted beyond Adyen's quoted documentation. Chapter 45 prose (46f), 29 and 43 prose (46a), 31 (46b), 32 prose (46c), 33 (46d), 41 and 47 prose (46e), 37, 39 and part-8-intro prose (46g, 46h), 38 and 46 (46i), 47 (46j, 47m), 49 (46k), 40 (ruling 42), 41 (ruling 43), 33 (rulings 41, 44).

## For the sessions holding chapter 48 and part-10-intro

- 48, license row: where it quotes Adyen's Sales Day Payout terms and says Stripe documents paying ahead only for Instant Payouts, add the Annual Report 2025 "default setup" caveat (47m) and the services terms' "Payout Delay" (47e), as chapters 13 and 42 now do.
- 48, acquiring row: "Neither lists its card-network memberships per country" should sit beside "Adyen's license pages name an acquiring entity for some markets" (46j) if it does not already.
- 48, platforms row: if Stripe's verification deadline is mentioned, use "typically 14 days for payouts and 28 for payments on Custom accounts" (48g), as chapter 34 now does.
- part-10 thesis how_why has a missing connective: "Adyen lists the countries and regions where it has an acquiring connection names its acquiring entity for some markets" (an "and" or comma is missing).

## Left open

- The check reports of the pages edited here (29, 32, 34, 35, 37, 39, 41, 42, 45, 47, part-8-intro, part-9-intro) are stale by content hash; `check_draft.py structure` passes for all 27 assigned pages, and the reader checks were not rerun.
