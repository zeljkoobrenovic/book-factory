# Verification — part-2-intro (permalink `part-2`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–37 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Opening: 'by the two providers' public pages' the online request comes from an Irish e-money institution and the counter request from a Dutch bank | 06; ruling 27(b); ledger line 01 | corrected to match | Stripe's disclosure names Stripe Technology Europe, Ltd.; Adyen names no acquiring entity per country, and chapter 6 gives Adyen N.V. as the author's reading of its license page. Intro now says 'by Stripe's public pages … and by my reading of Adyen's license page' |
| 2 | Neither publishes its network membership class per country or its volume per acquirer | 06 | agrees | — |
| 3 | Approval gains for the optimization products are each company's own figures, on different metrics, audited by no third party | 09 | agrees | Ruling 31(d) not contradicted: the intro does not say Adyen published nothing since its pilot |
| 4 | Ch. 6: a network membership only a licensed entity can hold; an acquirer of record that differs by country | 06 | agrees | — |
| 5 | Ch. 6: Adyen holds one banking license (2017) extended by branches | 06 (claims 41, 42) | agrees | — |
| 6 | Ch. 6: Stripe names its own e-money institutions as acquirer in the EEA and the UK, 'and banks in the United States' | 06; rulings 27(a), 33(b) | corrected to match | Now 'five banks plus a limited-purpose bank of its own in the United States', as chapter 6's key point says |
| 7 | Ch. 7: an iDEAL payment cannot be disputed through the payer's bank; a SEPA direct debit can be refunded without a reason for eight weeks | 07 | agrees | — |
| 8 | Ch. 8: Stripe's PaymentIntent (2018) can be retrieved; Adyen's Checkout API has no endpoint that returns a payment by its identifier | 08; rulings 12, 29 | agrees | Scoped to the Checkout API as ruling 29 requires |
| 9 | Ch. 9: both providers document reformatting, retrying and blocking inside the authorization call | 09 | agrees | — |
| 10 | Ch. 10: a routing layer unifies the authorization request and nothing after it; disputes, settlement, balances and stored cards stay one set per provider | 10 | agrees | — |
| 11 | Ch. 11: a payment stored offline is credit the merchant extends; Stripe and Adyen both document that the loss is the merchant's | 11 | agrees | — |
| 12 | Ch. 11: 'one payment across channels' is three properties | 11 | agrees | Labeled in the chapter as the author's judgement; the intro states it as the chapter's argument |

Counts: 12 company, network and regulation statements checked: 10 agree, 2 corrected to match, 0 no longer in the chapter and removed.

## Other checks

- **KEY POINTS:** three, and each matches what the chapters argue. Key point 3 (a rate cannot be compared until acquirer, method mix, metric and denominator are equal) is chapter 9's argument.
- **Chapter paragraphs:** each names the chapter's question (a shortened form of the `thesis.question` in the chapter's spec) and its Larkfield case. Cases: the acquirer inventory with four arrangements (ch. 6), direct debits at 21% treated like cards (ch. 7), Mila's set-up of 12 January 2027 (ch. 8), the two December rates (ch. 9), K8 and no orchestration product (ch. 10), the counter refund at a split studio (ch. 11).
- **Larkfield:** checked against the ledger: 1,140 split studios in NL and DE (Stripe online, Adyen terminals); four acquiring arrangements; SEPA Direct Debit 21% of online volume; 12 January 2027 set-up with a challenge in the banking app; 82.0% and 95.5% (illustrative), 13.5 points to 0.8 at the first attempt; routing rule 'the studio's provider', K8, no orchestration product. Ten Larkfield statements, all agree.
- **Links:** every `[[permalink]]` is in the style guide's valid list; no external URL in the running text (ruling 22).
- **Length and format:** 1118 words by `check_draft.py structure` (limit 1,200); `timetoread` 5 min (1118 ÷ 230); unit count and order unchanged; no spec change beyond the changelog entry.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build and render check results are in the report.

## Could not verify

Nothing.

## Ledger conflicts

None found.

## For other pages

None.
