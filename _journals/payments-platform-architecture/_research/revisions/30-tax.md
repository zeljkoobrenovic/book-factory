# Revision log — 30-tax (draft check round 1, ESCALATE)

Revised 2026-11-24. One line per failed result. No fact, number, date, quotation, hedge, source, figure, caption or `[[link]]` changed.

## Major

- evidence_is_explained, inputs table (p08): fixed in draft. One sentence before the table reads it: a billing or checkout flow holds four of the five inputs; the fifth, the seller's registrations, exists only if the seller enters it, and its absence produces a calculated zero.
- evidence_is_explained, When It Goes Wrong quotation (p26): fixed in draft. Added what it shows (tax charged but never recorded as a transaction is missing from reports and filing); p12 now also says so where the distinction is introduced.
- transition, Introduction ¶2 (p02): fixed in draft. Opens by picking up the zeros ("The zeros look alike because the provider that calculated them does only part of the job").
- transition, what-tax-asks opener (p07): fixed in draft. Picks up Priya's question ("Whether the tax is Stripe's job depends on what it asks of a seller").
- transition, stripe-tax opener: fixed with the reorder below; the opening sentence announces the four steps in order and the platform question before them.
- transition, p20 recommendation: fixed in draft ("Because only the system that calculates can explain a zero, the advice differs by provider").
- flow, "Next comes" and steps out of order (both readers): spec repair, local order inside the section. Stripe-tax is now in step order: liable party (p17), monitor (p15, step 1), register (p16, step 2), calculate (p12, step 3, with Figure 1), zero (p13, Figure 2), tax numbers (p14), file (new p33, step 4). p16 split at the filing sentence (registering and filing were two controlling ideas once in step order). Openers rewritten to name each step; section flow rationale rewritten.
- flow, calculation/transaction distinction has no visible purpose: fixed in draft (p12 says a calculation never recorded as a transaction is missing from reports and filing; p26 ties back).
- flow, "In the payment record store …" garbled (both readers): fixed in draft ("Larkfield's payment record store names the studio as the liable party on every payment").
- flow, €19.8 million (both readers): fixed in draft from the ledger ("payments revenue, the fees Larkfield charges studios on each payment").
- flow, dense Adyen paragraph (both readers): spec repair, split. p18 keeps the search and the four findings; new p34 holds the absence-of-evidence sentence and Orb, opened by "None of the four is a calculator" and "Nor does Adyen's newest acquisition fill it". House section not moved.
- flow, liable-party paragraph far from deemed supplier (spec fault, both readers): spec repair. p17 is now the first paragraph of the Stripe section, directly after the deemed-supplier paragraph, and its opener says why it comes first. Nothing lost.
- known_before_new, `on_behalf_of` (both readers): fixed in draft, one clause ("the field that names the connected account a charge is made for").
- known_before_new, KEY POINTS "thresholds": fixed in the callout (rule 3), gloss from the body ("the sales volumes that oblige a seller to register"). Three bullets and labels unchanged.
- intro_predicts_content, regulatory evidence not signalled: fixed in draft; the roadmap names EU rules and a US Supreme Court decision.

## Minor

- flow, Figure 3 displaced (spec): not moved. Its caption ends on "one of the two fixes", which is p21/p22's point, so it belongs in the four-places section.
- flow, Figure 1 displaced (spec): resolved by the reorder; the figure now sits in the walk through the four steps, at the calculation step it marks as the provider's.
- flow, registration defined in passing in the scene with a promise: fixed (the promise "and the next section defines it" removed; the short definition stays).
- flow, "piece of state": fixed ("one record the seller keeps"; "the list of places where the seller is registered"; p24 "one entry in the registration record"; synthesis "data the seller holds").
- flow, "the fourth design": fixed ("the fourth design, the seller's own rate table").
- flow, OSS caveat after the arithmetic: fixed; the hedge sentence, unchanged, moved before the registration and the arithmetic.
- known_before_new, "reversal tax transaction": fixed, one clause in p26 ("a reversal, a tax transaction that undoes the original one").
- known_before_new, Managed Payments: fixed ("Stripe's merchant-of-record product, Managed Payments").
- known_before_new, Level 2/3 data: fixed ("extra details sent with a card payment").

## Spec changes

- stripe-tax paragraphs reordered (p17, p15, p16, p12, p13, p14, p33), transitions and controlling ideas updated, section flow rationale and transition `introduces` rewritten; p16 split into p16 and p33; p18 split into p18 and p34; p08 controlling idea notes the table reading; p19 carry-over updated; `max_words` 5000 -> 5250 (5%); changelog entry dated 2026-11-24.

## Checks

- `validate_spec.py payments-platform-architecture 30-tax`: ok.
- `check_draft.py structure`: pass, 5,249 words (limit 5,250).
- `timetoread` 22 -> 23 (5,249 / 230).
