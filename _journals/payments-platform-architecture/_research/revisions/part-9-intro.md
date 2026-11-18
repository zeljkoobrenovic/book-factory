# Revision of part-9-intro (round-1 report, 2026-11-17)

- paragraph_traces_to_thesis p10 (dispute paragraph names no provider difference): added, from chapter 45: "Who paid had been decided when the payment was made: on Adyen by the chargeback logic set on the payment, on Stripe by the charge type." Spec p10 aligned.
- flow KEY POINTS bullet 2 ("not the payout"): the body now backs the claim (p03: "a card payment is final only when the dispute window closes", from chapter 42's take-away). The bullet's wording is not changed: callouts may be touched only to gloss a term (author's change 3). For the editor: recommend "so a payment's record stays open until the dispute window closes, not just until the payout."
- flow p02 (Part VIII rule unexplained): now "...must be correct before it is available: an answer may be late, but the record may not be wrong." (chapter 41's take-away wording). Spec p02 aligned.
- flow p04 (Studio Noord as an aside): Studio Noord named in p02 where the four payments are first mentioned ("four payments at Studio Noord, a yoga studio that uses Larkfield"); p04 now says plainly that each journey is told on Adyen, Studio Noord's provider.
- flow p05 position (spec): p05 moved from the introduction to the end of "Chapters in this part", in spec and prose; transitions and flow rationale updated (author's change 7: a single paragraph unit moved; its content unchanged).
- flow p05 ("where it stops"): now "each says where that documentation stops".
- flow p06 ("five weeks before the first journey's payment"): now "five weeks before Mila's class pass of 9 March 2027".
- flow p07 (three-clause sentence; €117.47): split into sentences ("Of its twelve steps, the first eleven each end in a promise. The 'Payment successful' ... reports the promise of the fifth step. Only the twelfth ... establishes that the studio's share arrived: €117.47, the €120 less Larkfield's €2.53.").
- flow p08 ("removes her presence and the approval"; "second branch"): now "Mila is not there to pay and the first attempt is declined"; "a second branch follows a renewal that is never collected".
- flow p10 ("counted it either way"; "decided at the sale"): now "the card network's monitoring counted the dispute whatever its outcome" and the provider clause above.
- flow p11 (rounding rule unaccounted): "the third and fourth journeys write two of them (refunds after payout, chargeback fees) as ledger entries; the rounding rule belongs to [[payment-ledgers]]".
- flow Sources line: now "Every fact on this page is repeated from the chapter that states it and cites its source."
- known_before_new p05 (spec; "the last journey's €15 fee"): resolved by the move; now "the dispute journey's €15 fee", after the dispute journey is introduced.
- known_before_new p06 (first journey's date): as above.
- conclusion so_what missing: added "When a payment of your own goes wrong, look first for the hand-off where a promise was taken for a fact, and for the later record that would have shown the difference."
- AC-1 (nothing fails in Journey 1): p07 now says "Nothing fails: it is the baseline."; closing line "Begin with [[journey-card-payment]], the class pass on which nothing fails."
- Trims to fit: the illustrative €0.61 provider cost dropped from the platform-payment paragraph (stated in that journey), the sentence "The failures to look for are between rows, not inside one." dropped, the closing sentence of the dispute paragraph shortened (the €412,000 is set against the journeys in Where to Begin).
- Length: 1,257 words; max_words raised 1,200 -> 1,260 (5%). timetoread 5 min unchanged.
