# Verification — part-7-intro (permalink `part-7`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–45 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source. All four chapters of the part (33–36) and chapter 32 had a verification file when this page was finished.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | On Stripe the assignment is permanent per account; Stripe says of loss and fee responsibilities "You can't update their values later." | 33 | agrees | Quotation matches the chapter's |
| 2 | Adyen says of the liable balance account that funds can be deducted from it when sellers' balances go negative | 33 | agrees | — |
| 3 | A merchant of record "becomes the seller and takes its liability whole" | 32 (rows 4, 105) | corrected to match | "takes over its obligations together", the wording of chapter 32's corrected hand-off |
| 4 | "Only Stripe documents the provider as a possible loss bearer. Adyen's public pages name only the platform" | 33 (current key point), 35 (row 41), 44 (row 49); ruling 41(b) | corrected to match | Now: Stripe documents it as a standing option; Adyen's default is the platform and it documents bearing a seller's losses itself only as a pilot program |
| 5 | Adyen's pages "give no period a seller's balance may stay negative and no reserve" | 33 (rows 67, 68), 35 (row 40); ruling 41(a) | no longer in the chapter and removed | Adyen documents 30 days and reserve accounts |
| 6 | Neither company publishes how many sellers finish sign-up | 34 (rows 4, 73); ruling 40(a) | agrees | Reworded to the chapter's term, "a completion rate for seller sign-up" |
| 7 | Accounts for a platform's sellers were in preview at Stripe and in development at Adyen in November 2026, on undated pages | 36 (rows 31, 33) | agrees | — |
| 8 | Ch. 33: the merchant is whoever the customer understands they are buying from | 33 (row 7) | agrees | — |
| 9 | Ch. 33: the configuration books the payment and assigns the loss | 33 | agrees | — |
| 10 | Ch. 33: Stripe lets the loss bearer be Stripe or the platform and fixes it per account | 33 | agrees | — |
| 11 | Ch. 33: "nothing public describes Adyen bearing a seller's losses" | 33; ruling 41(b) | corrected to match | Same wording as row 4 |
| 12 | Ch. 34: verification is a state the provider reopens for the life of the account | 34; ruling 2 | agrees | — |
| 13 | Ch. 34: payouts usually stop first | 34 (row 1) | agrees | — |
| 14 | Ch. 34: Adyen's standard deadline is 30 days for payout capabilities and 60 for receiving payments | 34; 44 (row 5) | agrees | "standard" is the chapter's word |
| 15 | Ch. 34: on Stripe, who collects the data follows from who bears the losses | 34 | agrees | — |
| 16 | Ch. 35: a split is a set of bookings inside the provider, derived from the charge type on Stripe and sent as typed instructions on Adyen | 35 | agrees | — |
| 17 | Ch. 35: sellers are paid within days and a card payment can be disputed for about four months | 35 | agrees | — |
| 18 | Ch. 36: Adyen's own banking licenses; for Stripe partner banks and lenders | 36 (row 13) | agrees | — |
| 19 | Ch. 36: both providers give the platform's server two seconds for a card authorization | 36 | agrees | — |
| 20 | Ch. 36: Stripe offers accounts and cards only to platforms that bear their sellers' losses | 36 (rows 49, 65) | agrees | The chapter's key point still says so; it adds that Issuing on other account types is available on request, which concerns the dashboard, not the loss condition |
| 21 | The same assignment settles who collects verification data, where a refund after payout is booked and whether accounts and cards may be offered | 34, 35, 36 | agrees | — |
| 22 | Rulings 18, 23 and 36 | — | agrees | The page makes no statement they touch |

Counts: 22 statements checked: 18 agree, 3 corrected to match, 1 no longer in the chapter and removed.

## Re-check after chapter verification

Nothing; every chapter's verification file was read.

## Other checks

- **KEY POINTS:** three, and each matches the chapters (the loss assignment, its permanence on Stripe, one decision seen four times).
- **Chapter paragraphs:** each names the chapter's question and its Larkfield case: three answers to Mila's €84.00 (33), Ironworks Climbing's nine days in May 2026 (34), the €412,000 and its €317,200 (35), the card for Tuesday's sales that ends as "not yet" (36).
- **Larkfield:** agrees with the ledger: 18 March 2027, €84.00, seven classes, €120.00 pass, Studio Noord, €117.47, Thursday 11 March 2027 (a Thursday), about €156 million, 230 Frozen Studios, nine days, €412,000 and €317,200 at the end of 2025.
- **Links:** all six `[[permalink]]` targets are valid; "Parts I to VI" is a plain range, and `[[part-6]]` follows it.
- **Length and format:** 1,057 words (limit 1,200); `timetoread` 5 min (1,057 ÷ 230 = 4.6); unit count and order unchanged. `spec.json`: p02 and p05 evidence, p05 controlling idea and the first chapter paragraph's evidence brought into line; changelog entry added.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build clean for this journal; render check OK.

## Ledger conflicts

None found. (Chapter 34's verification records one about Ironworks's capabilities; this page does not list capabilities.)

## For other pages

- The second illustration placeholder and the "comparison stops in named places" sentence now name three places, not four.
