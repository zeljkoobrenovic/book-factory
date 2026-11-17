# Revision after draft check, round 1 — 35-splits-balances-and-platform-payouts

Date: 2026-11-24. Report judged: round 1, 21 failed results (15 major, 6 minor) and 1 waived. One line per failed result. Words: 6,022 before, 6,373 after (within `max_words` 6,500; unchanged). `timetoread` 26 to 28. Apart from the corrections listed under "Content", no fact, number, date, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## evidence_is_explained

- Recovery table, "three ways, two limits" (major): fixed. The limits are stated by kind (a condition on the balance on Stripe, time on Adyen), and the unit ends, just before the table, with what it shows: the same three ways to recover under different names, and a fourth row for what happens when they fail, the platform paying after 180 days on Stripe and after more than 30 days on Adyen. The 180-day platform reserve is now explained in the same unit. Spec p23 controlling idea and `shows` aligned.

## transition_expresses_declared_relationship

- Payouts section opening (major): fixed. "A reversal finds a seller's balance empty because a payout schedule emptied it, which is Femke's third question: when does the money leave the provider?" Spec section transition aligned.
- "the figure Femke asks for" (major): fixed. "That leaves the open half of every payment summed for one studio, Larkfield's per-studio exposure figure" (ledger: Larkfield's per-studio exposure figure). Spec p39 aligned.

## flow_is_followable (major)

- Payouts section after reversals (spec): section not moved (whole sections never move). Instead the payout terms the recovery table uses (net settlement, top-up, the platform reserve) are defined in the reversals unit before the table (spec and prose), and the payouts section opens from the reversals. Recommendation for the editor: keep the order; if a move is ever wanted, payouts would precede reversals, following the payment's own timeline.
- Intro ¶2 circular sentence: fixed; "A refund or chargeback that arrives after the payout is taken from the balance the payment was booked to. If that balance is the platform's, the platform pays and then recovers the seller's share itself." Spec p02 aligned.
- "Three ways … two limits" count: fixed (see evidence_is_explained); the Managed Risk aside now sits before the sentence that introduces the table.
- Cross-border paragraph a digression: fixed; tied to the schedule ("a seller paid across a border waits longer and less predictably, while the dispute window runs the same"); "the chapter stops here" removed. Spec p27 aligned.
- "the advance this implies": fixed; "Adyen paying a seller before the card networks have paid Adyen" (ruling 18).
- 25 March vs "paid within days": fixed against the ledger: the payout is sent on 11 March, two days after the sale; the ledger keeps it in transit for Larkfield's ten-business-day return window *(assumption)* and marks it arrived on 25 March with no return. Spec p36 aligned.
- Stripe refund paragraph stacks caveats: fixed; it now leads with the practical point (handle two outcomes, book the same recovery entry), then states the documented gap. Spec p38 aligned.
- "the figure Femke asks for": fixed (see transitions).
- Failure patterns not mapped: fixed; the section opens "The €317,200 was the Orphaned Refund … Four related failures remain"; the first failure is named the Phantom Payment; the last says an unaged recovery account is one way into the Black-Box Balance. Spec p40, p43 aligned.

## flow_is_followable (minor)

- "a portion" vs the full transfer: fixed; "The table's 'portion' is the net effect". Spec p14 aligned.
- "a third decision": fixed; "Whether to reverse and when are two decisions; the platform's fee is a third". Spec p20 aligned.
- Years jump and the rest of the €412,000: fixed; "A year earlier, at the end of 2025"; the rest is named from the ledger (chargeback fees and a currency-conversion rounding rule). Spec p05 aligned.
- In Practice heading "Three Ways" (spec): fixed; heading now "Mila's €120 Split Three Ways, Then €84 Back", so the three are the parties of the split. Spec heading aligned.

## known_before_new

- Top-up and net settlement in the recovery table (major): fixed; both defined in p23 before the table; p26 now refers to top-ups as defined and gives only their scope. Spec p23, p26 aligned.
- Platform reserve and the 180-day transfer (major): fixed; the connected reserve is identified as the platform reserve from which Stripe covers a balance still negative after 180 days.
- Keel and K3 (major): fixed; introduced in the scene ("Keel, Larkfield's 2027 program to put its payments on an even keel, whose decision K3 requires a ledger entry for every movement, refunds after payout included"); p34 says "Under K3". Spec p07, p34 aligned.
- "chargeback reversal", "second chargeback" (minor): fixed; each glossed in a clause. Spec p42 aligned.
- Interchange, scheme fee, blended pricing and Interchange++ in the Adyen table (minor): fixed; the last row's cell says "(both explained below)"; interchange and scheme fee are glossed in the table already.

## flow_is_followable (waived)

- Where They Differ position: house format; transition strengthened ("The three designs exist on both providers; what differs is how each is built and what it leaves the platform to record").

## Content

- 25 March arrival explained by Larkfield's ten-business-day window (ledger, chapter 14 line).
- The remainder of the €412,000 named from the ledger (incident table).
- Keel and K3 introduced from the ledger's K3 wording.

## Not changed

- No failure judged wrong.
