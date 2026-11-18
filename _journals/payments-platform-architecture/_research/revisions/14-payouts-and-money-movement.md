# Revision after draft check, round 1 — 14-payouts-and-money-movement

Date: 2026-11-17. Report judged: round 1, 19 failed results (12 major, 7 minor). One line per failed result. Words (structure count): 5,549 before, 5,827 after (`max_words` 6,500, unchanged). `timetoread` 24 to 25.

## transition_expresses_declared_relationship

- Designs ¶1 (p32): fixed. The section opens "The payee check is the control before the money leaves; once it has left, what remains is how to record the payout."

## known_before_new

- Global Payouts and `posted` used before introduced (p11): fixed. Glossed at first use (Stripe's product for paying third parties who are not merchants on Stripe; `posted` is its status after sending); p20 now says "met above".
- Adyen priority used before introduced (p14): fixed. One sentence at first use: an Adyen sender picks a priority per transfer (`regular`, `instant`, `crossBorder`) and Adyen maps it to a route.

## flow_is_followable (major)

- Introduction ¶2, HTTP 200 sentence: fixed. Now says which question "paid" answers ("has the provider sent it?") and which it does not ("has the bank credited it?").
- Four states asserted; "empty cells" (p22): fixed. New subheading "One lifecycle in four states"; the paragraph gives the reason for four and points to the designs section; "empty cells" replaced (the table has "No status").
- "That is where the public record stops" interrupting the return thread (p25): fixed by a local move in spec and prose. p25 and its inference box now follow the four-state table, opening "The public record stops at these states"; the return, resend and never-returns paragraphs (p23, p24, p26) are now contiguous. Transitions of p23, p25, p26 and the section rationale updated.
- €1.17 illustration on an Adyen payout (content point): corrected. The page has no Adyen instant-payout price (Adyen publishes none), so the €1.17 figure is removed and the sentence says the cost of Mila's instant payout from Adyen needs a quote.
- Third-party paragraph after the design table (p36, spec): fixed by a local move. It now sits after the third design and before the summary paragraph and table, opening "The same three designs apply when the payee is not a merchant on the provider"; p35 opens "Whoever the payee". Spec order, transitions and rationale updated. Content unchanged.
- Take-away callback said the opening payout "was returned" (content point): fixed against the ledger's chapter 14 line (Mila's payout sent 11 March, arrived 25 March). The callback now says the opening owner is not Ines and states the return conditionally; spec callback updated.

## flow_is_followable (minor)

- Why the 412 payouts were returned (scene ¶1): fixed with a clause ("receiving banks that could not credit the new details"), a restatement of what a return is, not a new cause.
- "both contracts" (p16): fixed ("batch and instant, which the table compares").
- Sourcing parenthesis and unglossed terms (p18): fixed. Parenthesis moved to the end; payable batch, sales-day model (Adyen's default) and managed schedule glossed; "a batch in the provider's books, not the rail's" separates the two meanings of batch.
- "Booked is not departure either" (p21): fixed ("Nor does `booked` mean the money has left Adyen"), and the review status `pending` is named and distinguished from Stripe's `pending`.
- Package opt-out "matters for bulk payouts" (p28): fixed; says a bulk sender can go without the check and points to what the providers offer.
- Same-day arrival vs `booked` (p39): fixed ("the bank credits Ines's account that same day, the best case"), following the sentence that gives the five-business-day bound.
- K2 sentence placed in the Stripe paragraph (p42): fixed ("On both providers, webhooks only move the record's state").

## custom AC-3

- Adyen 100,000.00 EUR instant cap: fixed ("a limit likely to change").
- Stripe SWIFT and FX fees: fixed ("as of November 2026 and likely to change").
- Stripe Instant Payouts limits and 1% fee: fixed ("as of November 2026, and likely to change"; "a price likely to change").

## Content corrections (author's change 4)

- Removed the €1.17 *(illustration)* that applied Stripe's 1% Connect fee to Studio Noord's Adyen payout.
- Take-away callback no longer asserts the opening payout was returned.
