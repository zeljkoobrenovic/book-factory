# Verification — part-3-intro (permalink `part-3`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–37 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | A provider's knowledge rests on a double-entry ledger matched against network files and bank statements | 12, 15 | agrees | — |
| 2 | Ch. 12: balanced entries never edited; clearing accounts that must return to zero | 12 | agrees | — |
| 3 | Ch. 12: Adyen's 2021 engineering post describes refusing an unbalanced entry at the write | 12 (claims 31, 32) | agrees | Chapter: records enter only through templates proven to net to zero |
| 4 | Ch. 12: Stripe's 2024 post: many systems write into a log checked afterwards; 99.99% of dollar volume verified within four days | 12 (claim 1) | agrees | — |
| 5 | Ch. 13: a balance is the merchant's claim; pending, available, reserved are the provider's decisions | 13 | agrees | — |
| 6 | Ch. 13: Adyen documents paying whether or not the network has paid it, and takes back what has not settled within 30 days | 13; ruling 18 | agrees | — |
| 7 | Ch. 13: Stripe publishes a schedule and, for standard payouts, does not say | 13; ruling 18 | agrees | Not 'not public for both' |
| 8 | Ch. 14: 'paid' means sent; a failed transfer comes back days later as a new credit | 14 | agrees | — |
| 9 | Ch. 15: scheduled reports itemized per payout at Stripe and per payable batch at Adyen; write books from reports, not webhooks | 15; ruling 32 | agrees | The intro makes no statement about report timing |
| 10 | Ch. 16: only a licensed institution may hold customer money | 16 | agrees | — |
| 11 | Ch. 16: Stripe states it is an e-money institution in Europe and 'not a bank' in the United States; Adyen states it is a Dutch credit institution | 16; ruling 33 | agrees | — |
| 12 | Ch. 16: neither publishes which accounts hold the money | 16; ruling 33(f) | agrees | Chapter 16's key point has the same sentence; ruling 33(f) adds that deposits in Adyen business accounts are under the Dutch guarantee, which is about cover, not about which accounts hold payout balances |

Counts: 12 company, network and regulation statements checked: 12 agree, 0 corrected to match, 0 no longer in the chapter and removed.

## Other checks

- **KEY POINTS:** three, and each matches what the chapters argue. 
- **Chapter paragraphs:** each names the chapter's question (a shortened form of the `thesis.question` in the chapter's spec) and its Larkfield case. Cases: the €412,000 replayed through six accounts and one posting function (ch. 12), Mila's €120.00 as three figures (ch. 13), the Payout That Bounced (ch. 14), the close of Tuesday 9 March 2027 (ch. 15), the 14-day refund buffer (ch. 16).
- **Larkfield:** checked against the ledger: €412,000 higher at year-end 2025, three weeks, three causes; €117.47 owed to Studio Noord; 412 payouts, €386,000, June 2026, 19 days; Tuesday 9 March 2027; 14 days, about €43 million. Five Larkfield statements, all agree. The intro says 'at the end of 2025', consistent with ruling 24.
- **Links:** every `[[permalink]]` is in the style guide's valid list; no external URL in the running text (ruling 22).
- **Length and format:** 1120 words by `check_draft.py structure` (limit 1,200); `timetoread` 5 min (1120 ÷ 230); unit count and order unchanged; no spec change beyond the changelog entry.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build and render check results are in the report.

## Could not verify

Nothing.

## Ledger conflicts

None found.

## For other pages

None.
