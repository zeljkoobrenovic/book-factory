# Verification — part-9-intro (permalink `part-9`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–45 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source. All four journeys (42–45) had a verification file when this page was finished; 44 and 45 appeared during the pass.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe gives objects whose status can be read again; Adyen gives events and report lines keyed by a reference (KEY POINT 3, lead) | 42, 45 | agrees | — |
| 2 | A payment's record stays open until the dispute window closes, not the payout (KEY POINT 2) | 42 | agrees | — |
| 3 | Clocks run from seconds for an approval to about four months for a chargeback | 42, 45 | agrees | — |
| 4 | The records are from the two providers' documentation as read in November 2026 | 42–45 | agrees | — |
| 5 | The pairing of the two vocabularies is the book's own; neither company publishes one | 45 | agrees | — |
| 6 | The timing of clearing and settlement between banks is industry practice, not a cited rule | 42 | agrees | — |
| 7 | Mastercard's rule documents could not be read | 45 (row 80); ruling 17 | agrees | — |
| 8 | Adyen publishes no chargeback fee, so the €15 is an illustration | 45 | agrees | The chapter: "A fee per booked chargeback; amount not public" |
| 9 | J. 42: twelve steps, eleven ending in a promise; "Payment successful" reports the fifth; the twelfth establishes that €117.47 arrived | 42 | agrees | — |
| 10 | J. 42: on Stripe the payment is an object that can be read again | 42 | agrees | — |
| 11 | J. 42: Adyen's Checkout API has no call that returns a payment | 42 (row 41); rulings 12, 29 | agrees | Already scoped to the Checkout API |
| 12 | J. 42: a capture Adyen reported as successful can fail days later | 42 | agrees | — |
| 13 | J. 43: a declined renewal is an open debt with a clock | 43 | agrees | — |
| 14 | J. 43: the decline code decides whether a retry is allowed | 43 (row 22) | agrees | — |
| 15 | J. 43: Visa's rules of 24 October 2026 cap the number of retries | 43; rulings 19, 44 | agrees | "Visa's rules" is the wording ruling 44 allows |
| 16 | J. 43: no payment record says what the member is in between | 43 | agrees | — |
| 17 | J. 43: Stripe Billing retries an invoice it holds | 43; ruling 6 | agrees | — |
| 18 | J. 43: on Adyen the provider can retry a payment; the schedule, the membership state and the notice are Larkfield's | 43 (rows 25, 26) | agrees | — |
| 19 | J. 44: an instruction attached to the payment divides it | 44 | agrees | — |
| 20 | J. 44: the refund is debited from a balance the payout had emptied | 44 | agrees | — |
| 21 | J. 44: on Adyen the platform's own balance account stands behind the studio's | 44 (rows 49, 50); ruling 41 | agrees | The default, and Larkfield's case; the pilot in which Adyen bears the loss is in the chapter |
| 22 | J. 44: on Stripe the charge type decides whose balance is debited first | 44 (rows 44, 47) | agrees | — |
| 23 | J. 45: the merchant side answers once, within the 40 days Adyen gives for a Mastercard | 45 | agrees | — |
| 24 | J. 45: the amount and fee leave the balance before anyone has read evidence | 45 | agrees | — |
| 25 | J. 45: the card network counts the dispute either way | 45 (row 59) | agrees | — |
| 26 | J. 45: who paid had been decided at the sale | 45 | agrees | — |

Counts: 26 statements checked: 26 agree, 0 corrected, 0 removed. The page's text was not changed.

## Re-check after chapter verification

Nothing remains. Rows 19–26 were first checked against the unverified text of journeys 44 and 45 and checked again when their files appeared; nothing changed.

## Other checks

- **KEY POINTS:** three, and each matches the journeys.
- **Chapter paragraphs:** each names the journey's question and its payment: Mila's pass (42), her renewal (43), the split and the €84 refund (44), Bram de Wit's dispute (45).
- **Larkfield:** agrees with the ledger: €412,000 at year-end 2025, found January 2026, three weeks, three causes; 19:42 on Tuesday 9 March 2027 (a Tuesday); Thursday 11 March (a Thursday); €117.47, €2.53, €0.61 *(illustrative)*; €49, 1 and 4 April 2027; 18 March, €84; 2 February 2027 (five weeks before 9 March), 24 February, 5 March, 12 May, €15 *(illustrative)*, won; Studio Noord a yoga studio on Adyen; twelve steps.
- **Links:** all six `[[permalink]]` targets are valid; "Parts I to VIII" is a plain range followed by `[[part-8]]`.
- **Length and format:** 1,197 words (limit 1,200); `timetoread` 5 min (1,197 ÷ 230); nothing changed in `spec.json` but the changelog.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build clean for this journal; render check OK.

## Ledger conflicts

None found.
