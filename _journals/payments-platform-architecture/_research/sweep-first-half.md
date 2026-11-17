# Sweep — first half (preface pages, Parts I–V intros, chapters 01–26)

Sweep of 24 November 2026 for rulings 41–48. No new research: every replacement follows the owning chapter's current text. `introduction` and `how-payments-got-complicated` were not touched.

## Prose changes

| Page | Was | Now | Ruling |
| --- | --- | --- | --- |
| where-payment-systems-go-wrong | "started at one of the other twelve" (key point, chains section; spec thesis, supporting claim, units) | "the other eleven" (16 patterns less 5 money-truth) | coordinator's count fix |
| part-2-intro | "neither publishes its network membership class per country" | "neither lists its network memberships by network and country" | 46j, 47j |
| part-3-intro | "Neither publishes which accounts hold the money." | "Neither names the banks that hold the money." | 47g |
| 09 authorization-optimization | Retry paragraph went straight to "Neither publishes a recovery rate across merchants" | One sentence added before it: each has one post on its retry model (Stripe 23 January 2024, "more than 500 attributes"; Adyen 3 December 2020, "about 6% more orders than the baseline" in one experiment); two Sources entries copied from chapter 29 | 46a |
| 10 routing-and-orchestration | Key point: "No Stripe or Adyen page I read says whether network tokens survive a move." | Adyen's terms (2025) describe a service that shares them, cryptogram still from Adyen; no Stripe statement | 48d |
| 10 | "Here the public record stops … Neither company documents whether the network tokens it provisioned move with an export" | "Here the public record is thin …" plus Adyen's Network Token Sharing Service (Additional Services Terms, 13 June 2025) and the cryptogram; no Stripe statement; requestor identifier still undocumented | 48d |
| 10 | Inference block: "No document from Stripe, Adyen or a card network … confirms or denies this." | "unless a sharing service such as Adyen's was enabled"; "No document from Stripe or a card network" | 48d |
| 10 | Sources | Additional Services Terms entry copied from chapter 23 | 48d |
| 13 balances-and-funds-flows | Excerpt: "Stripe does not say." | "Stripe's documentation does not say." | 47e |
| 13 | Key point: "does not say whether that schedule waits for the network." | adds "beyond terms that let a payout wait when a network fails to pay Stripe" | 47e |
| 16 licences-and-safeguarding | Key point: "Neither publishes which accounts hold the money." | "Neither names the banks that hold the money." | 47g |
| 22 tokenization-vaulting-and-pci | "Neither company's export pages say whether network tokens travel; the next chapter takes that up." | adds "Adyen's terms (2025) describe a service that shares them"; Sources entry added; one connective sentence trimmed ("Now the choice in front of an integrator can be read.") to stay within 6,500 words | 48d |

Spec units aligned on each of these pages (controlling ideas, evidence, open question), with one changelog line dated 2026-11-24.

## Journal-spec entries corrected (also in each page's spec.json)

