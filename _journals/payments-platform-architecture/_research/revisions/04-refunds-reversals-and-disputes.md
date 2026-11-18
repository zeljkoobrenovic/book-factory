# 04-refunds-reversals-and-disputes — revision after draft check round 2 (2026-11-17)

One line per failed result. Words: 6,498 before, 6,791 after (`max_words` raised from 6,500 to 6,800, 4.6%). `timetoread` 28 → 30 min. Callouts, captions, links and Sources untouched; one figure moved (below), no figure or caption text changed.

- one_controlling_idea_per_paragraph, p15 (spec): repaired. Split in spec and prose into p15 (the merchant's fees are not returned) and new p15b (the customer waits days or weeks), each with its own evidence. No sentence lost; one connecting clause added.
- flow_is_followable, the two-stage table's dispute row and "the next section explains its dispute row" (draft): fixed. The lead-in now says the row runs ahead and names where each part is explained; the last cell says what "both directions" are, from facts already on the page (on Adyen a returned amount can be taken again; on Stripe a lost dispute can become won).
- flow_is_followable, seven Mastercard stage names (draft): fixed. "Chargeback reversed" and "second chargeback" are glossed right after the list, in the words of the provider comparison.
- flow_is_followable, "the merchant's answer is itself the pre-arbitration attempt" (draft): fixed. The sentence now says there is no separate Dispute Response in that flow and that the one answer is the last exchange before the network can be asked to rule.
- flow_is_followable, "That buys the count and the dispute fee, not the money" (draft): fixed. Says what the resolution fee buys (no dispute fee, no dispute added to the count the networks keep, described in the next paragraph) and what it does not.
- flow_is_followable, "my rule fails near a threshold" (draft): fixed. Near a threshold the first test (amount against fee) stops deciding and the third takes over.
- flow_is_followable, Figure 3 at p36 (spec): repaired. The figure line and caption moved to p19 (the issuer's 120-day clock, which the caption states), with a lead-in sentence; the figure evidence moved from p36 to p19 in the spec; renumbered with `renumber_figures.py` (paid-is-not-final is Figure 2, the dispute flow Figure 3); the "(Figure 3)" reference in p36 removed.
- flow_is_followable, "a second dispute can still arrive" (draft): fixed. "another dispute on the same payment … a new case, not the table's second chargeback, which is a later stage of this one".
- known_before_new, "auto-defended" (draft): fixed. Glossed after the quotation with a pointer to the next section.
- known_before_new, "Interchange Transactions" (draft): fixed. Glossed after the quotation as chapter 1 and the glossary do (the exchange of transaction records between members, not the fee).
- known_before_new, "Payment Facilitators" (draft): fixed. Glossed after the quotation from the glossary entry.
- Known point, "about 7 July" before the purchase date: fixed. The opening gives 9 March before 7 July ("120 days after the purchase").
- transition_expresses_declared_relationship (passed, three weakest named): strengthened. "Three Routes Back", "How a Card Dispute Runs" and "Two Design Decisions" each open by picking up the declared known information.
- Left for the editor: none.
