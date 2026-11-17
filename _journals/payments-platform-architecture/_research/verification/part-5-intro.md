# Verification — part-5-intro (permalink `part-5`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–37 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | The card industry's security standard binds every system a card number passes through or can affect | 22 | agrees | — |
| 2 | Stripe's documentation: the merchant is "ultimately responsible for payments you choose to accept" | 24 (claim 47) | agrees | Fragment matches the chapter's quotation |
| 3 | European law puts the loss on the side that avoids strong authentication | 25 (claim 38, PSD2 Art. 74(2)) | agrees | — |
| 4 | 'Stripe makes its fraud tool available only when its own client-side code collects the card' | 22 (claims 59, 60) | corrected to match | The sentence is exact in Stripe's PCI guide, but chapter 22 was hedged: Stripe's API reference says only that Radar 'performs best' with such integrations. The intro now attributes the rule to Stripe's PCI guide |
| 5 | Neither publishes a vault design | 22 | agrees | — |
| 6 | Adyen's fraud-risk model is not public | 24 | agrees | — |
| 7 | Neither company says how it monitors transactions | 26 | agrees | Ruling 36 not contradicted: the intro does not say re-verification is not public |
| 8 | The gains reported for network tokens are the vendors' own comparisons | 23; ruling 35(c) | agrees | — |
| 9 | Ch. 22: a provider-served frame, a token and an isolated vault; Stripe documents a vault that shares no credentials with its other services; Adyen publishes less | 22 | agrees | — |
| 10 | Ch. 23: a network token is a substitute card number the network keeps pointing at the current card | 23 | agrees | — |
| 11 | Ch. 23: Visa says six basis points, Adyen 3%, Stripe 3.8% for a bundle; not comparable | 23; ruling 35(c) | agrees | — |
| 12 | Ch. 24: the provider estimates the chance of a later fraud dispute and blocks above a threshold | 24 | agrees | — |
| 13 | Ch. 24: Stripe's 2026 figures: 41% of fraud disputes reported by day 14 and 86% by day 60 | 24 (claim 33) | agrees | The chapter notes the words are the description of Stripe's chart |
| 14 | Ch. 25: the loss moves to the bank only when authentication happens; a requested exemption or a merchant-initiated renewal leaves it with the merchant | 25 | agrees | — |
| 15 | Ch. 26: both providers hold verification as requirements with deadlines that switch payouts on and off | 26; ruling 2 | agrees | — |

Counts: 15 company, network and regulation statements checked: 14 agree, 1 corrected to match, 0 no longer in the chapter and removed.

## Other checks

- **KEY POINTS:** three, and each matches what the chapters argue. 
- **Chapter paragraphs:** each names the chapter's question (a shortened form of the `thesis.question` in the chapter's spec) and its Larkfield case. Cases: the 17 scripts and the SAQ A script line (ch. 22), Lotte Smit's renewal (ch. 23), the Card-Testing Weekend (ch. 24), Bram de Wit's pass (ch. 25), the Frozen Studios and K6 (ch. 26).
- **Larkfield:** checked against the ledger: Card-Testing Weekend 8–9 August 2026 (a Saturday and Sunday), 61,000 numbers, €1 drop-ins, one studio's booking widget, €4,100 in fees and refunds, 31 hours; January 2027, 17 third-party scripts; Lotte Smit, €49.00, renewal 1 March 2027, card replaced in February; Bram de Wit, €120.00, unchallenged, €135.00; May 2026, 230 studios, up to 12 days, K6 'verification is state, not a form'. Six Larkfield statements, all agree.
- **Links:** every `[[permalink]]` is in the style guide's valid list; no external URL in the running text (ruling 22).
- **Length and format:** 1065 words by `check_draft.py structure` (limit 1,200); `timetoread` 5 min (1065 ÷ 230); unit count and order unchanged; no spec change beyond the changelog entry.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build and render check results are in the report.

## Could not verify

Nothing.

## Ledger conflicts

None found.

## For other pages

None.