| Entry | Field | Was | Now | Ruling |
| --- | --- | --- | --- | --- |
| where-payment-systems-go-wrong | thesis claim | "one of the other twelve" | "one of the other eleven" | count fix |
| journey-of-a-payment | thesis how_why | "without naming the acquiring entity in each" | "and names the acquiring entity for some markets only" | 46j |
| refunds-reversals-and-disputes | AC-3 | "Adyen's dispute fee is stated as not public" | "stated as set by contract, with the one amount on its site (CAD 24.00, in Adyen Canada's fee disclosure) named" | 46f |
| refunds-reversals-and-disputes | thesis how_why | "Adyen's dispute fee is not public" | "set by contract (the one amount on its site is CAD 24.00 …)" | 46f |
| part-2 (part level, `part-2.json`) | thesis how_why | "network membership class per country" | "a list of its network memberships by network and country" | 46j, 47j |
| acquiring-and-network-connectivity | intent know, thesis how_why (and spec supporting claim) | "membership class per country" | "a list of (its) network memberships by network and country" | 46j, 47j |
| payment-state-machines | thesis how_why | "reasons for result codes and asynchronous modifications are not on record" | July 2021 post gives the reason for asynchronous modifications; result codes not on record | 47b, 48a |
| payment-routing-and-orchestration | thesis how_why | "No Stripe or Adyen page read says whether network tokens survive a move" | Adyen's terms (13 June 2025) describe a sharing service; no Stripe statement found | 48d |
| balances-and-funds-flows | intent know | "Stripe publishes nothing on whether it does so" | documentation does not say; terms (28 September 2026) let a payout wait | 47e |
| balances-and-funds-flows | thesis claim | "…does not say whether it waits for the network." | "…, beyond terms that let a payout wait when a network fails to pay Stripe." | 47e |
| balances-and-funds-flows | thesis how_why (and spec supporting claim 3) | "for standard payouts, not public for Stripe" | "not stated by Stripe beyond terms (28 September 2026) that let it delay a payout …" | 47e |
| payment-reconciliation-and-reporting | thesis how_why | "a daily window for scheduled reports but no duration from batch close" | "within 3 hours after the batch closes" plus the daily window | 47f |
| payment-reconciliation-and-reporting | AC-2 expected | "but not how long after batch close a report is ready" | "says to expect it within 3 hours after the batch closes" | 47f |
| licences-and-safeguarding | intent know | "where Adyen holds merchant funds" | "which banks hold the balances Adyen keeps before payout" | 47g |
| licences-and-safeguarding | thesis claim | "it does not publish where merchant funds sit" | "it says merchant balances are held by Adyen before settlement, in a country documented per settlement currency, without naming the banks" | 47g |
| licences-and-safeguarding | thesis how_why | "they do not say where merchant funds sit" | terms and documentation: held by Adyen, country per currency, no bank named | 47g |
| network-tokens | thesis how_why (and spec supporting claim) | "not answered in the public record" | answered for Adyen only (terms, 13 June 2025); no Stripe statement | 48d |
| payment-fraud-and-risk | intent know | "its bot-attack model (2026)" | adds fraud models: tree-based ensembles, weekly retraining (2024) | 48e |
| payment-fraud-and-risk | AC-3 | "Adyen's fraud-risk model … and the retraining interval of Radar are not public" | not public: Adyen's model beyond family and weekly retraining; Radar's current interval (daily in a 2019 post) | 48e |
| payment-fraud-and-risk | thesis how_why (and spec supporting claim) | "Adyen has described only its bot-attack feature pipeline"; "Adyen publishes no latency figure" | adds the 2024 model family and retraining; 20 ms median / 100 ms p99 per model endpoint (2025), no whole-decision figure | 48e |
| three-d-secure-and-sca | thesis how_why | "and no selection among methods" | product page and Sessions 2026 talk describe an engine that selects the pathway; documentation does not | 48f |

## Chapter thesis claims changed

- **where-payment-systems-go-wrong**: "twelve" → "eleven".
- **balances-and-funds-flows**: clause added, "beyond terms that let a payout wait when a network fails to pay Stripe".
- **licences-and-safeguarding**: "it does not publish where merchant funds sit" → "it says merchant balances are held by Adyen before settlement, in a country documented per settlement currency, without naming the banks".

## Checked and left

- Vault Hostage (patterns page): the entry makes no statement about network tokens or about what providers publish; nothing stale.
- part-5-intro: "Adyen has published little about its fraud-risk model" was already narrowed by its own audit and agrees with chapter 24.
- Chapter 8 prose and table already carry the 2021 reason; only the journal entry was stale.
- Chapters 3, 11, 17–21, 26: locked sentences remain true as worded (per their audits).
- Adyen pre-financing caveat (47m): non-owner pages (part-1-intro, part-3-intro, chapters 1, 3, 15, 16) attribute the statement to the Sales Day Payout terms and do not go beyond chapter 13; the Annual Report caveat is not repeated there.
- Chapter 24 names only Stripe on who is left with a seller's negative balance; it does not say "only Stripe", and the page is 4 words under its limit, so Adyen's pilot (ruling 41b) was not added.
- Chapter 22 read top to bottom against spec.json after its restoration: 41 paragraph units, 4 illustration placeholders, tables, front matter and Sources present and in order; nothing missing or garbled.

## Part-level clauses to review (not changed)

- Preface part thesis claim and Part III intent ("what the public record does not say about where either holds customer funds"): still true of the banks; Adyen now documents holder and country (47g).

## Verification

`validate_spec.py payments-platform-architecture`: all ok. `check_draft.py structure`: pass on every edited page. Build: `[built] payments-platform-architecture` (the four pre-existing "missing post" warnings for reference pages remain). Check reports of the edited pages are now stale and need a re-check.
