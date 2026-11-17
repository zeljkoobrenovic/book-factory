# Verification — part-1-intro (permalink `part-1`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–37 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Visa's public rules, edition of 24 October 2026: 120 calendar days for most kinds of dispute | 01 (claim 31), 04 (claim 2) | agrees | — |
| 2 | The issuer approves in seconds and moves no money; settlement a day or more later, as net amounts between banks; provider pays on its own schedule | 01, 02, 03 | agrees | Ruling 18 respected: payout 'on its own schedule', not 'after settlement' |
| 3 | Key point: the cardholder can dispute for about 120 days | 01, 04 | agrees | — |
| 4 | Ch. 1: six steps, at least five parties; message, then record, then money; the provider controls none of the three steps that decide the outcome | 01 | agrees | — |
| 5 | Ch. 1: acquirer = institution that accepts card payments on the merchant's behalf; first question: which legal entity is the acquirer in this country | 01 | agrees | — |
| 6 | Ch. 2: the promise is the issuer's, for up to an approved amount inside a window 'that Visa's rules set at 5 to 30 days' | 02 (claim 52, hedged) | corrected to match | Chapter 2 now says '5 to 30 days in Visa's general table' (Table 5-12 has country windows from 1 day). Intro now reads 'that Visa's general table sets at 5 to 30 days' |
| 7 | Ch. 2: an authorization moves no money and can lapse; no answer = unknown outcome, not a failed one | 02 | agrees | — |
| 8 | Ch. 3: capture is a claim; acquirer presents a clearing record; network moves one net amount per member bank per day; provider pays on its own schedule; 'settled' names three events | 03 | agrees | — |
| 9 | Ch. 3: Stripe counts its settlement timing from the capture | 03 (claims 48, 71) | agrees | — |
| 10 | Ch. 3: Adyen pays a whole sales day on a fixed delay whether or not it has received the funds (terms of 17 June 2024) | 03 (claim 54); ruling 18 | agrees | — |
| 11 | Ch. 4: three routes (cancel or reversal, refund that can fail, dispute with one answer for the merchant) | 04 | agrees | — |
| 12 | Ch. 4: Visa gives 120 days for most disputes and up to 540 where a service is delivered later | 04 (claims 2, 4) | agrees | — |
| 13 | Ch. 5: the fee is three payments: interchange, scheme fees, markup | 05 | agrees | — |
| 14 | Ch. 5: EU law caps only interchange, 0.2% consumer debit and 0.3% consumer credit | 05 | agrees | — |
| 15 | Ch. 5: as of November 2026 Stripe's published standard price blends the three; Adyen's passes interchange and scheme fees through at cost | 05 | agrees | — |

Counts: 15 company, network and regulation statements checked: 14 agree, 1 corrected to match, 0 no longer in the chapter and removed.

## Other checks

- **KEY POINTS:** three, and each matches what the chapters argue. Key point 1 says money moves 'a day or more later, as net amounts between banks', as chapters 1 and 3 do.
- **Chapter paragraphs:** each names the chapter's question (a shortened form of the `thesis.question` in the chapter's spec) and its Larkfield case. Cases: Mila's pass (ch. 1), the Double Charge (ch. 2), Wednesday 10 March 2027 (ch. 3), Bram's €120 (ch. 4), the fee on Mila's €120 (ch. 5).
- **Larkfield:** checked against the ledger: Bram de Wit, 2 February 2027, €120.00, chargeback 24 February, €15.00 fee (illustrative), window to 2 June 2027; Mila's pass Tuesday 9 March 2027 19:42, paid out Thursday 11 March, 'It says paid. Paid to whom?', €117.47, €2.53 = €0.24 + €0.06 + €0.31 + Larkfield's €1.92 (the intro lists the three provider-cost parts as shares of the €2.53 fee); Double Charge 1 November 2026, 1,840 members, €71,300. Weekdays match dates. Nine Larkfield statements, all agree.
- **Links:** every `[[permalink]]` is in the style guide's valid list; no external URL in the running text (ruling 22).
- **Length and format:** 1197 words by `check_draft.py structure` (limit 1,200); `timetoread` 5 min (1197 ÷ 230); unit count and order unchanged; no spec change beyond the changelog entry.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build and render check results are in the report.

## Could not verify

Nothing. The intro's sentence that the Double Charge job 'read a timeout as a refusal' is chapter 2's account; the ledger says only that it retried under a new key. They do not conflict.

## Ledger conflicts

None found.

## For other pages

None.
