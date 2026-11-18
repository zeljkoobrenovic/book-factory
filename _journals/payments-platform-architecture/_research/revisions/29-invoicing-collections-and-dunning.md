# Revision log — 29-invoicing-collections-and-dunning (draft check round 1, ESCALATE)

Revised 2026-11-17. One line per failed result. No fact, number, date, quotation, hedge, source, figure, caption or `[[link]]` changed, except the content corrections listed below.

## Major

- evidence_is_explained, p19 (fixed schedules): fixed in draft. Added the spec's `shows`: a fixed schedule is simple but blind to why the card was declined and to when the cardholder is paid.
- transition, scene opener (p05): fixed in draft. Opens on the carry-over ("Larkfield's collection process knew payments, not debts, and on 1 October 2026 that showed").
- transition, the-invoice opener (p08): fixed in draft. Opens on Femke's first question, parallel to the next two sections.
- transition, p13 (e-invoicing): fixed in draft. Opening sentence carries over the tax-driven freeze ("Tax rules, which already freeze the invoice, are now reaching the document itself").
- transition, designs opener (p27): fixed in draft. One sentence carries over the branches and states the cause (every branch needs a system that knows the invoice, so who runs collection follows from where it lives).
- transition, in-practice opener (p34): house format; transition strengthened. "Both problems" replaced by "uses two of the three designs, one for each kind of debt it collects".
- flow, p05 Renewal Wave named but not explained: fixed in draft, one clause from the ledger ("Larkfield's name for its monthly peak").
- flow, p09 "seven" and the terminal-state digression: fixed in draft. Counts now agree with the table ("the five states and seven of the transitions"); the terminal-state sentence moved, unchanged, to the end of the paragraph in parentheses.
- flow, p13 tangent (both readers): fixed in draft by the new opening sentence (see transition above). Kept in place (decision log: one paragraph at the end of the invoice section).
- flow, p16 interrupts the attempts argument (spec fault; both readers): spec repair. p16 moved, unchanged except its opening sentence, from attempts-against-a-debt to designs, directly before p31 (rule 7 of the 17 November changes). Not merged into p31: p31's prose does not repeat p16's figures, so a merge would only lengthen one paragraph. Transitions rewritten on both sides (p16 contrast with the designs' rule; p31 additional_support, "as thin and dated"). The move also fixes the known_before_new finding on Smart Retries, the account updater and Auto Rescue, now all explained before p16. AC-3 still met: the no-independent-measurement sentence is kept verbatim.
- flow, p22/p23 rescue window and Auto Rescue before p28 (spec fault): fixed in draft with a gloss at first use in p22 (Auto Rescue, "Adyen's feature that retries refused payments for the merchant"; rescue window, "the period during which Adyen keeps trying"). p28's duplicate gloss of the rescue window removed.
- flow, p30 refers to an instruction quoted only later: fixed in draft. p28 now states, as its spec evidence lists, that Adyen tells the merchant to cancel the rescue when the shopper provides a new payment method or cancels; p30 says "above". "exactly those cases" became "those cases", since the instruction does not name paying another way.
- flow, p32 table introduces facts the body never stated (both readers): content correction. Both facts are verified (verification rows 82 and 83). Stated in the body first: the "account closure or fraud" case and "no code list" in p28; the 42-day SEPA rescue window for the account in p22.
- flow, cash-application section placement (both readers): fixed in draft. p26 ends with the spec's reason: only a system that holds the invoices can apply such money, which is why the next section asks who holds them.
- flow, Keel and K5 with two contents (both readers): content correction. Keel introduced in one sentence (2027 program led by Femke, decisions K1 to K8, from the ledger). K5 stated once in the ledger's words (renewals spread and rate-limited by Larkfield, paced over 18 hours, retried on a schedule tied to decline codes); that the providers' scheduled retries are off for renewals is now said in plain words, as a consequence; p38 says "Because K5 paces the renewal job".
- flow, p36 "first row" before its table (both readers): fixed in draft ("the first row of the table below").
- flow, p39 Double Charge side point (both readers): fixed in draft. The incident sentence moved to the end of the paragraph and names it as Larkfield's own incident with a different route, so it no longer reads as the pattern the callout defines.
- known_before_new, p16 (Smart Retries, account updater): fixed by the move of p16 (see above).
- known_before_new, p22 rescue window: fixed in draft (gloss at first use).
- known_before_new, p28 shopper-not-present: fixed in draft, one sentence gloss.

## Minor

- flow, p05 night/evening order: fixed ("In those hours … That evening").
- flow, p03 Mila's class pass without context: fixed, one clause ("the one-off payment earlier parts of this book followed").
- flow, p11 Studio Noord's two roles: fixed, one clause ("Studio Noord here as Larkfield's customer for its own studio plan").
- flow, p22 unclear subject "It gives two reasons": fixed ("Adyen gives two reasons for the cap").
- flow, p20 15 against 20: fixed ("gives the limit as 15, not the 20 of Visa's current rules").
- flow, p36 day 0: fixed ("1 April 2027 (day 0)").
- flow, p35 "and now": fixed (open, paid and void "as that chapter gave them", and now uncollectible).
- flow, p37 the same number twice: fixed ("The other 25,620, still unpaid").
- known_before_new, p28 pspReference: fixed ("Adyen's identifier for a payment").
- Judge's note on the conclusion's negative so-what (passed): not changed; the check passed.

## Spec changes

- p16 moved to designs before p31, new controlling idea opening and transition_in; p31 transition_in rewritten; attempts section `how` and flow rationale, designs flow rationale updated; p22, p26, p28, p34, p39 controlling ideas extended to match the prose; the open question on flow notes records the move; `max_words` 6500 -> 6825 (5%); changelog entry dated 2026-11-17.

## Checks

- `validate_spec.py payments-platform-architecture 29-invoicing-collections-and-dunning`: ok.
- `check_draft.py structure`: pass, 6,794 words (limit 6,825).
- `timetoread` 28 -> 30 (6,794 / 230).
