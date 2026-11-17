# 01-journey-of-a-payment — revision after draft check round 1 (2026-11-24)

One line per failed result. Words: 6,203 before, 6,489 after (`max_words` 6,500, unchanged). `timetoread` 27 → 28 min. Callouts, figures, captions, links and Sources untouched.

- one_controlling_idea_per_paragraph, p26 (spec): repaired. Split in spec and prose into p26 (the platform layer) and new p41 (the acquirer-of-record question, the section's conclusion); the new paragraph opens "Positions, connections and layers all reduce to one question". No sentence lost; flow rationale of the section updated.
- transition, opening of "The Timeline": fixed. Opens "Those parties, each holding and risking something different, act in a fixed order, and three different things pass between them".
- flow_is_followable, Figure 1's four notes against Femke's four questions: fixed in the paragraph (figure and caption may not change). A closing sentence says the figure shows the point by step (approval, claim, settlement, payout) and that the fourth question stays open after all of them.
- flow_is_followable, "The rest of the table": fixed. "The table below sets out, party by party, who holds the money and who carries which risk. Beyond that documented boundary it is a generalization".
- known_before_new (AC-2), settlement before the timeline: fixed. Settlement and payout glossed in one sentence before the names table, from the chapter's own definitions.
- known_before_new (AC-2), Payment Facilitator inside the Visa quotation: fixed. Glossed after the quotation, with a pointer to the table that defines it.
- known_before_new, rulebook "Interchange": fixed. The gloss moved up to first use (same sentence as the facilitator gloss) and removed from the clearing paragraph, where it was a repeat.
- known_before_new, "full-stack": fixed. Glossed in the sentence before the table as Adyen's undefined term, read as volume Adyen also acquires by the author's inference (the reading the page already gives two paragraphs later).
- flow_is_followable, "The public record stops in three places": fixed. The three are marked First, Second, Third; the closing sentence is marked as their sum ("In sum"). The repeated "neither lists networks and countries" became "neither names the networks and countries"; no fact, date or hedge changed.
- flow_is_followable, "Three numbers in the table": fixed. Each number now says where it sits (the cast table above, the settlement row, the last row).
- flow_is_followable, K2 as "the rule behind that answer": fixed. K2 is given as the consequence for the payment record, with one sentence from the ledger's wording of K2 (a status is confirmed against the provider's record).
- flow_is_followable, failure table against the six steps: fixed. The spec's capture row restored ("The approval expires before the claim is made | The issuer | No named incident"), "Settlement and after" renamed "Clearing and settlement" as in the spec, and the lead sentence now says the table gives an incident where a step has one and that its last row is not a step. NOTE for the editor: "The issuer" as who knows first in the capture row is my generalization; the spec names the row but not that cell.
- flow_is_followable (minor), €117.47 + €2.53 = €120 although the acquirer receives less: fixed. A clause from the ledger: the provider's processing cost, interchange included, comes out of Larkfield's fee.
- flow_is_followable (minor), Stripe quotation does not show "settlement" used for a payout: fixed. The sentence now gives Stripe's own term "settlement timing" (verification row 62) for the delay before a payout.
- flow_is_followable (minor), 10 calendar days: fixed. "expires if the claim comes too late … 10 calendar days from a valid authorization" (verification row 19).
- flow_is_followable (minor), "the provider owns only one, the payout": fixed. "in its own right owns only one, the payout; where it also captures and presents the record, it does so in the acquirer's role".

Judged wrong: none. Left for the editor: none.
