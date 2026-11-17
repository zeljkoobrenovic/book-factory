# Verification — part-4-intro (permalink `part-4`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–37 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe's API v1 keeps a key for at least 24 hours; Adyen for 7 to 14 days (documentation read November 2026) | 18 (claims 13, 52); ruling 13 | agrees | Stated twice in the intro |
| 2 | Stripe retries an undelivered event for up to three days; Adyen for up to 30 days (in a queue) | 20 (claims 1, 15) | agrees | Stated twice in the intro |
| 3 | Each chapter says where the public record of implementation stops: 'most of it is Stripe engineering posts from 2017' | 17, 18, 19, 20, 21 | corrected to match | Chapters 18, 19 and 21 rest on Stripe posts of 2017, but chapter 17 also cites 2020 and 2026 Stripe material and a 2022 Adyen post, chapter 18 a 2021 Adyen post, and chapter 20 found no post at all. 'most' weakened to 'much' |
| 4 | Ch. 17: stable identifier, normalized vocabulary of states and refusal reasons, explicit line between response and what arrives later | 17 | agrees | — |
| 5 | Ch. 17: Stripe returns objects you can fetch again; Adyen's Checkout API returns a reference and a result code and has no call that returns a payment | 17; rulings 1, 12, 29 | agrees | Scoped to the Checkout API |
| 6 | Ch. 18: same key both times, derived from the business event and stored before the first attempt | 18 | agrees | — |
| 7 | Ch. 19: Stripe pins one dated version by account default, header or library release; two named breaking releases a year since October 2024 | 19 (claim 1) | agrees | — |
| 8 | Ch. 19: Adyen puts a number in each API's URL and gives a deprecated Checkout API version two years before end-of-life | 19 (claim 2) | agrees | — |
| 9 | Ch. 20: the confirming record is the payment object at Stripe and the settlement report at Adyen | 20; ruling 12 | agrees | — |
| 10 | Ch. 21: Stripe documents 100 requests a second per account in live mode and 25 per endpoint | 21 (claim 1) | agrees | — |
| 11 | Ch. 21: Adyen publishes no rate limit for its payments APIs | 21 (claim 2) | agrees | — |
| 12 | Ch. 21 case: refusals for volume were recorded as failed payments and 7,900 members got an email | 21, 29; ruling 37(a) | corrected to match | The intro gave only the first of the two steps. A link to [[invoicing-collections-and-dunning]], which owns the second, was added, as chapter 21 itself does |

Counts: 12 company, network and regulation statements checked: 10 agree, 2 corrected to match, 0 no longer in the chapter and removed.

## Other checks

- **KEY POINTS:** three, and each matches what the chapters argue. 
- **Chapter paragraphs:** each names the chapter's question (a shortened form of the `thesis.question` in the chapter's spec) and its Larkfield case. Cases: 'get payment' (ch. 17), the Double Charge (ch. 18), the Version Cliff (ch. 19), the Silent Webhook (ch. 20), the Renewal Wave (ch. 21).
- **Larkfield:** checked against the ledger: 'four of the eight incidents … happened in 2026' (ruling 24 respected); Version Cliff March 2026, reports wrong for 6 days, more than three years of changes in one step; Silent Webhook on Monday 14 September 2026, certificate expired shortly after midnight, 9 hours, 3,200 memberships, members that morning (ruling 20; no Saturday or Sunday); Renewal Wave 1 October 2026, 7,900 renewals delayed to the next day; Double Charge 1 November 2026, new idempotency key, 1,840 members, €71,300; 'get payment' never asked either provider. Ten Larkfield statements, all agree.
- **Links:** every `[[permalink]]` is in the style guide's valid list; no external URL in the running text (ruling 22).
- **Length and format:** 1188 words by `check_draft.py structure` (limit 1,200); `timetoread` 5 min (1188 ÷ 230); unit count and order unchanged; no spec change beyond the changelog entry.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build and render check results are in the report.

## Could not verify

Nothing.

## Ledger conflicts

None found.

## For other pages

None.
